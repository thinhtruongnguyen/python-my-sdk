# ModelsRepoCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**ModelsCommitUser**](ModelsCommitUser.md) |  | [optional] 
**committer** | [**ModelsCommitUser**](ModelsCommitUser.md) |  | [optional] 
**message** | **str** |  | [optional] 
**tree** | [**ModelsCommitMeta**](ModelsCommitMeta.md) |  | [optional] 

## Example

```python
from aioz_api_client.models.models_repo_commit import ModelsRepoCommit

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsRepoCommit from a JSON string
models_repo_commit_instance = ModelsRepoCommit.from_json(json)
# print the JSON string representation of the object
print(ModelsRepoCommit.to_json())

# convert the object into a dict
models_repo_commit_dict = models_repo_commit_instance.to_dict()
# create an instance of ModelsRepoCommit from a dict
models_repo_commit_from_dict = ModelsRepoCommit.from_dict(models_repo_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


