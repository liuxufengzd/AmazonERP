# DirectPurchaseRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ship_to** | [**Address**](Address.md) | The address where the shipment will be delivered. For vendor orders, shipTo information is pulled directly from the Amazon order. | [optional] 
**ship_from** | [**Address**](Address.md) | The address where the package will be picked up. | [optional] 
**return_to** | [**Address**](Address.md) | The address where the package will be returned if it cannot be delivered. | [optional] 
**packages** | [**PackageList**](PackageList.md) |  | [optional] 
**channel_details** | [**ChannelDetails**](ChannelDetails.md) |  | 
**label_specifications** | [**RequestedDocumentSpecification**](RequestedDocumentSpecification.md) | The document (label) specifications requested. The default label returned is PNG DPI 203 4x6 if no label specification is provided. Requesting an invalid file format results in a failure. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


