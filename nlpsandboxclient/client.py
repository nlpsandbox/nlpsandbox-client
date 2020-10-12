"""NLP client object"""
import urllib.parse

import requests

# Default data node endpoint is localhost
DATA_NODE_ENDPOINT = "http://0.0.0.0:8080/api/v1"


def _return_rest_body(response):
    """Returns either a dictionary or a string depending on the
    'content-type' of the response.
    """
    content_type = response.headers.get('content-type', None)
    if content_type.lower().strip().startswith('application/json'):
        return response.json()
    return response.text


class NlpClient:
    """Nlp client to interact with data node"""
    def __init__(self, data_node_endpoint=None):
        self.data_node_endpoint = data_node_endpoint
        self._requests_session = requests.Session()

    def get_clinical_notes(self):
        clinical_notes = self.rest_get("/notes")
        return clinical_notes

    def get_clinical_note(self, noteid=None):
        clinical_note = self.rest_get(f"/notes/{noteid}")
        return clinical_note

    def rest_get(self, uri, endpoint=None, headers=None):
        """Sends a HTTP GET request"""
        response = self._rest_call('get', uri, None, endpoint, headers)
        return _return_rest_body(response)

    def _rest_call(self, method, uri, data, endpoint, headers):
        """Sends HTTP requests"""
        uri, headers = self._build_uri_and_headers(uri, endpoint=endpoint,
                                                   headers=headers)
        requests_method_fn = getattr(self._requests_session, method)
        response = requests_method_fn(uri, data=data, headers=headers)
        return response

    def _build_uri_and_headers(self, uri, endpoint=None, headers=None):
        """Returns a tuple of the URI and headers to request with."""
        if endpoint is None:
            endpoint = self.data_node_endpoint

        # Check to see if the URI is incomplete (i.e. a Synapse URL)
        # In that case, append a Synapse endpoint to the URI
        parsed_url = urllib.parse.urlparse(uri)
        if parsed_url.netloc == '':
            uri = endpoint + uri

        return uri, headers
