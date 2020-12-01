"""Test client functions"""
from unittest.mock import Mock, patch

from nlpsandboxclient import api_client
from nlpsandboxclient.api_client import NlpApiClient, DataNodeApiClient


class TestApiClient:
    """Test base API client"""

    def setup_method(self):
        """Method called once per method"""
        self.host = api_client.DATA_NODE_HOST
        self.nlpclient = NlpApiClient(host=self.host)

    def test_get_service(self):
        """Test get service"""
        with patch.object(self.nlpclient, "rest_get") as rest_get:
            self.nlpclient.get_service()
            rest_get.assert_called_once_with("/service")

    def test_get_ui(self):
        """Test get ui"""
        with patch.object(self.nlpclient, "rest_get") as rest_get:
            self.nlpclient.get_ui()
            rest_get.assert_called_once_with("/ui", return_body=False)

    def test__build_uri_nonet(self):
        """Tests building of URI no net"""
        uri = self.nlpclient._build_uri("/foo")
        assert uri == f"{self.host}/foo"

    def test__build_uri_net(self):
        """Tests building of URI network in text"""
        text = "http://google.com/foo"
        uri = self.nlpclient._build_uri(text)
        assert uri == text

    def test__build_uri_endpoint(self):
        """Tests building of URI to specify endpoint"""
        uri = self.nlpclient._build_uri("/foo", endpoint="test")
        assert uri == "test/foo"

    def test__rest_call(self):
        """Test rest call"""
        response = Mock(status_code=200)
        with patch.object(self.nlpclient, "_build_uri",
                          return_value="/foo") as build_uri, \
             patch.object(self.nlpclient._requests_session,
                          "get", return_value=response) as request_get:
            self.nlpclient._rest_call("get", "/foo", None, "http://endpoint")
            build_uri.assert_called_once_with("/foo",
                                              endpoint="http://endpoint")
            request_get.assert_called_once_with("/foo", json=None,
                                                headers=None)

    def test_rest_get(self):
        """Test rest get"""
        with patch.object(self.nlpclient, "_rest_call",
                          return_value="/foo") as rest_call, \
             patch.object(api_client, "_return_rest_body",
                          return_value='temp') as return_body:
            returned = self.nlpclient.rest_get("/foo",
                                               endpoint="http://endpoint")
            rest_call.assert_called_once_with("get", "/foo", None,
                                              "http://endpoint")
            return_body.assert_called_once_with("/foo")
            assert returned == "temp"

    def test_rest_get_paginated(self):
        """Test rest get"""
        returned = {"links": {"next": ""}, "limit": 0, "offset": 0,
                    "testing": ["list", "of", "items"]}
        with patch.object(self.nlpclient, "rest_get",
                          return_value=returned) as rest_call:
            results = list(self.nlpclient.rest_get_paginated("/foo/bar",
                                                             limit=4,
                                                             offset=4))
            rest_call.assert_called_once_with("/foo/bar?limit=4&offset=4")
            assert ["list", "of", "items"] == results

    def test_rest_post(self):
        """Test rest get"""
        with patch.object(self.nlpclient, "_rest_call",
                          return_value="/foo") as rest_call, \
             patch.object(api_client, "_return_rest_body",
                          return_value='temp') as return_body:
            returned = self.nlpclient.rest_post("/foo", {"test": "me"},
                                                endpoint="http://endpoint")
            rest_call.assert_called_once_with(
                "post", "/foo", {"test": "me"}, "http://endpoint"
            )
            return_body.assert_called_once_with("/foo")
            assert returned == "temp"


class TestDataNodeApiClient:
    """Test client class"""
    def setup_method(self):
        """Method called once per method"""
        self.host = api_client.DATA_NODE_HOST
        self.nlp = DataNodeApiClient(host=self.host)

    def test_list_datasets(self):
        """Test get datasets"""
        with patch.object(self.nlp, "rest_get_paginated") as rest_get:
            list(self.nlp.list_datasets())
            rest_get.assert_called_once_with("/datasets")

    def test_get_dataset(self):
        """Test get dataset"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_dataset(dataset_id="foo")
            rest_get.assert_called_once_with("/datasets/foo")

    def test_create_dataset(self):
        """Test get dataset"""
        with patch.object(self.nlp, "rest_post") as rest_post:
            self.nlp.create_dataset(dataset_id="foo")
            rest_post.assert_called_once_with("/datasets?datasetId=foo",
                                              body={})

    def test_list_annotation_stores(self):
        """Test get annotation stores"""
        with patch.object(self.nlp, "rest_get_paginated") as rest_get:
            list(self.nlp.list_annotation_stores(dataset_id="foo"))
            rest_get.assert_called_once_with("/datasets/foo/annotationStores")

    def test_get_annotation_store(self):
        """Test get annotation store"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_annotation_store(dataset_id="foo",
                                          annotation_store_id="doo")
            rest_get.assert_called_once_with(
                "/datasets/foo/annotationStores/doo"
            )

    def test_list_fhir_stores(self):
        """Test get fhir stores"""
        with patch.object(self.nlp, "rest_get_paginated") as rest_get:
            list(self.nlp.list_fhir_stores(dataset_id="foo"))
            rest_get.assert_called_once_with("/datasets/foo/fhirStores")

    def test_get_fhir_store(self):
        """Test get fhir store"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_fhir_store(dataset_id="foo", fhir_store_id="doo")
            rest_get.assert_called_once_with(
                "/datasets/foo/fhirStores/doo"
            )

    def test_list_notes(self):
        """Test getting clinical notes"""
        with patch.object(self.nlp, "rest_get_paginated") as rest_get:
            list(self.nlp.list_notes(dataset_id="foo",
                                     fhir_store_id="doo"))
            rest_get.assert_called_once_with(
                "/datasets/foo/fhirStores/doo/fhir/Note"
            )

    def test_get_note(self):
        """Test getting clinical note"""
        with patch.object(self.nlp, "rest_get") as rest_get:
            self.nlp.get_note(dataset_id="foo", fhir_store_id="doo",
                              note_id="boo")
            rest_get.assert_called_once_with(
                "/datasets/foo/fhirStores/doo/fhir/Note/boo"
            )


def test__return_rest_body_text():
    """Test return of text"""
    response = Mock()
    response.headers = {"content-type": None}
    text = "testing text me"
    response.text = text
    returned = api_client._return_rest_body(response)
    assert returned == text


def test__return_rest_body_json():
    """Test return of text"""
    response = Mock()
    response.headers = {"content-type": "Application/json "}
    expected = {"bar": "foo"}
    with patch.object(response, "json",
                      return_value=expected) as response_json:
        returned = api_client._return_rest_body(response)
        response_json.assert_called_once()
        assert returned == expected
