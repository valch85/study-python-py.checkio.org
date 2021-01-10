"""
Create and return a new iterable that contains the same elements as the argument iterable items, but with the reversed
order of the elements inside every maximal strictly ascending sublist. This function should not modify the contents
of the original iterable.
"""
def reverse_ascending(items):

    return None




print(list(reverse_ascending([1, 2, 3, 4, 5])))# == [5, 4, 3, 2, 1]
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))# == [10, 7, 5, 4, 8, 7, 2, 3, 1]
print(list(reverse_ascending([5, 4, 3, 2, 1])))# == [5, 4, 3, 2, 1]
print(list(reverse_ascending([])))# == []
print(list(reverse_ascending([1])))# == [1]
print(list(reverse_ascending([1, 1])))# == [1, 1]
print(list(reverse_ascending([1, 1, 2])))# == [1, 2, 1]
