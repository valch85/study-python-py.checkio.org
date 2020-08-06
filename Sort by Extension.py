from typing import List

def sort_by_ext(files: List[str]) -> List[str]:

    return files


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
sort_by_ext(['1.cad', '1.bat', '1.aa']) # result == ['1.aa', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) # result == ['1.aa', '1.bat', '2.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) # result == ['.bat', '1.aa', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) # result == ['.aa', '.bat', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.', '1.aa']) # result == ['1.', '1.aa', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) # result == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) # result == ['1.aa', '1.bat', '1.cad', '.aa.doc']
