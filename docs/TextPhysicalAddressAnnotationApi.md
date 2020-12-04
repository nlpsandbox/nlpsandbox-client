# addressannotator.TextPhysicalAddressAnnotationApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_text_physical_address_annotations**](TextPhysicalAddressAnnotationApi.md#create_text_physical_address_annotations) | **POST** /textPhysicalAddressAnnotations | Annotate physical addresses in a clinical note


# **create_text_physical_address_annotations**
> TextPhysicalAddressAnnotations create_text_physical_address_annotations(text_physical_address_annotation_request=text_physical_address_annotation_request)

Annotate physical addresses in a clinical note

Return the physical addresse annotations found in a clinical note

### Example

```python
from __future__ import print_function
import time
import addressannotator
from addressannotator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = addressannotator.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with addressannotator.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addressannotator.TextPhysicalAddressAnnotationApi(api_client)
    text_physical_address_annotation_request = addressannotator.TextPhysicalAddressAnnotationRequest() # TextPhysicalAddressAnnotationRequest |  (optional)

    try:
        # Annotate physical addresses in a clinical note
        api_response = api_instance.create_text_physical_address_annotations(text_physical_address_annotation_request=text_physical_address_annotation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TextPhysicalAddressAnnotationApi->create_text_physical_address_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_physical_address_annotation_request** | [**TextPhysicalAddressAnnotationRequest**](TextPhysicalAddressAnnotationRequest.md)|  | [optional] 

### Return type

[**TextPhysicalAddressAnnotations**](TextPhysicalAddressAnnotations.md)

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

