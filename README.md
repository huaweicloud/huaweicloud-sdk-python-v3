English | [简体中文](./README_ZH.md)

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
    from huaweicloudsdkvpc.v2 import VpcClient
    ```

2. Config `{Service}Client` Configurations

    ```python
    # Using the default configuration
    config = HttpConfig.get_default_config()

    # Set Proxy if needed
    config.proxy_protocol = 'http'
    config.proxy_host = 'proxy.huaweicloud.com'
    config.proxy_port = 80
    config.proxy_user = 'test'
    config.proxy_password = 'test'
    
    # Skip ssl certifaction checking while using https protocal if needed
    config.ignore_ssl_verification = True
    ```

3. Initialize the `{Service}Client` instance:

    ```python
    credentials = BasicCredentials(ak, sk, project_id)

    vpc_client = VpcClient.new_builder(VpcClient) \
        .with_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()
    ```

	where:

	- `ak` is the access key id for your account.
	- `sk` is the secret access key for your account.
	- `project_id` is the id of the project.
    - `endpoint` is the service specific endpoints, see [Regions and Endpoints](https://developer.huaweicloud.com/intl/en-us/endpoint)

4. Send a request and print response.

	```python
	# Initialize a request and set parameters
	response = client.list_vpcs()
	print(respones)
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
        .with_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    list_vpc(vpc_client)

```
