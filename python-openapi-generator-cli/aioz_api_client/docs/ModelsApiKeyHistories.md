# ModelsApiKeyHistories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**model_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_api_key_histories import ModelsApiKeyHistories

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiKeyHistories from a JSON string
models_api_key_histories_instance = ModelsApiKeyHistories.from_json(json)
# print the JSON string representation of the object
print(ModelsApiKeyHistories.to_json())

# convert the object into a dict
models_api_key_histories_dict = models_api_key_histories_instance.to_dict()
# create an instance of ModelsApiKeyHistories from a dict
models_api_key_histories_from_dict = ModelsApiKeyHistories.from_dict(models_api_key_histories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


