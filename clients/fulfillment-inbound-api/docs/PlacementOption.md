# PlacementOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discounts** | [**list[Incentive]**](Incentive.md) | Discount for the offered option. | 
**expiration** | **datetime** | The expiration date of the placement option. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern &#x60;yyyy-MM-ddTHH:mm:ss.sssZ&#x60;. | [optional] 
**fees** | [**list[Incentive]**](Incentive.md) | The fee for the offered option. | 
**placement_option_id** | **str** | The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs. | 
**shipment_ids** | **list[str]** | Shipment ids. | 
**status** | **str** | The status of a placement option. Possible values: &#x60;OFFERED&#x60;, &#x60;ACCEPTED&#x60;, &#x60;EXPIRED&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


