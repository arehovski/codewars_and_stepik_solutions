"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:
"""


def rgb(r, g, b):
    r, g, b = check_range(r), check_range(g), check_range(b)
    return '{:0>2}'.format(hex(r)[2:].upper()) + '{:0>2}'.format(hex(g)[2:].upper()) + '{:0>2}'.format(hex(b)[2:].upper())


def check_range(n):
    if n < 0:
        return 0
    elif n > 255:
        return 255
    return n
