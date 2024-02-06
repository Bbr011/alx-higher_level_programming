#!/usr/bin/python3
"""lookupfunction"""


def lookup(obj):
    """list of available attributes and methods of an object"""
    list = sorted(dir(obj))
    return list
