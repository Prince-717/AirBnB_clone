#!/usr/bin/python3
"""
User class public class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Args:
        BaseModel ([class]): class biherited by User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
