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
- Extract only names and affiliations explicitly present.
- Match authors to affiliations using the text.
- Ignore LaTeX commands and formatting.
- Do not include markers in output.
- If none, use [].
- No guessing.
- Output JSON only.

<LATEX_PREAMBLE>
{text_input}
</LATEX_PREAMBLE>
"""

PROMPT_SUPER = r"""You are an expert academic data extraction AI.Extract authors and affiliations from a LaTeX preamble.

Return JSON matching:
{ExtractionResponse.model_json_schema()}

Rules:
- Extract only names and affiliations explicitly present.
- Match authors to affiliations via markers in the text.
- Ignore LaTeX commands and formatting.
- Do not include markers in output.
- If none, use [].
- No guessing.
- Output JSON only.

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
\author{{Peter Pickl\footnote{{Institut f\"ur theoretische Physik, Universit\"at
        Wien, Boltzmanngasse 5, 1090 Vienna, Austria
         E-mail: pickl@mathematik.uni-muenchen.de}}, Detlef Duerr\footnote{{Mathematisches Institut der Universit\"at
         M\"unchen, Theresienstra\ss e 39, 80333 M\"unchen, Germany.
         E-mail: duerr@mathematik.uni-muenchen.de}}}}.

Output:
{{"authors":[
  {{"name":"Peter Pickl","affiliations":["Institut für theoretische Physik, Universität Wien, Boltzmanngasse 5, 1090 Vienna, Austria"]}},
  {{"name":"Detlef Duerr","affiliations":["Mathematisches Institut der Universität München, Theresienstraße 39, 80333 München, Germany"]}}
]}} 

{text_input}

