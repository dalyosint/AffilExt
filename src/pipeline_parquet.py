import json
import logging
from pathlib import Path
# Used to convert Python objects → string
import jsonpickle
import ai_fallback
import os
import glob
# new approach
import polars as pl
import pyarrow.parquet as pq
import pyarrow as pa

import time
import matplotlib.pyplot as plt
# Multiprocessing
import concurrent.futures
# Used to pass extra parameters to multiprocessing
from functools import partial

import extract_cmds
import extract_author_aff
import match_data
import ror_dl
import util
from definition.data.ArxivMetadata import ArxivMetadata
from definition.data.Author import Author

# you can see which cpu worker is working
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(processName)s] - %(levelname)s - %(message)s')
logger = logging.getLogger("ParquetPipeline")


# json_str: str , arxiv_id: str  = input
# ArxivMetadata: output
# reads arXiv metadata JSON and output it to ArxivMetadata
def parse_metadata(json_str: str, arxiv_id: str) -> ArxivMetadata:
    try:
        # converts str to dic
        data = json.loads(json_str)

        authors_list = []
        if 'authors_parsed' in data:
            for auth in data['authors_parsed']:
                name = f"{auth[1]} {auth[0]}".strip()
                authors_list.append(Author(name, []))
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
        logger.warning(f"Metadata parsing issue for {arxiv_id}: {e}")
        return None


global_ror_orgs = None
global_ror_orgs_dict = None


def init_worker():
    """This runs once per CPU core to load the dataset exactly once per process."""
    global global_ror_orgs, global_ror_orgs_dict
    import match_data
    ror_dataset = match_data._get_ror_dataset()
    global_ror_orgs = match_data._process_ror_orgs(ror_dataset)
    global_ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)


from rapidfuzz import fuzz


def calculate_hybrid_f1(extracted_authors, ground_truth_authors, threshold=70):
    if not extracted_authors and not ground_truth_authors:
        return 1.0
    if not extracted_authors:
        return 0.0

    matched_gt = set()
    true_positives = 0

    for ext_author in extracted_authors:
        e_name = ext_author.name.lower().strip()
        best_idx = -1
        best_score = 0

        for j, gt_author in enumerate(ground_truth_authors):
            if j in matched_gt:
                continue

            t_name = gt_author.name.lower().strip()

            r_score = fuzz.ratio(e_name, t_name)
            t_score = fuzz.token_set_ratio(e_name, t_name)
            score = max(r_score, t_score)

            if score > best_score:
                best_score = score
                best_idx = j

        if best_score >= threshold:
            matched_gt.add(best_idx)
            true_positives += 1

    precision = true_positives / len(extracted_authors)
    recall = true_positives / len(ground_truth_authors) if ground_truth_authors else 0.0

    if precision + recall > 0:
        return 2 * precision * recall / (precision + recall)
    return 0.0


