"""NLP client object"""
import urllib.parse

import requests

from . import exceptions

# Default data node endpoint is localhost
DATA_NODE_ENDPOINT = "http://0.0.0.0:8080/api/v1"


def _return_rest_body(response):
    """Returns either a dictionary or a string depending on the
    'content-type' of the response.
    """
    content_type = response.headers.get('content-type', None)
    if content_type is not None and content_type.lower().strip().startswith(
            'application/json'):
        return response.json()
    return response.text


class NlpClient:
    """Nlp client to interact with data node"""
    def __init__(self, data_node_endpoint=None):
        self.data_node_endpoint = data_node_endpoint
        self._requests_session = requests.Session()

    def get_clinical_notes(self):
        """Returns all clinical notes"""
        return self.rest_get("/notes")

    def get_clinical_note(self, noteid=None):
        """Returns the clinical note for a given ID"""
        return self.rest_get(f"/notes/{noteid}")

    def get_health(self):
        """Get the health of the API"""
        return self.rest_get("/health")

    def get_dates(self):
        """Get all date annotations"""
        return self.rest_get("/annotations/dates")

    def rest_get(self, uri, endpoint=None):
        """Sends a HTTP GET request"""
        response = self._rest_call('get', uri, None, endpoint)
        return _return_rest_body(response)

    def _rest_call(self, method, uri, data, endpoint):
        """Sends HTTP requests"""
        uri = self._build_uri(uri, endpoint=endpoint)
        requests_method_fn = getattr(self._requests_session, method)
        response = requests_method_fn(uri, data=data)
        exceptions._raise_for_status(response)
        return response

    def _build_uri(self, uri, endpoint=None):
        """Returns a URI to request with."""
        if endpoint is None:
            endpoint = self.data_node_endpoint
        # Check to see if the URI is incomplete
        # In that case, append a endpoint to the URI
        parsed_url = urllib.parse.urlparse(uri)
        if parsed_url.netloc == '':
            uri = endpoint + uri
        return uri
