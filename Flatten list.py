# Input data: A nested list with integers.
# Output data: The one-dimensional list with integers. 
# How it is used: This concept is useful for parsing and analyzing files with complex structures and the task challenges your creativity in writing short code. 
def flat_list(array):
    array = str(array).replace('[', '').replace(']', '').replace(',', '').strip()
    print(array)
    return list(map(int, array.split(' '))) if array else []


print(flat_list([1, 2, 3])) #== [1, 2, 3], "First"
print(flat_list([1, [2, 2, 2], 4])) #== [1, 2, 2, 2, 4], "Second"
print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) #== [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
print(flat_list([-1, [1, [-2], 1], -1])) #== [-1, 1, -2, 1, -1], "Four"
print('Done! Check it')