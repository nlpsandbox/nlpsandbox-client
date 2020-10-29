#!/usr/bin/env python3
import json

import click
from nlpsandboxclient import evaluation


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
    eval_mapping = {"date": evaluation.DateEvaluation,
                    "person": evaluation.PersonNameEvaluation,
                    "address": evaluation.PhysicalAddressEvaluation}
    evaluator = eval_mapping[eval_type]()

    evaluator.convert_dict(pred_filepath, gold_filepath)
    results = evaluator.eval()
    # output json file
    json_object = json.dumps(results, indent=4)
    with open(output, "w") as outfile:
        outfile.write(json_object)


# @cli_evaluation.command(name='search2', help='test search')
# @click.option('--test1', default='1', help='test option')
# def search_cmd(test1):
#     click.echo('Hello world')


if __name__ == '__main__':
    cli()
