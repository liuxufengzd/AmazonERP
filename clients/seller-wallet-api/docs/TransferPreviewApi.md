# swagger_client.TransferPreviewApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfer_preview**](TransferPreviewApi.md#get_transfer_preview) | **GET** /finances/transfers/wallet/2024-03-01/transferPreview | Fetch potential fees that could be applied on a transaction on the basis of the source and destination country currency code


# **get_transfer_preview**
> TransferRatePreview get_transfer_preview(source_country_code, source_currency_code, destination_country_code, destination_currency_code, base_amount, marketplace_id)

Fetch potential fees that could be applied on a transaction on the basis of the source and destination country currency code

Retrieve a list of potential fees on a transaction.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransferPreviewApi()
source_country_code = 'US' # str | Country code of the source transaction account in ISO 3166 format.
source_currency_code = 'USD' # str | Currency code of the source transaction country in ISO 4217 format.
destination_country_code = 'FR' # str | Country code of the destination transaction account in ISO 3166 format.
destination_currency_code = 'EUR' # str | Currency code of the destination transaction country in ISO 4217 format.
base_amount = 1000.0 # float | The base transaction amount without any markup fees.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Fetch potential fees that could be applied on a transaction on the basis of the source and destination country currency code
    api_response = api_instance.get_transfer_preview(source_country_code, source_currency_code, destination_country_code, destination_currency_code, base_amount, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferPreviewApi->get_transfer_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_country_code** | **str**| Country code of the source transaction account in ISO 3166 format. | 
 **source_currency_code** | **str**| Currency code of the source transaction country in ISO 4217 format. | 
 **destination_country_code** | **str**| Country code of the destination transaction account in ISO 3166 format. | 
 **destination_currency_code** | **str**| Currency code of the destination transaction country in ISO 4217 format. | 
 **base_amount** | **float**| The base transaction amount without any markup fees. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**TransferRatePreview**](TransferRatePreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

