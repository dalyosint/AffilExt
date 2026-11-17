#! /usr/bin/env python3

"""
This is an ETL script to download all arXiv source files from a requester-pays AWS S3 bucket.
It performs "Surgical Filtering" on the data:
1. Loose PDF/Image files in the main tar are removed.
2. .gz archives inside the main tar are inspected.
   - If they contain images/binaries, they are unzipped in-memory, stripped of those files, and re-zipped.
   - If they are clean, they are copied essentially untouched.

DEPENDENCIES:
boto3[crt]>=1.20.0
tqdm

Python 3.11+ is recommended for performance.

USAGE:
python3 download_arxiv_tex_src.py --dest ./ --reprocess --warn-about-strange --download-in-parallel 8
"""

import sys
import tarfile
import hashlib
import csv
import argparse
import xml.etree.ElementTree as ET
import shutil
import logging
import time
import os
import boto3
import io
import gzip
import threading
import queue
import concurrent.futures
from botocore.exceptions import ClientError
from pathlib import Path
from typing import Dict, Optional, Tuple, List, NamedTuple
from dataclasses import dataclass
from datetime import datetime

from tqdm import tqdm

# --- CONSTANTS & CONFIGURATION ---
BUCKET_NAME = "arxiv"
MANIFEST_KEY = "src/arXiv_src_manifest.xml"
DEFAULT_DESTINATION = Path("./rawdata/")
MIN_FREE_SPACE_GB = 10
TAR_BLOCK_SIZE = 512
CHUNK_SIZE = 4096 * 1024  # 4MB

# --- FILTER CONFIGURATION ---
EXTENSIONS_TO_REMOVE = { # non-tex-source files we know of, mostly images
    '.pdf', '.ps', '.eps', '.epsf', '.epsi', '.eps~', '.epsx',
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ppt',
    '.tif', '.tiff', '.svg', '.fig', '.pstex', '.pstex_t', '.dot',
    '.fd', '.cfg', '.toc', '.prn', '.log', '.idx', '.xxx', '.out', '.aux',
    '.avi',
    'thumbs.db'
}

EXTENSIONS_EXPECTED_SOURCE = { # tex sources or similar we like to keep for sure
    '.tex', '.sty', '.cls', '.bbl', '.txt', '.md', '.ipynb',
    '.bib', '.bst', '.def', '.inc', '.ltx', '.gls', '.clo', '.dtx', '.ins',
    '.cry' # this seems to be some kind of compression used for tex files in the days back then ...
}

logger = logging.getLogger("ArXivETL")

# --- DATA STRUCTURES ---

@dataclass
class TransformationStats:
    original_size: int  # Size of the INPUT file (local)
    cleaned_size: int   # Size of the OUTPUT file (local)
    bytes_removed: int  # Uncompressed bytes removed

    @property
    def disk_saved(self) -> int:
        return self.original_size - self.cleaned_size

class ManifestEntry(NamedTuple):
    md5: str
    size: int

class ProcessingContext(NamedTuple):
    filename: str
    expected_md5: str
    s3_size: int          # The size of the original file on AWS
    original_path: Path
    cleaned_path: Path
    csv_log_path: Path
    inventory_csv_path: Path

# --- LOGGING UTILITIES ---

class TqdmLoggingHandler(logging.Handler):
    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)
        except Exception:
            self.handleError(record)

def setup_logging(dest_dir: Path, dry_run: bool) -> None:
    handlers = []
    tqdm_handler = TqdmLoggingHandler()
    tqdm_handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    handlers.append(tqdm_handler)

    if not dry_run or dest_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)
        log_file = dest_dir / "arxiv_etl.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
        handlers.append(file_handler)

    logging.basicConfig(level=logging.INFO, handlers=handlers)

# --- SYSTEM CHECKS ---

def check_disk_space(folder: Path) -> None:
    if not folder.exists(): return
    try:
        total, used, free = shutil.disk_usage(folder)
        free_gb = free // (2**30)
        if free_gb < MIN_FREE_SPACE_GB:
            logger.critical(f"Low disk space! Only {free_gb}GB remaining. Aborting.")
            sys.exit(1)
    except FileNotFoundError:
        pass

# --- CORE LOGIC ---

def get_s3_metadata(s3_client, key: str) -> Optional[dict]:
    try:
        return s3_client.head_object(Bucket=BUCKET_NAME, Key=key, RequestPayer='requester')
    except ClientError:
        return None

