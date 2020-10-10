def backward_string_by_word(text: str) -> str:
    reverce = ""
    for (z, i) in enumerate(text.split(" ")):
        if len(text.split(" ")) - 1 == z:
            reverce += i[::-1]
        else:
            reverce += i[::-1] + " "
    return reverce


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
