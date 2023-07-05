#!/usr/bin/python3
"""Unit tests for find_maximum function."""

import unittest
find_maximum = __import__('6-find_maximum').find_maximum


class TestFindMaximum(unittest.TestCase):

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(find_maximum(ordered_list), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered_list = [1, 2, 4, 3]
        self.assertEqual(find_maximum(unordered_list), 4)

    def test_max_at_beginning(self):
        """Test a list with the maximum value at the beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(find_maximum(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty_list = []
        self.assertEqual(find_maximum(empty_list), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element_list = [7]
        self.assertEqual(find_maximum(one_element_list), 7)

    def test_floats(self):
        """Test a list of floats."""
        float_list = [1.2, 3.5, -2.9, 7.8, 4.1]
        self.assertEqual(find_maximum(float_list), 7.8)

    def test_ints_and_floats(self):
        """Test a list of integers and floats."""
        ints_and_floats = [1.5, 10, -5, 8, 3.2]
        self.assertEqual(find_maximum(ints_and_floats), 10)

    def test_string(self):
        """Test a string."""
        string = "Hello World"
        self.assertEqual(find_maximum(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        string_list = ["Hello", "World", "Python"]
        self.assertEqual(find_maximum(string_list), "World")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(find_maximum(""), None)


if __name__ == '__main__':
    unittest.main()
