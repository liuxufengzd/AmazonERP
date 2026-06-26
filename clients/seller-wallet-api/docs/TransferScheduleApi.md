# swagger_client.TransferScheduleApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transfer_schedule**](TransferScheduleApi.md#create_transfer_schedule) | **POST** /finances/transfers/wallet/2024-03-01/transferSchedules | Create a transfer schedule request from Amazon Seller Wallet account to another customer-provided account
[**delete_schedule_transaction**](TransferScheduleApi.md#delete_schedule_transaction) | **DELETE** /finances/transfers/wallet/2024-03-01/transferSchedules/{transferScheduleId} | Delete a transaction request that is scheduled from Amazon Seller Wallet account to another customer-provided account
[**get_transfer_schedule**](TransferScheduleApi.md#get_transfer_schedule) | **GET** /finances/transfers/wallet/2024-03-01/transferSchedules/{transferScheduleId} | Find particular Amazon Seller Wallet account transfer schedule by Amazon transfer schedule identifier
[**list_transfer_schedules**](TransferScheduleApi.md#list_transfer_schedules) | **GET** /finances/transfers/wallet/2024-03-01/transferSchedules | The API will return all the transfer schedules for a given Amazon Seller Wallet account
[**update_transfer_schedule**](TransferScheduleApi.md#update_transfer_schedule) | **PUT** /finances/transfers/wallet/2024-03-01/transferSchedules | Update a transfer schedule information. Only fields (i.e; transferScheduleInformation, paymentPreference, transferScheduleStatus) in the request body can be updated.


# **create_transfer_schedule**
> TransferSchedule create_transfer_schedule(body, dest_account_digital_signature, amount_digital_signature, marketplace_id)

Create a transfer schedule request from Amazon Seller Wallet account to another customer-provided account

Create a transfer schedule request from a Seller Wallet account to another customer-provided account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransferScheduleApi()
body = swagger_client.TransferScheduleRequest() # TransferScheduleRequest | The payload of the request.
dest_account_digital_signature = 'U8AsRXdh5fvjozFIv6vRUal1EHdFHhrCArIgmWbPtW0HuTlN_LPteg8G8tbvF4QmoRekOO84nQxg8j4gs0wEyAktg2Sm80a_FaTswv-U8XUXGHZ1UBagGD9zEPrGBbia_N5gm4fCOW-V3mSieblwBiUyq8frUYL606WtuStHtE3zJgaj9-B1ObhudxxQALuBKjPeksc7-qyrT8lwchdkiaprNwsqpv3aKid7Ux3uwEzxiEedO3QWvv6nCZnNNxK-zz2Zj6tPDE_mgQk5tJv4xRgMxtcTMmr7_ce4A9wqRxQqwBerIHpOIzpZizmXAG56uG8-hJojmPwnsPif7ihMuw' # str | Digital signature for the destination bank account details.
amount_digital_signature = '1EHdFHhrCArIgmWbPtW0HuTlN_LPteg8G8tbvF4QmoRekOO84nQxg8j4gs0wEyAktg2Sm80a_FaTswv-U8XUXGHZ1UBagGD9zEPrGBbia_N5gm4fCOW-qyrT8lwchdkiaprNwsqpv3aKid7Ux3uwEzxiEedO3QWvv6nCZnNNxK-zz2Zj6tPDE_mgQk5tJv4xRgMxtcTMmr7' # str | Digital signature for the source currency transaction amount.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Create a transfer schedule request from Amazon Seller Wallet account to another customer-provided account
    api_response = api_instance.create_transfer_schedule(body, dest_account_digital_signature, amount_digital_signature, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferScheduleApi->create_transfer_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferScheduleRequest**](TransferScheduleRequest.md)| The payload of the request. | 
 **dest_account_digital_signature** | **str**| Digital signature for the destination bank account details. | 
 **amount_digital_signature** | **str**| Digital signature for the source currency transaction amount. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**TransferSchedule**](TransferSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule_transaction**
> DeleteTransferSchedule delete_schedule_transaction(transfer_schedule_id, marketplace_id)

Delete a transaction request that is scheduled from Amazon Seller Wallet account to another customer-provided account

Delete a transaction request that is scheduled from Amazon Seller Wallet account to another customer-provided account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransferScheduleApi()
transfer_schedule_id = 'amzn1.scheduletransfer.AGUGL2EM3ZHYSRJWH2UCRPIM5JFQ' # str | A unique reference ID for a scheduled transfer.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Delete a transaction request that is scheduled from Amazon Seller Wallet account to another customer-provided account
    api_response = api_instance.delete_schedule_transaction(transfer_schedule_id, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferScheduleApi->delete_schedule_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_schedule_id** | **str**| A unique reference ID for a scheduled transfer. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**DeleteTransferSchedule**](DeleteTransferSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_schedule**
> TransferSchedule get_transfer_schedule(transfer_schedule_id, marketplace_id)

Find particular Amazon Seller Wallet account transfer schedule by Amazon transfer schedule identifier

Find a particular Amazon Seller Wallet account transfer schedule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransferScheduleApi()
transfer_schedule_id = 'amzn1.transferschedule.AKNWCDNVP3FNJDCLK876' # str | The schedule ID of the Amazon Seller Wallet transfer.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Find particular Amazon Seller Wallet account transfer schedule by Amazon transfer schedule identifier
    api_response = api_instance.get_transfer_schedule(transfer_schedule_id, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferScheduleApi->get_transfer_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_schedule_id** | **str**| The schedule ID of the Amazon Seller Wallet transfer. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**TransferSchedule**](TransferSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transfer_schedules**
> TransferScheduleListing list_transfer_schedules(account_id, marketplace_id, next_page_token=next_page_token)

The API will return all the transfer schedules for a given Amazon Seller Wallet account

Retrieve transfer schedules of a Seller Wallet bank account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransferScheduleApi()
account_id = 'amzn1.account.AGUGL2EM3ZHYSRJWH2UCRPIM5JFQ' # str | The ID of the Amazon Seller Wallet account.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
next_page_token = 'Next Page Token' # str | A token that you use to retrieve the next page of results. The response includes `nextPageToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextPageToken` is null. Note that this operation can return empty pages. (optional)

try:
    # The API will return all the transfer schedules for a given Amazon Seller Wallet account
    api_response = api_instance.list_transfer_schedules(account_id, marketplace_id, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferScheduleApi->list_transfer_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the Amazon Seller Wallet account. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
 **next_page_token** | **str**| A token that you use to retrieve the next page of results. The response includes &#x60;nextPageToken&#x60; when the number of results exceeds the specified &#x60;pageSize&#x60; value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until &#x60;nextPageToken&#x60; is null. Note that this operation can return empty pages. | [optional] 

### Return type

[**TransferScheduleListing**](TransferScheduleListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transfer_schedule**
> TransferSchedule update_transfer_schedule(body, dest_account_digital_signature, amount_digital_signature, marketplace_id)

Update a transfer schedule information. Only fields (i.e; transferScheduleInformation, paymentPreference, transferScheduleStatus) in the request body can be updated.

Update transfer schedule information. Returns a transfer belonging to the updated scheduled transfer request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransferScheduleApi()
body = swagger_client.TransferSchedule() # TransferSchedule | The payload of the scheduled transfer request that is to be updated.
dest_account_digital_signature = 'U8AsRXdh5fvjozFIv6vRUal1EHdFHhrCArIgmWbPtW0HuTlN_LPteg8G8tbvF4QmoRekOO84nQxg8j4gs0wEyAktg2Sm80a_FaTswv-U8XUXGHZ1UBagGD9zEPrGBbia_N5gm4fCOW-V3mSieblwBiUyq8frUYL606WtuStHtE3zJgaj9-B1ObhudxxQALuBKjPeksc7-qyrT8lwchdkiaprNwsqpv3aKid7Ux3uwEzxiEedO3QWvv6nCZnNNxK-zz2Zj6tPDE_mgQk5tJv4xRgMxtcTMmr7_ce4A9wqRxQqwBerIHpOIzpZizmXAG56uG8-hJojmPwnsPif7ihMuw' # str | Digital signature for the destination bank account details.
amount_digital_signature = '1EHdFHhrCArIgmWbPtW0HuTlN_LPteg8G8tbvF4QmoRekOO84nQxg8j4gs0wEyAktg2Sm80a_FaTswv-U8XUXGHZ1UBagGD9zEPrGBbia_N5gm4fCOW-qyrT8lwchdkiaprNwsqpv3aKid7Ux3uwEzxiEedO3QWvv6nCZnNNxK-zz2Zj6tPDE_mgQk5tJv4xRgMxtcTMmr7' # str | Digital signature for the source currency transaction amount.
marketplace_id = 'A1RKKUPIHCS9HS' # str | The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    # Update a transfer schedule information. Only fields (i.e; transferScheduleInformation, paymentPreference, transferScheduleStatus) in the request body can be updated.
    api_response = api_instance.update_transfer_schedule(body, dest_account_digital_signature, amount_digital_signature, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferScheduleApi->update_transfer_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferSchedule**](TransferSchedule.md)| The payload of the scheduled transfer request that is to be updated. | 
 **dest_account_digital_signature** | **str**| Digital signature for the destination bank account details. | 
 **amount_digital_signature** | **str**| Digital signature for the source currency transaction amount. | 
 **marketplace_id** | **str**| The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**TransferSchedule**](TransferSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

