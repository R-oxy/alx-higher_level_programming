#!/usr/bin/python3
"""Test Base"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 92)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 177)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 66)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 128)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveAndLoadFromFile(unittest.TestCase):
    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_and_load_from_file(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        s1 = Square(5)
        s2 = Square(6)
        list_objs = [r1, r2, s1, s2]

        # Save objects to file
        Base.save_to_file(list_objs)

        # Load objects from file
        loaded_objs = Base.load_from_file()

        # Check number of loaded objects
        self.assertEqual(len(loaded_objs), 4)

        # Check object types
        self.assertIsInstance(loaded_objs[0], Rectangle)
        self.assertIsInstance(loaded_objs[1], Rectangle)
        self.assertIsInstance(loaded_objs[2], Square)
        self.assertIsInstance(loaded_objs[3], Square)

        # Check object attributes
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[0].width, 1)
        self.assertEqual(loaded_objs[0].height, 2)
        self.assertEqual(loaded_objs[0].x, 0)
        self.assertEqual(loaded_objs[0].y, 0)

        self.assertEqual(loaded_objs[1].id, 2)
        self.assertEqual(loaded_objs[1].width, 3)
        self.assertEqual(loaded_objs[1].height, 4)
        self.assertEqual(loaded_objs[1].x, 0)
        self.assertEqual(loaded_objs[1].y, 0)

        self.assertEqual(loaded_objs[2].id, 3)
        self.assertEqual(loaded_objs[2].size, 5)
        self.assertEqual(loaded_objs[2].x, 0)
        self.assertEqual(loaded_objs[2].y, 0)

        self.assertEqual(loaded_objs[3].id, 4)
        self.assertEqual(loaded_objs[3].size, 6)
        self.assertEqual(loaded_objs[3].x, 0)
        self.assertEqual(loaded_objs[3].y, 0)


class TestBaseSaveAndLoadFromFileCSV(unittest.TestCase):
    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_and_load_from_file_csv(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        s1 = Square(5)
        s2 = Square(6)
        list_objs = [r1, r2, s1, s2]

        # Save objects to CSV file
        Base.save_to_file_csv(list_objs)

        # Load objects from CSV file
        loaded_objs = Base.load_from_file_csv()

        # Check number of loaded objects
        self.assertEqual(len(loaded_objs), 4)

        # Check object types
        self.assertIsInstance(loaded_objs[0], Rectangle)
        self.assertIsInstance(loaded_objs[1], Rectangle)
        self.assertIsInstance(loaded_objs[2], Square)
        self.assertIsInstance(loaded_objs[3], Square)

        # Check object attributes
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[0].width, 1)
        self.assertEqual(loaded_objs[0].height, 2)
        self.assertEqual(loaded_objs[0].x, 0)
        self.assertEqual(loaded_objs[0].y, 0)

        self.assertEqual(loaded_objs[1].id, 2)
        self.assertEqual(loaded_objs[1].width, 3)
        self.assertEqual(loaded_objs[1].height, 4)
        self.assertEqual(loaded_objs[1].x, 0)
        self.assertEqual(loaded_objs[1].y, 0)

        self.assertEqual(loaded_objs[2].id, 3)
        self.assertEqual(loaded_objs[2].size, 5)
        self.assertEqual(loaded_objs[2].x, 0)
        self.assertEqual(loaded_objs[2].y, 0)

        self.assertEqual(loaded_objs[3].id, 4)
        self.assertEqual(loaded_objs[3].size, 6)
        self.assertEqual(loaded_objs[3].x, 0)
        self.assertEqual(loaded_objs[3].y, 0)


if __name__ == '__main__':
    unittest.main()
