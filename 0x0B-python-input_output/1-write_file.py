#!/usr/bin/python3
"""defines text file_writing function"""


def write_file(filename="", text=""):
    """return a string to the utf8 file
    Args:
        filename (str): name of file to write
        text (str): string to write
    Returns:
        text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return (len(text))
