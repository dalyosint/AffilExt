"""Hybrid extraction pipeline over a Parquet file of arXiv papers.

Each input row needs the columns ``id``, ``text`` (full LaTeX source) and ``metadata``
(arXiv/Kaggle metadata JSON). For every paper:

1. Rule-based extraction of authors and affiliations from the LaTeX commands.
2. Gate 1: the extracted authors must match the arXiv author list (hybrid fuzzy F1).
3. Gate 2: the affiliations must resolve to ROR organizations.
4. If either gate fails, fall back to the LLM (Ollama) and try matching again.

Results are written as checkpoint batches so an interrupted run can be resumed,
then merged into a single output Parquet file.
"""
import argparse
import concurrent.futures
import json
import logging
import statistics
import subprocess
from datetime import datetime, timezone
import time
from pathlib import Path

import jsonpickle
import polars as pl
import pyarrow.parquet as pq
import ai_fallback
import approach1_spacy_ner
import author_matching
import extract_author_aff
import extract_cmds
import llm_extraction
import match_data
from definition.data.ArxivMetadata import ArxivMetadata
from definition.data.Author import Author

logger = logging.getLogger("ParquetPipeline")

# Gate 1: minimum author-list F1 (0-1); the per-name similarity threshold lives in author_matching
AUTHOR_F1_THRESHOLD = 0.70
SLOW_PAPER_SECONDS = 15.0

# Statuses that trigger the LLM fallback
_AI_FALLBACK_STATUSES = {"extraction_failed", "low_author_similarity", "matching_failed"}

# Output columns are always strings (JSON). An explicit dtype keeps all batch files on the
# same schema even when a batch contains only None values, so they can be merged later.
_RESULT_DTYPE = pl.String

_LOG_FORMAT = "%(asctime)s - [%(processName)s] - %(levelname)s - %(message)s"


def configure_logging(level: int | str) -> None:
    # force=True so worker processes (spawned on macOS/Windows) are configured too
    logging.basicConfig(level=level, format=_LOG_FORMAT, force=True)


def parse_metadata(json_str: str, arxiv_id: str) -> ArxivMetadata | None:
    """Converts the raw arXiv metadata JSON string into an ArxivMetadata object."""
    try:
        data = json.loads(json_str)

        if "authors_parsed" in data:
            # authors_parsed entries are [last_name, first_name, suffix]
            authors_list = [Author(f"{auth[1]} {auth[0]}".strip(), []) for auth in data["authors_parsed"]]
        else:
            authors_list = [Author("Unknown", [])]

        return ArxivMetadata(
            arxiv_id=arxiv_id,
            version="v1",
            title=data.get("title", ""),
            comment=data.get("comments", ""),
            journal_ref=data.get("journal-ref", ""),
            doi=data.get("doi", ""),
            categories=data.get("categories", "").split(),
            last_updated=data.get("updated", ""),
            published_on=data.get("created", ""),
            authors=authors_list
        )
    except Exception as e:
        logger.warning("Metadata parsing issue for %s: %s", arxiv_id, e)
        return None


# Loaded once per worker process by init_worker()
global_ror_orgs = None
global_ror_orgs_dict = None


def init_worker(log_level: int | str = logging.INFO, spacy_skip_score: float | None = None) -> None:
    """Runs once per worker process: configures logging, matching settings and loads the ROR dataset."""
    global global_ror_orgs, global_ror_orgs_dict
    configure_logging(log_level)
    approach1_spacy_ner.SPACY_SKIP_SCORE = spacy_skip_score
    ror_dataset = match_data._get_ror_dataset()
    global_ror_orgs = match_data._process_ror_orgs(ror_dataset)
    global_ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)


