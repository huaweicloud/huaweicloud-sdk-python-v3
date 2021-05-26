# 3.0.45 2021-05-25

### HuaweiCloud SDK AS

- _Features_
    - Support more interfaces:
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
- _Bug Fix_
    - None
- _Change_
    - Modify the operation name of the following interfaces:
        - from `ExecuteScalingPolicies` to `BatchDeleteScalingPolicies`
        - from `EnableOrDisableScalingGroup` to `ResumeScalingGroup`
        - from `UpdateScalingGroupInstance` to `BatchAddScalingInstances`
        - from `CompleteLifecycleAction` to `AttachCallbackInstanceLifeCycleHook`
    - Remove the interface: `DeleteScalingTags`
    - Add the parameter `enterprise_project_id` to the interface `ListScalingGroups`.
    - Add the parameter `log_id` to the interface `ListScalingActivityV2Logs`.

### HuaweiCloud SDK BSS

- _Features_
    - Support interface `ListCustomerBillsMonthlyBreakDown` and `ListOrderDiscounts`.
- _Bug Fix_
    - None
- _Change_
    - Add query parameter _bill_date_begin_ and _bill_date_end_ to interface `ListSubCustomerResFeeRecords`.

### HuaweiCloud SDK CloudPipeline

- _Features_
    - Support interface: `StopPipelineNew`.
- _Bug Fix_
    - None
- _Change_
    - Remove interfaces `StartPipeline`, `StopPipeline`.

### HuaweiCloud SDK DMS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the name of interface from `ShowProjectTags` to `ShowQueueProjectTags`.

### HuaweiCloud SDK EPS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Change request parameter `offset` of interface `ListEnterpriseProject` from required to optional.

### HuaweiCloud SDK FunctionGraph

- _Features_
    - Support more interfaces:
        - `ListFunctionAsyncInvokeConfig`
        - `ShowFunctionAsyncInvokeConfig`
        - `DeleteFunctionAsyncInvokeConfig`
        - `UpdateFunctionAsyncInvokeConfig`
- _Bug Fix_
    - None
- _Change_
    - Modify the name of request parameter of interfaces `DeleteVersionAlias`,`UpdateVersionAlias`
      ,`ShowVersionAlias`: `name` -> `alias_name`
    - Modify the name of request parameter of interfaces `DeleteFunctionTrigger`,`UpdateTrigger`
      ,`ShowFunctionTrigger`: `triggerId` -> `trigger_id`

### HuaweiCloud SDK IAM

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the parameter `access_mode` to interface `CreateUsers`.
    - Change the parameter `authentication_code` of interface `DeleteBindingDevice` from required to optional.

### HuaweiCloud SDK Kafka

- _Features_
    - Support more interfaces:
        - `CreateInstanceUser`
        - `BatchDeleteInstanceUsers`
        - `ShowInstanceUsers`
        - `ShowTopicAccessPolicy`
        - `UpdateTopicAccessPolicy`
        - `ShowKafkaTopicPartitionDiskusage`
        - `ShowInstanceMessages`
        - `ResetUserPassword`
- _Bug Fix_
    - None
- _Change_
    - Modify the name of the interface:
        - from `ShowInstanceTags` to `ShowKafkaTags`
        - from `ShowProjectTags` to `ShowKafkaProjectTags`
        - from `BatchCreateOrDeleteInstanceTag` to `BatchCreateOrDeleteKafkaTag`
    - Modify the request body name of the interface:
        - from `BatchCreateOrDeleteInstanceTagRequestBody` to `BatchCreateOrDeleteKafkaTagRequestBody`
    - Modify the data type of parameter `sink_max_tasks` in the request body of interface `UpdateSinkTaskQuota` from
      String to Integer.

### HuaweiCloud SDK Meeting

- _Features_
    - Support more interfaces:
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
- _Bug Fix_
    - None
- _Change_
    - Modify the data type of parameter `X-Login-Type` of interface `CreateConfToken` from Integer to String.
    - Delete the unused parameter `forceEditFlag` of interface `UpdateResource` and `DeleteResource`.
    - Delete the unused parameter `forceDelete` of interface `DeleteCorp`.

### HuaweiCloud SDK OMS

