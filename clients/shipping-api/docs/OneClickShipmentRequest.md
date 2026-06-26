# OneClickShipmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ship_to** | [**Address**](Address.md) | The ship to address. | [optional] 
**ship_from** | [**Address**](Address.md) | The ship from address. | 
**return_to** | [**Address**](Address.md) | The return to address. | [optional] 
**ship_date** | **datetime** | The ship date and time (the requested pickup). This defaults to the current date and time. | [optional] 
**goods_owner** | [**GoodsOwner**](GoodsOwner.md) | The seller owning the goods before handing them over to the carrier | [optional] 
**packages** | [**PackageList**](PackageList.md) |  | 
**value_added_services_details** | [**OneClickShipmentValueAddedServiceDetails**](OneClickShipmentValueAddedServiceDetails.md) |  | [optional] 
**tax_details** | [**TaxDetailList**](TaxDetailList.md) |  | [optional] 
**channel_details** | [**ChannelDetails**](ChannelDetails.md) |  | 
**label_specifications** | [**RequestedDocumentSpecification**](RequestedDocumentSpecification.md) |  | 
**service_selection** | [**ServiceSelection**](ServiceSelection.md) |  | 
**shipper_instruction** | [**ShipperInstruction**](ShipperInstruction.md) | Optional field for shipper instruction. | [optional] 
**destination_access_point_details** | [**AccessPointDetails**](AccessPointDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


