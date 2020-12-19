def is_majority(items: list) -> bool:

    return items



print(is_majority([True, True, False, True, False]))# == True
print(is_majority([True, True, False]))# == True
print(is_majority([True, True, False, False]))# == False
print(is_majority([True, True, False, False, False]))# == False
print(is_majority([False]))# == False
print(is_majority([True]))# == True
print(is_majority([]))# == False


