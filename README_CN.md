[English](./README.md) | 简体中文

# 华为云开发者 Python 软件开发工具包 （Python SDK）

欢迎使用华为云 Python SDK。

华为云 Python SDK让您无需关心请求细节即可快速使用云服务器、虚拟私有云等多个华为云服务。

这里将向您介绍如何获取并使用华为云 Python SDK。

## 在线示例

[API Explorer](https://apiexplorer.developer.huaweicloud.com/apiexplorer/overview) 提供API检索及平台调试，支持全量快速检索、可视化调试、帮助文档查看、在线咨询。

## 现在开始

- 要使用华为云 Python SDK，您需要拥有云账号以及该账号对应的Access Key（AK）和Secret Access Key（SK）。 请在华为云控制台“我的凭证-访问密钥”页面上创建和查看您的AKSK。更多信息请查看[访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html)。

- 华为云 Python SDK 支持 python3 及以上版本。

## SDK 获取和安装

华为云 Python SDK 支持python3及以上版本。执行``python --version``检查当前python的版本信息.

- 使用 pip 安装

    执行如下命令安装华为云 Python SDK核心库以及相关服务库:
    
    ```bash
    # 安装核心库
    pip install huaweicloudsdkcore
    
    # 安装VPC服务库
    pip install huaweicloudsdkvpc
    ```

- 使用源码安装

    执行如下命令安装华为云 Python SDK核心库以及相关服务库:
    
    ```bash
    # 安装核心库
    cd huaweicloudsdkcore-${version}
    python setup.py install
    
    # 安装VPC服务库
    cd huaweicloudsdkvpc-${version}
    python setup.py install
    ```

## 开始使用

1. 导入依赖模块:

    ```python
    from huaweicloudsdkcore.auth.credentials import BasicCredentials
    from huaweicloudsdkcore.exceptions import exceptions
    from huaweicloudsdkcore.http.http_config import HttpConfig
    from huaweicloudsdkvpc.v2 import *
    ```

2. 配置客户端属性

    2.1 默认配置

    ```python
    # 使用默认配置
    config = HttpConfig.get_default_config()
    ```

    2.2 代理配置

    ```python
    # 使用代理服务器
    config.proxy_protocol = 'http'
    config.proxy_host = 'proxy.huaweicloud.com'
    config.proxy_port = 80
    config.proxy_user = 'username'
    config.proxy_password = 'password'
    ```

    2.3 连接配置

    ```python
    # 配置连接超时，支持统一指定超时时长timeout=timeout，或分别指定超时时长timeout=(connect timeout, read timeout)
    config.timeout = 3
    ```

    2.4 SSL配置

    ```python
    # 配置跳过服务端证书验证
    config.ignore_ssl_verification = True
    # 配置服务器端CA证书，用于SDK验证服务端证书合法性
    config.ssl_ca_cert = ssl_ca_cert
    ```

3. 初始化认证信息

    ```python
    credentials = BasicCredentials(ak, sk, project_id, domain_id)
    ```

	**说明:**

   	非全局服务仅需要提供project_id，domain_id无需提供。
    全局服务project_id必须为null，domain_id请按照实际情况填写。
    全局服务当前仅支持IAM。

    - `ak` 华为云账号Access Key。
    - `sk` 华为云账号Secret Access Key。
    - `project_id` 云服务所在项目 ID。
    - `domain_id` 华为云账号 ID。

4. 初始化客户端:

    ```python
    client = VpcClient.new_builder(VpcClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .with_file_log(path="test.log", log_level=logging.INFO) \  # 日志打印至文件
        .with_stream_log(log_level=logging.INFO) \                 # 日志打印至控制台
        .with_enable_http_log(True) \                              # 打开HTTP请求日志
        .build()
    ```

	**说明:**

    - `endpoint` 华为云各服务应用区域和各服务的终端节点，详情请查看[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
    - `with_file_log` 支持如下配置：
        - `path`: 日志文件路径。
        - `log_level`: 日志级别，默认INFO。
        - `max_bytes`: 单个日志文件大小，默认为10485760 bytes。
        - `backup_count`: 日志文件个数，默认为5个。
    - `with_stream_log` 支持如下配置：
        - `stream`: 流对象，默认sys.stdout。
        - `log_level`: 日志级别，默认INFO。
    
    **注意：**
    - `with_enable_http_log`: http日志仅用于开发场景下的问题定位，生产环境不推荐打开此功能。由于此功能会打印详细的请求以及相应信息，可能包含敏感信息，同时可能导致日志文件过大。

5. 发送请求并查看响应.

	```python
	# 初始化请求
	response = client.list_vpcs()
	print(respones)
	```

6. 异常处理

    | 一级分类 | 一级分类说明 | 二级分类 | 二级分类说明 |
    | :---- | :---- | :---- | :---- |
    | ConnectionException | 连接类异常 | HostUnreachableException | 网络不可达、被拒绝 |
    | | | SslHandShakeException | SSL认证异常 |
    | RequestTimeoutException | 响应超时异常 | CallTimeoutException | 单次请求，服务器处理超时未返回 |
    | | | RetryOutageException | 在重试策略消耗完成已后，仍无有效的响应 |
    | ServiceResponseException | 服务器响应异常 | ServerResponseException | 服务端内部错误，Http响应码：[500,] |
    | | | ClientRequestException | 请求参数不合法，Http响应码：[400， 500) |
    
    ```python
    # 异常处理
    try:
        response = client.list_vpcs()
    except exception.ServiceResponseException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
    ```

7. 异步场景

    ```python
    # 初始化异步客户端
    vpc_client = VpcAsyncClient.new_builder(VpcAsyncClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    # 发送异步请求
    request = ListVpcsRequest()
    response = client.list_vpcs_async(request)

    # 获取异步请求结果
    print(response.result())
    ```

## 代码实例

使用如下代码同步查询特定Region下的VPC清单，调用前请根据实际情况替换如下变量：`{your ak string}`、 `{your sk string}`、 `{your endpoint}` 以及 `{your project id}`。

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
