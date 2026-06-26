# OrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_sequence_number** | **str** | Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on. | 
**buyer_product_identifier** | **str** | Buyer&#39;s standard identification number (ASIN) of an item. | [optional] 
**vendor_product_identifier** | **str** | The vendor selected product identification of the item. | [optional] 
**title** | **str** | Title for the item. | [optional] 
**ordered_quantity** | [**ItemQuantity**](ItemQuantity.md) | Item quantity ordered. | 
**scheduled_delivery_shipment** | [**ScheduledDeliveryShipment**](ScheduledDeliveryShipment.md) | Details for the scheduled delivery shipment. | [optional] 
**gift_details** | [**GiftDetails**](GiftDetails.md) | Gift message and wrapId details. | [optional] 
**net_price** | [**Money**](Money.md) | Net price (before tax) to vendor with currency details. | 
**tax_details** | [**TaxItemDetails**](TaxItemDetails.md) | Total tax details for the line item. | [optional] 
**total_price** | [**Money**](Money.md) | The price to Amazon each (cost). | [optional] 
**buyer_customized_info** | [**BuyerCustomizedInfoDetail**](BuyerCustomizedInfoDetail.md) | The buyer information for products the vendor has configured as customizable, specifying the types of customizations or configurations along with types and ranges for their product. This provides the ability for buyers to customize multiple aspects of the products according to what the vendor allows. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


