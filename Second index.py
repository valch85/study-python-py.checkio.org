def second_index(text: str, symbol: str) -> [int, None]:
    first_index = text.find(symbol)
    if first_index == -1:
        return None
    else:
        answer = text.find(symbol, first_index + 1)
        if answer == -1:
            return None
        else:
            return answer


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')