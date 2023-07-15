#!/usr/bin/python3
"""
Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Args:
        BaseModel ([class]): class that inherited by Place
    """

    name = ""
    description = ""
    number_bathrooms = 0
    city_id = ""
    user_id = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
