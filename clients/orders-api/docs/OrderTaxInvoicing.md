# OrderTaxInvoicing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_invoice_preference** | **str** | The buyer&#39;s invoicing preference, which indicates whether the seller should issue an individual or a business invoice to the buyer.    **Note**: This attribute is only available in the Turkey marketplace.   **Possible values**: - &#x60;INDIVIDUAL&#x60; (Issues an individual invoice to the buyer) - &#x60;BUSINESS&#x60; (Issues a business invoice to the buyer) | [optional] 
**invoice_status** | **str** | The status of the invoice. Only available for Easy Ship orders and orders in the Brazil marketplace.  **Possible values**: - &#x60;NOT_REQUIRED&#x60; (The order does not require an electronic invoice to be uploaded) - &#x60;NOT_FOUND&#x60; (The order requires an electronic invoice but it is not uploaded) - &#x60;PROCESSING&#x60; (The required electronic invoice was uploaded and is processing) - &#x60;ERRORED&#x60; (The uploaded electronic invoice was not accepted) - &#x60;ACCEPTED&#x60; (The uploaded electronic invoice was accepted) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


