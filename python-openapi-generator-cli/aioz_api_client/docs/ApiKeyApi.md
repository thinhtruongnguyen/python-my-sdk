# aioz_api_client.ApiKeyApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_balance_get**](ApiKeyApi.md#api_key_balance_get) | **GET** /api-key/balance | Get Api Key Balance
[**api_key_permission_get**](ApiKeyApi.md#api_key_permission_get) | **GET** /api-key/permission | Get Api Key Permission
[**api_key_statistics_post**](ApiKeyApi.md#api_key_statistics_post) | **POST** /api-key/statistics | Get Api Key Statistics
[**api_key_task_histories_get**](ApiKeyApi.md#api_key_task_histories_get) | **GET** /api-key/task/histories | Get Tasks Histories
[**api_key_task_id_cancel_delete**](ApiKeyApi.md#api_key_task_id_cancel_delete) | **DELETE** /api-key/task/{id}/cancel | Cancel Task By Api Key
[**api_key_task_id_result_get**](ApiKeyApi.md#api_key_task_id_result_get) | **GET** /api-key/task/{id}/result | Get Task Result
[**api_key_task_post**](ApiKeyApi.md#api_key_task_post) | **POST** /api-key/task | Distribute Task (Api-Key)


# **api_key_balance_get**

Get Api Key Balance


### Return type

[**ResponseWalletWithAddressResponse**](ResponseWalletWithAddressResponse.md)

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

# **api_key_permission_get**


Get Api Key Permission


### Return type

[**ResponseGetApiKeyPermissionResponse**](ResponseGetApiKeyPermissionResponse.md)


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

# **api_key_statistics_post**

Get Api Key Statistics


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**RequestGetApiKeyStatisticsByModelIdRequest**](RequestGetApiKeyStatisticsByModelIdRequest.md)| Get Api Key Statistics Request | 


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

# **api_key_task_histories_get**

Get Tasks Histories


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ResponseApiKeyHistoryListResponse**](ResponseApiKeyHistoryListResponse.md)


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

# **api_key_task_id_cancel_delete**


Cancel Task By Api Key





### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task&#39;s id | 


### Return type

[**ResponseSuccessResponse**](ResponseSuccessResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_task_id_result_get**


Get Task Result



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task&#39;s id | 


### Return type

[**ResponseGetTaskResultResponse**](ResponseGetTaskResultResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_task_post**

Distribute Task (Api-Key)




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**RequestDistributeTaskRequest**](RequestDistributeTaskRequest.md)| Distribute Task Request | 


### Return type

[**ResponseDistributeTaskResponse**](ResponseDistributeTaskResponse.md)


### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

