#!/usr/bin/env python3
import click

from . import community, evaluate


@click.group()
@click.version_option(__version__)
@click.pass_context
def cli():
    """NLP Sandbox Client"""


def main():
    cli.add_command(community.cli)
    cli.add_command(evaluate.cli)
    cli()
