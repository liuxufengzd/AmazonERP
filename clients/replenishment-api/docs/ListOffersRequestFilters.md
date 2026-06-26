# ListOffersRequestFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplace_id** | [**MarketplaceId**](MarketplaceId.md) | The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE, and JP. The supported marketplaces for vendors only are BR, AU, MX, AE, and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace. | 
**skus** | **list[str]** | A list of SKUs to filter. This filter is only supported for sellers and not for vendors. | [optional] 
**asins** | **list[str]** | A list of Amazon Standard Identification Numbers (ASINs). | [optional] 
**eligibilities** | [**list[EligibilityStatus]**](EligibilityStatus.md) | A list of eligibilities associated with an offer. | [optional] 
**preferences** | [**Preference**](Preference.md) | Offer preferences to include in the result filter criteria. | [optional] 
**promotions** | [**Promotion**](Promotion.md) | Offer promotions to include in the result filter criteria. | [optional] 
**program_types** | [**ProgramTypes**](ProgramTypes.md) |  | 
**deliveries_conditions** | **list[str]** | A list of delivery condition types to filter the results by. Results are filtered to only include offers with the specified delivery conditions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


