# ShippingService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_service_name** | **str** | A plain text representation of a carrier&#39;s shipping service. For example, \&quot;UPS Ground\&quot; or \&quot;FedEx Standard Overnight\&quot;.  | 
**carrier_name** | **str** | The name of the carrier. | 
**shipping_service_id** | [**ShippingServiceIdentifier**](ShippingServiceIdentifier.md) |  | 
**shipping_service_offer_id** | **str** | An Amazon-defined shipping service offer identifier. | 
**ship_date** | [**Timestamp**](Timestamp.md) | The date that the carrier will ship the package. | 
**earliest_estimated_delivery_date** | [**Timestamp**](Timestamp.md) | The earliest date by which the shipment will be delivered. | [optional] 
**latest_estimated_delivery_date** | [**Timestamp**](Timestamp.md) | The latest date by which the shipment will be delivered. | [optional] 
**rate** | [**CurrencyAmount**](CurrencyAmount.md) | The amount that the carrier will charge for the shipment. | 
**rate_with_adjustments** | [**CurrencyAmount**](CurrencyAmount.md) | The amount that the carrier will charge for the shipment with adjustments. | 
**adjustment_item_list** | [**AdjustmentItemList**](AdjustmentItemList.md) | A list of adjustments applied to a shipping service. | [optional] 
**shipping_service_options** | [**ShippingServiceOptions**](ShippingServiceOptions.md) | Extra services offered by the carrier. | 
**available_shipping_service_options** | [**AvailableShippingServiceOptions**](AvailableShippingServiceOptions.md) |  | [optional] 
**available_label_formats** | [**LabelFormatList**](LabelFormatList.md) |  | [optional] 
**available_format_options_for_label** | [**AvailableFormatOptionsForLabelList**](AvailableFormatOptionsForLabelList.md) |  | [optional] 
**requires_additional_seller_inputs** | **bool** | When true, additional seller inputs are required. | 
**benefits** | [**Benefits**](Benefits.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


