# Container

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_type** | **str** | The type of container. | 
**container_identifier** | **str** | The container identifier. | 
**tracking_number** | **str** | The tracking number. | [optional] 
**manifest_id** | **str** | The manifest identifier. | [optional] 
**manifest_date** | **str** | The date of the manifest. | [optional] 
**ship_method** | **str** | The shipment method. This property is required when calling the &#x60;submitShipmentConfirmations&#x60; operation, and optional otherwise. | [optional] 
**scac_code** | **str** | SCAC code required for NA VOC vendors only. | [optional] 
**carrier** | **str** | Carrier required for EU VOC vendors only. | [optional] 
**container_sequence_number** | **int** | An integer that must be submitted for multi-box shipments only, where one item may come in separate packages. | [optional] 
**dimensions** | [**Dimensions**](Dimensions.md) |  | [optional] 
**weight** | [**Weight**](Weight.md) |  | 
**packed_items** | [**list[PackedItem]**](PackedItem.md) | A list of packed items. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


