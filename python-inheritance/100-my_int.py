#!/usr/bin/python3
"""Module that defines a rebellious MyInt class."""


class MyInt(int):
    """Represents an int with == and != inverted."""

    def __eq__(self, other):
        """Return the inverted equality result."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return the inverted inequality result."""
        return int(self) == int(other)
