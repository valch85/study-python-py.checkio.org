from typing import List

def checkio(data: List[int]) -> [int, float]:

    return data[0]


print(checkio([1, 2, 3, 4, 5]))# == 3, "Sorted list"
print(checkio([3, 1, 2, 5, 3]))# == 3, "Not sorted list"
print(checkio([1, 300, 2, 200, 1]))# == 2, "It's not an average"
print(checkio([3, 6, 20, 99, 10, 15]))# == 12.5, "Even length"
print(checkio(list(range(1000000))))# == 499999.5, "Long."


