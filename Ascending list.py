"""
Determine whether the sequence of elements items is ascending
so that its each element is strictly larger than (and not merely equal to) the element that precedes it.
"""
from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    # check the length if it 1 or less return true
    if len(items) <= 1:
        return True
    for i in range(0, len(items)-1, 1): # generate iterable for the digits position with the step 1 and iterate
        if items[i] < items[i+1]:
            pass
        else:
            return False
    return True


print(is_ascending([-5, 10, 99, 123456])) #== True
print(is_ascending([99])) #== True
print(is_ascending([4, 5, 6, 7, 3, 7, 9])) #== False
print(is_ascending([])) #== True
print(is_ascending([1, 1, 1, 1])) #== False
