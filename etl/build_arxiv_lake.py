"""
Builds the "arXiv lake": Parquet shards with one row per paper, the input of src/pipeline_parquet.py.

Input:
    - the filtered arXiv source tars produced by download_arxiv_tex_src.py (*_onlytext.tar)
    - the Kaggle arXiv metadata snapshot (arxiv-metadata-oai-snapshot.json, one JSON object per line)
Output:
    - shard_0000.parquet, shard_0001.parquet, ... with the columns
      id, text (all .tex files of the paper merged, root file first), categories, metadata (raw JSON line)

USAGE:
python3 build_arxiv_lake.py --source-dir ./rawdata --metadata arxiv-metadata-oai-snapshot.json --output-dir ./arxiv_lake
"""
import argparse
import gzip
import io
import json
import logging
import re
import tarfile
from pathlib import Path
from typing import Any

import pandas as pd
from tqdm import tqdm

DEFAULT_CHUNK_SIZE = 5000
DEFAULT_PATTERN = "*_onlytext.tar"
FILE_SEPARATOR = "\n\n<|FILE_SEP|>\n\n"

# A file counts as the root (main) file if it starts a LaTeX document
_ROOT_MARKERS = (r"\documentclass", r"\documentstyle")
# Single-file submissions are stored as a gzipped .tex instead of a tar.gz
_TEX_MARKERS = _ROOT_MARKERS + (r"\begin{document}", r"\author", r"\title")
# Old-style IDs lose their slash in the bulk tars: hep-ph0209124 -> hep-ph/0209124
_OLD_STYLE_ID = re.compile(r"^([a-z-]+(?:\.[A-Z]{2})?)(\d{7}(?:v\d+)?)$")

logger = logging.getLogger("ArxivLake")


def setup_logging(log_file: Path) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8"), logging.StreamHandler()],
    )


def load_metadata_map(path: Path) -> dict[str, dict[str, str]]:
    logger.info("Loading metadata from %s...", path)
    if not path.exists():
        raise FileNotFoundError(f"Metadata file not found: {path}")

    meta_map = {}
    with path.open("r", encoding="utf-8") as f:
        for line in tqdm(f, desc="Indexing metadata"):
            try:
                doc = json.loads(line)
            except json.JSONDecodeError:
                continue
            pid = doc.get("id")
            if pid:
                meta_map[pid] = {"categories": doc.get("categories", ""), "metadata": line.strip()}
    return meta_map


def sanitize_string(s: str) -> str:
    """Removes surrogate characters that crash PyArrow/Parquet."""
    try:
        return s.encode("utf-8", "replace").decode("utf-8")
    except Exception:
        return "unknown_filename"


def paper_id_from_member(member_name: str) -> str:
    """'2301/2301.00001.gz' -> '2301.00001'"""
    return Path(sanitize_string(member_name)).name.removesuffix(".gz")


def resolve_metadata_id(pid: str, meta_map: dict) -> str:
    """Maps a bulk-tar file name to its metadata ID (restores the slash of old-style IDs)."""
    if pid in meta_map:
        return pid
    match = _OLD_STYLE_ID.match(pid)
    if match:
        old_style = f"{match.group(1)}/{match.group(2)}"
        if old_style in meta_map:
            return old_style
    return pid


def _is_root(text: str) -> bool:
    return any(marker in text for marker in _ROOT_MARKERS)


def _extract_from_tar(targz_bytes: bytes) -> str | None:
    with tarfile.open(fileobj=io.BytesIO(targz_bytes), mode="r:gz") as inner:
        tex_members = [m for m in inner.getmembers() if m.name.endswith(".tex") and m.isfile()]
        if not tex_members:
            return None

        root_content: str | None = None
        other_contents: list[str] = []

        for member in tex_members:
            try:
                f_obj = inner.extractfile(member)
                if f_obj is None:
                    continue
                text = f_obj.read().decode("utf-8", errors="replace")
                safe_member_name = sanitize_string(member.name)

                if root_content is None and _is_root(text):
                    root_content = f"% <|ROOT: {safe_member_name}|>\n{text}"
                else:
                    other_contents.append(f"% <|FILE: {safe_member_name}|>\n{text}")
            except Exception:
                continue

        full_text_list = ([root_content] if root_content else []) + other_contents
        return FILE_SEPARATOR.join(full_text_list) if full_text_list else None


