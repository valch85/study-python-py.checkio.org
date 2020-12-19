def replace_last(line: list) -> list:
    if len(line) <= 1:
        return line
    else:
        answer = []
        for i in str(line[-1]):
            answer.append(int(i))
        for i in line[:-1]:
            answer.append(i)
        return answer



print(replace_last([2, 3, 4, 1])) #== [1, 2, 3, 4]
print(replace_last([1, 2, 3, 4])) #== [4, 1, 2, 3]
print(replace_last([1])) #== [1]
print(replace_last([])) #== []

