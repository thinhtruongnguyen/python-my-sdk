# RequestCalculateCostToVerifyAiModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_hash** | **str** |  | 
**platforms** | **List[str]** |  | 

## Example

```python
from aioz_api_client.models.request_calculate_cost_to_verify_ai_model_request import RequestCalculateCostToVerifyAiModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCalculateCostToVerifyAiModelRequest from a JSON string
request_calculate_cost_to_verify_ai_model_request_instance = RequestCalculateCostToVerifyAiModelRequest.from_json(json)
# print the JSON string representation of the object
print(RequestCalculateCostToVerifyAiModelRequest.to_json())

# convert the object into a dict
request_calculate_cost_to_verify_ai_model_request_dict = request_calculate_cost_to_verify_ai_model_request_instance.to_dict()
# create an instance of RequestCalculateCostToVerifyAiModelRequest from a dict
request_calculate_cost_to_verify_ai_model_request_from_dict = RequestCalculateCostToVerifyAiModelRequest.from_dict(request_calculate_cost_to_verify_ai_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


