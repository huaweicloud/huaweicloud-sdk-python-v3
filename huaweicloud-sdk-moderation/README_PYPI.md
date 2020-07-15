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

- Install from [source](https://github.com/huaweicloud/huaweicloud-sdk-python-v3)

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
    from huaweicloudsdk{service}.v2 import *
    ```

2. Config `{Service}Client` Configurations

    2.1 Use default configuration

    ```python
    #  Use default configuration
    config = HttpConfig.get_default_config()
    ```

    2.2 Proxy(Optional)

    ```python
    # Use Proxy if needed
    config.proxy_protocol = 'http'
    config.proxy_host = 'proxy.huaweicloud.com'
    config.proxy_port = 80
    config.proxy_user = 'username'
    config.proxy_password = 'password'
    ```

    2.3 Connection(Optional)

    ```python
    # seconds to wait for the server to send data before giving up, as a float, or (connect timeout, read timeout)
    config.timeout = 3
    ```

    2.4 SSL Certification(Optional)

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
    client = {Service}Client.new_builder({Service}Client) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .with_file_log(path="test.log", log_level=logging.INFO) \  # Write log files
        .with_stream_log(log_level=logging.INFO) \                 # Write log to console
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

    After enabled log, the SDK will print the access log by default, every request will be recorded in console like: '%(asctime)s %(thread)d %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s'

    ```shell script
    2020-06-16 10:44:02,019 4568 HuaweiCloud-SDK http_handler.py 28 INFO "GET https://vpc.cn-north-1.myhuaweicloud.com/v1/0904f9e1f100d2932f94c01f9aa1cfd7/vpcs" 200 11 0:00:00.543430 b5c927ffdab8401e772e70aa49972037
    ```

5. Send a request and print response.

	```python
	# Initialize a request and set parameters
	response = client.method()
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
        response = client.method()
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
    response = client.method()

    # get asynchronous response
    print(response.result())
    ```

8. Troubleshooting

    In some situation, you may need to debug your http requests, original http request and response information will be needed. The SDK provides a listener function to obtain the original encrypted http request and response information.

    **Warning:** The original http log can only be used in troubleshooting scenarios, please do not print the original http header or body in the production environment. The log content is not encrypted and may contain sensitive information such as the password of your ECS or the password of your IAM user account, etc. When the response body is binary content, the body will be printed as "***" without detailed information.

    ```python
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
    
    client = {Service}Client.new_builder({Service}Client) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .with_file_log(path="test.log", log_level=logging.INFO) \
        .with_stream_log(log_level=logging.INFO) \
        .with_http_handler(HttpHandler().add_response_handler(response_handler)) \
        .build()
    ```

	**where:**

    HttpHandler supports add_request_handler and add_response_handler.
