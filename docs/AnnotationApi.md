# nlpsandbox.AnnotationApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_annotation**](AnnotationApi.md#create_annotation) | **POST** /datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations | Create an annotation
[**delete_annotation**](AnnotationApi.md#delete_annotation) | **DELETE** /datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId} | Delete an annotation
[**get_annotation**](AnnotationApi.md#get_annotation) | **GET** /datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId} | Get an annotation
[**list_annotations**](AnnotationApi.md#list_annotations) | **GET** /datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations | List the annotations in an annotation store


# **create_annotation**
> AnnotationCreateResponse create_annotation(dataset_id, annotation_store_id, annotation_id)

Create an annotation

Create an annotation

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import annotation_api
from nlpsandbox.model.annotation_create_response import AnnotationCreateResponse
from nlpsandbox.model.error import Error
from nlpsandbox.model.annotation_id import AnnotationId
from nlpsandbox.model.annotation_store_id import AnnotationStoreId
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.annotation_create_request import AnnotationCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_api.AnnotationApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    annotation_store_id = AnnotationStoreId("awesome-annotation-store") # AnnotationStoreId | The ID of the annotation store
    annotation_id = AnnotationId("awesome-annotation") # AnnotationId | The ID of the annotation that is being created
    annotation_create_request = AnnotationCreateRequest(
        annotation_source=AnnotationSource(
            resource_source=ResourceSource(
                name="name_example",
            ),
        ),
        text_date_annotations=[
            TextDateAnnotation(),
        ],
        text_person_name_annotations=[
            TextPersonNameAnnotation(),
        ],
        text_location_annotations=[
            TextLocationAnnotation(),
        ],
        text_id_annotations=[
            TextIdAnnotation(),
        ],
        text_contact_annotations=[
            TextContactAnnotation(),
        ],
        text_covid_symptom_annotations=[
            TextCovidSymptomAnnotation(),
        ],
    ) # AnnotationCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an annotation
        api_response = api_instance.create_annotation(dataset_id, annotation_store_id, annotation_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationApi->create_annotation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an annotation
        api_response = api_instance.create_annotation(dataset_id, annotation_store_id, annotation_id, annotation_create_request=annotation_create_request)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationApi->create_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **annotation_store_id** | **AnnotationStoreId**| The ID of the annotation store |
 **annotation_id** | **AnnotationId**| The ID of the annotation that is being created |
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
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_annotation(dataset_id, annotation_store_id, annotation_id)

Delete an annotation

Deletes the annotation specified

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import annotation_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.annotation_id import AnnotationId
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.fhir_store_id import FhirStoreId
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_api.AnnotationApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    annotation_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the annotation store
    annotation_id = AnnotationId("awesome-annotation") # AnnotationId | The ID of the annotation

    # example passing only required values which don't have defaults set
    try:
        # Delete an annotation
        api_response = api_instance.delete_annotation(dataset_id, annotation_store_id, annotation_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationApi->delete_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **annotation_store_id** | **FhirStoreId**| The ID of the annotation store |
 **annotation_id** | **AnnotationId**| The ID of the annotation |

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

# **get_annotation**
> Annotation get_annotation(dataset_id, annotation_store_id, annotation_id)

Get an annotation

Returns the annotation specified

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import annotation_api
from nlpsandbox.model.annotation import Annotation
from nlpsandbox.model.error import Error
from nlpsandbox.model.annotation_id import AnnotationId
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.fhir_store_id import FhirStoreId
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_api.AnnotationApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    annotation_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the annotation store
    annotation_id = AnnotationId("awesome-annotation") # AnnotationId | The ID of the annotation

    # example passing only required values which don't have defaults set
    try:
        # Get an annotation
        api_response = api_instance.get_annotation(dataset_id, annotation_store_id, annotation_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationApi->get_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **annotation_store_id** | **FhirStoreId**| The ID of the annotation store |
 **annotation_id** | **AnnotationId**| The ID of the annotation |

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
> PageOfAnnotations list_annotations(dataset_id, annotation_store_id)

List the annotations in an annotation store

Returns the annotations in an annotation store

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import annotation_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.annotation_store_id import AnnotationStoreId
from nlpsandbox.model.page_limit import PageLimit
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.page_offset import PageOffset
from nlpsandbox.model.page_of_annotations import PageOfAnnotations
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_api.AnnotationApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    annotation_store_id = AnnotationStoreId("awesome-annotation-store") # AnnotationStoreId | The ID of the annotation store
    limit = PageLimit(10) # PageLimit | Maximum number of results returned (optional)
    offset = PageOffset(0) # PageOffset | Index of the first result that must be returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List the annotations in an annotation store
        api_response = api_instance.list_annotations(dataset_id, annotation_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationApi->list_annotations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the annotations in an annotation store
        api_response = api_instance.list_annotations(dataset_id, annotation_store_id, limit=limit, offset=offset)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling AnnotationApi->list_annotations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **annotation_store_id** | **AnnotationStoreId**| The ID of the annotation store |
 **limit** | **PageLimit**| Maximum number of results returned | [optional]
 **offset** | **PageOffset**| Index of the first result that must be returned | [optional]

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

