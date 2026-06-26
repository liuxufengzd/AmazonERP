# GovernmentInvoiceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contexts** | [**list[CarrierDetailsContext]**](CarrierDetailsContext.md) | Object that contains additional invoice creation information | [optional] 
**inbound_plan_id** | **str** | The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created. | [optional] 
**invoice_type** | **str** | Marketplace specific classification of the invoice type. Check &#39;invoiceType&#39; options using &#39;getInvoicesAttributes&#39; operation. | 
**marketplace_id** | **str** | The government invoices creation request will match the national authoritative source of the given marketplace. | 
**shipment_id** | **str** | The unique shipment identifier to get an invoice for. | 
**transaction_type** | **str** | Marketplace specific classification of the transaction type that originated the invoice. Check &#39;transactionType&#39; options using &#39;getInvoicesAttributes&#39; operation. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


