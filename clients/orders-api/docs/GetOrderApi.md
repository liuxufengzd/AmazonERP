# swagger_client.GetOrderApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order**](GetOrderApi.md#get_order) | **GET** /orders/2026-01-01/orders/{orderId} | 


# **get_order**
> GetOrderResponse get_order(order_id, included_data=included_data)



Returns the order that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.5 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetOrderApi()
order_id = 'order_id_example' # str | An Amazon-defined order identifier.
included_data = ['[BUYER, PACKAGES]'] # list[str] | A list of datasets to include in the response. (optional)

try:
    api_response = api_instance.get_order(order_id, included_data=included_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetOrderApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| An Amazon-defined order identifier. | 
 **included_data** | [**list[str]**](str.md)| A list of datasets to include in the response. | [optional] 

### Return type

[**GetOrderResponse**](GetOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

