# ResponseQueueTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsQueueTask**](ModelsQueueTask.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_queue_task_response import ResponseQueueTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseQueueTaskResponse from a JSON string
response_queue_task_response_instance = ResponseQueueTaskResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseQueueTaskResponse.to_json())

# convert the object into a dict
response_queue_task_response_dict = response_queue_task_response_instance.to_dict()
# create an instance of ResponseQueueTaskResponse from a dict
response_queue_task_response_from_dict = ResponseQueueTaskResponse.from_dict(response_queue_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


