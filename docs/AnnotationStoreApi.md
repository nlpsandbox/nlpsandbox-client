# datanode.AnnotationStoreApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_annotation_store**](AnnotationStoreApi.md#create_annotation_store) | **POST** /datasets/{datasetId}/annotationStores | Create an annotation store
[**delete_annotation_store**](AnnotationStoreApi.md#delete_annotation_store) | **DELETE** /datasets/{datasetId}/annotationStores/{annotationStoreId} | Delete an annotation store
[**get_annotation_store**](AnnotationStoreApi.md#get_annotation_store) | **GET** /datasets/{datasetId}/annotationStores/{annotationStoreId} | Get an annotation store
[**list_annotation_stores**](AnnotationStoreApi.md#list_annotation_stores) | **GET** /datasets/{datasetId}/annotationStores | List the annotation stores in a dataset


# **create_annotation_store**
> AnnotationStoreCreateResponse create_annotation_store(dataset_id, annotation_store_id, body=body)

Create an annotation store

Create an annotation store with the ID specified

### Example

```python
from __future__ import print_function
import time
import datanode
from datanode.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanode.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanode.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanode.AnnotationStoreApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
annotation_store_id = 'annotation_store_id_example' # str | The ID of the annotation store that is being created.
body = None # object |  (optional)

    try:
        # Create an annotation store
        api_response = api_instance.create_annotation_store(dataset_id, annotation_store_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationStoreApi->create_annotation_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **annotation_store_id** | **str**| The ID of the annotation store that is being created. | 
 **body** | **object**|  | [optional] 

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
> object delete_annotation_store(dataset_id, annotation_store_id)

Delete an annotation store

Deletes the annotation store specified

### Example

```python
from __future__ import print_function
import time
import datanode
from datanode.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanode.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanode.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanode.AnnotationStoreApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
annotation_store_id = 'annotation_store_id_example' # str | The ID of the annotation store

    try:
        # Delete an annotation store
        api_response = api_instance.delete_annotation_store(dataset_id, annotation_store_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationStoreApi->delete_annotation_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **annotation_store_id** | **str**| The ID of the annotation store | 

### Return type

**object**

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
from __future__ import print_function
import time
import datanode
from datanode.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanode.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanode.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanode.AnnotationStoreApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
annotation_store_id = 'annotation_store_id_example' # str | The ID of the annotation store

    try:
        # Get an annotation store
        api_response = api_instance.get_annotation_store(dataset_id, annotation_store_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationStoreApi->get_annotation_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **annotation_store_id** | **str**| The ID of the annotation store | 

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
> PageOfAnnotationStores list_annotation_stores(dataset_id, limit=limit, offset=offset)

List the annotation stores in a dataset

Returns the annotation stores

### Example

```python
from __future__ import print_function
import time
import datanode
from datanode.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanode.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanode.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanode.AnnotationStoreApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)

    try:
        # List the annotation stores in a dataset
        api_response = api_instance.list_annotation_stores(dataset_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationStoreApi->list_annotation_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]

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

