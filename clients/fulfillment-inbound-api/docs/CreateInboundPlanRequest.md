# CreateInboundPlanRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_marketplaces** | **list[str]** | Marketplaces where the items need to be shipped to. Currently only one marketplace can be selected in this request. | 
**items** | [**list[ItemInput]**](ItemInput.md) | Items included in this plan. | 
**name** | **str** | Name for the Inbound Plan. If one isn&#39;t provided, a default name will be provided. | [optional] 
**source_address** | [**AddressInput**](AddressInput.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


