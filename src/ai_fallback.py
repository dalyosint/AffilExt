import logging
import ollama
import re
import concurrent.futures
from pydantic import BaseModel, ValidationError
from typing import List

from definition.data.Author import Author as AIExtAuthor
from definition.data.ExtAuthorData import ExtAuthorInfo, ExtResults

_logger = logging.getLogger(__name__)


# Pydantic Models
class AuthorModel(BaseModel):
    name: str
    affiliations: List[str]


class ExtractionResponse(BaseModel):
    authors: List[AuthorModel]


# The winning prompt from your experiments
PROMPT_CONSTRAINED = """You are an academic data extraction AI.

Extract authors and affiliations from a LaTeX preamble.

Return JSON matching:
{json_schema}

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


def get_latex_preamble(text_content: str) -> str:
    r"""
    Captures everything from Line 1 down to \maketitle, \begin{abstract},
    or the first \section. Safely accommodates Standard, KOMA, ACM,
    IEEE, and AMS document classes.
    """
    cut_triggers = r'\\maketitle|\\begin\{abstract\}|\\section\{|\\chapter\{'
    match = re.search(cut_triggers, text_content, re.IGNORECASE)

    if match:
        target_text = text_content[:match.start()]

        # Limit to the BOTTOM 5000 characters of our cut
        # This throws away the massive wall of \usepackage commands at the top
        if len(target_text) > 5000:
            return target_text[-5000:]
        return target_text

    _logger.warning(r"Warning: Could not find \maketitle, abstract, or section tags.")
    return text_content[:5000]


def _call_ollama_api(model_name, messages, temp):
    """The raw API call wrapped for the timeout worker."""
    return ollama.chat(
        model=model_name,
        messages=messages,
        format=ExtractionResponse.model_json_schema(),
        options={"temperature": temp, "top_p": 0.1 if temp == 0.0 else 0.9}
    )


def extract_with_ollama(text_content: str, arxiv_metadata, model_name: str = "gemma2:2b",
                        timeout_seconds=50) -> ExtAuthorInfo:
    """
    Sends text to Ollama and enforces a structured JSON response.
    Includes a strict timeout executor from the experiment benchmarks.
    """
    _logger.info(f"AI Fallback extraction using Ollama for {arxiv_metadata.arxiv_id}")

    text_input = get_latex_preamble(text_content)

    # Format the prompt with our dynamic schema and input text
    schema_str = ExtractionResponse.model_json_schema()
    formatted_system_prompt = PROMPT_CONSTRAINED.replace("{json_schema}", str(schema_str)).replace("{text_input}",
                                                                                                   text_input)

    messages = [{'role': 'system', 'content': formatted_system_prompt}]
    temp = 0.0  # Strict best temperature from experiments

    # Setup timeout worker
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(_call_ollama_api, model_name, messages, temp)

    try:
        # Wait for the result, kill if it exceeds timeout
        response = future.result(timeout=timeout_seconds)
        json_content = response['message']['content']

        # Validate response
        parsed_data = ExtractionResponse.model_validate_json(json_content)

        # Convert Pydantic models back to the project's Author objects
        authors = [AIExtAuthor(name=a.name, affiliations=a.affiliations) for a in parsed_data.authors]

        if authors:
            # Wrap in ExtResults with a score of 1.0 (AI confidence)
            ext_results = [ExtResults(scheme_name="Ollama_AI_Fallback_Constrained", authors=authors, score=1.0)]
            return ExtAuthorInfo(ext_type="ai_fallback", extractions=ext_results)

    except concurrent.futures.TimeoutError:
        _logger.error(
            f"🚨 BOOM! TIMEOUT: Model {model_name} took over {timeout_seconds}s for {arxiv_metadata.arxiv_id}. Skipping.")
    except ValidationError as ve:
        _logger.error(f"JSON Validation Error for {arxiv_metadata.arxiv_id}: {ve}")
    except Exception as e:
        _logger.error(f"Ollama extraction failed for {arxiv_metadata.arxiv_id}: {e}")
    finally:
        # Kill the worker strictly
        executor.shutdown(wait=False, cancel_futures=True)

    return None




