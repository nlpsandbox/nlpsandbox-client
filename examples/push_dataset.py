from __future__ import print_function

import time
import datanodeclient
from datanodeclient.rest import ApiException
from pprint import pprint
import json
import sys

# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanodeclient.Configuration(
    host="http://10.23.55.45:8080/api/v1"
    # host="http://localhost:8080/api/v1"
)


dataset_id = '2014-i2b2-20201203'
fhir_store_id = 'evaluation'
annotation_store_id = 'goldstandard'

json_filename = 'evaluation-patient-bundles.json'

with datanodeclient.ApiClient(configuration) as api_client:
    dataset_api = datanodeclient.DatasetApi(api_client)
    fhir_store_api = datanodeclient.FhirStoreApi(api_client)
    annotation_store_api = datanodeclient.AnnotationStoreApi(api_client)
    patient_api = datanodeclient.PatientApi(api_client)
    note_api = datanodeclient.NoteApi(api_client)
    annotation_api = datanodeclient.AnnotationApi(api_client)

    try:
        # get the dataset
        dataset = dataset_api.get_dataset(dataset_id)
    except ApiException as e:
        if e.status == 404:
            # create dataset if not found
            try:
                dataset = dataset_api.create_dataset(
                    dataset_id,
                    dataset=datanodeclient.Dataset()
                )
            except ApiException as e:
                print("Exception when calling DatasetApi->create_dataset: %s\n" % e)
                sys.exit(-1)
        else:
            print("Exception when calling DatasetApi->get_dataset: %s\n" % e)
            sys.exit(-1)

    try:
        # get the FHIR store
        fhir_store = fhir_store_api.get_fhir_store(dataset_id, fhir_store_id)
    except ApiException as e:
        if e.status == 404:
            # create fhir store if not found
            try:
                fhir_store = fhir_store_api.create_fhir_store(
                    dataset_id,
                    fhir_store_id,
                    fhir_store=datanodeclient.FhirStore()
                )
            except ApiException as e:
                print("Exception when calling FhirStoreApi->create_fhir_store: %s\n" % e)
                sys.exit(-1)
        else:
            print("Exception when calling FhirStoreApi->get_fhir_store: %s\n" % e)
            sys.exit(-1)

    try:
        # get the annotation store
        annotation_store = annotation_store_api.get_annotation_store(dataset_id, annotation_store_id)
    except ApiException as e:
        if e.status == 404:
            # create annotation store if not found
            try:
                annotation_store = annotation_store_api.create_annotation_store(
                    dataset_id,
                    annotation_store_id,
                    annotation_store=datanodeclient.AnnotationStore()
                )
            except ApiException as e:
                print("Exception when calling AnnotationStoreApi->create_annotation_store: %s\n" % e)
                sys.exit(-1)
        else:
            print("Exception when calling AnnotationStoreApi->get_annotation_store: %s\n" % e)
            sys.exit(-1)

    print(f"dataset: {dataset}")
    print(f"fhir_store: {fhir_store}")
    print(f"annotation_store: {annotation_store}")

    with open(json_filename) as f:
        data = json.load(f)
        patient_bundles = data['patient_bundles']
        # patient_bundles = patient_bundles[:1]

    for patient_bundle in patient_bundles:
        patient = patient_bundle['patient']

        try:
            # Create a FHIR Patient
            patient = patient_api.create_patient(
                dataset_id,
                fhir_store_id,
                patient=patient)
            print(f"patient: {patient}")

            # Create the Note and Annotation objects linked to the patient
            note_bundles = patient_bundle['note_bundles']
            # note_bundles = note_bundles[:1]

            for note_bundle in note_bundles:
                note = note_bundle['note']
                note['patientId'] = patient.id
                try:
                    note = note_api.create_note(
                        dataset_id,
                        fhir_store_id,
                        note=note
                    )
                    print(f"note: {note}")
                except ApiException as e:
                    print("Exception when calling NoteApi->create_note: %s\n" % e)

                annotation = note_bundle['annotation']
                annotation['annotationSource']['resourceSource']['name'] = \
                    "{fhir_store_name}/fhir/Note/{note_id}".format(
                        fhir_store_name=fhir_store.name,
                        note_id=note.id
                    )
                try:
                    annotation = annotation_api.create_annotation(
                        dataset_id,
                        annotation_store_id,
                        annotation=annotation
                    )
                    print(f"annotation: {annotation}")
                except ApiException as e:
                    print("Exception when calling AnnotationApi->create_annotation: %s\n" % e)

                # time.sleep(1)

        except ApiException as e:
            print("Exception when calling PatientApi->create_patient: %s\n" % e)

        # time.sleep(1)
