# Experiments

Research scripts used to choose and tune the settings of the hybrid pipeline in `src/pipeline_parquet.py`.
They are not part of the pipeline itself. Each script reads its input files from the current working
directory, so run them from the folder that contains the data (data files are git-ignored).

| Script | Purpose | Inputs | Outputs |
|---|---|---|---|
| `experiment_llm.py` | Benchmarks LLMs (phi3, gemma2, qwen2.5), prompts and temperatures for the LLM fallback | `math_500.parquet` | `ai_experiment_results_final.json`, `prompt_benchmark_summary.csv` |
| `plot_ablation.py` | Plots the temperature ablation of the Qwen runs | `QwenT0/T3/T7.json`, `QwenT0/T3/T7.csv` | interactive Plotly chart |
| `analyze_thresholds.py` | Tunes the author-matching method and thresholds (Gate 1) | `QwenT0.json`, `math_100.parquet` | printed comparison |
| `evaluate_ner_impact.py` | Measures how many failed ROR matches spaCy NER rescues | `first_100_failed_matches.parquet`, ROR dataset | printed report |
| `analyze_results.py` | Exports failure scenarios from a pipeline run for inspection | `math_sample_processed_final.parquet` | `scenario_*.csv` |

Example:

```bash
cd experiments
python experiment_llm.py
```

Scripts that use pipeline code (`experiment_llm.py`, `analyze_thresholds.py`, `evaluate_ner_impact.py`)
add `src/` to the import path themselves.
