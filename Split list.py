def split_list(items: list) -> list:
    # your code here
    return [items]



split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) == [[1, 2], [3]]
split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
split_list([1]) == [[1], []]
split_list([]) == [[], []]

