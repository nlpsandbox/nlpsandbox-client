# nlpsandbox.TextIdAnnotationApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_text_id_annotations**](TextIdAnnotationApi.md#create_text_id_annotations) | **POST** /textIdAnnotations | Annotate IDs in a clinical note


# **create_text_id_annotations**
> TextIdAnnotationResponse create_text_id_annotations()

Annotate IDs in a clinical note

Return the ID annotations found in a clinical note

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import text_id_annotation_api
from nlpsandbox.model.text_id_annotation_request import TextIdAnnotationRequest
from nlpsandbox.model.error import Error
from nlpsandbox.model.text_id_annotation_response import TextIdAnnotationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = text_id_annotation_api.TextIdAnnotationApi(api_client)
    text_id_annotation_request = TextIdAnnotationRequest(
        note=Note(
            identifier=NoteId("awesome-note"),
            text="text_example",
            type="type_example",
            patient_id=PatientId("awesome-patient"),
        ),
    ) # TextIdAnnotationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Annotate IDs in a clinical note
        api_response = api_instance.create_text_id_annotations(text_id_annotation_request=text_id_annotation_request)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling TextIdAnnotationApi->create_text_id_annotations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_id_annotation_request** | [**TextIdAnnotationRequest**](TextIdAnnotationRequest.md)|  | [optional]

### Return type

[**TextIdAnnotationResponse**](TextIdAnnotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

