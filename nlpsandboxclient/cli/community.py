#!/usr/bin/env python3
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
@click.option('--data_endpoint', help='Data endpoint')
def get_clinical_notes(output, data_endpoint):
    """Gets all the clinical notes"""
    data_endpoint = (data_endpoint if data_endpoint is not None
                     else client.DATA_NODE_ENDPOINT)
    nlp = NlpClient(data_node_endpoint=data_endpoint)
    clinical_notes = nlp.get_clinical_notes()
    # Stdout or store to json
    utils.stdout_or_json(clinical_notes, output)


@cli.command()
@click.argument('noteid', type=click.INT)
@click.option('--output', help='Output json filepath', type=click.Path())
@click.option('--data_endpoint', help='Data endpoint')
def get_clinical_note(noteid, output, data_endpoint):
    """Gets clinical note of NOTEID"""
    data_endpoint = (data_endpoint if data_endpoint is not None
                     else client.DATA_NODE_ENDPOINT)
    nlp = NlpClient(data_node_endpoint=data_endpoint)
    clinical_note = nlp.get_clinical_note(noteid)
    utils.stdout_or_json(clinical_note, output)


@cli.command()
@click.option('--data_endpoint', help='Data endpoint')
def get_health(data_endpoint):
    """Gets health of the API"""
    data_endpoint = (data_endpoint if data_endpoint is not None
                     else client.DATA_NODE_ENDPOINT)
    nlp = NlpClient(data_node_endpoint=data_endpoint)
    print(nlp.get_health())


@cli.command()
@click.option('--output', help='Output json filepath', type=click.Path())
@click.option('--data_endpoint', help='Data endpoint.')
def get_dates(output, data_endpoint):
    """Get all date annotations"""
    data_endpoint = (data_endpoint if data_endpoint is not None
                     else client.DATA_NODE_ENDPOINT)
    nlp = NlpClient(data_node_endpoint=data_endpoint)
    dates = nlp.get_dates()
    utils.stdout_or_json(dates, output)


if __name__ == '__main__':
    cli()
