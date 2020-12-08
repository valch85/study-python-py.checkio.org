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

# These "asserts" are used for self-checking and not for testing
between_markers('What is >apple<', '>', '<') #== "apple", "One sym"
between_markers("<head><title>My new site</title></head>", "<title>", "</title>") #== "My new site", "HTML"
between_markers('No[/b] hi', '[b]', '[/b]') #== 'No', 'No opened'
between_markers('No [b]hi', '[b]', '[/b]') #== 'hi', 'No close'
between_markers('No hi', '[b]', '[/b]') #== 'No hi', 'No markers at all'
between_markers('No <hi>', '>', '<') #== '', 'Wrong direction'
