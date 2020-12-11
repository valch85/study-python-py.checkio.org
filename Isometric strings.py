def isometric_strings(str1: str, str2: str) -> bool:
    return len(list(zip(str1, str2))) == len(list(str1))


print(isometric_strings('add', 'egg')) #== True
print(isometric_strings('foo', 'bar')) #== False
print(isometric_strings('', '')) #== True
print(isometric_strings('all', 'all')) #== True
print(isometric_strings('1334557', 'abqceeg'))

