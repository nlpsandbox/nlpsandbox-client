# data-node.AnnotationApi

All URIs are relative to *https://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_annotation**](AnnotationApi.md#create_annotation) | **POST** /datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations | Create an annotation
[**delete_annotation**](AnnotationApi.md#delete_annotation) | **DELETE** /datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId} | Delete an annotation
[**get_annotation**](AnnotationApi.md#get_annotation) | **GET** /datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId} | Get an annotation
[**list_annotations**](AnnotationApi.md#list_annotations) | **GET** /datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations | List the annotations in an annotation store


# **create_annotation**
> AnnotationCreateResponse create_annotation(dataset_id, annotation_store_id, annotation_create_request=annotation_create_request)

Create an annotation

Create an annotation

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
    api_instance = data-node.AnnotationApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
annotation_store_id = 'annotation_store_id_example' # str | The ID of the annotation store
annotation_create_request = data-node.AnnotationCreateRequest() # AnnotationCreateRequest |  (optional)

    try:
        # Create an annotation
        api_response = api_instance.create_annotation(dataset_id, annotation_store_id, annotation_create_request=annotation_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationApi->create_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **annotation_store_id** | **str**| The ID of the annotation store | 
 **annotation_create_request** | [**AnnotationCreateRequest**](AnnotationCreateRequest.md)|  | [optional] 

### Return type

[**AnnotationCreateResponse**](AnnotationCreateResponse.md)

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

# **delete_annotation**
> object delete_annotation(dataset_id, annotation_store_id, annotation_id)

Delete an annotation

Deletes the annotation specified

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
    api_instance = data-node.AnnotationApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
annotation_store_id = 'annotation_store_id_example' # str | The ID of the annotation store
annotation_id = 'annotation_id_example' # str | The ID of the annotation

    try:
        # Delete an annotation
        api_response = api_instance.delete_annotation(dataset_id, annotation_store_id, annotation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationApi->delete_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **annotation_store_id** | **str**| The ID of the annotation store | 
 **annotation_id** | **str**| The ID of the annotation | 

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

# **get_annotation**
> Annotation get_annotation(dataset_id, annotation_store_id, annotation_id)

Get an annotation

Returns the annotation specified

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
    api_instance = data-node.AnnotationApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
annotation_store_id = 'annotation_store_id_example' # str | The ID of the annotation store
annotation_id = 'annotation_id_example' # str | The ID of the annotation

    try:
        # Get an annotation
        api_response = api_instance.get_annotation(dataset_id, annotation_store_id, annotation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationApi->get_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **annotation_store_id** | **str**| The ID of the annotation store | 
 **annotation_id** | **str**| The ID of the annotation | 

### Return type

[**Annotation**](Annotation.md)

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

# **list_annotations**
> PageOfAnnotations list_annotations(dataset_id, annotation_store_id, limit=limit, offset=offset)

List the annotations in an annotation store

Returns the annotations in an annotation store

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
    api_instance = data-node.AnnotationApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
annotation_store_id = 'annotation_store_id_example' # str | The ID of the annotation store
limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)

    try:
        # List the annotations in an annotation store
        api_response = api_instance.list_annotations(dataset_id, annotation_store_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationApi->list_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **annotation_store_id** | **str**| The ID of the annotation store | 
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]

### Return type

[**PageOfAnnotations**](PageOfAnnotations.md)

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

