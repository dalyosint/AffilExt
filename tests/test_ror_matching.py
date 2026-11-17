"""Matching extracted affiliations to ROR organizations (approach1_spacy_ner + match_data)."""
import approach1_spacy_ner as ner
import match_data
from conftest import FAKE_ROR_ORGS, make_metadata
from definition.data.Author import Author
from definition.data.ExtAuthorData import ExtAuthorInfo, ExtResults
from pipeline_parquet import parse_metadata


def test_matches_affiliation_with_department_noise(no_spacy):
    aff, (ror_id, score) = ner.get_matched_affiliation_spacy("Department of Physics, University of Oxford, UK",
                                                             FAKE_ROR_ORGS)
    assert aff == "Department of Physics, University of Oxford, UK"
    assert ror_id == "https://ror.org/052gg0110"
    assert score > 50


def test_results_are_cached_per_affiliation(no_spacy, monkeypatch):
    calls = []
    monkeypatch.setattr(ner, "extract_org_name_with_spacy", lambda text: calls.append(text) or text)
    for _ in range(3):
        ner.get_matched_affiliation_spacy("ETH Zurich", FAKE_ROR_ORGS)
    assert calls == ["ETH Zurich"]


def test_cache_resets_for_a_different_ror_dataset(no_spacy):
    other_orgs = [("https://ror.org/other", "eth zurich")]
    assert ner.get_matched_affiliation_spacy("ETH Zurich", FAKE_ROR_ORGS)[1][0] == "https://ror.org/05a28rw58"
    assert ner.get_matched_affiliation_spacy("ETH Zurich", other_orgs)[1][0] == "https://ror.org/other"


def test_spacy_skip_score_skips_ner_for_clear_matches(no_spacy, monkeypatch):
    calls = []
    monkeypatch.setattr(ner, "extract_org_name_with_spacy", lambda text: calls.append(text) or text)
    monkeypatch.setattr(ner, "SPACY_SKIP_SCORE", 90)
    ner.get_matched_affiliation_spacy("ETH Zurich", FAKE_ROR_ORGS)  # exact match -> no spaCy
    ner.get_matched_affiliation_spacy("Some Lab, Nowhere", FAKE_ROR_ORGS)  # weak match -> spaCy
    assert calls == ["Some Lab, Nowhere"]


def test_match_and_resolve_single_paper(no_spacy, fake_ror):
    ror_orgs, ror_orgs_dict = fake_ror
    meta = parse_metadata(make_metadata(["Alice Smith", "Bob Jones"]), "0000.00000")
    ext = ExtAuthorInfo(ext_type="test", extractions=[ExtResults(
        scheme_name="Test", score=1.0,
        authors=[Author("Alice Smith", ["University of Oxford"]), Author("Bob Jones", ["ETH Zurich"])])])

    result = match_data.match_and_resolve_single_paper(meta, ext, ror_orgs, ror_orgs_dict)

    assert result is not None
    assert len(result.matched_authors) == 2


def test_match_and_resolve_rejects_empty_input(fake_ror):
    ror_orgs, ror_orgs_dict = fake_ror
    assert match_data.match_and_resolve_single_paper(None, None, ror_orgs, ror_orgs_dict) is None
