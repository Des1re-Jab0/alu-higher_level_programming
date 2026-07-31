#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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


class TestBaseSaveToFile(unittest.TestCase):
    """Test cases for Base.save_to_file."""

    def tearDown(self):
        """Remove any JSON files created during the test."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_creates_file(self):
        """Test that save_to_file creates the expected file."""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_none_creates_empty_list_file(self):
        """Test that saving None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_content_matches_dictionaries(self):
        """Test that the saved JSON matches the objects' dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        expected = Rectangle.to_json_string(
            [r1.to_dictionary(), r2.to_dictionary()])
        self.assertEqual(content, expected)

    def test_save_overwrites_existing_file(self):
        """Test that save_to_file overwrites a pre-existing file."""
        r1 = Rectangle(10, 7)
        Rectangle.save_to_file([r1])
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, Rectangle.to_json_string(
            [r2.to_dictionary()]))


class TestBaseLoadFromFile(unittest.TestCase):
    """Test cases for Base.load_from_file."""

    def tearDown(self):
        """Remove any JSON files created during the test."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_missing_file_returns_empty_list(self):
        """Test that a missing file returns an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_returns_list_of_correct_type(self):
        """Test that loaded instances are of the correct class."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8)])
        result = Rectangle.load_from_file()
        self.assertIsInstance(result[0], Rectangle)

    def test_load_preserves_attributes(self):
        """Test that loaded instances preserve original attributes."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        result = Rectangle.load_from_file()
        self.assertEqual(str(result[0]), str(r1))

    def test_load_preserves_order_and_count(self):
        """Test that loaded instances match input order and count."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))

    def test_load_square_returns_square_instances(self):
        """Test loading works correctly for Square as well."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        result = Square.load_from_file()
        self.assertIsInstance(result[0], Square)
        self.assertEqual(str(result[0]), str(s1))
        self.assertEqual(str(result[1]), str(s2))


class TestBaseCreate(unittest.TestCase):
    """Test cases for Base.create."""

    def test_create_rectangle_from_dictionary(self):
        """Test creating a Rectangle instance from a dictionary."""
        r1 = Rectangle(3, 5, 1)
        d = r1.to_dictionary()
        r2 = Rectangle.create(**d)
        self.assertEqual(str(r1), str(r2))

    def test_create_square_from_dictionary(self):
        """Test creating a Square instance from a dictionary."""
        s1 = Square(10, 2, 1)
        d = s1.to_dictionary()
        s2 = Square.create(**d)
        self.assertEqual(str(s1), str(s2))

    def test_create_returns_new_instance(self):
        """Test that create returns a distinct object, not the same one."""
        r1 = Rectangle(3, 5, 1)
        d = r1.to_dictionary()
        r2 = Rectangle.create(**d)
        self.assertIsNot(r1, r2)


class TestBaseCSV(unittest.TestCase):
    """Test cases for Base.save_to_file_csv and load_from_file_csv."""

    def tearDown(self):
        """Remove any CSV files created during the test."""
        for filename in ("Rectangle.csv", "Square.csv"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_csv_creates_file(self):
        """Test that save_to_file_csv creates the expected file."""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file_csv([r])
        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_save_csv_none_creates_empty_file(self):
        """Test that saving None to CSV writes an empty file."""
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(), "")

    def test_csv_round_trip_rectangle(self):
        """Test a full CSV save/load round trip for Rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        result = Rectangle.load_from_file_csv()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))

    def test_csv_round_trip_square(self):
        """Test a full CSV save/load round trip for Square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        result = Square.load_from_file_csv()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(s1))
        self.assertEqual(str(result[1]), str(s2))

    def test_load_csv_missing_file_returns_empty_list(self):
        """Test that a missing CSV file returns an empty list."""
        self.assertEqual(Rectangle.load_from_file_csv(), [])
