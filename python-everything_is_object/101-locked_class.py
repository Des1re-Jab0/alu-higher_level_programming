#!/usr/bin/python3
"""Module that defines a class locking down new instance attributes."""


class LockedClass:
    """Prevents new instance attributes except first_name."""

    __slots__ = ["first_name"]
