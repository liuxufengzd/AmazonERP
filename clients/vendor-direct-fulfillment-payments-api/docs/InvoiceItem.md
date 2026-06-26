# InvoiceItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_sequence_number** | **str** | Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on. | 
**buyer_product_identifier** | **str** | Buyer&#39;s standard identification number (ASIN) of an item. | [optional] 
**vendor_product_identifier** | **str** | The vendor selected product identification of the item. | [optional] 
**invoiced_quantity** | [**ItemQuantity**](ItemQuantity.md) | Item quantity invoiced. | 
**net_cost** | [**Money**](Money.md) | Net price (before tax) to vendor with currency details. | 
**purchase_order_number** | **str** | The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code. | 
**vendor_order_number** | **str** | The vendor&#39;s order number for this order. | [optional] 
**hsn_code** | **str** | Harmonized System of Nomenclature (HSN) tax code. The HSN number cannot contain alphabets. | [optional] 
**tax_details** | [**list[TaxDetail]**](TaxDetail.md) | Individual tax details per line item. | [optional] 
**charge_details** | [**list[ChargeDetails]**](ChargeDetails.md) | Individual charge details per line item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


