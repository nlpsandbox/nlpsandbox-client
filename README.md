# NLP Sandbox Client

[![GitHub Stars](https://img.shields.io/github/stars/data2health/nlp-sandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client/stargazers)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/cli.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/cli)
[![GitHub CI](https://img.shields.io/github/workflow/status/data2health/nlp-sandbox-client/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client)
[![GitHub License](https://img.shields.io/github/license/data2health/nlp-sandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client/blob/main/LICENSE)

Python client to interact with the NLP Sandbox

## Usage

### Set your credentials

You need to set your NLP Sandbox credentials as environment variables to use the
NLP Sandbox client.

    export NLP_USERNAME="changeme"
    export NLP_API_TOKEN="changeme"

Currently, the value of `NLP_USERNAME` and `NLP_API_TOKEN` must be set to the
values of your Synapse username and API Key.

### Run the client using Docker

Once the environment variables `NLP_USERNAME` and `NLP_API_TOKEN` have been set,
try running the command below to show the help page of the client.

    docker run --rm -e NLP_USERNAME -e NLP_API_TOKEN nlpsandbox/cli

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