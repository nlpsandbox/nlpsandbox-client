#!/usr/bin/env python3

import click

from nlpsandboxclient.cli import community
from nlpsandboxclient.cli import evaluate


@click.group()
def cli():
    """NLP Sandbox Client"""


def entrypoint():
    cli.add_command(community.cli)
    cli.add_command(evaluate.cli)
    cli()


if __name__ == '__main__':
    entrypoint()
