# ResponseEstimateCostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseEstimateCostData**](ResponseEstimateCostData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_estimate_cost_response import ResponseEstimateCostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseEstimateCostResponse from a JSON string
response_estimate_cost_response_instance = ResponseEstimateCostResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseEstimateCostResponse.to_json())

# convert the object into a dict
response_estimate_cost_response_dict = response_estimate_cost_response_instance.to_dict()
# create an instance of ResponseEstimateCostResponse from a dict
response_estimate_cost_response_from_dict = ResponseEstimateCostResponse.from_dict(response_estimate_cost_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


