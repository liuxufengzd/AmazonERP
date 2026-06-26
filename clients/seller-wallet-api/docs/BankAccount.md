# BankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The unique bank account identifier provided by Amazon. To initiate a &#x60;SELF&#x60; transaction with Seller Wallet, you must choose &#x60;BANK_ACCOUNT&#x60; as the payment method type in the [getPaymentMethod](https://developer-docs.amazon.com/sp-api/reference/getpaymentmethods) request. Your Amazon Seller Wallet bank account identifier should match the &#x60;paymentMethodId&#x60; in the response. This field is required. | [optional] 
**account_holder_name** | **str** | The bank account holder&#39;s name (expected to be an Amazon customer). There is a 50 character limit. | [optional] 
**bank_account_number_format** | [**BankAccountNumberFormat**](BankAccountNumberFormat.md) | The format in which the bank account number is provided for &#x60;THIRD_PARTY&#x60; transaction requests. | [optional] 
**bank_name** | **str** | The name of the bank. This value is Amazon Seller Wallet for Amazon Seller Wallet accounts. | [optional] 
**bank_account_ownership_type** | [**BankAccountOwnershipType**](BankAccountOwnershipType.md) | Type of ownership of the bank account. This value is &#x60;SELF&#x60; for Amazon Seller Wallet accounts. | 
**routing_number** | **str** | Routing number for automated clearing house transfers for &#x60;THIRD_PARTY&#x60; transaction requests. This value is nine consecutive zeros for Amazon Seller Wallet accounts. | [optional] 
**bank_number_format** | [**BankNumberFormat**](BankNumberFormat.md) | The bank number format or routing number type for &#x60;THIRD_PARTY&#x60; transaction requests. | [optional] 
**account_country_code** | **str** | The two-digit country code in ISO 3166 format. | 
**account_currency** | **str** | Bank account currency code in ISO 4217 format. | 
**bank_account_number_tail** | **str** | The last 3 digit of the bank account number. This value is three consecutive zeros for Amazon Seller Wallet accounts. | 
**bank_account_holder_status** | [**BankAccountHolderStatus**](BankAccountHolderStatus.md) | The compliance status of the bank account holder. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


