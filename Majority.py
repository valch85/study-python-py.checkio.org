def is_majority(items: list) -> bool:
    # create lists for true & false count results
    ttt = []
    fff = []
    # go through the items list
    # and append them accordingly
    for i in items:
        if i == True:
            ttt.append(i)
        else:
            fff.append(i)

    # check the lenth of lists
    if len(ttt) <= len(fff):
        return False
    else:
        return True



print(is_majority([True, True, False, True, False]))# == True
print(is_majority([True, True, False]))# == True
print(is_majority([True, True, False, False]))# == False
print(is_majority([True, True, False, False, False]))# == False
print(is_majority([False]))# == False
print(is_majority([True]))# == True
print(is_majority([]))# == False


