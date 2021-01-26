# datanode.HealthCheckApi

All URIs are relative to *https://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_check**](HealthCheckApi.md#get_health_check) | **GET** /healthCheck | Get health check information


# **get_health_check**
> HealthCheck get_health_check()

Get health check information

Get information about the health of the service

### Example

```python
from __future__ import print_function
import time
import datanode
from datanode.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanode.Configuration(
    host = "https://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanode.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanode.HealthCheckApi(api_client)
    
    try:
        # Get health check information
        api_response = api_instance.get_health_check()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HealthCheckApi->get_health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthCheck**](HealthCheck.md)

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

