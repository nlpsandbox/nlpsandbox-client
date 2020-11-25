"""Utility functions"""
import json
import re


def stdout_or_json(json_dict: dict, output: str):
    """Write dict to json or stdout"""
    if output is None:
        print(json_dict)
    else:
        with open(output, 'w') as json_o:
            json.dump(json_dict, json_o)


def get_inputs_from_name(name: str, regex: str):
    """Get API input parameters from API output

    Args:
        name: Name of resource
        regex: String matching rule
    Returns:
        matched groups
    """
    match = re.match(regex, name)
    if not match:
        raise ValueError("Invalid name")
    return match