# Vehicle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**make** | **str** | Vehicle Brand. | 
**model** | **str** | Specific model of a vehicle. | 
**variant_name** | **str** | Name of the vehicle variant. | [optional] 
**body_style** | **str** | Body style of vehicle (example: Hatchback, Cabriolet). | [optional] 
**drive_type** | **str** | Drive type of vehicle(example: Rear wheel drive). | [optional] 
**energy** | **str** | Energy Source for the vehicle(example: Petrol) | [optional] 
**engine_output** | [**list[EngineOutput]**](EngineOutput.md) | Engine output of vehicle. | [optional] 
**manufacturing_start_date** | [**MonthAndYear**](MonthAndYear.md) | Vehicle manufacturing start date. | [optional] 
**manufacturing_stop_date** | [**MonthAndYear**](MonthAndYear.md) | Vehicle manufacturing stop date. If it is empty, then the vehicle is still being manufactured. | [optional] 
**last_processed_date** | **str** | The date on which the vehicle was last updated, in ISO-8601 date/time format. | [optional] 
**status** | [**VehicleStatusInCatalog**](VehicleStatusInCatalog.md) | Denotes if the vehicle is active or deleted from Amazon&#39;s catalog. | [optional] 
**identifiers** | [**list[VehicleIdentifiers]**](VehicleIdentifiers.md) | Identifiers that can be used to identify the vehicle uniquely | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


