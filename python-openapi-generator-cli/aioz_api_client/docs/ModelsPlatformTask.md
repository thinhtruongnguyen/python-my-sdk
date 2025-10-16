# ModelsPlatformTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | [optional] 
**test_result** | **Dict[str, object]** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**verify_task_id** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_platform_task import ModelsPlatformTask

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsPlatformTask from a JSON string
models_platform_task_instance = ModelsPlatformTask.from_json(json)
# print the JSON string representation of the object
print(ModelsPlatformTask.to_json())

# convert the object into a dict
models_platform_task_dict = models_platform_task_instance.to_dict()
# create an instance of ModelsPlatformTask from a dict
models_platform_task_from_dict = ModelsPlatformTask.from_dict(models_platform_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


