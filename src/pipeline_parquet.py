import pandas as pd
import json
import logging
from pathlib import Path
import jsonpickle
import time

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


def main():

    INPUT_FILE = "math_only_sample_500.parquet"
    OUTPUT_FILE = "math_sample_processed.parquet"

    # START TOTAL TIMER
    total_start_time = time.time()

    logger.info("Step 1: Loading ROR Dataset...")
    ror_dataset = match_data._get_ror_dataset()
    ror_orgs = match_data._process_ror_orgs(ror_dataset)
    ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)

    logger.info(f"Step 2: Loading Input Parquet {INPUT_FILE}...")
    df = pd.read_parquet(INPUT_FILE)

    extracted_results_column = []
    matched_results_column = []

    logger.info("Step 3: Processing papers...")

    count = 0

    # START PROCESS TIMER
    processing_start_time = time.time()

    rows = df.to_dict("records")

    for row in rows:

        paper_id = row['id']
        full_latex_text = row['text']
        metadata_raw = row['metadata']

        count += 1

        if count % 50 == 0:
            logger.info(f"Processed {count} papers...")

        meta_obj = parse_metadata(metadata_raw, paper_id)

        ext_cmds = extract_cmds.extract_cmds_from_string(full_latex_text)

        ext_info = extract_author_aff.extract_affiliations_from_obj(ext_cmds, meta_obj)

        if ext_info:

            extracted_results_column.append(jsonpickle.encode(ext_info))

            final_data = match_data.match_and_resolve_single_paper(
                meta_obj,
                ext_info,
                ror_orgs,
                ror_orgs_dict
            )

            if final_data:
                matched_results_column.append(jsonpickle.encode(final_data))
            else:
                matched_results_column.append(None)

        else:

            extracted_results_column.append(None)
            matched_results_column.append(None)


    # END PROCESS TIMER
    processing_end_time = time.time()
    processing_time = processing_end_time - processing_start_time

    logger.info(f"Processing time: {processing_time:.2f} seconds")
    logger.info(f"Processing time: {processing_time/60:.2f} minutes")


    logger.info("Step 4: Saving results...")

    df['extracted_info'] = extracted_results_column
    df['matched_info'] = matched_results_column

    df.to_parquet(OUTPUT_FILE)

    logger.info(f"Success! Output saved to {OUTPUT_FILE}")


    # END TOTAL TIMER
    total_end_time = time.time()
    total_time = total_end_time - total_start_time

    logger.info(f"Total pipeline time: {total_time:.2f} seconds")
    logger.info(f"Total pipeline time: {total_time/60:.2f} minutes")


if __name__ == "__main__":
    main()