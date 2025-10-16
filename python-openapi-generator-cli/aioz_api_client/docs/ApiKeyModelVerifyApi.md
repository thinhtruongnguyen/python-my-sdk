# aioz_api_client.ApiKeyModelVerifyApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_model_id_pre_verify_post**](ApiKeyModelVerifyApi.md#api_key_model_id_pre_verify_post) | **POST** /api-key/model/{id}/pre-verify | Check Valid Source code To Verify Ai Model By Api Key
[**api_key_model_id_verify_cost_post**](ApiKeyModelVerifyApi.md#api_key_model_id_verify_cost_post) | **POST** /api-key/model/{id}/verify/cost | Calculate Cost To Verify Ai Model By Api Key
[**api_key_model_id_verify_post**](ApiKeyModelVerifyApi.md#api_key_model_id_verify_post) | **POST** /api-key/model/{id}/verify | Verify Ai Model By Api Key
[**api_key_model_id_verify_task_get**](ApiKeyModelVerifyApi.md#api_key_model_id_verify_task_get) | **GET** /api-key/model/{id}/verify/task | Get List Verify Model Task By Commit Hash And Status
[**api_key_model_verify_hub_task_id_get**](ApiKeyModelVerifyApi.md#api_key_model_verify_hub_task_id_get) | **GET** /api-key/model/verify/hub/task/{id} | Get Model Versioning By Hub Task Id By Api Key
[**api_key_model_verify_platform_task_id_get**](ApiKeyModelVerifyApi.md#api_key_model_verify_platform_task_id_get) | **GET** /api-key/model/verify/platform/task/{id} | Get Verify Platform Task By Id By Api Key


# **api_key_model_id_pre_verify_post**
> ResponseCheckValidToVerifyAiModelResponse api_key_model_id_pre_verify_post(id, input, x_api_key=x_api_key)

Check Valid Source code To Verify Ai Model By Api Key

### Example


```python
import aioz_api_client
from aioz_api_client.models.request_check_valid_to_verify_ai_model_request import RequestCheckValidToVerifyAiModelRequest
from aioz_api_client.models.response_check_valid_to_verify_ai_model_response import ResponseCheckValidToVerifyAiModelResponse
from aioz_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioz_api_client.Configuration(
    host = "http://localhost/api/v1"
)


# Enter a context with an instance of the API client
with aioz_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioz_api_client.ApiKeyModelVerifyApi(api_client)
    id = 'id_example' # str | Model's id
    input = aioz_api_client.RequestCheckValidToVerifyAiModelRequest() # RequestCheckValidToVerifyAiModelRequest | Verify Ai Model Request
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Check Valid Source code To Verify Ai Model By Api Key
        api_response = api_instance.api_key_model_id_pre_verify_post(id, input, x_api_key=x_api_key)
        print("The response of ApiKeyModelVerifyApi->api_key_model_id_pre_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVerifyApi->api_key_model_id_pre_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **input** | [**RequestCheckValidToVerifyAiModelRequest**](RequestCheckValidToVerifyAiModelRequest.md)| Verify Ai Model Request | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseCheckValidToVerifyAiModelResponse**](ResponseCheckValidToVerifyAiModelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_model_id_verify_cost_post**
> ResponseEstimateCostResponse api_key_model_id_verify_cost_post(id, input, x_api_key=x_api_key)

Calculate Cost To Verify Ai Model By Api Key

### Example


```python
import aioz_api_client
from aioz_api_client.models.request_calculate_cost_to_verify_ai_model_request import RequestCalculateCostToVerifyAiModelRequest
from aioz_api_client.models.response_estimate_cost_response import ResponseEstimateCostResponse
from aioz_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioz_api_client.Configuration(
    host = "http://localhost/api/v1"
)


# Enter a context with an instance of the API client
with aioz_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioz_api_client.ApiKeyModelVerifyApi(api_client)
    id = 'id_example' # str | Model's id
    input = aioz_api_client.RequestCalculateCostToVerifyAiModelRequest() # RequestCalculateCostToVerifyAiModelRequest | Verify Ai Model Request
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Calculate Cost To Verify Ai Model By Api Key
        api_response = api_instance.api_key_model_id_verify_cost_post(id, input, x_api_key=x_api_key)
        print("The response of ApiKeyModelVerifyApi->api_key_model_id_verify_cost_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVerifyApi->api_key_model_id_verify_cost_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **input** | [**RequestCalculateCostToVerifyAiModelRequest**](RequestCalculateCostToVerifyAiModelRequest.md)| Verify Ai Model Request | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseEstimateCostResponse**](ResponseEstimateCostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_model_id_verify_post**
> ResponseVerifyAiModelResponse api_key_model_id_verify_post(id, input, x_api_key=x_api_key)

Verify Ai Model By Api Key

valid platform is [window, linux, macApple, macIntel]

### Example


```python
import aioz_api_client
from aioz_api_client.models.request_verify_ai_model_request import RequestVerifyAiModelRequest
from aioz_api_client.models.response_verify_ai_model_response import ResponseVerifyAiModelResponse
from aioz_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioz_api_client.Configuration(
    host = "http://localhost/api/v1"
)


# Enter a context with an instance of the API client
with aioz_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioz_api_client.ApiKeyModelVerifyApi(api_client)
    id = 'id_example' # str | Model's id
    input = aioz_api_client.RequestVerifyAiModelRequest() # RequestVerifyAiModelRequest | Verify Ai Model Request
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Verify Ai Model By Api Key
        api_response = api_instance.api_key_model_id_verify_post(id, input, x_api_key=x_api_key)
        print("The response of ApiKeyModelVerifyApi->api_key_model_id_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVerifyApi->api_key_model_id_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **input** | [**RequestVerifyAiModelRequest**](RequestVerifyAiModelRequest.md)| Verify Ai Model Request | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseVerifyAiModelResponse**](ResponseVerifyAiModelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_model_id_verify_task_get**
> ResponseModelVersioningGroupLiteListResponse api_key_model_id_verify_task_get(id, commit_hash, x_api_key=x_api_key, verify_status=verify_status)

Get List Verify Model Task By Commit Hash And Status

verifyStatus is one of rejected, verified, pending

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_model_versioning_group_lite_list_response import ResponseModelVersioningGroupLiteListResponse
from aioz_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioz_api_client.Configuration(
    host = "http://localhost/api/v1"
)


# Enter a context with an instance of the API client
with aioz_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioz_api_client.ApiKeyModelVerifyApi(api_client)
    id = 'id_example' # str | Model's id
    commit_hash = 'commit_hash_example' # str | 
    x_api_key = 'x_api_key_example' # str | api-key (optional)
    verify_status = 'verify_status_example' # str |  (optional)

    try:
        # Get List Verify Model Task By Commit Hash And Status
        api_response = api_instance.api_key_model_id_verify_task_get(id, commit_hash, x_api_key=x_api_key, verify_status=verify_status)
        print("The response of ApiKeyModelVerifyApi->api_key_model_id_verify_task_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVerifyApi->api_key_model_id_verify_task_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **commit_hash** | **str**|  | 
 **x_api_key** | **str**| api-key | [optional] 
 **verify_status** | **str**|  | [optional] 

### Return type

[**ResponseModelVersioningGroupLiteListResponse**](ResponseModelVersioningGroupLiteListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_model_verify_hub_task_id_get**
> ResponseModelVersioningResponse api_key_model_verify_hub_task_id_get(id, x_api_key=x_api_key)

Get Model Versioning By Hub Task Id By Api Key

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_model_versioning_response import ResponseModelVersioningResponse
from aioz_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioz_api_client.Configuration(
    host = "http://localhost/api/v1"
)


# Enter a context with an instance of the API client
with aioz_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioz_api_client.ApiKeyModelVerifyApi(api_client)
    id = 'id_example' # str | Hub Task's id
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Model Versioning By Hub Task Id By Api Key
        api_response = api_instance.api_key_model_verify_hub_task_id_get(id, x_api_key=x_api_key)
        print("The response of ApiKeyModelVerifyApi->api_key_model_verify_hub_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVerifyApi->api_key_model_verify_hub_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Hub Task&#39;s id | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseModelVersioningResponse**](ResponseModelVersioningResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_model_verify_platform_task_id_get**
> ResponseQueueTaskResponse api_key_model_verify_platform_task_id_get(id, x_api_key=x_api_key)

Get Verify Platform Task By Id By Api Key

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_queue_task_response import ResponseQueueTaskResponse
from aioz_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioz_api_client.Configuration(
    host = "http://localhost/api/v1"
)


# Enter a context with an instance of the API client
with aioz_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioz_api_client.ApiKeyModelVerifyApi(api_client)
    id = 'id_example' # str | Task's Id
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Verify Platform Task By Id By Api Key
        api_response = api_instance.api_key_model_verify_platform_task_id_get(id, x_api_key=x_api_key)
        print("The response of ApiKeyModelVerifyApi->api_key_model_verify_platform_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVerifyApi->api_key_model_verify_platform_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task&#39;s Id | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseQueueTaskResponse**](ResponseQueueTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

