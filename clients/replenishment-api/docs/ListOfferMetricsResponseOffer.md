# ListOfferMetricsResponseOffer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | The Amazon Standard Identification Number (ASIN). | [optional] 
**sku** | **str** | The SKU. This property is only supported for sellers and not for vendors. | [optional] 
**fulfillment_channel_type** | [**FulfillmentChannelType**](FulfillmentChannelType.md) | The fulfillment channel type of an offer. This property is only supported for sellers and not for vendors. | [optional] 
**brand_name** | **str** | The brand name associated with the offer. | [optional] 
**product_group** | **str** | The product group associated with the offer. This property is only supported for vendors and not for sellers. | [optional] 
**not_delivered_due_to_oos** | **float** | The percentage of items that were not shipped out of the total shipped units over a period of time due to being out of stock. Applicable to &#x60;PERFORMANCE&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**total_subscriptions_revenue** | **float** | The revenue generated from subscriptions over a period of time. Applicable to &#x60;PERFORMANCE&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**shipped_subscription_units** | **float** | The number of units shipped to the subscribers over a period of time. Applicable to &#x60;PERFORMANCE&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**active_subscriptions** | **float** | The number of active subscriptions present at the end of the period. Applicable to &#x60;PERFORMANCE&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**revenue_penetration** | **float** | The percentage of total program revenue out of total product revenue. Applicable to &#x60;PERFORMANCE&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**lost_revenue_due_to_oos** | **float** | The revenue that would have been generated had there not been out of stock. Applicable to &#x60;PERFORMANCE&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**coupons_revenue_penetration** | **float** | The percentage of revenue from ASINs with coupons out of total revenue from all ASINs. Applicable to &#x60;PERFORMANCE&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**share_of_coupon_subscriptions** | **float** | The percentage of new subscriptions from coupons. Applicable to &#x60;PERFORMANCE&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**next30_day_total_subscriptions_revenue** | **float** | The forecasted total subscription revenue for the next 30 days. Applicable to &#x60;FORECAST&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**next60_day_total_subscriptions_revenue** | **float** | The forecasted total subscription revenue for the next 60 days. Applicable to &#x60;FORECAST&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**next90_day_total_subscriptions_revenue** | **float** | The forecasted total subscription revenue for the next 90 days. Applicable to &#x60;FORECAST&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**next30_day_shipped_subscription_units** | **float** | The forecasted shipped subscription units for the next 30 days. Applicable to &#x60;FORECAST&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**next60_day_shipped_subscription_units** | **float** | The forecasted shipped subscription units for the next 60 days. Applicable to &#x60;FORECAST&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**next90_day_shipped_subscription_units** | **float** | The forecasted shipped subscription units for the next 90 days. Applicable to &#x60;FORECAST&#x60; &#x60;timePeriodType&#x60;. | [optional] 
**time_interval** | [**TimeInterval**](TimeInterval.md) | A time interval used to compute metrics. | [optional] 
**currency_code** | **str** | The currency code in ISO 4217 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


