"""Utility functions"""
import json
import re

import requests


def stdout_or_json(json_dict: dict, output: str):
    """Write dict to json or stdout"""
    if output is None:
        print(json_dict)
    else:
        with open(output, 'w') as json_o:
            json.dump(json_dict, json_o)


def camelcase_to_snakecase(value):
    """Change camelcase to snakecase"""
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub('_', value).lower()


def change_keys(obj, convert):
    """
    Recursivly goes through the dictionnary obj and replaces keys with the
    convert function.
    """
    if isinstance(obj, dict):
        new = {}
        for key, value in obj.items():
            new[convert(key)] = change_keys(value, convert)
    elif isinstance(obj, list):
        new = []
        for value in obj:
            new.append(change_keys(value, convert))
    else:
        return obj
    return new


def check_url(url: str):
    """Check if url is implemented

    Args:
        url: The url to check

    Raises:
        ValueError: If url is not implemented

    Examples:
        >>> check_url(url="https://www.google.com")

    """
    if not url.startswith("http"):
        url = f"http://{url}"
    response = requests.get(url)
    if not response.ok:
        raise ValueError(f"{url} not implemented")
