# ShipmentTransportationConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_information** | [**ContactInformation**](ContactInformation.md) |  | [optional] 
**freight_information** | [**FreightInformation**](FreightInformation.md) |  | [optional] 
**pallets** | [**list[PalletInput]**](PalletInput.md) | List of pallet configuration inputs. | [optional] 
**ready_to_ship_window** | [**WindowInput**](WindowInput.md) | The range of dates within which the seller intends to ship their items. This is the pick-up date or &#39;ready to ship&#39; date, not an estimated delivery date. | 
**shipment_id** | **str** | Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


