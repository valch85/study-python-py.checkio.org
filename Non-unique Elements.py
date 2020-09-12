from collections import Counter

def checkio(data: list) -> list:
    unique_list = []

    for x in data:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    if list.count(unique_list) == 0:
        print
    else:
        print(unique_list)
        #return data
    #print(data)

list(checkio([1, 2, 3, 1, 3])) #== [1, 3, 1, 3], "1st example"
list(checkio([1, 2, 3, 4, 5])) #== [], "2nd example"
list(checkio([5, 5, 5, 5, 5])) #== [5, 5, 5, 5, 5], "3rd example"
list(checkio([10, 9, 10, 10, 9, 8])) #== [10, 9, 10, 10, 9], "4th example"


