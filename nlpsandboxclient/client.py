"""NLP client object"""
from .api_client import DataNodeApiClient


def get_clinical_notes(host, datasetid):
    """Get all clinical notes for a dataset"""
    nlp = DataNodeApiClient(host=host)
    fhir_stores = nlp.list_fhir_stores(datasetid=datasetid)

    all_notes = []
    # Obtain all clinical notes for all fhir stores in a dataset
    for fhir_store in fhir_stores:
        clinical_notes = nlp.list_clinical_notes(
            datasetid=fhir_store.datasetid, fhir_storeid=fhir_store.id
        )
        # Obtain all clinical notes
        for note in clinical_notes:
            all_notes.append({
                "id": note.id,
                "noteType": note.note_type,
                "patientId": note.patientid,
                "text": note.text
            })

    return all_notes
