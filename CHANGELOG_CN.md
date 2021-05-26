# 3.0.45 2021-05-25

### HuaweiCloud SDK AS

- _新增特性_
    - 新增支持接口：
        - `ListApiVersions`
        - `ShowApiVersion`
        - `BatchProtectScalingInstances`
        - `BatchRemoveScalingInstances`
        - `CreateScalingTagInfo`
        - `BatchResumeScalingPolicies`
        - `BatchPauseScalingPolicies`
        - `PauseScalingGroup`
        - `BatchSetScalingInstancesStandby`
        - `BatchUnsetScalingInstancesStandby`
        - `ResumeScalingPolicy`
        - `PauseScalingPolicy`
- _解决问题_
    - 无
- _特性变更_
    - 接口名称调整：
        - `ExecuteScalingPolicies` -> `BatchDeleteScalingPolicies`
        - `EnableOrDisableScalingGroup` -> `ResumeScalingGroup`
        - `UpdateScalingGroupInstance` -> `BatchAddScalingInstances`
        - `CompleteLifecycleAction` -> `AttachCallbackInstanceLifeCycleHook`
    - 移除接口：
        - `DeleteScalingTags`
    - `ListScalingGroups` 接口新增参数 `enterprise_project_id`
    - `ListScalingActivityV2Logs` 接口新增参数 `log_id`

### HuaweiCloud SDK BSS

- _新增特性_
    - 新增支持接口：
        - 查询月度成本 `ListCustomerBillsMonthlyBreakDown`
        - 查询订单可用折扣 `ListOrderDiscounts`
- _解决问题_
    - 无
- _特性变更_
    - 查询客户消费记录接口 `ListSubCustomerResFeeRecords` 增加 query 参数：bill_date_begin 和 bill_date_end

### HuaweiCloud SDK CloudPipeline

- _新增特性_
    - 新增支持接口：停止流水线 `StopPipelineNew`
- _解决问题_
    - 无
- _特性变更_
    - 移除接口 `StartPipeline`、`StopPipeline`

### HuaweiCloud SDK DMS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口名称调整：（查询项目标签）ShowProjectTags -> ShowQueueProjectTags

### HuaweiCloud SDK EPS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口`ListEnterpriseProject`的请求参数`offset`从必填改为非必填

### HuaweiCloud SDK FunctionGraph

- _新增特性_
    - 新增支持接口：
        - `ListFunctionAsyncInvokeConfig`
        - `ShowFunctionAsyncInvokeConfig`
        - `DeleteFunctionAsyncInvokeConfig`
        - `UpdateFunctionAsyncInvokeConfig`
- _解决问题_
    - 无
- _特性变更_
    - 接口`DeleteVersionAlias`、`UpdateVersionAlias`、`ShowVersionAlias`的请求参数名称调整：`name` -> `alias_name`
    - 接口`DeleteFunctionTrigger`、`UpdateTrigger`、`ShowFunctionTrigger`的请求参数名称调整：`triggerId` -> `trigger_id`

### HuaweiCloud SDK IAM

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口 `CreateUsers` 新增请求体参数和响应体参数 _access_mode_
    - 接口 `DeleteBindingDevice` 将请求体参数 _authentication_code_ 设置为必填参数

### HuaweiCloud SDK Kafka

- _新增特性_
    - 新增支持接口：
        - `CreateInstanceUser`
        - `BatchDeleteInstanceUsers`
        - `ShowInstanceUsers`
        - `ShowTopicAccessPolicy`
        - `UpdateTopicAccessPolicy`
        - `ShowKafkaTopicPartitionDiskusage`
        - `ShowInstanceMessages`
        - `ResetUserPassword`
- _解决问题_
    - 无
- _特性变更_
    - 接口名称调整：
        - `ShowInstanceTags` -> `ShowKafkaTags`
        - `ShowProjectTags` -> `ShowKafkaProjectTags`
        - `BatchCreateOrDeleteInstanceTag` -> `BatchCreateOrDeleteKafkaTag`
    - 接口 `BatchCreateOrDeleteInstanceTag` 请求体名称调整：`BatchCreateOrDeleteInstanceTagRequestBody`
      -> `BatchCreateOrDeleteKafkaTagRequestBody`
    - 接口 `UpdateSinkTaskQuota` 请求体 `UpdateSinkTaskQuotaReq` 的请求参数 `sink_max_tasks` 数据类型调整：String → Integer

### HuaweiCloud SDK Meeting

- _新增特性_
    - 新增支持接口：
        - `ShowRecordingFileDownloadUrls`
        - `SearchQosParticipantDetail`
        - `SearchMemberVmrByCloudLink`
        - `SearchQosHistoryMeetings`
        - `UpdateStartedConfConfig`
        - `SearchQosParticipants`
        - `InviteUser`
        - `CreateWebSocketToken`
        - `CreateAppIdToken`
        - `SearchQosOnlineMeetings`
