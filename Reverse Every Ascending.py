"""
Create and return a new iterable that contains the same elements as the argument iterable items, but with the reversed
order of the elements inside every maximal strictly ascending sublist. This function should not modify the contents
of the original iterable.
"""
# 1st solution
def reverse_ascending(items):
    result = []
    start = 0
    for i in range(1, len(items)):
        if items[i] <= items[i-1]:
            # save reverted result from started position to i
            result += items[start:i][::-1]
            start = i
    # add to result from last star item to the end of array
    return result + items[start:][::-1]

# 2nd solution
"""
def reverse_ascending(items):
    temp, seq = [], []
    while items:
        x = items.pop(0)
        if not temp or x > temp[-1]:
            temp.append(x)
        else:
            seq+=sorted(temp, reverse = True)
            temp.clear()
            temp.append(x)   
    seq+=sorted(temp, reverse = True)
    return seq
"""


print(reverse_ascending([1, 2, 3, 4, 5]))# == [5, 4, 3, 2, 1]
print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))# == [10, 7, 5, 4, 8, 7, 2, 3, 1]
print(reverse_ascending([5, 4, 3, 2, 1]))# == [5, 4, 3, 2, 1]
print(reverse_ascending([]))# == []
print(reverse_ascending([1]))# == [1]
print(reverse_ascending([1, 1]))# == [1, 1]
print(reverse_ascending([1, 1, 2]))# == [1, 2, 1]
