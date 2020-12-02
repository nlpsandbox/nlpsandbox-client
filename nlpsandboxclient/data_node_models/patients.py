"""FHIR Patient"""
from .base import Model


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
