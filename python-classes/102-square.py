#!/usr/bin/python3
"""Module that defines a comparable Square class."""


class Square:
    """Represents a square that can be compared by area."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: the size of the new square, must be a positive number.
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
            TypeError: if value is not a number.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this square's area is smaller."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square's area is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this square's area is bigger."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square's area is bigger or equal."""
        return self.area() >= other.area()
