# nlpsandbox.DatasetApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](DatasetApi.md#create_dataset) | **POST** /datasets | Create a dataset
[**delete_dataset**](DatasetApi.md#delete_dataset) | **DELETE** /datasets/{datasetId} | Delete a dataset by ID
[**get_dataset**](DatasetApi.md#get_dataset) | **GET** /datasets/{datasetId} | Get a dataset by ID
[**list_datasets**](DatasetApi.md#list_datasets) | **GET** /datasets | Get all datasets


# **create_dataset**
> DatasetCreateResponse create_dataset(dataset_id)

Create a dataset

Create a dataset with the name specified

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import dataset_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.dataset_create_response import DatasetCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # str | The ID of the dataset that is being created
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a dataset
        api_response = api_instance.create_dataset(dataset_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling DatasetApi->create_dataset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a dataset
        api_response = api_instance.create_dataset(dataset_id, body=body)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling DatasetApi->create_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset that is being created |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**DatasetCreateResponse**](DatasetCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid request |  -  |
**409** | The request conflicts with current state of the target resource |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_dataset(dataset_id)

Delete a dataset by ID

Deletes the dataset for a given ID

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import dataset_api
from nlpsandbox.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # str | The ID of the dataset

    # example passing only required values which don't have defaults set
    try:
        # Delete a dataset by ID
        api_response = api_instance.delete_dataset(dataset_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling DatasetApi->delete_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **get_dataset**
> Dataset get_dataset(dataset_id)

Get a dataset by ID

Returns the dataset for a given ID

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import dataset_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.dataset import Dataset
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # str | The ID of the dataset

    # example passing only required values which don't have defaults set
    try:
        # Get a dataset by ID
        api_response = api_instance.get_dataset(dataset_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling DatasetApi->get_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset |

### Return type

[**Dataset**](Dataset.md)

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

# **list_datasets**
> PageOfDatasets list_datasets()

Get all datasets

Returns the datasets

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import dataset_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.page_of_datasets import PageOfDatasets
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)
    limit = PageLimit(10) # int | Maximum number of results returned (optional) if omitted the server will use the default value of 10
    offset = PageOffset(0) # int | Index of the first result that must be returned (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all datasets
        api_response = api_instance.list_datasets(limit=limit, offset=offset)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling DatasetApi->list_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results returned | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| Index of the first result that must be returned | [optional] if omitted the server will use the default value of 0

### Return type

[**PageOfDatasets**](PageOfDatasets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

