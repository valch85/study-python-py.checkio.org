
def is_acceptable_password(password: str) -> bool:
    if len(password) > 9:
        return True
    elif len(password) > 6 and any(c.isdigit() for c in password) and not all(c.isdigit() for c in password) and any(c.lower().islower() for c in password):
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
print(is_acceptable_password('short')) #== False
print(is_acceptable_password('short54')) #== True
print(is_acceptable_password('muchlonger')) #== True
print(is_acceptable_password('ashort')) #== False
print(is_acceptable_password('1234567')) #== False
print(is_acceptable_password('12345678910')) #== True