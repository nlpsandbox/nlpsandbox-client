"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import nlpsandbox
from nlpsandbox.model.note import Note
from nlpsandbox.model.note_id import NoteId
from nlpsandbox.model.patient_id import PatientId
from nlpsandbox.model.page_limit import PageLimit
from nlpsandbox.model.page_offset import PageOffset
from nlpsandbox.model.response_page_metadata import ResponsePageMetadata
from nlpsandbox.model.response_page_metadata_links import ResponsePageMetadataLinks
globals()['Note'] = Note
globals()['PageLimit'] = PageLimit
globals()['PageOffset'] = PageOffset
globals()['ResponsePageMetadata'] = ResponsePageMetadata
globals()['ResponsePageMetadataLinks'] = ResponsePageMetadataLinks
from nlpsandbox.model.page_of_notes import PageOfNotes


class TestPageOfNotes(unittest.TestCase):
    """PageOfNotes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPageOfNotes(self):
        """Test PageOfNotes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PageOfNotes()  # noqa: E501
        PageOfNotes(
            offset=PageOffset(10),
            limit=PageLimit(10),
            links=ResponsePageMetadataLinks(next="next"),
            total_results=30,
            notes=[Note(identifier=NoteId("identifier"),
                        text="text", type="type",
                        patient_id=PatientId('patient-1'))]
        )


if __name__ == '__main__':
    unittest.main()
