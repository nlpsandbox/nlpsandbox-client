# nlpsandboxsdk.TextContactAnnotationApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_text_contact_annotations**](TextContactAnnotationApi.md#create_text_contact_annotations) | **POST** /textContactAnnotations | Annotate contact information in a clinical note


# **create_text_contact_annotations**
> TextContactAnnotationResponse create_text_contact_annotations()

Annotate contact information in a clinical note

Return the contact annotations found in a clinical note

### Example

```python
import time
import nlpsandboxsdk
from nlpsandboxsdk.api import text_contact_annotation_api
from nlpsandboxsdk.model.text_contact_annotation_request import TextContactAnnotationRequest
from nlpsandboxsdk.model.text_contact_annotation_response import TextContactAnnotationResponse
from nlpsandboxsdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandboxsdk.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandboxsdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = text_contact_annotation_api.TextContactAnnotationApi(api_client)
    text_contact_annotation_request = TextContactAnnotationRequest(
        note=Note(
            identifier=NoteId("awesome-note"),
            text="text_example",
            type="type_example",
            patient_id=PatientId("awesome-patient"),
        ),
    ) # TextContactAnnotationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Annotate contact information in a clinical note
        api_response = api_instance.create_text_contact_annotations(text_contact_annotation_request=text_contact_annotation_request)
        pprint(api_response)
    except nlpsandboxsdk.ApiException as e:
        print("Exception when calling TextContactAnnotationApi->create_text_contact_annotations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_contact_annotation_request** | [**TextContactAnnotationRequest**](TextContactAnnotationRequest.md)|  | [optional]

### Return type

[**TextContactAnnotationResponse**](TextContactAnnotationResponse.md)

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

