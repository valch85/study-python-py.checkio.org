def split_list(items: list) -> list:
    answer = []
    middle = int(len(items)/2)
    if len(items)% 2 == 0:
        answer.append(items[0:middle])
        answer.append(items[middle:])
    else:
        answer.append(items[0:middle+1])
        answer.append(items[middle+1:])
    return answer


split_list([1, 2, 3, 4, 5, 6]) #== [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) #== [[1, 2], [3]]
split_list([1, 2, 3, 4, 5]) #== [[1, 2, 3], [4, 5]]
split_list([1]) #== [[1], []]
split_list([]) #== [[], []]

