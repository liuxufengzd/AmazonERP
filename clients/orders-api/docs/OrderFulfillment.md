# OrderFulfillment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_status** | [**FulfillmentStatus**](FulfillmentStatus.md) | The current status of the order in the fulfillment process, from pending to handover to carrier. | 
**fulfilled_by** | **str** | Specifies whether Amazon or the merchant is responsible for fulfilling this order.  **Possible values**: &#x60;AMAZON&#x60;, &#x60;MERCHANT&#x60;. | [optional] 
**fulfillment_service_level** | **str** | The category of the shipping speed option selected by the customer at checkout.  **Possible values**: &#x60;EXPEDITED&#x60;, &#x60;FREE_ECONOMY&#x60;, &#x60;NEXT_DAY&#x60;, &#x60;PRIORITY&#x60;, &#x60;SAME_DAY&#x60;, &#x60;SECOND_DAY&#x60;, &#x60;SCHEDULED&#x60;, &#x60;STANDARD&#x60;. | [optional] 
**ship_by_window** | [**DateTimeRange**](DateTimeRange.md) | The promised time period within which the order must be shipped to meet the customer&#39;s delivery expectations. | [optional] 
**deliver_by_window** | [**DateTimeRange**](DateTimeRange.md) | The promised time period within which the order should be delivered to the customer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


