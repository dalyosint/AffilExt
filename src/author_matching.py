"""Fuzzy comparison of author name lists (used by the pipeline's quality gate and the experiments)."""
from rapidfuzz import fuzz

# Calibrated in experiments/analyze_thresholds.py
DEFAULT_METHOD = "hybrid"
DEFAULT_NAME_THRESHOLD = 70


def name_similarity(name_a: str, name_b: str, method: str = DEFAULT_METHOD) -> float:
    """Similarity (0-100) of two names. Names are lower-cased and stripped before comparing.

    Methods:
        ratio:  plain edit-distance ratio
        token:  token_set_ratio (ignores word order and extra tokens, e.g. middle names)
        hybrid: max(ratio, token)
    """
    a = name_a.lower().strip()
    b = name_b.lower().strip()
    if method == "ratio":
        return fuzz.ratio(a, b)
    if method == "token":
        return fuzz.token_set_ratio(a, b)
    if method == "hybrid":
        return max(fuzz.ratio(a, b), fuzz.token_set_ratio(a, b))
    raise ValueError(f"Unknown name similarity method: {method!r}")


def author_match_scores(extracted_names: list[str], ground_truth_names: list[str],
                        threshold: float = DEFAULT_NAME_THRESHOLD, method: str = DEFAULT_METHOD) -> dict:
    """Precision, recall and F1 of extracted author names against the ground truth (e.g. arXiv metadata).

    Each extracted name is greedily matched to the most similar ground truth name that is still unmatched;
    it counts as a true positive if that similarity reaches the threshold.
    """
    if not extracted_names and not ground_truth_names:
        return {"precision": 1.0, "recall": 1.0, "f1_score": 1.0}
    if not extracted_names:
        return {"precision": 0.0, "recall": 0.0, "f1_score": 0.0}

    matched_gt = set()
    true_positives = 0

    for ext_name in extracted_names:
        best_idx = -1
        best_score = 0

        for j, gt_name in enumerate(ground_truth_names):
            if j in matched_gt:
                continue

            score = name_similarity(ext_name, gt_name, method)
            if score > best_score:
                best_score = score
                best_idx = j

        if best_score >= threshold:
            matched_gt.add(best_idx)
            true_positives += 1

    precision = true_positives / len(extracted_names)
    recall = true_positives / len(ground_truth_names) if ground_truth_names else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0

    return {"precision": precision, "recall": recall, "f1_score": f1}


def author_f1(extracted_names: list[str], ground_truth_names: list[str],
              threshold: float = DEFAULT_NAME_THRESHOLD, method: str = DEFAULT_METHOD) -> float:
    """F1 score only; see author_match_scores()."""
    return author_match_scores(extracted_names, ground_truth_names, threshold, method)["f1_score"]
