"""End-to-end behaviour of pipeline_parquet.process_single_paper (LLM and spaCy replaced by stubs)."""
import polars as pl
import pytest

import ai_fallback
import pipeline_parquet as pp
from conftest import make_metadata
from definition.data.Author import Author
from definition.data.ExtAuthorData import ExtAuthorInfo, ExtResults

GOOD_TEX = r"""\documentclass{article}
\author{Alice Smith\thanks{University of Oxford} \and Bob Jones\thanks{ETH Zurich}}
\begin{document}\maketitle\begin{abstract}A\end{abstract}\end{document}"""
NO_AUTHOR_TEX = r"\documentclass{article}\begin{document}No authors here.\end{document}"


@pytest.fixture
def pipeline(no_spacy, fake_ror, monkeypatch):
    ror_orgs, ror_orgs_dict = fake_ror
    monkeypatch.setattr(pp, "global_ror_orgs", ror_orgs)
    monkeypatch.setattr(pp, "global_ror_orgs_dict", ror_orgs_dict)
    ai_calls = []

    def fake_llm(text, meta, **kwargs):
        ai_calls.append(meta.arxiv_id)
        return None

    monkeypatch.setattr(ai_fallback, "extract_with_ollama", fake_llm)
    return ai_calls


def row(paper_id, tex, names=("Alice Smith", "Bob Jones")):
    return {"id": paper_id, "text": tex, "metadata": make_metadata(list(names))}


def test_rule_based_success_does_not_call_llm(pipeline):
    extracted, matched, ai, status, _, ai_used = pp.process_single_paper(row("1", GOOD_TEX))
    assert status == "success"
    assert extracted and matched and ai is None
    assert not ai_used and pipeline == []


def test_empty_extraction_falls_back_to_llm(pipeline):
    *_, status, _, ai_used = pp.process_single_paper(row("2", NO_AUTHOR_TEX))
    assert ai_used and pipeline == ["2"]
    assert status == "extraction_failed"


def test_low_author_similarity_falls_back_to_llm(pipeline):
    # LaTeX authors don't match the arXiv author list -> gate 1 fails
    *_, ai_used = pp.process_single_paper(row("3", GOOD_TEX, names=("Zhang Wei", "Maria Garcia")))
    assert ai_used and pipeline == ["3"]


def test_successful_llm_fallback_is_matched(pipeline, monkeypatch):
    def llm_success(text, meta, **kwargs):
        return ExtAuthorInfo(ext_type="ai_fallback", extractions=[ExtResults(
            scheme_name="AI", score=1.0,
            authors=[Author("Alice Smith", ["University of Oxford"]), Author("Bob Jones", ["ETH Zurich"])])])

    monkeypatch.setattr(ai_fallback, "extract_with_ollama", llm_success)
    extracted, matched, ai, status, _, ai_used = pp.process_single_paper(row("4", NO_AUTHOR_TEX))
    assert status == "success" and ai_used
    assert ai is not None and extracted == ai and matched


def test_broken_row_is_reported_not_raised(pipeline):
    *_, status, _, _ = pp.process_single_paper({"id": "5"})  # missing text/metadata
    assert status == "pipeline_error"


def test_parse_metadata_reads_kaggle_author_order():
    meta = pp.parse_metadata(make_metadata(["Alice Smith"]), "1")
    assert [a.name for a in meta.authors] == ["Alice Smith"]
    assert pp.parse_metadata("not json", "1") is None


def test_batches_with_all_null_results_can_be_merged(tmp_path):
    # Regression test: a batch whose result column is all None used to get the Null dtype,
    # which made the final scan_parquet merge fail with a SchemaError.
    for i, values in enumerate([[None, None], ['{"x": 1}', None]]):
        pl.DataFrame({"id": [f"a{i}", f"b{i}"]}).with_columns(
            pl.Series("ai_output", values, dtype=pp._RESULT_DTYPE)
        ).write_parquet(tmp_path / f"batch_{i}.parquet")

    merged = pl.scan_parquet(tmp_path / "*.parquet").collect()
    assert merged.height == 4


def test_main_end_to_end_with_resume(pipeline, fake_ror, monkeypatch, tmp_path):
    """Runs main() twice on a directory of shards: the second run must skip everything (resume)."""
    import concurrent.futures
    import json
    import sys

    import match_data

    ror_orgs, ror_orgs_dict = fake_ror
    monkeypatch.setattr(match_data, "get_ror_dataset", lambda: None)
    monkeypatch.setattr(match_data, "process_ror_orgs", lambda dataset: ror_orgs)
    monkeypatch.setattr(match_data, "process_ror_orgs_to_dict", lambda dataset: ror_orgs_dict)
    # threads instead of processes so the stubs above also apply inside the workers
    monkeypatch.setattr(concurrent.futures, "ProcessPoolExecutor", concurrent.futures.ThreadPoolExecutor)

    # a directory of shards, as produced by etl/build_arxiv_lake.py
    input_file = tmp_path / "lake"
    input_file.mkdir()
    output_file = tmp_path / "out.parquet"
    pl.DataFrame([row("good", GOOD_TEX)]).write_parquet(input_file / "shard_0000.parquet")
    pl.DataFrame([row("bad", NO_AUTHOR_TEX)]).write_parquet(input_file / "shard_0001.parquet")
    argv = ["pipeline_parquet.py", "-i", str(input_file), "-o", str(output_file),
            "--batch-dir", str(tmp_path / "batches"), "-w", "1", "-b", "1"]
    monkeypatch.setattr(sys, "argv", argv)

    pp.main()

    out = pl.read_parquet(output_file).sort("id")
    assert out["id"].to_list() == ["bad", "good"]
    assert out.filter(pl.col("id") == "good")["matched_info"][0] is not None
    assert out.filter(pl.col("id") == "bad")["matched_info"][0] is None

    summary = json.loads((tmp_path / "out.run_summary.json").read_text())
    assert summary["papers"]["processed_this_run"] == 2
    assert summary["papers"]["by_status"] == {"extraction_failed": 1, "success": 1}
    assert summary["llm_fallback"]["pushed"] == 1
    assert summary["settings"]["author_f1_threshold"] == pp.AUTHOR_F1_THRESHOLD

    pp.main()  # resume: nothing left to do
    summary = json.loads((tmp_path / "out.run_summary.json").read_text())
    assert summary["papers"]["processed_this_run"] == 0
    assert summary["papers"]["skipped_already_processed"] == 2
    assert pl.read_parquet(output_file).height == 2


def test_input_can_be_a_file_or_a_directory_of_shards(tmp_path):
    single = tmp_path / "one.parquet"
    pl.DataFrame([row("a", GOOD_TEX)]).write_parquet(single)
    shards = tmp_path / "lake"
    shards.mkdir()
    for name in ["shard_0001.parquet", "shard_0000.parquet"]:
        pl.DataFrame([row(name, GOOD_TEX)]).write_parquet(shards / name)

    assert pp._input_files(single) == [single]
    assert [f.name for f in pp._input_files(shards)] == ["shard_0000.parquet", "shard_0001.parquet"]
    assert pp._input_files(tmp_path / "missing.parquet") == []
    assert sum(b.num_rows for b in pp._iter_batches(pp._input_files(shards), batch_size=1)) == 2
