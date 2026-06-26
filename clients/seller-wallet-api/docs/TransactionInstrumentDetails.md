# TransactionInstrumentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account** | [**BankAccount**](BankAccount.md) | Details of the destination bank account. | 
**bank_account_number** | **str** | The bank account number of the destination payment method.  **Note:** This field is encrypted before Amazon receives it, so should not be used to generate &#x60;destAccountDigitalSignature&#x60;, and should not be included in the request signature. | 
**account_holder_name** | **str** | The bank account holder&#39;s name (expected to be an Amazon customer).  **Note:** This field is encrypted before Amazon receives it, so should not be used to generate &#x60;destAccountDigitalSignature&#x60;, and should not be included in the request signature. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


