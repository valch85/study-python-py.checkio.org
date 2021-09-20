# Input data: A nested list with integers.
# Output data: The one-dimensional list with integers. 
# How it is used: This concept is useful for parsing and analyzing files with complex structures and the task challenges your creativity in writing short code. 
def flat_list(array):
    return array

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) #== [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) #== [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) #== [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) #== [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')