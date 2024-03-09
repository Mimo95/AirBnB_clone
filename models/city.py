#!/usr/bin/python3
"""
This script defines a City class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class representing a city, inheriting from BaseModel.

    Attributes:
    - state_id (str): The ID of the state where the city is located.
    - name (str): The name of the city.
    """
    state_id = ""
    name = ""
