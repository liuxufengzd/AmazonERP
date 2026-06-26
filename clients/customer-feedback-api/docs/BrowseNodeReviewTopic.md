# BrowseNodeReviewTopic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | The name browse node review topic. | 
**browse_node_metrics** | [**BrowseNodeReviewTopicMetrics**](BrowseNodeReviewTopicMetrics.md) | The percentage of browse node reviews that mention the topic, and the effect the topic has on the star rating. | 
**review_snippets** | **list[str]** | A list of up to three snippets from reviews that contain the topic. This value is &#x60;null&#x60; if there aren&#39;t enough review snippets for the topic. | [optional] 
**subtopics** | [**list[BrowseNodeSubtopic]**](BrowseNodeSubtopic.md) | A list of the five subtopics that occur most frequently. This value is &#x60;null&#x60; if there are no subtopics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


