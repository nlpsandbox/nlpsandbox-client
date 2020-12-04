# dateannotator.TextDateAnnotationApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_text_date_annotations**](TextDateAnnotationApi.md#create_text_date_annotations) | **POST** /textDateAnnotations | Annotate dates in a clinical note


# **create_text_date_annotations**
> TextDateAnnotations create_text_date_annotations(text_date_annotation_request=text_date_annotation_request)

Annotate dates in a clinical note

Return the date annotations found in a clinical note

### Example

```python
from __future__ import print_function
import time
import dateannotator
from dateannotator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dateannotator.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with dateannotator.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dateannotator.TextDateAnnotationApi(api_client)
    text_date_annotation_request = dateannotator.TextDateAnnotationRequest() # TextDateAnnotationRequest |  (optional)

    try:
        # Annotate dates in a clinical note
        api_response = api_instance.create_text_date_annotations(text_date_annotation_request=text_date_annotation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TextDateAnnotationApi->create_text_date_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_date_annotation_request** | [**TextDateAnnotationRequest**](TextDateAnnotationRequest.md)|  | [optional] 

### Return type

[**TextDateAnnotations**](TextDateAnnotations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

