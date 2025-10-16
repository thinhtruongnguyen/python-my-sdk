# ResponseGetTaskResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseGetTaskResultData**](ResponseGetTaskResultData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_get_task_result_response import ResponseGetTaskResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTaskResultResponse from a JSON string
response_get_task_result_response_instance = ResponseGetTaskResultResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTaskResultResponse.to_json())

# convert the object into a dict
response_get_task_result_response_dict = response_get_task_result_response_instance.to_dict()
# create an instance of ResponseGetTaskResultResponse from a dict
response_get_task_result_response_from_dict = ResponseGetTaskResultResponse.from_dict(response_get_task_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


