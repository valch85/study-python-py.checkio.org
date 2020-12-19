def replace_last(line: list) -> list:
    # check for list with 0 or 1 element
    if len(line) <= 1:
        return line
    else:
        answer = []
        # get last element and put it to the 1st position of list
        answer.append(line[-1])
        # add to the list all other element except last
        answer = answer + line[:-1]
        return answer


print(replace_last([2, 3, 4, 1])) #== [1, 2, 3, 4]
print(replace_last([1, 2, 3, 4])) #== [4, 1, 2, 3]
print(replace_last([10, 10])) #== [10,10]
print(replace_last([1])) #== [1]
print(replace_last([])) #== []
