# GetFeatureSkuResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplace_id** | **str** | The requested marketplace. | 
**feature_name** | **str** | The name of the feature. | 
**is_eligible** | **bool** | When true, the seller SKU is eligible for the requested feature. | 
**ineligible_reasons** | **list[str]** | A list of one or more reasons that the seller SKU is ineligible for the feature.  Possible values: * &#x60;MERCHANT_NOT_ENROLLED&#x60;: The merchant isn&#39;t enrolled for the feature. * &#x60;SKU_NOT_ELIGIBLE&#x60;: The SKU doesn&#39;t reside in a warehouse that supports the feature. * &#x60;INVALID_SKU&#x60;: There is an issue with the SKU provided. | [optional] 
**seller_sku** | **str** | Used to identify an item in the given marketplace. SellerSKU is qualified by the seller&#39;s SellerId, which is included with every operation that you submit. | [optional] 
**fn_sku** | **str** | The unique SKU used by Amazon&#39;s fulfillment network. | [optional] 
**asin** | **str** | The Amazon Standard Identification Number (ASIN) of the item. | [optional] 
**sku_count** | **float** | The number of SKUs available for this service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


