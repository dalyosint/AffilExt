# AffilExt: Scalable Author-Affiliation Extraction Pipeline

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Data](https://img.shields.io/badge/Data-Parquet-orange.svg)
![tests](https://github.com/dalyosint/AffilExt/actions/workflows/tests.yml/badge.svg)

## 📌 Overview
AffilExt is a high-performance data pipeline designed to extract complex author-affiliation metadata from unstructured LaTeX source files. Built to process the entire arXiv pre-print corpus, this system bridges the data availability gap by parsing terabytes of raw text into a structured, queryable knowledge graph.

To balance extraction fidelity with computational constraints, AffilExt utilizes a **Cost-Optimized Hybrid Architecture**:
1. **High-Speed Deterministic Parsing:** A highly optimized, rule-based extraction engine processes standard formatting at scale.
2. **Validation Gate:** Extracted metadata undergoes consistency checks to flag malformed or ambiguous outputs.
3. **Selective LLM Augmentation:** Only failed edge-cases are routed to a Large Language Model (LLM) for targeted data repair and institutional name normalization, drastically reducing API costs compared to processing the full corpus.

## 🏗️ System Architecture

```text
[Raw Data]       [Stage 1: Rule-Based]      [Stage 2: Validation]       [Stage 3: Hybrid LLM]       [Output]

 arXiv S3   ──>  Regex Extractor      ──>   Consistency Checks   ──>   (Pass) ───────────────┐
   or                  │                           │                                         v
 Kaggle             (Fast)                  (Missing Data?)        (Fail) ──> LLM API ──> Parquet Storage
                                                                              (Repair)       │
                                                                                             v
                                                                                   Social Graph Generation
```

## 📂 Project Structure

```text
src/
├── main.py                 # Original per-paper pipeline: download → extract → match (files under data/)
├── pipeline_parquet.py     # Hybrid pipeline over a Parquet corpus (rule-based + LLM fallback, resumable)
├── download.py, ArxivAPI.py# arXiv API / Kaggle metadata import and LaTeX source download
├── ror_dl.py               # Downloads and minimizes the ROR (Research Organization Registry) dataset
├── extract_cmds.py         # Finds author/affiliation LaTeX commands in the source
├── extract_author_aff.py   # Rule-based parsing of those commands into authors + affiliations
├── definition/             # Parsing schemes (one per LaTeX author style) and data classes
├── match_data.py           # Matches affiliations to ROR organizations (RapidFuzz + spaCy NER)
├── ai_fallback.py          # LLM fallback for papers where rule-based extraction fails
├── llm_extraction.py       # Shared LLM parts: response schema, prompts, LaTeX windowing, Ollama call
├── author_matching.py      # Fuzzy author-name comparison (F1 quality gate)
├── graph_analysis.py       # Institution collaboration graph + Louvain community detection
└── scripts/                # Stats and manual-evaluation tools for the file-based pipeline (main.py)

experiments/                # Research scripts used to pick the LLM, prompts and thresholds (see experiments/README.md)
tests/                      # pytest suite
```

## ⚙️ Installation

Requires Python 3.12+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_trf   # NER model used for ROR matching in pipeline_parquet.py
```

The LLM fallback needs a running [Ollama](https://ollama.com) server with the model pulled:

```bash
ollama pull qwen2.5:0.5b
```

## 🚀 Usage

Run all commands from the `src/` directory.

### Hybrid Parquet pipeline

Input: a Parquet file with the columns `id`, `text` (full LaTeX source) and `metadata` (arXiv metadata JSON).

```bash
python pipeline_parquet.py --input math_subset.parquet --output math_sample_processed_final.parquet --workers 4
```

Results are checkpointed into `processed_batches/` after every batch. If a run is interrupted,
rerun the same command and already processed papers are skipped. The final file adds the columns
`extracted_info`, `matched_info` and `ai_output` (JSON strings). See `python pipeline_parquet.py -h` for all options.

Every run also writes `<output>.run_summary.json` with the settings (thresholds, LLM model and prompt, window sizes,
spaCy model), the git commit, the number of papers per status, LLM fallback counts and per-paper timings.

`--spacy-skip-score N` skips spaCy NER for affiliations that already match a ROR name with a score of at least `N`.
This is faster but can change results; by default spaCy always runs.

### Original file-based pipeline

```bash
python main.py all -c cs.SE -r 200          # download via arXiv API, then extract and match
python main.py all -c cs.SE -k arxiv.json   # use the Kaggle arXiv metadata dump instead of the API
python main.py extract                      # only re-run extraction on already downloaded papers
```

Data is stored under `data/` (papers, ROR dataset, stats).

### Tests and linting

```bash
pip install -r requirements-dev.txt
pytest          # spaCy and Ollama are stubbed, no models or data needed
ruff check .
```

Both also run on GitHub Actions for every push. Known gaps of the rule-based parser are listed as `xfail`
tests in `tests/test_rule_based_extraction.py`.

### Graph analysis

```bash
python graph_analysis.py math_sample_processed_final.parquet
```

## 🙏 Based On

This project builds on the original **AffilExt** by [Frylen](https://github.com/Frylen) (initial version, December 2024),
which provided the file-based pipeline: arXiv/Kaggle download (`main.py`, `download.py`, `ArxivAPI.py`),
the rule-based LaTeX command extraction and parsing schemes (`extract_cmds.py`, `extract_author_aff.py`, `definition/`),
ROR matching (`match_data.py`, `ror_dl.py`) and the analysis tools in `src/scripts/`.

Developed in this bachelor thesis on top of that base:
- Scalable Parquet pipeline with multiprocessing and crash-resumable checkpoints (`pipeline_parquet.py`)
- Quality gate on author similarity and selective LLM fallback via Ollama (`ai_fallback.py`, `llm_extraction.py`, `author_matching.py`)
- spaCy NER–assisted ROR matching (`approach1_spacy_ner.py`)
- Institution collaboration graph and community detection (`graph_analysis.py`)
- LLM, prompt, temperature and threshold experiments (`experiments/`)
