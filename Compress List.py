""" A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another,
 there is only one in the result Iterable (list, tuple, iterator ...).
"""
from typing import Iterable


def compress(items: list) -> Iterable:

    return items



print(compress([
  5, 5, 5,
  4, 5, 6,
  6, 5, 5,
  7, 8, 0,
  0])))# == [5, 4, 5, 6, 5, 7, 8, 0]


print(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])))# == [1, 2, 1]
print(compress([7, 7])))# == [7]
print(compress([])))# == []
print(compress([1, 2, 3, 4])))# == [1, 2, 3, 4]
print(compress([9, 9, 9, 9, 9, 9, 9])))# == [9]
