# PageOfPatients

A page of FHIR patients

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | [**PageOffset**](PageOffset.md) |  | 
**limit** | [**PageLimit**](PageLimit.md) |  | 
**links** | [**ResponsePageMetadataLinks**](ResponsePageMetadataLinks.md) |  | 
**total_results** | **int** | The total number of results in the result set | 
**patients** | [**[Patient]**](Patient.md) | An array of FHIR patients | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


