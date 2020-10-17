MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }


def morse_convert(morse):
    # go through each key, value and find relevant
    for key, value in MORSE.items():
        if morse == key:
            return value
    return "key doesn't exist"


def morse_decoder(code):
    # split by words (delimiter 3 spaces)
    code_split = code.split('   ')
    # line var to add words after conversion
    one_line = ""
    # go through each word
    for word in code_split:
        # split buy letters (delimiter 1 space)
        word_split = word.split()
        # word var to add letters after conversion
        one_word = ""

        # go through each letter
        for letter in word_split:
            # run morse_convert func and add result to word var
            one_word = one_word + str(morse_convert(letter))

        # add result to line var with space after each word
        one_line = one_line + one_word + " "

    # capitalize the line
    output = one_line.capitalize()
    # remove space at the end of the line if exists
    if str(output[-1]) == " ":
        output = output[:-1]

    return output


morse_decoder("... --- -- .   - . -..- -") #== "Some text"
morse_decoder("..--- ----- .---- ---..") #== "2018"
morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") #== "It was a good day"

