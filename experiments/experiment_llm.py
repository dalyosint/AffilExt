"""Benchmarks LLMs, prompts and temperatures for the LLM fallback against arXiv author metadata.

Results are appended to a JSONL file after every run so the experiment can be resumed after a crash.
"""
import asyncio
import json
import logging
import os
import sys
import time
from pathlib import Path

import polars as pl
from pydantic import ValidationError

# Experiments live outside src/, so make the pipeline modules importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

# existing pipeline tools
import extract_author_aff
import extract_cmds
import llm_extraction
from author_matching import author_match_scores
from pipeline_parquet import parse_metadata

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("ExperimentRunner")

#  Experiment Settings
MODELS = ["phi3:mini", "gemma2:2b", "qwen2.5:0.5b"]
PROMPTS = llm_extraction.PROMPTS
TEMPERATURES = [0.0, 0.3, 0.7]
TIMEOUT_SECONDS = 90

# Window sizes used for this experiment (the pipeline uses llm_extraction's larger defaults)
HEAD_CHARS = 5000
TAIL_CHARS = 1000


def extract_with_ollama_experiment(text_input, model_name, prompt_template, temp, timeout_seconds=TIMEOUT_SECONDS):
    """Returns (parsed_response | None, is_valid_json, error_message | None)."""
    prompt = llm_extraction.build_prompt(prompt_template, text_input)
    try:
        parsed_data = llm_extraction.query_ollama(prompt, model_name, temperature=temp,
                                                  timeout_seconds=timeout_seconds)
        return parsed_data, True, None
    except asyncio.TimeoutError:
        logger.error("TIMEOUT: %s did not respond within %ss. Skipping.", model_name, timeout_seconds)
        return None, False, f"Timeout: model failed to respond within {timeout_seconds} seconds."
    except ValidationError:
        return None, False, "JSON Validation Error"
    except Exception as e:
        return None, False, str(e)


def calculate_metrics_robust(extracted_authors: list[dict], ground_truth_authors: list[dict]) -> dict:
    """Precision, recall and F1 of author names (hybrid matching, threshold 70), rounded to 4 digits."""
    scores = author_match_scores([a.get("name", "") for a in extracted_authors],
                                 [a.get("name", "") for a in ground_truth_authors])
    return {key: round(value, 4) for key, value in scores.items()}


def evaluate_experiment(json_file):
    """Reads the final JSON results and calculates benchmark metrics using Polars."""
    logger.info("=" * 60)
    logger.info("FINAL BENCHMARKING RESULTS")
    logger.info("=" * 60)

    if not os.path.exists(json_file):
        logger.error("Could not find %s to evaluate.", json_file)
        return

    df = pl.read_json(json_file, schema_overrides={"error_msg": pl.String})

    summary_df = df.group_by("model", "prompt_type", "temperature").agg([
        pl.col("ai_author_f1").mean().round(4).alias("avg_f1"),
        pl.col("ai_author_precision").mean().round(4).alias("avg_precision"),
        pl.col("ai_author_recall").mean().round(4).alias("avg_recall"),
        (pl.col("valid_json").cast(pl.Int32).mean() * 100).round(2).alias("valid_json_percent"),
        pl.col("time_sec").mean().round(2).alias("avg_time_sec"),
    ]).sort(["model", "avg_f1"], descending=[False, True])  # best F1 per model at the top

    print(summary_df)

    summary_df.write_csv("prompt_benchmark_summary.csv")
    logger.info("Summary saved to prompt_benchmark_summary.csv")


def _config_key(paper_id, model, prompt_type, temperature) -> str:
    return f"{paper_id}_{model}_{prompt_type}_{temperature}"


def _load_processed_configs(jsonl_file: str) -> set:
    processed_configs = set()
    if not os.path.exists(jsonl_file):
        return processed_configs

    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                record = json.loads(line)
                # strip() so records written with the old "phi3:mini " model name still count as done
                processed_configs.add(_config_key(record['arxiv_id'], record['model'].strip(),
                                                  record['prompt_type'], record['temperature']))
            except (json.JSONDecodeError, KeyError):
                continue  # ignore corrupted lines

    logger.info("Resuming experiment. Found %d already completed runs.", len(processed_configs))
    return processed_configs


