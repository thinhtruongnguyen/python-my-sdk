# ResponseModelVersioningGroupLiteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsModelVersioningGroupLite**](ModelsModelVersioningGroupLite.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_model_versioning_group_lite_response import ResponseModelVersioningGroupLiteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseModelVersioningGroupLiteResponse from a JSON string
response_model_versioning_group_lite_response_instance = ResponseModelVersioningGroupLiteResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseModelVersioningGroupLiteResponse.to_json())

# convert the object into a dict
response_model_versioning_group_lite_response_dict = response_model_versioning_group_lite_response_instance.to_dict()
# create an instance of ResponseModelVersioningGroupLiteResponse from a dict
response_model_versioning_group_lite_response_from_dict = ResponseModelVersioningGroupLiteResponse.from_dict(response_model_versioning_group_lite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