"""

PROMPTS = {
    "Base_Prompt": PROMPT_BASE,
    "Constrained_Prompt": PROMPT_CONSTRAINED,
    "Super_Prompt": PROMPT_SUPER
}

#  Experiment Settings
MODELS = ["gemma2:2b" ] #, "gemma2:2b", "qwen2.5:0.5b"]phi3:mini"
TEMPERATURES = [0.0]  #, 0.3, 0.7]

def get_latex_preamble(text_content: str) -> str:
    r"""
    Captures everything from Line 1 down to \maketitle, \begin{abstract},
    or the first \section. This safely accommodates Standard, KOMA, ACM,
    IEEE, and AMS document classes.
    """
    # 1. Look for the commands that officially start the "Body Text"
    # We use re.IGNORECASE just in case someone typed \MakeTitle
    cut_triggers = r'\\maketitle|\\begin\{abstract\}|\\section\{|\\chapter\{'
    match = re.search(cut_triggers, text_content, re.IGNORECASE)

    if match:
        # 2. Cut the document right before the body text begins
        target_text = text_content[:match.start()]

        # 3. Limit to the BOTTOM 5000 characters of our cut.
        # This throws away the massive wall of \usepackage commands at the top,
        # leaving the clean author/title metadata at the bottom for the AI.
        if len(target_text) > 5000:
            return target_text[-5000:]
        return target_text

    # 4. Backup plan if none of the triggers are found
    print(r"Warning: Could not find \maketitle, abstract, or section tags.")
    return text_content[:5000]


def _call_ollama_api(model_name, messages, temp):
    """The raw API call that we will wrap in a timer."""
    return ollama.chat(
        model=model_name,
        messages=messages,
        format=ExtractionResponse.model_json_schema(),
        options={"temperature": temp, "top_p": 0.1 if temp == 0.0 else 0.9}
    )


def extract_with_ollama_experiment(text_input, model_name, system_prompt, temp, timeout_seconds=90):
    formatted_system_prompt = system_prompt.replace("{text_input}", text_input)
    messages = [{'role': 'system', 'content': formatted_system_prompt}]

    print("\n" + "=" * 60)
    print(f"🤖 DEBUG: Sending request to {model_name} | Temp: {temp}")
    print("SYSTEM MESSAGE (Rules + Data):")

    # Instantiate the executor WITHOUT the 'with' block
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(_call_ollama_api, model_name, messages, temp)

    try:
        # Wait for the result, kill if it exceeds timeout
        response = future.result(timeout=timeout_seconds)
        json_content = response['message']['content']
        parsed_data = ExtractionResponse.model_validate_json(json_content)
        print(f"✅ AI Output Parsed: {parsed_data}\n")
        return parsed_data, True, None

    except concurrent.futures.TimeoutError:
        # 1. This logs to your terminal so you can see it happening
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
        # THE MAGIC FIX: Force the executor to shut down WITHOUT waiting
        # for the stuck thread. This allows your script to actually move on!
        executor.shutdown(wait=False, cancel_futures=True)



def calculate_metrics_robust(extracted_authors, ground_truth_authors):
    """
    Calculates Precision, Recall, and F1-score for both Authors and Affiliations.
    Precision mathematically doubles as the Hallucination metric (e.g., 0.6 Precision = 40% Hallucination).
    """
    if not extracted_authors and not ground_truth_authors:
        return {
            "precision": 1.0, "recall": 1.0, "f1_score": 1.0,
            "aff_precision": 1.0, "aff_recall": 1.0, "aff_f1": 1.0
        }

    if not extracted_authors:
        return {
            "precision": 0.0, "recall": 0.0, "f1_score": 0.0,
            "aff_precision": 0.0, "aff_recall": 0.0, "aff_f1": 0.0
        }

    matched_gt = set()
    matched_pairs = []

    # --- STEP 1: One-to-one matching ---
    for i, ext_author in enumerate(extracted_authors):
        e_name = ext_author.get("name", "").lower().strip()
        best_idx = -1
        best_score = 0

        for j, gt_author in enumerate(ground_truth_authors):
            if j in matched_gt:
                continue

            t_name = gt_author.get("name", "").lower().strip()
            score = fuzz.ratio(e_name, t_name)

            if score > best_score:
                best_score = score
                best_idx = j

        if best_score >= 80:
            matched_gt.add(best_idx)
            matched_pairs.append((i, best_idx))

    true_positives = len(matched_pairs)

    # --- STEP 2: Precision / Recall (Authors) ---
    precision = true_positives / len(extracted_authors)
    recall = true_positives / len(ground_truth_authors) if ground_truth_authors else 0.0

    f1 = (2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0)

    # --- STEP 3: Affiliation Metrics ---
    aff_tp = 0
    aff_pred_total = 0
    aff_gt_total = 0

    for ext_idx, gt_idx in matched_pairs:
        ext_affs = extracted_authors[ext_idx].get("affiliations", [])
        gt_affs = ground_truth_authors[gt_idx].get("affiliations", [])

        ext_affs = [a.lower().strip() for a in ext_affs if a.strip()]
        gt_affs = [a.lower().strip() for a in gt_affs if a.strip()]

        aff_pred_total += len(ext_affs)
        aff_gt_total += len(gt_affs)

        used_gt = set()

        for e_aff in ext_affs:
            best_score = 0
            best_j = -1

            for j, t_aff in enumerate(gt_affs):
                if j in used_gt:
                    continue

                score = fuzz.token_set_ratio(e_aff, t_aff)

                if score > best_score:
                    best_score = score
                    best_j = j

            if best_score >= 70:
                aff_tp += 1
                used_gt.add(best_j)

    aff_precision = aff_tp / aff_pred_total if aff_pred_total else 0.0
    aff_recall = aff_tp / aff_gt_total if aff_gt_total else 0.0

    aff_f1 = (2 * aff_precision * aff_recall / (aff_precision + aff_recall) if aff_precision + aff_recall > 0 else 0.0)

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4),
        "aff_precision": round(aff_precision, 4),
        "aff_recall": round(aff_recall, 4),
        "aff_f1": round(aff_f1, 4)
    }


def main():
    INPUT_FILE = "math_100.parquet"
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

    TEST_LIMIT = 30
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

        # 1.  the Ground Truth
        meta_obj = parse_metadata(metadata_raw, paper_id)
        ground_truth_authors = []
        if meta_obj and hasattr(meta_obj, 'authors'):
            for author in meta_obj.authors:
                ground_truth_authors.append({
                    "name": getattr(author, 'name', ''),
                    "affiliations": getattr(author, 'affiliations', [])
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
        preamble = get_latex_preamble(full_latex)

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
                            "precision": 0.0, "recall": 0.0, "f1_score": 0.0,
                            "aff_precision": 0.0, "aff_recall": 0.0, "aff_f1": 0.0
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

                        # AI Affiliation Metrics
                        "ai_aff_f1": ai_metrics["aff_f1"],
                        "ai_aff_precision": ai_metrics["aff_precision"],  # (Hallucination metric)
                        "ai_aff_recall": ai_metrics["aff_recall"],  # (Missed affiliation metric)

                        # Baseline (Rule-based) Comparison
                        "rule_based_author_f1": rule_based_metrics["f1_score"],
                        "rule_based_aff_f1": rule_based_metrics["aff_f1"],

                        "rule_based_output": rule_based_authors_output,
                        "ai_output": ai_output_authors,
                        "error_msg": error_msg }
                    experiment_results.append(record)

                    # THE MAGIC FIX 2: Write and flush IMMEDIATELY after creating the record
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                    f.flush()
                    os.fsync(f.fileno())  # Belt-and-suspenders approach to force drive write

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f_final:
        json.dump(experiment_results, f_final, indent=4, ensure_ascii=False)

    logger.info(f"Experiment complete! Results saved cleanly to {OUTPUT_JSON}")

    f.write(json.dumps(record, ensure_ascii=False) + "\n")
    f.flush()  # Forces the computer to save it to the hard drive right now

if __name__ == "__main__":
    main()
