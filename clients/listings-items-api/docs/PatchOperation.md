# PatchOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Type of JSON Patch operation. Supported JSON Patch operations include &#x60;add&#x60;, &#x60;replace&#x60;, &#x60;merge&#x60; and &#x60;delete&#x60;. Refer to &lt;https://tools.ietf.org/html/rfc6902&gt;. | 
**path** | **str** | JSON Pointer path of the element to patch. Refer to [JavaScript Object Notation (JSON) Patch](https://tools.ietf.org/html/rfc6902) for more information. | 
**value** | **list[object]** | JSON value to &#x60;add&#x60;, &#x60;replace&#x60;, &#x60;merge&#x60; or &#x60;delete&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


