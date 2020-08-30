import re
def between_markers(text: str, begin: str, end: str) -> str:
    print("")
    print("#####")
    print(text)
    if begin in text:
        start = text.find(begin) + len(begin)
    else:
        start = -1
    ending = text.find(end)
    print(start)
    print(ending)
    if ending > 0 and start > ending:
        print("")
    elif start < 0 and ending < 0:
        print("answer")
        print(text)
    elif start < 0:
        print("answer")
        print(text[0:ending])
    elif ending < 0:
        print("answer")
        print(text[start:])
    else:
        print(text[start:ending])
    #return ''
# These "asserts" are used for self-checking and not for testing
between_markers('What is >apple<', '>', '<') #== "apple", "One sym"
between_markers("<head><title>My new site</title></head>", "<title>", "</title>") #== "My new site", "HTML"
between_markers('No[/b] hi', '[b]', '[/b]') #== 'No', 'No opened'
between_markers('No [b]hi', '[b]', '[/b]') #== 'hi', 'No close'
between_markers('No hi', '[b]', '[/b]') #== 'No hi', 'No markers at all'
between_markers('No <hi>', '>', '<') #== '', 'Wrong direction'
