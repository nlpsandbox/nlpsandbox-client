#!/usr/bin/env python3
import click
import synapseclient

from nlpsandboxclient import client, utils
from nlpsandboxclient.api_client import DATA_NODE_HOST


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
@click.option('--data_node_host',
              help=f'Data node host. If not specified, uses {DATA_NODE_HOST}')
@click.option('--datasetid', help='Dataset id')
def get_clinical_notes(output, data_node_host, datasetid):
    """Gets all the clinical notes"""
    data_node_host = (data_node_host if data_node_host is not None
                      else DATA_NODE_HOST)
    clinical_notes = client.get_clinical_notes(datasetid=datasetid,
                                               host=data_node_host)
    # Stdout or store to json
    utils.stdout_or_json(clinical_notes, output)


# @cli.command()
# @click.argument('noteid', type=click.INT)
# @click.option('--output', help='Output json filepath', type=click.Path())
# @click.option('--data_node_host',
#               help='Data node host.  If not specified, uses '
#                    'http://0.0.0.0:8080/api/v1')
# def get_clinical_note(noteid, output, data_node_host):
#     """Gets clinical note of NOTEID"""
#     data_node_host = (data_node_host if data_node_host is not None
#                       else client.DATA_NODE_HOST)
#     nlp = DataNodeClient(host=data_node_host)
#     clinical_note = nlp.get_clinical_note(noteid)
#     utils.stdout_or_json(clinical_note, output)


# @cli.command()
# @click.option('--data_node_host',
#               help='Data node host.  If not specified, uses '
#                    'http://0.0.0.0:8080/api/v1')
# def get_health(data_node_host):
#     """Gets health of the API"""
#     data_node_host = (data_node_host if data_node_host is not None
#                       else client.DATA_NODE_HOST)
#     nlp = DataNodeClient(host=data_node_host)
#     print(nlp.get_health())


# @cli.command()
# @click.option('--output', help='Output json filepath', type=click.Path())
# @click.option('--data_node_host',
#               help='Data node host.  If not specified, uses '
#                    'http://0.0.0.0:8080/api/v1')
# def get_dates(output, data_node_host):
#     """Get all date annotations"""
#     data_node_host = (data_node_host if data_node_host is not None
#                       else client.DATA_NODE_HOST)
#     nlp = DataNodeClient(host=data_node_host)
#     dates = nlp.get_dates()
#     utils.stdout_or_json(dates, output)


if __name__ == '__main__':
    cli()
