from unittest.mock import patch

from nlpsandboxclient.client import NlpClient

DATA_NODE_ENDPOINT = "http://0.0.0.0:8080/api/v1"
# Nlp = NlpClient(data_node_endpoint=DATA_NODE_ENDPOINT)

# response = Nlp.rest_get("/notes")

class TestClient:

    def setup_method(self):
        """Method called once per method"""
        print("foo")
        self.nlp = NlpClient(data_node_endpoint=DATA_NODE_ENDPOINT)

    def test_get_clinical_notes(self):
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_clinical_notes()
            rest_get.assert_called_once_with("/notes")

    def test_get_clinical_note(self):
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_clinical_note("12345")
            rest_get.assert_called_once_with("/notes/12345")

    def test_get_health(self):
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_health()
            rest_get.assert_called_once_with("/health")

    def test_get_dates(self):
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_dates()
            rest_get.assert_called_once_with("/annotations/dates")
    