"""NLP client object"""
from .api_client import DataNodeClient


def get_clinical_notes(host, datasetid):
    """Get all clinical notes for a dataset"""
    # host = "http://10.23.55.45:8080/api/v1"
    nlp = DataNodeClient(host=host)
    fhir_stores = nlp.get_fhir_stores(datasetid=datasetid)
    # Obtain fhir store ids
    fhir_store_ids = [fhir_store['name'].split("/")[3]
                      for fhir_store in fhir_stores['fhirStores']]
    all_notes = []
    # Obtain all clinical notes for all fhir stores in a dataset
    for fhir_store_id in fhir_store_ids:
        clinical_notes = nlp.get_clinical_notes(datasetid=datasetid,
                                                storeid=fhir_store_id)
        # Obtain all clinical notes
        for note in clinical_notes:
            all_notes.extend(note['notes'])

    return all_notes
