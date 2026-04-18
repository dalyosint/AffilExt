import json
import logging
import os
import glob
import time
import concurrent.futures
from functools import partial

# Used to convert Python objects → string
import jsonpickle
import polars as pl
import pyarrow.parquet as pq

# Your custom modules
import extract_cmds
import extract_author_aff
import match_data
from definition.data.ArxivMetadata import ArxivMetadata
from definition.data.Author import Author

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(processName)s] - %(levelname)s - %(message)s')
logger = logging.getLogger("ParquetPipeline")


def parse_metadata(json_str: str, arxiv_id: str) -> ArxivMetadata:
    try:
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
    """Runs once per CPU core to load the dataset exactly once per process."""
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

    extracted_result_json = None
    matched_result_json = None
    lowest_score = None
    status = "extraction_failed"

    try:
        full_latex_text = row['text']
        metadata_raw = row['metadata']

        meta_obj = parse_metadata(metadata_raw, paper_id)
        ext_cmds = extract_cmds.extract_cmds_from_string(full_latex_text)

        #  Traditional Extraction Only
        ext_info_trad = extract_author_aff.extract_affiliations_from_obj(ext_cmds, meta_obj)

        if ext_info_trad:
            extracted_result_json = jsonpickle.encode(ext_info_trad)
            logger.debug(f"[{paper_id}] Traditional extraction SUCCESS.")

            final_data = match_data.match_and_resolve_single_paper(
                meta_obj, ext_info_trad, global_ror_orgs, global_ror_orgs_dict
            )

            if final_data:
                matched_result_json = jsonpickle.encode(final_data)

                has_low_score = False
                current_lowest_score = 100.0

                # Check for scores below 80 using the correct 'affiliations' property
                for author in final_data.matched_authors:
                    for aff in author.affiliations:
                        if aff.score < current_lowest_score:
                            current_lowest_score = aff.score
                        if aff.score < 50:
                            has_low_score = True

                lowest_score = current_lowest_score

                if has_low_score:
                    status = "low_score_match"
                    logger.debug(f"[{paper_id}] Found match score below 80 (Lowest: {lowest_score:.2f}).")
                else:
                    status = "success"
                    logger.debug(f"[{paper_id}] Match SUCCESS (High score).")
            else:
                status = "matching_failed"
        else:
            logger.debug(f"[{paper_id}] Traditional extraction FAILED/EMPTY.")

    except Exception as e:
        logger.error(f"[{paper_id}] Failed processing paper: {e}", exc_info=False)
        status = "pipeline_error"

    duration = time.perf_counter() - paper_start_time
    if duration > 15.0:
        logger.warning(f"[{paper_id}] SLOW PROCESSING: Took {duration:.2f} seconds")

    # Add the extra columns directly to the dictionary if it's a target failure
    if status == "low_score_match":
        returned_row = row.copy()
        returned_row["extracted_info"] = extracted_result_json
        returned_row["matched_info"] = matched_result_json
        returned_row["lowest_score"] = lowest_score
    else:
        returned_row = None

    return paper_id, status, returned_row


def main():
    INPUT_FILE = "subset.parquet"  # Using subset.parquet based on your terminal logs
    TARGET_FAILED_PAPERS = 100  # Set to 100 based on your terminal logs
    OUTPUT_FILE = f"first_{TARGET_FAILED_PAPERS}_failed_matches.parquet"

    total_start_time = time.time()

    logger.info("Step 1: Loading ROR Dataset...")
    # Initialize globals for the main thread as well
    ror_dataset = match_data._get_ror_dataset()
    match_data._process_ror_orgs(ror_dataset)
    match_data._process_ror_orgs_to_dict(ror_dataset)

    logger.info(f"Step 2: Preparing to stream Input Parquet {INPUT_FILE}...")

    MAX_CORES = 2
    BATCH_SIZE = 50
    collected_failed_papers = []

    logger.info(f"Step 3: Processing papers looking for {TARGET_FAILED_PAPERS} bad matches...")
    processing_start_time = time.time()

    parquet_file = pq.ParquetFile(INPUT_FILE)
    batch_counter = 1

    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_CORES, initializer=init_worker) as executor:
        for batch in parquet_file.iter_batches(batch_size=BATCH_SIZE):

            if len(collected_failed_papers) >= TARGET_FAILED_PAPERS:
                break

            df_batch = pl.from_arrow(batch)
            logger.info(f"--- Starting Batch {batch_counter} ({df_batch.height} new rows) ---")

            rows = df_batch.to_dicts()
            results = list(executor.map(process_single_paper, rows, chunksize=5))

            for paper_id, status, returned_row in results:
                if status == "low_score_match":
                    collected_failed_papers.append(returned_row)
                    if len(collected_failed_papers) >= TARGET_FAILED_PAPERS:
                        break

            logger.info(
                f"Finished Batch {batch_counter}. Found: {len(collected_failed_papers)} / {TARGET_FAILED_PAPERS} failures so far.")
            batch_counter += 1

    processing_end_time = time.time()
    logger.info(f"Processing time: {(processing_end_time - processing_start_time) / 60:.2f} minutes")

    # --- SAVE FINAL FILE ---
    if collected_failed_papers:
        # Polars will automatically see 'extracted_info', 'matched_info', and 'lowest_score' in these dictionaries and make columns for them!
        df_failed = pl.DataFrame(collected_failed_papers[:TARGET_FAILED_PAPERS])
        df_failed.write_parquet(OUTPUT_FILE)
        logger.info(f"Success! Saved {len(df_failed)} bad matches to '{OUTPUT_FILE}'.")
    else:
        logger.warning(f"No papers with a match score below 80 were found in {INPUT_FILE}.")

    total_time = time.time() - total_start_time
    logger.info(f"Total pipeline time: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
