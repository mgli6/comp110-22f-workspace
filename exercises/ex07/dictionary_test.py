"""EX0y-Testing for Dictionary Functions."""
__author__ = "730571410"

from exercises.ex07.dictionary import count, favorite_color, invert


def test_invert_edge_case_empty() -> None:
    """Edge case 1 of invert: empty dictionary."""
    dict_x: dict[str, str] = {}
    assert invert(dict_x) == {}


def test_invert_use_case_one_many_items() -> None:
    """Use case 1 of invert: dictionary with multiple items."""
    dict_x: dict[str, str] = {"Yellow": "Purple", "Green": "Red", "Blue": "Orange"}
    assert invert(dict_x) == {"Purple": "Yellow", "Red": "Green", "Orange": "Blue"}


def test_invert_use_case_two_many_items_again() -> None:
    "Use case 2 of invert: dictionary with multiple items."
    dict_x: dict[str, str] = {"Happy": "Water", "Okay": "Tea", "Sad": "Juice", "Mad": "Soda"}
    assert invert(dict_x) == {"Water": "Happy", "Tea": "Okay", "Juice": "Sad", "Soda": "Mad"}


def test_favorite_color_edge_case_empty() -> None:
    """Edge case 1 of favorit_color: empty dictionary."""
    dict_x: dict[str, str] = {}
    assert favorite_color(dict_x) == ""


def test_favorite_color_use_case_one_many_items() -> None:
    """Use case 1 of favorite_color: dictionary with many items."""
    dict_x: dict[str, str] = {"Max": "purple", "Dogger": "red", "Bengal": "red"}
    assert favorite_color(dict_x) == "red"


def test_favorite_color_use_case_two_many_items_with_tie() -> None:
    """Use case 2 of favorite_color: dictionary with many items and a tie."""
    dict_x: dict[str, str] = {"Max": "purple", "Dogger": "red", "Bengal": "red", "Dino": "purple"}
    assert favorite_color(dict_x) == "red"


def test_count_edge_case_empty_list() -> None:
    """Edge case 1 of count: empty list."""
    list_x: list[str] = []
    assert count(list_x) == {}


def test_count_use_case_one_unique_list() -> None:
    """Use case 1 of count: list with only unique items."""
    list_x: list[str] = ["Dog", "Bengal", "Dino"]
    assert count(list_x) == {"Dog": 1, "Bengal": 1, "Dino": 1}


def test_count_use_case_two_duplicate_items() -> None:
    """Use case 2 of count: list with duplicate items."""
    list_x: list[str] = ["Dog", "Bengal", "Dino", "Dino", "Dog", "Dino"]
    assert count(list_x) == {"Dog": 2, "Bengal": 1, "Dino": 3}