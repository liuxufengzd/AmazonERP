# DropOffLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The drop-off location type at the destination address. | 
**attributes** | **dict(str, str)** | Additional information about the drop-off location. This information can vary depending on the type of drop-off location specified in the &#x60;type&#x60; field.  If the &#x60;type&#x60; is set to &#x60;FALLBACK_NEIGHBOR_DELIVERY&#x60;, the &#x60;attributes&#x60; object must include the keys &#x60;neighborName&#x60; and &#x60;houseNumber&#x60; to provide the name and house number of the designated neighbor.  For &#x60;RECEPTIONIST&#x60; type, the &#x60;attributes&#x60; object may include a &#x60;recipientName&#x60; field that contains the name of the person who received or will receive the package. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


