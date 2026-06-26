# swagger_client.VehiclesApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vehicles**](VehiclesApi.md#get_vehicles) | **GET** /catalog/2024-11-01/automotive/vehicles | 


# **get_vehicles**
> VehiclesResponse get_vehicles(marketplace_id, vehicle_type, page_token=page_token, updated_after=updated_after)



Get the latest collection of vehicles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
marketplace_id = 'A1PA6795UKMFR9' # str | An identifier for the marketplace in which the resource operates.
vehicle_type = 'CAR' # str | An identifier for vehicle type.
page_token = 'sdlkj234lkj234lksjdflkjwdflkjsfdlkj234234234234' # str | A token to fetch a certain page when there are multiple pages worth of results. (optional)
updated_after = '2024-01-05T18:00:03+00:00' # str | Date in ISO 8601 format, if provided only vehicles which are modified/added to Amazon's catalog after this date will be returned. (optional)

try:
    api_response = api_instance.get_vehicles(marketplace_id, vehicle_type, page_token=page_token, updated_after=updated_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->get_vehicles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| An identifier for the marketplace in which the resource operates. | 
 **vehicle_type** | **str**| An identifier for vehicle type. | 
 **page_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. | [optional] 
 **updated_after** | **str**| Date in ISO 8601 format, if provided only vehicles which are modified/added to Amazon&#39;s catalog after this date will be returned. | [optional] 

### Return type

[**VehiclesResponse**](VehiclesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

