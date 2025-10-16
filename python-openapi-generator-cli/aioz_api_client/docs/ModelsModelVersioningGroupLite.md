# ModelsModelVersioningGroupLite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_hash** | **str** | Dependency        map[string]interface{} &#x60;json:\&quot;dependency\&quot;&#x60; | [optional] 
**commit_message** | **str** | TestResult        map[string]interface{} &#x60;json:\&quot;test_result\&quot;&#x60; InputFormat       map[string]interface{} &#x60;json:\&quot;input_format\&quot;&#x60; OutputFormat      map[string]interface{} &#x60;json:\&quot;output_format\&quot;&#x60; SysRequired       map[string]interface{} &#x60;json:\&quot;sys_require\&quot;&#x60; | [optional] 
**is_active** | **bool** |  | [optional] 
**last_checked_at** | **str** |  | [optional] 
**model_id** | **str** |  | [optional] 
**pending_platforms** | [**List[ModelsPlatformTask]**](ModelsPlatformTask.md) |  | [optional] 
**rejected_platforms** | [**List[ModelsPlatformTask]**](ModelsPlatformTask.md) |  | [optional] 
**verified_platforms** | [**List[ModelsPlatformTask]**](ModelsPlatformTask.md) |  | [optional] 
**verify_status** | **str** |  | [optional] 

## Example

```python
from aioz_api_client.models.models_model_versioning_group_lite import ModelsModelVersioningGroupLite

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsModelVersioningGroupLite from a JSON string
models_model_versioning_group_lite_instance = ModelsModelVersioningGroupLite.from_json(json)
# print the JSON string representation of the object
print(ModelsModelVersioningGroupLite.to_json())

# convert the object into a dict
models_model_versioning_group_lite_dict = models_model_versioning_group_lite_instance.to_dict()
# create an instance of ModelsModelVersioningGroupLite from a dict
models_model_versioning_group_lite_from_dict = ModelsModelVersioningGroupLite.from_dict(models_model_versioning_group_lite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


