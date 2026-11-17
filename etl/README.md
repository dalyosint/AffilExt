# ETL: arXiv sources → Parquet lake

Stage 0 of AffilExt. These two scripts turn the complete arXiv LaTeX source corpus into a Parquet data lake,
the input of the extraction pipeline (`src/pipeline_parquet.py`). Developed together with my thesis supervisor.

```text
 Extract                                Transform                               Load
 ───────                                ─────────                               ────
 s3://arxiv/src/*.tar  ──download──>    drop images, PDFs, PostScript, ... ──>  *_onlytext.tar
 (requester-pays)        + MD5 check    inside every paper's .gz                       │
                                                                                       v
 arxiv-metadata-oai-snapshot.json ──────────────────────────────────────>  build_arxiv_lake.py
 (Kaggle)                                                                              │
                                                                                       v
                                                    arxiv_lake/shard_0000.parquet, shard_0001.parquet, ...
                                                    columns: id | text | categories | metadata
```

## 1. Download and filter: `download_arxiv_tex_src.py`

Downloads the arXiv bulk source tars from the requester-pays S3 bucket `arxiv` and filters them:

- Verifies every tar against the MD5 checksum in arXiv's manifest; corrupted downloads are deleted (unless `--keep-broken-files`).
- Removes loose binaries (PDF, PS/EPS, images, …) and, inside each paper's `.gz`, rebuilds the archive without them.
  Each tar gets an `_onlytext.csv` log of what was removed.
- Downloads in parallel (`--download-in-parallel N`) while one thread filters, with a bounded queue so
  downloads pause when filtering falls behind; aborts when less than 10 GB of disk space is left.
- Skips tars that were already processed, so an interrupted run can simply be restarted.

```bash
python download_arxiv_tex_src.py --dest ./rawdata --dry-run                       # show what would happen
python download_arxiv_tex_src.py --dest ./rawdata --download-in-parallel 8 \
       --download-everything-at-once --delete-unfiltered-tars
```

Without `--download-everything-at-once` only the first 4 tars are downloaded (a safety limit for testing).

**Requirements:** AWS credentials configured for boto3 (e.g. `aws configure`). The bucket is *requester-pays*:
the transfer is billed to your AWS account. See [arXiv bulk data access](https://info.arxiv.org/help/bulk_data_s3.html).

Other options: `--reprocess` (re-filter existing `_onlytext.tar` files, e.g. after changing the filter lists),
`--make-inventory` and `--warn-about-strange` (report file types that are neither known source nor known binary),
`--force-manifest` (re-download the manifest).

## 2. Build the lake: `build_arxiv_lake.py`

Reads every filtered tar and writes one row per paper:

| column | content |
|---|---|
| `id` | arXiv ID (old-style IDs such as `hep-ph/0209124` are restored from the bulk file name `hep-ph0209124.gz`) |
| `text` | all `.tex` files of the submission merged; the root file (with `\documentclass`/`\documentstyle`) first, files separated by `<\|FILE_SEP\|>` |
| `categories` | arXiv categories from the metadata snapshot |
| `metadata` | the raw metadata JSON line (authors, title, …); `{}` if the paper is not in the snapshot |

Both multi-file submissions (`.tar.gz`) and single-file submissions (a gzipped `.tex`) are supported.
Shards of 5000 papers are written with zstd compression.

```bash
python build_arxiv_lake.py --source-dir ./rawdata \
       --metadata arxiv-metadata-oai-snapshot.json --output-dir ./arxiv_lake
```

The metadata snapshot is available on [Kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv).
The script prints and logs (`arxiv_processing.log`) how many papers were written, had no TeX source,
or were missing from the metadata.

## 3. Run the extraction pipeline on the lake

```bash
cd ../src
python pipeline_parquet.py --input ../etl/arxiv_lake --output lake_processed.parquet --workers 8
```

The pipeline accepts the shard directory directly and streams it batch by batch.
