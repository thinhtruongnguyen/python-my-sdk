# ModelsOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**exp_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**org_username** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_offer import ModelsOffer

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsOffer from a JSON string
models_offer_instance = ModelsOffer.from_json(json)
# print the JSON string representation of the object
print(ModelsOffer.to_json())

# convert the object into a dict
models_offer_dict = models_offer_instance.to_dict()
# create an instance of ModelsOffer from a dict
models_offer_from_dict = ModelsOffer.from_dict(models_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


