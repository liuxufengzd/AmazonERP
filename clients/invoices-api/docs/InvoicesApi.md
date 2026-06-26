# swagger_client.InvoicesApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_government_invoice**](InvoicesApi.md#create_government_invoice) | **POST** /tax/invoices/2024-06-19/governmentInvoiceRequests | 
[**create_invoices_export**](InvoicesApi.md#create_invoices_export) | **POST** /tax/invoices/2024-06-19/exports | 
[**get_government_invoice_document**](InvoicesApi.md#get_government_invoice_document) | **GET** /tax/invoices/2024-06-19/governmentInvoiceRequests/{shipmentId} | 
[**get_government_invoice_status**](InvoicesApi.md#get_government_invoice_status) | **GET** /tax/invoices/2024-06-19/governmentInvoiceRequests | 
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /tax/invoices/2024-06-19/invoices/{invoiceId} | 
[**get_invoices**](InvoicesApi.md#get_invoices) | **GET** /tax/invoices/2024-06-19/invoices | 
[**get_invoices_attributes**](InvoicesApi.md#get_invoices_attributes) | **GET** /tax/invoices/2024-06-19/attributes | 
[**get_invoices_document**](InvoicesApi.md#get_invoices_document) | **GET** /tax/invoices/2024-06-19/documents/{invoicesDocumentId} | 
[**get_invoices_export**](InvoicesApi.md#get_invoices_export) | **GET** /tax/invoices/2024-06-19/exports/{exportId} | 
[**get_invoices_exports**](InvoicesApi.md#get_invoices_exports) | **GET** /tax/invoices/2024-06-19/exports | 


# **create_government_invoice**
> create_government_invoice(body)



Submits an asynchronous government invoice creation request.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0167 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
body = swagger_client.GovernmentInvoiceRequest() # GovernmentInvoiceRequest | Information required to create the government invoice.

try:
    api_instance.create_government_invoice(body)
except ApiException as e:
    print("Exception when calling InvoicesApi->create_government_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GovernmentInvoiceRequest**](GovernmentInvoiceRequest.md)| Information required to create the government invoice. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoices_export**
> ExportInvoicesResponse create_invoices_export(body)



Creates an invoice export request.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.167 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
body = swagger_client.ExportInvoicesRequest() # ExportInvoicesRequest | Information required to create the export request.

try:
    api_response = api_instance.create_invoices_export(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->create_invoices_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportInvoicesRequest**](ExportInvoicesRequest.md)| Information required to create the export request. | 

### Return type

[**ExportInvoicesResponse**](ExportInvoicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_government_invoice_document**
> GovtInvoiceDocumentResponse get_government_invoice_document(marketplace_id, transaction_type, shipment_id, invoice_type, inbound_plan_id=inbound_plan_id, file_format=file_format)



Returns an invoiceDocument object containing an invoiceDocumentUrl .  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0167 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
marketplace_id = 'marketplace_id_example' # str | The invoices returned will match the marketplace that you specify.
transaction_type = 'transaction_type_example' # str | Marketplace specific classification of the transaction type that originated the invoice. Check 'transactionType' options using 'getInvoicesAttributes' operation.
shipment_id = 'shipment_id_example' # str | The unique shipment identifier to get an invoice for.
invoice_type = 'invoice_type_example' # str | Marketplace specific classification of the invoice type. Check 'invoiceType' options using 'getInvoicesAttributes' operation.
inbound_plan_id = 'inbound_plan_id_example' # str | The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created. (optional)
file_format = 'file_format_example' # str | Requested file format. Default is XML (optional)

try:
    api_response = api_instance.get_government_invoice_document(marketplace_id, transaction_type, shipment_id, invoice_type, inbound_plan_id=inbound_plan_id, file_format=file_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_government_invoice_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The invoices returned will match the marketplace that you specify. | 
 **transaction_type** | **str**| Marketplace specific classification of the transaction type that originated the invoice. Check &#39;transactionType&#39; options using &#39;getInvoicesAttributes&#39; operation. | 
 **shipment_id** | **str**| The unique shipment identifier to get an invoice for. | 
 **invoice_type** | **str**| Marketplace specific classification of the invoice type. Check &#39;invoiceType&#39; options using &#39;getInvoicesAttributes&#39; operation. | 
 **inbound_plan_id** | **str**| The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created. | [optional] 
 **file_format** | **str**| Requested file format. Default is XML | [optional] 

### Return type

[**GovtInvoiceDocumentResponse**](GovtInvoiceDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_government_invoice_status**
> GovernmentInvoiceStatusResponse get_government_invoice_status(marketplace_id, transaction_type, shipment_id, invoice_type, inbound_plan_id=inbound_plan_id)



Returns the status of an invoice generation request.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0167 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
marketplace_id = 'marketplace_id_example' # str | The invoices status will match the marketplace that you specify.
transaction_type = 'transaction_type_example' # str | Marketplace specific classification of the transaction type that originated the invoice. Check 'transactionType' options using 'getInvoicesAttributes' operation.
shipment_id = 'shipment_id_example' # str | The unique shipment identifier to get an invoice for.
invoice_type = 'invoice_type_example' # str | Marketplace specific classification of the invoice type. Check 'invoiceType' options using 'getInvoicesAttributes' operation.
inbound_plan_id = 'inbound_plan_id_example' # str | The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created. (optional)

try:
    api_response = api_instance.get_government_invoice_status(marketplace_id, transaction_type, shipment_id, invoice_type, inbound_plan_id=inbound_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_government_invoice_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The invoices status will match the marketplace that you specify. | 
 **transaction_type** | **str**| Marketplace specific classification of the transaction type that originated the invoice. Check &#39;transactionType&#39; options using &#39;getInvoicesAttributes&#39; operation. | 
 **shipment_id** | **str**| The unique shipment identifier to get an invoice for. | 
 **invoice_type** | **str**| Marketplace specific classification of the invoice type. Check &#39;invoiceType&#39; options using &#39;getInvoicesAttributes&#39; operation. | 
 **inbound_plan_id** | **str**| The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created. | [optional] 

### Return type

[**GovernmentInvoiceStatusResponse**](GovernmentInvoiceStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> GetInvoiceResponse get_invoice(marketplace_id, invoice_id)



Returns invoice data for the specified invoice. This operation returns only a subset of the invoices data; refer to the response definition to get all the possible attributes. To get the full invoice, use the `createInvoicesExport` operation to start an export request.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 15 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
marketplace_id = 'marketplace_id_example' # str | The marketplace from which you want the invoice.
invoice_id = 'invoice_id_example' # str | The invoice identifier.

try:
    api_response = api_instance.get_invoice(marketplace_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The marketplace from which you want the invoice. | 
 **invoice_id** | **str**| The invoice identifier. | 

### Return type

[**GetInvoiceResponse**](GetInvoiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> GetInvoicesResponse get_invoices(marketplace_id, transaction_identifier_name=transaction_identifier_name, page_size=page_size, date_end=date_end, transaction_type=transaction_type, transaction_identifier_id=transaction_identifier_id, date_start=date_start, series=series, next_token=next_token, sort_order=sort_order, invoice_type=invoice_type, statuses=statuses, external_invoice_id=external_invoice_id, sort_by=sort_by)



Returns invoice details for the invoices that match the filters that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.1 | 20 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
marketplace_id = 'marketplace_id_example' # str | The response includes only the invoices that match the specified marketplace.
transaction_identifier_name = 'transaction_identifier_name_example' # str | The name of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the `transactionIdentifierId` field.Use the `getInvoicesAttributes` operation to check `transactionIdentifierName` options. (optional)
page_size = 56 # int | The maximum number of invoices you want to return in a single call.  Minimum: 1  Maximum: 200 (optional)
date_end = '2013-10-20T19:20:30+01:00' # datetime | The latest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is the current date-time. (optional)
transaction_type = 'transaction_type_example' # str | The marketplace-specific classification of the transaction type for which the invoice was created. Use the `getInvoicesAttributes` operation to check `transactionType` options. (optional)
transaction_identifier_id = 'transaction_identifier_id_example' # str | The ID of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the `transactionIdentifierName` field. (optional)
date_start = '2013-10-20T19:20:30+01:00' # datetime | The earliest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 24 hours prior to the time of the request. (optional)
series = 'series_example' # str | Return invoices with the specified series number. (optional)
next_token = 'next_token_example' # str | The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages. (optional)
sort_order = 'sort_order_example' # str | Sort the invoices in the response in ascending or descending order. (optional)
invoice_type = 'invoice_type_example' # str | The marketplace-specific classification of the invoice type. Use the `getInvoicesAttributes` operation to check `invoiceType` options. (optional)
statuses = ['statuses_example'] # list[str] | A list of statuses that you can use to filter invoices. Use the `getInvoicesAttributes` operation to check invoice status options.  Min count: 1 (optional)
external_invoice_id = 'external_invoice_id_example' # str | Return invoices that match this external ID. This is typically the Government Invoice ID. (optional)
sort_by = 'sort_by_example' # str | The attribute by which you want to sort the invoices in the response. (optional)

try:
    api_response = api_instance.get_invoices(marketplace_id, transaction_identifier_name=transaction_identifier_name, page_size=page_size, date_end=date_end, transaction_type=transaction_type, transaction_identifier_id=transaction_identifier_id, date_start=date_start, series=series, next_token=next_token, sort_order=sort_order, invoice_type=invoice_type, statuses=statuses, external_invoice_id=external_invoice_id, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The response includes only the invoices that match the specified marketplace. | 
 **transaction_identifier_name** | **str**| The name of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the &#x60;transactionIdentifierId&#x60; field.Use the &#x60;getInvoicesAttributes&#x60; operation to check &#x60;transactionIdentifierName&#x60; options. | [optional] 
 **page_size** | **int**| The maximum number of invoices you want to return in a single call.  Minimum: 1  Maximum: 200 | [optional] 
 **date_end** | **datetime**| The latest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is the current date-time. | [optional] 
 **transaction_type** | **str**| The marketplace-specific classification of the transaction type for which the invoice was created. Use the &#x60;getInvoicesAttributes&#x60; operation to check &#x60;transactionType&#x60; options. | [optional] 
 **transaction_identifier_id** | **str**| The ID of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the &#x60;transactionIdentifierName&#x60; field. | [optional] 
 **date_start** | **datetime**| The earliest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 24 hours prior to the time of the request. | [optional] 
 **series** | **str**| Return invoices with the specified series number. | [optional] 
 **next_token** | **str**| The response includes &#x60;nextToken&#x60; when the number of results exceeds the specified &#x60;pageSize&#x60; value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until &#x60;nextToken&#x60; is null. Note that this operation can return empty pages. | [optional] 
 **sort_order** | **str**| Sort the invoices in the response in ascending or descending order. | [optional] 
 **invoice_type** | **str**| The marketplace-specific classification of the invoice type. Use the &#x60;getInvoicesAttributes&#x60; operation to check &#x60;invoiceType&#x60; options. | [optional] 
 **statuses** | [**list[str]**](str.md)| A list of statuses that you can use to filter invoices. Use the &#x60;getInvoicesAttributes&#x60; operation to check invoice status options.  Min count: 1 | [optional] 
 **external_invoice_id** | **str**| Return invoices that match this external ID. This is typically the Government Invoice ID. | [optional] 
 **sort_by** | **str**| The attribute by which you want to sort the invoices in the response. | [optional] 

### Return type

[**GetInvoicesResponse**](GetInvoicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_attributes**
> GetInvoicesAttributesResponse get_invoices_attributes(marketplace_id)



Returns marketplace-dependent schemas and their respective set of possible values.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
marketplace_id = 'marketplace_id_example' # str | The marketplace identifier.

try:
    api_response = api_instance.get_invoices_attributes(marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The marketplace identifier. | 

### Return type

[**GetInvoicesAttributesResponse**](GetInvoicesAttributesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_document**
> GetInvoicesDocumentResponse get_invoices_document(invoices_document_id)



Returns the invoice document's ID and URL. Use the URL to download the ZIP file, which contains the invoices from the corresponding `createInvoicesExport` request.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0167 | 1 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoices_document_id = 'invoices_document_id_example' # str | The export document identifier.

try:
    api_response = api_instance.get_invoices_document(invoices_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoices_document_id** | **str**| The export document identifier. | 

### Return type

[**GetInvoicesDocumentResponse**](GetInvoicesDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_export**
> GetInvoicesExportResponse get_invoices_export(export_id)



Returns invoice export details (including the `exportDocumentId`, if available) for the export that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 15 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
export_id = 'export_id_example' # str | The unique identifier for the export.

try:
    api_response = api_instance.get_invoices_export(export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**| The unique identifier for the export. | 

### Return type

[**GetInvoicesExportResponse**](GetInvoicesExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_exports**
> GetInvoicesExportsResponse get_invoices_exports(marketplace_id, date_start=date_start, next_token=next_token, page_size=page_size, date_end=date_end, status=status)



Returns invoice exports details for exports that match the filters that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.1 | 20 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
marketplace_id = 'marketplace_id_example' # str | The returned exports match the specified marketplace.
date_start = '2013-10-20T19:20:30+01:00' # datetime | The earliest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 30 days ago. (optional)
next_token = 'next_token_example' # str | The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages. (optional)
page_size = 56 # int | The maximum number of invoices to return in a single call.  Minimum: 1  Maximum: 100 (optional)
date_end = '2013-10-20T19:20:30+01:00' # datetime | The latest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default value is the time of the request. (optional)
status = 'status_example' # str | Return exports matching the status specified.  (optional)

try:
    api_response = api_instance.get_invoices_exports(marketplace_id, date_start=date_start, next_token=next_token, page_size=page_size, date_end=date_end, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The returned exports match the specified marketplace. | 
 **date_start** | **datetime**| The earliest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 30 days ago. | [optional] 
 **next_token** | **str**| The response includes &#x60;nextToken&#x60; when the number of results exceeds the specified &#x60;pageSize&#x60; value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until &#x60;nextToken&#x60; is null. Note that this operation can return empty pages. | [optional] 
 **page_size** | **int**| The maximum number of invoices to return in a single call.  Minimum: 1  Maximum: 100 | [optional] 
 **date_end** | **datetime**| The latest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default value is the time of the request. | [optional] 
 **status** | **str**| Return exports matching the status specified.  | [optional] 

### Return type

[**GetInvoicesExportsResponse**](GetInvoicesExportsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

