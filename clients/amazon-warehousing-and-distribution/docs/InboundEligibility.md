# InboundEligibility

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ineligibility_reasons** | [**list[OrderIneligibilityReason]**](OrderIneligibilityReason.md) | If there are order level eligibility issues, then this list will contain those error codes and descriptions. | [optional] 
**packages_to_inbound** | [**list[SkuEligibility]**](SkuEligibility.md) | Details on SKU eligibility for each inbound package. | 
**previewed_at** | **datetime** | Timestamp when the eligibility check is performed. | 
**status** | [**InboundEligibilityStatus**](InboundEligibilityStatus.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


