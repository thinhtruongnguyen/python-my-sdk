# ResponseGetTaskResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ResponseResult**](ResponseResult.md) |  | [optional] 
**status** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**traceback** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_get_task_result_data import ResponseGetTaskResultData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTaskResultData from a JSON string
response_get_task_result_data_instance = ResponseGetTaskResultData.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTaskResultData.to_json())

# convert the object into a dict
response_get_task_result_data_dict = response_get_task_result_data_instance.to_dict()
# create an instance of ResponseGetTaskResultData from a dict
response_get_task_result_data_from_dict = ResponseGetTaskResultData.from_dict(response_get_task_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


