#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly or indirectly)
    from the specified class a_class.
    
    Args:
        obj: Object to check.
        a_class: Class to check inheritance against.
        
    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return isinstance(obj, type) and issubclass(obj, a_class) and obj != a_class
