"""NLP data node client that interacts with the SDK datanodeclient"""
from typing import List, Iterator

import datanode
from datanode.models import Annotation, AnnotationStore

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
        >>> notes = get_notes(host="0.0.0.0/api/v1",
        >>>                   dataset_id="awesome-dataset",
        >>>                   fhir_store_id="awesome-fhir-store")
        >>> notes[0]
        {
            "id": "noteid",
            "noteType": "",
            "patientId": "patient_id",
            "text": "Example text",
            "note_name": "dataset/awesome-dataset/fhirStores/awesome-fhirstore/fhir/Note/noteid"
        }
    """
    configuration = datanode.Configuration(host=host)
    all_notes = []
    offset = 0
    limit = 10
    with datanode.ApiClient(configuration) as api_client:
        note_api = datanode.NoteApi(api_client)
        # Obtain all clinical notes
        next_page = True
        while next_page:
            notes = note_api.list_notes(dataset_id, fhir_store_id,
                                        offset=offset, limit=limit)
            # change from snake case to camel case
            sanitized_notes = api_client.sanitize_for_serialization(
                notes.notes
            )
            for note in sanitized_notes:
                note["note_name"] = f"dataset/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Note/{note['id']}"
                all_notes.append(note)
            next_page = notes.links.next
            offset += limit
    return all_notes


def get_annotation_store(host: str, dataset_id: str,
                         annotation_store_id: str,
                         create_if_missing: bool = False) -> AnnotationStore:
    """Creates an annotation store

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        annotation_store_id: Annotation store Id
        create_if_missing: Creates annotation store if the resource
                           doesn't exist

    Returns:
        Data node Annotation Store object

    Examples:
        >>> annotation = create_annotation_store(
        >>>     host="0.0.0.0/api/v1", dataset_id="awesome-dataset",
        >>>     annotation_store_id="awesome-annotation-store"
        >>> )

    """
    configuration = datanode.Configuration(host=host)
    with datanode.ApiClient(configuration) as api_client:
        annotation_store_api = datanode.AnnotationStoreApi(api_client)
        try:
            # get the annotation store
            annotation_store_obj = annotation_store_api.get_annotation_store(
                dataset_id, annotation_store_id
            )
        except datanode.rest.ApiException as err:
            if err.status == 404 and create_if_missing:
                annotation_store_obj = annotation_store_api.create_annotation_store(
                    dataset_id, annotation_store_id, annotation_store={}
                )
            else:
                raise err
    return annotation_store_obj


def store_annotation(host: str, dataset_id: str, annotation_store_id: str,
                     annotation: dict) -> Annotation:
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
    configuration = datanode.Configuration(host=host)
    with datanode.ApiClient(configuration) as api_client:
        annotation_api = datanode.AnnotationApi(api_client)
        annotation_obj = annotation_api.create_annotation(
            dataset_id=dataset_id,
            annotation_store_id=annotation_store_id,
            annotation=annotation
        )
    return annotation_obj


def list_annotations(host: str, dataset_id: str,
                     annotation_store_id: str) -> Iterator[Annotation]:
    """List annotations

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        annotation_store_id: Annotation store Id

    Yields:
        Data node annotation objects

    Examples:
        >>> annotations = get_annotations(host="0.0.0.0/api/v1",
        >>>                               dataset_id="awesome-dataset",
        >>>                               annotation_store_id="awesome-annotation-store")

    """
    configuration = datanode.Configuration(host=host)
    offset = 0
    limit = 10
    with datanode.ApiClient(configuration) as api_client:
        annotation_api = datanode.AnnotationApi(api_client)
        next_page = True
        while next_page:
            annotations = annotation_api.list_annotations(
                dataset_id, annotation_store_id,
                offset=offset, limit=limit
            )
            # change from snake case to camel case
            sanitized_annotations = api_client.sanitize_for_serialization(
                annotations.annotations
            )
            for annotation in sanitized_annotations:
                yield annotation
            next_page = annotations.links.next
            offset += limit
