#!/usr/bin/python3
"""class MyList that inherits from list"""
class MyList(list):
    """Implements sorted printing for the built-in list class"""
    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
