# FulfillmentShipmentPackage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_number** | **int** | Identifies a package in a shipment. | 
**carrier_code** | **str** | Identifies the carrier who will deliver the shipment to the recipient. | 
**tracking_number** | **str** | The tracking number, if provided, can be used to obtain tracking and delivery information. | [optional] 
**amazon_fulfillment_tracking_number** | **str** | The Amazon fulfillment tracking number, if provided, can be used to obtain tracking and delivery information. | [optional] 
**estimated_arrival_date** | [**Timestamp**](Timestamp.md) | The estimated arrival date and time of the package, in ISO 8601 date time format. | [optional] 
**locker_details** | [**LockerDetails**](LockerDetails.md) | The locker details, if provided can be used to access locker delivery box. | [optional] 
**delivery_information** | [**DeliveryInformation**](DeliveryInformation.md) | The delivery information of the package, this information is only available post package delivery to its intended destination. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


