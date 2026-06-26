# Shipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | [**ShipmentId**](ShipmentId.md) |  | 
**amazon_order_id** | [**AmazonOrderId**](AmazonOrderId.md) |  | 
**seller_order_id** | [**SellerOrderId**](SellerOrderId.md) |  | [optional] 
**item_list** | [**ItemList**](ItemList.md) |  | 
**ship_from_address** | [**Address**](Address.md) | The address of the sender. | 
**ship_to_address** | [**Address**](Address.md) | The destination address for the shipment. | 
**package_dimensions** | [**PackageDimensions**](PackageDimensions.md) |  | 
**weight** | [**Weight**](Weight.md) | The package weight. | 
**insurance** | [**CurrencyAmount**](CurrencyAmount.md) | If you specify &#x60;DeclaredValue&#x60; in a previous call to the &#x60;createShipment&#x60; operation, then &#x60;Insurance&#x60; indicates the shipment insurance amount that the carrier uses. If &#x60;DeclaredValue&#x60; isn&#39;t with a previous call to the &#x60;createShipment&#x60; operation, then the shipment is insured for the carrier&#39;s minimum insurance amount, or the combined sale prices that the items are listed for in the shipment. | 
**shipping_service** | [**ShippingService**](ShippingService.md) |  | 
**label** | [**Label**](Label.md) | Data for creating a shipping label and dimensions for printing the label. If the shipment is canceled, an empty label is returned. | 
**status** | [**ShipmentStatus**](ShipmentStatus.md) | The shipment status. | 
**tracking_id** | [**TrackingId**](TrackingId.md) |  | [optional] 
**created_date** | [**Timestamp**](Timestamp.md) | The date and time the shipment is created. | 
**last_updated_date** | [**Timestamp**](Timestamp.md) | The date and time of the last update. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


