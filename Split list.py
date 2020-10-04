def split_list(items: list) -> list:
    arr1 = []
    arr2 = []
    if len(items)% 2 == 0:
        for i in range(0, len(items)/2):
            yield items[i:i]
    print(items)

split_list([1, 2, 3, 4, 5, 6]) #== [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) #== [[1, 2], [3]]
split_list([1, 2, 3, 4, 5]) #== [[1, 2, 3], [4, 5]]
split_list([1]) #== [[1], []]
split_list([]) #== [[], []]

