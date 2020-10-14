"""Utility functions"""
import json


def stdout_or_json(json_dict: dict, output: str):
    """Write dict to json or stdout"""
    if output is None:
        print(json_dict)
    else:
        with open(output, 'w') as json_o:
            json.dump(json_dict, json_o)
