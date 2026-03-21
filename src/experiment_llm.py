import json
import time
import logging
import re
import ollama
import polars as pl
from pydantic import BaseModel, ValidationError
from typing import List, Optional

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
    print(" Warning: Could not find \maketitle, abstract, or section tags.")
    return text_content[:5000]



#  Define Prompts
PROMPT_BASE = """Extract all authors and their affiliations following LaTeX preamble.
<LATEX_PREAMBLE>
{text_input}
</LATEX_PREAMBLE> 
"""

PROMPT_CONSTRAINEDT = """Extract authors and affiliations from a LaTeX preamble.

Rules:
- List all authors.
- List all affiliations explicitly given.
- Match authors to affiliations using only the text.
- If none, use [].
- No guessing.
- Output valid JSON only.

Example:
Input:
\\author{Alice Smith, Bob Johnson, Carol Lee}
\\affil{ University Alpha}
\\affil{ Institute Beta}

Output:
{"authors":[
{"name":"Alice Smith","affiliations":["University Alpha"]},
{"name":"Bob Johnson","affiliations":["Institute Beta"]},
{"name":"Carol Lee","affiliations":[]}
]}

Format:
{"authors":[{"name":"Author Name","affiliations":["Affiliation"]}]}

<LATEX_PREAMBLE>
{text_input}
</LATEX_PREAMBLE>
"""

PROMPT_SUPER = rf"""You are an expert academic data extraction AI.Extract authors and affiliations from a LaTeX preamble.

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
MODELS = ["phi3:mini " , "gemma2:2b", "qwen2.5:0.5b"]
TEMPERATURES = [0.0]  #, 0.3, 0.7]


def extract_with_ollama_experiment(text_input, model_name, system_prompt, temp):
    """Custom extraction function to allow dynamic prompts and parameters."""

    formatted_system_prompt = system_prompt.replace("{text_input}", text_input)

    # ==========================================
    # DEBUG: PRINT STATEMENTS TO SEE AI INPUT
    # ==========================================
    print("\n" + "=" * 60)
    print(f"🤖 DEBUG: Sending request to {model_name} | Temp: {temp}")
    print("-" * 60)
    print("SYSTEM MESSAGE (Rules + Data):")
    # We slice it to 1000 characters just so it doesn't flood your entire terminal,
    # but you can remove the [:1000] if you want to see the whole massive string!
    print(formatted_system_prompt[:1000] + "\n...[Text truncated for printing]...")
    print("=" * 60 + "\n")


    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {'role': 'system',
                 'content': formatted_system_prompt}

            ],
            # instead system_prompt prompt template
            format=ExtractionResponse.model_json_schema(),
            options={"temperature": temp, "top_p": 0.1 if temp == 0.0 else 0.9}
        )
        json_content = response['message']['content']
        parsed_data = ExtractionResponse.model_validate_json(json_content)
        print(f"✅ AI Output Parsed: {parsed_data}\n")
        return parsed_data, True, None

    except ValidationError as e:
        return None, False, "JSON Validation Error"
    except Exception as e:
        return None, False, str(e)


def check_hallucination(parsed_data: ExtractionResponse, preamble_text: str) -> bool:

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

