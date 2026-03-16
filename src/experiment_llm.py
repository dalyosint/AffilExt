import json
import time
import logging
import re
import ollama
import polars as pl
from pydantic import BaseModel, ValidationError
from typing import List

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



def get_latex_preamble(text_content: str) -> str:
    """
    Extracts everything before \begin{document} or the main content.
    This guarantees we capture authors/affiliations without the massive paper body.
    """
    match = re.search(r'\\begin\{document\}|\\maketitle|\\begin\{abstract\}', text_content)
    if match:
        preamble = text_content[:match.start()]
        return preamble[:8000]
    return text_content[:8000]


#  Define Prompts
PROMPT_BASE = """You are a precise data extraction assistant.
Your task is to extract all authors and their specific affiliations from the provided LaTeX text.
You must return the data strictly adhering to the provided JSON schema.

INPUT:
\\author{Alice Smith$^{1,2}$ and Bob Jones$^{2}$}
\\affiliation{$^{1}$Department of Physics, MIT}
\\affiliation{$^{2}$CERN, Geneva, Switzerland}

EXPECTED OUTPUT:
{
  "authors": [
    {
      "name": "Alice Smith",
      "affiliations": ["Department of Physics, MIT", "CERN, Geneva, Switzerland"]
    },
    {
      "name": "Bob Jones",
      "affiliations": ["CERN, Geneva, Switzerland"]
    }
  ]
}

Analyze the user's LaTeX input and respond ONLY with valid JSON. Do not include markdown blocks or conversational text.
"""

PROMPT_CONSTRAINED = """You are a highly strict data extraction assistant.
Your task is to extract all authors and their specific affiliations from the provided LaTeX text.

CRITICAL RULES:
1. ONLY extract authors and affiliations that physically exist in the text.
2. DO NOT guess, infer, or hallucinate affiliations.
3. If an author has no listed affiliation, leave their affiliations array EMPTY [].
4. Return ONLY valid JSON matching the schema. NO conversational text.

INPUT:
\\author{Alice Smith$^{1}$ and Bob Jones}
\\affiliation{$^{1}$Department of Physics, MIT}

EXPECTED OUTPUT:
{
  "authors": [
    {
      "name": "Alice Smith",
      "affiliations": ["Department of Physics, MIT"]
    },
    {
      "name": "Bob Jones",
      "affiliations": []
    }
  ]
}
"""

PROMPT_SUPER = """Task: Extract authors and their affiliations from LaTeX.

Read only the text inside <TEXT>.

Where authors usually appear:
- \\author{...}

Where affiliations usually appear:
- \\affiliation{...}
- \\institute{...}
- \\address{...}
- text after \\\\ inside \\author{}

Extraction procedure:
1. Find author names in \\author{...}
2. Find affiliations in \\affiliation{}, \\institute{}, or \\address{}
3. Match affiliations to the nearest author if possible.

Rules:
- Use ONLY text that appears inside the <TEXT> tags.
- Do NOT invent names.
- Do NOT guess affiliations.
- If an author has no affiliation → use [].
- If no authors exist → return {"authors": []}
- NEVER output the literal words "EXTRACTED_NAME" or "EXTRACTED_AFFILIATION". Replace them with the actual text.

Output format (JSON only):
{
  "authors": [
    {
      "name": "<EXTRACTED_NAME>",
      "affiliations": ["<EXTRACTED_AFFILIATION>"]
    }
  ]
}

Return ONLY valid JSON. No conversational text.

<TEXT>
{text_input}
</TEXT>
"""

PROMPTS = {
    "Base_Prompt": PROMPT_BASE,
    "Constrained_Prompt": PROMPT_CONSTRAINED,
    "Super_Prompt": PROMPT_SUPER
}

#  Experiment Settings
MODELS = ["llama3.2:latest", "gemma3:1b", "qwen2.5:0.5b"]
TEMPERATURES = [0.0, 0.3, 0.7]


def extract_with_ollama_experiment(text_input, model_name, system_prompt, temp):
    """Custom extraction function to allow dynamic prompts and parameters."""
    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': text_input}
            ],
            format=ExtractionResponse.model_json_schema(),
            options={"temperature": temp, "top_p": 0.1 if temp == 0.0 else 0.9}
        )
        json_content = response['message']['content']
        parsed_data = ExtractionResponse.model_validate_json(json_content)
        return parsed_data, True, None
    except ValidationError as e:
        return None, False, "JSON Validation Error"
    except Exception as e:
        return None, False, str(e)


def check_hallucination(parsed_data: ExtractionResponse, preamble_text: str) -> bool:
    """Returns True if the AI extracted a name or affiliation NOT found in the text."""
    if not parsed_data:
        return False

    clean_text = re.sub(r'\s+', ' ', preamble_text).lower()

    for author in parsed_data.authors:
        clean_name = re.sub(r'\s+', ' ', author.name).lower()
        if clean_name not in clean_text:
            return True

        for aff in author.affiliations:
            clean_aff = re.sub(r'\s+', ' ', aff).lower()
            if clean_aff not in clean_text:
                return True
    return False


def main():
    INPUT_FILE = "math_100.parquet"
    OUTPUT_JSON = "ai_experiment_results.json"

    logger.info(f"Loading {INPUT_FILE}...")
    df = pl.read_parquet(INPUT_FILE)
    rows = df.to_dicts()

    TEST_LIMIT = 5
    test_rows = rows[:TEST_LIMIT]
    logger.info(
        f"Starting experiment on {len(test_rows)} papers. Total configurations per paper: {len(MODELS) * len(PROMPTS) * len(TEMPERATURES)}")

    experiment_results = []

    for row in test_rows:
        paper_id = row.get('id', 'Unknown')
        logger.info(f"--- Processing Paper {paper_id} ---")

        full_latex = row['text']
        metadata_raw = row['metadata']
        meta_obj = parse_metadata(metadata_raw, paper_id)

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

        preamble = get_latex_preamble(full_latex)

        # 2. Iterate Experiment Matrix
        for model in MODELS:
            for prompt_name, prompt_content in PROMPTS.items():
                for temp in TEMPERATURES:
                    logger.info(f"Running {model} | {prompt_name} | Temp: {temp}")

                    start_time = time.time()
                    parsed_data, is_valid, error_msg = extract_with_ollama_experiment(
                        preamble, model, prompt_content, temp
                    )
                    duration = round(time.time() - start_time, 2)

                    is_hallucinated = check_hallucination(parsed_data, preamble) if is_valid else None

                    # Serialize AI Output
                    ai_output_authors = [a.model_dump() for a in parsed_data.authors] if is_valid else []

                    # Build the JSON record
                    record = {
                        "arxiv_id": paper_id,
                        "model": model,
                        "prompt_type": prompt_name,
                        "temperature": temp,
                        "time_sec": duration,
                        "valid_json": is_valid,
                        "hallucinated": is_hallucinated,
                        "rule_based_output": rule_based_authors_output,
                        "ai_output": ai_output_authors,
                        "error_msg": error_msg
                    }
                    experiment_results.append(record)

    # output the  JSON file
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(experiment_results, f, indent=4, ensure_ascii=False)

    logger.info(f"Experiment complete! Results saved cleanly to {OUTPUT_JSON}")


if __name__ == "__main__":
    main()

