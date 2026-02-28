import pandas as pd
import json
import logging
from pathlib import Path
import jsonpickle
import time
import matplotlib.pyplot as plt
import concurrent.futures
from functools import partial

import extract_cmds
import extract_author_aff
import match_data
import ror_dl
import util
from definition.data.ArxivMetadata import ArxivMetadata
from definition.data.Author import Author

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
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


# MUST BE AT TOP LEVEL FOR MACOS MULTIPROCESSING
def process_single_paper(row, ror_orgs, ror_orgs_dict):
    """Handles the processing for a single row to be run in a separate process."""
    paper_start_time = time.perf_counter()

    paper_id = row['id']
    full_latex_text = row['text']
    metadata_raw = row['metadata']

    meta_obj = parse_metadata(metadata_raw, paper_id)
    ext_cmds = extract_cmds.extract_cmds_from_string(full_latex_text)
    ext_info = extract_author_aff.extract_affiliations_from_obj(ext_cmds, meta_obj)

    extracted_result = None
    matched_result = None
    status = "extraction_failed"

    if ext_info:
        extracted_result = jsonpickle.encode(ext_info)
        final_data = match_data.match_and_resolve_single_paper(
            meta_obj, ext_info, ror_orgs, ror_orgs_dict
        )

        if final_data:
            matched_result = jsonpickle.encode(final_data)
            status = "success"
        else:
            status = "matching_failed"

    paper_end_time = time.perf_counter()
    duration = paper_end_time - paper_start_time

    return extracted_result, matched_result, status, duration


def main():
    INPUT_FILE = "math_only_sample_500.parquet"
    OUTPUT_FILE = "math_sample_processed.parquet"

    total_start_time = time.time()

    logger.info("Step 1: Loading ROR Dataset...")
    ror_dataset = match_data._get_ror_dataset()
    ror_orgs = match_data._process_ror_orgs(ror_dataset)
    ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)

    logger.info(f"Step 2: Loading Input Parquet {INPUT_FILE}...")
    df = pd.read_parquet(INPUT_FILE)
    rows = df.to_dict("records")

    extracted_results_column = []
    matched_results_column = []
    paper_processing_times = []
    success_count = 0
    extraction_failed_count = 0
    matching_failed_count = 0

    logger.info("Step 3: Processing papers with Multiprocessing...")
    processing_start_time = time.time()

    # Create a partial function with the ROR data permanently attached to it
    worker_func = partial(process_single_paper, ror_orgs=ror_orgs, ror_orgs_dict=ror_orgs_dict)

    # EXACTLY 4 PROCESSES FOR YOUR MAC
    MAX_CORES = 4

    # We use a chunksize of 5. This is highly optimized for your specific histogram:
    # It prevents the 40MB dict from being copied 500 individual times, but is small
    # enough that no CPU core gets stuck with too many of those 3-second papers.
    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_CORES) as executor:
        results = list(executor.map(worker_func, rows, chunksize=5))

    # Unpack the results
    for ext_res, match_res, status, duration in results:
        extracted_results_column.append(ext_res)
        matched_results_column.append(match_res)
        paper_processing_times.append(duration)

        if status == "success":
            success_count += 1
        elif status == "matching_failed":
            matching_failed_count += 1
        else:
            extraction_failed_count += 1

    processing_end_time = time.time()
    processing_time = processing_end_time - processing_start_time

    logger.info(f"Processing time: {processing_time:.2f} seconds")
    logger.info(f"Processing time: {processing_time / 60:.2f} minutes")

    # --- PLOTTING DIAGNOSTICS ---
    logger.info("Generating diagnostic plots...")

    plt.figure(figsize=(10, 6))
    plt.hist(paper_processing_times, bins=50, color='skyblue', edgecolor='black')
    plt.title('Distribution of Processing Times per Paper (Multiprocessing)')
    plt.xlabel('Processing Time (seconds)')
    plt.ylabel('Number of Papers')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('processing_times_histogram_multiprocess.png')
    plt.close()

    categories = ['Success', 'Extraction Failed', 'Matching Failed']
    counts = [success_count, extraction_failed_count, matching_failed_count]

    plt.figure(figsize=(8, 6))
    bars = plt.bar(categories, counts, color=['#4CAF50', '#F44336', '#FF9800'], edgecolor='black')
    plt.title('Paper Processing Outcomes (Multiprocessing)')
    plt.ylabel('Number of Papers')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + (max(counts) * 0.01), int(yval), ha='center', va='bottom',
                 fontweight='bold')
    plt.savefig('processing_outcomes_bar_multiprocess.png')
    plt.close()
    # ----------------------------

    logger.info("Step 4: Saving results...")
    df['extracted_info'] = extracted_results_column
    df['matched_info'] = matched_results_column
    df.to_parquet(OUTPUT_FILE)

    logger.info(f"Success! Output saved to {OUTPUT_FILE}")

    total_end_time = time.time()
    total_time = total_end_time - total_start_time
    logger.info(f"Total pipeline time: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()