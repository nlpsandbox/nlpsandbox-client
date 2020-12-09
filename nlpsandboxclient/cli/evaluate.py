#!/usr/bin/env python3
import json

import click
from nlpsandboxclient import client, evaluation, utils
from nlpsandboxclient.client import DATE_ANNOTATOR_HOST


@click.group(name='evaluate')
def cli():
    """Evaluation related commands"""


@cli.command(name="prediction")
@click.option('--pred_filepath', help='Prediction filepath',
              type=click.Path(exists=True), required=True)
@click.option('--gold_filepath', help='Gold standard filepath',
              type=click.Path(exists=True), required=True)
@click.option('--output', help='Specify output json path',
              type=click.Path())
@click.option('--eval_type', help='Type of evaluation.',
              type=click.Choice(['date', 'person', 'address'],
                                case_sensitive=False))
def evaluate_prediction(pred_filepath, gold_filepath, output, eval_type):
    """Evaluate the performance of a local prediction file"""
    eval_mapping = {
        "date": evaluation.DateEvaluation,
        "person": evaluation.PersonNameEvaluation,
        "address": evaluation.PhysicalAddressEvaluation
    }
    evaluator = eval_mapping[eval_type]()

    evaluator.convert_dict(pred_filepath, gold_filepath)
    results = evaluator.eval()
    utils.stdout_or_json(results, output)
    # json_object = json.dumps(results, indent=4)
    # with open(output, "w") as outfile:
    #     outfile.write(json_object)


@cli.command(name="text-date-annotate")
@click.option('--date_annotator_host',
              help='Date annotator host. '
                   f'If not specified, uses {DATE_ANNOTATOR_HOST}')
@click.option('--note_json', help='Clinical notes json',
              type=click.Path(exists=True))
@click.option('--output', help='Specify output json path',
              type=click.Path())
def text_date_annotate(date_annotator_host, note_json, output):
    """Evaluate the performance of a local prediction file"""
    date_annotator_host = (date_annotator_host
                           if date_annotator_host is not None
                           else DATE_ANNOTATOR_HOST)
    with open(note_json, "r") as note_f:
        notes = json.load(note_f)
    all_annotations = []
    for note in notes:
        note.pop("id")
        annotations = client.annotate_date(host=date_annotator_host,
                                           note={"note": note})
        annotations['annotationSource'] = {
            "resourceSource": {
                "name": note['note_name']
            }
        }
        all_annotations.append(annotations)
    utils.stdout_or_json(all_annotations, output)


@cli.command(name="get-annotator-service")
@click.option('--annotator_host',
              help='Date annotator host. '
                   f'If not specified, uses {DATE_ANNOTATOR_HOST}')
@click.option('--output', help='Specify output json path',
              type=click.Path())
def get_annotator_service(annotator_host, output):
    """Evaluate the performance of a local prediction file"""
    date_annotator_host = (annotator_host if annotator_host is not None
                           else DATE_ANNOTATOR_HOST)
    service = client.get_annotator_service_info(
        host=date_annotator_host
    )
    utils.stdout_or_json(service.to_dict(), output)


if __name__ == '__main__':
    cli()
