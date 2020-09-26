# function that convert var to integer if possible
def isint(x):
    try:
        a = int(x)
    except ValueError:
        return x
    else:
        return int(a)

def frequency_sort(items):
    # temp dict
    temp_dict = {}
    # count amount of items in list and add them to dict
    for iterator in items:
        temp_dict.update({str(iterator): items.count(iterator)})

    # temp dict for sorted items
    sort_dict = {}
    # going via KEY and VALUE of temp_dict and sort them in a reverse mode by VALUE
    # to get KEY use lambda (get second item in a list of [key, value]
    for k, v in sorted(temp_dict.items(), key=lambda item: item[1], reverse=True):
        # add result to the dict
        sort_dict.update({k: v})

    # list for answer
    answer = []
    # going throw KEYs of sort_dict
    for key in sort_dict:
        # get VALUE of the KEY
        value = sort_dict[key]
        # loop that add KEY as many times as in VALUE
        for iterable in range(value):
            # use function isint to convert digits to an integer
            answer.append(isint(key))

    return answer


frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) #== [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) #== ['bob', 'bob', 'bob', 'carl', 'alex']
frequency_sort([17, 99, 42]) #== [17, 99, 42]
frequency_sort([]) #== []
frequency_sort([1]) #== [1]
