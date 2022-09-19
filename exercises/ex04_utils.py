"""EX03-Wordle."""
__author__ = "730571410"

def all(grp: list[int], num: int) -> bool:
    """Checks if all integers in a list match a certain number.""" 
    i: int = 0
    if len(grp) == 0:
        return False
    while i < len(grp):
        if num == grp[i]:
            i += 1
        else: 
            return False
    return True


def max(nums: list[int]) -> int:
    """Returns the largest int in a list."""
    if len(nums) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    high: int = nums[0]
    while i < len(nums):
        if nums[i] > high:
            high = nums[i]
            i += 1
        else:
            i += 1
    return high


def is_equal(x: list[int], y: list[int]) -> bool:
    """Checks if every element at every index is equal in 2 lists"""
    i: int = 0
    while i < len(x) and i < len(y):
        if x[i] == y[i]:
            i += 1
        else:
            return False
    return True