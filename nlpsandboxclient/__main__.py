#!/usr/bin/env python3

import click
# from nlpsandboxclient.evaluation import evaluation
# from nlpsandboxclient.community import community
# from nlpsandboxclient.user import user as user_

from nlpsandboxclient.cli import community
from nlpsandboxclient.cli import evaluation


# @click.group()
# def main():
#     """Demo"""
#     print("plop")

# def entrypoint():
#     main.add_command(community)
#     main()


# cli = click.CommandCollection(sources=[community.cli_tools, evaluation.cli_evaluation])

@click.group()
def main():
    """Demo"""

def cli():
    main.add_command(community.cli_tools)
    main.add_command(evaluation.cli_evaluation)
    main()

if __name__ == '__main__':
    cli()

# @click.group()
# def cli():
#     """NLP Sandbox client"""


# @cli.command()
# @click.option('--pred_filepath', help='Prediction filepath',
#               type=click.Path(exists=True))
# @click.option('--gold_filepath', help='Gold standard filepath',
#               type=click.Path(exists=True))
# def evaluate(pred_filepath, gold_filepath):
#     """Evaluate the performance of a local prediction file"""
#     e = evaluation.Evaluation()
#     e.run()


# @cli.command()
# def user():
#     """Get and set user information"""
#     u = user_.User()
#     u.run()



# @cli.command()
# @click.option('--action', help='Get the number of users',
#               type=click.Path(exists=True))
# def community():
#     """Get information about the community"""
#     u = user_.User()
#     u.run()

# @click.group()
# def community():
#     """Community"""

# @click.group()
# def cli():
#     entry_point.add_command(community_commands.version)
#     # entry_point.add_command(group2.version)

# if __name__ == "__main__":
#     cli()
