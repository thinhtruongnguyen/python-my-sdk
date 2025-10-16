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
> ResponseApiKeyInfoResponse api_key_model_id_info_get(id, x_api_key=x_api_key)

Get Api Key Model Info

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_api_key_info_response import ResponseApiKeyInfoResponse
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
    api_instance = aioz_api_client.ApiKeyModelApi(api_client)
    id = 'id_example' # str | Model's id
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Api Key Model Info
        api_response = api_instance.api_key_model_id_info_get(id, x_api_key=x_api_key)
        print("The response of ApiKeyModelApi->api_key_model_id_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelApi->api_key_model_id_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseApiKeyInfoResponse**](ResponseApiKeyInfoResponse.md)

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

# **api_key_model_id_serving_get**
> ResponseCheckModelIsServingResponse api_key_model_id_serving_get(id, x_api_key=x_api_key)

Check Model Is Serving

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_check_model_is_serving_response import ResponseCheckModelIsServingResponse
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
    api_instance = aioz_api_client.ApiKeyModelApi(api_client)
    id = 'id_example' # str | Model's id
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Check Model Is Serving
        api_response = api_instance.api_key_model_id_serving_get(id, x_api_key=x_api_key)
        print("The response of ApiKeyModelApi->api_key_model_id_serving_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelApi->api_key_model_id_serving_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseCheckModelIsServingResponse**](ResponseCheckModelIsServingResponse.md)

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

# **api_key_model_id_statistics_post**
> ResponseGetTaskStatisticsResponse api_key_model_id_statistics_post(id, input, x_api_key=x_api_key)

Get Model Statistics

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
    api_instance = aioz_api_client.ApiKeyModelApi(api_client)
    id = 'id_example' # str | Model's id
    input = aioz_api_client.RequestGetApiKeyStatisticsByModelIdRequest() # RequestGetApiKeyStatisticsByModelIdRequest | Get Api Key Statistics By Model Id Request
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get Model Statistics
        api_response = api_instance.api_key_model_id_statistics_post(id, input, x_api_key=x_api_key)
        print("The response of ApiKeyModelApi->api_key_model_id_statistics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelApi->api_key_model_id_statistics_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **input** | [**RequestGetApiKeyStatisticsByModelIdRequest**](RequestGetApiKeyStatisticsByModelIdRequest.md)| Get Api Key Statistics By Model Id Request | 
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

# **api_key_model_id_task_cost_get**
> ResponseEstimateCostResponse api_key_model_id_task_cost_get(id, x_api_key=x_api_key)

Get cost to compute task by model api key

### Example


```python
import aioz_api_client
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
    api_instance = aioz_api_client.ApiKeyModelApi(api_client)
    id = 'id_example' # str | Model's id
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get cost to compute task by model api key
        api_response = api_instance.api_key_model_id_task_cost_get(id, x_api_key=x_api_key)
        print("The response of ApiKeyModelApi->api_key_model_id_task_cost_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelApi->api_key_model_id_task_cost_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model&#39;s id | 
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseEstimateCostResponse**](ResponseEstimateCostResponse.md)

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

# **api_key_model_verify_support_platforms_get**
> ResponseGetListPlatformSupportResponse api_key_model_verify_support_platforms_get(x_api_key=x_api_key)

Get List Platforms Support By Api Key

### Example


```python
import aioz_api_client
from aioz_api_client.models.response_get_list_platform_support_response import ResponseGetListPlatformSupportResponse
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
    api_instance = aioz_api_client.ApiKeyModelApi(api_client)
    x_api_key = 'x_api_key_example' # str | api-key (optional)

    try:
        # Get List Platforms Support By Api Key
        api_response = api_instance.api_key_model_verify_support_platforms_get(x_api_key=x_api_key)
        print("The response of ApiKeyModelApi->api_key_model_verify_support_platforms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyModelApi->api_key_model_verify_support_platforms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| api-key | [optional] 

### Return type

[**ResponseGetListPlatformSupportResponse**](ResponseGetListPlatformSupportResponse.md)

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

