# Annotation

An annotation record
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Resource name of the annotation record, of the form datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId} | [optional] 
**annotation_source** | [**AnnotationSource**](AnnotationSource.md) |  | [optional] 
**text_date_annotations** | [**list[TextDateAnnotation]**](TextDateAnnotation.md) | Date annotations in a text | [optional] 
**text_person_name_annotations** | [**list[TextPersonNameAnnotation]**](TextPersonNameAnnotation.md) | Person name annotations in a text | [optional] 
**text_physical_address_annotations** | [**list[TextPhysicalAddressAnnotation]**](TextPhysicalAddressAnnotation.md) | Physical address annotations in a text | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


