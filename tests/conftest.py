import json
import sys
import types
from pathlib import Path

import pytest

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

# Fake ROR registry used across tests: (ror_id, pre-processed name)
FAKE_ROR_ORGS = [
    ("https://ror.org/052gg0110", "university of oxford"),
    ("https://ror.org/05a28rw58", "eth zurich"),
    ("https://ror.org/02kkvpp62", "technical university of munich"),
]


class FakeRorOrg:
    def __init__(self, ror_id, name):
        self.ror_id = ror_id
        self.names = [name]


@pytest.fixture
def fake_ror():
    """Returns (ror_orgs, ror_orgs_dict) shaped like match_data's processed ROR dataset."""
    return FAKE_ROR_ORGS, {ror_id: FakeRorOrg(ror_id, name) for ror_id, name in FAKE_ROR_ORGS}


@pytest.fixture
def no_spacy(monkeypatch):
    """Replaces spaCy NER cleaning with the identity function so tests don't need the transformer model."""
    import approach1_spacy_ner
    monkeypatch.setattr(approach1_spacy_ner, "extract_org_name_with_spacy", lambda text: text)
    if hasattr(approach1_spacy_ner, "clear_caches"):
        approach1_spacy_ner.clear_caches()
        yield
        approach1_spacy_ner.clear_caches()
    else:
        yield


def make_metadata(names: list[str]) -> str:
    """arXiv/Kaggle metadata JSON for the given 'First Last' author names."""
    parsed = [[n.split()[-1], " ".join(n.split()[:-1]), ""] for n in names]
    return json.dumps({"title": "T", "authors_parsed": parsed, "categories": "math.CO"})
