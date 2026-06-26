# OrderTaxRegistration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of entity that the tax registration belongs to.  **Possible values**: - &#x60;BUYER&#x60; (Indicates that this is the buyer&#39;s tax registration information) - &#x60;MERCHANT&#x60; (Indicates that this is the merchant&#39;s tax registration information) - &#x60;MARKETPLACE&#x60; (Indicates that this is the marketplace&#39;s tax registration information) | [optional] 
**legal_name** | **str** | The legal name associated with the tax registration. | [optional] 
**tax_registration_type** | **str** | The type of the tax registration number.  **Possible values**: &#x60;BUSINESS&#x60;, &#x60;VAT&#x60;, &#x60;CST&#x60;, &#x60;CPF&#x60;, &#x60;CNPJ&#x60; | [optional] 
**tax_registration_number** | **str** | The tax registration number that identifies the entity for tax purposes. | [optional] 
**tax_registration_address** | [**CustomerAddress**](CustomerAddress.md) | The address associated with the tax registration. | [optional] 
**tax_registration_attributes** | [**list[TaxRegistrationAttribute]**](TaxRegistrationAttribute.md) | Additional attributes related to the tax registration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


