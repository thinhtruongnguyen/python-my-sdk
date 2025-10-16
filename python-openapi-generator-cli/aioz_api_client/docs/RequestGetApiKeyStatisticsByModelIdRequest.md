# RequestGetApiKeyStatisticsByModelIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.request_get_api_key_statistics_by_model_id_request import RequestGetApiKeyStatisticsByModelIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestGetApiKeyStatisticsByModelIdRequest from a JSON string
request_get_api_key_statistics_by_model_id_request_instance = RequestGetApiKeyStatisticsByModelIdRequest.from_json(json)
# print the JSON string representation of the object
print(RequestGetApiKeyStatisticsByModelIdRequest.to_json())

# convert the object into a dict
request_get_api_key_statistics_by_model_id_request_dict = request_get_api_key_statistics_by_model_id_request_instance.to_dict()
# create an instance of RequestGetApiKeyStatisticsByModelIdRequest from a dict
request_get_api_key_statistics_by_model_id_request_from_dict = RequestGetApiKeyStatisticsByModelIdRequest.from_dict(request_get_api_key_statistics_by_model_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


