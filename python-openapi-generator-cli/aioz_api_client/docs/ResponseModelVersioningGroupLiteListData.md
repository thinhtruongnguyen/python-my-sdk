# ResponseModelVersioningGroupLiteListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ModelsModelVersioningGroupLite]**](ModelsModelVersioningGroupLite.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_model_versioning_group_lite_list_data import ResponseModelVersioningGroupLiteListData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseModelVersioningGroupLiteListData from a JSON string
response_model_versioning_group_lite_list_data_instance = ResponseModelVersioningGroupLiteListData.from_json(json)
# print the JSON string representation of the object
print(ResponseModelVersioningGroupLiteListData.to_json())

# convert the object into a dict
response_model_versioning_group_lite_list_data_dict = response_model_versioning_group_lite_list_data_instance.to_dict()
# create an instance of ResponseModelVersioningGroupLiteListData from a dict
response_model_versioning_group_lite_list_data_from_dict = ResponseModelVersioningGroupLiteListData.from_dict(response_model_versioning_group_lite_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


