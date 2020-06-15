English | [简体中文](./README_CN.md)

# HuaweiCloud Python Software Development Kit (Python SDK)

The HuaweiCloud Python SDK allows you to easily work with Huawei Cloud services such as Elastic Compute Service (ECS) and Virtual Private Cloud(VPC) without the need to handle API related tasks.

This document introduces how to obtain and use HuaweiCloud Python SDK.

## Getting Started

- To use HuaweiCloud Python SDK, you must have Huawei Cloud account as well as the Access Key and Secret key of the HuaweiCloud account.

	The accessKey is required when initializing `{Service}Client`. You can create an AccessKey in the Huawei Cloud console. For more information, see [My Credentials](https://support.huaweicloud.com/en-us/usermanual-ca/en-us_topic_0046606340.html).

- HuaweiCloud Python SDK requires python 3 or later.


## Install Python SDK

HuaweiCloud Python SDK supports Python 3 or later. Run ``python --version`` to check the version of Python.

- Use python pip

	Run the following command to install the individual libraries of HuaweiCloud services:

	```bash
	# Install the core library
	pip install huaweicloudsdkcore
 
	# Install the VPC management library
	pip install huaweicloudsdkvpc
	```

- Install from source

	Run the following command to install the individual libraries of HuaweiCloud services:

	```bash
	# Install the core library
	cd huaweicloudsdkcore-${version}
	python setup.py install
 
	# Install the VPC management library
	cd huaweicloudsdkvpc-${version}
	python setup.py install
	```

## Use Python SDK

1. Import the required modules as follows:

    ```python
    from huaweicloudsdkcore.auth.credentials import BasicCredentials
    from huaweicloudsdkcore.exceptions import exceptions
    from huaweicloudsdkcore.http.http_config import HttpConfig
    from huaweicloudsdkvpc.v2 import *
    ```

2. Config `{Service}Client` Configurations

    2.1 Use default configuration

    ```python
    #  Use default configuration
    config = HttpConfig.get_default_config()
    ```

    2.2 Proxy

    ```python
    # Use Proxy if needed
    config.proxy_protocol = 'http'
    config.proxy_host = 'proxy.huaweicloud.com'
    config.proxy_port = 80
    config.proxy_user = 'username'
    config.proxy_password = 'password'
    ```

    2.3 Connection

    ```python
    # seconds to wait for the server to send data before giving up, as a float, or (connect timeout, read timeout)
    config.timeout = 3
    ```

    2.4 SSL Certification

    ```python
    # Skip ssl certifaction checking while using https protocol if needed
    config.ignore_ssl_verification = True
    # Server ca certification if needed
    config.ssl_ca_cert = ssl_ca_cert
    ```

3. Initialize Credentials

    ```python
    credentials = BasicCredentials(ak, sk, project_id, domain_id)
    ```

	**where:**
   	
    For project services, only need to provide project_id, domain_id is optional.
    For global services, project_id must be null, domain_id should be filled in according to the actual situation.
    Global services currently only support Iam.

	- `ak` is the access key id for your account.
	- `sk` is the secret access key for your account.
	- `project_id` is the id of the project.
  	- `project_id` is the account ID of huawei cloud.

4. Initialize the `{Service}Client` instance:

    ```python
    client = VpcClient.new_builder(VpcClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .with_file_log(path="test.log", log_level=logging.INFO) \  # Write log files
        .with_stream_log(log_level=logging.INFO) \                 # Write log to console
        .with_enable_http_log(True) \                              # log whole http request and response
        .build()
    ```

	**where:**

    - `endpoint`: service specific endpoints, see [Regions and Endpoints](https://developer.huaweicloud.com/intl/en-us/endpoint).
    - `with_file_log`:
        - `path`: log file path.
        - `log_level`: log level, default is INFO.
        - `max_bytes`: size of single log file, default is 10485760 bytes.
        - `backup_count`: count of log file, default is 5.
    - `with_stream_log`:
        - `stream`: stream object, default is sys.stdout.
        - `log_level`: log level, default is INFO.
    
    **Warning**
    - `with_enable_http_log`: We recommend you only use this for debugging purposes. Disable it in your production environments, as it records the whole request and response data, which may contains sensitive data, and it could be very large.

5. Send a request and print response.

	```python
	# Initialize a request and set parameters
	response = client.list_vpcs()
	print(respones)
	```

6. Exceptions

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
        response = client.list_vpcs()
    except exception.ServiceResponseException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
    ```

7. Asynchronous Requests

    ```python
    # Initialize asynchronous client
    vpc_client = VpcAsyncClient.new_builder(VpcAsyncClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    # send asynchronous request
    request = ListVpcsRequest()
    response = client.list_vpcs_async(request)

    # get asynchronous response
    print(response.result())
    ```

## Code example

The following example shows how to query a list of VPC in a specific region. Substitute the values for `{your ak string}`, `{your sk string}`, `{your endpoint}` and `{your project id}`.

```python
# coding: utf-8


from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkvpc.v2 import VpcClient


def list_vpc(client):
    try:
        response = client.list_vpcs()
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

    vpc_client = VpcClient.new_builder(VpcClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    list_vpc(vpc_client)

```
