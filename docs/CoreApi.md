# ubiops.CoreApi

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_deployment_requests_batch_delete**](CoreApi.md#batch_deployment_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch-delete | Delete multiple batch deployment requests
[**batch_deployment_requests_batch_get**](CoreApi.md#batch_deployment_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch-collect | Retrieve multiple batch deployment request results
[**batch_deployment_requests_create**](CoreApi.md#batch_deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch | Create batch deployment requests
[**batch_deployment_requests_delete**](CoreApi.md#batch_deployment_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch/{request_id} | Delete batch deployment requests
[**batch_deployment_requests_get**](CoreApi.md#batch_deployment_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch/{request_id} | Get batch deployment request
[**batch_deployment_requests_list**](CoreApi.md#batch_deployment_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch | List batch deployment requests
[**batch_pipeline_requests_batch_delete**](CoreApi.md#batch_pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch-delete | Delete multiple batch pipeline requests
[**batch_pipeline_requests_batch_get**](CoreApi.md#batch_pipeline_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch-collect | Retrieve multiple batch pipeline request results
[**batch_pipeline_requests_create**](CoreApi.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch | Create batch pipeline requests
[**batch_pipeline_requests_delete**](CoreApi.md#batch_pipeline_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/request-batch/{pipeline_request_id} | Delete batch pipeline requests
[**batch_pipeline_requests_get**](CoreApi.md#batch_pipeline_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/request-batch/{pipeline_request_id} | Get batch pipeline request
[**batch_pipeline_requests_list**](CoreApi.md#batch_pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/request-batch | List batch pipeline requests
[**blobs_create**](CoreApi.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
[**blobs_delete**](CoreApi.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
[**blobs_get**](CoreApi.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
[**blobs_list**](CoreApi.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
[**deployment_audit_events_list**](CoreApi.md#deployment_audit_events_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/audit | List audit events for a deployment
[**deployment_environment_variables_copy**](CoreApi.md#deployment_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/copy-environment-variables | Copy deployment environment variable
[**deployment_environment_variables_create**](CoreApi.md#deployment_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/environment-variables | Create deployment environment variable
[**deployment_environment_variables_delete**](CoreApi.md#deployment_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Delete deployment environment variable
[**deployment_environment_variables_get**](CoreApi.md#deployment_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Get deployment environment variable
[**deployment_environment_variables_list**](CoreApi.md#deployment_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables | List deployment environment variables
[**deployment_environment_variables_update**](CoreApi.md#deployment_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Update deployment environment variable
[**deployment_requests_create**](CoreApi.md#deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request | Create deployment requests
[**deployments_create**](CoreApi.md#deployments_create) | **POST** /projects/{project_name}/deployments | Create a deployment
[**deployments_delete**](CoreApi.md#deployments_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name} | Delete a deployment
[**deployments_get**](CoreApi.md#deployments_get) | **GET** /projects/{project_name}/deployments/{deployment_name} | Get details of deployment
[**deployments_list**](CoreApi.md#deployments_list) | **GET** /projects/{project_name}/deployments | List deployments in project
[**deployments_update**](CoreApi.md#deployments_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name} | Update a deployment
[**metrics_get**](CoreApi.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
[**organization_usage_details_get**](CoreApi.md#organization_usage_details_get) | **GET** /organizations/{organization_name}/usage/details | Get resource usage details
[**organization_usage_get**](CoreApi.md#organization_usage_get) | **GET** /organizations/{organization_name}/usage | Get resource usage
[**organization_users_create**](CoreApi.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
[**organization_users_delete**](CoreApi.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
[**organization_users_get**](CoreApi.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
[**organization_users_list**](CoreApi.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
[**organization_users_update**](CoreApi.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
[**organizations_create**](CoreApi.md#organizations_create) | **POST** /organizations | Create organizations
[**organizations_get**](CoreApi.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
[**organizations_list**](CoreApi.md#organizations_list) | **GET** /organizations | List organizations
[**organizations_resource_usage**](CoreApi.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | List resource usage of an organization
[**organizations_update**](CoreApi.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
[**permissions_list**](CoreApi.md#permissions_list) | **GET** /permissions | List the available permissions
[**pipeline_audit_events_list**](CoreApi.md#pipeline_audit_events_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/audit | List audit events for a pipeline
[**pipeline_object_attachments_create**](CoreApi.md#pipeline_object_attachments_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/attachments | Create object attachments
[**pipeline_object_attachments_delete**](CoreApi.md#pipeline_object_attachments_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/{destination_name} | Delete attachment of a source and destination object
[**pipeline_object_attachments_get**](CoreApi.md#pipeline_object_attachments_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/{destination_name} | Get an attachment of a source and destination object
[**pipeline_object_attachments_list**](CoreApi.md#pipeline_object_attachments_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/attachments | List object attachments
[**pipeline_object_attachments_source_get**](CoreApi.md#pipeline_object_attachments_source_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/ | List the attachments of a source object
[**pipeline_object_environment_variables_list**](CoreApi.md#pipeline_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name}/environment-variables | List pipeline object environment variables
[**pipeline_objects_create**](CoreApi.md#pipeline_objects_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/objects | Add an object to a pipeline
[**pipeline_objects_delete**](CoreApi.md#pipeline_objects_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Delete object from pipeline
[**pipeline_objects_get**](CoreApi.md#pipeline_objects_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Get an object in a pipeline
[**pipeline_objects_list**](CoreApi.md#pipeline_objects_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects | List objects in a pipeline
[**pipeline_objects_update**](CoreApi.md#pipeline_objects_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Update an object in a pipeline
[**pipeline_requests_create**](CoreApi.md#pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request | Make a request to a pipeline
[**pipelines_create**](CoreApi.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
[**pipelines_delete**](CoreApi.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete pipeline
[**pipelines_get**](CoreApi.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get pipeline
[**pipelines_list**](CoreApi.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
[**pipelines_update**](CoreApi.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update pipeline
[**project_audit_events_list**](CoreApi.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
[**project_environment_variables_create**](CoreApi.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](CoreApi.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](CoreApi.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](CoreApi.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](CoreApi.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**project_usage_get**](CoreApi.md#project_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
[**projects_create**](CoreApi.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](CoreApi.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](CoreApi.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](CoreApi.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](CoreApi.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_resource_usage**](CoreApi.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
[**projects_update**](CoreApi.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
[**request_schedules_create**](CoreApi.md#request_schedules_create) | **POST** /projects/{project_name}/schedules | Create request schedules
[**request_schedules_delete**](CoreApi.md#request_schedules_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a request schedule
[**request_schedules_get**](CoreApi.md#request_schedules_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a request schedule
[**request_schedules_list**](CoreApi.md#request_schedules_list) | **GET** /projects/{project_name}/schedules | List request schedules
[**request_schedules_update**](CoreApi.md#request_schedules_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a request schedule
[**role_assignments_create**](CoreApi.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign a role to a user in a project
[**role_assignments_delete**](CoreApi.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete a role from a user with the given role assignment id
[**role_assignments_get**](CoreApi.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get details of a role assignment
[**role_assignments_per_user_list**](CoreApi.md#role_assignments_per_user_list) | **GET** /projects/{project_name}/users/{user_id}/role-assignments | List the roles assigned to a specific user in a project
[**roles_create**](CoreApi.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
[**roles_delete**](CoreApi.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
[**roles_get**](CoreApi.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
[**roles_list**](CoreApi.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
[**roles_update**](CoreApi.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
[**service_status**](CoreApi.md#service_status) | **GET** /status | Service status
[**service_users_create**](CoreApi.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
[**service_users_delete**](CoreApi.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
[**service_users_get**](CoreApi.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
[**service_users_list**](CoreApi.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
[**service_users_token**](CoreApi.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
[**service_users_update**](CoreApi.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
[**user_create**](CoreApi.md#user_create) | **POST** /user | Create a new user
[**user_delete**](CoreApi.md#user_delete) | **DELETE** /user | Delete user
[**version_environment_variables_copy**](CoreApi.md#version_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/copy-environment-variables | Copy version environment variable
[**version_environment_variables_create**](CoreApi.md#version_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | Create version environment variable
[**version_environment_variables_delete**](CoreApi.md#version_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Delete version environment variable
[**version_environment_variables_get**](CoreApi.md#version_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Get version environment variable
[**version_environment_variables_list**](CoreApi.md#version_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | List version environment variables
[**version_environment_variables_update**](CoreApi.md#version_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Update version environment variable
[**versions_create**](CoreApi.md#versions_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions | Create versions
[**versions_delete**](CoreApi.md#versions_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Delete version
[**versions_file_download**](CoreApi.md#versions_file_download) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/download | Download deployment files
[**versions_file_upload**](CoreApi.md#versions_file_upload) | **PUT** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/upload | Upload deployment files
[**versions_get**](CoreApi.md#versions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Get version
[**versions_list**](CoreApi.md#versions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions | List versions
[**versions_update**](CoreApi.md#versions_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Update version


# **batch_deployment_requests_batch_delete**
> object batch_deployment_requests_batch_delete(project_name, deployment_name, version, data)

Delete multiple batch deployment requests


### Description
Delete multiple batch deployment requests. If one of the given batch deployment requests does not exist, an error message is given and no request is deleted. A maximum of 250 deployment requests can be deleted with this method.

### Required Parameters 
A list of ids for the batch requests

#### Request Examples 
```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
data = None # object | 

# Delete multiple batch deployment requests
api_response = api_instance.batch_deployment_requests_batch_delete(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | **object**|  | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_deployment_requests_batch_get**
> list[BatchDeploymentRequestDetail] batch_deployment_requests_batch_get(project_name, deployment_name, version, data)

Retrieve multiple batch deployment request results


### Description
Retrieve multiple batch deployment requests. If one of the given batch deployment requests does not exist, an error message is given and no request is returned. A maximum of 250 deployment requests can be retrieved with this method. The deployment requests are NOT returned in the order they are given in.

### Required Parameters 
A list of ids for the batch requests

#### Request Examples 
```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Response Structure 
A list of dictionaries containing the details of the retrieved deployment requests with the following fields:
 - `id`: Unique identifier for the deployment request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the deployment request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated
 - `request_data`: A dictionary containing the data that was sent when the request was created
 - `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples 
```
[
  {
    "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-29T08:09:10.729+00:00",
    "time_last_updated": "2020-06-29T08:09:10.729+00:00",
    "request_data": {
      "input": 82.2
    },
    "result": null,
    "error_message": null
  },
  {
    "id": "85711124-54db-4794-b83d-24492247c6e1",
    "status": "pending",
    "success": false,
    "time_created": "2020-06-25T09:37:17.765+00:00",
    "time_last_updated": "2020-03-25T09:37:17.765+00:00",
    "request_data": {
      "input": 52.4
    },
    "result": null,
    "error_message": null
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
data = None # object | 

# Retrieve multiple batch deployment request results
api_response = api_instance.batch_deployment_requests_batch_get(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**list[BatchDeploymentRequestDetail]**](BatchDeploymentRequestDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_deployment_requests_create**
> list[BatchDeploymentRequestCreateResponse] batch_deployment_requests_create(project_name, deployment_name, version, data)

Create batch deployment requests


### Description
Request multiple predictions from a deployment. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the deployment request collect methods. It is only possible to make a request if a deployment file is uploaded for that version and the deployment build has succeeded (meaning that the version is in available state).
In case of a **blob** field, the uuid of a previously uploaded blob must be provided.

If one of the requests is faulty, all requests are denied. The maximum number of requests per bulk call is 250.

### Required Parameters 
In case of structured input deployment: A list of dictionaries, where each dictionary contains the input fields of the deployment as keys. It is also possible to send a single dictionary as input.
In case of plain input deployment: A list of strings. It is also possible to send a single string as input.

#### Request Examples 
```
[
  {
    "input-field-1": 5.0,
    "input-field-2": "N",
    "input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "input-field-1": 3.0,
    "input-field-2": "S",
    "input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

### Response Structure 
A list of dictionaries containing the details of the created deployment requests with the following fields:
 - `id`: Unique identifier for the deployment request, which can be used to collect the result
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `time_created`: Server time that the request was made (current time)

#### Response Examples 
```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
data = [ubiops.DeploymentRequestCreate()] # list[DeploymentRequestCreate] | 

# Create batch deployment requests
api_response = api_instance.batch_deployment_requests_create(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**list[DeploymentRequestCreate]**](DeploymentRequestCreate.md)|  | 

### Return type

[**list[BatchDeploymentRequestCreateResponse]**](BatchDeploymentRequestCreateResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_deployment_requests_delete**
> batch_deployment_requests_delete(project_name, deployment_name, request_id, version)

Delete batch deployment requests


### Description
Delete a batch deployment request


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
request_id = 'request_id_example' # str | 
version = 'version_example' # str | 

# Delete batch deployment requests
api_instance.batch_deployment_requests_delete(project_name, deployment_name, request_id, version)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **request_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_deployment_requests_get**
> BatchDeploymentRequestSingleDetail batch_deployment_requests_get(project_name, deployment_name, request_id, version)

Get batch deployment request


### Description
Get a batch request for a deployment. With this method, the result of a batch request may be retrieved.

### Response Structure 
A dictionary containing the details of the deployment request with the following fields:
 - `id`: Unique identifier for the deployment request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the deployment request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated
 - `request_data`: A dictionary containing the data that was sent when the request was created
 - `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples 
```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "status": "pending",
  "success": false,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_last_updated": "2020-03-29T08:09:10.729+00:00",
  "request_data": {
    "input": 82.3
  },
  "result": null,
  "error_message": null
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
request_id = 'request_id_example' # str | 
version = 'version_example' # str | 

# Get batch deployment request
api_response = api_instance.batch_deployment_requests_get(project_name, deployment_name, request_id, version)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **request_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**BatchDeploymentRequestSingleDetail**](BatchDeploymentRequestSingleDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_deployment_requests_list**
> list[BatchDeploymentRequestList] batch_deployment_requests_list(project_name, deployment_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort)

List batch deployment requests


### Description
List all requests for a version

### Optional Parameters
The following parameters should be given as Query parameters: 
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'
- `success`: A boolean value that indicates whether the deployment request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting, can be 'asc' or 'desc'. The default sorting is done in descending order.

### Response Structure 
A list of dictionaries containing the details of the deployment requests with the following fields:
 - `id`: Unique identifier for the deployment request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the deployment request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated

#### Response Examples 
```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_last_updated": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_last_updated": "2020-03-28T20:00:26.613+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
status = 'status_example' # str |  (optional)
success = True # bool |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)

# List batch deployment requests
api_response = api_instance.batch_deployment_requests_list(project_name, deployment_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **status** | **str**|  | [optional] 
 **success** | **bool**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**list[BatchDeploymentRequestList]**](BatchDeploymentRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_batch_delete**
> object batch_pipeline_requests_batch_delete(project_name, pipeline_name, data)

Delete multiple batch pipeline requests


### Description
Delete multiple batch pipeline requests. If one of the given batch pipeline requests does not exist, an error message is given and no request is deleted. A maximum of 100 pipeline requests can be deleted with this method.

### Required Parameters 
A list of ids for the batch requests

#### Request Examples 
```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = None # object | 

# Delete multiple batch pipeline requests
api_response = api_instance.batch_pipeline_requests_batch_delete(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | **object**|  | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_batch_get**
> list[BatchPipelineRequestDetail] batch_pipeline_requests_batch_get(project_name, pipeline_name, data)

Retrieve multiple batch pipeline request results


### Description
Retrieve multiple batch pipeline requests. If one of the given batch pipeline requests does not exist, an error message is given and no request is returned. A maximum of 100 pipeline requests can be retrieved with this method. The pipeline requests are NOT returned in the order they are given in.

### Required Parameters 
A list of ids for the batch requests

#### Request Examples 
```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Response Structure 
A list of dictionaries containing the details of the retrieved pipeline requests with the following fields:
 - `id`: Unique identifier for the pipeline request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the pipeline request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated
 - `request_data`: A dictionary containing the data that was sent when the request was created
 - `deployment_requests`: A list of requests to the deployments in the pipeline. This field is empty when the request is initialized and is updated when all the deployment requests in the pipeline are completed.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples 
```
[
    {
      "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
      "status": "pending",
      "success": false,
      "time_created": "2020-063-28T20:00:26.613+00:00",
      "time_last_updated": "2020-03-28T20:00:26.613+00:00",
      "request_data": {
        "input_field": 23.5
      },
      "deployment_requests": [],
      "error_message": null
    },
    {
      "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
      "status": "pending",
      "success": false,
      "time_created": "2020-063-28T20:00:26.613+00:00",
      "time_last_updated": "2020-03-28T20:00:26.613+00:00",
      "request_data": {
        "input_field": 23.5
      },
      "deployment_requests": [],
      "error_message": null
    }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = None # object | 

# Retrieve multiple batch pipeline request results
api_response = api_instance.batch_pipeline_requests_batch_get(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**list[BatchPipelineRequestDetail]**](BatchPipelineRequestDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_create**
> list[BatchPipelineRequestCreateResponse] batch_pipeline_requests_create(project_name, pipeline_name, data)

Create batch pipeline requests


### Description
Request multiple predictions from a pipeline. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline request collect methods.

The maximum number of requests that can be created per batch is 100.

### Required Parameters 
In case of structured input pipeline: A list of dictionaries, where each dictionary contains the input fields of the pipeline as keys. It is also possible to send a single dictionary as input.
In case of plain input pipeline: A list of strings. It is also possible to send a single string as input.

#### Request Examples 
```
[
  {
    "pipeline-input-field-1": 5.0,
    "pipeline-input-field-2": "N",
    "pipeline-input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "pipeline-input-field-1": 3.0,
    "pipeline-input-field-2": "S",
    "pipeline-input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

### Response Structure 
A list of dictionaries containing the details of the created pipeline requests with the following fields:
 - `id`: Unique identifier for the pipeline request, which can be used to collect the result
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `time_created`: Server time that the request was made (current time)
 

#### Response Examples 
```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = [ubiops.PipelineRequestCreate()] # list[PipelineRequestCreate] | 

# Create batch pipeline requests
api_response = api_instance.batch_pipeline_requests_create(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**list[PipelineRequestCreate]**](PipelineRequestCreate.md)|  | 

### Return type

[**list[BatchPipelineRequestCreateResponse]**](BatchPipelineRequestCreateResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_delete**
> batch_pipeline_requests_delete(project_name, pipeline_name, pipeline_request_id)

Delete batch pipeline requests


### Description
Delete a batch pipeline request. This action cancels all the deployment requests in the pipeline.


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
pipeline_request_id = 'pipeline_request_id_example' # str | 

# Delete batch pipeline requests
api_instance.batch_pipeline_requests_delete(project_name, pipeline_name, pipeline_request_id)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **pipeline_request_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_get**
> BatchPipelineRequestSingleDetail batch_pipeline_requests_get(project_name, pipeline_name, pipeline_request_id)

Get batch pipeline request


### Description
Get a batch request for a pipeline. With this method, the result of the batch request may be retrieved.

### Response Structure 
A dictionary containing the details of the pipeline request with the following fields:
 - `id`: Unique identifier for the pipeline request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the pipeline request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated
 - `request_data`: A dictionary containing the data that was sent when the request was created
 - `deployment_requests`: A list of requests of the deployments in the pipeline. This field is empty when the request is initialized and is updated when all the deployment requests in the pipeline are completed.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
 - `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.

#### Response Examples 
```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "status": "pending",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_last_updated": "2020-03-28T20:00:26.613+00:00",
  "request_data": {
    "input_field": 23.5
  },
  "deployment_requests": [],
  "error_message": null,
  "created_by": "my.example.user@ubiops.com"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
pipeline_request_id = 'pipeline_request_id_example' # str | 

# Get batch pipeline request
api_response = api_instance.batch_pipeline_requests_get(project_name, pipeline_name, pipeline_request_id)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **pipeline_request_id** | **str**|  | 

### Return type

[**BatchPipelineRequestSingleDetail**](BatchPipelineRequestSingleDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_list**
> list[BatchPipelineRequestList] batch_pipeline_requests_list(project_name, pipeline_name, status=status, success=success, limit=limit, offset=offset, sort=sort)

List batch pipeline requests


### Description
List all requests for a pipeline

### Optional Parameters
The following parameters should be given as query parameters: 
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting, can be 'asc' or 'desc'. The default sorting is done in descending order.

### Response Structure 
A list of dictionaries containing the details of the pipeline requests with the following fields:
 - `id`: Unique identifier for the pipeline request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the pipeline request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated

#### Response Examples 
```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_last_updated": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_last_updated": "2020-03-28T20:00:26.613+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
status = 'status_example' # str |  (optional)
success = True # bool |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)

# List batch pipeline requests
api_response = api_instance.batch_pipeline_requests_list(project_name, pipeline_name, status=status, success=success, limit=limit, offset=offset, sort=sort)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **status** | **str**|  | [optional] 
 **success** | **bool**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**list[BatchPipelineRequestList]**](BatchPipelineRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_create**
> BlobList blobs_create(project_name, file, blob_ttl=blob_ttl)

Upload a blob


### Description 
Upload a blob to a project. The returned blob_id may be passed in a deployment or pipeline request as input.

The uploaded blob file can be retrieved by passing the blob_id as well. 

### Optional Parameters 
These parameters should be given in the header.
- `blob-ttl`: The Blob-TTL parameter designates the time to live of the blob in seconds. The default value is 259200 seconds (or 72 hours), the minimum value is 900 seconds and the maximum value is 259200 seconds. 

### Response Structure 
The details of the uploaded blob
- `id`: Unique identifier for the blob (UUID)
- `creation_date`: Time the blob was created
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

#### Response Examples
```
{
  "id": "b58fb853-9311-4583-9688-abed61830abc",
  "creation_date": "2020-05-18T11:26:57.904+00:00",
  "filename": "original-filename.jpg",
  "size": 3439,
  "ttl": 259200
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
file = '/path/to/file' # file | 
blob_ttl = 56 # int |  (optional)

# Upload a blob
api_response = api_instance.blobs_create(project_name, file, blob_ttl=blob_ttl)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **file** | **file**|  | 
 **blob_ttl** | **int**|  | [optional] 

### Return type

[**BlobList**](BlobList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_delete**
> blobs_delete(project_name, blob_id)

Delete a blob


### Description 
Delete a blob from a project


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
blob_id = 'blob_id_example' # str | 

# Delete a blob
api_instance.blobs_delete(project_name, blob_id)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **blob_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_get**
> file blobs_get(project_name, blob_id)

Get a blob


### Description 
Download a blob file in a project

### Response Structure 
- `file`: Blob file


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
blob_id = 'blob_id_example' # str | 

# Get a blob
with api_instance.blobs_get(project_name, blob_id) as response:
    filename = response.getfilename()
    content = response.read()

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **blob_id** | **str**|  | 

### Return type

**file**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_list**
> list[BlobList] blobs_list(project_name, range=range, creation_date=creation_date)

List blobs


### Description 
List all blobs in a project

### Optional Parameters 
These parameters should be given as GET parameters.
- `range`: Number of blobs to be returned. It may be a positive or a negative value. If it is positive, blobs uploaded starting from the creation_date towards the present time are returned. Otherwise, blobs uploaded towards the past are returned. The default value is -50. 
- `creation_date`: Get the blobs uploaded starting from this date. If it is not provided, the uploaded blobs are returned according to the *range* parameter. It should be provided in year-month-day hour:minute:second format.

### Response Structure
A list of details of the blobs in the project
 - `id`: Unique identifier for the blob (UUID)
 - `creation_date`: Time the blob was created
 - `filename`: Original filename of the blob
 - `size`: Size of the uploaded blob in bytes
 - `ttl`: Time to live of the blob in seconds

#### Response Examples
```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-13T14:39:50.149+00:00",
    "filename": "original-filename.jpg",
    "size": 562,
    "ttl": 12338
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T08:35:18.796+00:00",
    "filename": "original-filename2.jpg",
    "size": 3439,
    "ttl": 259200
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
range = 56 # int |  (optional)
creation_date = 'creation_date_example' # str |  (optional)

# List blobs
api_response = api_instance.blobs_list(project_name, range=range, creation_date=creation_date)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **range** | **int**|  | [optional] 
 **creation_date** | **str**|  | [optional] 

### Return type

[**list[BlobList]**](BlobList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployment_audit_events_list**
> list[AuditList] deployment_audit_events_list(project_name, deployment_name, action=action, limit=limit, offset=offset)

List audit events for a deployment


### Description 
List all audit events for a deployment including versions

### Optional Parameters
The following parameters should be given as query parameters:
- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure 
A list of details of the audit events for a deployment
- `id`: Unique identifier for the audit event (UUID)
- `date`: The date when the action was performed
- `action`: Type of action. It can be one of: create, update, delete, info. *info* action denotes that the action does not fall into create, update or delete categories.
- `user`: Email of the user who performed the action
- `event`: Description of the event
- `object_type`: Type of the object on which the action was performed
- `object_name`: Name of the object on which the action was performed. If the object is deleted at the time of listing audit events, this field is empty.

#### Response Examples 
```
[
  {
    "id": "25750859-e082-44df-bde9-cd85ca3f869c",
    "date": "2020-10-23T12:03:55.675+00:00",
    "action": "delete",
    "user": "user@example.com",
    "event": "Deleted environment variable ENV_VAR for deployment deployment-1",
    "object_type": "deployment",
    "object_name": "deployment-1"
  },
  {
    "id": "ce81814d-b00c-4094-a483-814afdb80875",
    "date": "2020-10-23T12:04:28.645+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created version v1 for deployment deployment-1",
    "object_type": "deployment",
    "object_name": "audit-deployment"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
action = 'action_example' # str |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

# List audit events for a deployment
api_response = api_instance.deployment_audit_events_list(project_name, deployment_name, action=action, limit=limit, offset=offset)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **action** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**list[AuditList]**](AuditList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployment_environment_variables_copy**
> list[InheritedEnvironmentVariableList] deployment_environment_variables_copy(project_name, deployment_name, data)

Copy deployment environment variable


### Description
Copy existing environment variables from a source object to the deployment. Variables of the deployment with the same name as ones from the source object will be overwritten with the new value. Only the copied variables are returned.

### Required Parameters
- `source_deployment`: The name of the deployment from which the variables will be copied

### Optional Parameters
- `source_version`: The version of the object from which the variables will be copied

#### Request Examples
Copy the environment variables from a deployment
```
{
  "source_deployment": "example-deployment"
}
```

Copy the environment variables from a version
```
{
  "source_deployment": "example-deployment",
  "source_version": "v1"
}
```

### Response Structure 
A list of the copied variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from. Will be null for copied environment variables.
- `inheritance_name`: Name of the parent object that this variable is inherited from. Will be null for copied environment variables.

#### Response Examples 
```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "deployment_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": null,
    "inheritance_name": null
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
data = ubiops.EnvironmentVariableCopy() # EnvironmentVariableCopy | 

# Copy deployment environment variable
api_response = api_instance.deployment_environment_variables_copy(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **data** | [**EnvironmentVariableCopy**](EnvironmentVariableCopy.md)|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployment_environment_variables_create**
> EnvironmentVariableList deployment_environment_variables_create(project_name, deployment_name, data)

Create deployment environment variable


### Description
Create an environment variable for the deployment. This variable will be inherited by all versions of this deployment. Variables inherited from the project can be shadowed by creating a variable with the same name.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "deployment_variable_a",
  "value": "some_value",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
"id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
"name": "deployment_variable_a",
"value": "some_value",
"secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

# Create deployment environment variable
api_response = api_instance.deployment_environment_variables_create(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployment_environment_variables_delete**
> deployment_environment_variables_delete(project_name, deployment_name, id)

Delete deployment environment variable


### Description
Delete an environment variable of the deployment


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
id = 'id_example' # str | 

# Delete deployment environment variable
api_instance.deployment_environment_variables_delete(project_name, deployment_name, id)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployment_environment_variables_get**
> EnvironmentVariableList deployment_environment_variables_get(project_name, deployment_name, id)

Get deployment environment variable


### Description
Retrieve details of a deployment environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
id = 'id_example' # str | 

# Get deployment environment variable
api_response = api_instance.deployment_environment_variables_get(project_name, deployment_name, id)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployment_environment_variables_list**
> list[InheritedEnvironmentVariableList] deployment_environment_variables_list(project_name, deployment_name)

List deployment environment variables


### Description
List the environment variables defined for the deployment. Includes environment variables defined at project level.
 
### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project` or null if the variable was defined for the deployment directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be null if the variable was defined for the deployment directly

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 

# List deployment environment variables
api_response = api_instance.deployment_environment_variables_list(project_name, deployment_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployment_environment_variables_update**
> EnvironmentVariableList deployment_environment_variables_update(project_name, deployment_name, id, data)

Update deployment environment variable


### Description
Update an environment variable for the deployment. This cannot be used to update inherited variables; to change an inherited variable for a specific deployment you can create a variable with the same name for the deployment.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

#### Request Examples
```
{
  "name": "deployment_variable_a",
  "value": "some new value",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
  "name": "deployment_variable_a",
  "value": "some new value",
  "secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
id = 'id_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

# Update deployment environment variable
api_response = api_instance.deployment_environment_variables_update(project_name, deployment_name, id, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployment_requests_create**
> DeploymentRequestList deployment_requests_create(project_name, deployment_name, version, data, timeout=timeout)

Create deployment requests


### Description 
Request a prediction from a deployment. Deployment requests are made for a specific version of a deployment. It is only possible to make a request if a deployment file is uploaded for that version and the deployment build has succeeded (meaning that the version is in available state).
In case of a **blob** field, the uuid of a previously uploaded blob must be provided.

### Required Parameters
A dictionary which contains the input fields of the deployment as keys

### Optional Parameters
These parameters should be given as GET parameters
- `timeout`: Timeout for the deployment request in seconds. The maximum allowed value is 3600 and the default value is 300.

#### Request Examples
```
{
  "input-field-1": 5.0,
  "input-field-2": "N",
  "input-field-3": [0.25, 0.25, 2.1, 16.3]
}
```

```
{
  "input-field-1": 5.0,
  "blob-input-field": "f52ff875-4980-4d71-9798-a469ef8cece2"
}
```

### Response Structure 
Details of the created deployment request
- `request_id`: Unique identifier for the deployment request
- `success`: A boolean value that indicates whether the deployment request was successful
- `result`: Deployment request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

#### Response Examples
A failed deployment request
```
{
  "request_id": "edcf07b5-ae15-46e6-ba29-daeed53eaa61",
  "success": false,
  "result": None,
  "error_message": "Asset ID not supported"
}
```

A successful deployment request
```
{
  "request_id": "b98a6d68-3173-409a-9e6e-a56804045a9c",
  "success": true,
  "result": {
    "output-field-1": "2.1369",
    "output-field-2": "5.5832",
  },
  "error_message": None
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
data = ubiops.DeploymentRequestCreate() # DeploymentRequestCreate | 
timeout = 56 # int |  (optional)

# Create deployment requests
api_response = api_instance.deployment_requests_create(project_name, deployment_name, version, data, timeout=timeout)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**DeploymentRequestCreate**](DeploymentRequestCreate.md)|  | 
 **timeout** | **int**|  | [optional] 

### Return type

[**DeploymentRequestList**](DeploymentRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_create**
> DeploymentList deployments_create(project_name, data)

Create a deployment


### Description 
Create a deployment by defining the input/output type and input/output fields. In case of **plain** type of input or output, input and output fields should not be given or passed as an empty list.

Possible data types for the input and output fields are:
- **int**: integer
- **string**: string
- **double**: double precision floating point
- **bool**: boolean value (False/True)
- **timestamp**: timestamp
- **array_int**: an array of integers
- **array_double**: an array of double precision floating points
- **array_string**: an array of strings
- **blob**: a blob field. This type of field can be used to pass blobs to the deployment. In deployment and pipeline requests, the uuid of a previously uploaded blob must be provided for this field.

### Required Parameters 
- `name`: Name of the deployment. It is unique within a project.
- `input_type`: Type of the input of the deployment. It can be either structured or plain.
- `output_type`: Type of the output of the deployment. It can be either structured or plain.
- `input_fields`: The list of required deployment input fields. It must contain the fields: name and data_type. The name of an input field is unique for a deployment.
- `output_fields`: The list of required deployment output fields. It must contain the fields: name and data_type. The name of an output field is unique for a deployment.

### Optional Parameters
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

#### Request Examples
A deployment with structured input and output type
```
{
  "name": "deployment-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```

A deployment with plain input type
```
{
  "name": "deployment-1",
  "description": "Deployment one"
  "input_type": "plain",
  "output_type": "structured",
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```

A deployment with plain input and output type
```
{
  "name": "deployment-1",
  "input_type": "plain",
  "output_type": "plain"
  "labels": {
    "type": "deployment"
  }
}
```

### Response Structure 
Details of the created deployment
- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is created
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name and data_type
- `output_fields`: The list of deployment output fields containing name and data_type
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated
- `number_of_versions`: Number of versions that this deployment has

#### Response Examples 
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "deployment-1",
  "project": "project-1",
  "description": "",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-18T08:32:14.876451Z",
  "number_of_versions": 0
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.DeploymentCreate() # DeploymentCreate | 

# Create a deployment
api_response = api_instance.deployments_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**DeploymentCreate**](DeploymentCreate.md)|  | 

### Return type

[**DeploymentList**](DeploymentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_delete**
> deployments_delete(project_name, deployment_name)

Delete a deployment


### Description 
Delete a deployment. If any of the versions of the deployment are referenced in a pipeline, the deployment cannot be deleted.


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 

# Delete a deployment
api_instance.deployments_delete(project_name, deployment_name)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_get**
> DeploymentList deployments_get(project_name, deployment_name)

Get details of deployment


### Description 
Retrieve details of a single deployment in a project

### Response Structure 
Details of a deployment
- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name and data_type
- `output_fields`: The list of deployment output fields containing name and data_type
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated
- `number_of_versions`: Number of versions that this deployment has

#### Response Examples 
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "deployment-1",
  "project": "project-1",
  "description": "",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-19T10:52:23.124784Z",
  "number_of_versions": 2
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 

# Get details of deployment
api_response = api_instance.deployments_get(project_name, deployment_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 

### Return type

[**DeploymentList**](DeploymentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_list**
> list[DeploymentList] deployments_list(project_name, labels=labels)

List deployments in project


### Description 
Deployments can be filtered according to the labels they have by giving labels as a query parameter. Deployments that have at least one of the labels on which is filtered, are returned.

### Optional Parameters
- `labels`: Filter on labels of the deployment. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure 
A list of details of the deployments in the project
- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name and data_type. It is empty in case of plain input type deployments.
- `output_fields`: The list of deployment output fields containing name and data_type. It is empty in case of plain output type deployments.
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated
- `number_of_versions`: Number of versions that this deployment has

#### Response Examples 
```
[
  {
    "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
    "name": "deployment-1",
    "project": "project-1",
    "description": "Temperature deployment",
    "input_type": "structured",
    "output_type": "structured",
    "input_fields": [
      {
        "name": "input-field-1",
        "data_type": "int"
      },
      {
        "name": "input-field-2",
        "data_type": "double"
      }
    ],
    "output_fields": [
      {
        "name": "output-field",
        "data_type": "double"
      }
    ],
    "labels": {
      "type": "deployment"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "number_of_versions": 1
  },
  {
    "id": "5f4e942f-d5b8-4d62-99b2-870c15a82127",
    "name": "deployment-2",
    "project": "project-1",
    "description": "Deployment two",
    "input_type": "structured",
    "output_type": "plain",
    "input_fields": [
      {
        "name": "input-field",
        "data_type": "int"
      }
    ],
    "output_fields": [],
    "labels": {
      "type": "deployment"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z",
    "number_of_versions": 2
  },
  {
    "id": "bd3fae9d-aeec-4cf3-8ef0-5f9224d41904",
    "name": "deployment-3",
    "description": "",
    "project": "project-1",
    "input_type": "plain",
    "output_type": "plain",
    "input_fields": [],
    "output_fields": [],
    "creation_date": "2020-06-18T08:32:14.876451Z",
    "last_updated": "2020-06-19T10:52:23.124784Z",
    "number_of_versions": 1
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
labels = 'labels_example' # str |  (optional)

# List deployments in project
api_response = api_instance.deployments_list(project_name, labels=labels)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **labels** | **str**|  | [optional] 

### Return type

[**list[DeploymentList]**](DeploymentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_update**
> DeploymentList deployments_update(project_name, deployment_name, data)

Update a deployment


### Description 
Update a deployment. It is only possible to update the name, description and labels fields. When updating labels, the labels will replace the existing value for labels. 

### Optional Parameters 
- `name`: New name for the deployment
- `description`: New description for the deployment
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.

#### Request Examples
```
{
  "name": "new-deployment-name"
}
```

### Response Structure 
Details of the updated deployment
- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name and data_type
- `output_fields`: The list of deployment output fields containing name and data_type
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated
- `number_of_versions`: Number of versions that this deployment has

#### Response Examples
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "new-deployment-name",
  "project": "project-1",
  "description": "New deployment description",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-19T10:52:23.124784Z",
  "number_of_versions": 2
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
data = ubiops.DeploymentUpdate() # DeploymentUpdate | 

# Update a deployment
api_response = api_instance.deployments_update(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **data** | [**DeploymentUpdate**](DeploymentUpdate.md)|  | 

### Return type

[**DeploymentList**](DeploymentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_get**
> list[Metrics] metrics_get(project_name, metric, start_time, end_time, object_type, interval=interval, object_id=object_id)

Get metrics


### Description 
Get metrics for the project or a specified object. The following metrics are available:

Metrics on pipeline level: 
 - `requests`: Number of requests made to the object
 - `failed_requests`: Number of failed requests made to the object
 - `input_volume`: Volume of incoming data in bytes
 - `object_requests`: Number of requests made to objects in the pipeline
 
Metrics on version level: 
 - `requests`: Number of requests made to the object
 - `failed_requests`: Number of failed requests made to the object
 - `input_volume`: Volume of incoming data in bytes
 - `output_volume`: Volume of outgoing data in bytes
 - `outputs`: Number of outgoing data items 
 - `compute`: Time in seconds for a request to complete
 - `instances`: Number of active deployment instances
 - `gb_seconds`: Usage of GB seconds, calculated by multiplying the deployment memory sizes in GB by the number of seconds the deployments are running
 - `active_time`: Time in seconds that the deployment is active

### Required Parameters 
- `start_time`: Starting time for the metric values to be returned. It should be provided in datetime isoformat.
- `end_time`: Ending time for the metric values to be returned. It should be provided in datetime isoformat.
- `object_type`: The type of the object for which the metrics are requested. It can be either `version` or `pipeline`.

### Optional Parameters 
- `interval`: Interval for the metric value. It can be minute, hour, day or month. The metric values will be aggregated according to this interval. The default value is hour.
- `object_id`: Uuid of the specific object for which the metrics are requested. When it is not provided, the metrics are aggregated for the given `object_type`.

### Response Structure 
- `start_time`: Timestamp denoting the start of the period over which the metric was measured
- `end_time`: Timestamp denoting the end of the period over which the metric was measured
- `value`: Aggregated metric value for the given interval

#### Response Examples
With interval as minute, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-13 12:03:00
```
[
  {
    "start_time": "2019-11-13T12:00:00+00:00",
    "end_time": "2019-11-13T12:01:00+00:00",
    "value": 100
  },
  {
    "start_time": "2019-11-13T12:01:00+00:00",
    "end_time": "2019-11-13T12:02:00+00:00",
    "value": 134
  },
  {
    "start_time": "2019-11-13T12:02:00+00:00",
    "end_time": "2019-11-13T12:03:00+00:00",
    "value": 112
  }
]

```

With interval as hour, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-13 14:00:00
```
[
  {
   "start_time": "2019-11-13T12:00:00+00:00",
   "end_time": "2019-11-13T13:00:00+00:00",
   "value": 92
  },
  {
    "start_time": "2019-11-13T13:00:00+00:00",
    "end_time": "2019-11-13T14:00:00+00:00",
    "value": 120
  },
  {
    "start_time": "2019-11-13T14:00:00+00:00",
    "end_time": "2019-11-13T15:00:00+00:00",
    "value": 0
  }
]
```
 
With interval as day, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-14 12:00:00
```
[
  {
   "start_time": "2019-11-13T00:00:00+00:00",
   "end_time": "2019-11-14T00:00:00+00:00",
   "value": 528
  },
  {
    "start_time": "2019-11-14T00:00:00+00:00",
    "end_time": "2019-11-15T00:00:00+00:00",
    "value": 342
  }
]
```
 
With interval as month, start_time as 2019-11-13 12:00:00 and end_time as 2019-12-13 12:00:00
```
[
  {
   "start_time": "2019-11-01T00:00:00+00:00",
   "end_time": "2019-12-01T00:00:00+00:00",
   "value": 1983
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
metric = 'metric_example' # str | 
start_time = 'start_time_example' # str | 
end_time = 'end_time_example' # str | 
object_type = 'object_type_example' # str | 
interval = 'interval_example' # str |  (optional)
object_id = 'object_id_example' # str |  (optional)

# Get metrics
api_response = api_instance.metrics_get(project_name, metric, start_time, end_time, object_type, interval=interval, object_id=object_id)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **metric** | **str**|  | 
 **start_time** | **str**|  | 
 **end_time** | **str**|  | 
 **object_type** | **str**|  | 
 **interval** | **str**|  | [optional] 
 **object_id** | **str**|  | [optional] 

### Return type

[**list[Metrics]**](Metrics.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_usage_details_get**
> list[UsagePerDay] organization_usage_details_get(organization_name, month=month)

Get resource usage details


### Description 
Get resource usage for the organization. This returns a list of metrics that are used for billing, aggregated per day.

### Optional Parameters 
- `month`: date indicating the month to fetch usage data for, formatted `YYYY-MM`. If omitted defaults to the current month

### Response Structure 
 - `metric`: The metric that was measured
 - `object_type`: Type of object the metric was measured for (version or pipeline)
 - `usage`: an array of objects each containing the following:
     - `day`: Timestamp denoting the start of the day
     - `value`: Aggregated metric value for the given unit over the given day

#### Response Examples
```
[
  {
    "object_type": "version",
    "metric": "gb_seconds",
    "usage": [
      {
        "day": "2020-07-29T00:00:00Z",
        "value": 4200
      },
      {
        "day": "2020-07-28T00:00:00Z",
        "value": 840
      },
      {
        "day": "2020-07-30T00:00:00Z",
        "value": 960
      }
    ]
  },
  {
    "object_type": "pipeline",
    "metric": "input_volume",
    "usage": [
      {
        "day": "2020-07-28T00:00:00Z",
        "value": 1098
      },
      {
        "day": "2020-07-06T00:00:00Z",
        "value": 18
      },
      {
        "day": "2020-07-16T00:00:00Z",
        "value": 9
      },
      {
        "day": "2020-07-15T00:00:00Z",
        "value": 117
      },
      {
        "day": "2020-07-08T00:00:00Z",
        "value": 90
      }
    ]
  }
]

```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 
month = 'month_example' # str |  (optional)

# Get resource usage details
api_response = api_instance.organization_usage_details_get(organization_name, month=month)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **month** | **str**|  | [optional] 

### Return type

[**list[UsagePerDay]**](UsagePerDay.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_usage_get**
> list[UsagePerMonth] organization_usage_get(organization_name, start_month=start_month)

Get resource usage


### Description 
Get resource usage for the organization. This returns a list of metrics that are used for billing, aggregated per month.

### Optional Parameters 
- `start_month`: date indicating the start month to fetch usage data from, formatted `YYYY-MM`. If omitted results are generated from one year ago.

### Response Structure 
 - `metric`: The metric that was measured
 - `object_type`: Type of object the metric was measured for (version or pipeline)
 - `usage`: an array of objects each containing the following:
     - `month`: Timestamp denoting the start of the month
     - `value`: Aggregated metric value for the given unit over the given month

#### Response Examples
```
[
  {
    "object_type": "pipeline",
    "metric": "input_volume",
    "usage": [
      {
        "month": "2019-08-01T00:00:00Z",
        "value": 1840
      },
      {
        "month": "2019-09-01T00:00:00Z",
        "value": 400
      },
      {
        "month": "2019-10-01T00:00:00Z",
        "value": 1204
      },
      {
        "month": "2019-11-01T00:00:00Z",
        "value": 1598
      },
      {
        "month": "2019-12-01T00:00:00Z",
        "value": 824
      },
      {
        "month": "2020-01-01T00:00:00Z",
        "value": 2036
      },
      {
        "month": "2020-02-01T00:00:00Z",
        "value": 1438
      },
      {
        "month": "2020-03-01T00:00:00Z",
        "value": 932
      },
      {
        "month": "2020-04-01T00:00:00Z",
        "value": 528
      },
      {
        "month": "2020-05-01T00:00:00Z",
        "value": 1484
      },
      {
        "month": "2020-06-01T00:00:00Z",
        "value": 1942
      },
      {
        "month": "2020-07-01T00:00:00Z",
        "value": 1332
      }
    ]
  }
]

```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 
start_month = 'start_month_example' # str |  (optional)

# Get resource usage
api_response = api_instance.organization_usage_get(organization_name, start_month=start_month)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **start_month** | **str**|  | [optional] 

### Return type

[**list[UsagePerMonth]**](UsagePerMonth.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_create**
> OrganizationUserDetail organization_users_create(organization_name, data)

Add a user to an organization


### Description
Add a user to an organization as admin or normal user. The user making the request must be admin of the organization.
The user can later be assigned roles in the projects defined in the scope the organization, such as project-admin, project-viewer etc.

### Required Parameters
- `email`: Email of the user 

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not 


#### Request Examples 
```
{
  "email": "test@example.com",
  "admin": false
}
```

### Response Structure 
Details of the added user
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 
data = ubiops.OrganizationUserCreate() # OrganizationUserCreate | 

# Add a user to an organization
api_response = api_instance.organization_users_create(organization_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **data** | [**OrganizationUserCreate**](OrganizationUserCreate.md)|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_delete**
> organization_users_delete(organization_name, user_id)

Delete a user from an organization


### Description 
Delete a user from an organization. The user making the request must be admin of the organization.
It is not possible to delete the last admin of an organization.

**When a user is deleted from an organization, all his roles from all projects defined in the scope of the organization are also deleted.**


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 

# Delete a user from an organization
api_instance.organization_users_delete(organization_name, user_id)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_get**
> OrganizationUserDetail organization_users_get(organization_name, user_id)

Get details of a user in an organization


### Description 
Get the details of a user in an organization. The user making the request must be admin of the organization.

### Response Structure 
Details of the user
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 

# Get details of a user in an organization
api_response = api_instance.organization_users_get(organization_name, user_id)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_list**
> list[OrganizationUserDetail] organization_users_list(organization_name)

List the users in an organization


### Description 
List users and their details in an organization

### Response Structure 
List of details of users
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples
```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name",
    "admin": true
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name",
    "admin": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 

# List the users in an organization
api_response = api_instance.organization_users_list(organization_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**list[OrganizationUserDetail]**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_update**
> OrganizationUserDetail organization_users_update(organization_name, user_id, data)

Update details of a user in an organization


### Description 
Update the admin status of a user in an organization. The user making the request must be admin of the organization.
It is not possible to change the last admin of an organization to a regular user.

### Required Parameters
- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not 


#### Request Examples 
```
{
  "admin": true
}
```

### Response Structure
Details of the user
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": true
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 
data = ubiops.OrganizationUserUpdate() # OrganizationUserUpdate | 

# Update details of a user in an organization
api_response = api_instance.organization_users_update(organization_name, user_id, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 
 **data** | [**OrganizationUserUpdate**](OrganizationUserUpdate.md)|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_create**
> OrganizationList organizations_create(data)

Create organizations


### Description 
Create a new organization. When a user creates an organization, s/he will automatically become an organization admin.

### Required Parameters 
- `name`: Name of the organization. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `subscription`: Name of the subscription for the organization
- `subscription_agreed`: A boolean field indicating whether the Services Agreement and Terms & Conditions are accepted

### Optional Parameters 
- `subscription_end_date`: End date of the subscription. The subscription will be cancelled on this date. A 'free' subscription cannot have a custom end_date as this subscription is always valid for a year.

#### Request Examples 
```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_agreed": true
}
```

```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_agreed": true,
  "subscription_end_date": "2021-03-25"
}
```

### Response Structure 
Details of the created organization
- `id`: Unique identifier for the organization (UUID) 

- `name`: Name of the organization 

- `creation_date`: Date and time the organization was created 


#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

data = ubiops.OrganizationCreate() # OrganizationCreate | 

# Create organizations
api_response = api_instance.organizations_create(data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**OrganizationCreate**](OrganizationCreate.md)|  | 

### Return type

[**OrganizationList**](OrganizationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_get**
> OrganizationDetail organizations_get(organization_name)

Get details of an organization


### Description 
Get the details of an organization

### Response Structure 
Details of the organization
- `id`: Unique identifier for the organization (UUID) 

- `name`: Name of the organization 

- `creation_date`: Time the organization was created 

- `subscription`: Name of the subscription 


#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 

# Get details of an organization
api_response = api_instance.organizations_get(organization_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**OrganizationDetail**](OrganizationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_list**
> list[OrganizationList] organizations_list()

List organizations


### Description 
List all organizations where the user making the request is a member

### Response Structure
A list of details of the organizations
- `id`: Unique identifier for the organization (UUID) 

- `name`: Name of the organization 

- `creation_date`: Date and time the organization was created 


#### Response Examples
```
[
  {
    "id": "45a1f903-4146-4f15-be4a-302455cd6f7e",
    "name": "organization-name",
    "creation_date": "2020-03-23T11:47:15.436240Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# List organizations
api_response = api_instance.organizations_list()
print(api_response)

# Close the connection
api_client.close()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrganizationList]**](OrganizationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_resource_usage**
> ResourceUsage organizations_resource_usage(organization_name)

List resource usage of an organization


### Description 
List the total number of resources used by this organization

### Response Structure
A list containing the number of
- projects 

- users 

- deployments 

- versions 

- pipelines 

currently used by the organization.

#### Response Examples
```
{
  "projects": 5,
  "users": 3,
  "deployments": 30,
  "versions": 47,
  "pipelines": 2
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 

# List resource usage of an organization
api_response = api_instance.organizations_resource_usage(organization_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**ResourceUsage**](ResourceUsage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_update**
> OrganizationDetail organizations_update(organization_name, data)

Update details of an organization


### Description 
Update an organization. The user making the request must be admin of the organization. Users are able to update the name of the organization, but changes to the subscription can only be done by Dutch Analytics.
To delete the end date of the current subscription, give the 'subscription_end_date' parameter with value null.

### Optional Parameters 
- `name`: New organization name
- `subscription`: New subscription
- `subscription_agreed`: A boolean field indicating whether the Services Agreement and Terms & Conditions are accepted upon upgrading the subscription
- `subscription_end_date`: End date of the new subscription. The required format is `YYYY-MM-DD`. The subscription will be cancelled on this date. If the subscription_end_date was previously set, but should be removed, give a null value for 'subscription_end_date'.

#### Request Examples


```
{
  "name": "new-organization-name"
}
```
```
{
  "subscription": "professional",
  "subscription_agreed": true
}
```
```
{
  "subscription_end_date": "2020-08-30",
  "subscription_agreed": true
}
```

### Response Structure 
Details of the organization
- `id`: Unique identifier for the organization (UUID) 

- `name`: Name of the organization 

- `creation_date`: Time the organization was created 

- `subscription`: Name of the subscription 


#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str | 
data = ubiops.OrganizationUpdate() # OrganizationUpdate | 

# Update details of an organization
api_response = api_instance.organizations_update(organization_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **data** | [**OrganizationUpdate**](OrganizationUpdate.md)|  | 

### Return type

[**OrganizationDetail**](OrganizationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_list**
> list[PermissionList] permissions_list()

List the available permissions


### Description 
List all the available permissions which can be used to create custom roles.

### Response Structure 
A list of available permissions
 - `name`: Name of the permission 



### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# List the available permissions
api_response = api_instance.permissions_list()
print(api_response)

# Close the connection
api_client.close()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PermissionList]**](PermissionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_audit_events_list**
> list[AuditList] pipeline_audit_events_list(project_name, pipeline_name, action=action, limit=limit, offset=offset)

List audit events for a pipeline


### Description 
List all audit events for a pipeline including objects and attachments

### Optional Parameters
The following parameters should be given as query parameters:
- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure 
A list of details of the audit events for a pipeline
- `id`: Unique identifier for the audit event (UUID)
- `date`: The date when the action was performed
- `action`: Type of action. It can be one of: create, update, delete, info. *info* action denotes that the action does not fall into create, update or delete categories.
- `user`: Email of the user who performed the action
- `event`: Description of the event
- `object_type`: Type of the object on which the action was performed
- `object_name`: Name of the object on which the action was performed. If the object is deleted at the time of listing audit events, this field is empty.

#### Response Examples 
```
[
  {
    "id": "44f326de-0ee3-4741-b72e-69e31b3ec55f",
    "date": "2020-10-23T12:21:12.460+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created pipeline object deployment-1 for pipeline pipeline-1",
    "object_type": "pipeline",
    "object_name": "pipeline-1"
  },
  {
    "id": "905cdc19-a02c-4f09-b2fb-42d92da21bda",
    "date": "2020-10-23T12:21:37.247+00:00",
    "action": "update",
    "user": "user@example.com",
    "event": "Updated pipeline object deployment-object for pipeline pipeline-1: name changed from deployment-1 to deployment-object",
    "object_type": "pipeline",
    "object_name": "pipeline-1"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
action = 'action_example' # str |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

# List audit events for a pipeline
api_response = api_instance.pipeline_audit_events_list(project_name, pipeline_name, action=action, limit=limit, offset=offset)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **action** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**list[AuditList]**](AuditList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_create**
> Attachments pipeline_object_attachments_create(project_name, pipeline_name, data)

Create object attachments


### Description 
Create an attachment between two pipeline objects. An attachment can only be made between two objects that have already been added to the pipeline. 
The object where the attachment starts is called the source object. The object that is linked is called the destination object. When attaching two objects, one must also define which source object output fields map to which destination object input fields.
All the input fields in the destination object must be provided in the mapping. In contrast, not all source object output fields need to be used in the mapping. It is also possible that one source output field may link to multiple destination input fields.

The *pipeline_start* object can only be a source object.

In case of plain type of objects, the mapping must be omitted or given as an empty list.

### Required Parameters 
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing source_field_name and destination_field_name keys. The source and destination fields should match in data type, e.g. integer source fields can only be mapped to integer type destination fields.

#### Request Examples 
An attachment between two versions
```
{
  "source_name": "deployment-1-v1",
  "destination_name": "deployment-2-v1",
  "mapping": [
    {
      "source_field_name": "deployment-output-field-1",
      "destination_field_name": "deployment-2-input-field-1"
    },
    {
      "source_field_name": "deployment-output-field-2",
      "destination_field_name": "deployment-2-input-field-2"
    },
    {
      "source_field_name": "deployment-output-field-3",
      "destination_field_name": "deployment-2-input-field-3"
    }
  ]
}
```

```
{
  "source_name": "blob-deployment-v3",
  "destination_name": "blob-deployment-v4",
  "mapping": []
}
```
 
An attachment between a pipeline and version
```
{
  "source_name": "pipeline_start",
  "destination_name": "deployment-2-v2",
  "mapping": [
    {
      "source_field_name": "pipeline-input-field-1",
      "destination_field_name": "deployment-input-field-1"
    },
    {
      "source_field_name": "pipeline-input-field-2",
      "destination_field_name": "deployment-input-field-2"
    }
  ]
}
```

### Response Structure 
Details of the created attachment
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing source_field_name and destination_field_name

#### Response Examples 
```
{
  "source_name": "pipeline-1",
  "destination_name": "deployment-2-v2",
  "mapping": [
    {
      "source_field_name": "pipeline-input-field-1",
      "destination_field_name": "deployment-input-field-1"
    },
    {
      "source_field_name": "pipeline-input-field-2",
      "destination_field_name": "deployment-input-field-2"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.AttachmentsCreate() # AttachmentsCreate | 

# Create object attachments
api_response = api_instance.pipeline_object_attachments_create(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**AttachmentsCreate**](AttachmentsCreate.md)|  | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_delete**
> pipeline_object_attachments_delete(project_name, destination_name, pipeline_name, source_name)

Delete attachment of a source and destination object


### Description 
Delete an attachment in a pipeline. The referenced and original objects of the attachment still exist in the pipeline, only the link between them is deleted.


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
destination_name = 'destination_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

# Delete attachment of a source and destination object
api_instance.pipeline_object_attachments_delete(project_name, destination_name, pipeline_name, source_name)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **destination_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_get**
> AttachmentsList pipeline_object_attachments_get(project_name, destination_name, pipeline_name, source_name)

Get an attachment of a source and destination object


### Description 
Get the details of a single attachment between a source and destination object in a pipeline

### Response Structure 
Details of the attachment
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing the link between the source object output field (source_field_name) and destination object input field (destination_field_name)

#### Response Examples 
```
{
  "source_name": "deployment-2-v2",
  "destination_name": "deployment-3-v1",
  "mapping": [
    {
      "source_field_name": "deployment-2-output-field-1",
      "destination_field_name": "deployment-3-input-field-1"
    },
    {
      "source_field_name": "deployment-2-output-field-2",
      "destination_field_name": "deployment-3-input-field-2"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
destination_name = 'destination_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

# Get an attachment of a source and destination object
api_response = api_instance.pipeline_object_attachments_get(project_name, destination_name, pipeline_name, source_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **destination_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

[**AttachmentsList**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_list**
> list[AttachmentsList] pipeline_object_attachments_list(project_name, pipeline_name)

List object attachments


### Description 
List all attachments in a pipeline

### Response Structure 
A list of details of the attachments in the pipeline
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing source_field_name and destination_field_name

#### Response Examples 
```
[
  {
    "source_name": "pipeline-1",
    "destination_name": "deployment-2-v2",
    "mapping": [
      {
        "source_field_name": "pipeline-input-field-1",
        "destination_field_name": "deployment-input-field-1"
      },
      {
        "source_field_name": "pipeline-input-field-2",
        "destination_field_name": "deployment-input-field-2"
      }
    ]
  },
  {
    "source_name": "deployment-2-v2",
    "destination_name": "deployment-3-v1",
    "mapping": [
      {
        "source_field_name": "deployment-output-field-1",
        "destination_field_name": "deployment-3-input-field-1"
      },
      {
        "source_field_name": "deployment-output-field-2",
        "destination_field_name": "deployment-3-input-field-2"
      },
      {
        "source_field_name": "deployment-output-field-3",
        "destination_field_name": "deployment-3-input-field-3"
      }
    ]
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

# List object attachments
api_response = api_instance.pipeline_object_attachments_list(project_name, pipeline_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[AttachmentsList]**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_source_get**
> list[AttachmentsList] pipeline_object_attachments_source_get(project_name, pipeline_name, source_name)

List the attachments of a source object


### Description 
List attachments of a source object in a pipeline

### Response Structure 
A list of details of the attachments of the given source object in the pipeline
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing the link between the source object output field (source_field_name) and destination object input field (destination_field_name)

#### Response Examples 
```
[
  {
    "source_name": "deployment-2-v2",
    "destination_name": "deployment-3-v1",
    "mapping": [
      {
        "source_field_name": "deployment-2-output-field-1",
        "destination_field_name": "deployment-3-input-field-1"
      },
      {
        "source_field_name": "deployment-2-output-field-2",
        "destination_field_name": "deployment-3-input-field-2"
      }
    ]
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

# List the attachments of a source object
api_response = api_instance.pipeline_object_attachments_source_get(project_name, pipeline_name, source_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

[**list[AttachmentsList]**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_environment_variables_list**
> list[InheritedEnvironmentVariableList] pipeline_object_environment_variables_list(project_name, name, pipeline_name)

List pipeline object environment variables


### Description
List environment variables accessible to objects in the pipeline
 
### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `deployment`, or `version`
- `inheritance_name`: Name of the parent object that this variable is inherited from

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "deployment",
    "inheritance_name": "deployment_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

# List pipeline object environment variables
api_response = api_instance.pipeline_object_environment_variables_list(project_name, name, pipeline_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_create**
> PipelineObjectList pipeline_objects_create(project_name, pipeline_name, data)

Add an object to a pipeline


### Description 
Create a pipeline object. The pipeline object that is added is a reference to the real object. In this way, multiple references to the same object may be added to a pipeline.
The reference_name refers to the deployment name and the version is the version of the deployment which will be added to the pipeline as an object.

### Required Parameters 
- `name`: Name of the pipeline object. It is unique within a pipeline
- `reference_name`: Name of the object it will reference
- `version`: Version name of reference object

#### Request Examples 
```
{
  "name": "deployment-1-v1",
  "reference_name": "deployment-1",
  "version": "version-1"
}
```

### Response Structure 
Details of the created pipeline object
- `id`: Unique identifier for the pipeline object (UUID)
- `name`: Name of the pipeline object
- `reference_name`: Name of the object it will reference
- `version`: Version name of reference object

#### Response Examples 
```
{
  "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
  "name": "deployment-1-v1",
  "reference_name": "deployment-1",
  "version": "version-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.PipelineObjectCreate() # PipelineObjectCreate | 

# Add an object to a pipeline
api_response = api_instance.pipeline_objects_create(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineObjectCreate**](PipelineObjectCreate.md)|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_delete**
> pipeline_objects_delete(project_name, name, pipeline_name)

Delete object from pipeline

  
### Description 
Delete a pipeline object. Only the reference in the pipeline is deleted. The original object (deployment and version) still exists.
If the object is attached to another object, the attachment is also deleted.


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

# Delete object from pipeline
api_instance.pipeline_objects_delete(project_name, name, pipeline_name)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_get**
> PipelineObjectList pipeline_objects_get(project_name, name, pipeline_name)

Get an object in a pipeline


### Description 
Retrieve the details of a single pipeline object

### Response Structure 
Details of the pipeline object
- `id`: Unique identifier for the pipeline object (UUID)
- `name`: Name of the pipeline object
- `reference_name`: Name of the object it references
- `version`: Version name of reference object

#### Response Examples 
A dictionary containing details of the pipeline object
```
{
  "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
  "name": "deployment-1-v1",
  "reference_name": "deployment-1",
  "version": "version-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

# Get an object in a pipeline
api_response = api_instance.pipeline_objects_get(project_name, name, pipeline_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_list**
> list[PipelineObjectList] pipeline_objects_list(project_name, pipeline_name)

List objects in a pipeline


### Description 
List all pipeline objects in a pipeline

### Response Structure 
A list of details of the pipeline objects in the pipeline
- `id`: Unique identifier for the pipeline object (UUID)
- `name`: Name of the pipeline object
- `reference_name`: Name of the object it references
- `version`: Version name of reference object

#### Response Examples 
A list of pipeline objects
```
[
  {
    "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
    "name": "deployment-1-v1",
    "reference_name": "deployment-1",
    "version": "version-1"
  },
  {
    "id": "1a4b0e28-3de1-442a-b1eb-947f22a69381",
    "name": "deployment-2-v1",
    "reference_name": "deployment-2",
    "version": "v1"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

# List objects in a pipeline
api_response = api_instance.pipeline_objects_list(project_name, pipeline_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[PipelineObjectList]**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_update**
> PipelineObjectList pipeline_objects_update(project_name, name, pipeline_name, data)

Update an object in a pipeline


### Description 
Update a pipeline object. It is not possible to update the reference_name. All necessary fields are validated again.

### Optional Parameters 
- `name`: New name for the pipeline object
- `version`: New version for the pipeline object. Since the input/output fields of different versions are the same, the version of a deployment pipeline object can be changed with another version of the same deployment.

#### Request Examples 
```
{
  "name": "new-pipeline-object-name"
}
```
 
```
{
  "name": "deployment-1-v2"
  "version": "version-2"
}
```

### Response Structure 
Details of the updated pipeline object
- `id`: Unique identifier for the pipeline object (UUID)
- `name`: Name of the pipeline object
- `reference_name`: Name of the object it references
- `version`: Version name of reference object

#### Response Examples 
```
{
  "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
  "name": "deployment-1-v2",
  "reference_name": "deployment-1",
  "version": "version-2"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.PipelineObjectUpdate() # PipelineObjectUpdate | 

# Update an object in a pipeline
api_response = api_instance.pipeline_objects_update(project_name, name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineObjectUpdate**](PipelineObjectUpdate.md)|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_requests_create**
> PipelineRequestList pipeline_requests_create(project_name, pipeline_name, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)

Make a request to a pipeline


### Description 
Make a pipeline request. This method returns all the results of the deployment requests made within the pipeline.

### Required Parameters 
A dictionary which contains the input fields of the pipeline as keys

### Optional Parameters
These parameters should be given as GET parameters
- `pipeline_timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 7200 and the default value is 3600.
- `deployment_timeout`: Timeout for each deployment request in the pipeline in seconds.  The maximum allowed value is 3600 and the default value is 300.
Maximum allowed value for both is 3600 seconds and the default value is 300 seconds.

#### Request Examples
```
{
  "pipeline-input-field-1": 5.0,
  "pipeline-input-field-2": "N"
}
```

### Response Structure 
- `project`: Name of the project in which the request is made
- `pipeline`: Name of the pipeline for which the request is made
- `pipeline_request_id`: Unique identifier for the pipeline request
- `deployment_requests`: A list of dictionaries containing the results of the deployment requests made for the version objects in the pipeline. The dictionaries contain the following fields:
    - `request_id`: Unique identifier for the deployment request
    - `pipeline_object`: Name of the object in the pipeline
    - `success`: A boolean value that indicates whether the deployment request was successful
    - `request_data`: Input data for the deployment request
    - `result`: Deployment request result value. NULL if the request failed.
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples
```
{
  "project": "project-1",
  "pipeline": "pipeline-1",
  "pipeline_request_id": "286f771b-6617-4985-ab49-12ed720e62b1",
  "deployment_requests": [
    {
      "request_id": "a7524614-bdb7-41e1-b4c1-653bb72c30b4",
      "pipeline_object": "deployment-object-1",
      "success": true,
      "request_data": {
        "deployment-1-input-field-1": 5,
        "deployment-1-input-field-2": 0.4
      },
      "result": {
        "deployment-1-output-field-1": 0.23,
        "deployment-1-output-field-2": 10
      },
      "error_message": None 
    },
    {
      "request_id": "fe322c50-58f8-4e67-b7d6-cba14273874e",
      "pipeline_object": "deployment-object-2",
      "success": false,
      "request_data": {
        "deployment-2-input-field": 10
      },
      "result": None,
      "error_message": "Invalid message format" 
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.PipelineRequestCreate() # PipelineRequestCreate | 
pipeline_timeout = 56 # int |  (optional)
deployment_timeout = 56 # int |  (optional)

# Make a request to a pipeline
api_response = api_instance.pipeline_requests_create(project_name, pipeline_name, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineRequestCreate**](PipelineRequestCreate.md)|  | 
 **pipeline_timeout** | **int**|  | [optional] 
 **deployment_timeout** | **int**|  | [optional] 

### Return type

[**PipelineRequestList**](PipelineRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_create**
> PipelineList pipelines_create(project_name, data)

Create pipelines


### Description 
Create a pipeline in a project. 

The input_fields represent the fields that the input data for pipeline requests should contain. When an object is attached to the pipeline, it means that the input data will be forwarded to these objects.

### Required Parameters 
- `name`: Name of the pipeline. It is unique within a project.
- `input_type`: Type of the pipeline. It can be either structured or plain.
- `input_fields`: A list of fields with name and data_type. In case of plain pipelines, the input_fields should be omitted or given as an empty list. For structured pipelines, it is possible to leave this field empty.

### Optional Parameters
- `description`: Description of the pipeline
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

#### Request Examples 
A structured pipeline
```
{
  "name": "pipeline-1",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```
 
A plain pipeline
```
{
  "name": "pipeline-2",
  "input_type": "plain",
  "description": "my description"
}
```

### Response Structure 
Details of the created pipeline
- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description`: Description of the pipeline
- `project`: Project name in which the pipeline is created
- `input_type`: Type of the pipeline
- `input_fields`: A list of pipeline fields with name and data_type
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

#### Response Examples 
```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "name": "pipeline-1",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-03-24T09:43:51.791253Z"
}
```
 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.PipelineCreate() # PipelineCreate | 

# Create pipelines
api_response = api_instance.pipelines_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**PipelineCreate**](PipelineCreate.md)|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_delete**
> pipelines_delete(project_name, pipeline_name)

Delete pipeline


### Description 
Delete a pipeline. This will also delete all objects and attachments in the pipeline.


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

# Delete pipeline
api_instance.pipelines_delete(project_name, pipeline_name)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get**
> PipelineList pipelines_get(project_name, pipeline_name)

Get pipeline


### Description 
Get the details of a single pipeline

### Response Structure 
Details of the pipeline
- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description` Description of the pipeline
- `project`: Project name in which the pipeline is defined
- `input_type`: Type of the pipeline
- `input_fields`: A list of pipeline fields with name and data_type
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

#### Response Examples 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

# Get pipeline
api_response = api_instance.pipelines_get(project_name, pipeline_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_list**
> list[PipelineList] pipelines_list(project_name, labels=labels)

List pipelines


### Description 
Pipelines can be filtered according to the labels they have by giving labels as a query parameter. Pipelines that have at least one of the labels on which is filtered, are returned.

### Optional Parameters
- `labels`: Filter on labels of the pipeline. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure 
A list of details of the pipelines in the project
- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description of the pipeline
- `input_type`: Type of the pipeline
- `input_fields`: A list of pipeline fields with name and data_type
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

#### Response Examples 
```
[
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "name": "pipeline-1",
    "project": "project-1",
    "description": "my description",
    "input_type": "structured",
    "input_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ],
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z"
  },
  {
    "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
    "name": "pipeline-2",
    "project": "project-1",
    "description": "my description",
    "input_type": "plain",
    "input_fields": [],
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
labels = 'labels_example' # str |  (optional)

# List pipelines
api_response = api_instance.pipelines_list(project_name, labels=labels)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **labels** | **str**|  | [optional] 

### Return type

[**list[PipelineList]**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_update**
> PipelineList pipelines_update(project_name, pipeline_name, data)

Update pipeline


    
### Description 
Update a pipeline. All necessary fields are validated again. When updating labels, the labels will replace the existing value for labels. 

### Optional Parameters 
- `name`: New name for the pipeline
- `description`: New description for the pipeline
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `input_type`: New type for the pipeline. It is possible to change the type from plain to structured and vice versa.
- `input_fields`: New input fields for the pipeline.

If the type of pipeline is updated to plain, the input fields are deleted. In this case, input_fields should either be omitted or provided as en empty list.
If the type of pipeline is updated to structured, the old fields are deleted, if there existed any. The new fields are created, if any is provided. If one or more old fields need to be kept, they must be provided again.

**To delete the input fields of a pipeline**, provide an empty list for input_fields field.

#### Request Examples 
```
{
  "name": "new-pipeline-name"
}
```

```
{
  "description": "New pipeline description",
  "labels": {
    "tag": "production"
  }
}
```

```
{
  "input_type": "plain"
}
```
 
```
{
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double"
    },
    {
      "name": "new-field-2",
      "data_type": "array_string"
    }
  ]
}
```

```
{
  "input_type": "structured",
  "input_fields": []
}
```

### Response Structure 
Details of the updated pipeline
- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description for the pipeline
- `input_type`: Type of the pipeline
- `input_fields`: A list of pipeline fields with name and data_type
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

#### Response Examples 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "new-pipeline-name",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double"
    },
    {
      "name": "new-field-2",
      "data_type": "array_string"
    }
  ],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.PipelineCreate() # PipelineCreate | 

# Update pipeline
api_response = api_instance.pipelines_update(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineCreate**](PipelineCreate.md)|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_audit_events_list**
> list[AuditList] project_audit_events_list(project_name, action=action, limit=limit, offset=offset)

List audit events in a project


### Description 
List all audit events in a project including all objects

### Optional Parameters
The following parameters should be given as query parameters:
- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure 
A list of details of the audit events in the project
- `id`: Unique identifier for the audit event (UUID)
- `date`: The date when the action was performed
- `action`: Type of action. It can be one of: create, update, delete, info. *info* action denotes that the action does not fall into create, update or delete categories.
- `user`: Email of the user who performed the action
- `event`: Description of the event
- `object_type`: Type of the object on which the action was performed
- `object_name`: Name of the object on which the action was performed. If the object is deleted at the time of listing audit events, this field is empty.

#### Response Examples 
```
[
  {
    "id": "54c1ea23-5773-4821-8fd7-1b577cc301bc",
    "date": "2020-05-23T11:53:02.873+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created project test-project",
    "object_type": "project",
    "object_name": "test-project"
  },
  {
    "id": "764e254c-7402-4445-ac79-009d08b21caa",
    "date": "2020-05-23T11:57:20.072+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created deployment deployment-1",
    "object_type": "deployment",
    "object_name": "deployment-1"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
action = 'action_example' # str |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

# List audit events in a project
api_response = api_instance.project_audit_events_list(project_name, action=action, limit=limit, offset=offset)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **action** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**list[AuditList]**](AuditList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_create**
> EnvironmentVariableList project_environment_variables_create(project_name, data)

Create project environment variable


### Description
Create an environment variable for the project. This variable will be inherited by all deployments in this project.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```

```
{
  "name": "database_password",
  "value": "password",
  "secret": true
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```

```
{
  "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
  "name": "database_password",
  "value": null,
  "secret": true
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

# Create project environment variable
api_response = api_instance.project_environment_variables_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_delete**
> project_environment_variables_delete(project_name, id)

Delete project environment variable


### Description
Delete an environment variable of the project


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

# Delete project environment variable
api_instance.project_environment_variables_delete(project_name, id)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_get**
> EnvironmentVariableList project_environment_variables_get(project_name, id)

Get project environment variable


### Description
Retrieve details of a project environment variable.

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

# Get project environment variable
api_response = api_instance.project_environment_variables_get(project_name, id)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_list**
> list[EnvironmentVariableList] project_environment_variables_list(project_name)

List project environment variables


### Description
List the environment variables defined for the project. These are the variables that are inherited by all deployments in this project.
 
### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 

# List project environment variables
api_response = api_instance.project_environment_variables_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[EnvironmentVariableList]**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_update**
> EnvironmentVariableList project_environment_variables_update(project_name, id, data)

Update project environment variable


### Description
Update an environment variable for the projects

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore. 
- `value`: The value of the variable as a string. It may be an empty string. 
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets). 

#### Request Examples
```
{
  "name": "database_schema",
  "value": "new+schema",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "new_schema",
  "secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

# Update project environment variable
api_response = api_instance.project_environment_variables_update(project_name, id, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_usage_get**
> list[UsagePerMonth] project_usage_get(project_name, start_month=start_month)

Get resource usage


### Description 
Get resource usage for the project. This returns a list of metrics that are used for billing, aggregated per month.

### Optional Parameters 
- `start_month`: date indicating the start month to fetch usage data from, formatted `YYYY-MM`. If omitted results are generated from one year ago.

### Response Structure 
 - `metric`: The metric that was measured
 - `object_type`: Type of object the metric was measured for (version or pipeline)
 - `usage`: an array of objects each containing the following:
     - `month`: Timestamp denoting the start of the month
     - `value`: Aggregated metric value for the given unit over the given month

#### Response Examples
```
[
  {
    "object_type": "pipeline",
    "metric": "input_volume",
    "usage": [
      {
        "month": "2019-08-01T00:00:00Z",
        "value": 1840
      },
      {
        "month": "2019-09-01T00:00:00Z",
        "value": 400
      },
      {
        "month": "2019-10-01T00:00:00Z",
        "value": 1204
      },
      {
        "month": "2019-11-01T00:00:00Z",
        "value": 1598
      },
      {
        "month": "2019-12-01T00:00:00Z",
        "value": 824
      },
      {
        "month": "2020-01-01T00:00:00Z",
        "value": 2036
      },
      {
        "month": "2020-02-01T00:00:00Z",
        "value": 1438
      },
      {
        "month": "2020-03-01T00:00:00Z",
        "value": 932
      },
      {
        "month": "2020-04-01T00:00:00Z",
        "value": 528
      },
      {
        "month": "2020-05-01T00:00:00Z",
        "value": 1484
      },
      {
        "month": "2020-06-01T00:00:00Z",
        "value": 1942
      },
      {
        "month": "2020-07-01T00:00:00Z",
        "value": 1332
      }
    ]
  }
]

```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
start_month = 'start_month_example' # str |  (optional)

# Get resource usage
api_response = api_instance.project_usage_get(project_name, start_month=start_month)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **start_month** | **str**|  | [optional] 

### Return type

[**list[UsagePerMonth]**](UsagePerMonth.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create**
> ProjectList projects_create(data)

Create projects


### Description 
Create a new project with the provided name.
**Only the organization admins have permission to make this request.** When a new project is created, the current organization admins are assigned project-admin role for the created project.

### Required Parameters 
- `name`: Name of the project. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `organization_name`: Name of the organization in which the project is going to be created
 
#### Request Examples 
```
{
  "name": "project-1",
  "organization_name": "organization-1"
}
```

### Response Structure 
Details of the created project
- `id`: Unique identifier for the project (UUID) 

- `name`: Name of the project 

- `creation_date`: Time the project was created 

- `organization_name`: Name of the organization in which the project is created

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

data = ubiops.ProjectCreate() # ProjectCreate | 

# Create projects
api_response = api_instance.projects_create(data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProjectCreate**](ProjectCreate.md)|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete**
> projects_delete(project_name)

Delete a project


### Description 
Delete a project. The user making the request must have appropriate permissions.
**When project is deleted, all the deployments and pipelines defined in it are also deleted.**


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 

# Delete a project
api_instance.projects_delete(project_name)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> ProjectList projects_get(project_name)

Get details of a project


### Description 
Get the details of a single project. The user making the request must have appropriate permissions.

### Response Structure 
Details of a project
- `id`: Unique identifier for the project (UUID) 

- `name`: Name of the project 

- `creation_date`: Time the project was created 

- `organization_name`: Name of the organization in which the project is created

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 

# Get details of a project
api_response = api_instance.projects_get(project_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list**
> list[ProjectList] projects_list()

List projects


### Description 
List all projects to which the user making request has access. The projects in organizations to which the user belongs are shown.

### Response Structure
A list of details of the projects
- `id`: Unique identifier for the project (UUID) 

- `name`: Name of the project 

- `creation_date`: Time the project was created 

- `organization_name`: Name of the organization in which the project is created

#### Response Examples
```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "name": "project-1",
    "creation_date": "2018-10-26",
    "organization_name": "organization-1"
  },
  {
    "id": "e6a85cd7-94cc-44cf-9fa0-4b462d5a71ab",
    "name": "project-2",
    "creation_date": "2019-06-20",
    "organization_name": "organization-2"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# List projects
api_response = api_instance.projects_list()
print(api_response)

# Close the connection
api_client.close()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProjectList]**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_log_list**
> list[Logs] projects_log_list(project_name, data)

List logs for a project


### Description 
Retrieve the logs of all objects in a project, including deployments, pipelines and requests. Using filters you can filter the logs on the objects and information of your choice. 

### Required Parameters 
- `filters`: A dictionary containing information to filter logs on. It may contain zero or more of the following fields: 

    - `deployment_name`: name of a deployment 

    - `version`: a version name. If this field is present in the request, deployment_name must also be given. The versions are only meaningful in combination with the deployments they are defined for. 

    - `pipeline_name`: name of a pipeline 

    - `pipeline_object_name`: name of a pipeline object. If this field is present in the request, pipeline_name must also be given. The pipeline objects are only meaningful in combination with the pipelines they are defined in. 

    - `request_id`: the UUID of a deployment request 

    - `pipeline_request_id`: the UUID of a pipeline request 

    - `system`: whether the log was generated by the system or user code (true / false) 


Any combination of filters may be given in the request. For example, if only a deployment_name is provided, all logs for that deployment are returned. These logs can contain information from all the pipelines that deployment is referenced in. If the filters dictionary is empty, all logs for all objects in the project are returned.

### Optional Parameters 
- `date`: Starting date for the logs. If it is not provided and the `id` parameter is not set, the most recent logs are returned. It should be provided in ISO 8601 format. The results are inclusive of the given date. 

- `id`: identifier for log lines. If specified, it will act as a starting point for the interval in which to query the logs. This can be useful when making multiple queries to obtain consecutive logs

    It will include the log having the log id equal to the id value in the response, regardless of whether the date_range is positive or negative.
- `limit`: Limit for the logs response. If specified, it will limit the total number of logs returned from the query to the specified number. Defaults to 50, the maximum is 500. 
 
- `date_range`: The date range parameter sets the interval of time in which to query the logs, specified in seconds. It may be a positive or a negative value. 

    If it is positive, logs starting from the specified date / log id (both inclusive) plus date range seconds towards the present time are returned. 

    Otherwise, logs starting from the specified date / log id (both inclusive) minus date range seconds towards the past are returned. 
 
    The default value is -21600 (6 hours). The maximum value is -/+ 86400 seconds (24 hours).
    
If no date or id is specified, the API will use the current time as a starting point and try to fetch the logs starting from now minus date range seconds into the past.

#### Request Examples 
```
{
  "filters": {
    "deployment_name": "deployment-1",
    "version": "v1"
  },
  "date": "2020-01-01T00:00:00.000000Z"
}
```

```
{
  "filters": {
    "pipeline_name": "pipeline-1"
  },
  "id": "41d7a7c5cd025e3501a00000",
  "date_range": -100
}
```

```
{
  "filters": {
    "pipeline_name": "pipeline-1",
    "deployment_name": "deployment-1",
    "version": "v1"
  },
  "date": "2020-01-01T00:00:00.000000Z",
  "date_range": -86400,
  "limit": 5
}
```

### Response Structure 
A list of log details
- `id`: Unique UUID of the log line 

- `log`: Log line text 

- `date`: Time the log line was created
 
The following fields will be returned on response if they are set for the log line:
- `deployment_name`:  The deployment which the log is related to 

- `version`:  The version which the log is related to 

- `pipeline_name`:  The pipeline which the log is related to 

- `pipeline_object_name`: The pipeline object which the log is related to 

- `request_id`:  The deployment request the log is related to 

- `pipeline_request_id`:  The pipeline request the log is related to 

- `system`:  Whether the log was generated by the system (true / false)

#### Response Examples 
Logs for a specific deployment and version
```
[
  {
    "id": "5dcad12ba76a2c6e4331f180",
    "deployment_name": "deployment-1",
    "version": "v1",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Prediction result 0.14981"
  },
  {
    "id": "5dcad12ba76a2c6e4331f181",
    "deployment_name": "deployment-1",
    "version": "v1",
    "pipeline_name": "pipeline-2",
    "pipeline_object_name": "deployment-1-v1-object",
    "pipeline_trace_id": "8bb6ed79-8606-4acf-acd2-90507130523c",
    "date": "2020-01-01T00:00:01.000000Z",
    "log": "[Error] Deployment call result (failed)"
  }
]
```
 
Logs for a specific pipeline
```
[
  {
    "id": "5dcad12ba76a2c6e4331f192",
    "deployment_name": "deployment-2",
    "version": "v2",
    "pipeline_name": "pipeline-1",
    "pipeline_object_name": "deployment-2-v2-object",
    "pipeline_trace_id": "4f75b10d-6012-47ab-ae68-cc9e69f35841",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Deployment call result (success): 0.2316"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.LogsCreate() # LogsCreate | 

# List logs for a project
api_response = api_instance.projects_log_list(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**LogsCreate**](LogsCreate.md)|  | 

### Return type

[**list[Logs]**](Logs.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_resource_usage**
> ProjectResourceUsage projects_resource_usage(project_name)

List resource usage of a project


### Description 
List the total number of resources used in a project

### Response Structure
A list containing the number of
- deployments 

- versions 

- pipelines 

currently defined in the project.

#### Response Examples
```
{
  "deployments": 30,
  "versions": 47,
  "pipelines": 2
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 

# List resource usage of a project
api_response = api_instance.projects_resource_usage(project_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**ProjectResourceUsage**](ProjectResourceUsage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_update**
> ProjectList projects_update(project_name, data)

Update a project


### Description 
Update the name of a single project. The user making the request must have appropriate permissions.

### Optional Parameters 
- `name`: New project name

#### Request Examples 
```
{
  "name": "project-name-example"
}
```

### Response Structure 
Details of a project
- `id`: Unique identifier for the project (UUID) 

- `name`: Name of the project 

- `creation_date`: Time the project was created 

- `organization_name`: Name of the organization in which the project is created

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.ProjectUpdate() # ProjectUpdate | 

# Update a project
api_response = api_instance.projects_update(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ProjectUpdate**](ProjectUpdate.md)|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_schedules_create**
> ScheduleList request_schedules_create(project_name, data)

Create request schedules


### Description 
Create a new request schedule with the provided name

### Required Parameters 
- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `object_type`: Type of object for which the request is made. Can be either 'deployment' or 'pipeline'. 

- `object_name`: Name of deployment or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 


### Optional Parameters
- `version`: Name of version if type of object is 'deployment' 

- `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary. 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds. This field is not used for batch requests. 

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'. 


#### Request Examples 
```
{
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 300,
  "enabled": true
}
```

### Response Structure 
Details of the created request schedule
- `name`: Name of the request 

- `object_type`: Type of object for which the request is made 

- `object_name`: Name of deployment or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 

- `version`: Name of version if type of object is 'deployment' 

- `request_data`: Input data for the request schedule 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled 

- `creation_date`: The date when the request schedule was created

#### Response Examples 
```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 300,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.ScheduleCreate() # ScheduleCreate | 

# Create request schedules
api_response = api_instance.request_schedules_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ScheduleCreate**](ScheduleCreate.md)|  | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_schedules_delete**
> request_schedules_delete(project_name, schedule_name)

Delete a request schedule


### Description 
Delete the request schedule from the project. 

If you want to temporarily disable a request schedule, update the request with `enabled` set to False.


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
schedule_name = 'schedule_name_example' # str | 

# Delete a request schedule
api_instance.request_schedules_delete(project_name, schedule_name)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **schedule_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_schedules_get**
> ScheduleList request_schedules_get(project_name, schedule_name)

Get details of a request schedule


### Description 
Retrieve details of a single request schedule

### Response Structure 
Details of a request schedule
- `name`: Name of the request 

- `object_type`: Type of object for which the request is made 

- `object_name`: Name of deployment or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 

- `version`: Name of version if type of object is 'deployment' 

- `request_data`: Input data for the request schedule 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled 

- `creation_date`: The date when the request schedule was created

#### Response Examples 
```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 200,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
schedule_name = 'schedule_name_example' # str | 

# Get details of a request schedule
api_response = api_instance.request_schedules_get(project_name, schedule_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **schedule_name** | **str**|  | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_schedules_list**
> list[ScheduleList] request_schedules_list(project_name)

List request schedules


### Description 
List the request schedules in a project. The user has to have 'requests.list' permission on either 'deployments.versions' or 'pipelines' to list the request schedules.

### Response Structure 
A list of details of all request schedules in a project
- `name`: Name of the request 

- `object_type`: Type of object for which the request is made 

- `object_name`: Name of deployment or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 

- `version`: Name of version if type of object is 'deployment' 

- `request_data`: Input data for the request schedule 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled 

- `creation_date`: The date when the request schedule was created

#### Response Examples 
```
[
    {
      "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
      "name": "test-request",
      "object_type": "deployment",
      "object_name": "test-deployment",
      "version": "v1",
      "schedule": "0 * 3 * *",
      "request_data": {
        "input_field_1": 2345,
        "input_field_2": 8765
      },
      "batch": false,
      "timeout": 200",
      "enabled": true,
      "creation_date": "2020-09-16T08:06:34.457679Z"
    }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 

# List request schedules
api_response = api_instance.request_schedules_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ScheduleList]**](ScheduleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_schedules_update**
> ScheduleList request_schedules_update(project_name, schedule_name, data)

Update a request schedule


### Description 
Update a request schedule in a project. Create permissions on the object are necessary for this action.

### Optional Parameters
- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `schedule`: Schedule in crontab format 

- `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary. 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'. 


#### Request Examples 
```
{
  "name": "test-request",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": true,
  "timeout": 360,
  "enabled": false
}
```

### Response Structure 
Details of the updated request schedule
- `name`: Name of the request 

- `object_type`: Type of object for which the request is made 

- `object_name`: Name of deployment or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 

- `version`: Name of version if type of object is 'deployment' 

- `request_data`: Input data for the request schedule 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled 

- `creation_date`: The date when the request schedule was created

#### Response Examples 
```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 360,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
schedule_name = 'schedule_name_example' # str | 
data = ubiops.ScheduleUpdate() # ScheduleUpdate | 

# Update a request schedule
api_response = api_instance.request_schedules_update(project_name, schedule_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **schedule_name** | **str**|  | 
 **data** | [**ScheduleUpdate**](ScheduleUpdate.md)|  | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_create**
> RoleAssignmentList role_assignments_create(project_name, data)

Assign a role to a user in a project


### Description 
Assign a role to a user in the scope of a project. This role can be assigned on either project level or on object level, which can be a deployment or pipeline.
The user making the request must have appropriate permissions.

### Required Parameters 
- `user_id`: Unique identifier for the user (UUID) 

- `role`: Name of the role to be assigned to the user 


### Optional Parameters
- `object_name`: Name of the object for which the role will be assigned 

- `object_type`: Type of the object for which the role will be assigned. It can be project, deployment or pipeline.

**object_name and object_type must be provided together. If neither of them is provided, the role is set on project level.**

#### Request Examples
Setting the role deployment-admin on project level for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363
```
{
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-admin"
}
```

Setting the role deployment-viewer on deployment-1 for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363
```
{
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-viewer",
  "object_name": "deployment-1",
  "object_type": "deployment"
}
```

### Response Structure 
Details of the created role assignment
- `id`: Unique identifier for the role assignment (UUID) 

- `user_id`: Unique identifier for the user (UUID) 

- `role`: Name of the role assigned to the user 

- `object_name`: Name of the object for which the role is assigned 

- `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.

#### Response Examples
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-admin",
  "object_name": "project-1",
  "object_type": "project"
}
```

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-viewer",
  "object_name": "deployment-1",
  "object_type": "deployment"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.RoleAssignmentCreate() # RoleAssignmentCreate | 

# Assign a role to a user in a project
api_response = api_instance.role_assignments_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**RoleAssignmentCreate**](RoleAssignmentCreate.md)|  | 

### Return type

[**RoleAssignmentList**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_delete**
> role_assignments_delete(project_name, id)

Delete a role from a user with the given role assignment id


### Description 
Delete a role of a user. The user making the request must have appropriate permissions. It is possible for a user to delete their own role if they have permissions to do so.


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

# Delete a role from a user with the given role assignment id
api_instance.role_assignments_delete(project_name, id)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_get**
> RoleAssignmentList role_assignments_get(project_name, id)

Get details of a role assignment


### Description 
Get the details of a role assignment of a user. The user making the request must have appropriate permissions.

### Response Structure 
Details of the role assignment
- `id`: Unique identifier for the role assignment (UUID) 

- `user_id`: Unique identifier for the user (UUID) 

- `role`: Name of the role assigned to the user 

- `object_name`: Name of the object for which the role is assigned 

- `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-viewer",
  "object_name": "deployment-1",
  "object_type": "deployment"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

# Get details of a role assignment
api_response = api_instance.role_assignments_get(project_name, id)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RoleAssignmentList**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_per_user_list**
> list[RoleAssignmentList] role_assignments_per_user_list(project_name, user_id)

List the roles assigned to a specific user in a project


### Description 
List the roles assigned to a user in the scope of a project. 

### Response Structure
- `id`: Unique identifier for the role assignment (UUID) 

- `user_id`: Unique identifier for the user (UUID) 

- `role`: Name of the role assigned to the user 

- `object_name`: Name of the object for which the role is assigned 

- `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.

#### Response Examples
```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "role": "deployment-viewer",
    "object_name": "deployment-1",
    "object_type": "deployment"
  },
  {
    "id": "13cf9dd7-7356-4797-b453-e0cb6b416162",
    "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "role": "pipeline-admin",
    "object_name": "pipeline-1",
    "object_type": "pipeline"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
user_id = 'user_id_example' # str | 

# List the roles assigned to a specific user in a project
api_response = api_instance.role_assignments_per_user_list(project_name, user_id)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**list[RoleAssignmentList]**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_create**
> RoleDetailList roles_create(project_name, data)

Create a custom role scoped in a project


### Description 
Create a custom role in the scope of a project. This role is not accessible from other projects. 
The user making the request must have appropriate permissions.

### Required Parameters 
- `name`: Name of the role which will be created. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `permissions`: A list of permissions which the role will contain. The list of available permissions can be obtained with */permissions* endpoint. 


#### Request Examples
```
{
  "name": "custom-deployment-editor-role",
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```

### Response Structure 
Details of the created role
- `id`: Unique identifier for the created role (UUID) 

- `name`: Name of the created role 

- `default`: A boolean value that indicates whether the role is a default role or not 

- `permissions`: A list of permissions which the role contains

#### Response Examples
```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "custom-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.RoleCreate() # RoleCreate | 

# Create a custom role scoped in a project
api_response = api_instance.roles_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**RoleCreate**](RoleCreate.md)|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_delete**
> roles_delete(project_name, role_name)

Delete a role from a project


### Description 
Delete a role from a project. The user making the request must have appropriate permissions.
**Default roles cannot be deleted.**


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 

# Delete a role from a project
api_instance.roles_delete(project_name, role_name)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_get**
> RoleDetailList roles_get(project_name, role_name)

Get details of a role


### Description 
Get the details of a role. The user making the request must have appropriate permissions.

### Response Structure
Details of the role
- `id`: Unique identifier for the role (UUID) 

- `name`: Name of the role 

- `default`: A boolean value that indicates whether the role is a default role or not 

- `permissions`: A list of permissions which the role contains

#### Response Examples
```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "custom-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 

# Get details of a role
api_response = api_instance.roles_get(project_name, role_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_list**
> list[RoleList] roles_list(project_name)

List the available roles in a project


### Description 
List the roles available in the scope of a project. Information on which permissions each role contains, can be obtained with a call to get details of a single role.

### Response Structure
- `id`: Unique identifier for the role (UUID) 

- `name`: Name of the role 

- `default`: A boolean value that indicates whether the role is a default role or not 


#### Response Examples
```
[
  {
    "id": "34e53855-9b50-47bc-b516-6cb971b1949c",
    "name": "project-admin",
    "default": true
  },
  {
    "id": "00132911-b5dd-4017-b399-85f3ffd2a7c3",
    "name": "project-editor",
    "default": true
  },
  {
    "id": "bf0d5823-8062-40f6-bbd2-21bc732f3c3b",
    "name": "project-viewer",
    "default": true
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 

# List the available roles in a project
api_response = api_instance.roles_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[RoleList]**](RoleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_update**
> RoleDetailList roles_update(project_name, role_name, data)

Update a role in a project


### Description 
Update a role in a project. The user making the request must have appropriate permissions.
**Default roles cannot be updated.**

### Optional Parameters 
- `name`: New name for the role. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `permissions`: A new list of permissions which the role will contain. The previous permissions will be replaced with the given ones. The list of available permissions can be obtained with */permissions* endpoint. 


#### Request Examples
```
{
  "name": "new-deployment-editor-role",
  "permissions": [
    "deployments.list",
    "deployments.get"
  ]
}
```

### Response Structure 
Details of the updated role
- `id`: Unique identifier for the role (UUID) 

- `name`: Name of the updated role 

- `default`: A boolean value that indicates whether the role is a default role or not 

- `permissions`: A list of permissions which the role contains

#### Response Examples
```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "new-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 
data = ubiops.RoleUpdate() # RoleUpdate | 

# Update a role in a project
api_response = api_instance.roles_update(project_name, role_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 
 **data** | [**RoleUpdate**](RoleUpdate.md)|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_status**
> Status service_status()

Service status


### Description
Request the API status. It can be used to determine whether the API is online. You do not have to be authenticated to access this method.

### Response Structure
- `status`: API status, either ok or fail. The database connection is tested at each status request, to make sure that the API is online.

#### Response Examples
```	
{
  "status": "ok"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# Service status
api_response = api_instance.service_status()
print(api_response)

# Close the connection
api_client.close()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_create**
> ServiceUserDetail service_users_create(project_name, data)

Create a new service user


### Description 
Create a new service user. A unique email is generated for the service user. Additionally, a token for this service user is generated. This token can be used to authorize requests sent to our API. 

The token is **ONLY** returned on creation and will not be accessible afterwards.

### Optional Parameters
- `name`: Name of the service user 


#### Request Examples 
```
{
  "name": "service-user-1"
}
```

### Response Structure 
Details of the created service user
- `id`: Unique identifier for the service user (UUID) 

- `email`: Email of the service user  

- `token`: The API token for the created service user  

- `name`: Name of the service user 

- `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81",
  "name": "service-user-1",
  "creation_date": "2020-03-24T09:16:27.504+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
data = ubiops.ServiceUserCreate() # ServiceUserCreate | 

# Create a new service user
api_response = api_instance.service_users_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ServiceUserCreate**](ServiceUserCreate.md)|  | 

### Return type

[**ServiceUserDetail**](ServiceUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_delete**
> service_users_delete(project_name, service_user_id)

Delete service user


### Description 
Delete a service user from a project


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 

# Delete service user
api_instance.service_users_delete(project_name, service_user_id)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_get**
> ServiceUserList service_users_get(project_name, service_user_id)

Retrieve details of a service user


### Description 
Retrieve details of a service user

### Response Structure 
Details of the service user
- `id`: Unique identifier for the service user (UUID) 

- `email`: Email of the service user  

- `name`: Name of the service user 

- `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 

# Retrieve details of a service user
api_response = api_instance.service_users_get(project_name, service_user_id)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

[**ServiceUserList**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_list**
> list[ServiceUserList] service_users_list(project_name)

List service users


### Description 
List service users defined in a project

### Response Structure 
List of details of the service users:
- `id`: Unique identifier for the service user (UUID) 

- `email`: Email of the service user 

- `name`: Name of the service user 

- `creation_date`: Date when the service user was created

#### Response Examples 
```
[
  {
    "id": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed",
    "email": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed.project1@serviceuser.ubiops.com",
    "name": "service-user-1",
    "creation_date": "2020-03-24T09:16:27.504+00:00"
  },
  {
    "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
    "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
    "name": "service-user-2",
    "creation_date": "2020-03-26T12:18:43.123+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 

# List service users
api_response = api_instance.service_users_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ServiceUserList]**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_token**
> ServiceUserTokenList service_users_token(project_name, service_user_id, data)

Reset the token of a service user


### Description 
Reset the token of a service user. The old token will be deleted and a new one will be created for the service user. No data should be sent in the body of the request.

### Response Structure 
Details of the new token for the service user
- `token`: The new API token for the service user

#### Response Examples
```
{
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 
data = None # object | 

# Reset the token of a service user
api_response = api_instance.service_users_token(project_name, service_user_id, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**ServiceUserTokenList**](ServiceUserTokenList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_update**
> ServiceUserList service_users_update(project_name, service_user_id, data)

Update service user details

 
### Description
Update the name of a service user

### Optional Parameters
- `name`: Name of the service user 


#### Request Examples 

```
{
  "name": "new-service-user-name",
}
```

### Response Structure 
Details of the updated service user
- `id`: Unique identifier for the service user (UUID) 

- `email`: Email of the service user  

- `name`: Name of the service user 

- `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 
data = ubiops.ServiceUserCreate() # ServiceUserCreate | 

# Update service user details
api_response = api_instance.service_users_update(project_name, service_user_id, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 
 **data** | [**ServiceUserCreate**](ServiceUserCreate.md)|  | 

### Return type

[**ServiceUserList**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> UserPendingDetail user_create(data)

Create a new user


### Description 
Create a new user with the given details - email, password, name and surname. After creation, an email is send to the email address to activate the acount.
The user is required to accept the terms and conditions. The password needs to be at least 8 characters long.

### Required Parameters
- `email`: Email of the user. This is a unique field. 

- `password`: Password of the user 

- `terms_conditions`: Boolean field. Pass True to accept terms and conditions. 


### Optional Parameters
- `name`: Name of the user 

- `surname`: Surname of the user 

- `newsletter`: Boolean field. Pass True to subscribe to the newsletters. 


#### Request Examples 
```
{
  "email": "test@example.com",
  "password": "secret-password",
  "name": "User name",
  "surname": "User surname",
  "terms_conditions": true,
  "newsletter": false
}
```

```
{
  "email": "test@example.com",
  "password": "secret-password",
  "terms_conditions": true,
  "newsletter": false

}
```

### Response Structure 
Details of the created user
 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 

#### Response Examples 
```
{
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

data = ubiops.UserPendingCreate() # UserPendingCreate | 

# Create a new user
api_response = api_instance.user_create(data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserPendingCreate**](UserPendingCreate.md)|  | 

### Return type

[**UserPendingDetail**](UserPendingDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete()

Delete user


### Description 
Delete the user that makes the request


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# Delete user
api_instance.user_delete()

# Close the connection
api_client.close()
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_environment_variables_copy**
> list[InheritedEnvironmentVariableList] version_environment_variables_copy(project_name, deployment_name, version, data)

Copy version environment variable


### Description
Copy existing environment variables from a source object to the version. Variables of the version with the same name as ones from the source object will be overwritten with the new value. Only the copied variables are returned.

### Required Parameters
- `source_deployment`: The name of the deployment from which the variables will be copied

### Optional Parameters
- `source_version`: The version of the object from which the variables will be copied

#### Request Examples
Copy the environment variables from a deployment
```
{
  "source_deployment": "example-deployment"
}
```

Copy the environment variables from a version
```
{
  "source_deployment": "example-deployment",
  "source_version": "v1"
}
```

### Response Structure 
A list of the copied variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from. Will be null for copied environment variables.
- `inheritance_name`: Name of the parent object that this variable is inherited from. Will be null for copied environment variables.

#### Response Examples 
```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "version_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": null,
    "inheritance_name": null
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
data = ubiops.EnvironmentVariableCopy() # EnvironmentVariableCopy | 

# Copy version environment variable
api_response = api_instance.version_environment_variables_copy(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**EnvironmentVariableCopy**](EnvironmentVariableCopy.md)|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_environment_variables_create**
> EnvironmentVariableList version_environment_variables_create(project_name, deployment_name, version, data)

Create version environment variable


### Description
Create an environment variable for the version. Variables inherited from the project or deployment can be shadowed by creating a variable with the same name.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "version_variable",
  "value": "another one",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "version_variable",
  "value": "another one",
  "secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

# Create version environment variable
api_response = api_instance.version_environment_variables_create(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_environment_variables_delete**
> version_environment_variables_delete(project_name, deployment_name, id, version)

Delete version environment variable


### Description
Delete an environment variable of a version


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
id = 'id_example' # str | 
version = 'version_example' # str | 

# Delete version environment variable
api_instance.version_environment_variables_delete(project_name, deployment_name, id, version)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **id** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_environment_variables_get**
> EnvironmentVariableList version_environment_variables_get(project_name, deployment_name, id, version)

Get version environment variable


### Description
Retrieve details of a version environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
id = 'id_example' # str | 
version = 'version_example' # str | 

# Get version environment variable
api_response = api_instance.version_environment_variables_get(project_name, deployment_name, id, version)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **id** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_environment_variables_list**
> list[InheritedEnvironmentVariableList] version_environment_variables_list(project_name, deployment_name, version)

List version environment variables


### Description
List the environment variables defined for the version. Includes environment variables defined at project level and deployment level.
 
### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `deployment`, or null if the variable was defined for the version directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be null if the variable was defined for the version directly

#### Response Examples 
```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "version_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "deployment",
    "inheritance_name": "deployment_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 

# List version environment variables
api_response = api_instance.version_environment_variables_list(project_name, deployment_name, version)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_environment_variables_update**
> EnvironmentVariableList version_environment_variables_update(project_name, deployment_name, id, version, data)

Update version environment variable


### Description
Update an environment variable for the version. This cannot be used to update inherited variables; to change an inherited variable for a specific version you can create a variable with the same name for the version.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

#### Request Examples
```
{
  "name": "version_variable",
  "value": "yet another one",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "version_variable",
  "value": "yet another one",
  "secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
id = 'id_example' # str | 
version = 'version_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

# Update version environment variable
api_response = api_instance.version_environment_variables_update(project_name, deployment_name, id, version, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **id** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_create**
> VersionList versions_create(project_name, deployment_name, data)

Create versions


### Description 
Create a version for a deployment

### Required Parameters 
- `version`: Name of the version of the deployment

### Optional Parameters 
- `language`: Language in which the version is provided. It can be python3.5, python3.6, python3.7 or python3.8. The default value is python3.7
- `memory_allocation`: Reserved memory for the version in MB. This value determines the memory allocated to the version: it should to be enough to encompass the deployment file and all requirements that need to be installed. The default value is 2048. The minimum and maximum values are 256 and 32768 respectively.
- `maximum_instances`: Upper bound of number of versions running. The default value is 5, the maximum value is 20. *Indicator of resource capacity:* if many deployment requests need to be handled in a short time, this number can be set higher to avoid long waiting times.
- `minimum_instances`: Lower bound of number of versions running. The default value is 0. Set this value greater than 0 to always have a always running version.
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped. The default value is 300, the minimum value is 10 and the maximum value is 3600. A high value means that the version stays active longer. Sending requests to a running version means that it will be already initialized and thus take a shorter timer. 

- `description`: Description for the version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

If the time that a request takes does not matter, keep the default values.

#### Request Examples 
```
{
  "version": "version-1",
  "language": "python3.6"
}
```
 
```
{
  "version": "version-1",
  "language": "python3.5",
  "memory_allocation": 512
}
```
 
```
{
  "version": "version-1",
  "maximum_instances": 4,
  "minimum_instances": 1
}
```

### Response Structure 
Details of the created version
- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `language`: Language in which the version is provided
- `memory_allocation`: Reserved memory for the version in MB  
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `description`: Description of the version
- `status`: The state of the version. It is set to *initialised* state on creation.
- `error_message`: The error message which explains why the version has failed building or deployment. It is empty if the version is available.
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `file_last_updated`: The date when a deployment file was last uploaded

#### Response Examples 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "language": "python3.5",
  "description": "",
  "status": "initialised",
  "error_message": "",
  "memory_allocation": 512,
  "maximum_instances": 5,
  "minimum_instances": 0,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z",
  "file_last_updated": "2020-05-12T16:23:15.456812Z",
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
data = ubiops.VersionCreate() # VersionCreate | 

# Create versions
api_response = api_instance.versions_create(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **data** | [**VersionCreate**](VersionCreate.md)|  | 

### Return type

[**VersionList**](VersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_delete**
> versions_delete(project_name, deployment_name, version)

Delete version

 
### Description 
Delete a deployment version. If the version is referenced from a pipeline, it cannot be deleted, it must be removed from the pipeline first.


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 

# Delete version
api_instance.versions_delete(project_name, deployment_name, version)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_file_download**
> file versions_file_download(project_name, deployment_name, version)

Download deployment files


### Description 
Download the deployment file of a version of a deployment

### Response Structure 
 - `file`: Deployment file of the version


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 

# Download deployment files
with api_instance.versions_file_download(project_name, deployment_name, version) as response:
    filename = response.getfilename()
    content = response.read()

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

**file**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_file_upload**
> Success versions_file_upload(project_name, deployment_name, version, file)

Upload deployment files


### Description 
Upload a file for a deployment version. This file should contain the deployment that will be run. It should be provided as a zip and a template can be found on https://github.com/UbiOps/deployment-template. The file is saved under a directory in the storage specified in the settings.

### Required Parameters
- `file`: Deployment file

### Response Structure
- `success`: Boolean indicating whether the deployment file upload succeeded or not



### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
file = '/path/to/file' # file | 

# Upload deployment files
api_response = api_instance.versions_file_upload(project_name, deployment_name, version, file)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**Success**](Success.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_get**
> VersionList versions_get(project_name, deployment_name, version)

Get version


### Description 
Retrieve details of a version of a deployment in a project

### Response Structure 
Details of a version
- `id`: Unique identifier for the version (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `language`: Language in which the version is provided
- `memory_allocation`: Reserved memory for the version in MB 
- `maximum_instances`: Upper bound of number of deployment pods running in parallel
- `minimum_instances`: Lower bound of number of deployment pods running in parallel
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `description`: Description of the version
- `status`: The state of the version
- `error_message`: The error message which explains why the version has failed building or deployment. It is empty if the version is available.
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `file_last_updated`: The date when a deployment file was last uploaded

#### Response Examples
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "memory_allocation": 512,
  "language": "python3.7",
  "description": "",
  "status": "active",
  "error_message": "",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "file_last_updated": "2020-06-23T11:17:28.128652Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 

# Get version
api_response = api_instance.versions_get(project_name, deployment_name, version)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**VersionList**](VersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_list**
> list[VersionList] versions_list(project_name, deployment_name, labels=labels)

List versions


### Description 
Versions can be filtered according to the labels they have by giving labels as a query parameter. Versions that have at least one of the labels on which is filtered, are returned.

### Optional Parameters
- `labels`: Filter on labels of the version. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure 
A list of details of the versions
- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `language`: Language in which the version is provided
- `memory_allocation`: Reserved memory usage for the version in MB
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `description`: Description of the version
- `status`: The state of the version
- `error_message`: The error message which explains why the version has failed building or deployment. It is empty if the version is available.
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `file_last_updated`: The date when a deployment file was last uploaded

#### Response Examples
```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "deployment": "deployment-1",
    "version": "version-1",
    "language": "python3.5",
    "description": "",
    "status": "active",
    "error_message": "",
    "memory_allocation": 512,
    "maximum_instances": 4,
    "minimum_instances": 1,
    "maximum_idle_time": 10,
    "labels": {
      "type": "version"
    },
    "creation_date": "2020-06-18T08:32:14.876451Z",
    "last_updated": "2020-06-19T10:52:23.124784Z",
    "file_last_updated": "2020-06-19T10:52:23.124784Z"
  },
  {
    "id": "24f6b80a-08c3-4d52-ac1a-2ea7e70f16a6",
    "deployment": "deployment-1",
    "version": "version-2",
    "language": "python3.6",
    "description": "",
    "status": "active",
    "error_message": "",
    "memory_allocation": 256,
    "maximum_instances": 5,
    "minimum_instances": 0,
    "maximum_idle_time": 10,
    "labels": {
      "type": "version"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "file_last_updated": "2020-06-23T11:17:28.128652Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
labels = 'labels_example' # str |  (optional)

# List versions
api_response = api_instance.versions_list(project_name, deployment_name, labels=labels)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **labels** | **str**|  | [optional] 

### Return type

[**list[VersionList]**](VersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_update**
> VersionList versions_update(project_name, deployment_name, version, data)

Update version


### Description 
Update a version of a deployment in a project. Updating the language field will cause the deployment to be build again. All necessary fields are validated again. When updating labels, the labels will replace the existing value for labels. 

### Optional Parameters 
- `version`: New name for the version
- `language`: New language for the version
- `memory_allocation`: New reserved memory for the version in MB
- `maximum_instances`: New upper bound of number of versions running
- `minimum_instances`: New lower bound of number of versions running
- `maximum_idle_time`: New maximum time in seconds a version stays idle before it is stopped
- `description`: New description for the version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.

#### Request Examples 
```
{
  "version": "new-version"
}
```
 
```
{
  "memory_allocation": 512,
  "maximum_instances": 4,
  "minimum_instances": 1
}
```

### Response Structure 
Details of the updated version
- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `language`: Language in which the version is provided
- `memory_allocation`: Reserved memory for the version in MB
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `description`: Description of the version
- `status`: The state of the version
- `error_message`: The error message which explains why the version has failed building or deployment. It is empty if the version is available.
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `file_last_updated`: The date when a deployment file was last uploaded

#### Response Examples 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "language": "python3.5",
  "description": "",
  "status": "active",
  "error_message": "",
  "memory_allocation": 512,
  "maximum_instances": 4,
  "minimum_instances": 1,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-23T18:04:76.123754Z",
  "file_last_updated": "2020-06-23T11:17:28.128652Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
import ubiops
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str | 
deployment_name = 'deployment_name_example' # str | 
version = 'version_example' # str | 
data = ubiops.VersionCreate() # VersionCreate | 

# Update version
api_response = api_instance.versions_update(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **deployment_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**VersionCreate**](VersionCreate.md)|  | 

### Return type

[**VersionList**](VersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

