"""Tests for ex05 functions."""
__author__ = "730571410"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_edge_case_no_evens() -> None:
    """Edge case #1 list with no evens."""
    xs: list[int] = [3, 7, 5]
    assert only_evens(xs) == []


def test_only_evens_use_case_many_items() -> None:
    """Use case #1 list with multiple items."""
    xs: list[int] = [1, 2 , 3]
    assert only_evens(xs) == [2]


def test_only_evens__use_case_many_items_again() -> None:
    """Use case #2 list with multiple items."""
    xs: list[int] = [3, 4, 6, 7, 6]
    assert only_evens(xs) == [4, 6, 6]


def test_concat_edge_case_empty_lists() -> None:
    """Edge case #1 two empty lists."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_use_case_many_items() -> None:
    """Use case #1 multiple lists with mulitple items."""
    xs: list[int] = [1, 3]
    ys: list[int] = [2, 4]
    assert concat(xs, ys) == [1, 3, 2, 4]


def test_concat_use_case_many_items_again() -> None:
    """Use case #2 multiple lists with mulitple items."""
    xs: list[int] = [10, 110, 190, 2000]
    ys: list[int] = [3, 55]
    assert concat(xs, ys) == [10, 110, 190, 2000, 3, 55]


def test_sub_edge_case_negative_start_and_longer_end() -> None:
    """Edge case #1 start is negative and end is longer than length of list."""
    xs: list[int] = [1, 2, 3, 4]
    start: int = -2
    end: int = 7
    assert sub(xs, start, end) == [1, 2, 3, 4]


def test_sub_use_case_many_items() -> None:
    """Use case #1 multiple items in list and start and end conform to expected values."""
    xs: list[int] = [1, 2, 3, 4]
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == [2, 3]


def test_sub_use_case_many_items_again() -> None:
    """Use case #2 multiple items in list and start and end conform to expected values."""
    xs: list[int] = [100, 250, 340, 490, 709, 800]
    start: int = 2
    end: int = 5
    assert sub(xs, start, end) == [340, 490, 709]    