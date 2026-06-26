# ServiceJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **datetime** | The date and time of the creation of the job in ISO 8601 format. | [optional] 
**service_job_id** | [**ServiceJobId**](ServiceJobId.md) | The service job identifier. | [optional] 
**service_job_status** | **str** | The status of the service job. | [optional] 
**scope_of_work** | [**ScopeOfWork**](ScopeOfWork.md) | The scope of work for the order. | [optional] 
**seller** | [**Seller**](Seller.md) | Information about the seller of the service job. | [optional] 
**service_job_provider** | [**ServiceJobProvider**](ServiceJobProvider.md) | Information about the service job provider. | [optional] 
**preferred_appointment_times** | [**list[AppointmentTime]**](AppointmentTime.md) | A list of appointment windows preferred by the buyer. Included only if the buyer selected appointment windows when creating the order. | [optional] 
**appointments** | [**list[Appointment]**](Appointment.md) | A list of appointments. | [optional] 
**service_order_id** | [**OrderId**](OrderId.md) | The Amazon-defined identifier for an order placed by the buyer in 3-7-7 format. | [optional] 
**product_order_ids** | **list[str]** | A list of associated product order IDs for the service job. | [optional] 
**tracking_ids** | **list[str]** | A list of associated product tracking IDs for the service job. | [optional] 
**marketplace_id** | **str** | The marketplace identifier. | [optional] 
**store_id** | **str** | The Amazon-defined identifier for the region scope. | [optional] 
**buyer** | [**Buyer**](Buyer.md) | Information about the buyer. | [optional] 
**associated_items** | [**list[AssociatedItem]**](AssociatedItem.md) | A list of items associated with the service job. | [optional] 
**service_location** | [**ServiceLocation**](ServiceLocation.md) | Information about the location of the service job. | [optional] 
**payments** | [**list[Payment]**](Payment.md) | A list that contains payment information for the service job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


