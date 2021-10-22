# slurm_client.SlurmApi

All URIs are relative to *http://localhost/slurm/v0.0.36*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurmctld_cancel_job**](SlurmApi.md#slurmctld_cancel_job) | **DELETE** /job/{job_id} | cancel or signal job
[**slurmctld_diag**](SlurmApi.md#slurmctld_diag) | **GET** /diag/ | get diagnostics
[**slurmctld_get_job**](SlurmApi.md#slurmctld_get_job) | **GET** /job/{job_id} | get job info
[**slurmctld_get_jobs**](SlurmApi.md#slurmctld_get_jobs) | **GET** /jobs/ | get list of jobs
[**slurmctld_get_node**](SlurmApi.md#slurmctld_get_node) | **GET** /node/{node_name} | get node info
[**slurmctld_get_nodes**](SlurmApi.md#slurmctld_get_nodes) | **GET** /nodes/ | get all node info
[**slurmctld_get_partition**](SlurmApi.md#slurmctld_get_partition) | **GET** /partition/{partition_name} | get partition info
[**slurmctld_get_partitions**](SlurmApi.md#slurmctld_get_partitions) | **GET** /partitions/ | get all partition info
[**slurmctld_ping**](SlurmApi.md#slurmctld_ping) | **GET** /ping/ | ping test
[**slurmctld_submit_job**](SlurmApi.md#slurmctld_submit_job) | **POST** /job/submit | submit new job
[**slurmctld_update_job**](SlurmApi.md#slurmctld_update_job) | **POST** /job/{job_id} | update job


# **slurmctld_cancel_job**
> slurmctld_cancel_job(job_id, signal=signal)

cancel or signal job

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
job_id = 56 # int | Slurm Job ID
signal = slurm_client.V0036Signal() # V0036Signal | signal to send to job (optional)

try:
    # cancel or signal job
    api_instance.slurmctld_cancel_job(job_id, signal=signal)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_cancel_job: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
job_id = 56 # int | Slurm Job ID
signal = slurm_client.V0036Signal() # V0036Signal | signal to send to job (optional)

try:
    # cancel or signal job
    api_instance.slurmctld_cancel_job(job_id, signal=signal)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_cancel_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID | 
 **signal** | [**V0036Signal**](.md)| signal to send to job | [optional] 

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
**200** | job cancelled or sent signal |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_diag**
> V0036Diag slurmctld_diag()

get diagnostics

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # get diagnostics
    api_response = api_instance.slurmctld_diag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_diag: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # get diagnostics
    api_response = api_instance.slurmctld_diag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_diag: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036Diag**](V0036Diag.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_job**
> V0036JobsResponse slurmctld_get_job(job_id)

get job info

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
job_id = 56 # int | Slurm Job ID

try:
    # get job info
    api_response = api_instance.slurmctld_get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_job: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
job_id = 56 # int | Slurm Job ID

try:
    # get job info
    api_response = api_instance.slurmctld_get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID | 

### Return type

[**V0036JobsResponse**](V0036JobsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_jobs**
> V0036JobsResponse slurmctld_get_jobs()

get list of jobs

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # get list of jobs
    api_response = api_instance.slurmctld_get_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_jobs: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # get list of jobs
    api_response = api_instance.slurmctld_get_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036JobsResponse**](V0036JobsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_node**
> V0036NodesResponse slurmctld_get_node(node_name)

get node info

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
node_name = 'node_name_example' # str | Slurm Node Name

try:
    # get node info
    api_response = api_instance.slurmctld_get_node(node_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_node: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
node_name = 'node_name_example' # str | Slurm Node Name

try:
    # get node info
    api_response = api_instance.slurmctld_get_node(node_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name | 

### Return type

[**V0036NodesResponse**](V0036NodesResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_nodes**
> V0036NodesResponse slurmctld_get_nodes()

get all node info

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # get all node info
    api_response = api_instance.slurmctld_get_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_nodes: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # get all node info
    api_response = api_instance.slurmctld_get_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_nodes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036NodesResponse**](V0036NodesResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | no nodes in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_partition**
> V0036PartitionsResponse slurmctld_get_partition(partition_name)

get partition info

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
partition_name = 'partition_name_example' # str | Slurm Partition Name

try:
    # get partition info
    api_response = api_instance.slurmctld_get_partition(partition_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_partition: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
partition_name = 'partition_name_example' # str | Slurm Partition Name

try:
    # get partition info
    api_response = api_instance.slurmctld_get_partition(partition_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Slurm Partition Name | 

### Return type

[**V0036PartitionsResponse**](V0036PartitionsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_partitions**
> V0036PartitionsResponse slurmctld_get_partitions()

get all partition info

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # get all partition info
    api_response = api_instance.slurmctld_get_partitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_partitions: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # get all partition info
    api_response = api_instance.slurmctld_get_partitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_get_partitions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036PartitionsResponse**](V0036PartitionsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_ping**
> V0036Pings slurmctld_ping()

ping test

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # ping test
    api_response = api_instance.slurmctld_ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_ping: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))

try:
    # ping test
    api_response = api_instance.slurmctld_ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036Pings**](V0036Pings.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_submit_job**
> V0036JobSubmissionResponse slurmctld_submit_job(v0036_job_submission)

submit new job

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
v0036_job_submission = slurm_client.V0036JobSubmission() # V0036JobSubmission | submit new job

try:
    # submit new job
    api_response = api_instance.slurmctld_submit_job(v0036_job_submission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_submit_job: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
v0036_job_submission = slurm_client.V0036JobSubmission() # V0036JobSubmission | submit new job

try:
    # submit new job
    api_response = api_instance.slurmctld_submit_job(v0036_job_submission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_submit_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0036_job_submission** | [**V0036JobSubmission**](V0036JobSubmission.md)| submit new job | 

### Return type

[**V0036JobSubmissionResponse**](V0036JobSubmissionResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submitted |  -  |
**0** | job rejected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_update_job**
> slurmctld_update_job(job_id, v0036_job_properties)

update job

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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
job_id = 56 # int | Slurm Job ID
v0036_job_properties = slurm_client.V0036JobProperties() # V0036JobProperties | update job

try:
    # update job
    api_instance.slurmctld_update_job(job_id, v0036_job_properties)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_update_job: %s\n" % e)
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
api_instance = slurm_client.SlurmApi(slurm_client.ApiClient(configuration))
job_id = 56 # int | Slurm Job ID
v0036_job_properties = slurm_client.V0036JobProperties() # V0036JobProperties | update job

try:
    # update job
    api_instance.slurmctld_update_job(job_id, v0036_job_properties)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmctld_update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID | 
 **v0036_job_properties** | [**V0036JobProperties**](V0036JobProperties.md)| update job | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job information |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

