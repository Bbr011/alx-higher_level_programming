#!/usr/bin/python3
"""Defines a class-checking function"""


def is_kind_of_class(obj, a_class):
    """ if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class

    Parameters:
    obj: object
    the object to check
    a_class: class
    class to check agains

    Returns:
    bool: True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)
