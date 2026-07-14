#!/usr/bin/python3
"""Module that reproduces a given Python bytecode as a class."""
import math


class MagicClass:
    """Represents a circle defined by its radius."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius: the radius of the circle, must be a number.

        Raises:
            TypeError: if radius is not an int or a float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
