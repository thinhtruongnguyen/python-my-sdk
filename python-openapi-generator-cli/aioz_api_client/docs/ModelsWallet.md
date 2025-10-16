# ModelsWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** |  | [optional] 
**debt** | **float** |  | [optional] 
**earnings** | **float** |  | [optional] 
**free_balance** | **float** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_wallet import ModelsWallet

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsWallet from a JSON string
models_wallet_instance = ModelsWallet.from_json(json)
# print the JSON string representation of the object
print(ModelsWallet.to_json())

# convert the object into a dict
models_wallet_dict = models_wallet_instance.to_dict()
# create an instance of ModelsWallet from a dict
models_wallet_from_dict = ModelsWallet.from_dict(models_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


