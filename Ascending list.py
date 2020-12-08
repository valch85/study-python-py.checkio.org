from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    # your code here
    return True


print(is_ascending([-5, 10, 99, 123456])) #== True
print(is_ascending([99])) #== True
print(is_ascending([4, 5, 6, 7, 3, 7, 9])) #== False
print(is_ascending([])) #== True
print(is_ascending([1, 1, 1, 1])) #== False


