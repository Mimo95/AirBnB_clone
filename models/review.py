#!/usr/bin/python3
"""
This script defines a Review class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a review, inheriting from BaseModel.

    Attributes:
    - place_id (str): The ID of the place associated with the review.
    - user_id (str): The ID of the user who wrote the review.
    - text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
