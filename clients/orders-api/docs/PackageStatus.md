# PackageStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Primary status classification of the package in the shipping workflow. | 
**detailed_status** | **str** | Granular status information providing specific details about the package&#39;s current location and handling stage.   **Possible values**: - &#x60;PENDING_SCHEDULE&#x60; (Package awaiting pickup scheduling) - &#x60;PENDING_PICK_UP&#x60; (Package ready for carrier collection from seller) - &#x60;PENDING_DROP_OFF&#x60; (Package awaiting seller delivery to carrier) - &#x60;LABEL_CANCELLED&#x60; (Shipping label canceled by seller) - &#x60;PICKED_UP&#x60; (Package collected by carrier from seller location) - &#x60;DROPPED_OFF&#x60; (Package delivered to carrier by seller) - &#x60;AT_ORIGIN_FC&#x60; (Package at originating fulfillment center) - &#x60;AT_DESTINATION_FC&#x60; (Package at destination fulfillment center) - &#x60;DELIVERED&#x60; (Package successfully delivered to recipient) - &#x60;REJECTED_BY_BUYER&#x60; (Package refused by intended recipient) - &#x60;UNDELIVERABLE&#x60; (Package cannot be delivered due to address or access issues) - &#x60;RETURNING_TO_SELLER&#x60; (Package in transit back to seller) - &#x60;RETURNED_TO_SELLER&#x60; (Package successfully returned to seller) - &#x60;LOST&#x60; (Package location unknown or confirmed lost) - &#x60;OUT_FOR_DELIVERY&#x60; (Package on delivery vehicle for final delivery) - &#x60;DAMAGED&#x60; (Package damaged during transit)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


