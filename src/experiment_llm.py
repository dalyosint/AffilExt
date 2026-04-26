import json
import time
import logging
import re
import os
import ollama
import concurrent.futures
import polars as pl
from pydantic import BaseModel, ValidationError
from typing import List, Optional
from rapidfuzz import fuzz
# existing pipeline tools
import extract_cmds
import extract_author_aff
from pipeline_parquet import parse_metadata

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("ExperimentRunner")

# Pydantic Models
class AuthorModel(BaseModel):
    name: str
    affiliations: List[str]

class ExtractionResponse(BaseModel):
    authors: List[AuthorModel]

# Prompts
PROMPT_BASE = """Extract the authors and affiliations from this LaTeX text and return it as JSON.
{text_input}
"""

PROMPT_CONSTRAINED = """You are an academic data extraction AI.
Extract authors and affiliations from a LaTeX preamble.
Return JSON matching:
{ExtractionResponse.model_json_schema()}
Rules:
Extraction Rules:
1. Strict Literal Extraction: Extract only author names and institutional affiliations explicitly present in the text.
2. Marker-Based Mapping: Utilize explicit textual markers (superscripts, asterisks, footnotes) or structural proximity to accurately map each author to their respective affiliations.
3. Exclude Metadata: Do not include email addresses, job titles, funding acknowledgments, or academic degrees in the author or affiliation fields. 
4. Multiple Affiliations: If an author belongs to multiple institutions, list each explicitly linked affiliation in their array.
5. Orphaned Authors: If an author has no identifiable affiliation, return an empty array [] for that author. Zero inference is permitted.
6. Clean Strings: Remove all linking markers, footnote symbols, and LaTeX structural commands from the final output strings.


<LATEX_PREAMBLE>
{text_input}
</LATEX_PREAMBLE>
"""

PROMPT_SUPER = r"""You are an expert academic data extraction AI.Extract authors and affiliations from a LaTeX preamble.
Return JSON matching:
{ExtractionResponse.model_json_schema()}
Rules:
Extraction Rules:
1. Strict Literal Extraction: Extract only author names and institutional affiliations explicitly present in the text.
2. Marker-Based Mapping: Utilize explicit textual markers (superscripts, asterisks, footnotes) or structural proximity to accurately map each author to their respective affiliations.
3. Exclude Metadata: Do not include email addresses, job titles, funding acknowledgments, or academic degrees in the author or affiliation fields. 
4. Multiple Affiliations: If an author belongs to multiple institutions, list each explicitly linked affiliation in their array.
5. Orphaned Authors: If an author has no identifiable affiliation, return an empty array [] for that author. Zero inference is permitted.
6. Clean Strings: Remove all linking markers, footnote symbols, and LaTeX structural commands from the final output strings. 


EXAMPLE 1 
Input:
\begin{{center}}
{{\large\textbf{{ON THE PSEUDOSPECTRUM OF ELLIPTIC QUADRATIC DIFFERENTIAL OPERATORS}}\\
\bigskip
\medskip
Karel \textsc{{Pravda-Starov}}\\
\bigskip
University of California, Berkeley}}
\end{{center}}

Output:
{{"authors":[
  {{"name":"Karel Pravda-Starov","affiliations":["University of California, Berkeley"]}}
]}}

EXAMPLE 2 
Input:
\begin{{large}}
{{J. Harnad}}$^{{\dagger \ddagger}}$\footnote{{harnad@crm.umontreal.ca}}
and
{{A. Yu. Orlov}}$^{{\star}}$\footnote{{orlovs@wave.sio.rssi.ru}}
\end{{large}} \\
\bigskip
\begin{{small}}
$^{{\dagger}}$ {{\em Centre de recherches math\'ematiques, Universit\'e de Montr\'eal\\
C.~P.~6128, succ. centre ville, Montr\'eal, Qu\'ebec, Canada H3C 3J7}} \\
\smallskip
$^{{\ddagger}}$ {{\em Department of Mathematics and Statistics, Concordia University\\
7141 Sherbrooke W., Montr\'eal, Qu\'ebec, Canada H4B 1R6}} \\
\smallskip
$^{{\star}}$ {{\em Nonlinear Wave Processes Laboratory, \\
Oceanology Institute, 36 Nakhimovskii Prospect\\
Moscow 117997, Russia}} \\
\end{{small}}
 
Output:
{{"authors":[
  {{"name":"J. Harnad","affiliations":["Centre de recherches mathématiques, Université de Montréal, C. P. 6128, succ. centre ville, Montréal, Québec, Canada H3C 3J7","Department of Mathematics and Statistics, Concordia University, 7141 Sherbrooke W., Montréal, Québec, Canada H4B 1R6"]}},
  {{"name":"A. Yu. Orlov","affiliations":["Nonlinear Wave Processes Laboratory, Oceanology Institute, 36 Nakhimovskii Prospect, Moscow 117997, Russia"]}}
]}} 

<LATEX_PREAMBLE>
{text_input}
</LATEX_PREAMBLE> 

"""

