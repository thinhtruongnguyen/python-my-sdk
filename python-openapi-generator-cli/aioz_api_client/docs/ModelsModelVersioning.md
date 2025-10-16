# ModelsModelVersioning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_hash** | **str** |  | [optional] 
**commit_message** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**dependency** | **Dict[str, object]** |  | [optional] 
**id** | **str** |  | [optional] 
**input_format** | **Dict[str, object]** |  | [optional] 
**model_id** | **str** |  | [optional] 
**node_reward** | **float** |  | [optional] 
**output_format** | **Dict[str, object]** |  | [optional] 
**platform** | **str** |  | [optional] 
**sys_require** | **Dict[str, object]** |  | [optional] 
**test_result** | **Dict[str, object]** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**verify_status** | **str** |  | [optional] 
**verify_task_id** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_model_versioning import ModelsModelVersioning

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsModelVersioning from a JSON string
models_model_versioning_instance = ModelsModelVersioning.from_json(json)
# print the JSON string representation of the object
print(ModelsModelVersioning.to_json())

# convert the object into a dict
models_model_versioning_dict = models_model_versioning_instance.to_dict()
# create an instance of ModelsModelVersioning from a dict
models_model_versioning_from_dict = ModelsModelVersioning.from_dict(models_model_versioning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


