""" Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items,
after which each element equals the median of the three elements in the original list ending in that position.
Wait...You don't know what the "median" is? Go check out the separate "Median" mission on CheckiO."""
from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    if len(els) <= 2:
        return els
    else:
        answer = []
        answer += els[0:2]
        for i in range(0, len(els)-2):
            temp = [els[i], els[i + 1], els[i + 2]]
            temp = sorted(temp)
            answer.append(temp[1])
        return answer


print(median_three([1, 2, 3, 4, 5, 6, 7]))# == [1, 2, 2, 3, 4, 5, 6]
print(median_three([1]))# == [1]
print(median_three([5,2,9,1,7,4,6,3,8]))# == [5,2,5,2,7,4,6,4,6]
