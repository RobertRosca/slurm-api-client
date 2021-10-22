# slurmdb_client.SlurmApi

All URIs are relative to *http://localhost/slurmdb/v0.0.36*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurmdbd_add_clusters**](SlurmApi.md#slurmdbd_add_clusters) | **POST** /clusters/ | Add clusters
[**slurmdbd_add_wckeys**](SlurmApi.md#slurmdbd_add_wckeys) | **POST** /wckeys/ | Add wckeys
[**slurmdbd_delete_account**](SlurmApi.md#slurmdbd_delete_account) | **DELETE** /account/{account_name} | Delete account
[**slurmdbd_delete_association**](SlurmApi.md#slurmdbd_delete_association) | **DELETE** /association/ | Delete association
[**slurmdbd_delete_cluster**](SlurmApi.md#slurmdbd_delete_cluster) | **DELETE** /cluster/{cluster_name} | Delete cluster
[**slurmdbd_delete_qos**](SlurmApi.md#slurmdbd_delete_qos) | **DELETE** /qos/{qos_name} | Delete QOS
[**slurmdbd_delete_user**](SlurmApi.md#slurmdbd_delete_user) | **DELETE** /user/{user_name} | Delete user
[**slurmdbd_delete_wckey**](SlurmApi.md#slurmdbd_delete_wckey) | **DELETE** /wckey/{wckey} | Delete wckey
[**slurmdbd_diag**](SlurmApi.md#slurmdbd_diag) | **GET** /diag/ | Get slurmdb diagnostics
[**slurmdbd_get_account**](SlurmApi.md#slurmdbd_get_account) | **GET** /account/{account_name} | Get account info
[**slurmdbd_get_accounts**](SlurmApi.md#slurmdbd_get_accounts) | **GET** /accounts/ | Get account list
[**slurmdbd_get_association**](SlurmApi.md#slurmdbd_get_association) | **GET** /association/ | Get association info
[**slurmdbd_get_associations**](SlurmApi.md#slurmdbd_get_associations) | **GET** /associations/ | Get association list
[**slurmdbd_get_cluster**](SlurmApi.md#slurmdbd_get_cluster) | **GET** /cluster/{cluster_name} | Get cluster info
[**slurmdbd_get_clusters**](SlurmApi.md#slurmdbd_get_clusters) | **GET** /clusters/ | Get cluster list
[**slurmdbd_get_db_config**](SlurmApi.md#slurmdbd_get_db_config) | **GET** /config | Dump all configuration information
[**slurmdbd_get_job**](SlurmApi.md#slurmdbd_get_job) | **GET** /job/{job_id} | Get job info
[**slurmdbd_get_jobs**](SlurmApi.md#slurmdbd_get_jobs) | **GET** /jobs/ | Get job list
[**slurmdbd_get_qos**](SlurmApi.md#slurmdbd_get_qos) | **GET** /qos/ | Get QOS list
[**slurmdbd_get_single_qos**](SlurmApi.md#slurmdbd_get_single_qos) | **GET** /qos/{qos_name} | Get QOS info
[**slurmdbd_get_tres**](SlurmApi.md#slurmdbd_get_tres) | **GET** /tres/ | Get TRES info
[**slurmdbd_get_user**](SlurmApi.md#slurmdbd_get_user) | **GET** /user/{user_name} | Get user info
[**slurmdbd_get_users**](SlurmApi.md#slurmdbd_get_users) | **GET** /users/ | Get user list
[**slurmdbd_get_wckey**](SlurmApi.md#slurmdbd_get_wckey) | **GET** /wckey/{wckey} | Get wckey info
[**slurmdbd_get_wckeys**](SlurmApi.md#slurmdbd_get_wckeys) | **GET** /wckeys/ | Get wckey list
[**slurmdbd_set_db_config**](SlurmApi.md#slurmdbd_set_db_config) | **POST** /config | Load all configuration information
[**slurmdbd_update_account**](SlurmApi.md#slurmdbd_update_account) | **POST** /accounts/ | Update accounts
[**slurmdbd_update_tres**](SlurmApi.md#slurmdbd_update_tres) | **POST** /tres/ | Set TRES info
[**slurmdbd_update_users**](SlurmApi.md#slurmdbd_update_users) | **POST** /users/ | Update user


# **slurmdbd_add_clusters**
> Dbv0036ResponseClusterAdd slurmdbd_add_clusters()

Add clusters

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Add clusters
    api_response = api_instance.slurmdbd_add_clusters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_add_clusters: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Add clusters
    api_response = api_instance.slurmdbd_add_clusters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_add_clusters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ResponseClusterAdd**](Dbv0036ResponseClusterAdd.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Unable to add cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_add_wckeys**
> Dbv0036ResponseWckeyAdd slurmdbd_add_wckeys()

Add wckeys

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Add wckeys
    api_response = api_instance.slurmdbd_add_wckeys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_add_wckeys: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Add wckeys
    api_response = api_instance.slurmdbd_add_wckeys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_add_wckeys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ResponseWckeyAdd**](Dbv0036ResponseWckeyAdd.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | Unable to add wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_account**
> Dbv0036ResponseAccountDelete slurmdbd_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
account_name = 'account_name_example' # str | Slurm Account Name

try:
    # Delete account
    api_response = api_instance.slurmdbd_delete_account(account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_account: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
account_name = 'account_name_example' # str | Slurm Account Name

try:
    # Delete account
    api_response = api_instance.slurmdbd_delete_account(account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name | 

### Return type

[**Dbv0036ResponseAccountDelete**](Dbv0036ResponseAccountDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete account |  -  |
**0** | Unable to delete account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_association**
> Dbv0036ResponseAssociationDelete slurmdbd_delete_association(account, user, cluster=cluster, partition=partition)

Delete association

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
account = 'account_example' # str | Account name
user = 'user_example' # str | User name
cluster = 'cluster_example' # str | Cluster name (optional)
partition = 'partition_example' # str | Partition Name (optional)

try:
    # Delete association
    api_response = api_instance.slurmdbd_delete_association(account, user, cluster=cluster, partition=partition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_association: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
account = 'account_example' # str | Account name
user = 'user_example' # str | User name
cluster = 'cluster_example' # str | Cluster name (optional)
partition = 'partition_example' # str | Partition Name (optional)

try:
    # Delete association
    api_response = api_instance.slurmdbd_delete_association(account, user, cluster=cluster, partition=partition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Account name | 
 **user** | **str**| User name | 
 **cluster** | **str**| Cluster name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0036ResponseAssociationDelete**](Dbv0036ResponseAssociationDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete associations |  -  |
**0** | Association not found or unable to delete association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_cluster**
> Dbv0036ResponseClusterDelete slurmdbd_delete_cluster(cluster_name)

Delete cluster

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
cluster_name = 'cluster_name_example' # str | Slurm cluster name

try:
    # Delete cluster
    api_response = api_instance.slurmdbd_delete_cluster(cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_cluster: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
cluster_name = 'cluster_name_example' # str | Slurm cluster name

try:
    # Delete cluster
    api_response = api_instance.slurmdbd_delete_cluster(cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name | 

### Return type

[**Dbv0036ResponseClusterDelete**](Dbv0036ResponseClusterDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete cluster |  -  |
**0** | Cluster not found or unable to delete cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_qos**
> Dbv0036ResponseQosDelete slurmdbd_delete_qos(qos_name)

Delete QOS

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
qos_name = 'qos_name_example' # str | Slurm QOS Name

try:
    # Delete QOS
    api_response = api_instance.slurmdbd_delete_qos(qos_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_qos: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
qos_name = 'qos_name_example' # str | Slurm QOS Name

try:
    # Delete QOS
    api_response = api_instance.slurmdbd_delete_qos(qos_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name | 

### Return type

[**Dbv0036ResponseQosDelete**](Dbv0036ResponseQosDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete qos |  -  |
**0** | Unable to delete QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_user**
> Dbv0036ResponseUserDelete slurmdbd_delete_user(user_name)

Delete user

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
user_name = 'user_name_example' # str | Slurm User Name

try:
    # Delete user
    api_response = api_instance.slurmdbd_delete_user(user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_user: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
user_name = 'user_name_example' # str | Slurm User Name

try:
    # Delete user
    api_response = api_instance.slurmdbd_delete_user(user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name | 

### Return type

[**Dbv0036ResponseUserDelete**](Dbv0036ResponseUserDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete user |  -  |
**0** | User not found or unable to delete user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_wckey**
> Dbv0036ResponseWckeyDelete slurmdbd_delete_wckey(wckey)

Delete wckey

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
wckey = 'wckey_example' # str | Slurm wckey name

try:
    # Delete wckey
    api_response = api_instance.slurmdbd_delete_wckey(wckey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_wckey: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
wckey = 'wckey_example' # str | Slurm wckey name

try:
    # Delete wckey
    api_response = api_instance.slurmdbd_delete_wckey(wckey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_delete_wckey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name | 

### Return type

[**Dbv0036ResponseWckeyDelete**](Dbv0036ResponseWckeyDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete wckey |  -  |
**0** | wckey not found or unable to delete wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_diag**
> Dbv0036Diag slurmdbd_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get slurmdb diagnostics
    api_response = api_instance.slurmdbd_diag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_diag: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get slurmdb diagnostics
    api_response = api_instance.slurmdbd_diag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_diag: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036Diag**](Dbv0036Diag.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Unable to query diagnostics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_account**
> Dbv0036AccountInfo slurmdbd_get_account(account_name)

Get account info

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
account_name = 'account_name_example' # str | Slurm Account Name

try:
    # Get account info
    api_response = api_instance.slurmdbd_get_account(account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_account: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
account_name = 'account_name_example' # str | Slurm Account Name

try:
    # Get account info
    api_response = api_instance.slurmdbd_get_account(account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name | 

### Return type

[**Dbv0036AccountInfo**](Dbv0036AccountInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_accounts**
> Dbv0036AccountInfo slurmdbd_get_accounts()

Get account list

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get account list
    api_response = api_instance.slurmdbd_get_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_accounts: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get account list
    api_response = api_instance.slurmdbd_get_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036AccountInfo**](Dbv0036AccountInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_association**
> Dbv0036AssociationsInfo slurmdbd_get_association(cluster=cluster, account=account, user=user, partition=partition)

Get association info

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
cluster = 'cluster_example' # str | Cluster name (optional)
account = 'account_example' # str | Account name (optional)
user = 'user_example' # str | User name (optional)
partition = 'partition_example' # str | Partition Name (optional)

try:
    # Get association info
    api_response = api_instance.slurmdbd_get_association(cluster=cluster, account=account, user=user, partition=partition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_association: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
cluster = 'cluster_example' # str | Cluster name (optional)
account = 'account_example' # str | Account name (optional)
user = 'user_example' # str | User name (optional)
partition = 'partition_example' # str | Partition Name (optional)

try:
    # Get association info
    api_response = api_instance.slurmdbd_get_association(cluster=cluster, account=account, user=user, partition=partition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0036AssociationsInfo**](Dbv0036AssociationsInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_associations**
> Dbv0036AssociationsInfo slurmdbd_get_associations()

Get association list

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get association list
    api_response = api_instance.slurmdbd_get_associations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_associations: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get association list
    api_response = api_instance.slurmdbd_get_associations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_associations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036AssociationsInfo**](Dbv0036AssociationsInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_cluster**
> Dbv0036ClusterInfo slurmdbd_get_cluster(cluster_name)

Get cluster info

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
cluster_name = 'cluster_name_example' # str | Slurm cluster name

try:
    # Get cluster info
    api_response = api_instance.slurmdbd_get_cluster(cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_cluster: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
cluster_name = 'cluster_name_example' # str | Slurm cluster name

try:
    # Get cluster info
    api_response = api_instance.slurmdbd_get_cluster(cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name | 

### Return type

[**Dbv0036ClusterInfo**](Dbv0036ClusterInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_clusters**
> Dbv0036ClusterInfo slurmdbd_get_clusters()

Get cluster list

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get cluster list
    api_response = api_instance.slurmdbd_get_clusters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_clusters: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get cluster list
    api_response = api_instance.slurmdbd_get_clusters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_clusters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ClusterInfo**](Dbv0036ClusterInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_db_config**
> Dbv0036ConfigInfo slurmdbd_get_db_config()

Dump all configuration information

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Dump all configuration information
    api_response = api_instance.slurmdbd_get_db_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_db_config: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Dump all configuration information
    api_response = api_instance.slurmdbd_get_db_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_db_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ConfigInfo**](Dbv0036ConfigInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | Unable to dump config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_job**
> Dbv0036JobInfo slurmdbd_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
job_id = 56 # int | Slurm Job ID

try:
    # Get job info
    api_response = api_instance.slurmdbd_get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_job: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
job_id = 56 # int | Slurm Job ID

try:
    # Get job info
    api_response = api_instance.slurmdbd_get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID | 

### Return type

[**Dbv0036JobInfo**](Dbv0036JobInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Unable to find job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_jobs**
> Dbv0036JobInfo slurmdbd_get_jobs(submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)

Get job list

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
submit_time = 'submit_time_example' # str | Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
start_time = 'start_time_example' # str | Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
end_time = 'end_time_example' # str | Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
account = 'account_example' # str | Comma delimited list of accounts to match (optional)
association = 'association_example' # str | Comma delimited list of associations to match (optional)
cluster = 'cluster_example' # str | Comma delimited list of cluster to match (optional)
constraints = 'constraints_example' # str | Comma delimited list of constraints to match (optional)
cpus_max = 'cpus_max_example' # str | Number of CPUs high range (optional)
cpus_min = 'cpus_min_example' # str | Number of CPUs low range (optional)
skip_steps = True # bool | Report job step information (optional)
disable_wait_for_result = True # bool | Disable waiting for result from slurmdbd (optional)
exit_code = 'exit_code_example' # str | Exit code of job (optional)
format = 'format_example' # str | Comma delimited list of formats to match (optional)
group = 'group_example' # str | Comma delimited list of groups to match (optional)
job_name = 'job_name_example' # str | Comma delimited list of job names to match (optional)
nodes_max = 'nodes_max_example' # str | Number of nodes high range (optional)
nodes_min = 'nodes_min_example' # str | Number of nodes low range (optional)
partition = 'partition_example' # str | Comma delimited list of partitions to match (optional)
qos = 'qos_example' # str | Comma delimited list of QOS to match (optional)
reason = 'reason_example' # str | Comma delimited list of job reasons to match (optional)
reservation = 'reservation_example' # str | Comma delimited list of reservations to match (optional)
state = 'state_example' # str | Comma delimited list of states to match (optional)
step = 'step_example' # str | Comma delimited list of job steps to match (optional)
node = 'node_example' # str | Comma delimited list of used nodes to match (optional)
wckey = 'wckey_example' # str | Comma delimited list of wckeys to match (optional)

try:
    # Get job list
    api_response = api_instance.slurmdbd_get_jobs(submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_jobs: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
submit_time = 'submit_time_example' # str | Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
start_time = 'start_time_example' # str | Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
end_time = 'end_time_example' # str | Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
account = 'account_example' # str | Comma delimited list of accounts to match (optional)
association = 'association_example' # str | Comma delimited list of associations to match (optional)
cluster = 'cluster_example' # str | Comma delimited list of cluster to match (optional)
constraints = 'constraints_example' # str | Comma delimited list of constraints to match (optional)
cpus_max = 'cpus_max_example' # str | Number of CPUs high range (optional)
cpus_min = 'cpus_min_example' # str | Number of CPUs low range (optional)
skip_steps = True # bool | Report job step information (optional)
disable_wait_for_result = True # bool | Disable waiting for result from slurmdbd (optional)
exit_code = 'exit_code_example' # str | Exit code of job (optional)
format = 'format_example' # str | Comma delimited list of formats to match (optional)
group = 'group_example' # str | Comma delimited list of groups to match (optional)
job_name = 'job_name_example' # str | Comma delimited list of job names to match (optional)
nodes_max = 'nodes_max_example' # str | Number of nodes high range (optional)
nodes_min = 'nodes_min_example' # str | Number of nodes low range (optional)
partition = 'partition_example' # str | Comma delimited list of partitions to match (optional)
qos = 'qos_example' # str | Comma delimited list of QOS to match (optional)
reason = 'reason_example' # str | Comma delimited list of job reasons to match (optional)
reservation = 'reservation_example' # str | Comma delimited list of reservations to match (optional)
state = 'state_example' # str | Comma delimited list of states to match (optional)
step = 'step_example' # str | Comma delimited list of job steps to match (optional)
node = 'node_example' # str | Comma delimited list of used nodes to match (optional)
wckey = 'wckey_example' # str | Comma delimited list of wckeys to match (optional)

try:
    # Get job list
    api_response = api_instance.slurmdbd_get_jobs(submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_time** | **str**| Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **start_time** | **str**| Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **end_time** | **str**| Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **account** | **str**| Comma delimited list of accounts to match | [optional] 
 **association** | **str**| Comma delimited list of associations to match | [optional] 
 **cluster** | **str**| Comma delimited list of cluster to match | [optional] 
 **constraints** | **str**| Comma delimited list of constraints to match | [optional] 
 **cpus_max** | **str**| Number of CPUs high range | [optional] 
 **cpus_min** | **str**| Number of CPUs low range | [optional] 
 **skip_steps** | **bool**| Report job step information | [optional] 
 **disable_wait_for_result** | **bool**| Disable waiting for result from slurmdbd | [optional] 
 **exit_code** | **str**| Exit code of job | [optional] 
 **format** | **str**| Comma delimited list of formats to match | [optional] 
 **group** | **str**| Comma delimited list of groups to match | [optional] 
 **job_name** | **str**| Comma delimited list of job names to match | [optional] 
 **nodes_max** | **str**| Number of nodes high range | [optional] 
 **nodes_min** | **str**| Number of nodes low range | [optional] 
 **partition** | **str**| Comma delimited list of partitions to match | [optional] 
 **qos** | **str**| Comma delimited list of QOS to match | [optional] 
 **reason** | **str**| Comma delimited list of job reasons to match | [optional] 
 **reservation** | **str**| Comma delimited list of reservations to match | [optional] 
 **state** | **str**| Comma delimited list of states to match | [optional] 
 **step** | **str**| Comma delimited list of job steps to match | [optional] 
 **node** | **str**| Comma delimited list of used nodes to match | [optional] 
 **wckey** | **str**| Comma delimited list of wckeys to match | [optional] 

### Return type

[**Dbv0036JobInfo**](Dbv0036JobInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | Unable to query jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_qos**
> Dbv0036QosInfo slurmdbd_get_qos()

Get QOS list

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get QOS list
    api_response = api_instance.slurmdbd_get_qos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_qos: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get QOS list
    api_response = api_instance.slurmdbd_get_qos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_qos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036QosInfo**](Dbv0036QosInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS&#39; |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_single_qos**
> Dbv0036QosInfo slurmdbd_get_single_qos(qos_name)

Get QOS info

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
qos_name = 'qos_name_example' # str | Slurm QOS Name

try:
    # Get QOS info
    api_response = api_instance.slurmdbd_get_single_qos(qos_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_single_qos: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
qos_name = 'qos_name_example' # str | Slurm QOS Name

try:
    # Get QOS info
    api_response = api_instance.slurmdbd_get_single_qos(qos_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_single_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name | 

### Return type

[**Dbv0036QosInfo**](Dbv0036QosInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_tres**
> Dbv0036TresInfo slurmdbd_get_tres()

Get TRES info

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get TRES info
    api_response = api_instance.slurmdbd_get_tres()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_tres: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get TRES info
    api_response = api_instance.slurmdbd_get_tres()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_tres: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036TresInfo**](Dbv0036TresInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to retrieve TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_user**
> Dbv0036UserInfo slurmdbd_get_user(user_name)

Get user info

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
user_name = 'user_name_example' # str | Slurm User Name

try:
    # Get user info
    api_response = api_instance.slurmdbd_get_user(user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_user: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
user_name = 'user_name_example' # str | Slurm User Name

try:
    # Get user info
    api_response = api_instance.slurmdbd_get_user(user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name | 

### Return type

[**Dbv0036UserInfo**](Dbv0036UserInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_users**
> Dbv0036UserInfo slurmdbd_get_users()

Get user list

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get user list
    api_response = api_instance.slurmdbd_get_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_users: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get user list
    api_response = api_instance.slurmdbd_get_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036UserInfo**](Dbv0036UserInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_wckey**
> Dbv0036WckeyInfo slurmdbd_get_wckey(wckey)

Get wckey info

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
wckey = 'wckey_example' # str | Slurm wckey name

try:
    # Get wckey info
    api_response = api_instance.slurmdbd_get_wckey(wckey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_wckey: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))
wckey = 'wckey_example' # str | Slurm wckey name

try:
    # Get wckey info
    api_response = api_instance.slurmdbd_get_wckey(wckey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_wckey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name | 

### Return type

[**Dbv0036WckeyInfo**](Dbv0036WckeyInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckey |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_wckeys**
> Dbv0036WckeyInfo slurmdbd_get_wckeys()

Get wckey list

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get wckey list
    api_response = api_instance.slurmdbd_get_wckeys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_wckeys: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Get wckey list
    api_response = api_instance.slurmdbd_get_wckeys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_get_wckeys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036WckeyInfo**](Dbv0036WckeyInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_set_db_config**
> Dbv0036ConfigResponse slurmdbd_set_db_config()

Load all configuration information

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Load all configuration information
    api_response = api_instance.slurmdbd_set_db_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_set_db_config: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Load all configuration information
    api_response = api_instance.slurmdbd_set_db_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_set_db_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ConfigResponse**](Dbv0036ConfigResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Load config |  -  |
**0** | Unable to set config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_account**
> Dbv0036AccountResponse slurmdbd_update_account()

Update accounts

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Update accounts
    api_response = api_instance.slurmdbd_update_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_update_account: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Update accounts
    api_response = api_instance.slurmdbd_update_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_update_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036AccountResponse**](Dbv0036AccountResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add/update list of accounts |  -  |
**0** | Unable to add or update accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_tres**
> Dbv0036ResponseTres slurmdbd_update_tres()

Set TRES info

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Set TRES info
    api_response = api_instance.slurmdbd_update_tres()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_update_tres: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Set TRES info
    api_response = api_instance.slurmdbd_update_tres()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_update_tres: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ResponseTres**](Dbv0036ResponseTres.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to update TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_users**
> Dbv0036ResponseUserUpdate slurmdbd_update_users()

Update user

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Update user
    api_response = api_instance.slurmdbd_update_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_update_users: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import slurmdb_client
from slurmdb_client.rest import ApiException
from pprint import pprint
configuration = slurmdb_client.Configuration()
# Configure API key authorization: token
configuration.api_key['X-SLURM-USER-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'
configuration = slurmdb_client.Configuration()
# Configure API key authorization: user
configuration.api_key['X-SLURM-USER-NAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Defining host is optional and default to http://localhost/slurmdb/v0.0.36
configuration.host = "http://localhost/slurmdb/v0.0.36"
# Create an instance of the API class
api_instance = slurmdb_client.SlurmApi(slurmdb_client.ApiClient(configuration))

try:
    # Update user
    api_response = api_instance.slurmdbd_update_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlurmApi->slurmdbd_update_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ResponseUserUpdate**](Dbv0036ResponseUserUpdate.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update users |  -  |
**0** | User not found or not able to update user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

