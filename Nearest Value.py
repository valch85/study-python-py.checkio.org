#1st solution
def nearest_value(values: set, one: int) -> int:
    values_sort = sorted(values)
    left_list, right_list = devide(values_sort)
    left_list_len = len(left_list)
    left_result = one - left_list[left_list_len-1]
    right_result = one - right_list[0]
    if abs(left_result) <= abs(right_result):
        if result(left_list):
            return int(left_list[0])
        else:
            return nearest_value(left_list, one)
    else:
        if result(right_list):
            return int(right_list[0])
        else:
            return nearest_value(right_list, one)


def devide(dev_list):
    dev_list = list(dev_list)
    length = len(dev_list)
    middle_index = length // 2
    left_list = dev_list[:middle_index]
    right_list = dev_list[middle_index:]
    return (left_list, right_list)


def result(answer_list):
    if len(answer_list) == 1:
        return True
    else:
        return False

'''
# 2nd solution
def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    n = 1
    while True:
        if (one - n) in values:
            return one - n
        elif (one + n) in values:
            return one + n
        n += 1
'''
print(nearest_value({4, 7, 10, 11, 12, 17}, 9)) #== 10
print(nearest_value({4, 7, 10, 11, 12, 17}, 8)) #== 7
print(nearest_value({4, 8, 10, 11, 12, 17}, 9)) #== 8
print(nearest_value({4, 9, 10, 11, 12, 17}, 9)) #== 9
print(nearest_value({4, 7, 10, 11, 12, 17}, 0)) #== 4
print(nearest_value({4, 7, 10, 11, 12, 17}, 100)) #== 17
print(nearest_value({5, 10, 8, 12, 89, 100}, 7)) #== 8
print(nearest_value({-1, 2, 3}, 0)) #== -1
