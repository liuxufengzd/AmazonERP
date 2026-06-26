# swagger_client.FbaOutboundApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_fulfillment_order**](FbaOutboundApi.md#cancel_fulfillment_order) | **PUT** /fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel | 
[**create_fulfillment_order**](FbaOutboundApi.md#create_fulfillment_order) | **POST** /fba/outbound/2020-07-01/fulfillmentOrders | 
[**create_fulfillment_return**](FbaOutboundApi.md#create_fulfillment_return) | **PUT** /fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/return | 
[**delivery_offers**](FbaOutboundApi.md#delivery_offers) | **POST** /fba/outbound/2020-07-01/deliveryOffers | 
[**get_feature_inventory**](FbaOutboundApi.md#get_feature_inventory) | **GET** /fba/outbound/2020-07-01/features/inventory/{featureName} | 
[**get_feature_sku**](FbaOutboundApi.md#get_feature_sku) | **GET** /fba/outbound/2020-07-01/features/inventory/{featureName}/{sellerSku} | 
[**get_features**](FbaOutboundApi.md#get_features) | **GET** /fba/outbound/2020-07-01/features | 
[**get_fulfillment_order**](FbaOutboundApi.md#get_fulfillment_order) | **GET** /fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId} | 
[**get_fulfillment_preview**](FbaOutboundApi.md#get_fulfillment_preview) | **POST** /fba/outbound/2020-07-01/fulfillmentOrders/preview | 
[**get_package_tracking_details**](FbaOutboundApi.md#get_package_tracking_details) | **GET** /fba/outbound/2020-07-01/tracking | 
[**list_all_fulfillment_orders**](FbaOutboundApi.md#list_all_fulfillment_orders) | **GET** /fba/outbound/2020-07-01/fulfillmentOrders | 
[**list_return_reason_codes**](FbaOutboundApi.md#list_return_reason_codes) | **GET** /fba/outbound/2020-07-01/returnReasonCodes | 
[**submit_fulfillment_order_status_update**](FbaOutboundApi.md#submit_fulfillment_order_status_update) | **PUT** /fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/status | 
[**update_fulfillment_order**](FbaOutboundApi.md#update_fulfillment_order) | **PUT** /fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId} | 


# **cancel_fulfillment_order**
> CancelFulfillmentOrderResponse cancel_fulfillment_order(seller_fulfillment_order_id)



Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified order identifier.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
seller_fulfillment_order_id = 'seller_fulfillment_order_id_example' # str | The identifier assigned to the item by the seller when the fulfillment order was created.

try:
    api_response = api_instance.cancel_fulfillment_order(seller_fulfillment_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->cancel_fulfillment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_fulfillment_order_id** | **str**| The identifier assigned to the item by the seller when the fulfillment order was created. | 

### Return type

[**CancelFulfillmentOrderResponse**](CancelFulfillmentOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fulfillment_order**
> CreateFulfillmentOrderResponse create_fulfillment_order(body)



Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
body = swagger_client.CreateFulfillmentOrderRequest() # CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequest parameter

try:
    api_response = api_instance.create_fulfillment_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->create_fulfillment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFulfillmentOrderRequest**](CreateFulfillmentOrderRequest.md)| CreateFulfillmentOrderRequest parameter | 

### Return type

[**CreateFulfillmentOrderResponse**](CreateFulfillmentOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fulfillment_return**
> CreateFulfillmentReturnResponse create_fulfillment_return(body, seller_fulfillment_order_id)



Creates a fulfillment return.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
body = swagger_client.CreateFulfillmentReturnRequest() # CreateFulfillmentReturnRequest | The request body of the `createFulfillmentReturn` operation.
seller_fulfillment_order_id = 'seller_fulfillment_order_id_example' # str | An identifier the seller assigns to the fulfillment order at the time it was created. The seller uses their own records to find the correct `sellerFulfillmentOrderId` value based on the buyer's request to return items.

try:
    api_response = api_instance.create_fulfillment_return(body, seller_fulfillment_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->create_fulfillment_return: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFulfillmentReturnRequest**](CreateFulfillmentReturnRequest.md)| The request body of the &#x60;createFulfillmentReturn&#x60; operation. | 
 **seller_fulfillment_order_id** | **str**| An identifier the seller assigns to the fulfillment order at the time it was created. The seller uses their own records to find the correct &#x60;sellerFulfillmentOrderId&#x60; value based on the buyer&#39;s request to return items. | 

### Return type

[**CreateFulfillmentReturnResponse**](CreateFulfillmentReturnResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delivery_offers**
> GetDeliveryOffersResponse delivery_offers(body)



Returns delivery options that include an estimated delivery date and offer expiration, based on criteria that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
body = swagger_client.GetDeliveryOffersRequest() # GetDeliveryOffersRequest | GetDeliveryOffersRequest parameter

try:
    api_response = api_instance.delivery_offers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->delivery_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetDeliveryOffersRequest**](GetDeliveryOffersRequest.md)| GetDeliveryOffersRequest parameter | 

### Return type

[**GetDeliveryOffersResponse**](GetDeliveryOffersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_inventory**
> GetFeatureInventoryResponse get_feature_inventory(marketplace_id, feature_name, next_token=next_token, query_start_date=query_start_date)



Returns a list of inventory items that are eligible for the fulfillment feature you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
marketplace_id = 'marketplace_id_example' # str | The marketplace for which to return a list of the inventory that is eligible for the specified feature.
feature_name = 'feature_name_example' # str | The name of the feature for which to return a list of eligible inventory.
next_token = 'next_token_example' # str | A string token returned in the response to your previous request that is used to return the next response page. A value of `null` will return the first page. (optional)
query_start_date = '2013-10-20T19:20:30+01:00' # datetime | A date that you can use to select inventory that has been updated since a specified date. An update is defined as any change in feature-enabled inventory availability. The date must be in the format `yyyy-MM-ddTHH:mm:ss.sssZ` (optional)

try:
    api_response = api_instance.get_feature_inventory(marketplace_id, feature_name, next_token=next_token, query_start_date=query_start_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_feature_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The marketplace for which to return a list of the inventory that is eligible for the specified feature. | 
 **feature_name** | **str**| The name of the feature for which to return a list of eligible inventory. | 
 **next_token** | **str**| A string token returned in the response to your previous request that is used to return the next response page. A value of &#x60;null&#x60; will return the first page. | [optional] 
 **query_start_date** | **datetime**| A date that you can use to select inventory that has been updated since a specified date. An update is defined as any change in feature-enabled inventory availability. The date must be in the format &#x60;yyyy-MM-ddTHH:mm:ss.sssZ&#x60; | [optional] 

### Return type

[**GetFeatureInventoryResponse**](GetFeatureInventoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_sku**
> GetFeatureSkuResponse get_feature_sku(marketplace_id, feature_name, seller_sku)



Returns the number of items with the `sellerSku` you specify that can have orders fulfilled using the specified feature. Note that if the `sellerSku` isn't eligible, the response will contain an empty `skuInfo` object. The parameters for this operation may contain special characters that require URL encoding. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
marketplace_id = 'marketplace_id_example' # str | The marketplace for which to return the count.
feature_name = 'feature_name_example' # str | The name of the feature.
seller_sku = 'seller_sku_example' # str | Used to identify an item in the given marketplace. `sellerSku` is qualified by the seller's `sellerId`, which is included with every operation that you submit.

try:
    api_response = api_instance.get_feature_sku(marketplace_id, feature_name, seller_sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_feature_sku: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The marketplace for which to return the count. | 
 **feature_name** | **str**| The name of the feature. | 
 **seller_sku** | **str**| Used to identify an item in the given marketplace. &#x60;sellerSku&#x60; is qualified by the seller&#39;s &#x60;sellerId&#x60;, which is included with every operation that you submit. | 

### Return type

[**GetFeatureSkuResponse**](GetFeatureSkuResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_features**
> GetFeaturesResponse get_features(marketplace_id)



Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you specify, and whether the seller for which you made the call is enrolled for each feature.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
marketplace_id = 'marketplace_id_example' # str | The marketplace for which to return the list of features.

try:
    api_response = api_instance.get_features(marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The marketplace for which to return the list of features. | 

### Return type

[**GetFeaturesResponse**](GetFeaturesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_order**
> GetFulfillmentOrderResponse get_fulfillment_order(seller_fulfillment_order_id)



Returns the fulfillment order indicated by the specified order identifier.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
seller_fulfillment_order_id = 'seller_fulfillment_order_id_example' # str | The identifier assigned to the item by the seller when the fulfillment order was created.

try:
    api_response = api_instance.get_fulfillment_order(seller_fulfillment_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_fulfillment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_fulfillment_order_id** | **str**| The identifier assigned to the item by the seller when the fulfillment order was created. | 

### Return type

[**GetFulfillmentOrderResponse**](GetFulfillmentOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_preview**
> GetFulfillmentPreviewResponse get_fulfillment_preview(body)



Returns a list of fulfillment order previews based on shipping criteria that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
body = swagger_client.GetFulfillmentPreviewRequest() # GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequest parameter

try:
    api_response = api_instance.get_fulfillment_preview(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_fulfillment_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFulfillmentPreviewRequest**](GetFulfillmentPreviewRequest.md)| GetFulfillmentPreviewRequest parameter | 

### Return type

[**GetFulfillmentPreviewResponse**](GetFulfillmentPreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_tracking_details**
> GetPackageTrackingDetailsResponse get_package_tracking_details(package_number)



Returns delivery tracking information for a package in an outbound shipment for a Multi-Channel Fulfillment order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
package_number = 56 # int | The unencrypted package identifier. You can obtain this value from the `getFulfillmentOrder` operation.

try:
    api_response = api_instance.get_package_tracking_details(package_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_package_tracking_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_number** | **int**| The unencrypted package identifier. You can obtain this value from the &#x60;getFulfillmentOrder&#x60; operation. | 

### Return type

[**GetPackageTrackingDetailsResponse**](GetPackageTrackingDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_fulfillment_orders**
> ListAllFulfillmentOrdersResponse list_all_fulfillment_orders(query_start_date=query_start_date, next_token=next_token)



Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by the `nextToken` parameter.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
query_start_date = '2013-10-20T19:20:30+01:00' # datetime | A date used to select fulfillment orders that were last updated after (or at) a specified time. An update is defined as any change in fulfillment order status, including the creation of a new fulfillment order. (optional)
next_token = 'next_token_example' # str | A string token returned in the response to your previous request. (optional)

try:
    api_response = api_instance.list_all_fulfillment_orders(query_start_date=query_start_date, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->list_all_fulfillment_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_start_date** | **datetime**| A date used to select fulfillment orders that were last updated after (or at) a specified time. An update is defined as any change in fulfillment order status, including the creation of a new fulfillment order. | [optional] 
 **next_token** | **str**| A string token returned in the response to your previous request. | [optional] 

### Return type

[**ListAllFulfillmentOrdersResponse**](ListAllFulfillmentOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_return_reason_codes**
> ListReturnReasonCodesResponse list_return_reason_codes(seller_sku, marketplace_id=marketplace_id, seller_fulfillment_order_id=seller_fulfillment_order_id, language=language)



Returns a list of return reason codes for a seller SKU in a given marketplace. The parameters for this operation may contain special characters that require URL encoding. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
seller_sku = 'seller_sku_example' # str | The seller SKU for which return reason codes are required.
marketplace_id = 'marketplace_id_example' # str | The marketplace for which the seller wants return reason codes. (optional)
seller_fulfillment_order_id = 'seller_fulfillment_order_id_example' # str | The identifier assigned to the item by the seller when the fulfillment order was created. The service uses this value to determine the marketplace for which the seller wants return reason codes. (optional)
language = 'language_example' # str | The language that the `TranslatedDescription` property of the `ReasonCodeDetails` response object should be translated into. (optional)

try:
    api_response = api_instance.list_return_reason_codes(seller_sku, marketplace_id=marketplace_id, seller_fulfillment_order_id=seller_fulfillment_order_id, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->list_return_reason_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_sku** | **str**| The seller SKU for which return reason codes are required. | 
 **marketplace_id** | **str**| The marketplace for which the seller wants return reason codes. | [optional] 
 **seller_fulfillment_order_id** | **str**| The identifier assigned to the item by the seller when the fulfillment order was created. The service uses this value to determine the marketplace for which the seller wants return reason codes. | [optional] 
 **language** | **str**| The language that the &#x60;TranslatedDescription&#x60; property of the &#x60;ReasonCodeDetails&#x60; response object should be translated into. | [optional] 

### Return type

[**ListReturnReasonCodesResponse**](ListReturnReasonCodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_fulfillment_order_status_update**
> SubmitFulfillmentOrderStatusUpdateResponse submit_fulfillment_order_status_update(seller_fulfillment_order_id, body)



Requests that Amazon update the status of an order in the sandbox testing environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Fulfillment Outbound Dynamic Sandbox Guide](https://developer-docs.amazon.com/sp-api/docs/fulfillment-outbound-dynamic-sandbox-guide) and [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
seller_fulfillment_order_id = 'seller_fulfillment_order_id_example' # str | The identifier assigned to the item by the seller when the fulfillment order was created.
body = swagger_client.SubmitFulfillmentOrderStatusUpdateRequest() # SubmitFulfillmentOrderStatusUpdateRequest | The identifier assigned to the item by the seller when the fulfillment order was created.

try:
    api_response = api_instance.submit_fulfillment_order_status_update(seller_fulfillment_order_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->submit_fulfillment_order_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_fulfillment_order_id** | **str**| The identifier assigned to the item by the seller when the fulfillment order was created. | 
 **body** | [**SubmitFulfillmentOrderStatusUpdateRequest**](SubmitFulfillmentOrderStatusUpdateRequest.md)| The identifier assigned to the item by the seller when the fulfillment order was created. | 

### Return type

[**SubmitFulfillmentOrderStatusUpdateResponse**](SubmitFulfillmentOrderStatusUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fulfillment_order**
> UpdateFulfillmentOrderResponse update_fulfillment_order(body, seller_fulfillment_order_id)



Updates and/or requests shipment for a fulfillment order with an order hold on it.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaOutboundApi()
body = swagger_client.UpdateFulfillmentOrderRequest() # UpdateFulfillmentOrderRequest | The request body of the `updateFulfillmentOrder` operation.
seller_fulfillment_order_id = 'seller_fulfillment_order_id_example' # str | The identifier assigned to the item by the seller when the fulfillment order was created.

try:
    api_response = api_instance.update_fulfillment_order(body, seller_fulfillment_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->update_fulfillment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFulfillmentOrderRequest**](UpdateFulfillmentOrderRequest.md)| The request body of the &#x60;updateFulfillmentOrder&#x60; operation. | 
 **seller_fulfillment_order_id** | **str**| The identifier assigned to the item by the seller when the fulfillment order was created. | 

### Return type

[**UpdateFulfillmentOrderResponse**](UpdateFulfillmentOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

