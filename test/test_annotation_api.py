"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest
from unittest.mock import patch

import datanode
from datanode.api.annotation_api import AnnotationApi  # noqa: E501
from datanode.models import ResourceSource


class TestAnnotationApi(unittest.TestCase):
    """AnnotationApi unit test stubs"""

    def setUp(self):
        self.api = AnnotationApi()  # noqa: E501
        self.patcher = patch('datanode.api_client.ApiClient.call_api')
        self.mock_foo = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_create_annotation(self):
        """Test case for create_annotation

        Create an annotation  # noqa: E501
        """
        self.api.create_annotation(
            dataset_id="awesome-dataset",
            annotation_store_id="awesome-annotation-store",
            annotation_id="awesome-annotation",
            annotation_create_request={
                "annotation_source": {
                    "resource_source": ResourceSource("source")
                },
                "text_date_annotations": []
            }
        )

    def test_delete_annotation(self):
        """Test case for delete_annotation

        Delete an annotation  # noqa: E501
        """
        self.api.delete_annotation(
            dataset_id="data",
            annotation_store_id="data",
            annotation_id="data"
        )

    def test_get_annotation(self):
        """Test case for get_annotation

        Get an annotation  # noqa: E501
        """
        self.api.get_annotation(
            dataset_id="data",
            annotation_store_id="data",
            annotation_id="data"
        )

    def test_list_annotations(self):
        """Test case for list_annotations

        List the annotations in an annotation store  # noqa: E501
        """
        self.api.list_annotations(
            dataset_id="data",
            annotation_store_id="data"
        )


if __name__ == '__main__':
    unittest.main()
