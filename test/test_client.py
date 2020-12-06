"""Test client functions"""
from unittest.mock import Mock, patch

import pytest

import datanode
from datanode.models import (Annotation, AnnotationStore, PageOfAnnotations,
                             PageOfNotes, Note)
from datanode.rest import ApiException
from nlpsandboxclient import client


# def test_get_notes():
#     configuration = Mock()
#     api = Mock()
#     note_api_mock = Mock()
#     host = "0.0.0.0"
#     configuration = Mock()
#     note_example = PageOfNotes(
#         notes=[Note(
#             id="12344", note_type="foo", patient_id="pat1", text="foobarbaz"
#         )],
#         offset=0, limit=3, links=Mock(next="")
#     )

#     with patch.object(datanode, "Configuration",
#                       return_value=configuration) as config,\
#          patch.object(datanode, "ApiClient") as api_client,\
#          patch.object(datanode, "NoteApi",
#                       return_value=note_api_mock) as note_api,\
#          patch.object(note_api_mock, "list_notes",
#                       return_value=note_example) as list_notes:

#         # To mock context manager
#         api_client.return_value = api_client
#         api_client.__enter__ = Mock(return_value=api)
#         api_client.__exit__ = Mock(return_value=None)

#         notes = client.get_notes(
#             host=host,
#             dataset_id="awesome-dataset",
#             fhir_store_id="awesome-fhir-store"
#         )
#         config.assert_called_once_with(host=host)
#         api_client.assert_called_once_with(configuration)
#         note_api.assert_called_once_with(api)
#         list_notes.assert_called_once_with("awesome-dataset",
#                                            "awesome-fhir-store",
#                                            limit=10, offset=0)
#         assert notes == [{
#             'id': '12344',
#             'noteType': 'foo',
#             'patientId': 'pat1',
#             'text': 'foobarbaz',
#             'note_name': 'dataset/awesome-dataset/fhirStores/awesome-fhir-store/fhir/Note/12344'
#         }]


