# nlpsandbox.PatientApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_patient**](PatientApi.md#create_patient) | **POST** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient | Create a FHIR patient
[**delete_patient**](PatientApi.md#delete_patient) | **DELETE** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient/{patientId} | Delete a FHIR patient
[**get_patient**](PatientApi.md#get_patient) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient/{patientId} | Get a FHIR patient
[**list_patients**](PatientApi.md#list_patients) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient | List the Patients in a FHIR store


# **create_patient**
> PatientCreateResponse create_patient(dataset_id, fhir_store_id, patient_id)

Create a FHIR patient

Create a FHIR patient

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import patient_api
from nlpsandbox.model.patient_id import PatientId
from nlpsandbox.model.error import Error
from nlpsandbox.model.patient_create_request import PatientCreateRequest
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.fhir_store_id import FhirStoreId
from nlpsandbox.model.patient_create_response import PatientCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nlpsandbox.Configuration(
    host = "http://example.com/api/v1"
)


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = patient_api.PatientApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store
    patient_id = PatientId("awesome-patient") # PatientId | The ID of the patient that is being created
    patient_create_request = PatientCreateRequest(
        gender="male",
    ) # PatientCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a FHIR patient
        api_response = api_instance.create_patient(dataset_id, fhir_store_id, patient_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling PatientApi->create_patient: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a FHIR patient
        api_response = api_instance.create_patient(dataset_id, fhir_store_id, patient_id, patient_create_request=patient_create_request)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling PatientApi->create_patient: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |
 **patient_id** | **PatientId**| The ID of the patient that is being created |
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
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_patient**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_patient(dataset_id, fhir_store_id, patient_id)

Delete a FHIR patient

Deletes the FHIR patient specified

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import patient_api
from nlpsandbox.model.patient_id import PatientId
from nlpsandbox.model.error import Error
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
    api_instance = patient_api.PatientApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store
    patient_id = PatientId("awesome-patient") # PatientId | The ID of the FHIR patient

    # example passing only required values which don't have defaults set
    try:
        # Delete a FHIR patient
        api_response = api_instance.delete_patient(dataset_id, fhir_store_id, patient_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling PatientApi->delete_patient: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |
 **patient_id** | **PatientId**| The ID of the FHIR patient |

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

# **get_patient**
> Patient get_patient(dataset_id, fhir_store_id, patient_id)

Get a FHIR patient

Returns the FHIR patient specified

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import patient_api
from nlpsandbox.model.patient_id import PatientId
from nlpsandbox.model.error import Error
from nlpsandbox.model.patient import Patient
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
    api_instance = patient_api.PatientApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store
    patient_id = PatientId("awesome-patient") # PatientId | The ID of the FHIR patient

    # example passing only required values which don't have defaults set
    try:
        # Get a FHIR patient
        api_response = api_instance.get_patient(dataset_id, fhir_store_id, patient_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling PatientApi->get_patient: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |
 **patient_id** | **PatientId**| The ID of the FHIR patient |

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
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_patients**
> PageOfPatients list_patients(dataset_id, fhir_store_id)

List the Patients in a FHIR store

Returns the Patients in a FHIR store

### Example


```python
import time
import nlpsandbox
from nlpsandbox.api import patient_api
from nlpsandbox.model.error import Error
from nlpsandbox.model.page_of_patients import PageOfPatients
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


# Enter a context with an instance of the API client
with nlpsandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = patient_api.PatientApi(api_client)
    dataset_id = DatasetId("awesome-dataset") # DatasetId | The ID of the dataset
    fhir_store_id = FhirStoreId("awesome-fhir-store") # FhirStoreId | The ID of the FHIR store
    limit = PageLimit(10) # PageLimit | Maximum number of results returned (optional)
    offset = PageOffset(0) # PageOffset | Index of the first result that must be returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List the Patients in a FHIR store
        api_response = api_instance.list_patients(dataset_id, fhir_store_id)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling PatientApi->list_patients: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the Patients in a FHIR store
        api_response = api_instance.list_patients(dataset_id, fhir_store_id, limit=limit, offset=offset)
        pprint(api_response)
    except nlpsandbox.ApiException as e:
        print("Exception when calling PatientApi->list_patients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **DatasetId**| The ID of the dataset |
 **fhir_store_id** | **FhirStoreId**| The ID of the FHIR store |
 **limit** | **PageLimit**| Maximum number of results returned | [optional]
 **offset** | **PageOffset**| Index of the first result that must be returned | [optional]

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
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

