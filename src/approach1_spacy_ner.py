"""
APPROACH 1: spaCy NER + RapidFuzz
==================================
Install dependencies:
    pip install spacy rapidfuzz
    python -m spacy download en_core_web_sm

How it works:
    1. Run the raw affiliation string through spaCy NER
    2. Extract only the ORG entities (e.g. "University of Cagliari")
    3. Pass the CLEANED name to RapidFuzz instead of the messy raw string
    4. This directly fixes the problem Frisch described on page 47

Plug-in point in your codebase: replace _get_matched_affiliation() in match_data.py
"""

import unicodedata
from rapidfuzz import fuzz, process, utils
import spacy
import re

# ---------------------------------------------------------------------------
# Load spaCy model once at module level (not inside the function!)
# This avoids reloading the model on every single call.
# ---------------------------------------------------------------------------
try:
    _nlp = spacy.load("en_core_web_sm")
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
    # (like zip codes or grant numbers)
    clean_string = re.sub(r'[^a-zA-Z\s]', '', combined_orgs)

    # Remove extra spaces
    clean_string = " ".join(clean_string.split())

    if not clean_string:
        return affiliation_string

    return clean_string


def _pre_process_string(string: str) -> str:
    """Normalise unicode and apply RapidFuzz default processing (lowercase, strip punctuation)."""
    normalized = unicodedata.normalize('NFD', string)
    return utils.default_process(normalized)


def _get_best_match(
        matches: list[tuple[str, float, int]],
        affiliation: str
) -> tuple[str, float, int]:
    """
    Re-rank the top partial_ratio matches using the full ratio() scorer.
    This avoids false positives where a short substring scores 100.
    (Same logic as original match_data.py)
    """
    best = ("", -1.0, -1)
    for match in matches:
        score = fuzz.ratio(match[0], affiliation)
        if score > best[1]:
            best = (match[0], score, match[2])
    return best


def get_matched_affiliation_spacy(
        affiliation: str,
        research_orgs: list[tuple[str, str]]  # list of (ror_id, preprocessed_name)
) -> tuple[str, tuple[str, float]]:
    """
    Match one affiliation string to the ROR dataset.

    Drop-in replacement for _get_matched_affiliation() in match_data.py

    Args:
        affiliation:     Raw extracted affiliation string from LaTeX
        research_orgs:   List of (ror_id, pre-processed org name) tuples

    Returns:
        (original_affiliation, (best_ror_id, score))
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


# ---------------------------------------------------------------------------
# Quick standalone test — run this file directly to verify it works
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        "Department of Mathematics, University of Cagliari, Via Ospedale 72, 09124 Cagliari, Italy",
        "Software Engineering, RWTH Aachen University, Germany",
        "Institute of Applied Physics and Computational Mathematics, P. O. Box 8009, Beijing, China, 100088",
        "Wireless Networking and Communications Group, Dept. of ECE, The University of Texas at Austin, TX 78712",
        "M. Smoluchowski Institute of Physics, Jagiellonian University, Kraków, Poland",
    ]

    print("=" * 60)
    print("APPROACH 1: spaCy NER Extraction Test")
    print("=" * 60)
    for raw in test_cases:
        cleaned = extract_org_name_with_spacy(raw)
        print(f"\n  RAW:     {raw}")
        print(f"  CLEANED: {cleaned}")
    print("\nIf CLEANED looks like a real institution name, Approach 1 is working.")