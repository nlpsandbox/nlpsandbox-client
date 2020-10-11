#!/usr/bin/env python3

import click
import synapseclient


# Command Group
@click.group(name='community')
def cli():
    """Community related commands"""


@cli.command()
def get_num_users():
    syn = synapseclient.login()
    res = syn.restGET("/teamMembers/count/3413388")
    print(res)


if __name__ == '__main__':
    cli()
