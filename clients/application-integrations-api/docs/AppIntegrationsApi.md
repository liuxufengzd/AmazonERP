# swagger_client.AppIntegrationsApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](AppIntegrationsApi.md#create_notification) | **POST** /appIntegrations/2024-04-01/notifications | 
[**delete_notifications**](AppIntegrationsApi.md#delete_notifications) | **POST** /appIntegrations/2024-04-01/notifications/deletion | 
[**record_action_feedback**](AppIntegrationsApi.md#record_action_feedback) | **POST** /appIntegrations/2024-04-01/notifications/{notificationId}/feedback | 


# **create_notification**
> CreateNotificationResponse create_notification(body)



Create a notification for sellers in Seller Central.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Sellers whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppIntegrationsApi()
body = swagger_client.CreateNotificationRequest() # CreateNotificationRequest | The request body for the `createNotification` operation.

try:
    api_response = api_instance.create_notification(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppIntegrationsApi->create_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateNotificationRequest**](CreateNotificationRequest.md)| The request body for the &#x60;createNotification&#x60; operation. | 

### Return type

[**CreateNotificationResponse**](CreateNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notifications**
> delete_notifications(body)



Remove your application's notifications from the Appstore notifications dashboard.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Sellers whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppIntegrationsApi()
body = swagger_client.DeleteNotificationsRequest() # DeleteNotificationsRequest | The request body for the `deleteNotifications` operation.

try:
    api_instance.delete_notifications(body)
except ApiException as e:
    print("Exception when calling AppIntegrationsApi->delete_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteNotificationsRequest**](DeleteNotificationsRequest.md)| The request body for the &#x60;deleteNotifications&#x60; operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_action_feedback**
> record_action_feedback(notification_id, body)



Records the seller's response to a notification.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Sellers whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppIntegrationsApi()
notification_id = 'notification_id_example' # str | A `notificationId` uniquely identifies a notification.
body = swagger_client.RecordActionFeedbackRequest() # RecordActionFeedbackRequest | The request body for the `recordActionFeedback` operation.

try:
    api_instance.record_action_feedback(notification_id, body)
except ApiException as e:
    print("Exception when calling AppIntegrationsApi->record_action_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| A &#x60;notificationId&#x60; uniquely identifies a notification. | 
 **body** | [**RecordActionFeedbackRequest**](RecordActionFeedbackRequest.md)| The request body for the &#x60;recordActionFeedback&#x60; operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

