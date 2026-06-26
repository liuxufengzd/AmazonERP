# swagger_client.ListingsApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_listings_item**](ListingsApi.md#delete_listings_item) | **DELETE** /listings/2021-08-01/items/{sellerId}/{sku} | 
[**get_listings_item**](ListingsApi.md#get_listings_item) | **GET** /listings/2021-08-01/items/{sellerId}/{sku} | 
[**patch_listings_item**](ListingsApi.md#patch_listings_item) | **PATCH** /listings/2021-08-01/items/{sellerId}/{sku} | 
[**put_listings_item**](ListingsApi.md#put_listings_item) | **PUT** /listings/2021-08-01/items/{sellerId}/{sku} | 
[**search_listings_items**](ListingsApi.md#search_listings_items) | **GET** /listings/2021-08-01/items/{sellerId} | 


# **delete_listings_item**
> ListingsItemSubmissionResponse delete_listings_item(seller_id, sku, marketplace_ids, issue_locale=issue_locale)



Delete a listings item for a selling partner.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 5 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListingsApi()
seller_id = 'seller_id_example' # str | A selling partner identifier, such as a merchant account or vendor code.
sku = 'sku_example' # str | A selling partner provided identifier for an Amazon listing.
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers for the request.
issue_locale = 'en_US' # str | A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale. (optional)

try:
    api_response = api_instance.delete_listings_item(seller_id, sku, marketplace_ids, issue_locale=issue_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->delete_listings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| A selling partner identifier, such as a merchant account or vendor code. | 
 **sku** | **str**| A selling partner provided identifier for an Amazon listing. | 
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers for the request. | 
 **issue_locale** | **str**| A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: &#x60;en_US&#x60;, &#x60;fr_CA&#x60;, &#x60;fr_FR&#x60;. Localized messages default to &#x60;en_US&#x60; when a localization is not available in the specified locale. | [optional] 

### Return type

[**ListingsItemSubmissionResponse**](ListingsItemSubmissionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listings_item**
> Item get_listings_item(seller_id, sku, marketplace_ids, issue_locale=issue_locale, included_data=included_data)



Returns details about a listings item for a selling partner.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 10 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListingsApi()
seller_id = 'seller_id_example' # str | A selling partner identifier, such as a merchant account or vendor code.
sku = 'sku_example' # str | A selling partner provided identifier for an Amazon listing.
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers for the request.
issue_locale = 'en_US' # str | A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale. (optional)
included_data = ['[\"summaries\"]'] # list[str] | A comma-delimited list of data sets to include in the response. Default: `summaries`. (optional) (default to ["summaries"])

try:
    api_response = api_instance.get_listings_item(seller_id, sku, marketplace_ids, issue_locale=issue_locale, included_data=included_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->get_listings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| A selling partner identifier, such as a merchant account or vendor code. | 
 **sku** | **str**| A selling partner provided identifier for an Amazon listing. | 
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers for the request. | 
 **issue_locale** | **str**| A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: &#x60;en_US&#x60;, &#x60;fr_CA&#x60;, &#x60;fr_FR&#x60;. Localized messages default to &#x60;en_US&#x60; when a localization is not available in the specified locale. | [optional] 
 **included_data** | [**list[str]**](str.md)| A comma-delimited list of data sets to include in the response. Default: &#x60;summaries&#x60;. | [optional] [default to [&quot;summaries&quot;]]

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_listings_item**
> ListingsItemSubmissionResponse patch_listings_item(seller_id, sku, marketplace_ids, body, included_data=included_data, mode=mode, issue_locale=issue_locale)



Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 5 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListingsApi()
seller_id = 'seller_id_example' # str | A selling partner identifier, such as a merchant account or vendor code.
sku = 'sku_example' # str | A selling partner provided identifier for an Amazon listing.
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers for the request.
body = swagger_client.ListingsItemPatchRequest() # ListingsItemPatchRequest | The request body schema for the `patchListingsItem` operation.
included_data = ['[\"issues\"]'] # list[str] | A comma-delimited list of data sets to include in the response. Default: `issues`. (optional) (default to ["issues"])
mode = 'VALIDATION_PREVIEW' # str | The mode of operation for the request. (optional)
issue_locale = 'en_US' # str | A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale. (optional)

try:
    api_response = api_instance.patch_listings_item(seller_id, sku, marketplace_ids, body, included_data=included_data, mode=mode, issue_locale=issue_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->patch_listings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| A selling partner identifier, such as a merchant account or vendor code. | 
 **sku** | **str**| A selling partner provided identifier for an Amazon listing. | 
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers for the request. | 
 **body** | [**ListingsItemPatchRequest**](ListingsItemPatchRequest.md)| The request body schema for the &#x60;patchListingsItem&#x60; operation. | 
 **included_data** | [**list[str]**](str.md)| A comma-delimited list of data sets to include in the response. Default: &#x60;issues&#x60;. | [optional] [default to [&quot;issues&quot;]]
 **mode** | **str**| The mode of operation for the request. | [optional] 
 **issue_locale** | **str**| A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: &#x60;en_US&#x60;, &#x60;fr_CA&#x60;, &#x60;fr_FR&#x60;. Localized messages default to &#x60;en_US&#x60; when a localization is not available in the specified locale. | [optional] 

### Return type

[**ListingsItemSubmissionResponse**](ListingsItemSubmissionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_listings_item**
> ListingsItemSubmissionResponse put_listings_item(seller_id, sku, marketplace_ids, body, included_data=included_data, mode=mode, issue_locale=issue_locale)



Creates a new or fully-updates an existing listings item for a selling partner.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 10 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListingsApi()
seller_id = 'seller_id_example' # str | A selling partner identifier, such as a merchant account or vendor code.
sku = 'sku_example' # str | A selling partner provided identifier for an Amazon listing.
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers for the request.
body = swagger_client.ListingsItemPutRequest() # ListingsItemPutRequest | The request body schema for the `putListingsItem` operation.
included_data = ['[\"issues\"]'] # list[str] | A comma-delimited list of data sets to include in the response. Default: `issues`. (optional) (default to ["issues"])
mode = 'VALIDATION_PREVIEW' # str | The mode of operation for the request. (optional)
issue_locale = 'en_US' # str | A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale. (optional)

try:
    api_response = api_instance.put_listings_item(seller_id, sku, marketplace_ids, body, included_data=included_data, mode=mode, issue_locale=issue_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->put_listings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| A selling partner identifier, such as a merchant account or vendor code. | 
 **sku** | **str**| A selling partner provided identifier for an Amazon listing. | 
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers for the request. | 
 **body** | [**ListingsItemPutRequest**](ListingsItemPutRequest.md)| The request body schema for the &#x60;putListingsItem&#x60; operation. | 
 **included_data** | [**list[str]**](str.md)| A comma-delimited list of data sets to include in the response. Default: &#x60;issues&#x60;. | [optional] [default to [&quot;issues&quot;]]
 **mode** | **str**| The mode of operation for the request. | [optional] 
 **issue_locale** | **str**| A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: &#x60;en_US&#x60;, &#x60;fr_CA&#x60;, &#x60;fr_FR&#x60;. Localized messages default to &#x60;en_US&#x60; when a localization is not available in the specified locale. | [optional] 

### Return type

[**ListingsItemSubmissionResponse**](ListingsItemSubmissionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_listings_items**
> ItemSearchResults search_listings_items(seller_id, marketplace_ids, issue_locale=issue_locale, included_data=included_data, identifiers=identifiers, identifiers_type=identifiers_type, variation_parent_sku=variation_parent_sku, package_hierarchy_sku=package_hierarchy_sku, created_after=created_after, created_before=created_before, last_updated_after=last_updated_after, last_updated_before=last_updated_before, with_issue_severity=with_issue_severity, with_status=with_status, without_status=without_status, sort_by=sort_by, sort_order=sort_order, page_size=page_size, page_token=page_token)



Search for and return a list of selling partner listings items and their respective details.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 5 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListingsApi()
seller_id = 'seller_id_example' # str | A selling partner identifier, such as a merchant account or vendor code.
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers for the request.
issue_locale = 'en_US' # str | A locale that is used to localize issues. When not provided, the default language code of the first marketplace is used. Examples: \"en_US\", \"fr_CA\", \"fr_FR\". When a localization is not available in the specified locale, localized messages default to \"en_US\". (optional)
included_data = ['[\"summaries\"]'] # list[str] | A comma-delimited list of datasets that you want to include in the response. Default: `summaries`. (optional) (default to ["summaries"])
identifiers = ['GM-ZDPI-9B4E'] # list[str] | A comma-delimited list of product identifiers that you can use to search for listings items.   **Note**:  1. This is required when you specify `identifiersType`. 2. You cannot use 'identifiers' if you specify `variationParentSku` or `packageHierarchySku`. (optional)
identifiers_type = 'SKU' # str | A type of product identifiers that you can use to search for listings items.   **Note**:  This is required when `identifiers` is provided. (optional)
variation_parent_sku = 'GM-ZDPI-9B4E' # str | Filters results to include listing items that are variation children of the specified SKU.   **Note**: You cannot use `variationParentSku` if you include `identifiers` or `packageHierarchySku` in your request. (optional)
package_hierarchy_sku = 'GM-ZDPI-9B4E' # str | Filter results to include listing items that contain or are contained by the specified SKU.   **Note**: You cannot use `packageHierarchySku` if you include `identifiers` or `variationParentSku` in your request. (optional)
created_after = '2024-03-01T01:30:00.000Z' # datetime | A date-time that is used to filter listing items. The response includes listings items that were created at or after this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. (optional)
created_before = '2024-03-31T21:45:00.000Z' # datetime | A date-time that is used to filter listing items. The response includes listings items that were created at or before this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. (optional)
last_updated_after = '2024-05-05T23:45:00.000Z' # datetime | A date-time that is used to filter listing items. The response includes listings items that were last updated at or after this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. (optional)
last_updated_before = '2024-05-01T01:15:00.000Z' # datetime | A date-time that is used to filter listing items. The response includes listings items that were last updated at or before this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. (optional)
with_issue_severity = ['WARNING'] # list[str] | Filter results to include only listing items that have issues that match one or more of the specified severity levels. (optional)
with_status = ['DISCOVERABLE'] # list[str] | Filter results to include only listing items that have the specified status. (optional)
without_status = ['BUYABLE'] # list[str] | Filter results to include only listing items that don't contain the specified statuses. (optional)
sort_by = 'lastUpdatedDate' # str | An attribute by which to sort the returned listing items. (optional) (default to lastUpdatedDate)
sort_order = 'DESC' # str | The order in which to sort the result items. (optional) (default to DESC)
page_size = 10 # int | The number of results that you want to include on each page. (optional) (default to 10)
page_token = 'sdlkj234lkj234lksjdflkjwdflkjsfdlkj234234234234' # str | A token that you can use to fetch a specific page when there are multiple pages of results. (optional)

try:
    api_response = api_instance.search_listings_items(seller_id, marketplace_ids, issue_locale=issue_locale, included_data=included_data, identifiers=identifiers, identifiers_type=identifiers_type, variation_parent_sku=variation_parent_sku, package_hierarchy_sku=package_hierarchy_sku, created_after=created_after, created_before=created_before, last_updated_after=last_updated_after, last_updated_before=last_updated_before, with_issue_severity=with_issue_severity, with_status=with_status, without_status=without_status, sort_by=sort_by, sort_order=sort_order, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->search_listings_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| A selling partner identifier, such as a merchant account or vendor code. | 
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers for the request. | 
 **issue_locale** | **str**| A locale that is used to localize issues. When not provided, the default language code of the first marketplace is used. Examples: \&quot;en_US\&quot;, \&quot;fr_CA\&quot;, \&quot;fr_FR\&quot;. When a localization is not available in the specified locale, localized messages default to \&quot;en_US\&quot;. | [optional] 
 **included_data** | [**list[str]**](str.md)| A comma-delimited list of datasets that you want to include in the response. Default: &#x60;summaries&#x60;. | [optional] [default to [&quot;summaries&quot;]]
 **identifiers** | [**list[str]**](str.md)| A comma-delimited list of product identifiers that you can use to search for listings items.   **Note**:  1. This is required when you specify &#x60;identifiersType&#x60;. 2. You cannot use &#39;identifiers&#39; if you specify &#x60;variationParentSku&#x60; or &#x60;packageHierarchySku&#x60;. | [optional] 
 **identifiers_type** | **str**| A type of product identifiers that you can use to search for listings items.   **Note**:  This is required when &#x60;identifiers&#x60; is provided. | [optional] 
 **variation_parent_sku** | **str**| Filters results to include listing items that are variation children of the specified SKU.   **Note**: You cannot use &#x60;variationParentSku&#x60; if you include &#x60;identifiers&#x60; or &#x60;packageHierarchySku&#x60; in your request. | [optional] 
 **package_hierarchy_sku** | **str**| Filter results to include listing items that contain or are contained by the specified SKU.   **Note**: You cannot use &#x60;packageHierarchySku&#x60; if you include &#x60;identifiers&#x60; or &#x60;variationParentSku&#x60; in your request. | [optional] 
 **created_after** | **datetime**| A date-time that is used to filter listing items. The response includes listings items that were created at or after this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. | [optional] 
 **created_before** | **datetime**| A date-time that is used to filter listing items. The response includes listings items that were created at or before this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. | [optional] 
 **last_updated_after** | **datetime**| A date-time that is used to filter listing items. The response includes listings items that were last updated at or after this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. | [optional] 
 **last_updated_before** | **datetime**| A date-time that is used to filter listing items. The response includes listings items that were last updated at or before this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. | [optional] 
 **with_issue_severity** | [**list[str]**](str.md)| Filter results to include only listing items that have issues that match one or more of the specified severity levels. | [optional] 
 **with_status** | [**list[str]**](str.md)| Filter results to include only listing items that have the specified status. | [optional] 
 **without_status** | [**list[str]**](str.md)| Filter results to include only listing items that don&#39;t contain the specified statuses. | [optional] 
 **sort_by** | **str**| An attribute by which to sort the returned listing items. | [optional] [default to lastUpdatedDate]
 **sort_order** | **str**| The order in which to sort the result items. | [optional] [default to DESC]
 **page_size** | **int**| The number of results that you want to include on each page. | [optional] [default to 10]
 **page_token** | **str**| A token that you can use to fetch a specific page when there are multiple pages of results. | [optional] 

### Return type

[**ItemSearchResults**](ItemSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

