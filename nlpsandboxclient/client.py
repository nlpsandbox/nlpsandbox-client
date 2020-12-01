"""
NLP data node client - This module has convenience functions to interact
with the DataNodeApiClient.
"""
from typing import List

from .api_client import DataNodeApiClient
from .datanode.models import Annotation, AnnotationStore


def get_clinical_notes(host: str, dataset_id: str) -> List[dict]:
    """Get all clinical notes for a dataset

    Args:
        host: Data node host IP.
        dataset_id: Dataset id

    Returns:
        list of clinical notes.

    Examples:
        >>> notes = get_clinical_notes(host="0.0.0.0/api/v1",
        >>>                            dataset_id="awesome-dataset")
        >>> notes[0]
        {
            "id": "noteid",
            "noteType": "",
            "patientId": "patient_id",
            "text": "Example text",
            "note_name": "dataset/awesome-dataset/fhirStores/awesome-fhirstore/fhir/Note/noteid"
        }
    """
    nlp = DataNodeApiClient(host=host)
    fhir_stores = nlp.list_fhir_stores(dataset_id=dataset_id)

    all_notes = []
    # Obtain all clinical notes for all fhir stores in a dataset
    for fhir_store in fhir_stores:
        clinical_notes = nlp.list_notes(dataset_id=dataset_id,
                                        fhir_store_id=fhir_store.id)
        # Obtain all clinical notes
        for note in clinical_notes:
            all_notes.append({
                "id": note.id,
                "noteType": note.note_type,
                "patientId": note.patient_id,
                "text": note.text,
                "note_name": f"dataset/{dataset_id}/fhirStores/{fhir_store.id}/fhir/Note/{note.id}"
            })
    return all_notes


def store_annotation(host: str, annotation_store: AnnotationStore,
                     annotation: dict) -> Annotation:
    """Store annotation

    Args:
        host: Data node host IP.
        annotation_store: AnnotationStore object
        annotation: Annotation dict

    Returns:
        Data node Annotation object

    Examples:
        >>> annotation_store = AnnotationStore(dataset_id="awesome-dataset",
                                               id="annotation-store-store")
        example_annotation = {
            "annotationSource": {
                "resourceSource": {
                    "name": "name"
                }
            },
            "textDateAnnotations": [
                {
                    "dateFormat": "MM/DD/YYYY",
                    "length": 10,
                    "start": 42,
                    "text": "10/26/2020"
                },
                {
                    "dateFormat": "MM/DD/YYYY",
                    "length": 10,
                    "start": 42,
                    "text": "10/26/2020"
                }
            ],
            "textPersonNameAnnotations": [],
            "textPhysicalAddressAnnotations": []
        }
        annotation = store_annotation(host="0.0.0.0/api/v1",
                                      annotation_store=annotation_store,
                                      annotation=example_annotation)

    """
    nlp = DataNodeApiClient(host=host)
    annotation_obj = nlp.create_annotation(
        dataset_id=annotation_store.datasetid,
        annotation_store_id=annotation_store.id,
        annotation=annotation
    )
    return annotation_obj
