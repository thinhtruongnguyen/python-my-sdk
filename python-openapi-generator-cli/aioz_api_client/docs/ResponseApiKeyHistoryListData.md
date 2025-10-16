# ResponseApiKeyHistoryListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ModelsApiKeyHistories]**](ModelsApiKeyHistories.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_api_key_history_list_data import ResponseApiKeyHistoryListData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseApiKeyHistoryListData from a JSON string
response_api_key_history_list_data_instance = ResponseApiKeyHistoryListData.from_json(json)
# print the JSON string representation of the object
print(ResponseApiKeyHistoryListData.to_json())

# convert the object into a dict
response_api_key_history_list_data_dict = response_api_key_history_list_data_instance.to_dict()
# create an instance of ResponseApiKeyHistoryListData from a dict
response_api_key_history_list_data_from_dict = ResponseApiKeyHistoryListData.from_dict(response_api_key_history_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


