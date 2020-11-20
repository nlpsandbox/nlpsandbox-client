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

    def get_ui(self, return_body=False):
        """Get the ui of the API"""
        return self.rest_get("/ui", return_body=return_body)

    def rest_get(self, uri, endpoint=None, return_body=True):
        """Sends a HTTP GET request"""
        response = self._rest_call('get', uri, None, endpoint)
        if return_body:
            return _return_rest_body(response)
        return response

    def rest_get_paginated(self, uri, limit=10, offset=0):
        """Get pagniated rest call"""
        new_uri = utils._limit_and_offset(uri, limit=limit, offset=offset)
        while new_uri:
            page = self.rest_get(new_uri)
            new_uri = page['links']['next']
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

    def list_datasets(self):
        """Lists all datasets"""
        return self.rest_get_paginated("/datasets")

    def get_dataset(self, datasetid=None):
        """Get a dataset"""
        return self.rest_get(f"/datasets/{datasetid}")

    def list_annotation_stores(self, datasetid=None):
        """List the annotation stores for a dataset"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/annotationStore"
        )

    def get_annotation_store(self, datasetid=None, storeid=None):
        """Get an annotation store"""
        return self.rest_get(
            f"/datasets/{datasetid}/annotationStore/{storeid}"
        )

    def list_annotations(self, datasetid=None, storeid=None):
        """List the annotations for an annotation store"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/annotationStore/{storeid}/annotations"
        )

    def get_annotation(self, datasetid=None, storeid=None, annotationid=None):
        """Get an annotation"""
        return self.rest_get(
            f"/datasets/{datasetid}/annotationStore/{storeid}/"
            f"annotations/{annotationid}"
        )

    def list_fhir_stores(self, datasetid):
        """List the FHIR stores in a dataset"""
        return self.rest_get(f"/datasets/{datasetid}/fhirStores")

    def get_fhir_store(self, datasetid, storeid):
        """Get a FHIR store"""
        return self.rest_get(f"/datasets/{datasetid}/fhirStores/{storeid}")

    def list_clinical_notes(self, datasetid, storeid):
        """List clinical notes in a FHIR store"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note"
        )

    def get_clinical_note(self, datasetid, storeid, noteid):
        """Get a clinical note"""
        return self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note/{noteid}"
        )

    def list_patients(self, datasetid, storeid):
        """Lists the patients in a FHIR store"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note"
        )

    def get_patient(self, datasetid, storeid, noteid):
        """Get a FHIR patient"""
        return self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note/{noteid}"
        )
