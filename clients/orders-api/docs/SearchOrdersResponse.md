# SearchOrdersResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**list[Order]**](Order.md) | An array containing all orders that match the search criteria. | 
**pagination** | [**Pagination**](Pagination.md) | Pagination occurs when a request has results that exceed the response limit. This means the results are divided into individual pages. To retrieve a different page, you must pass the token value as the &#x60;paginationToken&#x60; query parameter in the subsequent request. All other parameters must be provided with the same values that were provided with the request that generated this token, with the exception of &#x60;maxResultsPerPage&#x60; and &#x60;includedData&#x60;, which can be modified between calls. The token will expire after 24 hours. When there are no other pages to fetch, the &#x60;pagination&#x60; field will be absent from the response. | [optional] 
**last_updated_before** | **datetime** | Only orders updated before the specified time are returned. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format. | [optional] 
**created_before** | **datetime** | Only orders placed before the specified time are returned. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


