# ItemShippingConstraints

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pallet_delivery** | [**ConstraintType**](ConstraintType.md) | The line item must be delivered by pallet. | [optional] 
**cash_on_delivery** | [**ConstraintType**](ConstraintType.md) | Payment must be collected from the customer at the time of delivery. | [optional] 
**signature_confirmation** | [**ConstraintType**](ConstraintType.md) | The recipient of the line item must sign to confirm its delivery. | [optional] 
**recipient_identity_verification** | [**ConstraintType**](ConstraintType.md) | The person receiving the line item must be the same as the intended recipient of the order. | [optional] 
**recipient_age_verification** | [**ConstraintType**](ConstraintType.md) | The carrier must confirm that the recipient is of the legal age to receive the line item upon delivery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


