# ResponseCheckValidToVerifyAiModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseCheckValidToVerifyAiModelData**](ResponseCheckValidToVerifyAiModelData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_check_valid_to_verify_ai_model_response import ResponseCheckValidToVerifyAiModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckValidToVerifyAiModelResponse from a JSON string
response_check_valid_to_verify_ai_model_response_instance = ResponseCheckValidToVerifyAiModelResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckValidToVerifyAiModelResponse.to_json())

# convert the object into a dict
response_check_valid_to_verify_ai_model_response_dict = response_check_valid_to_verify_ai_model_response_instance.to_dict()
# create an instance of ResponseCheckValidToVerifyAiModelResponse from a dict
response_check_valid_to_verify_ai_model_response_from_dict = ResponseCheckValidToVerifyAiModelResponse.from_dict(response_check_valid_to_verify_ai_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


