"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""

import re


def increment_string(string):
    pattern = r"[0-9]+(?=$)"
    match = re.search(pattern, string)
    if match:
        new_int = int(match.group(0)) + 1
        new_int = "{:0>{}}".format(new_int, len(str(match.group(0))))
        return re.sub(pattern, new_int, string)
    return string + '1'
