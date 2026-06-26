# TransactionAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The unique identifier provided by Amazon to identify the account. | [optional] 
**bank_account_holder_name** | **str** | The account holder&#39;s name. | [optional] 
**bank_name** | **str** | The name of the bank. | 
**bank_account_number_format** | [**BankAccountNumberFormat**](BankAccountNumberFormat.md) | The format for the bank account number. | 
**bank_account_number_tail** | **str** | The last three digits of the bank account number. | [optional] 
**bank_account_country_code** | **str** | The two-digit country code, in ISO 3166 format. This field is optional for &#x60;transactionSourceAccount&#x60;, but is mandatory for &#x60;transactionDestinationAccount&#x60;. | [optional] 
**bank_account_currency** | **str** | The currency code in ISO 4217 format. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


