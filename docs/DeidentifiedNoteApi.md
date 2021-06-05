# nlpsandbox.DeidentifiedNoteApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deidentified_notes**](DeidentifiedNoteApi.md#create_deidentified_notes) | **POST** /deidentifiedNotes | Deidentify a clinical note


# **create_deidentified_notes**
> DeidentifyResponse create_deidentified_notes()

Deidentify a clinical note

Returns the deidentified note

### Example

```python
import time
import nlpsandbox
from nlpsandbox.apis import deidentified_note_api
from nlpsandbox.models.error import Error
from nlpsandbox.models.deidentify_response import DeidentifyResponse
from nlpsandbox.models.deidentify_request import DeidentifyRequest
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deidentified_note_api.DeidentifiedNoteApi(api_client)
    deidentify_request = DeidentifyRequest(
        note=Note(
            identifier=NoteId("awesome-note"),
            text="text_example",
            type="type_example",
            patient_id=PatientId("awesome-patient"),
        ),
        deidentification_steps=[
            DeidentificationStep(
                confidence_threshold=95.5,
                masking_char_config=MaskingCharConfig(
                    masking_char="*",
                ),
                annotation_type_mask_config={},
                redact_config={},
                date_offset_config=DateOffsetConfig(
                    offset_days=1,
                ),
                annotation_types=[
                    "text_date",
                ],
            ),
        ],
    ) # DeidentifyRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deidentify a clinical note
        api_response = api_instance.create_deidentified_notes(deidentify_request=deidentify_request)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling DeidentifiedNoteApi->create_deidentified_notes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deidentify_request** | [**DeidentifyRequest**](DeidentifyRequest.md)|  | [optional]

### Return type

[**DeidentifyResponse**](DeidentifyResponse.md)

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

