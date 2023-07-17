#!/usr/bin/python3
"""Test Square"""
import unittest
from models.square import Square
from models.base import Base


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_square_with_args(self):
        s = Square(5, 2, 8, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 1)

    def test_square_without_id(self):
        s = Square(5, 2, 8)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 2)

    def test_square_defaults(self):
        s = Square(3)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 3)

    def test_square_with_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_square_with_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_with_negative_x(self):
        with self.assertRaises(ValueError):
            Square(5, -2, 8)

    def test_square_with_negative_y(self):
        with self.assertRaises(ValueError):
            Square(5, 2, -8)

    def test_square_with_float_size(self):
        with self.assertRaises(TypeError):
            Square(5.5)

    def test_square_with_string_x(self):
        with self.assertRaises(TypeError):
            Square(5, "x", 8)

    def test_square_with_string_y(self):
        with self.assertRaises(TypeError):
            Square(5, 2, "y")

    def test_square_with_list_size(self):
        with self.assertRaises(TypeError):
            Square([5], 8)

    def test_square_with_dict_x(self):
        with self.assertRaises(TypeError):
            Square(5, {"x": 2}, 8)


class TestSquareProperties(unittest.TestCase):
    """Unittests for testing properties of the Square class."""

    def test_square_size_property(self):
        s = Square(5)
        s.size = 8
        self.assertEqual(s.size, 8)

    def test_square_x_property(self):
        s = Square(5)
        s.x = 3
        self.assertEqual(s.x, 3)

    def test_square_y_property(self):
        s = Square(5)
        s.y = 6
        self.assertEqual(s.y, 6)

    def test_square_size_property_with_negative_value(self):
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -8

    def test_square_x_property_with_string(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.x = "3"

    def test_square_y_property_with_float_value(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.y = 6.5


class TestSquareArea(unittest.TestCase):
    """Unittests for testing area method of the Square class."""

    def test_square_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_area_with_size_zero(self):
        s = Square(0)
        self.assertEqual(s.area(), 0)


class TestSquareDisplay(unittest.TestCase):
    """Unittests for testing display method of the Square class."""

    def test_square_display(self):
        s = Square(3)
        expected_output = "###\n###\n###"
        with self.assertLogs() as logs:
            s.display()
        self.assertEqual("\n".join(logs.output), expected_output)

    def test_square_display_with_x_y(self):
        s = Square(3, 2, 1)
        expected_output = "\n  ###\n  ###\n  ###"
        with self.assertLogs() as logs:
            s.display()
        self.assertEqual("\n".join(logs.output), expected_output)


class TestSquareStrRepr(unittest.TestCase):
    """Unittests for testing __str__ and __repr__ methods of the Square class."""

    def test_square_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_square_repr(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(repr(s), "Square(4, 2, 1, 12)")

if __name__ == "__main__":
    unittest.main()
