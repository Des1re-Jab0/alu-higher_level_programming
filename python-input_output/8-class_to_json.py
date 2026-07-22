#!/usr/bin/python3
"""Module that returns the dictionary description of an object."""


def class_to_json(obj):
    """Return the serializable dictionary of a Class instance."""
    return obj.__dict__
