# ResponseSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_success_response import ResponseSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessResponse from a JSON string
response_success_response_instance = ResponseSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseSuccessResponse.to_json())

# convert the object into a dict
response_success_response_dict = response_success_response_instance.to_dict()
# create an instance of ResponseSuccessResponse from a dict
response_success_response_from_dict = ResponseSuccessResponse.from_dict(response_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


