#!/usr/bin/python3
"""modules"""
import json


class Base:
    """base class.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing Base
        Args:
            id: The base id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """json convertor"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