def process_single_paper(row: dict) -> tuple:
    """Processes one paper row. Runs inside a worker process."""
    paper_start_time = time.perf_counter()
    paper_id = row.get("id", "Unknown")

    logger.debug("[%s] Starting processing...", paper_id)

    extracted_result = None
    matched_result = None
    ai_result = None
    status = "extraction_failed"
    ai_used = False

    try:
        full_latex_text = row["text"]
        meta_obj = parse_metadata(row["metadata"], paper_id)
        ext_cmds = extract_cmds.extract_cmds_from_string(full_latex_text)

        # --- 1. Rule-based extraction ---
        ext_info_trad = extract_author_aff.extract_affiliations_from_obj(ext_cmds, meta_obj)

        if ext_info_trad and ext_info_trad.extractions:
            # Gate 1: author list similarity
            best_ext = match_data._get_best_extraction(ext_info_trad.extractions)
            f1_score = author_matching.author_f1([a.name for a in best_ext.authors],
                                                 [a.name for a in meta_obj.authors])

            if f1_score >= AUTHOR_F1_THRESHOLD:
                logger.debug("[%s] Rule-based extraction SUCCESS (F1: %.2f).", paper_id, f1_score)
                extracted_result = jsonpickle.encode(ext_info_trad)

                # Gate 2: ROR match resolution
                final_data = match_data.match_and_resolve_single_paper(
                    meta_obj, ext_info_trad, global_ror_orgs, global_ror_orgs_dict
                )

                if final_data:
                    matched_result = jsonpickle.encode(final_data)
                    status = "success"
                    logger.debug("[%s] Rule-based match SUCCESS.", paper_id)
                else:
                    status = "matching_failed"
                    logger.debug("[%s] Rule-based match FAILED (unmatched institutions).", paper_id)
            else:
                status = "low_author_similarity"
                logger.debug("[%s] Rule-based extraction FAILED (author F1 %.2f < %.2f).",
                             paper_id, f1_score, AUTHOR_F1_THRESHOLD)
        else:
            status = "extraction_failed"
            logger.debug("[%s] Rule-based extraction FAILED (empty extraction).", paper_id)

        # --- 2. LLM fallback ---
        if status in _AI_FALLBACK_STATUSES:
            ai_used = True
            logger.info("[%s] Rule-based failed (%s). Falling back to AI extraction...", paper_id, status)
            ext_info_ai = ai_fallback.extract_with_ollama(full_latex_text, meta_obj)

            if ext_info_ai:
                ai_result = jsonpickle.encode(ext_info_ai)
                extracted_result = ai_result  # the AI extraction replaces the rule-based one
                logger.debug("[%s] AI extraction SUCCESS.", paper_id)

                final_data = match_data.match_and_resolve_single_paper(
                    meta_obj, ext_info_ai, global_ror_orgs, global_ror_orgs_dict
                )

                if final_data:
                    matched_result = jsonpickle.encode(final_data)
                    status = "success"
                    logger.debug("[%s] AI match SUCCESS.", paper_id)
                else:
                    status = "matching_failed"
                    logger.debug("[%s] AI match FAILED.", paper_id)
            else:
                status = "extraction_failed"
                logger.debug("[%s] AI extraction FAILED/EMPTY.", paper_id)

    except Exception as e:
        logger.error("[%s] Failed processing paper: %s", paper_id, e, exc_info=True)
        status = "pipeline_error"

    duration = time.perf_counter() - paper_start_time
    if duration > SLOW_PAPER_SECONDS:
        logger.warning("[%s] SLOW PROCESSING: took %.2f seconds", paper_id, duration)

    return extracted_result, matched_result, ai_result, status, duration, ai_used


