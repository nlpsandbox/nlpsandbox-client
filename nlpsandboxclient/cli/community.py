#!/usr/bin/env python3
import json

import click
import synapseclient

from nlpsandboxclient import client, utils
from nlpsandboxclient.client import DATA_NODE_HOST


# Command Group
@click.group(name='community', no_args_is_help=True)
def cli():
    """Community related commands"""


@cli.command(no_args_is_help=True)
def get_num_users():
    """Gets the number of NLP Sandbox users"""
    syn = synapseclient.login()
    res = syn.restGET("/teamMembers/count/3413388")
    print(res)


@cli.command(no_args_is_help=True)
@click.option('--output', help='Output json filepath', type=click.Path())
@click.option('--data_node_host', help='Data node host',
              default=DATA_NODE_HOST, show_default=True)
@click.option('--dataset_id', help='Dataset id')
@click.option('--fhir_store_id', help='Dataset id')
def list_notes(output, data_node_host, dataset_id, fhir_store_id):
    """Gets all the clinical notes"""
    clinical_notes = client.list_notes(host=data_node_host,
                                       dataset_id=dataset_id,
                                       fhir_store_id=fhir_store_id)
    # Stdout or store to json
    utils.stdout_or_json(list(clinical_notes), output)


@cli.command(no_args_is_help=True)
@click.option('--data_node_host', help='Data node host',
              default=DATA_NODE_HOST, show_default=True)
@click.option('--dataset_id', help='Dataset id')
@click.option('--annotation_store_id', help='Dataset id')
@click.option('--annotation_json', help='Json file with annotations to store',
              type=click.Path(exists=True))
def store_annotations(data_node_host, dataset_id, annotation_store_id,
                      annotation_json):
    """Store annotations"""
    with open(annotation_json, "r") as annot_f:
        annotations = json.load(annot_f)
    # If only one annotation is passed in, turn it into a list
    if isinstance(annotations, dict):
        annotations = [annotations]
    # Create annotation store object
    for annotation in annotations:
        client.store_annotation(
            host=data_node_host,
            dataset_id=dataset_id,
            annotation_store_id=annotation_store_id,
            annotation=annotation
        )


@cli.command(no_args_is_help=True)
@click.option('--data_node_host', help='Data node host',
              default=DATA_NODE_HOST, show_default=True)
@click.option('--dataset_id', help='Dataset id')
@click.option('--annotation_store_id', help='Dataset id')
@click.option('--create_if_missing', help='Create resource if missing', is_flag=True)
def get_annotation_store(data_node_host, dataset_id, annotation_store_id, create_if_missing):
    """Create annotation store"""
    # Create annotation store object
    annotation_store = client.get_annotation_store(
        host=data_node_host, dataset_id=dataset_id,
        annotation_store_id=annotation_store_id,
        create_if_missing=create_if_missing
    )
    print(annotation_store.name)


@cli.command(no_args_is_help=True)
@click.option('--data_node_host', help='Data node host',
              default=DATA_NODE_HOST, show_default=True)
@click.option('--dataset_id', help='Dataset id')
@click.option('--annotation_store_id', help='Dataset id')
@click.option('--output', help='Output json filepath', type=click.Path())
def list_annotations(data_node_host, dataset_id, annotation_store_id, output):
    """List annotations"""
    # Create annotation store object
    annotations = client.list_annotations(
        host=data_node_host, dataset_id=dataset_id,
        annotation_store_id=annotation_store_id
    )
    utils.stdout_or_json(list(annotations), output)


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
