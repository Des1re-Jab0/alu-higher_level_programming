#!/usr/bin/python3
"""Module that appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
