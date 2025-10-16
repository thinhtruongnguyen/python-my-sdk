# aioz_api_client.ApiKeyRepositoryApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_repository_owner_username_repository_name_commit_history_get**](ApiKeyRepositoryApi.md#api_key_repository_owner_username_repository_name_commit_history_get) | **GET** /api-key/repository/{ownerUsername}/{repositoryName}/commit/history | Get commit history by repository name and branch name by api key


# **api_key_repository_owner_username_repository_name_commit_history_get**


Get commit history by repository name and branch name by api key




### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_username** | **str**| repository&#39;s owner | 
 **repository_name** | **str**| repository&#39;s name | 
 **sha** | **str**| Sha is the sha of the commit (optional) | 
 **page** | **int**| Page is the page number (default: 1) (optional) | [optional] [default to 1]
 **page_size** | **int**| PageSize is the page size (default: 10) (optional) | [optional] [default to 10]
 **path** | **str**| Path is the path of the file (optional) | [optional] 
 **repo_type** | **str**|  | [optional] 

### Return type

[**ResponseGetCommitHistoryResponse**](ResponseGetCommitHistoryResponse.md)

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

