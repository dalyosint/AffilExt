from approach1_spacy_ner import extract_org_name_with_spacy
from approach2_sbert import get_matched_affiliation_sbert


def get_matched_affiliation_hybrid(
        affiliation: str,
        research_orgs: list[tuple[str, str]]
) -> tuple[str, tuple[str, float]]:
    cleaned_affiliation = extract_org_name_with_spacy(affiliation)

    if not cleaned_affiliation.strip():
        cleaned_affiliation = affiliation

    _, (ror_id, score) = get_matched_affiliation_sbert(cleaned_affiliation, research_orgs)

    return affiliation, (ror_id, score)