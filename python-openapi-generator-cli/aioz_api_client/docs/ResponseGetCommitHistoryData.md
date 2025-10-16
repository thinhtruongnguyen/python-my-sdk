# ResponseGetCommitHistoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**List[ModelsCommit]**](ModelsCommit.md) |  | [optional] 
**has_more** | **bool** |  | [optional] 
**last_page** | **int** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_get_commit_history_data import ResponseGetCommitHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetCommitHistoryData from a JSON string
response_get_commit_history_data_instance = ResponseGetCommitHistoryData.from_json(json)
# print the JSON string representation of the object
print(ResponseGetCommitHistoryData.to_json())

# convert the object into a dict
response_get_commit_history_data_dict = response_get_commit_history_data_instance.to_dict()
# create an instance of ResponseGetCommitHistoryData from a dict
response_get_commit_history_data_from_dict = ResponseGetCommitHistoryData.from_dict(response_get_commit_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


