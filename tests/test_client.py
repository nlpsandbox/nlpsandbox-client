"""Test client functions"""
from unittest.mock import Mock, patch

import datanodeclient

from nlpsandboxclient import client


def test_get_notes():
    configuration = Mock()
    api = Mock()
    note_api_mock = Mock()
    host = "0.0.0.0"
    configuration = Mock()
    note_example = datanodeclient.models.PageOfNotes(
        notes=[datanodeclient.models.Note(
            id="12344", note_type="foo", patient_id="pat1", text="foobarbaz"
        )],
        offset=0, limit=3, links="foo"
    )

    with patch.object(datanodeclient, "Configuration",
                      return_value=configuration) as config,\
         patch.object(datanodeclient, "ApiClient") as api_client,\
         patch.object(datanodeclient, "NoteApi",
                      return_value=note_api_mock) as note_api,\
         patch.object(note_api_mock, "list_notes",
                      return_value=note_example) as list_notes:

        # To mock context manager
        api_client.return_value = api_client
        api_client.__enter__ = Mock(return_value=api)
        api_client.__exit__ = Mock(return_value=None)

        notes = client.get_notes(
            host=host,
            dataset_id="awesome-dataset",
            fhir_store_id="awesome-fhir-store"
        )
        config.assert_called_once_with(host=host)
        api_client.assert_called_once_with(configuration)
        note_api.assert_called_once_with(api)
        list_notes.assert_called_once_with("awesome-dataset", "awesome-fhir-store")
        assert notes == [{
            'id': '12344',
            'noteType': 'foo',
            'patientId': 'pat1',
            'text': 'foobarbaz',
            'note_name': 'dataset/awesome-dataset/fhirStores/awesome-fhir-store/fhir/Note/12344'
        }]
