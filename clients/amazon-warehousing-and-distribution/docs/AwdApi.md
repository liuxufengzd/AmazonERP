# swagger_client.AwdApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inbound**](AwdApi.md#cancel_inbound) | **POST** /awd/2024-05-09/inboundOrders/{orderId}/cancellation | 
[**check_inbound_eligibility**](AwdApi.md#check_inbound_eligibility) | **POST** /awd/2024-05-09/inboundEligibility | 
[**confirm_inbound**](AwdApi.md#confirm_inbound) | **POST** /awd/2024-05-09/inboundOrders/{orderId}/confirmation | 
[**confirm_outbound**](AwdApi.md#confirm_outbound) | **POST** /awd/2024-05-09/outboundOrders/{orderId}/confirmation | 
[**confirm_replenishment_order**](AwdApi.md#confirm_replenishment_order) | **POST** /awd/2024-05-09/replenishmentOrders/{orderId}/confirmation | 
[**create_inbound**](AwdApi.md#create_inbound) | **POST** /awd/2024-05-09/inboundOrders | 
[**create_outbound**](AwdApi.md#create_outbound) | **POST** /awd/2024-05-09/outboundOrders | 
[**create_replenishment_order**](AwdApi.md#create_replenishment_order) | **POST** /awd/2024-05-09/replenishmentOrders | 
[**get_inbound**](AwdApi.md#get_inbound) | **GET** /awd/2024-05-09/inboundOrders/{orderId} | 
[**get_inbound_shipment**](AwdApi.md#get_inbound_shipment) | **GET** /awd/2024-05-09/inboundShipments/{shipmentId} | 
[**get_inbound_shipment_labels**](AwdApi.md#get_inbound_shipment_labels) | **GET** /awd/2024-05-09/inboundShipments/{shipmentId}/labels | 
[**get_label_page_types**](AwdApi.md#get_label_page_types) | **GET** /awd/2024-05-09/inboundShipments/{shipmentId}/labelPageTypes | 
[**get_outbound**](AwdApi.md#get_outbound) | **GET** /awd/2024-05-09/outboundOrders/{orderId} | 
[**get_replenishment_order**](AwdApi.md#get_replenishment_order) | **GET** /awd/2024-05-09/replenishmentOrders/{orderId} | 
[**list_inbound_shipments**](AwdApi.md#list_inbound_shipments) | **GET** /awd/2024-05-09/inboundShipments | 
[**list_inventory**](AwdApi.md#list_inventory) | **GET** /awd/2024-05-09/inventory | 
[**list_outbounds**](AwdApi.md#list_outbounds) | **GET** /awd/2024-05-09/outboundOrders | 
[**list_replenishment_orders**](AwdApi.md#list_replenishment_orders) | **GET** /awd/2024-05-09/replenishmentOrders | 
[**update_inbound**](AwdApi.md#update_inbound) | **PUT** /awd/2024-05-09/inboundOrders/{orderId} | 
[**update_inbound_shipment_transport_details**](AwdApi.md#update_inbound_shipment_transport_details) | **PUT** /awd/2024-05-09/inboundShipments/{shipmentId}/transport | 
[**update_outbound**](AwdApi.md#update_outbound) | **PUT** /awd/2024-05-09/outboundOrders/{orderId} | 


# **cancel_inbound**
> cancel_inbound(order_id)



Cancels an AWD Inbound order and its associated shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | The ID of the inbound order you want to cancel.

try:
    api_instance.cancel_inbound(order_id)
except ApiException as e:
    print("Exception when calling AwdApi->cancel_inbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ID of the inbound order you want to cancel. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_inbound_eligibility**
> InboundEligibility check_inbound_eligibility(body)



Determines if the packages you specify are eligible for an AWD inbound order and contains error details for ineligible packages.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
body = swagger_client.InboundPackages() # InboundPackages | Represents the packages you want to inbound.

try:
    api_response = api_instance.check_inbound_eligibility(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->check_inbound_eligibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InboundPackages**](InboundPackages.md)| Represents the packages you want to inbound. | 

### Return type

[**InboundEligibility**](InboundEligibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_inbound**
> confirm_inbound(order_id)



Confirms an AWD inbound order in `DRAFT` status.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | The ID of the inbound order that you want to confirm.

try:
    api_instance.confirm_inbound(order_id)
except ApiException as e:
    print("Exception when calling AwdApi->confirm_inbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ID of the inbound order that you want to confirm. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_outbound**
> confirm_outbound(order_id)



Confirms an AWD outbound order for a set of shipments that contain items that must be outbound to a destination node. You can confirm the order only if it's in an`ELIGIBLE` state.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | ID for the outbound order you want to confirm.

try:
    api_instance.confirm_outbound(order_id)
except ApiException as e:
    print("Exception when calling AwdApi->confirm_outbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID for the outbound order you want to confirm. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_replenishment_order**
> confirm_replenishment_order(order_id)



Confirms an AWD replenishment order in ELIGIBLE state with a set of shipments containing items that are needed to be replenished to an FBA node. Order can only be confirmed in ELIGIBLE state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | ID of the replenishment order to be confirmed.

try:
    api_instance.confirm_replenishment_order(order_id)
except ApiException as e:
    print("Exception when calling AwdApi->confirm_replenishment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of the replenishment order to be confirmed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inbound**
> InboundOrderReference create_inbound(body)



Creates a draft AWD inbound order with a list of packages for inbound shipment. The operation creates one shipment per order.   **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
body = swagger_client.InboundOrderCreationData() # InboundOrderCreationData | Payload for creating an inbound order.

try:
    api_response = api_instance.create_inbound(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->create_inbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InboundOrderCreationData**](InboundOrderCreationData.md)| Payload for creating an inbound order. | 

### Return type

[**InboundOrderReference**](InboundOrderReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_outbound**
> OutboundOrderReference create_outbound(body)



Creates a draft AWD outbound order with the specified products. The API returns the order ID for the newly created order and starts an async validation check on the outbound products. After the validation check, the order status transitions from `VALIDATING` to `ELIGIBLE/INELIGIBLE`.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
body = swagger_client.OutboundOrderCreationData() # OutboundOrderCreationData | Payload for creating an outbound order.

try:
    api_response = api_instance.create_outbound(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->create_outbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OutboundOrderCreationData**](OutboundOrderCreationData.md)| Payload for creating an outbound order. | 

### Return type

[**OutboundOrderReference**](OutboundOrderReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_replenishment_order**
> ReplenishmentOrderReference create_replenishment_order(body)



Creates an AWD replenishment order with given products to replenish. The API will return the order ID of the newly created order and also start an async validation check on the products to e. The order status will transition to ELIGIBLE/INELIGIBLE status from VALIDATING post validation check

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
body = swagger_client.ReplenishmentOrderCreationData() # ReplenishmentOrderCreationData | Payload for creating a replenishment order.

try:
    api_response = api_instance.create_replenishment_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->create_replenishment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplenishmentOrderCreationData**](ReplenishmentOrderCreationData.md)| Payload for creating a replenishment order. | 

### Return type

[**ReplenishmentOrderReference**](ReplenishmentOrderReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound**
> InboundOrder get_inbound(order_id)



Retrieves an AWD inbound order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | The ID of the inbound order that you want to retrieve.

try:
    api_response = api_instance.get_inbound(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->get_inbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ID of the inbound order that you want to retrieve. | 

### Return type

[**InboundOrder**](InboundOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_shipment**
> InboundShipment get_inbound_shipment(shipment_id, sku_quantities=sku_quantities)



Retrieves an AWD inbound shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
shipment_id = 'shipment_id_example' # str | ID for the shipment. A shipment contains the cases being inbounded.
sku_quantities = 'SHOW' # str | If equal to `SHOW`, the response includes the shipment SKU quantity details.  Defaults to `HIDE`, in which case the response does not contain SKU quantities (optional)

try:
    api_response = api_instance.get_inbound_shipment(shipment_id, sku_quantities=sku_quantities)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->get_inbound_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID for the shipment. A shipment contains the cases being inbounded. | 
 **sku_quantities** | **str**| If equal to &#x60;SHOW&#x60;, the response includes the shipment SKU quantity details.  Defaults to &#x60;HIDE&#x60;, in which case the response does not contain SKU quantities | [optional] 

### Return type

[**InboundShipment**](InboundShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_shipment_labels**
> ShipmentLabels get_inbound_shipment_labels(shipment_id, page_type=page_type, format_type=format_type)



Retrieves the box labels for a shipment ID that you specify. This is an asynchronous operation. If the label status is `GENERATED`, then the label URL is available.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
shipment_id = 'shipment_id_example' # str | ID for the shipment.
page_type = 'PLAIN_PAPER' # str | Page type for the generated labels. The default is `PLAIN_PAPER`. (optional)
format_type = 'PDF' # str | The format type of the output file that contains your labels. The default format type is `PDF`. (optional)

try:
    api_response = api_instance.get_inbound_shipment_labels(shipment_id, page_type=page_type, format_type=format_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->get_inbound_shipment_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID for the shipment. | 
 **page_type** | **str**| Page type for the generated labels. The default is &#x60;PLAIN_PAPER&#x60;. | [optional] 
 **format_type** | **str**| The format type of the output file that contains your labels. The default format type is &#x60;PDF&#x60;. | [optional] 

### Return type

[**ShipmentLabels**](ShipmentLabels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_label_page_types**
> ShipmentLabelPageTypes get_label_page_types(shipment_id)



Retrieves the available label page types for a shipment ID that you specify. This is an asynchronous operation. If the label status is `GENERATED`, then the pageTypes are available.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
shipment_id = 'shipment_id_example' # str | ID for the shipment.

try:
    api_response = api_instance.get_label_page_types(shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->get_label_page_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID for the shipment. | 

### Return type

[**ShipmentLabelPageTypes**](ShipmentLabelPageTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound**
> OutboundOrder get_outbound(order_id)



Retrieves an AWD outbound order with a set of shipments that contain items that are outbound into a destination channel. If the order is not eligible, the validation errors field is included in the order response. The API returns the order ID for the newly created order and starts an async validation check on the outbound products. After the validation check, the order status transitions from `VALIDATING` to `ELIGIBLE/INELIGIBLE`.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | ID for the outbound order to be retrieved.

try:
    api_response = api_instance.get_outbound(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->get_outbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID for the outbound order to be retrieved. | 

### Return type

[**OutboundOrder**](OutboundOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_order**
> ReplenishmentOrder get_replenishment_order(order_id)



Retrieves an AWD Replenishment order with a set of shipments containing items that is/was planned to be replenished into an FBA node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | ID of the replenishment order to be retrieved.

try:
    api_response = api_instance.get_replenishment_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->get_replenishment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of the replenishment order to be retrieved. | 

### Return type

[**ReplenishmentOrder**](ReplenishmentOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_shipments**
> ShipmentListing list_inbound_shipments(sort_by=sort_by, sort_order=sort_order, shipment_status=shipment_status, updated_after=updated_after, updated_before=updated_before, max_results=max_results, next_token=next_token)



Retrieves a summary of all the inbound AWD shipments associated with a merchant, with the ability to apply optional filters.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
sort_by = 'sort_by_example' # str | Field to sort results by. By default, the response will be sorted by UPDATED_AT. (optional)
sort_order = 'ASCENDING' # str | Sort the response in ASCENDING or DESCENDING order. By default, the response will be sorted in DESCENDING order. (optional)
shipment_status = 'CREATED' # str | Filter by inbound shipment status. (optional)
updated_after = '2023-01-12T10:00:00.000Z' # datetime | List the inbound shipments that were updated after a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format. (optional)
updated_before = '2023-01-12T10:00:00.000Z' # datetime | List the inbound shipments that were updated before a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format. (optional)
max_results = 25 # int | Maximum number of results to return. (optional) (default to 25)
next_token = 'SampleToken' # str | A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages. (optional)

try:
    api_response = api_instance.list_inbound_shipments(sort_by=sort_by, sort_order=sort_order, shipment_status=shipment_status, updated_after=updated_after, updated_before=updated_before, max_results=max_results, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->list_inbound_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Field to sort results by. By default, the response will be sorted by UPDATED_AT. | [optional] 
 **sort_order** | **str**| Sort the response in ASCENDING or DESCENDING order. By default, the response will be sorted in DESCENDING order. | [optional] 
 **shipment_status** | **str**| Filter by inbound shipment status. | [optional] 
 **updated_after** | **datetime**| List the inbound shipments that were updated after a certain time (inclusive). The date must be in &lt;a href&#x3D;&#39;https://developer-docs.amazon.com/sp-api/docs/iso-8601&#39;&gt;ISO 8601&lt;/a&gt; format. | [optional] 
 **updated_before** | **datetime**| List the inbound shipments that were updated before a certain time (inclusive). The date must be in &lt;a href&#x3D;&#39;https://developer-docs.amazon.com/sp-api/docs/iso-8601&#39;&gt;ISO 8601&lt;/a&gt; format. | [optional] 
 **max_results** | **int**| Maximum number of results to return. | [optional] [default to 25]
 **next_token** | **str**| A token that is used to retrieve the next page of results. The response includes &#x60;nextToken&#x60; when the number of results exceeds the specified &#x60;maxResults&#x60; value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until &#x60;nextToken&#x60; is null. Note that this operation can return empty pages. | [optional] 

### Return type

[**ShipmentListing**](ShipmentListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory**
> InventoryListing list_inventory(sku=sku, sort_order=sort_order, details=details, next_token=next_token, max_results=max_results)



Lists AWD inventory associated with a merchant with the ability to apply optional filters.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
sku = 'TestSKU' # str | Filter by seller or merchant SKU for the item. (optional)
sort_order = 'sort_order_example' # str | Sort the response in `ASCENDING` or `DESCENDING` order. (optional)
details = 'SHOW' # str | Set to `SHOW` to return summaries with additional inventory details. Defaults to `HIDE,` which returns only inventory summary totals. (optional)
next_token = 'SampleToken' # str | A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages. (optional)
max_results = 25 # int | Maximum number of results to return. (optional) (default to 25)

try:
    api_response = api_instance.list_inventory(sku=sku, sort_order=sort_order, details=details, next_token=next_token, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->list_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| Filter by seller or merchant SKU for the item. | [optional] 
 **sort_order** | **str**| Sort the response in &#x60;ASCENDING&#x60; or &#x60;DESCENDING&#x60; order. | [optional] 
 **details** | **str**| Set to &#x60;SHOW&#x60; to return summaries with additional inventory details. Defaults to &#x60;HIDE,&#x60; which returns only inventory summary totals. | [optional] 
 **next_token** | **str**| A token that is used to retrieve the next page of results. The response includes &#x60;nextToken&#x60; when the number of results exceeds the specified &#x60;maxResults&#x60; value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until &#x60;nextToken&#x60; is null. Note that this operation can return empty pages. | [optional] 
 **max_results** | **int**| Maximum number of results to return. | [optional] [default to 25]

### Return type

[**InventoryListing**](InventoryListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outbounds**
> OutboundListing list_outbounds(updated_after=updated_after, updated_before=updated_before, sort_order=sort_order, max_results=max_results, next_token=next_token)



Retrieves all outbound AWD orders (with optional filters) that pertain to a merchant. By default, orders are sorted by the `updatedAt` attribute in descending order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
updated_after = '2023-01-12T10:00:00.000Z' # datetime | Get the outbound orders updated after a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format. (optional)
updated_before = '2023-01-12T10:00:00.000Z' # datetime | Get the outbound orders updated before a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format. (optional)
sort_order = 'sort_order_example' # str | Sort the response in `ASCENDING` or `DESCENDING` order. (optional)
max_results = 25 # int | Maximum number of results to return. (optional) (default to 25)
next_token = 'SampleToken' # str | A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages. (optional)

try:
    api_response = api_instance.list_outbounds(updated_after=updated_after, updated_before=updated_before, sort_order=sort_order, max_results=max_results, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->list_outbounds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**| Get the outbound orders updated after a certain time (inclusive). The date must be in &lt;a href&#x3D;&#39;https://developer-docs.amazon.com/sp-api/docs/iso-8601&#39;&gt;ISO 8601&lt;/a&gt; format. | [optional] 
 **updated_before** | **datetime**| Get the outbound orders updated before a certain time (inclusive). The date must be in &lt;a href&#x3D;&#39;https://developer-docs.amazon.com/sp-api/docs/iso-8601&#39;&gt;ISO 8601&lt;/a&gt; format. | [optional] 
 **sort_order** | **str**| Sort the response in &#x60;ASCENDING&#x60; or &#x60;DESCENDING&#x60; order. | [optional] 
 **max_results** | **int**| Maximum number of results to return. | [optional] [default to 25]
 **next_token** | **str**| A token that is used to retrieve the next page of results. The response includes &#x60;nextToken&#x60; when the number of results exceeds the specified &#x60;maxResults&#x60; value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until &#x60;nextToken&#x60; is null. Note that this operation can return empty pages. | [optional] 

### Return type

[**OutboundListing**](OutboundListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replenishment_orders**
> ReplenishmentOrderListing list_replenishment_orders(updated_after=updated_after, updated_before=updated_before, sort_order=sort_order, max_results=max_results, next_token=next_token)



Retrieves all the AWD replenishment orders pertaining to a merchant with optional filters. API by default will sort orders by updatedAt attribute in descending order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
updated_after = '2023-01-12T10:00:00.000Z' # datetime | Get the replenishment orders updated after certain time (Inclusive) Date should be in ISO 8601 format as defined by date-time in - https://www.rfc-editor.org/rfc/rfc3339. (optional)
updated_before = '2023-01-12T10:00:00.000Z' # datetime | Get the replenishment orders updated before certain time (Inclusive) Date should be in ISO 8601 format as defined by date-time in - https://www.rfc-editor.org/rfc/rfc3339. (optional)
sort_order = 'ASCENDING' # str | Sort the response in ASCENDING or DESCENDING order. The default sort order is DESCENDING. (optional)
max_results = 25 # int | Maximum results to be returned in a single response. (optional) (default to 25)
next_token = 'SampleToken' # str | A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages. (optional)

try:
    api_response = api_instance.list_replenishment_orders(updated_after=updated_after, updated_before=updated_before, sort_order=sort_order, max_results=max_results, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->list_replenishment_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**| Get the replenishment orders updated after certain time (Inclusive) Date should be in ISO 8601 format as defined by date-time in - https://www.rfc-editor.org/rfc/rfc3339. | [optional] 
 **updated_before** | **datetime**| Get the replenishment orders updated before certain time (Inclusive) Date should be in ISO 8601 format as defined by date-time in - https://www.rfc-editor.org/rfc/rfc3339. | [optional] 
 **sort_order** | **str**| Sort the response in ASCENDING or DESCENDING order. The default sort order is DESCENDING. | [optional] 
 **max_results** | **int**| Maximum results to be returned in a single response. | [optional] [default to 25]
 **next_token** | **str**| A token that is used to retrieve the next page of results. The response includes &#x60;nextToken&#x60; when the number of results exceeds the specified &#x60;maxResults&#x60; value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until &#x60;nextToken&#x60; is null. Note that this operation can return empty pages. | [optional] 

### Return type

[**ReplenishmentOrderListing**](ReplenishmentOrderListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound**
> update_inbound(order_id, body)



Updates an AWD inbound order that is in `DRAFT` status and not yet confirmed. Use this operation to update the `packagesToInbound`, `originAddress` and `preferences` attributes.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | The ID of the inbound order that you want to update.
body = swagger_client.InboundOrder() # InboundOrder | Represents an AWD inbound order.

try:
    api_instance.update_inbound(order_id, body)
except ApiException as e:
    print("Exception when calling AwdApi->update_inbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ID of the inbound order that you want to update. | 
 **body** | [**InboundOrder**](InboundOrder.md)| Represents an AWD inbound order. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound_shipment_transport_details**
> update_inbound_shipment_transport_details(shipment_id, body)



Updates transport details for an AWD shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
shipment_id = 'shipment_id_example' # str | The shipment ID.
body = swagger_client.TransportationDetails() # TransportationDetails | Transportation details for the shipment.

try:
    api_instance.update_inbound_shipment_transport_details(shipment_id, body)
except ApiException as e:
    print("Exception when calling AwdApi->update_inbound_shipment_transport_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| The shipment ID. | 
 **body** | [**TransportationDetails**](TransportationDetails.md)| Transportation details for the shipment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_outbound**
> OutboundOrderReference update_outbound(order_id, body)



Updates an AWD outbound order that is in `DRAFT`, `ELIGIBLE`, or `INELIGIBLE` status. This API allows updates on `productsToOutbound` and `orderPreferences` attributes only. Any updates will restart the outbound order validation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AwdApi()
order_id = 'order_id_example' # str | ID for the outbound order to be updated.
body = swagger_client.OutboundOrder() # OutboundOrder | Represents an AWD outbound order.

try:
    api_response = api_instance.update_outbound(order_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwdApi->update_outbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID for the outbound order to be updated. | 
 **body** | [**OutboundOrder**](OutboundOrder.md)| Represents an AWD outbound order. | 

### Return type

[**OutboundOrderReference**](OutboundOrderReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

