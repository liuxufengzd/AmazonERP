# BrowseNodeReviewTopics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positive_topics** | [**list[BrowseNodeReviewTopic]**](BrowseNodeReviewTopic.md) | A list of the most positive review topics. When the &#x60;sortBy&#x60; query parameter is set to &#x60;MENTIONS&#x60;, the number of reviews of items within the requested browse node that mention the topic determine the topic&#39;s placement in the list. When &#x60;sortBy&#x60; is set to &#x60;STAR_RATING_IMPACT&#x60;, the effect that the topic has on the star rating of items within the requested browse node determine placement in the list. This value is &#x60;null&#x60; if there are not enough positive reviews for the requested browse node.  **Max length:** 10 | [optional] 
**negative_topics** | [**list[BrowseNodeReviewTopic]**](BrowseNodeReviewTopic.md) | A list of the most negative review topics. When the &#x60;sortBy&#x60; query parameter is set to &#x60;MENTIONS&#x60;, the number of reviews of items within the requested browse node that mention the topic determine the topic&#39;s placement in the list. When &#x60;sortBy&#x60; is set to &#x60;STAR_RATING_IMPACT&#x60;, the effect that the topic has on the star rating of items within the requested browse node determine placement in the list. This value is &#x60;null&#x60; if there are not enough negative reviews for the requested browse node.  **Max length:** 10 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


