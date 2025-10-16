# ResponseWalletWithAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsWalletWithAddress**](ModelsWalletWithAddress.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'success']

## Example

```python
from aioz_api_client.models.response_wallet_with_address_response import ResponseWalletWithAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseWalletWithAddressResponse from a JSON string
response_wallet_with_address_response_instance = ResponseWalletWithAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseWalletWithAddressResponse.to_json())

# convert the object into a dict
response_wallet_with_address_response_dict = response_wallet_with_address_response_instance.to_dict()
# create an instance of ResponseWalletWithAddressResponse from a dict
response_wallet_with_address_response_from_dict = ResponseWalletWithAddressResponse.from_dict(response_wallet_with_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


