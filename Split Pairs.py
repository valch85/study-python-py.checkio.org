# 1st solution
def split_pairs(a):
    n = len(a)

    zero_mass = []
    if n % 2 == 1:
        a = a + str("_")
    if n == 0:
        return zero_mass

    massive = []
    i = 0
    while i < n:
        l = 0
        line = ""
        while l < 2:
            line = str(line) + str(a[i+l])
            l += 1

        massive.append(line)
        i += 2

    return massive

"""
# 2nd solution 
def split_pairs(a):
    result = []
    if len(a) % 2 != 0:
        a = a + '_'
    i = iter(a)
    while True:
        try:
            ch1 = next(i)
            ch2 = next(i)
            result.append(''.join((ch1,ch2)))
        except StopIteration:
            break
    return result
"""


split_pairs('abcd') #== ['ab', 'cd']
split_pairs('abc') #== ['ab', 'c_']
split_pairs('abcdf') #== ['ab', 'cd', 'f_']
split_pairs('a') #== ['a_']
split_pairs('') #== []
