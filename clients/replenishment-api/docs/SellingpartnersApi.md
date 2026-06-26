# swagger_client.SellingpartnersApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_selling_partner_metrics**](SellingpartnersApi.md#get_selling_partner_metrics) | **POST** /replenishment/2022-11-07/sellingPartners/metrics/search | 


# **get_selling_partner_metrics**
> GetSellingPartnerMetricsResponse get_selling_partner_metrics(body=body)



Returns aggregated replenishment program metrics for a selling partner.   **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SellingpartnersApi()
body = swagger_client.GetSellingPartnerMetricsRequest() # GetSellingPartnerMetricsRequest | The request body for the `getSellingPartnerMetrics` operation. (optional)

try:
    api_response = api_instance.get_selling_partner_metrics(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellingpartnersApi->get_selling_partner_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSellingPartnerMetricsRequest**](GetSellingPartnerMetricsRequest.md)| The request body for the &#x60;getSellingPartnerMetrics&#x60; operation. | [optional] 

### Return type

[**GetSellingPartnerMetricsResponse**](GetSellingPartnerMetricsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

