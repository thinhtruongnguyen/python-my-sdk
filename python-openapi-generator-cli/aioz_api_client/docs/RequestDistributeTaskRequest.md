# RequestDistributeTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[object]** |  | [optional] 
**input_params** | **Dict[str, object]** |  | [optional] 
**model_id** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.request_distribute_task_request import RequestDistributeTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDistributeTaskRequest from a JSON string
request_distribute_task_request_instance = RequestDistributeTaskRequest.from_json(json)
# print the JSON string representation of the object
print(RequestDistributeTaskRequest.to_json())

# convert the object into a dict
request_distribute_task_request_dict = request_distribute_task_request_instance.to_dict()
# create an instance of RequestDistributeTaskRequest from a dict
request_distribute_task_request_from_dict = RequestDistributeTaskRequest.from_dict(request_distribute_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


