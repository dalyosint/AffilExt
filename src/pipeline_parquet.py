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


def process_single_paper(row):
    """Handles the processing for a single row to be run in a separate process."""
    paper_start_time = time.perf_counter()
    paper_id = row.get('id', 'Unknown')

    logger.debug(f"[{paper_id}] Starting processing...")

    extracted_result = None
    matched_result = None
    ai_result = None
    status = "extraction_failed"

    try:
        full_latex_text = row['text']
        metadata_raw = row['metadata']

        logger.debug(f"[{paper_id}] Parsing metadata...")
        meta_obj = parse_metadata(metadata_raw, paper_id)
        ext_cmds = extract_cmds.extract_cmds_from_string(full_latex_text)

        #  Traditional Extraction
        # ext_info_trad = extract_author_aff.extract_affiliations_from_obj(ext_cmds, meta_obj)
        # if ext_info_trad:
          #  extracted_result = jsonpickle.encode(ext_info_trad)
           # logger.debug(f"[{paper_id}] Traditional extraction SUCCESS.")
        #else:
         #   logger.debug(f"[{paper_id}] Traditional extraction FAILED/EMPTY.")

        ext_info_trad = None
        extracted_result = None

        #  AI Extraction (The Experiment)
        logger.info(f"Running AI extraction for {paper_id}...")
        ext_info_ai = ai_fallback.extract_with_ollama(full_latex_text, meta_obj)
        if ext_info_ai:
            ai_result = jsonpickle.encode(ext_info_ai)
            logger.debug(f"[{paper_id}] AI extraction SUCCESS.")
        else:
            logger.debug(f"[{paper_id}] AI extraction FAILED/EMPTY.")

        # Choose which one to use for ROR Matching

        ext_info_for_matching = ext_info_trad if ext_info_trad else ext_info_ai

        if ext_info_for_matching:
            final_data = match_data.match_and_resolve_single_paper(
                meta_obj, ext_info_for_matching, global_ror_orgs, global_ror_orgs_dict
            )

            if final_data:
                logger.debug(f"[{paper_id}] Running ROR Matching...")
                matched_result = jsonpickle.encode(final_data)
                status = "success"
                logger.debug(f"[{paper_id}] Match SUCCESS.")
            else:
                status = "matching_failed"
                logger.debug(f"[{paper_id}] Match FAILED .")

    except Exception as e:
        logger.error(f"[{paper_id}] Failed processing paper: {e}", exc_info=True )
        status = "pipeline_error"

    paper_end_time = time.perf_counter()
    duration = paper_end_time - paper_start_time

    if duration > 15.0:
        logger.warning(f"[{paper_id}] SLOW PROCESSING: Took {duration:.2f} seconds")

    return extracted_result, matched_result, ai_result, status, duration


def main():
    INPUT_FILE = "math_500.parquet"
    OUTPUT_DIR = "processed_batches"  #  We use a directory now instead of a single file
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
    paper_processing_times = []

    logger.info("Step 3: Processing papers in streams with Multiprocessing...")
    processing_start_time = time.time()

    parquet_file = pq.ParquetFile(INPUT_FILE)
    batch_counter = 1

    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_CORES, initializer=init_worker ) as executor:

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

            for ext_res, match_res, ai_res, status, duration in results:
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
                        f"{batch_ext_fail} Ext Fail")
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
    logger.info(f"Total pipeline time: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
git