"""ex05 function skeletons."""
__author__ = "730571410"


def only_evens(xs: list[int]) -> list[int]:
    """Returns a list containing only even elements of the input list."""
    evens: list[int] = []
    for x in xs:
        if x % 2 == 0:
            evens.append(x) 
    return evens
            

def concat(xs: list[int], ys: list[int]):
    """Returns a list containing the first list followed by the second list."""
    new_list: list[int] = []
    for x in xs:
        new_list.append(x)
    for y in ys:
        new_list.append(y)
    return new_list
    

def sub(xs: list[int], start: int, end: int):
    """Returns a list that is a subset of a list between a specified start index and end index - 1."""
    i: int = start
    new_list: list[int] = []
    if start < 0:
        i = 0
    if end > len(xs):
        end = len(xs)
    while i >= start and i < end:
        new_list.append(xs[i])
        i += 1
    return new_list