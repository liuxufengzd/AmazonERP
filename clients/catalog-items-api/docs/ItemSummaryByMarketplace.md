# ItemSummaryByMarketplace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplace_id** | **str** | Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
**adult_product** | **bool** | When &#x60;true&#x60;, the Amazon catalog item is intended for an adult audience or is sexual in nature. | [optional] 
**autographed** | **bool** | When &#x60;true&#x60;, the Amazon catalog item is autographed. | [optional] 
**brand** | **str** | Name of the brand that is associated with the Amazon catalog item. | [optional] 
**browse_classification** | [**ItemBrowseClassification**](ItemBrowseClassification.md) | Classification (browse node) that is associated with the Amazon catalog item. | [optional] 
**color** | **str** | The color that is associated with the Amazon catalog item. | [optional] 
**contributors** | [**list[ItemContributor]**](ItemContributor.md) | Individual contributors to the creation of the item, such as the authors or actors. | [optional] 
**item_classification** | **str** | Classification type that is associated with the Amazon catalog item. | [optional] 
**item_name** | **str** | The name that is associated with the Amazon catalog item. | [optional] 
**manufacturer** | **str** | The name of the manufacturer that is associated with the Amazon catalog item. | [optional] 
**memorabilia** | **bool** | When true, the item is classified as memorabilia. | [optional] 
**model_number** | **str** | The model number that is associated with the Amazon catalog item. | [optional] 
**package_quantity** | **int** | The quantity of the Amazon catalog item within one package. | [optional] 
**part_number** | **str** | The part number that is associated with the Amazon catalog item. | [optional] 
**release_date** | **date** | The earliest date on which the Amazon catalog item can be shipped to customers. | [optional] 
**size** | **str** | The name of the size of the Amazon catalog item. | [optional] 
**style** | **str** | The name of the style that is associated with the Amazon catalog item. | [optional] 
**trade_in_eligible** | **bool** | When true, the Amazon catalog item is eligible for trade-in. | [optional] 
**website_display_group** | **str** | The identifier of the website display group that is associated with the Amazon catalog item. | [optional] 
**website_display_group_name** | **str** | The display name of the website display group that is associated with the Amazon catalog item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


