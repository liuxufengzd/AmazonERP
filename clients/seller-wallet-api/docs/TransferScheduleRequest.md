# TransferScheduleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account_id** | **str** | The unique identifier of the source Amazon Seller Wallet bank account from which money is debited. | 
**source_currency_code** | **str** | The three-letter currency code of the source payment method country, in ISO 4217 format. | 
**destination_account_id** | **str** | The unique identifier of the destination bank account where the money is deposited. | 
**destination_transaction_instrument** | [**TransactionInstrumentDetails**](TransactionInstrumentDetails.md) | Details of the destination bank account in the transaction request. | 
**transaction_type** | [**TransactionType**](TransactionType.md) | The type of the scheduled transaction. | 
**transfer_schedule_information** | [**TransferScheduleInformation**](TransferScheduleInformation.md) | The configuration of the scheduled transfer. | 
**payment_preference** | [**PaymentPreference**](PaymentPreference.md) | The payment preference of the scheduled transfer. | 
**transfer_schedule_status** | [**TransferScheduleStatus**](TransferScheduleStatus.md) | The type of transaction schedule. This field is required when you update a transfer schedule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


