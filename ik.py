#!/usr/bin/python3

"""
The functions in this file were written to solve the problems described by:
https://www.interviewkickstart.com/blog/advanced-python-coding-challenges
"""


import calendar


def check_dup_letters(foo):
    """Write a function in Python to check duplicate letters.  It must accept a string, i.e., a sentence.  The function
    should return True if the sentence has any word with duplicate letters, else return False."""
    foo = foo.lower()
    for i in foo:
        if foo.count(i) > 1:
            return True
    return False


def morse(foo):
    """ Write a code in Python to create a Morse code translator.  You can take a string with alphanumeric characters in
    lower or upper case.  The string can also have any special characters as a part of the Morse code.  Special
    characters can include commas, colons, apostrophes, exclamation marks, periods, and question marks.  The code
    should return the Morse code that is equivalent to the string."""

    morse_dict = {  # copied from https://www.educative.io/answers/how-to-write-a-morse-code-translator-in-python
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ',': '--..--', ':': '---...', "'": '.----.', '!': '-.-.--', '.': '.-.-.-', '?': '..--..',
        ' ': '/'
    }

    foo = foo.upper()
    ret = ''
    for i in foo:
        if i in morse_dict:
            ret += morse_dict[i] + ' '
    return ret


def fri13(month, year):
    """Write a function to detect 13th Friday.  The function can accept two parameters, and both will be numbers.
    The first parameter will be the number indicating the month, and the second will be the year in four digits.
    Your function should parse the parameters, and it must return True when the month contains a Friday with the
    13th, else return False."""

    f = calendar.weekday(year, month, 13)
    return f == calendar.FRIDAY


if __name__ == '__main__':
    a = ("QWERTY", "QWEeRTYq")
    for i in a:
        print('The string "' + i + '" has duplicate letters:', check_dup_letters(i))
    print()

    b = "The quick brown fox jumped over the lazy dog."
    print("Morse code follows for:", b)
    print(morse(b))
    print()

    c = [(5, 2022), (9, 2023)]
    cal = calendar.TextCalendar()
    for i in c:
        # print("Here is the calendar for " + str(i[0]) + '/' + str(i[1]))
        cal.prmonth(i[1], i[0])
        print("The 13th is a Friday:", fri13(i[0], i[1]))
        print()
