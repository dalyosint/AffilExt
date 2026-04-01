import polars as pl
import re
import os


def get_latex_metadata_window(text_content: str) -> str:
    """
    Captures everything from Line 1 down to \maketitle, \begin{abstract},
    or the first \section / \chapter.
    """
    # 1. Look for the commands that officially start the "Body Text"
    cut_triggers = r'\\maketitle|\\begin\{abstract\}|\\section\{|\\chapter\{'
    match = re.search(cut_triggers, text_content, re.IGNORECASE)

    if match:
        # 2. Cut the document right before the body text begins
        target_text = text_content[:match.start()]

        # 3. Limit to the BOTTOM 5000 characters of our cut.
        if len(target_text) > 5000:
            return target_text[-5000:]
        return target_text

    # 4. Backup plan if none of the triggers are found
    return text_content[:5000]


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
            windowed_text = get_latex_metadata_window(full_latex)

            # Write the output clearly to a Markdown file so it's easy to read
            f.write(f"## Paper ID: {paper_id}\n")
            f.write("```latex\n")
            f.write(windowed_text.strip() + "\n")
            f.write("```\n")
            f.write("-" * 80 + "\n\n")

    print(f"Done! Open '{OUTPUT_FILE}' and scroll through to check your coverage.")


if __name__ == "__main__":
    main()