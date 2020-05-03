import re


def left_join(phrases: tuple) -> str:
    p1 = ''
    for (y, n) in enumerate(phrases):
        if (len(phrases) - 1) == y:
            p1 += str(right_left(n))
            pass
        else:
            p1 += str(right_left(n))
            p1 += ","
    return p1


def right_left(rrr):
    rrr = re.sub('right', 'left', rrr.rstrip())
    return rrr


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
