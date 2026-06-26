# RejectedShippingService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_name** | **str** | The rejected shipping carrier name. For example, USPS. | 
**shipping_service_name** | **str** | The rejected shipping service localized name. For example, FedEx Standard Overnight. | 
**shipping_service_id** | [**ShippingServiceIdentifier**](ShippingServiceIdentifier.md) | The rejected shipping service identifier. For example, &#x60;FEDEX_PTP_STANDARD_OVERNIGHT&#x60;. | 
**rejection_reason_code** | **str** | A reason code meant to be consumed programatically. For example, &#x60;CARRIER_CANNOT_SHIP_TO_POBOX&#x60;. | 
**rejection_reason_message** | **str** | A localized human readable description of the rejected reason. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


