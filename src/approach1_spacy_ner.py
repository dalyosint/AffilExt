"""
APPROACH 1: spaCy NER + RapidFuzz
"""

import spacy
import re
from rapidfuzz import fuzz, process

# Import the helper functions from match_data instead of duplicating them
from match_data import _pre_process_string, _get_best_match

try:
    _nlp = spacy.load("en_core_web_trf")
    print("[Approach 1] spaCy model loaded successfully.")
except OSError:
    raise RuntimeError(
        "spaCy model not found. Run: python -m spacy download en_core_web_sm"
    )

_TOP_MATCHES_LIMIT = 10


def extract_org_name_with_spacy(affiliation_string: str) -> str:
    """
    Smarter spaCy extraction: Combines all ORG entities and cleans the output.
    """
    doc = _nlp(affiliation_string)

    # Extract all ORG entities
    org_entities = [ent.text for ent in doc.ents if ent.label_ == "ORG"]

    if not org_entities:
        return affiliation_string

    # FIX 1: Combine all found ORGs instead of picking the longest one
    combined_orgs = " ".join(org_entities)

    # FIX 2: Strip out numbers and weird punctuation that spaCy accidentally included
    clean_string = re.sub(r'[^a-zA-Z\s]', '', combined_orgs)

    # Remove extra spaces
    clean_string = " ".join(clean_string.split())

    if not clean_string:
        return affiliation_string

    return clean_string


def get_matched_affiliation_spacy(
        affiliation: str,
        research_orgs: list[tuple[str, str]]
) -> tuple[str, tuple[str, float]]:
    """
    Match one affiliation string to the ROR dataset using spaCy cleaning first.
    """
    # ---- STEP 1: Use spaCy to extract just the institution name ----
    cleaned = extract_org_name_with_spacy(affiliation)

    # ---- STEP 2: Pre-process for RapidFuzz ----
    org_names = [org[1] for org in research_orgs]
    preprocessed = _pre_process_string(cleaned)

    # ---- STEP 3: Fuzzy match the CLEAN name (not the raw string) ----
    matches = process.extract(
        preprocessed,
        org_names,
        scorer=fuzz.partial_ratio,
        limit=_TOP_MATCHES_LIMIT
    )

    best_match = _get_best_match(matches, preprocessed)
    return affiliation, (research_orgs[best_match[2]][0], best_match[1])