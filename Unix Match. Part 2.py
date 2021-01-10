"""
Sometimes you find yourself in a situation when, among a huge number of files on your computer or in a separate folder,
you need to find files of a certain type. For example, images with the extension '.jpg' or documents with the extension
'.txt', or even files that have the word 'butterfly' in their name. Doing this manually can be time-consuming.
'Matching' or patterns for searching files by a specific mask are just what you need for these sort of challenges.
This mission will help you understand how this works.
You need to find out if the given unix pattern matches the given filename.
Here is a small table that shows symbols that can be used in patterns.
[seq] 	matches any character in seq, for example [123] means any character - '1', '2' or '3'
[!seq] 	matches any character not in seq, for example [!123] means any character except '1', '2' and '3'
[] 	seq without any chars will never match
Note that the expression in one pair of square brackets responds only for 1 character. So
('0123', '[!abc]123') == True, but ('00123', '[!abc]123') = False
"""
import re


def unix_match(filename: str, pattern: str) -> bool:
    # create temp pattern string
    pattern_temp = ""

    # special case for [!]
    if "[!]" in pattern:
        # convert characters ".", "*" & "?" to regexp format
        for i in pattern:
            if i == '[':
                pattern_temp = pattern_temp + "\["
            elif i == '!':
                pattern_temp = pattern_temp + "\!"
            elif i == ']':
                pattern_temp = pattern_temp + "\]"
            elif i == '.':
                pattern_temp = pattern_temp + "\."
            else:
                pattern_temp = pattern_temp + str(i)
        # check match with regexp library
        result = re.match(pattern_temp, filename)
        if result:
            return True
        else:
            return False


    # get 1st and last position in pattern of "[" & "]"
    if "[" in pattern:
        result = {}
        for key, value in enumerate(pattern):
            result.setdefault(value, []).append(key)
        start = int(result['['][0])
        end = int(result[']'][-1])
        # check is characters exists between []
        if len(pattern[start:end+1]) <= 2:
            return False

    # convert characters ".", "*" & "?" to regexp format
    for i in pattern:
        if i == '?':
            pattern_temp = pattern_temp + "."
        elif i == '*':
            pattern_temp = pattern_temp + ".*"
        elif i == '.':
            pattern_temp = pattern_temp + "\."
        elif i == '!':
            pattern_temp = pattern_temp + "^"
        else:
            pattern_temp = pattern_temp + str(i)
    # check match with regexp library
    result = re.match(pattern_temp, filename)
    if result:
        return True
    else:
        return False


print(unix_match('somefile.txt', 'somefile.txt'))# == True
print(unix_match('1name.txt', '[!abc]name.txt'))# == True (!abc)
print(unix_match('log1.txt', 'log[!0].txt'))# == True
print(unix_match('log1.txt', 'log[1234567890].txt'))# == True
print(unix_match('log1.txt', 'log[!1].txt'))# == False
print(unix_match('name.txt', 'name[]txt'))# == False
print(unix_match('[!]check.txt', '[!]check.txt'))# == True
print(unix_match('checkio.txt', '[c[]heckio.txt'))# == True
print(unix_match('nametxt', 'name[]txt'))# == False
