def left(position: str):
    return(chr(ord(position[0])-1)+chr(ord(position[1])-1))


def right(position: set):
    return(chr(ord(position[0])+1)+chr(ord(position[1])-1))


def safe_pawns(pawns: set) -> int:
    pawns = list(pawns)
    save_pawns = 0
    for position in pawns:
        if left(position) in pawns:
            save_pawns = save_pawns + 1
        elif right(position) in pawns:
            save_pawns = save_pawns + 1
        else:
            save_pawns = save_pawns + 0
    return save_pawns


safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) #== 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) #== 1

