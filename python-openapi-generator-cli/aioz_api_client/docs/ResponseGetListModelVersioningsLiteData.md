# ResponseGetListModelVersioningsLiteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ModelsModelVersioningGroupLite]**](ModelsModelVersioningGroupLite.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_get_list_model_versionings_lite_data import ResponseGetListModelVersioningsLiteData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetListModelVersioningsLiteData from a JSON string
response_get_list_model_versionings_lite_data_instance = ResponseGetListModelVersioningsLiteData.from_json(json)
# print the JSON string representation of the object
print(ResponseGetListModelVersioningsLiteData.to_json())

# convert the object into a dict
response_get_list_model_versionings_lite_data_dict = response_get_list_model_versionings_lite_data_instance.to_dict()
# create an instance of ResponseGetListModelVersioningsLiteData from a dict
response_get_list_model_versionings_lite_data_from_dict = ResponseGetListModelVersioningsLiteData.from_dict(response_get_list_model_versionings_lite_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


