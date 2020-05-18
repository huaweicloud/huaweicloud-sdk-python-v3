[English](./README.md) | 简体中文

# 华为云开发者 Python 软件开发工具包 （Python SDK）

欢迎使用华为云 Python SDK。

华为云 Python SDK让您无需关心请求细节即可快速使用云服务器、虚拟私有云等多个华为云服务。

这里将向您介绍如何获取并使用华为云 Python SDK。

## 在线示例

[API Explorer](https://apiexplorer.developer.huaweicloud.com/apiexplorer/overview) 提供API检索及平台调试，支持全量快速检索、可视化调试、帮助文档查看、在线咨询。



## 现在开始

- 要使用华为云 .Net SDK，您需要拥有云账号以及该账号对应的Access Key（AK）和Secret Access Key（SK）。 请在华为云控制台“我的凭证-访问密钥”页面上创建和查看您的AKSK。更多信息请查看[访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html).

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
    from huaweicloudsdkvpc.v2 import VpcClient
    ```

2. 配置客户端属性

    ```python
    # 使用默认配置
    config = HttpConfig.get_default_config()

    # 配置Proxy（可选）
    config.proxy_protocol = 'http'
    config.proxy_host = 'proxy.huaweicloud.com'
    config.proxy_port = 80
    config.proxy_user = 'test'
    config.proxy_password = 'test'
    
    # 配置HTTPS请求跳过SSL证书验证（可选）
    config.ignore_ssl_verification = True
    ```

3. 初始化客户端:

    ```python
    credentials = BasicCredentials(ak, sk, project_id)

    vpc_client = VpcClient.new_builder(VpcClient) \
        .with_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()
    ```

	说明:

	- `ak` 华为云账号Access Key。
	- `sk` 华为云账号Secret Access Key。
	- `project_id` 云服务所在项目 ID。
    - `endpoint` 华为云各服务应用区域和各服务的终端节点，详情请查看[地区和终端节点](https://developer.huaweicloud.com/endpoint)。


4. 发送请求并查看响应.

	```python
	# 初始化请求
	response = client.list_vpcs()
	print(respones)
	```

## 代码实例

使用如下代码查询特定Region下的VPC清单，调用前请根据实际情况替换如下变量：`{your ak string}`、 `{your sk string}`、 `{your endpoint}` 以及 `{your project id}`。

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
