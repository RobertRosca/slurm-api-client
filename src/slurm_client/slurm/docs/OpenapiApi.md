# slurm_client.OpenapiApi

All URIs are relative to *http://localhost/slurm/v0.0.36*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openapi_get**](OpenapiApi.md#openapi_get) | **GET** /openapi | Retrieve OpenAPI Specification
[**openapi_json_get**](OpenapiApi.md#openapi_json_get) | **GET** /openapi.json | Retrieve OpenAPI Specification
[**openapi_v3_get**](OpenapiApi.md#openapi_v3_get) | **GET** /openapi/v3 | Retrieve OpenAPI Specification
[**openapi_yaml_get**](OpenapiApi.md#openapi_yaml_get) | **GET** /openapi.yaml | Retrieve OpenAPI Specification


# **openapi_get**
> openapi_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurm_client
from slurm_client.rest import ApiException
from pprint import pprint
configuration = slurm_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurm_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurm/v0.0.36
configuration.host = "http://localhost/slurm/v0.0.36"
# Create an instance of the API class
api_instance = slurm_client.OpenapiApi(slurm_client.ApiClient(configuration))

try:
    # Retrieve OpenAPI Specification
    api_instance.openapi_get()
except ApiException as e:
    print("Exception when calling OpenapiApi->openapi_get: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurm_client
from slurm_client.rest import ApiException
from pprint import pprint
configuration = slurm_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurm_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurm/v0.0.36
configuration.host = "http://localhost/slurm/v0.0.36"
# Create an instance of the API class
api_instance = slurm_client.OpenapiApi(slurm_client.ApiClient(configuration))

try:
    # Retrieve OpenAPI Specification
    api_instance.openapi_get()
except ApiException as e:
    print("Exception when calling OpenapiApi->openapi_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_json_get**
> openapi_json_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurm_client
from slurm_client.rest import ApiException
from pprint import pprint
configuration = slurm_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurm_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurm/v0.0.36
configuration.host = "http://localhost/slurm/v0.0.36"
# Create an instance of the API class
api_instance = slurm_client.OpenapiApi(slurm_client.ApiClient(configuration))

try:
    # Retrieve OpenAPI Specification
    api_instance.openapi_json_get()
except ApiException as e:
    print("Exception when calling OpenapiApi->openapi_json_get: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurm_client
from slurm_client.rest import ApiException
from pprint import pprint
configuration = slurm_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurm_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurm/v0.0.36
configuration.host = "http://localhost/slurm/v0.0.36"
# Create an instance of the API class
api_instance = slurm_client.OpenapiApi(slurm_client.ApiClient(configuration))

try:
    # Retrieve OpenAPI Specification
    api_instance.openapi_json_get()
except ApiException as e:
    print("Exception when calling OpenapiApi->openapi_json_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_v3_get**
> openapi_v3_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurm_client
from slurm_client.rest import ApiException
from pprint import pprint
configuration = slurm_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurm_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurm/v0.0.36
configuration.host = "http://localhost/slurm/v0.0.36"
# Create an instance of the API class
api_instance = slurm_client.OpenapiApi(slurm_client.ApiClient(configuration))

try:
    # Retrieve OpenAPI Specification
    api_instance.openapi_v3_get()
except ApiException as e:
    print("Exception when calling OpenapiApi->openapi_v3_get: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurm_client
from slurm_client.rest import ApiException
from pprint import pprint
configuration = slurm_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurm_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurm/v0.0.36
configuration.host = "http://localhost/slurm/v0.0.36"
# Create an instance of the API class
api_instance = slurm_client.OpenapiApi(slurm_client.ApiClient(configuration))

try:
    # Retrieve OpenAPI Specification
    api_instance.openapi_v3_get()
except ApiException as e:
    print("Exception when calling OpenapiApi->openapi_v3_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_yaml_get**
> openapi_yaml_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurm_client
from slurm_client.rest import ApiException
from pprint import pprint
configuration = slurm_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurm_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurm/v0.0.36
configuration.host = "http://localhost/slurm/v0.0.36"
# Create an instance of the API class
api_instance = slurm_client.OpenapiApi(slurm_client.ApiClient(configuration))

try:
    # Retrieve OpenAPI Specification
    api_instance.openapi_yaml_get()
except ApiException as e:
    print("Exception when calling OpenapiApi->openapi_yaml_get: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurm_client
from slurm_client.rest import ApiException
from pprint import pprint
configuration = slurm_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurm_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurm/v0.0.36
configuration.host = "http://localhost/slurm/v0.0.36"
# Create an instance of the API class
api_instance = slurm_client.OpenapiApi(slurm_client.ApiClient(configuration))

try:
    # Retrieve OpenAPI Specification
    api_instance.openapi_yaml_get()
except ApiException as e:
    print("Exception when calling OpenapiApi->openapi_yaml_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

