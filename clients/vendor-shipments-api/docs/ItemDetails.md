# ItemDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | The purchase order number for the shipment being confirmed. If the items in this shipment belong to multiple purchase order numbers that are in particular carton or pallet within the shipment, then provide the purchaseOrderNumber at the appropriate carton or pallet level. Formatting Notes: 8-character alpha-numeric code. | [optional] 
**lot_number** | **str** | The batch or lot number associates an item with information the manufacturer considers relevant for traceability of the trade item to which the Element String is applied. The data may refer to the trade item itself or to items contained. This field is mandatory for all perishable items. | [optional] 
**lot_number_source_reference** | **str** | The location identifier where the product receives a traceability lot number. Provide this field for products subject to the FDA Food Safety Modernization Act (FSMA) Section 204. When you provide &#x60;lotNumberSourceReference&#x60;, you must also specify the corresponding &#x60;lotNumberSourceType&#x60; field. | [optional] 
**lot_number_source_type** | **str** | The identifier type used for the lot number source. Provide this field when you specify &#x60;lotNumberSourceReference&#x60;. | [optional] 
**country_of_origin** | **str** | The two-character country code for the country where the product was manufactured or originates. Use ISO 3166-1 alpha-2 format. | [optional] 
**regulation_references** | [**RegulationReferences**](RegulationReferences.md) | Regulatory requirements and compliance information for the item. | [optional] 
**expiry** | [**Expiry**](Expiry.md) | Expiry refers to the collection of dates required  for certain items. These could be either expiryDate or mfgDate and expiryAfterDuration. These are mandatory for perishable items. | [optional] 
**maximum_retail_price** | [**Money**](Money.md) | Maximum retail price of the item being shipped. | [optional] 
**handling_code** | **str** | Identification of the instructions on how specified item/carton/pallet should be handled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


