*****************
nlpsandbox-client
*****************

**nlpsandboxclient** is a set of tools and commands that provides an interface
for NLP sandbox data node, annotation services, and evaluation of annotation results.
This repository consists of 3 packages:

- **nlpsandbox**: Python SDK client that wraps all the NLP Sandbox APIs
- **nlpsandboxclient**: - Convenience functions that infer user behavior of the SDK client.

.. _Synapse: https://www.synapse.org/
.. _synapseclient: https://python-docs.synapse.org/build/html/index.html
.. _NLP sandbox schemas: https://github.com/nlpsandbox/nlpsandbox-schemas

Installation
============
To install from pypi:

.. code:: console

    $ pip install nlpsandbox-client

To install from the source:

.. code:: console

    $ python setup.py install

Configuration
=============
This client interfaces with the data-node_ or annotators such as date-annotator-example_.
There are two main ways of running this code, and each way has its preferred method
of setting Synapse credentials.

(1) Local Python Installation: Please learn more about `Synapse client configuration`_.

.. code:: console

    nlp-cli --version

(2) Docker: The client will read environmental variables for your Synapse credentials.

    a. Create the file that contains the future environment variables

    .. code:: console

        cp .env.sample .env

    b. Update the configuration values in *.env*. Set the values of **SYNAPSE_AUTH_TOKEN** to be your Synapse personal access token.

    c. Run docker command

    .. code:: console

        docker run --rm --env-file .env nlpsandbox/cli

.. _data-node: https://github.com/nlpsandbox/data-node
.. _date-annotator-example: https://github.com/nlpsandbox/date-annotator-example
.. _Synapse client configuration: https://docs.synapse.org/articles/client_configuration.html

Contributing
============
Interested in contributing? **Awesome!** We follow the typical `GitHub workflow`_
of forking a repo, creating a branch, and opening pull requests.  For more
information on how you can add or propose a change, visit our `contributing guide`_.

.. _Github workflow: https://guides.github.com/introduction/flow/
.. _contributing guide: https://github.com/nlpsandbox/nlpsandbox-client/blob/develop/CONTRIBUTING.md
