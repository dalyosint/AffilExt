import json
import logging
from pathlib import Path
# Used to convert Python objects → string
import jsonpickle
import ai_fallback

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


def process_single_paper(row, ror_orgs, ror_orgs_dict):
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
        logger.debug(f"[{paper_id}] Running Traditional Extraction...")
        ext_info_trad = extract_author_aff.extract_affiliations_from_obj(ext_cmds, meta_obj)
        if ext_info_trad:
            extracted_result = jsonpickle.encode(ext_info_trad)
            logger.debug(f"[{paper_id}] Traditional extraction SUCCESS.")
        else:
            logger.debug(f"[{paper_id}] Traditional extraction FAILED/EMPTY.")


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
                meta_obj, ext_info_for_matching, ror_orgs, ror_orgs_dict
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

    INPUT_FILE = "math_100.parquet"
    OUTPUT_FILE = "math_sample_processed.parquet"

    # start time
    total_start_time = time.time()

    logger.info("Step 1: Loading ROR Dataset...")
    ror_dataset = match_data._get_ror_dataset()
    ror_orgs = match_data._process_ror_orgs(ror_dataset)
    ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)

    logger.info(f"Step 2: Preparing to stream Input Parquet {INPUT_FILE}...")


    # Create a partial function with the ROR data permanently attached to it
    worker_func = partial(process_single_paper, ror_orgs=ror_orgs, ror_orgs_dict=ror_orgs_dict)

    MAX_CORES = 2
    BATCH_SIZE = 50

    # Diagnostics tracking
    success_count = 0
    extraction_failed_count = 0
    matching_failed_count = 0
    paper_processing_times = []

    logger.info("Step 3: Processing papers in streams with Multiprocessing...")
    processing_start_time = time.time()

    # Open the large parquet file for streaming reads
    parquet_file = pq.ParquetFile(INPUT_FILE)
    parquet_writer = None

    batch_counter = 1
    # ProcessPoolExecutor keeps the cores busy
    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_CORES) as executor:

        # iter_batches() streams the file in chunks without loading everything into memory
        for batch in parquet_file.iter_batches(batch_size=BATCH_SIZE):
            logger.info(f"--- Starting Batch {batch_counter} ({BATCH_SIZE} rows) ---")
            # Convert PyArrow batch to Polars DataFrame, then to dicts
            df_batch = pl.from_arrow(batch)
            rows = df_batch.to_dicts()


            # Execute the batch in parallel
            # While one row waits for AI, another core picks up the next row for extraction
            results = list(executor.map(worker_func, rows, chunksize=5))

            # Prepare columns for the results
            extracted_results_column = []
            matched_results_column = []
            ai_results_column = []

            batch_success = 0
            batch_match_fail = 0
            batch_ext_fail = 0
            # Unpack the results
            for ext_res, match_res, ai_res, status, duration in results:
                extracted_results_column.append(ext_res)
                matched_results_column.append(match_res)
                ai_results_column.append(ai_res)
                paper_processing_times.append(duration)

                if status == "success":
                    success_count += 1
                elif status == "matching_failed":
                    matching_failed_count += 1
                else:
                    extraction_failed_count += 1

            # Append the new results as columns to the current batch
            df_batch = df_batch.with_columns([
                pl.Series("extracted_info", extracted_results_column),
                pl.Series("matched_info", matched_results_column),
                pl.Series("ai_output", ai_results_column)
            ])

            # Convert back to PyArrow table for writing
            result_table = df_batch.to_arrow()

            # Write the batch directly to the output Parquet file
            if parquet_writer is None:
                # Initialize the writer with the schema of the first fully processed batch
                parquet_writer = pq.ParquetWriter(OUTPUT_FILE, result_table.schema)

            parquet_writer.write_table(result_table)
            logger.info(f"Successfully processed and wrote a batch of {len(rows)} rows.")

            for _, _, _, status, _ in results:
                if status == "success":
                    batch_success += 1
                elif status == "matching_failed":
                    batch_match_fail += 1
                else:
                    batch_ext_fail += 1

            logger.info(f"Finished Batch {batch_counter}. "
                        f"Stats: {batch_success} Success | "
                        f"{batch_match_fail} Match Fail | "
                        f"{batch_ext_fail} Ext Fail")
            batch_counter += 1


    # Close the writer once all streaming is done
    if parquet_writer:
        parquet_writer.close()
        logger.info("Parquet file successfully sealed and saved!")

    processing_end_time = time.time()
    processing_time = processing_end_time - processing_start_time

    logger.info(f"Processing time: {processing_time:.2f} seconds")
    logger.info(f"Processing time: {processing_time / 60:.2f} minutes")

    logger.info(f"Success! Final streamed output saved to {OUTPUT_FILE}")

    total_end_time = time.time()
    total_time = total_end_time - total_start_time
    logger.info(f"Total pipeline time: {total_time:.2f} seconds")



if __name__ == "__main__":
    main()