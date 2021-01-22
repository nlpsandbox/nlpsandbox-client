# data-node.ServiceApi

All URIs are relative to *https://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service**](ServiceApi.md#get_service) | **GET** /service | Get service information


# **get_service**
> Service get_service()

Get service information

Get information about the service

### Example

```python
from __future__ import print_function
import time
import data-node
from data-node.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = data-node.Configuration(
    host = "https://example.com/api/v1"
)


# Enter a context with an instance of the API client
with data-node.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data-node.ServiceApi(api_client)
    
    try:
        # Get service information
        api_response = api_instance.get_service()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceApi->get_service: %s\n" % e)
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
**404** | The specified resource was not found |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

