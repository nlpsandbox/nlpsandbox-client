"""Test client functions"""
from unittest.mock import patch

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
