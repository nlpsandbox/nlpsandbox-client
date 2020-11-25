"""
NLP SDK client.  For developers only - interfaces with the API and
does not assume user behavior for how functions would be used.
"""
import json
import urllib.parse

import requests
from synapseclient.core import utils

from . import exceptions

# Default data node endpoint
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


class NlpApiClient:
    """Nlp base client that does generic rest calls"""
    def __init__(self, host: str = None):
        self.host = host
        self._requests_session = requests.Session()

    def get_service(self):
        """Get the health of the API"""
        return self.rest_get("/service")

    def get_ui(self, return_body: bool = False):
        """Get the ui of the API"""
        return self.rest_get("/ui", return_body=return_body)

    def rest_get(self, uri: str, endpoint: str = None,
                 return_body: bool = True):
        """Sends a HTTP GET request"""
        response = self._rest_call('get', uri, None, endpoint)
        if return_body:
            return _return_rest_body(response)
        return response

    def rest_post(self, uri: str, body: str, endpoint: str = None):
        """Sends an HTTP POST request."""
        response = self._rest_call(
            'post', uri, body, endpoint,
            headers={'Content-Type': 'application/json'}
        )
        return _return_rest_body(response)

    def rest_get_paginated(self, uri, limit=10, offset=0):
        """Get pagniated rest call"""
        new_uri = utils._limit_and_offset(uri, limit=limit, offset=offset)
        while new_uri:
            page = self.rest_get(new_uri)
            new_uri = page['links']['next']
            yield page

    def _rest_call(self, method, uri, data, endpoint, headers=None):
        """Sends HTTP requests"""
        uri = self._build_uri(uri, endpoint=endpoint)
        requests_method_fn = getattr(self._requests_session, method)
        response = requests_method_fn(uri, data=data, headers=headers)
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


class DataNodeApiClient(NlpApiClient):
    """Nlp client to interact with data node"""

    def list_datasets(self):
        """Lists all datasets"""
        return self.rest_get_paginated("/datasets")

    def get_dataset(self, datasetid: str):
        """Get a dataset"""
        return self.rest_get(f"/datasets/{datasetid}")

    def create_dataset(self, datasetid: str):
        """Create a dataset"""
        return self.rest_post(f"/datasets?datasetId={datasetid}",
                              body=json.dumps({}))

    def list_annotation_stores(self, datasetid: str):
        """List the annotation stores for a dataset"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/annotationStores"
        )

    def get_annotation_store(self, datasetid: str, annotation_storeid: str):
        """Get an annotation store"""
        return self.rest_get(
            f"/datasets/{datasetid}/annotationStores/{annotation_storeid}"
        )

    def create_annotation_store(self, datasetid: str,
                                annotation_storeid: str):
        """Create an annotation store"""
        return self.rest_post(
            f"/datasets/{datasetid}/annotationStores?"
            f"annotationStoreId={annotation_storeid}",
            body=json.dumps({})
        )

    def list_annotations(self, datasetid: str, annotation_storeid: str):
        """List the annotations for an annotation store"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/annotationStores/"
            f"{annotation_storeid}/annotations"
        )

    def get_annotation(self, datasetid: str, annotation_storeid: str,
                       annotationid: str):
        """Get an annotation"""
        return self.rest_get(
            f"/datasets/{datasetid}/annotationStores/{annotation_storeid}/"
            f"annotations/{annotationid}"
        )

    def create_annotation(self, datasetid: str, annotation_storeid: str,
                          annotation: dict):
        """Create an annotation"""
        return self.rest_post(
            f"/datasets/{datasetid}/annotationStore/"
            f"{annotation_storeid}/annotations",
            body=json.dumps(annotation)
        )

    def list_fhir_stores(self, datasetid: str):
        """List the FHIR stores in a dataset"""
        return self.rest_get_paginated(f"/datasets/{datasetid}/fhirStores")

    def get_fhir_store(self, datasetid: str, fhir_storeid: str):
        """Get a FHIR store"""
        return self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}"
        )

    def create_fhir_store(self, datasetid: str, fhir_storeid: str):
        """Create a FHIR store"""
        return self.rest_post(
            f"/datasets/{datasetid}/fhirStores?fhirStoreId={fhir_storeid}",
            body=json.dumps({})
        )

    def list_clinical_notes(self, datasetid: str, fhir_storeid: str):
        """List clinical notes in a FHIR store"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/Note"
        )

    def get_clinical_note(self, datasetid: str, fhir_storeid: str,
                          noteid: str):
        """Get a clinical note"""
        return self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/"
            f"Note/{noteid}"
        )

    def create_clinical_note(self, datasetid: str, fhir_storeid: str,
                             note: dict):
        """Create a clinical note"""
        return self.rest_post(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/Note",
            body=json.dumps(note)
        )

    def list_patients(self, datasetid: str, fhir_storeid: str):
        """Lists the patients in a FHIR store"""
        return self.rest_get_paginated(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/Patient"
        )

    def get_patient(self, datasetid: str, fhir_storeid: str, patientid: str):
        """Get a FHIR patient"""
        return self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/"
            f"Patient/{patientid}"
        )

    def create_patient(self, datasetid: str, fhir_storeid: str,
                       patient: dict):
        """Create a FHIR patient"""
        return self.rest_post(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/Patient",
            body=json.dumps(patient)
        )
