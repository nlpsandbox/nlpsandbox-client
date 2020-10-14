#!/usr/bin/env python3
import json

import click
import synapseclient

from nlpsandboxclient import client
from nlpsandboxclient.client import NlpClient


# Command Group
@click.group(name='community')
def cli():
    """Community related commands"""


@cli.command()
def get_num_users():
    """Gets the number of NLP Sandbox users"""
    syn = synapseclient.login()
    res = syn.restGET("/teamMembers/count/3413388")
    print(res)


@cli.command()
@click.option('--output', help='Output filepath', type=click.Path())
def get_clinical_notes(output):
    """Gets all the clinical notes"""
    nlp = NlpClient(data_node_endpoint=client.DATA_NODE_ENDPOINT)
    clinical_notes = nlp.get_clinical_notes()
    # Stdout or store to json
    if output is None:
        print(clinical_notes)
    else:
        with open(output, 'w') as json_o:
            json.dump(clinical_notes, json_o)


if __name__ == '__main__':
    cli()