- _Features_
    - Support `Object Storage Migration Service`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK RabbitMQ

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the name of the following interfaces:
        - from `BatchCreateOrDeleteInstanceTag` to `BatchCreateOrDeleteRabbitMqTag`;
        - from `ShowProjectTags` to `ShowRabbitMqProjectTags`;
        - from `ShowInstanceTags` to `ShowRabbitMqTags`.
    - Modify the request body name of interface `BatchCreateOrDeleteInstanceTag`
      from `BatchCreateOrDeleteInstanceTagRequestBody` to
      `BatchCreateOrDeleteRabbitMqTagRequestBody`.

# 3.0.43-rc 2021-05-14

### HuaweiCloud SDK ECS

- _Features_
    - None
- _Bug Fix_
    - Solve the issue of abnormal parsing result when using interface `NovaShowKeypair` to obtain the secret key.
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add new result values `CLOUDSSD` and `LOCALSSD` to response field `type` of interface `ListInstances`.
    - Add an optional request parameter `complete_version` to interface `ListBackups`.
    - Change request parameter `type` of interface `ListSlowlogStatistics` from optional to required.

# 3.0.42-rc 2021-05-10

### HuaweiCloud SDK BMS

- _Features_
    - Support interface `BatchCreateBaremetalServerTags`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DDS

- _Features_
    - Support interfaces `MigrateAz`, `ListAz2Migrate`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK EPS

- _Features_
    - None
