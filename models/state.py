#!/usr/bin/python3
"""
This script defines a State class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A class representing a state, inheriting from BaseModel.

    Attributes:
    - name (str): The name of the state.
    """
    name = ""
