# OrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_sequence_number** | **str** | Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on. | 
**amazon_product_identifier** | **str** | Amazon Standard Identification Number (ASIN) of an item. | [optional] 
**vendor_product_identifier** | **str** | The vendor selected product identification of the item. | [optional] 
**ordered_quantity** | [**ItemQuantity**](ItemQuantity.md) | Item quantity ordered. | 
**is_back_order_allowed** | **bool** | When true, we will accept backorder confirmations for this item. | 
**net_cost** | [**Money**](Money.md) | The net cost of an item per each or weight unit. | [optional] 
**list_price** | [**Money**](Money.md) | The list price of an item per each or weight unit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


