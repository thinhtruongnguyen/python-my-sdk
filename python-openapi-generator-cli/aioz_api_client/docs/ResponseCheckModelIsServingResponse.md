# ResponseCheckModelIsServingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseCheckModelIsServingData**](ResponseCheckModelIsServingData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_check_model_is_serving_response import ResponseCheckModelIsServingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckModelIsServingResponse from a JSON string
response_check_model_is_serving_response_instance = ResponseCheckModelIsServingResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckModelIsServingResponse.to_json())

# convert the object into a dict
response_check_model_is_serving_response_dict = response_check_model_is_serving_response_instance.to_dict()
# create an instance of ResponseCheckModelIsServingResponse from a dict
response_check_model_is_serving_response_from_dict = ResponseCheckModelIsServingResponse.from_dict(response_check_model_is_serving_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


