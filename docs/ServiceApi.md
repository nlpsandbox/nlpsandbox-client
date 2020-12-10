# annotator.ServiceApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service**](ServiceApi.md#service) | **GET** /service | Get service information


# **service**
> Service service()

Get service information

Get information about the service

### Example

```python
from __future__ import print_function
import time
import annotator
from annotator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = annotator.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with annotator.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotator.ServiceApi(api_client)
    
    try:
        # Get service information
        api_response = api_instance.service()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceApi->service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

