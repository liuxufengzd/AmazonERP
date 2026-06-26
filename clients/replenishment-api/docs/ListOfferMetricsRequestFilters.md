# ListOfferMetricsRequestFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_frequency** | [**AggregationFrequency**](AggregationFrequency.md) |  | [optional] 
**time_interval** | [**TimeInterval**](TimeInterval.md) | A time interval used to compute metrics. | 
**time_period_type** | [**TimePeriodType**](TimePeriodType.md) |  | 
**marketplace_id** | [**MarketplaceId**](MarketplaceId.md) | The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE, and JP. The supported marketplaces for vendors only are BR, AU, MX, AE, and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace. | 
**program_types** | [**ProgramTypes**](ProgramTypes.md) |  | 
**asins** | **list[str]** | A list of Amazon Standard Identification Numbers (ASINs) to filter by. | [optional] 
**skus** | **list[str]** | [Applicable only for Sellers] A list of SKUs to filter by. | [optional] 
**fulfillment_channel_types** | [**list[FulfillmentChannelType]**](FulfillmentChannelType.md) | [Applicable only for Sellers] The fulfillment channel types to filter by. | [optional] 
**brand_names** | **list[str]** | [Applicable only for US marketplace] A list of brand names to filter by. | [optional] 
**product_groups** | **list[str]** | [Applicable only for Vendors] A list of product group names to filter by. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


