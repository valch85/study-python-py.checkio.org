from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    # check is borders exists in list of items if no return whole list
    if border in items:
        # create a counter that will increase each item check
        counter = 0
        for item in items:
            # counter increase
            counter += 1
            # when border is the same as item
            if item == border:
                # return items list from begging till the counter
                # (position where the border is the same as item)
                return items[:counter]
            else:
                pass
    else:
        return items


print(list(remove_all_after([1, 2, 3, 4, 5], 3)))# == [1, 2, 3]
print(list(remove_all_after([1, 1, 2, 2, 3, 3], 2)))# == [1, 1, 2]
print(list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)))# == [1, 1, 2]
print(list(remove_all_after([1, 1, 5, 6, 7], 2)))# == [1, 1, 5, 6, 7]
print(list(remove_all_after([], 0)))# == []
print(list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))# == [7]
