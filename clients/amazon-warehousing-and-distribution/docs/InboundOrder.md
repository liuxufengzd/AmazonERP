# InboundOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Date when this order was created. | 
**destination_details** | [**DestinationDetails**](DestinationDetails.md) | Destination details of an inbound order based on the assigned region and DC for the order. | [optional] 
**external_reference_id** | **str** | Reference ID that can be used to correlate the order with partner resources. | [optional] 
**order_id** | **str** | Inbound order ID. | 
**order_status** | [**InboundStatus**](InboundStatus.md) | Inbound order status. | 
**origin_address** | [**Address**](Address.md) | Origin address from where the inbound order will be shipped. | 
**packages_to_inbound** | [**list[DistributionPackageQuantity]**](DistributionPackageQuantity.md) | List of packages to be inbounded. | 
**preferences** | [**InboundPreferences**](InboundPreferences.md) |  | [optional] 
**updated_at** | **datetime** | Date when this order was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


