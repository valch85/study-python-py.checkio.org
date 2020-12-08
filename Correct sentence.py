def correct_sentence(text: str) -> str:
    return text


correct_sentence("greetings, friends") #== "Greetings, friends."
correct_sentence("Greetings, friends") #== "Greetings, friends."
correct_sentence("Greetings, friends.") #== "Greetings, friends."
correct_sentence("hi") #== "Hi."
correct_sentence("welcome to New York") #== "Welcome to New York."
