"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import annotator
from annotator.model.text_contact_annotation import TextContactAnnotation
globals()['TextContactAnnotation'] = TextContactAnnotation
from annotator.model.text_contact_annotation_response import TextContactAnnotationResponse


class TestTextContactAnnotationResponse(unittest.TestCase):
    """TextContactAnnotationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTextContactAnnotationResponse(self):
        """Test TextContactAnnotationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TextContactAnnotationResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
