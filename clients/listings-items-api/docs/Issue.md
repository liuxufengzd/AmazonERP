# Issue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | An issue code that identifies the type of issue. | 
**message** | **str** | A message that describes the issue. | 
**severity** | **str** | The severity of the issue. | 
**attribute_names** | **list[str]** | The names of the attributes associated with the issue, if applicable. | [optional] 
**categories** | **list[str]** | List of issue categories.   Possible values:   * &#39;INVALID_ATTRIBUTE&#39; - Indicating an invalid attribute in the listing.   * &#39;MISSING_ATTRIBUTE&#39; - Highlighting a missing attribute in the listing.   * &#39;INVALID_IMAGE&#39; - Signifying an invalid image in the listing.   * &#39;MISSING_IMAGE&#39; - Noting the absence of an image in the listing.   * &#39;INVALID_PRICE&#39; - Pertaining to issues with the listing&#39;s price-related attributes.   * &#39;MISSING_PRICE&#39; - Pointing out the absence of a price attribute in the listing.   * &#39;DUPLICATE&#39; - Identifying listings with potential duplicate problems, such as this ASIN potentially being a duplicate of another ASIN.   * &#39;QUALIFICATION_REQUIRED&#39; - Indicating that the listing requires qualification-related approval. | 
**enforcements** | [**IssueEnforcements**](IssueEnforcements.md) | This field provides information about the enforcement actions taken by Amazon that affect the publishing or status of a listing. It also includes details about any associated exemptions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


