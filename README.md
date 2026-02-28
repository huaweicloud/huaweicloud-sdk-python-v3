English | [简体中文](./README_CN.md)

<p align="center">
<a href="https://www.huaweicloud.com/"><img width="450px" height="102px" src="https://console-static.huaweicloud.com/static/authui/20210202115135/public/custom/images/logo-en.svg"></a>
</p>

<h1 align="center">Huawei Cloud Python Software Development Kit (Python SDK)</h1>

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/huaweicloudsdkcore)](https://www.python.org/)
[![PyPI Version](https://img.shields.io/pypi/v/huaweicloudsdkcore?color=009999)](https://pypi.org/search/?q=huaweicloudsdk)
[![License](https://img.shields.io/badge/license-Apache--2.0-green)](https://www.apache.org/licenses/LICENSE-2.0)

The Huawei Cloud Python SDK allows you to easily work with Huawei Cloud services such as Elastic Compute Service (ECS)
and Virtual Private Cloud (VPC) without the need to handle API related tasks.

This document introduces how to obtain and use Huawei Cloud Python SDK.

## Requirements

- To use Huawei Cloud Python SDK, you must have Huawei Cloud account as well as the Access Key (AK) and Secret key (SK) of the
  Huawei Cloud account. You can create an Access Key in the Huawei Cloud console. For more information,
  see [My Credentials](https://support.huaweicloud.com/en-us/usermanual-ca/en-us_topic_0046606340.html).

- To use Huawei Cloud Python SDK to access the APIs of specific service, please make sure you do have activated the
  service in [Huawei Cloud console](https://console.huaweicloud.com/?locale=en-us) if needed.

- Huawei Cloud Python SDK requires **Python 3.6** or later, run command `python --version` to check the version of Python.

## Install Python SDK

You could use **pip** or **source code** to install dependencies.

You can get the SDK version information through [SDK center](https://console-intl.huaweicloud.com/apiexplorer/#/sdkcenter?language=Python) or [PYPI](https://pypi.org/search/?q=huaweicloudsdk).

### Individual Cloud Service

Take using VPC SDK for example, you need to install `huaweicloudsdkvpc` library:

- Use python pip

```bash
# Install the VPC management library
pip install huaweicloudsdkvpc
```

- Install from source code

```bash
# Install the VPC management library
cd huaweicloudsdkvpc-${version}
python setup.py install
```

### Cloud Service Collection Package

You can install `huaweicloudsdkall`, which will install all SDK supported service packages:

- Use python pip

```bash
pip install huaweicloudsdkall
```

- Install from source code

```bash
cd huaweicloudsdkall-${version}
python setup.py install
```

## Code example

- The following example shows how to query a list of VPC in a specific region, you need to substitute your
  real `{Service}Client` for `VpcClient` in actual use.
- Hard-coding ak and sk for authentication into the code has a great security risk. It is recommended to store the ciphertext in the profile or environment variables and decrypt it when used to ensure security.
- In this example, ak and sk are stored in environment variables. Please configure the environment variables `HUAWEICLOUD_SDK_AK` and `HUAWEICLOUD_SDK_SK` before running this example.

**Simplified Demo**

```python
# coding: utf-8

import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkvpc.v2 import ListVpcsRequest, VpcClient
from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion
from huaweicloudsdkcore.exceptions import exceptions

if __name__ == "__main__":
    # Configure authentication
    # Do not hard-code authentication information into the code, as this may pose a security risk
    # Authentication can be configured through environment variables and other methods. Please refer to Chapter 2.4 Authentication Management
    credentials = BasicCredentials(os.getenv("HUAWEICLOUD_SDK_AK"), os.getenv("HUAWEICLOUD_SDK_SK"))

    # Create a service client
    client = VpcClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(VpcRegion.value_of("cn-north-4")) \
        .build()
    
    # Send the request and get the response
    try:
        request = ListVpcsRequest()
        response = client.list_vpcs(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
```

**Detailed Demo**

```python
# coding: utf-8

import os
import logging

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.http_handler import HttpHandler
from huaweicloudsdkvpc.v2 import VpcClient, ListVpcsRequest
from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion
from huaweicloudsdkcore.exceptions import exceptions

if __name__ == "__main__":
    # Configure authentication
    # Do not hard-code authentication information into the code, as this may pose a security risk
    # Authentication can be configured through environment variables and other methods. Please refer to Chapter 2.4 Authentication Management
    # If project_id is not filled in, the SDK will automatically call the IAM service to query the project id corresponding to the region.
    credentials = BasicCredentials(os.getenv("HUAWEICLOUD_SDK_AK"), os.getenv("HUAWEICLOUD_SDK_SK"), project_id="{your projectId string}") \
            .with_iam_endpoint("https://iam.cn-north-4.myhuaweicloud.com")  # Configure the SDK built-in IAM service endpoint

    # Use default configuration
    http_config = HttpConfig.get_default_config()
    # Configure whether to ignore the SSL certificate verification, default is false
    http_config.ignore_ssl_verification = True
    # Configure CA certificate file
    http_config.ssl_ca_cert = '/path/to/certfile'
    # The default connection timeout is 60 seconds, the default read timeout is 120 seconds
    http_config.timeout = (60, 120)
    # Configure proxy as needed
    # Replace the proxy protocol, host and port in the example according to the actual situation
    http_config.proxy_protocol = 'http'
    http_config.proxy_host = 'proxy.huaweicloud.com'
    http_config.proxy_port = 80
    # Configure the username and password if the proxy requires authentication
    http_config.proxy_user = os.getenv("PROXY_USERNAME")
    http_config.proxy_password = os.getenv("PROXY_PASSWORD")

    # The HTTP handler is used to print the request and response, do not use it in the production environment
    def response_handler(**kwargs):
        response = kwargs.get("response")
        request = response.request

        info = "> Request %s %s HTTP/1.1" % (request.method, request.path_url) + "\n"
        if len(request.headers) != 0:
            info = info + "> Headers:" + "\n"
            for each in request.headers:
                info = info + "    %s: %s" % (each, request.headers[each]) + "\n"
        info = info + "> Body: %s" % request.body + "\n\n"
    
        info = info + "< Response HTTP/1.1 %s " % response.status_code + "\n"
        if len(response.headers) != 0:
            info = info + "< Headers:" + "\n"
            for each in response.headers:
                info = info + "    %s: %s" % (each, response.headers[each],) + "\n"
        info = info + "< Body: %s" % response.content
        print(info)

    http_handler = HttpHandler().add_response_handler(response_handler)

    # Create a service client
    client = (VpcClient.new_builder()
              .with_credentials(credentials)  # Configure authentication
              .with_region(VpcRegion.value_of("cn-north-4"))  # Configure region, it will throw a KeyError if the region does not exist
              .with_http_config(http_config)  # Configure HTTP
              .with_stream_log(log_level=logging.INFO)  # Configure request log output to console
              .with_file_log(path="test.log", log_level=logging.INFO)  # Configure request log output to file
              .with_http_handler(http_handler)  # Configure HTTP handler
              .build())

    # Send the request and get the response
    try:
        request = ListVpcsRequest()
        response = client.list_vpcs(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
```

## Online Debugging

[API Explorer](https://apiexplorer.developer.intl.huaweicloud.com/apiexplorer/overview) provides api retrieval, SDK samples and online debugging, supports full fast retrieval, visual debugging, help document viewing, and online consultation.

## Changelog

Detailed changes for each released version are documented in
the [CHANGELOG.md](https://github.com/huaweicloud/huaweicloud-sdk-python-v3/blob/master/CHANGELOG.md).

## User Manual [:top:](#huawei-cloud-python-software-development-kit-python-sdk)

* [1. Client Configuration](#1-client-configuration-top)
    * [1.1 Default Configuration](#11-default-configuration-top)
    * [1.2 Network Proxy](#12-network-proxy-top)
    * [1.3 Timeout Configuration](#13-timeout-configuration-top)
    * [1.4 SSL Certification](#14-ssl-certification-top)
* [2. Credentials Configuration](#2-credentials-configuration-top)
    * [2.1 Use Temporary AK&SK](#22-use-temporary-aksk-top)
    * [2.2 Use Permanent AK&SK](#21-use-permanent-aksk-top)
    * [2.3 Use IdpId&IdTokenFile](#23-use-idpididtokenfile-top)
    * [2.4 Authentication Management](#24-authentication-management-top)
      * [2.4.1 Environment Variables](#241-environment-variables-top)
	  * [2.4.2 Profile](#242-profile-top)
	  * [2.4.3 Metadata](#243-metadata-top)
	  * [2.4.4 Provider Chain](#244-provider-chain-top)
* [3. Client Initialization](#3-client-initialization-top)
    * [3.1 Initialize the client with specified Endpoint](#31-initialize-the-serviceclient-with-specified-endpoint-top)
    * [3.2 Initialize the client with specified Region (Recommended)](#32-initialize-the-serviceclient-with-specified-region-recommended-top)
    * [3.3 Custom Configuration](#33-custom-configuration-top)
        * [3.3.1 IAM endpoint configuration](#331-iam-endpoint-configuration-top)
        * [3.3.2 Region configuration](#332-region-configuration-top)
    * [3.4 User Agent](#34-user-agent-top)
* [4. Send Requests and Handle Responses](#4-send-requests-and-handle-responses-top)
    * [4.1 Exceptions](#41-exceptions-top)
    * [4.2 Get Response Object](#42-get-response-object-top)
* [5. Use Asynchronous Client](#5-use-asynchronous-client-top)
* [6. Troubleshooting](#6-troubleshooting-top)
    * [6.1 Access Log](#61-access-log-top)
    * [6.2 Original HTTP Listener](#62-original-http-listener-top)
* [7. API Invoker](#7-api-invoker-top)
    * [7.1 Custom request headers](#71-custom-request-headers-top)
    * [7.2 Retry](#72-retry-top)
* [8. Upload and download files](#7-upload-and-download-files-top)
* [9. FAQ](#9-faq-top)
    * [9.1 How to use in Cloud Service Alliance Scenarios](#91-how-to-use-in-cloud-service-alliance-scenarios-top)

### 1. Client Configuration [:top:](#user-manual-top)

#### 1.1 Default Configuration [:top:](#user-manual-top)

```python
from huaweicloudsdkcore.http.http_config import HttpConfig

#  Use default configuration
http_config = HttpConfig.get_default_config()

client = VpcClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

#### 1.2 Network Proxy [:top:](#user-manual-top)

```python
http_config = HttpConfig.get_default_config()
# Use Proxy if needed
# Replace the proxy protocol, host and port in the example according to the actual situation
http_config.proxy_protocol = 'http'
http_config.proxy_host = 'proxy.huaweicloud.com'
http_config.proxy_port = 80
# Configure the username and password if the proxy requires authentication
# In this example, username and password are stored in environment variables. Please configure the environment variables PROXY_USERNAME and PROXY_PASSWORD before running this example.
http_config.proxy_user = os.getenv("PROXY_USERNAME")
http_config.proxy_password = os.getenv("PROXY_PASSWORD")

client = VpcClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

#### 1.3 Timeout Configuration [:top:](#user-manual-top)

```python
http_config = HttpConfig.get_default_config()
# The default connection timeout is 60 seconds, the default read timeout is 120 seconds
# Set the connection timeout and read timeout to 120 seconds
http_config.timeout = 120
# Set the connection timeout to 60 seconds and the read timeout to 120 seconds
http_config.timeout = (60, 120)

client = VpcClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

#### 1.4 SSL Certification [:top:](#user-manual-top)

```python
http_config = HttpConfig.get_default_config()
# Skip SSL certifaction checking while using https protocol if needed
http_config.ignore_ssl_verification = True
# Configure the server's CA certificate for the SDK to verify the legitimacy of the server
http_config.ssl_ca_cert = ssl_ca_cert

client = VpcClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

### 2. Credentials Configuration [:top:](#user-manual-top)

There are two types of Huawei Cloud services, `regional` services and `global` services.

Global services contain BSS, DevStar, EPS, IAM, RMS, TMS.

For `regional` services' authentication, projectId is required to initialize BasicCredentials.

For `global` services' authentication, domainId is required to initialize GlobalCredentials.

The following authentications are supported:

- temporary AK&SK + SecurityToken
- permanent AK&SK
- IdpId&IdTokenFile

#### 2.1 Use Temporary AK&SK [:top:](#user-manual-top)

It's required to obtain temporary AK&SK and security token first, which could be obtained through
permanent AK&SK or through an agency.

- Obtaining a temporary access key and security token through token, you could refer to
document: https://support.huaweicloud.com/en-us/api-iam/iam_04_0002.html . The API mentioned in the document above
corresponds to the method of `CreateTemporaryAccessKeyByToken` in IAM SDK.

- Obtaining a temporary access key and security token through an agency, you could refer to
document: https://support.huaweicloud.com/en-us/api-iam/iam_04_0101.html . The API mentioned in the document above
corresponds to the method of `CreateTemporaryAccessKeyByAgency` in IAM SDK.

**Parameter description**:

- `ak` is the access key ID for your account.
- `sk` is the secret access key for your account.
- `security_token` is the security token when using temporary AK/SK.
- `project_id` is the ID of your project depending on your region which you want to operate.
- `domain_id` is the account ID of Huawei Cloud.

After the temporary AK&SK&SecurityToken is successfully obtained, you can use the following example to initialize the authentication:

```python
# Regional services
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
security_token = os.getenv("HUAWEICLOUD_SDK_SECURITY_TOKEN")
project_id = "{your projectId string}"

basic_credentials = BasicCredentials(ak, sk, project_id).with_security_token(security_token)

# Global services
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
security_token = os.getenv("HUAWEICLOUD_SDK_SECURITY_TOKEN")
domain_id = "{your domainId string}"

global_credentials = GlobalCredentials(ak, sk, domain_id).with_security_token(security_token)
```

#### 2.2 Use Permanent AK&SK [:top:](#user-manual-top)

> ⚠️The Huawei Cloud main account is for administrators and has full access to resources and cloud services. If the AK and SK are leaked, it will pose a significant information security risk to the system; therefore, their use is not recommended.
> It is recommended to use the AK and SK of a minimally authorized IAM user. For details about how to use IAM securely, please refer to the [Best Practices for Using IAM](https://support.huaweicloud.com/intl/en-us/bestpractice-iam/iam_0426.html).

**Parameter description**:

- `ak` is the access key ID for your account.
- `sk` is the secret access key for your account.
- `project_id` is the ID of your project depending on your region which you want to operate.
- `domain_id` is the account ID of Huawei Cloud.

```python
# Regional services
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
project_id = "{your projectId string}"

basic_credentials = BasicCredentials(ak, sk, project_id)

# Global services
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
domain_id = "{your domainId string}"

global_credentials = GlobalCredentials(ak, sk, domain_id)
```

**Notice**:

- project_id/domain_id supports **automatic acquisition** in version `3.0.26-beta` or later, if you want to use this
  feature, you need to provide the ak and sk of your account and the id of the region, and then build your client
  instance with method `with_region()`, detailed example could refer
  to [3.2 Initialize the client with specified Region](#32-initialize-the-serviceclient-with-specified-region-recommended-top).

#### 2.3 Use IdpId&IdTokenFile [:top:](#user-manual-top)

Obtain a federated identity authentication token using an OpenID Connect ID token, refer to the [Obtaining a Token with an OpenID Connect ID Token](https://support.huaweicloud.com/intl/en-us/api-iam/iam_13_0605.html)

**Parameter description**:

- `idp_id` Identity provider ID.
- `id_token_file` Id token file path. Id token is constructed by the enterprise IdP to carry the identity information of federated users.
- `project_id` is the ID of your project depending on your region which you want to operate.
- `domain_id` is the account ID of Huawei Cloud.

```python
from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials

# Regional service
basic_cred = BasicCredentials() \
    .with_idp_id(idp_id) \
    .with_id_token_file(id_token_file) \
    .with_project_id(project_id)

# Global service
global_cred = GlobalCredentials() \
    .with_idp_id(idp_id) \
    .with_id_token_file(id_token_file) \
    .with_domain_id(domain_id)
```

#### 2.4 Authentication Management [:top:](#user-manual-top)

Getting Authentication from providers is supported since `v3.0.98`

**Regional services** use `XxxCredentialProvider.get_basic_credential_xxx_provider`

**Global services** use `XxxCredentialProvider.get_global_credential_xxx_provider`

##### 2.4.1 Environment Variables [:top:](#user-manual-top)

**AK/SK Auth**

| Environment Variables  |  Notice |
| ------------ | ------------ |
| HUAWEICLOUD_SDK_AK  | Required, AccessKey  |
| HUAWEICLOUD_SDK_SK  |  Required, SecretKey |
| HUAWEICLOUD_SDK_SECURITY_TOKEN  | Optional, this parameter needs to be specified when using temporary ak/sk  |
| HUAWEICLOUD_SDK_PROJECT_ID  | Optional, used for regional services, required in multi-ProjectId scenarios  |
| HUAWEICLOUD_SDK_DOMAIN_ID  | Optional, used for global services  |

Configure environment variables:

```
// Linux
export HUAWEICLOUD_SDK_AK=YOUR_AK
export HUAWEICLOUD_SDK_SK=YOUR_SK

// Windows
set HUAWEICLOUD_SDK_AK=YOUR_AK
set HUAWEICLOUD_SDK_SK=YOUR_SK
```

Get the credentials from configured environment variables:

```python
from huaweicloudsdkcore.auth.provider import EnvCredentialProvider

# basic
basic_provider = EnvCredentialProvider.get_basic_credential_env_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = EnvCredentialProvider.get_global_credential_env_provider()
global_cred = global_provider.get_credentials()
```

**IdpId/IdTokenFile Auth**

| Environment Variables  |  Notice |
| ------------ | ------------ |
| HUAWEICLOUD_SDK_IDP_ID  | Required, identity provider Id |
| HUAWEICLOUD_SDK_ID_TOKEN_FILE  |  Required, id token file path |
| HUAWEICLOUD_SDK_PROJECT_ID  | For basic credentials, this parameter is required  |
| HUAWEICLOUD_SDK_DOMAIN_ID  | For global credentials, this parameter is required  |

Configure environment variables:

```
// Linux
export HUAWEICLOUD_SDK_IDP_ID=YOUR_IDP_ID
export HUAWEICLOUD_SDK_ID_TOKEN_FILE=/some_path/your_token_file
export HUAWEICLOUD_SDK_PROJECT_ID=YOUR_PROJECT_ID // For basic credentials, this parameter is required
export HUAWEICLOUD_SDK_DOMAIN_ID=YOUR_DOMAIN_ID // For global credentials, this parameter is required

// Windows
set HUAWEICLOUD_SDK_IDP_ID=YOUR_IDP_ID
set HUAWEICLOUD_SDK_ID_TOKEN_FILE=/some_path/your_token_file
set HUAWEICLOUD_SDK_PROJECT_ID=YOUR_PROJECT_ID // For basic credentials, this parameter is required
set HUAWEICLOUD_SDK_DOMAIN_ID=YOUR_DOMAIN_ID // For global credentials, this parameter is required
```

Get the credentials from configured environment variables:

```python
from huaweicloudsdkcore.auth.provider import EnvCredentialProvider

# basic
basic_provider = EnvCredentialProvider.get_basic_credential_env_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = EnvCredentialProvider.get_global_credential_env_provider()
global_cred = global_provider.get_credentials()
```

##### 2.4.2 Profile [:top:](#user-manual-top)

The profile will be read from the user's home directory by default, linux`~/.huaweicloud/credentials`,windows`C:\Users\USER_NAME\.huaweicloud\credentials`, the path to the profile can be modified by configuring the environment variable `HUAWEICLOUD_SDK_CREDENTIALS_FILE`

**AK/SK Auth**

| Configuration Parameters  |  Notice |
| ------------ | ------------ |
| ak  | Required, AccessKey  |
| sk  |  Required, SecretKey |
| security_token  | Optional, this parameter needs to be specified when using temporary ak/sk  |
| project_id  | Optional, used for regional services, required in multi-ProjectId scenarios  |
| domain_id  | Optional, used for global services  |
| iam_endpoint  | optional, endpoint for authentication, default is `https://iam.myhuaweicloud.com` |

The content of the profile is as follows:

```ini
[basic]
ak = your_ak
sk = your_sk

[global]
ak = your_ak
sk = your_sk
```

Get the credentials from profile:

```python
from huaweicloudsdkcore.auth.provider import ProfileCredentialProvider

# basic
basic_provider = ProfileCredentialProvider.get_basic_credential_profile_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = ProfileCredentialProvider.get_global_credential_profile_provider()
global_cred = global_provider.get_credentials()
```

**IdpId/IdTokenFile Auth**

| Configuration Parameters  |  Notice |
| ------------ | ------------ |
| idp_id  | Required, identity provider Id |
| id_token_file  |  Required, id token file path |
| project_id  | For basic credentials, this parameter is required  |
| domain_id  | For global credentials, this parameter is required  |
| iam_endpoint  | optional, endpoint for authentication, default is `https://iam.myhuaweicloud.com` |

The content of the profile is as follows:

```ini
[basic]
idp_id = your_idp_id
id_token_file = /some_path/your_token_file
project_id = your_project_id

[global]
idp_id = your_idp_id
id_token_file = /some_path/your_token_file
domainId = your_domain_id
```

Get the credentials from profile:

```python
from huaweicloudsdkcore.auth.provider import ProfileCredentialProvider

# basic
basic_provider = ProfileCredentialProvider.get_basic_credential_profile_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = ProfileCredentialProvider.get_global_credential_profile_provider()
global_cred = global_provider.get_credentials()
```

##### 2.4.3 Metadata [:top:](#user-manual-top)

Get temporary AK/SK and securitytoken from instance's metadata. Refer to the [Obtaining Metadata](https://support.huaweicloud.com/intl/en-us/usermanual-ecs/ecs_03_0166.html) for more information.

Manually obtain authentication from instance metadata:

```python
from huaweicloudsdkcore.auth.provider import MetadataCredentialProvider

# basic
basic_provider = MetadataCredentialProvider.get_basic_credential_metadata_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = MetadataCredentialProvider.get_global_credential_metadata_provider()
global_cred = global_provider.get_credentials()
```

##### 2.4.4 Provider Chain [:top:](#user-manual-top)

When creating a service client without credentials, try to load authentication in the order **Environment Variables -> Profile -> Metadata**

Get authentication from provider chain:

```python
from huaweicloudsdkcore.auth.provider import CredentialProviderChain

# basic
basic_chain = CredentialProviderChain.get_basic_credential_provider_chain()
basic_cred = basic_chain.get_credentials()

# global
global_chain = CredentialProviderChain.get_global_credential_provider_chain()
global_cred = global_chain.get_credentials()
```

Custom credentials provider chain is supported:

```python
from huaweicloudsdkcore.auth.provider import CredentialProviderChain, ProfileCredentialProvider, MetadataCredentialProvider

providers = [
    ProfileCredentialProvider.get_basic_credential_profile_provider(),
    MetadataCredentialProvider.get_basic_credential_metadata_provider()
]

chain = CredentialProviderChain(providers)
credentials = chain.get_credentials()
```

### 3. Client Initialization [:top:](#user-manual-top)

There are two ways to initialize the {Service}Client, you could choose one you preferred.

#### 3.1 Initialize the {Service}Client with specified Endpoint [:top:](#user-manual-top)

```python
# Specify the endpoint, take the endpoint of VPC service in region of cn-north-4 for example
endpoint = "https://vpc.cn-north-4.myhuaweicloud.com"

# Initialize the credentials, you should provide project_id or domain_id in this way, take initializing BasicCredentials for example
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
project_id = "{your projectId string}"
basic_credentials = BasicCredentials(ak, sk, project_id)

# Initialize specified service client instance, take initializing the regional service VPC's VpcClient for example
client = VpcClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()
```

**where:**

- `endpoint` varies by services and regions,
  see [Regions and Endpoints](https://developer.huaweicloud.com/intl/en-us/endpoint) to obtain correct endpoint.

- When you meet some trouble in getting projectId using the specified region way, you could use this way instead.

#### 3.2 Initialize the {Service}Client with specified Region **(Recommended)** [:top:](#user-manual-top)

```python
import os
# dependency for region module
from huaweicloudsdkiam.v3.region.iam_region import IamRegion

# Initialize the credentials, project_id or domain_id could be unassigned in this situation
# Take initializing GlobalCredentials for example
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
global_credentials = GlobalCredentials(ak, sk)

# Initialize specified service client instance
# Take initializing the global service IAM's IamClient for example
client = IamClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(global_credentials) \
    .with_region(IamRegion.CN_NORTH_4) \
    .build()
```

**Notice:**

- If you use {Service}Region to initialize {Service}Client, project_id/domain_id supports automatic acquisition, you
  don't need to configure it when initializing Credentials.

- Multiple ProjectId situation is **not supported**.

- You can query the supported regions through [Regions and Endpoints](https://console-intl.huaweicloud.com/apiexplorer/#/endpoint
). You may get exception such as `Unsupported regionId` if you specify an unsupported region.

**Comparison of the two ways:**

| Initialization | Advantages | Disadvantage |
| :---- | :---- | :---- |
| Specified Endpoint | The API can be invoked successfully once it has been published in the environment. | You need to prepare projectId and endpoint yourself.
| Specified Region | No need for projectId and endpoint, it supports automatic acquisition if you configure it in the right way. | The supported services and regions are limited.

#### 3.3 Custom Configuration [:top:](#user-manual-top)

**Notice:** Supported since v3.0.93

##### 3.3.1 IAM endpoint configuration [:top:](#user-manual-top)

Automatically acquiring projectId/domainId will invoke the [KeystoneListProjects](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=KeystoneListProjects) /[KeystoneListAuthDomains](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=KeystoneListAuthDomains) interface of IAM service.

The endpoint being called will be queried from the [mapping table](./huaweicloud-sdk-core/huaweicloudsdkcore/auth/endpoint.py), and if it cannot be found, the default value **https://iam.myhuaweicloud.com** will be used.

**European station users need to specify the endpoint as https://iam.eu-west-101.myhuaweicloud.eu**, you can modify the endpoint in the following two ways.

###### 3.3.1.1 Global scope [:top:](#user-manual-top)

This configuration takes effect globally, specified by environment variable `HUAWEICLOUD_SDK_IAM_ENDPOINT`

```
//linux
export HUAWEICLOUD_SDK_IAM_ENDPOINT=https://iam.cn-north-4.myhuaweicloud.com

//windows
set HUAWEICLOUD_SDK_IAM_ENDPOINT=https://iam.cn-north-4.myhuaweicloud.com
```

###### 3.3.1.2 Credentials scope [:top:](#user-manual-top)

This configuration is only valid for a credential, and it will override the global configuration

```python
import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials

ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
iam_endpoint = "https://iam.cn-north-4.myhuaweicloud.com"
credentials = BasicCredentials(ak, sk).with_iam_endpoint(iam_endpoint)
```

##### 3.3.2 Region configuration [:top:](#user-manual-top)

###### 3.3.2.1 Code [:top:](#user-manual-top)

```python
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkecs.v2 import EcsClient

# Create a region with custom region id and endpoint
region = Region("cn-north-9", "https://ecs.cn-north-9.myhuaweicloud.com")

client = EcsClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(region) \
    .build()
```

###### 3.3.2.2 Environment variable [:top:](#user-manual-top)

Specified by environment variable, the format is `HUAWEICLOUD_SDK_REGION_{SERVICE_NAME}_{REGION_ID}={endpoint}`

Notice: the name of environment variable is UPPER-CASE, replacing hyphens with underscores.

```
// Take ECS and IoTDA services as examples

// linux
export HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_9=https://ecs.cn-north-9.myhuaweicloud.com
export HUAWEICLOUD_SDK_REGION_IOTDA_AP_SOUTHEAST_1=https://iotda.ap-southwest-1.myhuaweicloud.com

// windows
set HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_9=https://ecs.cn-north-9.myhuaweicloud.com
set HUAWEICLOUD_SDK_REGION_IOTDA_AP_SOUTHEAST_1=https://iotda.ap-southwest-1.myhuaweicloud.com
```

A region corresponding to multiple endpoints is supported since **v3.1.60**, if the main endpoint cannot be connected, it will automatically switch to the backup endpoint.

The format is `HUAWEICLOUD_SDK_REGION_{SERVICE_NAME}_{REGION_ID}={endpoint1},{endpoint2}`, separate multiple endpoints with commas, such as `HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_9=https://ecs.cn-north-9.myhuaweicloud.com,https://ecs.cn-north-9.myhuaweicloud.cn`

###### 3.3.2.3 Profile [:top:](#user-manual-top)

The profile will be read from the user's home directory by default, linux`~/.huaweicloud/regions.yaml`,windows`C:\Users\USER_NAME\.huaweicloud\regions.yaml`,the default file may not exist, but if the file exists and the content format is incorrect, an exception will be thrown for parsing errors.

The path to the profile can be modified by configuring the environment variable `HUAWEICLOUD_SDK_REGIONS_FILE`, like `HUAWEICLOUD_SDK_REGIONS_FILE=/tmp/my_regions.yml`

The file content format is as follows:

```yaml
# Service name is case-insensitive
ECS:
  - id: 'cn-north-1'
    endpoint: 'https://ecs.cn-north-1.myhuaweicloud.com'
  - id: 'cn-north-9'
    endpoint: 'https://ecs.cn-north-9.myhuaweicloud.com'
IoTDA:
  - id: 'ap-southwest-1'
    endpoint: 'https://iotda.ap-southwest-1.myhuaweicloud.com'
```

A region corresponding to multiple endpoints is supported since v3.1.62, if the main endpoint cannot be connected, it will automatically switch to the backup endpoint.

```yaml
ECS:
  - id: 'cn-north-1'
    endpoints:
      - 'https://ecs.cn-north-1.myhuaweicloud.com'
      - 'https://ecs.cn-north-1.myhuaweicloud.cn'
```

###### 3.3.2.4 Region supply chain [:top:](#user-manual-top)

The default lookup order is **environment variables -> profile -> region defined in SDK** of method **Region.value_of(region_id)**, if the region is not found in the above ways, an exception **KeyError**  will be thrown.

```python
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion

region1 = EcsRegion.value_of("cn-north-1")
region2 = EcsRegion.value_of("cn-north-9")
```

#### 3.4 User Agent [:top:](#user-manual-top)

Additional information will be appended to the User-Agent in the request header by default since **v3.1.165**. It is used by service to identify what SDK language, python version, and platform info a client is using to call into their service, and a random identifier will be generated and appended to the User-Agent. The identifier will be stored in the user's home directory, as `~/.huaweicloud/application_id` on Linux and `C:\Users\USER_NAME\.huaweicloud\application_id` on Windows.

The above information will be used to protect the security of your and your users' Huawei Cloud accounts.

You can disable this automatic User-Agent augmentation by explicitly setting a custom User-Agent header value. The value is recommended to be less than 50 characters and should use US-ASCII visible characters:

```python
http_config = HttpConfig.get_default_config()
# Append custom User-Agent information to replace the default
http_config.user_agent = "custom user agent..."

client = IamClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

### 4. Send Requests and Handle Responses [:top:](#user-manual-top)

```python
# Initialize a request and print response, take interface of ListVpcs for example
request = ListVpcsRequest(limit=1)

response = client.list_vpcs(request)
print(response)
```

#### 4.1 Exceptions [:top:](#user-manual-top)

| Level 1 | Notice | Level 2 | Notice |
| :---- | :---- | :---- | :---- |
| ConnectionException | Connection error | HostUnreachableException | Host is not reachable |
| | | SslHandShakeException | SSL certification error |
| RequestTimeoutException | Request timeout | CallTimeoutException | timeout for single request |
| | | RetryOutageException | no response after retrying |
| ServiceResponseException | service response error | ServerResponseException | server inner error, http status code: [500,] |
| | | ClientRequestException | invalid request, http status code: [400? 500) |

```python
# handle exceptions
try:
    request = ListVpcsRequest(limit=1)
    response = client.list_vpcs(request)
    print(response)
except exceptions.ServiceResponseException as e:
    print(e.status_code)
    print(e.request_id)
    print(e.error_code)
    print(e.error_msg)
```

#### 4.2 Get Response Object [:top:](#user-manual-top)

The default response format of each request is `json string`, if you want to obtain the response object, the Python SDK
supports using method `to_json_object()` to get it.

```python
request = ListVpcsRequest(limit=1)
# original response json string
response = client.list_vpcs(request)
print(response)
# response object
response_obj = response.to_json_object()
print(response_obj["vpcs"])
```

**Notice:** This method is only supported in version `3.0.34-rc` or later.

### 5. Use Asynchronous Client [:top:](#user-manual-top)

```python
# Initialize asynchronous client, take VpcAsyncClient for example
client = VpcAsyncClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()

# send asynchronous request
request = ListVpcsRequest(limit=1)
response = client.list_vpcs_async(request)

# get asynchronous response
print(response.result())
```

### 6. Troubleshooting [:top:](#user-manual-top)

SDK supports `Access` log and `Debug` log which could be configured manually.

#### 6.1 Access Log [:top:](#user-manual-top)

SDK supports print access log which could be enabled by manual configuration, the log could be output to the console or
specified files.

Initialize specified service client instance, take VpcClient for example:

```python
client = (VpcClient.new_builder()
          .with_file_log(path="test.log", log_level=logging.INFO)  # Write log files
          .with_stream_log(log_level=logging.INFO)  # Write log to console
          .build())
```

**where:**

- `with_file_log`:
    - `path` means log file path.
    - `log_level` means log level, default is INFO.
    - `max_bytes` means size of single log file, the default value is 10485760 bytes.
    - `backup_count` means count of log file, the default value is 5.
- `with_stream_log`:
    - `stream` means stream object, the default value is sys.stdout.
    - `log_level` means log level, the default value is INFO.

After enabled log, the SDK will print the access log by default, every request will be recorded to the console like:

```text
2020-06-16 10:44:02,019 4568 HuaweiCloud-SDK http_handler.py 28 INFO "GET https://vpc.cn-north-1.myhuaweicloud.com/v1/0904f9e1f100d2932f94c01f9aa1cfd7/vpcs" 200 11 0:00:00.543430 b5c927ffdab8401e772e70aa49972037
```

The format of access log is:

```python
%(asctime)s %(thread)d %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s
```

#### 6.2 Original HTTP Listener [:top:](#user-manual-top)

In some situation, you may need to debug your http requests, original http request and response information will be
needed. The SDK provides a listener function to obtain the original encrypted http request and response information.

> :warning:  Warning: The original http log information is used in debugging stage only, please do not print the original http header or body in the production environment. These log information is not encrypted and contains sensitive data such as the password of your ECS virtual machine, or the password of your IAM user account, etc. When the response body is binary content, the body will be printed as "***" without detailed information.

```python
from huaweicloudsdkcore.http.http_handler import HttpHandler
from huaweicloudsdkvpc.v3 import VpcClient


def response_handler(**kwargs):
    response = kwargs.get("response")
    request = response.request

    info = "> Request %s %s HTTP/1.1" % (request.method, request.path_url) + "\n"
    if len(request.headers) != 0:
        info = info + "> Headers:" + "\n"
        for each in request.headers:
            info = info + "    %s: %s" % (each, request.headers[each]) + "\n"
    info = info + "> Body: %s" % request.body + "\n\n"

    info = info + "< Response HTTP/1.1 %s " % response.status_code + "\n"
    if len(response.headers) != 0:
        info = info + "< Headers:" + "\n"
        for each in response.headers:
            info = info + "    %s: %s" % (each, response.headers[each],) + "\n"
    info = info + "< Body: %s" % response.content
    print(info)


if __name__ == "__main__":
    http_handler = HttpHandler().add_response_handler(response_handler)
    client = VpcClient.new_builder() \
    	.with_http_handler(http_handler) \
        .build()
```

**Notice:**

HttpHandler supports method `add_request_handler` and `add_response_handler`.

### 7. API Invoker [:top:](#user-manual-top)

#### 7.1 Custom request headers [:top:](#user-manual-top)

You can flexibly configure request headers as needed. **Do not** specify common request headers such as `Host`, `Authorization`, `User-Agent`, `Content-Type` unless necessary, as this may cause the errors.

**Sync invoke**

```python
client = VpcClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(VpcRegion.value_of("cn-north-4")) \
    .build()

request = ListVpcsRequest()
# Custom request headers
response = client.list_vpcs_invoker(request) \
    .add_header("key1", "value1") \
    .add_header("key2", "value2") \
    .invoke()
print(response)
```

**Async invoke**

```python
client = VpcAsyncClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(VpcRegion.value_of("cn-north-4")) \
    .build()

request = ListVpcsRequest()
response = client.list_vpcs_async_invoker(request) \
    # Custom request headers
    .add_header("key1", "value1") \
    .add_header("key2", "value2") \
    .invoke().result()
print(response)
```

#### 7.2 Retry [:top:](#user-manual-top)

Retry feature is supported since `v3.1.97`, the following parameters is required:

- retry_condition: whether to retry based on the last response or exception.
- max_retries: maximum number of retries when retry conditions are met, in range [1, 10].
- backoff_strategy: calculate delay(milliseconds) before next retry.

```python
from huaweicloudsdkcore.exceptions.exceptions import ConnectionException, ServerResponseException
from huaweicloudsdkvpc.v2 import ListVpcsRequest
from huaweicloudsdkvpc.v2.vpc_client import VpcClient

from huaweicloudsdkcore.retry.backoff_strategy import BackoffStrategies


client = VpcClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(VpcRegion.value_of("cn-north-4")) \
    .build()

request = ListVpcsRequest()
# Retry on connection exception, max retry times is 3, retry interval strategy is immediate retry.
response = client.list_vpcs_invoker(request).with_retry(
    retry_condition=lambda resp, exc: isinstance(exc, ConnectionException),
    max_retries=3,
    backoff_strategy=BackoffStrategies.NONE
).invoke()

# Retry on server response exception, max retry times is 3, retry interval strategy is equal jitter backoff strategy.
# response = client.list_vpcs_invoker(request).with_retry(
#     retry_condition=lambda resp, exc: isinstance(exc, ServerResponseException) and exc.status_code == 503,
#     max_retries=10,
#     backoff_strategy=BackoffStrategies.EQUAL_JITTER
# ).invoke()
```

### 8. Upload and download files [:top:](#user-manual-top)

Take the interface `CreateImageWatermark` of the service `Data Security Center` as an example, this interface needs to upload an image file and return the watermarked image file stream:

```python
# coding: utf-8

import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.formdata import FormFile
from huaweicloudsdkdsc.v1 import *


def create_image_watermark(client):

    try:
        request = CreateImageWatermarkRequest()
        # Open the file in mode "rb", create a Formfile object.
        image_file = FormFile(open("demo.jpg", "rb"))
        body = CreateImageWatermarkRequestBody(file=image_file, blind_watermark="test_watermark")
        request.body = body
        response = client.create_image_watermark(request)
        image_file.close()

        # Define the method of downloading files.
        def save(stream):
            with open("result.jpg", "wb") as f:
                f.write(stream.content)
        # Download the file.
        response.consume_download_stream(save)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == "__main__":
    ak = os.getenv("HUAWEICLOUD_SDK_AK")
    sk = os.getenv("HUAWEICLOUD_SDK_SK")
    endpoint = "{your endpoint}"
    project_id = "{your project id}"
    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)
    dsc_client = DscClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    create_image_watermark(dsc_client)
```

### 9. FAQ [:top:](#user-manual-top)

#### 9.1 How to use in Cloud Service Alliance Scenarios [:top:](#user-manual-top)

```python
# Specify the endpoint, take the endpoint of VPC service in region of eu-west-101 for example
endpoint = "https://vpc.eu-west-101.myhuaweicloud.com"

# Initialize the credentials, you should provide project_id or domain_id in this way, take initializing BasicCredentials for example
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
project_id = "{your projectId string}"
basic_credentials = BasicCredentials(ak, sk, project_id)

# Initialize specified service client instance, take initializing the regional service VPC's VpcClient for example
client = VpcClient.new_builder() \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()
```