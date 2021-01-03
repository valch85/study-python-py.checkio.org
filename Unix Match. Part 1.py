"""Sometimes you find yourself in a situation when, among a huge number of files on your computer or in a separate
folder, you need to find files of a certain type. For example, images with the extension '.jpg' or documents with the
extension '.txt', or even files that have the word 'butterfly' in their name. Doing this manually can be time-consuming.
'Matching' or patterns for searching files by a specific mask are just what you need for these sort of challenges.
This mission will help you understand how this works.
You need to find out if the given unix pattern matches the given filename.
Let me show you what I mean by matching the filenames in the unix-shell. For example, * matches everything and *.txt
matches all of the files that have txt extension. Here is a small table that shows symbols that can be used in
patterns."""


def unix_match(filename: str, pattern: str) -> bool:

    return filename == pattern


print(unix_match('somefile.txt', '*'))# == True
print(unix_match('other.exe', '*'))# == True
print(unix_match('my.exe', '*.txt'))# == False
print(unix_match('log1.txt', 'log?.txt'))# == True
print(unix_match('log12.txt', 'log?.txt'))# == False
print(unix_match('log12.txt', 'log??.txt'))# == True


