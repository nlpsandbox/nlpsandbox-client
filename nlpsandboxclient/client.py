"""NLP data node client that interacts with the NLP SDK client"""
from typing import List, Iterator, Union

import requests

import nlpsandbox
from nlpsandbox.models import (
    Annotation, AnnotationStore, Dataset, Note, Tool
)
from nlpsandbox.api import (
    annotation_store_api, annotation_api, dataset_api, note_api,
    text_contact_annotation_api,
    text_covid_symptom_annotation_api,
    text_date_annotation_api,
    text_id_annotation_api,
    text_person_name_annotation_api,
    text_location_annotation_api,
    tool_api,
)
from . import utils

DATA_NODE_HOST = "http://0.0.0.0:8080/api/v1"


def list_notes(host: str, dataset_id: str, fhir_store_id: str) -> List[dict]:
    """Get all clinical notes for a dataset

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        fhir_store_id: FHIR store Id

    Yields:
        list of clinical notes.

    Examples:
        >>> notes = get_notes(host="0.0.0.0/api/v1",
        >>>                   dataset_id="awesome-dataset",
        >>>                   fhir_store_id="awesome-fhir-store")
        >>> list(notes)[0]
        {
            "id": "noteid",
            "noteType": "",
            "patientId": "patient_id",
            "text": "Example text",
            "note_name": "dataset/awesome-dataset/fhirStores/awesome-fhirstore/fhir/Note/noteid"
        }
    """
    configuration = utils.get_api_configuration(host=host)
    offset = 0
    limit = 10
    with nlpsandbox.ApiClient(configuration) as api_client:
        note_instance = note_api.NoteApi(api_client)
        # Obtain all clinical notes
        next_page = True
        while next_page:
            notes = note_instance.list_notes(dataset_id, fhir_store_id,
                                             offset=offset, limit=limit)
            # change from snake case to camel case
            sanitized_notes = api_client.sanitize_for_serialization(
                notes.notes
            )
            for note in sanitized_notes:
                # note_name is added for convenience for the controller as
                # it is needed to store the annotations
                note["note_name"] = f"dataset/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Note/{note['identifier']}"
                yield note
            next_page = notes.links.next
            offset += limit


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
    configuration = utils.get_api_configuration(host=host)
    with nlpsandbox.ApiClient(configuration) as api_client:
        annot_store_instance = annotation_store_api.AnnotationStoreApi(
            api_client
        )
        try:
            # get the annotation store
            annotation_store_obj = annot_store_instance.get_annotation_store(
                dataset_id, annotation_store_id
            )
        except nlpsandbox.rest.ApiException as err:
            if err.status == 404 and create_if_missing:
                annotation_store_obj = annot_store_instance.create_annotation_store(
                    dataset_id, annotation_store_id, body={}
                )
            else:
                raise err
    return annotation_store_obj


def get_annotation(host: str, dataset_id: str,
                   annotation_store_id: str,
                   annotation_id: str) -> Annotation:
    """Gets an annotation

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        annotation_store_id: Annotation store Id
        annotation_id: Annotation Id

    Returns:
        Data node Annotation object

    Examples:
        >>> annotation = get_annotation(
        >>>     host="0.0.0.0/api/v1", dataset_id="awesome-dataset",
        >>>     annotation_store_id="awesome-annotation-store",
        >>>     annotation_id="awesome-annotation"
        >>> )

    """
    configuration = utils.get_api_configuration(host=host)
    with nlpsandbox.ApiClient(configuration) as api_client:
        annot_instance = annotation_api.AnnotationApi(
            api_client
        )
        # get the annotation store
        annotation_store_obj = annot_instance.get_annotation(
            dataset_id, annotation_store_id, annotation_id
        )
    return annotation_store_obj


