#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """Represents a square whose size is accessed via a property."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: the size of the new square, must be a positive integer.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating it.

        Args:
            value: the new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