- _解决问题_
    - 无
- _特性变更_
    - 接口 `CreateConfToken` 修改请求参数 `X-Login-Type` 的数据类型：Integer -> String
    - 接口 `UpdateResource`, `DeleteResource` 删除请求参数 `forceEditFlag`
    - 接口 `DeleteCorp` 删除请求参数 `forceDelete`

### HuaweiCloud SDK OMS

- _新增特性_
    - 支持对象存储迁移服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK RabbitMQ

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口名称调整：
        - `BatchCreateOrDeleteInstanceTag` -> `BatchCreateOrDeleteRabbitMqTag`
        - `ShowProjectTags` -> `ShowRabbitMqProjectTags`
        - `ShowInstanceTags` -> `ShowRabbitMqTags`
    - 接口 `BatchCreateOrDeleteInstanceTag` 请求体名称调整：BatchCreateOrDeleteInstanceTagRequestBody ->
      BatchCreateOrDeleteRabbitMqTagRequestBody

# 3.0.43-rc 2021-05-14

### HuaweiCloud SDK ECS

- _新增特性_
    - 无
- _解决问题_
    - 解决了使用接口`NovaShowKeypair`获取秘钥，结果解析异常的问题
- _特性变更_
    - 无

### HuaweiCloud SDK RDS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口`ListInstances`的响应字段`type`新增结果值: `CLOUDSSD`、`LOCALSSD`
    - 接口`ListBackups`新增可选的请求参数`complete_version`
    - 将接口`ListSlowlogStatistics`的请求参数`type`从非必填改为必填

# 3.0.42-rc 2021-05-10

### HuaweiCloud SDK BMS

- _新增特性_
    - 新增支持接口`BatchCreateBaremetalServerTags`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK DDS

- _新增特性_
    - 新增支持接口`MigrateAz`、`ListAz2Migrate`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK EPS

- _新增特性_
    - 无
