#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """the class to define a square"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise ValueError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
