# OrderAcknowledgementItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_sequence_number** | **str** | Line item sequence number for the item. | [optional] 
**amazon_product_identifier** | **str** | Amazon Standard Identification Number (ASIN) of an item. | [optional] 
**vendor_product_identifier** | **str** | The vendor selected product identification of the item. Should be the same as was sent in the purchase order. | [optional] 
**ordered_quantity** | [**ItemQuantity**](ItemQuantity.md) | The quantity of this item ordered. | 
**net_cost** | [**Money**](Money.md) | The net cost of an item per each or weight unit that must match the cost on the invoice. This is a required field. If left blank, Amazon systems will reject the file. Price information must not be zero or negative. | [optional] 
**list_price** | [**Money**](Money.md) | The list price of an item per each or weight unit. Required only if a vendor sells books at list price. | [optional] 
**discount_multiplier** | **str** | The discount multiplier that should be applied to the price if a vendor sells books with a list price. This is a multiplier factor to arrive at a final discounted price. A multiplier of .90 would be the factor if a 10% discount is given. | [optional] 
**item_acknowledgements** | [**list[OrderItemAcknowledgement]**](OrderItemAcknowledgement.md) | This is used to indicate acknowledged quantity. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


