def letter_check(password):
    passlist = []
    #fase 1
    for c in password.lower():
        print("fase 1" + " = " + str(c))
        if len(passlist) == 3:
            return False
        else:
            # fase 2
            if len(passlist) == 0:
                print("fase 2" + " = " + str(c))
                passlist.append(c)
            else:
                # fase 3
                 if c == passlist[-1]:
                    print("fase 3" + " = " + str(c))
                    passlist.append(c)
                 else:
                    # fase 4
                    passlist = []
                    print("fase 4" + " = " + str(c))
                    passlist.append(c)
    return True


print(letter_check('aaaaaabb1'))# == False


def remove_space(text: str):
    new_text = ""
    for char in text:
        if char.isspace:
            pass
        else:
            new_text = str(new_text) + str(char)
    print("new text is = " + str(new_text))

remove_space('all 123 LETTERS! ')






========

