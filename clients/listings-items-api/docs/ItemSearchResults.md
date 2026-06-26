# ItemSearchResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_results** | **int** | The total number of selling partner listings items found for the search criteria (only results up to the page count limit is returned per request regardless of the number found).  Note: The maximum number of items (SKUs) that can be returned and paged through is 1000. | 
**pagination** | [**Pagination**](Pagination.md) | If available, the &#x60;nextToken&#x60; and/or &#x60;previousToken&#x60; values required to return paginated results. | [optional] 
**items** | [**list[Item]**](Item.md) | A list of listings items. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


