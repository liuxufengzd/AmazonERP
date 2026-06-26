# swagger_client.AccountsApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountsApi.md#get_account) | **GET** /finances/transfers/wallet/2024-03-01/accounts/{accountId} | Find particular Amazon Seller Wallet account by Amazon account identifier
[**list_account_balances**](AccountsApi.md#list_account_balances) | **GET** /finances/transfers/wallet/2024-03-01/accounts/{accountId}/balance | Find balance in particular Amazon Seller Wallet account by Amazon account identifier
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /finances/transfers/wallet/2024-03-01/accounts | Get all Amazon Seller Wallet accounts for the seller


# **get_account**
> BankAccount get_account(account_id, marketplace_id)

Find particular Amazon Seller Wallet account by Amazon account identifier

Retrieve a Seller Wallet bank account by Amazon account identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 'amzn1.account.AGUGL2EM3ZHYSRJWH2UCRPIM5JFQ' # str | The ID of the Amazon Seller Wallet account.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Find particular Amazon Seller Wallet account by Amazon account identifier
    api_response = api_instance.get_account(account_id, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the Amazon Seller Wallet account. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_balances**
> BalanceListing list_account_balances(account_id, marketplace_id)

Find balance in particular Amazon Seller Wallet account by Amazon account identifier

Retrieve the balance in a given Seller Wallet bank account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 'amzn1.account.AGUGL2EM3ZHYSRJWH2UCRPIM5JFQ' # str | The ID of the Amazon Seller Wallet account.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Find balance in particular Amazon Seller Wallet account by Amazon account identifier
    api_response = api_instance.list_account_balances(account_id, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_account_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the Amazon Seller Wallet account. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**BalanceListing**](BalanceListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> BankAccountListing list_accounts(marketplace_id)

Get all Amazon Seller Wallet accounts for the seller

Get Seller Wallet accounts for a seller.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Get all Amazon Seller Wallet accounts for the seller
    api_response = api_instance.list_accounts(marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**BankAccountListing**](BankAccountListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

