#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """a and b must be integers or floats
    a and b must be first casted to integers if they are float
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    return a + b


print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
print(add_integer('cool', -2))
