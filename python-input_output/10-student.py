#!/usr/bin/python3
"""Module that defines a Student class with filtered serialization."""


class Student:
    """Represents a student that can serialize selected attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary of the Student, optionally filtered."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
