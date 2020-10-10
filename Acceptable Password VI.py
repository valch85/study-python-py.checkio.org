# Taken from mission Acceptable Password V
# Taken from mission Acceptable Password IV
# Taken from mission Acceptable Password III
# Taken from mission Acceptable Password II
# Taken from mission Acceptable Password I
import re


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6 and has_didgit(password):
        return True
    else:
        return False


def has_didgit(password):
    return bool(re.search(r'\d', password))


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6 and any(c.isdigit() for c in password) and any(c.lower().islower() for c in password):
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    if len(password) > 9:
        return True
    elif len(password) > 6 and any(c.isdigit() for c in password) and not all(c.isdigit() for c in password) and any(
            c.lower().islower() for c in password):
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password):
    if "password" in password.lower():
        return False
    if len(password) > 9 and len(set(password)) >= 3:
        return True
    elif len(password) > 6 and any(map(str.isdigit, password)) and not password.isdigit() and len(set(password)) >= 3:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
