def words_order(text: str, words: list) -> bool:
    text_list = text.split(" ")
    agregator = []
    if len(words) > len(set(words)):
        return False
    for index, word in enumerate(words):
        if word in text_list:
            agregator.append(text_list.index(word))
        else:
            return False
    if sorted(agregator) == agregator:
        return True
    else:
        return False

"""    
    text_words = []
    for w in text.split():
        if w in words:
            text_words.append(w)
    if sorted(text_words, key=text.index) == words:
        return True
    else:
        return False
"""

if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

