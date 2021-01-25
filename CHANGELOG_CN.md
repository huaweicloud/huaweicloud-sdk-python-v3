## 3.0.31-rc 2021-01-25
## HuaweiCloud SDK Core
- ### 新增特性
    - 无
- ### 解决问题
    - 无
- ### 特性变更
    - 设置默认ConnectionTimeout为60秒
    - 设置默认ReadTimeout为120秒

## HuaweiCloud SDK BSS
- ### 新增特性
    - 新增支持接口：查询订单可用折扣
- ### 解决问题
    - 无
- ### 特性变更
    - 无

## HuaweiCloud SDK ECS
- ### 新增特性
    - 新增支持接口：修改云服务器云主机销毁时间
- ### 解决问题
    - 无
- ### 特性变更
    - 无


## 3.0.30-rc 2021-01-15
## HuaweiCloud SDK Core
- ### 新增特性
    - Region管理支持使用`value_of`方法获取`region`信息
- ### 解决问题
    - 调用临时AK/SK返回异常问题修复
- ### 特性变更
    - 无

## HuaweiCloud SDK DGC
- ### 新增特性
    - 新增支持接口：作业相关接口（增删改查）、脚本相关接口（增删改查）、资源相关接口（增删改查）
- ### 解决问题
    - 无
- ### 特性变更
    - 无

## HuaweiCloud SDK IAM
- ### 新增特性
    - 无
- ### 解决问题
    - 无
- ### 特性变更
    - 创建/查询用户接口响应字段 `is_domain_owner` 类型调整：string → boolean

## HuaweiCloud SDK Meeting
- ### 新增特性
    - 新增支持接口：查询企业的资源使用信息
- ### 解决问题
    - 无
- ### 特性变更
    - `预约会议` 接口增加 `是否允许来宾启动会议` 参数
    - `查询会议详情` 接口增加响应字段 `appId`、`isAutoInvite`、`isNotOverlayPidName`

## HuaweiCloud SDK RDS
- ### 新增特性
    - 新增支持接口：查询跨区域备份策略、设置跨区域备份策略、获取跨区域备份列表、查询跨区域可恢复时间段、查询跨区域备份实例列表
- ### 解决问题
    - 无
- ### 特性变更
    - 无

## HuaweiCloud SDK SWR
- ### 新增特性
    - 支持容器镜像服务
- ### 解决问题
    - 无
- ### 特性变更
    - 无


## 3.0.29-beta 2020-12-31
## HuaweiCloud SDK CloudIDE
 - ### 新增特性
    - 新增支持接口：查询当前账号访问权限（ShowAccountStatus）
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK DCS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修正接口返回数据类型避免反序列化失败：
        - 查询所有实例列表接口：响应参数`Tags`类型调整 Tag → ResourceTag
        - 查询慢日志接口：响应参数`duration`类型调整 int32 → string
        - 查询大key分析详情接口：响应参数`db`类型调整 int32 → string
        - 查询热key分析详情接口：响应参数`db`类型调整 int32 → string
 - ### 特性变更
    - 无

## HuaweiCloud SDK DGC
 - ### 新增特性
    - 支持数据湖治理中心服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK RDS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 创建实例接口响应类型调整

## HuaweiCloud SDK SMN
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修正消息发布接口请求参数：Object → Map<String, String>
 - ### 特性变更
    - 无


## 3.0.28-beta 2020-12-28
## HuaweiCloud SDK DCS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修改缓存接口port类型为integer
 - ### 特性变更
    - 无


## 3.0.27-beta 2020-12-25
## HuaweiCloud SDK DCS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 接口ListInstances请求Query参数名称调整：id → instance_id

## HuaweiCloud SDK RMS
 - ### 新增特性
    - 新增支持接口：资源查询相关接口、Region查询相关接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## 3.0.26-beta 2020-12-23
## HuaweiCloud SDK Core
 - ### 新增特性
    - 支持Region管理，用户新建客户端时可以通过{Service}Region传入，无需自己配置endpoint。配置Region后，支持自动回填ProjectId/DomainId
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK BSS
 - ### 新增特性
    - 新增支持接口：查询用量单位列表
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK CES
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - ShowMetricData接口字段更新

## HuaweiCloud SDK Live
 - ### 新增特性
    - 新增支持接口：查询播放画像信息
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK MPC
 - ### 新增特性
    - 新增支持接口：视频增强模板相关接口，声道合并任务相关接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK RDS
 - ### 新增特性
    - 支持云数据库服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK SMN
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 消息模板名称中字段类型调整

