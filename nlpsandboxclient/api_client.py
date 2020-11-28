"""
NLP SDK client.  For developers only - interfaces with the API and
does not assume user behavior for how functions would be used.
"""
import os
from typing import Iterator
import urllib.parse

import requests
from synapseclient import core

from . import utils
from .datanode.models import (Annotation, AnnotationStore, Dataset,
                              FhirStore, Note, Patient)

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
        if host is None:
            host = DATA_NODE_HOST
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
            'post', uri, body, endpoint
        )
        return _return_rest_body(response)

    def rest_get_paginated(self, uri, limit=10, offset=0):
        """Get pagniated rest call"""
        new_uri = core.utils._limit_and_offset(uri, limit=limit, offset=offset)
        while new_uri:
            page = self.rest_get(new_uri)
            new_uri = page['links']['next']
            # Make sure to only return the list of resources
            page.pop("limit")
            page.pop("links")
            page.pop("offset")
            # This will yield the list of resources
            # 'dict_keys' object is not subscriptable
            resouces = page.pop(list(page.keys())[0])
            for resource in resouces:
                yield resource

    def _rest_call(self, method, uri, data, endpoint, headers=None):
        """Sends HTTP requests"""
        uri = self._build_uri(uri, endpoint=endpoint)
        requests_method_fn = getattr(self._requests_session, method)
        response = requests_method_fn(uri, json=data, headers=headers)
        utils._raise_for_status(response)
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

    def list_datasets(self) -> Iterator[Dataset]:
        """Lists all datasets"""
        datasets = self.rest_get_paginated("/datasets")
        for dataset in datasets:
            # The id of the dataset is found in datasets/{datasetId}
            # Which is the basename
            yield Dataset(id=os.path.basename(dataset['name']), **dataset)

    def get_dataset(self, datasetid: str) -> Dataset:
        """Get a dataset"""
        dataset = self.rest_get(f"/datasets/{datasetid}")
        return Dataset(id=datasetid, **dataset)

    def create_dataset(self, datasetid: str) -> Dataset:
        """Create a dataset"""
        dataset = self.rest_post(f"/datasets?datasetId={datasetid}",
                                 body={})
        return Dataset(id=datasetid, **dataset)

    def list_annotation_stores(self,
                               datasetid: str) -> Iterator[AnnotationStore]:
        """List the annotation stores for a dataset"""
        annotation_stores = self.rest_get_paginated(
            f"/datasets/{datasetid}/annotationStores"
        )
        for store in annotation_stores:
            yield AnnotationStore(datasetid=datasetid,
                                  id=os.path.basename(store['name']),
                                  **store)

    def get_annotation_store(self, datasetid: str,
                             annotation_storeid: str) -> AnnotationStore:
        """Get an annotation store"""
        store = self.rest_get(
            f"/datasets/{datasetid}/annotationStores/{annotation_storeid}"
        )
        return AnnotationStore(datasetid=datasetid, id=annotation_storeid,
                               **store)

    def create_annotation_store(self, datasetid: str,
                                annotation_storeid: str) -> AnnotationStore:
        """Create an annotation store"""
        store = self.rest_post(
            f"/datasets/{datasetid}/annotationStores?"
            f"annotationStoreId={annotation_storeid}",
            body={}
        )
        return AnnotationStore(datasetid=datasetid, id=annotation_storeid,
                               **store)

    def list_annotations(self, datasetid: str,
                         annotation_storeid: str) -> Iterator[Annotation]:
        """List the annotations for an annotation store"""
        annotations = self.rest_get_paginated(
            f"/datasets/{datasetid}/annotationStores/"
            f"{annotation_storeid}/annotations"
        )
        for annotation in annotations:
            yield Annotation(datasetid=datasetid,
                             annotation_storeid=annotation_storeid,
                             id=os.path.basename(annotation['name']),
                             **annotation)

    def get_annotation(self, datasetid: str, annotation_storeid: str,
                       annotationid: str) -> Annotation:
        """Get an annotation"""
        annotation = self.rest_get(
            f"/datasets/{datasetid}/annotationStores/{annotation_storeid}/"
            f"annotations/{annotationid}"
        )
        return Annotation(datasetid=datasetid,
                          annotation_storeid=annotation_storeid,
                          id=annotationid,
                          **annotation)

    def create_annotation(self, datasetid: str, annotation_storeid: str,
                          annotation: dict) -> Annotation:
        """Create an annotation"""
        annotation = self.rest_post(
            f"/datasets/{datasetid}/annotationStores/"
            f"{annotation_storeid}/annotations",
            body=annotation
        )
        return Annotation(datasetid=datasetid,
                          annotation_storeid=annotation_storeid,
                          id=os.path.basename(annotation['name']),
                          **annotation)

    def list_fhir_stores(self, datasetid: str) -> Iterator[FhirStore]:
        """List the FHIR stores in a dataset"""
        fhir_stores = self.rest_get_paginated(
            f"/datasets/{datasetid}/fhirStores"
        )
        for fhir_store in fhir_stores:
            yield FhirStore(datasetid=datasetid,
                            id=os.path.basename(fhir_store['name']),
                            **fhir_store)

    def get_fhir_store(self, datasetid: str, fhir_storeid: str) -> FhirStore:
        """Get a FHIR store"""
        fhir_store = self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}"
        )
        return FhirStore(datasetid=datasetid, id=fhir_storeid,
                         **fhir_store)

    def create_fhir_store(self, datasetid: str,
                          fhir_storeid: str) -> FhirStore:
        """Create a FHIR store"""
        fhir_store = self.rest_post(
            f"/datasets/{datasetid}/fhirStores?fhirStoreId={fhir_storeid}",
            body={}
        )
        return FhirStore(datasetid=datasetid, id=fhir_storeid,
                         **fhir_store)

    def list_clinical_notes(self, datasetid: str,
                            fhir_storeid: str) -> Iterator[Note]:
        """List clinical notes in a FHIR store"""
        notes = self.rest_get_paginated(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/Note"
        )
        for note in notes:
            yield Note(datasetid=datasetid, fhir_storeid=fhir_storeid, **note)

    def get_clinical_note(self, datasetid: str, fhir_storeid: str,
                          noteid: str) -> Note:
        """Get a clinical note"""
        note = self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/"
            f"Note/{noteid}"
        )
        return Note(datasetid=datasetid, fhir_storeid=fhir_storeid, **note)

    def create_clinical_note(self, datasetid: str, fhir_storeid: str,
                             note: dict) -> Note:
        """Create a clinical note

        Args:
            datasetid: Dataset id
            fhir_storeid: FHIR store id
            note: Note request body
        """
        note_body = self.rest_post(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/Note",
            body=note
        )
        return Note(datasetid=datasetid, fhir_storeid=fhir_storeid,
                    **note_body)

    def list_patients(self, datasetid: str,
                      fhir_storeid: str) -> Iterator[Patient]:
        """Lists the patients in a FHIR store"""
        patients = self.rest_get_paginated(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/Patient"
        )
        for patient in patients:
            yield Patient(datasetid=datasetid, fhir_storeid=fhir_storeid,
                          **patient)

    def get_patient(self, datasetid: str, fhir_storeid: str,
                    patientid: str) -> Patient:
        """Get a FHIR patient"""
        patient = self.rest_get(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/"
            f"Patient/{patientid}"
        )
        return Patient(datasetid=datasetid, fhir_storeid=fhir_storeid,
                       **patient)

    def create_patient(self, datasetid: str, fhir_storeid: str,
                       patient: dict) -> Patient:
        """Create a FHIR patient"""
        patient = self.rest_post(
            f"/datasets/{datasetid}/fhirStores/{fhir_storeid}/fhir/Patient",
            body=patient
        )
        return Patient(datasetid=datasetid, fhir_storeid=fhir_storeid,
                       **patient)
