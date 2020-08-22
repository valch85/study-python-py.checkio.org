def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    return ''

# These "asserts" are used for self-checking and not for testing
between_markers('What is >apple<', '>', '<') #== "apple", "One sym"
between_markers("<head><title>My new site</title></head>", "<title>", "</title>") #== "My new site", "HTML"
between_markers('No[/b] hi', '[b]', '[/b]') #== 'No', 'No opened'
between_markers('No [b]hi', '[b]', '[/b]') #== 'hi', 'No close'
between_markers('No hi', '[b]', '[/b]') #== 'No hi', 'No markers at all'
between_markers('No <hi>', '>', '<') #== '', 'Wrong direction'
