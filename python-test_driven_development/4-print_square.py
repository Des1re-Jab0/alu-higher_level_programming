#!/usr/bin/python3
"""Module that prints a square of hash characters.

Defines print_square, which prints a size x size square using
the # character.
"""


def print_square(size):
    """Print a square of # characters with the given side length.

    Raises a TypeError if size is not an integer, or a ValueError
    if size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
