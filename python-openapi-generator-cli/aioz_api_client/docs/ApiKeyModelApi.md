# aioz_api_client.ApiKeyModelApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_model_id_info_get**](ApiKeyModelApi.md#api_key_model_id_info_get) | **GET** /api-key/model/{id}/info | Get Api Key Model Info
[**api_key_model_id_serving_get**](ApiKeyModelApi.md#api_key_model_id_serving_get) | **GET** /api-key/model/{id}/serving | Check Model Is Serving
[**api_key_model_id_statistics_post**](ApiKeyModelApi.md#api_key_model_id_statistics_post) | **POST** /api-key/model/{id}/statistics | Get Model Statistics
[**api_key_model_id_task_cost_get**](ApiKeyModelApi.md#api_key_model_id_task_cost_get) | **GET** /api-key/model/{id}/task/cost | Get cost to compute task by model api key
[**api_key_model_verify_support_platforms_get**](ApiKeyModelApi.md#api_key_model_verify_support_platforms_get) | **GET** /api-key/model/verify/support/platforms | Get List Platforms Support By Api Key


# **api_key_model_id_info_get**

Get Api Key Model Info




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 

### Return type

[**ResponseApiKeyInfoResponse**](ResponseApiKeyInfoResponse.md)


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

# **api_key_model_id_serving_get**

Check Model Is Serving





### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 


### Return type

[**ResponseCheckModelIsServingResponse**](ResponseCheckModelIsServingResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_model_id_statistics_post**


Get Model Statistics




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **input** | [**RequestGetApiKeyStatisticsByModelIdRequest**](RequestGetApiKeyStatisticsByModelIdRequest.md)| Get Api Key Statistics By Model Id Request | 


### Return type

[**ResponseGetTaskStatisticsResponse**](ResponseGetTaskStatisticsResponse.md)


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

# **api_key_model_id_task_cost_get**


Get cost to compute task by model api key




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 


### Return type

[**ResponseEstimateCostResponse**](ResponseEstimateCostResponse.md)


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

# **api_key_model_verify_support_platforms_get**

Get List Platforms Support By Api Key





### Return type

[**ResponseGetListPlatformSupportResponse**](ResponseGetListPlatformSupportResponse.md)



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

