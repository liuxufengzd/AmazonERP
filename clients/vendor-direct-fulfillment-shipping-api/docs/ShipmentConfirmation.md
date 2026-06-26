# ShipmentConfirmation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | Purchase order number corresponding to the shipment. | 
**shipment_details** | [**ShipmentDetails**](ShipmentDetails.md) | Shipment information. | 
**selling_party** | [**PartyIdentification**](PartyIdentification.md) | ID of the selling party or vendor. | 
**ship_from_party** | [**PartyIdentification**](PartyIdentification.md) | Warehouse code of vendor. | 
**items** | [**list[Item]**](Item.md) | Provide the details of the items in this shipment. If any of the item details field is common at a package or a pallet level, then provide them at the corresponding package. | 
**containers** | [**list[Container]**](Container.md) | Provide the details of the items in this shipment. If any of the item details field is common at a package or a pallet level, then provide them at the corresponding package. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


