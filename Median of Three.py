""" Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items,
after which each element equals the median of the three elements in the original list ending in that position.
Wait...You don't know what the "median" is? Go check out the separate "Median" mission on CheckiO."""
from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:

    return []


    print(median_three([1, 2, 3, 4, 5, 6, 7]))# == [1, 2, 2, 3, 4, 5, 6]
    print(median_three([1]))# == [1]
