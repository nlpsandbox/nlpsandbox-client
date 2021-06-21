# nlpsandbox.TextLocationAnnotationApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_text_location_annotations**](TextLocationAnnotationApi.md#create_text_location_annotations) | **POST** /textLocationAnnotations | Annotate locations in a clinical note


# **create_text_location_annotations**
> TextLocationAnnotationResponse create_text_location_annotations()

Annotate locations in a clinical note

Return the location annotations found in a clinical note

### Example

```python
import time
import nlpsandbox
from nlpsandbox.api import text_location_annotation_api
from nlpsandbox.model.text_location_annotation_response import TextLocationAnnotationResponse
from nlpsandbox.model.error import Error
from nlpsandbox.model.text_location_annotation_request import TextLocationAnnotationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = text_location_annotation_api.TextLocationAnnotationApi(api_client)
    text_location_annotation_request = TextLocationAnnotationRequest(
        note=Note(
            identifier=NoteId("awesome-note"),
            text="text_example",
            type="type_example",
            patient_id=PatientId("awesome-patient"),
        ),
    ) # TextLocationAnnotationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Annotate locations in a clinical note
        api_response = api_instance.create_text_location_annotations(text_location_annotation_request=text_location_annotation_request)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling TextLocationAnnotationApi->create_text_location_annotations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_location_annotation_request** | [**TextLocationAnnotationRequest**](TextLocationAnnotationRequest.md)|  | [optional]

### Return type

[**TextLocationAnnotationResponse**](TextLocationAnnotationResponse.md)

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

