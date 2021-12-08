# nlpsandbox.NoteApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_note**](NoteApi.md#create_note) | **POST** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Note | Create a note
[**delete_note**](NoteApi.md#delete_note) | **DELETE** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Note/{noteId} | Delete a note
[**get_note**](NoteApi.md#get_note) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Note/{noteId} | Get a note
[**list_notes**](NoteApi.md#list_notes) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Note | List notes


# **create_note**
> NoteCreateResponse create_note(dataset_id, fhir_store_id, note_id)

Create a note

Create a note

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import nlpsandbox
from nlpsandbox.api import note_api
from nlpsandbox.model.note_id import NoteId
from nlpsandbox.model.error import Error
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.fhir_store_id import FhirStoreId
from nlpsandbox.model.note_create_request import NoteCreateRequest
from nlpsandbox.model.note_create_response import NoteCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with nlpsandbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = note_api.NoteApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store
    note_id = NoteId("awesome-note") # NoteId | The ID of the note that is being created
    note_create_request = NoteCreateRequest(
        text="On 12/26/2020, Ms. Chloe Price met with Dr. Prescott in Seattle.",
        type="loinc:LP29684-5",
        patient_id=PatientId("awesome-patient"),
    ) # NoteCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a note
        api_response = api_instance.create_note(dataset_id, fhir_store_id, note_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling NoteApi->create_note: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a note
        api_response = api_instance.create_note(dataset_id, fhir_store_id, note_id, note_create_request=note_create_request)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling NoteApi->create_note: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |
 **note_id** | **NoteId**| The ID of the note that is being created |
 **note_create_request** | [**NoteCreateRequest**](NoteCreateRequest.md)|  | [optional]

### Return type

[**NoteCreateResponse**](NoteCreateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **delete_note**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_note(dataset_id, fhir_store_id, note_id)

Delete a note

Deletes the note specified

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import nlpsandbox
from nlpsandbox.api import note_api
from nlpsandbox.model.note_id import NoteId
from nlpsandbox.model.error import Error
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.fhir_store_id import FhirStoreId
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with nlpsandbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = note_api.NoteApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store
    note_id = NoteId("awesome-note") # NoteId | The ID of the note

    # example passing only required values which don't have defaults set
    try:
        # Delete a note
        api_response = api_instance.delete_note(dataset_id, fhir_store_id, note_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling NoteApi->delete_note: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |
 **note_id** | **NoteId**| The ID of the note |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **get_note**
> Note get_note(dataset_id, fhir_store_id, note_id)

Get a note

Returns the note specified

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import nlpsandbox
from nlpsandbox.api import note_api
from nlpsandbox.model.note_id import NoteId
from nlpsandbox.model.error import Error
from nlpsandbox.model.note import Note
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.fhir_store_id import FhirStoreId
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with nlpsandbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = note_api.NoteApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store
    note_id = NoteId("awesome-note") # NoteId | The ID of the note

    # example passing only required values which don't have defaults set
    try:
        # Get a note
        api_response = api_instance.get_note(dataset_id, fhir_store_id, note_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling NoteApi->get_note: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |
 **note_id** | **NoteId**| The ID of the note |

### Return type

[**Note**](Note.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **list_notes**
> PageOfNotes list_notes(dataset_id, fhir_store_id)

List notes

Returns the notes in a FHIR store

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import nlpsandbox
from nlpsandbox.api import note_api
from nlpsandbox.model.page_of_notes import PageOfNotes
from nlpsandbox.model.error import Error
from nlpsandbox.model.page_limit import PageLimit
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.fhir_store_id import FhirStoreId
from nlpsandbox.model.page_offset import PageOffset
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with nlpsandbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = note_api.NoteApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store
    limit = PageLimit(10) # PageLimit | Maximum number of results returned (optional)
    offset = PageOffset(0) # PageOffset | Index of the first result that must be returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List notes
        api_response = api_instance.list_notes(dataset_id, fhir_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling NoteApi->list_notes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List notes
        api_response = api_instance.list_notes(dataset_id, fhir_store_id, limit=limit, offset=offset)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling NoteApi->list_notes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |
 **limit** | **PageLimit**| Maximum number of results returned | [optional]
 **offset** | **PageOffset**| Index of the first result that must be returned | [optional]

### Return type

[**PageOfNotes**](PageOfNotes.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

