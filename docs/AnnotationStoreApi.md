# nlpsandbox.AnnotationStoreApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_annotation_store**](AnnotationStoreApi.md#create_annotation_store) | **POST** /datasets/{datasetId}/annotationStores | Create an annotation store
[**delete_annotation_store**](AnnotationStoreApi.md#delete_annotation_store) | **DELETE** /datasets/{datasetId}/annotationStores/{annotationStoreId} | Delete an annotation store
[**get_annotation_store**](AnnotationStoreApi.md#get_annotation_store) | **GET** /datasets/{datasetId}/annotationStores/{annotationStoreId} | Get an annotation store
[**list_annotation_stores**](AnnotationStoreApi.md#list_annotation_stores) | **GET** /datasets/{datasetId}/annotationStores | List the annotation stores in a dataset


# **create_annotation_store**
> AnnotationStoreCreateResponse create_annotation_store(dataset_id, annotation_store_id)

Create an annotation store

Create an annotation store with the ID specified

### Example

```python
import time
import nlpsandbox
from nlpsandbox.api import annotation_store_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.annotation_store_id import AnnotationStoreId
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.annotation_store_create_response import AnnotationStoreCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_store_api.AnnotationStoreApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    annotation_store_id = AnnotationStoreId("awesome-annotation-store") # AnnotationStoreId | The ID of the annotation store that is being created.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an annotation store
        api_response = api_instance.create_annotation_store(dataset_id, annotation_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationStoreApi->create_annotation_store: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an annotation store
        api_response = api_instance.create_annotation_store(dataset_id, annotation_store_id, body=body)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationStoreApi->create_annotation_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **annotation_store_id** | **AnnotationStoreId**| The ID of the annotation store that is being created. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**AnnotationStoreCreateResponse**](AnnotationStoreCreateResponse.md)

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

# **delete_annotation_store**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_annotation_store(dataset_id, annotation_store_id)

Delete an annotation store

Deletes the annotation store specified

### Example

```python
import time
import nlpsandbox
from nlpsandbox.api import annotation_store_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.annotation_store_id import AnnotationStoreId
from nlpsandbox.model.dataset_id import DatasetId
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_store_api.AnnotationStoreApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    annotation_store_id = AnnotationStoreId("awesome-annotation-store") # AnnotationStoreId | The ID of the annotation store

    # example passing only required values which don't have defaults set
    try:
        # Delete an annotation store
        api_response = api_instance.delete_annotation_store(dataset_id, annotation_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationStoreApi->delete_annotation_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **annotation_store_id** | **AnnotationStoreId**| The ID of the annotation store |

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

# **get_annotation_store**
> AnnotationStore get_annotation_store(dataset_id, annotation_store_id)

Get an annotation store

Returns the annotation store specified

### Example

```python
import time
import nlpsandbox
from nlpsandbox.api import annotation_store_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.annotation_store_id import AnnotationStoreId
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.annotation_store import AnnotationStore
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_store_api.AnnotationStoreApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    annotation_store_id = AnnotationStoreId("awesome-annotation-store") # AnnotationStoreId | The ID of the annotation store

    # example passing only required values which don't have defaults set
    try:
        # Get an annotation store
        api_response = api_instance.get_annotation_store(dataset_id, annotation_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationStoreApi->get_annotation_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **annotation_store_id** | **AnnotationStoreId**| The ID of the annotation store |

### Return type

[**AnnotationStore**](AnnotationStore.md)

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

# **list_annotation_stores**
> PageOfAnnotationStores list_annotation_stores(dataset_id)

List the annotation stores in a dataset

Returns the annotation stores

### Example

```python
import time
import nlpsandbox
from nlpsandbox.api import annotation_store_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.page_limit import PageLimit
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.page_offset import PageOffset
from nlpsandbox.model.page_of_annotation_stores import PageOfAnnotationStores
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_store_api.AnnotationStoreApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    limit = PageLimit(10) # PageLimit | Maximum number of results returned (optional)
    offset = PageOffset(0) # PageOffset | Index of the first result that must be returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List the annotation stores in a dataset
        api_response = api_instance.list_annotation_stores(dataset_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationStoreApi->list_annotation_stores: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the annotation stores in a dataset
        api_response = api_instance.list_annotation_stores(dataset_id, limit=limit, offset=offset)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationStoreApi->list_annotation_stores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **limit** | **PageLimit**| Maximum number of results returned | [optional]
 **offset** | **PageOffset**| Index of the first result that must be returned | [optional]

### Return type

[**PageOfAnnotationStores**](PageOfAnnotationStores.md)

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

