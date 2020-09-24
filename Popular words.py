def popular_words(text: str, words: list) -> dict:
    low_text = text.lower()
    print(low_text)


popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near'])

#== {
#        'i': 4,
#        'was': 3,
#        'three': 0,
#        'near': 0
#    }


