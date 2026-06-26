# GetSellingPartnerMetricsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_frequency** | [**AggregationFrequency**](AggregationFrequency.md) |  | [optional] 
**time_interval** | [**TimeInterval**](TimeInterval.md) | A time interval used to compute metrics. | 
**metrics** | [**list[Metric]**](Metric.md) | The list of metrics requested. If no metric value is provided, data for all metrics will be returned. | [optional] 
**filters** | [**GetSellingPartnerMetricsRequestFilters**](GetSellingPartnerMetricsRequestFilters.md) | Use these parameters to filter results. Any result must match all provided parameters. For parameters that accept multiple values (arrays), the API returns results that match at least one value in the array. | [optional] 
**time_period_type** | [**TimePeriodType**](TimePeriodType.md) |  | 
**marketplace_id** | [**MarketplaceId**](MarketplaceId.md) | The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE, and JP. The supported marketplaces for vendors only are BR, AU, MX, AE, and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace. | 
**program_types** | [**ProgramTypes**](ProgramTypes.md) | The list of replenishment program types for which to return metrics. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


