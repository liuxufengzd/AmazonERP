# ProcessingDirective

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_filter** | [**EventFilter**](EventFilter.md) | A &#x60;notificationType&#x60; filter. Note: eventFilter and filterExpression are mutually exclusive, meaning if eventFilter is provided, filterExpression field cannot be used. | [optional] 
**filter_expression** | **str** | An expression for filtering events before delivery to destination based on the notification payload (example: FulfillmentOrderStatusNotification.FulfillmentOrderStatus &#x3D;&#x3D; &#x60;SHIPPED&#x60; ). The &#x60;filterExpression&#x60; is a string that follows the CEL expression syntax (https://github.com/google/cel-spec) excluding arithmetic operators (+, -, *, /, %) and list/map indexing ([]). Refer to Notification Type Values to determine if filter Expression is supported for a Notification Type. Refer to CEL Operators (https://developer-docs.amazon.com/sp-api/docs/filter-notification-subscriptions) to see if a CEL operator is supported.   Note: eventFilter and filterExpression are mutually exclusive. You can use filterExpression to replace existing eventFilter configurations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


