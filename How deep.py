def how_deep(structure):
    structure = str(structure)
    return structure


print(how_deep((1, 2, 3)))# == 1
print(how_deep((1, 2, (3,))))# == 2
print(how_deep((1, 2, (3, (4,)))))# == 3
print(how_deep(()))# == 1
print(how_deep(((),)))# == 2
print(how_deep((((),),)))# == 3
print(how_deep((1, (2,), (3,))))# == 2
print(how_deep((1, ((),), (3,))))# == 3