def get_manifest_data(local_path: Path, force_refresh: bool = False) -> Dict[str, ManifestEntry]:
    """Parses XML to get MD5 AND File Size."""
    s3 = boto3.client('s3')
    should_download = False
    meta = get_s3_metadata(s3, MANIFEST_KEY)

    if meta:
        remote_mtime = meta['LastModified'].timestamp()
        if not local_path.exists() or local_path.stat().st_size == 0:
            logger.info("Manifest missing/empty. Downloading...")
            should_download = True
        elif force_refresh:
            should_download = True
        else:
            local_mtime = local_path.stat().st_mtime
            if remote_mtime > local_mtime + 1.0:
                local_dt = datetime.fromtimestamp(local_mtime).strftime('%Y-%m-%d')
                remote_dt = datetime.fromtimestamp(remote_mtime).strftime('%Y-%m-%d')
                logger.info(f"Manifest S3 newer ({remote_dt} vs {local_dt}). Updating...")
                should_download = True
            else:
                logger.info("Local manifest is up-to-date.")

    if should_download:
        try:
            s3.download_file(Bucket=BUCKET_NAME, Key=MANIFEST_KEY, Filename=str(local_path), ExtraArgs={'RequestPayer': 'requester'})
            if meta:
                mtime = meta['LastModified'].timestamp()
                os.utime(local_path, (mtime, mtime))
        except Exception as e:
            logger.error(f"Manifest download failed: {e}")
            sys.exit(1)

    try:
        tree = ET.parse(local_path)
    except ET.ParseError:
        logger.error("XML Parse Error.")
        sys.exit(1)

    manifest = {}
    for file_elem in tree.getroot().findall("file"):
        n = file_elem.find("filename")
        m = file_elem.find("md5sum")
        s = file_elem.find("size")

        if n is not None and m is not None and s is not None:
            if n.text and m.text and s.text:
                clean_name = Path(n.text).name
                manifest[clean_name] = ManifestEntry(md5=m.text, size=int(s.text))
    return manifest

def download_artifact(filename: str, dest_path: Path, dry_run: bool, disable_pbar: bool = False) -> bool:
    if dest_path.exists(): return True
    if dry_run:
        logger.info(f"[DRY-RUN] Download {filename}")
        return True

    # Initialize boto3 client inside thread to ensure thread safety
    s3 = boto3.client('s3')
    key = f"src/{filename}"
    try:
        meta = s3.head_object(Bucket=BUCKET_NAME, Key=key, RequestPayer='requester')
        # Only show inner progress bar if not running many parallel tasks
        with tqdm(total=meta['ContentLength'], unit='B', unit_scale=True, desc="Downloading", leave=False, disable=disable_pbar) as pbar:
            s3.download_file(
                Bucket=BUCKET_NAME, Key=key, Filename=str(dest_path),
                ExtraArgs={'RequestPayer': 'requester'},
                Callback=lambda b: pbar.update(b)
            )
        mtime = meta['LastModified'].timestamp()
        os.utime(dest_path, (mtime, mtime))
        return True
    except Exception as e:
        logger.error(f"Download error {filename}: {e}")
        if dest_path.exists(): dest_path.unlink()
        return False

def verify_artifact(path: Path, expected_md5: str, dry_run: bool, disable_pbar: bool = False) -> bool:
    if dry_run: return True
    md5 = hashlib.md5()
    with path.open("rb") as f:
        with tqdm(total=path.stat().st_size, unit='B', unit_scale=True, desc="Verifying MD5", leave=False, disable=disable_pbar) as pbar:
            for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
                md5.update(chunk)
                pbar.update(len(chunk))
    if md5.hexdigest() != expected_md5:
        logger.error(f"MD5 Mismatch: {path.name}")
        return False
    return True

# --- THE SURGICAL TRANSFORM LOGIC ---

