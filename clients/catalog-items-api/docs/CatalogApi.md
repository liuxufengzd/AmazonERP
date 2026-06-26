# swagger_client.CatalogApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_item**](CatalogApi.md#get_catalog_item) | **GET** /catalog/2022-04-01/items/{asin} | 
[**search_catalog_items**](CatalogApi.md#search_catalog_items) | **GET** /catalog/2022-04-01/items | 


# **get_catalog_item**
> Item get_catalog_item(asin, marketplace_ids, included_data=included_data, locale=locale)



Retrieves details for an item in the Amazon catalog.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header contains the usage plan rate limits for the operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
asin = 'asin_example' # str | The Amazon Standard Identification Number (ASIN) of the item.
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
included_data = ['[\"summaries\"]'] # list[str] | A comma-delimited list of datasets to include in the response. (optional) (default to ["summaries"])
locale = 'en_US' # str | The locale for which you want to retrieve localized summaries. Defaults to the primary locale of the marketplace. (optional)

try:
    api_response = api_instance.get_catalog_item(asin, marketplace_ids, included_data=included_data, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| The Amazon Standard Identification Number (ASIN) of the item. | 
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
 **included_data** | [**list[str]**](str.md)| A comma-delimited list of datasets to include in the response. | [optional] [default to [&quot;summaries&quot;]]
 **locale** | **str**| The locale for which you want to retrieve localized summaries. Defaults to the primary locale of the marketplace. | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_catalog_items**
> ItemSearchResults search_catalog_items(marketplace_ids, identifiers=identifiers, identifiers_type=identifiers_type, included_data=included_data, locale=locale, seller_id=seller_id, keywords=keywords, brand_names=brand_names, classification_ids=classification_ids, page_size=page_size, page_token=page_token, keywords_locale=keywords_locale)



Search for a list of Amazon catalog items and item-related information. You can search by identifier or by keywords.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header contains the usage plan rate limits for the operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
identifiers = ['shoes'] # list[str] | A comma-delimited list of product identifiers that you can use to search the Amazon catalog. **Note:** You cannot include `identifiers` and `keywords` in the same request. (optional)
identifiers_type = 'ASIN' # str | The type of product identifiers that you can use to search the Amazon catalog. **Note:** `identifiersType` is required when `identifiers` is in the request. (optional)
included_data = ['[\"summaries\"]'] # list[str] | A comma-delimited list of datasets to include in the response. (optional) (default to ["summaries"])
locale = 'en_US' # str | The locale for which you want to retrieve localized summaries. Defaults to the primary locale of the marketplace. (optional)
seller_id = 'seller_id_example' # str | A selling partner identifier, such as a seller account or vendor code. **Note:** Required when `identifiersType` is `SKU`. (optional)
keywords = ['shoes'] # list[str] | A comma-delimited list of keywords that you can use to search the Amazon catalog. **Note:** You cannot include `keywords` and `identifiers` in the same request. (optional)
brand_names = ['Beautiful Boats'] # list[str] | A comma-delimited list of brand names that you can use to limit the search in queries based on `keywords`. **Note:** Cannot be used with `identifiers`. (optional)
classification_ids = ['12345678'] # list[str] | A comma-delimited list of classification identifiers that you can use to limit the search in queries based on `keywords`. **Note:** Cannot be used with `identifiers`. (optional)
page_size = 10 # int | The number of results to include on each page. (optional) (default to 10)
page_token = 'sdlkj234lkj234lksjdflkjwdflkjsfdlkj234234234234' # str | A token that you can use to fetch a specific page when there are multiple pages of results. (optional)
keywords_locale = 'en_US' # str | The language of the keywords that are included in queries based on `keywords`. Defaults to the primary locale of the marketplace. **Note:** Cannot be used with `identifiers`. (optional)

try:
    api_response = api_instance.search_catalog_items(marketplace_ids, identifiers=identifiers, identifiers_type=identifiers_type, included_data=included_data, locale=locale, seller_id=seller_id, keywords=keywords, brand_names=brand_names, classification_ids=classification_ids, page_size=page_size, page_token=page_token, keywords_locale=keywords_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->search_catalog_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
 **identifiers** | [**list[str]**](str.md)| A comma-delimited list of product identifiers that you can use to search the Amazon catalog. **Note:** You cannot include &#x60;identifiers&#x60; and &#x60;keywords&#x60; in the same request. | [optional] 
 **identifiers_type** | **str**| The type of product identifiers that you can use to search the Amazon catalog. **Note:** &#x60;identifiersType&#x60; is required when &#x60;identifiers&#x60; is in the request. | [optional] 
 **included_data** | [**list[str]**](str.md)| A comma-delimited list of datasets to include in the response. | [optional] [default to [&quot;summaries&quot;]]
 **locale** | **str**| The locale for which you want to retrieve localized summaries. Defaults to the primary locale of the marketplace. | [optional] 
 **seller_id** | **str**| A selling partner identifier, such as a seller account or vendor code. **Note:** Required when &#x60;identifiersType&#x60; is &#x60;SKU&#x60;. | [optional] 
 **keywords** | [**list[str]**](str.md)| A comma-delimited list of keywords that you can use to search the Amazon catalog. **Note:** You cannot include &#x60;keywords&#x60; and &#x60;identifiers&#x60; in the same request. | [optional] 
 **brand_names** | [**list[str]**](str.md)| A comma-delimited list of brand names that you can use to limit the search in queries based on &#x60;keywords&#x60;. **Note:** Cannot be used with &#x60;identifiers&#x60;. | [optional] 
 **classification_ids** | [**list[str]**](str.md)| A comma-delimited list of classification identifiers that you can use to limit the search in queries based on &#x60;keywords&#x60;. **Note:** Cannot be used with &#x60;identifiers&#x60;. | [optional] 
 **page_size** | **int**| The number of results to include on each page. | [optional] [default to 10]
 **page_token** | **str**| A token that you can use to fetch a specific page when there are multiple pages of results. | [optional] 
 **keywords_locale** | **str**| The language of the keywords that are included in queries based on &#x60;keywords&#x60;. Defaults to the primary locale of the marketplace. **Note:** Cannot be used with &#x60;identifiers&#x60;. | [optional] 

### Return type

[**ItemSearchResults**](ItemSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

