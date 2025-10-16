# RequestVerifyAiModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_hash** | **str** |  | [optional] 
**platforms** | **List[str]** |  | 

## Example

```python
from aioz_api_client.models.request_verify_ai_model_request import RequestVerifyAiModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestVerifyAiModelRequest from a JSON string
request_verify_ai_model_request_instance = RequestVerifyAiModelRequest.from_json(json)
# print the JSON string representation of the object
print(RequestVerifyAiModelRequest.to_json())

# convert the object into a dict
request_verify_ai_model_request_dict = request_verify_ai_model_request_instance.to_dict()
# create an instance of RequestVerifyAiModelRequest from a dict
request_verify_ai_model_request_from_dict = RequestVerifyAiModelRequest.from_dict(request_verify_ai_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


