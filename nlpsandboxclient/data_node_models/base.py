"""Base model for data node models"""


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
