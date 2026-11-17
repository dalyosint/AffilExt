"""etl/build_arxiv_lake.py: arXiv bulk source tars + metadata snapshot -> Parquet shards."""
import gzip
import io
import json
import sys
import tarfile
from pathlib import Path

import polars as pl
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "etl"))
import build_arxiv_lake as lake  # noqa: E402

MAIN_TEX = r"\documentclass{article}\author{Alice Smith\thanks{Oxford}}\begin{document}\input{sec}\end{document}"
SECTION_TEX = r"\section{Intro} Text."


def tar_gz(files: dict[str, str]) -> bytes:
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as tar:
        for name, content in files.items():
            data = content.encode()
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
    return buffer.getvalue()


def add_bytes(tar: tarfile.TarFile, name: str, data: bytes) -> None:
    info = tarfile.TarInfo(name)
    info.size = len(data)
    tar.addfile(info, io.BytesIO(data))


def test_multi_file_submission_puts_root_first():
    text = lake.extract_merged_tex(tar_gz({"a_sec.tex": SECTION_TEX, "main.tex": MAIN_TEX, "fig.png": "x"}))
    parts = text.split(lake.FILE_SEPARATOR)
    assert parts[0].startswith("% <|ROOT: main.tex|>")
    assert parts[1].startswith("% <|FILE: a_sec.tex|>")
    assert len(parts) == 2  # non-.tex files are ignored


def test_single_file_submission_is_not_dropped():
    text = lake.extract_merged_tex(gzip.compress(MAIN_TEX.encode()), "2301.00002")
    assert text == f"% <|ROOT: 2301.00002|>\n{MAIN_TEX}"


def test_gzipped_non_tex_and_garbage_are_skipped():
    assert lake.extract_merged_tex(gzip.compress(b"%!PS-Adobe-2.0 binary stuff")) is None
    assert lake.extract_merged_tex(b"not even gzip") is None


def test_latex209_documentstyle_counts_as_root():
    old = r"\documentstyle{article}\begin{document}x\end{document}"
    assert lake.extract_merged_tex(tar_gz({"z.tex": SECTION_TEX, "a.tex": old})).startswith("% <|ROOT: a.tex|>")


@pytest.mark.parametrize("pid, expected", [
    ("2301.00001", "2301.00001"),
    ("hep-ph0209124", "hep-ph/0209124"),
    ("math.GT0309136", "math.GT/0309136"),
    ("9999.99999", "9999.99999"),  # unknown IDs are kept as they are
])
def test_resolve_metadata_id(pid, expected):
    meta = {"2301.00001": {}, "hep-ph/0209124": {}, "math.GT/0309136": {}}
    assert lake.resolve_metadata_id(pid, meta) == expected


def test_build_lake_end_to_end(tmp_path):
    source = tmp_path / "rawdata"
    source.mkdir()
    with tarfile.open(source / "arXiv_src_2301_001_onlytext.tar", "w") as outer:
        add_bytes(outer, "2301/2301.00001.gz", tar_gz({"main.tex": MAIN_TEX, "sec.tex": SECTION_TEX}))
        add_bytes(outer, "2301/2301.00002.gz", gzip.compress(MAIN_TEX.encode()))
        add_bytes(outer, "2301/hep-ph0209124.gz", gzip.compress(MAIN_TEX.encode()))
        add_bytes(outer, "2301/2301.00003.gz", gzip.compress(b"%!PS-Adobe binary"))
        add_bytes(outer, "2301/2301.00004.gz", gzip.compress(MAIN_TEX.encode()))  # no metadata
        add_bytes(outer, "2301/2301.00005.pdf", b"%PDF")
    # an unfiltered original next to it must not be read by default (it would duplicate papers)
    with tarfile.open(source / "arXiv_src_2301_001.tar", "w") as original:
        add_bytes(original, "2301/2301.00001.gz", tar_gz({"main.tex": MAIN_TEX}))

    metadata = tmp_path / "snapshot.json"
    metadata.write_text("\n".join(json.dumps({"id": pid, "categories": "math.CO"})
                                  for pid in ["2301.00001", "2301.00002", "hep-ph/0209124", "2301.00003"]))

    stats = lake.build_lake(source, metadata, tmp_path / "lake", chunk_size=2)

    shards = sorted((tmp_path / "lake").glob("shard_*.parquet"))
    assert [s.name for s in shards] == ["shard_0000.parquet", "shard_0001.parquet"]
    df = pl.read_parquet(shards)
    assert df.columns == ["id", "text", "categories", "metadata"]
    assert df["id"].to_list() == ["2301.00001", "2301.00002", "hep-ph/0209124", "2301.00004"]
    assert df.filter(pl.col("id") == "hep-ph/0209124")["categories"][0] == "math.CO"
    assert df.filter(pl.col("id") == "2301.00004")["metadata"][0] == "{}"
    assert stats == {"papers_written": 4, "no_tex_found": 1, "missing_metadata": 1, "shards": 2}
