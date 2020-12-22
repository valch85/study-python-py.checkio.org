# Sort the numbers in an array. But the position of zeros should not be changed.
from typing import Iterable


def except_zero(items: list) -> Iterable:
    temp = sorted(items)
    temp_arr = []
    answer_arr = []
    counter = 0
    for i in temp:
        if i != 0:
            temp_arr.append(i)

    for i in items:
        if i != 0:
            answer_arr.append(temp_arr[counter])
            counter += 1
        else:
            answer_arr.append(int(0))

    return answer_arr


print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))# == [1, 3, 0, 0, 4, 4, 5, 0, 7]
print(list(except_zero([0, 2, 3, 1, 0, 4, 5])))# == [0, 1, 2, 3, 0, 4, 5]
print(list(except_zero([0, 0, 0, 1, 0])))# == [0, 0, 0, 1, 0]
print(list(except_zero([4, 5, 3, 1, 1])))# == [1, 1, 3, 4, 5]
print(list(except_zero([0, 0])))# == [0, 0]
