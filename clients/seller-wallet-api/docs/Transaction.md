# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The unique identifier of the Amazon Seller Wallet bank account from which the money is debited. | 
**transaction_id** | **str** | The unique identifier provided by Amazon to the transaction. | 
**transaction_type** | [**TransactionType**](TransactionType.md) | The type of the transaction. | 
**transaction_status** | [**TransactionStatus**](TransactionStatus.md) | The status of the transaction. | 
**transaction_request_date** | **datetime** | The date when the transaction was initiated. | 
**expected_completion_date** | **datetime** | The expected completion date of the transaction. | [optional] 
**transaction_actual_completion_date** | **datetime** | The transaction&#39;s completion date. | [optional] 
**last_update_date** | **datetime** | The date of the most recent account balance update. | 
**requester_name** | **str** | The Amazon Seller Wallet customer who requested the transaction. | [optional] 
**transaction_requester_source** | **str** | The transaction initiation source. This value is either the Amazon portal or PISP name that the customer used to start the transaction. | 
**transaction_description** | **str** | A description of the transaction that the requester provides when they initiate the transaction. | 
**transaction_source_account** | [**TransactionAccount**](TransactionAccount.md) | The source bank account details in the transaction. | [optional] 
**transaction_destination_account** | [**TransactionAccount**](TransactionAccount.md) | The destination bank account details in the transaction. | 
**transaction_request_amount** | [**Currency**](Currency.md) | The amount for which the transfer was initiated. | 
**transfer_rate_details** | [**TransferRatePreview**](TransferRatePreview.md) | The fees and rates that apply to the transaction, as applicable. | 
**transaction_final_amount** | [**Currency**](Currency.md) | The amount of completed transaction in the destination account currency. This value is only populated for international transactions | [optional] 
**transaction_failure_reason** | **str** | The reason the transaction failed, if applicable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