def _load_processed_ids(output_dir: Path) -> set:
    """Collects the IDs of all papers already written to checkpoint batches (for resuming)."""
    processed_ids = set()
    existing_files = list(output_dir.glob("*.parquet"))
    if not existing_files:
        return processed_ids

    logger.info("Found %d existing batch files. Loading to resume...", len(existing_files))
    for file in existing_files:
        try:
            # only read the 'id' column to save RAM
            processed_ids.update(pl.read_parquet(file, columns=["id"])["id"].to_list())
        except Exception as e:
            logger.warning("Could not read %s, it might be corrupted from a previous crash: %s", file, e)

    logger.info("Resuming pipeline. Found %d already completed papers.", len(processed_ids))
    return processed_ids


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Hybrid (rule-based + LLM) author-affiliation extraction over a Parquet file.")
    parser.add_argument("-i", "--input", default="math_subset.parquet",
                        help="Input Parquet file with columns id, text, metadata. Default: %(default)s")
    parser.add_argument("-o", "--output", default="math_sample_processed_final.parquet",
                        help="Final merged output Parquet file. Default: %(default)s")
    parser.add_argument("--batch-dir", default="processed_batches",
                        help="Directory for checkpoint batches (used for resuming). Default: %(default)s")
    parser.add_argument("-w", "--workers", type=int, default=4,
                        help="Number of worker processes. Default: %(default)s")
    parser.add_argument("-b", "--batch-size", type=int, default=1000,
                        help="Rows per checkpoint batch. Default: %(default)s")
    parser.add_argument("--spacy-skip-score", type=float, default=None,
                        help="Skip spaCy NER when the raw affiliation already matches a ROR name with at least this "
                             "score (0-100). Faster, but can change results. Default: always use spaCy")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                        help="Default: %(default)s")
    return parser


def _git_commit() -> str | None:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                              cwd=Path(__file__).parent, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def _summarize_durations(durations: list[float]) -> dict:
    if not durations:
        return {}
    ordered = sorted(durations)
    return {
        "mean": round(statistics.fmean(ordered), 3),
        "median": round(statistics.median(ordered), 3),
        "p95": round(ordered[min(len(ordered) - 1, int(0.95 * len(ordered)))], 3),
        "max": round(ordered[-1], 3),
    }


def build_run_summary(args: argparse.Namespace, status_counts: dict, ai_pushed: int, ai_failed: int,
                      durations: list[float], skipped_already_processed: int, wall_seconds: float) -> dict:
    """Everything needed to report and reproduce a run: settings, code version, outcome counts and timings."""
    processed = sum(status_counts.values())
    return {
        "finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "git_commit": _git_commit(),
        "settings": {
            "input": str(args.input),
            "output": str(args.output),
            "workers": args.workers,
            "batch_size": args.batch_size,
            "author_f1_threshold": AUTHOR_F1_THRESHOLD,
            "name_similarity_threshold": author_matching.DEFAULT_NAME_THRESHOLD,
            "name_similarity_method": author_matching.DEFAULT_METHOD,
            "llm_model": llm_extraction.DEFAULT_MODEL,
            "llm_prompt": next(k for k, v in llm_extraction.PROMPTS.items() if v is llm_extraction.DEFAULT_PROMPT),
            "llm_window_chars": {"head": llm_extraction.DEFAULT_HEAD_CHARS, "tail": llm_extraction.DEFAULT_TAIL_CHARS},
            "spacy_model": approach1_spacy_ner.SPACY_MODEL,
            "spacy_skip_score": args.spacy_skip_score,
        },
        "papers": {
            "processed_this_run": processed,
            "skipped_already_processed": skipped_already_processed,
            "by_status": dict(sorted(status_counts.items())),
            "success_rate": round(status_counts.get("success", 0) / processed, 4) if processed else None,
        },
        "llm_fallback": {
            "pushed": ai_pushed,
            "failed": ai_failed,
            "rescued": ai_pushed - ai_failed,
            "share_of_papers": round(ai_pushed / processed, 4) if processed else None,
        },
        "seconds_per_paper": _summarize_durations(durations),
        "wall_time_seconds": round(wall_seconds, 1),
    }


