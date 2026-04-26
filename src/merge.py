import polars as pl
import os
import glob


def merge_parquet_batches():
    INPUT_DIR = "processed_batches"
    FINAL_OUTPUT_FILE = "math_sample_processed_final.parquet"

    # Check if there are any files to merge
    batch_files = glob.glob(os.path.join(INPUT_DIR, "*.parquet"))

    if not batch_files:
        print(f"❌ No batch files found in '{INPUT_DIR}'.")
        return

    print(f"Found {len(batch_files)} batch files. Merging them now...")

    try:
        # scan_parquet reads them lazily, sink_parquet writes chunk-by-chunk
        # so it won't crash your RAM even if the batches are huge!
        pl.scan_parquet(os.path.join(INPUT_DIR, "*.parquet")).sink_parquet(FINAL_OUTPUT_FILE)
        print(f"✅ Success! All batches combined and saved to '{FINAL_OUTPUT_FILE}'.")

    except Exception as e:
        print(f"❌ Failed to combine files: {e}")


if __name__ == "__main__":
    merge_parquet_batches()