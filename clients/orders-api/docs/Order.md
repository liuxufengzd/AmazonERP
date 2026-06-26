# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | An Amazon-defined order identifier. | 
**order_aliases** | [**list[Alias]**](Alias.md) | Alternative identifiers that can be used to reference this order, such as seller-defined order numbers. | [optional] 
**created_time** | **datetime** | The time when the customer placed the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format. | 
**last_updated_time** | **datetime** | The most recent time when any aspect of this order was modified by Amazon or the seller. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format. | 
**programs** | **list[str]** | Special programs associated with this order that may affect fulfillment or customer experience.   **Possible values**: &#x60;AMAZON_BAZAAR&#x60;, &#x60;AMAZON_BUSINESS&#x60;, &#x60;AMAZON_EASY_SHIP&#x60;, &#x60;AMAZON_HAUL&#x60;, &#x60;DELIVERY_BY_AMAZON&#x60;, &#x60;FBM_SHIP_PLUS&#x60;, &#x60;INVOICE_BY_AMAZON&#x60;, &#x60;IN_STORE_PICK_UP&#x60;, &#x60;PREMIUM&#x60;, &#x60;PREORDER&#x60;, &#x60;PRIME&#x60; | [optional] 
**associated_orders** | [**list[AssociatedOrder]**](AssociatedOrder.md) | Other orders that have a direct relationship to this order, such as replacement or exchange orders. | [optional] 
**sales_channel** | [**SalesChannel**](SalesChannel.md) | Information about where this order was placed. | 
**buyer** | [**Buyer**](Buyer.md) | Information about the customer who purchased this order. | [optional] 
**recipient** | [**Recipient**](Recipient.md) | Information about the person or location where this order should be delivered. | [optional] 
**proceeds** | [**OrderProceeds**](OrderProceeds.md) | Financial information about this order. | [optional] 
**payment** | [**OrderPayment**](OrderPayment.md) | Payment information for the order. | [optional] 
**tax** | [**OrderTax**](OrderTax.md) | Tax-related information for the order. | [optional] 
**fulfillment** | [**OrderFulfillment**](OrderFulfillment.md) | Information about how this order is being processed and shipped. | [optional] 
**order_items** | [**list[OrderItem]**](OrderItem.md) | The list of all order items included in this order. | 
**packages** | [**list[OrderPackage]**](OrderPackage.md) | Shipping packages created for this order, including tracking information. **Note:** Only available for merchant-fulfilled (FBM) orders. | [optional] 
**fulfillment_orders** | [**list[FulfillmentOrder]**](FulfillmentOrder.md) | The list of fulfillment orders associated with this customer order. Each entry corresponds to one fulfillment unit created by Amazon for this order. **Note:** Only available for EasyShip orders at present. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


