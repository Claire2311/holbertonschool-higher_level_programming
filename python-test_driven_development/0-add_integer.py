#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    return a + b

    # if not (isinstance(a, int) or isinstance(a, float)):
    #     raise TypeError('a must be an integer')
    # elif not (isinstance(b, int) or isinstance(b, float)):
    #     raise TypeError('b must be an integer')
    # elif isinstance(a, float)


print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
print(add_integer('cool', -2))
