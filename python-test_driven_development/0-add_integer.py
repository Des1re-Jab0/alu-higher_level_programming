#!/usr/bin/python3
"""Module that provides a function to add two integers.

This module defines add_integer, which adds two numbers after
casting any float arguments to integers first.
"""


def add_integer(a, b=98):
    """Add two integers, casting floats to integers first.

    Raises a TypeError if either argument is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
