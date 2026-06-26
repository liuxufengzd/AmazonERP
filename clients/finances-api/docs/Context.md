# Context

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_name** | **str** | The store name associated with the transaction. | [optional] 
**order_type** | **str** | The transaction&#39;s order type. | [optional] 
**channel** | **str** | Channel details of related transaction. | [optional] 
**asin** | **str** | The Amazon Standard Identification Number (ASIN) of the item. | [optional] 
**sku** | **str** | The Stock Keeping Unit (SKU) of the item. | [optional] 
**quantity_shipped** | **int** | The quantity of the item shipped. | [optional] 
**fulfillment_network** | **str** | The fulfillment network of the item. | [optional] 
**payment_type** | **str** | The type of payment. | [optional] 
**payment_method** | **str** | The method of payment. | [optional] 
**payment_reference** | **str** | The reference number of the payment. | [optional] 
**payment_date** | [**ModelDate**](ModelDate.md) | The date of the payment. | [optional] 
**deferral_reason** | **str** | The deferral policy applied to the transaction.  **Examples:** &#x60;B2B&#x60; (invoiced orders), &#x60;DD7&#x60; (delivery date policy) | [optional] 
**maturity_date** | [**ModelDate**](ModelDate.md) | The release date of the transaction. | [optional] 
**start_time** | [**ModelDate**](ModelDate.md) | The start time of the transaction. | [optional] 
**end_time** | [**ModelDate**](ModelDate.md) | The end time of the transaction. | [optional] 
**context_type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


