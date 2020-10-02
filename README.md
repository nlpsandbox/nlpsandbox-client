# NLP Sandbox Evaluation Tool

Evaluate the performance of NLP Sandbox Tools

## Development

Create a new conda environment using the Python version listed in the *Dockerfile*
of this repository (currently Python 3.8.5).

    conda create --name nlp-sandbox-evaluation python=3.8.5
    conda activate nlp-sandbox-evaluation

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