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
> ResponseWalletWithAddressResponse api_key_balance_get(x_api_key=x_api_key)

Get Api Key Balance

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_wallet_with_address_response import ResponseWalletWithAddressResponse
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
    api_instance = aioz_api_client.ApiKeyApi(api_client)
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Api Key Balance
        api_response = api_instance.api_key_balance_get(x_api_key=x_api_key)
        print("The response of ApiKeyApi->api_key_balance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_balance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseWalletWithAddressResponse**](ResponseWalletWithAddressResponse.md)

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

# **api_key_permission_get**
> ResponseGetApiKeyPermissionResponse api_key_permission_get(x_api_key=x_api_key)

Get Api Key Permission

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_get_api_key_permission_response import ResponseGetApiKeyPermissionResponse
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
    api_instance = aioz_api_client.ApiKeyApi(api_client)
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Api Key Permission
        api_response = api_instance.api_key_permission_get(x_api_key=x_api_key)
        print("The response of ApiKeyApi->api_key_permission_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_permission_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseGetApiKeyPermissionResponse**](ResponseGetApiKeyPermissionResponse.md)

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

# **api_key_statistics_post**
> ResponseGetTaskStatisticsResponse api_key_statistics_post(input, x_api_key=x_api_key)

Get Api Key Statistics

### Example


```python
import aioz_api_client
from aioz_api_client.models.request_get_api_key_statistics_by_model_id_request import RequestGetApiKeyStatisticsByModelIdRequest
from aioz_api_client.models.response_get_task_statistics_response import ResponseGetTaskStatisticsResponse
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
    api_instance = aioz_api_client.ApiKeyApi(api_client)
    input = aioz_api_client.RequestGetApiKeyStatisticsByModelIdRequest() # RequestGetApiKeyStatisticsByModelIdRequest | Get Api Key Statistics Request
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Api Key Statistics
        api_response = api_instance.api_key_statistics_post(input, x_api_key=x_api_key)
        print("The response of ApiKeyApi->api_key_statistics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_statistics_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**RequestGetApiKeyStatisticsByModelIdRequest**](RequestGetApiKeyStatisticsByModelIdRequest.md)| Get Api Key Statistics Request | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseGetTaskStatisticsResponse**](ResponseGetTaskStatisticsResponse.md)

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

# **api_key_task_histories_get**
> ResponseApiKeyHistoryListResponse api_key_task_histories_get(x_api_key=x_api_key, limit=limit, offset=offset)

Get Tasks Histories

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_api_key_history_list_response import ResponseApiKeyHistoryListResponse
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
    api_instance = aioz_api_client.ApiKeyApi(api_client)
    x_api_key = 'x_api_key_example' # str | api-key (optional)
    limit = 10 # int |  (optional) (default to 10)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Tasks Histories
        api_response = api_instance.api_key_task_histories_get(x_api_key=x_api_key, limit=limit, offset=offset)
        print("The response of ApiKeyApi->api_key_task_histories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_task_histories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| api-key | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ResponseApiKeyHistoryListResponse**](ResponseApiKeyHistoryListResponse.md)

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

# **api_key_task_id_cancel_delete**
> ResponseSuccessResponse api_key_task_id_cancel_delete(id, x_api_key=x_api_key)

Cancel Task By Api Key

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
    api_instance = aioz_api_client.ApiKeyApi(api_client)
    id = 'id_example' # str | Task's id
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Cancel Task By Api Key
        api_response = api_instance.api_key_task_id_cancel_delete(id, x_api_key=x_api_key)
        print("The response of ApiKeyApi->api_key_task_id_cancel_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_task_id_cancel_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task&#39;s id | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_task_id_result_get**
> ResponseGetTaskResultResponse api_key_task_id_result_get(id, x_api_key=x_api_key)

Get Task Result

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_get_task_result_response import ResponseGetTaskResultResponse
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
    api_instance = aioz_api_client.ApiKeyApi(api_client)
    id = 'id_example' # str | Task's id
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Task Result
        api_response = api_instance.api_key_task_id_result_get(id, x_api_key=x_api_key)
        print("The response of ApiKeyApi->api_key_task_id_result_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_task_id_result_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task&#39;s id | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseGetTaskResultResponse**](ResponseGetTaskResultResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_task_post**
> ResponseDistributeTaskResponse api_key_task_post(input, x_api_key=x_api_key)

Distribute Task (Api-Key)

### Example


```python
import aioz_api_client
from aioz_api_client.models.request_distribute_task_request import RequestDistributeTaskRequest
from aioz_api_client.models.response_distribute_task_response import ResponseDistributeTaskResponse
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
    api_instance = aioz_api_client.ApiKeyApi(api_client)
    input = aioz_api_client.RequestDistributeTaskRequest() # RequestDistributeTaskRequest | Distribute Task Request
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Distribute Task (Api-Key)
        api_response = api_instance.api_key_task_post(input, x_api_key=x_api_key)
        print("The response of ApiKeyApi->api_key_task_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_task_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**RequestDistributeTaskRequest**](RequestDistributeTaskRequest.md)| Distribute Task Request | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseDistributeTaskResponse**](ResponseDistributeTaskResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

