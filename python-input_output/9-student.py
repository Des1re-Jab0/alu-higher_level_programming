#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization."""


class Student:
    """Represents a student that can serialize to a dictionary."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of the Student."""
        return self.__dict__