class TestClient:

    def setup_method(self):
        self.configuration = Mock()
        self.api = Mock()
        self.mock_api = Mock()
        self.host = "0.0.0.0"
        self.config = patch.object(datanode, "Configuration",
                                   return_value=self.configuration)
        self.api_client = patch.object(datanode, "ApiClient")
        self.dataset_id = "awesome-dataset"
        self.annotation_store_id = "annotation-store"
        self.fhir_store_id = "fhir-store"
        # To mock context manager

    def test_get_notes(self):
        note_example = PageOfNotes(
            notes=[Note(
                id="12344", note_type="foo", patient_id="pat1", text="foobarbaz"
            )],
            offset=0, limit=3, links=Mock(next="")
        )

        with self.config as config,\
             self.api_client as api_client,\
             patch.object(datanode, "NoteApi",
                          return_value=self.mock_api) as note_api,\
             patch.object(self.mock_api, "list_notes",
                          return_value=note_example) as list_notes:

            # To mock context manager
            api_client.return_value = api_client
            api_client.__enter__ = Mock(return_value=self.api)
            api_client.__exit__ = Mock(return_value=None)

            notes = client.get_notes(
                host=self.host,
                dataset_id=self.dataset_id,
                fhir_store_id=self.fhir_store_id
            )
            config.assert_called_once_with(host=self.host)
            api_client.assert_called_once_with(self.configuration)
            note_api.assert_called_once_with(self.api)
            list_notes.assert_called_once_with(self.dataset_id,
                                               self.fhir_store_id,
                                               limit=10, offset=0)
            assert notes == [{
                'id': '12344',
                'noteType': 'foo',
                'patientId': 'pat1',
                'text': 'foobarbaz',
                'note_name': f'dataset/{self.dataset_id}/fhirStores/{self.fhir_store_id}/fhir/Note/12344'
            }]

    def test_get_annotation_store__get(self):
        """Test getting of annotation store"""
        store_example = AnnotationStore(name="fooo")

        with self.config as config,\
            self.api_client as api_client,\
            patch.object(datanode, "AnnotationStoreApi",
                          return_value=self.mock_api) as resource_api,\
            patch.object(self.mock_api, "get_annotation_store",
                         return_value=store_example) as get_store:

            api_client.return_value = api_client
            api_client.__enter__ = Mock(return_value=self.api)
            api_client.__exit__ = Mock(return_value=None)

            store = client.get_annotation_store(
                host=self.host,
                dataset_id =self.dataset_id,
                annotation_store_id = self.fhir_store_id
            )
            config.assert_called_once_with(host=self.host)
            api_client.assert_called_once_with(self.configuration)
            resource_api.assert_called_once_with(self.api)
            get_store.assert_called_once_with(self.dataset_id,
                                              self.fhir_store_id)
            assert store == store_example

    def test_get_annotation_store__not_create(self):
        """Test creating of annotation store if create_if_missing is False"""
        with self.config as config,\
             self.api_client as api_client,\
             patch.object(datanode, "AnnotationStoreApi",
                          return_value=self.mock_api) as resource_api,\
             patch.object(self.mock_api, "get_annotation_store",
                          side_effect=ApiException(status=404)) as get_store,\
             pytest.raises(ApiException):

            api_client.return_value = api_client
            api_client.__enter__ = Mock(return_value=self.api)
            api_client.__exit__ = Mock(return_value=None)

            client.get_annotation_store(
                host=self.host,
                dataset_id = self.dataset_id,
                annotation_store_id = self.annotation_store_id,
            )
            config.assert_called_once_with(host=self.host)
            api_client.assert_called_once_with(self.configuration)
            resource_api.assert_called_once_with(self.api)

    def test_get_annotation_store__create(self):
        """Test creating of annotation store if create_if_missing is True"""
        store_example = AnnotationStore(name="fooo")

        with self.config as config,\
             self.api_client as api_client,\
             patch.object(datanode, "AnnotationStoreApi",
                          return_value=self.mock_api) as resource_api,\
             patch.object(self.mock_api, "get_annotation_store",
                          side_effect=ApiException(status=404)) as get_store,\
             patch.object(self.mock_api, "create_annotation_store",
                          return_value=store_example) as create_store:

            api_client.return_value = api_client
            api_client.__enter__ = Mock(return_value=self.api)
            api_client.__exit__ = Mock(return_value=None)

            store = client.get_annotation_store(
                host=self.host, dataset_id = self.dataset_id,
                annotation_store_id = self.fhir_store_id,
                create_if_missing = True
            )

            config.assert_called_once_with(host=self.host)
            api_client.assert_called_once_with(self.configuration)
            resource_api.assert_called_once_with(self.api)
            get_store.assert_called_once_with(self.dataset_id,
                                              self.fhir_store_id)
            assert store == store_example

    def test_list_annotations(self):
        """Test creating of annotation store if create_if_missing is True"""
        annotation_example = PageOfAnnotations(
            annotations=[Annotation(
                name="12344"
            )],
            offset=0, limit=3, links=Mock(next="")
        )

        with self.config as config,\
             self.api_client as api_client,\
             patch.object(datanode, "AnnotationApi",
                          return_value=self.mock_api) as resource_api,\
             patch.object(self.mock_api, "list_annotations",
                          return_value=annotation_example) as list_annotations:

            api_client.return_value = api_client
            api_client.__enter__ = Mock(return_value=self.api)
            api_client.__exit__ = Mock(return_value=None)

            annotations = client.list_annotations(
                host=self.host, dataset_id = self.dataset_id,
                annotation_store_id = self.annotation_store_id
            )
            assert list(annotations) == [Annotation(name="12344")]

            config.assert_called_once_with(host=self.host)
            api_client.assert_called_once_with(self.configuration)
            resource_api.assert_called_once_with(self.api)
            list_annotations.assert_called_once_with(
                self.dataset_id, self.annotation_store_id,
                offset=0, limit=10
            )
