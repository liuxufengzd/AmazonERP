# GetFulfillmentPreviewRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplace_id** | **str** | The marketplace the fulfillment order is placed against. | [optional] 
**address** | [**Address**](Address.md) | The destination address for the fulfillment order preview. | 
**items** | [**GetFulfillmentPreviewItemList**](GetFulfillmentPreviewItemList.md) | Identifying information and quantity information for the items in the fulfillment order preview. Maximum of 100 line items with a maximum of 250 units per order.  | 
**shipping_speed_categories** | [**ShippingSpeedCategoryList**](ShippingSpeedCategoryList.md) | A list of shipping methods used for creating fulfillment order previews.  Possible values:  * &#x60;Standard&#x60;: Standard shipping method. * &#x60;Expedited&#x60;: Expedited shipping method. * &#x60;Priority&#x60;: Priority shipping method. * &#x60;ScheduledDelivery&#x60;: Scheduled Delivery shipping method. **Note:** Shipping method service level agreements vary by marketplace. Sellers should see the Seller Central website in their marketplace for shipping method service level agreements and fulfillment fees. | [optional] 
**include_cod_fulfillment_preview** | **bool** | When true, returns all fulfillment order previews both for COD and not for COD. Otherwise, returns only fulfillment order previews that are not for COD. | [optional] 
**include_delivery_windows** | **bool** | When true, returns the &#x60;ScheduledDeliveryInfo&#x60; response object, which contains the available delivery windows for a Scheduled Delivery. The &#x60;ScheduledDeliveryInfo&#x60; response object can only be returned for fulfillment order previews with &#x60;ShippingSpeedCategories&#x60; equal to &#x60;ScheduledDelivery&#x60;. | [optional] 
**feature_constraints** | [**list[FeatureSettings]**](FeatureSettings.md) | A list of features and their fulfillment policies to apply to the order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


