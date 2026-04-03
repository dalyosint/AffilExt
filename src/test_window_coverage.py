import polars as pl
import re
import os


def get_latex_metadata_windows(text_content: str) -> str:
    """
    Captures the "Head" (preamble) and the "Tail" (end of document)
    to catch authors at the top, and affiliations at the bottom.
    """
    # this function did cover 88%
    cut_triggers = r'\\begin\{abstract\}|\\section\|\\abstract\{|\\chapter\{'
    head_match = re.search(cut_triggers, text_content, re.IGNORECASE)

    if head_match:
        head_text = text_content[:head_match.start()]
        if len(head_text) > 4000:
            head_text = head_text[-4000:]  # Keep the bottom 4000 chars of the head
    else:
        head_text = text_content[:4000]

    # Grab the last 3000 characters of the entire file.
    # This safely catches \address{} blocks right before \end{document}
    tail_text = text_content[-1000:]


    combined_text = (
        "--- START OF DOCUMENT HEAD ---\n"
        f"{head_text}\n\n"
        "--- START OF DOCUMENT TAIL ---\n"
        f"{tail_text}"
    )

    return combined_text


def main():
    INPUT_FILE = "math_100.parquet"
    OUTPUT_FILE = "coverage_test_results.md"

    print(f"Loading {INPUT_FILE}...")
    try:
        df = pl.read_parquet(INPUT_FILE)
        rows = df.to_dicts()
    except Exception as e:
        print(f"Error loading parquet file: {e}")
        return

    print(f"Testing Window Strategy on {len(rows)} papers...")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Window of Interest Coverage Test\n\n")
        f.write(
            "Review these outputs to ensure the `\\author` and affiliation blocks are caught inside the window.\n\n")

        for idx, row in enumerate(rows):
            paper_id = row.get('id', f'Unknown_{idx}')
            full_latex = row.get('text', '')

            # Run our scissors
            windowed_text = get_latex_metadata_windows(full_latex)

            # Write the output clearly to a Markdown file so it's easy to read
            f.write(f"## Paper ID: {paper_id}\n")
            f.write("```latex\n")
            f.write(windowed_text.strip() + "\n")
            f.write("```\n")
            f.write("-" * 80 + "\n\n")

    print(f"Done! Open '{OUTPUT_FILE}' and scroll through to check your coverage.")


if __name__ == "__main__":
    main()