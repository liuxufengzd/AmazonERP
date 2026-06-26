# CreateFulfillmentOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplace_id** | **str** | The marketplace the fulfillment order is placed against. | [optional] 
**seller_fulfillment_order_id** | **str** | A fulfillment order identifier that the seller creates to track their fulfillment order. The &#x60;sellerFulfillmentOrderId&#x60; must be unique for each fulfillment order that a seller creates. If the seller&#39;s system already creates unique order identifiers, then these might be good values for them to use. | 
**displayable_order_id** | **str** | A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of &#x60;displayableOrderId&#x60; should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.  The value must be an alpha-numeric or ISO 8859-1 compliant string from one to 40 characters in length. Cannot contain two spaces in a row. Leading and trailing white space is removed. | 
**displayable_order_date** | [**Timestamp**](Timestamp.md) | The date and time of the fulfillment order. Displays as the order date in recipient-facing materials such as the outbound shipment packing slip. | 
**displayable_order_comment** | **str** | Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip. | 
**shipping_speed_category** | [**ShippingSpeedCategory**](ShippingSpeedCategory.md) | The shipping method for the fulfillment order. When this value is &#x60;ScheduledDelivery&#x60;, choose Ship for the &#x60;fulfillmentAction&#x60;. Hold is not a valid &#x60;fulfillmentAction&#x60; value when the &#x60;shippingSpeedCategory&#x60; value is &#x60;ScheduledDelivery&#x60;. Note: Shipping method service level agreements vary by marketplace. Sellers can refer to [Seller Central]( https://developer-docs.amazon.com/sp-api/docs/seller-central-urls) for shipping method service-level agreements and multi-channel fulfillment fees. | 
**delivery_window** | [**DeliveryWindow**](DeliveryWindow.md) |  | [optional] 
**destination_address** | [**Address**](Address.md) | The destination address for the fulfillment order. | 
**delivery_preferences** | [**DeliveryPreferences**](DeliveryPreferences.md) | The delivery preferences applied to the destination address. These preferences are applied when possible and are best effort. For eligible orders, the default delivery preference is to leave the package unattended at the front door. This feature is currently supported only in the JP marketplace and not applicable for other marketplaces. For eligible orders, the default delivery preference will be to deliver the package unattended at the front door, unless you specify otherwise. | [optional] 
**fulfillment_action** | [**FulfillmentAction**](FulfillmentAction.md) |  | [optional] 
**fulfillment_policy** | [**FulfillmentPolicy**](FulfillmentPolicy.md) |  | [optional] 
**cod_settings** | [**CODSettings**](CODSettings.md) |  | [optional] 
**ship_from_country_code** | **str** | The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format. | [optional] 
**notification_emails** | [**NotificationEmailList**](NotificationEmailList.md) |  | [optional] 
**feature_constraints** | [**list[FeatureSettings]**](FeatureSettings.md) | A list of features and their fulfillment policies to apply to the order. | [optional] 
**items** | [**CreateFulfillmentOrderItemList**](CreateFulfillmentOrderItemList.md) | A list of items to include in the fulfillment order preview, including quantity. Maximum of 100 line items with a maximum of 250 units per order. | 
**payment_information** | [**PaymentInformationList**](PaymentInformationList.md) | An array of various payment attributes related to this fulfillment order. This property is required if the order is placed against the India marketplace. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


