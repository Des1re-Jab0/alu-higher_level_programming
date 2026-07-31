#!/usr/bin/python3
"""Module that formats text with indentation.

Defines text_indentation, which prints text with extra new
lines after each ., ? and : character.
"""


def text_indentation(text):
    """Print text with two new lines after each ., ? and : .

    Raises a TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ".?:"
    length = len(text)
    i = 0
    while i < length:
        print(text[i], end="")
        if text[i] in special_chars and i + 1 < length:
            print("\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1
