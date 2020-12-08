def correct_sentence(text: str) -> str:
    if text[-1] != ".":
        text = text + "."
    text = text[0].upper() + text[1:]
    return text


correct_sentence("greetings, friends") #== "Greetings, friends."
correct_sentence("Greetings, friends") #== "Greetings, friends."
correct_sentence("Greetings, friends.") #== "Greetings, friends."
correct_sentence("hi") #== "Hi."
correct_sentence("welcome to New York") #== "Welcome to New York."
