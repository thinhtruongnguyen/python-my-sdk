# ModelsApiKeyPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | [optional] 
**uses_remaining** | **int** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_api_key_package import ModelsApiKeyPackage

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiKeyPackage from a JSON string
models_api_key_package_instance = ModelsApiKeyPackage.from_json(json)
# print the JSON string representation of the object
print(ModelsApiKeyPackage.to_json())

# convert the object into a dict
models_api_key_package_dict = models_api_key_package_instance.to_dict()
# create an instance of ModelsApiKeyPackage from a dict
models_api_key_package_from_dict = ModelsApiKeyPackage.from_dict(models_api_key_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