- _Bug Fix_
    - [Issue 17](https://github.com/huaweicloud/huaweicloud-sdk-go-v3/issues/17): Fix the issue that `EpDetailType` enum
      is defined incorrectly.
- _Change_
    - None

### HuaweiCloud SDK IEC

- _Features_
    - Support `Intelligent EdgeCloud` service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the name of response body of interface `ListOffSiteInstances`: `OffSiteInstanceListResponse`
      -> `OffSiteInstanceListResponseBody`
    - Modify the name of response field of interface `ListOffSiteInstances`: `offsite_backup_instances`
      -> `offsite_backup_instance`

# 3.0.41-rc 2021-04-30

### HuaweiCloud SDK BCS

- _Features_
    - Support interface `ListOpRecord`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DDS

- _Features_
    - Support interfaces:
        - `ShowShardingBalancer`
        - `SetBalancerSwitch`
        - `SetBalancerWindow`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK HSS

- _Features_
    - Support interface `ListHosts`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK IAM

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add optional values to request parameter `type` of the interface `ShowDomainQuota`:
        - `assigment_group_mp`
        - `assigment_agency_mp`
        - `assigment_group_ep`
        - `assigment_user_ep`

### HuaweiCloud SDK IoTDA

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove interfaces:
        - `ListSubscriptions`
        - `CreateSubscription`
        - `UpdateSubscription`
        - `ShowSubscription`
        - `DeleteSubscription`

### HuaweiCloud SDK MPC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add request parameters `language`、`sky_switch` to the interface `CreateMpeCallBack`.
    - Update optional values of request parameter `subtitle_type` of interface `CreateTranscodingTask`.

### HuaweiCloud SDK ProjectMan

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add a field `project_code` to response body of the interface `ShowProjectInfoV4`.

# 3.0.40-rc 2021-04-15

### HuaweiCloud SDK RDS

- _Features_
    - Support more interfaces about database management operations.
        - `CreateSqlserverDatabase`
        - `DeleteSqlserverDatabase`
        - `ListSqlserverDatabases`
    - Support more interfaces about user management operations.
        - `CreateSqlserverDbUser`
        - `ListSqlserverDbUsers`
        - `ListAuthorizedSqlserverDbUsers`
        - `DeleteSqlserverDbUser`
        - `AllowSqlserverDbUserPrivilege`
        - `RevokeSqlserverDbUserPrivilege`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DDS

- _Features_
    - Support more interfaces `DeleteDatabaseUser`,`DeleteDatabaseRole`,`ShowConnectionStatistics`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ProjectMan

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add fields `closed_time` ,`id` ,`created_time` to reponse body of interfaces `ListIssuesV4`, `ListChildIssuesV4`.

### HuaweiCloud SDK AOM

- _Features_
    - Support `Application Operations Management` service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK OCR

- _Features_
    - None
- _Bug Fix_
    - Standardize the naming of interface parameters.
- _Change_
    - None

### HuaweiCloud SDK VPC

- _Features_
    - None
- _Bug Fix_
    - Fix the bug, open the tags of the VPC and subnet.
- _Change_
    - None

# 3.0.39-rc 2021-03-30

### HuaweiCloud SDK Kafka

- _Features_
    - None
- _Bug Fix_
    - Fix the issue that the interface for querying messages does not contain the timestamp field.
- _Change_
    - None

### HuaweiCloud SDK Moderation

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add request parameters `moderation_rule` and `ad_glossaries` to interface `RunImageModeration`.
    - Change the parameter `category_suggestion` to `category_suggestions` of the interface  `RunTextModeration`.
    - Change the type of the response parameter `confidence` to `object` of the interface `RunImageModeration `.

### HuaweiCloud SDK ProjectMan

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the attribute `name` to the response body `IssueResponseV4` of the interfaces `ShowIssueV4`
      and `UpdateIssueV4`.
    - Change the attribute `work_time` to `work_date` in `ShowProjectWorkHoursResponseBody` in the response body of the
      interfaces `ShowProjectWorkHours` and `ListProjectWorkHours`.

### HuaweiCloud SDK SMN

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Change the request parameter `protocol`  of the interface `PublishMessage`  from mandatory to optional.
    - Change the attribute `subject`  of the class `PublishMessageRequestBody` in the request body of the
      interface `PublishMessage`  from mandatory to optional.

# 3.0.38-rc 2021-03-26

### HuaweiCloud SDK Live

- _Features_
    - None
- _Bug Fix_
    - Fix the problem of deserialization error of the response of interface `ListLiveStreamsOnline`.
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - None
- _Bug Fix_
    - Fix the problem that some fields in the response body of interface `ListSlowlogStatistics` are empty.
- _Change_
    - None

### HuaweiCloud SDK SMN

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Change the property `protocol` in `ListMessageTemplates` from required to optional.

# 3.0.37-rc 2021-03-19

### HuaweiCloud SDK ECS

- _Features_
    - None
- _Bug Fix_
    - Fix the problem of deserialization failure of response body of interface `ListFlavors`.
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support more interfaces related to active code management.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.36-rc 2021-03-16

### HuaweiCloud SDK EIP

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add request field `enterprise_project_id` in interface `CreatePrePaidPublicip`.

### HuaweiCloud SDK ProjectMan

- _Features_
    - None
- _Bug Fix_
    - Fix the problem that the SDK can not be used.
- _Change_
    - None

# 3.0.35-rc 2021-03-15

### HuaweiCloud SDK Core

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - If the `endpoint` input by the user does not contain a protocol prefix, the `https` prefix will be automatically
      added.
    - Do not support the default values of the optional parameters anymore.

### HuaweiCloud SDK CES

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Class adjustment in interface `CreateAlarmRequestBody`: change class definition of property `metric`
      from `MetricInfoForAlarm` to `MetricForAlarm`.

### HuaweiCloud SDK DDS

- _Features_
    - Support more interfaces:
        - `RestoreNewInstance`
        - `ListSessions`
        - `DeleteSession`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ECS

- _Features_
    - Support more interface: `ShowServerGroup`.
- _Bug Fix_
    - None
- _Change_
    - Change the interface name from `ShowWindowsServerPassword` to `ShowServerPassword`.
    - Change the interface name from `DeleteWindowsServerPassword` to `DeleteServerPassword`.

### HuaweiCloud SDK ELB

- _Features_
    - Support more interface: `ListAllMembers`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK FunctionGraph

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Interface `ListDependencies` adjustment: change the data type of property `size` of the response definition from
      string to int.

### HuaweiCloud SDK IAM

- _Features_
    - Support more interfaces:
        - `KeystoneShowIdentityProvider`
        - `KeystoneCreateIdentityProvider`
        - `KeystoneUpdateIdentityProvider`
        - `KeystoneDeleteIdentityProvider`
        - `CreateTokenWithIdToken`
- _Bug Fix_
    - None
- _Change_
    - Do not support interface `CreateUnscopeTokenByIdpInitiated` anymore.

### HuaweiCloud SDK IMS

- _Features_
    - Support more interfaces:
        - `ListImageByTags` which mead list images queried by tags.
        - `ListImagesTags` which means list all tags of all images in current account.
        - `ListImageTags` which means list all tags of specified image.
        - `AddImageTag`
        - `DeleteImageTag`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ProjectMan

- _Features_
    - Support more interfaces:
        - `CreateCustomfields`
        - `ShowBugsPerDeveloper`
        - `ShowCompletionRate`
        - `ShowBugDensityV2`
        - `ShowProjectInfoV4`
- _Bug Fix_
    - Change the incorrect name of interface from `ShowtIssueCompletionRate` to `ShowIssueCompletionRate`.
- _Change_
    - Change the data type of property `created_time` and `updated_time` in class `ListProjectV4ResponseBody` from
      string to int.

### HuaweiCloud SDK RDS

- _Features_
    - Support `Postgresql` related interfaces.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.34-rc 2021-02-27

### HuaweiCloud SDK Core

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Optimize the description of `README` and the format of `CHANGELOG`.
    - Support to use method `to_json_object()` to get response object of your requests.

### HuaweiCloud SDK BMS

- _Features_
    - None
- _Bug Fix_
    - Correct operation name from `WindowsBaremetalServerCleanPwd` to `DeleteWindowsBareMetalServerPassword`.
- _Change_
    - None

### HuaweiCloud SDK CES

- _Features_
    - None
- _Bug Fix_
    - Fix the problem of circular dependency in the `CreateAlarmResponse` class.
- _Change_
    - None

### HuaweiCloud SDK DDS

- _Features_
    - Support more interfaces: `DownloadSlowlog` and `DownloadErrorlog`.
- _Bug Fix_
    - Correct operation name from `ModifyConfigurationParameter` to `UpdateConfigurationParameter`, change the class
      name of this operation from `ModifyConfigurationParameterRequestBody` to `UpdateConfigurationParameterRequestBody`
      .
- _Change_
    - None

### HuaweiCloud SDK DGC

- _Features_
    - None
- _Bug Fix_
    - Correct operation name from `ModifyJob` to `UpdateJob`.
    - Correct operation name from `ModifyScript` to `UpdateScript`.
    - Correct operation name from `ModifyResource` to `UpdateResource`.
- _Change_
    - None

### HuaweiCloud SDK ELB

- _Features_
    - None
- _Bug Fix_
    - Correct operation name from `ListMenbers` to `ListMembers`.
- _Change_
    - None

### HuaweiCloud SDK EPS

- _Features_
    - None
- _Bug Fix_
    - Correct operation name from `ModifyEnterpriseProject` to `UpdateEnterpriseProject`.
- _Change_
    - None

### HuaweiCloud SDK IAM

- _Features_
    - None
- _Bug Fix_
    - Correct property from `pwd_stength` to `pwd_strength` in class `KeystoneUserResult`.
- _Change_
    - None

### HuaweiCloud SDK IoTDA

- _Features_
    - Offline the following interfaces:
        - CreateAppCertificate
        - ListAppCertificates
        - ShowAppCertificate
        - UpdateAppCertificate
        - DeleteAppCertificate
- _Bug Fix_
    - None
- _Change_
    - Hide the internal fields `Sp-Auth-Token` and `Stage-Auth-Token` of all interfaces which doesn't affect actual use
      in SDK.

### HuaweiCloud SDK IMS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Delete the default value `disk_format='vhd'` in the class `ListImagesRequest`.
    - Delete the default value `disk_format='vhd'` in the class `GlanceListImagesRequest`.

### HuaweiCloud SDK Meeting

- _Features_
    - None
- _Bug Fix_
    - Correct operation name from `EditMeeting` to `UpdateMeeting`.
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - None
- _Bug Fix_
    - Correct operation name from `DoManualBackup` to `CreateManualBackup`.
    - Correct operation name from `ModifyConfiguration` to `UpdateConfiguration`.
    - Correct operation name from `ModifyInstanceConfiguration` to `UpdateInstanceConfiguration`.
    - Fix the problem of circular dependency in the classes of `CreateInstanceResponse`
      and `CreateConfigurationResponse`.
- _Change_
    - Add property `is_auto_pay` to the operation `StartInstanceAction` in the scenario of changing a single-node system
      to a primary/standby mode.

# 3.0.33-rc 2021-02-07

### HuaweiCloud SDK Core

- _Features_
    - None
- _Bug Fix_
    - Add default config of `HttpConfig` when initialing a service client using function `build()`.
- _Change_
    - None

### HuaweiCloud SDK IMS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Interface `ListOsVersions` adjustment: change the data type of `os_bit` which is the property of response of the
      interface from string to integer.

### HuaweiCloud SDK IoTDA

- _Features_
    - Support more interfaces: ListAsyncCommands, ListAsyncHistoryCommands, CreateAppCertificate, ListAppCertificates,
      ShowAppCertificate, UpdateAppCertificate, DeleteAppCertificate
- _Bug Fix_
    - None
- _Change_
    - SDK of interface `DeviceManagement` deprecated.(It's not supported any more in SDK, but you can also using it by
      customized coding using API.)

### HuaweiCloud SDK Live

- _Features_
    - Support more interfaces: ListLiveSampleLogs, CreateDomain, DeleteDomain, UpdateDomain, ShowDomain,
      CreateDomainMapping, DeleteDomainMapping
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK OCR

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Interfaces adjustment: change the class name of response of all interfaces from `xxResultBody`
      or `xxResultResponse`
      or `xxResponseBodyItems` to `xxResult`.

# 3.0.32-rc 2021-01-30

### HuaweiCloud SDK DNS

- _Features_
    - Support `Domain Name Service`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ECS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Change interface name from `UpdateAutoTerminateTimeServer` to `UpdateServerAutoTerminateTime`.

### HuaweiCloud SDK EVS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Interface `CinderCreateVolume` is supported to specify the id of dedicated storage pool using
      property `OS-SCH-HNT:scheduler_hints`.
    - Modify property type of `allocated` of class `QuotaDetails` from `String` to `Integer`.

### HuaweiCloud SDK IAM

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Increases the property `access_mode` of response class of interface `ShowUser`.

# 3.0.31-rc.1 2021-01-26

### HuaweiCloud SDK CCE

- _Features_
    - None
- _Bug Fix_
    - Modify file `cce_region.py`.
- _Change_
    - None

# 3.0.31-rc 2021-01-25

### HuaweiCloud SDK Core

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - The default value of `ConnectionTimeout` is set to 60 seconds.
    - The default value of `ReadTimeout` is set to 120 seconds.

### HuaweiCloud SDK BSS

- _Features_
    - Support more interface: ListOrderDiscounts.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ECS

- _Features_
    - Support more interface: UpdateAutoTerminateTimeServer.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.30-rc 2021-01-15

### HuaweiCloud SDK Core

- _Features_
    - Support function `value_of` to get region information.
- _Bug Fix_
    - Fix response exception when using temporary AK/SK.
- _Change_
    - None

### HuaweiCloud SDK IAM

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the data type of response field `is_domain_owner` from string to boolean of interface `ShowUser`
      and `CreateUser`.

### HuaweiCloud SDK Meeting

- _Features_
    - Support more interface: ShowOrgRes
- _Bug Fix_
    - None
- _Change_
    - Interface `CreateMeeting` supports parameter `allowGuestStartConf`.
    - Add response fields of `ShowMeetingDetail`: `appId`, `isAutoInvite`, `isNotOverlayPidName`.

### HuaweiCloud SDK RDS

- _Features_
    - Support more interfaces: ShowOffSiteBackupPolicy, SetOffSiteBackupPolicy, ListOffSiteBackups,
      ListOffSiteRestoreTimes, ListOffSiteRestoreTimes
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK SWR

- _Features_
    - Support `Software Repository for Container` service.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.29-beta 2020-12-31

### HuaweiCloud SDK CloudIDE

- _Features_
    - Support more interface: ShowAccountStatus
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DCS

- _Features_
    - None
- _Bug Fix_
    - Modify the interface return data type to prevent deserialization failure:
        - ListSlowlog: change data type of `Tags` from Tag to ResourceTag.
        - ListInstances: change data type of `duration` from int32 to string.
        - ShowBigkeyScanTaskDetails: change data type of `db` from int32 to string.
        - ShowHotkeyTaskDetails: change data type of `db` from int32 to string.
- _Change_
    - None

### HuaweiCloud SDK DGC

- _Features_
    - Support `Data Lake Governance Center` service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Interface modification: response type of interface `CreateInstance` adjustment.

### HuaweiCloud SDK SMN

- _Features_
    - None
- _Bug Fix_
    - Modify the request parameters of interface `PublishMessage` from Object to Map<String, String>
- _Change_
    - None

# 3.0.28-beta 2020-12-28

### HuaweiCloud SDK DCS

- _Features_
    - None
- _Bug Fix_
    - Change property type of `port` from string to integer.
- _Change_
    - None

# 3.0.27-beta 2020-12-25

### HuaweiCloud SDK DCS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Query parameter in interface `ListInstances` modification: id → instance_id.

### HuaweiCloud SDK RMS

- _Features_
    - Support more interfaces: `Resources` related interfaces and `Region` related interfaces.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.26-beta 2020-12-23

### HuaweiCloud SDK Core

- _Features_
    - Support Endpoint Resolver: it's supported to use {Service}Region when initializing {ServiceClient} which can
      automatically backfill endpoint. After choosing a region, the projectId/domainId will be backfilled automatically.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK BSS

- _Features_
    - Support more interfaces: ListMeasureUnits.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CES

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Update interface: ShowMetricData

### HuaweiCloud SDK DLI

- _Features_
    - Support Data Lake Insight service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Live

- _Features_
    - Support more interfaces: ShowStreamPortrait.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK MPC

- _Features_
    - Support more interfaces: QualityEnhanceTemplate related interfaces and MergeChannelsTask related interfaces.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - Support Relational Database Service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK SMN

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Update field type in message_template_name.

# 3.0.25-beta 2020-12-15

### HuaweiCloud SDK CCE

- _Features_
    - Support Cloud Container Engine service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ELB

- _Features_
    - None
- _Bug Fix_
    - Fix the problem that sending request to interface `CreateListener` returns empty response.
    - Fix the problem that sending request to interface `CreateListener` returns response with wrong type.
- _Change_
    - None

### HuaweiCloud SDK FunctionGraph

- _Features_
    - Support more interfaces: UpdateFunctionReservedInstances.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support more interfaces: CreatePortalRefNonce.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK NAT

- _Features_
    - None
- _Bug Fix_
    - Fix the problem that using interface `BatchCreateNatGatewayDnatRules` failed.
- _Change_
    - None

# 3.0.24-beta 2020-12-04

### HuaweiCloud SDK SMN

- _Features_
    - Support Simple Message Notification service.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.23-beta 2020-11-30

### HuaweiCloud SDK BCS

- _Features_
    - Support BlockChain Service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK BMS

- _Features_
    - Support Bare Metal Server service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK BSS

- _Features_
    - Support more interfaces: ListUsageTypes, ModPeriodToOnDemand.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CBR

- _Features_
    - Support more interfaces: MigrateVaultResource.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CES

- _Features_
    - Support more interfaces:
        - ListEvents
        - ListEventDetail
        - CreateResourceGroup
        - UpdateResourceGroup
        - DeleteResourceGroup
        - ListResourceGroup
        - UpdateAlarm
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ECS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - [Issue 21](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/21) Open related interface.

### HuaweiCloud SDK IAM

- _Features_
    - Support more interfaces.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Live

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Name of service client modification: LiveAPIClient → LiveClient.

### HuaweiCloud SDK Meeting

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Property of interface `CreateMeeting` adjustment: increase property `callInRestriction`.
    - Property of interface `EditMeeting` adjustment: increase property `callInRestriction`.

# 3.0.22-beta 2020-11-17

### HuaweiCloud SDK DMS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Type of property adjustment: type of property `created` and type of `eff_date` are changed from `string`
      to `integer64`.

### HuaweiCloud SDK ECS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Property adjustment:  increase property `dry_run` in interfaces `CreatePostPaidServers` and `CreateServers` which
      means whether parameters will be checked before sending real requests.

### HuaweiCloud SDK NAT

- _Features_
    - Support NAT Gateway service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Kafka

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Name of interface adjustment: UpdateInstanceCrossVPCIP → UpdateInstanceCrossVpcIp

### HuaweiCloud SDK RMS

- _Features_
    - Support Resource Manager Service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK VPC

- _Features_
    - Support more interfaces: interfaces related to Network ACLs.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.21-beta 2020-11-11

### HuaweiCloud SDK Core

- _Features_
    - None
- _Bug Fix_
    - Fix the problem of parameter conversion error when special characters exclude `-` and `_` are in query paramters.
- _Change_
    - None

### HuaweiCloud SDK CBR

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Interface adjustment: property `object_type` in interface `CreateVault` support key `turbo`.
    - Interface adjustment: property `description` in interface `UpdatePolicy` is removed.

### HuaweiCloud SDK CES

- _Features_
    - Add examples of interface response and adjust some filed description.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CloudPipeline

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the name of generated Client class: devcloudpipeline_client → cloudpipeline_client,
      devcloudpipeline_async_client → cloudpipeline_async_client

### HuaweiCloud SDK DevStar

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify interface parameters and adjust sample code.

# 3.0.20-beta 2020-11-02

### HuaweiCloud SDK CES

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Interface adjustment: property `alarm_type` in class `CreateAlarmRequestBody` support key `RESOURCE_GROUP`.
    - Interface adjustment: property `meta_data` in class `ListAlarmHistoriesResponse` only returns total number of
      alarm histories.

### HuaweiCloud SDK ELB

- _Features_
    - None
- _Bug Fix_
    - Modify wrong parameter in class `CreateL7ruleRequestBody`.
- _Change_
    - None

# 3.0.19-beta 2020-10-31

### HuaweiCloud SDK CBR

- _Features_
    - Support more interfaces: interfaces related to `TAG`.
- _Bug Fix_
    - [Issue 17](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/17) fix the problem of interface:
      ListBackups.
- _Change_
    - None

### HuaweiCloud SDK CTS

- _Features_
    - Support more interface: ListQuotas
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK EPS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Adjust interfaces' names, replace abbreviations of `EP` with `EnterpriseProject`, the involved interfaces are:
        1. ListEP → ListEnterpriseProject
        2. CreateEP → CreateEnterpriseProject
        3. ShowEP → ShowEnterpriseProject
        4. ModifyEP → ModifyEnterpriseProject
        5. EnableEP → EnableEnterpriseProject
        6. ShowEPQuota → ShowEnterpriseProjectQuota
        7. ShowResourceBindEP → ShowResourceBindEnterpriseProject
        8. DisableEP → DisableEnterpriseProject

### HuaweiCloud SDK FunctionGraph

- _Features_
    - Support more interfaces: UpdateTrigger, ListFunctionStatistics, ListStatistics, ListQuotas
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK IAM

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Adjust interfaces' names, the involved interfaces are:
        1. KeystoneCreateUserTokenByPasswordAndMFA → KeystoneCreateUserTokenByPasswordAndMfa
        2. CreateUnscopeTokenByIDPInitiated → CreateUnscopeTokenByIdpInitiated

### HuaweiCloud SDK ProjectMan

- _Features_
    - Support more interfaces: iteration information, user information, project members, project information, project
      indicators, project statistics, etc.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.18-beta 2020-10-20

### HuaweiCloud SDK DCS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove redundant `Dcs` in interfaces.

### HuaweiCloud SDK ELB

- _Features_
    - Support more interfaces of version v2.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK IoTDA

- _Features_
    - Support more interfaces related to rules.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support more interfaces.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.17-beta 2020-10-14

### HuaweiCloud SDK BSS

- _Features_
    - Partner center supports exporting product catalog prices.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DCS

- _Features_
    - Support more interfaces.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Live

- _Features_
    - Support more interfaces of version v2 of Live.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.16-beta 2020-10-12

### HuaweiCloud SDK CTS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Delete deprecated interfaces of version v1.

### HuaweiCloud SDK DevStar

- _Features_
    - None
- _Bug Fix_
    - Modify the credential type of DevStarClient: the correct credential type is GlobalCredentials.
- _Change_
    - None

# 3.0.15-beta 2020-09-30

### HuaweiCloud SDK ELB

- _Features_
    - Support Elastic Load Balance service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK EIP

- _Features_
    - Support Elastic IP service.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.14-beta 2020-09-24

### HuaweiCloud SDK BSS

- _Features_
    - None
- _Bug Fix_
    - Fix the problem that the class `BssClient` cannot be loaded.
- _Change_
    - None

### HuaweiCloud SDK TestHub

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - The original service name `TestHub` has been changed to `CloudTest`, because `TestHub` couldn't be published in
      SDK Center successfully.

# 3.0.13-beta 2020-09-16

### HuaweiCloud SDK ECS

- _Features_
    - None
- _Bug Fix_
    - Fix parameter type of interfaces.
- _Change_
    - None

### HuaweiCloud SDK BSS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Update interfaces.

### HuaweiCloud SDK Live

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Adjust descriptions of banned interface.

# 3.0.12-beta 2020-09-11

### HuaweiCloud SDK Meeting

- _Features_
    - None
- _Bug Fix_
    - Fix failed to create credentials
- _Change_
    - None

# 3.0.11-beta 2020-09-09

### HuaweiCloud SDK DMS

- _Features_
    - Support Distributed Message Services, provide Kafka premium instances and RabbitMQ premium instances with
      dedicated resources.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support more APIs: Meeting Control / Meeting Management.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK VPC

- _Features_
    - None
- _Bug Fix_
    - Fix the problem that security group related interfaces have wrong data type.
- _Change_
    - None

# 3.0.10-beta 2020-09-04

### HuaweiCloud SDK Core

- _Features_
    - None
- _Bug Fix_
    - Fix the problem that the enumeration code cannot be generated for integer enumeration parameters without format
      defined in yaml.
- _Change_
    - Modify User Agent of Http Request header.

# 3.0.9-beta 2020-08-28

### HuaweiCloud SDK Core

- _Features_
    - None
- _Bug Fix_
    - Solve the problem of losing innermost type when data types are nested in multiple layers.
- _Change_
    - None

### HuaweiCloud SDK BSS

- _Features_
    - Support Business Support System service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CloudPipeline

- _Features_
    - Support CloudPipeline service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK FunctionGraph

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify service name, change abbreviation FGS to full name FunctionGraph.

### HuaweiCloud SDK IAM

- _Features_
    - Support more APIs: consistency of console related APIs.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK IoTDA

- _Features_
    - Support more APIs: batch operation related APIs and asynchronous related APIs.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support more APIs: meeting minutes related APIs.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ProjectMan

- _Features_
    - Support Project Management service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK VPC

- _Features_
    - Support more APIs: security group, security group rules, available IP count related APIs.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.8-beta 2020-8-14

### HuaweiCloud SDK Core

- _Features_
    - Support temporary AK/SK authentication mode.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK APIG

- _Features_
    - Support API Gateway service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CloudIDE

- _Features_
    - Support Cloud IDE service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK KMS

- _Features_
    - Support Key Management Service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Live

- _Features_
    - Support Live Service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK MPC

- _Features_
    - Support Media Processing Center.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ServiceStage

- _Features_
    - Support ServiceStage.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.7-beta 2020-07-30

### HuaweiCloud SDK CBR

- _Features_
    - Support Cloud Backup and Recovery Service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK ECS

- _Features_
    - Publish new interfaces, such as ChangeServerOs and ResetServerPassword.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK VPC

- _Features_
    - Support interfaces of version v3.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.6-beta 2020-07-15

### HuaweiCloud SDK Core

- _Features_
    - Support file upload and download.
- _Bug Fix_
    - None
- _Change_
    - None

## Example

- _Features_
    - None
- _Bug Fix_
    - [Issue #1](https://github.com/huaweicloud/huaweicloud-sdk-python-v3/issues/1): Fix test vpc example.
- _Change_
    - None

### HuaweiCloud SDK IAM

- _Features_
    - None
- _Bug Fix_
    - Fix parsing failure of response body of interface keystoneListVersions.
- _Change_
    - None

### HuaweiCloud SDK IoTDA

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Support related interfaces of application management.

### HuaweiCloud SDK Meeting

- _Features_
    - Support cloud meeting management and control services.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK EPS

- _Features_
    - Support Enterprise Project Management Service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK EVS

- _Features_
    - None
- _Bug Fix_
    - [Issue #3](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/3): Fix call error of interface
      ShowVolume.
- _Change_
    - None

### HuaweiCloud SDK TMS

- _Features_
    - Support Tag Management Service.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.5-beta 2020-6-30

### HuaweiCloud SDK Core

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Use with_http_handler to replace with_enable_http_log to support users to customize the request log output in the
      troubleshooting scenario.

### HuaweiCloud SDK CTS

- _Features_
    - Support Cloud Trace Service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK EVS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Support full service interface.

### HuaweiCloud SDK IoTDA

- _Features_
    - Support IoT Device Access Service.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.3-beta 2020-06-15

### HuaweiCloud SDK Core

- _Features_
    - Support async client.
    - Support logs.
    - Support enable http logs for troubleshooting.
- _Bug Fix_
    - None
- _Change_
    - None
