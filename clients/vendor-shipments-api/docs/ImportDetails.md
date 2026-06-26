# ImportDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_of_payment** | **str** | This is used for import purchase orders only. If the recipient requests, this field will contain the shipment method of payment. | [optional] 
**seal_number** | **str** | The container&#39;s seal number. | [optional] 
**route** | [**Route**](Route.md) | The route and stop details for this shipment. | [optional] 
**import_containers** | **str** | Types and numbers of container(s) for import purchase orders. Can be a comma-separated list if shipment has multiple containers. | [optional] 
**billable_weight** | [**Weight**](Weight.md) | Billable weight of the direct imports shipment. | [optional] 
**estimated_ship_by_date** | **datetime** | Date on which the shipment is expected to be shipped. This value should not be in the past and not more than 60 days out in the future. | [optional] 
**handling_instructions** | **str** | Identification of the instructions on how specified item/carton/pallet should be handled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


