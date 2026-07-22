#!/usr/bin/python3
"""Module that defines a Rectangle based on BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle validated by BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
