#!/usr/bin/python3
"""Module that defines a Student class able to reload from JSON."""


class Student:
    """Represents a student that can serialize and reload itself."""

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

    def reload_from_json(self, json):
        """Replace all attributes of the Student from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
