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
from annotator.model.note import Note
globals()['Note'] = Note
from annotator.model.text_covid_symptom_annotation_request import TextCovidSymptomAnnotationRequest


class TestTextCovidSymptomAnnotationRequest(unittest.TestCase):
    """TextCovidSymptomAnnotationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTextCovidSymptomAnnotationRequest(self):
        """Test TextCovidSymptomAnnotationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TextCovidSymptomAnnotationRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
