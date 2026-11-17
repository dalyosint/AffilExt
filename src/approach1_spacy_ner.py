"""
APPROACH 1: spaCy NER + RapidFuzz

Matches an extracted affiliation string to a ROR organization:
1. spaCy NER keeps only the organization names (drops addresses, cities, numbers, ...)
2. RapidFuzz finds the best matching ROR name.

Performance notes:
- The spaCy model is loaded lazily on first use (once per process).
- The list of ROR names is built once per ROR dataset instead of once per affiliation.
- Results are cached per affiliation string; the same institutions appear in thousands of papers.
- Optionally (SPACY_SKIP_SCORE) spaCy is skipped when the raw string already matches a ROR name well.
"""
import logging
import re
from functools import lru_cache

from rapidfuzz import fuzz, process

# Import the helper functions from match_data instead of duplicating them
from match_data import get_best_match, pre_process_string

_logger = logging.getLogger(__name__)

SPACY_MODEL = "en_core_web_trf"
_TOP_MATCHES_LIMIT = 10
_CACHE_SIZE = 200_000

# If set (0-100): first match the raw affiliation without spaCy and only run spaCy when the score is
# below this value. None (default) always runs spaCy, which reproduces the original behaviour exactly.
SPACY_SKIP_SCORE: float | None = None

_nlp = None
_current_orgs: list[tuple[str, str]] | None = None  # the ROR list the caches belong to
_current_org_names: list[str] = []


def _get_nlp():
    global _nlp
    if _nlp is None:
        import spacy
        try:
            _nlp = spacy.load(SPACY_MODEL)
        except OSError as e:
            raise RuntimeError(f"spaCy model not found. Run: python -m spacy download {SPACY_MODEL}") from e
        _logger.info("spaCy model '%s' loaded.", SPACY_MODEL)
    return _nlp


def extract_org_name_with_spacy(affiliation_string: str) -> str:
    """
    Combines all ORG entities found by spaCy and cleans the output.
    Returns the input unchanged if spaCy finds no organization.
    """
    doc = _get_nlp()(affiliation_string)

    org_entities = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    if not org_entities:
        return affiliation_string

    # Combine all found ORGs instead of picking the longest one
    combined_orgs = " ".join(org_entities)

    # Strip out numbers and punctuation that spaCy included, then collapse whitespace
    clean_string = re.sub(r'[^a-zA-Z\s]', '', combined_orgs)
    clean_string = " ".join(clean_string.split())

    return clean_string or affiliation_string


def clear_caches() -> None:
    """Forgets cached matches (e.g. after switching the ROR dataset or the matching settings)."""
    global _current_orgs, _current_org_names
    _current_orgs = None
    _current_org_names = []
    _match_cached.cache_clear()


def _use_ror_orgs(research_orgs: list[tuple[str, str]]) -> None:
    global _current_orgs, _current_org_names
    if research_orgs is not _current_orgs:
        clear_caches()
        _current_orgs = research_orgs
        _current_org_names = [org[1] for org in research_orgs]


def _fuzzy_match(preprocessed: str) -> tuple[str, float]:
    matches = process.extract(
        preprocessed,
        _current_org_names,
        scorer=fuzz.partial_ratio,
        limit=_TOP_MATCHES_LIMIT
    )
    best_match = get_best_match(matches, preprocessed)
    return _current_orgs[best_match[2]][0], best_match[1]


@lru_cache(maxsize=_CACHE_SIZE)
def _match_cached(affiliation: str) -> tuple[str, float]:
    if SPACY_SKIP_SCORE is not None:
        raw_match = _fuzzy_match(pre_process_string(affiliation))
        if raw_match[1] >= SPACY_SKIP_SCORE:
            return raw_match

    cleaned = extract_org_name_with_spacy(affiliation)
    return _fuzzy_match(pre_process_string(cleaned))


def get_matched_affiliation_spacy(
        affiliation: str,
        research_orgs: list[tuple[str, str]]
) -> tuple[str, tuple[str, float]]:
    """
    Matches one affiliation string to the ROR dataset using spaCy cleaning first.
    Returns (affiliation, (ror_id, score)).
    """
    _use_ror_orgs(research_orgs)
    return affiliation, _match_cached(affiliation)
