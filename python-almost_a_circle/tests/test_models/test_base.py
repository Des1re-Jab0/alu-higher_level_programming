#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
from models.base import Base


class TestBaseInit(unittest.TestCase):
    """Test cases for Base.__init__."""

    def test_id_public_attribute(self):
        """Test that id is set as a public attribute."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_id_none_increments_nb_objects(self):
        """Test that a None id assigns an incremented value."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_explicit_does_not_increment(self):
        """Test that giving an explicit id keeps ordering correct."""
        b1 = Base()
        Base(100)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)

    def test_id_is_integer(self):
        """Test that a default-assigned id is an integer."""
        b = Base()
        self.assertIsInstance(b.id, int)

    def test_id_zero(self):
        """Test explicitly passing id as 0."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test explicitly passing a negative id."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_string(self):
        """Test explicitly passing a string as id."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")


class TestBaseToJSONString(unittest.TestCase):
    """Test cases for Base.to_json_string."""

    def test_none_returns_brackets(self):
        """Test that None returns the string [] ."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list_returns_brackets(self):
        """Test that an empty list returns the string [] ."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """Test conversion of a list of dictionaries to JSON."""
        list_dicts = [{"id": 1, "width": 10, "height": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(
            result, '[{"id": 1, "width": 10, "height": 2}]')

    def test_returns_string_type(self):
        """Test that the return type is a string."""
        result = Base.to_json_string([{"id": 1}])
        self.assertIsInstance(result, str)

    def test_multiple_dicts(self):
        """Test conversion of multiple dictionaries."""
        list_dicts = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(result, '[{"id": 1}, {"id": 2}]')


class TestBaseFromJSONString(unittest.TestCase):
    """Test cases for Base.from_json_string."""

    def test_none_returns_empty_list(self):
        """Test that None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string_returns_empty_list(self):
        """Test that an empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json_string(self):
        """Test conversion of a valid JSON string to a list."""
        json_string = '[{"id": 1, "width": 10}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"id": 1, "width": 10}])

    def test_returns_list_type(self):
        """Test that the return type is a list."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertIsInstance(result, list)

    def test_round_trip_with_to_json_string(self):
        """Test that from_json_string reverses to_json_string."""
        original = [{"id": 1}, {"id": 2}]
        json_str = Base.to_json_string(original)
        result = Base.from_json_string(json_str)
        self.assertEqual(result, original)


if __name__ == "__main__":
    unittest.main()
