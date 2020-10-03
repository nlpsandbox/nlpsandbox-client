# NLP Sandbox Client

[![GitHub Stars](https://img.shields.io/github/stars/data2health/nlp-sandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client/stargazers)
[![GitHub CI](https://img.shields.io/github/workflow/status/data2health/nlp-sandbox-client/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client)
[![GitHub License](https://img.shields.io/github/license/data2health/nlp-sandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client/blob/main/LICENSE)

Python client to interact with the NLP Sandbox

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

    python setup.py develop --user

Run the program

    $ nlp-cli
    Usage: nlp-cli [OPTIONS] COMMAND [ARGS]...

    NLP Sandbox client

    Options:
    --help  Show this message and exit.

    Commands:
    evaluate  Evaluate the performance of a local prediction file