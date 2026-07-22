#!/usr/bin/python3
"""Module that adds a new attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj if it supports it."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
