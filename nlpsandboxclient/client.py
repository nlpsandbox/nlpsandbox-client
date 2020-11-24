"""NLP client object"""
from .api_client import DataNodeApiClient


def get_clinical_notes(host, datasetid):
    """Get all clinical notes for a dataset"""
    nlp = DataNodeApiClient(host=host)
    fhir_stores = nlp.list_fhir_stores(datasetid=datasetid)
    fhir_store_ids = []
    for fhir_store_info in fhir_stores:
        for fhir_store in fhir_store_info['fhirStores']:
            fhir_store_ids.append(fhir_store['name'].split("/")[3])

    all_notes = []
    # Obtain all clinical notes for all fhir stores in a dataset
    for fhir_store_id in fhir_store_ids:
        clinical_notes = nlp.list_clinical_notes(datasetid=datasetid,
                                                 fhir_storeid=fhir_store_id)
        # Obtain all clinical notes
        for note in clinical_notes:
            all_notes.extend(note['notes'])

    return all_notes
