# ResponseGetTaskStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseGetTaskStatisticsData**](ResponseGetTaskStatisticsData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_get_task_statistics_response import ResponseGetTaskStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTaskStatisticsResponse from a JSON string
response_get_task_statistics_response_instance = ResponseGetTaskStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTaskStatisticsResponse.to_json())

# convert the object into a dict
response_get_task_statistics_response_dict = response_get_task_statistics_response_instance.to_dict()
# create an instance of ResponseGetTaskStatisticsResponse from a dict
response_get_task_statistics_response_from_dict = ResponseGetTaskStatisticsResponse.from_dict(response_get_task_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


