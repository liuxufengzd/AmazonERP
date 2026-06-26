# swagger_client.VendorDFSandboxApi

All URIs are relative to *https://sandbox.sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_order_scenarios**](VendorDFSandboxApi.md#generate_order_scenarios) | **POST** /vendor/directFulfillment/sandbox/2021-10-28/orders | 


# **generate_order_scenarios**
> TransactionReference generate_order_scenarios(body)



Submits a request to generate test order data for Vendor Direct Fulfillment API entities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorDFSandboxApi()
body = swagger_client.GenerateOrderScenarioRequest() # GenerateOrderScenarioRequest | The request payload containing parameters for generating test order data scenarios.

try:
    api_response = api_instance.generate_order_scenarios(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorDFSandboxApi->generate_order_scenarios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateOrderScenarioRequest**](GenerateOrderScenarioRequest.md)| The request payload containing parameters for generating test order data scenarios. | 

### Return type

[**TransactionReference**](TransactionReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

