"""Models for the data node"""


# Define models
class Model:
    """Base model class"""
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @property
    def id(self):
        # If id isn't specified, but name is,
        # The id can be inferred
        # if self.kwargs.get("id") is None and self.kwargs.get("name") is not None:
        #     return os.path.basename(self.kwargs.get("name"))
        return self.kwargs.get("id")

    @property
    def name(self):
        return self.kwargs.get("name")


class Dataset(Model):
    """Dataset model"""
    pass


class AnnotationStore(Model):
    """AnnotationStore model"""
    @property
    def dataset_id(self):
        return self.kwargs.get("dataset_id")


class Annotation(Model):
    """Annotation model"""
    @property
    def dataset_id(self):
        return self.kwargs.get("dataset_id")

    @property
    def annotation_store_id(self):
        return self.kwargs.get("annotation_store_id")

    @property
    def annotation_source(self):
        return self.kwargs.get("annotationSource")

    @property
    def text_date_annotations(self):
        return self.kwargs.get("textDateAnnotations")

    @property
    def text_person_name_annotations(self):
        return self.kwargs.get("textPersonNameAnnotations")

    @property
    def text_physical_address_annotations(self):
        return self.kwargs.get("textPhysicalAddressAnnotations")


class FhirStore(Model):
    """FhirStore model"""

    @property
    def dataset_id(self):
        return self.kwargs.get("dataset_id")


class Note(Model):
    """Clinical note model"""
    @property
    def dataset_id(self):
        return self.kwargs.get("dataset_id")

    @property
    def fhir_store_id(self):
        return self.kwargs.get("fhir_store_id")

    @property
    def note_type(self):
        return self.kwargs.get("noteType")

    @property
    def patient_id(self):
        return self.kwargs.get("patientId")

    @property
    def text(self):
        return self.kwargs.get("text")


class Patient(Model):
    """Patient model"""
    @property
    def dataset_id(self):
        return self.kwargs.get("dataset_id")

    @property
    def fhir_store_id(self):
        return self.kwargs.get("fhir_store_id")

    @property
    def gender(self):
        return self.kwargs.get("gender")

    @property
    def identifier(self):
        return self.kwargs.get("identifier")
