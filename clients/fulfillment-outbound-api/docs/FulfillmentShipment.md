# FulfillmentShipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_shipment_id** | **str** | A shipment identifier assigned by Amazon. | 
**fulfillment_center_id** | **str** | An identifier for the fulfillment center from which the shipment is sent. | 
**fulfillment_shipment_status** | **str** | The current status of the shipment. | 
**shipping_date** | [**Timestamp**](Timestamp.md) | The meaning of the &#x60;shippingDate&#x60; value depends on the current status of the shipment. If the current value of FulfillmentShipmentStatus is:  * Pending - shippingDate represents the estimated time that the shipment will leave the Amazon fulfillment center.  * Shipped - shippingDate represents the date that the shipment left the Amazon fulfillment center.  If a shipment includes more than one package, &#x60;shippingDate&#x60; applies to all of the packages in the shipment. If the value of &#x60;FulfillmentShipmentStatus&#x60; is &#x60;CancelledByFulfiller&#x60; or &#x60;CancelledBySeller&#x60;, &#x60;shippingDate&#x60; is not returned. The value must be in ISO 8601 date time format. | [optional] 
**estimated_arrival_date** | [**Timestamp**](Timestamp.md) | The estimated arrival date and time of the shipment, in ISO 8601 date time format. Note that this value can change over time. If a shipment includes more than one package, &#x60;estimatedArrivalDate&#x60; applies to all of the packages in the shipment. If the shipment is cancelled, &#x60;estimatedArrivalDate&#x60; is not returned. | [optional] 
**shipping_notes** | **list[str]** | Provides additional insight into shipment timeline. Primarily used to communicate that actual delivery dates aren&#39;t available. | [optional] 
**fulfillment_shipment_item** | [**FulfillmentShipmentItemList**](FulfillmentShipmentItemList.md) |  | 
**fulfillment_shipment_package** | [**FulfillmentShipmentPackageList**](FulfillmentShipmentPackageList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


