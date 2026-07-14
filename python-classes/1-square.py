#!/usr/bin/python3
"""Module that defines a Square class with a private size."""


class Square:
    """Represents a square defined by its private size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the size of the new square.
        """
        self.__size = size
