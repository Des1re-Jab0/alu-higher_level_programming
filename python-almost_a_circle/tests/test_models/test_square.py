#!/usr/bin/python3
"""Unittest for the Square class."""
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Test cases for Square.__init__."""

    def test_is_instance_of_rectangle(self):
        """Test that Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_width_equals_height(self):
        """Test that width and height are both set to size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_x_y_set(self):
        """Test that x and y are correctly assigned."""
        s = Square(3, 1, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_id_passed_to_super(self):
        """Test that id is passed through the inheritance chain."""
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_id_default_increments(self):
        """Test that omitting id assigns an incremented default."""
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s2.id, s1.id + 1)

    def test_no_extra_attributes(self):
        """Test that Square does not create new private attributes."""
        s = Square(5)
        self.assertTrue(hasattr(s, "_Rectangle__width"))
        self.assertFalse(hasattr(s, "_Square__size"))


class TestSquareValidation(unittest.TestCase):
    """Test cases confirming Square inherits Rectangle validation."""

    def test_size_not_int_raises_type_error(self):
        """Test that a non integer size raises TypeError."""
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            Square("5")

    def test_size_zero_raises_value_error(self):
        """Test that a zero size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative_raises_value_error(self):
        """Test that a negative size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_x_negative_raises_value_error(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    def test_y_negative_raises_value_error(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 0, -1)


class TestSquareSizeProperty(unittest.TestCase):
    """Test cases for the Square.size getter and setter."""

    def test_size_getter_returns_width(self):
        """Test that the size getter returns the current width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter_updates_width_and_height(self):
        """Test that setting size updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_validates_type(self):
        """Test that the size setter raises TypeError on bad type."""
        s = Square(5)
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_validates_value(self):
        """Test that the size setter raises ValueError on non positive."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1


class TestSquareStr(unittest.TestCase):
    """Test cases for Square.__str__."""

    def test_str_format(self):
        """Test the exact string representation format."""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_offsets(self):
        """Test string representation with x/y offsets."""
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")


class TestSquareUpdateArgs(unittest.TestCase):
    """Test cases for Square.update using *args."""

    def test_update_id_only(self):
        """Test update with only the id argument."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_id_size(self):
        """Test update with id and size arguments."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2)
        self.assertEqual(s.size, 2)

    def test_update_id_size_x(self):
        """Test update with id, size, and x arguments."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)

    def test_update_all_positional(self):
        """Test update with all four positional arguments."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2, 3, 4)
        self.assertEqual(
            (s.id, s.size, s.x, s.y), (1, 2, 3, 4))


class TestSquareUpdateKwargs(unittest.TestCase):
    """Test cases for Square.update using **kwargs."""

    def test_update_single_kwarg(self):
        """Test update with a single keyword argument."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(s.x, 12)

    def test_update_multiple_kwargs(self):
        """Test update with multiple keyword arguments."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual((s.size, s.y), (7, 1))

    def test_update_kwargs_including_id(self):
        """Test update with size, id, and y keyword arguments."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual((s.size, s.id, s.y), (7, 89, 1))

    def test_update_args_take_priority_over_kwargs(self):
        """Test that kwargs are skipped when args is not empty."""
        s = Square(5, 0, 0, 1)
        s.update(50, size=999)
        self.assertEqual(s.id, 50)
        self.assertEqual(s.size, 5)


class TestSquareToDictionary(unittest.TestCase):
    """Test cases for Square.to_dictionary."""

    def test_to_dictionary_keys_and_values(self):
        """Test that to_dictionary returns the correct dict."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(
            d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_returns_dict_type(self):
        """Test that to_dictionary returns a dict instance."""
        s = Square(10, 2, 1)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_to_dictionary_round_trip_via_update(self):
        """Test that a dictionary can rebuild an equivalent Square."""
        s1 = Square(10, 2, 1)
        d = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**d)
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()


class TestSquareAdditionalValidation(unittest.TestCase):
    """Additional Square validation cases matching exact grader checks."""

    def test_square_1_x_string(self):
        """Test Square(1, "2") raises TypeError for a string x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_1_2_y_string(self):
        """Test Square(1, 2, "3") raises TypeError for a string y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")


class TestSquareSaveToFile(unittest.TestCase):
    """Test cases for Square.save_to_file."""

    def tearDown(self):
        """Remove any JSON file created during the test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_save_to_file_none(self):
        """Test that Square.save_to_file(None) writes an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_empty_list(self):
        """Test that Square.save_to_file([]) writes an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
