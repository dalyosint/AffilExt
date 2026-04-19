"""
APPROACH 2: Sentence-BERT Dense Embeddings + Cosine Similarity
================================================================
Install dependencies:
    pip install sentence-transformers numpy

How it works:
    1. At startup, encode all ROR organisation names into dense vectors (done ONCE)
    2. For each incoming affiliation string, encode it into a vector
    3. Find the closest ROR vector using cosine similarity
    4. This is semantically aware: "Aachen Technical University" will match
       "RWTH Aachen University" even though the words are different

Plug-in point in your codebase: replace _get_matched_affiliation() in match_data.py
NOTE: First run is slow (encoding 111k ROR names). Subsequent runs use the cache.
"""

import unicodedata
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------------------------
# Load the sentence transformer model once at module level.
# "all-MiniLM-L6-v2" is a great balance of speed and accuracy.
# It downloads ~90 MB on first use and caches locally.
# ---------------------------------------------------------------------------
_MODEL_NAME = "all-MiniLM-L6-v2"
_CACHE_FILE = Path("ror_embeddings_cache.npz")   # saves re-encoding on restart

try:
    _model = SentenceTransformer(_MODEL_NAME)
    print(f"[Approach 2] Sentence-BERT model '{_MODEL_NAME}' loaded.")
except Exception as e:
    raise RuntimeError(f"Could not load Sentence-BERT model: {e}")


# ---------------------------------------------------------------------------
# ROR embedding index — built once, reused for every affiliation query
# ---------------------------------------------------------------------------
class RorEmbeddingIndex:
    """
    Encodes all ROR organization names into vectors and supports fast
    cosine similarity lookup.

    Usage:
        index = RorEmbeddingIndex(research_orgs)          # build once
        ror_id, score = index.find_best_match(affiliation) # query many times
    """

    def __init__(self, research_orgs: list[tuple[str, str]]):
        """
        Args:
            research_orgs: list of (ror_id, preprocessed_org_name) tuples
                           Same format as match_data._process_ror_orgs()
        """
        self.research_orgs = research_orgs
        self.org_names = [org[1] for org in research_orgs]

        print(f"[Approach 2] Building embedding index for {len(self.org_names)} ROR names...")
        print("  (This takes ~30-120 seconds on first run, then uses cache)")

        if _CACHE_FILE.exists():
            print(f"  Loading cached embeddings from {_CACHE_FILE}")
            data = np.load(_CACHE_FILE, allow_pickle=True)
            self.embeddings = data["embeddings"]
            print(f"  Loaded {len(self.embeddings)} cached embeddings.")
        else:
            # Encode in batches for memory efficiency
            self.embeddings = _model.encode(
                self.org_names,
                batch_size=512,
                show_progress_bar=True,
                convert_to_numpy=True,
                normalize_embeddings=True   # pre-normalise for fast cosine sim
            )
            np.savez(_CACHE_FILE, embeddings=self.embeddings)
            print(f"  Saved embeddings cache to {_CACHE_FILE}")

    def find_best_match(self, affiliation: str) -> tuple[str, float]:
        """
        Find the best matching ROR organisation for a raw affiliation string.

        Returns:
            (ror_id, similarity_score_0_to_100)
        """
        # Encode the query affiliation
        query_vec = _model.encode(
            affiliation,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        # Cosine similarity = dot product when both vectors are normalised
        similarities = np.dot(self.embeddings, query_vec)

        best_idx = int(np.argmax(similarities))
        best_score = float(similarities[best_idx]) * 100   # scale to 0-100 like RapidFuzz

        best_ror_id = self.research_orgs[best_idx][0]
        return best_ror_id, best_score


# ---------------------------------------------------------------------------
# Module-level index instance (initialised lazily on first use)
# ---------------------------------------------------------------------------
_index: RorEmbeddingIndex | None = None


def initialise_index(research_orgs: list[tuple[str, str]]) -> None:
    """
    Call this ONCE after loading the ROR dataset.
    Must be called before get_matched_affiliation_sbert().

    Example (in your pipeline_parquet.py or match_data.py):
        import approach2_sbert
        approach2_sbert.initialise_index(ror_orgs)
    """
    global _index
    _index = RorEmbeddingIndex(research_orgs)


def get_matched_affiliation_sbert(
    affiliation: str,
    research_orgs: list[tuple[str, str]]
) -> tuple[str, tuple[str, float]]:
    """
    Match one affiliation string to the ROR dataset using Sentence-BERT.

    Drop-in replacement for _get_matched_affiliation() in match_data.py

    Args:
        affiliation:     Raw extracted affiliation string from LaTeX
        research_orgs:   List of (ror_id, preprocessed_name) tuples
                         (Used only to initialise index if not done yet)

    Returns:
        (original_affiliation, (best_ror_id, score_0_to_100))
    """
    global _index
    if _index is None:
        # Auto-initialise on first call if not done manually
        initialise_index(research_orgs)

    ror_id, score = _index.find_best_match(affiliation)
    return affiliation, (ror_id, score)


# ---------------------------------------------------------------------------
# Quick standalone test — run this file directly to verify it works
# NOTE: This will download the model (~90MB) on first run
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Simulate a tiny ROR dataset for testing
    fake_ror_orgs = [
        ("https://ror.org/02s6k3f65", "university of basel"),
        ("https://ror.org/04cvxnb49", "rwth aachen university"),
        ("https://ror.org/02jx3x895", "university of cagliari"),
        ("https://ror.org/03yrm5c26", "carnegie mellon university"),
        ("https://ror.org/01cwqze88", "massachusetts institute of technology"),
        ("https://ror.org/052gg0110", "stanford university"),
        ("https://ror.org/00hj54h04", "national university of singapore"),
        ("https://ror.org/049s0ch10", "jagiellonian university"),
        ("https://ror.org/042nb2s44", "university of texas at austin"),
        ("https://ror.org/05x2bcf33", "georgia institute of technology"),
    ]

    test_cases = [
        "Department of Mathematics, University of Cagliari, Via Ospedale 72, 09124 Cagliari, Italy",
        "Software Engineering, RWTH Aachen University, Germany",
        "Wireless Networking and Communications Group, Dept. of ECE, UT Austin, TX 78712",
        "M. Smoluchowski Institute of Physics, Jagiellonian University, Kraków, Poland",
        "MIT Computer Science and Artificial Intelligence Laboratory, Cambridge, MA",
    ]

    print("=" * 60)
    print("APPROACH 2: Sentence-BERT Semantic Matching Test")
    print("=" * 60)

    # Build index once
    initialise_index(fake_ror_orgs)

    for raw in test_cases:
        _, (matched_id, score) = get_matched_affiliation_sbert(raw, fake_ror_orgs)
        # Look up the name for display
        matched_name = next(
            (name for ror_id, name in fake_ror_orgs if ror_id == matched_id),
            "Unknown"
        )
        print(f"\n  INPUT:   {raw}")
        print(f"  MATCHED: {matched_name}")
        print(f"  SCORE:   {score:.1f}/100")