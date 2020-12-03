"""NLP data node client that interacts with the SDK datanodeclient"""
import os
from typing import List

import datanodeclient

DATA_NODE_HOST = "http://10.23.55.45:8080/api/v1"


def get_notes(host: str, dataset_id: str, fhir_store_id: str) -> List[dict]:
    """Get all clinical notes for a dataset

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        fhir_store_id: FHIR store Id

    Returns:
        list of clinical notes.

    Examples:
        >>> notes = get_clinical_notes(host="0.0.0.0/api/v1",
        >>>                            dataset_id="awesome-dataset",
        >>>                            fhir_store_id="awesome-fhir-store")
        >>> notes[0]
        {
            "id": "noteid",
            "noteType": "",
            "patientId": "patient_id",
            "text": "Example text",
            "note_name": "dataset/awesome-dataset/fhirStores/awesome-fhirstore/fhir/Note/noteid"
        }
    """
    configuration = datanodeclient.Configuration(
        host = host
    )
    all_notes = []
    with datanodeclient.ApiClient(configuration) as api_client:
        fhir_store_api = datanodeclient.FhirStoreApi(api_client)
        note_api = datanodeclient.NoteApi(api_client)

        fhir_stores = fhir_store_api.list_fhir_stores(dataset_id)
        for fhir_store in fhir_stores.fhir_stores:
            fhir_store_id = os.path.basename(fhir_store.name)
            # Obtain all clinical notes for all fhir stores in a dataset
            notes = note_api.list_notes(dataset_id, fhir_store_id)

            for note in notes.notes:
                all_notes.append({
                    "id": note.id,
                    "noteType": note.note_type,
                    "patientId": note.patient_id,
                    "text": note.text,
                    "note_name": f"dataset/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Note/{note.id}"
                })
    return all_notes


def store_annotation(host: str, dataset_id: str, annotation_store_id: str,
                     annotation: dict) -> datanodeclient.models.Annotation:
    """Store annotation

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        annotation_store_id: Annotation store Id
        annotation: Annotation dict

    Returns:
        Data node Annotation object

    Examples:
        >>> example_annotation = {
        >>>     "annotationSource": {
        >>>         "resourceSource": {
        >>>             "name": "name"
        >>>         }
        >>>     },
        >>>     "textDateAnnotations": [
        >>>         {
        >>>             "dateFormat": "MM/DD/YYYY",
        >>>             "length": 10,
        >>>             "start": 42,
        >>>             "text": "10/26/2020"
        >>>         },
        >>>         {
        >>>             "dateFormat": "MM/DD/YYYY",
        >>>             "length": 10,
        >>>             "start": 42,
        >>>             "text": "10/26/2020"
        >>>         }
        >>>     ],
        >>>     "textPersonNameAnnotations": [],
        >>>     "textPhysicalAddressAnnotations": []
        >>> }
        >>> annotation = store_annotation(host="0.0.0.0/api/v1",
        >>>                               dataset_id="awesome-dataset",
        >>>                               annotation_store_id="awesome-annotation-store",
        >>>                               annotation=example_annotation)

    """
    configuration = datanodeclient.Configuration(
        host = host
    )
    with datanodeclient.ApiClient(configuration) as api_client:
        annotation_api = datanodeclient.AnnotationApi(api_client)
        annotation_obj = annotation_api.create_annotation(
            dataset_id=dataset_id,
            annotation_store_id=annotation_store_id,
            annotation=annotation
        )
    return annotation_obj
