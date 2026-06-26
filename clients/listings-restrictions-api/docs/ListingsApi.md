# swagger_client.ListingsApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_listings_restrictions**](ListingsApi.md#get_listings_restrictions) | **GET** /listings/2021-08-01/restrictions | 


# **get_listings_restrictions**
> RestrictionList get_listings_restrictions(asin, seller_id, marketplace_ids, condition_type=condition_type, reason_locale=reason_locale, product_type=product_type)



Returns listing restrictions for an item in the Amazon Catalog.   **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 10 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListingsApi()
asin = 'B0000ASIN1' # str | The Amazon Standard Identification Number (ASIN) of the item.
seller_id = 'seller_id_example' # str | A selling partner identifier, such as a merchant account.
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers for the request.
condition_type = 'used_very_good' # str | The condition used to filter restrictions. (optional)
reason_locale = 'en_US' # str | A locale for reason text localization. When not provided, the default language code of the first marketplace is used. Examples: \"en_US\", \"fr_CA\", \"fr_FR\". Localized messages default to \"en_US\" when a localization is not available in the specified locale. (optional)
product_type = 'SHIRT' # str | The product type of the item. When provided with the brand name, the API evaluates GTIN exemption restrictions in addition to brand restrictions for the specified product type. (optional)

try:
    api_response = api_instance.get_listings_restrictions(asin, seller_id, marketplace_ids, condition_type=condition_type, reason_locale=reason_locale, product_type=product_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->get_listings_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| The Amazon Standard Identification Number (ASIN) of the item. | 
 **seller_id** | **str**| A selling partner identifier, such as a merchant account. | 
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers for the request. | 
 **condition_type** | **str**| The condition used to filter restrictions. | [optional] 
 **reason_locale** | **str**| A locale for reason text localization. When not provided, the default language code of the first marketplace is used. Examples: \&quot;en_US\&quot;, \&quot;fr_CA\&quot;, \&quot;fr_FR\&quot;. Localized messages default to \&quot;en_US\&quot; when a localization is not available in the specified locale. | [optional] 
 **product_type** | **str**| The product type of the item. When provided with the brand name, the API evaluates GTIN exemption restrictions in addition to brand restrictions for the specified product type. | [optional] 

### Return type

[**RestrictionList**](RestrictionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

