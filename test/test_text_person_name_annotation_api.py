"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest
from unittest.mock import patch

import nlpsandbox
from nlpsandbox.api.text_person_name_annotation_api import TextPersonNameAnnotationApi  # noqa: E501


class TestTextPersonNameAnnotationApi(unittest.TestCase):
    """TextPersonNameAnnotationApi unit test stubs"""

    def setUp(self):
        self.api = TextPersonNameAnnotationApi()  # noqa: E501
        self.patcher = patch('nlpsandbox.api_client.ApiClient.call_api')
        self.mock_foo = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_create_text_person_name_annotations(self):
        """Test case for create_text_person_name_annotations

        Annotate person names in a clinical note  # noqa: E501
        """
        self.api.create_text_person_name_annotations(
            text_person_name_annotation_request={
                "note": {
                    "identifier": "note-1",
                    "type": "note-type",
                    "text": "my text here",
                    "patient_id": "patient-1"
                }
            }
        )


if __name__ == '__main__':
    unittest.main()
