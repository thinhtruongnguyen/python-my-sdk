# ResponseVerifyAiModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_verify_ai_model_response import ResponseVerifyAiModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseVerifyAiModelResponse from a JSON string
response_verify_ai_model_response_instance = ResponseVerifyAiModelResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseVerifyAiModelResponse.to_json())

# convert the object into a dict
response_verify_ai_model_response_dict = response_verify_ai_model_response_instance.to_dict()
# create an instance of ResponseVerifyAiModelResponse from a dict
response_verify_ai_model_response_from_dict = ResponseVerifyAiModelResponse.from_dict(response_verify_ai_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


