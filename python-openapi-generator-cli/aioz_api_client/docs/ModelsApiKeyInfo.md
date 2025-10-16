# ModelsApiKeyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_price** | **float** |  | [optional] 
**commit_hash** | **str** |  | [optional] 
**input_format** | **Dict[str, object]** |  | [optional] 
**model_description** | **str** |  | [optional] 
**model_id** | **str** |  | [optional] 
**output_format** | **Dict[str, object]** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_api_key_info import ModelsApiKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiKeyInfo from a JSON string
models_api_key_info_instance = ModelsApiKeyInfo.from_json(json)
# print the JSON string representation of the object
print(ModelsApiKeyInfo.to_json())

# convert the object into a dict
models_api_key_info_dict = models_api_key_info_instance.to_dict()
# create an instance of ModelsApiKeyInfo from a dict
models_api_key_info_from_dict = ModelsApiKeyInfo.from_dict(models_api_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


