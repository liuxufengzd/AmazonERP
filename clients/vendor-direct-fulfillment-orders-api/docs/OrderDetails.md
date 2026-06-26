# OrderDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_order_number** | **str** | The customer order number. | 
**order_date** | **datetime** | The date the order was placed. This  field is expected to be in ISO-8601 date/time format, for example:2018-07-16T23:00:00Z/ 2018-07-16T23:00:00-05:00 /2018-07-16T23:00:00-08:00. If no time zone is specified, UTC should be assumed. | 
**order_status** | **str** | Current status of the order. | [optional] 
**shipment_details** | [**ShipmentDetails**](ShipmentDetails.md) |  | 
**tax_total** | [**TaxItemDetails**](TaxItemDetails.md) |  | [optional] 
**selling_party** | [**PartyIdentification**](PartyIdentification.md) | PartyID of vendor code. | 
**ship_from_party** | [**PartyIdentification**](PartyIdentification.md) | PartyID of vendor&#39;s warehouse. | 
**ship_to_party** | [**Address**](Address.md) | Name/Address and tax details of the ship to party. | 
**bill_to_party** | [**PartyIdentification**](PartyIdentification.md) | Name/Address and tax details of the bill to party. | 
**has_customizable_items** | **bool** | When &#x60;true&#x60;, the order contains customizable items. | [optional] 
**items** | [**list[OrderItem]**](OrderItem.md) | A list of items in this purchase order. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


