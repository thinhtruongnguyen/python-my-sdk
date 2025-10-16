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


Check Valid Source code To Verify Ai Model By Api Key




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **input** | [**RequestCheckValidToVerifyAiModelRequest**](RequestCheckValidToVerifyAiModelRequest.md)| Verify Ai Model Request | 


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

Calculate Cost To Verify Ai Model By Api Key





### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **input** | [**RequestCalculateCostToVerifyAiModelRequest**](RequestCalculateCostToVerifyAiModelRequest.md)| Verify Ai Model Request | 


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


Verify Ai Model By Api Key

valid platform is [window, linux, macApple, macIntel]




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **input** | [**RequestVerifyAiModelRequest**](RequestVerifyAiModelRequest.md)| Verify Ai Model Request | 


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


Get List Verify Model Task By Commit Hash And Status

verifyStatus is one of rejected, verified, pending




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **commit_hash** | **str**|  | 
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

Get Model Versioning By Hub Task Id By Api Key





### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Hub Task&#39;s id | 


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


Get Verify Platform Task By Id By Api Key



Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task&#39;s Id | 

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

