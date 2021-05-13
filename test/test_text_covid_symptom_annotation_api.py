"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import annotator
from annotator.api.text_covid_symptom_annotation_api import TextCovidSymptomAnnotationApi  # noqa: E501


class TestTextCovidSymptomAnnotationApi(unittest.TestCase):
    """TextCovidSymptomAnnotationApi unit test stubs"""

    def setUp(self):
        self.api = TextCovidSymptomAnnotationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_text_covid_symptom_annotations(self):
        """Test case for create_text_covid_symptom_annotations

        Annotate COVID symptoms in a clinical note  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
