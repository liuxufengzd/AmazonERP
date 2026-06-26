# swagger_client.SearchOrdersApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_orders**](SearchOrdersApi.md#search_orders) | **GET** /orders/2026-01-01/orders | 


# **search_orders**
> SearchOrdersResponse search_orders(created_after=created_after, created_before=created_before, last_updated_after=last_updated_after, last_updated_before=last_updated_before, fulfillment_statuses=fulfillment_statuses, marketplace_ids=marketplace_ids, fulfilled_by=fulfilled_by, max_results_per_page=max_results_per_page, pagination_token=pagination_token, included_data=included_data)



Returns orders created or updated during the time period that you specify. You can filter the response for specific types of orders.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0056 | 20 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchOrdersApi()
created_after = '2025-01-01T00:00:00Z' # datetime | The response includes orders created at or after this time. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: You must provide exactly one of `createdAfter` and `lastUpdatedAfter` in your request. If `createdAfter` is provided, neither `lastUpdatedAfter` nor `lastUpdatedBefore` may be provided. (optional)
created_before = '2025-01-01T00:00:00Z' # datetime | The response includes orders created at or before this time. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: If you include `createdAfter` in the request, `createdBefore` is optional, and if provided must be equal to or after the `createdAfter` date and at least two minutes before the time of the request. If `createdBefore` is provided, neither `lastUpdatedAfter` nor `lastUpdatedBefore` may be provided. (optional)
last_updated_after = '2025-01-01T00:00:00Z' # datetime | The response includes orders updated at or after this time. An update is any change made by Amazon or the seller, including changes to order status. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: You must provide exactly one of `createdAfter` and `lastUpdatedAfter`. If `lastUpdatedAfter` is provided, neither `createdAfter` nor `createdBefore` may be provided. (optional)
last_updated_before = '2025-01-01T00:00:00Z' # datetime | The response includes orders updated at or before this time. An update is any change made by Amazon or the seller, including changes to order status. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: If you include `lastUpdatedAfter` in the request, `lastUpdatedBefore` is optional, and if provided must be equal to or after the `lastUpdatedAfter` date and at least two minutes before the time of the request. If `lastUpdatedBefore` is provided, neither `createdAfter` nor `createdBefore` may be provided. (optional)
fulfillment_statuses = ['[PENDING, UNSHIPPED]'] # list[str] | A list of `FulfillmentStatus` values you can use to filter the results. (optional)
marketplace_ids = ['[ATVPDKIKX0DER, A2EUQ1WTGCTBG2]'] # list[str] | The response includes orders that were placed in marketplaces you include in this list.  Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) for a complete list of `marketplaceId` values. (optional)
fulfilled_by = ['[AMAZON, MERCHANT]'] # list[str] | The response includes orders that are fulfilled by the parties that you include in this list. (optional)
max_results_per_page = 50 # int | The maximum number of orders that can be returned per page. The value must be between 1 and 100. **Default:** 100. (optional)
pagination_token = '2YgYW55IGNhcm5hbCBwbGVhc3VyZS4' # str | Pagination occurs when a request produces a response that exceeds the `maxResultsPerPage`. This means that the response is divided into individual pages. To retrieve the next page, you must pass the `nextToken` value as the `paginationToken` query parameter in the next request. You will not receive a `nextToken` value on the last page. (optional)
included_data = ['[BUYER, PACKAGES]'] # list[str] | A list of datasets to include in the response. (optional)

try:
    api_response = api_instance.search_orders(created_after=created_after, created_before=created_before, last_updated_after=last_updated_after, last_updated_before=last_updated_before, fulfillment_statuses=fulfillment_statuses, marketplace_ids=marketplace_ids, fulfilled_by=fulfilled_by, max_results_per_page=max_results_per_page, pagination_token=pagination_token, included_data=included_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchOrdersApi->search_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| The response includes orders created at or after this time. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: You must provide exactly one of &#x60;createdAfter&#x60; and &#x60;lastUpdatedAfter&#x60; in your request. If &#x60;createdAfter&#x60; is provided, neither &#x60;lastUpdatedAfter&#x60; nor &#x60;lastUpdatedBefore&#x60; may be provided. | [optional] 
 **created_before** | **datetime**| The response includes orders created at or before this time. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: If you include &#x60;createdAfter&#x60; in the request, &#x60;createdBefore&#x60; is optional, and if provided must be equal to or after the &#x60;createdAfter&#x60; date and at least two minutes before the time of the request. If &#x60;createdBefore&#x60; is provided, neither &#x60;lastUpdatedAfter&#x60; nor &#x60;lastUpdatedBefore&#x60; may be provided. | [optional] 
 **last_updated_after** | **datetime**| The response includes orders updated at or after this time. An update is any change made by Amazon or the seller, including changes to order status. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: You must provide exactly one of &#x60;createdAfter&#x60; and &#x60;lastUpdatedAfter&#x60;. If &#x60;lastUpdatedAfter&#x60; is provided, neither &#x60;createdAfter&#x60; nor &#x60;createdBefore&#x60; may be provided. | [optional] 
 **last_updated_before** | **datetime**| The response includes orders updated at or before this time. An update is any change made by Amazon or the seller, including changes to order status. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: If you include &#x60;lastUpdatedAfter&#x60; in the request, &#x60;lastUpdatedBefore&#x60; is optional, and if provided must be equal to or after the &#x60;lastUpdatedAfter&#x60; date and at least two minutes before the time of the request. If &#x60;lastUpdatedBefore&#x60; is provided, neither &#x60;createdAfter&#x60; nor &#x60;createdBefore&#x60; may be provided. | [optional] 
 **fulfillment_statuses** | [**list[str]**](str.md)| A list of &#x60;FulfillmentStatus&#x60; values you can use to filter the results. | [optional] 
 **marketplace_ids** | [**list[str]**](str.md)| The response includes orders that were placed in marketplaces you include in this list.  Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) for a complete list of &#x60;marketplaceId&#x60; values. | [optional] 
 **fulfilled_by** | [**list[str]**](str.md)| The response includes orders that are fulfilled by the parties that you include in this list. | [optional] 
 **max_results_per_page** | **int**| The maximum number of orders that can be returned per page. The value must be between 1 and 100. **Default:** 100. | [optional] 
 **pagination_token** | **str**| Pagination occurs when a request produces a response that exceeds the &#x60;maxResultsPerPage&#x60;. This means that the response is divided into individual pages. To retrieve the next page, you must pass the &#x60;nextToken&#x60; value as the &#x60;paginationToken&#x60; query parameter in the next request. You will not receive a &#x60;nextToken&#x60; value on the last page. | [optional] 
 **included_data** | [**list[str]**](str.md)| A list of datasets to include in the response. | [optional] 

### Return type

[**SearchOrdersResponse**](SearchOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

