"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import datanode
from datanode.model.note import Note
from datanode.model.note_id import NoteId
from datanode.model.patient_id import PatientId
globals()['Note'] = Note
from datanode.model.page_of_notes_all_of import PageOfNotesAllOf


class TestPageOfNotesAllOf(unittest.TestCase):
    """PageOfNotesAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPageOfNotesAllOf(self):
        """Test PageOfNotesAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PageOfNotesAllOf()  # noqa: E501
        PageOfNotesAllOf(
            notes=[Note(identifier=NoteId("identifier"),
                        text="text", type="type",
                        patient_id=PatientId('patient-1'))]
        )


if __name__ == '__main__':
    unittest.main()
