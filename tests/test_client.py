"""Test client functions"""
import requests
from unittest.mock import Mock, patch

from nlpsandboxclient import client
from nlpsandboxclient.client import NlpClient


class TestClient:
    """Test client class"""

    def setup_method(self):
        """Method called once per method"""
        self.data_node_endpoint = "http://0.0.0.0:8080/api/v1"
        self.nlp = NlpClient(data_node_endpoint=self.data_node_endpoint)

    def test_get_clinical_notes(self):
        """Test getting clinical notes"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_clinical_notes()
            rest_get.assert_called_once_with("/notes")

    def test_get_clinical_note(self):
        """Test getting clinical note"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_clinical_note("12345")
            rest_get.assert_called_once_with("/notes/12345")

    def test_get_health(self):
        """Test get health"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_health()
            rest_get.assert_called_once_with("/health")

    def test_get_dates(self):
        """Test get dates"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_dates()
            rest_get.assert_called_once_with("/annotations/dates")

    def test__build_uri_nonet(self):
        """Tests building of URI no net"""
        uri = self.nlp._build_uri("/foo")
        assert uri == f"{self.data_node_endpoint}/foo"

    def test__build_uri_net(self):
        """Tests building of URI network in text"""
        text = "http://google.com/foo"
        uri = self.nlp._build_uri(text)
        assert uri == text

    def test__build_uri_endpoint(self):
        """Tests building of URI to specify endpoint"""
        uri = self.nlp._build_uri("/foo", endpoint="test")
        assert uri == "test/foo"

    def test__rest_call(self):
        """Test rest call"""
        with patch.object(self.nlp, "_build_uri",
                          return_value="/foo") as build_uri, \
             patch.object(self.nlp._requests_session,
                          "get") as request_get:
            self.nlp._rest_call("get", "/foo", None, "http://endpoint")
            build_uri.assert_called_once_with("/foo",
                                              endpoint="http://endpoint")
            request_get.assert_called_once_with("/foo", data=None)


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
