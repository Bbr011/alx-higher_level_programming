#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of, or if obj is an instance of a class that inherited from, a_class.

    Parameters:
    obj: object
        The object to check.
    a_class: type
        The class to check against.

    Returns:
    bool: True if obj is an instance of a_class or its subclass, otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
