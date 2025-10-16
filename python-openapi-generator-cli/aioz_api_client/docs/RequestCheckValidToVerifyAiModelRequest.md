# RequestCheckValidToVerifyAiModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_hash** | **str** |  | 
**platforms** | **List[str]** |  | 

## Example

```python
from aioz_api_client.models.request_check_valid_to_verify_ai_model_request import RequestCheckValidToVerifyAiModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCheckValidToVerifyAiModelRequest from a JSON string
request_check_valid_to_verify_ai_model_request_instance = RequestCheckValidToVerifyAiModelRequest.from_json(json)
# print the JSON string representation of the object
print(RequestCheckValidToVerifyAiModelRequest.to_json())

# convert the object into a dict
request_check_valid_to_verify_ai_model_request_dict = request_check_valid_to_verify_ai_model_request_instance.to_dict()
# create an instance of RequestCheckValidToVerifyAiModelRequest from a dict
request_check_valid_to_verify_ai_model_request_from_dict = RequestCheckValidToVerifyAiModelRequest.from_dict(request_check_valid_to_verify_ai_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


