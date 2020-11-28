"""NLP client object"""
from typing import List

from .api_client import DataNodeApiClient


def get_clinical_notes(host: str, dataset_id: str) -> List[dict]:
    """Get all clinical notes for a dataset"""
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
                "patientId": note.patientid,
                "text": note.text,
                "note_name": f"dataset/{dataset_id}/fhirStores/{fhir_store.id}/fhir/Note/{note.id}"
            })
    return all_notes
