#!/usr/bin/python3
"""
function that prints My name is <first name> <last name>
>>> say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """first_name and last_name must be strings"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
