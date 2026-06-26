# OrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** | A unique identifier for this specific item within the order. | 
**quantity_ordered** | **int** | The number of units of this item that the customer ordered. | 
**measurement** | [**Measurement**](Measurement.md) | The unit of measure and value for items sold by weight, volume, or other measurements rather than simple count. | [optional] 
**associated_order_items** | [**list[AssociatedOrderItem]**](AssociatedOrderItem.md) | A list of order items associated with this item. For example, a value-add service purchased with the product. | [optional] 
**programs** | **list[str]** | Special programs that apply specifically to this item within the order.  **Possible values**: &#x60;TRANSPARENCY&#x60;, &#x60;SUBSCRIBE_AND_SAVE&#x60; | [optional] 
**product** | [**ItemProduct**](ItemProduct.md) | Information about the product being ordered. | 
**proceeds** | [**ItemProceeds**](ItemProceeds.md) | The money that the seller receives from the sale of this specific item. | [optional] 
**expense** | [**ItemExpense**](ItemExpense.md) | The expense information related to this specific item. | [optional] 
**promotion** | [**ItemPromotion**](ItemPromotion.md) | Details about any discounts, coupons, or promotional offers applied to this item. | [optional] 
**cancellation** | [**ItemCancellation**](ItemCancellation.md) | The cancellation information of the order item. | [optional] 
**fulfillment** | [**ItemFulfillment**](ItemFulfillment.md) | Information about how the order item should be processed, packed, and shipped to the customer. | [optional] 
**tax** | [**ItemTax**](ItemTax.md) | Tax-related information for this order item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


