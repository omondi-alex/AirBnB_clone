#!/usr/bin/python3
"""
File: place.py

Author:
    Samson Tedla <samitedla23@gmail.com>
    Elnatan Samuel <krosection999@gmail.com>

Defines a class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A class that represents a Place inheriting from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