- _解决问题_
    - [Issue 17](https://github.com/huaweicloud/huaweicloud-sdk-go-v3/issues/17): 修复`EpDetailType`枚举定义错误的问题
- _特性变更_
    - 无

### HuaweiCloud SDK IEC

- _新增特性_
    - 支持IEC智能边缘云服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK RDS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口`ListOffSiteInstances`的响应体名称调整：`OffSiteInstanceListResponse` -> `OffSiteInstanceListResponseBody`
    - 接口`ListOffSiteInstances`的响应字段名称调整：`offsite_backup_instances` -> `offsite_backup_instance`

# 3.0.41-rc 2021-04-30

### HuaweiCloud SDK BCS

- _新增特性_
    - 新增支持查询异步操作结果的接口`ListOpRecord`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK DDS

- _新增特性_
    - 新增支持的接口
        - 查询集群均衡设置 `ShowShardingBalancer`
        - 设置集群均衡开关 `SetBalancerSwitch`
        - 设置集群均衡活动时间窗 `SetBalancerWindow`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK HSS

- _新增特性_
    - 新增支持查询弹性云服务器状态列表的接口`ListHosts`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK IAM

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 查询账号配额接口`ShowDomainQuota`的请求参数`type`增加可选值：
        - `assigment_group_mp`
        - `assigment_agency_mp`
        - `assigment_group_ep`
        - `assigment_user_ep`

### HuaweiCloud SDK IoTDA

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 下线订阅管理相关接口：
        - `ListSubscriptions`
        - `CreateSubscription`
        - `UpdateSubscription`
        - `ShowSubscription`
        - `DeleteSubscription`

### HuaweiCloud SDK MPC

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口`CreateMpeCallBack`新增请求参数`language`、`sky_switch`
    - 接口`CreateTranscodingTask`的请求参数`subtitle_type`可选值调整为`0`、`1`、`2`

### HuaweiCloud SDK ProjectMan

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 获取项目详情接口`ShowProjectInfoV4`的响应体新增字段`project_code`

# 3.0.40-rc 2021-04-15

### HuaweiCloud SDK RDS

- _新增特性_
    - 新增支持管理数据库的接口
        - `CreateSqlserverDatabase`
        - `DeleteSqlserverDatabase`
        - `ListSqlserverDatabases`
    - 新增支持管理用户的接口
        - `CreateSqlserverDbUser`
        - `ListSqlserverDbUsers`
        - `ListAuthorizedSqlserverDbUsers`
        - `DeleteSqlserverDbUser`
        - `AllowSqlserverDbUserPrivilege`
        - `RevokeSqlserverDbUserPrivilege`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK DDS

- _新增特性_
    - 新增支持接口`DeleteDatabaseUser`、`DeleteDatabaseRole`、`ShowConnectionStatistics`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ProjectMan

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口`ListIssuesV4`, `ListChildIssuesV4`响应体新增字段`closed_time` 、`id` 、`created_time`

### HuaweiCloud SDK AOM

- _新增特性_
    - 支持AOM应用运维管理服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK OCR

- _新增特性_
    - 无
- _解决问题_
    - 规范接口参数的命名
- _特性变更_
    - 无

### HuaweiCloud SDK VPC

- _新增特性_
    - 无
- _解决问题_
    - 修复问题，开放vpc和子网的标签
- _特性变更_
    - 无

# 3.0.39-rc 2021-03-30

### HuaweiCloud SDK Kafka

- _新增特性_
    - 无
- _解决问题_
    - 修复查询消息接口没有时间戳字段的问题
- _特性变更_
    - 无

### HuaweiCloud SDK Moderation

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口`RunImageModeration `增加请求参数`moderation_rule `、`ad_glossaries `
    - 接口`RunTextModeration `修改参数`category_suggestion `为`category_suggestions`
    - 修改接口`RunImageModeration `中响应参数`confidence`为`object`类型

### HuaweiCloud SDK ProjectMan

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口`ShowIssueV4`、`UpdateIssueV4`的响应体 `IssueResponseV4`增加`name`属性
    - 将接口`ShowProjectWorkHours`、`ListProjectWorkHours`的响应体`ShowProjectWorkHoursResponseBody`下的属性`work_time`
      修改为`work_date`

### HuaweiCloud SDK SMN

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 将接口`PublishMessage`的请求参数`protocol`从必填改为非必填
    - 将接口 `PublishMessage` 请求体的 `PublishMessageRequestBody` 类属性 `subject` 由必填改为非必填

# 3.0.38-rc 2021-03-26

### HuaweiCloud SDK Live

- _新增特性_
    - 无
- _解决问题_
    - 解决 ListLiveStreamsOnline 接口响应体反序列化失败的问题
- _特性变更_
    - 无

### HuaweiCloud SDK RDS

- _新增特性_
    - 无
- _解决问题_
    - 解决 ListSlowlogStatistics 接口响应体部分字段为空的问题
- _特性变更_
    - 无

### HuaweiCloud SDK SMN

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 将接口 `ListSlowlogStatistics` 下的 `property` 属性从必填调整为非必填

# 3.0.37-rc 2021-03-19

### HuaweiCloud SDK ECS

- _新增特性_
    - 无
- _解决问题_
    - 解决 ListFlavors 接口响应体反序列化出错的问题
- _特性变更_
    - 无

### HuaweiCloud SDK Meeting

- _新增特性_
    - 新增激活码管理相关接口
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.36-rc 2021-03-16

### HuaweiCloud SDK EIP

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 申请包周期弹性公网IP接口增加 `enterprise_project_id` 字段

### HuaweiCloud SDK ProjectMan

- _新增特性_
    - 无
- _解决问题_
    - 修复接口无法调用的问题
- _特性变更_
    - 无

# 3.0.35-rc 2021-03-15

### HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 当用户传入的 `endpoint` 未带协议前缀时，支持自动加上 `https` 前缀
    - 不再支持默认值回填功能

### HuaweiCloud SDK CES

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 使用资源分组创建告警规则时，维度字段调整为非必填，即 `CreateAlarmRequestBody` 类中的属性 `metric` 对应类调整：
      `MetricInfoForAlarm` → `MetricForAlarm`

### HuaweiCloud SDK DDS

- _新增特性_
    - 新增支持接口：
        - 根据备份恢复新实例 `RestoreNewInstance`
        - 查询实例节点会话 `ListSessions`
        - 终结实例节点会话 `DeleteSession`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ECS

- _新增特性_
    - 新增支持接口：查询云服务器组详情 `ShowServerGroup`
- _解决问题_
    - 无
- _特性变更_
    - 云服务器获取密码接口名调整：`ShowWindowsServerPassword` → `ShowServerPassword`
    - 云服务器清除密码接口名调整：`DeleteWindowsServerPassword` → `DeleteServerPassword`

### HuaweiCloud SDK ELB

- _新增特性_
    - 新增支持接口：查询当前租户下的后端服务器列表 `ListAllMembers`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK FunctionGraph

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口获取依赖包列表 `ListDependencies` 响应体的属性 `size` 类型调整：string → int

### HuaweiCloud SDK IAM

- _新增特性_
    - 新增支持接口：
        - 查询身份提供商详情 `KeystoneShowIdentityProvider`
        - 注册身份提供商 `KeystoneCreateIdentityProvider`
        - 更新身份提供商 `KeystoneUpdateIdentityProvider`
        - 删除身份提供商 `KeystoneDeleteIdentityProvider`
        - 获取联邦认证token(OpenId Connect Id token方式) `CreateTokenWithIdToken`
- _解决问题_
    - 无
- _特性变更_
    - 下线接口：获取联邦认证unscoped token `CreateUnscopeTokenByIdpInitiated`

### HuaweiCloud SDK IMS

- _新增特性_
    - 新增支持接口：
        - 按标签查询镜像 `ListImageByTags`
        - 查询租户所有镜像标签 `ListImagesTags`
        - 查询镜像标签 `ListImageTags`
        - 添加镜像标签 `AddImageTag`
        - 删除镜像标签 `DeleteImageTag`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ProjectMan

- _新增特性_
    - 新增支持接口：
        - 创建工作项类型自定义字段 `CreateCustomfields`
        - 查询人均bug `ShowBugsPerDeveloper`
        - 查询需求按时完成率 `ShowCompletionRate`
        - 查询缺陷密度 `ShowBugDensityV2`
        - 获取项目详情 `ShowProjectInfoV4`
- _解决问题_
    - 修改接口命名错误：`ShowtIssueCompletionRate` → `ShowIssueCompletionRate`
- _特性变更_
    - `ListProjectV4` 接口响应体中的 `created_time` 和 `updated_time` 属性类型调整：string → int

### HuaweiCloud SDK RDS

- _新增特性_
    - 支持 Postgresql 相关接口
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.34-rc 2021-02-27

### HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 优化 README 文档描述及 CHANGELOG 日志格式
    - 支持使用 `to_json_object()` 方法获取请求的响应对象

### HuaweiCloud SDK BMS

- _新增特性_
    - 无
- _解决问题_
    - 修复接口方法命名不合理的问题：`WindowsBaremetalServerCleanPwd` → `DeleteWindowsBareMetalServerPassword`
- _特性变更_
    - 无

### HuaweiCloud SDK CES

- _新增特性_
    - 无
- _解决问题_
    - 修复类 `CreateAlarmResponse` 出现循环依赖的问题
- _特性变更_
    - 无

### HuaweiCloud SDK DDS

- _新增特性_
    - 新增支持接口：获取慢日志下载链接 `DownloadSlowlog`、获取错误日志下载链接 `DownloadErrorlog`
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK DGC

- _新增特性_
    - 无
- _解决问题_
    - 修复接口方法命名不合理的问题：
        - `ModifyJob` → `UpdateJob`
        - `ModifyScript` → `UpdateScript`
        - `ModifyResource` → `UpdateResource`
- _特性变更_
    - 无

### HuaweiCloud SDK ELB

- _新增特性_
    - 无
- _解决问题_
    - 修复接口方法命名不合理的问题：`ListMenbers` → `ListMembers`
    - 修复接口 `ShowMember` 需要传 query 参数 `X-Auth-Token` 的问题
- _特性变更_
    - 无

### HuaweiCloud SDK EPS

- _新增特性_
    - 无
- _解决问题_
    - 修复接口方法命名不合理的问题：`ModifyEnterpriseProject` → `UpdateEnterpriseProject`
- _特性变更_
    - 无

### HuaweiCloud SDK IAM

- _新增特性_
    - 无
- _解决问题_
    - 修复 `KeystoneUserResult` 类中属性名的错误定义问题：`pwd_stength` → `pwd_strength`
- _特性变更_
    - 无

### HuaweiCloud SDK IoTDA

- _新增特性_
    - 下线以下接口：
        - CreateAppCertificate
        - ListAppCertificates
        - ShowAppCertificate
        - UpdateAppCertificate
        - DeleteAppCertificate
- _解决问题_
    - 无
- _特性变更_
    - 隐藏接口内部字段 `Sp-Auth-Token`、`Stage-Auth-Token`，不影响用户使用

### HuaweiCloud SDK IMS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 类 `ListImagesRequest` 中取消默认值 `disk_format='vhd'`
    - 类 `GlanceListImagesRequest` 中取消默认值 `disk_format='vhd'`

### HuaweiCloud SDK Meeting

- _新增特性_
    - 无
- _解决问题_
    - 修复接口方法命名不合理的问题：`EditMeeting` → `UpdateMeeting`
- _特性变更_
    - 无

### HuaweiCloud SDK RDS

- _新增特性_
    - 无
- _解决问题_
    - 修复接口方法命名不合理的问题：
        - `DoManualBackup` → `CreateManualBackup`
        - `ModifyConfiguration` → `UpdateConfiguration`
        - `ModifyInstanceConfiguration` → `UpdateInstanceConfiguration`
    - 修复类 `CreateInstanceResponse` 和 `CreateConfigurationResponse` 出现循环依赖的问题
- _特性变更_
    - 接口 `StartInstanceAction` 请求中单机转主备场景增加 `is_auto_pay` 属性

# 3.0.33-rc 2021-02-07

### HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 初始化客户端的 `build()` 方法中增加默认 `HttpConfig` 配置
- _特性变更_
    - 无

### HuaweiCloud SDK IMS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 查询镜像支持的OS列表(ListOsVersions)接口返回体属性 `os_bit` 数据类型调整：string → int32

### HuaweiCloud SDK IoTDA

- _新增特性_
    - 新增支持接口：查询设备下队列中的命令(ListAsyncCommands)、查询设备下的历史命令(ListAsyncHistoryCommands)、上传应用侧CA证书(CreateAppCertificate)
      、查询应用侧CA证书列表(ListAppCertificates)、查询应用侧CA证书(ShowAppCertificate)、更新应用侧CA证书(UpdateAppCertificate)、删除应用侧CA证书(
      DeleteAppCertificate)
- _解决问题_
    - 无
- _特性变更_
    - 下线支持接口（接口不在支持通过SDK调用，仍可通过API直接调用）：重置设备指纹(DeviceManagement)

### HuaweiCloud SDK Live

- _新增特性_
    - 新增支持接口：获取直播播放日志(ListLiveSampleLogs)、创建直播域名(CreateDomain)、删除直播域名(DeleteDomain)、修改直播域名(UpdateDomain)、查询直播域名(
      ShowDomain)、创建直播域名映射关系(CreateDomainMapping)、删除直播域名映射关系(DeleteDomainMapping)
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK OCR

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 所有接口响应类类名调整：xxResultBody / xxResultResponse / xxResponseBodyItems 都统一调整为 xxResult

# 3.0.32-rc 2021-01-30

### HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - HTTP请求直接返回响应体的原始json，而不是封装的对象
    - 支持直接返回异常信息

### HuaweiCloud SDK DNS

- _新增特性_
    - 支持云解析服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ECS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口名称调整: UpdateAutoTerminateTimeServer → UpdateServerAutoTerminateTime

### HuaweiCloud SDK EVS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 创建云硬盘接口支持指定专属存储池ID
    - 查询配额相关接口属性 `allocated` 类型调整: string → int

### HuaweiCloud SDK IAM

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 查询IAM用户详情接口响应体增加属性`access_mode`

### HuaweiCloud SDK OCR

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 增值税发票识别接口删除冗余属性 `issue_id` , 调整属性类型 `seller_seal` : String → List<String>

# 3.0.31-rc.1 2021-01-26

### HuaweiCloud SDK CCE

- _新增特性_
    - 无
- _解决问题_
    - 修正文件`cce_region.py`
- _特性变更_
    - 无

# 3.0.31-rc 2021-01-25

### HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 设置默认ConnectionTimeout为60秒
    - 设置默认ReadTimeout为120秒

### HuaweiCloud SDK BSS

- _新增特性_
    - 新增支持接口：查询订单可用折扣
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ECS

- _新增特性_
    - 新增支持接口：修改云服务器云主机销毁时间
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.30-rc 2021-01-15

### HuaweiCloud SDK Core

- _新增特性_
    - Region管理支持使用`value_of`方法获取`region`信息
- _解决问题_
    - 调用临时AK/SK返回异常问题修复
- _特性变更_
    - 无

### HuaweiCloud SDK DGC

- _新增特性_
    - 新增支持接口：作业相关接口（增删改查）、脚本相关接口（增删改查）、资源相关接口（增删改查）
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK IAM

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 创建/查询用户接口响应字段 `is_domain_owner` 类型调整：string → boolean

### HuaweiCloud SDK Meeting

- _新增特性_
    - 新增支持接口：查询企业的资源使用信息
- _解决问题_
    - 无
- _特性变更_
    - `预约会议` 接口增加 `是否允许来宾启动会议` 参数
    - `查询会议详情` 接口增加响应字段 `appId`、`isAutoInvite`、`isNotOverlayPidName`

### HuaweiCloud SDK RDS

- _新增特性_
    - 新增支持接口：查询跨区域备份策略、设置跨区域备份策略、获取跨区域备份列表、查询跨区域可恢复时间段、查询跨区域备份实例列表
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK SWR

- _新增特性_
    - 支持容器镜像服务
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.29-beta 2020-12-31

### HuaweiCloud SDK CloudIDE

- _新增特性_
    - 新增支持接口：查询当前账号访问权限（ShowAccountStatus）
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK DCS

- _新增特性_
    - 无
- _解决问题_
    - 修正接口返回数据类型避免反序列化失败：
        - 查询所有实例列表接口：响应参数`Tags`类型调整 Tag → ResourceTag
        - 查询慢日志接口：响应参数`duration`类型调整 int32 → string
        - 查询大key分析详情接口：响应参数`db`类型调整 int32 → string
        - 查询热key分析详情接口：响应参数`db`类型调整 int32 → string
- _特性变更_
    - 无

### HuaweiCloud SDK DGC

- _新增特性_
    - 支持数据湖治理中心服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK RDS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 创建实例接口响应类型调整

### HuaweiCloud SDK SMN

- _新增特性_
    - 无
- _解决问题_
    - 修正消息发布接口请求参数：Object → Map<String, String>
- _特性变更_
    - 无

# 3.0.28-beta 2020-12-28

### HuaweiCloud SDK DCS

- _新增特性_
    - 无
- _解决问题_
    - 修改缓存接口port类型为integer
- _特性变更_
    - 无

# 3.0.27-beta 2020-12-25

### HuaweiCloud SDK DCS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口ListInstances请求Query参数名称调整：id → instance_id

### HuaweiCloud SDK RMS

- _新增特性_
    - 新增支持接口：资源查询相关接口、Region查询相关接口
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.26-beta 2020-12-23

### HuaweiCloud SDK Core

- _新增特性_
    - 支持Region管理，用户新建客户端时可以通过{Service}Region传入，无需自己配置endpoint。配置Region后，支持自动回填ProjectId/DomainId
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK BSS

- _新增特性_
    - 新增支持接口：查询用量单位列表
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK CES

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - ShowMetricData接口字段更新

### HuaweiCloud SDK Live

- _新增特性_
    - 新增支持接口：查询播放画像信息
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK MPC

- _新增特性_
    - 新增支持接口：视频增强模板相关接口，声道合并任务相关接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK RDS

- _新增特性_
    - 支持云数据库服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK SMN

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 消息模板名称中字段类型调整

# 3.0.25-beta 2020-12-15

### HuaweiCloud SDK CCE

- _新增特性_
    - 支持云容器引擎服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ELB

- _新增特性_
    - 无
- _解决问题_
    - 创建监听器接口返回为空问题修复
    - 证书列表查询接口返回非列表问题修复
- _特性变更_
    - 无

### HuaweiCloud SDK FunctionGraph

- _新增特性_
    - 新增支持接口：更新函数预留实例个数
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Meeting

- _新增特性_
    - 新增支持接口：获取页面免登陆跳转的nonce信息
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK NAT

- _新增特性_
    - 无
- _解决问题_
    - 修复批量创建DNAT规则失败的问题
- _特性变更_
    - 无

# 3.0.24-beta 2020-12-04

### HuaweiCloud SDK SMN

- _新增特性_
    - 支持消息通知服务
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.23-beta 2020-11-30

### HuaweiCloud SDK BCS

- _新增特性_
    - 支持区块链服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK BMS

- _新增特性_
    - 支持裸金属服务器
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK BSS

- _新增特性_
    - 新增支持接口：查询使用量列表，设置/取消包周期资源到期转按需
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK CBR

- _新增特性_
    - 新增支持接口：迁移资源接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK CES

- _新增特性_
    - 新增支持接口：
        - 查询事件监控列表
        - 查询某一个事件监控详情
        - 创建资源分组
        - 更新资源分组
        - 删除资源分组
        - 查询所有资源分组
        - 修改告警规则
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ECS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - [Issue 21](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/21) 开放查询SSH密钥详情接口

### HuaweiCloud SDK IAM

- _新增特性_
    - 新增支持接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Live

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - Live服务客户端名字修正：LiveAPIClient → LiveClient

### HuaweiCloud SDK Meeting

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 创建会议接口增加字段 `callInRestriction`
    - 编辑预约会议接口增加字段 `callInRestriction`

# 3.0.22-beta 2020-11-17

### HuaweiCloud SDK DMS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 属性类型调整：属性 `创建队列的时间` 由 `string` 类型调整为 `integer64` 类型

### HuaweiCloud SDK ECS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 创建虚拟机接口（按需和包周期）增加 `dry_run` 属性，表示是否预检此次请求

### HuaweiCloud SDK NAT

- _新增特性_
    - 支持NAT网关服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Kafka

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口名调整：UpdateInstanceCrossVPCIP → UpdateInstanceCrossVpcIp

### HuaweiCloud SDK RMS

- _新增特性_
    - 支持资源管理服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK VPC

- _新增特性_
    - 支持网络ACL相关接口
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.21-beta 2020-11-11

### HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 修复请求参数中有除-_外特殊字符时model代码错误的问题
- _特性变更_
    - 无

### HuaweiCloud SDK CBR

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 创建存储库接口(CreateVault)新增存储库turbo类型
    - 修改策略接口(UpdatePolicy)删除多余字段

### HuaweiCloud SDK CES

- _新增特性_
    - 新增接口响应示例，调整字段描述
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK CloudPipeline

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 生成客户端文件的名字调整：devcloudpipeline_client → cloudpipeline_client, devcloudpipeline_async_client →
      cloudpipeline_async_client

### HuaweiCloud SDK DevStar

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 修改接口参数，调整示例代码

# 3.0.20-beta 2020-11-02

### HuaweiCloud SDK CES

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 创建告警规则接口增加资源分组字段
    - 查询告警历史接口响应体metadata修改，只返回total字段

### HuaweiCloud SDK ELB

- _新增特性_
    - 无
- _解决问题_
    - 创建转发规则接口参数名错误问题修复
- _特性变更_
    - 无

# 3.0.19-beta 2020-10-31

### HuaweiCloud SDK CBR

- _新增特性_
    - 新增支持接口：TAG标签相关接口
- _解决问题_
    - [Issue 17](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/17) 修复ListBackups接口响应体问题
- _特性变更_
    - 无

### HuaweiCloud SDK CTS

- _新增特性_
    - 新增支持接口：ListQuotas（查询租户追踪器配额信息）
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK EPS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口名称调整，原有的`*EP`接口展开为`*EnterpriseProject`，涉及接口：
        1. ListEP → ListEnterpriseProject
        2. CreateEP → CreateEnterpriseProject
        3. ShowEP → ShowEnterpriseProject
        4. ModifyEP → ModifyEnterpriseProject
        5. EnableEP → EnableEnterpriseProject
        6. ShowEPQuota → ShowEnterpriseProjectQuota
        7. ShowResourceBindEP → ShowResourceBindEnterpriseProject
        8. DisableEP → DisableEnterpriseProject

### HuaweiCloud SDK FunctionGraph

- _新增特性_
    - 新增支持接口：更新触发器、获取指定时间段的函数运行指标、租户函数统计信息、查询租户配额
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Iam

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口名称调整，涉及接口：
        1. KeystoneCreateUserTokenByPasswordAndMFA → KeystoneCreateUserTokenByPasswordAndMfa
        2. CreateUnscopeTokenByIDPInitiated → CreateUnscopeTokenByIdpInitiated

### HuaweiCloud SDK ProjectMan

- _新增特性_
    - 新增支持接口：迭代信息、用户信息、项目成员、项目信息、项目指标、项目统计等相关方法的接口
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.18-beta 2020-10-20

### HuaweiCloud SDK DCS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 接口名中去掉冗余的Dcs服务名

### HuaweiCloud SDK ELB

- _新增特性_
    - 增加v2版本接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK IoTDA

- _新增特性_
    - 增加规则相关接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Meeting

- _新增特性_
    - 增加支持接口
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.17-beta 2020-10-14

### HuaweiCloud SDK BSS

- _新增特性_
    - 伙伴中心支持导出产品目录价
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK DCS

- _新增特性_
    - 增加支持接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Live

- _新增特性_
    - 新增直播V2接口
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.16-beta 2020-10-12

### HuaweiCloud SDK CTS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 删除v1版本废弃接口

### HuaweiCloud SDK DevStar

- _新增特性_
    - 无
- _解决问题_
    - 服务客户端认证类型调整为全局认证，即GlobalCredentials
- _特性变更_
    - 无

# 3.0.15-beta 2020-09-30

## Huaweicloud SDK ELB

- _新增特性_
    - 支持弹性负载均衡服务
- _解决问题_
    - 无
- _特性变更_
    - 无

## Huaweicloud SDK EIP

- _新增特性_
    - 支持弹性公网IP服务
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.14-beta 2020-09-24

### HuaweiCloud SDK BSS

- _新增特性_
    - 无
- _解决问题_
    - 修复BssClient类无法加载的问题
- _特性变更_
    - 无

### HuaweiCloud SDK TestHub

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 原TestHub服务名变更为CloudTest，原命名无法正常上线SDK中心。

# 3.0.13-beta 2020-09-16

### HuaweiCloud SDK ECS

- _新增特性_
    - 无
- _解决问题_
    - 修正接口参数类型
- _特性变更_
    - 无

### HuaweiCloud SDK BSS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 运营能力开放接口更新

### HuaweiCloud SDK Live

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 修改禁播参数描述

# 3.0.12-beta 2020-09-11

### HuaweiCloud SDK Meeting

- _新增特性_
    - 无
- _解决问题_
    - 修复创建认证凭证失败的问题
- _特性变更_
    - 无

# 3.0.11-beta 2020-09-09

### HuaweiCloud SDK DMS

- _新增特性_
    - 支持分布式消息服务，提供Kafka专享版和RabbitMQ专享版
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Meeting

- _新增特性_
    - 新增支持接口：会议控制/会议管理
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK VPC

- _新增特性_
    - 无
- _解决问题_
    - 修复安全组相关接口类型错误的问题
- _特性变更_
    - 无

# 3.0.10-beta 2020-09-04

### HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 修复yaml中没有定义format的整型枚举参数无法生成枚举代码的问题
- _特性变更_
    - 调整Http请求头的User-Agent信息

# 3.0.9-beta 2020-08-28

### HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 解决类型多层嵌套时最内层类型丢失的问题
- _特性变更_
    - 无

### HuaweiCloud SDK BSS

- _新增特性_
    - 支持运营能力开发服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK CloudPipeline

- _新增特性_
    - 支持流水线服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK FunctionGraph

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 调整服务名，由缩写FGS调整为全称FunctionGraph

### HuaweiCloud SDK IAM

- _新增特性_
    - 新增支持接口：console一致性相关接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK IoTDA

- _新增特性_
    - 新增支持接口：批量操作接口和异步接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Meeting

- _新增特性_
    - 新增支持接口：会议纪要相关接口
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ProjectMan

- _新增特性_
    - 支持项目管理服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK VPC

- _新增特性_
    - 新增支持接口：安全组、安全组规则和可用IP数
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.8-beta 2020-8-14

### HuaweiCloud SDK Core

- _新增特性_
    - 支持临时AK/SK认证模式
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK APIG

- _新增特性_
    - 支持API网关
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK CloudIDE

- _新增特性_
    - 支持云测服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK KMS

- _新增特性_
    - 支持密钥管理服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK Live

- _新增特性_
    - 支持视频直播服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK MPC

- _新增特性_
    - 支持媒体转码服务
- _解决问题_
    - 无
- _特性变更_
    - 无

### HuaweiCloud SDK ServiceStage

- _新增特性_
    - 支持应用管理与运维平台
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.7-beta 2020-07-30

## HuaweiCloud SDK CBR

- _新增特性_
    - 支持云备份服务
- _解决问题_
    - 无
- _特性变更_
    - 无

## HuaweiCloud SDK ECS

- _新增特性_
    - 新增支持接口，如变更操作系统 / 重置密码
- _解决问题_
    - 无
- _特性变更_
    - 无

## HuaweiCloud SDK VPC

- _新增特性_
    - 支持VPC v3版本的接口
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.6-beta 2020-07-15

## HuaweiCloud SDK Core

- _新增特性_
    - 支持上传下载
- _解决问题_
    - 无
- _特性变更_
    - 无

## Examples

- _新增特性_
    - 无
- _解决问题_
    - [Issue #1](https://github.com/huaweicloud/huaweicloud-sdk-python-v3/issues/1)：修复list vpc示例
- _特性变更_
    - 无

## HuaweiCloud SDK IAM

- _新增特性_
    - 无
- _解决问题_
    - 修复keystoneListVersions响应体解析失败问题
- _特性变更_
    - 无

## HuaweiCloud SDK IoTDA

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 支持资源空间相关接口

## HuaweiCloud SDK Meeting

- _新增特性_
    - 新增会议控制/会议管理功能
- _解决问题_
    - 无
- _特性变更_
    - 无

## HuaweiCloud SDK EPS

- _新增特性_
    - 支持企业管理服务
- _解决问题_
    - 无
- _特性变更_
    - 无

## HuaweiCloud SDK EVS

- _新增特性_
    - 无
- _解决问题_
    - [Issue #3](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/3)：获取单个磁盘详情接口报错问题修复
- _特性变更_
    - 无

## HuaweiCloud SDK TMS

- _新增特性_
    - 支持标签管理服务
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.5-beta 2020-06-30

## HuaweiCloud SDK Core

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 使用with_http_handler替代原有的with_enable_http_log开关，支持用户在问题定位场景自定义请求日志输出

## HuaweiCloud SDK CTS

- _新增特性_
    - 支持云审计服务
- _解决问题_
    - 无
- _特性变更_
    - 无

## HuaweiCloud SDK EVS

- _新增特性_
    - 无
- _解决问题_
    - 无
- _特性变更_
    - 支持全量服务接口

## HuaweiCloud SDK IoTDA

- _新增特性_
    - 支持设备接入服务
- _解决问题_
    - 无
- _特性变更_
    - 无

# 3.0.3-beta 2020-06-15

## HuaweiCloud SDK Core

- _新增特性_
    - 支持异步客户端
    - 支持日志
    - 问题定位场景，支持打开HTTP日志
- _解决问题_
    - 无
- _特性变更_
    - 无

## HuaweiCloud SDK DevStar

- _新增特性_
    - 支持查询模板列表
    - 支持查询模板详情
    - 支持查询任务状态
    - 支持通过DevStar模板创建生成应用代码任务
- _解决问题_
    - 无
- _特性变更_
    - 无
