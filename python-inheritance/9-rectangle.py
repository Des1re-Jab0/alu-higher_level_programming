#!/usr/bin/python3
"""Module that defines a full Rectangle with area and printing."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle that can compute and print itself."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description [Rectangle] <w>/<h>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
