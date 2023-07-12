#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def load_from_json_file(filename):
    """Write an object to a text file using JSON representation."""
    with open(filename) as myfile:
        return json.load(myfile)
