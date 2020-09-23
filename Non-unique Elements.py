def checkio(data: list) -> list:
    new_list = []
    for iterator in data:
        if data.count(iterator) > 1:
            new_list.append(iterator)
    return new_list

list(checkio([1, 2, 3, 1, 3])) #== [1, 3, 1, 3], "1st example"
list(checkio([1, 2, 3, 4, 5])) #== [], "2nd example"
list(checkio([5, 5, 5, 5, 5])) #== [5, 5, 5, 5, 5], "3rd example"
list(checkio([10, 9, 10, 10, 9, 8])) #== [10, 9, 10, 10, 9], "4th example"


