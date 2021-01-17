# datanode.NoteApi

All URIs are relative to *https://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_note**](NoteApi.md#create_note) | **POST** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Note | Create a note
[**delete_note**](NoteApi.md#delete_note) | **DELETE** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Note/{noteId} | Delete a note
[**get_note**](NoteApi.md#get_note) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Note/{noteId} | Get a note
[**list_notes**](NoteApi.md#list_notes) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Note | List notes


# **create_note**
> NoteCreateResponse create_note(dataset_id, fhir_store_id, note_create_request=note_create_request)

Create a note

Create a note

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
    api_instance = datanode.NoteApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
note_create_request = datanode.NoteCreateRequest() # NoteCreateRequest |  (optional)

    try:
        # Create a note
        api_response = api_instance.create_note(dataset_id, fhir_store_id, note_create_request=note_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NoteApi->create_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **note_create_request** | [**NoteCreateRequest**](NoteCreateRequest.md)|  | [optional] 

### Return type

[**NoteCreateResponse**](NoteCreateResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note**
> object delete_note(dataset_id, fhir_store_id, note_id)

Delete a note

Deletes the note specified

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
    api_instance = datanode.NoteApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
note_id = 'note_id_example' # str | The ID of the note

    try:
        # Delete a note
        api_response = api_instance.delete_note(dataset_id, fhir_store_id, note_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NoteApi->delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **note_id** | **str**| The ID of the note | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note**
> Note get_note(dataset_id, fhir_store_id, note_id)

Get a note

Returns the note specified

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
    api_instance = datanode.NoteApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
note_id = 'note_id_example' # str | The ID of the note

    try:
        # Get a note
        api_response = api_instance.get_note(dataset_id, fhir_store_id, note_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NoteApi->get_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **note_id** | **str**| The ID of the note | 

### Return type

[**Note**](Note.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notes**
> PageOfNotes list_notes(dataset_id, fhir_store_id, limit=limit, offset=offset)

List notes

Returns the notes in a FHIR store

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
    api_instance = datanode.NoteApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)

    try:
        # List notes
        api_response = api_instance.list_notes(dataset_id, fhir_store_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NoteApi->list_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]

### Return type

[**PageOfNotes**](PageOfNotes.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

