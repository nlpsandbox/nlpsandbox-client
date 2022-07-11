# Tool

Information about an NLP tool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The tool name | 
**version** | **str** | The version of the tool (SemVer string) | 
**license** | [**License**](License.md) |  | 
**repository** | **str** | The place where the code lives | 
**description** | **str** | A short, one-sentence summary of the tool | 
**author** | **str** | The author of the tool | 
**author_email** | **str** | The email address of the author | 
**url** | **str** | The URL to the homepage of the tool | 
**type** | [**ToolType**](ToolType.md) |  | 
**api_version** | **str** | The version of the tool OpenAPI specification | 
**programming_languages** | [**[ProgrammingLanguage]**](ProgrammingLanguage.md) | The programming languages used to develop this tool | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


