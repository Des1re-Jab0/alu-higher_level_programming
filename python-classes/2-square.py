#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


class Square:
    """Represents a square with a validated private size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: the size of the new square, must be a positive integer.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
