"""Rule-based extraction of authors and affiliations from LaTeX (extract_cmds + extract_author_aff)."""
import pytest

import extract_author_aff
import extract_cmds
import match_data
from conftest import make_metadata
from pipeline_parquet import parse_metadata

AUTHORS = ["Alice Smith", "Bob Jones"]
EXPECTED = [("Alice Smith", ["University of Oxford"]), ("Bob Jones", ["ETH Zurich"])]


def extract(tex: str, names=AUTHORS):
    meta = parse_metadata(make_metadata(names), "0000.00000")
    info = extract_author_aff.extract_affiliations_from_obj(extract_cmds.extract_cmds_from_string(tex), meta)
    if not info or not info.extractions:
        return None
    best = match_data.get_best_extraction(info.extractions)
    return [(a.name, a.affiliations) for a in best.authors]


def test_thanks_footnotes():
    tex = r"""\documentclass{article}
\title{T}
\author{Alice Smith\thanks{University of Oxford} \and Bob Jones\thanks{ETH Zurich}}
\begin{document}\maketitle\end{document}"""
    assert extract(tex) == EXPECTED


def test_revtex_author_affiliation_pairs():
    tex = r"""\documentclass{revtex4}
\begin{document}
\author{Alice Smith}
\affiliation{University of Oxford}
\author{Bob Jones}
\affiliation{ETH Zurich}
\maketitle
\end{document}"""
    assert extract(tex) == EXPECTED


def test_document_without_authors_gives_nothing():
    assert extract(r"\documentclass{article}\begin{document}Hello\end{document}") is None


# --- Known gaps of the rule-based parser. These papers are currently handled by the LLM fallback. ---
# Remove the xfail marker once the corresponding scheme is implemented.

@pytest.mark.xfail(reason="No multi-command schemes exist (definition/multi_cmd_scheme is empty)", strict=True)
def test_authblk_numbered_affil():
    tex = r"""\documentclass{article}
\usepackage{authblk}
\author[1]{Alice Smith}
\author[2]{Bob Jones}
\affil[1]{University of Oxford}
\affil[2]{ETH Zurich}
\begin{document}\maketitle\end{document}"""
    assert extract(tex) == EXPECTED


@pytest.mark.xfail(reason="No multi-command schemes exist (definition/multi_cmd_scheme is empty)", strict=True)
def test_elsarticle_labelled_address():
    tex = r"""\documentclass{elsarticle}
\begin{document}
\begin{frontmatter}
\author[a]{Alice Smith}
\author[b]{Bob Jones}
\address[a]{University of Oxford}
\address[b]{ETH Zurich}
\end{frontmatter}
\end{document}"""
    assert extract(tex) == EXPECTED


@pytest.mark.xfail(reason="AuthorAddress scheme only returns the first author/address pair", strict=True)
def test_amsart_author_address_pairs():
    tex = r"""\documentclass{amsart}
\begin{document}
\author{Alice Smith}
\address{University of Oxford}
\author{Bob Jones}
\address{ETH Zurich}
\maketitle
\end{document}"""
    assert extract(tex) == EXPECTED


@pytest.mark.xfail(reason=r"Institute scheme ignores \inst{n} markers and leaks 'author' into the first name",
                   strict=True)
def test_llncs_institute_with_inst_markers():
    tex = r"""\documentclass{llncs}
\begin{document}
\author{Alice Smith\inst{1} \and Bob Jones\inst{2}}
\institute{University of Oxford \and ETH Zurich}
\maketitle
\end{document}"""
    assert extract(tex) == EXPECTED
