# SegmentedFeaturedOffer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_id** | **str** | The seller identifier for the offer. | 
**condition** | [**Condition**](Condition.md) | Item Condition. | 
**sub_condition** | **str** | The item subcondition of the offer. | [optional] 
**fulfillment_type** | [**FulfillmentType**](FulfillmentType.md) | The fulfillment type for the offer. Possible values are &#x60;AFN&#x60; (Amazon Fulfillment Network) and &#x60;MFN&#x60; (Merchant Fulfillment Network). | 
**listing_price** | [**MoneyType**](MoneyType.md) | The offer buying price. This doesn&#39;t include shipping, points, or applicable promotions. | 
**shipping_options** | [**list[ShippingOption]**](ShippingOption.md) | A list of shipping options associated with this offer | [optional] 
**points** | [**Points**](Points.md) | The number of Amazon Points that are offered with the purchase of an item and the monetary value of these points. Note that the Points element is only returned in Japan (JP). | [optional] 
**prime_details** | [**PrimeDetails**](PrimeDetails.md) | Amazon Prime details. | [optional] 
**featured_offer_segments** | [**list[FeaturedOfferSegment]**](FeaturedOfferSegment.md) | The list of segment information in which the offer is featured. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