def process_single_paper(row):
    """Handles the processing for a single row to be run in a separate process."""
    paper_start_time = time.perf_counter()
    paper_id = row.get('id', 'Unknown')

    logger.debug(f"[{paper_id}] Starting processing...")

    extracted_result = None
    matched_result = None
    ai_result = None
    status = "extraction_failed"
    ai_used = False

    try:
        full_latex_text = row['text']
        metadata_raw = row['metadata']

        logger.debug(f"[{paper_id}] Parsing metadata...")
        meta_obj = parse_metadata(metadata_raw, paper_id)
        ext_cmds = extract_cmds.extract_cmds_from_string(full_latex_text)

        # --- 1. Try Rule-Based (Traditional) Extraction First ---
        ext_info_trad = extract_author_aff.extract_affiliations_from_obj(ext_cmds, meta_obj)

        if ext_info_trad and ext_info_trad.extractions:
            # 1.1 Gate 1: Check Author F1 Score
            best_ext = match_data._get_best_extraction(ext_info_trad.extractions)
            f1_score = calculate_hybrid_f1(best_ext.authors, meta_obj.authors, threshold=70)

            if f1_score >= 0.70:
                logger.debug(f"[{paper_id}] Traditional extraction SUCCESS (F1: {f1_score:.2f}).")
                extracted_result = jsonpickle.encode(ext_info_trad)

                # 1.2 Gate 2: Check ROR Match Resolution
                final_data = match_data.match_and_resolve_single_paper(
                    meta_obj, ext_info_trad, global_ror_orgs, global_ror_orgs_dict
                )

                if final_data:
                    matched_result = jsonpickle.encode(final_data)
                    status = "success"
                    logger.debug(f"[{paper_id}] Traditional Match SUCCESS.")
                else:
                    status = "matching_failed"
                    logger.debug(f"[{paper_id}] Traditional Match FAILED (Unmatched institutions).")
            else:
                logger.debug(
                    f"[{paper_id}] Traditional extraction FAILED (Low author similarity: {f1_score:.2f} < 0.70).")
                status = "low_author_similarity"
        else:
            logger.debug(f"[{paper_id}] Traditional extraction FAILED (Empty extraction).")
            status = "extraction_failed"

        # --- 2. AI Fallback (Only if extraction or matching failed) ---
        if status in ["extraction_failed", "low_author_similarity", "matching_failed"]:
            ai_used = True
            logger.info(f"Rule-based failed for {paper_id}. Falling back to AI extraction...")
            ext_info_ai = ai_fallback.extract_with_ollama(full_latex_text, meta_obj)

            if ext_info_ai:
                ai_result = jsonpickle.encode(ext_info_ai)
                extracted_result = ai_result  # Overwrite with AI's extraction payload
                logger.debug(f"[{paper_id}] AI extraction SUCCESS.")

                # Attempt to match the AI extraction
                final_data = match_data.match_and_resolve_single_paper(
                    meta_obj, ext_info_ai, global_ror_orgs, global_ror_orgs_dict
                )

                if final_data:
                    matched_result = jsonpickle.encode(final_data)
                    status = "success"
                    logger.debug(f"[{paper_id}] AI Match SUCCESS.")
                else:
                    status = "matching_failed"
                    logger.debug(f"[{paper_id}] AI Match FAILED.")
            else:
                logger.debug(f"[{paper_id}] AI extraction FAILED/EMPTY.")
                status = "extraction_failed"

    except Exception as e:
        logger.error(f"[{paper_id}] Failed processing paper: {e}", exc_info=True)
        status = "pipeline_error"

    paper_end_time = time.perf_counter()
    duration = paper_end_time - paper_start_time

    if duration > 15.0:
        logger.warning(f"[{paper_id}] SLOW PROCESSING: Took {duration:.2f} seconds")

    return extracted_result, matched_result, ai_result, status, duration, ai_used


