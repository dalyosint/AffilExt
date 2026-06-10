# AffilExt: Scalable Author-Affiliation Extraction Pipeline

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Data](https://img.shields.io/badge/Data-Parquet-orange.svg)

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