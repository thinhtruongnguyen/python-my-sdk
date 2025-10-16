# ResponseGetTaskStatisticsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cost** | **int** |  | [optional] 
**total_failed** | **int** |  | [optional] 
**total_request** | **int** |  | [optional] 
**total_success** | **int** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_get_task_statistics_data import ResponseGetTaskStatisticsData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTaskStatisticsData from a JSON string
response_get_task_statistics_data_instance = ResponseGetTaskStatisticsData.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTaskStatisticsData.to_json())

# convert the object into a dict
response_get_task_statistics_data_dict = response_get_task_statistics_data_instance.to_dict()
# create an instance of ResponseGetTaskStatisticsData from a dict
response_get_task_statistics_data_from_dict = ResponseGetTaskStatisticsData.from_dict(response_get_task_statistics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


