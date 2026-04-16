import logging
import ollama
import re
import concurrent.futures
from pydantic import BaseModel, ValidationError
from typing import List
import threading
import queue

import asyncio
from ollama import AsyncClient
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


def get_latex_metadata_windows(text_content: str) -> str:
    """
    Captures the "Head" (preamble) and the "Tail" (end of document)
    to catch authors at the top, and affiliations at the bottom.
    """
    cut_triggers = r'\\begin\{abstract\}|\\section\|\\abstract\{|\\chapter\{'
    head_match = re.search(cut_triggers, text_content, re.IGNORECASE)

    if head_match:
        head_text = text_content[:head_match.start()]
        if len(head_text) > 5000:
            head_text = head_text[-5000:]  # Keep the bottom 5000 chars of the head
    else:
        head_text = text_content[:5000]

    # Grab the last 1000 characters of the entire file.
    # This safely catches \address{} blocks right before \end{document}
    tail_text = text_content[-1000:]

    combined_text = (
        "--- START OF DOCUMENT HEAD ---\n"
        f"{head_text}\n\n"
        "--- START OF DOCUMENT TAIL ---\n"
        f"{tail_text}"
    )

    return combined_text



def extract_with_ollama(text_content: str, arxiv_metadata, model_name: str = "qwen2.5:0.5b",
                        timeout_seconds=20) -> ExtAuthorInfo:
    _logger.info(f"AI Fallback extraction using Ollama for {arxiv_metadata.arxiv_id}")

    text_input = get_latex_metadata_windows(text_content)
    formatted_system_prompt = PROMPT_CONSTRAINED.replace("{text_input}", text_input)
    messages = [{'role': 'system', 'content': formatted_system_prompt}]
    temp = 0.0

    # Define the async call inside the function
    async def run_ollama():
        client = AsyncClient()
        return await client.chat(
            model=model_name,
            messages=messages,
            format=ExtractionResponse.model_json_schema(),
            options={"temperature": temp, "top_p": 0.1 if temp == 0.0 else 0.9}
        )

    try:
        # Run it synchronously with a strict, leak-proof timeout
        response = asyncio.run(asyncio.wait_for(run_ollama(), timeout=timeout_seconds))

        json_content = response['message']['content']
        parsed_data = ExtractionResponse.model_validate_json(json_content)

        authors = [AIExtAuthor(name=a.name, affiliations=a.affiliations) for a in parsed_data.authors]

        if authors:
            ext_results = [ExtResults(scheme_name="Ollama_AI_Fallback_Constrained", authors=authors, score=1.0)]
            return ExtAuthorInfo(ext_type="ai_fallback", extractions=ext_results)

    except asyncio.TimeoutError:
        _logger.error(
            f"🚨 BOOM! TIMEOUT: Model {model_name} took over {timeout_seconds}s for {arxiv_metadata.arxiv_id}. Skipping.")
    except ValidationError as ve:
        _logger.error(f"JSON Validation Error for {arxiv_metadata.arxiv_id}: {ve}")
    except Exception as e:
        _logger.error(f"Ollama extraction failed for {arxiv_metadata.arxiv_id}: {e}")

    return None




