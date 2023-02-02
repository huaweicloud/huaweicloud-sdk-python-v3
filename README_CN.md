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
- 调用前请根据实际情况替换如下变量：`{your ak string}`、 `{your sk string}`、 `{your endpoint}` 以及 `{your project id}`。

```python
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
* [7. 文件上传与下载](#7-文件上传与下载-top)

### 1. 客户端连接参数 [:top:](#用户手册-top)

#### 1.1 默认配置 [:top:](#用户手册-top)

```python
from huaweicloudsdkcore.http.http_config import HttpConfig

# 使用默认配置
config = HttpConfig.get_default_config()
```

#### 1.2 网络代理 [:top:](#用户手册-top)

```python
# 根据需要配置网络代理
config.proxy_protocol = 'http'
config.proxy_host = 'proxy.huaweicloud.com'
config.proxy_port = 80
config.proxy_user = 'username'
config.proxy_password = 'password'
```

#### 1.3 超时配置 [:top:](#用户手册-top)

```python
# 默认连接超时时间为60秒，读取超时时间为120秒
# 将连接超时时间和读取超时时间统一设置为120秒
config.timeout = 120
# 将连接超时时间设置为60秒，读取超时时间设置为120秒
config.timeout = (60, 120)
```

#### 1.4 SSL 配置 [:top:](#用户手册-top)

```python
# 根据需要配置是否跳过SSL证书校验
config.ignore_ssl_verification = True
# 配置服务器端CA证书，用于SDK验证服务端证书合法性
config.ssl_ca_cert = ssl_ca_cert
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
basic_credentials = BasicCredentials(ak, sk, project_id)

# Global级服务
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
from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials

# Region级服务
basic_credentials = BasicCredentials(ak, sk, project_id).with_security_token(security_token)

# Global级服务
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
# 增加region依赖
from huaweicloudsdkiam.v3.region.iam_region import IamRegion

# 初始化客户端认证信息，使用当前客户端初始化方式可不填 project_id/domain_id
# 以初始化 GlobalCredentials 为例
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

- 当前支持指定 Region 方式初始化客户端的 region_id : af-south-1, ap-southeast-1, ap-southeast-2, ap-southeast-3, cn-east-2, cn-east-3,
  cn-north-1, cn-north-4, cn-south-1, cn-southwest-2, ru-northwest-2。调用其他 region 可能会抛出 `Unsupported regionId` 的异常信息。

**两种方式对比：**

| 初始化方式 | 优势 | 劣势 |
| :---- | :---- | :---- | 
| 指定云服务 Endpoint 方式 | 只要接口已在当前环境发布就可以成功调用 | 需要用户自行查找并填写 projectId 和 endpoint
| 指定 Region 方式 | 无需指定 projectId 和 endpoint，按照要求配置即可自动获取该值并回填 | 支持的服务和 region 有限制

#### 3.3 自定义配置 [:top:](#用户手册-top)

**注：**3.0.93版本起支持

##### 3.3.1 IAM endpoint配置

自动获取用户的 projectId 和 domainId 会分别调用统一身份认证服务的 [KeystoneListProjects](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=KeystoneListProjects) 和 [KeystoneListAuthDomains](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=KeystoneListAuthDomains) 接口，默认访问的endpoint为 https://iam.myhuaweicloud.com

用户可以通过以下两种方式来修改endpoint

###### 3.3.1.1 全局级

全局范围生效，通过环境变量`HUAWEICLOUD_SDK_IAM_ENDPOINT`指定

```
//linux
export HUAWEICLOUD_SDK_IAM_ENDPOINT=https://iam.cn-north-4.myhuaweicloud.com

//windows
set HUAWEICLOUD_SDK_IAM_ENDPOINT=https://iam.cn-north-4.myhuaweicloud.com
```

###### 3.3.1.2 凭证级

只对单个凭证生效，会覆盖全局配置

```python
from huaweicloudsdkcore.auth.credentials import BasicCredentials

iam_endpoint = "https://iam.cn-north-4.myhuaweicloud.com"
credentials = BasicCredentials(ak, sk).with_iam_endpoint(iam_endpoint)
```

##### 3.3.2 Region配置

###### 3.3.2.1 环境变量

通过环境变量配置，格式为`HUAWEICLOUD_SDK_REGION_{SERIVCE_NAME}_{REGION_ID}={endpoint}`

注：环境变量名全大写，中划线替换为下划线

```
// 以ECS和IoTDA服务为例

// linux
export HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_99=https://ecs.cn-north-99.myhuaweicloud.com
export HUAWEICLOUD_SDK_REGION_IOTDA_AP_SOUTHEAST_10=https://iotda.ap-southwest-10.myhuaweicloud.com

// windows
set HUAWEICLOUD_SDK_REGION_ECS_CN_NORTH_99=https://ecs.cn-north-99.myhuaweicloud.com
set HUAWEICLOUD_SDK_REGION_IOTDA_AP_SOUTHEAST_10=https://iotda.ap-southwest-10.myhuaweicloud.com
```

###### 3.3.2.2 文件配置

通过yaml文件配置，默认会从用户主目录下读取region配置文件，linux为`~/.huaweicloud/regions.yaml`，windows为`C:\Users\USER_NAME\.huaweicloud\regions.yaml`，默认配置文件可以不存在，但是如果配置文件存在且内容格式不对会解析错误抛出异常。

可以通过配置环境变量`HUAWEICLOUD_SDK_REGIONS_FILE`来修改默认文件的路径，如`HUAWEICLOUD_SDK_REGIONS_FILE=/tmp/my_regions.yml`

文件内容格式如下：

```yaml
# 服务名不区分大小写
ECS:
  - id: 'cn-north-10'
    endpoint: 'https://ecs.cn-north-10.myhuaweicloud.com'
  - id: 'cn-north-11'
    endpoint: 'https://ecs.cn-north-11.myhuaweicloud.com'
IoTDA:
  - id: 'ap-southwest-9'
    endpoint: 'https://iotda.ap-southwest-9.myhuaweicloud.com'
```

###### 3.3.2.3 Region提供链

默认查找顺序为 **环境变量 -> 配置文件 -> SDK中已定义Region**，以上方式都找不到region会抛出异常，获取region示例：

```python
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion

region1 = EcsRegion.value_of("cn-north-10")
region2 = EcsRegion.value_of("cn-north-11")
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

### 7. 文件上传与下载 [:top:](#用户手册-top)

以数据安全中心服务的嵌入图片水印接口为例，该接口需要上传一个图片文件，并返回加过水印的图片文件流：

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
