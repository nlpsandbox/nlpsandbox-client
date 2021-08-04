#!/usr/bin/env python3
import click

import synapseclient

from nlpsandboxclient import utils


# Command Group
@click.group(name='community', no_args_is_help=True)
@click.option('-c', 'synapse_config', help="Synapse configuration file",
              default=synapseclient.client.CONFIG_FILE,
              type=click.Path(exists=True), show_default=True)
@click.pass_context
def cli(ctx, synapse_config):
    """Commands for NLP Sandbox users."""
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj['synapse_config'] = synapse_config


@cli.command()
@click.pass_context
def get_num_users(ctx):
    """Gets the number of NLP Sandbox users"""
    syn = utils.synapse_login(synapse_config=ctx.obj['synapse_config'])
    res = syn.restGET("/teamMembers/count/3413388")
    print(f"Number of NLP sandbox users: {res['count']}")


if __name__ == '__main__':
    cli(obj={})