PROMPTS = {
    "Base_Prompt": PROMPT_BASE,
    "Constrained_Prompt": PROMPT_CONSTRAINED,
    "Super_Prompt": PROMPT_SUPER
}

#  Experiment Settings
MODELS =  ["phi3:mini ", "gemma2:2b", "qwen2.5:0.5b"]


TEMPERATURES = [0.0, 0.3, 0.7]

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
        if len(head_text) > 5000:
            head_text = head_text[-5000:]  # Keep the bottom 4000 chars of the head
    else:
        head_text = text_content[:5000]

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



def _call_ollama_api(model_name, messages, temp):
    """The raw API call that we will wrap in a timer."""
    return ollama.chat(
        model=model_name,
        messages=messages,
        format=ExtractionResponse.model_json_schema(),
        options={"temperature": temp,
                 "top_p": 0.1 if temp == 0.0 else 0.9
                 }
    )


def extract_with_ollama_experiment(text_input, model_name, system_prompt, temp, timeout_seconds=90):
    formatted_system_prompt = system_prompt.replace("{text_input}", text_input)
    messages = [{'role': 'system', 'content': formatted_system_prompt}]

    print("\n" + "=" * 60)
    print(f"🤖 DEBUG: Sending request to {model_name} | Temp: {temp}")
    print("SYSTEM MESSAGE (Rules + Data):")

    #  create a worker
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    # we call the ollama api
    future = executor.submit(_call_ollama_api, model_name, messages, temp)

    try:
        # Wait for the result, kill if it exceeds timeout
        response = future.result(timeout=timeout_seconds)
        json_content = response['message']['content']
        # json evaluation
        parsed_data = ExtractionResponse.model_validate_json(json_content)
        print(f"✅ AI Output Parsed: {parsed_data}\n")
        # no json was outputed
        return parsed_data, True, None

    except concurrent.futures.TimeoutError:
        # limit run out ( 3 minutes )
        logger.error(f"🚨 BOOM! TIMEOUT: {model_name} took too long! Skipping to the next one.")

        # 2. You can also add a standard print statement if you prefer
        print(f"⚠️ [CUSTOM MESSAGE] The model {model_name} choked on this paper. Moving on!")

        # 3. This string gets saved into your JSONL file under the 'error_msg' key
        return None, False, f"Custom Timeout Error: Model failed to respond within {timeout_seconds} seconds."

    except ValidationError:
        return None, False, "JSON Validation Error"
    except Exception as e:
        return None, False, str(e)
    finally:
        # we kill the worker
        executor.shutdown(wait=False, cancel_futures=True)


