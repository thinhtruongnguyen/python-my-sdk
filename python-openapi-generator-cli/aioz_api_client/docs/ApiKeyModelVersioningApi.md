# aioz_api_client.ApiKeyModelVersioningApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_model_id_versioning_delete**](ApiKeyModelVersioningApi.md#api_key_model_id_versioning_delete) | **DELETE** /api-key/model/{id}/versioning | Delete Model Versioning By Commit Hash By Api Key
[**api_key_model_id_versioning_get**](ApiKeyModelVersioningApi.md#api_key_model_id_versioning_get) | **GET** /api-key/model/{id}/versioning | Get Current Model Versioning By Model Id By ApiKey
[**api_key_model_id_versioning_list_get**](ApiKeyModelVersioningApi.md#api_key_model_id_versioning_list_get) | **GET** /api-key/model/{id}/versioning/list | Get Verified List Model Versioning By Api Key
[**api_key_model_id_versioning_put**](ApiKeyModelVersioningApi.md#api_key_model_id_versioning_put) | **PUT** /api-key/model/{id}/versioning | Change Model Versioning By Commit Hash By Api Key


# **api_key_model_id_versioning_delete**
> ResponseSuccessResponse api_key_model_id_versioning_delete(id, commit_hash, x_api_key=x_api_key)

Delete Model Versioning By Commit Hash By Api Key

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_success_response import ResponseSuccessResponse
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
    api_instance = aioz_api_client.ApiKeyModelVersioningApi(api_client)
    id = 'id_example' # str | Model's id
    commit_hash = 'commit_hash_example' # str | 
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Delete Model Versioning By Commit Hash By Api Key
        api_response = api_instance.api_key_model_id_versioning_delete(id, commit_hash, x_api_key=x_api_key)
        print("The response of ApiKeyModelVersioningApi->api_key_model_id_versioning_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVersioningApi->api_key_model_id_versioning_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **commit_hash** | **str**|  | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseSuccessResponse**](ResponseSuccessResponse.md)

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

# **api_key_model_id_versioning_get**
> ResponseModelVersioningGroupLiteResponse api_key_model_id_versioning_get(id, x_api_key=x_api_key)

Get Current Model Versioning By Model Id By ApiKey

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_model_versioning_group_lite_response import ResponseModelVersioningGroupLiteResponse
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
    api_instance = aioz_api_client.ApiKeyModelVersioningApi(api_client)
    id = 'id_example' # str | Model's id
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Current Model Versioning By Model Id By ApiKey
        api_response = api_instance.api_key_model_id_versioning_get(id, x_api_key=x_api_key)
        print("The response of ApiKeyModelVersioningApi->api_key_model_id_versioning_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVersioningApi->api_key_model_id_versioning_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseModelVersioningGroupLiteResponse**](ResponseModelVersioningGroupLiteResponse.md)

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

# **api_key_model_id_versioning_list_get**
> ResponseGetListModelVersioningLiteResponse api_key_model_id_versioning_list_get(id, x_api_key=x_api_key, limit=limit, offset=offset, verify_status=verify_status)

Get Verified List Model Versioning By Api Key

verifyStatus is verified or all. Use verified to get verified versioning. Use all to get verified history

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_get_list_model_versioning_lite_response import ResponseGetListModelVersioningLiteResponse
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
    api_instance = aioz_api_client.ApiKeyModelVersioningApi(api_client)
    id = 'id_example' # str | Model's id
    x_api_key = 'x_api_key_example' # str | api-key (optional)
    limit = 10 # int |  (optional) (default to 10)
    offset = 0 # int |  (optional) (default to 0)
    verify_status = 'verify_status_example' # str |  (optional)

    try:
        # Get Verified List Model Versioning By Api Key
        api_response = api_instance.api_key_model_id_versioning_list_get(id, x_api_key=x_api_key, limit=limit, offset=offset, verify_status=verify_status)
        print("The response of ApiKeyModelVersioningApi->api_key_model_id_versioning_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVersioningApi->api_key_model_id_versioning_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **x_api_key** | **str**| api-key | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 0]
 **verify_status** | **str**|  | [optional] 

### Return type

[**ResponseGetListModelVersioningLiteResponse**](ResponseGetListModelVersioningLiteResponse.md)

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

# **api_key_model_id_versioning_put**
> ResponseSuccessResponse api_key_model_id_versioning_put(id, commit_hash, x_api_key=x_api_key)

Change Model Versioning By Commit Hash By Api Key

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_success_response import ResponseSuccessResponse
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
    api_instance = aioz_api_client.ApiKeyModelVersioningApi(api_client)
    id = 'id_example' # str | Model's id
    commit_hash = 'commit_hash_example' # str | 
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Change Model Versioning By Commit Hash By Api Key
        api_response = api_instance.api_key_model_id_versioning_put(id, commit_hash, x_api_key=x_api_key)
        print("The response of ApiKeyModelVersioningApi->api_key_model_id_versioning_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelVersioningApi->api_key_model_id_versioning_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **commit_hash** | **str**|  | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseSuccessResponse**](ResponseSuccessResponse.md)

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

