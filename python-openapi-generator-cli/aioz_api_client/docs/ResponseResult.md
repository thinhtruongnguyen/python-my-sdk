# ResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_logs** | **str** |  | [optional] 
**output** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_result import ResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseResult from a JSON string
response_result_instance = ResponseResult.from_json(json)
# print the JSON string representation of the object
print(ResponseResult.to_json())

# convert the object into a dict
response_result_dict = response_result_instance.to_dict()
# create an instance of ResponseResult from a dict
response_result_from_dict = ResponseResult.from_dict(response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


