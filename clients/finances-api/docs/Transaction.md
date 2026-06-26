# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selling_partner_metadata** | [**SellingPartnerMetadata**](SellingPartnerMetadata.md) | Metadata that describes the seller. | [optional] 
**related_identifiers** | [**RelatedIdentifiers**](RelatedIdentifiers.md) | Identifiers related to the transaction, such as order and shipment IDs. | [optional] 
**transaction_type** | **str** | The type of transaction.  **Possible value:** &#x60;Shipment&#x60; | [optional] 
**transaction_id** | **str** | The unique identifier of the transaction. | [optional] 
**transaction_status** | **str** | The status of the transaction.  **Possible values:**  * &#x60;DEFERRED&#x60;: the transaction is currently deferred. * &#x60;RELEASED&#x60;: the transaction is currently released. * &#x60;DEFERRED_RELEASED&#x60;: the transaction was deferred in the past, but is now released. The status of a deferred transaction is updated to &#x60;DEFERRED_RELEASED&#x60; when the transaction is released. | [optional] 
**description** | **str** | Describes the reasons for the transaction.  **Example:** &#39;Order Payment&#39;, &#39;Refund Order&#39; | [optional] 
**posted_date** | [**ModelDate**](ModelDate.md) | The date and time when the transaction was posted. | [optional] 
**total_amount** | [**Currency**](Currency.md) | The total amount of money in the transaction. | [optional] 
**marketplace_details** | [**MarketplaceDetails**](MarketplaceDetails.md) | Information about the marketplace where the transaction occurred. | [optional] 
**items** | [**Items**](Items.md) | Additional information about the items in the transaction. | [optional] 
**contexts** | [**Contexts**](Contexts.md) | Additional Information about the transaction. | [optional] 
**breakdowns** | [**list[Breakdown]**](Breakdown.md) | A list of breakdowns that detail how the total amount is calculated for the transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


