# FulfillmentOrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_sku** | **str** | The seller SKU of the item. | 
**seller_fulfillment_order_item_id** | **str** | A fulfillment order item identifier submitted with a call to the &#x60;createFulfillmentOrder&#x60; operation. | 
**quantity** | [**Quantity**](Quantity.md) |  | 
**gift_message** | **str** | A message to the gift recipient, if applicable. | [optional] 
**displayable_comment** | **str** | Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip. | [optional] 
**fulfillment_network_sku** | **str** | Amazon&#39;s fulfillment network SKU of the item. | [optional] 
**order_item_disposition** | **str** | Indicates whether the item is sellable or unsellable. | [optional] 
**cancelled_quantity** | [**Quantity**](Quantity.md) | The item quantity that was cancelled by the seller. | 
**unfulfillable_quantity** | [**Quantity**](Quantity.md) | The item quantity that is unfulfillable. | 
**estimated_ship_date** | [**Timestamp**](Timestamp.md) | The estimated date and time that the item quantity is scheduled to ship from the fulfillment center. Note that this value can change over time. If the shipment that contains the item quantity is cancelled, &#x60;estimatedShipDate&#x60; is not returned. | [optional] 
**estimated_arrival_date** | [**Timestamp**](Timestamp.md) | The estimated arrival date and time of the item quantity. Note that this value can change over time. If the shipment that contains the item quantity is cancelled, &#x60;estimatedArrivalDate&#x60; is not returned. | [optional] 
**per_unit_price** | [**Money**](Money.md) | The amount to be collected from the recipient for this item in a COD (Cash On Delivery) order. | [optional] 
**per_unit_tax** | [**Money**](Money.md) | The tax on the amount to be collected from the recipient for this item in a COD (Cash On Delivery) order. | [optional] 
**per_unit_declared_value** | [**Money**](Money.md) | The monetary value assigned by the seller to this item. This is a required field for India MCF orders. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


