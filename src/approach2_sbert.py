import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------------------------
# Load the sentence transformer model once at module level.
# ---------------------------------------------------------------------------
_MODEL_NAME = "all-MiniLM-L6-v2"
_CACHE_FILE = Path("ror_embeddings_cache.npz")

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
    """

    def __init__(self, research_orgs: list[tuple[str, str]]):
        self.research_orgs = research_orgs
        self.org_names = [org[1] for org in research_orgs]

        if _CACHE_FILE.exists():
            data = np.load(_CACHE_FILE, allow_pickle=True)
            self.embeddings = data["embeddings"]
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

    def find_best_match(self, affiliation: str) -> tuple[str, float]:
        # Encode the query affiliation
        query_vec = _model.encode(
            affiliation,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        # Cosine similarity = dot product when both vectors are normalised
        similarities = np.dot(self.embeddings, query_vec)

        best_idx = int(np.argmax(similarities))
        best_score = float(similarities[best_idx]) * 100   # scale to 0-100 format

        best_ror_id = self.research_orgs[best_idx][0]
        return best_ror_id, best_score


# ---------------------------------------------------------------------------
# Module-level integration functions
# ---------------------------------------------------------------------------
_index: RorEmbeddingIndex | None = None


def initialise_index(research_orgs: list[tuple[str, str]]) -> None:
    """Call this ONCE after loading the ROR dataset."""
    global _index
    _index = RorEmbeddingIndex(research_orgs)


def get_matched_affiliation_sbert(
    affiliation: str,
    research_orgs: list[tuple[str, str]]
) -> tuple[str, tuple[str, float]]:
    """
    Match one affiliation string to the ROR dataset using Sentence-BERT.
    """
    global _index
    if _index is None:
        # Auto-initialise on first call if not done manually
        initialise_index(research_orgs)

    ror_id, score = _index.find_best_match(affiliation)
    return affiliation, (ror_id, score)