def calculate_metrics_robust(extracted_authors, ground_truth_authors):
    """
    Calculates Precision, Recall, and F1-score for Authors.
    Uses the Hybrid max(ratio, token_set_ratio) approach calibrated to a threshold of 70.
    """
    if not extracted_authors and not ground_truth_authors:
        return {"precision": 1.0, "recall": 1.0, "f1_score": 1.0}

    if not extracted_authors:
        return {"precision": 0.0, "recall": 0.0, "f1_score": 0.0}

    matched_gt = set()
    matched_pairs = []

    for i, ext_author in enumerate(extracted_authors):
        e_name = ext_author.get("name", "").lower().strip()
        best_idx = -1
        best_score = 0

        for j, gt_author in enumerate(ground_truth_authors):
            if j in matched_gt:
                continue

            t_name = gt_author.get("name", "").lower().strip()

            # Hybrid Fuzzy Logic
            exact_score = fuzz.ratio(e_name, t_name)
            token_score = fuzz.token_set_ratio(e_name, t_name)
            score = max(exact_score, token_score)

            if score > best_score:
                best_score = score
                best_idx = j

        # Calibrated threshold based on our scientific analysis
        if best_score >= 70:
            matched_gt.add(best_idx)
            matched_pairs.append((i, best_idx))

    true_positives = len(matched_pairs)

    precision = true_positives / len(extracted_authors)
    recall = true_positives / len(ground_truth_authors) if ground_truth_authors else 0.0
    f1 = (2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0)

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4)
    }

def evaluate_experiment(json_file):
        """Reads the final JSON results and calculates benchmark metrics using Polars."""

        logger.info("\n" + "=" * 60)
        logger.info("📊 FINAL BENCHMARKING RESULTS")
        logger.info("=" * 60)

        if not os.path.exists(json_file):
            logger.error(f"Could not find {json_file} to evaluate.")
            return

        # Load the JSON file into a Polars DataFrame
        df = pl.read_json(json_file, schema_overrides={"error_msg": pl.String})

        # Group by prompt_type and calculate our metrics
        summary_df = df.group_by("model", "prompt_type", "temperature").agg([
            # 1. Average F1 Score
            pl.col("ai_author_f1").mean().round(4).alias("avg_f1"),

            # 1b. Average Precision & Recall (for deeper insights)
            pl.col("ai_author_precision").mean().round(4).alias("avg_precision"),
            pl.col("ai_author_recall").mean().round(4).alias("avg_recall"),

            # 2. Percentage of Valid JSON outputs
            (pl.col("valid_json").cast(pl.Int32).mean() * 100).round(2).alias("valid_json_percent"),

            # 3. Average Execution Time
            pl.col("time_sec").mean().round(2).alias("avg_time_sec"),

            # Total times this prompt was tested
            # pl.len().alias("total_runs")

         ]).sort(["model", "avg_f1"], descending=[False, True])   # Sort so the best F1 score is at the top

        print("\n")
        print(summary_df)

        # Optionally save this summary to a CSV for easy viewing later
        summary_df.write_csv("prompt_benchmark_summary.csv")
        logger.info("✅ Summary saved to prompt_benchmark_summary.csv")
        print("=" * 50 + "\n")


