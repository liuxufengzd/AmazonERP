# ItemSearchResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_results** | **int** | For searches that are based on &#x60;identifiers&#x60;, &#x60;numberOfResults&#x60; is the total number of Amazon catalog items found. For searches that are based on &#x60;keywords&#x60;, &#x60;numberOfResults&#x60; is the estimated total number of Amazon catalog items that are matched by the search query. Only results up to the page count limit are returned per request regardless of the number found.  **Note:** The maximum number of items (ASINs) that can be returned and paged through is 1,000. | 
**pagination** | [**Pagination**](Pagination.md) | The &#x60;nextToken&#x60; and &#x60;previousToken&#x60; values that are required to retrieve paginated results. | [optional] 
**refinements** | [**Refinements**](Refinements.md) | Search refinements for searches that are based on &#x60;keywords&#x60;. | [optional] 
**items** | [**list[Item]**](Item.md) | A list of items from the Amazon catalog. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


