#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Represents the base of all geometry classes."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
