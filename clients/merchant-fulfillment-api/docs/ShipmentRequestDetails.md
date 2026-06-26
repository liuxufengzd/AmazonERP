# ShipmentRequestDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_order_id** | [**AmazonOrderId**](AmazonOrderId.md) | An Amazon-defined order identifier in 3-7-7 format. | 
**seller_order_id** | [**SellerOrderId**](SellerOrderId.md) | A seller-defined order identifier. | [optional] 
**item_list** | [**ItemList**](ItemList.md) |  | 
**ship_from_address** | [**Address**](Address.md) | The address of the sender. | 
**package_dimensions** | [**PackageDimensions**](PackageDimensions.md) | The package dimensions. | 
**weight** | [**Weight**](Weight.md) | The package weight. | 
**must_arrive_by_date** | [**Timestamp**](Timestamp.md) | The date by which the package must arrive to keep the promise to the customer, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. If &#x60;MustArriveByDate&#x60; is specified, only shipping service offers that can be delivered by that date are returned. | [optional] 
**ship_date** | [**Timestamp**](Timestamp.md) | When used in a request, this is the date and time that the seller wants to ship the package. When used in a response, this is the date and time that the package can be shipped by the indicated method. | [optional] 
**shipping_service_options** | [**ShippingServiceOptions**](ShippingServiceOptions.md) | Extra services offered by the carrier. | 
**label_customization** | [**LabelCustomization**](LabelCustomization.md) | Label customization options. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


