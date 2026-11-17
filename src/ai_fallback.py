"""LLM fallback for papers where rule-based extraction fails (used by pipeline_parquet.py)."""
import logging

from pydantic import ValidationError

import llm_extraction
from definition.data.Author import Author as AIExtAuthor
from definition.data.ExtAuthorData import ExtAuthorInfo, ExtResults

_logger = logging.getLogger(__name__)


def extract_with_ollama(text_content: str, arxiv_metadata, model_name: str = llm_extraction.DEFAULT_MODEL,
                        timeout_seconds: float = 15) -> ExtAuthorInfo | None:
    """Extracts authors and affiliations from the LaTeX source with the LLM. Returns None on failure."""
    arxiv_id = arxiv_metadata.arxiv_id
    _logger.info("AI fallback extraction using Ollama for %s", arxiv_id)

    text_input = llm_extraction.get_latex_metadata_windows(text_content)
    prompt = llm_extraction.build_prompt(llm_extraction.DEFAULT_PROMPT, text_input)

    try:
        parsed_data = llm_extraction.query_ollama(prompt, model_name, temperature=0.0,
                                                  timeout_seconds=timeout_seconds)
    except TimeoutError:
        _logger.error("Timeout: model %s took over %ss for %s. Skipping.", model_name, timeout_seconds, arxiv_id)
        return None
    except ValidationError as ve:
        _logger.error("JSON validation error for %s: %s", arxiv_id, ve)
        return None
    except Exception as e:
        _logger.error("Ollama extraction failed for %s: %s", arxiv_id, e)
        return None

    authors = [AIExtAuthor(name=a.name, affiliations=a.affiliations) for a in parsed_data.authors]
    if not authors:
        return None

    ext_results = [ExtResults(scheme_name="Ollama_AI_Fallback_Constrained", authors=authors, score=1.0)]
    return ExtAuthorInfo(ext_type="ai_fallback", extractions=ext_results)
