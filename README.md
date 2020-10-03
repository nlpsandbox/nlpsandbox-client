# NLP Sandbox Client

[![GitHub Stars](https://img.shields.io/github/stars/data2health/nlp-sandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client)
[![GitHub CI](https://img.shields.io/github/workflow/status/data2health/nlp-sandbox-client/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client)
[![GitHub License](https://img.shields.io/github/license/data2health/nlp-sandbox-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-client)

Python client to interact with the NLP Sandbox

## Development

Create a new conda environment using the Python version listed in the *Dockerfile*
of this repository (currently Python 3.8.5).

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