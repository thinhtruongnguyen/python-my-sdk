# ResponseCheckModelIsServingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumers** | **int** |  | [optional] 
**serving** | **bool** |  | [optional] 

## Example

```python
from aioz_api_client.models.response_check_model_is_serving_data import ResponseCheckModelIsServingData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckModelIsServingData from a JSON string
response_check_model_is_serving_data_instance = ResponseCheckModelIsServingData.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckModelIsServingData.to_json())

# convert the object into a dict
response_check_model_is_serving_data_dict = response_check_model_is_serving_data_instance.to_dict()
# create an instance of ResponseCheckModelIsServingData from a dict
response_check_model_is_serving_data_from_dict = ResponseCheckModelIsServingData.from_dict(response_check_model_is_serving_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


