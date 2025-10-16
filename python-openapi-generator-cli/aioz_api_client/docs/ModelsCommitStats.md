# ModelsCommitStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** |  | [optional] 
**deletions** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_commit_stats import ModelsCommitStats

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsCommitStats from a JSON string
models_commit_stats_instance = ModelsCommitStats.from_json(json)
# print the JSON string representation of the object
print(ModelsCommitStats.to_json())

# convert the object into a dict
models_commit_stats_dict = models_commit_stats_instance.to_dict()
# create an instance of ModelsCommitStats from a dict
models_commit_stats_from_dict = ModelsCommitStats.from_dict(models_commit_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


