#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """text must be a string
    There should be no space at the beginning or at the end of
    each printed line
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = ""

    for i in text:
        new_text += i

        if i in [".", "?", ":"]:
            print("{}\n".format(new_text.strip()))
            new_text = ""

    if new_text.strip() != "":
        print("{}".format(new_text.strip()), end="")
