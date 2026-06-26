# CreateFulfillmentOrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_sku** | **str** | The seller SKU of the item. | 
**seller_fulfillment_order_item_id** | **str** | A fulfillment order item identifier that the seller creates to track fulfillment order items. Used to disambiguate multiple fulfillment items that have the same &#x60;sellerSku&#x60; value. For example, the seller might assign different &#x60;sellerFulfillmentOrderItemId&#x60; values to two items in a fulfillment order that share the same &#x60;sellerSku&#x60; value but have different &#x60;giftMessage&#x60; values. | 
**quantity** | [**Quantity**](Quantity.md) |  | 
**gift_message** | **str** | A message to the gift recipient, if applicable. | [optional] 
**displayable_comment** | **str** | Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip. | [optional] 
**fulfillment_network_sku** | **str** | Amazon&#39;s fulfillment network SKU of the item. | [optional] 
**per_unit_declared_value** | [**Money**](Money.md) | The monetary value assigned by the seller to this item. This is a required field for India MCF orders. | [optional] 
**per_unit_price** | [**Money**](Money.md) | The amount to be collected from the recipient for this item in a COD (Cash On Delivery) order. | [optional] 
**per_unit_tax** | [**Money**](Money.md) | The tax on the amount to be collected from the recipient for this item in a COD (Cash On Delivery) order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


