#!/usr/bin/python3

"""
    unittest for user model.
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    """
        Examining User class
    """

    def test_City_inheritance(self):
        """
            examines that the City class Inherits from the BaseModel
        """
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_type_name(self):
        """
            Examined the type of name
        """
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        """
            Examine the type of name
        """
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)
