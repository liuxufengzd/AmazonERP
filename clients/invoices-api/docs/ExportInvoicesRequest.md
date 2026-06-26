# ExportInvoicesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_end** | **date** | The latest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is the time of the request. | [optional] 
**date_start** | **date** | The earliest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 24 hours prior to the time of the request. | [optional] 
**external_invoice_id** | **str** | The external ID of the invoices you want included in the response. | [optional] 
**file_format** | [**FileFormat**](FileFormat.md) |  | [optional] 
**invoice_type** | **str** | The marketplace-specific classification of the invoice type. Use the &#x60;getInvoicesAttributes&#x60; operation to check &#x60;invoiceType&#x60; options. | [optional] 
**marketplace_id** | **str** | The ID of the marketplace from which you want the invoices. | 
**series** | **str** | The series number of the invoices you want included in the response. | [optional] 
**statuses** | **list[str]** | A list of statuses that you can use to filter invoices. Use the &#x60;getInvoicesAttributes&#x60; operation to check invoice status options.  Min count: 1 | [optional] 
**transaction_identifier** | [**TransactionIdentifier**](TransactionIdentifier.md) |  | [optional] 
**transaction_type** | **str** | The marketplace-specific classification of the transaction type for which the invoice was created. Use the &#x60;getInvoicesAttributes&#x60; operation to check &#x60;transactionType&#x60; options | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


