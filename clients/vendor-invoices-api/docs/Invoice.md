# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_type** | **str** | Identifies the type of invoice. | 
**id** | **str** | Unique number relating to the charges defined in this document. This will be invoice number if the document type is Invoice or CreditNote number if the document type is Credit Note. Failure to provide this reference will result in a rejection. | 
**reference_number** | **str** | An additional unique reference number used for regulatory or other purposes. | [optional] 
**_date** | **datetime** | Date when the invoice/credit note information was generated in the origin&#39;s accounting system. The invoice date should be on or after the purchase order creation date. | 
**remit_to_party** | [**PartyIdentification**](PartyIdentification.md) | Name, address and tax details of the party receiving the payment of this invoice. | 
**ship_to_party** | [**PartyIdentification**](PartyIdentification.md) | Name, address and tax details of the party receiving a shipment of products. | [optional] 
**ship_from_party** | [**PartyIdentification**](PartyIdentification.md) | Name, address and tax details of the party sending a shipment of products. | [optional] 
**bill_to_party** | [**PartyIdentification**](PartyIdentification.md) | Name, address and tax details of the party to whom this invoice is issued. | [optional] 
**payment_terms** | [**PaymentTerms**](PaymentTerms.md) | The payment terms for the invoice. | [optional] 
**invoice_total** | [**Money**](Money.md) | Total monetary amount charged in the invoice or full value of credit note to be paid including all relevant taxes. It is the total amount of invoice (including charges, less allowances) before terms discount (if discount is applicable). | 
**tax_details** | [**list[TaxDetails]**](TaxDetails.md) | Total tax amount details for all line items. | [optional] 
**additional_details** | [**list[AdditionalDetails]**](AdditionalDetails.md) | Additional details provided by the selling party, for tax related or other purposes. | [optional] 
**charge_details** | [**list[ChargeDetails]**](ChargeDetails.md) | Total charge amount details for all line items. | [optional] 
**allowance_details** | [**list[AllowanceDetails]**](AllowanceDetails.md) | Total allowance amount details for all line items. | [optional] 
**items** | [**list[InvoiceItem]**](InvoiceItem.md) | The list of invoice items. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


