# ModelsFollow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_follow import ModelsFollow

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsFollow from a JSON string
models_follow_instance = ModelsFollow.from_json(json)
# print the JSON string representation of the object
print(ModelsFollow.to_json())

# convert the object into a dict
models_follow_dict = models_follow_instance.to_dict()
# create an instance of ModelsFollow from a dict
models_follow_from_dict = ModelsFollow.from_dict(models_follow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


