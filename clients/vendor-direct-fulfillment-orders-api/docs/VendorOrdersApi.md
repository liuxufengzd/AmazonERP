# swagger_client.VendorOrdersApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order**](VendorOrdersApi.md#get_order) | **GET** /vendor/directFulfillment/orders/2021-12-28/purchaseOrders/{purchaseOrderNumber} | 
[**get_orders**](VendorOrdersApi.md#get_orders) | **GET** /vendor/directFulfillment/orders/2021-12-28/purchaseOrders | 
[**submit_acknowledgement**](VendorOrdersApi.md#submit_acknowledgement) | **POST** /vendor/directFulfillment/orders/2021-12-28/acknowledgements | 


# **get_order**
> Order get_order(purchase_order_number)



Returns purchase order information for the purchaseOrderNumber that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 10 | 10 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorOrdersApi()
purchase_order_number = 'purchase_order_number_example' # str | The order identifier for the purchase order that you want. Formatting Notes: alpha-numeric code.

try:
    api_response = api_instance.get_order(purchase_order_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorOrdersApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_number** | **str**| The order identifier for the purchase order that you want. Formatting Notes: alpha-numeric code. | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> OrderList get_orders(created_after, created_before, ship_from_party_id=ship_from_party_id, status=status, limit=limit, sort_order=sort_order, next_token=next_token, include_details=include_details)



Returns a list of purchase orders created during the time frame that you specify. You define the time frame using the createdAfter and createdBefore parameters. You must use both parameters. You can choose to get only the purchase order numbers by setting the includeDetails parameter to false. In that case, the operation returns a list of purchase order numbers. You can then call the getOrder operation to return the details of a specific order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 10 | 10 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorOrdersApi()
created_after = '2013-10-20T19:20:30+01:00' # datetime | Purchase orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
created_before = '2013-10-20T19:20:30+01:00' # datetime | Purchase orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
ship_from_party_id = 'ship_from_party_id_example' # str | The vendor warehouse identifier for the fulfillment warehouse. If not specified, the result will contain orders for all warehouses. (optional)
status = 'status_example' # str | Returns only the purchase orders that match the specified status. If not specified, the result will contain orders that match any status. (optional)
limit = 789 # int | The limit to the number of purchase orders returned. (optional)
sort_order = 'sort_order_example' # str | Sort the list in ascending or descending order by order creation date. (optional)
next_token = 'next_token_example' # str | Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call. (optional)
include_details = 'true' # str | When true, returns the complete purchase order details. Otherwise, only purchase order numbers are returned. (optional) (default to true)

try:
    api_response = api_instance.get_orders(created_after, created_before, ship_from_party_id=ship_from_party_id, status=status, limit=limit, sort_order=sort_order, next_token=next_token, include_details=include_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorOrdersApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| Purchase orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format. | 
 **created_before** | **datetime**| Purchase orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format. | 
 **ship_from_party_id** | **str**| The vendor warehouse identifier for the fulfillment warehouse. If not specified, the result will contain orders for all warehouses. | [optional] 
 **status** | **str**| Returns only the purchase orders that match the specified status. If not specified, the result will contain orders that match any status. | [optional] 
 **limit** | **int**| The limit to the number of purchase orders returned. | [optional] 
 **sort_order** | **str**| Sort the list in ascending or descending order by order creation date. | [optional] 
 **next_token** | **str**| Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call. | [optional] 
 **include_details** | **str**| When true, returns the complete purchase order details. Otherwise, only purchase order numbers are returned. | [optional] [default to true]

### Return type

[**OrderList**](OrderList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_acknowledgement**
> TransactionId submit_acknowledgement(body)



Submits acknowledgements for one or more purchase orders.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 10 | 10 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorOrdersApi()
body = swagger_client.SubmitAcknowledgementRequest() # SubmitAcknowledgementRequest | The request body containing the acknowledgement to an order

try:
    api_response = api_instance.submit_acknowledgement(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorOrdersApi->submit_acknowledgement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmitAcknowledgementRequest**](SubmitAcknowledgementRequest.md)| The request body containing the acknowledgement to an order | 

### Return type

[**TransactionId**](TransactionId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

