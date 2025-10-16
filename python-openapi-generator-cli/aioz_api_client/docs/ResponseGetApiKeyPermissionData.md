# ResponseGetApiKeyPermissionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_packages** | [**List[ModelsApiKeyPackage]**](ModelsApiKeyPackage.md) |  | [optional] 
**limit_models** | **bool** |  | [optional] 
**models** | **List[str]** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_get_api_key_permission_data import ResponseGetApiKeyPermissionData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetApiKeyPermissionData from a JSON string
response_get_api_key_permission_data_instance = ResponseGetApiKeyPermissionData.from_json(json)
# print the JSON string representation of the object
print(ResponseGetApiKeyPermissionData.to_json())

# convert the object into a dict
response_get_api_key_permission_data_dict = response_get_api_key_permission_data_instance.to_dict()
# create an instance of ResponseGetApiKeyPermissionData from a dict
response_get_api_key_permission_data_from_dict = ResponseGetApiKeyPermissionData.from_dict(response_get_api_key_permission_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


