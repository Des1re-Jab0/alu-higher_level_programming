#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ascending ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_default_argument(self):
        """Test calling with no argument uses the default."""
        self.assertIsNone(max_integer())

    def test_all_same_values(self):
        """Test with all identical values."""
        self.assertEqual(max_integer([2, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
