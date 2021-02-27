*****************
nlpsandbox-client
*****************

**nlpsandboxclient** is a set of tools and commands that provides an interface
for NLP sandbox data node, annotation services, and evaluation of annotation results.
This repository consists of 3 packages:

- **datanode**: Python SDK client that wraps `data-node API`_
- **annotator**: Python SDK client for the NLP annotators `date-annotator API`_,
`person-name-annotator API`_, `physical-address-annotator API`_
- **nlpsandboxclient**: Uses **datanode**, **annotator** to interact with NLP services
and the synapseclient_ library to pull information from Synapse (account required).

.. _Synapse: https://www.synapse.org/
.. _synapseclient: https://python-docs.synapse.org/build/html/index.html
.. _data-node API: https://nlpsandbox.github.io/nlpsandbox-schemas/data-node/latest/openapi.json
.. _date-annotator API: https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/openapi.json
.. _person-name-annotator API: https://nlpsandbox.github.io/nlpsandbox-schemas/person-name-annotator/latest/openapi.json
.. _physical-address-annotator API: https://nlpsandbox.github.io/nlpsandbox-schemas/physical-address-annotator/latest/openapi.json

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
(2) Docker: The client will read environmental variables for your Synapse credentials. 
   a. Create the file that contains the future environment variables

    .. code:: console

        cp .env.sample .env

   b. Update the configuration values in *.env*. Set the values of **SYNAPSE_USERNAME**
   and **SYNAPSE_APIKEY** with the credentials of your Synapse account.

   c. Export the variables defined in .env to environment variables

    .. code:: console

        export $(grep -v '^#' .env | xargs -d '\n')


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
