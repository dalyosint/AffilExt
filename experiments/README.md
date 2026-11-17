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
python experiment_llm.py -h      # all options: input, number of papers, models, prompts, temperatures, window sizes
```

## Re-running the LLM benchmark

Results produced before November 2026 were affected by bugs that changed what the models received
(prompt without the JSON schema, doubled braces in the Super prompt examples, head window not cut at `\section`,
`"phi3:mini "` model name with a trailing space). Re-run the benchmark before reporting numbers:

```bash
ollama pull phi3:mini && ollama pull gemma2:2b && ollama pull qwen2.5:0.5b
cd experiments
python experiment_llm.py -i math_500.parquet --results results_v2.jsonl --final-json results_v2.json
```

- Use a **new** `--results` file; an existing file's runs are treated as done and skipped (that is how resuming works).
- If the run is interrupted, run the same command again; it continues where it stopped.
- `results_v2.config.json` records the exact settings and git commit used.
- `prompt_benchmark_summary.csv` holds average F1, precision, recall, valid-JSON rate and time per model/prompt/temperature,
  computed over all records in the results file.
- To reproduce the earlier window size or try the pipeline's, pass `--head-chars/--tail-chars`
  (experiment default 5000/1000, pipeline default 10000/2000).

Scripts that use pipeline code (`experiment_llm.py`, `analyze_thresholds.py`, `evaluate_ner_impact.py`)
add `src/` to the import path themselves.
