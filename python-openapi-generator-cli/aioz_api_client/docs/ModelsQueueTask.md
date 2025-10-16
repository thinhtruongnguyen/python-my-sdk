# ModelsQueueTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**object_name** | **str** |  | [optional] 
**result** | **Dict[str, object]** |  | [optional] 
**state** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_queue_task import ModelsQueueTask

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsQueueTask from a JSON string
models_queue_task_instance = ModelsQueueTask.from_json(json)
# print the JSON string representation of the object
print(ModelsQueueTask.to_json())

# convert the object into a dict
models_queue_task_dict = models_queue_task_instance.to_dict()
# create an instance of ModelsQueueTask from a dict
models_queue_task_from_dict = ModelsQueueTask.from_dict(models_queue_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


