# PaymentExecution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | The payment method used for this payment execution (for example, CashOnDelivery, ConvenienceStore, CreditCard, Invoice, Pix, and so on). | [optional] 
**payment_amount** | [**Money**](Money.md) | The monetary value of the payment execution. | [optional] 
**acquirer_id** | **str** | The unique identifier of the payment processor or acquiring bank that authorizes the payment.   **Note**: This attribute is only available for orders in the Brazil (BR) marketplace when the &#x60;paymentMethod&#x60; is &#x60;CreditCard&#x60; or &#x60;Pix&#x60;. | [optional] 
**card_brand** | **str** | The card network or brand used in the payment transaction (for example, Visa or Mastercard).  **Note**: This attribute is only available for orders in the Brazil (BR) marketplace when the &#x60;paymentMethod&#x60; is &#x60;CreditCard&#x60;. | [optional] 
**authorization_code** | **str** | The unique code that confirms the payment authorization.  **Note**: This attribute is only available for orders in the Brazil (BR) marketplace when the &#x60;paymentMethod&#x60; is &#x60;CreditCard&#x60; or &#x60;Pix&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


