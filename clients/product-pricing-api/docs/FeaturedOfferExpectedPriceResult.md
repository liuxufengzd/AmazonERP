# FeaturedOfferExpectedPriceResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featured_offer_expected_price** | [**FeaturedOfferExpectedPrice**](FeaturedOfferExpectedPrice.md) |  | [optional] 
**result_status** | **str** | The status of the FOEP computation. Possible values include &#x60;VALID_FOEP&#x60;, &#x60;NO_COMPETING_OFFER&#x60;, &#x60;OFFER_NOT_ELIGIBLE&#x60;, &#x60;OFFER_NOT_FOUND&#x60;, and &#x60;ASIN_NOT_ELIGIBLE&#x60;. Additional values might be added in the future. | 
**competing_featured_offer** | [**FeaturedOffer**](FeaturedOffer.md) | The offer that will likely be the featured offer if the target offer is priced above its FOEP. If the target offer is currently the featured offer, this property will be different than &#x60;currentFeaturedOffer&#x60;. | [optional] 
**current_featured_offer** | [**FeaturedOffer**](FeaturedOffer.md) | The offer that is currently the featured offer. If the target offer is not currently featured, then this property will be equal to &#x60;competingFeaturedOffer&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


