# ItemReviewTopic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | The name of the item review topic. | 
**asin_metrics** | [**ItemReviewTopicMetrics**](ItemReviewTopicMetrics.md) | The ASIN&#39;s review topic metrics. | 
**parent_asin_metrics** | [**ItemReviewTopicMetrics**](ItemReviewTopicMetrics.md) | The parent ASIN&#39;s review topic metrics. This value is &#x60;null&#x60; if there isn&#39;t enough topic data for the parent ASIN. | [optional] 
**browse_node_metrics** | [**ItemReviewBrowseNodeMetrics**](ItemReviewBrowseNodeMetrics.md) | The browse node&#39;s review topic metrics. This value is &#x60;null&#x60; if there isn&#39;t enough topic data for the browse node. | [optional] 
**child_asin_metrics** | [**ChildAsinMetrics**](ChildAsinMetrics.md) | The review topic metrics for other child ASINs that have the same parent ASIN. This value is &#x60;null&#x60; if there isn&#39;t any child ASIN metric data. | [optional] 
**review_snippets** | **list[str]** | A list of up to three snippets from reviews that contain the topic. This value is &#x60;null&#x60; if there aren&#39;t enough review snippets for the topic. | [optional] 
**subtopics** | [**list[ItemReviewSubtopic]**](ItemReviewSubtopic.md) | A list of up to five top subtopics for the topic. The percentage of customer reviews that mention the subtopic determine the topic&#39;s placement in the list. This value is &#x60;null&#x60; if there are no subtopics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


