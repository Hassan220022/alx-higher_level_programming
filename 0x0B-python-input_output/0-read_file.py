#!/usr/bin/python3
"""
Module for reading and printing the contents of a file.
"""


def read_file(filename=""):
    """
    Reads a file and prints its contents to the standard output.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs.
    """
    try:
        with open(filename, "r", encoding="UTF-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError as e:
        print(f"Error: {e}")
