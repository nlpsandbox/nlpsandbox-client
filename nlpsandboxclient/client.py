"""NLP client object"""
import urllib.parse

import requests
from synapseclient.core import utils

from . import exceptions

# Default data node endpoint is localhost
# DATA_NODE_HOST = "http://0.0.0.0:8080/api/v1"
# add this as default for now
DATA_NODE_HOST = "http://10.23.55.45:8080/api/v1"


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
    """Nlp base client that does generic rest calls"""
    def __init__(self, host=None):
        self.host = host
        self._requests_session = requests.Session()

    def get_service(self):
        """Get the health of the API"""
        return self.rest_get("/service")

    # def get_ui(self, return_body=False):
    #     """Get the ui of the API"""
    #     return self.rest_get("/ui", return_body=return_body)

    def rest_get(self, uri, endpoint=None, return_body=True):
        """Sends a HTTP GET request"""
        response = self._rest_call('get', uri, None, endpoint)
        if return_body:
            return _return_rest_body(response)
        return response

    def rest_get_paginated(self, uri, limit=10, offset=0):
        """Get pagniated rest call"""
        next_results = True
        while next_results:
            uri = utils._limit_and_offset(uri, limit=limit, offset=offset)
            page = self.rest_get(uri)
            next_results = page['links']['next']
            offset += limit
            yield page

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
            endpoint = self.host
        # Check to see if the URI is incomplete
        # In that case, append a endpoint to the URI
        parsed_url = urllib.parse.urlparse(uri)
        if parsed_url.netloc == '':
            uri = endpoint + uri
        return uri


class DataNodeClient(NlpClient):
    """Nlp client to interact with data node"""

    # def get_clinical_notes(self):
    #     """Returns all clinical notes"""
    #     return self.rest_get("/notes")

    def get_datasets(self):
        """Returns all datasets"""
        return self.rest_get("/datasets")

    def get_dataset(self, datasetid=None):
        """Returns a dataset"""
        return self.rest_get(f"/datasets/{datasetid}")

    def get_annotation_stores(self, datasetid=None):
        """Returns the annotation stores for a dataset"""
        return self.rest_get(f"/datasets/{datasetid}/annotationStore")

    def get_annotation_store(self, datasetid=None, storeid=None):
        """Returns a annotation store for a specific annotation store id"""
        return self.rest_get(
            f"/datasets/{datasetid}/annotationStore/{storeid}"
        )

    def get_fhir_stores(self, datasetid):
        """Returns the fhir stores for a dataset"""
        return self.rest_get(f"/datasets/{datasetid}/fhirStores")

    def get_fhir_store(self, datasetid, storeid):
        """Returns the fhir store for a specific fhir store id"""
        return self.rest_get(f"/datasets/{datasetid}/fhirStores/{storeid}")

    def get_clinical_notes(self, datasetid, storeid):
        """Returns the clinical note for a given ID"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note"
        )

    def get_clinical_note(self, datasetid, storeid, noteid):
        """Returns the clinical note for a given ID"""
        return self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note/{noteid}"
        )

    def get_dates(self):
        """Get all date annotations"""
        return self.rest_get("/annotations/dates")
