#!/usr/bin/env python3
import click
# from nlpsandboxclient import validation


@click.group(name='validate')
def cli():
    """Validation related commands"""


@cli.command(name="tool")
@click.option('--tool_host', help='The address of the Tool to validate',
              required=True)
@click.option('--tool_type', help='The type of the Tool',
              required=True)
def validate_tool(pred_filepath, gold_filepath, output_directory):
    """Validate the Tool specified"""
    # TBA


if __name__ == '__main__':
    cli()
