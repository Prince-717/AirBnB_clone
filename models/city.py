#!/usr/bin/python3
"""
Class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Args:
        BaseModel ([class]): class that inherited by City
    """
    state_id = ""
    name = ""
