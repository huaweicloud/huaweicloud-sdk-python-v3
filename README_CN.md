[English](./README.md) | 简体中文

<p align="center">
  <a href="https://www.huaweicloud.com/"><img width="270px" height="90px" src="https://console-static.huaweicloud.com/static/authui/20210202115135/public/custom/images/logo.svg"></a>
</p>

<h1 align="center">华为云开发者 Python 软件开发工具包（Python SDK）</h1>

欢迎使用华为云 Python SDK。

华为云 Python SDK让您无需关心请求细节即可快速使用弹性云服务器、虚拟私有云等多个华为云服务。

这里将向您介绍如何获取并使用华为云 Python SDK 。

## 使用前提

- 要使用华为云 Java SDK ，您需要拥有华为云账号以及该账号对应的 Access Key（AK）和 Secret Access Key（SK）。请在华为云控制台 “我的凭证-访问密钥” 页面上创建和查看您的 AK&SK
  。更多信息请查看 [访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html) 。

- 要使用华为云 Java SDK 访问指定服务的 API
  ，您需要确认已在 [华为云控制台](https://console.huaweicloud.com/console/?locale=zh-cn&region=cn-north-4#/home) 开通当前服务。

- 华为云 Python SDK 支持 **python3** 及以上版本。可执行 `python --version` 检查当前 python 的版本信息。

## SDK 获取和安装

您可以使用 pip 安装 SDK 依赖包，也可以使用源码安装 SDK 依赖包。

无论您要使用哪个产品/服务的开发工具包，都必须安装 `huaweicloudsdkcore` 。以使用虚拟私有云 VPC SDK 为例，您需要安装 `huaweicloudsdkcore` 和 `huaweicloudsdkvpc` ：

- 使用 pip 安装

``` bash
# 安装核心库
pip install huaweicloudsdkcore

# 安装VPC服务库
pip install huaweicloudsdkvpc
```

- 使用源码安装

``` bash
# 安装核心库
cd huaweicloudsdkcore-${version}
python setup.py install

# 安装VPC服务库
cd huaweicloudsdkvpc-${version}
python setup.py install
```

## 代码示例

- 使用如下代码同步查询指定 Region 下的 VPC 清单，实际使用中请将 `VpcClient` 替换为您使用的产品/服务相应的 `{Service}Client`。
- 调用前请根据实际情况替换如下变量：`{your ak string}`、 `{your sk string}`、 `{your endpoint}` 以及 `{your project id}`。

``` python
# coding: utf-8


from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_config import HttpConfig
# 导入指定云服务的库 huaweicloudsdk{service}
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

## 在线调试

[API Explorer](https://apiexplorer.developer.huaweicloud.com/apiexplorer/overview)
提供API检索及平台调试，支持全量快速检索、可视化调试、帮助文档查看、在线咨询。

## 变更日志

每个版本的详细更改记录可在 [变更日志](https://github.com/huaweicloud/huaweicloud-sdk-python-v3/blob/master/CHANGELOG_CN.md) 中查看。

## 用户手册 [:top:](#华为云开发者-python-软件开发工具包python-sdk)

* [1. 客户端连接参数](#1-客户端连接参数-top)
    * [1.1 默认配置](#11-默认配置-top)
    * [1.2 网络代理](#12-网络代理-top)
    * [1.3 超时配置](#13-超时配置-top)
    * [1.4 SSL 配置](#14-ssl-配置-top)
* [2. 客户端认证信息](#2-客户端认证信息-top)
    * [2.1 使用永久 AK 和 SK](#21-使用永久-ak-和-sk-top)
    * [2.2 使用临时 AK 和 SK](#22-使用临时-ak-和-sk-top)
* [3. 客户端初始化](#3-客户端初始化-top)
    * [3.1 指定云服务 Endpoint 方式](#31-指定云服务-endpoint-方式-top)
    * [3.2 指定 Region 方式（推荐）](#32-指定-region-方式-推荐-top)
* [4. 发送请求并查看响应](#4-发送请求并查看响应-top)
    * [4.1 异常处理](#41-异常处理-top)
    * [4.2 获取响应对象](#42-获取响应对象-top)
* [5. 异步客户端使用](#5-异步客户端使用-top)
* [6. 故障处理](#6-故障处理-top)
    * [6.1 访问日志](#61-访问日志-top)
    * [6.2 HTTP 监听器](#62-http-监听器-top)

### 1. 客户端连接参数 [:top:](#用户手册-top)

#### 1.1 默认配置 [:top:](#用户手册-top)

``` python
# 使用默认配置
config = HttpConfig.get_default_config()
```

#### 1.2 网络代理 [:top:](#用户手册-top)

``` python
# 根据需要配置网络代理
config.proxy_protocol = 'http'
config.proxy_host = 'proxy.huaweicloud.com'
config.proxy_port = 80
config.proxy_user = 'username'
config.proxy_password = 'password'
```

#### 1.3 超时配置 [:top:](#用户手册-top)

``` python
# 默认连接超时时间为60秒，读取超时时间为120秒，支持统一指定超时时长timeout=timeout，或分别指定超时时长timeout=(connect timeout, read timeout)
config.timeout = 120
```

#### 1.4 SSL 配置 [:top:](#用户手册-top)

``` python
# 根据需要配置是否跳过SSL证书校验
config.ignore_ssl_verification = True
# 配置服务器端CA证书，用于SDK验证服务端证书合法性
config.ssl_ca_cert = ssl_ca_cert
```

### 2. 客户端认证信息 [:top:](#用户手册-top)

华为云服务存在两种部署方式，Region 级服务和 Global 级服务。

Global 级服务有 BSS、DevStar、EPS、IAM、RMS、TMS。

Region 级服务需要提供 projectId 。Global 级服务需要提供 domainId 。

客户端认证可以使用永久 AK&SK 认证，也可以使用临时 AK&SK&SecurityToken 认证。

**认证参数说明**：

- `ak` 华为云账号 Access Key
- `sk` 华为云账号 Secret Access Key
- `project_id` 云服务所在项目 ID ，根据你想操作的项目所属区域选择对应的项目 ID
- `domain_id` 华为云账号 ID
- `security_token` 采用临时 AK&SK 认证场景下的安全票据

#### 2.1 使用永久 AK 和 SK [:top:](#用户手册-top)

``` python
# Region级服务
basic_credentials = BasicCredentials(ak, sk, project_id)

# Global级服务
global_credentials = GlobalCredentials(ak, sk, domain_id)
```

- `3.0.26-beta` 及以上版本支持通过永久 AK&SK 回填 project_id/domain_id ，需要在初始化客户端时配合 `with_region()`
  方法使用，代码示例详见 [3.2 指定Region方式（推荐）](#32-指定-region-方式-推荐-top) 。

#### 2.2 使用临时 AK 和 SK [:top:](#用户手册-top)

首先需要获得临时 AK、SK 和 SecurityToken ，可以从永久 AK&SK 获得，或者通过委托授权获得。

- 通过永久 AK&SK 获得可以参考文档：https://support.huaweicloud.com/api-iam/iam_04_0002.html ，对应 IAM SDK
  中的 `CreateTemporaryAccessKeyByToken` 方法。

- 通过委托授权获得可以参考文档：https://support.huaweicloud.com/api-iam/iam_04_0101.html ，对应 IAM SDK
  中的 `CreateTemporaryAccessKeyByAgency` 方法。

临时 AK&SK&SecurityToken 获取成功后，可使用如下方式初始化认证信息：

``` python
# Region级服务
basic_credentials = BasicCredentials(ak, sk, project_id).with_security_token(security_token)

# Global级服务
global_credentials = GlobalCredentials(ak, sk, domain_id).with_security_token(security_token)
```

### 3. 客户端初始化 [:top:](#用户手册-top)

客户端初始化有两种方式，可根据需要选择下列两种方式中的一种：

#### 3.1 指定云服务 Endpoint 方式 [:top:](#用户手册-top)

``` python
# 初始化指定云服务的客户端 {Service}Client ，以初始化 VpcClient 为例
client = VpcClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()
```

**说明:**

- `endpoint` 是华为云各服务应用区域和各服务的终端节点，详情请查看 [地区和终端节点](https://developer.huaweicloud.com/endpoint) 。

#### 3.2 指定 Region 方式 **（推荐）** [:top:](#用户手册-top)

``` python
# 增加region依赖
from huaweicloudsdkiam.v3.region.iam_region import IamRegion

# 使用当前客户端初始化方式可不填 domain_id
global_credentials = GlobalCredentials(ak, sk)

# 初始化指定云服务的客户端 {Service}Client ，以初始化 IamClient 为例
client = IamClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(global_credentials) \
    .with_region(IamRegion.CN_NORTH_4) \
    .build()
```

**说明:**

- 指定 Region 方式创建客户端的场景，支持自动获取用户的 projectId 或者 domainId，初始化认证信息时可无需指定相应参数。
- 不适用于 `多ProjectId` 的场景。

### 4. 发送请求并查看响应 [:top:](#用户手册-top)

``` python
# 初始化请求，以调用接口 ListVpcs 为例
request = ListVpcsRequest(limit=1)

response = client.list_vpcs(request)
print(response)
```

#### 4.1 异常处理 [:top:](#用户手册-top)

| 一级分类 | 一级分类说明 | 二级分类 | 二级分类说明 |
| :---- | :---- | :---- | :---- |
| ConnectionException | 连接类异常 | HostUnreachableException | 网络不可达、被拒绝 |
| | | SslHandShakeException | SSL认证异常 |
| RequestTimeoutException | 响应超时异常 | CallTimeoutException | 单次请求，服务器处理超时未返回 |
| | | RetryOutageException | 在重试策略消耗完成已后，仍无有效的响应 |
| ServiceResponseException | 服务器响应异常 | ServerResponseException | 服务端内部错误，Http响应码：[500,] |
| | | ClientRequestException | 请求参数不合法，Http响应码：[400， 500) |

``` python
# 异常处理
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

#### 4.2 获取响应对象 [:top:](#用户手册-top)

Python SDK 默认返回的 response 为原始响应的 Json 数据，如果需要获取当前数据对象，可以使用 `to_json_object()` 方法：

``` python
request = ListVpcsRequest(limit=1)
# 原始响应Json
response = client.list_vpcs(request)
print(response)
# 响应对象
response_obj = response.to_json_object()
print(response_obj["vpcs"])
```

**说明**：该方法仅在 `3.0.34-rc` 及以上版本可以使用

### 5. 异步客户端使用 [:top:](#用户手册-top)

``` python
# 初始化异步客户端，以初始化 VpcAsyncClient 为例
client = VpcAsyncClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()

# 发送异步请求
request = ListVpcsRequest(limit=1)
response = client.list_vpcs_async(request)

# 获取异步请求结果
print(response.result())
```

### 6. 故障处理 [:top:](#用户手册-top)

SDK 提供 Access 级别的访问日志及 Debug 级别的原始 HTTP 监听器日志，用户可根据需要进行配置。

#### 6.1 访问日志 [:top:](#用户手册-top)

SDK 支持打印 Access 级别的访问日志，需要用户手动打开日志开关，支持打印到控制台或者指定的文件。示例如下：

``` python
client = VpcClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .with_file_log(path="test.log", log_level=logging.INFO) \  # 日志打印至文件
    .with_stream_log(log_level=logging.INFO) \                 # 日志打印至控制台
    .build()
```

**说明**：

- `with_file_log` 支持如下配置：
    - `path`：日志文件路径
    - `log_level`：日志级别，默认INFO
    - `max_bytes`：单个日志文件大小，默认为10485760 bytes
    - `backup_count`：日志文件个数，默认为5个
- `with_stream_log` 支持如下配置：
    - `stream`：流对象，默认sys.stdout
    - `log_level`：日志级别，默认INFO

打开日志开关后，每次请求都会有一条记录，如：

``` text 
2020-06-16 10:44:02,019 4568 HuaweiCloud-SDK http_handler.py 28 INFO "GET https://vpc.cn-north-1.myhuaweicloud.com/v1/0904f9e1f100d2932f94c01f9aa1cfd7/vpcs" 200 11 0:00:00.543430 b5c927ffdab8401e772e70aa49972037
```

日志格式为：

``` python
%(asctime)s %(thread)d %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s
```

#### 6.2 HTTP 监听器 [:top:](#用户手册-top)

在某些场景下可能对业务发出的 HTTP 请求进行 Debug ，需要看到原始的 HTTP 请求和返回信息，SDK 提供监听器功能来获取原始的为加密的 HTTP 请求和返回信息。

> :warning:  Warning: 原始信息打印仅在 Debug 阶段使用，请不要在生产系统中将原始的 HTTP 头和 Body 信息打印到日志，这些信息并未加密且其中包含敏感数据，例如所创建虚拟机的密码，IAM 用户的密码等；当 Body 体为二进制内容，即 Content-Type 标识为二进制时，Body 为"***"，详细内容不输出。

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

**说明:**
HttpHandler 支持如下方法 `add_request_handler`、`add_response_handler` 。