def main():
    INPUT_FILE = ("math_500.parquet")
    OUTPUT_JSONL = "ai_experiment_results.jsonl"
    OUTPUT_JSON = "ai_experiment_results_final.json"

    # 1. READ EXISTING RESULTS TO RESUME WHERE WE LEFT OFF
    processed_configs = set()
    if os.path.exists(OUTPUT_JSONL):
        with open(OUTPUT_JSONL, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    record = json.loads(line)
                    config_key = f"{record['arxiv_id']}_{record['model']}_{record['prompt_type']}"
                    processed_configs.add(config_key)
                except json.JSONDecodeError:
                    continue  # Ignore corrupted lines
        logger.info(f"Resuming experiment. Found {len(processed_configs)} already completed runs.")


    logger.info(f"Loading {INPUT_FILE}...")
    df = pl.read_parquet(INPUT_FILE)
    rows = df.to_dicts()

    TEST_LIMIT = 500
    test_rows = rows[:TEST_LIMIT]
    logger.info(
        f"Starting experiment on {len(test_rows)} papers. Total configurations per paper: {len(MODELS) * len(PROMPTS) * len(TEMPERATURES)}")

    experiment_results = []
    with open(OUTPUT_JSONL, "a", encoding="utf-8") as f:
     for row in test_rows:
        paper_id = row.get('id', 'Unknown')
        logger.info(f"--- Processing Paper {paper_id} ---")

        full_latex = row['text']
        metadata_raw = row['metadata']

        # the Ground truth
        meta_obj = parse_metadata(metadata_raw, paper_id)
        ground_truth_authors = []
        if meta_obj:  # Just check if parsing succeeded (didn't return None)
            for author in meta_obj.authors:
                ground_truth_authors.append({
                    "name": author.name,
                    "affiliations": []  # Hardcode to empty list since we know they don't exist
                })



        # 1. Run Traditional Rule-Based

        ext_cmds_list = extract_cmds.extract_cmds_from_string(full_latex)
        ext_info_trad = extract_author_aff.extract_affiliations_from_obj(ext_cmds_list, meta_obj)
        # Serialize the Rule-Based Output to a list of dicts for clean JSON comparison
        rule_based_authors_output = []
        if ext_info_trad and ext_info_trad.extractions:
            for ext in ext_info_trad.extractions:
                for author in ext.authors:
                    rule_based_authors_output.append({
                        "name": author.name,
                        "affiliations": author.affiliations
                    })

        rule_based_metrics = calculate_metrics_robust(rule_based_authors_output, ground_truth_authors)


        preamble = get_latex_metadata_windows(full_latex)
        # 2. Iterate Experiment Matrix
        for model in MODELS:
            for prompt_name, prompt_content in PROMPTS.items():
                current_config_key = f"{paper_id}_{model}_{prompt_name}"
                if current_config_key in processed_configs:
                    logger.info(f"Skipping {current_config_key} - Already processed.")
                    continue  # Skip to the next one!

                for temp in TEMPERATURES:
                    logger.info(f"Running {model} | {prompt_name} | Temp: {temp}")

                    start_time = time.time()
                    parsed_data, is_valid, error_msg = extract_with_ollama_experiment(
                        preamble, model, prompt_content, temp
                    )
                    duration = round(time.time() - start_time, 2)

                    # Serialize AI Output
                    ai_output_authors = [a.model_dump() for a in parsed_data.authors] if is_valid else []

                    # Run Metrics
                    if is_valid:
                        ai_metrics = calculate_metrics_robust(ai_output_authors, ground_truth_authors)
                    else:
                        ai_metrics = {
                            "precision": 0.0, "recall": 0.0, "f1_score": 0.0
                        }

                    # Build the JSON record
                    record = {
                        "arxiv_id": paper_id,
                        "model": model,
                        "prompt_type": prompt_name,
                        "temperature": temp,
                        "time_sec": duration,
                        "valid_json": is_valid,

                        # AI Author Metrics
                        "ai_author_f1": ai_metrics["f1_score"],
                        "ai_author_precision": ai_metrics["precision"],  # (Hallucination metric)
                        "ai_author_recall": ai_metrics["recall"],  # (Missed author metric)

                        # Baseline (Rule-based) Comparison
                        "rule_based_author_f1": rule_based_metrics["f1_score"],


                        "rule_based_output": rule_based_authors_output,
                        "ai_output": ai_output_authors,
                        "error_msg": error_msg }
                    experiment_results.append(record)

                    # THE MAGIC FIX 2: Write and flush IMMEDIATELY after creating the record
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                    f.flush()
                    os.fsync(f.fileno())  # Belt-and-suspenders approach to force drive write

                    # Output a final compiled JSON file if the script successfully finishes everything
     with open(OUTPUT_JSON, "w", encoding="utf-8") as f_final:
        json.dump(experiment_results, f_final, indent=4, ensure_ascii=False)

     logger.info(f"Experiment complete! Results saved cleanly to {OUTPUT_JSON}")
     evaluate_experiment(OUTPUT_JSON)

if __name__ == "__main__":
    main()
