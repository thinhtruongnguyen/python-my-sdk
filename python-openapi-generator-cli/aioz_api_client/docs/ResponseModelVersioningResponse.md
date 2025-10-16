# ResponseModelVersioningResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsModelVersioning**](ModelsModelVersioning.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_model_versioning_response import ResponseModelVersioningResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseModelVersioningResponse from a JSON string
response_model_versioning_response_instance = ResponseModelVersioningResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseModelVersioningResponse.to_json())

# convert the object into a dict
response_model_versioning_response_dict = response_model_versioning_response_instance.to_dict()
# create an instance of ResponseModelVersioningResponse from a dict
response_model_versioning_response_from_dict = ResponseModelVersioningResponse.from_dict(response_model_versioning_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