## 3.0.25-beta 2020-12-15
## HuaweiCloud SDK CCE
 - ### 新增特性
    - 支持云容器引擎服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK ELB
 - ### 新增特性
    - 无
 - ### 解决问题
    - 创建监听器接口返回为空问题修复
    - 证书列表查询接口返回非列表问题修复
 - ### 特性变更
    - 无

## HuaweiCloud SDK FunctionGraph
 - ### 新增特性
    - 新增支持接口：更新函数预留实例个数
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK Meeting
 - ### 新增特性
    - 新增支持接口：获取页面免登陆跳转的nonce信息
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK NAT
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修复批量创建DNAT规则失败的问题
 - ### 特性变更
    - 无


## 3.0.24-beta 2020-12-04
## HuaweiCloud SDK SMN
 - ### 新增特性
    - 支持消息通知服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


## 3.0.23-beta 2020-11-30
## HuaweiCloud SDK BCS
 - ### 新增特性
    - 支持区块链服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK BMS
 - ### 新增特性
    - 支持裸金属服务器
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK BSS
 - ### 新增特性
    - 新增支持接口：查询使用量列表，设置/取消包周期资源到期转按需
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK CBR
 - ### 新增特性
    - 新增支持接口：迁移资源接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK CES
 - ### 新增特性
    - 新增支持接口：
     - 查询事件监控列表
     - 查询某一个事件监控详情
     - 创建资源分组
     - 更新资源分组
     - 删除资源分组
     - 查询所有资源分组
     - 修改告警规则
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK ECS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - [Issue 21](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/21) 开放查询SSH密钥详情接口

## HuaweiCloud SDK IAM
 - ### 新增特性
    - 新增支持接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK Live
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - Live服务客户端名字修正：LiveAPIClient → LiveClient

## HuaweiCloud SDK Meeting
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 创建会议接口增加字段 `callInRestriction`
    - 编辑预约会议接口增加字段 `callInRestriction`


## 3.0.22-beta 2020-11-17
## HuaweiCloud SDK DMS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 属性类型调整：属性 `创建队列的时间` 由 `string` 类型调整为 `integer64` 类型

## HuaweiCloud SDK ECS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 创建虚拟机接口（按需和包周期）增加 `dry_run` 属性，表示是否预检此次请求

## HuaweiCloud SDK NAT
 - ### 新增特性
    - 支持NAT网关服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK Kafka
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 接口名调整：UpdateInstanceCrossVPCIP → UpdateInstanceCrossVpcIp

## HuaweiCloud SDK RMS
 - ### 新增特性
    - 支持资源管理服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK VPC
 - ### 新增特性
    - 支持网络ACL相关接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


## 3.0.21-beta 2020-11-11
## HuaweiCloud SDK Core
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修复请求参数中有除-_外特殊字符时model代码错误的问题
 - ### 特性变更
    - 无

## HuaweiCloud SDK CBR
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 创建存储库接口(CreateVault)新增存储库turbo类型
    - 修改策略接口(UpdatePolicy)删除多余字段

## HuaweiCloud SDK CES
 - ### 新增特性
    - 新增接口响应示例，调整字段描述
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK CloudPipeline
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 生成客户端文件的名字调整：devcloudpipeline_client → cloudpipeline_client, devcloudpipeline_async_client → cloudpipeline_async_client

## HuaweiCloud SDK DevStar
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 修改接口参数，调整示例代码


## 3.0.20-beta 2020-11-02
## HuaweiCloud SDK CES
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 创建告警规则接口增加资源分组字段
    - 查询告警历史接口响应体metadata修改，只返回total字段

## HuaweiCloud SDK ELB
 - ### 新增特性
    - 无
 - ### 解决问题
    - 创建转发规则接口参数名错误问题修复
 - ### 特性变更
    - 无


## 3.0.19-beta 2020-10-31
## HuaweiCloud SDK CBR
 - ### 新增特性
    - 新增支持接口：TAG标签相关接口
 - ### 解决问题
    - [Issue 17](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/17) 修复ListBackups接口响应体问题
 - ### 特性变更
    - 无

