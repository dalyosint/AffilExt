import pandas as pd
import json
import logging
from pathlib import Path
import jsonpickle

# Import our workers
import extract_cmds
import extract_author_aff
import match_data
import ror_dl
import util
from definition.data.ArxivMetadata import ArxivMetadata
from definition.data.Author import Author

# Setup simple logging so we can see what's happening
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("ParquetPipeline")


def parse_metadata(json_str: str, arxiv_id: str) -> ArxivMetadata:
    """
    Helper: Converts the raw JSON string from your Parquet metadata column
    into the format the repo expects (ArxivMetadata object).
    """
    try:
        data = json.loads(json_str)

        # We need to manually build the Author list from the metadata
        # (Assuming 'authors_parsed' or similar field exists, otherwise basic parsing)
        authors_list = []
        if 'authors_parsed' in data:
            for auth in data['authors_parsed']:
                # auth is typically [lastname, firstname, affiliation]
                name = f"{auth[1]} {auth[0]}".strip()
                authors_list.append(Author(name, []))  # Affiliations list is empty initially
        else:
            # Fallback if parsed authors aren't there
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

    # --- PHASE 1: PREPARATION ---
    logger.info("Step 1: Loading ROR Dataset (The dictionary for matching)...")
    # This ensures we have the organization database ready in memory
    ror_dataset = match_data._get_ror_dataset()
    ror_orgs = match_data._process_ror_orgs(ror_dataset)
    ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)

    logger.info(f"Step 2: Loading Input Parquet {INPUT_FILE}...")
    df = pd.read_parquet(INPUT_FILE)

    # We will store results in these lists
    extracted_results_column = []
    matched_results_column = []

    # --- PHASE 2: PROCESSING CONVEYOR BELT ---
    logger.info("Step 3: Processing papers...")

    count = 0
    # ... inside src/pipeline_parquet.py ...

    # REPLACE THE OLD LOOP WITH THIS:
    for index, row in df.iterrows():
        paper_id = row['id']
        full_latex_text = row['text']
        metadata_raw = row['metadata']

        count += 1
        if count % 50 == 0:
            logger.info(f"Processed {count} papers...")

        # A. Parse Metadata
        meta_obj = parse_metadata(metadata_raw, paper_id)

        # B. Extract Commands
        ext_cmds = extract_cmds.extract_cmds_from_string(full_latex_text)

        # C. Extract Affiliations
        ext_info = extract_author_aff.extract_affiliations_from_obj(ext_cmds, meta_obj)

        # Save extraction result (as a JSON string)
        if ext_info:
            extracted_results_column.append(jsonpickle.encode(ext_info))

            # --- THIS IS THE KEY CHANGE ---
            # D. Match and Resolve (New Single Function Call)
            # We use the new function from match_data.py to do everything at once
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
            # ------------------------------

        else:
            extracted_results_column.append(None)
            matched_results_column.append(None)
    # --- PHASE 3: SAVING ---
    logger.info("Step 4: Saving results to new Parquet file...")

    # Add new columns to the dataframe
    df['extracted_info'] = extracted_results_column
    df['matched_info'] = matched_results_column

    # Save
    df.to_parquet(OUTPUT_FILE)
    logger.info(f"Success! Output saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()