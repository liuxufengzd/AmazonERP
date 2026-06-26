# TransactionInitiationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account_id** | **str** | The unique identifier of the source Amazon Seller Wallet bank account from which the money is debited. | 
**destination_account_id** | **str** | The unique identifier of the destination bank account where the money is deposited. | [optional] 
**destination_transaction_instrument** | [**TransactionInstrumentDetails**](TransactionInstrumentDetails.md) | Details of the destination bank account in the transaction request. | 
**transaction_description** | **str** | A description of the transaction. | [optional] 
**customer_payment_reference** | **str** | If the payment is for VAT (Value-Added-Tax) then enter VAT identification number in this field which will be mandatory. The length constraint is 140 characters and do not allow user to enter any sensitive information other than VAT-ID. | [optional] 
**payee_contact_information** | [**PayeeContactInformation**](PayeeContactInformation.md) | The contact information of a payee. | [optional] 
**source_amount** | [**Currency**](Currency.md) | The transaction amount in the source account&#39;s currency format. Requests that use a currency other than the source bank account currency fail. | 
**transfer_rate_details** | [**TransferRatePreview**](TransferRatePreview.md) | The fees and foreign exchange rates that apply to the transaction. Transfer Rate Preview is currently optional. This field is required when the third party honors the fees and rates of the Seller Wallet transaction. | [optional] 
**request_time** | **datetime** | The time at which the transaction was initiated in [ISO 8601 date time format](https://developer-docs.amazon.com/sp-api/docs/iso-8601). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


