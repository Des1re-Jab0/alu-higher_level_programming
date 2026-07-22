#!/usr/bin/python3
"""Module that defines a printable Square based on Rectangle."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square that prints its own description."""

    def __init__(self, size):
        """Initialize a new Square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description [Square] <w>/<h>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