def process_inner_gz(member_name: str, fileobj, remove_log: list, inventory_log: list,
                     make_inventory: bool, warn_strange: bool) -> Tuple[bool, Optional[bytes], int]:
    """
    Inspects a .gz file.
    Returns: (was_modified, new_gz_bytes, bytes_removed)
    """
    fileobj.seek(0)
    files_to_remove = []

    try:
        # Pass 1: Inspection
        with tarfile.open(fileobj=fileobj, mode='r|gz') as inner_tar:
            for inner_member in inner_tar:
                ext = Path(inner_member.name).suffix.lower()

                # Check 1: Remove binaries
                if ext in EXTENSIONS_TO_REMOVE:
                    files_to_remove.append(inner_member.name)

                # Check 2: Identify "Strange" files (Not source, not binary, not symlink/dir)
                elif ext not in EXTENSIONS_EXPECTED_SOURCE:
                    is_special = inner_member.issym() or inner_member.islnk() or inner_member.isdir()

                    if not is_special:
                        if warn_strange:
                            logger.info(f"Strange file in {member_name}: {inner_member.name}")

                        if make_inventory:
                            inventory_log.append((member_name, inner_member.name, inner_member.size))

    except (tarfile.ReadError, EOFError, OSError, gzip.BadGzipFile):
        return False, None, 0

    if not files_to_remove:
        return False, None, 0

    # Pass 2: Rebuild
    fileobj.seek(0)
    new_gz_buffer = io.BytesIO()
    bytes_removed_count = 0

    try:
        with tarfile.open(fileobj=fileobj, mode='r|gz') as source_tar:
            with gzip.GzipFile(fileobj=new_gz_buffer, mode='wb', compresslevel=6) as gzip_stream:
                with tarfile.open(fileobj=gzip_stream, mode='w') as new_tar:
                    for inner_member in source_tar:
                        if inner_member.name in files_to_remove:
                            remove_log.append((f"{member_name}::{inner_member.name}", inner_member.size))
                            bytes_removed_count += inner_member.size
                            continue

                        # Fix: Handle Symlinks/Dirs
                        if inner_member.issym() or inner_member.islnk():
                            continue # Skip bad symlinks to avoid crash

                        if inner_member.isfile():
                            f_in = source_tar.extractfile(inner_member)
                            if f_in:
                                new_tar.addfile(inner_member, f_in)
                            else:
                                new_tar.addfile(inner_member)
                        else:
                            new_tar.addfile(inner_member)

    except Exception as e:
        logger.error(f"Error rebuilding {member_name}: {e}")
        return False, None, 0

    return True, new_gz_buffer.getvalue(), bytes_removed_count

def transform_artifact(ctx: ProcessingContext, append_logs: bool = False,
                       make_inventory: bool = False, warn_strange: bool = False) -> TransformationStats:
    remove_log = []
    inventory_log = []
    bytes_removed = 0

    original_disk_size = ctx.original_path.stat().st_size
    bytes_since_flush = 0
    FLUSH_THRESHOLD = 50 * 1024 * 1024

    # Only show progress if it's the main thing happening, otherwise it gets messy
    # But for transform, we always want a bar unless we completely suppress it.
    with tqdm(total=original_disk_size, unit='B', unit_scale=True, desc=f"Filtering {ctx.filename}", leave=False) as pbar:
        with tarfile.open(ctx.original_path, "r") as src, \
             open(ctx.cleaned_path, "wb") as dst_f, \
             tarfile.open(fileobj=dst_f, mode="w") as dst_tar:

            for member in src:
                pbar.update(member.size + TAR_BLOCK_SIZE)
                ext = Path(member.name).suffix.lower()

                # 1. OUTER FILTERING
                if ext in EXTENSIONS_TO_REMOVE:
                    remove_log.append((member.name, member.size))
                    bytes_removed += member.size
                    continue

                # 2. INNER INSPECTION
                if ext == ".gz":
                    f = src.extractfile(member)
                    if f:
                        modified, new_bytes, inner_removed = process_inner_gz(
                            member.name, f, remove_log, inventory_log,
                            make_inventory, warn_strange
                        )

                        if modified and new_bytes:
                            bytes_removed += inner_removed
                            new_info = tarfile.TarInfo(name=member.name)
                            new_info.size = len(new_bytes)
                            new_info.mtime = member.mtime
                            new_info.mode = member.mode
                            dst_tar.addfile(new_info, io.BytesIO(new_bytes))
                        else:
                            f.seek(0)
                            dst_tar.addfile(member, f)
                    else:
                        dst_tar.addfile(member)

                else:
                    # 3. OTHER FILES
                    # Check "Strange" loose files
                    if ext not in EXTENSIONS_EXPECTED_SOURCE:
                        is_special = member.issym() or member.islnk() or member.isdir()
                        if not is_special:
                            if warn_strange:
                                logger.info(f"Strange loose file: {member.name}")
                            if make_inventory:
                                inventory_log.append((member.name, "loose_file", member.size))

                    f = src.extractfile(member)
                    if f:
                        dst_tar.addfile(member, f)
                    else:
                        dst_tar.addfile(member)

                # Flush logic
                bytes_since_flush += member.size
                if bytes_since_flush > FLUSH_THRESHOLD:
                    dst_f.flush()
                    os.fsync(dst_f.fileno())
                    bytes_since_flush = 0

            dst_f.flush()
            os.fsync(dst_f.fileno())

    # Write Removal Log (Always)
    csv_mode = "a" if append_logs else "w"
    with ctx.csv_log_path.open(csv_mode, newline="", encoding="utf-8", errors="backslashreplace") as f:
        writer = csv.writer(f)
        if not append_logs: writer.writerow(["filename", "size_bytes"])
        writer.writerows(remove_log)

    # Write Inventory Log (Only if flag set AND logs exist)
    if make_inventory and inventory_log:
        inv_mode = "a" if append_logs else "w"
        with ctx.inventory_csv_path.open(inv_mode, newline="", encoding="utf-8", errors="backslashreplace") as f:
            writer = csv.writer(f)
            if not append_logs: writer.writerow(["container", "inner_file", "size_bytes"])
            writer.writerows(inventory_log)

    # Calculate final disk size
    cleaned_disk_size = ctx.cleaned_path.stat().st_size

    return TransformationStats(
        original_size=original_disk_size,
        cleaned_size=cleaned_disk_size,
        bytes_removed=bytes_removed
    )

