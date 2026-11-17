"""experiments/experiment_llm.py runs, resumes and evaluates all records (Ollama replaced by a stub)."""
import importlib.util
import json
import sys
from pathlib import Path

import polars as pl

import llm_extraction
from conftest import make_metadata

EXPERIMENT = Path(__file__).resolve().parent.parent / "experiments" / "experiment_llm.py"
TEX = r"\documentclass{article}\author{Alice Smith\thanks{Oxford}}\begin{document}\end{document}"


def load_experiment():
    spec = importlib.util.spec_from_file_location("experiment_llm", EXPERIMENT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_experiment_runs_resumes_and_evaluates_all_records(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)  # the summary CSV is written to the working directory
    calls = []

    def fake_query(prompt, model_name, temperature, timeout_seconds):
        calls.append((model_name, temperature))
        return llm_extraction.ExtractionResponse(authors=[{"name": "Alice Smith", "affiliations": ["Oxford"]}])

    monkeypatch.setattr(llm_extraction, "query_ollama", fake_query)
    exp = load_experiment()

    pl.DataFrame([{"id": f"p{i}", "text": TEX, "metadata": make_metadata(["Alice Smith"])} for i in range(2)]
                 ).write_parquet(tmp_path / "in.parquet")
    base_args = ["experiment_llm.py", "-i", "in.parquet", "--models", "m1", "--prompts", "Constrained_Prompt",
                 "--results", "res.jsonl", "--final-json", "final.json"]

    # first session: one temperature
    monkeypatch.setattr(sys, "argv", base_args + ["--temperatures", "0.0"])
    exp.main()
    assert len(calls) == 2

    # resumed session: adds a second temperature, must not redo the first one
    monkeypatch.setattr(sys, "argv", base_args + ["--temperatures", "0.0", "0.7"])
    exp.main()
    assert calls[2:] == [("m1", 0.7), ("m1", 0.7)]

    records = json.loads((tmp_path / "final.json").read_text())
    assert len(records) == 4  # includes the records of the first session
    assert all(r["ai_author_f1"] == 1.0 for r in records)
    summary = pl.read_csv(tmp_path / "prompt_benchmark_summary.csv")
    assert summary.height == 2  # one row per (model, prompt, temperature)
    assert json.loads((tmp_path / "res.config.json").read_text())["temperatures"] == [0.0, 0.7]
