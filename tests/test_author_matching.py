import pytest

from author_matching import author_f1, author_match_scores, name_similarity


def test_identical_lists_score_one():
    assert author_f1(["Alice Smith", "Bob Jones"], ["Alice Smith", "Bob Jones"]) == 1.0


def test_both_empty_is_perfect_and_extracted_empty_is_zero():
    assert author_f1([], []) == 1.0
    assert author_f1([], ["Alice Smith"]) == 0.0


def test_initials_and_word_order_still_match():
    # token_set_ratio handles reordering, ratio handles small spelling differences
    assert author_f1(["Smith Alice"], ["Alice Smith"]) == 1.0
    assert author_f1(["Alice Smyth"], ["Alice Smith"]) == 1.0


def test_unrelated_names_do_not_match():
    assert author_f1(["Zhang Wei"], ["Alice Smith"]) == 0.0


def test_each_ground_truth_author_is_matched_only_once():
    scores = author_match_scores(["Alice Smith", "Alice Smith"], ["Alice Smith"])
    assert scores["precision"] == 0.5
    assert scores["recall"] == 1.0


def test_precision_and_recall():
    scores = author_match_scores(["Alice Smith"], ["Alice Smith", "Bob Jones"])
    assert scores == pytest.approx({"precision": 1.0, "recall": 0.5, "f1_score": 2 / 3})


@pytest.mark.parametrize("method", ["ratio", "token", "hybrid"])
def test_methods_are_case_insensitive(method):
    assert name_similarity("ALICE SMITH", "alice smith", method) == 100


def test_unknown_method_raises():
    with pytest.raises(ValueError):
        name_similarity("a", "b", "nope")
