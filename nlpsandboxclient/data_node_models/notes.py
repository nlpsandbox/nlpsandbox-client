"""FHIR Clinical note"""


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
