#!/usr/bin/python3
"""This defines the Amenity class."""
from models.base_model import BaseModel
from models import storage

class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
