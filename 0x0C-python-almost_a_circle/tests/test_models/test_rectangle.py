#!/usr/bin/python3
"""Test Rectangle"""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_with_args(self):
        r = Rectangle(5, 10, 2, 8, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)
        self.assertEqual(r.id, 1)

    def test_rectangle_without_id(self):
        r = Rectangle(5, 10, 2, 8)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)
        self.assertEqual(r.id, 2)

    def test_rectangle_defaults(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 3)

    def test_rectangle_with_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_rectangle_with_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_rectangle_with_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_rectangle_with_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_rectangle_with_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 8)

    def test_rectangle_with_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -8)

    def test_rectangle_with_float_width(self):
        with self.assertRaises(TypeError):
            Rectangle(5.5, 10)

    def test_rectangle_with_string_x(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "x", 8)

    def test_rectangle_with_string_y(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "y")

    def test_rectangle_with_list_width(self):
        with self.assertRaises(TypeError):
            Rectangle([5], 10)

    def test_rectangle_with_dict_x(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, {"x": 2}, 8)


class TestRectangleProperties(unittest.TestCase):
    """Unittests for testing properties of the Rectangle class."""

    def test_rectangle_width_property(self):
        r = Rectangle(5, 10)
        r.width = 8
        self.assertEqual(r.width, 8)

    def test_rectangle_height_property(self):
        r = Rectangle(5, 10)
        r.height = 15
        self.assertEqual(r.height, 15)

    def test_rectangle_x_property(self):
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)

    def test_rectangle_y_property(self):
        r = Rectangle(5, 10)
        r.y = 6
        self.assertEqual(r.y, 6)

    def test_rectangle_width_property_with_negative_value(self):
        r = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            r.width = -8

    def test_rectangle_height_property_with_zero_value(self):
        r = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            r.height = 0

    def test_rectangle_x_property_with_string(self):
        r = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            r.x = "3"

    def test_rectangle_y_property_with_float_value(self):
        r = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            r.y = 6.5


class TestRectangleArea(unittest.TestCase):
    """Unittests for testing area method of the Rectangle class."""

    def test_rectangle_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_rectangle_area_with_width_zero(self):
        r = Rectangle(0, 10)
        self.assertEqual(r.area(), 0)

    def test_rectangle_area_with_height_zero(self):
        r = Rectangle(5, 0)
        self.assertEqual(r.area(), 0)


class TestRectangleDisplay(unittest.TestCase):
    """Unittests for testing display method of the Rectangle class."""

    def test_rectangle_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###"
        with self.assertLogs() as logs:
            r.display()
        self.assertEqual("\n".join(logs.output), expected_output)

    def test_rectangle_display_with_x_y(self):
        r = Rectangle(3, 2, 2, 1)
        expected_output = "\n  ###\n  ###"
        with self.assertLogs() as logs:
            r.display()
        self.assertEqual("\n".join(logs.output), expected_output)


class TestRectangleStrRepr(unittest.TestCase):
    """Unittests for testing __str__ and __repr__ methods of the Rectangle class."""

    def test_rectangle_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

if __name__ == "__main__":
    unittest.main()
