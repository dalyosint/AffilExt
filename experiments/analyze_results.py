import polars as pl
import time


def extract_scenarios(parquet_file: str):
    print(f"Scanning {parquet_file} to extract failure scenarios...")
    start_time = time.time()

    # scan_parquet keeps memory usage virtually at zero
    df = pl.scan_parquet(parquet_file)

    # ==========================================
    # SCENARIO 1: Completely Failed
    # (No extraction from Baseline OR AI)
    # ==========================================
    print("Extracting 'Completely Failed' papers...")
    completely_failed_df = df.filter(
        pl.col("extracted_info").is_null()
    ).select(["id", "extracted_info", "ai_output"])

    # Save to CSV so you can easily open it
    completely_failed_df.sink_csv("scenario_completely_failed.csv")

    # ==========================================
    # SCENARIO 2: Went to AI and AI FAILED
    # (Failed baseline, pushed to AI, but still no match)
    # ==========================================
    print("Extracting 'AI Failed' papers...")
    went_to_ai_but_failed_df = df.filter(
        # Condition for going to AI
        ~(pl.col("matched_info").is_not_null() & pl.col("ai_output").is_null()) &
        # Condition for failing at the end
        pl.col("matched_info").is_null()
    ).select(["id", "extracted_info", "ai_output"])

    went_to_ai_but_failed_df.sink_csv("scenario_ai_failed.csv")

    # ==========================================
    # SCENARIO 3: Failed Matching
    # (Extracted by someone, but no ROR match)
    # Note: Your previous run showed 0 for this, but here is the code just in case!
    # ==========================================
    print("Extracting 'Failed Matching' papers...")
    failed_matching_df = df.filter(
        pl.col("extracted_info").is_not_null() & pl.col("matched_info").is_null()
    ).select(["id", "extracted_info", "ai_output"])

    failed_matching_df.sink_csv("scenario_failed_matching.csv")

    print("\n" + "=" * 50)
    print(f"Extraction complete in {time.time() - start_time:.2f} seconds!")
    print("You can now open the following files in Excel, VS Code, or Notepad:")
    print(" - scenario_completely_failed.csv")
    print(" - scenario_ai_failed.csv")
    print(" - scenario_failed_matching.csv")
    print("=" * 50)


if __name__ == "__main__":
    # Point this to your compiled final output file
    extract_scenarios("math_sample_processed_final.parquet")
