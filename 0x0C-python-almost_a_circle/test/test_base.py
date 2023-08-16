#!/usr/bin/python3
"""
    Unittest for the create function of the Base class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
        test for Base
    """
    def test_creation_id(self):
        """
            test if value of id has the good assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(9)
        b4 = Base(-5)
        b5 = Base(6.3)
        b6 = Base()
        b7 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 9)
        self.assertEqual(b4.id, -5)
        self.assertEqual(b5.id, 6.3)
        self.assertEqual(b6.id, 4)
        self.assertEqual(b7.id, 5)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])

    def test_rectangle_create(self):
        """test rectangle creation"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_square_create(self):
        """test square creation"""
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
if __name__ == "__main__":
    unittest.main()
