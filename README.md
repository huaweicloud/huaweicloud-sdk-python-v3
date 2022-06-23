English | [简体中文](./README_CN.md)

<p align="center">
<a href="https://www.huaweicloud.com/"><img width="450px" height="102px" src="https://console-static.huaweicloud.com/static/authui/20210202115135/public/custom/images/logo-en.svg"></a>
</p>

<h1 align="center">Huawei Cloud Python Software Development Kit (Python SDK)</h1>

The Huawei Cloud Python SDK allows you to easily work with Huawei Cloud services such as Elastic Compute Service (ECS)
and Virtual Private Cloud (VPC) without the need to handle API related tasks.

This document introduces how to obtain and use Huawei Cloud Python SDK.

## Requirements

- To use Huawei Cloud Python SDK, you must have Huawei Cloud account as well as the Access Key and Secret Key of the
  Huawei Cloud account. You can create an Access Key in the Huawei Cloud console. For more information,
  see [My Credentials](https://support.huaweicloud.com/en-us/usermanual-ca/en-us_topic_0046606340.html).

- To use Huawei Cloud Python SDK to access the APIs of specific service, please make sure you do have activated the
  service in [Huawei Cloud console](https://console.huaweicloud.com/?locale=en-us) if needed.

- Huawei Cloud Python SDK requires **Python 3.3** or later, run command `python --version` to check the version of Python.

## Install Python SDK

You could use **pip** or **source code** to install dependencies.

### Individual Cloud Service

Take using VPC SDK for example, you need to install `huaweicloudsdkcore` library and `huaweicloudsdkvpc` library:

- Use python pip

``` bash
# Install the VPC management library
pip install huaweicloudsdkvpc
```

- Install from source code

``` bash
# Install the VPC management library
cd huaweicloudsdkvpc-${version}
python setup.py install
```

### Cloud Service Collection Package

You can install `huaweicloudsdkall`, which will install all SDK supported service packages:

- Use python pip

``` bash
pip install huaweicloudsdkall
```

- Install from source code

``` bash
cd huaweicloudsdkall-${version}
python setup.py install
```

## Code example

- The following example shows how to query a list of VPC in a specific region, you need to substitute your
  real `{Service}Client` for `VpcClient` in actual use.
- Substitute the values for `{your ak string}`, `{your sk string}`, `{your endpoint string}` and `{your project id}`.

``` python
# coding: utf-8


from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_config import HttpConfig
# import specified service library huaweicloudsdk{service}, take vpc for example
from huaweicloudsdkvpc.v2 import *


def list_vpc(client):
    try:
        request = ListVpcsRequest(limit=1)
        response = client.list_vpcs(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == "__main__":
    ak = "{your ak string}"
    sk = "{your sk string}"
    endpoint = "{your endpoint}"
    project_id = "{your project id}"

    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)

    vpc_client = VpcClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    list_vpc(vpc_client)
```

## Changelog

Detailed changes for each released version are documented in
the [CHANGELOG.md](https://github.com/huaweicloud/huaweicloud-sdk-python-v3/blob/master/CHANGELOG.md).

## User Manual [:top:](#huawei-cloud-python-software-development-kit-python-sdk)

* [1. Client Configuration](#1-client-configuration-top)
    * [1.1  Default Configuration](#11-default-configuration-top)
    * [1.2  Network Proxy](#12-network-proxy-top)
    * [1.3  Connection](#13-connection-top)
    * [1.4  SSL Certification](#14-ssl-certification-top)
* [2. Credentials Configuration](#2-credentials-configuration-top)
    * [2.1  Use Permanent AK&SK](#21-use-permanent-aksk-top)
    * [2.2  Use Temporary AK&SK](#22-use-temporary-aksk-top)
* [3. Client Initialization](#3-client-initialization-top)
    * [3.1  Initialize the client with specified Endpoint](#31-initialize-the-serviceclient-with-specified-endpoint-top)
    * [3.2  Initialize the client with specified Region (Recommended)](#32-initialize-the-serviceclient-with-specified-region-recommended-top)
    * [3.3 Custom Configuration](#33-custom-configuration-top)
        * [3.3.1 IAM endpoint configuration](#331-iam-endpoint-configuration-top)
        * [3.3.2 Region configuration](#332-region-configuration-top)
* [4. Send Requests and Handle Responses](#4-send-requests-and-handle-responses-top)
    * [4.1  Exceptions](#41-exceptions-top)
    * [4.2  Get Response Object](#42-get-response-object-top)
* [5. Use Asynchronous Client](#5-use-asynchronous-client-top)
* [6. Troubleshooting](#6-troubleshooting-top)
    * [6.1 Access Log](#61-access-log-top)
    * [6.2 Original HTTP Listener](#62-original-http-listener-top)
* [7. Upload and download files](#7-upload-and-download-files-top)

### 1. Client Configuration [:top:](#user-manual-top)

#### 1.1 Default Configuration [:top:](#user-manual-top)

``` python
#  Use default configuration
config = HttpConfig.get_default_config()
```

#### 1.2 Network Proxy [:top:](#user-manual-top)

``` python
# Use Proxy if needed
config.proxy_protocol = 'http'
config.proxy_host = 'proxy.huaweicloud.com'
config.proxy_port = 80
config.proxy_user = 'username'
config.proxy_password = 'password'
```

#### 1.3 Connection [:top:](#user-manual-top)

``` python
# The default connection timeout is 60 seconds, the default read timeout is 120 seconds. You could specify a unified timeout by using config.timeout=timeout, or specify timeout separately config.timeout=(connect timeout, read timeout)
config.timeout = 120
```

#### 1.4 SSL Certification [:top:](#user-manual-top)

``` python
# Skip ssl certifaction checking while using https protocol if needed
config.ignore_ssl_verification = True
# Server ca certification if needed
config.ssl_ca_cert = ssl_ca_cert
```

### 2. Credentials Configuration [:top:](#user-manual-top)

There are two types of Huawei Cloud services, `regional` services and `global` services.

Global services contain BSS, DevStar, EPS, IAM, RMS, TMS.

For `regional` services' authentication, projectId is required to initialize BasicCredentials. For `global` services'
authentication, domainId is required to initialize GlobalCredentials.

**Parameter description**:

- `ak` is the access key ID for your account.
- `sk` is the secret access key for your account.
- `project_id` is the ID of your project depending on your region which you want to operate.
- `domain_id` is the account ID of Huawei Cloud.
- `security_token` is the security token when using temporary AK/SK.

#### 2.1 Use Permanent AK&SK [:top:](#user-manual-top)

``` python
# Regional services
basic_credentials = BasicCredentials(ak, sk, project_id)

# Global services
global_credentials = GlobalCredentials(ak, sk, domain_id)
```

**Notice**:

- project_id/domain_id supports **automatic acquisition** in version `3.0.26-beta` or later, if you want to use this
  feature, you need to provide the ak and sk of your account and the id of the region, and then build your client
  instance with method `with_region()`, detailed example could refer
  to [3.2 Initialize the client with specified Region](#32-initialize-the-serviceclient-with-specified-region-recommended-top)
  .

#### 2.2 Use Temporary AK&SK [:top:](#user-manual-top)

It's required to obtain temporary access key, security key and security token first, which could be obtained through
permanent access key and security key or through an agency.

Obtaining a temporary access key token through permanent access key and security key, you could refer to
document: https://support.huaweicloud.com/en-us/api-iam/iam_04_0002.html . The API mentioned in the document above
corresponds to the method of `CreateTemporaryAccessKeyByToken` in IAM SDK.

Obtaining a temporary access key and security token through an agency, you could refer to
document: https://support.huaweicloud.com/en-us/api-iam/iam_04_0101.html . The API mentioned in the document above
corresponds to the method of `CreateTemporaryAccessKeyByAgency` in IAM SDK.

``` python
# Regional services
basic_credentials = BasicCredentials(ak, sk, project_id).with_security_token(security_token)

# Global services
global_credentials = GlobalCredentials(ak, sk, domain_id).with_security_token(security_token)
```

### 3. Client Initialization [:top:](#user-manual-top)

There are two ways to initialize the {Service}Client, you could choose one you preferred.

#### 3.1 Initialize the {Service}Client with specified Endpoint [:top:](#user-manual-top)

``` python
# Specify the endpoint, take the endpoint of VPC service in region of cn-north-4 for example
endpoint = "https://vpc.cn-north-4.myhuaweicloud.com"

# Initialize the credentials, you should provide project_id or domain_id in this way, take initializing BasicCredentials for example
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

``` python
# dependency for region module
from huaweicloudsdkiam.v3.region.iam_region import IamRegion

# Initialize the credentials, project_id or domain_id could be unassigned in this situation, take initializing GlobalCredentials for example
global_credentials = GlobalCredentials(ak, sk)

# initialize specified service client instance, take initializing the global service IAM's IamClient for example
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

- Supported region list: af-south-1, ap-southeast-1, ap-southeast-2, ap-southeast-3, cn-east-2, cn-east-3, cn-north-1,
  cn-north-4, cn-south-1, cn-southwest-2, ru-northwest-2. You may get exception such as `Unsupported regionId` if your
  region don't in the list above.

**Comparison of the two ways:**

| Initialization | Advantages | Disadvantage |
| :---- | :---- | :---- |
| Specified Endpoint | The API can be invoked successfully once it has been published in the environment. | You need to prepare projectId and endpoint yourself.
| Specified Region | No need for projectId and endpoint, it supports automatic acquisition if you configure it in the right way. | The supported services and regions are limited.

#### 3.3 Custom Configuration

**Notice:** Supported since v0.0.92

##### 3.3.1 IAM endpoint configuration

Automatically acquiring projectId/domainId will invoke the [KeystoneListProjects](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=KeystoneListProjects) /[KeystoneListAuthDomains](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=KeystoneListAuthDomains) interface of IAM service. The default iam enpoint is `https://iam.myhuaweicloud.com`, you can modify the endpoint in the following two ways:

###### 3.3.1.1 Global scope

This configuration takes effect globally, specified by environment variable `HUAWEICLOUD_SDK_IAM_ENDPOINT`

```
//linux
export HUAWEICLOUD_SDK_IAM_ENDPOINT=https://iam.cn-north-4.myhuaweicloud.com

//windows
set HUAWEICLOUD_SDK_IAM_ENDPOINT=https://iam.cn-north-4.myhuaweicloud.com
```

###### 3.3.1.2 Credentials scope

This configuration is only valid for a credential, and it will override the global configuration

```python
from huaweicloudsdkcore.auth.credentials import BasicCredentials

iam_endpoint = "https://iam.cn-north-4.myhuaweicloud.com"
credentials = BasicCredentials(ak, sk).with_iam_endpoint(iam_endpoint)
```

##### 3.3.2 Region configuration

###### 3.3.2.1 Environment variable

Specified by environment variable, the format is `HUAWEICLOUD_SDK_REGION_{SERIVCE_NAME}_{REGION_ID}={endpoint}`

Notice: the name of environment variable is UPPER-CASE, replacing hyphens with underscores.

```
// Take ECS and IoTDA services as examples

// linux
export HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_99=https://ecs.cn-north-99.myhuaweicloud.com
export HUAWEICLOUD_SDK_REGION_IOTDA_AP_SOUTHEAST_10=https://iotda.ap-southwest-10.myhuaweicloud.com

// windows
set HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_99=https://ecs.cn-north-99.myhuaweicloud.com
set HUAWEICLOUD_SDK_REGION_IOTDA_AP_SOUTHEAST_10=https://iotda.ap-southwest-10.myhuaweicloud.com
```

###### 3.3.2.2 Profile

The profile will be read from the user's home directory by default, linux`~/.huaweicloud/regions.yaml`,windows`C:\Users\USER_NAME\.huaweicloud\regions.yaml`,the default file may not exist, but if the file exists and the content format is incorrect, an exception will be thrown for parsing errors.

The path to the profile can be modified by configuring the environment variable `HUAWEICLOUD_SDK_REGIONS_FILE`, like `HUAWEICLOUD_SDK_REGIONS_FILE=/tmp/my_regions.yml`

The file content format is as follows:

```yaml
# Serivce name is case-insensitive
ECS:
  - id: 'cn-north-10'
    endpoint: 'https://ecs.cn-north-10.myhuaweicloud.com'
  - id: 'cn-north-11'
    endpoint: 'https://ecs.cn-north-11.myhuaweicloud.com'
IoTDA:
  - id: 'ap-southwest-9'
    endpoint: 'https://iotda.ap-southwest-9.myhuaweicloud.com'
```

###### 3.3.2.3 Region supply chain

The default order is **environment variables -> profile -> region defined in SDK**, if the region is not found in the above ways, an exception will be thrown.

```python
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion

region1 = EcsRegion.value_of("cn-north-10")
region2 = EcsRegion.value_of("cn-north-11")
```

### 4. Send Requests and Handle Responses [:top:](#user-manual-top)

``` python
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

``` python
# handle exceptions
try:
    request = ListVpcsRequest(limit=1)
    response = client.list_vpcs(request)
    print(response)
except exception.ServiceResponseException as e:
    print(e.status_code)
    print(e.request_id)
    print(e.error_code)
    print(e.error_msg)
```

#### 4.2 Get Response Object [:top:](#user-manual-top)

The default response format of each request is `json string`, if you want to obtain the response object, the Python SDK
supports using method `to_json_object()` to get it.

``` python
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

``` python
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

For example:

``` python
# Initialize specified service client instance, take VpcClient for example
client = VpcClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .with_file_log(path="test.log", log_level=logging.INFO) \  # Write log files
    .with_stream_log(log_level=logging.INFO) \                 # Write log to console
    .build()
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

``` text
2020-06-16 10:44:02,019 4568 HuaweiCloud-SDK http_handler.py 28 INFO "GET https://vpc.cn-north-1.myhuaweicloud.com/v1/0904f9e1f100d2932f94c01f9aa1cfd7/vpcs" 200 11 0:00:00.543430 b5c927ffdab8401e772e70aa49972037
```

The format of access log is:

``` python
%(asctime)s %(thread)d %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s
```

#### 6.2 Original HTTP Listener [:top:](#user-manual-top)

In some situation, you may need to debug your http requests, original http request and response information will be
needed. The SDK provides a listener function to obtain the original encrypted http request and response information.

> :warning:  Warning: The original http log information is used in debugging stage only, please do not print the original http header or body in the production environment. These log information is not encrypted and contains sensitive data such as the password of your ECS virtual machine, or the password of your IAM user account, etc. When the response body is binary content, the body will be printed as "***" without detailed information.

``` python
import logging
from huaweicloudsdkcore.http.http_handler import HttpHandler


def response_handler(**kwargs):
    logger = kwargs.get("logger")
    response = kwargs.get("response")
    request = response.request

    base = "> Request %s %s HTTP/1.1" % (request.method, request.path_url) + "\n"
    if len(request.headers) != 0:
        base = base + "> Headers:" + "\n"
        for each in request.headers:
            base = base + "    %s : %s" % (each, request.headers[each]) + "\n"
    base = base + "> Body: %s" % request.body + "\n\n"

    base = base + "< Response HTTP/1.1 %s " % response.status_code + "\n"
    if len(response.headers) != 0:
        base = base + "< Headers:" + "\n"
        for each in response.headers:
            base = base + "    %s : %s" % (each, response.headers[each],) + "\n"
    base = base + "< Body: %s" % response.content
    logger.debug(base)


if __name__ == "__main__":
    client = VpcClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(basic_credentials) \
        .with_stream_log(log_level=logging.DEBUG) \
        .with_http_handler(HttpHandler().add_response_handler(response_handler)) \
        .with_endpoint(endpoint) \
        .build()
```

**Notice:**

HttpHandler supports method `add_request_handler` and `add_response_handler`.

### 7. Upload and download files [:top:](#user-manual-top)

Take the interface `CreateImageWatermark` of the service `Data Security Center` as an example, this interface needs to upload an image file and return the watermarked image file stream:

```python
# coding: utf-8
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
    ak = "{your ak string}"
    sk = "{your sk string}"
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