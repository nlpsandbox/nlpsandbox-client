#!/usr/bin/env python3
import click

from .. import __version__
from . import community, evaluate


@click.group()
@click.version_option(__version__)
def cli():
    """NLP Sandbox Client"""


def main():
    cli.add_command(community.cli)
    cli.add_command(evaluate.cli)
    cli()
