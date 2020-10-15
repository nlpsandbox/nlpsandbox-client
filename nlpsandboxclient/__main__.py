#!/usr/bin/env python3
import click

from .cli import community, evaluate


@click.group()
def cli():
    """NLP Sandbox Client"""


def entrypoint():
    cli.add_command(community.cli)
    cli.add_command(evaluate.cli)
    cli()
