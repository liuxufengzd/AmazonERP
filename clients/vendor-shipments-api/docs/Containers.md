# Containers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_type** | **str** | The type of container. | 
**container_sequence_number** | **str** | An integer that must be submitted for multi-box shipments only, where one item may come in separate packages. | [optional] 
**container_identifiers** | [**list[ContainerIdentification]**](ContainerIdentification.md) | A list of carton identifiers. | 
**tracking_number** | **str** | The tracking number used for identifying the shipment. | [optional] 
**dimensions** | [**Dimensions**](Dimensions.md) |  | [optional] 
**weight** | [**Weight**](Weight.md) |  | [optional] 
**tier** | **int** | Number of layers per pallet. | [optional] 
**block** | **int** | Number of cartons per layer on the pallet. | [optional] 
**inner_containers_details** | [**InnerContainersDetails**](InnerContainersDetails.md) |  | [optional] 
**packed_items** | [**list[PackedItems]**](PackedItems.md) | A list of packed items. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


