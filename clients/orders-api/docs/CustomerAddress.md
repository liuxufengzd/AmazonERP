# CustomerAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The full name of the person who will receive the delivery at this address. | [optional] 
**company_name** | **str** | The name of the business or organization at this address. | [optional] 
**address_line1** | **str** | The primary street address. | [optional] 
**address_line2** | **str** | Additional address information. | [optional] 
**address_line3** | **str** | Additional address information. | [optional] 
**city** | **str** | The city of the address. | [optional] 
**district_or_county** | **str** | The district or county of the address. | [optional] 
**state_or_region** | **str** | The state, province, or region of the address. | [optional] 
**municipality** | **str** | The municipality of the address. | [optional] 
**postal_code** | **str** | The postal code, ZIP code, or equivalent mailing code of the address. | [optional] 
**country_code** | **str** | The two-letter country code identifying the country of the address, in ISO 3166-1 format. | [optional] 
**phone** | **str** | The contact phone number for delivery coordination and customer communication.  **Note**: The buyer phone number will be suppressed in some cases, including but not limited to:  - All FBA (Fulfillment by Amazon) orders. - Shipped FBM (Fulfilled by the merchant) orders when current date is past the latest delivery date. | [optional] 
**extended_fields** | [**AddressExtendedFields**](AddressExtendedFields.md) | Additional address components specific to certain countries that provide more detailed location information.  **Note**: Only available with Brazil shipping addresses. | [optional] 
**address_type** | **str** | The type of location.  **Possible values**: &#x60;RESIDENTIAL&#x60;, &#x60;COMMERCIAL&#x60;, &#x60;PICKUP_POINT&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


