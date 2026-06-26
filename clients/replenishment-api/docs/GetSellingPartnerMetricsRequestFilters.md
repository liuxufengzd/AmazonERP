# GetSellingPartnerMetricsRequestFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asins** | **list[str]** | A list of Amazon Standard Identification Numbers (ASINs) to filter by. ASIN filter is supported for these metrics: SHIPPED_SUBSCRIPTION_UNITS, TOTAL_SUBSCRIPTIONS_REVENUE, ACTIVE_SUBSCRIPTIONS, NOT_DELIVERED_DUE_TO_OOS, LOST_REVENUE_DUE_TO_OOS, COUPONS_REVENUE_PENETRATION, SHARE_OF_COUPON_SUBSCRIPTIONS and REVENUE_PENETRATION. | [optional] 
**skus** | **list[str]** | [Applicable only for Sellers] A list of SKUs to filter by. SKU filter is supported for these metrics: SHIPPED_SUBSCRIPTION_UNITS, TOTAL_SUBSCRIPTIONS_REVENUE, ACTIVE_SUBSCRIPTIONS, NOT_DELIVERED_DUE_TO_OOS, LOST_REVENUE_DUE_TO_OOS, COUPONS_REVENUE_PENETRATION, SHARE_OF_COUPON_SUBSCRIPTIONS and REVENUE_PENETRATION. | [optional] 
**fulfillment_channel_types** | [**list[FulfillmentChannelType]**](FulfillmentChannelType.md) | [Applicable only for Sellers] The fulfillment channel types to filter by. Fulfillment channel type filter is supported for these metrics: SHIPPED_SUBSCRIPTION_UNITS, TOTAL_SUBSCRIPTIONS_REVENUE, ACTIVE_SUBSCRIPTIONS, NOT_DELIVERED_DUE_TO_OOS, LOST_REVENUE_DUE_TO_OOS, COUPONS_REVENUE_PENETRATION, SHARE_OF_COUPON_SUBSCRIPTIONS and REVENUE_PENETRATION. | [optional] 
**brand_names** | **list[str]** | [Applicable only for US marketplace] A list of brand names to filter by. Brand name filter is supported for these metrics: SHIPPED_SUBSCRIPTION_UNITS, TOTAL_SUBSCRIPTIONS_REVENUE, ACTIVE_SUBSCRIPTIONS, NOT_DELIVERED_DUE_TO_OOS, LOST_REVENUE_DUE_TO_OOS, COUPONS_REVENUE_PENETRATION, SHARE_OF_COUPON_SUBSCRIPTIONS, REVENUE_PENETRATION, SUBSCRIBER_NON_SUBSCRIBER_AVERAGE_REVENUE, SUBSCRIBER_NON_SUBSCRIBER_AVERAGE_REORDERS, REVENUE_BY_DELIVERIES, SUBSCRIBER_RETENTION, REVENUE_PENETRATION_BY_SELLER_FUNDING, SUBSCRIBER_LIFETIME_VALUE_BY_CUSTOMER_SEGMENT and SIGNUP_CONVERSION_BY_SELLER_FUNDING. | [optional] 
**product_groups** | **list[str]** | [Applicable only for Vendors] A list of product group names to filter by. Product group filter is supported for these metrics: SHIPPED_SUBSCRIPTION_UNITS, TOTAL_SUBSCRIPTIONS_REVENUE, ACTIVE_SUBSCRIPTIONS, NOT_DELIVERED_DUE_TO_OOS, LOST_REVENUE_DUE_TO_OOS, COUPONS_REVENUE_PENETRATION, SHARE_OF_COUPON_SUBSCRIPTIONS and REVENUE_PENETRATION. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