def main():
    args = _build_arg_parser().parse_args()
    configure_logging(args.log_level)

    input_file = Path(args.input)
    output_file = Path(args.output)
    batch_dir = Path(args.batch_dir)
    summary_file = output_file.with_name(output_file.stem + ".run_summary.json")

    if not input_file.is_file():
        logger.error("Input file not found: %s", input_file)
        return

    total_start_time = time.time()

    batch_dir.mkdir(parents=True, exist_ok=True)
    processed_ids = _load_processed_ids(batch_dir)

    status_counts: dict[str, int] = {}
    durations: list[float] = []
    ai_pushed_count = 0
    ai_failed_count = 0
    skipped_count = 0

    logger.info("Processing %s with %d workers (ROR dataset is loaded once per worker)...",
                input_file, args.workers)
    processing_start_time = time.time()

    parquet_file = pq.ParquetFile(input_file)

    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers, initializer=init_worker,
                                                initargs=(args.log_level, args.spacy_skip_score)) as executor:

        for batch_counter, batch in enumerate(parquet_file.iter_batches(batch_size=args.batch_size), start=1):
            df_batch = pl.from_arrow(batch)

            # Skip papers that were already processed in a previous run
            if processed_ids:
                rows_before = df_batch.height
                df_batch = df_batch.filter(~pl.col("id").is_in(list(processed_ids)))
                skipped_count += rows_before - df_batch.height

            if df_batch.height == 0:
                logger.info("--- Skipping batch %d (all rows already processed) ---", batch_counter)
                continue

            logger.info("--- Starting batch %d (%d new rows) ---", batch_counter, df_batch.height)
            rows = df_batch.to_dicts()
            results = list(executor.map(process_single_paper, rows, chunksize=50))
            processed_ids.update(r["id"] for r in rows)

            extracted_results_column = []
            matched_results_column = []
            ai_results_column = []
            batch_status: dict[str, int] = {}
            batch_ai_pushed = 0
            batch_ai_failed = 0

            for ext_res, match_res, ai_res, status, duration, ai_used in results:
                extracted_results_column.append(ext_res)
                matched_results_column.append(match_res)
                ai_results_column.append(ai_res)
                durations.append(duration)
                batch_status[status] = batch_status.get(status, 0) + 1

                if ai_used:
                    batch_ai_pushed += 1
                    if status != "success":
                        batch_ai_failed += 1

            for status, count in batch_status.items():
                status_counts[status] = status_counts.get(status, 0) + count
            ai_pushed_count += batch_ai_pushed
            ai_failed_count += batch_ai_failed

            df_batch = df_batch.with_columns([
                pl.Series("extracted_info", extracted_results_column, dtype=_RESULT_DTYPE),
                pl.Series("matched_info", matched_results_column, dtype=_RESULT_DTYPE),
                pl.Series("ai_output", ai_results_column, dtype=_RESULT_DTYPE),
            ])

            # Checkpoint: timestamp in the name avoids overwriting batches from earlier runs
            batch_filename = batch_dir / f"batch_{batch_counter}_{int(time.time())}.parquet"
            df_batch.write_parquet(batch_filename)
            logger.info("Saved checkpoint: %s", batch_filename)

            batch_success = batch_status.get("success", 0)
            batch_match_fail = batch_status.get("matching_failed", 0)
            logger.info("Finished batch %d. Stats: %d Success | %d Match Fail | %d Ext Fail | "
                        "AI Pushed: %d | AI Failed: %d",
                        batch_counter, batch_success, batch_match_fail,
                        len(results) - batch_success - batch_match_fail, batch_ai_pushed, batch_ai_failed)

    logger.info("Processing time: %.2f minutes", (time.time() - processing_start_time) / 60)

    # Merge all checkpoint batches into one file; sink_parquet streams without loading everything into RAM
    logger.info("Compiling all batch files into final output...")
    try:
        pl.scan_parquet(batch_dir / "*.parquet").sink_parquet(output_file)
        logger.info("Final compiled output saved to %s", output_file)
    except Exception as e:
        logger.error("Failed to compile final file: %s. The batches are still safe in '%s'.", e, batch_dir)

    summary = build_run_summary(args, status_counts, ai_pushed_count, ai_failed_count, durations,
                                skipped_count, time.time() - total_start_time)
    summary_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    logger.info("=== PIPELINE COMPLETION STATS (this run) ===")
    logger.info("Processed papers: %d (by status: %s)", summary["papers"]["processed_this_run"],
                summary["papers"]["by_status"])
    logger.info("Pushed to AI: %d | failed by AI: %d", ai_pushed_count, ai_failed_count)
    logger.info("Total pipeline time: %.2f seconds", summary["wall_time_seconds"])
    logger.info("Run summary written to %s", summary_file)
    logger.info("=================================")


if __name__ == "__main__":
    main()
