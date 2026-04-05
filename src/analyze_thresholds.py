import json
import polars as pl
from rapidfuzz import fuzz
import pandas as pd
from pipeline_parquet import parse_metadata


def calculate_experimental_f1(extracted_authors, ground_truth_authors, method, threshold):
    """Calculates F1 score based on a specific RapidFuzz method and threshold."""
    if not extracted_authors and not ground_truth_authors:
        return 1.0
    if not extracted_authors:
        return 0.0

    matched_gt = set()
    true_positives = 0

    for ext_author in extracted_authors:
        e_name = ext_author.get("name", "").lower().strip()
        best_idx = -1
        best_score = 0

        for j, gt_author in enumerate(ground_truth_authors):
            if j in matched_gt:
                continue

            t_name = gt_author.get("name", "").lower().strip()

            if method == "ratio":
                score = fuzz.ratio(e_name, t_name)
            elif method == "token":
                score = fuzz.token_set_ratio(e_name, t_name)
            elif method == "hybrid":
                score = max(fuzz.ratio(e_name, t_name), fuzz.token_set_ratio(e_name, t_name))

            if score > best_score:
                best_score = score
                best_idx = j

        if best_score >= threshold:
            matched_gt.add(best_idx)
            true_positives += 1

    precision = true_positives / len(extracted_authors)
    recall = true_positives / len(ground_truth_authors) if ground_truth_authors else 0.0

    if precision + recall > 0:
        return 2 * precision * recall / (precision + recall)
    return 0.0


def main():
    print("Loading data...")
    # Load AI outputs
    with open('QwenT0.json', 'r', encoding='utf-8') as f:
        ai_results = json.load(f)

    # Load Ground Truth from Parquet
    df = pl.read_parquet('math_100.parquet').to_dicts()
    gt_dict = {}
    for row in df:
        paper_id = row.get('id')
        meta_obj = parse_metadata(row['metadata'], paper_id)
        if meta_obj:
            gt_dict[paper_id] = [{"name": a.name} for a in meta_obj.authors]

    # Target specific run to evaluate (Qwen2.5, Constrained Prompt, Temp 0.0)
    target_runs = [r for r in ai_results if
                   r['model'] == 'qwen2.5:0.5b' and r['prompt_type'] == 'Constrained_Prompt' and r[
                       'temperature'] == 0.0 and r['valid_json']]

    print(f"Testing across {len(target_runs)} papers...\n")


    # scores printing
    print("=== HOW THE ALGORITHMS GRADE STRINGS (TOP 30) ===")

    # Slice the first 30 papers
    for run in target_runs[:50]:
        paper_id = run['arxiv_id']

        ext_names = [a.get("name", "") for a in run['ai_output']]
        gt_names = [a.get("name", "") for a in gt_dict.get(paper_id, [])]

        print(f"\n📄 Paper {paper_id}:")

        if not ext_names:
            print("  [No authors extracted by AI]")
            continue
        if not gt_names:
            print("  [No authors in Ground Truth]")
            continue

        # Compare each AI name to the best Ground Truth name
        for e_name in ext_names:
            e_name_clean = e_name.lower().strip()

            best_t_name = None
            best_ratio = 0
            best_token = 0
            best_hybrid = 0

            # Find the closest real name
            for t_name in gt_names:
                t_name_clean = t_name.lower().strip()

                # Calculate all three scores
                r_score = fuzz.ratio(e_name_clean, t_name_clean)
                t_score = fuzz.token_set_ratio(e_name_clean, t_name_clean)
                h_score = max(r_score, t_score)

                # Keep the match that has the highest hybrid score
                if h_score > best_hybrid:
                    best_hybrid = h_score
                    best_ratio = r_score
                    best_token = t_score
                    best_t_name = t_name

            # Print the detailed breakdown for this pair
            if best_t_name:
                print(f"  AI Extracted : '{e_name}'")
                print(f"  Ground Truth : '{best_t_name}'")
                print(
                    f"  ➔ Scores     : Ratio = {best_ratio:.1f} | Token = {best_token:.1f} | Hybrid = {best_hybrid:.1f}")
                print("  -")

    print("=================================================\n")
    # =========================================================

    print("Starting Threshold Evaluation...\n")

    methods = ["ratio", "token", "hybrid"]
    thresholds = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    results_data = []

    for method in methods:
        for thresh in thresholds:
            total_f1 = 0

            for run in target_runs:
                paper_id = run['arxiv_id']
                ext_authors = run['ai_output']
                gt_authors = gt_dict.get(paper_id, [])

                f1 = calculate_experimental_f1(ext_authors, gt_authors, method, thresh)
                total_f1 += f1

            avg_f1 = total_f1 / len(target_runs) if target_runs else 0
            results_data.append({"Method": method, "Threshold": thresh, "Avg_F1": round(avg_f1, 4)})

    # Print results nicely using Pandas
    results_df = pd.DataFrame(results_data)
    pivot_table = results_df.pivot(index="Threshold", columns="Method", values="Avg_F1")

    print("=== F1 SCORE BASED ON EVALUATION STRICTNESS ===")
    print(pivot_table)


if __name__ == "__main__":
    main()