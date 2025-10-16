# ModelsCommitUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_commit_user import ModelsCommitUser

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsCommitUser from a JSON string
models_commit_user_instance = ModelsCommitUser.from_json(json)
# print the JSON string representation of the object
print(ModelsCommitUser.to_json())

# convert the object into a dict
models_commit_user_dict = models_commit_user_instance.to_dict()
# create an instance of ModelsCommitUser from a dict
models_commit_user_from_dict = ModelsCommitUser.from_dict(models_commit_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