def main():
    INPUT_FILE = "subset.parquet"
    OUTPUT_DIR = "processed_batches"  # We use a directory now instead of a single file
    FINAL_OUTPUT_FILE = "math_sample_processed_final.parquet"

    # start time
    total_start_time = time.time()

    # --- 1. CRASH RESILIENCE: Create directory and load processed IDs ---
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    processed_ids = set()

    # Look for any existing batch files in the folder to resume from
    existing_files = glob.glob(os.path.join(OUTPUT_DIR, "*.parquet"))
    if existing_files:
        logger.info(f"Found {len(existing_files)} existing batch files. Loading to resume...")
        # We only read the 'id' column to save RAM!
        for file in existing_files:
            try:
                existing_df = pl.read_parquet(file, columns=["id"])
                processed_ids.update(existing_df["id"].to_list())
            except Exception as e:
                logger.warning(f"Could not read {file}, it might be corrupted from a previous crash: {e}")

        logger.info(f"Resuming pipeline. Found {len(processed_ids)} already completed papers.")
    # --------------------------------------------------------------------

    logger.info("Step 1: Loading ROR Dataset...")
    ror_dataset = match_data._get_ror_dataset()
    ror_orgs = match_data._process_ror_orgs(ror_dataset)
    ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)

    logger.info(f"Step 2: Preparing to stream Input Parquet {INPUT_FILE}...")

    worker_func = partial(process_single_paper, ror_orgs=ror_orgs, ror_orgs_dict=ror_orgs_dict)

    MAX_CORES = 2
    BATCH_SIZE = 50

    success_count = 0
    extraction_failed_count = 0
    matching_failed_count = 0
    ai_pushed_count = 0
    ai_failed_count = 0
    paper_processing_times = []

    logger.info("Step 3: Processing papers in streams with Multiprocessing...")
    processing_start_time = time.time()

    parquet_file = pq.ParquetFile(INPUT_FILE)
    batch_counter = 1

    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_CORES, initializer=init_worker) as executor:

        for batch in parquet_file.iter_batches(batch_size=BATCH_SIZE):
            df_batch = pl.from_arrow(batch)

            # --- 2. FILTER: Skip papers we already processed ---
            if processed_ids:
                df_batch = df_batch.filter(~pl.col("id").is_in(list(processed_ids)))

            if df_batch.height == 0:
                logger.info(f"--- Skipping Batch {batch_counter} (All rows already processed) ---")
                batch_counter += 1
                continue
            # ---------------------------------------------------

            logger.info(f"--- Starting Batch {batch_counter} ({df_batch.height} new rows) ---")
            rows = df_batch.to_dicts()

            # Execute the batch in parallel

            results = list(executor.map(process_single_paper, rows, chunksize=5))
            # Add these new IDs to our set so we don't process them again if we read the file twice
            for r in rows:
                processed_ids.add(r['id'])

            extracted_results_column = []
            matched_results_column = []
            ai_results_column = []

            batch_success = 0
            batch_match_fail = 0
            batch_ext_fail = 0
            batch_ai_pushed = 0
            batch_ai_failed = 0

            for ext_res, match_res, ai_res, status, duration, ai_used in results:
                extracted_results_column.append(ext_res)
                matched_results_column.append(match_res)
                ai_results_column.append(ai_res)
                paper_processing_times.append(duration)

                if status == "success":
                    batch_success += 1
                    success_count += 1
                elif status == "matching_failed":
                    batch_match_fail += 1
                    matching_failed_count += 1
                else:
                    batch_ext_fail += 1
                    extraction_failed_count += 1

                if ai_used:
                    batch_ai_pushed += 1
                    ai_pushed_count += 1
                    if status != "success":
                        batch_ai_failed += 1
                        ai_failed_count += 1

            df_batch = df_batch.with_columns([
                pl.Series("extracted_info", extracted_results_column),
                pl.Series("matched_info", matched_results_column),
                pl.Series("ai_output", ai_results_column)
            ])

            # --- 3. SAVE CHECKPOINT: Write just this batch to disk safely ---
            # We add a timestamp to the filename to avoid accidental overwrites
            batch_filename = os.path.join(OUTPUT_DIR, f"batch_{batch_counter}_{int(time.time())}.parquet")
            df_batch.write_parquet(batch_filename)
            logger.info(f"Saved checkpoint: {batch_filename}")
            # ----------------------------------------------------------------

            logger.info(f"Finished Batch {batch_counter}. "
                        f"Stats: {batch_success} Success | "
                        f"{batch_match_fail} Match Fail | "
                        f"{batch_ext_fail} Ext Fail | "
                        f"AI Pushed: {batch_ai_pushed} | "
                        f"AI Failed: {batch_ai_failed}")
            batch_counter += 1

    processing_end_time = time.time()
    logger.info(f"Processing time: {(processing_end_time - processing_start_time) / 60:.2f} minutes")

    # --- 4. OPTIONAL: Compile all the little batches into one final file at the end ---
    logger.info("Compiling all batch files into final output...")
    try:
        # sink_parquet streams the data chunk-by-chunk directly to the hard drive without filling RAM
        pl.scan_parquet(os.path.join(OUTPUT_DIR, "*.parquet")).sink_parquet(FINAL_OUTPUT_FILE)
        logger.info(f"Success! Final compiled output saved to {FINAL_OUTPUT_FILE}")

    except Exception as e:
        logger.error(f"Failed to compile final file: {e}. Don't worry, your data is safe in the '{OUTPUT_DIR}' folder.")
    # ----------------------------------------------------------------------------------

    total_time = time.time() - total_start_time
    logger.info("=== PIPELINE COMPLETION STATS ===")
    logger.info(f"Total processed papers: {success_count + matching_failed_count + extraction_failed_count}")
    logger.info(f"Total successful (Rule-based + AI): {success_count}")
    logger.info(f"Total pushed to AI: {ai_pushed_count}")
    logger.info(f"Total failed by AI: {ai_failed_count}")
    logger.info(f"Total pipeline time: {total_time:.2f} seconds")
    logger.info("=================================")


if __name__ == "__main__":
    main()