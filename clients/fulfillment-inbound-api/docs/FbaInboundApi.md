# swagger_client.FbaInboundApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inbound_plan**](FbaInboundApi.md#cancel_inbound_plan) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/cancellation | 
[**cancel_self_ship_appointment**](FbaInboundApi.md#cancel_self_ship_appointment) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentCancellation | 
[**confirm_delivery_window_options**](FbaInboundApi.md#confirm_delivery_window_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions/{deliveryWindowOptionId}/confirmation | 
[**confirm_packing_option**](FbaInboundApi.md#confirm_packing_option) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingOptions/{packingOptionId}/confirmation | 
[**confirm_placement_option**](FbaInboundApi.md#confirm_placement_option) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/placementOptions/{placementOptionId}/confirmation | 
[**confirm_shipment_content_update_preview**](FbaInboundApi.md#confirm_shipment_content_update_preview) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}/confirmation | 
[**confirm_transportation_options**](FbaInboundApi.md#confirm_transportation_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/transportationOptions/confirmation | 
[**create_inbound_plan**](FbaInboundApi.md#create_inbound_plan) | **POST** /inbound/fba/2024-03-20/inboundPlans | 
[**create_marketplace_item_labels**](FbaInboundApi.md#create_marketplace_item_labels) | **POST** /inbound/fba/2024-03-20/items/labels | 
[**generate_delivery_window_options**](FbaInboundApi.md#generate_delivery_window_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions | 
[**generate_packing_options**](FbaInboundApi.md#generate_packing_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingOptions | 
[**generate_placement_options**](FbaInboundApi.md#generate_placement_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/placementOptions | 
[**generate_self_ship_appointment_slots**](FbaInboundApi.md#generate_self_ship_appointment_slots) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots | 
[**generate_shipment_content_update_previews**](FbaInboundApi.md#generate_shipment_content_update_previews) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews | 
[**generate_transportation_options**](FbaInboundApi.md#generate_transportation_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/transportationOptions | 
[**get_delivery_challan_document**](FbaInboundApi.md#get_delivery_challan_document) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryChallanDocument | 
[**get_inbound_operation_status**](FbaInboundApi.md#get_inbound_operation_status) | **GET** /inbound/fba/2024-03-20/operations/{operationId} | 
[**get_inbound_plan**](FbaInboundApi.md#get_inbound_plan) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId} | 
[**get_self_ship_appointment_slots**](FbaInboundApi.md#get_self_ship_appointment_slots) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots | 
[**get_shipment**](FbaInboundApi.md#get_shipment) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId} | 
[**get_shipment_content_update_preview**](FbaInboundApi.md#get_shipment_content_update_preview) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId} | 
[**list_delivery_window_options**](FbaInboundApi.md#list_delivery_window_options) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions | 
[**list_inbound_plan_boxes**](FbaInboundApi.md#list_inbound_plan_boxes) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/boxes | 
[**list_inbound_plan_items**](FbaInboundApi.md#list_inbound_plan_items) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/items | 
[**list_inbound_plan_pallets**](FbaInboundApi.md#list_inbound_plan_pallets) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/pallets | 
[**list_inbound_plans**](FbaInboundApi.md#list_inbound_plans) | **GET** /inbound/fba/2024-03-20/inboundPlans | 
[**list_item_compliance_details**](FbaInboundApi.md#list_item_compliance_details) | **GET** /inbound/fba/2024-03-20/items/compliance | 
[**list_packing_group_boxes**](FbaInboundApi.md#list_packing_group_boxes) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/boxes | 
[**list_packing_group_items**](FbaInboundApi.md#list_packing_group_items) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/items | 
[**list_packing_options**](FbaInboundApi.md#list_packing_options) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingOptions | 
[**list_placement_options**](FbaInboundApi.md#list_placement_options) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/placementOptions | 
[**list_prep_details**](FbaInboundApi.md#list_prep_details) | **GET** /inbound/fba/2024-03-20/items/prepDetails | 
[**list_shipment_boxes**](FbaInboundApi.md#list_shipment_boxes) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/boxes | 
[**list_shipment_content_update_previews**](FbaInboundApi.md#list_shipment_content_update_previews) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews | 
[**list_shipment_items**](FbaInboundApi.md#list_shipment_items) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/items | 
[**list_shipment_pallets**](FbaInboundApi.md#list_shipment_pallets) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/pallets | 
[**list_transportation_options**](FbaInboundApi.md#list_transportation_options) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/transportationOptions | 
[**schedule_self_ship_appointment**](FbaInboundApi.md#schedule_self_ship_appointment) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots/{slotId}/schedule | 
[**set_packing_information**](FbaInboundApi.md#set_packing_information) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingInformation | 
[**set_prep_details**](FbaInboundApi.md#set_prep_details) | **POST** /inbound/fba/2024-03-20/items/prepDetails | 
[**update_inbound_plan_name**](FbaInboundApi.md#update_inbound_plan_name) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/name | 
[**update_item_compliance_details**](FbaInboundApi.md#update_item_compliance_details) | **PUT** /inbound/fba/2024-03-20/items/compliance | 
[**update_shipment_name**](FbaInboundApi.md#update_shipment_name) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/name | 
[**update_shipment_source_address**](FbaInboundApi.md#update_shipment_source_address) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/sourceAddress | 
[**update_shipment_tracking_details**](FbaInboundApi.md#update_shipment_tracking_details) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/trackingDetails | 


# **cancel_inbound_plan**
> CancelInboundPlanResponse cancel_inbound_plan(inbound_plan_id)



Cancels an Inbound Plan. Charges may apply if the cancellation is performed outside of a void window. The window for Amazon Partnered Carriers is 24 hours for Small Parcel Delivery (SPD) and one hour for Less-Than-Truckload (LTL) carrier shipments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.

try:
    api_response = api_instance.cancel_inbound_plan(inbound_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->cancel_inbound_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 

### Return type

[**CancelInboundPlanResponse**](CancelInboundPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_self_ship_appointment**
> CancelSelfShipAppointmentResponse cancel_self_ship_appointment(inbound_plan_id, shipment_id, body)



Cancels a self-ship appointment slot against a shipment. Only available in the following [marketplaces](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids): MX, BR, EG, SA, AE, IN. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
body = swagger_client.CancelSelfShipAppointmentRequest() # CancelSelfShipAppointmentRequest | The body of the request to `cancelSelfShipAppointment`.

try:
    api_response = api_instance.cancel_self_ship_appointment(inbound_plan_id, shipment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->cancel_self_ship_appointment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**CancelSelfShipAppointmentRequest**](CancelSelfShipAppointmentRequest.md)| The body of the request to &#x60;cancelSelfShipAppointment&#x60;. | 

### Return type

[**CancelSelfShipAppointmentResponse**](CancelSelfShipAppointmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_delivery_window_options**
> ConfirmDeliveryWindowOptionsResponse confirm_delivery_window_options(inbound_plan_id, shipment_id, delivery_window_option_id)



Confirms the delivery window option for chosen shipment within an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new delivery window options cannot be generated, but the chosen delivery window option can be updated before shipment closure. The window is used to provide the expected time when a shipment will arrive at the warehouse. All transportation options which have the program `CONFIRMED_DELIVERY_WINDOW` require a delivery window to be confirmed prior to transportation option confirmation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | The shipment to confirm the delivery window option for.
delivery_window_option_id = 'delivery_window_option_id_example' # str | The id of the delivery window option to be confirmed.

try:
    api_response = api_instance.confirm_delivery_window_options(inbound_plan_id, shipment_id, delivery_window_option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->confirm_delivery_window_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| The shipment to confirm the delivery window option for. | 
 **delivery_window_option_id** | **str**| The id of the delivery window option to be confirmed. | 

### Return type

[**ConfirmDeliveryWindowOptionsResponse**](ConfirmDeliveryWindowOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_packing_option**
> ConfirmPackingOptionResponse confirm_packing_option(inbound_plan_id, packing_option_id)



Confirms the packing option for an inbound plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
packing_option_id = 'packing_option_id_example' # str | Identifier of a packing option.

try:
    api_response = api_instance.confirm_packing_option(inbound_plan_id, packing_option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->confirm_packing_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **packing_option_id** | **str**| Identifier of a packing option. | 

### Return type

[**ConfirmPackingOptionResponse**](ConfirmPackingOptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_placement_option**
> ConfirmPlacementOptionResponse confirm_placement_option(inbound_plan_id, placement_option_id)



Confirms the placement option for an inbound plan. Once confirmed, it cannot be changed for the Inbound Plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
placement_option_id = 'placement_option_id_example' # str | The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs.

try:
    api_response = api_instance.confirm_placement_option(inbound_plan_id, placement_option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->confirm_placement_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **placement_option_id** | **str**| The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs. | 

### Return type

[**ConfirmPlacementOptionResponse**](ConfirmPlacementOptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_shipment_content_update_preview**
> ConfirmShipmentContentUpdatePreviewResponse confirm_shipment_content_update_preview(inbound_plan_id, shipment_id, content_update_preview_id)



Confirm a shipment content update preview and accept the changes in transportation cost.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
content_update_preview_id = 'content_update_preview_id_example' # str | Identifier of a content update preview.

try:
    api_response = api_instance.confirm_shipment_content_update_preview(inbound_plan_id, shipment_id, content_update_preview_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->confirm_shipment_content_update_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **content_update_preview_id** | **str**| Identifier of a content update preview. | 

### Return type

[**ConfirmShipmentContentUpdatePreviewResponse**](ConfirmShipmentContentUpdatePreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_transportation_options**
> ConfirmTransportationOptionsResponse confirm_transportation_options(inbound_plan_id, body)



Confirms all the transportation options for an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new transportation options can not be generated or confirmed for the Inbound Plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
body = swagger_client.ConfirmTransportationOptionsRequest() # ConfirmTransportationOptionsRequest | The body of the request to `confirmTransportationOptions`.

try:
    api_response = api_instance.confirm_transportation_options(inbound_plan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->confirm_transportation_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**ConfirmTransportationOptionsRequest**](ConfirmTransportationOptionsRequest.md)| The body of the request to &#x60;confirmTransportationOptions&#x60;. | 

### Return type

[**ConfirmTransportationOptionsResponse**](ConfirmTransportationOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inbound_plan**
> CreateInboundPlanResponse create_inbound_plan(body)



Creates an inbound plan. An inbound plan contains all the necessary information to send shipments into Amazon's fufillment network.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
body = swagger_client.CreateInboundPlanRequest() # CreateInboundPlanRequest | The body of the request to `createInboundPlan`.

try:
    api_response = api_instance.create_inbound_plan(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->create_inbound_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInboundPlanRequest**](CreateInboundPlanRequest.md)| The body of the request to &#x60;createInboundPlan&#x60;. | 

### Return type

[**CreateInboundPlanResponse**](CreateInboundPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_marketplace_item_labels**
> CreateMarketplaceItemLabelsResponse create_marketplace_item_labels(body)



For a given marketplace - creates labels for a list of MSKUs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
body = swagger_client.CreateMarketplaceItemLabelsRequest() # CreateMarketplaceItemLabelsRequest | The body of the request to `createMarketplaceItemLabels`.

try:
    api_response = api_instance.create_marketplace_item_labels(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->create_marketplace_item_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMarketplaceItemLabelsRequest**](CreateMarketplaceItemLabelsRequest.md)| The body of the request to &#x60;createMarketplaceItemLabels&#x60;. | 

### Return type

[**CreateMarketplaceItemLabelsResponse**](CreateMarketplaceItemLabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_delivery_window_options**
> GenerateDeliveryWindowOptionsResponse generate_delivery_window_options(inbound_plan_id, shipment_id)



Generates available delivery window options for a given shipment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | The shipment to generate delivery window options for.

try:
    api_response = api_instance.generate_delivery_window_options(inbound_plan_id, shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->generate_delivery_window_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| The shipment to generate delivery window options for. | 

### Return type

[**GenerateDeliveryWindowOptionsResponse**](GenerateDeliveryWindowOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_packing_options**
> GeneratePackingOptionsResponse generate_packing_options(inbound_plan_id)



Generates available packing options for the inbound plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.

try:
    api_response = api_instance.generate_packing_options(inbound_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->generate_packing_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 

### Return type

[**GeneratePackingOptionsResponse**](GeneratePackingOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_placement_options**
> GeneratePlacementOptionsResponse generate_placement_options(inbound_plan_id, body)



Generates placement options for the inbound plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
body = swagger_client.GeneratePlacementOptionsRequest() # GeneratePlacementOptionsRequest | The body of the request to `generatePlacementOptions`.

try:
    api_response = api_instance.generate_placement_options(inbound_plan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->generate_placement_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**GeneratePlacementOptionsRequest**](GeneratePlacementOptionsRequest.md)| The body of the request to &#x60;generatePlacementOptions&#x60;. | 

### Return type

[**GeneratePlacementOptionsResponse**](GeneratePlacementOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_self_ship_appointment_slots**
> GenerateSelfShipAppointmentSlotsResponse generate_self_ship_appointment_slots(inbound_plan_id, shipment_id, body)



Initiates the process of generating the appointment slots list. Only available in the following [marketplaces](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids): MX, BR, EG, SA, AE, IN. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
body = swagger_client.GenerateSelfShipAppointmentSlotsRequest() # GenerateSelfShipAppointmentSlotsRequest | The body of the request to `generateSelfShipAppointmentSlots`.

try:
    api_response = api_instance.generate_self_ship_appointment_slots(inbound_plan_id, shipment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->generate_self_ship_appointment_slots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**GenerateSelfShipAppointmentSlotsRequest**](GenerateSelfShipAppointmentSlotsRequest.md)| The body of the request to &#x60;generateSelfShipAppointmentSlots&#x60;. | 

### Return type

[**GenerateSelfShipAppointmentSlotsResponse**](GenerateSelfShipAppointmentSlotsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_shipment_content_update_previews**
> GenerateShipmentContentUpdatePreviewsResponse generate_shipment_content_update_previews(inbound_plan_id, shipment_id, body)



Generate a shipment content update preview given a set of intended boxes and/or items for a shipment with a confirmed carrier. The shipment content update preview will be viewable with the updated costs and contents prior to confirmation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
body = swagger_client.GenerateShipmentContentUpdatePreviewsRequest() # GenerateShipmentContentUpdatePreviewsRequest | The body of the request to `generateShipmentContentUpdatePreviews`.

try:
    api_response = api_instance.generate_shipment_content_update_previews(inbound_plan_id, shipment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->generate_shipment_content_update_previews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**GenerateShipmentContentUpdatePreviewsRequest**](GenerateShipmentContentUpdatePreviewsRequest.md)| The body of the request to &#x60;generateShipmentContentUpdatePreviews&#x60;. | 

### Return type

[**GenerateShipmentContentUpdatePreviewsResponse**](GenerateShipmentContentUpdatePreviewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_transportation_options**
> GenerateTransportationOptionsResponse generate_transportation_options(inbound_plan_id, body)



Generates available transportation options for a given placement option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
body = swagger_client.GenerateTransportationOptionsRequest() # GenerateTransportationOptionsRequest | The body of the request to `generateTransportationOptions`.

try:
    api_response = api_instance.generate_transportation_options(inbound_plan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->generate_transportation_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**GenerateTransportationOptionsRequest**](GenerateTransportationOptionsRequest.md)| The body of the request to &#x60;generateTransportationOptions&#x60;. | 

### Return type

[**GenerateTransportationOptionsResponse**](GenerateTransportationOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_challan_document**
> GetDeliveryChallanDocumentResponse get_delivery_challan_document(inbound_plan_id, shipment_id)



Provide delivery challan document for PCP transportation in IN marketplace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.

try:
    api_response = api_instance.get_delivery_challan_document(inbound_plan_id, shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_delivery_challan_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 

### Return type

[**GetDeliveryChallanDocumentResponse**](GetDeliveryChallanDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_operation_status**
> InboundOperationStatus get_inbound_operation_status(operation_id)



Gets the status of the processing of an asynchronous API call.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
operation_id = 'operation_id_example' # str | Identifier of an asynchronous operation.

try:
    api_response = api_instance.get_inbound_operation_status(operation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_inbound_operation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**| Identifier of an asynchronous operation. | 

### Return type

[**InboundOperationStatus**](InboundOperationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_plan**
> InboundPlan get_inbound_plan(inbound_plan_id)



Fetches the top level information about an inbound plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.

try:
    api_response = api_instance.get_inbound_plan(inbound_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_inbound_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 

### Return type

[**InboundPlan**](InboundPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_ship_appointment_slots**
> GetSelfShipAppointmentSlotsResponse get_self_ship_appointment_slots(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)



Retrieves a list of available self-ship appointment slots used to drop off a shipment at a warehouse. Only available in the following [marketplaces](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids): MX, BR, EG, SA, AE, IN. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
page_size = 10 # int | The number of self ship appointment slots to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.get_self_ship_appointment_slots(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_self_ship_appointment_slots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of self ship appointment slots to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**GetSelfShipAppointmentSlotsResponse**](GetSelfShipAppointmentSlotsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment**
> Shipment get_shipment(inbound_plan_id, shipment_id)



Provides the full details for a specific shipment within an inbound plan. The `transportationOptionId` inside `acceptedTransportationSelection` can be used to retrieve the transportation details for the shipment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.

try:
    api_response = api_instance.get_shipment(inbound_plan_id, shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_content_update_preview**
> ContentUpdatePreview get_shipment_content_update_preview(inbound_plan_id, shipment_id, content_update_preview_id)



Retrieve a shipment content update preview which provides a summary of the requested shipment content changes along with the transportation cost implications of the change that can only be confirmed prior to the expiry date specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
content_update_preview_id = 'content_update_preview_id_example' # str | Identifier of a content update preview.

try:
    api_response = api_instance.get_shipment_content_update_preview(inbound_plan_id, shipment_id, content_update_preview_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_shipment_content_update_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **content_update_preview_id** | **str**| Identifier of a content update preview. | 

### Return type

[**ContentUpdatePreview**](ContentUpdatePreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_window_options**
> ListDeliveryWindowOptionsResponse list_delivery_window_options(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)



Retrieves all delivery window options for a shipment. Delivery window options must first be generated by the `generateDeliveryWindowOptions` operation before becoming available.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | The shipment to get delivery window options for.
page_size = 10 # int | The number of delivery window options to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_delivery_window_options(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_delivery_window_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| The shipment to get delivery window options for. | 
 **page_size** | **int**| The number of delivery window options to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListDeliveryWindowOptionsResponse**](ListDeliveryWindowOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_plan_boxes**
> ListInboundPlanBoxesResponse list_inbound_plan_boxes(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)



Provides a paginated list of box packages in an inbound plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
page_size = 10 # int | The number of boxes to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_inbound_plan_boxes(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_inbound_plan_boxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of boxes to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListInboundPlanBoxesResponse**](ListInboundPlanBoxesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_plan_items**
> ListInboundPlanItemsResponse list_inbound_plan_items(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)



Provides a paginated list of item packages in an inbound plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
page_size = 10 # int | The number of items to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_inbound_plan_items(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_inbound_plan_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of items to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListInboundPlanItemsResponse**](ListInboundPlanItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_plan_pallets**
> ListInboundPlanPalletsResponse list_inbound_plan_pallets(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)



Provides a paginated list of pallet packages in an inbound plan. An inbound plan will have pallets when the related details are provided after generating Less-Than-Truckload (LTL) carrier shipments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
page_size = 10 # int | The number of pallets to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_inbound_plan_pallets(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_inbound_plan_pallets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of pallets to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListInboundPlanPalletsResponse**](ListInboundPlanPalletsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_plans**
> ListInboundPlansResponse list_inbound_plans(page_size=page_size, pagination_token=pagination_token, status=status, sort_by=sort_by, sort_order=sort_order)



Provides a list of inbound plans with minimal information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
page_size = 10 # int | The number of inbound plans to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)
status = 'status_example' # str | The status of an inbound plan. (optional)
sort_by = 'sort_by_example' # str | Sort by field. (optional)
sort_order = 'sort_order_example' # str | The sort order. (optional)

try:
    api_response = api_instance.list_inbound_plans(page_size=page_size, pagination_token=pagination_token, status=status, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_inbound_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of inbound plans to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 
 **status** | **str**| The status of an inbound plan. | [optional] 
 **sort_by** | **str**| Sort by field. | [optional] 
 **sort_order** | **str**| The sort order. | [optional] 

### Return type

[**ListInboundPlansResponse**](ListInboundPlansResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_item_compliance_details**
> ListItemComplianceDetailsResponse list_item_compliance_details(mskus, marketplace_id)



List the inbound compliance details for MSKUs in a given marketplace.  **Note:** MSKUs that contain certain characters must be encoded. For more information, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).  The following characters must be double percent encoded:  - `%` - `+` - `,`  **Examples:** An MSKU value of `test%msku` is encoded as `test%2525msku`. An MSKU value of `test,msku` is encoded as `test%252Cmsku`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
mskus = ['mskus_example'] # list[str] | A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
marketplace_id = 'marketplace_id_example' # str | The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    api_response = api_instance.list_item_compliance_details(mskus, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_item_compliance_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mskus** | [**list[str]**](str.md)| A list of merchant SKUs, a merchant-supplied identifier of a specific SKU. | 
 **marketplace_id** | **str**| The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**ListItemComplianceDetailsResponse**](ListItemComplianceDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packing_group_boxes**
> ListPackingGroupBoxesResponse list_packing_group_boxes(inbound_plan_id, packing_group_id, page_size=page_size, pagination_token=pagination_token)



Retrieves a page of boxes from a given packing group. These boxes were previously provided through the `setPackingInformation` operation. This API is used for workflows where boxes are packed before Amazon determines shipment splits.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
packing_group_id = 'packing_group_id_example' # str | Identifier of a packing group.
page_size = 10 # int | The number of packing group boxes to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_packing_group_boxes(inbound_plan_id, packing_group_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_packing_group_boxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **packing_group_id** | **str**| Identifier of a packing group. | 
 **page_size** | **int**| The number of packing group boxes to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListPackingGroupBoxesResponse**](ListPackingGroupBoxesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packing_group_items**
> ListPackingGroupItemsResponse list_packing_group_items(inbound_plan_id, packing_group_id, page_size=page_size, pagination_token=pagination_token)



Retrieves a page of items in a given packing group. Packing options must first be generated by the corresponding operation before packing group items can be listed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
packing_group_id = 'packing_group_id_example' # str | Identifier of a packing group.
page_size = 10 # int | The number of packing group items to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_packing_group_items(inbound_plan_id, packing_group_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_packing_group_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **packing_group_id** | **str**| Identifier of a packing group. | 
 **page_size** | **int**| The number of packing group items to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListPackingGroupItemsResponse**](ListPackingGroupItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packing_options**
> ListPackingOptionsResponse list_packing_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)



Retrieves a list of all packing options for an inbound plan. Packing options must first be generated by the corresponding operation before becoming available.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
page_size = 10 # int | The number of packing options to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_packing_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_packing_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of packing options to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListPackingOptionsResponse**](ListPackingOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_placement_options**
> ListPlacementOptionsResponse list_placement_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)



Provides a list of all placement options for an inbound plan. Placement options must first be generated by the corresponding operation before becoming available.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
page_size = 10 # int | The number of placement options to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_placement_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_placement_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of placement options to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListPlacementOptionsResponse**](ListPlacementOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prep_details**
> ListPrepDetailsResponse list_prep_details(marketplace_id, mskus)



Get preparation details for a list of MSKUs in a specified marketplace.\\n\\n**Note:** MSKUs that contain certain characters must be encoded. For more information, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).\\n\\nThe following characters must be double percent encoded:\\n\\n- `%`\\n- `+`\\n- `,`\\n\\n**Examples:** An MSKU value of `test%msku` is encoded as `test%2525msku`. An MSKU value of `test,msku` is encoded as `test%252Cmsku`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
marketplace_id = 'marketplace_id_example' # str | The marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
mskus = ['mskus_example'] # list[str] | A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.

try:
    api_response = api_instance.list_prep_details(marketplace_id, mskus)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_prep_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
 **mskus** | [**list[str]**](str.md)| A list of merchant SKUs, a merchant-supplied identifier of a specific SKU. | 

### Return type

[**ListPrepDetailsResponse**](ListPrepDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_boxes**
> ListShipmentBoxesResponse list_shipment_boxes(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)



Provides a paginated list of box packages in a shipment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
page_size = 10 # int | The number of boxes to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_shipment_boxes(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_shipment_boxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of boxes to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListShipmentBoxesResponse**](ListShipmentBoxesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_content_update_previews**
> ListShipmentContentUpdatePreviewsResponse list_shipment_content_update_previews(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)



Retrieve a paginated list of shipment content update previews for a given shipment. The shipment content update preview is a summary of the requested shipment content changes along with the transportation cost implications of the change that can only be confirmed prior to the expiry date specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
page_size = 10 # int | The number of content update previews to return. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_shipment_content_update_previews(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_shipment_content_update_previews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of content update previews to return. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListShipmentContentUpdatePreviewsResponse**](ListShipmentContentUpdatePreviewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_items**
> ListShipmentItemsResponse list_shipment_items(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)



Provides a paginated list of item packages in a shipment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
page_size = 10 # int | The number of items to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_shipment_items(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_shipment_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of items to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListShipmentItemsResponse**](ListShipmentItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_pallets**
> ListShipmentPalletsResponse list_shipment_pallets(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)



Provides a paginated list of pallet packages in a shipment. A palletized shipment will have pallets when the related details are provided after generating Less-Than-Truckload (LTL) carrier shipments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
page_size = 10 # int | The number of pallets to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

try:
    api_response = api_instance.list_shipment_pallets(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_shipment_pallets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of pallets to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListShipmentPalletsResponse**](ListShipmentPalletsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transportation_options**
> ListTransportationOptionsResponse list_transportation_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token, placement_option_id=placement_option_id, shipment_id=shipment_id)



Retrieves all transportation options for a shipment. Transportation options must first be generated by the `generateTransportationOptions` operation before becoming available.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
page_size = 10 # int | The number of transportation options to return in the response matching the given query. (optional) (default to 10)
pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)
placement_option_id = 'placement_option_id_example' # str | The placement option to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified. (optional)
shipment_id = 'shipment_id_example' # str | The shipment to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified. (optional)

try:
    api_response = api_instance.list_transportation_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token, placement_option_id=placement_option_id, shipment_id=shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->list_transportation_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of transportation options to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 
 **placement_option_id** | **str**| The placement option to get transportation options for. Either &#x60;placementOptionId&#x60; or &#x60;shipmentId&#x60; must be specified. | [optional] 
 **shipment_id** | **str**| The shipment to get transportation options for. Either &#x60;placementOptionId&#x60; or &#x60;shipmentId&#x60; must be specified. | [optional] 

### Return type

[**ListTransportationOptionsResponse**](ListTransportationOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_self_ship_appointment**
> ScheduleSelfShipAppointmentResponse schedule_self_ship_appointment(inbound_plan_id, shipment_id, slot_id, body)



Confirms or reschedules a self-ship appointment slot against a shipment. Only available in the following [marketplaces](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids): MX, BR, EG, SA, AE, IN. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
slot_id = 'slot_id_example' # str | An identifier to a self-ship appointment slot.
body = swagger_client.ScheduleSelfShipAppointmentRequest() # ScheduleSelfShipAppointmentRequest | The body of the request to `scheduleSelfShipAppointment`.

try:
    api_response = api_instance.schedule_self_ship_appointment(inbound_plan_id, shipment_id, slot_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->schedule_self_ship_appointment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **slot_id** | **str**| An identifier to a self-ship appointment slot. | 
 **body** | [**ScheduleSelfShipAppointmentRequest**](ScheduleSelfShipAppointmentRequest.md)| The body of the request to &#x60;scheduleSelfShipAppointment&#x60;. | 

### Return type

[**ScheduleSelfShipAppointmentResponse**](ScheduleSelfShipAppointmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_packing_information**
> SetPackingInformationResponse set_packing_information(inbound_plan_id, body)



Sets packing information for an inbound plan. This should be called after an inbound plan is created to populate the box level information required for planning and transportation estimates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
body = swagger_client.SetPackingInformationRequest() # SetPackingInformationRequest | The body of the request to `setPackingInformation`.

try:
    api_response = api_instance.set_packing_information(inbound_plan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->set_packing_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**SetPackingInformationRequest**](SetPackingInformationRequest.md)| The body of the request to &#x60;setPackingInformation&#x60;. | 

### Return type

[**SetPackingInformationResponse**](SetPackingInformationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_prep_details**
> SetPrepDetailsResponse set_prep_details(body)



Set the preparation details for a list of MSKUs in a specified marketplace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
body = swagger_client.SetPrepDetailsRequest() # SetPrepDetailsRequest | The body of the request to `setPrepDetails`.

try:
    api_response = api_instance.set_prep_details(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->set_prep_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetPrepDetailsRequest**](SetPrepDetailsRequest.md)| The body of the request to &#x60;setPrepDetails&#x60;. | 

### Return type

[**SetPrepDetailsResponse**](SetPrepDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound_plan_name**
> update_inbound_plan_name(inbound_plan_id, body)



Updates the name of an existing inbound plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
body = swagger_client.UpdateInboundPlanNameRequest() # UpdateInboundPlanNameRequest | The body of the request to `updateInboundPlanName`.

try:
    api_instance.update_inbound_plan_name(inbound_plan_id, body)
except ApiException as e:
    print("Exception when calling FbaInboundApi->update_inbound_plan_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**UpdateInboundPlanNameRequest**](UpdateInboundPlanNameRequest.md)| The body of the request to &#x60;updateInboundPlanName&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_compliance_details**
> UpdateItemComplianceDetailsResponse update_item_compliance_details(marketplace_id, body)



Update compliance details for a list of MSKUs. The details provided here are only used for the India (IN - A21TJRUUN4KGV) marketplace compliance validation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
marketplace_id = 'marketplace_id_example' # str | The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
body = swagger_client.UpdateItemComplianceDetailsRequest() # UpdateItemComplianceDetailsRequest | The body of the request to `updateItemComplianceDetails`.

try:
    api_response = api_instance.update_item_compliance_details(marketplace_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->update_item_compliance_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
 **body** | [**UpdateItemComplianceDetailsRequest**](UpdateItemComplianceDetailsRequest.md)| The body of the request to &#x60;updateItemComplianceDetails&#x60;. | 

### Return type

[**UpdateItemComplianceDetailsResponse**](UpdateItemComplianceDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_name**
> update_shipment_name(inbound_plan_id, shipment_id, body)



Updates the name of an existing shipment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
body = swagger_client.UpdateShipmentNameRequest() # UpdateShipmentNameRequest | The body of the request to `updateShipmentName`.

try:
    api_instance.update_shipment_name(inbound_plan_id, shipment_id, body)
except ApiException as e:
    print("Exception when calling FbaInboundApi->update_shipment_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**UpdateShipmentNameRequest**](UpdateShipmentNameRequest.md)| The body of the request to &#x60;updateShipmentName&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_source_address**
> UpdateShipmentSourceAddressResponse update_shipment_source_address(inbound_plan_id, shipment_id, body)



Updates the source address of an existing shipment. The shipment source address can only be updated prior to the confirmation of the shipment carriers. As a result of the updated source address, existing transportation options will be invalidated and will need to be regenerated to capture the potential difference in transportation options and quotes due to the new source address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
body = swagger_client.UpdateShipmentSourceAddressRequest() # UpdateShipmentSourceAddressRequest | The body of the request to `updateShipmentSourceAddress`.

try:
    api_response = api_instance.update_shipment_source_address(inbound_plan_id, shipment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->update_shipment_source_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**UpdateShipmentSourceAddressRequest**](UpdateShipmentSourceAddressRequest.md)| The body of the request to &#x60;updateShipmentSourceAddress&#x60;. | 

### Return type

[**UpdateShipmentSourceAddressResponse**](UpdateShipmentSourceAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_tracking_details**
> UpdateShipmentTrackingDetailsResponse update_shipment_tracking_details(inbound_plan_id, shipment_id, body)



Updates a shipment's tracking details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FbaInboundApi()
inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
body = swagger_client.UpdateShipmentTrackingDetailsRequest() # UpdateShipmentTrackingDetailsRequest | The body of the request to `updateShipmentTrackingDetails`.

try:
    api_response = api_instance.update_shipment_tracking_details(inbound_plan_id, shipment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FbaInboundApi->update_shipment_tracking_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**UpdateShipmentTrackingDetailsRequest**](UpdateShipmentTrackingDetailsRequest.md)| The body of the request to &#x60;updateShipmentTrackingDetails&#x60;. | 

### Return type

[**UpdateShipmentTrackingDetailsResponse**](UpdateShipmentTrackingDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

