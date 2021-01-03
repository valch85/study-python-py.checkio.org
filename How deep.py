# You are given a tuple that consists of integers and other tuples, which in turn can also contain tuples.
# Your task is to find out how deep this structure is or how deep the nesting of these tuples is.
# For example, in the (1, 2, 3) tuple the depth of nesting is 1. And in the (1, 2, (3,)) tuple the depth of nesting is 2,
# since one of the elements of the first tuple is also a tuple. And in the (1, 2, (3, (4,))) tuple the depth of nesting
# is 3, since one of the elements of the first tuple is a tuple, but since inside it contains another tuple, it increases
# the depth by one, so the nesting depth turns out to be 3.
# It’s important to note that an empty tuple also increases the depth of the structure, that is, () - indicates the
# nesting depth 1, ((),) - indicates the nesting depth 2.


# 1st
# def how_deep(structure, n=1):
#    return max([n] + [how_deep(s, n+1) for s in structure if isinstance(s, tuple)])

# 2nd
def how_deep(struct):
    if type(struct) not in [list, tuple]:
        return 0
    if len(struct) == 0:
        return 1
    return 1 + max(how_deep(x) for x in struct)


# 3d
"""
def how_deep(structure):
    count = 0
    if isinstance(structure, (tuple)):
        count += 1
        counts_elems = []
        for elem in structure:
            counts_elems.append(how_deep(elem))
        count += max(counts_elems, default=0)
    return count
"""


print(how_deep((1, 2, 3)))  # == 1
print(how_deep((1, 2, (3,))))# == 2
print(how_deep((1, 2, (3, (4,)))))# == 3
print(how_deep(()))# == 1
print(how_deep(((),)))# == 2
print(how_deep((((),),)))# == 3
print(how_deep((1, (2,), (3,))))# == 2
print(how_deep((1, ((),), (3,))))  # == 3
