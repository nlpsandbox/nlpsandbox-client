"""NLP client object"""
import os
import re

from .api_client import DataNodeApiClient


def extract_name(responses: list, key: str):
    """Extract the name annotations from rest call responses

    Args:
        responses: list of response bodies
        key: Key that stores the returned names
    """
    for response_info in responses:
        for response in response_info[key]:
            yield response['name']


def get_inputs_from_name(name: str, regex: str):
    """Get API input parameters from API output

    Args:
        name: Name of resource
        regex: String matching rule

    Returns:
        matched groups
    """
    match = re.match(regex, name)
    if not match:
        raise ValueError("Invalid name")
    return match


class DataNodeClient:
    """Data node client"""
    def __init__(self, host: str = None):
        self.client = DataNodeApiClient(host=host)

    def list_datasets(self):
        """Lists dataset ids"""
        datasets = self.client.list_datasets()
        return extract_name(datasets, "datasets")

    def create_dataset(self, datasetname: str):
        """Create a dataset"""
        match = get_inputs_from_name(datasetname, "datasets/(.*)")
        return self.client.create_dataset(datasetid=match.group(1))

    def list_annotation_stores(self, datasetname):
        """List the annotation stores for a dataset"""
        match = get_inputs_from_name(datasetname, "datasets/(.*)")
        annotation_stores = self.client.list_annotation_stores(
            datasetid=match.group(1)
        )
        return extract_name(annotation_stores, "annotationStores")

    def create_annotation_store(self, datasetname=None,
                                annotation_storeid=None):
        """Create an annotation store"""
        match = get_inputs_from_name(datasetname, "datasets/(.*)")
        return self.client.create_annotation_store(datasetid=match.group(1),
                                                   storeid=annotation_storeid)

    def list_annotations(self, annotation_store_name=None):
        """List the annotations for an annotation store"""
        match = get_inputs_from_name(
            annotation_store_name,
            "datasets/(.*)/annotationStore/(.*)$"
        )
        annotations = self.client.list_annotations(
            datasetid=match.group(1), storeid=match.group(2)
        )
        for annotation in annotations:
            for annot in annotation['annotations']:
                yield annot

    def get_annotation(self, annotation_name):
        """Get an annotation"""
        match = get_inputs_from_name(
            annotation_name,
            "datasets/(.*)/annotationStore/(.*)/annotations/(.*)$"
        )
        return self.client.get_annotation(
            datasetid=match.group(1), storeid=match.group(2),
            annotationid=match.group(3)
        )

    def create_annotation(self, annotation_store_name, annotationid):
        """Create an annotation"""
        match = get_inputs_from_name(
            annotation_store_name,
            "datasets/(.*)/annotationStore/(.*)$"
        )
        return self.client.create_annotation(
            datasetid=match.group(1),
            storeid=match.group(2),
            annotation=annotationid
        )

    def list_fhir_stores(self, datasetname):
        """List the FHIR stores in a dataset"""
        match = get_inputs_from_name(datasetname, "datasets/(.*)")
        fhir_stores=  self.client.list_fhir_stores(datasetid=match.group(1))
        return extract_name(fhir_stores, "fhirStores")

    def create_fhir_store(self, datasetname, fhirstoreid):
        """Create a FHIR store"""
        match = get_inputs_from_name(datasetname, "datasets/(.*)")
        return self.client.create_fhir_store(datasetid=match.group(1),
                                             storeid=fhirstoreid)

    def list_clinical_notes(self, fhirstore_name):
        """List clinical notes in a FHIR store"""
        match = get_inputs_from_name(fhirstore_name,
                                     "datasets/(.*)/fhirStores/(.*)$")
        notes = self.client.list_clinical_notes(datasetid=match.group(1),
                                                storeid=match.group(2))
        for note in notes:
            yield note['notes']

    def get_clinical_note(self, fhirstore_name, noteid):
        """Get a clinical note"""
        match = get_inputs_from_name(fhirstore_name,
                                     "datasets/(.*)/fhirStores/(.*)$")
        return self.client.get_clinical_note(datasetid=match.group(1),
                                             storeid=match.group(2),
                                             noteid=noteid)

    def create_clinical_note(self, fhirstore_name, noteid):
        """Create a clinical note"""
        match = get_inputs_from_name(fhirstore_name,
                                     "datasets/(.*)/fhirStores/(.*)$")
        return self.client.create_clinical_note(datasetid=match.group(1),
                                                storeid=match.group(2),
                                                note=noteid)

    def list_patients(self, fhirstore_name):
        """Lists the patients in a FHIR store"""
        match = get_inputs_from_name(fhirstore_name,
                                     "datasets/(.*)/fhirStores/(.*)$")
        patients =  self.client.list_patients(datasetid=match.group(1),
                                              storeid=match.group(2))
        for patient in patients:
            yield patient['patients']

    def get_patient(self, fhirstore_name, patientid):
        """Get a FHIR patient"""
        match = get_inputs_from_name(fhirstore_name,
                                     "datasets/(.*)/fhirStores/(.*)$")
        return self.client.get_patient(datasetid=match.group(1),
                                       storeid=match.group(2),
                                       patientid=patientid)

    def create_patient(self, fhirstore_name, patientid):
        """Create a FHIR patient"""
        match = get_inputs_from_name(fhirstore_name,
                                     "datasets/(.*)/fhirStores/(.*)$")
        return self.client.create_patient(datasetid=match.group(1),
                                          storeid=match.group(2),
                                          patient=patientid)


def get_dataset_clinical_notes(host, datasetid):
    """Get all clinical notes for a dataset"""
    # host = "http://10.23.55.45:8080/api/v1"
    nlp = DataNodeApiClient(host=host)
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
