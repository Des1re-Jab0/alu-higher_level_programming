#!/usr/bin/python3
"""Module that checks instance relationship including inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass."""
    return isinstance(obj, a_class)
