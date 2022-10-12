"""EX07-Dictionary Functions."""
__author__ = "730571410"

def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the key and the value."""
    result: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in result:
            raise KeyError("Cannot have more than one value associated with a single key.")
        result[dictionary[key]] = key        
    return result


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most popular favorite color."""
    counter: dict[str, int] = {}
    for key in dictionary:
        if dictionary[key] in counter:
            counter[dictionary[key]] += 1
        else:
            counter[dictionary[key]] = 1
    max_color: int = 0
    result: str = ""
    for color in counter:
        if counter[color] > max_color:
            result = color
    return result


def count(list_x: list[str]) -> dict[str, int]:
    """Returns a dictionary of the number of times a str appeared."""
    result: dict[str, int] = {}
    for string in list_x:
        if string in result:
            result[string] += 1
        else:
            result[string] = 1
    return result