# BrowseNodeReturnTrendsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browse_node_id** | **str** | The requested browse node id. A browse node id is the unique identifier of a given browse node. | 
**display_name** | **str** | The display name of the browse node, as visible on the Amazon retail website. | 
**marketplace_id** | **str** | The requested marketplace id. | 
**country_code** | **str** | The two digit country code of requested marketplace id, in ISO 3166-1 alpha-2 format. | 
**date_range** | [**DateRange**](DateRange.md) | The range of dates during which the returns were made. | 
**return_trends** | [**list[BrowseNodeReturnTrend]**](BrowseNodeReturnTrend.md) | The browse node return trends. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


