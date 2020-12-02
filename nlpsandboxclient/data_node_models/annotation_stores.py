"""Annotation Store"""
from .base import Model


class AnnotationStore(Model):
    """AnnotationStore model"""
    @property
    def dataset_id(self):
        return self.kwargs.get("dataset_id")
