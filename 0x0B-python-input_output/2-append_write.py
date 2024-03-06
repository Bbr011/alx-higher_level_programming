#!/usr/bin/python3
"""defines a file_appending fun"""


def append_write(filename="", text=""):
    """appending a string to uft8 file
    Args:
        filename (str): file to append to
        text (str): text to be appended
    Returns:
        lenght of text appended
    """
    with open(filename, 'a', encoding="uft-8") as f:
        f.write(text)
        return (len(text))
