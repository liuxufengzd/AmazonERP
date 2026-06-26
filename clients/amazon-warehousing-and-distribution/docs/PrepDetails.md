# PrepDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_owner** | [**LabelOwner**](LabelOwner.md) |  | [optional] 
**prep_category** | [**PrepCategory**](PrepCategory.md) | The preparation category for shipping an item to Amazon&#39;s fulfillment network. | [optional] 
**prep_instructions** | [**list[PrepInstruction]**](PrepInstruction.md) | Contains information about the preparation of the inbound products. The system auto-generates this field with the use of the &#x60;prepCategory&#x60;, and if you attempt to pass a value for this field, the system will ignore it. | [optional] 
**prep_owner** | [**PrepOwner**](PrepOwner.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


