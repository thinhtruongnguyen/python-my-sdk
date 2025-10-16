# ResponseFailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'fail']

## Example

```python
from aioz_api_client.models.response_fail_response import ResponseFailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseFailResponse from a JSON string
response_fail_response_instance = ResponseFailResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseFailResponse.to_json())

# convert the object into a dict
response_fail_response_dict = response_fail_response_instance.to_dict()
# create an instance of ResponseFailResponse from a dict
response_fail_response_from_dict = ResponseFailResponse.from_dict(response_fail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


