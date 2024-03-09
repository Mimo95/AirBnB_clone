#!/usr/bin/python3
"""
This script defines an Amenity class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class representing an amenity, inheriting from BaseModel.

    Attributes:
    - name (str): The name of the amenity.
    """
    name = ""
