# ModelsCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**ModelsUser**](ModelsUser.md) |  | [optional] 
**commit_affected_files** | **List[str]** |  | [optional] 
**commit_data** | [**ModelsUser**](ModelsUser.md) |  | [optional] 
**commit_meta** | [**ModelsCommitMeta**](ModelsCommitMeta.md) |  | [optional] 
**parents** | [**List[ModelsCommitMeta]**](ModelsCommitMeta.md) |  | [optional] 
**repo_commit** | [**ModelsRepoCommit**](ModelsRepoCommit.md) |  | [optional] 
**stats** | [**ModelsCommitStats**](ModelsCommitStats.md) |  | [optional] 

## Example

```python
from aioz_api_client.models.models_commit import ModelsCommit

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsCommit from a JSON string
models_commit_instance = ModelsCommit.from_json(json)
# print the JSON string representation of the object
print(ModelsCommit.to_json())

# convert the object into a dict
models_commit_dict = models_commit_instance.to_dict()
# create an instance of ModelsCommit from a dict
models_commit_from_dict = ModelsCommit.from_dict(models_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


