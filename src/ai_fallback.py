import logging
import ollama
import re
import concurrent.futures
from pydantic import BaseModel, ValidationError
from typing import List
import threading
import queue

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
        if len(target_text) > 3000:
            return target_text[-3000:]
        return target_text

    _logger.warning(r"Warning: Could not find \maketitle, abstract, or section tags.")
    return text_content[:3000]


def _call_ollama_api_worker(model_name, messages, temp, result_queue):
    """The raw API call wrapped for a daemon thread."""
    try:
        response = ollama.chat(
            model=model_name,
            messages=messages,
            format=ExtractionResponse.model_json_schema(),
            options={"temperature": temp, "top_p": 0.1 if temp == 0.0 else 0.9}
        )
        # Put successful response in the queue
        result_queue.put(("success", response))
    except Exception as e:
        # Put the error in the queue if it fails
        result_queue.put(("error", e))

def extract_with_ollama(text_content: str, arxiv_metadata, model_name: str = "gemma2:2b",
                        timeout_seconds=30) -> ExtAuthorInfo:
    """
    Sends text to Ollama and enforces a structured JSON response.
    Includes a strict timeout executor from the experiment benchmarks.
    """
    _logger.info(f"AI Fallback extraction using Ollama for {arxiv_metadata.arxiv_id}")

    text_input = get_latex_preamble(text_content)
    schema_str = ExtractionResponse.model_json_schema()
    formatted_system_prompt = PROMPT_CONSTRAINED.replace("{json_schema}", str(schema_str)).replace("{text_input}",
                                                                                                   text_input)

    messages = [{'role': 'system', 'content': formatted_system_prompt}]
    temp = 0.0

    # 1. Create a queue to get the data out of the thread
    result_queue = queue.Queue()

    # 2. Spin up a DAEMON thread (daemon=True is the magic fix that prevents hangs)
    t = threading.Thread(
        target=_call_ollama_api_worker,
        args=(model_name, messages, temp, result_queue),
        daemon=True
    )
    t.start()

    try:
        # Wait for the result, kill if it exceeds timeout.
        # If timeout hits, queue.Empty is raised.
        status, response = result_queue.get(timeout=timeout_seconds)

        if status == "error":
            raise response  # Re-raise whatever error happened inside the thread

        json_content = response['message']['content']

        # Validate response
        parsed_data = ExtractionResponse.model_validate_json(json_content)

        authors = [AIExtAuthor(name=a.name, affiliations=a.affiliations) for a in parsed_data.authors]

        if authors:
            ext_results = [ExtResults(scheme_name="Ollama_AI_Fallback_Constrained", authors=authors, score=1.0)]
            return ExtAuthorInfo(ext_type="ai_fallback", extractions=ext_results)

    except queue.Empty:
        # This catches the timeout. The daemon thread is left behind to die automatically.
        _logger.error(
            f"🚨 BOOM! TIMEOUT: Model {model_name} took over {timeout_seconds}s for {arxiv_metadata.arxiv_id}. Skipping.")
    except ValidationError as ve:
        _logger.error(f"JSON Validation Error for {arxiv_metadata.arxiv_id}: {ve}")
    except Exception as e:
        _logger.error(f"Ollama extraction failed for {arxiv_metadata.arxiv_id}: {e}")

    return None




