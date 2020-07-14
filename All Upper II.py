def is_all_upper(text: str) -> bool:
    converted_text_without_space = text.replace(" ", "")
    converted_text = ''.join([i for i in converted_text_without_space if not i.isdigit()])
    if len(converted_text) <= 0:
        return False
    elif not all(map(str.isalpha, converted_text)):
        return False
    else:
        if text == text.upper():
            return True
        else:
            return False


if __name__ == '__main__':
    print("Example:")
    # These "asserts" are used for self-checking and not for an auto-testing
    print(is_all_upper('ALL UPPER'))# == True
    print(is_all_upper('all lower'))# == False
    print(is_all_upper('mixed UPPER and lower'))# == False
    print(is_all_upper(' '))# == False
    print(is_all_upper('DSFS123'))  # == True
    print(is_all_upper('123')) # == False