# --- WORKER FUNCTIONS FOR PARALLEL EXECUTION ---

def log_stats(filename, action_name, stats, s3_size):
    """Thread-safe logging helper"""
    mb = 1024**2
    disk_delta = (stats.original_size - stats.cleaned_size) / mb
    s3_delta = (s3_size - stats.cleaned_size) / mb
    resulting_size_as_percentage_of_original = 100.0 * stats.cleaned_size / s3_size
    logger.info(
        f"{action_name} {filename}: "
        f"Saved {disk_delta:.1f}MB (Disk) | "
        f"Total Reduction vs S3: {s3_delta:.1f}MB (result is {resulting_size_as_percentage_of_original:.1f}% of original size)"
    )

def download_and_verify_worker(ctx: ProcessingContext,
                               dry_run: bool,
                               keep_broken: bool,
                               parallel_count: int) -> Optional[ProcessingContext]:
    """
    Worker function to handle download and verification.
    Returns ctx if the file is ready for processing, None if it failed.
    """
    check_disk_space(ctx.original_path.parent) # Check space before download

    # Disable individual progress bars if running in parallel to avoid console mess
    disable_pbar = parallel_count > 1

    if not download_artifact(ctx.filename, ctx.original_path, dry_run, disable_pbar):
        return None

    if not verify_artifact(ctx.original_path, ctx.expected_md5, dry_run, disable_pbar):
        if not keep_broken and not dry_run:
            ctx.original_path.unlink()
        return None

    return ctx

def filter_consumer_worker(queue_in: queue.Queue, args):
    """
    Consumes files from queue and runs the transformation (filtering).
    """
    while True:
        task = queue_in.get()
        if task is None:
            queue_in.task_done()
            break

        ctx, is_reprocess, s3_size = task

        try:
            if args.dry_run:
                logger.info(f"[DRY-RUN] Processing {ctx.filename}")
            else:
                if is_reprocess:
                    reproc_out = ctx.cleaned_path.with_suffix(".reproc.tar")
                    reproc_ctx = ProcessingContext(
                        filename=ctx.filename, expected_md5="", s3_size=s3_size,
                        original_path=ctx.cleaned_path, cleaned_path=reproc_out,
                        csv_log_path=ctx.csv_log_path, inventory_csv_path=ctx.inventory_csv_path
                    )
                    try:
                        stats = transform_artifact(reproc_ctx, append_logs=True,
                                                   make_inventory=args.make_inventory,
                                                   warn_strange=args.warn_about_strange)
                        reproc_out.replace(ctx.cleaned_path)
                        log_stats(ctx.filename, "Reprocessed", stats, s3_size)
                    except Exception as e:
                        logger.error(f"Reprocess failed {ctx.filename}: {e}", exc_info=True)
                        if reproc_out.exists(): reproc_out.unlink()

                else:
                    # Normal processing
                    try:
                        stats = transform_artifact(ctx, append_logs=False,
                                                   make_inventory=args.make_inventory,
                                                   warn_strange=args.warn_about_strange)
                        log_stats(ctx.filename, "Finished", stats, s3_size)

                        if args.delete_unfiltered_tars:
                            ctx.original_path.unlink()
                    except Exception as e:
                        logger.error(f"Transform failed {ctx.filename}: {e}", exc_info=True)
                        if ctx.cleaned_path.exists(): ctx.cleaned_path.unlink()

        except Exception as e:
            logger.error(f"Worker Error: {e}")
        finally:
            queue_in.task_done()

# --- MAIN ---

