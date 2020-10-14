#!/usr/bin/env python3

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
@click.option('--output_directory', help='Scoring json output filepath ',
              type=click.Path(exists=True), required=True)
def evaluate_prediction(pred_filepath, gold_filepath, output_directory):
    """Evaluate the performance of a local prediction file"""
    date_e = evaluation.DateEvaluation()
    date_e.convert_dict(pred_filepath, gold_filepath)
    date_e_results = date_e.eval(output_directory)
    # Running the person name eval module
    name_e = evaluation.PersonNameEvaluation()
    name_e.convert_dict(pred_filepath, gold_filepath)
    name_e_results = name_e.eval(output_directory)
    # Running the address eval module
    address_e = evaluation.PhysicalAddressEvaluation()
    address_e.convert_dict(pred_filepath, gold_filepath)
    address_e_results = address_e.eval(output_directory)
    _ = (date_e_results, name_e_results, address_e_results)


# @cli_evaluation.command(name='search2', help='test search')
# @click.option('--test1', default='1', help='test option')
# def search_cmd(test1):
#     click.echo('Hello world')


if __name__ == '__main__':
    cli()
