"""Validation of data and platform components like NLP Tools"""

from jsonschema import validate

from .client import NlpClient


class NlpToolClient(NlpClient):
    """Client for developed Nlp Tools"""
    def __init__(self, tool_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tool_type = tool_type

    def get_tool(self):
        """Get tool schema"""
        return self.rest_get("/tool")

    def validate(self):
        """Validate schema"""
        # Check schema is correct first
        if self.get_ui().status_code != 200:
            raise ValueError("/ui endpoint not configured")
        if self.get_health().get('status') != 'pass':
            raise ValueError("/health endpoint not configured")
        # Fake schema
        schema = {
            "type": "object",
            "properties": {
                "price": {"type": "number"},
                "name": {"type": "string"},
            },
        }
        data = self.get_tool()
        # If no exception is raised by validate(), the instance is valid.
        validate(instance=data, schema=schema)
