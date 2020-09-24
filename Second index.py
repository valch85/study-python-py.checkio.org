def second_index(text: str, symbol: str) -> [int, None]:

    # your code here
    return 0



second_index("sims", "s") #== 3, "First"
second_index("find the river", "e") #== 12, "Second"
second_index("hi", " ") #is None, "Third"
second_index("hi mayor", " ") #is None, "Fourth"
second_index("hi mr Mayor", " ") #== 5, "Fifth"
