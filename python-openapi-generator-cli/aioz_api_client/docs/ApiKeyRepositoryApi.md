# aioz_api_client.ApiKeyRepositoryApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_repository_owner_username_repository_name_commit_history_get**](ApiKeyRepositoryApi.md#api_key_repository_owner_username_repository_name_commit_history_get) | **GET** /api-key/repository/{ownerUsername}/{repositoryName}/commit/history | Get commit history by repository name and branch name by api key


# **api_key_repository_owner_username_repository_name_commit_history_get**
> ResponseGetCommitHistoryResponse api_key_repository_owner_username_repository_name_commit_history_get(owner_username, repository_name, sha, x_api_key=x_api_key, page=page, page_size=page_size, path=path, repo_type=repo_type)

Get commit history by repository name and branch name by api key

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_get_commit_history_response import ResponseGetCommitHistoryResponse
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
    api_instance = aioz_api_client.ApiKeyRepositoryApi(api_client)
    owner_username = 'owner_username_example' # str | repository's owner
    repository_name = 'repository_name_example' # str | repository's name
    sha = 'sha_example' # str | Sha is the sha of the commit (optional)
    x_api_key = 'x_api_key_example' # str | api-key (optional)
    page = 1 # int | Page is the page number (default: 1) (optional) (optional) (default to 1)
    page_size = 10 # int | PageSize is the page size (default: 10) (optional) (optional) (default to 10)
    path = 'path_example' # str | Path is the path of the file (optional) (optional)
    repo_type = 'repo_type_example' # str |  (optional)

    try:
        # Get commit history by repository name and branch name by api key
        api_response = api_instance.api_key_repository_owner_username_repository_name_commit_history_get(owner_username, repository_name, sha, x_api_key=x_api_key, page=page, page_size=page_size, path=path, repo_type=repo_type)
        print("The response of ApiKeyRepositoryApi->api_key_repository_owner_username_repository_name_commit_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyRepositoryApi->api_key_repository_owner_username_repository_name_commit_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_username** | **str**| repository&#39;s owner | 
 **repository_name** | **str**| repository&#39;s name | 
 **sha** | **str**| Sha is the sha of the commit (optional) | 
 **x_api_key** | **str**| api-key | [optional] 
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

