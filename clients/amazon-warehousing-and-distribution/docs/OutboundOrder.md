# OutboundOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_on** | **datetime** | Date on which this outbound order was confirmed. | [optional] 
**created_at** | **datetime** | Date on which this outbound order was created. | [optional] 
**eligible_packages_to_outbound** | [**list[DistributionPackageQuantity]**](DistributionPackageQuantity.md) | List of packages that are eligible for outbound. | [optional] 
**eligible_products_to_outbound** | [**list[ProductQuantity]**](ProductQuantity.md) | List of product units that are eligible for outbound. | [optional] 
**execution_errors** | [**list[OutboundExecutionError]**](OutboundExecutionError.md) | Execution errors associated with the outbound order. This field will be populated if the order failed validation. | [optional] 
**order_id** | **str** | Order ID for the outbound order. | 
**order_preferences** | [**list[OrderAttribute]**](OrderAttribute.md) | Order preferences for this outbound order. | [optional] 
**order_status** | [**OutboundStatus**](OutboundStatus.md) | Status for the outbound order. | 
**outbound_shipments** | [**list[OutboundShipment]**](OutboundShipment.md) | List of outbound shipments that are part of this order. | 
**packages_to_outbound** | [**list[DistributionPackageQuantity]**](DistributionPackageQuantity.md) | List of packages to be outbound. | [optional] 
**products_to_outbound** | [**list[ProductQuantity]**](ProductQuantity.md) | List of product units to be outbound. | [optional] 
**shipped_outbound_packages** | [**list[DistributionPackageQuantity]**](DistributionPackageQuantity.md) | Outbound packages that are shipped after the execution has completed post confirmation. | [optional] 
**shipped_outbound_products** | [**list[ProductQuantity]**](ProductQuantity.md) | Outbound product units that are shipped after the execution has completed post confirmation. | [optional] 
**updated_at** | **datetime** | Date on which this outbound order was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


