#!/usr/bin/python3
"""Module that defines a Square class able to compute its area."""


class Square:
    """Represents a square that can compute its own area."""

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

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
