# ResponseModelVersioningGroupLiteListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseModelVersioningGroupLiteListData**](ResponseModelVersioningGroupLiteListData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_model_versioning_group_lite_list_response import ResponseModelVersioningGroupLiteListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseModelVersioningGroupLiteListResponse from a JSON string
response_model_versioning_group_lite_list_response_instance = ResponseModelVersioningGroupLiteListResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseModelVersioningGroupLiteListResponse.to_json())

# convert the object into a dict
response_model_versioning_group_lite_list_response_dict = response_model_versioning_group_lite_list_response_instance.to_dict()
# create an instance of ResponseModelVersioningGroupLiteListResponse from a dict
response_model_versioning_group_lite_list_response_from_dict = ResponseModelVersioningGroupLiteListResponse.from_dict(response_model_versioning_group_lite_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


