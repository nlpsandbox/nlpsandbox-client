#!/usr/bin/env python3
import click

from . import community, evaluate, submit


@click.group()
def cli():
    """NLP Sandbox Client"""


def main():
    cli.add_command(community.cli)
    cli.add_command(evaluate.cli)
    cli()
