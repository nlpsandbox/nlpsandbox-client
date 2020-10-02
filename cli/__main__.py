#!/usr/bin/env python3

import click
from evaluate import evaluation


@click.group()
def cli():
    """NLP Sandbox client"""


@cli.command()
@click.option('--pred_filepath', help='Prediction filepath',
              type=click.Path(exists=True))
@click.option('--gold_filepath', help='Gold standard filepath',
              type=click.Path(exists=True))
def evaluate(pred_filepath, gold_filepath):
    """Evaluate the performance of a local prediction file"""
    e = evaluation.Evaluation()
    e.run()


if __name__ == "__main__":
    cli()
