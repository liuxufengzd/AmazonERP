# ListOffersResponseOffer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | The SKU. This property is only supported for sellers and not for vendors. | [optional] 
**asin** | **str** | The Amazon Standard Identification Number (ASIN). | [optional] 
**marketplace_id** | [**MarketplaceId**](MarketplaceId.md) | The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE, and JP. The supported marketplaces for vendors only are BR, AU, MX, AE, and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace. | [optional] 
**eligibility** | [**EligibilityStatus**](EligibilityStatus.md) | The offer eligibility status. | [optional] 
**offer_program_configuration** | [**OfferProgramConfiguration**](OfferProgramConfiguration.md) |  | [optional] 
**program_type** | [**ProgramType**](ProgramType.md) | The replenishment program for the offer. | [optional] 
**vendor_codes** | **list[str]** | A list of vendor codes associated with the offer. | [optional] 
**price** | **float** | The current price of the offer. This is the listed price amount for the item. | [optional] 
**price_currency_code** | **str** | The currency code in ISO 4217 format for the price. For example, &#x60;USD&#x60; for US dollars. | [optional] 
**inventory** | **int** | The available inventory count for the offer. | [optional] 
**stock_risk** | **str** | The stock risk level of the offer, indicating the risk of the offer going out of stock. | [optional] 
**deliveries_conditions** | [**list[DeliveriesCondition]**](DeliveriesCondition.md) | A list of delivery conditions for the offer, indicating the health of upcoming deliveries. Each condition describes the quantity of upcoming deliveries associated with a particular delivery condition type. | [optional] 
**subscriptions** | **int** | The number of active subscriptions for the offer. | [optional] 
**fulfillment_network_id_type** | **str** | The fulfillment network identifier type for the offer, indicating how the offer is fulfilled. | [optional] 
**forecast_deliveries** | [**ForecastDeliveries**](ForecastDeliveries.md) | The projected subscriber demand for the offer over different time horizons. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


