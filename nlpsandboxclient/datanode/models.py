"""Models for the data node"""
# Define models
class Model:
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
    pass


class AnnotationStore(Model):

    @property
    def datasetid(self):
        return self.kwargs.get("datasetid")


class Annotation(Model):

    @property
    def datasetid(self):
        return self.kwargs.get("datasetid")

    @property
    def annotation_store_id(self):
        return self.kwargs.get("annotation_storeid")

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
    @property
    def datasetid(self):
        return self.kwargs.get("datasetid")


class Note(Model):
    @property
    def datasetid(self):
        return self.kwargs.get("datasetid")

    @property
    def fhir_storeid(self):
        return self.kwargs.get("fhir_storeid")

    @property
    def note_type(self):
        return self.kwargs.get("noteType")

    @property
    def patientid(self):
        return self.kwargs.get("patientId")

    @property
    def text(self):
        return self.kwargs.get("text")


class Patient(Model):
    @property
    def datasetid(self):
        return self.kwargs.get("datasetid")

    @property
    def fhir_storeid(self):
        return self.kwargs.get("fhir_storeid")

    @property
    def gender(self):
        return self.kwargs.get("gender")

    @property
    def identifier(self):
        return self.kwargs.get("identifier")
