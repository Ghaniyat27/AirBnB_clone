#!/usr/bin/python3
"""
This is the User creation class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