## HuaweiCloud SDK CTS
 - ### 新增特性
    - 新增支持接口：ListQuotas（查询租户追踪器配额信息）
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK EPS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 接口名称调整，原有的`*EP`接口展开为`*EnterpriseProject`，涉及接口：
     1. ListEP → ListEnterpriseProject
     2. CreateEP → CreateEnterpriseProject
     3. ShowEP → ShowEnterpriseProject
     4. ModifyEP → ModifyEnterpriseProject
     5. EnableEP → EnableEnterpriseProject
     6. ShowEPQuota → ShowEnterpriseProjectQuota
     7. ShowResourceBindEP → ShowResourceBindEnterpriseProject
     8. DisableEP → DisableEnterpriseProject

## HuaweiCloud SDK FunctionGraph
 - ### 新增特性
    - 新增支持接口：更新触发器、获取指定时间段的函数运行指标、租户函数统计信息、查询租户配额
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK Iam
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 接口名称调整，涉及接口：
     1. KeystoneCreateUserTokenByPasswordAndMFA → KeystoneCreateUserTokenByPasswordAndMfa
     2. CreateUnscopeTokenByIDPInitiated → CreateUnscopeTokenByIdpInitiated

## HuaweiCloud SDK ProjectMan
 - ### 新增特性
    - 新增支持接口：迭代信息、用户信息、项目成员、项目信息、项目指标、项目统计等相关方法的接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


## 3.0.18-beta 2020-10-20
## HuaweiCloud SDK DCS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 接口名中去掉冗余的Dcs服务名

## HuaweiCloud SDK ELB
 - ### 新增特性
    - 增加v2版本接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK IoTDA
 - ### 新增特性
    - 增加规则相关接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK Meeting
 - ### 新增特性
    - 增加支持接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


## 3.0.17-beta 2020-10-14
## HuaweiCloud SDK BSS
 - ### 新增特性
    - 伙伴中心支持导出产品目录价
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK DCS
 - ### 新增特性
    - 增加支持接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK Live
 - ### 新增特性
    - 新增直播V2接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


## 3.0.16-beta 2020-10-12
## HuaweiCloud SDK CTS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 删除v1版本废弃接口

## HuaweiCloud SDK DevStar
 - ### 新增特性
    - 无
 - ### 解决问题
    - 服务客户端认证类型调整为全局认证，即GlobalCredentials
 - ### 特性变更
    - 无


## 3.0.15-beta 2020-09-30
## Huaweicloud SDK ELB
 - ### 新增特性
    - 支持弹性负载均衡服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## Huaweicloud SDK EIP
 - ### 新增特性
    - 支持弹性公网IP服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


## 3.0.14-beta 2020-09-24
## HuaweiCloud SDK BSS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修复BssClient类无法加载的问题
 - ### 特性变更
    - 无

## HuaweiCloud SDK TestHub
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 原TestHub服务名变更为CloudTest，原命名无法正常上线SDK中心。 


## 3.0.13-beta 2020-09-16
## HuaweiCloud SDK ECS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修正接口参数类型
 - ### 特性变更
    - 无

## HuaweiCloud SDK BSS
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 运营能力开放接口更新

## HuaweiCloud SDK Live
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 修改禁播参数描述


## 3.0.12-beta 2020-09-11
## HuaweiCloud SDK Meeting
 - ### 新增特性
    - 无 
 - ### 解决问题
    - 修复创建认证凭证失败的问题
 - ### 特性变更
    - 无 


# 3.0.11-beta 2020-09-09
## HuaweiCloud SDK DMS
 - ### 新增特性
    - 支持分布式消息服务，提供Kafka专享版和RabbitMQ专享版
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无 

## HuaweiCloud SDK Meeting
 - ### 新增特性
    - 新增支持接口：会议控制/会议管理
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK VPC
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修复安全组相关接口类型错误的问题
 - ### 特性变更
    - 无


# 3.0.10-beta 2020-09-04
## HuaweiCloud SDK Core
 - ### 新增特性
    - 无
 - ### 解决问题
    - 修复yaml中没有定义format的整型枚举参数无法生成枚举代码的问题
 - ### 特性变更
    - 调整Http请求头的User-Agent信息


# 3.0.9-beta 2020-08-28
## HuaweiCloud SDK Core
 - ### 新增特性
    - 无
 - ### 解决问题
    - 解决类型多层嵌套时最内层类型丢失的问题
 - ### 特性变更
    - 无

