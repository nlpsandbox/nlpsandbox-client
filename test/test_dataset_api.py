"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest
from unittest.mock import patch

import nlpsandboxsdk
from nlpsandboxsdk.api.dataset_api import DatasetApi  # noqa: E501


class TestDatasetApi(unittest.TestCase):
    """DatasetApi unit test stubs"""

    def setUp(self):
        self.api = DatasetApi()  # noqa: E501
        self.patcher = patch('nlpsandboxsdk.api_client.ApiClient.call_api')
        self.mock_foo = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_create_dataset(self):
        """Test case for create_dataset

        Create a dataset  # noqa: E501
        """
        self.api.create_dataset(
            dataset_id="foo",
            body={}
        )

    def test_delete_dataset(self):
        """Test case for delete_dataset

        Delete a dataset by ID  # noqa: E501
        """
        self.api.delete_dataset(
            dataset_id="foo"
        )

    def test_get_dataset(self):
        """Test case for get_dataset

        Get a dataset by ID  # noqa: E501
        """
        self.api.get_dataset(
            dataset_id="foo"
        )

    def test_list_datasets(self):
        """Test case for list_datasets

        Get all datasets  # noqa: E501
        """
        self.api.list_datasets()


if __name__ == '__main__':
    unittest.main()
