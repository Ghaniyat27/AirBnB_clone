#!/usr/bin/python3

"""
    unittest for amenity.py.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        Examining Amenity class
    """

    def test_Amenity_inheritence(self):
        """
        examines that the Amenity class Inherits from BaseModel
        """        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """
            Examined that Amenity class had a name attribute.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """
            examined that Amenity class had a name attribute's type.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)
