#!/usr/bin/env python3
import json

import click
import synapseclient

from nlpsandboxclient import client, utils
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
@click.option('--output', help='Output json filepath', type=click.Path())
def get_clinical_notes(output):
    """Gets all the clinical notes"""
    nlp = NlpClient(data_node_endpoint=client.DATA_NODE_ENDPOINT)
    clinical_notes = nlp.get_clinical_notes()
    # Stdout or store to json
    utils.stdout_or_json(clinical_notes, output)


@cli.command()
@click.argument('noteid', type=click.INT)
@click.option('--output', help='Output json filepath', type=click.Path())
def get_clinical_note(noteid, output):
    """Gets clinical note of NOTEID"""
    nlp = NlpClient(data_node_endpoint=client.DATA_NODE_ENDPOINT)
    clinical_note = nlp.get_clinical_note(noteid)
    utils.stdout_or_json(clinical_note, output)


@cli.command()
def get_health():
    """Gets health of the API"""
    nlp = NlpClient(data_node_endpoint=client.DATA_NODE_ENDPOINT)
    print(nlp.get_health())


@cli.command()
@click.option('--output', help='Output json filepath', type=click.Path())
def get_dates(output):
    """Get all date annotations"""
    nlp = NlpClient(data_node_endpoint=client.DATA_NODE_ENDPOINT)
    dates = nlp.get_dates()
    utils.stdout_or_json(dates, output)


if __name__ == '__main__':
    cli()