def main():
    parser = argparse.ArgumentParser(description="ArXiv Source Bulk ETL")
    parser.add_argument("--dest", type=Path, default=DEFAULT_DESTINATION)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delete-unfiltered-tars", action="store_true")
    parser.add_argument("--keep-broken-files", action="store_true")
    parser.add_argument("--download-everything-at-once", action="store_true")
    parser.add_argument("--force-manifest", action="store_true")
    parser.add_argument("--reprocess", action="store_true", help="Reprocess existing _onlytext.tar files")

    # New Arguments
    parser.add_argument("--make-inventory", action="store_true", help="Create _inventory.csv files for unknown extensions")
    parser.add_argument("--warn-about-strange", action="store_true", help="Log info when strange file extensions are found")
    parser.add_argument("--download-in-parallel", type=int, default=1, help="Number of parallel downloads (default: 1)")

    args = parser.parse_args()

    setup_logging(args.dest, args.dry_run)
    check_disk_space(args.dest)

    manifest_path = args.dest / Path(MANIFEST_KEY).name
    manifest = get_manifest_data(manifest_path, args.force_manifest)
    sorted_files = sorted(manifest.keys())

    logger.info(f"Starting ETL. Files: {len(sorted_files)} | Mode: {'DRY RUN' if args.dry_run else 'LIVE'} | Parallel: {args.download_in_parallel}")

    max_files = 4 if not args.download_everything_at_once else float('inf')

    # --- CONCURRENCY SETUP ---
    # Queue: Holds items ready for filtering (ctx, is_reprocess, s3_size)
    # We limit size to prevent downloading everything if filtering is slow
    processing_queue = queue.Queue(maxsize=args.download_in_parallel * 2)

    # Start the Filter Consumer Thread
    filter_thread = threading.Thread(target=filter_consumer_worker, args=(processing_queue, args), daemon=True)
    filter_thread.start()

    processed_count = 0

    # Start the Download Producers (ThreadPool)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.download_in_parallel) as executor:
        future_map = {} # Maps future -> (ctx, s3_size)

        # 1. SUBMISSION PHASE (Iterate fast, queue up tasks)
        logger.info("Scanning manifest and scheduling tasks...")

        for filename in sorted_files:
            if processed_count >= max_files:
                logger.info("Safety limit reached.")
                break

            entry = manifest[filename]
            ctx = ProcessingContext(
                filename=filename,
                expected_md5=entry.md5,
                s3_size=entry.size,
                original_path=args.dest / filename,
                cleaned_path=args.dest / f"{Path(filename).stem}_onlytext.tar",
                csv_log_path=args.dest / f"{Path(filename).stem}_onlytext.csv",
                inventory_csv_path=args.dest / f"{Path(filename).stem}_inventory.csv"
            )

            # --- DECISION LOGIC ---

            # Case A: Reprocess Existing
            if ctx.cleaned_path.exists() and ctx.csv_log_path.exists():
                if args.reprocess:
                    if args.dry_run:
                        continue
                    logger.info(f"Queuing for reprocess: {ctx.cleaned_path.name}")
                    # Put directly into processing queue (blocking if full)
                    processing_queue.put((ctx, True, entry.size))
                    continue
                else:
                    if args.delete_unfiltered_tars and ctx.original_path.exists() and not args.dry_run:
                        try: ctx.original_path.unlink()
                        except OSError: pass
                    if args.dry_run: logger.info(f"[DRY-RUN] Skip {filename}")
                    continue

            # Case B: New Download needed
            processed_count += 1

            future = executor.submit(
                download_and_verify_worker,
                ctx, args.dry_run, args.keep_broken_files, args.download_in_parallel
            )
            future_map[future] = (ctx, entry.size)

        # 2. MONITORING PHASE (Progress bar tracks COMPLETION, not submission)
        if future_map:
            logger.info(f"Waiting for {len(future_map)} downloads to complete...")
            with tqdm(total=len(future_map), desc="Downloading & Verifying", unit="file") as pbar:
                for future in concurrent.futures.as_completed(future_map):
                    ctx_info = future_map[future]
                    ctx_obj, s3_size = ctx_info

                    try:
                        result_ctx = future.result()
                        if result_ctx:
                            # Download success -> Add to processing queue
                            # This PUT might block if the filter thread is slow.
                            # That is GOOD. It pauses the progress bar and throttles downloads.
                            processing_queue.put((result_ctx, False, s3_size))
                    except Exception as e:
                        logger.error(f"Unexpected error in download thread for {ctx_obj.filename}: {e}")
                    finally:
                        pbar.update(1)

    # Signal Filter Thread to stop
    processing_queue.put(None)
    filter_thread.join()

    logger.info("ETL Pipeline Complete.")

if __name__ == "__main__":
    main()
