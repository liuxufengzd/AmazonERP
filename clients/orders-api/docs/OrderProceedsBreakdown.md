# OrderProceedsBreakdown

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The proceeds category.   **Possible values**: &#x60;ITEM&#x60;, &#x60;SHIPPING&#x60;, &#x60;GIFT_WRAP&#x60;, &#x60;COD_FEE&#x60;, &#x60;TAX&#x60;, &#x60;DISCOUNT&#x60;, &#x60;DELIVERY_TIP&#x60;, &#x60;OTHER&#x60;. **Note:** &#x60;DELIVERY_TIP&#x60; is charged separately and not attributed to a specific item. The remaining categories are aggregated across all order items. | 
**status** | **str** | The processing status of the charge. Only present for categories processed separately after checkout, such as &#x60;DELIVERY_TIP&#x60;.  **Possible values**: &#x60;PENDING&#x60;, &#x60;FINALIZED&#x60;. | [optional] 
**subtotal** | [**Money**](Money.md) | The monetary amount for the proceeds category. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


