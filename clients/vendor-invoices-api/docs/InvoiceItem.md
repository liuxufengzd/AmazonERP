# InvoiceItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_sequence_number** | **int** | Unique number related to this line item. | 
**amazon_product_identifier** | **str** | Amazon Standard Identification Number (ASIN) of an item. | [optional] 
**vendor_product_identifier** | **str** | The vendor selected product identifier of the item. Should be the same as was provided in the purchase order. | [optional] 
**invoiced_quantity** | [**ItemQuantity**](ItemQuantity.md) | Invoiced quantity of this item. Quantity must be greater than zero. | 
**net_cost** | [**Money**](Money.md) | The item cost to Amazon, which should match the cost on the order. Price information should not be zero or negative. It indicates net unit price. Net cost means VAT is not included in cost. If items are priced by weight, this cost need to be considered in conjunction with netCostUnitOfMeasure. E.g.: $5/LB | 
**net_cost_unit_of_measure** | [**NetCostUnitOfMeasure**](NetCostUnitOfMeasure.md) | This field represents weight unit of measure of items that are ordered by cases and supporting priced by weight. | [optional] 
**purchase_order_number** | **str** | The Amazon purchase order number for this invoiced line item. Formatting Notes: 8-character alpha-numeric code. This value is mandatory only when invoiceType is Invoice, and is not required when invoiceType is CreditNote. | [optional] 
**hsn_code** | **str** | HSN Tax code. The HSN number cannot contain alphabets. | [optional] 
**credit_note_details** | [**CreditNoteDetails**](CreditNoteDetails.md) | Details required in order to process a credit note. This information is required only if invoiceType is CreditNote. | [optional] 
**tax_details** | [**list[TaxDetails]**](TaxDetails.md) | Individual tax details per line item. | [optional] 
**charge_details** | [**list[ChargeDetails]**](ChargeDetails.md) | Individual charge details per line item. | [optional] 
**allowance_details** | [**list[AllowanceDetails]**](AllowanceDetails.md) | Individual allowance details per line item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


