# ModelsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_request_to_join** | **bool** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**blocked** | **bool** |  | [optional] 
**blocked_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**followers** | [**List[ModelsFollow]**](ModelsFollow.md) |  | [optional] 
**followers_count** | **int** |  | [optional] 
**followings** | [**List[ModelsFollow]**](ModelsFollow.md) |  | [optional] 
**followings_count** | **int** |  | [optional] 
**github_link** | **str** |  | [optional] 
**github_name** | **str** |  | [optional] 
**home_page_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**interests** | **str** |  | [optional] 
**invite_offers** | [**List[ModelsOffer]**](ModelsOffer.md) |  | [optional] 
**invite_offers_count** | **int** |  | [optional] 
**is_following** | **bool** |  | [optional] 
**join_id** | **str** |  | [optional] 
**join_offers** | [**List[ModelsOffer]**](ModelsOffer.md) |  | [optional] 
**join_offers_count** | **int** |  | [optional] 
**members** | [**List[ModelsMember]**](ModelsMember.md) |  | [optional] 
**members_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**twitter_link** | **str** |  | [optional] 
**twitter_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**visibility** | **str** |  | [optional] 
**wallet** | [**ModelsWallet**](ModelsWallet.md) |  | [optional] 
**wallet_address** | **str** |  | [optional] 
**wallet_connection** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_user import ModelsUser

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsUser from a JSON string
models_user_instance = ModelsUser.from_json(json)
# print the JSON string representation of the object
print(ModelsUser.to_json())

# convert the object into a dict
models_user_dict = models_user_instance.to_dict()
# create an instance of ModelsUser from a dict
models_user_from_dict = ModelsUser.from_dict(models_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


