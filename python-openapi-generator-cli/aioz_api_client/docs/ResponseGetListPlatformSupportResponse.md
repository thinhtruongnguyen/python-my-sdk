# ResponseGetListPlatformSupportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_get_list_platform_support_response import ResponseGetListPlatformSupportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetListPlatformSupportResponse from a JSON string
response_get_list_platform_support_response_instance = ResponseGetListPlatformSupportResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetListPlatformSupportResponse.to_json())

# convert the object into a dict
response_get_list_platform_support_response_dict = response_get_list_platform_support_response_instance.to_dict()
# create an instance of ResponseGetListPlatformSupportResponse from a dict
response_get_list_platform_support_response_from_dict = ResponseGetListPlatformSupportResponse.from_dict(response_get_list_platform_support_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


