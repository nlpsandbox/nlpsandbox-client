# NLP Sandbox Client

[![GitHub Release](https://img.shields.io/github/release/nlpsandbox/nlpsandbox-client.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/nlpsandbox-client/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/nlpsandbox/nlpsandbox-client/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/nlpsandbox-client)
[![GitHub License](https://img.shields.io/github/license/nlpsandbox/nlpsandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/nlpsandbox-client)
[![PyPi](https://img.shields.io/pypi/v/nlpsandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=PyPi&logo=PyPi)](https://pypi.org/project/nlpsandbox-client)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/nlpsandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/nlpsandbox-client)
[![Discord](https://img.shields.io/discord/770484164393828373.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://discord.gg/Zb4ymtF "Realtime support / chat with the community and the team")

NLP Sandbox Python Client

## Usage

### Create configuration

1. Create the file that contains the future environment variables

        cp .env.sample .env

2. Update the configuration values in *.env*. Set the values of `SYNAPSE_USERNAME`
   and `SYNAPSE_APIKEY` with the credentials of your Synapse account.

3. Export the variables defined in .env to environment variables

        export $(grep -v '^#' .env | xargs -d '\n')

### Run the client using Docker

    docker run --rm nlpsandbox/cli

### Evaluate the performance of a local prediction file

    docker run --rm nlpsandbox/cli evaluate

## Development

Create a new conda environment using the Python version listed in the
[Dockerfile](Dockerfile) of this repository (currently Python 3.8.5).

    conda create --name nlp-sandbox-client python=3.8.5
    conda activate nlp-sandbox-client

Install the project in *develop* mode. This command must be executed each time
the content of *setup.py* is updated.

<!-- currently not working: python setup.py develop --user -->
    pip install -e .

Run the program

    $ nlp-cli
    Usage: nlp-cli [OPTIONS] COMMAND [ARGS]...

    NLP Sandbox client

    Options:
    --help  Show this message and exit.

    Commands:
    evaluate  Evaluate the performance of a local prediction file

## Tests

```
nlp-cli evaluate prediction --pred_filepath tests/data/prediction_1.json --gold_filepath tests/data/goldstandard_1.json
```