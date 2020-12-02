"""FHIR store"""


class FhirStore(Model):
    """FhirStore model"""

    @property
    def dataset_id(self):
        return self.kwargs.get("dataset_id")
