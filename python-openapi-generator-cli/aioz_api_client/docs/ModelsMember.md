# ModelsMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_member import ModelsMember

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsMember from a JSON string
models_member_instance = ModelsMember.from_json(json)
# print the JSON string representation of the object
print(ModelsMember.to_json())

# convert the object into a dict
models_member_dict = models_member_instance.to_dict()
# create an instance of ModelsMember from a dict
models_member_from_dict = ModelsMember.from_dict(models_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


