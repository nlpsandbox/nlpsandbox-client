#!/usr/bin/env python3

import click
from nlpsandboxclient.evaluation import evaluation
from nlpsandboxclient.user import user as user_


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


@cli.command()
def user():
    """Get and set user information"""
    u = user_.User()
    u.run()


if __name__ == "__main__":
    cli()
