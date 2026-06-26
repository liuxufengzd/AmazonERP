# OutboundShipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp when the shipment was created. | [optional] 
**destination_address** | [**Address**](Address.md) | Destination address for this shipment. | 
**order_id** | **str** | Outbound order ID this outbound shipment belongs to. | 
**origin_address** | [**Address**](Address.md) | Origin address for this shipment. | 
**shipment_package_quantities** | [**list[DistributionPackageQuantity]**](DistributionPackageQuantity.md) | Specific distribution packages that are included in the context of this shipment. | [optional] 
**shipment_id** | **str** | Unique shipment ID. | 
**shipment_product_quantities** | [**list[ProductQuantity]**](ProductQuantity.md) | Specific product units that are included in the context of this shipment. | [optional] 
**shipment_status** | [**OutboundShipmentStatus**](OutboundShipmentStatus.md) | Current status of this shipment. | 
**updated_at** | **datetime** | Timestamp when the shipment was updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


