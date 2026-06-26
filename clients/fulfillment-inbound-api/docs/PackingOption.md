# PackingOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discounts** | [**list[Incentive]**](Incentive.md) | Discount for the offered option. | 
**expiration** | **datetime** | The time at which this packing option is no longer valid. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern &#x60;yyyy-MM-ddTHH:mm:ss.sssZ&#x60;. | [optional] 
**fees** | [**list[Incentive]**](Incentive.md) | Fee for the offered option. | 
**packing_groups** | **list[str]** | Packing group IDs. | 
**packing_option_id** | **str** | Identifier of a packing option. | 
**status** | **str** | The status of the packing option. Possible values: &#x60;OFFERED&#x60;, &#x60;ACCEPTED&#x60;, &#x60;EXPIRED&#x60;. | 
**supported_configurations** | [**list[PackingConfiguration]**](PackingConfiguration.md) | A list of possible configurations for this option. | 
**supported_shipping_configurations** | [**list[ShippingConfiguration]**](ShippingConfiguration.md) | **This field is deprecated**. Use the &#x60;shippingRequirements&#x60; property under &#x60;supportedConfigurations&#x60; instead. List of supported shipping modes. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


