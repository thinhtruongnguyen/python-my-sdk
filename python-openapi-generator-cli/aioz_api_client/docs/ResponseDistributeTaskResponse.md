# ResponseDistributeTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_distribute_task_response import ResponseDistributeTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDistributeTaskResponse from a JSON string
response_distribute_task_response_instance = ResponseDistributeTaskResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseDistributeTaskResponse.to_json())

# convert the object into a dict
response_distribute_task_response_dict = response_distribute_task_response_instance.to_dict()
# create an instance of ResponseDistributeTaskResponse from a dict
response_distribute_task_response_from_dict = ResponseDistributeTaskResponse.from_dict(response_distribute_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


