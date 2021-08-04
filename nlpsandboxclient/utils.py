"""Utility functions"""
import json
import os
import re

import requests
import synapseclient
from synapseclient.core.exceptions import (
    SynapseNoCredentialsError,
    SynapseAuthenticationError,
)

import nlpsandbox


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


def synapse_login(synapse_config=synapseclient.client.CONFIG_FILE):
    """Login to Synapse

    Args:
        synapse_config: Path to synapse configuration file.
                        Defaults to ~/.synapseConfig

    Returns:
        Synapse connection
    """
    try:
        syn = synapseclient.Synapse(configPath=synapse_config)
        syn.login(silent=True)
    except (SynapseNoCredentialsError, SynapseAuthenticationError):
        raise ValueError(
            "Login error: please make sure you have correctly "
            "configured your client.  Instructions here: "
            "https://help.synapse.org/docs/Client-Configuration.1985446156.html. "
            "You can also create a Synapse Personal Access Token and set it "
            "as an environmental variable: "
            "SYNAPSE_AUTH_TOKEN='<my_personal_access_token>'"
        )
    return syn


def get_api_configuration(host: str):
    """Get API configuration

    Args:
        host: Tool IP

    Returns:
        API configuration

    Examples:
        >>> get_api_configuration(host="http://0.0.0.0:8080/api/v1")

    """
    # Check if URL exists
    check_url(url=os.path.join(host, "ui"))
    configuration = nlpsandbox.Configuration(host=host)
    return configuration
