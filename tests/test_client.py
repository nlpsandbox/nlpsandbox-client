"""Test client functions"""
from unittest.mock import Mock, patch

from nlpsandboxclient import api_client
from nlpsandboxclient.api_client import NlpClient, DataNodeClient


class TestClient:
    """Test client class"""

    def setup_method(self):
        """Method called once per method"""
        self.host = api_client.DATA_NODE_HOST
        self.nlpclient = NlpClient(host=self.host)
        self.nlp = DataNodeClient(host=self.host)

    def test_get_clinical_notes(self):
        """Test getting clinical notes"""
        with patch.object(self.nlp, "rest_get_paginated") as rest_get:
            self.nlp.get_clinical_notes(datasetid="foo", storeid="doo")
            rest_get.assert_called_once_with(
                "/datasets/foo/fhirStores/doo/fhir/Note"
            )

    def test_get_clinical_note(self):
        """Test getting clinical note"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_clinical_note(datasetid="foo", storeid="doo",
                                       noteid="boo")
            rest_get.assert_called_once_with(
                "/datasets/foo/fhirStores/doo/fhir/Note/boo"
            )

    def test_get_service(self):
        """Test get service"""
        with patch.object(self.nlpclient, "rest_get") as rest_get:
            self.nlpclient.get_service()
            rest_get.assert_called_once_with("/service")

    def test_get_ui(self):
        """Test get ui"""
        with patch.object(self.nlpclient, "rest_get") as rest_get:
            self.nlpclient.get_ui()
            rest_get.assert_called_once_with("/ui", return_body=False)

    def test_get_datasets(self):
        """Test get datasets"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_datasets()
            rest_get.assert_called_once_with("/datasets")

    def test_get_dataset(self):
        """Test get dataset"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_dataset(datasetid="foo")
            rest_get.assert_called_once_with("/datasets/foo")

    def test_get_annotation_stores(self):
        """Test get annotation stores"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_annotation_stores(datasetid="foo")
            rest_get.assert_called_once_with("/datasets/foo/annotationStore")

    def test_get_annotation_store(self):
        """Test get annotation store"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_annotation_store(datasetid="foo", storeid="doo")
            rest_get.assert_called_once_with(
                "/datasets/foo/annotationStore/doo"
            )

    def test_get_fhir_stores(self):
        """Test get fhir stores"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_fhir_stores(datasetid="foo")
            rest_get.assert_called_once_with("/datasets/foo/fhirStores")

    def test_get_fhir_store(self):
        """Test get fhir store"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_fhir_store(datasetid="foo", storeid="doo")
            rest_get.assert_called_once_with(
                "/datasets/foo/fhirStores/doo"
            )

    def test__build_uri_nonet(self):
        """Tests building of URI no net"""
        uri = self.nlpclient._build_uri("/foo")
        assert uri == f"{self.host}/foo"

    def test__build_uri_net(self):
        """Tests building of URI network in text"""
        text = "http://google.com/foo"
        uri = self.nlpclient._build_uri(text)
        assert uri == text

    def test__build_uri_endpoint(self):
        """Tests building of URI to specify endpoint"""
        uri = self.nlpclient._build_uri("/foo", endpoint="test")
        assert uri == "test/foo"

    def test__rest_call(self):
        """Test rest call"""
        with patch.object(self.nlpclient, "_build_uri",
                          return_value="/foo") as build_uri, \
             patch.object(self.nlpclient._requests_session,
                          "get") as request_get:
            self.nlpclient._rest_call("get", "/foo", None, "http://endpoint")
            build_uri.assert_called_once_with("/foo",
                                              endpoint="http://endpoint")
            request_get.assert_called_once_with("/foo", data=None)

    def test_rest_get(self):
        """Test rest get"""
        with patch.object(self.nlpclient, "_rest_call",
                          return_value="/foo") as rest_call, \
             patch.object(client, "_return_rest_body",
                          return_value='temp') as return_body:
            returned = self.nlpclient.rest_get("/foo",
                                               endpoint="http://endpoint")
            rest_call.assert_called_once_with("get", "/foo", None,
                                              "http://endpoint")
            return_body.assert_called_once_with("/foo")
            assert returned == "temp"


def test__return_rest_body_text():
    """Test return of text"""
    response = Mock()
    response.headers = {"content-type": None}
    text = "testing text me"
    response.text = text
    returned = client._return_rest_body(response)
    assert returned == text


def test__return_rest_body_json():
    """Test return of text"""
    response = Mock()
    response.headers = {"content-type": "Application/json "}
    expected = {"bar": "foo"}
    with patch.object(response, "json",
                      return_value=expected) as response_json:
        returned = client._return_rest_body(response)
        response_json.assert_called_once()
        assert returned == expected
