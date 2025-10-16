# ResponseGetCommitHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseGetCommitHistoryData**](ResponseGetCommitHistoryData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_get_commit_history_response import ResponseGetCommitHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetCommitHistoryResponse from a JSON string
response_get_commit_history_response_instance = ResponseGetCommitHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetCommitHistoryResponse.to_json())

# convert the object into a dict
response_get_commit_history_response_dict = response_get_commit_history_response_instance.to_dict()
# create an instance of ResponseGetCommitHistoryResponse from a dict
response_get_commit_history_response_from_dict = ResponseGetCommitHistoryResponse.from_dict(response_get_commit_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


