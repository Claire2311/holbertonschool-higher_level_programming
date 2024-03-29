#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """the class to define a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        if not isinstance(size, int):
            raise ValueError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and \
            isinstance(value[0], int) and isinstance(value[1], int) and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print('')
        for i in range(self.position[1]):
            print("")

        for x in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
