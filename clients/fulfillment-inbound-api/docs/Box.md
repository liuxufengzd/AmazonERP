# Box

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_id** | **str** | The ID provided by Amazon that identifies a given box. This ID is comprised of the external shipment ID (which is generated after transportation has been confirmed) and the index of the box. | [optional] 
**content_information_source** | [**BoxContentInformationSource**](BoxContentInformationSource.md) |  | [optional] 
**destination_region** | [**Region**](Region.md) |  | [optional] 
**dimensions** | [**Dimensions**](Dimensions.md) |  | [optional] 
**external_container_identifier** | **str** | The external identifier for this container / box. | [optional] 
**external_container_identifier_type** | **str** | Type of the external identifier used. Can be: &#x60;AMAZON&#x60;, &#x60;SSCC&#x60;. | [optional] 
**items** | [**list[Item]**](Item.md) | Items contained within the box. | [optional] 
**package_id** | **str** | Primary key to uniquely identify a Package (Box or Pallet). | 
**quantity** | **int** | The number of containers where all other properties like weight or dimensions are identical. | [optional] 
**template_name** | **str** | Template name of the box. | [optional] 
**weight** | [**Weight**](Weight.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


