# datanodeclient.FhirStoreApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fhir_store**](FhirStoreApi.md#create_fhir_store) | **POST** /datasets/{datasetId}/fhirStores | Create a FHIR store
[**delete_fhir_store**](FhirStoreApi.md#delete_fhir_store) | **DELETE** /datasets/{datasetId}/fhirStores/{fhirStoreId} | Delete a FHIR store
[**get_fhir_store**](FhirStoreApi.md#get_fhir_store) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId} | Get a FHIR store
[**list_fhir_stores**](FhirStoreApi.md#list_fhir_stores) | **GET** /datasets/{datasetId}/fhirStores | List the FHIR stores in a dataset


# **create_fhir_store**
> FhirStore create_fhir_store(dataset_id, fhir_store_id, fhir_store=fhir_store)

Create a FHIR store

Create a FHIR store with the ID specified

### Example

```python
from __future__ import print_function
import time
import datanodeclient
from datanodeclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanodeclient.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanodeclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanodeclient.FhirStoreApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'awesome-fhir-store' # str | The ID of the FHIR store that is being created.
fhir_store = datanodeclient.FhirStore() # FhirStore |  (optional)

    try:
        # Create a FHIR store
        api_response = api_instance.create_fhir_store(dataset_id, fhir_store_id, fhir_store=fhir_store)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FhirStoreApi->create_fhir_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store that is being created. | 
 **fhir_store** | [**FhirStore**](FhirStore.md)|  | [optional] 

### Return type

[**FhirStore**](FhirStore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |
**409** | The request conflicts with current state of the target resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fhir_store**
> FhirStore delete_fhir_store(dataset_id, fhir_store_id)

Delete a FHIR store

Deletes the FHIR store specified

### Example

```python
from __future__ import print_function
import time
import datanodeclient
from datanodeclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanodeclient.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanodeclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanodeclient.FhirStoreApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store

    try:
        # Delete a FHIR store
        api_response = api_instance.delete_fhir_store(dataset_id, fhir_store_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FhirStoreApi->delete_fhir_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 

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
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fhir_store**
> FhirStore get_fhir_store(dataset_id, fhir_store_id)

Get a FHIR store

Returns the FHIR store specified

### Example

```python
from __future__ import print_function
import time
import datanodeclient
from datanodeclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanodeclient.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanodeclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanodeclient.FhirStoreApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store

    try:
        # Get a FHIR store
        api_response = api_instance.get_fhir_store(dataset_id, fhir_store_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FhirStoreApi->get_fhir_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 

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
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fhir_stores**
> PageOfFhirStores list_fhir_stores(dataset_id, limit=limit, offset=offset)

List the FHIR stores in a dataset

Returns the FHIR stores

### Example

```python
from __future__ import print_function
import time
import datanodeclient
from datanodeclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datanodeclient.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with datanodeclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datanodeclient.FhirStoreApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)

    try:
        # List the FHIR stores in a dataset
        api_response = api_instance.list_fhir_stores(dataset_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FhirStoreApi->list_fhir_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]

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
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

