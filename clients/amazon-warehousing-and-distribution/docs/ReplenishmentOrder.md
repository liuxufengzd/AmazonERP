# ReplenishmentOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_on** | **datetime** | Date on which this replenishment order was confirmed. | [optional] 
**created_at** | **datetime** | Date on which this replenishment order was created. | [optional] 
**distribution_ineligible_reasons** | [**list[DistributionIneligibleReason]**](DistributionIneligibleReason.md) | Distribution errors associated with the order related to the products or packages to replenish. This field will be populated if the order has products or packages which failed validation. | [optional] 
**eligible_products** | [**list[DistributionProduct]**](DistributionProduct.md) | List of product units that are eligible for replenishment. | [optional] 
**order_id** | **str** | Order Id of the replenishment order. | 
**status** | [**ReplenishmentOrderStatus**](ReplenishmentOrderStatus.md) |  | 
**outbound_shipments** | [**list[OutboundShipmentSummary]**](OutboundShipmentSummary.md) | List of outbound shipments that are part of this order. | 
**products** | [**list[DistributionProduct]**](DistributionProduct.md) | Requested amount of single product units to be replenished. | [optional] 
**shipped_products** | [**list[DistributionProduct]**](DistributionProduct.md) | Outbound product units that are shipped after the execution has completed post confirmation. | [optional] 
**updated_at** | **datetime** | Date on which this replenishment order was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


