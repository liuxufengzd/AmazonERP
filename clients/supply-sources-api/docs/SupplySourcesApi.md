# swagger_client.SupplySourcesApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_supply_source**](SupplySourcesApi.md#archive_supply_source) | **DELETE** /supplySources/2020-07-01/supplySources/{supplySourceId} | 
[**create_supply_source**](SupplySourcesApi.md#create_supply_source) | **POST** /supplySources/2020-07-01/supplySources | 
[**get_supply_source**](SupplySourcesApi.md#get_supply_source) | **GET** /supplySources/2020-07-01/supplySources/{supplySourceId} | 
[**get_supply_sources**](SupplySourcesApi.md#get_supply_sources) | **GET** /supplySources/2020-07-01/supplySources | 
[**update_supply_source**](SupplySourcesApi.md#update_supply_source) | **PUT** /supplySources/2020-07-01/supplySources/{supplySourceId} | 
[**update_supply_source_status**](SupplySourcesApi.md#update_supply_source_status) | **PUT** /supplySources/2020-07-01/supplySources/{supplySourceId}/status | 


# **archive_supply_source**
> ErrorList archive_supply_source(supply_source_id)



Archive a supply source, making it inactive. Cannot be undone.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplySourcesApi()
supply_source_id = 'supply_source_id_example' # str | The unique identifier of a supply source.

try:
    api_response = api_instance.archive_supply_source(supply_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplySourcesApi->archive_supply_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_source_id** | **str**| The unique identifier of a supply source. | 

### Return type

[**ErrorList**](ErrorList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_supply_source**
> CreateSupplySourceResponse create_supply_source(payload)



Create a new supply source.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplySourcesApi()
payload = swagger_client.CreateSupplySourceRequest() # CreateSupplySourceRequest | A request to create a supply source.

try:
    api_response = api_instance.create_supply_source(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplySourcesApi->create_supply_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateSupplySourceRequest**](CreateSupplySourceRequest.md)| A request to create a supply source. | 

### Return type

[**CreateSupplySourceResponse**](CreateSupplySourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supply_source**
> SupplySource get_supply_source(supply_source_id)



Retrieve a supply source.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplySourcesApi()
supply_source_id = 'supply_source_id_example' # str | The unique identifier of a supply source.

try:
    api_response = api_instance.get_supply_source(supply_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplySourcesApi->get_supply_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_source_id** | **str**| The unique identifier of a supply source. | 

### Return type

[**SupplySource**](SupplySource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supply_sources**
> GetSupplySourcesResponse get_supply_sources(next_page_token=next_page_token, page_size=page_size)



The path to retrieve paginated supply sources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplySourcesApi()
next_page_token = 'next_page_token_example' # str | The pagination token to retrieve a specific page of results. (optional)
page_size = 10 # float | The number of supply sources to return per paginated request. (optional) (default to 10)

try:
    api_response = api_instance.get_supply_sources(next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplySourcesApi->get_supply_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The pagination token to retrieve a specific page of results. | [optional] 
 **page_size** | **float**| The number of supply sources to return per paginated request. | [optional] [default to 10]

### Return type

[**GetSupplySourcesResponse**](GetSupplySourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supply_source**
> ErrorList update_supply_source(supply_source_id, payload=payload)



Update the configuration and capabilities of a supply source.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplySourcesApi()
supply_source_id = 'supply_source_id_example' # str | The unique identitier of a supply source.
payload = swagger_client.UpdateSupplySourceRequest() # UpdateSupplySourceRequest |  (optional)

try:
    api_response = api_instance.update_supply_source(supply_source_id, payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplySourcesApi->update_supply_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_source_id** | **str**| The unique identitier of a supply source. | 
 **payload** | [**UpdateSupplySourceRequest**](UpdateSupplySourceRequest.md)|  | [optional] 

### Return type

[**ErrorList**](ErrorList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supply_source_status**
> ErrorList update_supply_source_status(supply_source_id, payload=payload)



Update the status of a supply source.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplySourcesApi()
supply_source_id = 'supply_source_id_example' # str | The unique identifier of a supply source.
payload = swagger_client.UpdateSupplySourceStatusRequest() # UpdateSupplySourceStatusRequest |  (optional)

try:
    api_response = api_instance.update_supply_source_status(supply_source_id, payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplySourcesApi->update_supply_source_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_source_id** | **str**| The unique identifier of a supply source. | 
 **payload** | [**UpdateSupplySourceStatusRequest**](UpdateSupplySourceStatusRequest.md)|  | [optional] 

### Return type

[**ErrorList**](ErrorList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

