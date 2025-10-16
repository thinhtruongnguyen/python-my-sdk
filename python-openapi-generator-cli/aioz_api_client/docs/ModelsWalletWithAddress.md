# ModelsWalletWithAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** |  | [optional] 
**debt** | **float** |  | [optional] 
**earnings** | **float** |  | [optional] 
**free_balance** | **float** |  | [optional] 
**wallet_address** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_wallet_with_address import ModelsWalletWithAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsWalletWithAddress from a JSON string
models_wallet_with_address_instance = ModelsWalletWithAddress.from_json(json)
# print the JSON string representation of the object
print(ModelsWalletWithAddress.to_json())

# convert the object into a dict
models_wallet_with_address_dict = models_wallet_with_address_instance.to_dict()
# create an instance of ModelsWalletWithAddress from a dict
models_wallet_with_address_from_dict = ModelsWalletWithAddress.from_dict(models_wallet_with_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


