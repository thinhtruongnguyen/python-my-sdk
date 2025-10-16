# ResponseGetListModelVersioningLiteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseGetListModelVersioningsLiteData**](ResponseGetListModelVersioningsLiteData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_get_list_model_versioning_lite_response import ResponseGetListModelVersioningLiteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetListModelVersioningLiteResponse from a JSON string
response_get_list_model_versioning_lite_response_instance = ResponseGetListModelVersioningLiteResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetListModelVersioningLiteResponse.to_json())

# convert the object into a dict
response_get_list_model_versioning_lite_response_dict = response_get_list_model_versioning_lite_response_instance.to_dict()
# create an instance of ResponseGetListModelVersioningLiteResponse from a dict
response_get_list_model_versioning_lite_response_from_dict = ResponseGetListModelVersioningLiteResponse.from_dict(response_get_list_model_versioning_lite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


