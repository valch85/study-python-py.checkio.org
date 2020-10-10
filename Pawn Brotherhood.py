"""def safe_pawns(pawns: set) -> int:
    save = []
    for v in pawns:
        if v :
            save.add(v)
    return(save.count())


safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) #== 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) #== 1
"""


def left(v: set):
    test_arr = []
    for n in v:
        test_arr.append(chr(ord(n[0])-1))
        test_arr.append(chr(ord(n[1])-1))
    print(test_arr)

left({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})