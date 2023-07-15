#!/usr/bin/python3
"""
Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Args:
        BaseModel ([class]): class that inherited by Review
    """
    place_id = ""
    user_id = ""
    text = ""
