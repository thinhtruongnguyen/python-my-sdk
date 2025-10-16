# ResponseApiKeyHistoryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseApiKeyHistoryListData**](ResponseApiKeyHistoryListData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_api_key_history_list_response import ResponseApiKeyHistoryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseApiKeyHistoryListResponse from a JSON string
response_api_key_history_list_response_instance = ResponseApiKeyHistoryListResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseApiKeyHistoryListResponse.to_json())

# convert the object into a dict
response_api_key_history_list_response_dict = response_api_key_history_list_response_instance.to_dict()
# create an instance of ResponseApiKeyHistoryListResponse from a dict
response_api_key_history_list_response_from_dict = ResponseApiKeyHistoryListResponse.from_dict(response_api_key_history_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


