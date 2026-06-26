# swagger_client.CustomerFeedbackApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_browse_node_return_topics**](CustomerFeedbackApi.md#get_browse_node_return_topics) | **GET** /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/returns/topics | 
[**get_browse_node_return_trends**](CustomerFeedbackApi.md#get_browse_node_return_trends) | **GET** /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/returns/trends | 
[**get_browse_node_review_topics**](CustomerFeedbackApi.md#get_browse_node_review_topics) | **GET** /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/reviews/topics | 
[**get_browse_node_review_trends**](CustomerFeedbackApi.md#get_browse_node_review_trends) | **GET** /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/reviews/trends | 
[**get_item_browse_node**](CustomerFeedbackApi.md#get_item_browse_node) | **GET** /customerFeedback/2024-06-01/items/{asin}/browseNode | 
[**get_item_review_topics**](CustomerFeedbackApi.md#get_item_review_topics) | **GET** /customerFeedback/2024-06-01/items/{asin}/reviews/topics | 
[**get_item_review_trends**](CustomerFeedbackApi.md#get_item_review_trends) | **GET** /customerFeedback/2024-06-01/items/{asin}/reviews/trends | 


# **get_browse_node_return_topics**
> BrowseNodeReturnTopicsResponse get_browse_node_return_topics(browse_node_id, marketplace_id)



Retrieve the topics that customers mention when they return items in a browse node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerFeedbackApi()
browse_node_id = 'browse_node_id_example' # str | A browse node ID is a unique identifier for a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.
marketplace_id = 'marketplace_id_example' # str | The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.

try:
    api_response = api_instance.get_browse_node_return_topics(browse_node_id, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerFeedbackApi->get_browse_node_return_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browse_node_id** | **str**| A browse node ID is a unique identifier for a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content. | 
 **marketplace_id** | **str**| The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. | 

### Return type

[**BrowseNodeReturnTopicsResponse**](BrowseNodeReturnTopicsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browse_node_return_trends**
> BrowseNodeReturnTrendsResponse get_browse_node_return_trends(browse_node_id, marketplace_id)



Retrieve the trends of topics that customers mention when they return items in a browse node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerFeedbackApi()
browse_node_id = 'browse_node_id_example' # str | A browse node ID is a unique identifier of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.
marketplace_id = 'marketplace_id_example' # str | The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.

try:
    api_response = api_instance.get_browse_node_return_trends(browse_node_id, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerFeedbackApi->get_browse_node_return_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browse_node_id** | **str**| A browse node ID is a unique identifier of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content. | 
 **marketplace_id** | **str**| The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. | 

### Return type

[**BrowseNodeReturnTrendsResponse**](BrowseNodeReturnTrendsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browse_node_review_topics**
> BrowseNodeReviewTopicsResponse get_browse_node_review_topics(browse_node_id, marketplace_id, sort_by)



Retrieve a browse node's ten most positive and ten most negative review topics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerFeedbackApi()
browse_node_id = 'browse_node_id_example' # str | The ID of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.
marketplace_id = 'marketplace_id_example' # str | The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.
sort_by = 'MENTIONS' # str | The metric by which to sort the data in the response.

try:
    api_response = api_instance.get_browse_node_review_topics(browse_node_id, marketplace_id, sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerFeedbackApi->get_browse_node_review_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browse_node_id** | **str**| The ID of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content. | 
 **marketplace_id** | **str**| The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. | 
 **sort_by** | **str**| The metric by which to sort the data in the response. | 

### Return type

[**BrowseNodeReviewTopicsResponse**](BrowseNodeReviewTopicsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browse_node_review_trends**
> BrowseNodeReviewTrendsResponse get_browse_node_review_trends(browse_node_id, marketplace_id)



Retrieve the positive and negative review trends of items in a browse node for the past six months.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerFeedbackApi()
browse_node_id = 'browse_node_id_example' # str | A browse node ID is a unique identifier of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.
marketplace_id = 'marketplace_id_example' # str | The marketplace ID is the globally unique identifier of a marketplace. For more information, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

try:
    api_response = api_instance.get_browse_node_review_trends(browse_node_id, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerFeedbackApi->get_browse_node_review_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browse_node_id** | **str**| A browse node ID is a unique identifier of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content. | 
 **marketplace_id** | **str**| The marketplace ID is the globally unique identifier of a marketplace. For more information, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**BrowseNodeReviewTrendsResponse**](BrowseNodeReviewTrendsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_browse_node**
> BrowseNodeResponse get_item_browse_node(asin, marketplace_id)



This API returns the associated browse node of the requested ASIN. A browse node is a location in a browse tree that is used for navigation, product classification, and website content on the Amazon retail website.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerFeedbackApi()
asin = 'asin_example' # str | The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace.
marketplace_id = 'marketplace_id_example' # str | The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.

try:
    api_response = api_instance.get_item_browse_node(asin, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerFeedbackApi->get_item_browse_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. | 
 **marketplace_id** | **str**| The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. | 

### Return type

[**BrowseNodeResponse**](BrowseNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_review_topics**
> ItemReviewTopicsResponse get_item_review_topics(asin, marketplace_id, sort_by)



Retrieve an item's ten most positive and ten most negative review topics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerFeedbackApi()
asin = 'asin_example' # str | The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. The value must be a child ASIN.
marketplace_id = 'marketplace_id_example' # str | The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.
sort_by = 'MENTIONS' # str | The metric by which to sort data in the response.

try:
    api_response = api_instance.get_item_review_topics(asin, marketplace_id, sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerFeedbackApi->get_item_review_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. The value must be a child ASIN. | 
 **marketplace_id** | **str**| The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. | 
 **sort_by** | **str**| The metric by which to sort data in the response. | 

### Return type

[**ItemReviewTopicsResponse**](ItemReviewTopicsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_review_trends**
> ItemReviewTrendsResponse get_item_review_trends(asin, marketplace_id)



Retrieve an item's positive and negative review trends for the past six months.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerFeedbackApi()
asin = 'asin_example' # str | The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. This API takes child ASIN as an input.
marketplace_id = 'marketplace_id_example' # str | The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.

try:
    api_response = api_instance.get_item_review_trends(asin, marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerFeedbackApi->get_item_review_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. This API takes child ASIN as an input. | 
 **marketplace_id** | **str**| The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. | 

### Return type

[**ItemReviewTrendsResponse**](ItemReviewTrendsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