def main():
    INPUT_FILE = "math_500.parquet"
    OUTPUT_JSONL = "ai_experiment_results.jsonl"
    OUTPUT_JSON = "ai_experiment_results_final.json"
    TEST_LIMIT = 500

    processed_configs = _load_processed_configs(OUTPUT_JSONL)

    logger.info("Loading %s...", INPUT_FILE)
    test_rows = pl.read_parquet(INPUT_FILE).to_dicts()[:TEST_LIMIT]
    logger.info("Starting experiment on %d papers. Total configurations per paper: %d",
                len(test_rows), len(MODELS) * len(PROMPTS) * len(TEMPERATURES))

    experiment_results = []
    with open(OUTPUT_JSONL, "a", encoding="utf-8") as f:
        for row in test_rows:
            paper_id = row.get('id', 'Unknown')
            logger.info("--- Processing Paper %s ---", paper_id)

            full_latex = row['text']

            # Ground truth: the arXiv author list (arXiv metadata has no affiliations)
            meta_obj = parse_metadata(row['metadata'], paper_id)
            ground_truth_authors = [{"name": a.name, "affiliations": []} for a in meta_obj.authors] if meta_obj else []

            # 1. Baseline: rule-based extraction
            ext_cmds_list = extract_cmds.extract_cmds_from_string(full_latex)
            ext_info_trad = extract_author_aff.extract_affiliations_from_obj(ext_cmds_list, meta_obj)
            rule_based_authors_output = []
            if ext_info_trad and ext_info_trad.extractions:
                for ext in ext_info_trad.extractions:
                    for author in ext.authors:
                        rule_based_authors_output.append({"name": author.name, "affiliations": author.affiliations})

            rule_based_metrics = calculate_metrics_robust(rule_based_authors_output, ground_truth_authors)

            preamble = llm_extraction.get_latex_metadata_windows(full_latex, HEAD_CHARS, TAIL_CHARS)

            # 2. Experiment matrix
            for model in MODELS:
                for prompt_name, prompt_template in PROMPTS.items():
                    for temp in TEMPERATURES:
                        config_key = _config_key(paper_id, model, prompt_name, temp)
                        if config_key in processed_configs:
                            logger.info("Skipping %s - already processed.", config_key)
                            continue

                        logger.info("Running %s | %s | Temp: %s", model, prompt_name, temp)

                        start_time = time.time()
                        parsed_data, is_valid, error_msg = extract_with_ollama_experiment(
                            preamble, model, prompt_template, temp
                        )
                        duration = round(time.time() - start_time, 2)

                        ai_output_authors = [a.model_dump() for a in parsed_data.authors] if is_valid else []
                        if is_valid:
                            ai_metrics = calculate_metrics_robust(ai_output_authors, ground_truth_authors)
                        else:
                            ai_metrics = {"precision": 0.0, "recall": 0.0, "f1_score": 0.0}

                        record = {
                            "arxiv_id": paper_id,
                            "model": model,
                            "prompt_type": prompt_name,
                            "temperature": temp,
                            "time_sec": duration,
                            "valid_json": is_valid,

                            # AI author metrics
                            "ai_author_f1": ai_metrics["f1_score"],
                            "ai_author_precision": ai_metrics["precision"],  # hallucination metric
                            "ai_author_recall": ai_metrics["recall"],  # missed author metric

                            # Baseline (rule-based) comparison
                            "rule_based_author_f1": rule_based_metrics["f1_score"],

                            "rule_based_output": rule_based_authors_output,
                            "ai_output": ai_output_authors,
                            "error_msg": error_msg,
                        }
                        experiment_results.append(record)

                        # Write and flush immediately so a crash loses at most one run
                        f.write(json.dumps(record, ensure_ascii=False) + "\n")
                        f.flush()
                        os.fsync(f.fileno())

    # Compiled JSON of this run's records once everything finished
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f_final:
        json.dump(experiment_results, f_final, indent=4, ensure_ascii=False)

    logger.info("Experiment complete! Results saved to %s", OUTPUT_JSON)
    evaluate_experiment(OUTPUT_JSON)


if __name__ == "__main__":
    main()
