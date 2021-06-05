# nlpsandbox.FhirStoreApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fhir_store**](FhirStoreApi.md#create_fhir_store) | **POST** /datasets/{datasetId}/fhirStores | Create a FHIR store
[**delete_fhir_store**](FhirStoreApi.md#delete_fhir_store) | **DELETE** /datasets/{datasetId}/fhirStores/{fhirStoreId} | Delete a FHIR store
[**get_fhir_store**](FhirStoreApi.md#get_fhir_store) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId} | Get a FHIR store
[**list_fhir_stores**](FhirStoreApi.md#list_fhir_stores) | **GET** /datasets/{datasetId}/fhirStores | List the FHIR stores in a dataset


# **create_fhir_store**
> FhirStoreCreateResponse create_fhir_store(dataset_id, fhir_store_id)

Create a FHIR store

Create a FHIR store with the ID specified

### Example

```python
import time
import nlpsandbox
from nlpsandbox.apis import fhir_store_api
from nlpsandbox.models.error import Error
from nlpsandbox.models.dataset_id import DatasetId
from nlpsandbox.models.fhir_store_create_response import FhirStoreCreateResponse
from nlpsandbox.models.fhir_store_id import FhirStoreId
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fhir_store_api.FhirStoreApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store that is being created.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a FHIR store
        api_response = api_instance.create_fhir_store(dataset_id, fhir_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling FhirStoreApi->create_fhir_store: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a FHIR store
        api_response = api_instance.create_fhir_store(dataset_id, fhir_store_id, body=body)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling FhirStoreApi->create_fhir_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store that is being created. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**FhirStoreCreateResponse**](FhirStoreCreateResponse.md)

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

# **delete_fhir_store**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_fhir_store(dataset_id, fhir_store_id)

Delete a FHIR store

Deletes the FHIR store specified

### Example

```python
import time
import nlpsandbox
from nlpsandbox.apis import fhir_store_api
from nlpsandbox.models.error import Error
from nlpsandbox.models.dataset_id import DatasetId
from nlpsandbox.models.fhir_store_id import FhirStoreId
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fhir_store_api.FhirStoreApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store

    # example passing only required values which don't have defaults set
    try:
        # Delete a FHIR store
        api_response = api_instance.delete_fhir_store(dataset_id, fhir_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling FhirStoreApi->delete_fhir_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |

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

# **get_fhir_store**
> FhirStore get_fhir_store(dataset_id, fhir_store_id)

Get a FHIR store

Returns the FHIR store specified

### Example

```python
import time
import nlpsandbox
from nlpsandbox.apis import fhir_store_api
from nlpsandbox.models.error import Error
from nlpsandbox.models.fhir_store import FhirStore
from nlpsandbox.models.dataset_id import DatasetId
from nlpsandbox.models.fhir_store_id import FhirStoreId
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fhir_store_api.FhirStoreApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store

    # example passing only required values which don't have defaults set
    try:
        # Get a FHIR store
        api_response = api_instance.get_fhir_store(dataset_id, fhir_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling FhirStoreApi->get_fhir_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |

### Return type

[**FhirStore**](FhirStore.md)

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

# **list_fhir_stores**
> PageOfFhirStores list_fhir_stores(dataset_id)

List the FHIR stores in a dataset

Returns the FHIR stores

### Example

```python
import time
import nlpsandbox
from nlpsandbox.apis import fhir_store_api
from nlpsandbox.models.error import Error
from nlpsandbox.models.page_of_fhir_stores import PageOfFhirStores
from nlpsandbox.models.page_limit import PageLimit
from nlpsandbox.models.dataset_id import DatasetId
from nlpsandbox.models.page_offset import PageOffset
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fhir_store_api.FhirStoreApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    limit = PageLimit(10) # PageLimit | Maximum number of results returned (optional)
    offset = PageOffset(0) # PageOffset | Index of the first result that must be returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List the FHIR stores in a dataset
        api_response = api_instance.list_fhir_stores(dataset_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling FhirStoreApi->list_fhir_stores: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the FHIR stores in a dataset
        api_response = api_instance.list_fhir_stores(dataset_id, limit=limit, offset=offset)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling FhirStoreApi->list_fhir_stores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **limit** | **PageLimit**| Maximum number of results returned | [optional]
 **offset** | **PageOffset**| Index of the first result that must be returned | [optional]

### Return type

[**PageOfFhirStores**](PageOfFhirStores.md)

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

