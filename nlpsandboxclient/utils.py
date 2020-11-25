"""Utility functions"""
import json

from requests.exceptions import HTTPError


def _raise_for_status(response):
    """
    Replacement for requests.response.raise_for_status().
    Catches and wraps NLP HTTP errors with appropriate text.
    """
    if response.status_code not in [200, 201, 202]:
        raise HTTPError(response.json()['title'], response)


def stdout_or_json(json_dict: dict, output: str):
    """Write dict to json or stdout"""
    if output is None:
        print(json_dict)
    else:
        with open(output, 'w') as json_o:
            json.dump(json_dict, json_o)
