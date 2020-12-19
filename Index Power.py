def index_power(array: list, n: int) -> int:

    return None



print(index_power([1, 2, 3, 4], 2)) # == 9, "Square"
print(index_power([1, 3, 10, 100], 3)) # == 1000000, "Cube"
print(index_power([0, 1], 0)) # == 1, "Zero power"
print(index_power([1, 2], 3)) #== -1, "IndexError"


