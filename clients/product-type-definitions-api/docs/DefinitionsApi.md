# swagger_client.DefinitionsApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_definitions_product_type**](DefinitionsApi.md#get_definitions_product_type) | **GET** /definitions/2020-09-01/productTypes/{productType} | 
[**search_definitions_product_types**](DefinitionsApi.md#search_definitions_product_types) | **GET** /definitions/2020-09-01/productTypes | 


# **get_definitions_product_type**
> ProductTypeDefinition get_definitions_product_type(product_type, marketplace_ids, seller_id=seller_id, product_type_version=product_type_version, requirements=requirements, requirements_enforced=requirements_enforced, locale=locale, parentage_level=parentage_level)



Retrieve an Amazon product type definition.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 5 | 10 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefinitionsApi()
product_type = 'LUGGAGE' # str | The Amazon product type name.
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers for the request. Note: This parameter is limited to one marketplaceId at this time.
seller_id = 'seller_id_example' # str | A selling partner identifier. When provided, seller-specific requirements and values are populated within the product type definition schema, such as brand names associated with the selling partner. (optional)
product_type_version = 'LATEST' # str | The version of the Amazon product type to retrieve. Defaults to \"LATEST\". Prerelease versions of product type definitions may be retrieved with \"RELEASE_CANDIDATE\". If no prerelease version is currently available, the \"LATEST\" live version will be provided. (optional) (default to LATEST)
requirements = 'LISTING' # str | The name of the requirements set to retrieve requirements for. (optional) (default to LISTING)
requirements_enforced = 'ENFORCED' # str | Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all the required attributes being present (such as for partial updates). (optional) (default to ENFORCED)
locale = 'DEFAULT' # str | Locale for retrieving display labels and other presentation details. Defaults to the default language of the first marketplace in the request. (optional) (default to DEFAULT)
parentage_level = 'CHILD' # str | The parentage level of the listing to retrieve a schema for. When provided, the schema is simplified by resolving all conditional logic related to the specified parentage level, resulting in a smaller schema with fewer conditions. (optional)

try:
    api_response = api_instance.get_definitions_product_type(product_type, marketplace_ids, seller_id=seller_id, product_type_version=product_type_version, requirements=requirements, requirements_enforced=requirements_enforced, locale=locale, parentage_level=parentage_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefinitionsApi->get_definitions_product_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | **str**| The Amazon product type name. | 
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers for the request. Note: This parameter is limited to one marketplaceId at this time. | 
 **seller_id** | **str**| A selling partner identifier. When provided, seller-specific requirements and values are populated within the product type definition schema, such as brand names associated with the selling partner. | [optional] 
 **product_type_version** | **str**| The version of the Amazon product type to retrieve. Defaults to \&quot;LATEST\&quot;. Prerelease versions of product type definitions may be retrieved with \&quot;RELEASE_CANDIDATE\&quot;. If no prerelease version is currently available, the \&quot;LATEST\&quot; live version will be provided. | [optional] [default to LATEST]
 **requirements** | **str**| The name of the requirements set to retrieve requirements for. | [optional] [default to LISTING]
 **requirements_enforced** | **str**| Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all the required attributes being present (such as for partial updates). | [optional] [default to ENFORCED]
 **locale** | **str**| Locale for retrieving display labels and other presentation details. Defaults to the default language of the first marketplace in the request. | [optional] [default to DEFAULT]
 **parentage_level** | **str**| The parentage level of the listing to retrieve a schema for. When provided, the schema is simplified by resolving all conditional logic related to the specified parentage level, resulting in a smaller schema with fewer conditions. | [optional] 

### Return type

[**ProductTypeDefinition**](ProductTypeDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_definitions_product_types**
> ProductTypeList search_definitions_product_types(marketplace_ids, keywords=keywords, item_name=item_name, locale=locale, search_locale=search_locale)



Search for and return a list of Amazon product types that have definitions available.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 5 | 10 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefinitionsApi()
marketplace_ids = ['ATVPDKIKX0DER'] # list[str] | A comma-delimited list of Amazon marketplace identifiers for the request.
keywords = ['LUGGAGE'] # list[str] | A comma-delimited list of keywords to search product types. **Note:** Cannot be used with `itemName`. (optional)
item_name = 'Running shoes' # str | Title of ASIN to get product type recommendation. **Note:** Cannot be used with `keywords`. (optional)
locale = 'en_US' # str | Locale for display names in response. Defaults to primary locale of the marketplace. (optional)
search_locale = 'en_US' # str | Language used for `keywords` or `itemName` parameters. Defaults to primary locale of the marketplace. (optional)

try:
    api_response = api_instance.search_definitions_product_types(marketplace_ids, keywords=keywords, item_name=item_name, locale=locale, search_locale=search_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefinitionsApi->search_definitions_product_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_ids** | [**list[str]**](str.md)| A comma-delimited list of Amazon marketplace identifiers for the request. | 
 **keywords** | [**list[str]**](str.md)| A comma-delimited list of keywords to search product types. **Note:** Cannot be used with &#x60;itemName&#x60;. | [optional] 
 **item_name** | **str**| Title of ASIN to get product type recommendation. **Note:** Cannot be used with &#x60;keywords&#x60;. | [optional] 
 **locale** | **str**| Locale for display names in response. Defaults to primary locale of the marketplace. | [optional] 
 **search_locale** | **str**| Language used for &#x60;keywords&#x60; or &#x60;itemName&#x60; parameters. Defaults to primary locale of the marketplace. | [optional] 

### Return type

[**ProductTypeList**](ProductTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

