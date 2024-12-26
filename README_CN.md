[English](./README.md) | 简体中文

<p align="center">
  <a href="https://www.huaweicloud.com/"><img width="270px" height="90px" src="https://console-static.huaweicloud.com/static/authui/20210202115135/public/custom/images/logo.svg"></a>
</p>

<h1 align="center">华为云开发者 Python 软件开发工具包（Python SDK）</h1>

欢迎使用华为云 Python SDK。

华为云 Python SDK让您无需关心请求细节即可快速使用弹性云服务器（ECS）、虚拟私有云（VPC）等多个华为云服务。

这里将向您介绍如何获取并使用华为云 Python SDK 。

## 使用前提

- 要使用华为云 Python SDK ，您需要拥有华为云账号以及该账号对应的 Access Key（AK）和 Secret Access Key（SK）。请在华为云控制台 “我的凭证-访问密钥” 页面上创建和查看您的 AK&SK
  。更多信息请查看 [访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html) 。

- 要使用华为云 Python SDK 访问指定服务的 API
  ，您需要确认已在 [华为云控制台](https://console.huaweicloud.com/console/?locale=zh-cn&region=cn-north-4#/home) 开通当前服务。

- 华为云 Python SDK 支持 **python3.3以上** 的版本。可执行 `python --version` 检查当前 python 的版本信息。

## SDK 获取和安装

您可以使用 pip 安装 SDK 依赖包，也可以使用源码安装 SDK 依赖包。

您可以通过 [SDK中心](https://console.huaweicloud.com/apiexplorer/#/sdkcenter?language=Python) 或 [PYPI](https://pypi.org/search/?q=huaweicloudsdk) 查询SDK版本信息。

### 独立云服务包

以使用虚拟私有云 VPC SDK 为例，您需要安装 `huaweicloudsdkvpc`：

- 使用 pip 安装

```bash
# 安装VPC服务包
pip install huaweicloudsdkvpc
```

- 使用源码安装

```bash
# 安装VPC服务包
cd huaweicloudsdkvpc-${version}
python setup.py install
```

### 云服务集合包

您可以安装`huaweicloudsdkall`，这么做会安装所有SDK支持的服务包：

- 使用 pip 安装

```bash
pip install huaweicloudsdkall
```

- 使用源码安装

```bash
cd huaweicloudsdkall-${version}
python setup.py install
```

## 代码示例

- 使用如下代码同步查询指定 Region 下的 VPC 清单，实际使用中请将 `VpcClient` 替换为您使用的产品/服务相应的 `{Service}Client`。
- 认证用的ak和sk直接写到代码中有很大的安全风险，建议在配置文件或者环境变量中密文存放，使用时解密，确保安全。
- 本示例中的ak和sk保存在环境变量中，运行本示例前请先在本地环境中配置环境变量`HUAWEICLOUD_SDK_AK`和`HUAWEICLOUD_SDK_SK`。

**精简示例**

```python
# coding: utf-8

import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkvpc.v2 import ListVpcsRequest, VpcClient
from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion
from huaweicloudsdkcore.exceptions import exceptions

if __name__ == "__main__":
    # 配置认证信息
    # 请勿将认证信息硬编码到代码中，有安全风险
    # 可通过环境变量等方式配置认证信息，参考2.4认证信息管理章节
    credentials = BasicCredentials(os.getenv("HUAWEICLOUD_SDK_AK"), os.getenv("HUAWEICLOUD_SDK_SK"))

    # 创建服务客户端
    client = VpcClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(VpcRegion.value_of("cn-north-4")) \
        .build()

    # 发送请求并获取响应
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

**详细示例**

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
    # 配置认证信息
    # 请勿将认证信息硬编码到代码中，有安全风险
    # 可通过环境变量等方式配置认证信息，参考2.4认证信息管理章节
    # 如果未填写project_id，SDK会自动调用IAM服务查询所在region对应的项目id
    credentials = BasicCredentials(os.getenv("HUAWEICLOUD_SDK_AK"), os.getenv("HUAWEICLOUD_SDK_SK"), project_id="{your projectId string}") \
        .with_iam_endpoint("https://iam.cn-north-4.myhuaweicloud.com") # 配置SDK内置的IAM服务地址，默认为https://iam.myhuaweicloud.com

    # 使用默认配置
    http_config = HttpConfig.get_default_config()
    # 配置是否忽略SSL证书校验， 默认不忽略
    http_config.ignore_ssl_verification = True
    # 配置CA证书文件
    http_config.ssl_ca_cert = '/path/to/certfile'
    # 默认连接超时时间为60秒，读取超时时间为120秒，可根据需要配置
    http_config.timeout = (60, 120)
    # 根据需要配置网络代理
    # 请根据实际情况替换示例中的代理协议、地址和端口号
    http_config.proxy_protocol = 'http'
    http_config.proxy_host = 'proxy.huaweicloud.com'
    http_config.proxy_port = 80
    # 如果代理需要认证，请配置用户名和密码
    http_config.proxy_user = os.getenv("PROXY_USERNAME")
    http_config.proxy_password = os.getenv("PROXY_PASSWORD")

    # 注册监听器用于打印原始的请求和响应信息, 请勿用于生产环境
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

    # 创建服务客户端
    client = VpcClient.new_builder() \
        .with_credentials(credentials) \  # 配置认证信息
        .with_region(VpcRegion.value_of("cn-north-4")) \  # 配置地区, 如果地区不存在会抛出KeyError
        .with_http_config(http_config) \  # HTTP配置
        .with_stream_log(log_level=logging.INFO) \  # 配置请求日志输出到控制台
        .with_file_log(path="test.log", log_level=logging.INFO) \  # 配置请求日志输出到文件
        .with_http_handler(http_handler) \  # 配置HTTP监听器
        .build()

    # 发送请求并获取响应
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

## 在线调试

[API Explorer](https://apiexplorer.developer.huaweicloud.com/apiexplorer/overview)
提供API检索、SDK示例及平台调试，支持全量快速检索、可视化调试、帮助文档查看、在线咨询。

## 变更日志

每个版本的详细更改记录可在 [变更日志](https://github.com/huaweicloud/huaweicloud-sdk-python-v3/blob/master/CHANGELOG_CN.md) 中查看。

## 用户手册 [:top:](#华为云开发者-python-软件开发工具包python-sdk)

* [1. 客户端连接参数](#1-客户端连接参数-top)
    * [1.1 默认配置](#11-默认配置-top)
    * [1.2 网络代理](#12-网络代理-top)
    * [1.3 超时配置](#13-超时配置-top)
    * [1.4 SSL 配置](#14-ssl-配置-top)
* [2. 认证信息配置](#2-认证信息配置-top)
  * [2.1 使用永久 AK 和 SK](#21-使用永久-ak-和-sk-top)
  * [2.2 使用临时 AK 和 SK](#22-使用临时-ak-和-sk-top)
  * [2.3 使用 IdpId 和 IdTokenFile](#23-使用-idpid-和-idtokenfile-top)
  * [2.4 认证信息管理](#24-认证信息管理-top)
    * [2.4.1 环境变量](#241-环境变量-top)
	* [2.4.2 配置文件](#242-配置文件-top)
	* [2.4.3 实例元数据](#243-实例元数据-top)
	* [2.4.4 认证信息提供链](#244-认证信息提供链-top)
* [3. 客户端初始化](#3-客户端初始化-top)
    * [3.1 指定云服务 Endpoint 方式](#31-指定云服务-endpoint-方式-top)
    * [3.2 指定 Region 方式（推荐）](#32-指定-region-方式-推荐-top)
    * [3.3 自定义配置](#33-自定义配置-top)
        * [3.3.1 IAM endpoint配置](#331-IAM-endpoint配置-top)
        * [3.3.2 Region配置](#332-Region配置-top)
* [4. 发送请求并查看响应](#4-发送请求并查看响应-top)
    * [4.1 异常处理](#41-异常处理-top)
    * [4.2 获取响应对象](#42-获取响应对象-top)
* [5. 异步客户端使用](#5-异步客户端使用-top)
* [6. 故障处理](#6-故障处理-top)
    * [6.1 访问日志](#61-访问日志-top)
    * [6.2 HTTP 监听器](#62-http-监听器-top)
* [7. 接口调用器](#7-接口调用器-top)
    * [7.1 自定义请求头](#71-自定义请求头-top)
    * [7.2 请求重试](#72-请求重试-top)
* [8. 文件上传与下载](#8-文件上传与下载-top)
* [9. FAQ](#9-faq-top)
    * [9.1 云联盟场景如何调用](#91-云联盟场景如何调用-top)

### 1. 客户端连接参数 [:top:](#用户手册-top)

#### 1.1 默认配置 [:top:](#用户手册-top)

```python
from huaweicloudsdkcore.http.http_config import HttpConfig

# 使用默认配置
http_config = HttpConfig.get_default_config()

client = VpcClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

#### 1.2 网络代理 [:top:](#用户手册-top)

```python
http_config = HttpConfig.get_default_config()
# 根据需要配置网络代理
# 请根据实际情况替换示例中的代理协议、地址和端口号
http_config.proxy_protocol = 'http'
http_config.proxy_host = 'proxy.huaweicloud.com'
http_config.proxy_port = 80
# 如果代理需要认证，请配置用户名和密码
# 本示例中的账号和密码保存在环境变量中，运行本示例前请先在本地环境中配置环境变量PROXY_USERNAME和PROXY_PASSWORD
http_config.proxy_user = os.getenv("PROXY_USERNAME")
http_config.proxy_password = os.getenv("PROXY_PASSWORD")

client = VpcClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

#### 1.3 超时配置 [:top:](#用户手册-top)

```python
http_config = HttpConfig.get_default_config()
# 默认连接超时时间为60秒，读取超时时间为120秒
# 将连接超时时间和读取超时时间统一设置为120秒
http_config.timeout = 120
# 将连接超时时间设置为60秒，读取超时时间设置为120秒
http_config.timeout = (60, 120)

client = VpcClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

#### 1.4 SSL 配置 [:top:](#用户手册-top)

```python
http_config = HttpConfig.get_default_config()
# 根据需要配置是否跳过SSL证书校验
http_config.ignore_ssl_verification = True
# 配置服务器端CA证书，用于SDK验证服务端证书合法性
http_config.ssl_ca_cert = '/path/to/certfile'

client = VpcClient.new_builder() \
    .with_http_config(http_config) \
    .build()
```

### 2. 认证信息配置 [:top:](#用户手册-top)

华为云服务存在两种部署方式，Region 级服务和 Global 级服务。

Global 级服务有 BSS、DevStar、EPS、IAM、RMS、TMS。

Region 级服务使用 BasicCredentials 初始化，需要提供 projectId 。

Global 级服务使用 GlobalCredentials 初始化，需要提供 domainId 。

客户端认证方式支持以下几种：

- 永久 AK&SK 认证
- 临时 AK&SK&SecurityToken 认证
- IdpId&IdTokenFile 认证

#### 2.1 使用永久 AK 和 SK [:top:](#用户手册-top)

**认证参数说明**：

- `ak` 华为云账号 Access Key
- `sk` 华为云账号 Secret Access Key
- `project_id` 云服务所在项目 ID ，根据你想操作的项目所属区域选择对应的项目 ID
- `domain_id` 华为云账号 ID

```python
# Region级服务
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
project_id = "{your projectId string}"

basic_credentials = BasicCredentials(ak, sk, project_id)

# Global级服务
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
domain_id = "{your domainId string}"

global_credentials = GlobalCredentials(ak, sk, domain_id)
```

- `3.0.26-beta` 及以上版本支持自动获取 projectId/domainId ，用户需要指定当前华为云账号的永久 AK&SK 和 对应的 region_id，同时在初始化客户端时配合 `with_region()`
  方法使用，代码示例详见 [3.2 指定Region方式（推荐）](#32-指定-region-方式-推荐-top) 。

#### 2.2 使用临时 AK 和 SK [:top:](#用户手册-top)

首先需要获得临时 AK、SK 和 SecurityToken ，可以从永久 AK&SK 获得，或者通过委托授权获得。

- 通过永久 AK&SK 获得可以参考文档：https://support.huaweicloud.com/api-iam/iam_04_0002.html ，对应 IAM SDK
  中的 `CreateTemporaryAccessKeyByToken` 方法。

- 通过委托授权获得可以参考文档：https://support.huaweicloud.com/api-iam/iam_04_0101.html ，对应 IAM SDK
  中的 `CreateTemporaryAccessKeyByAgency` 方法。

**认证参数说明**：

- `ak` 华为云账号 Access Key
- `sk` 华为云账号 Secret Access Key
- `security_token` 采用临时 AK&SK 认证场景下的安全票据
- `project_id` 云服务所在项目 ID ，根据你想操作的项目所属区域选择对应的项目 ID
- `domain_id` 华为云账号 ID

临时 AK&SK&SecurityToken 获取成功后，可使用如下方式初始化认证信息：

```python
import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials

# Region级服务
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
security_token = os.getenv("HUAWEICLOUD_SDK_SECURITY_TOKEN")
project_id = "{your projectId string}"

basic_credentials = BasicCredentials(ak, sk, project_id).with_security_token(security_token)

# Global级服务
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
security_token = os.getenv("HUAWEICLOUD_SDK_SECURITY_TOKEN")
domain_id = "{your domainId string}"

global_credentials = GlobalCredentials(ak, sk, domain_id).with_security_token(security_token)
```

#### 2.3 使用 IdpId 和 IdTokenFile [:top:](#用户手册-top)

通过OpenID Connect ID token方式获取联邦认证token, 可参考文档：[获取联邦认证token(OpenID Connect ID token方式)](https://support.huaweicloud.com/api-iam/iam_13_0605.html)

**认证参数说明**：

- `Idp_id` 身份提供商ID
- `Id_token_file` 存放id_token的文件路径，id_token由企业IdP构建，携带联邦用户身份信息
- `projec_id` 云服务所在项目 ID ，根据你想操作的项目所属区域选择对应的项目 ID
- `domain_id` 华为云账号 ID

```python
from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials

# Region级服务
basic_cred = BasicCredentials() \
    .with_idp_id(idp_id) \
    .with_id_token_file(id_token_file) \
    .with_project_id(project_id)

# Global级服务
global_cred = GlobalCredentials() \
    .with_idp_id(idp_id) \
    .with_id_token_file(id_token_file) \
    .with_domain_id(domain_id)
```

#### 2.4 认证信息管理 [:top:](#用户手册-top)

从**3.0.98**版本起，支持从各类提供器中获取认证信息

**Region级服务** 请使用 `XxxCredentialProvider.get_basic_credential_xxx_provider`

**Global级服务** 请使用 `XxxCredentialProvider.get_global_credential_xxx_provider`

##### 2.4.1 环境变量 [:top:](#用户手册-top)

**AK/SK认证**

| 环境变量  |  说明 |
| ------------ | ------------ |
| HUAWEICLOUD_SDK_AK  | 必填，AccessKey  |
| HUAWEICLOUD_SDK_SK  |  必填，SecretKey |
| HUAWEICLOUD_SDK_SECURITY_TOKEN  | 可选, 使用临时ak/sk认证时需要指定该参数  |
| HUAWEICLOUD_SDK_PROJECT_ID  | 可选，用于Region级服务，多ProjectId场景下必填  |
| HUAWEICLOUD_SDK_DOMAIN_ID  | 可选，用于Global级服务  |

配置环境变量：

```
// Linux
export HUAWEICLOUD_SDK_AK=YOUR_AK
export HUAWEICLOUD_SDK_SK=YOUR_SK

// Windows
set HUAWEICLOUD_SDK_AK=YOUR_AK
set HUAWEICLOUD_SDK_SK=YOUR_SK
```

从配置的环境变量中获取认证信息：

```python
from huaweicloudsdkcore.auth.provider import EnvCredentialProvider

# basic
basic_provider = EnvCredentialProvider.get_basic_credential_env_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = EnvCredentialProvider.get_global_credential_env_provider()
global_cred = global_provider.get_credentials()
```

**IdpId/IdTokenFile认证**

| 环境变量  |  说明 |
| ------------ | ------------ |
| HUAWEICLOUD_SDK_IDP_ID  | 必填，身份提供商ID |
| HUAWEICLOUD_SDK_ID_TOKEN_FILE  |  必填，存放id_token的文件路径 |
| HUAWEICLOUD_SDK_PROJECT_ID  | basic类型认证时，该参数必填  |
| HUAWEICLOUD_SDK_DOMAIN_ID  | global类型认证时，该参数必填  |

配置环境变量：

```
// Linux
export HUAWEICLOUD_SDK_IDP_ID=YOUR_IDP_ID
export HUAWEICLOUD_SDK_ID_TOKEN_FILE=/some_path/your_token_file
export HUAWEICLOUD_SDK_PROJECT_ID=YOUR_PROJECT_ID // basic认证时必填
export HUAWEICLOUD_SDK_DOMAIN_ID=YOUR_DOMAIN_ID // global认证时必填

// Windows
set HUAWEICLOUD_SDK_IDP_ID=YOUR_IDP_ID
set HUAWEICLOUD_SDK_ID_TOKEN_FILE=/some_path/your_token_file
set HUAWEICLOUD_SDK_PROJECT_ID=YOUR_PROJECT_ID // basic认证时必填
set HUAWEICLOUD_SDK_DOMAIN_ID=YOUR_DOMAIN_ID // global认证时必填
```

从配置的环境变量中获取认证信息：

```python
from huaweicloudsdkcore.auth.provider import EnvCredentialProvider

# basic
basic_provider = EnvCredentialProvider.get_basic_credential_env_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = EnvCredentialProvider.get_global_credential_env_provider()
global_cred = global_provider.get_credentials()
```

##### 2.4.2 配置文件 [:top:](#用户手册-top)

默认会从用户主目录下读取认证信息配置文件，linux为`~/.huaweicloud/credentials`，windows为`C:\Users\USER_NAME\.huaweicloud\credentials`，可以通过配置环境变量`HUAWEICLOUD_SDK_CREDENTIALS_FILE`来修改默认文件的路径

**AK/SK认证**

| 配置参数  |  说明 |
| ------------ | ------------ |
| ak  | 必填，AccessKey  |
| sk  |  必填，SecretKey |
| security_token  | 可选, 使用临时ak/sk认证时需要指定该参数  |
| project_id  | 可选，用于Region级服务，多ProjectId场景下必填  |
| domain_id  | 可选，用于Global级服务  |
| iam_endpoint  | 可选，用于身份认证的endpoint，默认为`https://iam.myhuaweicloud.com` |

配置文件内容如下：

```ini
[basic]
ak = your_ak
sk = your_sk

[global]
ak = your_ak
sk = your_sk
```

从配置文件中读取认证信息：

```python
from huaweicloudsdkcore.auth.provider import ProfileCredentialProvider

# basic
basic_provider = ProfileCredentialProvider.get_basic_credential_profile_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = ProfileCredentialProvider.get_global_credential_profile_provider()
global_cred = global_provider.get_credentials()
```

**IdpId/IdTokenFile认证**

| 配置参数  |  说明 |
| ------------ | ------------ |
| idp_id  | 必填，身份提供商ID |
| id_token_file  |  必填，存放id_token的文件路径 |
| project_id  | basic类型认证时，该参数必填  |
| domain_id  | global类型认证时，该参数必填  |
| iam_endpoint  | 可选，用于身份认证的endpoint，默认为`https://iam.myhuaweicloud.com` |

配置文件内容如下：

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

从配置文件中读取认证信息：

```python
from huaweicloudsdkcore.auth.provider import ProfileCredentialProvider

# basic
basic_provider = ProfileCredentialProvider.get_basic_credential_profile_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = ProfileCredentialProvider.get_global_credential_profile_provider()
global_cred = global_provider.get_credentials()
```

##### 2.4.3 实例元数据 [:top:](#用户手册-top)

从实例元数据获取临时AK/SK和securitytoken，关于元数据获取请参阅：[元数据获取](https://support.huaweicloud.com/usermanual-ecs/ecs_03_0166.html)

手动获取实例元数据认证信息：

```python
from huaweicloudsdkcore.auth.provider import MetadataCredentialProvider

# basic
basic_provider = MetadataCredentialProvider.get_basic_credential_metadata_provider()
basic_cred = basic_provider.get_credentials()

# global
global_provider = MetadataCredentialProvider.get_global_credential_metadata_provider()
global_cred = global_provider.get_credentials()
```

##### 2.4.4 认证信息提供链 [:top:](#用户手册-top)

在创建服务客户端，未显式指定认证信息时，按照顺序 **环境变量 -> 配置文件 -> 实例元数据** 尝试加载认证信息

通过提供链获取认证信息：

```python
from huaweicloudsdkcore.auth.provider import CredentialProviderChain

# basic
basic_chain = CredentialProviderChain.get_basic_credential_provider_chain()
basic_cred = basic_chain.get_credentials()

# global
global_chain = CredentialProviderChain.get_global_credential_provider_chain()
global_cred = global_chain.get_credentials()
```

支持自定义认证信息提供链：

```python
from huaweicloudsdkcore.auth.provider import CredentialProviderChain, ProfileCredentialProvider, MetadataCredentialProvider

providers = [
    ProfileCredentialProvider.get_basic_credential_profile_provider(),
    MetadataCredentialProvider.get_basic_credential_metadata_provider()
]

chain = CredentialProviderChain(providers)
credentials = chain.get_credentials()
```

### 3. 客户端初始化 [:top:](#用户手册-top)

客户端初始化有两种方式，可根据需要选择下列两种方式中的一种：

#### 3.1 指定云服务 Endpoint 方式 [:top:](#用户手册-top)

```python
# 指定终端节点，以 VPC 服务北京四的 endpoint 为例
endpoint = "https://vpc.cn-north-4.myhuaweicloud.com"

# 初始化客户端认证信息，需要填写相应 project_id/domain_id，以初始化 BasicCredentials 为例
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
project_id = "{your projectId string}"
basic_credentials = BasicCredentials(ak, sk, project_id)

# 初始化指定云服务的客户端 {Service}Client ，以初始化 Region 级服务 VPC 的 VpcClient 为例
client = VpcClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()
```

**说明:**

- `endpoint` 是华为云各服务应用区域和各服务的终端节点，详情请查看 [地区和终端节点](https://developer.huaweicloud.com/endpoint) 。

- 当用户使用指定 Region 方式无法自动获取 projectId 时，可以使用当前方式调用接口。

#### 3.2 指定 Region 方式 **（推荐）** [:top:](#用户手册-top)

```python
import os
# 增加region依赖
from huaweicloudsdkiam.v3.region.iam_region import IamRegion

# 初始化客户端认证信息，使用当前客户端初始化方式可不填 project_id/domain_id
# 以初始化 GlobalCredentials 为例
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
global_credentials = GlobalCredentials(ak, sk)

# 初始化指定云服务的客户端 {Service}Client
# 以初始化 Global 级服务 IAM 的 IamClient 为例
client = IamClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(global_credentials) \
    .with_region(IamRegion.CN_NORTH_4) \
    .build()
```

**说明:**

- 指定 Region 方式创建客户端的场景，支持自动获取用户的 projectId 或者 domainId，初始化认证信息时可无需指定相应参数。

- **不适用**于 `多ProjectId` 的场景。

- 支持指定的 Region 可通过[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint)查询。调用不支持的 region 可能会抛出 `Unsupported regionId` 的异常信息。

**两种方式对比：**

| 初始化方式 | 优势 | 劣势 |
| :---- | :---- | :---- |
| 指定云服务 Endpoint 方式 | 只要接口已在当前环境发布就可以成功调用 | 需要用户自行查找并填写 projectId 和 endpoint
| 指定 Region 方式 | 无需指定 projectId 和 endpoint，按照要求配置即可自动获取该值并回填 | 支持的服务和 region 有限制

#### 3.3 自定义配置 [:top:](#用户手册-top)

**注：**3.0.93版本起支持

##### 3.3.1 IAM endpoint配置 [:top:](#用户手册-top)

自动获取用户的 projectId 和 domainId 会分别调用统一身份认证服务的 [KeystoneListProjects](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=KeystoneListProjects) 和 [KeystoneListAuthDomains](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=KeystoneListAuthDomains) 接口，默认访问的endpoint为 https://iam.myhuaweicloud.com， **欧洲站用户需要指定 endpoint 为 https://iam.eu-west-101.myhuaweicloud.eu**

用户可以通过以下两种方式来修改endpoint

###### 3.3.1.1 全局级 [:top:](#用户手册-top)

全局范围生效，通过环境变量`HUAWEICLOUD_SDK_IAM_ENDPOINT`指定

```
//linux
export HUAWEICLOUD_SDK_IAM_ENDPOINT=https://iam.cn-north-4.myhuaweicloud.com

//windows
set HUAWEICLOUD_SDK_IAM_ENDPOINT=https://iam.cn-north-4.myhuaweicloud.com
```

###### 3.3.1.2 凭证级 [:top:](#用户手册-top)

只对单个凭证生效，会覆盖全局配置

```python
import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials

iam_endpoint = "https://iam.cn-north-4.myhuaweicloud.com"
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
credentials = BasicCredentials(ak, sk).with_iam_endpoint(iam_endpoint)
```

##### 3.3.2 Region配置 [:top:](#用户手册-top)

###### 3.3.2.1 代码配置 [:top:](#用户手册-top)

```python
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkecs.v2 import EcsClient

# 使用自定义的regionId和endpoint创建一个region
region = Region("cn-north-9", "https://ecs.cn-north-9.myhuaweicloud.com")

client = EcsClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(region) \
    .build()
```

###### 3.3.2.2 环境变量 [:top:](#用户手册-top)

通过环境变量配置，格式为`HUAWEICLOUD_SDK_REGION_{SERVICE_NAME}_{REGION_ID}={endpoint}`

注：环境变量名全大写，中划线替换为下划线

```
// 以ECS和IoTDA服务为例

// linux
export HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_9=https://ecs.cn-north-9.myhuaweicloud.com
export HUAWEICLOUD_SDK_REGION_IOTDA_AP_SOUTHEAST_1=https://iotda.ap-southwest-1.myhuaweicloud.com

// windows
set HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_9=https://ecs.cn-north-9.myhuaweicloud.com
set HUAWEICLOUD_SDK_REGION_IOTDA_AP_SOUTHEAST_1=https://iotda.ap-southwest-1.myhuaweicloud.com
```

从**3.1.62**版本起，支持配置一个region对应多个endpoint，主要endpoint无法连接会自动切换到备用endpoint

格式为`HUAWEICLOUD_SDK_REGION_{SERVICE_NAME}_{REGION_ID}={endpoint1},{endpoint2}`, 多个endpoint之间用英文逗号隔开, 比如`HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_9=https://ecs.cn-north-9.myhuaweicloud.com,https://ecs.cn-north-9.myhuaweicloud.cn`

###### 3.3.2.3 文件配置 [:top:](#用户手册-top)

通过yaml文件配置，默认会从用户主目录下读取region配置文件，linux为`~/.huaweicloud/regions.yaml`，windows为`C:\Users\USER_NAME\.huaweicloud\regions.yaml`，默认配置文件可以不存在，但是如果配置文件存在且内容格式不对会解析错误抛出异常。

可以通过配置环境变量`HUAWEICLOUD_SDK_REGIONS_FILE`来修改默认文件的路径，如`HUAWEICLOUD_SDK_REGIONS_FILE=/tmp/my_regions.yml`

文件内容格式如下：

```yaml
# 服务名不区分大小写
ECS:
  - id: 'cn-north-1'
    endpoint: 'https://ecs.cn-north-1.myhuaweicloud.com'
  - id: 'cn-north-9'
    endpoint: 'https://ecs.cn-north-9.myhuaweicloud.com'
IoTDA:
  - id: 'ap-southwest-1'
    endpoint: 'https://iotda.ap-southwest-1.myhuaweicloud.com'
```

从**3.1.62**版本起，支持配置一个region对应多个endpoint，主要endpoint无法连接会自动切换到备用endpoint，格式如下：

```yaml
ECS:
  - id: 'cn-north-1'
    endpoints:
      - 'https://ecs.cn-north-1.myhuaweicloud.com'
      - 'https://ecs.cn-north-1.myhuaweicloud.cn'
```

###### 3.3.2.4 Region提供链 [:top:](#用户手册-top)

**Region.value_of(region_id)** 默认查找顺序为 **环境变量 -> 配置文件 -> SDK中已定义Region**，以上方式都找不到region会抛出异常 **KeyError**，获取region示例：

```python
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion

region1 = EcsRegion.value_of("cn-north-1")
region2 = EcsRegion.value_of("cn-north-9")
```

### 4. 发送请求并查看响应 [:top:](#用户手册-top)

```python
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

```python
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

```python
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

```python
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

SDK 支持打印 Access 级别的访问日志，需要用户手动打开日志开关，支持打印到控制台或者指定的文件。

初始化指定服务的客户端实例，以 VpcClient 为例：

```python
client = VpcClient.new_builder() \
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

```text
2020-06-16 10:44:02,019 4568 HuaweiCloud-SDK http_handler.py 28 INFO "GET https://vpc.cn-north-1.myhuaweicloud.com/v1/0904f9e1f100d2932f94c01f9aa1cfd7/vpcs" 200 11 0:00:00.543430 b5c927ffdab8401e772e70aa49972037
```

日志格式为：

```python
%(asctime)s %(thread)d %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s
```

#### 6.2 HTTP 监听器 [:top:](#用户手册-top)

在某些场景下可能对业务发出的 HTTP 请求进行 Debug ，需要看到原始的 HTTP 请求和返回信息，SDK 提供监听器功能来获取原始的为加密的 HTTP 请求和返回信息。

> :warning:  Warning: 原始信息打印仅在 Debug 阶段使用，请不要在生产系统中将原始的 HTTP 头和 Body 信息打印到日志，这些信息并未加密且其中包含敏感数据，例如所创建虚拟机的密码，IAM 用户的密码等；当 Body 体为二进制内容，即 Content-Type 标识为二进制时，Body 为"***"，详细内容不输出。

```python
from huaweicloudsdkcore.http.http_handler import HttpHandler


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

**说明:**
HttpHandler 支持如下方法 `add_request_handler`、`add_response_handler` 。

### 7. 接口调用器 [:top:](#用户手册-top)

#### 7.1 自定义请求头 [:top:](#用户手册-top)

可以根据需要灵活地配置请求头域参数，非必要**请勿**指定诸如`Host`、`Authorization`、`User-Agent`、`Content-Type`等通用请求头，可能会导致接口调用错误。

**同步调用**

```python
client = VpcClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(VpcRegion.value_of("cn-north-4")) \
    .build()

request = ListVpcsRequest()
response = client.list_vpcs_invoker(request) \
    # 自定义请求头
    .add_header("key1", "value1") \
    .add_header("key2", "value2") \
    .invoke()
print(response)
```

**异步调用**

```python
client = VpcAsyncClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(VpcRegion.value_of("cn-north-4")) \
    .build()

request = ListVpcsRequest()
response = client.list_vpcs_async_invoker(request) \
    # 自定义请求头
    .add_header("key1", "value1") \
    .add_header("key2", "value2") \
    .invoke().result()
print(response)
```

#### 7.2 请求重试 [:top:](#用户手册-top)

`v3.1.97`版本起支持请求重试，需要配置以下参数：

- 重试条件：根据上一次请求的响应或异常来判断是否重试
- 最大重试次数：当符合重试条件时的最大重试次数，指定范围[1, 10]
- 重试策略：计算每次重试前的等待时间（毫秒）

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
# 当发生网络连接异常时进行请求重试，最大重试次数为3，重试间隔策略为立即重试
response = client.list_vpcs_invoker(request).with_retry(
    retry_condition=lambda resp, exc: isinstance(exc, ConnectionException),
    max_retries=3,
    backoff_strategy=BackoffStrategies.NONE
).invoke()

# 当服务不可用时进行请求重试，最大重试次数为10，重试间隔策略为等抖动指数退避
# response = client.list_vpcs_invoker(request).with_retry(
#     retry_condition=lambda resp, exc: isinstance(exc, ServerResponseException) and exc.status_code == 503,
#     max_retries=10,
#     backoff_strategy=BackoffStrategies.EQUAL_JITTER
# ).invoke()
```

### 8. 文件上传与下载 [:top:](#用户手册-top)

以数据安全中心服务的嵌入图片水印接口为例，该接口需要上传一个图片文件，并返回加过水印的图片文件流：

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
        # 以只读方式、二进制格式打开文件，创建一个FormFile对象
        image_file = FormFile(open("demo.jpg", "rb"))
        body = CreateImageWatermarkRequestBody(file=image_file, blind_watermark="test_watermark")
        request.body = body
        response = client.create_image_watermark(request)
        image_file.close()

        # 定义下载文件的方法
        def save(stream):
            with open("result.jpg", "wb") as f:
                f.write(stream.content)
        # 下载文件
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

### 9. FAQ [:top:](#用户手册-top)

#### 9.1 云联盟场景如何调用 [:top:](#用户手册-top)

```python
# 指定终端节点，以 云联盟都柏林节点调用 VPC 服务为例
endpoint = "https://vpc.eu-west-101.myhuaweicloud.com"

# 初始化客户端认证信息，需要填写相应 project_id/domain_id，以初始化 BasicCredentials 为例
ak = os.getenv("HUAWEICLOUD_SDK_AK")
sk = os.getenv("HUAWEICLOUD_SDK_SK")
project_id = "{your projectId string}"
basic_credentials = BasicCredentials(ak, sk, project_id)

# 初始化指定云服务的客户端 {Service}Client ，以初始化 Region 级服务 VPC 的 VpcClient 为例
client = VpcClient.new_builder() \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()
```