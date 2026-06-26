# OrderPackage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_reference_id** | **str** | A unique identifier for this package within the context of the order. | 
**created_time** | **datetime** | The exact time when this shipping package was created and prepared for shipment. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format. | [optional] 
**package_status** | [**PackageStatus**](PackageStatus.md) | The current status of this package. | [optional] 
**carrier** | **str** | The carrier responsible for transporting this package to the customer. | [optional] 
**ship_time** | **datetime** | The exact time when this package was handed over to the carrier and began its journey to the customer. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format. | [optional] 
**shipping_service** | **str** | The specific shipping method or service used for delivering this package. | [optional] 
**tracking_number** | **str** | The carrier-provided tracking number that customers can use to monitor the package&#39;s delivery progress. | [optional] 
**ship_from_address** | [**MerchantAddress**](MerchantAddress.md) | The physical address from which this package was shipped, typically the merchant&#39;s warehouse or fulfillment center. | [optional] 
**package_items** | [**list[PackageItem]**](PackageItem.md) | A list of all order items included in this specific package. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


