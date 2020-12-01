"""
NLP data node client - This module has convenience functions to interact
with the DataNodeApiClient.
"""
from typing import List

from .api_client import DataNodeApiClient


def get_clinical_notes(host: str, datasetid: str) -> List[dict]:
    """Get all clinical notes for a dataset

    Args:
        host: Data node host IP.
        dataset: Dataset id

    Returns:
        list of clinical notes.

    Examples:
        >>> notes = get_clinical_notes(host="0.0.0.0/api/v1",
                                       datasetid="awesome-dataset")
    """
    nlp = DataNodeApiClient(host=host)
    fhir_stores = nlp.list_fhir_stores(datasetid=datasetid)

    all_notes = []
    # Obtain all clinical notes for all fhir stores in a dataset
    for fhir_store in fhir_stores:
        clinical_notes = nlp.list_notes(datasetid=datasetid,
                                        fhir_storeid=fhir_store.id)
        # Obtain all clinical notes
        for note in clinical_notes:
            all_notes.append({
                "id": note.id,
                "noteType": note.note_type,
                "patientId": note.patientid,
                "text": note.text,
                "note_name": f"dataset/{datasetid}/fhirStores/{fhir_store.id}/fhir/Note/{note.id}"
            })
    return all_notes
