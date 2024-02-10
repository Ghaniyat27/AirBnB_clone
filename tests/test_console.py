#!/usr/bin/python3
"""Examine the console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class test console"""

    def create(self):
        """creates the instance"""
        return HBNBCommand()

    def test_quit(self):
        """ examine the quit method
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """examine the EQF method
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
