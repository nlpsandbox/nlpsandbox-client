"""Annotation"""
from .base import Model


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


