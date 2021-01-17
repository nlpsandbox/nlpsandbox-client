# datanode.PatientApi

All URIs are relative to *https://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_patient**](PatientApi.md#create_patient) | **POST** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient | Create a FHIR patient
[**delete_patient**](PatientApi.md#delete_patient) | **DELETE** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient/{patientId} | Delete a FHIR patient
[**get_patient**](PatientApi.md#get_patient) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient/{patientId} | Get a FHIR patient
[**list_patients**](PatientApi.md#list_patients) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient | List the Patients in a FHIR store


# **create_patient**
> PatientCreateResponse create_patient(dataset_id, fhir_store_id, patient_create_request=patient_create_request)

Create a FHIR patient

Create a FHIR patient

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
    api_instance = datanode.PatientApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
patient_create_request = datanode.PatientCreateRequest() # PatientCreateRequest |  (optional)

    try:
        # Create a FHIR patient
        api_response = api_instance.create_patient(dataset_id, fhir_store_id, patient_create_request=patient_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatientApi->create_patient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **patient_create_request** | [**PatientCreateRequest**](PatientCreateRequest.md)|  | [optional] 

### Return type

[**PatientCreateResponse**](PatientCreateResponse.md)

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

# **delete_patient**
> object delete_patient(dataset_id, fhir_store_id, patient_id)

Delete a FHIR patient

Deletes the FHIR patient specified

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
    api_instance = datanode.PatientApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
patient_id = 'patient_id_example' # str | The ID of the FHIR patient

    try:
        # Delete a FHIR patient
        api_response = api_instance.delete_patient(dataset_id, fhir_store_id, patient_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatientApi->delete_patient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **patient_id** | **str**| The ID of the FHIR patient | 

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

# **get_patient**
> Patient get_patient(dataset_id, fhir_store_id, patient_id)

Get a FHIR patient

Returns the FHIR patient specified

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
    api_instance = datanode.PatientApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
patient_id = 'patient_id_example' # str | The ID of the FHIR patient

    try:
        # Get a FHIR patient
        api_response = api_instance.get_patient(dataset_id, fhir_store_id, patient_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatientApi->get_patient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **patient_id** | **str**| The ID of the FHIR patient | 

### Return type

[**Patient**](Patient.md)

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

# **list_patients**
> PageOfPatients list_patients(dataset_id, fhir_store_id, limit=limit, offset=offset)

List the Patients in a FHIR store

Returns the Patients in a FHIR store

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
    api_instance = datanode.PatientApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)

    try:
        # List the Patients in a FHIR store
        api_response = api_instance.list_patients(dataset_id, fhir_store_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatientApi->list_patients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]

### Return type

[**PageOfPatients**](PageOfPatients.md)

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

