# aioz_api_client.ApiKeyModelVersioningApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_model_id_versioning_delete**](ApiKeyModelVersioningApi.md#api_key_model_id_versioning_delete) | **DELETE** /api-key/model/{id}/versioning | Delete Model Versioning By Commit Hash By Api Key
[**api_key_model_id_versioning_get**](ApiKeyModelVersioningApi.md#api_key_model_id_versioning_get) | **GET** /api-key/model/{id}/versioning | Get Current Model Versioning By Model Id By ApiKey
[**api_key_model_id_versioning_list_get**](ApiKeyModelVersioningApi.md#api_key_model_id_versioning_list_get) | **GET** /api-key/model/{id}/versioning/list | Get Verified List Model Versioning By Api Key
[**api_key_model_id_versioning_put**](ApiKeyModelVersioningApi.md#api_key_model_id_versioning_put) | **PUT** /api-key/model/{id}/versioning | Change Model Versioning By Commit Hash By Api Key


# **api_key_model_id_versioning_delete**


Delete Model Versioning By Commit Hash By Api Key



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **commit_hash** | **str**|  | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_model_id_versioning_get**


Get Current Model Versioning By Model Id By ApiKey




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 


### Return type

[**ResponseModelVersioningGroupLiteResponse**](ResponseModelVersioningGroupLiteResponse.md)


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

# **api_key_model_id_versioning_list_get**


Get Verified List Model Versioning By Api Key

verifyStatus is verified or all. Use verified to get verified versioning. Use all to get verified history



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 0]
 **verify_status** | **str**|  | [optional] 

### Return type

[**ResponseGetListModelVersioningLiteResponse**](ResponseGetListModelVersioningLiteResponse.md)



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

# **api_key_model_id_versioning_put**


Change Model Versioning By Commit Hash By Api Key





### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **commit_hash** | **str**|  | 


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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

