"""NLP client object"""
import os

from .api_client import DataNodeApiClient


def extract_name(responses, key):
    """Extract the name annotations from rest call responses

    Args:
        key: Key that stores the returned names
    """
    for response_info in responses:
        for response in response_info[key]:
            yield os.path.basename(response['name'])


class DataNodeClient:
    """Data node client"""
    def __init__(self, host=None):
        self.client = DataNodeApiClient(host=host)

    def list_datasets(self):
        """Lists dataset ids"""
        datasets = self.client.list_datasets()
        return extract_name(datasets, "datasets")
        # for dataset_info in datasets:
        #     for dataset in dataset_info['datasets']:
        #         yield dataset['name'].replace("datasets/", "")

    def create_dataset(self, datasetid=None):
        """Create a dataset"""
        return self.client.create_dataset(datasetid=datasetid)

    def list_annotation_stores(self, datasetid=None):
        """List the annotation stores for a dataset"""
        annotation_stores = self.client.list_annotation_stores(
            datasetid=datasetid
        )
        return extract_name(annotation_stores, "annotationStores")

#     def create_annotation_store(self, datasetid=None, storeid=None):
#         """Create an annotation store"""
#         return self.rest_post(
#             f"/datasets/{datasetid}/annotationStore?"
#             f"annotationStoreId={storeid}",
#             body=json.dumps({})
#         )

#     def list_annotations(self, datasetid=None, storeid=None):
#         """List the annotations for an annotation store"""
#         return self.rest_get_paginated(
#             f"/datasets/{datasetid}/annotationStore/{storeid}/annotations"
#         )

#     def get_annotation(self, datasetid=None, storeid=None, annotationid=None):
#         """Get an annotation"""
#         return self.rest_get(
#             f"/datasets/{datasetid}/annotationStore/{storeid}/"
#             f"annotations/{annotationid}"
#         )

#     def create_annotation(self, datasetid, storeid, annotation):
#         """Create an annotation"""
#         return self.rest_post(
#             f"/datasets/{datasetid}/annotationStore/{storeid}/annotations",
#             body=json.dumps(annotation)
#         )

#     def list_fhir_stores(self, datasetid):
#         """List the FHIR stores in a dataset"""
#         return self.rest_get(f"/datasets/{datasetid}/fhirStores")

#     def get_fhir_store(self, datasetid, storeid):
#         """Get a FHIR store"""
#         return self.rest_get(f"/datasets/{datasetid}/fhirStores/{storeid}")

#     def create_fhir_store(self, datasetid, storeid):
#         """Create a FHIR store"""
#         return self.rest_post(
#             f"/datasets/{datasetid}/fhirStores?fhirStoreId={storeid}",
#             body=json.dumps({})
#         )

#     def list_clinical_notes(self, datasetid, storeid):
#         """List clinical notes in a FHIR store"""
#         return self.rest_get_paginated(
#             f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note"
#         )

#     def get_clinical_note(self, datasetid, storeid, noteid):
#         """Get a clinical note"""
#         return self.rest_get(
#             f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note/{noteid}"
#         )

#     def create_clinical_note(self, datasetid, storeid, note):
#         """Create a clinical note"""
#         return self.rest_post(
#             f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Note",
#             body=json.dumps(note)
#         )

#     def list_patients(self, datasetid, storeid):
#         """Lists the patients in a FHIR store"""
#         return self.rest_get_paginated(
#             f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Patient"
#         )

#     def get_patient(self, datasetid, storeid, patientid):
#         """Get a FHIR patient"""
#         return self.rest_get(
#             f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/"
#             f"Patient/{patientid}"
#         )

#     def create_patient(self, datasetid, storeid, patient):
#         """Create a FHIR patient"""
#         return self.rest_post(
#             f"/datasets/{datasetid}/fhirStores/{storeid}/fhir/Patient",
#             body=json.dumps(patient)
#         )

def get_dataset_clinical_notes(host, datasetid):
    """Get all clinical notes for a dataset"""
    # host = "http://10.23.55.45:8080/api/v1"
    nlp = DataNodeClient(host=host)
    fhir_stores = nlp.list_fhir_stores(datasetid=datasetid)
    # Obtain fhir store ids
    fhir_store_ids = [fhir_store['name'].split("/")[3]
                      for fhir_store in fhir_stores['fhirStores']]
    all_notes = []
    # Obtain all clinical notes for all fhir stores in a dataset
    for fhir_store_id in fhir_store_ids:
        clinical_notes = nlp.list_clinical_notes(datasetid=datasetid,
                                                 storeid=fhir_store_id)
        # Obtain all clinical notes
        for note in clinical_notes:
            all_notes.extend(note['notes'])

    return all_notes
