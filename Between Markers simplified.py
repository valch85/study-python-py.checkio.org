def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text:
        start = text.find(begin) + len(begin)
    else:
        start = -1
    ending = text.find(end)
    if ending > 0 and start > ending:
        return ""
    elif start < 0 and ending < 0:
        return text
    elif start < 0:
        return text[0:ending]
    elif ending < 0:
        return text[start:]
    else:
        return text[start:ending]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')

