# ReturnItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_return_item_id** | **str** | An identifier the seller assigns to the return item. | 
**seller_fulfillment_order_item_id** | **str** | The identifier assigned to the item by the seller when the fulfillment order was created. | 
**amazon_shipment_id** | **str** | The identifier for the shipment that is associated with the return item. | 
**seller_return_reason_code** | **str** | The return reason code assigned to the return item by the seller. | 
**return_comment** | **str** | An optional comment about the return item. | [optional] 
**amazon_return_reason_code** | **str** | The return reason code that the Amazon fulfillment center assigned to the return item. | [optional] 
**status** | [**FulfillmentReturnItemStatus**](FulfillmentReturnItemStatus.md) | Indicates if the return item has been processed by an Amazon fulfillment center. | 
**status_changed_date** | [**Timestamp**](Timestamp.md) | Indicates when the status last changed. | 
**return_authorization_id** | **str** | Identifies the return authorization used to return this item. Refer to &#x60;ReturnAuthorization&#x60;. | [optional] 
**return_received_condition** | [**ReturnItemDisposition**](ReturnItemDisposition.md) |  | [optional] 
**fulfillment_center_id** | **str** | The identifier for the Amazon fulfillment center that processed the return item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


