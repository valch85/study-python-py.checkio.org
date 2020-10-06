def split_list(items: list) -> list:
    arr1 = []
    arr2 = []
    print(int(len(items)/2))
    if len(items)% 2 == 0:
        i = 0
        for v in range(0, int(len(items)/2)):
            print(items[i])
            i = i+1

            #arr1.append(i)
    #print(arr1)

split_list([1, 2, 3, 4, 5, 6]) #== [[1, 2, 3], [4, 5, 6]]
"""split_list([1, 2, 3]) #== [[1, 2], [3]]
split_list([1, 2, 3, 4, 5]) #== [[1, 2, 3], [4, 5]]
split_list([1]) #== [[1], []]
split_list([]) #== [[], []]"""

