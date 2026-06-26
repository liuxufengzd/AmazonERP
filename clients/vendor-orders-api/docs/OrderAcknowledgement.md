# OrderAcknowledgement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | The purchase order number. Formatting Notes: 8-character alpha-numeric code. | 
**selling_party** | [**PartyIdentification**](PartyIdentification.md) | Name, address and tax details of the party receiving a shipment of products. | 
**acknowledgement_date** | **datetime** | The date and time when the purchase order is acknowledged, in ISO-8601 date/time format. | 
**items** | [**list[OrderAcknowledgementItem]**](OrderAcknowledgementItem.md) | A list of the items being acknowledged with associated details. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


