# ResponseEstimateCostData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** |  | [optional] 
**symbol** | **str** |  | [optional] [default to '$']
**unit** | **str** |  | [optional] [default to 'USD']

## Example

```python
from aioz_api_client.models.response_estimate_cost_data import ResponseEstimateCostData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseEstimateCostData from a JSON string
response_estimate_cost_data_instance = ResponseEstimateCostData.from_json(json)
# print the JSON string representation of the object
print(ResponseEstimateCostData.to_json())

# convert the object into a dict
response_estimate_cost_data_dict = response_estimate_cost_data_instance.to_dict()
# create an instance of ResponseEstimateCostData from a dict
response_estimate_cost_data_from_dict = ResponseEstimateCostData.from_dict(response_estimate_cost_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


