# datanodeclient.PatientApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_patient**](PatientApi.md#create_patient) | **POST** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient | Create a FHIR Patient
[**delete_patient**](PatientApi.md#delete_patient) | **DELETE** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient/{patientId} | Delete a FHIR Patient
[**get_patient**](PatientApi.md#get_patient) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient/{patientId} | Get a FHIR Patient
[**list_patients**](PatientApi.md#list_patients) | **GET** /datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient | List the Patients in a FHIR store


# **create_patient**
> Patient create_patient(dataset_id, fhir_store_id, patient=patient)

Create a FHIR Patient

Create a FHIR Patient

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
    api_instance = datanodeclient.PatientApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
patient = datanodeclient.Patient() # Patient |  (optional)

    try:
        # Create a FHIR Patient
        api_response = api_instance.create_patient(dataset_id, fhir_store_id, patient=patient)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatientApi->create_patient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset | 
 **fhir_store_id** | **str**| The ID of the FHIR store | 
 **patient** | [**Patient**](Patient.md)|  | [optional] 

### Return type

[**Patient**](Patient.md)

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

# **delete_patient**
> Patient delete_patient(dataset_id, fhir_store_id, patient_id)

Delete a FHIR Patient

Deletes the FHIR Patient specified

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
    api_instance = datanodeclient.PatientApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
patient_id = 'patient_id_example' # str | The ID of the FHIR Patient

    try:
        # Delete a FHIR Patient
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
 **patient_id** | **str**| The ID of the FHIR Patient | 

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
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_patient**
> Patient get_patient(dataset_id, fhir_store_id, patient_id)

Get a FHIR Patient

Returns the FHIR Patient specified

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
    api_instance = datanodeclient.PatientApi(api_client)
    dataset_id = 'dataset_id_example' # str | The ID of the dataset
fhir_store_id = 'fhir_store_id_example' # str | The ID of the FHIR store
patient_id = 'patient_id_example' # str | The ID of the FHIR Patient

    try:
        # Get a FHIR Patient
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
 **patient_id** | **str**| The ID of the FHIR Patient | 

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
**403** | Unauthorized |  -  |
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
    api_instance = datanodeclient.PatientApi(api_client)
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
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

