def frequency_sort(items):
    temp_dict = {}
    for iterator in items:
        #print(str(iterator) + " = " + str(items.count(iterator)))
        temp_dict.update({str(iterator): items.count(iterator)})

    #sort_dict = {k: v for k, v in sorted(temp_dict.items(), key=lambda item: item[1])}
    sort_dict = {}
    for k, v in sorted(temp_dict.items(), key=lambda item: item[1], reverse=True):
        sort_dict.update({k: v})

    answer = []
    for i in sort_dict:

        for (sort_dict[i] < 0):
            answer.append(i)
            sort_dict[i]=sort_dict[i]-1

    print(answer)





    #print(temp_dict.items())
    #print(sort_dict)
    #return None

frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) #== [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) #== ['bob', 'bob', 'bob', 'carl', 'alex']
frequency_sort([17, 99, 42]) #== [17, 99, 42]
frequency_sort([]) #== []
frequency_sort([1]) #== [1]
