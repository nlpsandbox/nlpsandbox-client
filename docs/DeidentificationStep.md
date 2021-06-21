# DeidentificationStep

The configuration of a deidentification step

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation_types** | **[str]** | The types of annotations to which the de-identifer should apply the selected strategy | 
**confidence_threshold** | **float** | The minimum confidence level for a given annotation to be de-identified | [optional]  if omitted the server will use the default value of 0
**masking_char_config** | [**MaskingCharConfig**](MaskingCharConfig.md) |  | [optional] 
**annotation_type_mask_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Configuration for the \&quot;annotation type\&quot; strategy. E.g. \&quot;John Smith lives at 123 Main St\&quot; -&gt; \&quot;[PERSON_NAME] lives at [LOCATION]\&quot;. | [optional] 
**redact_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Configuration for the redaction strategy. E.g. \&quot;John Smith lives at 123 Main St\&quot; -&gt; \&quot;lives at\&quot;. | [optional] 
**date_offset_config** | [**DateOffsetConfig**](DateOffsetConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