def _extract_single_gz(gz_bytes: bytes, name: str) -> str | None:
    try:
        text = gzip.decompress(gz_bytes).decode("utf-8", errors="replace")
    except (OSError, EOFError):
        return None
    if not any(marker in text for marker in _TEX_MARKERS):
        return None  # not a TeX file (e.g. a gzipped PostScript)
    return f"% <|ROOT: {sanitize_string(name)}|>\n{text}"


def extract_merged_tex(gz_bytes: bytes, name: str = "main.tex") -> str | None:
    """All .tex files of one submission merged into one string, the root file first.

    Handles both multi-file submissions (.tar.gz) and single-file submissions (gzipped .tex).
    """
    try:
        return _extract_from_tar(gz_bytes)
    except (tarfile.TarError, OSError, EOFError):
        return _extract_single_gz(gz_bytes, name)


def _write_shard(buffer: list[dict[str, Any]], output_dir: Path, counter: int) -> None:
    out_file = output_dir / f"shard_{counter:04d}.parquet"
    pd.DataFrame(buffer).to_parquet(out_file, engine="pyarrow", compression="zstd")
    logger.info("Saved %s with %d records.", out_file, len(buffer))


def build_lake(source_dir: Path, metadata_path: Path, output_dir: Path,
               pattern: str = DEFAULT_PATTERN, chunk_size: int = DEFAULT_CHUNK_SIZE) -> dict[str, int]:
    """Builds the Parquet shards and returns counts for reporting."""
    output_dir.mkdir(parents=True, exist_ok=True)
    meta_map = load_metadata_map(metadata_path)

    outer_tars = sorted(source_dir.glob(pattern))
    logger.info("Found %d source tar files matching '%s'.", len(outer_tars), pattern)

    stats = {"papers_written": 0, "no_tex_found": 0, "missing_metadata": 0, "shards": 0}
    buffer: list[dict[str, Any]] = []

    for outer_path in tqdm(outer_tars, desc="Processing outer tars"):
        try:
            with tarfile.open(outer_path, "r") as outer:
                for member in outer:
                    if not member.name.endswith(".gz"):
                        continue

                    pid = resolve_metadata_id(paper_id_from_member(member.name), meta_map)
                    meta = meta_map.get(pid)
                    if meta is None:
                        stats["missing_metadata"] += 1
                        meta = {"categories": "", "metadata": "{}"}

                    f_obj = outer.extractfile(member)
                    if f_obj is None:
                        continue

                    text = extract_merged_tex(f_obj.read(), Path(member.name).name.removesuffix(".gz"))
                    if not text:
                        stats["no_tex_found"] += 1
                        continue

                    buffer.append({"id": pid, "text": text, "categories": meta["categories"],
                                   "metadata": meta["metadata"]})

                    if len(buffer) >= chunk_size:
                        try:
                            _write_shard(buffer, output_dir, stats["shards"])
                            stats["papers_written"] += len(buffer)
                            stats["shards"] += 1
                        except Exception as save_err:
                            # Clear the buffer anyway, otherwise every following paper fails too
                            logger.critical("CRITICAL SAVE ERROR: %s. Dropping buffer of %d items to recover.",
                                            save_err, len(buffer))
                        buffer = []

        except Exception as e:
            logger.error("Error processing %s: %s", outer_path.name, sanitize_string(str(e)))
            continue

    if buffer:
        try:
            _write_shard(buffer, output_dir, stats["shards"])
            stats["papers_written"] += len(buffer)
            stats["shards"] += 1
        except Exception as e:
            logger.error("Failed final flush: %s", e)

    logger.info("Done: %s", stats)
    return stats


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build Parquet shards (id, text, categories, metadata) "
                                                 "from filtered arXiv source tars.")
    parser.add_argument("--source-dir", type=Path, required=True,
                        help="Directory with the tars from download_arxiv_tex_src.py")
    parser.add_argument("--metadata", type=Path, required=True,
                        help="Kaggle arxiv-metadata-oai-snapshot.json")
    parser.add_argument("--output-dir", type=Path, required=True, help="Where the Parquet shards are written")
    parser.add_argument("--pattern", default=DEFAULT_PATTERN,
                        help="Glob for the source tars. Default: %(default)s (the filtered tars; '*.tar' would "
                             "also read unfiltered originals and duplicate papers)")
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE, help="Papers per shard. Default: %(default)s")
    parser.add_argument("--log-file", type=Path, default=Path("arxiv_processing.log"), help="Default: %(default)s")
    args = parser.parse_args(argv)

    setup_logging(args.log_file)
    build_lake(args.source_dir, args.metadata, args.output_dir, args.pattern, args.chunk_size)


if __name__ == "__main__":
    main()
