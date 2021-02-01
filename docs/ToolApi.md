# annotator.ToolApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tool**](ToolApi.md#get_tool) | **GET** /tool | Get tool information
[**get_tool_dependencies**](ToolApi.md#get_tool_dependencies) | **GET** /tool/dependencies | Get tool dependencies


# **get_tool**
> Tool get_tool()

Get tool information

Get information about the tool

### Example

```python
import time
import annotator
from annotator.api import tool_api
from annotator.model.error import Error
from annotator.model.tool import Tool
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = annotator.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with annotator.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tool_api.ToolApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get tool information
        api_response = api_instance.get_tool()
        pprint(api_response)
    except annotator.ApiException as e:
        print("Exception when calling ToolApi->get_tool: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Tool**](Tool.md)

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

# **get_tool_dependencies**
> ToolDependencies get_tool_dependencies()

Get tool dependencies

Get the dependencies of this tool

### Example

```python
import time
import annotator
from annotator.api import tool_api
from annotator.model.error import Error
from annotator.model.tool_dependencies import ToolDependencies
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = annotator.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with annotator.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tool_api.ToolApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get tool dependencies
        api_response = api_instance.get_tool_dependencies()
        pprint(api_response)
    except annotator.ApiException as e:
        print("Exception when calling ToolApi->get_tool_dependencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ToolDependencies**](ToolDependencies.md)

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