def _store_annotation(host: str, dataset_id: str, annotation_store_id: str,
                      annotation_id: str, annotation: dict) -> Annotation:
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
        >>>     "textLocationAnnotations": []
        >>> }
        >>> annotation = store_annotation(host="0.0.0.0/api/v1",
        >>>                               dataset_id="awesome-dataset",
        >>>                               annotation_store_id="awesome-annotation-store",
        >>>                               annotation_id="awesome-id",
        >>>                               annotation=example_annotation)

    """

    configuration = utils.get_api_configuration(host=host)
    with nlpsandbox.ApiClient(configuration) as api_client:
        annotation_instance = annotation_api.AnnotationApi(api_client)
        new_annotation = utils.change_keys(annotation,
                                           utils.camelcase_to_snakecase)
        annotation_obj = annotation_instance.create_annotation(
            dataset_id=dataset_id,
            annotation_store_id=annotation_store_id,
            annotation_id=annotation_id,
            annotation_create_request=new_annotation,
            async_req=True
        )
    return annotation_obj.get()


def list_annotations(host: str, dataset_id: str,
                     annotation_store_id: str) -> Iterator[dict]:
    """List annotations

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        annotation_store_id: Annotation store Id

    Yields:
        Data node annotation objects

    Examples:
        >>> annotations = list_annotations(host="0.0.0.0/api/v1",
        >>>                                dataset_id="awesome-dataset",
        >>>                                annotation_store_id="awesome-annotation-store")

    """
    configuration = utils.get_api_configuration(host=host)
    offset = 0
    limit = 10
    with nlpsandbox.ApiClient(configuration) as api_client:
        annotation_instance = annotation_api.AnnotationApi(api_client)
        next_page = True
        while next_page:
            annotations = annotation_instance.list_annotations(
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


def _annotate_person_name(api_client, text_annotation_request: dict) -> dict:
    """Annotate notes with date

    Args:
        host: Data node host IP
        text_annotation_request: Text person name annotation request

    Yields:
        Annotated notes

    Examples:
        >>> example_request = {
        >>>    "note": {
        >>>        "identifier": "note-1",
        >>>        "type": "loinc:LP29684-5",
        >>>        "patient_id": "507f1f77bcf86cd799439011",
        >>>        "text": "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott."
        >>>    }
        >>> }
        >>> host = "0.0.0.0/api/v1"
        >>> configuration = utils.get_api_configuration(host=host)
        >>> with nlpsandbox.ApiClient(configuration) as api_client:
        >>>     annotations = _annotate_person_name(
        >>>         api_client=api_client,
        >>>         text_annotation_request=example_request
        >>>     )

    """
    api_instance = text_person_name_annotation_api.TextPersonNameAnnotationApi(api_client)
    annotations = api_instance.create_text_person_name_annotations(
        text_person_name_annotation_request=text_annotation_request
    )
    return annotations


def _annotate_location(api_client, text_annotation_request: dict) -> dict:
    """Annotate notes with date

    Args:
        host: Data node host IP
        text_annotation_request: Text location annotation request

    Yields:
        Annotated notes

    Examples:
        >>> example_request = {
        >>>    "note": {
        >>>        "identifier": "note-1",
        >>>        "type": "loinc:LP29684-5",
        >>>        "patient_id": "507f1f77bcf86cd799439011",
        >>>        "text": "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott."
        >>>    }
        >>> }
        >>> host = "0.0.0.0/api/v1"
        >>> configuration = utils.get_api_configuration(host=host)
        >>> with nlpsandbox.ApiClient(configuration) as api_client:
        >>>     annotations = _annotate_location(
        >>>         api_client=api_client,
        >>>         text_annotation_request=example_request
        >>>     )

    """
    api_instance = text_location_annotation_api.TextLocationAnnotationApi(api_client)
    annotations = api_instance.create_text_location_annotations(
        text_location_annotation_request=text_annotation_request
    )
    return annotations


def _annotate_date(api_client, text_annotation_request: dict) -> dict:
    """Annotate notes with date

    Args:
        host: Data node host IP
        text_annotation_request: Text date annotation request

    Yields:
        Annotated notes

    Examples:
        >>> example_request = {
        >>>    "note": {
        >>>        "identifier": "note-1",
        >>>        "type": "loinc:LP29684-5",
        >>>        "patient_id": "507f1f77bcf86cd799439011",
        >>>        "text": "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott."
        >>>    }
        >>> }
        >>> host = "0.0.0.0/api/v1"
        >>> configuration = utils.get_api_configuration(host=host)
        >>> with nlpsandbox.ApiClient(configuration) as api_client:
        >>>     annotations = _annotate_person(
        >>>         api_client=api_client,
        >>>         text_annotation_request=example_request
        >>> )

    """
    api_instance = text_date_annotation_api.TextDateAnnotationApi(api_client)
    annotations = api_instance.create_text_date_annotations(
        text_date_annotation_request=text_annotation_request
    )
    return annotations


def _annotate_contact(api_client, text_annotation_request: dict) -> dict:
    """Annotate notes with contact

    Args:
        host: Data node host IP
        text_annotation_request: Text contact annotation request

    Yields:
        Annotated notes

    Examples:
        >>> example_request = {
        >>>    "note": {
        >>>        "identifier": "note-1",
        >>>        "type": "loinc:LP29684-5",
        >>>        "patient_id": "507f1f77bcf86cd799439011",
        >>>        "text": "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott. Her phone number is 203-555-4545."
        >>>    }
        >>> }
        >>> host = "0.0.0.0/api/v1"
        >>> configuration = utils.get_api_configuration(host=host)
        >>> with nlpsandbox.ApiClient(configuration) as api_client:
        >>>     annotations = _annotate_contact(
        >>>         api_client=api_client,
        >>>         text_annotation_request=example_request
        >>>     )

    """
    api_instance = text_contact_annotation_api.TextContactAnnotationApi(
        api_client
    )
    annotations = api_instance.create_text_contact_annotations(
        text_contact_annotation_request=text_annotation_request
    )
    return annotations


def _annotate_id(api_client, text_annotation_request: dict) -> dict:
    """Annotate notes with id

    Args:
        host: Data node host IP
        text_annotation_request: Text id annotation request

    Yields:
        Annotated notes

    Examples:
        >>> example_request = {
        >>>    "note": {
        >>>        "identifier": "note-1",
        >>>        "type": "loinc:LP29684-5",
        >>>        "patient_id": "507f1f77bcf86cd799439011",
        >>>        "text": "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott. Her SSN is 123-45-6789."
        >>>    }
        >>> }
        >>> host = "0.0.0.0/api/v1"
        >>> configuration = utils.get_api_configuration(host=host)
        >>> with nlpsandbox.ApiClient(configuration) as api_client:
        >>>     annotations = _annotate_id(
        >>>         api_client=api_client,
        >>>         text_annotation_request=example_request
        >>>     )

    """
    api_instance = text_id_annotation_api.TextIdAnnotationApi(
        api_client
    )
    annotations = api_instance.create_text_id_annotations(
        text_id_annotation_request=text_annotation_request
    )
    return annotations


def _annotate_covid_symptom(api_client, text_annotation_request: dict) -> dict:
    """Annotate notes with covid symptom

    Args:
        host: Data node host IP
        text_annotation_request: Text id annotation request

    Yields:
        Annotated notes

    Examples:
        >>> example_request = {
        >>>    "note": {
        >>>        "identifier": "note-1",
        >>>        "type": "loinc:LP29684-5",
        >>>        "patient_id": "507f1f77bcf86cd799439011",
        >>>        "text": "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott. She's had a dry cough for almost a week now."
        >>>    }
        >>> }
        >>> host = "0.0.0.0/api/v1"
        >>> configuration = utils.get_api_configuration(host=host)
        >>> with nlpsandbox.ApiClient(configuration) as api_client:
        >>>     annotations = _annotate_covid_symptom(
        >>>         api_client=api_client,
        >>>         text_annotation_request=example_request
        >>>     )

    """  # noqa: E501
    api_instance = text_covid_symptom_annotation_api.TextCovidSymptomAnnotationApi(  # noqa: E501
        api_client
    )
    annotations = api_instance.create_text_covid_symptom_annotations(
        text_covid_symptom_annotation_request=text_annotation_request
    )
    return annotations


def annotate_note(host: str, note: Union[dict, Note],
                  tool_type: str) -> dict:
    """Annotate notes

    Args:
        host: Data node host IP
        note: Clinical note
        tool_type: Type of annotator

    Yields:
        Annotated notes

    Examples:
        >>> example_note = {
        >>>    "identifier": "note-1",
        >>>    "noteType": "loinc:LP29684-5",
        >>>    "patientId": "507f1f77bcf86cd799439011",
        >>>    "text": "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott."
        >>> }
        >>> annotations = annotate_note(host="0.0.0.0/api/v1",
        >>>                             note=example_note,
        >>>                             tool_type="date")

    """
    configuration = utils.get_api_configuration(host=host)
    # Change clinical note into text annotation request format
    if isinstance(note, Note):
        text_annotator_req = {"note": note.to_dict()}
    else:
        text_annotator_req = {
            "note": utils.change_keys(note, utils.camelcase_to_snakecase)
        }
    with nlpsandbox.ApiClient(configuration) as api_client:
        if tool_type == "nlpsandbox:date-annotator":
            annotations = _annotate_date(api_client, text_annotator_req)
        elif tool_type == "nlpsandbox:person-name-annotator":
            annotations = _annotate_person_name(api_client, text_annotator_req)
        elif tool_type == "nlpsandbox:location-annotator":
            annotations = _annotate_location(api_client, text_annotator_req)
        elif tool_type == "nlpsandbox:contact-annotator":
            annotations = _annotate_contact(api_client, text_annotator_req)
        elif tool_type == "nlpsandbox:id-annotator":
            annotations = _annotate_id(api_client, text_annotator_req)
        elif tool_type == "nlpsandbox:covid-symptom-annotator":
            annotations = _annotate_covid_symptom(api_client,
                                                  text_annotator_req)
        else:
            raise ValueError(f"Invalid annotator_type: {tool_type}")
        sanitized_annotations = api_client.sanitize_for_serialization(
            annotations
        )
    return sanitized_annotations


def get_tool(host: str) -> Tool:
    """Get annotater service

    Args:
        host: Annotation Service host IP

    Returns:
        Service object

    Raises:
        ValueError: If tool base URL isn't redirected to tool service endpoint

    Examples:
        >>> tool = get_tool(host="0.0.0.0/api/v1")

    """
    configuration = utils.get_api_configuration(host=host)
    with nlpsandbox.ApiClient(configuration) as api_client:
        tool_instance = tool_api.ToolApi(api_client)
        tool_info = tool_instance.get_tool()
    # check if tool / redirects to /tool path
    redirect_info = _get_tool_redirect(host)
    if tool_info.to_dict() != redirect_info:
        raise ValueError("Tool base URL must redirect to tool service")
    return tool_info


def list_datasets(host: str) -> List[dict]:
    """Get all datasets

    Args:
        host: Data node host IP

    Yields:
        list of datasets.

    Examples:
        >>> datasets = list_datasets(host="0.0.0.0/api/v1")
        >>> list(datasets)[0]
        >>> {
        >>>    "name": "datasets/testing"
        >>> }
    """
    configuration = utils.get_api_configuration(host=host)
    offset = 0
    limit = 10
    with nlpsandbox.ApiClient(configuration) as api_client:
        api_instance = dataset_api.DatasetApi(api_client)
        # Obtain all clinical notes
        next_page = True
        while next_page:
            datasets = api_instance.list_datasets(offset=offset, limit=limit)
            # change from snake case to camel case
            sanitized = api_client.sanitize_for_serialization(
                datasets.datasets
            )
            for dataset in sanitized:
                yield dataset
            next_page = datasets.links.next
            offset += limit


def _get_tool_redirect(host: str) -> Tool:
    """Make sure tool's base URL redirects to tool service

    Args:
        host: Annotation Service host IP

    Returns:
        Service object

    Examples:
        >>> tool = _get_tool_redirect(host="0.0.0.0/api/v1")

    """

    if not host.startswith("http"):
        host = f"http://{host}"
    # Remove /api/v1 string
    host = host.replace("/api/v1", '')
    response = requests.get(host)
    tool_response = utils.change_keys(response.json(),
                                      utils.camelcase_to_snakecase)
    return tool_response


def store_annotations(host: str, dataset_id: str, annotation_store_id: str,
                      annotations: List[dict],
                      delete_existing_annotations: bool = True):
    """Store submission annotated notes.  Delete an annotation store if
    the annotation store exists, then create a new annotation store, then
    store the annotation.

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        annotation_store_id: Annotation store Id
        annotations: List of data node Annotations
        delete_existing_annotations: To delete existing annotation store.
                                     Default is True.
    """
    configuration = utils.get_api_configuration(host=host)
    with nlpsandbox.ApiClient(configuration) as api_client:
        annot_store_instance = annotation_store_api.AnnotationStoreApi(
            api_client
        )
        try:
            # Always try to delete the annotation store prior to
            # storing predictions
            if delete_existing_annotations:
                annot_store_instance.delete_annotation_store(
                    dataset_id, annotation_store_id
                )
                print("Deleted existing Annotation Store")
        except nlpsandbox.rest.ApiException:
            pass
        try:
            annot_store_instance.create_annotation_store(
                dataset_id, annotation_store_id, body={}
            )
            print("Created Annotation Store")
        except nlpsandbox.rest.ApiException:
            print("Using existing Annotation Store")

    for annotation in annotations:
        annotation_id = annotation[
            'annotationSource'
        ]['resourceSource']['name'].split("/")[-1]
        _store_annotation(
            host=host,
            dataset_id=dataset_id,
            annotation_store_id=annotation_store_id,
            annotation_id=annotation_id,
            annotation=annotation
        )


def store_dataset(host: str, dataset_id: str) -> Dataset:
    """Creates a dataset"""
    configuration = utils.get_api_configuration(host=host)
    # Enter a context with an instance of the API client
    with nlpsandbox.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = dataset_api.DatasetApi(api_client)
        body = {}
        dataset = api_instance.create_dataset(dataset_id, body=body)
    return dataset


def delete_dataset(host: str, dataset_id: str):
    """Deletes a dataset"""
    configuration = utils.get_api_configuration(host=host)
    # Enter a context with an instance of the API client
    with nlpsandbox.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = dataset_api.DatasetApi(api_client)
        api_instance.delete_dataset(dataset_id)