## HuaweiCloud SDK BSS
 - ### 新增特性
    - 支持运营能力开发服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK CloudPipeline
 - ### 新增特性
    - 支持流水线服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK FunctionGraph
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 调整服务名，由缩写FGS调整为全称FunctionGraph

## HuaweiCloud SDK IAM
 - ### 新增特性
    - 新增支持接口：console一致性相关接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK IoTDA
 - ### 新增特性
    - 新增支持接口：批量操作接口和异步接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK Meeting
 - ### 新增特性
    - 新增支持接口：会议纪要相关接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK ProjectMan
 - ### 新增特性
    - 支持项目管理服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK VPC
 - ### 新增特性
    - 新增支持接口：安全组、安全组规则和可用IP数
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


# 3.0.8-beta 2020-8-14
## HuaweiCloud SDK Core
 - ### 新增特性
    - 支持临时AK/SK认证模式
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK APIG
 - ### 新增特性
    - 支持API网关
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK CloudIDE
 - ### 新增特性
    - 支持云测服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK KMS
 - ### 新增特性
    - 支持密钥管理服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK Live
 - ### 新增特性
    - 支持视频直播服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK MPC
 - ### 新增特性
    - 支持媒体转码服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## HuaweiCloud SDK ServiceStage
 - ### 新增特性
    - 支持应用管理与运维平台
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


# __3.0.7-beta__ __2020-07-30__
## __HuaweiCloud SDK CBR__
 - ### 新增特性
    - 支持云备份服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## __HuaweiCloud SDK ECS__
 - ### 新增特性
    - 新增支持接口，如变更操作系统 / 重置密码
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## __HuaweiCloud SDK VPC__
 - ### 新增特性
    - 支持VPC v3版本的接口
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


# __3.0.6-beta__ __2020-07-15__
## __HuaweiCloud SDK Core__
  - ### 新增特性
    - 支持上传下载
  - ### 解决问题
    - 无
  - ### 特性变更
    - 无
    
## __Examples__
  - ### 新增特性
    - 无
  - ### 解决问题
    - [Issue #1](https://github.com/huaweicloud/huaweicloud-sdk-python-v3/issues/1)：修复list vpc示例
  - ### 特性变更
    - 无

## __HuaweiCloud SDK IAM__
  - ### 新增特性
     - 无
  - ### 解决问题
     - 修复keystoneListVersions响应体解析失败问题
  - ### 特性变更
     - 无

## __HuaweiCloud SDK IoTDA__
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 支持资源空间相关接口

## __HuaweiCloud SDK Meeting__
  - ### 新增特性
    - 新增会议控制/会议管理功能
  - ### 解决问题
    - 无
  - ### 特性变更
    - 无
    
## __HuaweiCloud SDK EPS__
 - ### 新增特性
    - 支持企业管理服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无

## __HuaweiCloud SDK EVS__
 - ### 新增特性
    - 无
 - ### 解决问题
    - [Issue #3](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/3)：获取单个磁盘详情接口报错问题修复
 - ### 特性变更
    - 无

## __HuaweiCloud SDK TMS__
 - ### 新增特性
    - 支持标签管理服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无


# __3.0.5-beta__ __2020-06-30__
## __HuaweiCloud SDK Core__
  - ### 新增特性
    - 无
  - ### 解决问题
    - 无
  - ### 特性变更
    - 使用with_http_handler替代原有的with_enable_http_log开关，支持用户在问题定位场景自定义请求日志输出
    
## __HuaweiCloud SDK CTS__
 - ### 新增特性
    - 支持云审计服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无
     
## __HuaweiCloud SDK EVS__
 - ### 新增特性
    - 无
 - ### 解决问题
    - 无
 - ### 特性变更
    - 支持全量服务接口
            
## __HuaweiCloud SDK IoTDA__
 - ### 新增特性
    - 支持设备接入服务
 - ### 解决问题
    - 无
 - ### 特性变更
    - 无
    

# __3.0.3-beta__ __2020-06-15__
## __HuaweiCloud SDK Core__
  - ### 新增特性
    - 支持异步客户端
    - 支持日志
    - 问题定位场景，支持打开HTTP日志
  - ### 解决问题
    - 无
  - ### 特性变更
    - 无

## __HuaweiCloud SDK DevStar__
  - ### 新增特性
    - 支持查询模板列表
    - 支持查询模板详情
    - 支持查询任务状态
    - 支持通过DevStar模板创建生成应用代码任务
  - ### 解决问题
    - 无
  - ### 特性变更
    - 无
