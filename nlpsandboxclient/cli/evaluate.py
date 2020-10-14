#!/usr/bin/env python3

import click
from nlpsandboxclient.evaluation import evaluation


@click.group(name='evaluate')
def cli():
    """Evaluation related commands"""


@cli.command(name="prediction")
@click.option('--pred_filepath', help='Prediction filepath',
              type=click.Path(exists=True), required=True)
@click.option('--gold_filepath', help='Gold standard filepath',
              type=click.Path(exists=True), required=True)
def evaluate_prediction(pred_filepath, gold_filepath):
    """Evaluate the performance of a local prediction file"""
    date_e = evaluation.Evaluation("date")
    date_e.convert_dict(pred_filepath, gold_filepath)
    date_e_results = date_e.eval()
    # Running the person name eval module
    name_e = evaluation.Evaluation("person")
    name_e.convert_dict(pred_filepath, gold_filepath)
    name_e_results = name_e.eval()
    # Running the address eval module
    address_e = evaluation.Evaluation("address")
    address_e.convert_dict(pred_filepath, gold_filepath)
    address_e_results = address_e.eval()
    _ = (date_e_results, name_e_results, address_e_results)


# @cli_evaluation.command(name='search2', help='test search')
# @click.option('--test1', default='1', help='test option')
# def search_cmd(test1):
#     click.echo('Hello world')


if __name__ == '__main__':
    cli()
