import polars as pl
import jsonpickle
import json


def main():
    # 1. Load your processed dataset
    PARQUET_FILE = "math_sample_processed_final.parquet"
    print(f"Loading data from {PARQUET_FILE}...")
    df = pl.read_parquet(PARQUET_FILE)

    # Leon's Thresholds from the thesis
    NAME_CUTOFF = 70.0
    AFF_CUTOFF = 50.0

    total_papers = 0
    exact_author_count_matches = 0

    total_authors_extracted = 0
    successful_name_matches = 0

    total_affiliations_extracted = 0
    successful_aff_matches = 0

    for row in df.to_dicts():
        matched_json = row.get("matched_info")
        raw_metadata = row.get("metadata")

        # Skip if matching failed for this paper
        if not matched_json or matched_json == "null":
            continue

        # Decode the jsonpickle string back into MatchedPaperData
        matched_data = jsonpickle.decode(matched_json)
        total_papers += 1

        # --- Metric 1: Author Count Ratio ---
        # Compare ground truth (ArXiv metadata) to the extracted amount
        meta_dict = json.loads(raw_metadata)
        arxiv_author_count = len(meta_dict.get('authors_parsed', []))
        ext_author_count = len(matched_data.matched_authors)

        if arxiv_author_count == ext_author_count and arxiv_author_count > 0:
            exact_author_count_matches += 1

        # --- Metric 2 & 3: Name Similarity & Affiliation Match Rate ---
        for author in matched_data.matched_authors:
            total_authors_extracted += 1

            # Metric 2: Did the name match the ArXiv ground truth closely enough?
            if author.score >= NAME_CUTOFF:
                successful_name_matches += 1

            # Metric 3: Was the affiliation successfully linked to ROR?
            for aff in author.affiliations:
                total_affiliations_extracted += 1
                if aff.score >= AFF_CUTOFF:
                    successful_aff_matches += 1

    print("\n--- EXTRACTION EVALUATION RESULTS ---")
    print(f"Total Successfully Processed Papers: {total_papers}")

    print(f"\nMetric 1: Author Count Match")
    print(
        f"Papers where Extracted Author Count == ArXiv Author Count: {exact_author_count_matches}/{total_papers} ({(exact_author_count_matches / total_papers) * 100:.2f}%)")

    print(f"\nMetric 2: Name Similarity (Threshold >= {NAME_CUTOFF})")
    print(
        f"Successfully matched names: {successful_name_matches}/{total_authors_extracted} ({(successful_name_matches / total_authors_extracted) * 100:.2f}%)")

    if total_affiliations_extracted > 0:
        print(f"\nMetric 3: Affiliation Rate (Threshold >= {AFF_CUTOFF})")
        print(
            f"Successfully matched institutions to ROR: {successful_aff_matches}/{total_affiliations_extracted} ({(successful_aff_matches / total_affiliations_extracted) * 100:.2f}%)")


if __name__ == "__main__":
    main()