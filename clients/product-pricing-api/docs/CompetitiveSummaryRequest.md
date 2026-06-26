# CompetitiveSummaryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | [**Asin**](Asin.md) | The Amazon Standard Identification Number for the item. | 
**marketplace_id** | [**MarketplaceId**](MarketplaceId.md) | A marketplace identifier. | 
**included_data** | [**list[CompetitiveSummaryIncludedData]**](CompetitiveSummaryIncludedData.md) | The list of requested competitive pricing data for the product. | 
**lowest_priced_offers_inputs** | [**list[LowestPricedOffersInput]**](LowestPricedOffersInput.md) | The list of &#x60;lowestPricedOffersInput&#x60; parameters that are used to build &#x60;lowestPricedOffers&#x60; in the response. This attribute is only valid if &#x60;lowestPricedOffers&#x60; is requested in &#x60;includedData&#x60; | [optional] 
**method** | [**HttpMethod**](HttpMethod.md) | HTTP method type | 
**uri** | [**HttpUri**](HttpUri.md) | The URI associated with the individual APIs that are called as part of the batch request. For &#x60;getCompetitiveSummary&#x60;, this is &#x60;/products/pricing/2022-05-01/items/competitiveSummary&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


