# PackageTrackingDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_number** | **int** | The package identifier. | 
**tracking_number** | **str** | The tracking number for the package. | [optional] 
**customer_tracking_link** | **str** | Link on swiship.com that allows customers to track the package. | [optional] 
**carrier_code** | **str** | The name of the carrier. | [optional] 
**carrier_phone_number** | **str** | The phone number of the carrier. | [optional] 
**carrier_url** | **str** | The URL of the carrier&#39;s website. | [optional] 
**ship_date** | [**Timestamp**](Timestamp.md) | The shipping date for the package. | [optional] 
**estimated_arrival_date** | [**Timestamp**](Timestamp.md) | The estimated arrival date. | [optional] 
**ship_to_address** | [**TrackingAddress**](TrackingAddress.md) | The destination city for the package. | [optional] 
**current_status** | [**CurrentStatus**](CurrentStatus.md) |  | [optional] 
**current_status_description** | **str** | Description corresponding to the &#x60;CurrentStatus&#x60; value. | [optional] 
**delivery_window** | [**DateRange**](DateRange.md) | The delivery window for the package. This is available after the package reaches its destination delivery station. | [optional] 
**signed_for_by** | **str** | The name of the person who signed for the package. | [optional] 
**additional_location_info** | [**AdditionalLocationInfo**](AdditionalLocationInfo.md) |  | [optional] 
**tracking_events** | [**TrackingEventList**](TrackingEventList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


