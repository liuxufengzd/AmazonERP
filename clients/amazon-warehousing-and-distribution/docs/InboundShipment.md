# InboundShipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | [**CarrierCode**](CarrierCode.md) | The shipment carrier code. | [optional] 
**created_at** | **datetime** | Timestamp when the shipment was created. The date is returned in &lt;a href&#x3D;&#39;https://developer-docs.amazon.com/sp-api/docs/iso-8601&#39;&gt;ISO 8601&lt;/a&gt; format. | [optional] 
**destination_address** | [**Address**](Address.md) | Destination address for this shipment. | 
**external_reference_id** | **str** | Client-provided reference ID that can correlate this shipment to client resources. For example, to map this shipment to an internal bookkeeping order record. | [optional] 
**order_id** | **str** | The AWD inbound order ID that this inbound shipment belongs to. | 
**origin_address** | [**Address**](Address.md) | Origin address for this shipment. | 
**received_quantity** | [**list[InventoryQuantity]**](InventoryQuantity.md) | Quantity received (at the receiving end) as part of this shipment. | [optional] 
**ship_by** | **datetime** | Timestamp when the shipment will be shipped. | [optional] 
**shipment_container_quantities** | [**list[DistributionPackageQuantity]**](DistributionPackageQuantity.md) | Packages that are part of this shipment. | 
**shipment_id** | **str** | Unique shipment ID. | 
**shipment_sku_quantities** | [**list[SkuQuantity]**](SkuQuantity.md) | Quantity details at SKU level for the shipment. This attribute will only appear if the skuQuantities parameter in the request is set to SHOW. | [optional] 
**destination_region** | **str** | Assigned region where the order will be shipped. This can differ from what was passed as preference. AWD currently supports following region IDs: [us-west, us-east, us-southcentral, us-southeast] | [optional] 
**shipment_status** | [**InboundShipmentStatus**](InboundShipmentStatus.md) | Current status of this shipment. | 
**tracking_id** | **str** | Carrier-unique tracking ID for this shipment. | [optional] 
**updated_at** | **datetime** | Timestamp when the shipment was updated. The date is returned in &lt;a href&#x3D;&#39;https://developer-docs.amazon.com/sp-api/docs/iso-8601&#39;&gt;ISO 8601&lt;/a&gt; format. | [optional] 
**warehouse_reference_id** | **str** | An AWD-provided reference ID that you can use to interact with the warehouse. For example, a carrier appointment booking. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


