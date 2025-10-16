# ResponseApiKeyInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsApiKeyInfo**](ModelsApiKeyInfo.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_api_key_info_response import ResponseApiKeyInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseApiKeyInfoResponse from a JSON string
response_api_key_info_response_instance = ResponseApiKeyInfoResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseApiKeyInfoResponse.to_json())

# convert the object into a dict
response_api_key_info_response_dict = response_api_key_info_response_instance.to_dict()
# create an instance of ResponseApiKeyInfoResponse from a dict
response_api_key_info_response_from_dict = ResponseApiKeyInfoResponse.from_dict(response_api_key_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


