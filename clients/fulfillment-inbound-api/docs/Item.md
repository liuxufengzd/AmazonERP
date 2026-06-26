# Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | The Amazon Standard Identification Number (ASIN) of the item. | 
**expiration** | **str** | The expiration date of the MSKU. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern&#x60;YYYY-MM-DD&#x60;. The same MSKU with different expiration dates cannot go into the same box. | [optional] 
**fnsku** | **str** | A unique identifier assigned by Amazon to products stored in and fulfilled from an Amazon fulfillment center. | 
**label_owner** | **str** | Specifies who will label the items. Options include &#x60;AMAZON&#x60;, &#x60;SELLER&#x60;, and &#x60;NONE&#x60;. &#x60;AMAZON&#x60; is not an accepted value in the US marketplace. | 
**manufacturing_lot_code** | **str** | The manufacturing lot code. | [optional] 
**msku** | **str** | The merchant-defined SKU ID. | 
**prep_instructions** | [**list[PrepInstruction]**](PrepInstruction.md) | Special preparations that are required for an item. | 
**quantity** | **int** | The number of the specified MSKU. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


