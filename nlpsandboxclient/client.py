"""NLP client object"""
from . import api_client
from .api_client import DataNodeApiClient
from . import utils


class DataNodeClient:
    """Data node client that utilizes the API client"""
    def __init__(self, host: str = None):
        self.client = DataNodeApiClient(host=host)

    def list_datasets(self):
        """Lists dataset ids"""
        datasets = self.client.list_datasets()
        return utils.extract_name(datasets, "datasets")

    def create_dataset(self, datasetname: str):
        """Create a dataset"""
        match = utils.get_inputs_from_name(datasetname, "datasets/(.*)")
        return self.client.create_dataset(datasetid=match.group(1))

    def list_annotation_stores(self, datasetname: str):
        """List the annotation stores for a dataset"""
        match = utils.get_inputs_from_name(datasetname, "datasets/(.*)")
        annotation_stores = self.client.list_annotation_stores(
            datasetid=match.group(1)
        )
        return utils.extract_name(annotation_stores, "annotationStores")

    def create_annotation_store(self, datasetname: str, annotation_storeid: str):
        """Create an annotation store"""
        match = utils.get_inputs_from_name(datasetname, "datasets/(.*)")
        return self.client.create_annotation_store(
            datasetid=match.group(1), annotation_storeid=annotation_storeid
        )

    def list_annotations(self, annotation_store_name: str):
        """List the annotations for an annotation store"""
        match = utils.get_inputs_from_name(
            annotation_store_name,
            "datasets/(.*)/annotationStore/(.*)$"
        )
        annotations = self.client.list_annotations(
            datasetid=match.group(1), annotation_storeid=match.group(2)
        )
        for annotation in annotations:
            for annot in annotation['annotations']:
                yield annot

    def get_annotation(self, annotation_name: str):
        """Get an annotation"""
        match = utils.get_inputs_from_name(
            annotation_name,
            "datasets/(.*)/annotationStore/(.*)/annotations/(.*)$"
        )
        return self.client.get_annotation(
            datasetid=match.group(1), annotation_storeid=match.group(2),
            annotationid=match.group(3)
        )

    def create_annotation(self, annotation_store_name: str, annotation: str):
        """Create an annotation"""
        match = utils.get_inputs_from_name(
            annotation_store_name,
            "datasets/(.*)/annotationStore/(.*)$"
        )
        return self.client.create_annotation(
            datasetid=match.group(1),
            annotation_storeid=match.group(2),
            annotation=annotation
        )

    def list_fhir_stores(self, datasetname: str):
        """List the FHIR stores in a dataset"""
        match = utils.get_inputs_from_name(datasetname, "datasets/(.*)")
        fhir_stores = self.client.list_fhir_stores(datasetid=match.group(1))
        return utils.extract_name(fhir_stores, "fhirStores")

    def create_fhir_store(self, datasetname: str, fhirstoreid: str):
        """Create a FHIR store"""
        match = utils.get_inputs_from_name(datasetname, "datasets/(.*)")
        return self.client.create_fhir_store(datasetid=match.group(1),
                                             fhir_storeid=fhirstoreid)

    def list_clinical_notes(self, fhirstore_name: str):
        """List clinical notes in a FHIR store"""
        match = utils.get_inputs_from_name(fhirstore_name,
                                           "datasets/(.*)/fhirStores/(.*)$")
        notes = self.client.list_clinical_notes(datasetid=match.group(1),
                                                fhir_storeid=match.group(2))
        for note in notes:
            yield note['notes']

    def get_clinical_note(self, fhirstore_name: str, noteid: str):
        """Get a clinical note"""
        match = utils.get_inputs_from_name(fhirstore_name,
                                           "datasets/(.*)/fhirStores/(.*)$")
        return self.client.get_clinical_note(datasetid=match.group(1),
                                             fhir_storeid=match.group(2),
                                             noteid=noteid)

    def create_clinical_note(self, fhirstore_name: str, noteid: str):
        """Create a clinical note"""
        match = utils.get_inputs_from_name(fhirstore_name,
                                           "datasets/(.*)/fhirStores/(.*)$")
        return self.client.create_clinical_note(datasetid=match.group(1),
                                                fhir_storeid=match.group(2),
                                                note=noteid)

    def list_patients(self, fhirstore_name: str):
        """Lists the patients in a FHIR store"""
        match = utils.get_inputs_from_name(fhirstore_name,
                                           "datasets/(.*)/fhirStores/(.*)$")
        patients = self.client.list_patients(datasetid=match.group(1),
                                             fhir_storeid=match.group(2))
        for patient in patients:
            yield patient['patients']

    def get_patient(self, fhirstore_name: str, patientid: str):
        """Get a FHIR patient"""
        match = utils.get_inputs_from_name(fhirstore_name,
                                           "datasets/(.*)/fhirStores/(.*)$")
        return self.client.get_patient(datasetid=match.group(1),
                                       fhir_storeid=match.group(2),
                                       patientid=patientid)

    def create_patient(self, fhirstore_name: str, patientid: str):
        """Create a FHIR patient"""
        match = utils.get_inputs_from_name(fhirstore_name,
                                           "datasets/(.*)/fhirStores/(.*)$")
        return self.client.create_patient(datasetid=match.group(1),
                                          fhir_storeid=match.group(2),
                                          patient=patientid)


def get_clinical_notes(dataset_name, host=api_client.DATA_NODE_HOST):
    """Get all clinical notes for a dataset"""
    nlp = DataNodeClient(host=host)
    fhirstores = nlp.list_fhir_stores(datasetname=dataset_name)
    all_notes = []
    # Obtain all clinical notes for all fhir stores in a dataset
    for fhirstore_name in fhirstores:
        clinical_notes = nlp.list_clinical_notes(fhirstore_name)
        # Obtain all clinical notes
        for note in clinical_notes:
            all_notes.extend(note)
    return all_notes
