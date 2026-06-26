# swagger_client.TransactionsApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /finances/transfers/wallet/2024-03-01/transactions | Create a transaction request from Amazon Seller Wallet account to another customer-provided account
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /finances/transfers/wallet/2024-03-01/transactions/{transactionId} | Find particular Amazon Seller Wallet account transaction by Amazon transaction identifier
[**list_account_transactions**](TransactionsApi.md#list_account_transactions) | **GET** /finances/transfers/wallet/2024-03-01/transactions | The API will return all the transactions for a given Amazon Seller Wallet account sorted by the transaction request date


# **create_transaction**
> CreateTransactionResponse create_transaction(body, dest_account_digital_signature, amount_digital_signature, marketplace_id)

Create a transaction request from Amazon Seller Wallet account to another customer-provided account

Create a transaction request from a Seller Wallet account to another customer-provided account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
body = swagger_client.TransactionInitiationRequest() # TransactionInitiationRequest | The payload of the request
dest_account_digital_signature = 'U8AsRXdh5fvjozFIv6vRUal1EHdFHhrCArIgmWbPtW0HuTlN_LPteg8G8tbvF4QmoRekOO84nQxg8j4gs0wEyAktg2Sm80a_FaTswv-U8XUXGHZ1UBagGD9zEPrGBbia_N5gm4fCOW-V3mSieblwBiUyq8frUYL606WtuStHtE3zJgaj9-B1ObhudxxQALuBKjPeksc7-qyrT8lwchdkiaprNwsqpv3aKid7Ux3uwEzxiEedO3QWvv6nCZnNNxK-zz2Zj6tPDE_mgQk5tJv4xRgMxtcTMmr7_ce4A9wqRxQqwBerIHpOIzpZizmXAG56uG8-hJojmPwnsPif7ihMuw' # str | Digital signature for the destination bank account details. For more information, refer to [Third-Party Provider Signature Guidance](https://developer-docs.amazon.com/sp-api/docs/tpp-registration-signature-guidance).
amount_digital_signature = '1EHdFHhrCArIgmWbPtW0HuTlN_LPteg8G8tbvF4QmoRekOO84nQxg8j4gs0wEyAktg2Sm80a_FaTswv-U8XUXGHZ1UBagGD9zEPrGBbia_N5gm4fCOW-qyrT8lwchdkiaprNwsqpv3aKid7Ux3uwEzxiEedO3QWvv6nCZnNNxK-zz2Zj6tPDE_mgQk5tJv4xRgMxtcTMmr7' # str | Digital signature for the source currency transaction amount. Sign in the order of the request definitions. You can omit empty or optional fields. For more information, refer to [Third-Party Provider Signature Guidance](https://developer-docs.amazon.com/sp-api/docs/tpp-registration-signature-guidance).
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Create a transaction request from Amazon Seller Wallet account to another customer-provided account
    api_response = api_instance.create_transaction(body, dest_account_digital_signature, amount_digital_signature, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionInitiationRequest**](TransactionInitiationRequest.md)| The payload of the request | 
 **dest_account_digital_signature** | **str**| Digital signature for the destination bank account details. For more information, refer to [Third-Party Provider Signature Guidance](https://developer-docs.amazon.com/sp-api/docs/tpp-registration-signature-guidance). | 
 **amount_digital_signature** | **str**| Digital signature for the source currency transaction amount. Sign in the order of the request definitions. You can omit empty or optional fields. For more information, refer to [Third-Party Provider Signature Guidance](https://developer-docs.amazon.com/sp-api/docs/tpp-registration-signature-guidance). | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> Transaction get_transaction(transaction_id, marketplace_id)

Find particular Amazon Seller Wallet account transaction by Amazon transaction identifier

Find a transaction by the Amazon transaction identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
transaction_id = 'amzn1.transaction.AGUGL2EM3ZHYSRJWH2UCRPIM5JFQ' # str | The ID of the Amazon Seller Wallet transaction.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Find particular Amazon Seller Wallet account transaction by Amazon transaction identifier
    api_response = api_instance.get_transaction(transaction_id, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID of the Amazon Seller Wallet transaction. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_transactions**
> TransactionListing list_account_transactions(account_id, marketplace_id, next_page_token=next_page_token)

The API will return all the transactions for a given Amazon Seller Wallet account sorted by the transaction request date

Retrieve a list of transactions for a given Seller Wallet bank account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
account_id = 'amzn1.account.AGUGL2EM3ZHYSRJWH2UCRPIM5JFQ' # str | The ID of the Amazon Seller Wallet account.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
next_page_token = 'Next Page Token' # str | A token that you use to retrieve the next page of results. The response includes `nextPageToken` when the number of results exceeds 100. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextPageToken` is null. Note that this operation can return empty pages. (optional)

try:
    # The API will return all the transactions for a given Amazon Seller Wallet account sorted by the transaction request date
    api_response = api_instance.list_account_transactions(account_id, marketplace_id, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_account_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the Amazon Seller Wallet account. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
 **next_page_token** | **str**| A token that you use to retrieve the next page of results. The response includes &#x60;nextPageToken&#x60; when the number of results exceeds 100. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until &#x60;nextPageToken&#x60; is null. Note that this operation can return empty pages. | [optional] 

### Return type

[**TransactionListing**](TransactionListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

