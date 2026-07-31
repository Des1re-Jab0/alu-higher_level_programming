#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Test cases for Rectangle.__init__."""

    def test_is_instance_of_base(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_width_height_set(self):
        """Test that width and height are correctly assigned."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_x_y_set(self):
        """Test that x and y are correctly assigned."""
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_id_passed_to_super(self):
        """Test that id is passed through to the Base constructor."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_id_default_increments(self):
        """Test that omitting id assigns an incremented default."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, r1.id + 1)


class TestRectangleValidation(unittest.TestCase):
    """Test cases for Rectangle attribute validation."""

    def test_width_not_int_raises_type_error(self):
        """Test that a non integer width raises TypeError."""
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            Rectangle("2", 10)

    def test_height_not_int_raises_type_error(self):
        """Test that a non integer height raises TypeError."""
        with self.assertRaisesRegex(
                TypeError, "height must be an integer"):
            Rectangle(10, "10")

    def test_x_not_int_raises_type_error(self):
        """Test that a non integer x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_y_not_int_raises_type_error(self):
        """Test that a non integer y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, {})

    def test_width_zero_raises_value_error(self):
        """Test that a zero width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative_raises_value_error(self):
        """Test that a negative width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_zero_raises_value_error(self):
        """Test that a zero height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative_raises_value_error(self):
        """Test that a negative height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_negative_raises_value_error(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_y_negative_raises_value_error(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_x_zero_is_valid(self):
        """Test that x equal to 0 is valid."""
        r = Rectangle(10, 2, 0, 5)
        self.assertEqual(r.x, 0)

    def test_y_zero_is_valid(self):
        """Test that y equal to 0 is valid."""
        r = Rectangle(10, 2, 5, 0)
        self.assertEqual(r.y, 0)

    def test_setter_validates_width(self):
        """Test that setting width via setter re-validates."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_setter_validates_x(self):
        """Test that setting x via setter re-validates."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}

    def test_bool_not_treated_as_valid_int(self):
        """Test that a bool is technically accepted (subclass of int)."""
        r = Rectangle(10, 2)
        r.width = True
        self.assertEqual(r.width, 1)


class TestRectangleArea(unittest.TestCase):
    """Test cases for Rectangle.area."""

    def test_area_basic(self):
        """Test area of a simple rectangle."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_with_offsets(self):
        """Test area is unaffected by x/y offsets."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_area_square_shape(self):
        """Test area when width equals height."""
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)


class TestRectangleDisplay(unittest.TestCase):
    """Test cases for Rectangle.display."""

    def capture_display(self, rect):
        """Helper to capture display() stdout output."""
        captured = io.StringIO()
        sys.stdout = captured
        rect.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_display_no_offset(self):
        """Test display with no x/y offset."""
        r = Rectangle(2, 2)
        output = self.capture_display(r)
        self.assertEqual(output, "##\n##\n")

    def test_display_with_x_offset(self):
        """Test display with an x offset adds leading spaces."""
        r = Rectangle(3, 2, 1, 0)
        output = self.capture_display(r)
        self.assertEqual(output, " ###\n ###\n")

    def test_display_with_y_offset(self):
        """Test display with a y offset adds leading newlines."""
        r = Rectangle(2, 3, 2, 2)
        output = self.capture_display(r)
        self.assertEqual(output, "\n\n  ##\n  ##\n  ##\n")


class TestRectangleStr(unittest.TestCase):
    """Test cases for Rectangle.__str__."""

    def test_str_format(self):
        """Test the exact string representation format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_id(self):
        """Test string representation with a default assigned id."""
        r = Rectangle(5, 5, 1)
        self.assertEqual(
            str(r), "[Rectangle] ({}) 1/0 - 5/5".format(r.id))


class TestRectangleUpdateArgs(unittest.TestCase):
    """Test cases for Rectangle.update using *args."""

    def test_update_id_only(self):
        """Test update with only the id argument."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        """Test update with id and width arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual((r.id, r.width), (89, 2))

    def test_update_id_width_height(self):
        """Test update with id, width, and height arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual((r.id, r.width, r.height), (89, 2, 3))

    def test_update_all_positional(self):
        """Test update with all five positional arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 2, 3, 4, 5))

    def test_update_no_args_no_change(self):
        """Test update with no arguments changes nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (1, 10, 10, 10, 10))


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Test cases for Rectangle.update using **kwargs."""

    def test_update_single_kwarg(self):
        """Test update with a single keyword argument."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_multiple_kwargs(self):
        """Test update with multiple keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, x=2)
        self.assertEqual((r.width, r.x), (1, 2))

    def test_update_kwargs_order_independent(self):
        """Test that keyword argument order does not matter."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(
            (r.id, r.width, r.x, r.y), (89, 2, 3, 1))

    def test_update_args_take_priority_over_kwargs(self):
        """Test that kwargs are skipped when args is not empty."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(50, height=999)
        self.assertEqual(r.id, 50)
        self.assertEqual(r.height, 10)


class TestRectangleToDictionary(unittest.TestCase):
    """Test cases for Rectangle.to_dictionary."""

    def test_to_dictionary_keys_and_values(self):
        """Test that to_dictionary returns the correct dict."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": r.id, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_returns_dict_type(self):
        """Test that to_dictionary returns a dict instance."""
        r = Rectangle(10, 2, 1, 9)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_round_trip_via_update(self):
        """Test that a dictionary can rebuild an equivalent Rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        d = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**d)
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
