# ResponseGetApiKeyPermissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseGetApiKeyPermissionData**](ResponseGetApiKeyPermissionData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_get_api_key_permission_response import ResponseGetApiKeyPermissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetApiKeyPermissionResponse from a JSON string
response_get_api_key_permission_response_instance = ResponseGetApiKeyPermissionResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetApiKeyPermissionResponse.to_json())

# convert the object into a dict
response_get_api_key_permission_response_dict = response_get_api_key_permission_response_instance.to_dict()
# create an instance of ResponseGetApiKeyPermissionResponse from a dict
response_get_api_key_permission_response_from_dict = ResponseGetApiKeyPermissionResponse.from_dict(response_get_api_key_permission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


