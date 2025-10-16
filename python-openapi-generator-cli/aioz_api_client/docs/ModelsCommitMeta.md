# ModelsCommitMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_commit_meta import ModelsCommitMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsCommitMeta from a JSON string
models_commit_meta_instance = ModelsCommitMeta.from_json(json)
# print the JSON string representation of the object
print(ModelsCommitMeta.to_json())

# convert the object into a dict
models_commit_meta_dict = models_commit_meta_instance.to_dict()
# create an instance of ModelsCommitMeta from a dict
models_commit_meta_from_dict = ModelsCommitMeta.from_dict(models_commit_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


