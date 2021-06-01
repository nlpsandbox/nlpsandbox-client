# nlpsandboxsdk.HealthCheckApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_check**](HealthCheckApi.md#get_health_check) | **GET** /healthCheck | Get health check information


# **get_health_check**
> HealthCheck get_health_check()

Get health check information

Get information about the health of the service

### Example

```python
import time
import nlpsandboxsdk
from nlpsandboxsdk.api import health_check_api
from nlpsandboxsdk.model.error import Error
from nlpsandboxsdk.model.health_check import HealthCheck
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandboxsdk.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandboxsdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_check_api.HealthCheckApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get health check information
        api_response = api_instance.get_health_check()
        pprint(api_response)
    except nlpsandboxsdk.ApiException as e:
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

