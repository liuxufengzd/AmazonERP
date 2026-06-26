# TransferSchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_schedule_id** | **str** | The unique identifier provided by Amazon to the scheduled transfer. | 
**transaction_type** | [**TransactionType**](TransactionType.md) | The type of transfer. | 
**transaction_source_account** | [**TransactionAccount**](TransactionAccount.md) | Details of the source bank account in the scheduled transfer. | [optional] 
**transaction_destination_account** | [**TransactionAccount**](TransactionAccount.md) | Details of the destination bank account in the scheduled transfer. Here &#x60;bankAccountCountryCode&#x60; is a required field. | 
**transfer_schedule_status** | [**TransferScheduleStatus**](TransferScheduleStatus.md) | The type of transfer schedule. This information can be modified when you update a transfer schedule. | 
**transfer_schedule_information** | [**TransferScheduleInformation**](TransferScheduleInformation.md) | The fields required for the scheduled transfer. This information can be modified when you update a transfer schedule. | 
**payment_preference** | [**PaymentPreference**](PaymentPreference.md) | The payment preference of the scheduled transfer. This information can be modified when you update a transfer schedule. | [optional] 
**transfer_schedule_failures** | [**list[TransferScheduleFailures]**](TransferScheduleFailures.md) | A list of transfer schedule failures. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


