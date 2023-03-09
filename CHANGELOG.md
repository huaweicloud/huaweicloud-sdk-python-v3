# 3.1.30 2023-03-09

### HuaweiCloud SDK AOS

- _Features_
  - Support the following interfaces：
    - `ListTemplates`
    - `DeleteTemplate`
    - `ShowTemplateMetadata`
    - `UpdateTemplateMetadata`
    - `ShowTemplateVersionContent`
    - `DeleteTemplateVersion`
    - `ShowTemplateVersionMetadata`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListExecutionPlans`:
    - Add the enum values `APPLY_IN_PROGRESS` to the response parameter `status`
    - The response parameter `stack_name`, `execution_plan_name` changed to required
  - Remove the enum values `IN_PLACE_UPDATE` from the response parameter `action` from the interface `GetExecutionPlan`
  - The response parameter `stack_name`, `execution_plan_name` changed to required of the interface `GetExecutionPlanMetadata`
  - Add the response parameter `resource_attributes` to the interface `ListStackResources`
  - Changes of the interface `EstimateExecutionPlanPrice`:
    - Add the response parameter `unsupported_message`
    - Modify the type `object` -> `double` of the response parameter `sale_price`
    - Modify the type `object` -> `double` of the response parameter `discount`
    - Modify the type `object` -> `double` of the response parameter `original_price`
    - Remove the enum values `WEEK` from the response parameter `period_type`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interfaces `ShowCategoryList`, `ListPublisher`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `connection_status_update_time`, `active_time` to the interface `UpdateDevice`
  - Add the response parameters `connection_status_update_time`, `active_time` to the interface `ShowDevice`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `extended_parameters` to the interface `RecognizeAutoClassification`

# 3.1.29 2023-03-07

### HuaweiCloud SDK VOD

- _Features_
  - Support the interface `ModifySubtitle`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.28 2023-03-02

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateWorkflow`:
    - Remove the request parameter `trigger`
    - Modify the type of the response parameter `template_i18n`
  - Modify the type of the response parameter `template_i18n` of the interface `ListWorkflow`

### HuaweiCloud SDK BCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `result` to the interface `BatchInviteMembersToChannel`
  - Modify the type `string` -> `int32` of the response parameter `node_count` of the interface `ListNotifications`
  - Modify the type `string` -> `int32` of the response parameter `node_count` of the interface `ListMembers`
  - Remove the response parameter `result` from the interface `DownloadBlockchainCert`
  - Remove the response parameter `result` from the interface `DownloadBlockchainSdkConfig`
  - Remove the response parameter `result` from the interface `CreateBlockchainCertByUserName`

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListBareMetalServers`:
    - Add the enum values `HARD_REBOOT`, `DELETED` to the response parameter `status`
    - Remove the enum values `suspended` from the response parameter `OS-EXT-STS:vm_state`
  - Changes of the interface `CreateBareMetalServers`:
    - Add the request parameter `chargingMode`
    - Remove the request parameter `chargingmode`
  - Remove the enum values `SUSPENDED` from the response parameter `OS-EXT-STS:vm_state` from the interface `ChangeBaremetalServerName`
  - Changes of the interface `ListBareMetalServerDetails`:
    - Add the enum values `HARD_REBOOT`, `DELETED` to the response parameter `status`
    - Remove the enum values `suspended` from the response parameter `OS-EXT-STS:vm_state`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowDomainFullConfig`:
    - Modify the type `string` -> `int32` of the response parameter `error_code`
    - Modify the type `string` -> `int32` of the response parameter `target_code`
  - Changes of the interface `UpdateDomainFullConfig`:
    - Modify the type `string` -> `int32` of the request parameter `error_code`
    - Modify the type `string` -> `int32` of the request parameter `target_code`

### HuaweiCloud SDK CodeHub

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `page`, `per_page` to the interface `ListCommits`

### HuaweiCloud SDK DDS

- _Features_
  - Support the interfaces `ShowReplSetName`, `UpdateReplSetName`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DRIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `ip` to the interface `ListV2xEdges`
  
### HuaweiCloud SDK EG

- _Features_
  - Support the following interfaces：
    - `CheckPutEvents`
    - `ListObsBuckets`
    - `ListWorkflowTriggers`
    - `ListPubMetrics`
    - `ListSubMetrics`
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `ROCKETMQ` to the request parameter `type` to the interface `CreateEventSource`
  - The request parameter `name` changed to required of the interface `CreateChannel`
  - Changes of the interface `ListSubscriptions`:
    - Add the response parameter `used`
    - Modify the type of the response parameter `transform`
  - Changes of the interface `CreateSubscription`:
    - Add the response parameter `used`
    - Modify the type of the request parameter `transform`
    - The request parameter `detail` changed to required
    - Modify the type of the response parameter `transform`
  - Changes of the interface `ShowDetailOfSubscription`:
    - Add the response parameter `used`
    - Modify the type of the response parameter `transform`
  - Changes of the interface `UpdateSubscription`:
    - Add the response parameter `used`
    - Modify the type of the request parameter `transform`
    - The request parameter `detail` changed to required
    - Modify the type of the response parameter `transform`
  - Changes of the interface `CreateSubscriptionTarget`:
    - Modify the type of the request parameter `transform`
    - The request parameter `detail` changed to required
    - Modify the type of the response parameter `transform`
  - Modify the type of the response parameter `transform` of the interface `ShowDetailOfSubscriptionTarget`
  - Changes of the interface `UpdateSubscriptionTarget`:
    - Modify the type of the request parameter `transform`
    - The request parameter `detail` changed to required
    - Modify the type of the response parameter `transform`
  - The request parameter `vpc_id`, `subnet_id` changed to required of the interface `CreateConnection`
  - Add the enum values `EG_RESTORE_AGENCY` to the request parameter `type` to the interface `ListAgencies`
  - Add the enum values `EG_RESTORE_AGENCY` to the request parameter `type` to the interface `CreateAgencies`
  - Changes of the interface `ListQuotas`:
    - Add the enum values `SOURCE_ROCKETMQ` to the request parameter `type`
    - Add the enum values `SOURCE_ROCKETMQ` to the response parameter `type`
  - Changes of the interface `ListTriggers`:
    - Add the response parameter `used`
    - Modify the type of the response parameter `transform`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateTrigger`:
    - Add the request parameter `event_data`
    - Add the response parameters `trigger_id`, `trigger_type_code`, `trigger_status`, `event_data`, `last_updated_time`, `created_time`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the following interfaces：
    - `ResetDbUserPassword`
    - `ModifyDbUserPrivilege`
    - `ListDbUsers`
    - `CreateDbUser`
    - `DeleteDbUser`
    - `ListInstanceDatabases`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `order_ids` to the interface `ListSimCards`

### HuaweiCloud SDK Image

- _Features_
  - Support the following interfaces：
    - `CreateVideoSynthesisTask`
    - `ShowVideoSynthesisTask`
    - `CreateImageToVideoTask`
    - `ShowImageToVideoTask`
    - `CreateVideoCuttingTask`
    - `ShowVideoCuttingTask`
    - `CreateVideoTranslateTask`
    - `ShowVideoTranslateTask`
    - `CreateImageHighresolutionMattingTask`
    - `ShowImageHighresolutionMattingTask`
    - `CreateImageTranslateTask`
    - `ShowImageTranslateTask`
    - `CreateVideoCoverAnalysisTask`
    - `ShowVideoCoverAnalysisTask`
    - `CreateVideoSummarizationAnalysisTask`
    - `ShowVideoSummarizationAnalysisTask`
    - `CreateVideoShotSplitTask`
    - `ShowVideoShotSplitTask`
    - `RunImageWisedesignCrop`
    - `RunImageWisedesignInpainting`
    - `RunImageWisedesignColorfilter`
    - `RunImageWisedesignCombine`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTDA

- _Features_
  - Support the interfaces `ListOtaPackageInfo`, `CreateOtaPackage`, `ShowOtaPackage`, `DeleteOtaPackage`
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
  - Changes of the interface `ListInstanceConsumerGroups`:
    - Add the response parameter `groups`
    - Remove the response parameters `group_ids`, `next_offset`, `previous_offset`

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `external_datasources`, `effective_days` to the interface `CreateCluster`
  - Add the response parameter `effective_days` to the interface `ShowAutoScalingPolicy`

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interface `ListSpecIssueStayTimes`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `ListSslCertDownloadLink`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `configuration` to the interface `UpdateConfiguration`
  - The request parameter `alias` changed to not required of the interface `UpdatePostgresqlInstanceAlias`
  - The request parameter `comment` changed to not required of the interface `UpdateDatabase`

# 3.1.27 2023-02-23

### HuaweiCloud SDK BSS

- _Features_
  - Support the interface `ListCustomerAccountChangeRecords`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `value` changed to required of the interface `ListVault`
  - Changes of the interface `CreateVault`:
    - The request parameter `value` changed to required
    - The response parameter `value` changed to required
  - The response parameter `value` changed to required of the interface `ShowVault`
  - Changes of the interface `UpdateVault`:
    - The request parameter `value` changed to required
    - The response parameter `value` changed to required
  - The response parameter `value` changed to required of the interface `ListProtectable`
  - The response parameter `value` changed to required of the interface `ShowProtectable`
  - The response parameter `value` changed to required of the interface `ShowVaultResourceInstances`

### HuaweiCloud SDK CloudIDE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateRequest`:
    - Add the request parameters `request_type`, `above_text`, `following_text`
    - Add the response parameter `dispatched_task_number`
    - The request parameter `signature` changed to not required
  - Add the response parameter `request_type` to the interface `ShowResult`

### HuaweiCloud SDK CPH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `phone_model_name` to the interface `ChangeCloudPhoneServerModel`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `mainObject`, `stopObject`, `synonymObject` changed to not required of the interface `CreateLoadIkThesaurus`

### HuaweiCloud SDK DDS

- _Features_
  - Support the interface `ShrinkInstanceNodes`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - Support the interface `CreateClusterV2`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `active` to the interface `ListRoutingRules`
  - Add the request parameter `mysql_forwarding` to the interface `CreateRuleAction`
  - Add the response parameter `mysql_forwarding` to the interface `ListRuleActions`
  - Changes of the interface `UpdateRuleAction`:
    - Add the request parameter `mysql_forwarding`
    - Add the response parameter `mysql_forwarding`
  - Add the response parameter `mysql_forwarding` to the interface `ShowRuleAction`

### HuaweiCloud SDK LakeFormation

- _Features_
  - Support the interfaces `BatchUpdateLakeFormationInstanceTags`, `CreateLakeFormationInstance`, `ListPolicy`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `key`, `value` from the interface `ShowLakeFormationInstance`
  - Remove the response parameters `column_statistics_desc`, `column_statistics_objects` from the interface `SetPartitionColumnStatistics`

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowJobExeListNew`:
    - Add the enum values `FAILED`, `KILLED`, `NEW`, `NEW_SAVING`, `SUBMITTED`, `ACCEPTED`, `RUNNING`, `FINISHED`, Remove the enum values `FAILED：失败`, `KILLED：已终止`, `NEW：已创建`, `NEW_SAVING：已创建保存中`, `SUBMITTED：已提交`, `ACCEPTED：已接受`, `RUNNING：运行中`, `FINISHED：已完成` from the request parameter `job_state`
    - Add the enum values `FAILED`, `KILLED`, `UNDEFINED`, `SUCCEEDED`, Remove the enum values `FAILED：执行失败的作业。`, `KILLED：执行中被手动终止的作业。`, `UNDEFINED：正在执行的作业。`, `SUCCEEDED：执行成功的作业。` from the request parameter `job_result`
  - Add the enum values `path_suffix`, `length`, `modification_time`, Remove the enum values `path_suffix：文件或目录名称`, `length：文件大小`, `modification_time：修改时间` from the request parameter `sort_key` to the interface `ShowHdfsFileList`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `UpdateDbUserPrivilege`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `X-Client-Token` to the interface `CreateInstance`

### HuaweiCloud SDK SCM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `certificate_chain` changed to not required of the interface `ImportCertificate`
  - Add the response parameter `entire_certificate` to the interface `ExportCertificate`

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `flag` to the interface `UpdatePremiumHost`

# 3.1.26 2023-02-16

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `id` from the interface `CreateApp`
  - Changes of the interface `ListResourceUnderNode`:
    - Add the request parameter `ci_ids`
    - The request parameter `ci_id` changed to not required

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interface `CreateLogin`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `id`, `property_name`, `property_value`, `extension_version_id`, `created_at`, `updated_at` from the interface `ListExtensions`
  - Remove the response parameters `id`, `property_name`, `property_value`, `extension_version_id`, `created_at`, `updated_at` from the interface `ShowExtensionDetail`

### HuaweiCloud SDK CSS

- _Features_
  - Support the interface `ChangeSecurityGroup`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ChangeMode`:
    - Add the request parameter `changeModeReq`
    - Remove the request parameter `changeModeRequestBody`
  - Changes of the interface `AddIndependentNode`:
    - Add the request parameter `IndependentReq`
    - Remove the request parameter `IndependentRequestBody`

### HuaweiCloud SDK CTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `compress_type`, `is_sort_by_service` to the interface `UpdateTracker`
  - Add the request parameters `compress_type`, `is_sort_by_service` to the interface `CreateTracker`
  - Add the response parameters `compress_type`, `is_sort_by_service` to the interface `ListTrackers`

### HuaweiCloud SDK DCS

- _Features_
  - Support the interfaces `CreateCustomTemplate`, `CreateAutoExpireScanTask`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DRIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `esn` to the interface `ShowHistoryTrafficEvents`

### HuaweiCloud SDK DWS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `project_id`, `cluster_id`, `limit`, `offset`, `sort_key`, `sort_dir` to the interface `ListClusterSnapshots`

### HuaweiCloud SDK FRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `nod_threshold` to the interface `DetectLiveByUrl`
  - Add the request parameter `nod_threshold` to the interface `DetectLiveByUrlIntl`
  - Add the request parameter `nod_threshold` to the interface `DetectLiveByFile`
  - Add the request parameter `nod_threshold` to the interface `DetectLiveByFileIntl`
  - Add the request parameter `nod_threshold` to the interface `DetectLiveByBase64`
  - Add the request parameter `nod_threshold` to the interface `DetectLiveByBase64Intl`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `host` changed to required of the interface `AddDatabasePermission`

### HuaweiCloud SDK Image

- _Features_
  - Support the interfaces `RunImageSuperResolution`, `RunRecaptureDetect`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OSM

- _Features_
  - Support the following interfaces：
    - `CreateAuthorization`
    - `CreateFeedback`
    - `ShowDownloadAccessoryUrl`
    - `CreateQuestionInSession`
    - `CreateSession`
    - `CreateEvaluate`
    - `ListFeedbackOption`
    - `CreateQaFeedbacks`
    - `CreateAskQuestion`
    - `ShowQaPairDetail`
    - `ShowAssociatedQuestions`
    - `ShowQaPairs`
    - `ListRecommendWords`
    - `CreateQaAsk`
    - `ShowTheme`
    - `ListArticles`
    - `ListNotices`
    - `ListTools`
    - `CreateDiagnoseFeedback`
    - `ListDiagnoseItems`
    - `ListDiagnoseJob`
    - `ListDiagnoseRecords`
    - `CreateDiagnoseJob`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RocketMQ

- _Features_
  - Support the interfaces `CreateInstanceByEngine`, `BatchCreateOrDeleteRocketmqTag`, `ShowRocketmqTags`, `ShowRocketmqProjectTags`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `limit`, `offset` to the interface `ListInstances`
  - Add the request parameters `limit`, `offset` to the interface `ShowConsumerListOrDetails`
  - Add the request parameters `limit`, `offset` to the interface `ListConsumerGroupOfTopic`

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateHost`:
    - Remove the enum values `TLS v1.3` from the request parameter `tls`
    - Remove the enum values `TLS v1.3` from the response parameter `tls`
  - Remove the enum values `TLS v1.3` from the response parameter `tls` from the interface `ShowHost`
  - Remove the enum values `TLS v1.3` from the response parameter `tls` from the interface `CreatePremiumHost`
  - Remove the enum values `TLS v1.3` from the response parameter `tls` from the interface `ShowPremiumHost`
  - Changes of the interface `UpdatePremiumHost`:
    - Remove the enum values `TLS v1.3` from the request parameter `tls`
    - Remove the enum values `TLS v1.3` from the response parameter `tls`

# 3.1.25 2023-02-09

### HuaweiCloud SDK LakeFormation

- _Features_
  - Support the service `LakeFormation`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudArtifact

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - `CloudArtifact` is renamed to `CodeArtsArtifact`

### HuaweiCloud SDK CloudBuild

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - `CloudBuild` is renamed to `CodeArts Build`

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `fail_resource_infos` to the interface `RenewalResources`
  - Add the response parameter `fail_resource_infos` to the interface `CancelResourcesSubscription`

### HuaweiCloud SDK DBSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `SwitchRiskRule`:
    - Add the response parameter `status`
    - Remove the response parameter `result`

### HuaweiCloud SDK DDS

- _Features_
  - Support the interface `ListLtsSlowLogs`
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
  - Add the response parameter `error_code` to the interface `ListAsyncInvocations`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowPauseResumeStutus`:
    - Add the request parameter `X-Auth-Token`
    - Add the response parameters `master_instance_id`, `slave_instance_id`, `data_sync_indicators`, `rto_and_rpo_indicators`
    - Remove the request parameter `x-auth-token`

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `roma_forwarding`, `influxdb_forwarding`, `functiongraph_forwarding`, `mrs_kafka_forwarding`, `dms_rocketmq_forwarding` to the interface `ListRuleActions`
  - Add the request parameters `roma_forwarding`, `influxdb_forwarding`, `functiongraph_forwarding`, `mrs_kafka_forwarding`, `dms_rocketmq_forwarding` to the interface `CreateRuleAction`
  - Changes of the interface `UpdateRuleAction`:
    - Add the request parameters `roma_forwarding`, `influxdb_forwarding`, `functiongraph_forwarding`, `mrs_kafka_forwarding`, `dms_rocketmq_forwarding`
    - Add the response parameters `roma_forwarding`, `influxdb_forwarding`, `functiongraph_forwarding`, `mrs_kafka_forwarding`, `dms_rocketmq_forwarding`
  - Add the response parameters `roma_forwarding`, `influxdb_forwarding`, `functiongraph_forwarding`, `mrs_kafka_forwarding`, `dms_rocketmq_forwarding` to the interface `ShowRuleAction`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `RecognizeTollInvoice`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListErrorlogForLts`, `ListSlowlogForLts`, `ListSlowLogStatisticsForLts`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.24 2023-02-02

### HuaweiCloud SDK AOS

- _Features_
  - Support the interface `UpdateStack`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `executor` to the interface `ApplyExecutionPlan`
  - Changes of the interface `ListStackEvents`:
    - Add the request parameters `filter`, `field`
    - Remove the response parameters `resource_id_key`, `resource_id_value`, `resource_name`, `resource_type`, `time`, `event_type`, `event_message`, `elapsed_seconds`
  - The response parameter `stack_name` changed to required of the interface `GetStackMetadata`
  - Add the request parameter `executor` to the interface `CreateStack`
  - Changes of the interface `ListStackResources`:
    - Add the response parameter `index_key`
    - Remove the enum values `DELETION_SKIPPED` from the response parameter `resource_status`
  - Add the request parameter `executor` to the interface `DeployStack`

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `fail_resource_infos` to the interface `RenewalResources`
  - Add the response parameter `fail_resource_infos` to the interface `CancelResourcesSubscription`

### HuaweiCloud SDK CloudPipeline

- _Features_
  - Support the following interfaces：
    - `RunPipeline`
    - `BatchShowPipelinesLatestStatus`
    - `ShowPipelineRunDetail`
    - `ListPipelines`
    - `DeletePipeline`
    - `StopPipelineRun`
    - `ListPipelineRuns`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `GaussDB` to the request parameter `type` to the interface `CreateInstance`
  - Add the enum values `GaussDB` to the request parameter `datastore_type` to the interface `ListInstances`
  - Add the enum values `GaussDB` to the response parameter `type` to the interface `ListBackups`

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `all_billing_cycle` to the interface `ListBackPools`
  - Add the request parameter `all_billing_cycle` to the interface `ListSimPools`

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `IsoImage` to the request parameter `type` to the interface `CreateImage`

### HuaweiCloud SDK Kafka

- _Features_
  - Support the interfaces `CreateInstanceByEngine`, `ShowEngineInstanceExtendProductInfo`, `ResizeEngineInstance`, `CreateReassignmentTask`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `sasl_enabled_mechanisms` to the interface `ListInstances`
  - The request parameter `kafka_manager_user`, `kafka_manager_password` changed to not required of the interface `CreatePostPaidInstance`
  - Add the response parameter `sasl_enabled_mechanisms` to the interface `ShowInstance`

### HuaweiCloud SDK Moderation

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `white_glossaries` to the interface `RunTextModeration`

# 3.1.23 2023-01-19

### HuaweiCloud SDK CCM

- _Features_
  - Support the interfaces `EnableCertificateAuthorityCrl`, `DisableCertificateAuthorityCrl`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `enc_cert_info` to the interface `ListCertificate`
  - Add the response parameter `enc_cert_info` to the interface `ShowCertificate`
  - Changes of the interface `ExportCertificate`:
    - Add the request parameter `is_sm_standard`
    - Add the response parameters `enc_certificate`, `enc_private_key`, `enc_sm2_enveloped_key`

### HuaweiCloud SDK DWS

- _Features_
  - Support the interfaces `ListMonitorIndicatorData`, `ListMonitorIndicators`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK HSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListRiskConfigCheckRules`:
    - Add the response parameters `enable_fix`, `enable_click`
    - Remove the response parameters `fix_status`, `enable_auto_fix`
  - Add the request parameter `check_type` to the interface `ShowCheckRuleDetail`
  - The request parameter `version`, `host_id_list` changed to required of the interface `SwitchHostsProtectStatus`

### HuaweiCloud SDK IoTDA

- _Features_
  - Support the interface `UploadBatchTaskFile`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTEdge

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `virtual_ipv6_address` to the interface `ShowEdgeNode`

# 3.1.22 2023-01-12

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `is_has_trusted_root_ca` to the interface `ListApiGroupsV2`
  - Add the response parameter `is_has_trusted_root_ca` to the interface `UpdateApiGroupV2`
  - Add the response parameter `is_has_trusted_root_ca` to the interface `ShowDetailsOfApiGroupV2`
  - Add the response parameter `is_has_trusted_root_ca` to the interface `UpdateApiV2`
  - Add the response parameter `is_has_trusted_root_ca` to the interface `ShowDetailsOfApiV2`
  - Changes of the interface `BatchPublishOrOfflineApiV2`:
    - Add the request parameter `group_id`
    - The request parameter `env_id` changed to required
  - Add the response parameter `is_has_trusted_root_ca` to the interface `ListApiVersionDetailV2`
  - Add the request parameters `bandwidth_charging_mode`, `ingress_bandwidth_size`, `ingress_bandwidth_charging_mode` to the interface `CreateInstanceV2`
  - Add the response parameters `bandwidth_charging_mode`, `ingress_bandwidth_charging_mode` to the interface `UpdateInstanceV2`
  - Add the response parameters `bandwidth_charging_mode`, `ingress_bandwidth_charging_mode` to the interface `ShowDetailsOfInstanceV2`
  - Add the request parameter `bandwidth_charging_mode` to the interface `AddEngressEipV2`
  - Add the request parameter `bandwidth_charging_mode` to the interface `UpdateEngressEipV2`
  - The request parameter `version` changed to not required of the interface `ImportMicroservice`
  - Add the response parameter `is_has_trusted_root_ca` to the interface `CreateCertificateV2`
  - Add the response parameter `is_has_trusted_root_ca` to the interface `ListCertificatesV2`
  - Add the response parameter `is_has_trusted_root_ca` to the interface `UpdateCertificateV2`
  - Add the response parameter `is_has_trusted_root_ca` to the interface `ShowDetailsOfCertificateV2`

### HuaweiCloud SDK BSS

- _Features_
  - Support the interface `ListFreeResourcesUsageRecords`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `sub_service_type_code`, `sub_service_type_name`, `sub_resource_type_code`, `sub_resource_type_name`, `sub_resource_id`, `sub_resource_name` to the interface `ListCustomerselfResourceRecordDetails`
  - Add the response parameters `sub_service_type_code`, `sub_service_type_name`, `sub_resource_type_code`, `sub_resource_type_name`, `sub_resource_id`, `sub_resource_name` to the interface `ListCustomerselfResourceRecords`
  - The request parameter `operator` changed to required of the interface `ListCosts`

### HuaweiCloud SDK BSSINTL

- _Features_
  - Support the interface `ListFreeResourcesUsageRecords`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `sub_service_type_code`, `sub_service_type_name`, `sub_resource_type_code`, `sub_resource_type_name`, `sub_resource_id`, `sub_resource_name` to the interface `ListCustomerselfResourceRecordDetails`
  - Add the response parameters `sub_service_type_code`, `sub_service_type_name`, `sub_resource_type_code`, `sub_resource_type_name`, `sub_resource_id`, `sub_resource_name` to the interface `ListCustomerselfResourceRecords`
  - The request parameter `operator` changed to required of the interface `ListCosts`

### HuaweiCloud SDK CES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListAlarmHistories`:
    - Add the response parameter `data_points`
    - Remove the response parameter `datapoints`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `object_scope` to the interface `ListDbObjects`
  - Add the response parameter `object_scope` to the interface `ShowDbObjectCollectionStatus`

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the following interfaces：
    - `ExecuteAssetAction`
    - `UpdateDataPathPolicy`
    - `PublishData`
    - `PublishImage`
    - `BatchDeleteLabel`
    - `BatchDownloadResourceStatData`
    - `PublishApp`
    - `ShowTaskInstanceMetricData`
    - `BatchCancelJob`
    - `BatchRetryJob`
    - `BatchDeleteJob`
    - `PublishWorkflow`
    - `UpdateAssetVersion`
    - `DeleteAssetVersion`
    - `UpdateJob`
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ListRecentJob`
  - Remove the response parameter `latest_version` from the interface `ListAsset`
  - Remove the response parameter `latest_version` from the interface `ShowAsset`
  - Add the response parameters `failed_reason`, `labels`, `picture` to the interface `ShowAssetVersion`
  - Remove the response parameter `latest_version` from the interface `ListStar`
  - The request parameter `column` changed to required of the interface `CreateDatabaseData`
  - The request parameter `column` changed to required of the interface `UpdateDatabaseData`
  - Add the response parameter `deletable` to the interface `ListData`
  - Add the response parameter `deletable` to the interface `ShowData`
  - Add the response parameter `failed_reason` to the interface `ListDataJob`
  - Add the request parameter `storage_quota` to the interface `UpdateProject`
  - Add the response parameter `storage_quota` to the interface `ShowProject`
  - Remove the response parameters `path`, `name`, `type`, `size`, `create_time`, `download_url` from the interface `ShowProjectTrace`
  - Add the response parameters `allowed_operate`, `deletable` to the interface `ShowProjectTraceData`
  - Changes of the interface `ListComputingResources`:
    - Add the response parameter `node_labels`
    - Remove the request parameters `label`, `offset`, `limit`
  - Remove the request parameter `job_retain_time` from the interface `UpdateJobConfig`
  - Remove the response parameter `job_retain_time` from the interface `ShowJobConfig`
  - Remove the response parameter `count` from the interface `ListLabel`
  - Remove the request parameter `name` from the interface `BatchUpdateNodeLabel`
  - Remove the request parameter `user_id_type` from the interface `DeleteUser`
  - Add the response parameter `host_name` to the interface `ShowTaskInstances`

### HuaweiCloud SDK FRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveByUrl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveByUrlIntl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveFaceByUrl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveByFile`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveByFileIntl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveFaceByFile`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveByBase64`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveByBase64Intl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectLiveFaceByBase64`
  - Add the request parameter `Enterprise-Project-Id` to the interface `SearchFaceByFaceId`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectFaceByFile`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectFaceByFileIntl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `UpdateFace`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DeleteFaceByExternalImageId`
  - Add the request parameter `Enterprise-Project-Id` to the interface `ShowFacesByLimit`
  - Add the request parameter `Enterprise-Project-Id` to the interface `CompareFaceByFile`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DeleteFaceByFaceId`
  - Add the request parameter `Enterprise-Project-Id` to the interface `ShowFacesByFaceId`
  - Add the request parameter `Enterprise-Project-Id` to the interface `AddFacesByBase64`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectFaceByUrl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectFaceByUrlIntl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DeleteFaceSet`
  - Add the request parameter `Enterprise-Project-Id` to the interface `ShowFaceSet`
  - Add the request parameter `Enterprise-Project-Id` to the interface `CompareFaceByBase64`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectFaceByBase64`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectFaceByBase64Intl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `CreateFaceSet`
  - Add the request parameter `Enterprise-Project-Id` to the interface `ShowAllFaceSets`
  - Add the request parameter `Enterprise-Project-Id` to the interface `SearchFaceByFile`
  - Add the request parameter `Enterprise-Project-Id` to the interface `AddFacesByUrl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `AddFacesByFile`
  - Add the request parameter `Enterprise-Project-Id` to the interface `SearchFaceByUrl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `SearchFaceByBase64`
  - Add the request parameter `Enterprise-Project-Id` to the interface `CompareFaceByUrl`
  - Add the request parameter `Enterprise-Project-Id` to the interface `BatchDeleteFaces`

### HuaweiCloud SDK HSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `policy_id`, `policy_name`, `protection_mode`, `bait_protection_status`, `protection_directory`, `protection_type`, `operating_system` changed to required of the interface `UpdateProtectionPolicy`
  - The request parameter `operating_system`, `ransom_protection_status`, `backup_protection_status`, `policy_id`, `pattern`, `agent_id_list`, `host_id_list` changed to required of the interface `StartProtection`
  - The request parameter `host_id_list`, `agent_id_list`, `close_protection_type` changed to required of the interface `StopProtection`
  - The request parameter `policy_id`, `pattern` changed to required of the interface `UpdateBackupPolicyInfo`
  - Add the response parameters `enterprise_project_id`, `enterprise_project_name` to the interface `ListQuotasDetail`
  - Add the response parameters `host_status`, `agent_status`, `protect_status`, `asset_value`, `keyword`, `hash` to the interface `ListSecurityEvents`
  - Changes of the interface `ChangeEvent`:
    - Add the request parameters `keyword`, `hash`
    - Remove the request parameter `description`
  - The request parameter `group_id` changed to not required of the interface `DeleteHostsGroup`
  - The request parameter `group_name`, `host_id_list` changed to required of the interface `AddHostsGroup`
  - The request parameter `target_policy_group_id` changed to required of the interface `AssociatePolicyGroup`
  - The request parameter `operate_type`, `vul_id`, `host_id_list` changed to required of the interface `ChangeVulStatus`
  - Changes of the interface `SetWtpProtectionStatusInfo`:
    - Add the request parameter `charging_mode`
    - Remove the request parameter `payment_mode`

### HuaweiCloud SDK IVS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectStandardByIdCardImage`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectStandardByNameAndId`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectExtentionByNameAndId`
  - Add the request parameter `Enterprise-Project-Id` to the interface `DetectExtentionByIdCardImage`

### HuaweiCloud SDK OCR

- _Features_
  - Support the interface `RecognizeCustomTemplate`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `RecognizeGeneralTable`:
    - Add the request parameters `return_char_location`, `return_rectification_matrix`
    - Add the response parameter `char_list`
  - Add the request parameter `language` to the interface `RecognizeGeneralText`
  - Changes of the interface `RecognizeWebImage`:
    - Add the response parameter `extracted_data`
    - Remove the response parameters `extracted_data`, `contact_info`, `image_size`, `height`, `width`, `name`, `phone`, `province`, `city`, `district`, `detail_address`

### HuaweiCloud SDK RocketMQ

- _Features_
  - Support the interface `ListRocketInstanceTopics`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `name` to the interface `ShowOneTopic`

# 3.1.21 2023-01-05

### HuaweiCloud SDK CPH

- _Features_
  - Support the following interfaces：
    - `ListProjectTags`
    - `ListResourceTags`
    - `ListResourceInstances`
    - `BatchCreateTags`
    - `BatchDeleteTags`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `enterprise_project_id` to the interface `ListCloudPhoneServers`
  - Add the response parameter `enterprise_project_id` to the interface `ShowCloudPhoneServerDetail`

### HuaweiCloud SDK DCS

- _Features_
  - Support the interface `ListConfigHistories`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DNS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
    - `ListResoleRules`
    - `SetPrivateZoneProxyPattern`
    - `ShowDomainQuota`
    - `ShowRetrieval`
    - `CreateRetrieval`
    - `ShowRetrievalVerification`
    - `CreateRetrievalVerification`
    - `ListEndpoints`
    - `CreateEndpoint`
    - `ShowEndpoint`
    - `UpdateEndpoint`
    - `DeleteEndpoint`
    - `ListEndpointIpaddresses`
    - `AssociateEndpointIpaddress`
    - `DisassociateEndpointIpaddress`
    - `ListEndpointVpcs`
    - `CreateResolveRule`
    - `AssociateResolveRuleRouter`
    - `DisassociateResolveRuleRouter`
    - `ShowResoleRule`
    - `UpdateResolveRule`
    - `DeleteResolveRule`
    - `BatchDeleteZones`
    - `BatchDeletePtrRecords`
    - `BatchSetZonesStatus`
    - `BatchSetRecordSetsStatus`
    - `BatchDeleteRecordSets`
  - Changes of the interface `CreatePrivateZone`:
    - Add the request parameter `proxy_pattern`
    - Add the response parameter `proxy_pattern`
  - Add the response parameter `proxy_pattern` to the interface `ListPrivateZones`

### HuaweiCloud SDK DRIS

- _Features_
  - Support the interface `BatchShowRadars`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DRS

- _Features_
  - Support the interfaces `ShowDbObjectCollectionStatus`, `ShowUpdateObjectSavingStatus`, `CollectDbObjectsAsync`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListDbObjects`:
    - Add the request parameter `db_names`
    - Add the response parameters `status`, `id`

### HuaweiCloud SDK DWS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `count`, `datastore_type`, `available_zones`, `ram`, `vcpus`, `datastores`, `volume`, `elastic_volume_specs` to the interface `ListNodeTypes`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `DISABLED`, Remove the enum values `DISABLE` from the response parameter `trigger_status` to the interface `ListFunctionTriggers`
  - Add the enum values `DISABLED`, Remove the enum values `DISABLE` from the request parameter `trigger_status` to the interface `UpdateTrigger`
  - Add the enum values `DISABLED`, Remove the enum values `DISABLE` from the response parameter `trigger_status` to the interface `ShowFunctionTrigger`
  - Add the request parameter `enable_stream_response` to the interface `CreateWorkflow`
  - Add the request parameter `enable_stream_response` to the interface `UpdateWorkFlow`
  - Add the response parameter `enable_stream_response` to the interface `ShowWorkFlow`

### HuaweiCloud SDK HiLens

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `deployment_num` to the interface `ShowNodes`
  - Add the response parameter `cluster_node_type` to the interface `ShowNode`
  - Add the request parameters `offset`, `limit` to the interface `ShowUpgradeProgress`
  - Add the request parameters `offset`, `limit` to the interface `ListTasks`
  - Add the request parameters `offset`, `limit` to the interface `ShowDeploymentPods`
  - Add the request parameters `offset`, `limit` to the interface `ListWorkSpaces`

### HuaweiCloud SDK IoTEdge

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `app_version` changed to not required of the interface `CreateEdgeNode`
  - Add the response parameter `reliability_level` to the interface `ShowEdgeNode`

### HuaweiCloud SDK Live

- _Features_
  - Support the interface `ListUpStreamDetail`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListBandwidthDetail`:
    - Add the request parameter `service_type`
    - The request parameter `play_domains` changed to required
  - Changes of the interface `ListDomainTrafficDetail`:
    - Add the request parameter `service_type`
    - The request parameter `play_domains` changed to required
  - Changes of the interface `ListDomainBandwidthPeak`:
    - Add the request parameter `service_type`
    - The request parameter `play_domains` changed to required
  - Changes of the interface `ListDomainTrafficSummary`:
    - Add the request parameter `service_type`
    - The request parameter `play_domains` changed to required
  - Add the request parameter `service_type` to the interface `ListUsersOfStream`
  - Add the request parameter `type` to the interface `ShowUpBandwidth`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateSearchCriterias`:
    - Add the request parameter `eps_id`
    - Remove the request parameter `epsId`
  - Changes of the interface `DeleteSearchCriterias`:
    - Add the request parameter `eps_id`
    - Remove the request parameter `epsId`

### HuaweiCloud SDK Moderation

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `white_glossary_names` to the interface `RunTextModeration`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListPorts`:
    - Add the request parameter `security_groups`
    - Modify the type `string` -> `array` of the request parameter `fixed_ips`

# 3.1.20 2022-12-29

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `verified_client_certificate_enabled` to the interface `ListApiGroupsV2`
  - Add the response parameter `verified_client_certificate_enabled` to the interface `ShowDetailsOfApiGroupV2`
  - Add the response parameter `verified_client_certificate_enabled` to the interface `UpdateApiGroupV2`
  - Add the response parameter `verified_client_certificate_enabled` to the interface `ShowDetailsOfApiV2`
  - Add the response parameter `verified_client_certificate_enabled` to the interface `UpdateApiV2`
  - Add the response parameter `verified_client_certificate_enabled` to the interface `ListApiVersionDetailV2`
  - Add the request parameter `verified_client_certificate_enabled` to the interface `UpdateDomainV2`
  - Add the response parameters `id`, `name`, `type`, `instance_id`, `project_id`, `create_time`, `update_time` to the interface `ShowDetailsOfDomainNameCertificateV2`
  - Add the request parameter `oas_version` to the interface `ExportApiDefinitionsV2`
  - Add the response parameter `instance_id` to the interface `ListVpcChannelsV2`
  - Add the response parameter `instance_id` to the interface `ShowDetailsOfVpcChannelV2`
  - Add the response parameter `instance_id` to the interface `UpdateVpcChannelV2`
  - Add the enum values `inbound_eip`, `outbound_eip`, Remove the enum values `inbound`, `outbound` from the request parameter `dim` to the interface `ListMetricData`
  - Add the request parameter `vpcep_service_name` to the interface `CreateInstanceV2`
  - Add the response parameter `is_releasable` to the interface `ShowDetailsOfInstanceV2`
  - Changes of the interface `UpdateInstanceV2`:
    - Add the request parameter `vpcep_service_name`
    - Add the response parameter `is_releasable`
  - Add the request parameter `trusted_root_ca` to the interface `CreateCertificateV2`
  - Add the request parameter `verified_client_certificate_enabled` to the interface `BatchAssociateCertsV2`
  - Add the request parameter `verified_client_certificate_enabled` to the interface `BatchDisassociateCertsV2`
  - Add the request parameter `trusted_root_ca` to the interface `UpdateCertificateV2`
  - Add the request parameter `verified_client_certificate_enabled` to the interface `BatchAssociateDomainsV2`
  - Add the request parameter `verified_client_certificate_enabled` to the interface `BatchDisassociateDomainsV2`
  - Add the response parameter `verified_client_certificate_enabled` to the interface `ListAttachedDomainsV2`

### HuaweiCloud SDK CFW

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `fw_instance_id`, `enterprise_project_id` to the interface `ListDnsServers`
  - Add the request parameters `fw_instance_id`, `enterprise_project_id` to the interface `UpdateDnsServers`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListVpcProtects`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListRuleHitCount`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `DeleteAclRuleCount`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ChangeIpsSwitchUsingPost`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListIpsSwitchStatusUsingGet`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListEastWestFirewall`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ChangeEwProtectStatus`
  - Add the request parameter `enterprise_project_id` to the interface `ListFlowLogs`
  - Add the request parameter `enterprise_project_id` to the interface `ListAccessControlLogs`
  - Add the request parameter `enterprise_project_id` to the interface `ListAttackLogs`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `AddRuleAclUsingPost`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `DeleteRuleAclUsingDelete`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `UpdateRuleAclUsingPut`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListRuleAclsUsingGet`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListRuleAclUsingPut`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `AddBlackWhiteListUsingPost`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `DeleteBlackWhiteListUsingDelete`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `UpdateBlackWhiteListUsingPut`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListBlackWhiteListsUsingGet`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ChangeIpsProtectModeUsingPost`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListIpsProtectModeUsingPost`
  - Changes of the interface `ListFirewallUsingGet`:
    - Add the request parameters `enterprise_project_id`, `fw_instance_id`
    - Add the response parameters `fw_instance_name`, `enterprise_project_id`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `AddServiceSetUsingPost`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `DeleteServiceSetUsingDelete`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListServiceSetDetails`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `UpdateServiceSetUsingPut`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `AddServiceItemsUsingPost`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListServiceItemsDetails`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `DeleteServiceItemUsingDelete`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListParseDomainDetails`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `CountEips`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ChangeProtectEip`
  - Changes of the interface `ListEipResources`:
    - Add the request parameters `fw_instance_id`, `fw_key_word`, `eps_id`
    - Add the response parameters `fw_instance_name`, `fw_instance_id`, `fw_enterprise_project_id`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `DeleteAddressItemUsingDelete`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `AddAddressItemsUsingPost`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListAddressItemsUsingGet`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `AddAddressSetInfoUsingPost`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListAddressSetListUsingGet`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `DeleteAddressSetInfoUsingDelete`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListAddressSetDetailUsingGet`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `UpdateAddressSetInfoUsingPut`
  - Add the request parameters `enterprise_project_id`, `fw_instance_id` to the interface `ListServiceSet`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `int32` of the response parameter `size` of the interface `ListClustersDetails`
  - Modify the type `string` -> `int32` of the response parameter `size` of the interface `ShowClusterDetail`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `int32` -> `int64` of the response parameter `size` of the interface `CreateBigkeyScanTask`
  - Modify the type `int32` -> `int64` of the response parameter `size` of the interface `ShowBigkeyScanTaskDetails`
  - Modify the type `int32` -> `int64` of the response parameter `size` of the interface `CreateHotkeyScanTask`
  - Modify the type `int32` -> `int64` of the response parameter `size` of the interface `ShowHotkeyTaskDetails`

### HuaweiCloud SDK DNS

- _Features_
  - Support the interfaces `AssociateResolveRuleRouter`, `DisassociateResolveRuleRouter`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `total_count` from the interface `ListPublicZones`
  - Remove the response parameter `total_count` from the interface `ListPrivateZones`
  - Remove the response parameter `total_count` from the interface `ListRecordSetsByZone`
  - Remove the response parameter `total_count` from the interface `ListRecordSets`
  - Remove the response parameter `total_count` from the interface `BatchDeleteRecordSetWithLine`
  - Remove the response parameter `total_count` from the interface `BatchUpdateRecordSetWithLine`
  - Remove the response parameter `total_count` from the interface `ListRecordSetsWithLine`
  - Remove the response parameter `total_count` from the interface `CreateRecordSetWithBatchLines`
  - Remove the response parameter `total_count` from the interface `ShowRecordSetByZone`
  - Remove the response parameter `total_count` from the interface `ListPtrRecords`
  - Remove the response parameter `total_count` from the interface `ListCustomLine`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `charging_mode`, `period_order` to the interface `BatchCreateJobs`
  - Add the enum values `forRetryJob` to the request parameter `precheck_mode` to the interface `BatchCheckJobs`
  - Add the response parameters `period_order`, `object_infos` to the interface `BatchListJobDetails`

### HuaweiCloud SDK DWS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `elb` to the interface `ListClusterDetails`
  - Add the request parameters `offset`, `limit` to the interface `ListAlarmSubs`
  - Add the request parameters `offset`, `limit` to the interface `ListEvents`
  - Add the request parameters `offset`, `limit` to the interface `ListEventSubs`

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `extendParam` to the interface `ChangeBandwidthToPeriod`
  - Add the request parameter `extendParam` to the interface `ChangePublicipToPeriod`
  - Changes of the interface `ListBandwidthPkg`:
    - Add the response parameter `tenantId`
    - Remove the response parameter `tenant_id`
  - The request parameter `associate_instance_type`, `associate_instance_id` changed to required of the interface `UpdateAssociatePublicip`
  - The request parameter `associate_instance_type`, `associate_instance_id` changed to required of the interface `AssociatePublicips`

### HuaweiCloud SDK ELB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListLoadbalancersByTags`:
    - Remove the request parameter `without_any_tag`
    - The request parameter `values` changed to required
  - Changes of the interface `ListListenersByTags`:
    - Remove the request parameter `without_any_tag`
    - The request parameter `values` changed to required
  - Add the response parameters `ipgroup_bindings`, `ipgroup_max_length` to the interface `ShowQuota`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `total_count` to the interface `ListInstanceTags`

### HuaweiCloud SDK HiLens

- _Features_
  - Support the following interfaces：
    - `ListPlatformManager`
    - `ListFirmwares`
    - `ShowDeployments`
    - `CreateDeployment`
    - `ShowDeployment`
    - `UpdateDeployment`
    - `StartAndStopDeployment`
    - `DeletePod`
    - `StartAndStopDeploymentPod`
    - `AddDeploymentNodes`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `id`, `name`, `description`, `created_at`, `cluster_id`, `cluster_node_state`, `cluster_node_type`, `firmware_name`, `upgrade_firmware_version`, `firmware_status`, `firmware_upgrade_record`, `state`, `type`, `active_status`, `cpu`, `host_ips`, `tags` from the interface `ShowNodes`
  - Changes of the interface `CreateNode`:
    - Remove the request parameter `log_group_id`
    - The request parameter `component`, `type` changed to required
  - Changes of the interface `ShowNode`:
    - Remove the response parameter `log_group_id`
    - Modify the type `int32` -> `string` of the response parameter `firmware_upgrade_time`
    - The response parameter `component`, `type` changed to required
  - Changes of the interface `UpdateNode`:
    - Remove the request parameter `log_group_id`
    - The request parameter `component`, `type` changed to required
  - Modify the type `string` -> `int32` of the response parameter `status` of the interface `ShowUpgradeProgress`
  - Changes of the interface `ShowResourceTags`:
    - Add the response parameter `count`
    - Remove the response parameter `total`
  - Modify the type `string` -> `int32` of the response parameter `count` of the interface `ListSecrets`
  - Changes of the interface `CreateSecret`:
    - Add the response parameter `secret`
    - Remove the response parameters `id`, `name`, `description`, `project_id`, `created_at`, `updated_at`, `secrets`, `tags`
  - Changes of the interface `UpdateSecret`:
    - Add the response parameter `secret`
    - Remove the response parameters `id`, `name`, `description`, `project_id`, `created_at`, `updated_at`, `secrets`, `tags`
  - Changes of the interface `ShowSkillOrderList`:
    - Modify the type `int32` -> `int64` of the response parameter `update_time`
    - Modify the type `int32` -> `int64` of the response parameter `expire_time`
    - Modify the type `string` -> `int32` of the response parameter `order_limit`
  - Changes of the interface `CreateOrderForm`:
    - Add the response parameter `order_id`
    - Remove the request parameters `data`, `total`
    - Remove the response parameters `data`, `total`
  - Changes of the interface `ShowSkillOrderInfo`:
    - Add the response parameters `expiration_stop_flag`, `package_order_id`, `icon`, `commission_flag`, `product_info`, `package_id`, `measure_type`, `update_time`, `channel_limit`, `resource_step_size`, `cloud_service_type`, `developer_id`, `amount`, `format`, `resource_type`, `expire_time`, `measure_unit`, `skill_chip`, `versions`, `skill_name`, `skill_type`, `used_amount`, `charge_model`, `resource_spec_code`, `skill_id`, `skill_platform`, `order_limit`, `order_id`, `status`
    - Remove the response parameters `total`, `data`
  - Add the response parameter `deployment_id` to the interface `DeleteDeployment`
  - Remove the response parameter `deployment_tags` from the interface `UpdateDeploymentUsingPatch`
  - Changes of the interface `ShowDeploymentPods`:
    - Add the response parameters `start_resources`, `channel_resources`, `skill_project_id`
    - Remove the response parameters `app_docker_login`, `app_id`, `expire_time`, `image_url`, `license`, `modelKey`
    - The response parameter `host_network`, `restart_policy`, `app_url`, `name` changed to required
  - Changes of the interface `CreateWorkSpace`:
    - Add the response parameter `workspace_id`
    - Remove the response parameter `name`

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `sub_jobs_result`, `sub_jobs_list` to the interface `ShowJob`
  - Add the response parameters `sub_jobs_result`, `sub_jobs_list` to the interface `ShowJobProgress`

### HuaweiCloud SDK IoTEdge

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `protocol`, `edge_app_name` to the interface `BatchListEdgeApps`
  - Add the request parameters `edge_app_name`, `protocol` to the interface `CreateEdgeApp`
  - Add the response parameters `protocol`, `edge_app_name` to the interface `ShowEdgeApp`
  - Add the response parameter `name` to the interface `BatchListEdgeAppVersions`
  - Add the request parameters `supplier`, `tpl_id` to the interface `CreateEdgeApplicationVersion`
  - Add the response parameters `supplier`, `tpl_id` to the interface `ShowEdgeApplicationVersion`
  - Changes of the interface `UpdateEdgeApplicationVersion`:
    - Add the request parameter `tpl_id`
    - Add the response parameter `name`
  - Add the response parameter `name` to the interface `UpdateEdgeApplicationVersionState`
  - Add the request parameters `os_type`, `reliability_level`, `network_access_point`, `offline_cache_configs`, `device_auth_info` to the interface `CreateEdgeNode`
  - Add the response parameters `offline_cache_configs`, `device_auth_info` to the interface `ShowEdgeNode`

### HuaweiCloud SDK MapDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateCredential`:
    - Add the request parameter `credential`
    - Remove the request parameter `description`

### HuaweiCloud SDK VOD

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `name` changed to not required of the interface `UpdateTranscodeTemplate`
  - Changes of the interface `UpdateTemplateGroupCollection`:
    - The request parameter `collection_id` changed to required
    - The request parameter `name`, `template_group_list` changed to not required

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `tenant_id`, `created_at`, `updated_at` to the interface `ListVpcs`
  - Add the response parameters `tenant_id`, `created_at`, `updated_at` to the interface `CreateVpc`
  - Add the response parameters `tenant_id`, `created_at`, `updated_at` to the interface `ShowVpc`
  - Add the response parameters `tenant_id`, `created_at`, `updated_at` to the interface `UpdateVpc`
  - Add the response parameters `tenant_id`, `created_at`, `updated_at` to the interface `ListSubnets`
  - Add the response parameters `tenant_id`, `created_at`, `updated_at` to the interface `CreateSubnet`
  - Add the response parameters `tenant_id`, `created_at`, `updated_at` to the interface `ShowSubnet`
  - Add the response parameters `created_at`, `updated_at` to the interface `ListRouteTables`
  - Add the response parameters `created_at`, `updated_at` to the interface `CreateRouteTable`
  - Add the response parameters `created_at`, `updated_at` to the interface `ShowRouteTable`
  - Add the response parameters `created_at`, `updated_at` to the interface `UpdateRouteTable`
  - Add the response parameters `created_at`, `updated_at` to the interface `AssociateRouteTable`
  - Add the response parameters `created_at`, `updated_at` to the interface `DisassociateRouteTable`

# 3.1.19 2022-12-26

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateWorkflow`:
    - Add the request parameter `policy`
    - Remove the request parameters `citation_urns`, `information`, `alarm_name`
    - Remove the response parameters `param_name`, `domain_id`, `domain_name`
  - The request parameter `action` changed to not required of the interface `UpdateWorkflowTriggerStatus`
  - Remove the response parameters `workflow_urn`, `headers`, `input`, `output`, `created_by`, `node_id`, `begin_time`, `end_time`, `function_execution_id`, `output`, `status` from the interface `SearchWorkflowExecutionDetail`
  - Changes of the interface `ListAllScriptByName`:
    - Remove the request parameter `page_total`
    - The request parameter `order_by_column` changed to required
    - The request parameter `project_id` changed to not required
  - Changes of the interface `ListAllVersionByVersionId`:
    - Remove the request parameter `page_total`
    - The request parameter `order_by_column` changed to required
    - The request parameter `project_id` changed to not required
  - Changes of the interface `ListAllJobByName`:
    - Add the request parameter `enterprise_project_id`
    - Add the response parameters `is_latest_version`, `version_number`
    - The request parameter `order_by_column` changed to required
  - The request parameter `order_by_column` changed to required of the interface `ListTemplateByJobId`
  - The request parameter `share_type` changed to not required of the interface `SearchTemplateById`
  - Changes of the interface `ListWorkflow`:
    - Remove the request parameter `template_name_list`
    - Remove the response parameters `param_name`, `domain_id`, `domain_name`
  - Remove the response parameters `workflow_id`, `workflow_urn`, `status`, `headers`, `input`, `output`, `begin_time`, `end_time`, `last_update_time`, `created_by`, `execution_result_list`, `approve_user_name_list`, `project_id`, `workflow_edit_time`, `last_record_id_with_snapshot` from the interface `ExecuteWorkflow`
  - Remove the response parameters `workflow_urn`, `node_id`, `begin_time`, `end_time`, `function_execution_id`, `output`, `status` from the interface `ListWorkflowExecutions`
  - The request parameter `event_sn` changed to required of the interface `ListNotifiedHistories`
  - Modify the type `string` -> `enum` of the response parameter `type` of the interface `ShowActionRule`
  - Modify the type `string` -> `enum` of the request parameter `type` of the interface `AddActionRule`
  - Modify the type `string` -> `enum` of the request parameter `type` of the interface `UpdateActionRule`
  - Modify the type `string` -> `enum` of the response parameter `type` of the interface `ListActionRule`
  - The request parameter `resource_provider` changed to not required of the interface `AddEvent2alarmRule`
  - The request parameter `resource_provider` changed to not required of the interface `UpdateEventRule`
  - The response parameter `resource_provider` changed to not required of the interface `ListEvent2alarmRule`
  - Modify the type `string` -> `enum` of the request parameter `register_type` of the interface `CreateApp`
  - Changes of the interface `UpdateApp`:
    - Remove the response parameters `aom_id`, `app_id`, `create_time`, `creator`, `description`, `display_name`, `eps_id`, `modified_time`, `modifier`, `name`, `register_type`
    - Modify the type `string` -> `enum` of the request parameter `register_type`
  - Remove the request parameters `model_id`, `model_type` from the interface `UpdateComponent`
  - Changes of the interface `CreateEnv`:
    - The request parameter `component_id`, `os_type` changed to required
    - The request parameter `region` changed to not required
  - Changes of the interface `UpdateEnv`:
    - The request parameter `component_id`, `os_type` changed to required
    - The request parameter `region` changed to not required
  - Remove the response parameters `create_time`, `creator`, `description`, `modified_time`, `modifier`, `register_type`, `sub_app_id` from the interface `ShowComponentByName`

### HuaweiCloud SDK CBH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListCbhInstance`:
    - Add the response parameters `quotaDetail`, `publicip`, `expTime`, `startTime`, `endTime`, `releaseTime`, `instanceId`, `privateIp`, `taskStatus`, `vpcId`, `subnetId`, `securityGroupId`, `createinstanceStatus`, `failReason`, `instanceKey`, `orderId`, `periodNum`, `resourceId`, `alterPermit`, `publicId`, `bastionVersion`, `newBastionVersion`, `instanceStatus`, `instanceDescription`, `slaveZone`, `enterpriseProjectId`, `instanceType`, `haId`, `slaveZoneDisplay`, `webPort`, `vip`
    - Remove the response parameters `quota_detail`, `public_ip`, `exp_time`, `start_time`, `end_time`, `release_time`, `instance_id`, `private_ip`, `task_status`, `vpc_id`, `subnet_id`, `security_group_id`, `createinstance_status`, `fail_reason`, `instance_key`, `order_id`, `period_num`, `resource_id`, `alter_permit`, `public_id`, `bastion_version`, `new_bastion_version`, `instance_status`, `instance_description`
    - The response parameter `is_auto_renew` changed to not required
  - The response parameter `task_id`, `order_id` changed to not required of the interface `UpgradeCbhInstance`
  - Changes of the interface `ResetPassword`:
    - Add the response parameter `request_info`
    - Remove the response parameters `code`, `description`, `task_id`, `order_id`
  - Changes of the interface `ShowAvailableZoneInfo`:
    - Add the response parameter `availability_zone`
    - Remove the response parameter `availability_zones`
  - Changes of the interface `ResetLoginMethod`:
    - Add the response parameter `request_info`
    - Remove the response parameters `code`, `description`, `task_id`, `order_id`
  - Changes of the interface `ChangeInstanceNetwork`:
    - Add the response parameters `status`, `security_grp_status`, `public_eip_status`, `nics`
    - Remove the response parameters `type`, `security_groups`
    - The response parameter `firewall_status` changed to required
    - The response parameter `public_eip_statu` changed to not required
  - The request parameter `slave_availability_zone` changed to not required of the interface `CreateInstance`
  - Changes of the interface `ChangeInstanceOrder`:
    - Add the response parameter `orderId`
    - Remove the response parameter `order_id`

### HuaweiCloud SDK DSC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowSpecification`:
    - Add the response parameter `orderInfos`
    - Remove the response parameter `order_infos`
  - Add the response parameter `is_default` to the interface `ListRuleGroups`

### HuaweiCloud SDK HSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `laddr` to the interface `ListPorts`
  - Add the response parameters `os_name`, `agent_status` to the interface `ListProtectionServer`
  - Remove the response parameter `associated_vaults` from the interface `ShowBackupPolicyInfo`
  - Add the response parameters `os_type`, `event_details` to the interface `ListSecurityEvents`
  - Add the response parameter `enterprise_project_name` to the interface `ListAlarmWhiteList`
  - Remove the response parameter `repair_necessity` from the interface `ListVulHosts`

### HuaweiCloud SDK Live

- _Features_
  - Support the interface `UpdateDomainIp6Switch`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowDomain`:
    - Add the request parameter `enterprise_project_id`
    - Add the response parameters `enterprise_project_id`, `is_ipv6`
  - Changes of the interface `UpdateDomain`:
    - Add the request parameter `enterprise_project_id`
    - Add the response parameter `enterprise_project_id`
  - Add the request parameter `enterprise_project_id` to the interface `CreateDomain`

### HuaweiCloud SDK LTS

- _Features_
  - Support the following interfaces：
    - `Deletefavorite`
    - `ListTopnTrafficStatistics`
    - `Createfavorite`
    - `CreateTags`
    - `CreateDashboardGroup`
    - `CreateDashBoard`
    - `ListHistorySql`
    - `ListCriterias`
    - `CreateSearchCriterias`
    - `DeleteSearchCriterias`
    - `ListQueryAllSearchCriterias`
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameters `enterprise_project_name`, `ttl_in_days` from the interface `CreateLogStream`

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListTranscodingTask`:
    - Remove the response parameter `ref_frames_count`
    - The response parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Changes of the interface `CreateTranscodingTask`:
    - Remove the request parameters `ref_frames_count`, `aspect_ratio`
    - The request parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Changes of the interface `ListTemplate`:
    - Remove the response parameter `ref_frames_count`
    - The response parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Changes of the interface `CreateTransTemplate`:
    - Remove the request parameter `ref_frames_count`
    - The request parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Changes of the interface `UpdateTransTemplate`:
    - Remove the request parameter `ref_frames_count`
    - The request parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Changes of the interface `ListTemplateGroup`:
    - Remove the response parameters `ref_frames_count`, `aspect_ratio`
    - The response parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Changes of the interface `CreateTemplateGroup`:
    - Remove the request parameters `ref_frames_count`, `aspect_ratio`
    - The request parameter `name` changed to required
    - The request parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Changes of the interface `UpdateTemplateGroup`:
    - Remove the request parameters `ref_frames_count`, `aspect_ratio`
    - The request parameter `group_id` changed to required
    - The request parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Remove the request parameter `project_id` from the interface `UpdateBucketAuthorized`
  - Remove the request parameter `aspect_ratio` from the interface `CreateThumbnailsTask`
  - Changes of the interface `ListEditingJob`:
    - Remove the response parameters `ref_frames_count`, `ref_frames_count`
    - The response parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval`, `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required
  - Changes of the interface `CreateEditingJob`:
    - Remove the request parameters `ref_frames_count`, `ref_frames_count`
    - The request parameter `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval`, `codec`, `sample_rate`, `PVC`, `hls_interval`, `dash_interval` changed to not required

### HuaweiCloud SDK VOD

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `group_id`, `name`, `bitrate`, `frame_rate`, `video_codec`, `format`, `hls_interval` changed to required of the interface `UpdateTranscodeTemplate`
  - The response parameter `bitrate`, `frame_rate`, `video_codec`, `format`, `hls_interval` changed to required of the interface `ListTranscodeTemplate`
  - The request parameter `name`, `bitrate`, `frame_rate`, `video_codec`, `format`, `hls_interval` changed to required of the interface `CreateTranscodeTemplate`
  - The request parameter `name`, `template_group_list` changed to required of the interface `UpdateTemplateGroupCollection`
  - The request parameter `name`, `template_group_list` changed to required of the interface `CreateTemplateGroupCollection`

# 3.1.18 2022-12-22

### HuaweiCloud SDK APIG

- _Features_
  - Support the interfaces `ListProjectInstanceTags`, `ListInstanceTags`, `BatchCreateOrDeleteInstanceTags`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - Support the following interfaces：
    - `ExpandInstanceStorage`
    - `ListClusterScaleInNumbers`
    - `ListDisasterRecover`
    - `CreateDisasterRecovery`
    - `DeleteDataSource`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShrinkCluster`:
    - Add the request parameter `clusterShrinkReq`
    - Add the response parameter `job_id`
    - Remove the request parameters `shrink_number`, `online`, `type`, `retry`, `force_backup`, `need_agency`
  - Changes of the interface `ExecuteRedistributionCluster`:
    - Add the request parameter `redistributionReq`
    - Remove the request parameters `redis_mode`, `parallel_jobs`
  - Changes of the interface `CreateClusterWorkload`:
    - Add the request parameter `workload_status`
    - Add the response parameters `workload_res_code`, `workload_res_str`
    - Remove the request parameters `workload_switch`, `max_concurrency_num`
  - Changes of the interface `ListClusterWorkload`:
    - Add the response parameters `workload_res_code`, `workload_res_str`
    - The response parameter `workload_switch` changed to required
  - Changes of the interface `CreateWorkloadPlan`:
    - Add the request parameter `workloadPlan`
    - Add the response parameters `workload_res_code`, `workload_res_str`
    - Remove the request parameters `plan_id`, `plan_name`, `logical_cluster_name`
  - Changes of the interface `AddWorkloadQueue`:
    - Add the request parameter `workload_queue`
    - Add the response parameters `workload_res_code`, `workload_res_str`
    - Remove the request parameters `workload_queue_name`, `logical_cluster_name`, `short_query_optimize`, `short_query_concurrency_num`, `workload_resource_item_list`
  - Add the response parameters `workload_res_code`, `workload_res_str` to the interface `ListWorkloadQueue`
  - Changes of the interface `DeleteWorkloadQueue`:
    - Add the response parameters `workload_res_code`, `workload_res_str`
    - The request parameter `logical_cluster_name` changed to required
  - Changes of the interface `CopySnapshot`:
    - Add the request parameter `linkCopyReq`
    - Add the response parameter `snapshot_id`
    - Remove the request parameters `backup_name`, `description`
  - Remove the response parameters `version`, `configure_status` from the interface `ListAuditLog`
  - Changes of the interface `CreateDataSource`:
    - Add the request parameter `extDataSourceReq`
    - Add the response parameters `id`, `job_id`
    - Remove the request parameters `data_source_id`, `type`, `data_source_name`, `user_name`, `user_pwd`, `description`, `reboot`, `connect_info`
  - Changes of the interface `UpdateDataSource`:
    - Add the request parameter `reconfigure`
    - Add the response parameter `job_id`
    - Remove the request parameters `database`, `agency`
  - Add the response parameters `datastore`, `cluster_name`, `bak_expected_start_time`, `bak_keep_day`, `bak_period`, `db_user`, `progress`, `backup_key`, `prior_backup_key`, `base_backup_key`, `backup_device`, `total_backup_size`, `base_backup_name`, `support_inplace_restore`, `fine_grained_backup`, `backup_level`, `fine_grained_backup_detail`, `guest_agent_version`, `cluster_status` to the interface `ListSnapshotDetails`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowWorkflowExecutionForPage`:
    - Add the response parameter `created_by`
    - Remove the response parameter `create_by`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the interface `ModifyVolume`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `offset`, `limit` to the interface `ListAvailableFlavorInfos`

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `tag_name` changed to required of the interface `CreateTag`
  - Remove the request parameters `sim_card_id`, `partner`, `package_type`, `sim_type` from the interface `ListProPricePlans`
  - Changes of the interface `ListSimCards`:
    - Remove the request parameters `expire_time_duration`, `traffic_warning_threshold`, `sim_status_in`
    - Remove the response parameters `sn`, `supply_code`, `bundle_id`, `test_type`
  - Changes of the interface `StopSimCard`:
    - Remove the request parameter `price_plan_list`
    - Remove the response parameter `sim_price_plan_list`
  - Changes of the interface `ResetSimCard`:
    - Remove the request parameter `price_plan_list`
    - Remove the response parameter `sim_price_plan_list`
  - Remove the response parameters `sn`, `supply_code`, `bundle_id`, `test_type` from the interface `ShowSimCard`
  - Changes of the interface `ListSimPricePlans`:
    - Remove the request parameter `sim_price_plan_id`
    - Remove the response parameters `partner`, `partner_pid`

### HuaweiCloud SDK IEF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `purchase_id`, `state_details`, `cert_remaining_valid_time` to the interface `ListEdgeNodes`
  - Add the response parameters `purchase_id`, `state_details`, `cert_remaining_valid_time` to the interface `UpdateEdgeNode`
  - Add the response parameters `purchase_id`, `state_details`, `cert_remaining_valid_time` to the interface `ShowEdgeNodeDetail`
  - Add the response parameters `purchase_id`, `state_details`, `cert_remaining_valid_time` to the interface `ListEdgeGroups`
  - Add the response parameters `purchase_id`, `state_details`, `cert_remaining_valid_time` to the interface `UpdateEdgeGroup`
  - Add the response parameters `purchase_id`, `state_details`, `cert_remaining_valid_time` to the interface `ShowEdgeGroupDetail`
  - Add the response parameters `purchase_id`, `state_details`, `cert_remaining_valid_time` to the interface `UpdateEdgeGroupNodeBinding`

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `vault_id` to the interface `CopyImageCrossRegion`

### HuaweiCloud SDK IoTDA

- _Features_
  - Support the interface `SearchDevices`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `device_side` to the interface `CreateRule`
  - Add the response parameter `device_side` to the interface `ListRules`
  - Add the response parameter `device_side` to the interface `ShowRule`
  - Changes of the interface `UpdateRule`:
    - Add the request parameter `device_side`
    - Add the response parameter `device_side`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `sasl_enabled_mechanisms` to the interface `CreatePostPaidInstance`

### HuaweiCloud SDK RocketMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `enterprise_project_id`, `enable_acl` to the interface `CreatePostPaidInstance`

### HuaweiCloud SDK SFSTurbo

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateShare`:
    - Add the request parameter `CreateShareRequestBody`
    - Remove the request parameter `share`
  - Changes of the interface `ListShares`:
    - Modify the type `int32` -> `int64` of the request parameter `offset`
    - Modify the type `int32` -> `int64` of the request parameter `limit`
  - Changes of the interface `ExpandShare`:
    - Add the request parameter `ExpandShareRequestBody`
    - Remove the request parameter `extend`
  - Changes of the interface `CreateSharedTag`:
    - Add the request parameter `CreateSharedTagRequestBody`
    - Remove the request parameter `tag`
  - Changes of the interface `BatchAddSharedTags`:
    - Add the request parameter `BatchAddSharedTagsRequestBody`
    - Remove the request parameter `add_shareed_tags`

# 3.1.17 2022-12-19

### HuaweiCloud SDK APM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `function` changed to required of the interface `ShowMonitorItemViewConfig`
  - The request parameter `view_type`, `collector_name`, `metric_set`, `function`, `env_id`, `start_time`, `end_time` changed to required of the interface `ShowTrend`
  - The request parameter `view_type`, `collector_name`, `metric_set`, `function`, `page`, `page_size`, `env_id`, `start_time`, `end_time` changed to required of the interface `ShowSumTable`
  - Changes of the interface `ShowRawTable`:
    - Add the request parameter `last_row_id`
    - Remove the request parameter `lastRowId`
    - The request parameter `function` changed to required
  - Changes of the interface `SearchAgent`:
    - Add the request parameter `order_by_status`
    - Remove the request parameter `orderByStatus`

### HuaweiCloud SDK BCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `order_fade_enabled`, `is_support_tc3`, `order_fade_cache`, `deploy_status`, `block_info`, `cluster_platform_type`, `status`, `status_detail`, `order_fade_enabled` to the interface `ShowBlockchainDetail`
  - Add the response parameter `result` to the interface `DeleteMemberInvite`
  - Add the response parameter `result` to the interface `HandleNotification`
  - Changes of the interface `CreateNewBlockchain`:
    - Modify the type `string` -> `int64` of the request parameter `node_flavor`
    - Modify the type `string` -> `int64` of the request parameter `cce_flavor`
    - Modify the type `string` -> `int64` of the request parameter `init_node_pwd`
    - Modify the type `string` -> `int64` of the request parameter `az`
    - Modify the type `string` -> `int64` of the request parameter `cluster_platform_type`
  - Add the response parameter `result` to the interface `DownloadBlockchainCert`
  - Add the response parameter `result` to the interface `DownloadBlockchainSdkConfig`
  - Add the response parameter `filesystemUsage` to the interface `ListEntityMetric`
  - Add the response parameter `result` to the interface `CreateBlockchainCertByUserName`

### HuaweiCloud SDK CBH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `available_zone_id` changed to not required of the interface `CreateInstanceOrder`

### HuaweiCloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateVault`:
    - Add the enum values `workspace` to the request parameter `object_type`
    - Add the enum values `workspace` to the response parameter `object_type`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ListVault`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ShowVault`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `UpdateVault`
  - Add the enum values `OS::Workspace::DesktopV2` to the response parameter `resource_type` to the interface `ShowBackup`
  - Changes of the interface `ListBackups`:
    - Add the enum values `OS::Workspace::DesktopV2` to the request parameter `resource_type`
    - Add the enum values `OS::Workspace::DesktopV2` to the response parameter `resource_type`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ListProtectable`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ShowProtectable`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ShowVaultResourceInstances`

### HuaweiCloud SDK CC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `interflow_mode` to the interface `CreateBandwidthPackage`
  - Changes of the interface `ListInterRegionBandwidths`:
    - Add the response parameter `inter_region_bandwidths`
    - Remove the response parameter `inter_region_bandwidth`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateCluster`:
    - Add the request parameter `vpcPermissions`
    - Add the response parameter `orderId`
    - Remove the request parameter `vpcPermisssions`
    - Remove the response parameter `ordeId`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `server_id` to the interface `ListServersDetails`

### HuaweiCloud SDK EIP

- _Features_
  - Support the interfaces `ShowResourcesJobDetail`, `ChangeBandwidthToPeriod`, `ChangePublicipToPeriod`
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
  - Changes of the interface `CreateFunction`:
    - Add the request parameters `depend_version_list`, `func_vpc`
    - Add the response parameter `depend_version_list`
  - Changes of the interface `UpdateFunctionCode`:
    - Add the request parameter `depend_version_list`
    - Add the response parameter `depend_version_list`
  - Add the response parameter `depend_version_list` to the interface `ShowFunctionCode`
  - Add the response parameter `depend_version_list` to the interface `ShowFunctionConfig`
  - Changes of the interface `ListReservedInstanceConfigs`:
    - Add the request parameters `marker`, `limit`
    - Add the response parameter `reserved_instances`
    - Remove the response parameter `reservedinstances`
  - Add the response parameter `depend_version_list` to the interface `ImportFunction`
  - Changes of the interface `ListFunctionReservedInstances`:
    - Add the request parameter `limit`
    - Remove the request parameter `maxitems`
  - Changes of the interface `ShowWorkflowExecutionForPage`:
    - Add the request parameters `offset`, `limit`, `start_time`, `end_time`
    - Remove the request parameter `CreateWorkflowRequestBody`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameters `id`, `weight` from the interface `SetGaussMySqlProxyWeight`
  - Add the enum values `Pending` to the response parameter `status` to the interface `ShowGaussMySqlJobInfo`
  - Changes of the interface `ListScheduleJobs`:
    - Add the response parameter `job_status`
    - Remove the response parameter `task_status`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListConfigurationDatastores`:
    - Add the response parameter `datastore_name`
    - Remove the response parameter `datastore_type`
  - Remove the request parameters `instance`, `vcpus`, `ram` from the interface `ModifyEpsQuotas`
  - Remove the response parameters `instance`, `vcpus`, `ram`, `instance`, `vcpus`, `ram` from the interface `ListEpsQuotas`

### HuaweiCloud SDK HSS

- _Features_
  - Support the following interfaces：
    - `ShowAssetStatistic`
    - `ListUserStatistics`
    - `ListPortStatistics`
    - `ListProcessStatistics`
    - `ListAppStatistics`
    - `ListAutoLaunchStatistics`
    - `ListPorts`
    - `ListApps`
    - `ListAutoLaunchs`
    - `ListAppChangeHistories`
    - `ListAutoLaunchChangeHistories`
    - `ListProtectionServer`
    - `ListProtectionPolicy`
    - `UpdateProtectionPolicy`
    - `StartProtection`
    - `StopProtection`
    - `ShowBackupPolicyInfo`
    - `UpdateBackupPolicyInfo`
    - `ChangeEvent`
    - `ListAlarmWhiteList`
    - `ListHostGroups`
    - `ChangeHostsGroup`
    - `AddHostsGroup`
    - `DeleteHostsGroup`
    - `ListPolicyGroup`
    - `AssociatePolicyGroup`
    - `ListVulHosts`
    - `ChangeVulStatus`
    - `ListWtpProtectHost`
    - `SetWtpProtectionStatusInfo`
    - `SetRaspSwitch`
    - `ListHostProtectHistoryInfo`
    - `ListHostRaspProtectHistoryInfo`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `fix_status`, `enable_auto_fix`, `rule_params` to the interface `ListRiskConfigCheckRules`
  - Add the response parameter `extend_info` to the interface `ListSecurityEvents`
  - Changes of the interface `ListHostStatus`:
    - Add the response parameters `enterprise_project_id`, `agent_create_time`, `agent_update_time`, `agent_version`, `upgrade_status`, `upgrade_result_code`, `upgradable`
    - The request parameter `region` changed to required
  - The request parameter `vul_id` changed to required of the interface `ListVulnerabilities`

### HuaweiCloud SDK IEF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `key`, `value` changed to not required of the interface `ListTags`
  - The request parameter `key`, `value` changed to not required of the interface `CreateTag`
  - The response parameter `key`, `value` changed to not required of the interface `ListEdgeNodes`
  - The response parameter `key`, `value` changed to not required of the interface `ShowEdgeNodeDetail`
  - The response parameter `key`, `value` changed to not required of the interface `UpdateEdgeNode`
  - Add the request parameter `device_ids` to the interface `CreateEdgeGroup`
  - Changes of the interface `ListEdgeGroupCerts`:
    - Add the response parameter `groupcerts`
    - Remove the response parameter `edge_groups`
  - The response parameter `type` changed to not required of the interface `ListDevices`
  - The request parameter `type` changed to not required of the interface `CreateDevice`
  - The response parameter `type` changed to not required of the interface `ShowDevice`
  - The response parameter `type` changed to not required of the interface `UpdateDevice`
  - The response parameter `type` changed to not required of the interface `ShowDeviceTwin`
  - Changes of the interface `UpdateDeviceTwin`:
    - The request parameter `twin`, `property_visitors` changed to not required
    - The response parameter `type` changed to not required
  - The response parameter `key`, `value` changed to not required of the interface `ListDeviceTemplates`
  - The request parameter `key`, `value` changed to not required of the interface `CreateDeviceTemplate`
  - The response parameter `key`, `value` changed to not required of the interface `ShowDeviceTemplate`
  - The response parameter `key`, `value` changed to not required of the interface `UpdateDeviceTemplateById`
  - The response parameter `key`, `value` changed to not required of the interface `ListResourceByTags`
  - The request parameter `key`, `value` changed to not required of the interface `BatchAddDeleteTags`
  - The response parameter `read_only` changed to not required of the interface `ListApps`
  - The response parameter `read_only` changed to not required of the interface `ShowAppDetail`
  - The response parameter `read_only` changed to not required of the interface `UpdateApp`
  - The response parameter `read_only` changed to not required of the interface `ListAppVersions`
  - The request parameter `read_only` changed to not required of the interface `CreateAppVersions`
  - The response parameter `read_only` changed to not required of the interface `ShowAppVersionDetail`
  - Changes of the interface `UpdateAppVersion`:
    - The request parameter `read_only` changed to not required
    - The response parameter `read_only` changed to not required
  - The response parameter `host_network`, `read_only` changed to not required of the interface `ListDeployments`
  - The request parameter `host_network`, `read_only` changed to not required of the interface `CreateDeployments`
  - The response parameter `host_network`, `read_only` changed to not required of the interface `ShowDeployment`
  - Changes of the interface `UpdateDeployment`:
    - The request parameter `replicas`, `host_network`, `read_only` changed to not required
    - The response parameter `host_network`, `read_only` changed to not required
  - The response parameter `host_network`, `read_only`changed to not required of the interface `ListPods`
  - The request parameter `description` changed to not required of the interface `CreateEncryptdatas`
  - The request parameter `description` changed to not required of the interface `UpdateEncryptdatas`
  - Changes of the interface `ListBatchJob`:
    - Add the response parameters `task_total_count`, `task_success_count`, `task_failed_count`, `status_last_updated_at`, `description`
    - Remove the response parameters `task_count`, `success_count`, `failed_count`, `updated_at`
  - Changes of the interface `ShowBatchJob`:
    - Add the response parameter `status_last_updated_at`
    - Remove the response parameter `updated_at`

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `key` to the interface `CreateRecordCallbackConfig`
  - Changes of the interface `UpdateRecordCallbackConfig`:
    - Add the request parameter `key`
    - Add the response parameters `id`, `publish_domain`, `app`, `notify_callback_url`, `notify_event_subscription`, `sign_type`, `create_time`, `update_time`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `UpdateSqlAlarmRule`
  - Add the request parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `CreateSqlAlarmRule`
  - Add the response parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `ListSqlAlarmRules`
  - Add the request parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `UpdateKeywordsAlarmRule`
  - Add the request parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `CreateKeywordsAlarmRule`
  - Add the response parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `ListKeywordsAlarmRules`
  - The request parameter `host_id_list` changed to not required of the interface `ListHost`
  - The request parameter `is_analysis`, `is_analysis` changed to not required of the interface `UpdateStructConfig`
  - The request parameter `is_analysis`, `is_analysis` changed to not required of the interface `CreateStructConfig`

### HuaweiCloud SDK OSM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `resource_type_id` to the interface `ListAuthorizations`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `restart` changed to required of the interface `StartInstanceRestartAction`

### HuaweiCloud SDK Workspace

- _Features_
  - Support the interface `ShowQuotas`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.16 2022-12-15

### HuaweiCloud SDK APM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `function` changed to required of the interface `ShowMonitorItemViewConfig`
  - The request parameter `view_type`, `collector_name`, `metric_set`, `function`, `env_id`, `start_time`, `end_time` changed to required of the interface `ShowTrend`
  - The request parameter `view_type`, `collector_name`, `metric_set`, `function`, `page`, `page_size`, `env_id`, `start_time`, `end_time` changed to required of the interface `ShowSumTable`
  - Changes of the interface `ShowRawTable`:
    - Add the request parameter `last_row_id`
    - Remove the request parameter `lastRowId`
    - The request parameter `function` changed to required
  - Changes of the interface `SearchAgent`:
    - Add the request parameter `order_by_status`
    - Remove the request parameter `orderByStatus`

### HuaweiCloud SDK BCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `order_fade_enabled`, `is_support_tc3`, `order_fade_cache`, `deploy_status`, `block_info`, `cluster_platform_type`, `status`, `status_detail`, `order_fade_enabled` to the interface `ShowBlockchainDetail`
  - Add the response parameter `result` to the interface `DeleteMemberInvite`
  - Add the response parameter `result` to the interface `HandleNotification`
  - Changes of the interface `CreateNewBlockchain`:
    - Modify the type `string` -> `int64` of the request parameter `node_flavor`
    - Modify the type `string` -> `int64` of the request parameter `cce_flavor`
    - Modify the type `string` -> `int64` of the request parameter `init_node_pwd`
    - Modify the type `string` -> `int64` of the request parameter `az`
    - Modify the type `string` -> `int64` of the request parameter `cluster_platform_type`
  - Add the response parameter `result` to the interface `DownloadBlockchainCert`
  - Add the response parameter `result` to the interface `DownloadBlockchainSdkConfig`
  - Add the response parameter `filesystemUsage` to the interface `ListEntityMetric`
  - Add the response parameter `result` to the interface `CreateBlockchainCertByUserName`

### HuaweiCloud SDK CBH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `available_zone_id` changed to not required of the interface `CreateInstanceOrder`

### HuaweiCloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateVault`:
    - Add the enum values `workspace` to the request parameter `object_type`
    - Add the enum values `workspace` to the response parameter `object_type`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ListVault`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ShowVault`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `UpdateVault`
  - Add the enum values `OS::Workspace::DesktopV2` to the response parameter `resource_type` to the interface `ShowBackup`
  - Changes of the interface `ListBackups`:
    - Add the enum values `OS::Workspace::DesktopV2` to the request parameter `resource_type`
    - Add the enum values `OS::Workspace::DesktopV2` to the response parameter `resource_type`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ListProtectable`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ShowProtectable`
  - Add the enum values `workspace` to the response parameter `object_type` to the interface `ShowVaultResourceInstances`

### HuaweiCloud SDK CC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `interflow_mode` to the interface `CreateBandwidthPackage`
  - Changes of the interface `ListInterRegionBandwidths`:
    - Add the response parameter `inter_region_bandwidths`
    - Remove the response parameter `inter_region_bandwidth`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateCluster`:
    - Add the request parameter `vpcPermissions`
    - Add the response parameter `orderId`
    - Remove the request parameter `vpcPermisssions`
    - Remove the response parameter `ordeId`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `server_id` to the interface `ListServersDetails`

### HuaweiCloud SDK EIP

- _Features_
  - Support the interfaces `ShowResourcesJobDetail`, `ChangeBandwidthToPeriod`, `ChangePublicipToPeriod`
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
  - Changes of the interface `CreateFunction`:
    - Add the request parameters `depend_version_list`, `func_vpc`
    - Add the response parameter `depend_version_list`
  - Changes of the interface `UpdateFunctionCode`:
    - Add the request parameter `depend_version_list`
    - Add the response parameter `depend_version_list`
  - Add the response parameter `depend_version_list` to the interface `ShowFunctionCode`
  - Add the response parameter `depend_version_list` to the interface `ShowFunctionConfig`
  - Changes of the interface `ListReservedInstanceConfigs`:
    - Add the request parameters `marker`, `limit`
    - Add the response parameter `reserved_instances`
    - Remove the response parameter `reservedinstances`
  - Add the response parameter `depend_version_list` to the interface `ImportFunction`
  - Changes of the interface `ListFunctionReservedInstances`:
    - Add the request parameter `limit`
    - Remove the request parameter `maxitems`
  - Changes of the interface `ShowWorkflowExecutionForPage`:
    - Add the request parameters `offset`, `limit`, `start_time`, `end_time`
    - Remove the request parameter `CreateWorkflowRequestBody`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameters `id`, `weight` from the interface `SetGaussMySqlProxyWeight`
  - Add the enum values `Pending` to the response parameter `status` to the interface `ShowGaussMySqlJobInfo`
  - Changes of the interface `ListScheduleJobs`:
    - Add the response parameter `job_status`
    - Remove the response parameter `task_status`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListConfigurationDatastores`:
    - Add the response parameter `datastore_name`
    - Remove the response parameter `datastore_type`
  - Remove the request parameters `instance`, `vcpus`, `ram` from the interface `ModifyEpsQuotas`
  - Remove the response parameters `instance`, `vcpus`, `ram`, `instance`, `vcpus`, `ram` from the interface `ListEpsQuotas`

### HuaweiCloud SDK HSS

- _Features_
  - Support the following interfaces：
    - `ShowAssetStatistic`
    - `ListUserStatistics`
    - `ListPortStatistics`
    - `ListProcessStatistics`
    - `ListAppStatistics`
    - `ListAutoLaunchStatistics`
    - `ListPorts`
    - `ListApps`
    - `ListAutoLaunchs`
    - `ListAppChangeHistories`
    - `ListAutoLaunchChangeHistories`
    - `ListProtectionServer`
    - `ListProtectionPolicy`
    - `UpdateProtectionPolicy`
    - `StartProtection`
    - `StopProtection`
    - `ShowBackupPolicyInfo`
    - `UpdateBackupPolicyInfo`
    - `ChangeEvent`
    - `ListAlarmWhiteList`
    - `ListHostGroups`
    - `ChangeHostsGroup`
    - `AddHostsGroup`
    - `DeleteHostsGroup`
    - `ListPolicyGroup`
    - `AssociatePolicyGroup`
    - `ListVulHosts`
    - `ChangeVulStatus`
    - `ListWtpProtectHost`
    - `SetWtpProtectionStatusInfo`
    - `SetRaspSwitch`
    - `ListHostProtectHistoryInfo`
    - `ListHostRaspProtectHistoryInfo`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `fix_status`, `enable_auto_fix`, `rule_params` to the interface `ListRiskConfigCheckRules`
  - Add the response parameter `extend_info` to the interface `ListSecurityEvents`
  - Changes of the interface `ListHostStatus`:
    - Add the response parameters `enterprise_project_id`, `agent_create_time`, `agent_update_time`, `agent_version`, `upgrade_status`, `upgrade_result_code`, `upgradable`
    - The request parameter `region` changed to required
  - The request parameter `vul_id` changed to required of the interface `ListVulnerabilities`

### HuaweiCloud SDK IEF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `key`, `value` changed to not required of the interface `ListTags`
  - The request parameter `key`, `value` changed to not required of the interface `CreateTag`
  - The response parameter `key`, `value` changed to not required of the interface `ListEdgeNodes`
  - The response parameter `key`, `value` changed to not required of the interface `ShowEdgeNodeDetail`
  - The response parameter `key`, `value` changed to not required of the interface `UpdateEdgeNode`
  - Add the request parameter `device_ids` to the interface `CreateEdgeGroup`
  - Changes of the interface `ListEdgeGroupCerts`:
    - Add the response parameter `groupcerts`
    - Remove the response parameter `edge_groups`
  - The response parameter `type` changed to not required of the interface `ListDevices`
  - The request parameter `type` changed to not required of the interface `CreateDevice`
  - The response parameter `type` changed to not required of the interface `ShowDevice`
  - The response parameter `type` changed to not required of the interface `UpdateDevice`
  - The response parameter `type` changed to not required of the interface `ShowDeviceTwin`
  - Changes of the interface `UpdateDeviceTwin`:
    - The request parameter `twin`, `property_visitors` changed to not required
    - The response parameter `type` changed to not required
  - The response parameter `key`, `value` changed to not required of the interface `ListDeviceTemplates`
  - The request parameter `key`, `value` changed to not required of the interface `CreateDeviceTemplate`
  - The response parameter `key`, `value` changed to not required of the interface `ShowDeviceTemplate`
  - The response parameter `key`, `value` changed to not required of the interface `UpdateDeviceTemplateById`
  - The response parameter `key`, `value` changed to not required of the interface `ListResourceByTags`
  - The request parameter `key`, `value` changed to not required of the interface `BatchAddDeleteTags`
  - The response parameter `read_only` changed to not required of the interface `ListApps`
  - The response parameter `read_only` changed to not required of the interface `ShowAppDetail`
  - The response parameter `read_only` changed to not required of the interface `UpdateApp`
  - The response parameter `read_only` changed to not required of the interface `ListAppVersions`
  - The request parameter `read_only` changed to not required of the interface `CreateAppVersions`
  - The response parameter `read_only` changed to not required of the interface `ShowAppVersionDetail`
  - Changes of the interface `UpdateAppVersion`:
    - The request parameter `read_only` changed to not required
    - The response parameter `read_only` changed to not required
  - The response parameter `host_network`, `read_only` changed to not required of the interface `ListDeployments`
  - The request parameter `host_network`, `read_only` changed to not required of the interface `CreateDeployments`
  - The response parameter `host_network`, `read_only` changed to not required of the interface `ShowDeployment`
  - Changes of the interface `UpdateDeployment`:
    - The request parameter `replicas`, `host_network`, `read_only` changed to not required
    - The response parameter `host_network`, `read_only` changed to not required
  - The response parameter `host_network`, `read_only`changed to not required of the interface `ListPods`
  - The request parameter `description` changed to not required of the interface `CreateEncryptdatas`
  - The request parameter `description` changed to not required of the interface `UpdateEncryptdatas`
  - Changes of the interface `ListBatchJob`:
    - Add the response parameters `task_total_count`, `task_success_count`, `task_failed_count`, `status_last_updated_at`, `description`
    - Remove the response parameters `task_count`, `success_count`, `failed_count`, `updated_at`
  - Changes of the interface `ShowBatchJob`:
    - Add the response parameter `status_last_updated_at`
    - Remove the response parameter `updated_at`

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `key` to the interface `CreateRecordCallbackConfig`
  - Changes of the interface `UpdateRecordCallbackConfig`:
    - Add the request parameter `key`
    - Add the response parameters `id`, `publish_domain`, `app`, `notify_callback_url`, `notify_event_subscription`, `sign_type`, `create_time`, `update_time`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `UpdateSqlAlarmRule`
  - Add the request parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `CreateSqlAlarmRule`
  - Add the response parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `ListSqlAlarmRules`
  - Add the request parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `UpdateKeywordsAlarmRule`
  - Add the request parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `CreateKeywordsAlarmRule`
  - Add the response parameters `trigger_condition_count`, `trigger_condition_frequency`, `whether_recovery_policy`, `recovery_policy` to the interface `ListKeywordsAlarmRules`
  - The request parameter `host_id_list` changed to not required of the interface `ListHost`
  - The request parameter `is_analysis`, `is_analysis` changed to not required of the interface `UpdateStructConfig`
  - The request parameter `is_analysis`, `is_analysis` changed to not required of the interface `CreateStructConfig`

### HuaweiCloud SDK OSM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `resource_type_id` to the interface `ListAuthorizations`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `restart` changed to required of the interface `StartInstanceRestartAction`

### HuaweiCloud SDK Workspace

- _Features_
  - Support the interface `ShowQuotas`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.15 2022-12-08

### HuaweiCloud SDK MapDS

- _Features_
  - Support the `Map Data Service`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK AOS

- _Features_
  - Support the interfaces `GetExecutionPlan`, `DeleteExecutionPlan`, `DescribeExecutionPlan`, `GetStackMetadata`
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `executor` from the interface `ListExecutionPlans`
  - Remove the request parameter `executor` from the interface `CreateExecutionPlan`
  - Remove the request parameter `executor` from the interface `ApplyExecutionPlan`
  - Changes of the interface `ListStackEvents`:
    - Remove the request parameters `limit`, `marker`, `executor`
    - Remove the response parameter `next_marker`
  - Remove the request parameter `executor` from the interface `ListStacks`
  - Remove the request parameter `executor` from the interface `CreateStack`
  - Remove the request parameter `executor` from the interface `GetStackTemplate`
  - Changes of the interface `ListStackResources`:
    - Remove the request parameter `executor`
    - Remove the response parameters `create_time`, `update_time`
  - Changes of the interface `ListStackOutputs`:
    - Remove the request parameters `executor`, `limit`, `marker`
    - Remove the response parameter `next_marker`
  - Remove the request parameter `executor` from the interface `DeployStack`
  - Remove the request parameter `executor` from the interface `DeleteStack`

### HuaweiCloud SDK APM

- _Features_
  - Support the interfaces `SearchAgent`, `ChangeAgentStatus`, `DeleteAgent`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CBH

- _Features_
  - Support the following interfaces：
    - `ListQuotaState`
    - `ShowNetworkConfiguration`
    - `StopCbhInstance`
    - `UpgradeCbhInstance`
    - `RestartCbhInstance`
    - `InstallInstanceEip`
    - `UninstallInstanceEip`
    - `ResetPassword`
    - `ShowAvailableZoneInfo`
    - `StartCbhInstance`
    - `SearchQuota`
    - `ResetLoginMethod`
    - `CreateInstanceOrder`
    - `ChangeInstanceNetwork`
    - `CreateInstance`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListCbhInstance`:
    - Add the response parameters `public_ip`, `is_auto_renew`
    - Remove the request parameter `X-Auth-Token`
    - Remove the response parameter `publicip`
    - The response parameter `zh_cn`, `en_us`, `exp_time`, `start_time`, `end_time`, `release_time`, `instance_id`, `private_ip`, `task_status`, `vpc_id`, `subnet_id`, `security_group_id`, `createinstance_status`, `fail_reason`, `instance_key`, `order_id`, `period_num`, `resource_id`, `public_id`, `alter_permit`, `bastion_version`, `new_bastion_version`, `instance_status`, `instance_description` changed to required

### HuaweiCloud SDK CC

- _Features_
  - Support the following interfaces：
    - `ListDomainTags`
    - `DeleteTag`
    - `BatchCreateDeleteTags`
    - `ListResourceByFilterTag`
    - `ListTags`
    - `CreateTag`
    - `ListQuotas`
    - `ListBandwidthPackages`
    - `CreateBandwidthPackage`
    - `ShowBandwidthPackage`
    - `UpdateBandwidthPackage`
    - `DeleteBandwidthPackage`
    - `AssociateBandwidthPackage`
    - `DisassociateBandwidthPackage`
    - `ListInterRegionBandwidths`
    - `CreateInterRegionBandwidth`
    - `ShowInterRegionBandwidth`
    - `UpdateInterRegionBandwidth`
    - `DeleteInterRegionBandwidth`
    - `ListAuthorisations`
    - `CreateAuthorisation`
    - `ListPermissions`
    - `UpdateAuthorisation`
    - `DeleteAuthorisation`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `version` changed to not required of the interface `CreateAddonInstance`
  - The request parameter `version` changed to not required of the interface `UpdateAddonInstance`

### HuaweiCloud SDK CFW

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListIpsSwitchStatusUsingGet`:
    - Add the response parameters `id`, `virtual_patches_status`
    - Remove the response parameters `object_id`, `virtual_patches_stauts`
  - The request parameter `ips_type` changed to required of the interface `ChangeIpsSwitchUsingPost`
  - Remove the response parameters `fw_instance_id`, `resource_id`, `name`, `ha_type`, `charge_mode`, `service_type`, `engine_type`, `flavor`, `protect_objects`, `status`, `description`, `is_old_firewall_instance`, `support_ipv6`, `feature_toggle` from the interface `ListFirewallUsingGet`

### HuaweiCloud SDK CloudDeploy

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `enum` to the request parameter `type` to the interface `StartDeployTask`

### HuaweiCloud SDK DBSS

- _Features_
  - Support the following interfaces：
    - `ListAuditInstances`
    - `ShowAuditQuota`
    - `ListEcsSpecification`
    - `ListAvailabilityZoneInfos`
    - `ListAuditInstanceJobs`
    - `ListAuditDatabases`
    - `ListAuditOperateLogs`
    - `ListAuditRuleScopes`
    - `ListSqlInjectionRules`
    - `ListAuditRuleRisks`
    - `ShowAuditRuleRisk`
    - `ListAuditSensitiveMasks`
    - `ListProjectResourceTags`
    - `ListResourceInstanceByTag`
    - `CountResourceInstanceByTag`
    - `BatchAddResourceTag`
    - `BatchDeleteResourceTag`
    - `CreateInstancesPeriodOrder`
    - `UpdateAuditSecurityGroup`
    - `AddRdsNoAgentDatabase`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `name`, `job_type`, `engine_type`, `job_direction`, `task_type`, `net_type`, `enterprise_project_id`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `is_auto_renew`, `security_group_id` changed to not required of the interface `BatchCreateJobsAsync`
  - The request parameter `name`, `job_type`, `engine_type`, `job_direction`, `task_type`, `net_type`, `enterprise_project_id`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `is_auto_renew`, `security_group_id` changed to not required of the interface `CreateJob`
  - The response parameter `name`, `job_type`, `engine_type`, `job_direction`, `task_type`, `net_type`, `enterprise_project_id`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `is_auto_renew`, `security_group_id` changed to not required of the interface `ListAsyncJobDetail`
  - The request parameter `name`, `job_type`, `engine_type`, `job_direction`, `task_type`, `net_type`, `enterprise_project_id`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `is_auto_renew`, `security_group_id` changed to not required of the interface `UpdateBatchAsyncJobs`
  - The response parameter `name`, `job_type`, `engine_type`, `job_direction`, `task_type`, `net_type`, `enterprise_project_id`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `is_auto_renew`, `security_group_id` changed to not required of the interface `ShowJobDetail`
  - The request parameter `name`, `job_type`, `engine_type`, `job_direction`, `task_type`, `net_type`, `enterprise_project_id`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum`, `is_auto_renew`, `security_group_id` changed to not required of the interface `UpdateJob`
  - Changes of the interface `ExecuteJobAction`:
    - Add the request parameters `is_sync_re_edit`, `force_delete`
    - The request parameter `job_id`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum` changed to not required
  - Changes of the interface `BatchExecuteJobActions`:
    - Add the request parameters `is_sync_re_edit`, `force_delete`
    - The request parameter `job_id`, `ip`, `db_port`, `ssl_link`, `ssl_cert_name`, `ssl_cert_key`, `ssl_cert_check_sum` changed to not required

### HuaweiCloud SDK DSC

- _Features_
  - Support the following interfaces：
    - `CreateProductOrder`
    - `ShowSpecification`
    - `ShowTopics`
    - `UpdateDefaultTopic`
    - `ShowRules`
    - `ChangeRule`
    - `AddRule`
    - `DeleteRule`
    - `ListRuleGroups`
    - `AddRuleGroup`
    - `DeleteRuleGroup`
    - `AddScanJob`
    - `ListRelationDb`
    - `ListRelationTable`
    - `ListRelationColumn`
    - `ListRelationBuckets`
    - `ListRelationFile`
    - `ListDbMaskTask`
    - `ChangeDbTemplateOperation`
    - `UpdateAssetName`
    - `ListBuckets`
    - `AddBuckets`
    - `DeleteBucket`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - Support the interfaces `ListHostOverview`, `ListHostDisk`, `ListHostNet`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK EIP

- _Features_
  - Support the following interfaces：
    - `ListBandwidthPkg`
    - `CountPublicIp`
    - `ShowPublicIpType`
    - `CountPublicIpInstance`
    - `BatchCreatePublicips`
    - `BatchDeletePublicIp`
    - `BatchDisassociatePublicips`
    - `CountEipAvailableResources`
- _Bug Fix_
  - None
- _Change_
  - Remove the enum values `` from the request parameter `associate_instance_type` from the interface `AssociatePublicips`
  - Remove the enum values `` from the request parameter `associate_instance_type` from the interface `UpdateAssociatePublicip`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `dep_id` to the interface `CreateDependency`
  - Add the response parameter `dep_id` to the interface `CreateDependencyVersion`
  - Add the request parameters `enable_dynamic_memory`, `enable_auth_in_header` to the interface `UpdateFunctionConfig`
  - Changes of the interface `ShowWorkflowExecutionForPage`:
    - Add the request parameters `offset`, `limit`
    - Add the response parameters `total`, `size`, `executions`
    - Remove the request parameters `page`, `page_size`
    - Remove the response parameters `pager`, `hisRecords`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the following interfaces：
    - `RestartGaussMySqlInstance`
    - `ShowGaussMySqlConfiguration`
    - `UpdateGaussMySqlConfiguration`
    - `DeleteGaussMySqlConfiguration`
    - `SwitchGaussMySqlConfiguration`
    - `RestartGaussMySqlNode`
    - `UpdateProxySessionConsistence`
    - `ListImmediateJobs`
    - `ListScheduleJobs`
    - `CancelScheduleTask`
    - `DeleteTaskRecord`
    - `UpgradeGaussMySqlInstanceDatabase`
    - `SwitchGaussMySqlInstanceSsl`
    - `UpdateGaussMySqlInstanceEip`
    - `CancelGaussMySqlInstanceEip`
    - `InvokeGaussMySqlInstanceSwitchOver`
    - `UpdateGaussMySqlInstanceOpsWindow`
    - `UpdateGaussMySqlInstanceSecurityGroup`
    - `UpdateGaussMySqlInstanceInternalIp`
    - `UpdateGaussMySqlInstancePort`
    - `UpdateGaussMySqlInstanceAlias`
    - `DeleteGaussMySqlBackup`
    - `CreateGaussMySqlConfiguration`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListAvailableFlavorInfos`:
    - Add the request parameter `x-auth-token`
    - Add the response parameter `list`
    - Remove the response parameter `optional_flavor_list`
    - The response parameter `instance_id`, `instance_name`, `vcpus`, `ram`, `spec_code`, `az_status`, `region_status`, `total_count` changed to required
  - Changes of the interface `ShowSlowLogDesensitization`:
    - Add the request parameter `x-auth-token`
    - The response parameter `desensitization_status` changed to required
  - The response parameter `type`, `key`, `values`, `total_count` changed to required of the interface `ListProjectTags`
  - The request parameter `instance`, `vcpus`, `ram` changed to required of the interface `ModifyEpsQuotas`
  - Changes of the interface `ListEpsQuotas`:
    - Remove the response parameters `enterprise_project_id`, `enterprise_project_name`, `quota`, `used`
    - The response parameter `total_count` changed to required

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `publicip_id` to the interface `ResizeInstance`

### HuaweiCloud SDK LTS

- _Features_
  - Support the interface `ListTimeLineTrafficStatistics`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interfaces `DownloadAttachment`, `DeleteAttachment`, `ListStatusStatistic`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id` to the interface `CreateIssueV4`
  - Add the response parameters `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id` to the interface `ListIssuesSfV4`
  - Add the response parameters `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id` to the interface `ListIssuesV4`
  - Add the response parameters `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id` to the interface `UpdateIssueV4`
  - Add the response parameters `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id` to the interface `ShowIssueV4`
  - Add the response parameters `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id` to the interface `ListChildIssuesV4`
  - Add the response parameters `user_id`, `user_num_id` to the interface `ListProjectIssuesRecordsV4`
  - Add the response parameters `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id`, `user_id`, `user_num_id` to the interface `CreateSystemIssueV4`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ShowSecondLevelMonitoring`, `SetSecondLevelMonitor`, `ShowAutoEnlargePolicy`, `SetAutoEnlargePolicy`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RocketMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `broker_num` changed to required of the interface `CreatePostPaidInstance`
  - Changes of the interface `UpdateInstance`:
    - Add the request parameter `enable_acl`
    - Remove the request parameter `retention_policy`
  - Add the response parameter `job_id` to the interface `BatchUpdateConsumerGroup`
  - Changes of the interface `ShowGroup`:
    - Add the response parameters `app_id`, `app_name`, `permissions`
    - Remove the response parameter `from_beginning`

### HuaweiCloud SDK TMS

- _Features_
  - Support the following interfaces：
    - `ListResource`
    - `CreateResourceTag`
    - `DeleteResourceTag`
    - `ListTagKeys`
    - `ListTagValues`
    - `ShowResourceTag`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.14 2022-12-01

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `formula` to the interface `ListCustomerselfResourceRecords`

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `formula` to the interface `ListCustomerselfResourceRecords`

### HuaweiCloud SDK CFW

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListIpsSwitchStatusUsingGet`:
    - Add the response parameter `data`
    - Remove the response parameters `object_id`, `basic_defense_status`, `virtual_patches_stauts`
  - Changes of the interface `ListEastWestFirewall`:
    - Add the response parameter `protect_infos`
    - Remove the response parameter `protected_infos`
  - The request parameter `fw_instance_id` changed to not required of the interface `ListAttackLogs`
  - Add the request parameter `type` to the interface `UpdateRuleAclUsingPut`
  - Add the request parameters `list_type`, `object_id` to the interface `UpdateBlackWhiteListUsingPut`
  - Changes of the interface `ListFirewallUsingGet`:
    - Add the response parameter `data`
    - Remove the response parameters `fw_instance_id`, `resource_id`, `name`, `ha_type`, `charge_mode`, `service_type`, `engine_type`, `flavor`, `protect_objects`, `status`, `description`, `is_old_firewall_instance`, `support_ipv6`, `feature_toggle`
  - Changes of the interface `ListServiceSetDetails`:
    - Add the response parameter `data`
    - Remove the response parameters `id`, `name`, `description`
  - Changes of the interface `CountEips`:
    - Add the response parameter `data`
    - Remove the response parameters `object_id`, `eip_total`, `eip_protected`
  - Changes of the interface `ListEipResources`:
    - Add the response parameter `data`
    - Remove the response parameters `id`, `public_ip`, `status`, `public_ipv6`, `enterprise_project_id`, `device_id`, `device_name`, `device_owner`, `associate_instance_type`
  - Add the request parameter `address_type` to the interface `UpdateAddressSetInfoUsingPut`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interfaces `CreateAcceptance`, `CreateRequest`, `ShowResult`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - Support the following interfaces：
    - `CheckCluster`
    - `ShrinkCluster`
    - `ListDssPools`
    - `ListStatistics`
    - `SwitchOverCluster`
    - `CancelReadonlyCluster`
    - `UpdateMaintenanceWindow`
    - `ListClusterCn`
    - `BatchCreateClusterCn`
    - `BatchDeleteClusterCn`
    - `ListClusterConfigurations`
    - `ListClusterConfigurationsParameter`
    - `UpdateConfiguration`
    - `ListSnapshotStatistics`
    - `ExecuteRedistributionCluster`
    - `ListClusterWorkload`
    - `CreateClusterWorkload`
    - `CreateWorkloadPlan`
    - `ListWorkloadQueue`
    - `AddWorkloadQueue`
    - `DeleteWorkloadQueue`
    - `CopySnapshot`
    - `ListClusterSnapshots`
    - `DeleteSnapshotPolicy`
    - `ListSnapshotPolicy`
    - `CreateSnapshotPolicy`
    - `DeleteDisasterRecovery`
    - `StartDisasterRecovery`
    - `PauseDisasterRecovery`
    - `SwitchoverDisasterRecovery`
    - `SwitchFailoverDisaster`
    - `RestoreDisaster`
    - `ListAuditLog`
    - `ListDataSource`
    - `CreateDataSource`
    - `UpdateDataSource`
    - `ListElbs`
    - `AssociateElb`
    - `DisassociateElb`
    - `AssociateEip`
    - `DisassociateEip`
    - `UpdateClusterDns`
    - `CreateClusterDns`
    - `DeleteClusterDns`
    - `ListAlarmConfigs`
    - `ListAlarmDetail`
    - `ListAlarmStatistic`
    - `ListAlarmSubs`
    - `CreateAlarmSub`
    - `UpdateAlarmSub`
    - `DeleteAlarmSub`
    - `ListEvents`
    - `ListEventSpecs`
    - `ListEventSubs`
    - `CreateEventSub`
    - `UpdateEventSub`
    - `DeleteEventSub`
    - `ListJobDetails`
    - `ListQuotas`
    - `ListTags`
    - `ListClusterTags`
    - `BatchCreateResourceTag`
    - `BatchDeleteResourceTag`
    - `ListAvailabilityZones`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the interface `AsyncInvokeReservedFunction`
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `http` to the response parameter `runtime` to the interface `ListDependencies`
  - Add the enum values `http` to the response parameter `runtime` to the interface `ListDependencyVersion`
  - Changes of the interface `CreateFunction`:
    - Add the enum values `http` to the request parameter `runtime`
    - Add the enum values `http` to the response parameter `runtime`
  - Add the enum values `http` to the response parameter `runtime` to the interface `ListFunctions`
  - Add the enum values `http` to the response parameter `runtime` to the interface `UpdateFunctionCode`
  - Add the enum values `http` to the response parameter `runtime` to the interface `ShowFunctionCode`
  - Changes of the interface `UpdateFunctionConfig`:
    - Add the enum values `http` to the request parameter `runtime`
    - Add the enum values `http` to the response parameter `runtime`
  - Add the enum values `http` to the response parameter `runtime` to the interface `ShowFunctionConfig`
  - Add the enum values `http` to the response parameter `runtime` to the interface `UpdateFunctionMaxInstanceConfig`
  - Changes of the interface `ListReservedInstanceConfigs`:
    - Add the response parameters `reservedinstances`, `page_info`, `count`
    - Remove the response parameters `function_urn`, `qualifier_type`, `qualifier_name`, `min_count`, `idle_mode`, `tactics_config`
  - Add the enum values `http` to the response parameter `runtime` to the interface `CreateFunctionVersion`
  - Add the enum values `http` to the response parameter `runtime` to the interface `ListFunctionVersions`
  - Add the enum values `http` to the response parameter `runtime` to the interface `ImportFunction`

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `sim_card_id`, `partner`, `package_type`, `sim_type` to the interface `ListProPricePlans`
  - Changes of the interface `ListSimCards`:
    - Add the request parameters `expire_time_duration`, `traffic_warning_threshold`, `sim_status_in`
    - Add the response parameters `sn`, `supply_code`, `bundle_id`, `test_type`
  - Changes of the interface `StopSimCard`:
    - Add the request parameter `price_plan_list`
    - Add the response parameter `sim_price_plan_list`
  - Changes of the interface `ResetSimCard`:
    - Add the request parameter `price_plan_list`
    - Add the response parameter `sim_price_plan_list`
  - Add the response parameters `sn`, `supply_code`, `bundle_id`, `test_type` to the interface `ShowSimCard`
  - Add the response parameter `order_id` to the interface `ListSimPools`
  - Changes of the interface `ListSimPricePlans`:
    - Add the request parameter `sim_price_plan_id`
    - Add the response parameters `partner`, `partner_pid`
  - Add the response parameter `id` to the interface `CreateAttribute`

### HuaweiCloud SDK Image

- _Features_
  - Support the interfaces `RunQueryCustomTags`, `RunDeleteCustomTags`, `RunImageMediaTaggingDet`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `use_default_tags` to the interface `RunImageMediaTagging`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `CopyConfiguration`, `ListInstanceParamHistories`, `ListMsdtcHosts`, `BatchAddMsdtcs`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IEF

- _Features_
  - Support the following interfaces：
    - `ListEdgeGroups`
    - `CreateEdgeGroup`
    - `ShowEdgeGroupDetail`
    - `UpdateEdgeGroup`
    - `DeleteEdgeGroup`
    - `UpdateEdgeGroupNodeBinding`
    - `ListEdgeGroupCerts`
    - `CreateEdgeGroupCert`
    - `ShowEdgeGroupCertDetail`
    - `DeleteEdgeGroupCert`
    - `ListSystemEvents`
    - `CreateSystemEvent`
    - `ShowSystemEventDetail`
    - `DeleteSystemEvent`
    - `StartSystemEvent`
    - `StopSystemEvent`
    - `ListBatchJob`
    - `CreateBatchJob`
    - `ShowBatchJob`
    - `DeleteBatchJob`
    - `StopBatchJob`
    - `ListProducts`
    - `CreateProduct`
    - `ShowProductDetail`
    - `DeleteProduct`
    - `RestoreBatchJob`
    - `RetryBatchJob`
    - `ShowQuota`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListEdgeNodes`:
    - Add the response parameter `identifier`
  - Changes of the interface `ShowEdgeNodeDetail`:
    - Add the response parameter `identifier`
  - Changes of the interface `UpdateEdgeNode`:
    - Add the response parameter `identifier`
  - Changes of the interface `UpdateNodeByDeviceId`:
    - The request parameter `relation`, `comment` changed to not required
    - The response parameter `relation`, `comment` changed to not required
  - Changes of the interface `ListApps`:
    - Add the response parameter `run_as_user`
    - Modify the type `string` -> `boolean` of the response parameter `host_pid`
  - Changes of the interface `ShowAppDetail`:
    - Add the response parameter `run_as_user`
    - Modify the type `string` -> `boolean` of the response parameter `host_pid`
  - Changes of the interface `UpdateApp`:
    - Add the response parameter `run_as_user`
    - Modify the type `string` -> `boolean` of the response parameter `host_pid`
  - Changes of the interface `ListAppVersions`:
    - Add the response parameter `run_as_user`
    - Modify the type `string` -> `boolean` of the response parameter `host_pid`
  - Changes of the interface `CreateAppVersions`:
    - Add the request parameter `run_as_user`
    - Modify the type `string` -> `boolean` of the request parameter `host_pid`
  - Changes of the interface `ShowAppVersionDetail`:
    - Add the response parameter `run_as_user`
    - Modify the type `string` -> `boolean` of the response parameter `host_pid`
  - Changes of the interface `UpdateAppVersion`:
    - Add the request parameter `run_as_user`
    - Add the response parameter `run_as_user`
    - Modify the type `string` -> `boolean` of the request parameter `host_pid`
    - Modify the type `string` -> `boolean` of the response parameter `host_pid`
  - Changes of the interface `ListDeployments`:
    - Add the response parameters `run_as_user`, `run_as_user`
  - Add the request parameters `run_as_user`, `run_as_user` to the interface `CreateDeployments`
  - Changes of the interface `ShowDeployment`:
    - Add the response parameters `run_as_user`, `run_as_user`
  - Changes of the interface `UpdateDeployment`:
    - Add the request parameters `run_as_user`, `run_as_user`
    - Add the response parameters `run_as_user`, `run_as_user`

# 3.1.13 2022-11-30

### HuaweiCloud SDK AOM

- _Features_
  - Support the following interfaces：
    - `ListNotifiedHistories`
    - `ListMuteRule`
    - `UpdateMuteRule`
    - `AddMuteRules`
    - `DeleteMuteRules`
    - `ShowActionRule`
    - `ListActionRule`
    - `UpdateActionRule`
    - `AddActionRule`
    - `DeleteActionRule`
    - `ListEvent2alarmRule`
    - `UpdateEventRule`
    - `AddEvent2alarmRule`
    - `DeleteEvent2alarmRule`
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `enum` of the request parameter `statistic` of the interface `AddAlarmRule`

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `retry_count`, `retry_count` to the interface `CreateApiV2`
  - Changes of the interface `UpdateApiV2`:
    - Add the request parameters `retry_count`, `retry_count`
    - Add the response parameters `retry_count`, `retry_count`
  - Add the response parameters `retry_count`, `retry_count` to the interface `ShowDetailsOfApiV2`
  - Add the response parameters `retry_count`, `retry_count` to the interface `ListApiVersionDetailV2`
  - Add the request parameter `is_http_redirect_to_https` to the interface `AssociateDomainV2`
  - Add the request parameter `is_http_redirect_to_https` to the interface `UpdateDomainV2`
  - Add the request parameter `labels` to the interface `ImportMicroservice`
  - Add the response parameter `is_http_redirect_to_https` to the interface `ListAttachedDomainsV2`

### HuaweiCloud SDK CPH

- _Features_
  - Support the interfaces `PushFile`, `InstallApk`, `UninstallApk`, `PushShareFiles`
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `DeleteShareFiles`
  - The response parameter `band_widths`, `request_id` changed to not required of the interface `ShowBandwidthDetail`
  - The response parameter `request_id` changed to not required of the interface `UpdateBandwidth`
  - The response parameter `encode_servers`, `request_id` changed to not required of the interface `ListEncodeServers`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `RestartEncodeServer`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `ListJobs`
  - The response parameter `error_msg`, `execute_msg`, `job_id`, `end_time`, `begin_time`, `error_code`, `status`, `request_id` changed to not required of the interface `ShowJob`
  - The response parameter `phone_images`, `request_id` changed to not required of the interface `ListCloudPhoneImages`
  - Changes of the interface `ListCloudPhoneModels`:
    - Add the request parameter `status`
    - The response parameter `phone_models`, `request_id` changed to not required
  - The response parameter `phones`, `request_id` changed to not required of the interface `ListCloudPhones`
  - The response parameter `order_id`, `product_id`, `request_id` changed to not required of the interface `CreateCloudPhoneServer`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `ImportTraffic`
  - The response parameter `phone_name`, `server_id`, `phone_id`, `image_id`, `vnc_enable`, `phone_model_name`, `status`, `access_infos`, `property`, `metadata`, `create_time`, `update_time`, `request_id` changed to not required of the interface `ShowCloudPhoneDetail`
  - The response parameter `request_id` changed to not required of the interface `UpdatePhoneName`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `BatchMigrateCloudPhone`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `ResetCloudPhone`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `RestartCloudPhone`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `BatchImportCloudPhoneData`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `StopCloudPhone`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `BatchExportCloudPhoneData`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `UpdateCloudPhoneProperty`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `RunShellCommand`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `PushShareApps`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `DeleteShareApps`
  - Changes of the interface `DeleteShareFiles`:
    - Add the request parameter `DeleteShareFilesRequestBody`
    - Remove the request parameter `PushShareFilesRequestBody`
    - The response parameter `jobs`, `request_id` changed to not required
  - The response parameter `jobs`, `request_id` changed to not required of the interface `RunSyncCommand`
  - The response parameter `server_models`, `request_id` changed to not required of the interface `ListCloudPhoneServerModels`
  - The response parameter `servers`, `request_id` changed to not required of the interface `ListCloudPhoneServers`
  - The response parameter `server_name`, `availability_zone`, `server_id`, `server_model_name`, `phone_model_name`, `keypair_name`, `status`, `vpc_id`, `cidr`, `vpc_cidr`, `subnet_id`, `subnet_cidr`, `resource_project_id`, `metadata`, `intranet_ip`, `access_ip`, `server_ip`, `public_ip`, `band_width_name`, `band_width_id`, `band_width_size`, `band_width_charge_mode`, `band_width_share_type`, `create_time`, `update_time`, `volume_name`, `volume_id`, `volume_size`, `volume_type`, `create_time`, `update_time`, `network_version`, `security_groups`, `create_time`, `update_time`, `request_id` changed to not required of the interface `ShowCloudPhoneServerDetail`
  - The response parameter `request_id` changed to not required of the interface `UpdateServerName`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `RestartCloudPhoneServer`
  - The response parameter `order_id`, `product_id`, `request_id` changed to not required of the interface `ChangeCloudPhoneServerModel`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `UpdateKeypair`
  - The response parameter `jobs`, `request_id` changed to not required of the interface `ListShareFiles`
  - The response parameter `order_id`, `product_id`, `request_id` changed to not required of the interface `CreateNet2CloudPhoneServer`

### HuaweiCloud SDK DDM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `is_auto_pay` to the interface `ExpandInstanceNodes`

### HuaweiCloud SDK DDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `int32` of the request parameter `num` of the interface `AddReadonlyNode`

### HuaweiCloud SDK EIP

- _Features_
  - Support the interfaces `DisassociatePublicips`, `AssociatePublicips`
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
  - Add the request parameter `metric_type` to the interface `ShowTenantMetric`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the following interfaces：
    - `ListAvailableFlavorInfos`
    - `CheckWeekPassword`
    - `ModifyPort`
    - `UpdateClientNetwork`
    - `DeleteEnlargeFailNode`
    - `ShowIpNumRequirement`
    - `ShowAutoEnlargePolicy`
    - `ShowSlowLogDesensitization`
    - `SwitchSlowlogDesensitization`
    - `ShowErrorLog`
    - `CopyConfiguration`
    - `CompareConfiguration`
    - `ListConfigurationDatastores`
    - `ShowAllInstancesBackups`
    - `CreateBack`
    - `ShowRecyclePolicy`
    - `SetRecyclePolicy`
    - `ListRecycleInstances`
    - `ShowPauseResumeStutus`
    - `PauseResumeDataSynchronization`
    - `ListProjectTags`
    - `ListEpsQuotas`
    - `ModifyEpsQuotas`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `public_ip`, `public_ip_id` changed to not required of the interface `ModifyPublicIp`
  - Add the request parameter `SwitchToMasterDisasterRecoveryBody` to the interface `SwitchToMaster`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the following interfaces：
    - `CopyConfiguration`
    - `DeleteJob`
    - `ListEpsQuotas`
    - `ModifyEpsQuota`
    - `ListAvailableFlavors`
    - `ShowSslCertDownloadLink`
    - `ListApplicableInstances`
    - `ListAppliedHistories`
    - `ListRestorableInstances`
    - `ListTasks`
    - `ShowDeploymentForm`
    - `ShowInstanceDisk`
    - `ListProjectTags`
    - `ListInstanceTags`
    - `AddInstanceTags`
    - `ShowProjectQuotas`
    - `ListRecycleInstances`
    - `ShowConfigurationDetail`
    - `DeleteConfiguration`
    - `ListConfigurationsDiff`
    - `ShowBalanceStatus`
    - `ShowInstanceSnapshot`
    - `ValidateWeakPassword`
    - `ListHistoryOperations`
    - `ListBindedEips`
    - `ResetConfiguration`
    - `ListGaussDbDatastores`
    - `AttachEip`
    - `ListPredefinedTags`
    - `SwitchConfiguration`
    - `ValidateParaGroupName`
    - `ShowRecyclePolicy`
    - `CreateConfigurationTemplate`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `enable_standby_backup` to the interface `ShowBackupPolicy`
  - Add the request parameter `enable_standby_backup` to the interface `SetBackupPolicy`

### HuaweiCloud SDK MPC

- _Features_
  - Support the following interfaces：
    - `ListNotifySmnTopicConfig`
    - `NotifySmnTopicConfig`
    - `ListNotifyEvent`
    - `DeleteTranscodingTaskByConsole`
    - `ListStatSummary`
    - `ListAllBuckets`
    - `UpdateBucketAuthorized`
    - `ListAllObsObjList`
    - `ShowAgenciesTask`
    - `CreateAgenciesTask`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK MRS

- _Features_
  - Support the interfaces `UpdateClusterName`, `ShowAutoScalingPolicy`
- _Bug Fix_
  - None
- _Change_
  - The response parameter `result` changed to required of the interface `UpdateAgencyMapping`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `boolean` of the response parameter `read_only_by_user` of the interface `ListInstances`

### HuaweiCloud SDK ROMA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `status` from the interface `UpdateProduct`
  - Remove the response parameters `bool_false`, `bool_true` from the interface `ListProperties`
  - Remove the request parameters `bool_false`, `bool_true` from the interface `CreateProperty`
  - Remove the response parameters `bool_false`, `bool_true` from the interface `ShowProperty`
  - Changes of the interface `UpdateProperty`:
    - Remove the request parameters `bool_false`, `bool_true`
    - Remove the response parameters `bool_false`, `bool_true`
  - Remove the response parameters `bool_false`, `bool_true` from the interface `ListRequestProperties`
  - Changes of the interface `CreateRequestProperty`:
    - Remove the request parameters `bool_false`, `bool_true`
    - Remove the response parameters `bool_false`, `bool_true`
  - Remove the response parameters `bool_false`, `bool_true` from the interface `ShowRequestProperty`
  - Changes of the interface `UpdateRequestProperty`:
    - Remove the request parameters `bool_false`, `bool_true`
    - Remove the response parameters `bool_false`, `bool_true`
  - Remove the response parameters `bool_false`, `bool_true` from the interface `ListResponseProperties`
  - Remove the request parameters `bool_false`, `bool_true` from the interface `CreateResponseProperty`
  - Remove the response parameters `bool_false`, `bool_true` from the interface `ShowResponseProperty`
  - Changes of the interface `UpdateResponseProperty`:
    - Remove the request parameters `bool_false`, `bool_true`
    - Remove the response parameters `bool_false`, `bool_true`
  - Add the request parameters `cookie_param_name`, `alias_urn`, `cookie_param_name`, `alias_urn`, `cookie_param_name` to the interface `CreateApiV2`
  - Add the response parameters `cookie_param_name`, `alias_urn`, `alias_urn`, `cookie_param_name`, `cookie_param_name` to the interface `ShowDetailsOfApiV2`
  - Changes of the interface `UpdateApiV2`:
    - Add the request parameters `cookie_param_name`, `alias_urn`, `cookie_param_name`, `alias_urn`, `cookie_param_name`
    - Add the response parameters `cookie_param_name`, `alias_urn`, `alias_urn`, `cookie_param_name`, `cookie_param_name`
  - Add the response parameters `cookie_param_name`, `alias_urn`, `alias_urn`, `cookie_param_name`, `cookie_param_name` to the interface `ListApiVersionDetailV2`
  - Add the response parameters `microservice_info`, `type` to the interface `ListVpcChannelsV2`
  - Add the response parameters `microservice_info`, `type` to the interface `ShowDetailsOfVpcChannelV2`
  - Add the response parameters `microservice_info`, `type` to the interface `UpdateVpcChannelV2`
  - Add the response parameters `microservice_info`, `type` to the interface `ListProjectVpcChannelsV2`
  - Add the response parameters `microservice_info`, `type` to the interface `UpdateProjectVpcChannel`
  - Add the response parameter `ingress_ips` to the interface `ShowDetailsOfInstanceV2`

### HuaweiCloud SDK SIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `chinese_8k_general` to the request parameter `property` to the interface `PushTranscriberJobs`
  - Add the enum values `chinese_huaxiaoru_common`, `chinese_huaxiaohan_common`, `chinese_huaxiaoning_common`, `chinese_huaxiaozhen_common`, `english_alvin_common`, `english_amy_common` to the request parameter `property` to the interface `RunTts`

# 3.1.12 2022-11-24

### HuaweiCloud SDK DWR

- _Features_
  - Support the service `Data Warehouse Report`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK AOS

- _Features_
  - Support the interfaces `ListStackEvents`, `ListStackResources`, `DeleteStack`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK APM

- _Features_
  - Support the following interfaces：
    - `ShowBusinessDetail`
    - `ShowSubBusinessDetail`
    - `ListAlarmData`
    - `ListAlarmNotify`
    - `SearchBusinessTopology`
    - `SearchEnvTopology`
    - `SearchTransactionConfig`
    - `ListBusinessEnv`
    - `SearchTransaction`
    - `ShowTransactionDetail`
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `DeleteEnv`
  - Changes of the interface `ListAkSk`:
    - Modify the type `date` -> `string` of the response parameter `gmt_create`
    - Modify the type `date` -> `string` of the response parameter `gmt_modify`
  - The request parameter `monitor_item_id`, `env_id` changed to required of the interface `SaveMonitorItemConfig`
  - The request parameter `x-business-id` changed to not required of the interface `ListEnvMonitorItem`
  - The request parameter `business_id` changed to not required of the interface `ShowTopologyTree`
  - Changes of the interface `ListEnvTags`:
    - The request parameter `business_id` changed to required
    - Modify the type `date` -> `string` of the response parameter `gmt_create`
    - Modify the type `date` -> `string` of the response parameter `gmt_modify`
  - The request parameter `region`, `biz_id` changed to required of the interface `ShowSpanSearch`
  - The request parameter `view_type`, `collector_name`, `metric_set`, `title`, `table_direction`, `group_by`, `filter`, `span`, `span_field`, `page`, `page_size`, `search_word`, `instance_id`, `monitor_item_id`, `env_id`, `start_time`, `end_time` changed to required of the interface `ShowRawTable`
  - The request parameter `env_id`, `clob_id` changed to required of the interface `ShowClobDetail`
  - The request parameter `env_id`, `page`, `page_size` changed to required of the interface `ListEnvInstances`
  - Changes of the interface `ShowAkSks`:
    - Modify the type `date` -> `string` of the response parameter `gmt_create`
    - Modify the type `date` -> `string` of the response parameter `gmt_modify`

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `sub_service_type_code`, `sub_service_type_name`, `sub_resource_type_code`, `sub_resource_type_name`, `sub_resource_id`, `sub_resource_name` to the interface `ListSubCustomerBillDetail`

### HuaweiCloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `children` to the interface `ShowBackup`
  - Add the response parameter `children` to the interface `ListBackups`

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `configurationsOverride` to the interface `CreateCluster`
  - Add the response parameter `configurationsOverride` to the interface `ListClusters`
  - Changes of the interface `UpdateCluster`:
    - Add the request parameters `eniNetwork`, `hostNetwork`
    - Add the response parameter `configurationsOverride`
  - Changes of the interface `DeleteCluster`:
    - Add the request parameter `delete_sfs30`
    - Add the response parameter `configurationsOverride`
  - Add the response parameter `configurationsOverride` to the interface `ShowCluster`
  - Add the request parameter `initializedConditions` to the interface `CreateNode`
  - Add the response parameter `initializedConditions` to the interface `ListNodes`
  - Add the response parameter `initializedConditions` to the interface `UpdateNode`
  - Add the response parameter `initializedConditions` to the interface `DeleteNode`
  - Add the response parameter `initializedConditions` to the interface `ShowNode`
  - Add the request parameter `initializedConditions` to the interface `AddNode`
  - Add the request parameter `initializedConditions` to the interface `ResetNode`
  - Add the request parameters `customSecurityGroups`, `initializedConditions` to the interface `CreateNodePool`
  - Add the response parameters `customSecurityGroups`, `initializedConditions` to the interface `ListNodePools`
  - Changes of the interface `UpdateNodePool`:
    - Add the request parameter `initializedConditions`
    - Add the response parameters `customSecurityGroups`, `initializedConditions`
  - Add the response parameters `customSecurityGroups`, `initializedConditions` to the interface `DeleteNodePool`
  - Add the response parameters `customSecurityGroups`, `initializedConditions` to the interface `ShowNodePool`

### HuaweiCloud SDK CES

- _新增特性_
  - 支持以下接口：
    - `ListAlarmTemplates`
    - `CreateAlarmTemplate`
    - `BatchDeleteAlarmTemplates`
    - `ShowAlarmTemplate`
    - `UpdateAlarmTemplate`
    - `ListAlarmTemplateAssociationAlarms`
    - `ListResourceGroups`
    - `CreateResourceGroup`
    - `ShowResourceGroup`
    - `UpdateResourceGroup`
    - `ListResourceGroupsServicesResources`
    - `BatchDeleteResourceGroups`
    - `BatchCreateResources`
    - `BatchDeleteResources`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSE

- _Features_
  - Support the interfaces `UpgradeEngine`, `RetryEngine`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CSS

- _Features_
  - Support the interfaces `UpdateInstance`, `ChangeMode`, `AddIndependentNode`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `totalSize`, `volume` to the interface `ListClustersDetails`
  - Add the response parameter `volume` to the interface `ShowClusterDetail`
  - The request parameter `endpointWithDnsName` changed to not required of the interface `StartVpecp`

### HuaweiCloud SDK DAS

- _Features_
  - Support the following interfaces：
    - `ShowSqlLimitSwitchStatus`
    - `ChangeSqlLimitSwitchStatus`
    - `ListSqlLimitRules`
    - `CreateSqlLimitRules`
    - `DeleteSqlLimitRules`
    - `ExportTopSqlTemplatesDetails`
    - `ShowSqlLimitJobInfo`
    - `ExportSlowSqlTemplatesDetails`
    - `ExportTopSqlTrendDetails`
- _Bug Fix_
  - None
- _Change_
  - Modify the type `object` -> `array` of the response parameter `quotas` of the interface `ShowQuotas`

### HuaweiCloud SDK DDS

- _Features_
  - Support the following interfaces：
    - `ListAppliedInstances`
    - `ShowConfigurationAppliedHistory`
    - `ShowConfigurationModifyHistory`
    - `CompareConfiguration`
    - `CopyConfiguration`
    - `ResetConfiguration`
    - `ListTasks`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `is_auto_pay` to the interface `AddReadonlyNode`

### HuaweiCloud SDK DNS

- _Features_
  - Support the following interfaces：
    - `SetPrivateZoneProxyPattern`
    - `AssociateHealthCheck`
    - `DisassociateHealthCheck`
    - `CreateRetrieval`
    - `ShowRetrieval`
    - `CreateRetrievalVerification`
    - `ShowRetrievalVerification`
    - `CreateEndpoint`
    - `ShowEndpoint`
    - `ListEndpoints`
    - `UpdateEndpoint`
    - `DeleteEndpoint`
    - `AssociateEndpointIpaddress`
    - `ListEndpointIpaddresses`
    - `DisassociateEndpointIpaddress`
    - `ListEndpointVpcs`
    - `CreateResolveRule`
    - `ShowResoleRule`
    - `ListResoleRules`
    - `UpdateResolveRule`
    - `DeleteResolveRule`
    - `CreateLineGroup`
    - `ListLineGroups`
    - `ShowLineGroup`
    - `UpdateLineGroups`
    - `DeleteLineGroup`
    - `BatchDeleteZones`
    - `BatchDeletePtrRecords`
    - `BatchSetZonesStatus`
    - `BatchSetRecordSetsStatus`
    - `BatchDeleteRecordSets`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the following interfaces：
    - `CreateDependencyVersion`
    - `ListDependencyVersion`
    - `ShowDependencyVersion`
    - `DeleteDependencyVersion`
    - `ListReservedInstanceConfigs`
    - `ListFunctionReservedInstances`
    - `ListFunctionAsMetric`
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `AsyncInvokeReservedFunction`
  - Add the request parameter `custom_image` to the interface `UpdateFunctionConfig`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the following interfaces：
    - `ResizeColdVolume`
    - `CreateColdVolume`
    - `ModifyPublicIp`
    - `SwitchSsl`
    - `SetAutoEnlargePolicy`
    - `RestartInstance`
    - `ShowApplicableInstances`
    - `ShowModifyHistory`
    - `ShowApplyHistory`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `restore_info`, `port` to the interface `CreateInstance`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `test_interval` to the interface `RecognizeHealthCode`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ShowDomainName`, `ShowDnsName`, `ShowReplicationStatus`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ROMA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateDatasourceInfo`:
    - Add the request parameter `ssl`
    - Remove the request parameter `custom_plugin_id`
    - The request parameter `datasource_name`, `datasource_type`, `app_id` changed to required
  - Add the response parameter `ssl` to the interface `ListDatasources`
  - Changes of the interface `UpdateDatasourceInfo`:
    - Add the request parameter `ssl`
    - Add the response parameter `ssl`
    - Remove the request parameter `custom_plugin_id`
    - The request parameter `datasource_name`, `datasource_type`, `app_id` changed to required
  - Add the response parameter `ssl` to the interface `ShowDataourceDetail`
  - Changes of the interface `StartTestDatasource`:
    - Add the request parameter `ssl`
    - Remove the request parameter `custom_plugin_id`
    - The request parameter `datasource_name`, `datasource_type`, `app_id` changed to required
  - Changes of the interface `CreateCommonTask`:
    - Remove the response parameter `created_by`
    - The request parameter `task_name`, `task_type`, `source_datasource_id`, `target_datasource_id`, `task_detail` changed to required
  - Changes of the interface `UpdateTask`:
    - Remove the response parameter `created_by`
    - The request parameter `task_name`, `task_type`, `source_datasource_id`, `target_datasource_id`, `task_detail` changed to required
  - Remove the response parameter `created_by` from the interface `ShowTask`
  - The request parameter `action_id` changed to required of the interface `BatchStartOrStopTasks`
  - The request parameter `task_name`, `operation_types` changed to required of the interface `CreateMultiTasks`
  - The request parameter `operation_types`, `repulling_snapshot` changed to required of the interface `UpdateMultiTasks`
  - The request parameter `source_datasource_id`, `target_datasource_id` changed to required of the interface `CreateMultiTaskMappings`

### HuaweiCloud SDK SA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ImportEvents`:
    - Add the request parameters `dest_ip`, `cve_ids`
    - Remove the request parameter `destc_ip`
    - Modify the type `string` -> `date-time` of the request parameter `first_observed_time`
    - Modify the type `string` -> `date-time` of the request parameter `last_observed_time`
    - Modify the type `string` -> `date-time` of the request parameter `create_time`
    - Modify the type `string` -> `date-time` of the request parameter `arrive_time`
    - Modify the type `string` -> `date-time` of the request parameter `release_time`
    - Modify the type `string` -> `date-time` of the request parameter `start_time`
    - Modify the type `string` -> `date-time` of the request parameter `modified`

### HuaweiCloud SDK WAF

- _Features_
  - Support the interfaces `CreatePrepaidCloudWaf`, `ChangePrepaidCloudWaf`, `ShowSubscriptionInfo`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.11 2022-11-17

### HuaweiCloud SDK AOS

- _Features_
  - Support the `Application Orchestration Service`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DC

- _Features_
  - Support the service `Direct Connect`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CFW

- _Features_
  - Support the service `Cloud Firewall`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK APIG

- _Features_
  - Support the following interfaces：
    - `ListPlugins`
    - `CreatePlugin`
    - `ShowPlugin`
    - `UpdatePlugin`
    - `DeletePlugin`
    - `AttachApiToPlugin`
    - `DetachApiFromPlugin`
    - `ListPluginAttachedApis`
    - `ListPluginAttachableApis`
    - `AttachPluginToApi`
    - `DetachPluginFromApi`
    - `ListApiAttachedPlugins`
    - `ListApiAttachablePlugins`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `type`, `microservice_labels` to the interface `CreateVpcChannelV2`
  - Add the response parameter `microservice_labels` to the interface `ListVpcChannelsV2`
  - Add the response parameter `microservice_labels` to the interface `ShowDetailsOfVpcChannelV2`
  - Changes of the interface `UpdateVpcChannelV2`:
    - Add the request parameters `type`, `microservice_labels`
    - Add the response parameter `microservice_labels`
  - Add the request parameter `microservice_labels` to the interface `CreateMemberGroup`
  - Add the response parameter `microservice_labels` to the interface `ListMemberGroups`
  - Add the response parameter `microservice_labels` to the interface `ShowDetailsOfMemberGroup`
  - Changes of the interface `UpdateMemberGroup`:
    - Add the request parameter `microservice_labels`
    - Add the response parameter `microservice_labels`
  - Add the request parameter `tags` to the interface `CreateInstanceV2`

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `id` changed to required of the interface `DeleteServerNics`

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `sub_customer_association_type` changed to required of the interface `CreateSubEnterpriseAccount`

### HuaweiCloud SDK CloudArtifact

- _Features_
  - Support the interface `ShowProjectReleaseFiles`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudDeploy

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `encrypt` to the request parameter `type` to the interface `CreateDeployTaskByTemplate`
  - Changes of the interface `StartDeployTask`:
    - Add the request parameters `trigger_source`, `key`
    - Remove the request parameters `description`, `name`, `limits`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the following interfaces：
    - `AddExtensionEvaluation`
    - `AddExtensionEvaluationReply`
    - `CheckMaliciousExtensionEvaluation`
    - `DeleteEvaluationReply`
    - `DeleteEvaluation`
    - `AddExtensionStar`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `integer` -> `int32` of the request parameter `new_capacity` of the interface `ResizeInstance`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `gaussdbv5`, `postgresql`, `kafka`, `gaussdbv5ha` to the request parameter `db_type` to the interface `BatchCreateJobs`
  - Add the enum values `gaussdbv5`, `kafka`, `gaussdbv5ha` to the request parameter `db_type` to the interface `BatchValidateConnections`
  - Add the enum values `gaussdbv5`, `postgresql`, `kafka`, `gaussdbv5ha` to the request parameter `db_type` to the interface `BatchUpdateJob`
  - Changes of the interface `ListCompareResult`:
    - Add the response parameters `line_compare_detail`, `content_compare_diff`, `compare_task_list`
    - Remove the response parameters `LineCompareDetail`, `ContentCompareDiff`, `CompareTaskList`
  - Changes of the interface `BatchListJobDetails`:
    - Add the response parameters `is_multi_az`, `az_name`, `master_az`, `slave_az`, `node_role`
    - Add the enum values `gaussdbv5`, `postgresql`, `kafka`, `gaussdbv5ha` to the response parameter `db_type`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `enum` of the request parameter `monitorMetrics` of the interface `RegisterServerMonitor`

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `VPN` to the request parameter `associate_instance_type` to the interface `DisassociatePublicips`
  - Add the enum values `VPN` to the request parameter `associate_instance_type` to the interface `AssociatePublicips`

### HuaweiCloud SDK EPS

- _Features_
  - Support the interface `ListProviders`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the interfaces `ShowInstanceRole`, `SwitchToMaster`, `SwitchToSlave`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `ttl` to the interface `CreateMessage`
  - Add the request parameters `Sp-Auth-Token`, `Stage-Auth-Token` to the interface `ListCertificates`
  - Changes of the interface `AddCertificate`:
    - Add the request parameters `Sp-Auth-Token`, `Stage-Auth-Token`, `addCertificateRequestBody`
    - Remove the request parameter `AddCertificateRequestBody`
  - Add the request parameters `Sp-Auth-Token`, `Stage-Auth-Token` to the interface `DeleteCertificate`
  - Changes of the interface `CheckCertificate`:
    - Add the request parameters `Sp-Auth-Token`, `Stage-Auth-Token`, `checkCertificateRequestBody`
    - Remove the request parameter `CheckCertificateRequestBody`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `new_password` changed to required of the interface `ResetPassword`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeGeneralTable`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeVatInvoice`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeInvoiceVerification`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeGeneralText`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeWebImage`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeHealthCode`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeQuotaInvoice`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeIdCard`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeHandwriting`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeVehicleLicense`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeTransportationLicense`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeTaxiInvoice`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeAutoClassification`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeTollInvoice`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeMvsInvoice`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeLicensePlate`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeFlightItinerary`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeBusinessLicense`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeDriverLicense`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeBusinessCard`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeTrainTicket`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeVin`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizePassport`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeBankcard`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeInsurancePolicy`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeFinancialStatement`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeQualificationCertificate`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeThailandIdcard`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeMyanmarIdcard`
  - Changes of the interface `RecognizeMyanmarDriverLicense`:
    - Add the request parameter `Enterprise-Project-Id`
    - Add the response parameters `birth`, `birth`
    - Remove the response parameters `Birth`, `Birth`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeChileIdCard`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeThailandLicensePlate`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeWaybillElectronic`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizePcrTestRecord`
  - Changes of the interface `RecognizeIdDocument`:
    - Add the request parameter `Enterprise-Project-Id`
    - Modify the type `object` -> `object` of the response parameter `result`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeHkIdCard`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeCambodianIdCard`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeExitEntryPermit`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeMainlandTravelPermit`
  - Add the request parameter `Enterprise-Project-Id` to the interface `RecognizeMacaoIdCard`

### HuaweiCloud SDK OSM

- _Features_
  - Support the interface `RevokeMessage`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ROMA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `app_name` from the interface `CreateDeviceGroup`
  - Remove the response parameters `total`, `app_id`, `permissions` from the interface `ShowDeviceGroupTree`
  - Remove the response parameter `app_name` from the interface `UpdateDeviceGroup`
  - Add the request parameter `user_name` to the interface `CreateDevice`
  - Changes of the interface `ListDevices`:
    - Add the response parameter `device_id`
    - Remove the response parameter `plugin_id`
  - Add the response parameters `device_id`, `device_id` to the interface `BatchFreezeDevices`
  - Changes of the interface `UpdateDevice`:
    - Add the response parameter `device_id`
    - Remove the response parameter `plugin_id`
  - Changes of the interface `ShowDevice`:
    - Add the response parameter `device_id`
    - Modify the type `enum` -> `integer` of the response parameter `status`
    - Modify the type `enum` -> `integer` of the response parameter `online_status`
    - Modify the type `enum` -> `integer` of the response parameter `device_type`
    - Modify the type `enum` -> `integer` of the response parameter `plugin_id`
  - Changes of the interface `ListSubsets`:
    - Add the response parameter `device_id`
    - Remove the response parameter `plugin_id`
  - Add the request parameter `ResetAuthenticationRequestBody` to the interface `ResetAuthentication`
  - Changes of the interface `UpdateProduct`:
    - Add the response parameter `status`
    - Remove the response parameter `authentication`
  - Add the request parameter `ResetProductAuthenticationRequestBody` to the interface `ResetProductAuthentication`
  - Remove the response parameters `app_name`, `sql_field`, `sql_where`, `rule_express` from the interface `CreateRule`
  - Add the request parameters `enum_dict`, `method` to the interface `CreateProperty`
  - Changes of the interface `ListProperties`:
    - Add the response parameter `enum_dict`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Changes of the interface `UpdateProperty`:
    - Add the request parameter `enum_dict`
    - Add the response parameters `enum_dict`, `method`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Changes of the interface `ShowProperty`:
    - Add the response parameters `enum_dict`, `method`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Changes of the interface `CreateRequestProperty`:
    - Add the request parameters `enum_dict`, `method`
    - Add the response parameter `enum_dict`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Changes of the interface `ListRequestProperties`:
    - Add the response parameter `enum_dict`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Changes of the interface `UpdateRequestProperty`:
    - Add the request parameter `enum_dict`
    - Add the response parameter `enum_dict`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Changes of the interface `ShowRequestProperty`:
    - Add the response parameter `enum_dict`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Add the request parameters `enum_dict`, `method` to the interface `CreateResponseProperty`
  - Changes of the interface `ListResponseProperties`:
    - Add the response parameter `enum_dict`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Changes of the interface `UpdateResponseProperty`:
    - Add the request parameter `enum_dict`
    - Add the response parameter `enum_dict`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`
  - Changes of the interface `ShowResponseProperty`:
    - Add the response parameter `enum_dict`
    - Add the enum values `boolean`, `array` to the response parameter `data_type`

### HuaweiCloud SDK TMS

- _Features_
  - Support the interface `ListProviders`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK UGO

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `RunSqlConversion`:
    - Add the enum values `GaussDB Centralized`, Remove the enum values `GaussDB(for openGauss)` from the request parameter `target_db_type`
    - Add the enum values `2.0`, Remove the enum values `2020` from the request parameter `target_db_version`
  - Changes of the interface `ConfirmTargetDbType`:
    - Modify the type `string` -> `enum` of the request parameter `target_db_type`
    - Modify the type `string` -> `enum` of the request parameter `target_db_version`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateSubnet`:
    - Add the enum values `addresstime` to the request parameter `opt_name`
    - Add the enum values `addresstime` to the response parameter `opt_name`
  - Add the enum values `addresstime` to the response parameter `opt_name` to the interface `ListSubnets`
  - Add the enum values `addresstime` to the response parameter `opt_name` to the interface `ShowSubnet`
  - Add the enum values `addresstime` to the request parameter `opt_name` to the interface `UpdateSubnet`

# 3.1.10 2022-11-14

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `job_id` changed to required of the interface `DeleteServerNics`
  - Changes of the interface `UpdateBaremetalServerInterfaceAttachments`:
    - Modify the type `string` -> `boolean` of the request parameter `delete_on_termination`
    - The request parameter `delete_on_termination` changed to required
  - Add the response parameter `remote_console` to the interface `ShowServerRemoteConsole`

### HuaweiCloud SDK CPH

- _Features_
  - Support the interface `DeleteShareFiles`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `StopCloudPhone`:
    - Add the request parameter `StopCloudPhoneRequestBody`
    - Remove the request parameter `StopCloudPhoneReuqestBody`
  - Changes of the interface `ShowCloudPhoneServerDetail`:
    - Add the response parameters `server_name`, `availability_zone`, `server_id`, `server_model_name`, `phone_model_name`, `keypair_name`, `status`, `vpc_id`, `cidr`, `vpc_cidr`, `subnet_id`, `subnet_cidr`, `resource_project_id`, `metadata`, `addresses`, `network_version`, `create_time`, `update_time`
    - Remove the response parameter `servers`
  - Remove the request parameter `br_cidr` from the interface `CreateNet2CloudPhoneServer`

### HuaweiCloud SDK CSMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `sys_tags` to the interface `ListSecretTags`

### HuaweiCloud SDK DDS

- _Features_
  - Support the following interfaces：
    - `ShowSlowlogDesensitizationSwitch`
    - `ListRecycleInstances`
    - `CheckWeakPassword`
    - `ShowUpgradeDuration`
    - `ShowDiskUsage`
    - `ListSslCertDownloadAddress`
    - `DeleteAuditLog`
    - `ShowRecyclePolicy`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `X-Language` to the interface `SwitchSlowlogDesensitization`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the interface `ShowWorkflowExecutionForPage`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `enable_stream_response` to the interface `ListWorkflow`
  - Add the response parameter `enable_stream_response` to the interface `UpdateWorkFlow`

### HuaweiCloud SDK GSL

- _Features_
  - Support the interfaces `ListBackPools`, `ListBackPoolMembers`
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
  - Remove the request parameter `specify_project` from the interface `ListStreamForbidden`
  - Remove the request parameter `specify_project` from the interface `DeleteStreamForbidden`
  - Remove the request parameter `specify_project` from the interface `UpdateStreamForbidden`
  - Remove the request parameter `specify_project` from the interface `CreateStreamForbidden`
  - Remove the enum values `global` from the response parameter `service_area` from the interface `ShowDomain`
  - Remove the enum values `global` from the response parameter `service_area` from the interface `UpdateDomain`
  - Remove the enum values `global` from the request parameter `service_area` from the interface `CreateDomain`
  - Remove the request parameter `specify_project` from the interface `DeleteDomainMapping`
  - Remove the request parameter `specify_project` from the interface `CreateDomainMapping`

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `resource_id` to the interface `ListHosts`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ShowPostgresqlParamValue`, `UpdatePostgresqlParameterValue`, `ListDrRelations`
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `ESSD` to the request parameter `type` to the interface `CreateInstance`
  - Add the enum values `ESSD` to the response parameter `type` to the interface `ListInstances`
  - Add the enum values `ESSD` to the request parameter `type` to the interface `CreateRestoreInstance`
  - Add the request parameter `is_revoke_public_privilege` to the interface `CreatePostgresqlDatabase`

### HuaweiCloud SDK VPCEP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `array` of the response parameter `Action` of the interface `ListEndpoints`
  - Modify the type `string` -> `array` of the response parameter `Action` of the interface `DeleteEndpointPolicy`
  - Changes of the interface `UpdateEndpointPolicy`:
    - Modify the type `string` -> `array` of the request parameter `Action`
    - Modify the type `string` -> `array` of the response parameter `Action`

### HuaweiCloud SDK WAF

- _Features_
  - Support the interfaces `MigrateCompositeHosts`, `ShowSourceIp`, `ListNoticeConfigs`, `UpdateAlertNoticeConfig`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `instance_name` to the interface `ListInstance`
  - Add the response parameters `enabled`, `ltsAttackStreamID` to the interface `ShowLtsInfoConfig`
  - Changes of the interface `UpdateLtsInfoConfig`:
    - Add the request parameters `enabled`, `ltsAttackStreamID`
    - Add the response parameters `enabled`, `ltsAttackStreamID`
    - The request parameter `enabale` changed to not required
  - Add the response parameter `description` to the interface `ShowIpGroup`

# 3.1.9 2022-11-08

### HuaweiCloud SDK HSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListQuotasDetail`:
    - Add the response parameter `on_demand_num`
    - Remove the response parameter `on_demand_numn`

### HuaweiCloud SDK Meeting

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn` to the interface `SearchMeetings`
  - Changes of the interface `CreateMeeting`:
    - Add the request parameters `isHostCameraOn`, `isGuestCameraOn`
    - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn`
  - Changes of the interface `UpdateMeeting`:
    - Add the request parameters `isHostCameraOn`, `isGuestCameraOn`
    - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn`
  - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn` to the interface `ShowMeetingDetail`
  - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn` to the interface `SearchOnlineMeetings`
  - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn` to the interface `ShowOnlineMeetingDetail`
  - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn` to the interface `SearchHisMeetings`
  - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn` to the interface `ShowHisMeetingDetail`
  - Changes of the interface `CreateRecurringMeeting`:
    - Add the request parameters `isHostCameraOn`, `isGuestCameraOn`
    - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn`
  - Changes of the interface `UpdateRecurringMeeting`:
    - Add the request parameters `isHostCameraOn`, `isGuestCameraOn`
    - Add the response parameters `onlineAttendeeAmount`, `isHostCameraOn`, `isGuestCameraOn`

# 3.1.8 2022-11-03

### HuaweiCloud SDK DevSecurity

- _Features_
  - Support the service `DevSecurity`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GA

- _Features_
  - Support the service `Global accelerator`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudDeploy

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `id`, `release_id`, `duration`, `execution_state`, `executor_id`, `executor_nick_name`, `steps` to the interface `ListDeployTasks`
  - Add the response parameters `update_time`, `lastest_connection_time`, `connection_status`, `owner_name`, `updator_id`, `create_time`, `nick_name`, `owner_id`, `updator_name`, `connection_result` to the interface `ListHosts`
  - Changes of the interface `ListHostGroups`:
    - Add the response parameter `updated_by`
    - Remove the response parameter `update_by`
  - Changes of the interface `ShowDeploymentGroupDetail`:
    - Add the response parameter `updated_by`
    - Remove the response parameter `update_by`
  - Add the response parameters `update_time`, `lastest_connection_time`, `connection_status`, `owner_name`, `updator_id`, `create_time`, `nick_name`, `owner_id`, `updator_name`, `connection_result` to the interface `ShowDeploymentHostDetail`
  - Add the response parameters `id`, `release_id`, `duration`, `execution_state`, `executor_id`, `executor_nick_name`, `steps` to the interface `ShowDeployTaskDetail`
  - Add the response parameter `type` to the interface `ListDeployTaskHistoryByDate`
  - Changes of the interface `ShowProjectSuccessRate`:
    - Add the response parameters `start_date`, `end_date`
    - Remove the response parameters `start_time`, `end_time`
  - Changes of the interface `ListTaskSuccessRate`:
    - Add the response parameters `start_date`, `end_date`
    - Remove the response parameters `start_time`, `end_time`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListClustersDetails`:
    - Add the response parameter `failedReason`
    - Remove the response parameter `failed_reasons`
  - Changes of the interface `ShowClusterDetail`:
    - Add the response parameter `failedReason`
    - Remove the response parameter `failed_reasons`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `true`, `false`
  - Add the enum values `true`, `false`
  - Add the enum values `up`, `down`, `non-dbs`
  - Add the enum values `success`, `failed`
  - Changes of the interface `ListCompareResult`:
    - Add the enum values `DB`, `TABLE`, `VIEW`, `EVENT`, `ROUTINE`, `INDEX`, `TRIGGER`, `SYNONYM`, `FUNCTION`, `PROCEDURE`, `TYPE`, `RULE`, `DEFAULT_TYPE`, `PLAN_GUIDE`, `CONSTRAINT`, `FILE_GROUP`, `PARTITION_FUNCTION`, `PARTITION_SCHEME`, `TABLE_COLLATION`
    - Add the enum values `CONSISTENT`, `INCONSISTENT`, `COMPARING`, `WAITING_FOR_COMPARISON`, `FAILED_TO_COMPARE`, `TARGET_DB_NOT_EXIT`, `CAN_NOT_COMPARE`
    - Add the enum values `CONSISTENT`, `INCONSISTENT`, `COMPARING`, `WAITING_FOR_COMPARISON`, `FAILED_TO_COMPARE`, `TARGET_DB_NOT_EXIT`, `CAN_NOT_COMPARE`
    - Add the enum values `CONSISTENT`, `INCONSISTENT`, `COMPARING`, `WAITING_FOR_COMPARISON`, `FAILED_TO_COMPARE`, `TARGET_DB_NOT_EXIT`, `CAN_NOT_COMPARE`
    - Add the enum values `RUNNING`, `WAITING_FOR_RUNNING`, `SUCCESSFUL`, `FAILED`, `CANCELLED`, `TIMEOUT_INTERRUPT`, `FULL_DOING`, `INCRE_DOING`
  - Add the enum values `FULL_TRANS`, `FULL_INCR_TRANS`, `INCR_TRANS`
  - Add the enum values `CREATING`, `CREATE_FAILED`, `CONFIGURATION`, `STARTJOBING`, `WAITING_FOR_START`, `START_JOB_FAILED`, `PAUSING`, `FULL_TRANSFER_STARTED`, `FULL_TRANSFER_FAILED`, `FULL_TRANSFER_COMPLETE`, `INCRE_TRANSFER_STARTED`, `INCRE_TRANSFER_FAILED`, `RELEASE_RESOURCE_STARTED`, `RELEASE_RESOURCE_FAILED`, `RELEASE_RESOURCE_COMPLETE`, `REBUILD_NODE_STARTED`, `REBUILD_NODE_FAILED`, `CHANGE_JOB_STARTED`, `CHANGE_JOB_FAILED`, `DELETED`, `CHILD_TRANSFER_STARTING`, `CHILD_TRANSFER_STARTED`, `CHILD_TRANSFER_COMPLETE`, `CHILD_TRANSFER_FAILED`, `RELEASE_CHILD_TRANSFER_STARTED`, `RELEASE_CHILD_TRANSFER_COMPLETE`, `NODE_UPGRADE_START`, `NODE_UPGRADE_COMPLETE`, `NODE_UPGRADE_FAILED`
  - Changes of the interface `ShowJobList`:
    - Add the enum values `PAUSING`, `REBUILD_NODE_STARTED`, `REBUILD_NODE_FAILED`, `DELETED`, `NODE_UPGRADE_START`, `NODE_UPGRADE_COMPLETE`, `NODE_UPGRADE_FAILED` to the request parameter `status`
    - Add the enum values `CREATING`, `CREATE_FAILED`, `CONFIGURATION`, `STARTJOBING`, `WAITING_FOR_START`, `START_JOB_FAILED`, `PAUSING`, `FULL_TRANSFER_STARTED`, `FULL_TRANSFER_FAILED`, `FULL_TRANSFER_COMPLETE`, `INCRE_TRANSFER_STARTED`, `INCRE_TRANSFER_FAILED`, `RELEASE_RESOURCE_STARTED`, `RELEASE_RESOURCE_FAILED`, `RELEASE_RESOURCE_COMPLETE`, `REBUILD_NODE_STARTED`, `REBUILD_NODE_FAILED`, `CHANGE_JOB_STARTED`, `CHANGE_JOB_FAILED`, `DELETED`, `CHILD_TRANSFER_STARTING`, `CHILD_TRANSFER_STARTED`, `CHILD_TRANSFER_COMPLETE`, `CHILD_TRANSFER_FAILED`, `RELEASE_CHILD_TRANSFER_STARTED`, `RELEASE_CHILD_TRANSFER_COMPLETE`, `NODE_UPGRADE_START`, `NODE_UPGRADE_COMPLETE`, `NODE_UPGRADE_FAILED`
    - Add the enum values `migration`, `sync`, `cloudDataGuard`
    - Add the enum values `FULL_TRANS`, `FULL_INCR_TRANS`, `INCR_TRANS`
    - Modify the type `string` -> `enum` of the response parameter `status`
  - Add the enum values `CREATING`, `CREATE_FAILED`, `CONFIGURATION`, `STARTJOBING`, `WAITING_FOR_START`, `START_JOB_FAILED`, `PAUSING`, `FULL_TRANSFER_STARTED`, `FULL_TRANSFER_FAILED`, `FULL_TRANSFER_COMPLETE`, `INCRE_TRANSFER_STARTED`, `INCRE_TRANSFER_FAILED`, `RELEASE_RESOURCE_STARTED`, `RELEASE_RESOURCE_FAILED`, `RELEASE_RESOURCE_COMPLETE`, `REBUILD_NODE_STARTED`, `REBUILD_NODE_FAILED`, `CHANGE_JOB_STARTED`, `CHANGE_JOB_FAILED`, `DELETED`, `CHILD_TRANSFER_STARTING`, `CHILD_TRANSFER_STARTED`, `CHILD_TRANSFER_COMPLETE`, `CHILD_TRANSFER_FAILED`, `RELEASE_CHILD_TRANSFER_STARTED`, `RELEASE_CHILD_TRANSFER_COMPLETE`, `NODE_UPGRADE_START`, `NODE_UPGRADE_COMPLETE`, `NODE_UPGRADE_FAILED`
  - Changes of the interface `BatchSwitchover`:
    - Add the enum values `Sharding`, `ReplicaSet`, `ReplicaSingle`
    - Add the enum values `Single`, `Ha`, `GR`, `Sharding`, `Sharding4.0+`, `ReplicaSet`, `Replica`, `ReplicaSingle`, `Cluster`, `Independent`, `Combined`, `Distributed`, `NoSharding`
    - Add the enum values `up`, `down`, `non-dbs`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `destination_type` changed to not required of the interface `NovaCreateServers`

### HuaweiCloud SDK EPS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `region_id` to the interface `MigrateResource`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ShowGaussMySqlProxy`
  - Add the request parameter `lower_case_table_names` to the interface `CreateGaussMySqlInstance`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `RecognizeGeneralText`:
    - Add the request parameter `character_mode`
    - Add the response parameters `confidence`, `char_list`
  - Changes of the interface `RecognizeThailandIdcard`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`

### HuaweiCloud SDK WAF

- _Features_
  - Support the following interfaces：
    - `ListInstance`
    - `CreateInstance`
    - `ShowInstance`
    - `RenameInstance`
    - `DeleteInstance`
    - `ShowLtsInfoConfig`
    - `UpdateLtsInfoConfig`
    - `ListIpGroup`
    - `CreateIpGroup`
    - `ShowIpGroup`
    - `UpdateIpGroup`
    - `DeleteIpGroup`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.7 2022-11-02

### HuaweiCloud SDK APIG

- _Features_
  - Support the following interfaces：
    - `UpdateHealthCheck`
    - `BatchEnableMembers`
    - `BatchDisableMembers`
    - `ListMemberGroups`
    - `CreateMemberGroup`
    - `ShowDetailsOfMemberGroup`
    - `UpdateMemberGroup`
    - `DeleteMemberGroup`
    - `ListMetricData`
    - `ImportMicroservice`
    - `ListCertificatesV2`
    - `CreateCertificateV2`
    - `BatchAssociateCertsV2`
    - `BatchDisassociateCertsV2`
    - `ShowDetailsOfCertificateV2`
    - `UpdateCertificateV2`
    - `DeleteCertificateV2`
    - `BatchAssociateDomainsV2`
    - `BatchDisassociateDomainsV2`
    - `ListAttachedDomainsV2`
    - `UpdateBackendInstancesV2`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateAclStrategyV2`:
    - Modify the type `string` -> `enum` of the request parameter `acl_type`
    - Modify the type `string` -> `enum` of the request parameter `entity_type`
  - Changes of the interface `UpdateAclStrategyV2`:
    - Modify the type `string` -> `enum` of the request parameter `acl_type`
    - Modify the type `string` -> `enum` of the request parameter `entity_type`
  - Add the enum values `DOMAIN_ID` to the response parameter `entity_type` to the interface `ListAclPolicyBindedToApiV2`
  - Changes of the interface `CreateVpcChannelV2`:
    - Add the request parameters `member_groups`, `microservice_info`, `dict_code`
    - The request parameter `port`, `balance_strategy`, `member_type` changed to required
  - Changes of the interface `ListVpcChannelsV2`:
    - Add the request parameters `dict_code`, `member_host`, `member_port`, `member_group_name`, `member_group_id`
    - Add the response parameters `microservice_info`, `type`, `dict_code`, `microservice_version`, `microservice_port`
    - The response parameter `port`, `balance_strategy`, `member_type` changed to required
  - Changes of the interface `ShowDetailsOfVpcChannelV2`:
    - Add the response parameters `microservice_info`, `type`, `dict_code`, `microservice_version`, `microservice_port`
    - The response parameter `port`, `balance_strategy`, `member_type` changed to required
  - Changes of the interface `UpdateVpcChannelV2`:
    - Add the request parameters `member_groups`, `microservice_info`, `dict_code`
    - Add the response parameters `microservice_info`, `type`, `dict_code`, `microservice_version`, `microservice_port`
    - The request parameter `port`, `balance_strategy`, `member_type` changed to required
    - The response parameter `port`, `balance_strategy`, `member_type` changed to required
  - Add the request parameters `member_group_name`, `member_group_id`, `precise_search` to the interface `ListBackendInstancesV2`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowUrlTaskInfo`:
    - Modify the type `int32` -> `int64` of the response parameter `modify_time`
    - Modify the type `int32` -> `int64` of the response parameter `create_time`

### HuaweiCloud SDK ECS

- _Features_
  - Support the interfaces `UpdateServerBlockDevice`, `RegisterServerMonitor`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interface `UpdateTransactionSplitStatus`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `transaction_split` to the interface `ShowGaussMySqlProxy`
  - Add the response parameter `transaction_split` to the interface `ShowGaussMySqlProxyList`

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateScalingPolicy`:
    - Add the request parameter `autoScalingPolicyReqV11`
    - Remove the request parameter `auto_scaling_policy_req_V11`
  - Changes of the interface `CreateCluster`:
    - Add the request parameter `createClusterReqV11`
    - Remove the request parameter `cluster_req`
  - Remove the response parameters `name`, `uri`, `parameters`, `nodes`, `active_master`, `fail_action`, `before_component_start`, `start_time`, `state` from the interface `ListClusters`
  - Changes of the interface `UpdateClusterScaling`:
    - Add the request parameter `clusterScalingReq`
    - Remove the request parameter `cluster_scaling_req`
  - Remove the response parameters `name`, `uri`, `parameters`, `nodes`, `active_master`, `fail_action`, `before_component_start`, `start_time`, `state` from the interface `ShowClusterDetails`
  - Changes of the interface `CreateClusterTag`:
    - Add the request parameter `createTagReq`
    - Remove the request parameter `CreateTagRequest`
  - Changes of the interface `BatchCreateClusterTags`:
    - Add the request parameter `batchCreateClusterTagsReq`
    - Remove the request parameter `BatchCreateClusterTagsRequest`
  - Remove the request parameters `key`, `value` from the interface `BatchDeleteClusterTags`
  - Changes of the interface `ListClustersByTags`:
    - Add the request parameter `listResourceReq`
    - Remove the request parameter `ListResourceRequest`
    - Remove the request parameters `key`, `value`, `auto_scaling_enable`, `min_capacity`, `max_capacity`, `resources_plans`, `rules`, `exec_scripts`, `name`, `uri`, `parameters`, `nodes`, `active_master`, `fail_action`, `before_component_start`, `action_stages`, `job_type`, `job_name`, `jar_path`, `arguments`, `input`, `output`, `job_log`, `hive_script_path`, `hql`, `shutdown_cluster`, `submit_job_once_cluster_run`, `file_action` from the interface `CreateCluster`
  - Changes of the interface `CreateExecuteJob`:
    - Add the request parameter `jobExecution`
    - Remove the request parameter `job_execution_dto`
    - Remove the response parameter `job_submit_result`
  - Changes of the interface `BatchDeleteJobs`:
    - Add the request parameter `jobBatchDelete`
    - Remove the request parameter `job_batch_delete`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListPostgresqlExtension`, `CreatePostgresqlExtension`, `DeletePostgresqlExtension`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `sichuan_8k_common` to the request parameter `property` to the interface `PushTranscriberJobs`
  - Add the enum values `chinese_huaxiaolong_common`, `chinese_huaxiaorui_common` to the request parameter `property` to the interface `RunTts`

# 3.1.6 2022-10-27

### HuaweiCloud SDK BMS

- _Features_
  - Support the interfaces `DeleteServerNics`, `UpdateBaremetalServerInterfaceAttachments`, `AddServerNics`, `ShowServerRemoteConsole`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `int32` -> `int64` of the response parameter `id` of the interface `ShowUrlTaskInfo`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interfaces `ListExtensions`, `ShowExtensionDetail`, `ShowExtensionEvaluation`, `ShowExtensionEvaluationStar`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CodeHub

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListMergeRequest`:
    - Add the response parameter `merge_requests`
    - Remove the response parameter `mergeRequests`
  - Changes of the interface `ShowMergeRequest`:
    - Add the response parameters `approval_merge_request_approvers`, `closed_at`, `created_at`, `devcloud_source_branch`, `is_source_branch_exist`, `merge_request_assignee_list`, `merge_request_diff`, `merge_status`, `source_branch`, `target_branch`, `updated_at`
    - Remove the response parameters `approvalMergeRequestApprovers`, `closedAt`, `createdAt`, `devcloudSourceBranch`, `isSourceBranchExist`, `mergeRequestAssigneeList`, `mergeRequestDiff`, `mergeStatus`, `sourceBranch`, `targetBranch`, `updatedAt`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowInstance`:
    - Modify the type `string` -> `int64` of the response parameter `begin_time`
    - Modify the type `string` -> `int64` of the response parameter `end_time`
    - Modify the type `string` -> `int64` of the response parameter `current_time`
    - Modify the type `string` -> `int64` of the response parameter `next_expand_time`
    - Modify the type `string` -> `int64` of the response parameter `expand_effect_time`
    - Modify the type `string` -> `int64` of the response parameter `expand_interval_time`
  - Modify the type `int32` -> `integer` of the request parameter `new_capacity` of the interface `ResizeInstance`
  - Add the response parameters `target_instance_address`, `migration_method`, `task_name`, `target_instance_id`, `source_instance_name`, `target_instance_name`, `migrate_type`, `created_at`, `source_instance_id`, `task_id`, `data_source`, `status` to the interface `ListMigrationTask`
  - Changes of the interface `ListRedislog`:
    - Add the response parameter `backup_id`
    - Remove the response parameter `backupId`
  - Add the response parameter `enable_show` to the interface `ListBackgroundTask`

### HuaweiCloud SDK DDS

- _Features_
  - Support the following interfaces：
    - `AddReadonlyNode`
    - `UpgradeDatabaseVersion`
    - `ShowSecondLevelMonitoringStatus`
    - `SwitchSecondLevelMonitoring`
    - `ChangeOpsWindow`
    - `SetRecyclePolicy`
    - `ExpandReplicasetNode`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `node_type` to the interface `ListConfigurations`
  - Add the response parameter `patch_available` to the interface `ListInstances`
  - Add the request parameter `node_ids` to the interface `ResizeInstanceVolume`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `X-Client-Token`, `batch_create_in_multi_az` to the interface `CreateServers`
  - Add the request parameter `X-Client-Token` to the interface `CreatePostPaidServers`

### HuaweiCloud SDK ELB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `tls-1-1`, `tls-1-2`, `tls-1-2-strict`, Remove the enum values ` tls-1-1`, ` tls-1-2`, ` tls-1-2-strict` from the request parameter `tls_ciphers_policy` to the interface `CreateListener`
  - Remove the request parameter `cascade` from the interface `DeleteListener`
  - Remove the request parameter `cascade` from the interface `DeleteLoadbalancer`
  - Changes of the interface `ListApiVersions`:
    - Add the response parameter `versions`
    - Remove the response parameters `id`, `status`
  - Remove the request parameter `global_eip_ids` from the interface `CreateLoadBalancer`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the interfaces `ShowRestorableList`, `ListRestoreTime`, `DeleteBackup`, `RestoreExistingInstance`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK HSS

- _Features_
  - Support the following interfaces：
    - `ListUsers`
    - `ListUserChangeHistories`
    - `ShowResourceQuotas`
    - `ListQuotasDetail`
    - `SwitchHostsProtectStatus`
    - `BatchCreateTags`
    - `DeleteResourceInstanceTag`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListRiskConfigs`:
    - Add the request parameter `check_name`
    - Remove the request parameter `check_type`
  - Changes of the interface `ShowCheckRuleDetail`:
    - Add the request parameter `check_name`
    - Remove the request parameter `check_type`
  - Changes of the interface `ListHostStatus`:
    - Add the request parameter `server_group`
    - The request parameter `region` changed to not required
  - Changes of the interface `ListVulnerabilities`:
    - Add the response parameter `severity_level`
    - Modify the type `int32` -> `string` of the response parameter `repair_necessity`

### HuaweiCloud SDK IEF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ShowEdgeNodeUpgradeDetails`
  - Add the request parameter `ief-instance-id` to the interface `UpdateNodeByDeviceId`
  - Remove the response parameters `affinity`, `updated_at` from the interface `ListPods`
  - Remove the response parameter `encrypt_data` from the interface `CreateEncryptdatas`
  - Changes of the interface `ListEncryptdatas`:
    - Add the response parameter `encrypt_datas`
    - Remove the response parameter `encrypt_data`
  - Remove the response parameter `encrypt_data` from the interface `UpdateEncryptdatas`
  - Changes of the interface `ListNodeEncryptdatas`:
    - Add the response parameter `encrypt_datas`
    - Remove the response parameter `encrypt_data`

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `market` to the request parameter `__imagetype` to the interface `ListTags`
  - Changes of the interface `GlanceListImages`:
    - Add the enum values `market` to the request parameter `__imagetype`
    - Add the enum values `market` to the response parameter `__imagetype`
  - Add the enum values `market` to the response parameter `__imagetype` to the interface `GlanceShowImage`
  - Add the enum values `market` to the response parameter `__imagetype` to the interface `GlanceUpdateImage`

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `properties` to the interface `CreateMessage`
  - Add the response parameter `properties` to the interface `ListDeviceMessages`
  - Add the response parameter `properties` to the interface `ShowDeviceMessage`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreatePostPaidInstance`:
    - Add the request parameters `disk_encrypted_enable`, `disk_encrypted_key`
    - Add the enum values `2.7` to the request parameter `engine_version`

### HuaweiCloud SDK Meeting

- _Features_
  - Support the following interfaces：
    - `SearchCorpExternalDir`
    - `SetCohost`
    - `BatchHand`
    - `CancelBroadcast`
    - `AllowWaitingParticipant`
    - `MoveToWaitingRoom`
    - `AllowClientRecord`
    - `ShowLayout`
    - `SaveLayout`
    - `DeleteLayout`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Moderation

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `float` -> `integer` of the request parameter `frame_interval` of the interface `RunCreateVideoModerationJob`
  - Modify the type `float` -> `integer` of the response parameters `start_time`, `end_time` of the interface `RunQueryAudioModerationJob`
  - Changes of the interface `RunQueryVideoModerationJob`:
    - Modify the type `integer` -> `float` of the response parameter `time`
    - Modify the type `integer` -> `float` of the response parameters `start_time`, `end_time`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `read_only_by_user` to the interface `ListInstances`
  - Add the request parameters `hosts`, `databases` to the interface `CreateDbUser`

### HuaweiCloud SDK SCM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `enterprise_project_id` changed to required of the interface `ListCertificates`
  - Add the response parameter `fingerprint` to the interface `ShowCertificate`

### HuaweiCloud SDK SFSTurbo

- _Features_
  - Support the interface `ChangeShareName`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.5 2022-09-28

### HuaweiCloud SDK APM

- _Features_
  - Support the interfaces `DeleteEnv`, `DeleteApp`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `sk` to the interface `CreateAkSk`
  - Add the response parameter `sk` to the interface `DeleteAkSk`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `domain_id` to the interface `ListDomains`
  - Changes of the interface `CreateDomain`:
    - Add the request parameter `domain_id`
    - Add the response parameter `domain_id`
  - Add the response parameter `domain_id` to the interface `ShowDomainDetail`
  - Add the response parameter `domain_id` to the interface `DeleteDomain`
  - Add the response parameter `domain_id` to the interface `EnableDomain`
  - Add the response parameter `domain_id` to the interface `DisableDomain`
  - Changes of the interface `UpdateDomainOrigin`:
    - Add the request parameter `domain_id`
    - Add the response parameter `domain_id`
  - Add the response parameters `origin_range_status`, `user_agent_filter`, `origin_request_url_rewrite`, `error_code_redirect_rules` to the interface `ShowDomainFullConfig`
  - Add the request parameters `origin_range_status`, `user_agent_filter`, `origin_request_url_rewrite`, `error_code_redirect_rules` to the interface `UpdateDomainFullConfig`

### HuaweiCloud SDK CloudRTC

- _Features_
  - Support the interfaces `RemoveUsers`, `RemoveRoom`, `UpdateIndividualStreamJob`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `variable_mode`, `share_mode` to the interface `ListVariables`
  - Changes of the interface `UpdateTask`:
    - Add the request parameters `name`, `conditions`, `is_disabled`
    - Add the response parameter `taskInfo`
    - Remove the request parameter `case_name`
    - Remove the response parameter `taskinfo`
    - Modify the type `string` -> `object` of the request parameter `check_end_length`
    - Modify the type `string` -> `object` of the request parameter `check_end_str`
    - Modify the type `string` -> `object` of the request parameter `check_end_type`
  - Changes of the interface `ShowTask`:
    - Add the response parameter `taskInfo`
    - Remove the response parameter `taskinfo`
  - Add the response parameters `respTimeRange`, `progressState`, `createBy`, `statusValue` to the interface `ShowReport`
  - Add the request parameters `case_id`, `name`, `case_type`, `increase_setting`, `stages`, `status`, `temp_id`, `sort` to the interface `UpdateCase`
  - Changes of the interface `UpdateTemp`:
    - Modify the type `string` -> `object` of the request parameter `check_end_length`
    - Modify the type `string` -> `object` of the request parameter `check_end_str`
    - Modify the type `string` -> `object` of the request parameter `check_end_type`
  - Changes of the interface `UpdateTaskRelatedTestCase`:
    - Add the response parameter `taskInfo`
    - Remove the response parameter `taskinfo`
  - Add the response parameters `end_time`, `parallel` to the interface `ShowHistoryRunInfo`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowInstance`:
    - Modify the type `string` -> `int64` of the response parameter `begin_time`
    - Modify the type `string` -> `int64` of the response parameter `end_time`
    - Modify the type `string` -> `int64` of the response parameter `current_time`
    - Modify the type `string` -> `int64` of the response parameter `next_expand_time`
    - Modify the type `string` -> `int64` of the response parameter `expand_effect_time`
    - Modify the type `string` -> `int64` of the response parameter `expand_interval_time`
  - Modify the type `int32` -> `integer` of the request parameter `new_capacity` of the interface `ResizeInstance`
  - Add the response parameters `target_instance_address`, `migration_method`, `task_name`, `target_instance_id`, `source_instance_name`, `target_instance_name`, `migrate_type`, `created_at`, `source_instance_id`, `task_id`, `data_source`, `status` to the interface `ListMigrationTask`
  - Changes of the interface `ListRedislog`:
    - Add the response parameter `backup_id`
    - Remove the response parameter `backupId`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `region` changed to required of the interface `ListFlavors`

### HuaweiCloud SDK IEF

- _Features_
  - Support the following interfaces：
    - `RestartDeploymentsPod`
    - `ShowEdgeNodeUpgradeDetails`
    - `UpgradeEdgeNode`
    - `ListEncryptdatas`
    - `CreateEncryptdatas`
    - `ShowEncryptdatas`
    - `UpdateEncryptdatas`
    - `DeleteEncryptdatas`
    - `ListNodeEncryptdatas`
    - `CreateNodeEncryptdatas`
    - `DeleteNodeEncryptdatas`
    - `ListEncryptdataNodes`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateEdgeNode`:
    - Add the request parameter `UpdateEdgeNodeRequestBody`
    - Remove the request parameter `UpdateEdgeNodeBody`
  - Changes of the interface `EnableDisableEdgeNodes`:
    - Add the request parameter `EnableDisableEdgeNodesRequestBody`
    - Remove the request parameter `node`
  - Add the response parameter `host_pid` to the interface `ListApps`
  - Add the response parameter `host_pid` to the interface `UpdateApp`
  - Add the response parameter `host_pid` to the interface `ShowAppDetail`
  - Add the request parameter `host_pid` to the interface `CreateAppVersions`
  - Add the response parameter `host_pid` to the interface `ListAppVersions`
  - Changes of the interface `UpdateAppVersion`:
    - Add the request parameter `host_pid`
    - Add the response parameter `host_pid`
  - Add the response parameter `host_pid` to the interface `ShowAppVersionDetail`

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `width`, `height` changed to not required of the interface `ShowTranscodingsTemplate`
  - Changes of the interface `UpdateTranscodingsTemplate`:
    - Add the request parameter `trans_type`
    - The request parameter `width`, `height` changed to not required
  - Changes of the interface `CreateTranscodingsTemplate`:
    - Add the request parameter `trans_type`
    - The request parameter `width`, `height` changed to not required

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `type`, `idcard_number`, `phone_number`, `province`, `city`, `vaccination_status`, `pcr_test_result`, `pcr_test_organization`, `pcr_test_time`, `pcr_sampling_time`, `reached_city` to the interface `RecognizeHealthCode`

### HuaweiCloud SDK VPCEP

- _Features_
  - Support the following interfaces：
    - `UpdateEndpointServiceName`
    - `UpdateEndpointConnectionsDesc`
    - `BatchAddEndpointServicePermissions`
    - `BatchRemoveEndpointServicePermissions`
    - `UpdateEndpointServicePermissionDesc`
    - `UpdateEndpointPolicy`
    - `DeleteEndpointPolicy`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateEndpointService`:
    - Add the request parameter `description`
    - Add the response parameter `description`
  - Changes of the interface `ListEndpointService`:
    - Add the request parameter `public_border_group`
    - Add the response parameters `description`, `public_border_group`
    - Modify the type `string` -> `enum` of the response parameter `service_type`
    - Modify the type `enum` -> `string` of the response parameter `server_type`
  - Changes of the interface `UpdateEndpointService`:
    - Add the request parameter `description`
    - Add the response parameter `description`
  - Changes of the interface `ListServiceDetails`:
    - Add the response parameter `description`
    - Modify the type `string` -> `enum` of the response parameter `service_type`
  - Remove the response parameters `id`, `marker_id`, `created_at`, `updated_at`, `domain_id`, `status` from the interface `ListServiceConnections`
  - Add the response parameter `description` to the interface `AcceptOrRejectEndpoint`
  - Remove the response parameters `id`, `permission`, `created_at` from the interface `ListServicePermissionsDetails`
  - Changes of the interface `CreateEndpoint`:
    - Add the request parameter `description`
    - Add the response parameters `specification_name`, `description`, `policy_statement`, `enable_status`
  - Changes of the interface `ListEndpoints`:
    - Add the request parameter `public_border_group`
    - Add the response parameters `description`, `policy_statement`, `endpoint_pool_id`, `public_border_group`
  - Add the response parameters `description`, `policy_statement` to the interface `ListEndpointInfoDetails`
  - Remove the response parameters `status`, `id`, `updated`, `version`, `min_version`, `links` from the interface `ListVersionDetails`
  - Remove the response parameters `status`, `id`, `updated`, `version`, `min_version`, `links` from the interface `ListSpecifiedVersionDetails`
  - Changes of the interface `ListResourceInstances`:
    - Add the request parameters `sys_tags`, `without_any_tag`
    - Remove the request parameters `key`, `value`, `key`, `value`, `key`, `value`, `key`, `value`

# 3.1.4 2022-09-26

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `version`, `last_modified` to the interface `CreateDependency`
  - Add the response parameters `version`, `last_modified` to the interface `ListDependencies`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `disk_encrypted_key`, `public_management_connect_address`, `subnet_cidr`, `subnet_name`, `enable_acl` to the interface `ListInstances`
  - Add the response parameters `disk_encrypted_key`, `public_management_connect_address`, `subnet_cidr`, `subnet_name`, `enable_acl` to the interface `ShowInstance`
  - Add the request parameters `oper_type`, `new_broker_num`, `new_product_id` to the interface `ResizeInstance`

### HuaweiCloud SDK Moderation

- _Features_
  - None
- _Bug Fix_
  - Fix the problem that the response parameters' type of the interface `CheckImageModeration` is incorrect
- _Change_
  - None

# 3.1.3 2022-09-22

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `network_type`, `alias_urn`, `network_type`, `alias_urn` to the interface `CreateApiV2`
  - Add the response parameters `network_type`, `alias_urn`, `network_type`, `alias_urn` to the interface `ShowDetailsOfApiV2`
  - Changes of the interface `UpdateApiV2`:
    - Add the request parameters `network_type`, `alias_urn`, `network_type`, `alias_urn`
    - Add the response parameters `network_type`, `alias_urn`, `network_type`, `alias_urn`
  - Add the response parameters `network_type`, `alias_urn`, `network_type`, `alias_urn` to the interface `ListApiVersionDetailV2`
  - Remove the response parameters `url_domain`, `id`, `status`, `min_ssl_version` from the interface `UpdateDomainV2`
  - Add the response parameters `req_uri`, `auth_type` to the interface `ListApisUnbindedToAclPolicyV2`
  - Add the response parameters `authorizer_version`, `authorizer_alias_uri` to the interface `ListCustomAuthorizersV2`
  - Add the request parameters `authorizer_version`, `authorizer_alias_uri` to the interface `CreateCustomAuthorizerV2`
  - Add the response parameters `authorizer_version`, `authorizer_alias_uri` to the interface `ShowDetailsOfCustomAuthorizersV2`
  - Changes of the interface `UpdateCustomAuthorizerV2`:
    - Add the request parameters `authorizer_version`, `authorizer_alias_uri`
    - Add the response parameters `authorizer_version`, `authorizer_alias_uri`
  - The request parameter `env_id` changed to required of the interface `ExportApiDefinitionsV2`
  - Changes of the interface `ListTagsV2`:
    - Add the response parameter `tags`
    - Remove the response parameter `responses`
  - Remove the response parameters `id`, `name`, `enable`, `config`, `instance_id`, `update_time` from the interface `CreateFeatureV2`
  - Add the response parameter `ingress_ip_v6` to the interface `ShowDetailsOfInstanceV2`
  - Add the response parameter `ingress_ip_v6` to the interface `UpdateInstanceV2`

### HuaweiCloud SDK CES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `event_type` to the interface `CreateEvents`
  - Add the response parameter `event_type` to the interface `ListEventDetail`

### HuaweiCloud SDK CloudPipeline

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ShowAgentStatus`, `RegisterAgent`

### HuaweiCloud SDK CodeCheck

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `check_end_time` to the interface `CheckRecord`
  - Add the response parameter `events` to the interface `ShowTaskDefects`
  - Remove the response parameters `name`, `cfg_key`, `default_value`, `option_value`, `is_required`, `description`, `type`, `status` from the interface `CheckParameters`
  - Add the response parameter `value` to the interface `CheckRulesetParameters`

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListProjectSets`:
    - Add the response parameter `source`
    - Remove the response parameter `status`
  - Add the response parameter `parallel` to the interface `ShowTaskSet`

### HuaweiCloud SDK CTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `group_id`, `stream_id` to the interface `ListTrackers`

### HuaweiCloud SDK DDM

- _Features_
  - Support the interfaces `ResetAdministrator`, `ValidateWeakPassword`, `ResizeFlavor`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `admin_user_name`, `admin_user_password` to the interface `CreateInstance`
  - Add the response parameter `admin_user_name` to the interface `ShowInstance`
  - Add the response parameter `host` to the interface `ListSlowLog`

### HuaweiCloud SDK DevStar

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `none` to the response parameter `deploy_type` to the interface `ShowApplicationV3`
  - Add the response parameter `subscribe_guide` to the interface `ShowApplicationDependentResources`
  - Add the enum values `none` to the response parameter `deploy_type` to the interface `ListApplicationsV6`
  - Add the response parameter `category_name` to the interface `ShowApplicationReleaseRepositories`
  - Add the response parameter `subscribe_guide` to the interface `ShowTemplateV3`
  - Add the response parameter `subscribe_guide` to the interface `ListTemplatesV2`
  - Add the response parameter `subscribe_guide` to the interface `ListTemplates`

### HuaweiCloud SDK EG

- _Features_
  - Support the following interfaces：
    - `ListApiVersions`
    - `ListEventSchema`
    - `CreateEventSchema`
    - `ShowDetailOfEventSchema`
    - `UpdateEventSchema`
    - `DeleteEventSchema`
    - `ListEventSchemaVersions`
    - `CreateEventSchemaVersion`
    - `ShowDetailOfEventSchemaVersion`
    - `DeleteEventSchemaVersion`
    - `DiscoverEventSchemaFromData`
    - `ListConnections`
    - `CreateConnection`
    - `ShowDetailOfConnection`
    - `UpdateConnection`
    - `DeleteConnection`
    - `ListAgencies`
    - `CreateAgencies`
    - `ListTriggers`
    - `UpdateEndpoint`
    - `DeleteEndpoint`
    - `ListEndpoints`
    - `CreateEndpoint`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `id`, `name`, `label`, `description`, `provider_type`, `event_types`, `created_time`, `updated_time`, `channel_id`, `channel_name` from the interface `ListEventSources`
  - Changes of the interface `CreateEventSource`:
    - Add the request parameters `type`, `detail`
    - Add the response parameters `event_types`, `type`, `detail`, `status`
  - Add the response parameters `event_types`, `type`, `detail`, `status` to the interface `ShowDetailOfEventSource`
  - Changes of the interface `UpdateEventSource`:
    - Add the request parameter `detail`
    - Add the response parameters `event_types`, `type`, `detail`, `status`
  - Remove the response parameters `name`, `label`, `metadata` from the interface `ListEventTarget`
  - Add the response parameter `connection_id` to the interface `ListSubscriptions`
  - Changes of the interface `CreateSubscription`:
    - Add the request parameter `connection_id`
    - Add the response parameter `connection_id`
  - Add the response parameter `connection_id` to the interface `ShowDetailOfSubscription`
  - Changes of the interface `UpdateSubscription`:
    - Add the request parameter `connection_id`
    - Add the response parameter `connection_id`
  - Changes of the interface `CreateSubscriptionTarget`:
    - Add the request parameter `connection_id`
    - Add the response parameter `connection_id`
  - Add the response parameter `connection_id to the interface `ShowDetailOfSubscriptionTarget`
  - Changes of the interface `UpdateSubscriptionTarget`:
    - Add the request parameter `connection_id`
    - Add the response parameter `connection_id`
  - Changes of the interface `ListQuotas`:
    - Add the enum values `CONNECTION`, `PRIVATE_ENDPOINT`, `SOURCE_RABBITMQ` to the request parameter `type`
    - Add the enum values `CONNECTION`, `PRIVATE_ENDPOINT`, `SOURCE_RABBITMQ` to the response parameter `type`
    - Modify the type `string` -> `int32` of the response parameter `max`
    - Modify the type `string` -> `int32` of the response parameter `min`
    - Modify the type `string` -> `int32` of the response parameter `quota`
    - Modify the type `string` -> `int32` of the response parameter `used`

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `port_id` to the interface `CreatePublicip`
  - Add the request parameter `port_id` to the interface `CreatePrePaidPublicip`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interface `ListGaussMySqlInstanceDetailInfo`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `error_info` to the interface `ListDeviceMessages`
  - Add the response parameter `error_info` to the interface `ShowDeviceMessage`

### HuaweiCloud SDK Moderation

- _Features_
  - Support the interface `CheckImageModeration`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `url`, `categories` changed to required of the interface `RunCreateAudioModerationJob`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `RecognizeIdCard`:
    - Add the request parameter `detect_copy`
    - Add the response parameter `detect_copy_result`

### HuaweiCloud SDK OMS

- _Features_
  - Support the following interfaces：
    - `ListTaskGroup`
    - `CreateTaskGroup`
    - `ShowTaskGroup`
    - `DeleteTaskGroup`
    - `StopTaskGroup`
    - `StartTaskGroup`
    - `RetryTaskGroup`
    - `UpdateTaskGroup`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `enable_metadata_migration`, `object_overwrite_mode`, `consistency_check`, `enable_requester_pays` to the interface `ListTasks`
  - Changes of the interface `CreateTask`:
    - Add the request parameters `enable_metadata_migration`, `object_overwrite_mode`, `consistency_check`, `enable_requester_pays`
    - Add the response parameters `id`, `task_name`
  - Changes of the interface `ShowTask`:
    - Add the response parameters `enable_metadata_migration`, `object_overwrite_mode`, `consistency_check`, `enable_requester_pays`
    - Modify the type `int64` -> `string` of the request parameter `task_id`
  - Modify the type `int64` -> `string` of the request parameter `task_id` of the interface `DeleteTask`
  - Modify the type `int64` -> `string` of the request parameter `task_id` of the interface `StopTask`
  - Modify the type `int64` -> `string` of the request parameter `task_id` of the interface `StartTask`
  - Modify the type `int64` -> `string` of the request parameter `task_id` of the interface `UpdateBandwidthPolicy`

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interfaces `DownloadImageFile`, `ListScrumProjectStatuses`, `UploadAttachments`
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
  - Add the enum values `rabbitmq`, Remove the enum values `true`, `false` from the request parameter `all_failure` to the interface `BatchRestartOrDeleteInstances`

### HuaweiCloud SDK SMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `disks` from the interface `ListTemplates`
  - Remove the response parameter `disks` from the interface `ShowTemplate`
  - Remove the request parameter `disks` from the interface `UpdateMigproject`
  - Remove the response parameter `disks` from the interface `ShowMigproject`

### HuaweiCloud SDK VOD

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `pack_type`, `pack_type` to the interface `PublishAssets`
  - Add the response parameters `pack_type`, `pack_type` to the interface `UnpublishAssets`
  - Add the response parameters `pack_type`, `pack_type` to the interface `ShowAssetMeta`
  - Add the response parameters `pack_type`, `pack_type` to the interface `ShowAssetDetail`
  - Add the response parameters `pack_type`, `pack_type` to the interface `ShowTakeOverTaskDetails`
  - Add the response parameters `pack_type`, `pack_type` to the interface `ShowTakeOverAssetDetails`

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `rule` to the interface `DeleteIgnoreRule`

# 3.1.2 2022-09-15

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `root_resource_id`, `parent_resource_id`, `trade_id`, `product_spec_desc` to the interface `ListCustomerselfResourceRecordDetails`

### HuaweiCloud SDK CDN

- _Features_
  - Support the interfaces `ShowTags`, `CreateTags`, `BatchDeleteTags`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowUrlTaskInfo`:
    - Add the response parameter `result`
    - Remove the response parameter `results`
  - Add the response parameter `error_code_cache` to the interface `ShowDomainFullConfig`
  - Add the request parameter `error_code_cache` to the interface `UpdateDomainFullConfig`

### HuaweiCloud SDK CodeHub

- _Features_
  - Support the following interfaces：
    - `ListFilesByQuery`
    - `ListBranchesByRepositoryId`
    - `CreateNewBranch`
    - `AssociateIssues`
    - `ListMergeRequest`
    - `ShowMergeRequest`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListSubfiles`:
    - Add the response parameters `error`, `result`, `status`
    - Remove the response parameters `trees`, `total`
  - Changes of the interface `ShowStatisticalData`:
    - Add the response parameters `error`, `result`, `status`
    - Remove the response parameters `repoName`, `commitCount`, `repoSize`, `lastCommitTime`, `codeLines`, `branchCount`, `archiveUrl`
  - Modify the type `string` -> `boolean` of the request parameter `force` of the interface `CreateCommit`
  - Changes of the interface `AddProtectBranchV2`:
    - Modify the type `int32` -> `enum` of the request parameter `push_access_level`
    - Modify the type `int32` -> `enum` of the request parameter `merge_access_level`

### HuaweiCloud SDK CSE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `create_revision`, `update_revision` to the interface `UploadKie`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `CloseKibanaPublicReq` to the interface `UpdateCloseKibana`
  - Add the request parameter `payInfo` to the interface `CreateCluster`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `enterprise_project_name`, `update_at`, `product_type`, `storage_type`, `launched_at`, `cache_mode`, `support_slow_log_flag`, `db_number`, `replica_count`, `sharding_count`, `bandwidth_info` to the interface `ShowInstance`
  - Add the response parameter `backupId` to the interface `ListRedislog`
  - Add the response parameter `instance_id` to the interface `ShowIpWhitelist`
  - Add the request parameter `instance_id` to the interface `UpdateIpWhitelist`
  - Add the response parameters `updated_at`, `created_at`, `status` to the interface `ListBackgroundTask`

### HuaweiCloud SDK DLI

- _Features_
  - Support the interfaces `CreateDownloadJob`, `UpdateTableOwner`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListGlobalValues`:
    - Add the response parameter `is_sensitive`
    - Modify the type `int32` -> `string` of the response parameter `id`
  - Changes of the interface `CreateGlobleValue`:
    - Add the request parameter `CreateGlobalValueReq`
    - Remove the request parameter `createGlobaleValueReq`
  - Remove the request parameter `var_name` from the interface `UpdateGlobalValue`
  - Remove the request parameters `event_type`, `operation`, `timestamp`, `topic`, `name`, `attributes` from the interface `CreateIefSystemEvents`
  - Changes of the interface `ListJobs`:
    - Add the request parameters `owner`, `tags`
    - Add the response parameters `message`, `end_time`
    - Remove the response parameters `key`, `value`
  - Modify the type `object` -> `string` of the request parameter `partition_spec` of the interface `ImportData`
  - Remove the request parameters `key`, `value` from the interface `RunJob`
  - Remove the response parameters `key`, `value` from the interface `ShowDetailInfo`
  - Remove the response parameters `key`, `value` from the interface `ShowJobStatus`
  - Remove the request parameters `key`, `value` from the interface `CreateDatabase`
  - Modify the type `int64` -> `int32` of the response parameter `create_time` of the interface `ListAllTables`
  - Remove the request parameters `limit`, `offset` from the interface `ShowObjectUser`
  - Remove the request parameters `key`, `value` from the interface `CreateFlinkJar`
  - Add the request parameter `job_type` to the interface `UpdateFlinkJar`
  - Changes of the interface `ListFlinkJobs`:
    - Add the response parameter `user_name`
    - Remove the response parameter `username`
  - Remove the request parameters `key`, `value` from the interface `CreateFlinkSql`
  - Changes of the interface `CreateFlinkTemplate`:
    - Remove the request parameters `key`, `value`
    - Modify the type `string` -> `enum` of the request parameter `job_type`
  - Modify the type `int32` -> `int64` of the response parameter `update_time` of the interface `ListResources`
  - Changes of the interface `UploadResources`:
    - Add the request parameter `USER-ID`
    - Remove the request parameters `USER_ID`, `key`, `value`
    - The request parameter `group` changed to required
  - Changes of the interface `UploadFiles`:
    - Add the request parameter `USER-ID`
    - Remove the request parameter `USER_ID`
    - The request parameter `group` changed to required
  - Changes of the interface `UploadJars`:
    - Add the request parameter `USER-ID`
    - Remove the request parameter `USER_ID`
    - The request parameter `group` changed to required
  - Changes of the interface `UploadPythonFiles`:
    - Add the request parameter `USER-ID`
    - Remove the request parameter `USER_ID`
    - The request parameter `group` changed to required
  - Changes of the interface `ListBatches`:
    - Add the request parameters `end`, `order`, `start`
    - Add the response parameter `duration`
  - Changes of the interface `CreateBatchJob`:
    - Add the request parameter `USER-ID`
    - Remove the request parameter `USER_ID`
    - The request parameter `queue` changed to not required
  - Changes of the interface `ListElasticResourcePools`:
    - Modify the type `int32` -> `int64` of the response parameter `update_time`
    - Modify the type `int32` -> `int64` of the response parameter `create_time`
  - Add the request parameter `tags` to the interface `ListEnhancedConnections`
  - Remove the request parameters `key`, `value` from the interface `CreateEnhancedConnection`
  - Changes of the interface `ListDatasourceConnections`:
    - Add the request parameter `tags`
    - Remove the response parameters `is_success`, `message`, `connection_id`, `destination`, `state`, `process`, `name`, `connection_url`, `cluster_name`, `service`, `create_time`
  - Remove the request parameters `key`, `value` from the interface `CreateDatasourceConnection`
  - Changes of the interface `ShowDatasourceConnection`:
    - Add the response parameter `queueList`
    - Remove the response parameter `available_queue_info`
  - Changes of the interface `ListQueues`:
    - Add the response parameter `resource_type`
    - Remove the request parameters `page-size`, `current-page`, `order`
    - Remove the response parameters `queue_resource_type`, `cu_spec`, `cu_scale_out_limit`, `cu_scale_in_limit`, `elastic_resource_pool_name`
    - Modify the type `string` -> `int64` of the response parameter `queue_id`
    - Modify the type `array` -> `string` of the response parameter `labels`
  - Remove the request parameters `key`, `value` from the interface `CreateQueue`
  - Changes of the interface `ShowQueueDetail`:
    - Add the response parameters `queue_name`, `cu_count`, `charging_mode`
    - Remove the request parameter `queue_type`
    - Remove the response parameters `queueName`, `cuCount`, `chargingMode`, `queueType`, `resource_type`, `cu_spec`, `cu_scale_out_limit`, `cu_scale_in_limit`, `elastic_resource_pool_name`
    - Modify the type `string` -> `int64` of the response parameter `queue_id`
  - Changes of the interface `RunQueueAction`:
    - Add the request parameter `RunQueueActionReq`
    - Remove the request parameter `body`
  - The request parameter `repeat_day` changed to not required of the interface `CreateQueuePlan`
  - The request parameter `repeat_day` changed to not required of the interface `ChangeQueuePlan`

### HuaweiCloud SDK EVS

- _Features_
  - Support the following interfaces：
    - `ShowVersion`
    - `ListVersions`
    - `CinderShowVolumeTransfer`
    - `CinderDeleteVolumeTransfer`
    - `CinderListVolumeTransfers`
    - `CinderCreateVolumeTransfer`
    - `CinderAcceptVolumeTransfer`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IEF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `ListApps`
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `UpdateApp`
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `ShowAppDetail`
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `ListAppVersions`
  - Add the request parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `CreateAppVersions`
  - Changes of the interface `UpdateAppVersion`:
    - Add the request parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu`
    - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu`
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `ShowAppVersionDetail`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `ttl_in_days` to the interface `CreateLogStream`
  - Add the request parameter `whether_to_rows` to the interface `ListStructuredLogsWithTimeRange`
  - The request parameter `isAnalysis` changed to not required of the interface `UpdateStructTemplate`
  - The request parameter `isAnalysis` changed to not required of the interface `CreateStructTemplate`

### HuaweiCloud SDK Moderation

- _Features_
  - Support the interfaces `RunCreateVideoModerationJob`, `RunQueryVideoModerationJob`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `url` changed to not required of the interface `RunCreateAudioModerationJob`

# 3.1.1 2022-09-08

### HuaweiCloud SDK IAM

- _Features_
  - Support the custom credential `IamCredentials`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `root_resource_id`, `parent_resource_id`, `trade_id`, `product_spec_desc` to the interface `ListCustomerselfResourceRecordDetails`

### HuaweiCloud SDK CDN

- _Features_
  - Support the interfaces `ShowTags`, `CreateTags`, `BatchDeleteTags`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowUrlTaskInfo`:
    - Add the response parameter `result`
    - Remove the response parameter `results`
  - Add the response parameter `error_code_cache` to the interface `ShowDomainFullConfig`
  - Add the request parameter `error_code_cache` to the interface `UpdateDomainFullConfig`

### HuaweiCloud SDK CodeHub

- _Features_
  - Support the following interfaces：
    - `ListFilesByQuery`
    - `ListBranchesByRepositoryId`
    - `CreateNewBranch`
    - `AssociateIssues`
    - `ListMergeRequest`
    - `ShowMergeRequest`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListSubfiles`:
    - Add the response parameters `error`, `result`, `status`
    - Remove the response parameters `trees`, `total`
  - Changes of the interface `ShowStatisticalData`:
    - Add the response parameters `error`, `result`, `status`
    - Remove the response parameters `repoName`, `commitCount`, `repoSize`, `lastCommitTime`, `codeLines`, `branchCount`, `archiveUrl`
  - Modify the type `string` -> `boolean` of the request parameter `force` of the interface `CreateCommit`
  - Changes of the interface `AddProtectBranchV2`:
    - Modify the type `int32` -> `enum` of the request parameter `push_access_level`
    - Modify the type `int32` -> `enum` of the request parameter `merge_access_level`

### HuaweiCloud SDK CSE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `create_revision`, `update_revision` to the interface `UploadKie`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `CloseKibanaPublicReq` to the interface `UpdateCloseKibana`
  - Add the request parameter `payInfo` to the interface `CreateCluster`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `enterprise_project_name`, `update_at`, `product_type`, `storage_type`, `launched_at`, `cache_mode`, `support_slow_log_flag`, `db_number`, `replica_count`, `sharding_count`, `bandwidth_info` to the interface `ShowInstance`
  - Add the response parameter `backupId` to the interface `ListRedislog`
  - Add the response parameter `instance_id` to the interface `ShowIpWhitelist`
  - Add the request parameter `instance_id` to the interface `UpdateIpWhitelist`
  - Add the response parameters `updated_at`, `created_at`, `status` to the interface `ListBackgroundTask`

### HuaweiCloud SDK DLI

- _Features_
  - Support the interfaces `CreateDownloadJob`, `UpdateTableOwner`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListGlobalValues`:
    - Add the response parameter `is_sensitive`
    - Modify the type `int32` -> `string` of the response parameter `id`
  - Changes of the interface `CreateGlobleValue`:
    - Add the request parameter `CreateGlobalValueReq`
    - Remove the request parameter `createGlobaleValueReq`
  - Remove the request parameter `var_name` from the interface `UpdateGlobalValue`
  - Remove the request parameters `event_type`, `operation`, `timestamp`, `topic`, `name`, `attributes` from the interface `CreateIefSystemEvents`
  - Changes of the interface `ListJobs`:
    - Add the request parameters `owner`, `tags`
    - Add the response parameters `message`, `end_time`
    - Remove the response parameters `key`, `value`
  - Modify the type `object` -> `string` of the request parameter `partition_spec` of the interface `ImportData`
  - Remove the request parameters `key`, `value` from the interface `RunJob`
  - Remove the response parameters `key`, `value` from the interface `ShowDetailInfo`
  - Remove the response parameters `key`, `value` from the interface `ShowJobStatus`
  - Remove the request parameters `key`, `value` from the interface `CreateDatabase`
  - Modify the type `int64` -> `int32` of the response parameter `create_time` of the interface `ListAllTables`
  - Remove the request parameters `limit`, `offset` from the interface `ShowObjectUser`
  - Remove the request parameters `key`, `value` from the interface `CreateFlinkJar`
  - Add the request parameter `job_type` to the interface `UpdateFlinkJar`
  - Changes of the interface `ListFlinkJobs`:
    - Add the response parameter `user_name`
    - Remove the response parameter `username`
  - Remove the request parameters `key`, `value` from the interface `CreateFlinkSql`
  - Changes of the interface `CreateFlinkTemplate`:
    - Remove the request parameters `key`, `value`
    - Modify the type `string` -> `enum` of the request parameter `job_type`
  - Modify the type `int32` -> `int64` of the response parameter `update_time` of the interface `ListResources`
  - Changes of the interface `UploadResources`:
    - Add the request parameter `USER-ID`
    - Remove the request parameters `USER_ID`, `key`, `value`
    - The request parameter `group` changed to required
  - Changes of the interface `UploadFiles`:
    - Add the request parameter `USER-ID`
    - Remove the request parameter `USER_ID`
    - The request parameter `group` changed to required
  - Changes of the interface `UploadJars`:
    - Add the request parameter `USER-ID`
    - Remove the request parameter `USER_ID`
    - The request parameter `group` changed to required
  - Changes of the interface `UploadPythonFiles`:
    - Add the request parameter `USER-ID`
    - Remove the request parameter `USER_ID`
    - The request parameter `group` changed to required
  - Changes of the interface `ListBatches`:
    - Add the request parameters `end`, `order`, `start`
    - Add the response parameter `duration`
  - Changes of the interface `CreateBatchJob`:
    - Add the request parameter `USER-ID`
    - Remove the request parameter `USER_ID`
    - The request parameter `queue` changed to not required
  - Changes of the interface `ListElasticResourcePools`:
    - Modify the type `int32` -> `int64` of the response parameter `update_time`
    - Modify the type `int32` -> `int64` of the response parameter `create_time`
  - Add the request parameter `tags` to the interface `ListEnhancedConnections`
  - Remove the request parameters `key`, `value` from the interface `CreateEnhancedConnection`
  - Changes of the interface `ListDatasourceConnections`:
    - Add the request parameter `tags`
    - Remove the response parameters `is_success`, `message`, `connection_id`, `destination`, `state`, `process`, `name`, `connection_url`, `cluster_name`, `service`, `create_time`
  - Remove the request parameters `key`, `value` from the interface `CreateDatasourceConnection`
  - Changes of the interface `ShowDatasourceConnection`:
    - Add the response parameter `queueList`
    - Remove the response parameter `available_queue_info`
  - Changes of the interface `ListQueues`:
    - Add the response parameter `resource_type`
    - Remove the request parameters `page-size`, `current-page`, `order`
    - Remove the response parameters `queue_resource_type`, `cu_spec`, `cu_scale_out_limit`, `cu_scale_in_limit`, `elastic_resource_pool_name`
    - Modify the type `string` -> `int64` of the response parameter `queue_id`
    - Modify the type `array` -> `string` of the response parameter `labels`
  - Remove the request parameters `key`, `value` from the interface `CreateQueue`
  - Changes of the interface `ShowQueueDetail`:
    - Add the response parameters `queue_name`, `cu_count`, `charging_mode`
    - Remove the request parameter `queue_type`
    - Remove the response parameters `queueName`, `cuCount`, `chargingMode`, `queueType`, `resource_type`, `cu_spec`, `cu_scale_out_limit`, `cu_scale_in_limit`, `elastic_resource_pool_name`
    - Modify the type `string` -> `int64` of the response parameter `queue_id`
  - Changes of the interface `RunQueueAction`:
    - Add the request parameter `RunQueueActionReq`
    - Remove the request parameter `body`
  - The request parameter `repeat_day` changed to not required of the interface `CreateQueuePlan`
  - The request parameter `repeat_day` changed to not required of the interface `ChangeQueuePlan`

### HuaweiCloud SDK EVS

- _Features_
  - Support the following interfaces：
    - `ShowVersion`
    - `ListVersions`
    - `CinderShowVolumeTransfer`
    - `CinderDeleteVolumeTransfer`
    - `CinderListVolumeTransfers`
    - `CinderCreateVolumeTransfer`
    - `CinderAcceptVolumeTransfer`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IEF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `ListApps`
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `UpdateApp`
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `ShowAppDetail`
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `ListAppVersions`
  - Add the request parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `CreateAppVersions`
  - Changes of the interface `UpdateAppVersion`:
    - Add the request parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu`
    - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu`
  - Add the response parameters `cpu`, `memory`, `gpu`, `npu`, `cpu`, `memory`, `gpu`, `npu` to the interface `ShowAppVersionDetail`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `ttl_in_days` to the interface `CreateLogStream`
  - Add the request parameter `whether_to_rows` to the interface `ListStructuredLogsWithTimeRange`
  - The request parameter `isAnalysis` changed to not required of the interface `UpdateStructTemplate`
  - The request parameter `isAnalysis` changed to not required of the interface `CreateStructTemplate`

### HuaweiCloud SDK Moderation

- _Features_
  - Support the interfaces `RunCreateVideoModerationJob`, `RunQueryVideoModerationJob`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `url` changed to not required of the interface `RunCreateAudioModerationJob`

# 3.0.108 2022-09-01

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `indirect_partner_id` to the interface `ListCustomerOrders`
  - Add the request parameter `indirect_partner_id` to the interface `ShowCustomerOrderDetails`
  - Add the request parameter `indirect_partner_id` to the interface `ListCustomerOnDemandResources`

### HuaweiCloud SDK CC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the enum values `er` from the response parameter `used_scene` from the interface `ListCloudConnections`
  - Remove the request parameter `used_scene` from the interface `CreateCloudConnection`
  - Remove the enum values `er` from the response parameter `used_scene` from the interface `ShowCloudConnection`
  - Remove the enum values `er` from the response parameter `used_scene` from the interface `UpdateCloudConnection`
  - Remove the enum values `er` from the response parameter `type` from the interface `ListNetworkInstances`
  - Remove the enum values `er` from the request parameter `type` from the interface `CreateNetworkInstance`
  - Remove the enum values `er` from the response parameter `type` from the interface `ShowNetworkInstance`
  - Remove the enum values `er` from the response parameter `type` from the interface `UpdateNetworkInstance`

### HuaweiCloud SDK CDM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `id`, `type` changed to not required of the interface `ShowJobs`
  - The request parameter `id`, `type` changed to not required of the interface `UpdateJob`
  - The request parameter `id`, `type` changed to not required of the interface `CreateAndStartRandomClusterJob`
  - The request parameter  `id`, `type` changed to not required of the interface `CreateJob`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `ordeId` to the interface `CreateCluster`
  - Changes of the interface `ShowClusterDetail`:
    - Add the response parameters `vpcepIp`, `elbWhiteListResp`
    - Remove the response parameters `elbWhiteList`, `action`
  - Remove the request parameter `isAutoPay` from the interface `UpdateUnbindPublic`
  - Changes of the interface `ListYmlsJob`:
    - Add the response parameter `configList`
    - Remove the response parameter `configurations`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `version`, `last_modified` from the interface `CreateDependency`
  - Remove the response parameters `version`, `last_modified` from the interface `ListDependencies`

### HuaweiCloud SDK IAM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateDomainProtectPolicy`:
    - Add the request parameters `allow_user`, `mobile`, `admin_check`, `email`, `scene`
    - Remove the response parameter `operation_protection`
  - Remove the response parameter `operation_protection` from the interface `ShowDomainProtectPolicy`
  - The request parameter `maximum_consecutive_identical_chars`, `minimum_password_age`, `minimum_password_length`, `number_of_recent_passwords_disallowed`, `password_not_username_or_invert`, `password_validity_period`, `password_char_combination` changed to not required of the interface `UpdateDomainPasswordPolicy`
  - The request parameter `account_validity_period`, `custom_info_for_login`, `lockout_duration`, `login_failed_times`, `period_with_login_failures`, `session_timeout`, `show_recent_login_info` changed to not required of the interface `UpdateDomainLoginPolicy`
  - Add the enum values `mapping` to the request parameter `type` to the interface `ShowDomainQuota`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `UpdateDbUserComment`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `comment` to the interface `CreateDbUser`

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListStatistics`:
    - Modify the type `array` -> `string` of the request parameter `hosts`
    - Modify the type `array` -> `string` of the request parameter `instances`
  - Changes of the interface `ListQpsTimeline`:
    - Modify the type `array` -> `string` of the request parameter `hosts`
    - Modify the type `array` -> `string` of the request parameter `instances`
  - Modify the type `array` -> `string` of the request parameter `instances` of the interface `ListBandwidthTimeline`
  - Changes of the interface `ListTopAbnormal`:
    - Modify the type `array` -> `string` of the request parameter `hosts`
    - Modify the type `array` -> `string` of the request parameter `instances`
  - Changes of the interface `ListOverviewsClassification`:
    - Modify the type `array` -> `string` of the request parameter `hosts`
    - Modify the type `array` -> `string` of the request parameter `instances`

# 3.0.107 2022-08-29

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `batch_create_in_multi_az` to the interface `CreatePostPaidServers`

### HuaweiCloud SDK IMS

- _Features_
  - Support the interface `ShowJobProgress`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `SetReadOnlySwitch`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `FailoverRequestBody` to the interface `StartFailover`

# 3.0.106 2022-08-25

### HuaweiCloud SDK CDM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateJob`:
    - Add the request parameters `rows_written`, `rows_read`, `files_written`, `extended-configs`, `value`, `extended-configs`, `value`, `extended-configs`, `value`
    - Remove the request parameters `files_writte`, `values`, `values`, `values`
  - Changes of the interface `ShowJobs`:
    - Add the response parameters `rows_written`, `rows_read`, `files_written`, `extended-configs`, `value`, `extended-configs`, `value`, `extended-configs`, `value`
    - Remove the response parameters `files_writte`, `values`, `values`, `values`
  - Changes of the interface `CreateAndStartRandomClusterJob`:
    - Add the request parameters `rows_written`, `rows_read`, `files_written`, `extended-configs`, `value`, `extended-configs`, `value`, `extended-configs`, `value`
    - Remove the request parameters `files_writte`, `values`, `values`, `values`
  - Changes of the interface `CreateJob`:
    - Add the request parameters `rows_written`, `rows_read`, `files_written`, `extended-configs`, `value`, `extended-configs`, `value`, `extended-configs`, `value`
    - Remove the request parameters `files_writte`, `values`, `values`, `values`

### HuaweiCloud SDK DLI

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `flink_version` to the interface `CreateFlinkSql`
  - Add the request parameter `flink_version` to the interface `UpdateFlinkSql`
  - The request parameter `key`, `value` changed to required of the interface `CreateElasticResourcePool`
  - Add the response parameters `elastic_resource_pool_name`, `manager`, `label` to the interface `ListElasticResourcePools`
  - Changes of the interface `ListQueues`:
    - Add the request parameters `page-size`, `current-page`, `order`
    - Add the response parameters `queue_id`, `elastic_resource_pool_name`

### HuaweiCloud SDK ELB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
    - `ListMasterSlavePools`
    - `CreateMasterSlavePool`
    - `ShowMasterSlavePool`
    - `DeleteMasterSlavePool`
  - Add the response parameter `waf_failure_action` to the interface `ListLoadBalancers`
  - Add the request parameter `waf_failure_action` to the interface `CreateLoadBalancer`
  - Add the response parameter `waf_failure_action` to the interface `ShowLoadBalancer`
  - Changes of the interface `UpdateLoadBalancer`:
    - Add the request parameter `waf_failure_action`
    - Add the response parameter `waf_failure_action`
    - Remove the request parameter `cloud_service_console_url`
  - Add the response parameters `enc_certificate`, `enc_private_key` to the interface `ListCertificates`
  - Add the request parameters `enc_certificate`, `enc_private_key` to the interface `CreateCertificate`
  - Add the response parameters `enc_certificate`, `enc_private_key` to the interface `ShowCertificate`
  - Changes of the interface `UpdateCertificate`:
    - Add the request parameters `enc_certificate`, `enc_private_key`
    - Add the response parameters `enc_certificate`, `enc_private_key`
  - Add the response parameter `sni_match_algo` to the interface `ListListeners`
  - Add the request parameter `sni_match_algo` to the interface `CreateListener`
  - Add the response parameter `sni_match_algo` to the interface `ShowListener`
  - Changes of the interface `UpdateListener`:
    - Add the request parameter `sni_match_algo`
    - Add the response parameter `sni_match_algo`
  - Add the request parameter `instance_id` to the interface `ListMembers`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `RecognizeWebImage`:
    - Add the request parameter `detect_font`
    - Add the response parameters `font_list`, `font_scores`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `SetDatabaseUserPrivilege`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VOD

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `int32` -> `int64` of the request parameter `size` of the interface `CheckMd5Duplication`

### HuaweiCloud SDK WAF

- _Features_
  - Support the interface `ListRequestTimeline`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `description` to the interface `UpdateGeoipRule`

# 3.0.105 2022-08-22

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `uri` -> `string` of the request parameter `object` of the interface `CreateRecordIndex`

# 3.0.104 2022-08-18

### HuaweiCloud SDK BSSINTL

- _Features_
  - Support the interfaces `ListIndirectPartners`, `ListCosts`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `indirect_partner_id` to the interface `ListSubCustomers`
  - Add the request parameter `indirect_partner_id` to the interface `CreateSubCustomer`
  - Add the request parameter `indirect_partner_id` to the interface `ShowSubCustomerBudget`
  - Add the request parameter `indirect_partner_id` to the interface `UpdateSubCustomerBudget`
  - Add the request parameter `indirect_partner_id` to the interface `FreezeSubCustomers`
  - Add the request parameter `indirect_partner_id` to the interface `UnfreezeSubCustomers`

### HuaweiCloud SDK CloudIDE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `arch` to the interface `ListProjectTemplates`

### HuaweiCloud SDK CPH

- _Features_
  - Support the service `Cloud Phone`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DLI

- _Features_
  - Support the interface `AssociateQueueToElasticResourcePool`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `msg_confirm_topic` changed to not required of the interface `ChangeFlinkJobStatusReport`
  - Remove the request parameters `key`, `value` from the interface `CreateFlinkJar`
  - Remove the request parameters `key`, `value` from the interface `UpdateFlinkJar`
  - Remove the request parameters `key`, `value` from the interface `CreateFlinkSql`
  - Remove the request parameters `key`, `value` from the interface `UpdateFlinkSql`
  - Add the request parameter `elastic_resource_pool_name` to the interface `CreateQueue`
  - Modify the type `string` -> `array` of the response parameter `labels` of the interface `ListQueues`
  - Add the response parameters `queue_id`, `elastic_resource_pool_name` to the interface `ShowQueueDetail`
  - The request parameter `repeat_day` changed to required of the interface `CreateQueuePlan`
  - The request parameter `repeat_day` changed to required of the interface `ChangeQueuePlan`

### HuaweiCloud SDK ECS

- _Features_
  - Support the interface `ListServersByTag`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `destination_type` changed to required of the interface `NovaCreateServers`

### HuaweiCloud SDK EG

- _Features_
  - Support the service `EventGrid`
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
  - Changes of the interface `CreateFunction`:
    - Add the response parameters `enable_dynamic_memory`, `is_stateful_function`, `enable_auth_in_header`, `custom_image`
    - The request parameter `file`, `link` changed to required
    - Modify the type `int32` -> `string` of the response parameter `user_id`
    - Modify the type `int32` -> `string` of the response parameter `user_group_id`
    - The response parameter `concurrent_num` changed to required
    - The response parameter `mount_share_path` changed to not required
  - Changes of the interface `ListFunctions`:
    - Add the response parameter `fail_count`
    - Remove the request parameter `X-Auth-Token`
    - The response parameter `concurrent_num` changed to required
  - Changes of the interface `ShowFunctionCode`:
    - Remove the response parameter `id`
    - The response parameter `file`, `link`, `concurrent_num` changed to required
  - Changes of the interface `UpdateFunctionCode`:
    - Remove the response parameter `id`
    - The request parameter `file`, `link` changed to required
    - The response parameter `file`, `link`, `concurrent_num` changed to required
  - Changes of the interface `ShowFunctionConfig`:
    - Add the response parameters `is_stateful_function`, `enable_auth_in_header`, `custom_image`
    - Remove the response parameter `id`
    - Modify the type `int32` -> `string` of the response parameter `user_id`
    - Modify the type `int32` -> `string` of the response parameter `user_group_id`
    - The response parameter `concurrent_num` changed to required
    - The response parameter `mount_share_path` changed to not required
  - Changes of the interface `UpdateFunctionConfig`:
    - Add the response parameters `enable_auth_in_header`, `custom_image`
    - Remove the request parameter `X-Auth-Token`
    - Remove the response parameter `id`
    - Modify the type `int32` -> `string` of the request parameter `user_id`
    - Modify the type `int32` -> `string` of the request parameter `user_group_id`
    - The request parameter `concurrent_num` changed to required
    - The request parameter `mount_share_path` changed to not required
    - Modify the type `int32` -> `string` of the response parameter `user_id`
    - Modify the type `int32` -> `string` of the response parameter `user_group_id`
    - The response parameter `concurrent_num` changed to required
    - The response parameter `mount_share_path` changed to not required
  - Changes of the interface `UpdateFunctionMaxInstanceConfig`:
    - Remove the response parameter `id`
    - Modify the type `int32` -> `string` of the response parameter `user_id`
    - Modify the type `int32` -> `string` of the response parameter `user_group_id`
    - The response parameter `concurrent_num` changed to required
    - The response parameter `mount_share_path` changed to not required
  - Changes of the interface `CreateFunctionVersion`:
    - Remove the response parameter `id`
    - Modify the type `int32` -> `string` of the response parameter `user_id`
    - Modify the type `int32` -> `string` of the response parameter `user_group_id`
    - The response parameter `concurrent_num` changed to required
    - The response parameter `mount_share_path` changed to not required
  - Changes of the interface `ListFunctionVersions`:
    - Add the response parameters `is_stateful_function`, `enable_auth_in_header`, `custom_image`, `reserved_instance_idle_mode`
    - Remove the response parameters `log_group_id`, `log_stream_id`
    - The response parameter `concurrent_num` changed to required
  - Add the enum values `SMN`, `RABBITMQ`, `DEDICATEDGATEWAY`, `OPENSOURCEKAFKA`, `APIC`, `GAUSSMONGO`, `EVENTGRID` to the request parameter `trigger_type_code` to the interface `CreateFunctionTrigger`
  - Changes of the interface `ListFunctionTriggers`:
    - Add the enum values `RABBITMQ`, `DEDICATEDGATEWAY`, `OPENSOURCEKAFKA`, `APIC`, `GAUSSMONGO`, `EVENTGRID` to the response parameter `trigger_type_code`
    - Add the enum values `DISABLE`, Remove the enum values `DISABLED` from the response parameter `trigger_status`
  - Add the enum values `RABBITMQ`, `DEDICATEDGATEWAY`, `OPENSOURCEKAFKA`, `APIC`, `GAUSSMONGO`, `EVENTGRID` to the request parameter `trigger_type_code` to the interface `DeleteFunctionTrigger`
  - Changes of the interface `ShowFunctionTrigger`:
    - Add the enum values `RABBITMQ`, `DEDICATEDGATEWAY`, `OPENSOURCEKAFKA`, `APIC`, `GAUSSMONGO`, `EVENTGRID` to the request parameter `trigger_type_code`
    - Add the enum values `RABBITMQ`, `DEDICATEDGATEWAY`, `OPENSOURCEKAFKA`, `APIC`, `GAUSSMONGO`, `EVENTGRID` to the response parameter `trigger_type_code`
    - Add the enum values `DISABLE`, Remove the enum values `DISABLED` from the response parameter `trigger_status`
  - Changes of the interface `UpdateTrigger`:
    - Add the enum values `DISABLE`, Remove the enum values `DISABLED` from the request parameter `trigger_status`
    - Add the enum values `RABBITMQ`, `DEDICATEDGATEWAY`, `OPENSOURCEKAFKA`, `APIC`, `GAUSSMONGO`, `EVENTGRID` to the request parameter `trigger_type_code`
    - The request parameter `trigger_status` changed to not required
  - Modify the type `float` -> `int32` of the response parameter `value` of the interface `ListStatistics`
  - Changes of the interface `UpdateFunctionReservedInstancesCount`:
    - Add the request parameter `UpdateFunctionReservedInstancesCountRequestBody`
    - Add the response parameters `idle_mode`, `tactics_config`
    - Remove the request parameter `UpdateFunctionReservedInstancesRequestBody`
  - Changes of the interface `CreateDependency`:
    - Add the response parameters `version`, `last_modified`
    - Modify the type `enum` -> `string` of the response parameter `runtime`
  - Changes of the interface `ListDependencies`:
    - Add the request parameters `maxitems`, `ispublic`
    - Add the response parameters `version`, `last_modified`
    - Modify the type `int32` -> `int64` of the response parameter `count`
  - Changes of the interface `ShowDependcy`:
    - Add the response parameters `version`, `last_modified`
    - Modify the type `enum` -> `string` of the response parameter `runtime`
  - Changes of the interface `UpdateDependcy`:
    - Add the request parameter `UpdateDependcyRequestBody`
    - Remove the request parameter `UpdateDependencyRequestBody`
    - Modify the type `enum` -> `string` of the response parameter `runtime`
  - Remove the response parameters `content`, `last_modified` from the interface `CreateEvent`
  - Remove the response parameters `content`, `last_modified` from the interface `UpdateEvent`
  - Changes of the interface `ImportFunction`:
    - Add the request parameter `package`
    - Remove the request parameter `X-Auth-Token`
    - The response parameter `concurrent_num` changed to required
  - Add the request parameter `X-Auth-Token` to the interface `EnableLtsLogs`
  - Add the response parameter `group_name` to the interface `ShowLtsLogDetails`
  - The request parameter `request_id` changed to required of the interface `CancelAsyncInvocation`
  - Changes of the interface `CreateWorkflow`:
    - Add the request parameter `duration`
    - Add the enum values `SMN`, `APIG`, `APIG_DE` to the request parameter `trigger_type`
  - Changes of the interface `ListWorkflow`:
    - Add the request parameters `enterprise_project`, `mode`
    - Remove the response parameters `id`, `workflow_urn`, `name`, `description`, `created_time`, `updated_time`, `created_by`
  - Add the request parameter `X-WorkflowRun-MergeFnParameters` to the interface `StartWorkflowExecution`
  - Remove the response parameters `workflow_id`, `workflow_urn`, `execution_id`, `status`, `begin_time`, `end_time`, `last_update_time`, `created_by` from the interface `ListWorkflowExecutions`
  - Changes of the interface `ShowWorkflowExecution`:
    - Add the request parameter `X-Get-Workflow-Full-History-Data`
    - Modify the type `string` -> `object` of the response parameter `workflow_urn`
  - Changes of the interface `ShowWorkFlow`:
    - Remove the response parameters `name`, `description`, `triggers`, `start`, `functions`, `states`, `constants`, `retries`, `mode`, `express_config`, `enterprise_project_id`
    - Modify the type `string` -> `object` of the response parameter `workflow_urn`
    - The response parameter `id`, `workflow_urn`, `created_time`, `updated_time`, `created_by` changed to required
  - Changes of the interface `UpdateWorkFlow`:
    - Add the request parameter `duration`
    - Add the enum values `SMN`, `APIG`, `APIG_DE` to the request parameter `trigger_type`
    - Modify the type `string` -> `object` of the response parameter `workflow_urn`
    - The response parameter `id`, `workflow_urn`, `name`, `description`, `created_time`, `updated_time`, `created_by` changed to required

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `RecognizeIdCard`:
    - Add the request parameter `detect_reproduce`
    - Add the response parameter `detect_reproduce_result`

### HuaweiCloud SDK ProjectMan

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateIssueV4`:
    - Add the request parameter `field_name`
    - Add the response parameter `field_name`
  - Add the response parameter `field_name` to the interface `ListIssuesV4`
  - Changes of the interface `UpdateIssueV4`:
    - Add the request parameter `field_name`
    - Add the response parameter `field_name`
  - Add the response parameter `field_name` to the interface `ListChildIssuesV4`
  - Changes of the interface `CreateSystemIssueV4`:
    - Add the request parameter `field_name`
    - Add the response parameter `field_name`

### HuaweiCloud SDK ROMA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `limit`, `offset` to the interface `ListNotification`

### HuaweiCloud SDK VOD

- _Features_
  - Support the following interfaces：
    - `ListTranscodeTemplate`
    - `UpdateTranscodeTemplate`
    - `CreateTranscodeTemplate`
    - `DeleteTranscodeTemplate`
    - `ListTemplateGroupCollection`
    - `UpdateTemplateGroupCollection`
    - `CreateTemplateGroupCollection`
    - `DeleteTemplateGroupCollection`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListIgnoreRule`:
    - Add the response parameter `domain`
    - Remove the response parameter `domains`
  - Add the response parameter `policyid` to the interface `ListGeoipRule`
  - Add the request parameter `description` to the interface `UpdateGeoipRule`

# 3.0.103 2022-08-11

### HuaweiCloud SDK APM

- _Features_
  - Support the following interfaces：
    - `ListOpenRegion`
    - `ListSupportedRegion`
    - `ShowTopologyTree`
    - `ShowMonitorItemViewConfig`
    - `ListEnvTags`
    - `ShowTopology`
    - `ShowEventDetail`
    - `ShowSpanSearch`
    - `ShowTraceEvents`
    - `ShowTrend`
    - `ShowSumTable`
    - `ShowRawTable`
    - `ShowClobDetail`
    - `ListEnvInstances`
    - `ShowEnvMonitorItems`
    - `ListApps`
    - `ListAppEnvs`
    - `ShowAkSks`
    - `CreateAkSk`
    - `DeleteAkSk`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BSS

- _Features_
  - Support the interface `ListCosts`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CDN

- _Features_
  - Support the interface `ShowUrlTaskInfo`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `ipv6_accelerate` to the interface `ShowDomainFullConfig`
  - Add the request parameter `ipv6_accelerate` to the interface `UpdateDomainFullConfig`

### HuaweiCloud SDK CSMS

- _Features_
  - Support the interfaces `UploadSecretBlob`, `DownloadSecretBlob`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the following interfaces：
    - `ListGaussMySqlDatabaseUser`
    - `CreateGaussMySqlDatabaseUser`
    - `DeleteGaussMySqlDatabaseUser`
    - `ResetGaussMySqlDatabasePassword`
    - `AddDatabasePermission`
    - `DeleteDatabasePermission`
    - `ListGaussMySqlDatabaseCharsets`
    - `ListGaussMySqlDatabase`
    - `CreateGaussMySqlDatabase`
    - `DeleteGaussMySqlDatabase`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `enableHyG`, `trafficIpList`, `cryptAlgorithm`, `enableHttps`, `tags` to the interface `ListGraphs`
  - Add the response parameters `enableHyG`, `trafficIpList`, `cryptAlgorithm`, `enableHttps`, `tags` to the interface `ShowGraph`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreatePostPaidInstance`:
    - Add the request parameter `broker_num`
    - Add the enum values `c6.2u4g.cluster`, `c6.4u8g.cluster`, `c6.8u16g.cluster`, `c6.12u24g.cluster`, `c6.16u32g.cluster` to the request parameter `specification`
    - Add the enum values `250`, `500`, `1000`, `1500`, `2000` to the request parameter `partition_num`
    - Add the enum values `dms.physical.storage.high.v2`, `dms.physical.storage.ultra.v2` to the request parameter `storage_spec_code`
    - The request parameter `specification` changed to not required
  - Add the response parameters `description`, `access_user`, `ssl_two_way_enable`, `cert_replaced`, `public_boundwidth`, `agent_enable`, `public_access_enabled`, `node_num`, `new_spec_billing_enable`, `broker_num` to the interface `ListInstances`
  - Add the response parameters `description`, `access_user`, `ssl_two_way_enable`, `cert_replaced`, `public_boundwidth`, `agent_enable`, `public_access_enabled`, `node_num`, `new_spec_billing_enable`, `broker_num` to the interface `ShowInstance`
  - The request parameter `engine` changed to not required of the interface `ShowInstanceExtendProductInfo`
  - Changes of the interface `ShowPartitionBeginningMessage`:
    - Add the response parameter `offset`
    - Remove the response parameter `message_offset`
  - Changes of the interface `ShowPartitionEndMessage`:
    - Add the response parameter `offset`
    - Remove the response parameter `message_offset`
  - Add the response parameter `product_alias` to the interface `ListEngineProducts`

### HuaweiCloud SDK Moderation

- _Features_
  - Support the interfaces `RunCreateAudioModerationJob`, `RunQueryAudioModerationJob`
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `ad_glossaries` from the interface `RunImageModeration`

### HuaweiCloud SDK OCR

- _Features_
  - Support the interface `RecognizeMacaoIdCard`
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
  - Remove the request parameter `count` from the interface `CreateRestoreInstance`

### HuaweiCloud SDK SWR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `filter` to the interface `ListNamespaces`
  - Add the request parameters `limit`, `offset`, `order_column`, `order_type` to the interface `ListReposDetails`
  - Add the request parameter `filter` to the interface `ListRepositoryTags`
  - Add the request parameters `namespace`, `name`, `center`, `limit`, `offset`, `order_column`, `order_type` to the interface `ListSharedReposDetails`
  - Changes of the interface `ListRetentionHistories`:
    - Add the request parameter `filter`
    - Remove the request parameters `offset`, `limit`

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `DeleteIgnoreRule`:
    - Add the response parameter `advanced`
    - Remove the response parameter `rule`
  - Changes of the interface `CreateIgnoreRule`:
    - Add the request parameter `advanced`
    - Add the response parameter `advanced`
  - Add the response parameter `advanced` to the interface `ListIgnoreRule`
  - Changes of the interface `ListStatistics`:
    - Remove the response parameter `host`
    - Modify the type `string` -> `array` of the request parameter `instances`
    - Modify the type `string` -> `array` of the request parameter `hosts`
  - Changes of the interface `ListQpsTimeline`:
    - Modify the type `string` -> `array` of the request parameter `instances`
    - Modify the type `string` -> `array` of the request parameter `hosts`
  - Modify the type `string` -> `array` of the request parameter `instances` of the interface `ListBandwidthTimeline`
  - Changes of the interface `ListTopAbnormal`:
    - Modify the type `string` -> `array` of the request parameter `instances`
    - Modify the type `string` -> `array` of the request parameter `hosts`
  - Changes of the interface `ListOverviewsClassification`:
    - Modify the type `string` -> `array` of the request parameter `instances`
    - Modify the type `string` -> `array` of the request parameter `hosts`
  - Add the response parameters `geoip_enable`, `load_balance_enable`, `ipv6_protection_enable`, `policy_sharing_enable`, `ip_group`, `robot_action_enable`, `http2_enable`, `timeout_config_enable` to the interface `ShowConsoleConfig`
  - Add the response parameter `producer` to the interface `CreateValueList`
  - Modify the type `string` -> `enum` of the response parameter `type` of the interface `ListValueList`
  - Remove the response parameter `timestamp` from the interface `UpdateValueList`
  - Add the response parameter `payload_location` to the interface `ListEvent`
  - Changes of the interface `CreateHost`:
    - Add the request parameters `web_tag`, `exclusive_ip`, `paid_type`, `lb_algorithm`, `weight`
    - Add the response parameters `lb_algorithm`, `web_tag`, `block_page`, `extend`, `weight`, `ipv6`
  - Changes of the interface `ListHost`:
    - Add the response parameters `region`, `web_tag`, `ipv6`
    - Remove the response parameter `timeout_config`
  - Modify the type `string` -> `enum` of the response parameter `back_protocol` of the interface `ListHostRoute`
  - Add the response parameters `web_tag`, `ipv6` to the interface `DeleteHost`
  - Changes of the interface `UpdateHost`:
    - Add the request parameters `web_tag`, `exclusive_ip`, `paid_type`, `circuit_breaker`
    - Add the response parameters `projectid`, `extend`, `traffic_mark`, `circuit_breaker`, `access_progress`, `weight`, `ipv6`
    - Remove the request parameter `lb_algorithm`
    - Remove the response parameter `ipv6_enable`
    - Modify the type `enum` -> `string` of the response parameter `protocol`
    - Modify the type `boolean` -> `string` of the response parameter `web_tag`
    - Modify the type `string` -> `enum` of the response parameter `lb_algorithm`
  - Add the response parameters `domainid`, `projectid`, `enterprise_project_id`, `locked`, `tls`, `cipher`, `block_page`, `extend`, `traffic_mark`, `circuit_breaker`, `lb_algorithm`, `web_tag`, `flag`, `description`, `http2_enable`, `access_progress`, `weight` to the interface `ShowHost`
  - Add the response parameters `robot_action`, `modulex_options` to the interface `CreatePolicy`
  - Add the response parameters `robot_action`, `modulex_options`, `hosts` to the interface `ListPolicy`
  - Add the response parameters `robot_action`, `modulex_options` to the interface `DeletePolicy`
  - Add the response parameters `robot_action`, `modulex_options`, `hosts` to the interface `UpdatePolicyProtectHost`
  - Changes of the interface `UpdatePolicy`:
    - Add the request parameters `level`, `full_detection`, `robot_action`, `modulex_options`, `hosts`, `bind_host`, `extend`
    - Add the response parameters `robot_action`, `modulex_options`
  - Add the response parameters `robot_action`, `modulex_options`, `hosts` to the interface `ShowPolicy`
  - Add the enum values `custom`, `ignore` to the request parameter `ruletype` to the interface `UpdatePolicyRuleStatus`
  - Changes of the interface `CreateWhiteblackipRule`:
    - Add the request parameter `ip_group_id`
    - Add the response parameters `name`, `ip_group`, `status`, `description`
    - The request parameter `addr` changed to not required
  - Add the response parameters `name`, `ip_group` to the interface `ListWhiteblackipRule`
  - Add the response parameter `ip_group` to the interface `DeleteWhiteBlackIpRule`
  - Changes of the interface `UpdateWhiteblackipRule`:
    - Add the request parameter `ip_group_id`
    - Add the response parameters `name`, `ip_group`
    - The request parameter `addr` changed to not required
  - Add the response parameters `timestamp`, `status`, `description` to the interface `CreatePrivacyRule`
  - Add the response parameter `description` to the interface `ListPrivacyRule`
  - Add the response parameters `timestamp`, `status`, `description` to the interface `UpdatePrivacyRule`
  - Changes of the interface `CreateGeoipRule`:
    - Add the request parameters `name`, `status`
    - Add the response parameters `name`, `status`
  - Add the response parameters `name`, `status` to the interface `ListGeoipRule`
  - Add the response parameters `name`, `status` to the interface `DeleteGeoipRule`
  - Changes of the interface `UpdateGeoipRule`:
    - Add the request parameter `name`
    - Add the response parameter `name`
  - Remove the response parameters `content`, `key` from the interface `ListCertificates`
  - Changes of the interface `ListCompositeHosts`:
    - Add the response parameters `hostid`, `web_tag`, `access_progress`, `premium_waf_instances`, `description`, `exclusive_ip`, `region`
    - Remove the response parameters `pci_dss`, `pci_3ds`, `cname`, `is_dual_az`, `ipv6`
  - Changes of the interface `ShowCompositeHost`:
    - Add the response parameters `hostid`, `web_tag`, `access_progress`, `premium_waf_instances`, `description`, `exclusive_ip`, `region`
    - Remove the response parameters `pci_dss`, `pci_3ds`, `cname`, `is_dual_az`, `ipv6`
  - Changes of the interface `CreatePremiumHost`:
    - Add the request parameters `block_page`, `description`, `weight`
    - Add the response parameters `server`, `proxy`, `locked`, `timestamp`, `tls`, `cipher`, `extend`, `flag`, `description`, `enterprise_project_id`, `protect_status`, `access_status`, `block_page`
    - Modify the type `string` -> `enum` of the response parameter `protocol`
  - Changes of the interface `ListPremiumHost`:
    - Add the response parameters `extend`, `region`, `description`, `web_tag`, `hostid`
    - Remove the response parameters `mode`, `pool_ids`
  - Changes of the interface `DeletePremiumHost`:
    - Add the response parameters `extend`, `description`, `web_tag`, `host_id`
    - Remove the response parameters `mode`, `pool_ids`
  - Changes of the interface `UpdatePremiumHost`:
    - Add the response parameters `description`, `projectid`, `enterprise_project_id`, `web_tag`, `lb_algorithm`, `access_progress`, `weight`
    - Remove the request parameters `flag`, `extend`
    - Remove the response parameters `mode`, `pool_ids`, `project_id`, `access_code`
  - Changes of the interface `ShowPremiumHost`:
    - Add the response parameters `description`, `projectid`, `enterprise_project_id`, `web_tag`, `access_progress`, `weight`
    - Remove the response parameters `mode`, `pool_ids`, `project_id`, `access_code`
  - Changes of the interface `UpdateCertificate`:
    - Add the request parameters `content`, `key`
    - The request parameter `name` changed to required

# 3.0.102 2022-08-08

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interfaces:
    - `UpdateSqlFilterControl`
    - `ShowSqlFilterControl`
    - `SetSqlFilterRule`
    - `ShowSqlFilterRule`
    - `DeleteSqlFilterRule`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.101 2022-08-02

### HuaweiCloud SDK CCM

- _Features_
  - Support the interface `RevokeCertificateAuthority`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `extended_key_usage` to the interface `CreateCertificate`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `flavors` to the interface `ShowGaussMySqlFlavors`
  - Add the response parameter `instance` to the interface `ShowGaussMySqlInstanceInfo`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the interface `UpgradeDbVersion`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `patch_available` to the interface `ListInstances`

### HuaweiCloud SDK Image

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `language` from the interface `RunImageDescription`

### HuaweiCloud SDK Live

- _Features_
  - Support the interface `CreateRecordIndex`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interfaces `CreateProjectDomain`, `ListProjectDomains`, `UpdateProjectDomain`, `CancelProjectDomain`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `auto` to the request parameter `audio_format` to the interface `RecognizeShortAudio`

# 3.0.100 2022-07-28

### HuaweiCloud SDK CBS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `CreateTbSession`, `ExecuteTbSession`, `DeleteTbSession`
  - Modify the type `string` -> `int32` of the request parameter `top` of the interface `CollectHotQuestions`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `db_type`, `db_type`, `key`, `value`, `key`, `value` changed to not required of the interface `BatchCreateJobs`
  - The request parameter `id`, `object_type`, `object_name` changed to not required of the interface `BatchSetObjects`
  - The request parameter `name`, `alarm_to_user`, `db_type`, `db_type`, `node_type`, `engine_type`, `net_type`, `store_db_info`, `key`, `value` changed to not required of the interface `BatchUpdateJob`
  - The response parameter `db_type`, `db_type`, `db_type`, `db_type` changed to not required of the interface `BatchListJobDetails`
  - The request parameter `id`, `select` changed to not required of the interface `BatchChangeData`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interfaces `ShowDedicatedResourceInfo`, `SetGaussMySqlProxyWeight`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `proxy`, `master_node`, `readonly_nodes` to the interface `ShowGaussMySqlProxy`
  - Add the response parameter `proxy_list` to the interface `ShowGaussMySqlProxyList`
  - Add the response parameter `proxy_flavor_groups` to the interface `ShowGaussMySqlProxyFlavors`
  - Changes of the interface `ShowGaussMySqlBackupList`:
    - Add the enum values `BUILDING`, `COMPLETED`, `FAILED`, `AVAILABLE` to the response parameter `status`
    - Add the enum values `auto`, `manual` to the response parameter `type`
    - Add the enum values `0`, `1`, `2` to the response parameter `backup_level`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateInstance`:
    - Add the request parameters `period_type`, `period_num`, `is_auto_renew`, `is_auto_pay`
    - Add the enum values `prePaid` to the request parameter `charge_mode`
  - Add the request parameter `is_auto_pay` to the interface `RunInstanceAction`
  - Changes of the interface `CreateRestoreInstance`:
    - Add the request parameters `period_type`, `period_num`, `is_auto_renew`, `is_auto_pay`
    - Add the enum values `prePaid` to the request parameter `charge_mode`
  - Modify the type `string` -> `boolean` of the request parameter `is_auto_pay` of the interface `ResizeInstanceFlavor`

### HuaweiCloud SDK GSL

- _Features_
  - Support the interface `ShowMonthUsages`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK KMS

- _Features_
  - Support the following interfaces：
    - `ListKeyStores`
    - `CreateKeyStore`
    - `ShowKeyStore`
    - `DeleteKeyStore`
    - `EnableKeyStore`
    - `DisableKeyStore`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `keystore_id` to the interface `CreateKey`
  - Add the response parameters `keystore_id`, `key_label` to the interface `ListKeys`
  - Add the response parameters `keystore_id`, `key_label` to the interface `ListKeyDetail`
  - Add the response parameters `keystore_id`, `key_label` to the interface `ListKmsByTags`

### HuaweiCloud SDK NLP

- _Features_
  - Support the interface `RunConstituencyParser`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.99 2022-07-21

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `int32` of the response parameter `status` of the interface `ListLatelyApiStatisticsV2`

### HuaweiCloud SDK CES

- _Features_
  - Support the following interfaces：
    - `ListAlarmRules`
    - `CreateAlarmRules`
    - `BatchDeleteAlarmRules`
    - `BatchEnableAlarmRules`
    - `ListAlarmRuleResources`
    - `DeleteAlarmRuleResources`
    - `AddAlarmRuleResources`
    - `ListAlarmRulePolicies`
    - `UpdateAlarmRulePolicies`
    - `ListAgentDimensionInfo`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListAlarmHistories`:
    - Add the response parameter `datapoints`
    - Remove the response parameters `data_points`, `type`, `notification_list`, `type`, `notification_list`
    - Modify the type `string` -> `enum` of the response parameter `status`
    - Modify the type `int32` -> `enum` of the response parameter `level`
    - Modify the type `string` -> `enum` of the response parameter `type`
    - Modify the type `integer` -> `enum` of the response parameter `period`
    - Modify the type `float` -> `double` of the response parameter `value`
    - Modify the type `integer` -> `enum` of the response parameter `suppress_duration`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interface `ShowInstanceStatusInfo`
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameters `instance_user_domain_name`, `instance_user_name` from the interface `CreateInstance`
  - Remove the request parameters `instance_user_domain_name`, `instance_user_name` from the interface `CreateInstanceBy3rd`

### HuaweiCloud SDK HSS

- _Features_
  - Support the interfaces:
    - `ListHostStatus`
    - `ListPasswordComplexity`
    - `ListRiskConfigCheckRules`
    - `ListRiskConfigHosts`
    - `ListRiskConfigs`
    - `ListSecurityEvents`
    - `ListVulnerabilities`
    - `ListWeakPasswordUsers`
    - `ShowCheckRuleDetail`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Image

- _Features_
  - Support the interface `RunImageDescription`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `security_group_rules_links` to the interface `NeutronListSecurityGroupRules`

# 3.0.98 2022-07-14

### HuaweiCloud SDK Core

- _Features_
  - Support federal authentication
  - Support authentication management
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VCM

- _Features_
  - Support the service `Video Content Moderation`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `effective_tag_pairs`, `cost_unit_pairs` to the interface `ListCustomerBillsMonthlyBreakDown`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `tls_version` to the interface `UpdateDomainFullConfig`
  - Add the response parameter `tls_version` to the interface `ShowDomainFullConfig`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `tags`, `cpu_type` to the interface `ShowInstance`

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `date-time` -> `string` of the response parameter `create_time` of the interface `ListPublicips`
  - Modify the type `date-time` -> `string` of the response parameter `create_time` of the interface `ShowPublicip`

### HuaweiCloud SDK Image

- _Features_
  - Support the interfaces `RunImageMediaTagging`, `RunImageMainObjectDetection`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `port_filter`, `ovs_hybrid_plug` to the interface `ListPorts`
  - Add the response parameters `port_filter`, `ovs_hybrid_plug` to the interface `UpdatePort`
  - Add the response parameters `port_filter`, `ovs_hybrid_plug` to the interface `ShowPort`
  - Add the response parameter `remote_address_group_id` to the interface `CreateSecurityGroup`
  - Add the response parameter `remote_address_group_id` to the interface `ListSecurityGroups`
  - Add the response parameter `remote_address_group_id` to the interface `ShowSecurityGroup`
  - Add the response parameter `remote_address_group_id` to the interface `ListSecurityGroupRules`
  - Add the response parameter `remote_address_group_id` to the interface `ShowSecurityGroupRule`
  - Add the response parameter `remote_address_group_id` to the interface `NeutronListSecurityGroups`
  - Add the response parameter `remote_address_group_id` to the interface `NeutronUpdateSecurityGroup`
  - Add the response parameter `remote_address_group_id` to the interface `NeutronShowSecurityGroup`
  - Add the response parameter `remote_address_group_id` to the interface `NeutronListSecurityGroupRules`
  - Add the response parameter `remote_address_group_id` to the interface `NeutronShowSecurityGroupRule`

# 3.0.97 2022-07-07

### HuaweiCloud SDK APM

- _Features_
  - Support the interfaces `SearchApplication`, `SaveMonitorItemConfig`, `ListEnvMonitorItem`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CCE

- _Features_
  - Support the interfaces `UpdateClusterEip`, `ShowClusterEndpoints`, `ShowVersion`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListNodes`:
    - Add the response parameters `isStatic`, `privateIPv6IP`
    - The response parameter `key`, `effect` changed to required
  - Changes of the interface `CreateNode`:
    - Add the request parameter `isStatic`
    - The request parameter `key`, `effect` changed to required
  - Changes of the interface `ShowNode`:
    - Add the response parameters `isStatic`, `privateIPv6IP`
    - The response parameter `key`, `effect` changed to required
  - Changes of the interface `DeleteNode`:
    - Add the response parameters `isStatic`, `privateIPv6IP`
    - The response parameter `key`, `effect` changed to required
  - Changes of the interface `UpdateNode`:
    - Add the response parameters `isStatic`, `privateIPv6IP`
    - The response parameter `key`, `effect` changed to required
  - The request parameter `key`, `effect` changed to required of the interface `AddNode`
  - The request parameter `key`, `effect` changed to required of the interface `ResetNode`
  - Changes of the interface `ListNodePools`:
    - Add the response parameter `isStatic`
    - The response parameter `key`, `effect` changed to required
  - Changes of the interface `CreateNodePool`:
    - Add the request parameter `isStatic`
    - The request parameter `key`, `effect` changed to required
  - Changes of the interface `ShowNodePool`:
    - Add the response parameter `isStatic`
    - The response parameter `key`, `effect` changed to required
  - Changes of the interface `DeleteNodePool`:
    - Add the response parameter `isStatic`
    - The response parameter `key`, `effect` changed to required
  - Changes of the interface `UpdateNodePool`:
    - Add the response parameter `isStatic`
    - The request parameter `key`, `effect` changed to required
    - The response parameter `key`, `effect` changed to required

### HuaweiCloud SDK CloudRTC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `filling_policy` to the interface `CreateMixJob`
  - Changes of the interface `UpdateMixJob`:
    - Add the request parameter `filling_policy`
    - Add the response parameter `filling_policy`
  - Add the response parameter `filling_policy` to the interface `ShowMixJob`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `CREATING` from the interface `ListClustersDetails`
  - Remove the response parameter `CREATING` from the interface `ShowClusterDetail`
  - Add the request parameter `unBindPublicReq` to the interface `UpdateUnbindPublic`
  - Changes of the interface `ListYmlsJob`:
    - Add the response parameter `configurations`
    - Remove the response parameter `configList`
  - Changes of the interface `ListYmls`:
    - Add the response parameter `configurations`
    - Remove the response parameter `configList`

### HuaweiCloud SDK CTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateNotification`:
    - Add the request parameter `filter`
    - Add the response parameter `filter`
  - Add the request parameter `filter` to the interface `CreateNotification`
  - Add the response parameter `filter` to the interface `ListNotifications`

### HuaweiCloud SDK ELB

- _Features_
  - Support the interfaces `ListMasterSlavePools`, `CreateMasterSlavePool`, `ShowMasterSlavePool`, `DeleteMasterSlavePool`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListSystemSecurityPolicies`:
    - Modify the type `array` -> `string` of the response parameter `protocols`
    - Modify the type `array` -> `string` of the response parameter `ciphers`
  - Add the request parameter `X-Auth-Token` to the interface `ListQuotaDetails`
  - Add the request parameter `public_border_group` to the interface `ListAvailabilityZones`
  - Changes of the interface `CreateLoadBalancer`:
    - Add the request parameters `id`, `global_eip_ids`
    - Remove the request parameter `min_l4_flavor_id`
    - The request parameter `X-Auth-Token` changed to required
  - Changes of the interface `ListLoadBalancers`:
    - Add the response parameters `global_eips`, `public_border_group`
    - Remove the response parameter `min_l4_flavor_id`
    - The request parameter `X-Auth-Token` changed to required
  - Changes of the interface `UpdateLoadBalancer`:
    - Add the request parameter `cloud_service_console_url`
    - Add the response parameters `global_eips`, `public_border_group`
    - Remove the request parameter `min_l4_flavor_id`
    - Remove the response parameter `min_l4_flavor_id`
  - Changes of the interface `ShowLoadBalancer`:
    - Add the response parameters `global_eips`, `public_border_group`
    - Remove the response parameter `min_l4_flavor_id`
  - Add the request parameter `X-Auth-Token` to the interface `ChangeLoadbalancerChargeMode`
  - Remove the request parameters `enc_certificate`, `enc_private_key` from the interface `CreateCertificate`
  - Remove the response parameters `enc_certificate`, `enc_private_key` from the interface `ListCertificates`
  - Changes of the interface `UpdateCertificate`:
    - Remove the request parameters `enc_certificate`, `enc_private_key`
    - Remove the response parameters `enc_certificate`, `enc_private_key`
  - Remove the response parameters `enc_certificate`, `enc_private_key` from the interface `ShowCertificate`
  - Add the request parameter `quic_config` to the interface `CreateListener`
  - Add the response parameter `quic_config` to the interface `ListListeners`
  - Changes of the interface `UpdateListener`:
    - Add the request parameter `quic_config`
    - Add the response parameter `quic_config`
  - Add the response parameter `quic_config` to the interface `ShowListener`
  - Add the request parameters `vpc_id`, `type` to the interface `CreatePool`
  - Changes of the interface `ListPools`:
    - Add the request parameters `vpc_id`, `type`
    - Add the response parameters `created_at`, `updated_at`, `vpc_id`, `type`
  - Changes of the interface `UpdatePool`:
    - Add the request parameters `X-Auth-Token`, `vpc_id`, `type`
    - Add the response parameters `created_at`, `updated_at`, `vpc_id`, `type`
  - Add the response parameters `created_at`, `updated_at`, `vpc_id`, `type` to the interface `ShowPool`
  - Modify the type `enum` -> `string` of the request parameter `project_id` of the interface `CreateMember`
  - Changes of the interface `ListMembers`:
    - Add the response parameters `status`, `loadbalancers`, `created_at`, `updated_at`
    - Remove the request parameter `instance_id`
  - Add the response parameters `status`, `loadbalancers`, `created_at`, `updated_at` to the interface `UpdateMember`
  - Add the response parameters `status`, `loadbalancers`, `created_at`, `updated_at` to the interface `ShowMember`
  - Add the response parameters `status`, `loadbalancers`, `created_at`, `updated_at` to the interface `ListAllMembers`
  - Add the response parameters `created_at`, `updated_at` to the interface `ListHealthMonitors`
  - Add the response parameters `created_at`, `updated_at` to the interface `UpdateHealthMonitor`
  - Add the response parameters `created_at`, `updated_at` to the interface `ShowHealthMonitor`
  - Add the request parameter `redirect_pools_config` to the interface `CreateL7Policy`
  - Add the response parameters `redirect_pools_config`, `created_at`, `updated_at` to the interface `ListL7Policies`
  - Changes of the interface `UpdateL7Policy`:
    - Add the request parameter `redirect_pools_config`
    - Add the response parameters `redirect_pools_config`, `created_at`, `updated_at`
  - Add the response parameters `redirect_pools_config`, `created_at`, `updated_at` to the interface `ShowL7Policy`
  - Add the request parameter `X-Auth-Token` to the interface `BatchUpdatePoliciesPriority`
  - Add the response parameters `created_at`, `updated_at` to the interface `ListL7Rules`
  - Add the response parameters `created_at`, `updated_at` to the interface `UpdateL7Rule`
  - Add the response parameters `created_at`, `updated_at` to the interface `ShowL7Rule`
  - Changes of the interface `UpdateIpList`:
    - Remove the request parameters `name`, `ip_list`, `description`
    - The request parameter `X-Auth-Token` changed to required
  - Changes of the interface `BatchDeleteIpList`:
    - Add the request parameter `BatchDeleteIpListRequestBody`
    - Remove the request parameter `BatchDeleteIpGroupIpListRequestBody`
    - The request parameter `X-Auth-Token` changed to required
  - Changes of the interface `BatchCreateMembers`:
    - Add the request parameter `BatchCreateMembersRequestBody`
    - Add the response parameter `status`
    - Remove the request parameter `BatchCreateMemberRequestBody`
  - Changes of the interface `BatchDeleteMembers`:
    - Add the request parameter `BatchDeleteMembersRequestBody`
    - Remove the request parameter `BatchDeleteMemberRequestBody`
  - Changes of the interface `UpdateLogtank`:
    - Add the request parameter `UpdateLogtankRequestBody`
    - Remove the request parameter `logtank`

### HuaweiCloud SDK IoTEdge

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces:
    - `CreateAccessCode`
    - `ShowProtocolMappings`
    - `UploadProtocolMappings`
    - `BatchUpdateConfigs`
    - `ShowExternalEntity`
  - Add the enum values `COMPOSITE_APPLICATION`, `DATA_COLLECTION` to the request parameter `function_type` to the interface `CreateEdgeApp`
  - Add the response parameters `sdk_version`, `deploy_multi_instance` to the interface `BatchListEdgeAppVersions`
  - Add the request parameters `sdk_version`, `deploy_multi_instance`, `ext_devices`, `tcp_socket`, `period_seconds`, `failure_threshold`, `tcp_socket`, `period_seconds`, `failure_threshold` to the interface `CreateEdgeApplicationVersion`
  - Changes of the interface `UpdateEdgeApplicationVersion`:
    - Add the request parameters `deploy_multi_instance`, `sdk_version`, `ext_devices`, `tcp_socket`, `period_seconds`, `failure_threshold`, `tcp_socket`, `period_seconds`, `failure_threshold`
    - Add the response parameters `sdk_version`, `deploy_multi_instance`
    - The request parameter `arch` changed to not required
  - Add the response parameters `deploy_multi_instance`, `sdk_version`, `tcp_socket`, `period_seconds`, `failure_threshold`, `tcp_socket`, `period_seconds`, `failure_threshold`, `ext_devices` to the interface `ShowEdgeApplicationVersion`
  - Add the response parameters `sdk_version`, `deploy_multi_instance` to the interface `UpdateEdgeApplicationVersionState`
  - Add the request parameters `edge_node_id`, `verify_code`, `time_out`, `arch`, `base_path`, `hardware_model` to the interface `CreateEdgeNode`
  - Add the response parameters `ha_config`, `hardware_model` to the interface `ShowEdgeNode`
  - Add the request parameter `CreateInstallCmdRequestBody` to the interface `CreateInstallCmd`
  - Changes of the interface `BatchListModules`:
    - Add the response parameters `control_status`, `container_settings`
    - Add the enum values `DELETE_SUCCESS`, `STOPPED` to the response parameter `state`
    - Add the enum values `GATEWAY_MANAGER`, `COMPOSITE_APPLICATION`, `DATA_COLLECTION` to the response parameter `function_type`
  - Add the request parameters `module_name`, `container_settings` to the interface `CreateModule`
  - Changes of the interface `UpdateModule`:
    - Add the request parameters `module_name`, `container_settings`
    - Add the response parameter `control_status`
    - The request parameter `app_version` changed to not required
    - Add the enum values `DELETE_SUCCESS`, `STOPPED` to the response parameter `state`
    - Add the enum values `GATEWAY_MANAGER`, `COMPOSITE_APPLICATION`, `DATA_COLLECTION` to the response parameter `function_type`
  - Changes of the interface `ShowModule`:
    - Add the response parameters `control_status`, `container_settings`
    - Add the enum values `DELETE_SUCCESS`, `STOPPED` to the response parameter `state`
    - Add the enum values `GATEWAY_MANAGER`, `COMPOSITE_APPLICATION`, `DATA_COLLECTION` to the response parameter `function_type`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `title` to the interface `RecognizeVatInvoice`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `SetSensitiveSlowLog`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RMS

- _Features_
  - Support the interface `ListSchemas`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `chinese_16k_travel` to the request parameter `property` to the interface `RecognizeShortAudio`
  - Add the enum values `chinese_16k_media` to the request parameter `property` to the interface `PushTranscriberJobs`
  - Add the response parameter `audio_duration` to the interface `CollectTranscriberJob`
  - Add the enum values `chinese_huaxiaomei_common`, `chinese_huaxiaofei_common` to the request parameter `property` to the interface `RunTts`

# 3.0.96 2022-06-30

### HuaweiCloud SDK UGO

- _Features_
  - Support `Database and Application Migration` service.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `mobile_phone` changed to required of the interface `SendVerificationMessageCode`

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `email` changed to required of the interface `SendVerificationMessageCode`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `cache_url_parameter_filter` to the interface `ShowDomainFullConfig`
  - Add the request parameter `cache_url_parameter_filter` to the interface `UpdateDomainFullConfig`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interface `UploadExtensionFile`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DNS

- _Features_
  - Support the interfaces `CreateRecordSetWithBatchLines`, `BatchUpdateRecordSetWithLine`, `BatchDeleteRecordSetWithLine`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `records` changed to not required of the interface `CreateRecordSetWithLine`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the interface `UpdateFunctionMaxInstanceConfig`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `lb_port` to the interface `ListInstances`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `total_count` to the interface `ListComponentInfos`

### HuaweiCloud SDK IEF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateTag`:
    - Add the request parameter `CreateTagRequestBody`
    - Remove the request parameter `tag`
  - Add the request parameters `sort`, `state` to the interface `ListEdgeNodes`

### HuaweiCloud SDK OCR

- _Features_
  - Support the interfaces `RecognizeHkIdCard`, `RecognizeCambodianIdCard`, `RecognizeExitEntryPermit`, `RecognizeMainlandTravelPermit`
- _Bug Fix_
  - None
- _Change_
  - Modify the type `int32` -> `float` of the response parameter `direction` of the interface `RecognizeGeneralText`

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interfaces `CreateProjectModule`, `ListProjectModules`, `UpdateProjectModule`, `DeleteProjectModule`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK UGO

- _Features_
  - Support the following interfaces:
    - `ListQuotas`
    - `RunSqlConversion`
    - `ListEvaluationProjects`
    - `CreateEvaluationProject`
    - `ShowEvaluationProjectStatus`
    - `ShowEvaluationProjectDetail`
    - `ConfirmTargetDbType`
    - `DeleteEvaluationProject`
    - `ListMigrationProjects`
    - `CreateMigrationProject`
    - `ShowMigrationProjectStatus`
    - `CheckPermission`
    - `ListPermissionCheckResult`
    - `ShowMigrationProjectDetail`
    - `CommitSyntaxConversion`
    - `ListSyntaxConversionProgress`
    - `CommitVerification`
    - `ListVerificationProgress`
    - `DownloadFailureReport`
    - `DeleteMigrationProject`
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `MigrateSqlStatement`
  - Changes of the interface `ListApiVersions`:
    - Add the request parameter `X-Auth-Token`
    - The response parameter `id`, `links`, `version`, `status`, `updated` changed to required
  - Changes of the interface `ShowApiVersionInfo`:
    - Add the request parameter `X-Auth-Token`
    - The response parameter `id`, `links`, `version`, `status`, `updated` changed to required

### HuaweiCloud SDK WAF

- _Features_
  - Support the interface `ListOverviewsClassification`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `host` to the interface `ListStatistics`
  - Add the response parameter `timeout_config` to the interface `ListHost`
  - Add the response parameter `timeout_config` to the interface `ShowHost`
  - Changes of the interface `UpdateHost`:
    - Add the request parameters `block_page`, `traffic_mark`, `flag`, `extend`, `http2_enable`, `ipv6_enable`, `lb_algorithm`, `timeout_config`
    - Add the response parameters `http2_enable`, `ipv6_enable`, `lb_algorithm`, `timeout_config`
  - Changes of the interface `UpdatePremiumHost`:
    - Add the request parameters `mode`, `locked`, `protect_status`, `access_status`, `timestamp`, `pool_ids`, `block_page`, `traffic_mark`, `flag`, `extend`, `circuit_breaker`, `timeout_config`
    - Add the response parameter `timeout_config`
  - Add the response parameter `timeout_config` to the interface `ShowPremiumHost`

# 3.0.95 2022-06-25

### HuaweiCloud SDK Core

- _Features_
  - None
- _Bug Fix_
  - Fix the problem that the cloud service package depended on the lower version of `huaweicloudsdkcore` causing `ModuleNotFoundError`
- _Change_
  - None

### HuaweiCloud SDK CodeCheck

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `cyclomatic_complexity_per_file`, `file_duplication_ratio` to the interface `ShowTaskDetail`

### HuaweiCloud SDK DDS

- _Features_
  - Support the following interfaces:
    - `ShowEntityConfiguration`
    - `UpdateEntityConfiguration`
    - `ShowConfigurationParameter`
    - `UpdateConfigurationParameter`
    - `DeleteConfiguration`
    - `ListConfigurations`
    - `CreateConfiguration`
    - `SwitchConfiguration`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `configurations`, `charge_info` to the interface `CreateInstance`
  - Changes of the interface `ResizeInstanceVolume`:
    - Add the request parameter `is_auto_pay`
    - Add the response parameter `order_id`
  - Changes of the interface `AddShardingNode`:
    - Add the request parameter `is_auto_pay`
    - Add the response parameter `order_id`
  - Changes of the interface `ResizeInstance`:
    - Add the request parameter `is_auto_pay`
    - Add the response parameter `order_id`
  - Add the request parameters `configurations`, `charge_info` to the interface `RestoreNewInstance`

# 3.0.94 2022-06-23

### HuaweiCloud SDK Core

- _Features_
  - Support configuring custom regions
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DLI

- _Features_
  - Support Data Lake Insight service.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CSE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UploadKie`:
    - Add the request parameter `upload_file`
    - Remove the request parameter `UploadFile`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateCluster`:
    - Add the request parameters `httpsEnable`, `authorityEnable`, `adminPwd`
    - The request parameter `availability_zone` changed to required
  - Changes of the interface `ListClustersDetails`:
    - Add the response parameters `publicKibanaResp`, `elbWhiteList`, `publicIp`, `bandwidthSize`, `diskEncrypted`, `backupAvailable`, `enterpriseProjectId`, `ip`
    - Remove the response parameter `enterprise_project_id`
  - Remove the request parameter `X-Auth-Token` from the interface `DeleteCluster`
  - Changes of the interface `ShowClusterDetail`:
    - Add the response parameters `publicKibanaResp`, `elbWhiteList`, `publicIp`, `vpcId`, `subnetId`, `securityGroupId`, `bandwidthSize`, `diskEncrypted`, `backupAvailable`, `enterpriseProjectId`, `period`, `ip`
    - Remove the response parameter `enterprise_project_id`
  - Changes of the interface `ListFlavors`:
    - Add the response parameters `type`, `availableAZ`
  - Changes of the interface `StartVpecp`:
    - Modify the type `string` -> `boolean` of the request parameter `endpointWithDnsName`
  - Changes of the interface `CreateCluster`:
    - Add the request parameter `payInfo`
    - Add the response parameter `cluster`
    - Remove the response parameter `schema`
  - Changes of the interface `RestartCluster`:
    - Add the request parameter `RestartClusterRequestBody`
    - Remove the request parameters `X-Auth-Token`, `RollingRestartReq`

### HuaweiCloud SDK DRS

- _Features_
  - Support the interfaces `ListAvailableZone`, `UpdateTuningParams`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `master_az`, `slave_az` to the interface `BatchCreateJobs`
  - Add the request parameter `slot_name` to the interface `BatchSetPolicy`

### HuaweiCloud SDK ELB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListQuotaDetails`:
    - Add the request parameter `quota_key`
    - Remove the request parameter `type`
  - Changes of the interface `ListListeners`:
    - Add the request parameters `loadbalancer_id`, `connection_limit`, `admin_state_up`, `http2_enable`, `enterprise_project_id`
    - Remove the request parameters `member_timeout`, `client_timeout`, `keepalive_timeout`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `subnet_id` to the interface `ListInstances`
  - Add the request parameter `subnet_id` to the interface `ExpandInstanceNode`

### HuaweiCloud SDK VSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `AuthorizeDomains`:
    - Add the response parameter `usage_notice`
    - Add the enum values `free` to the request parameter `auth_mode`

# 3.0.93 2022-06-19

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - Fix the problem that the response parameter's type of the interface `ListRangeQueryAomPromGet` is incorrect
- _Change_
  - None

### HuaweiCloud SDK OCR

- _Features_
  - Support the interface `RecognizeIdDocument`
- _Bug Fix_
  - None
- _Change_
  - None
  
### HuaweiCloud SDK RMS

- _Features_
  - Support the interface `RunQuery`, `CreateStoredQuery`, `ListStoredQueries`, `ShowStoredQuery`, `UpdateStoredQuery`, `DeleteStoredQuery`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `domain_id`, `project_id`, `region`, `company_name`, `product_name` changed to required of the interface `CheckProductHealthy`
  - Changes of the interface `ImportEvents`:
    - The request parameter `type`, `domain_id`, `business`, `checkitem_id`, `checkpoint_id`, `spec_id`, `patch_id` changed to required
    - The request parameter `type`, `domain_id`, `product_feature`, `arrive_time`, `verification_state` changed to not required

### HuaweiCloud SDK VSS

- _Features_
  - Support the interfaces `ShowReportStatus`, `DownloadTaskReport`, `ExecuteGenerateReport`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.92 2022-06-09

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateCluster`:
    - Add the response parameter `schema`
    - Remove the response parameters `id`, `name`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `enum` of the response parameter `runtime` of the interface `UpdateFunctionCode`
  - Modify the type `string` -> `enum` of the response parameter `runtime` of the interface `ShowFunctionCode`
  - Changes of the interface `UpdateFunctionConfig`:
    - Add the request parameter `domain_names`
    - Add the response parameter `domain_names`
    - Modify the type `string` -> `enum` of the response parameter `runtime`
  - Modify the type `string` -> `enum` of the response parameter `runtime` of the interface `ShowFunctionConfig`
  - Modify the type `string` -> `enum` of the response parameter `runtime` of the interface `CreateFunctionVersion`
  - Add the request parameter `option` to the interface `ListStatistics`
  - Modify the type `string` -> `enum` of the response parameter `runtime` of the interface `CreateDependency`
  - Modify the type `string` -> `enum` of the response parameter `runtime` of the interface `ListDependencies`
  - Modify the type `string` -> `enum` of the response parameter `runtime` of the interface `UpdateDependency`
  - Modify the type `string` -> `enum` of the response parameter `runtime` of the interface `ShowDependency`
  - The request parameter `content` changed to required of the interface `UpdateEvent`
  - Add the request parameter `marker` to the interface `ListFunctionAsyncInvocations`
  - The request parameter `workflow_urns` changed to required of the interface `BatchDeleteWorkflows`
  - The request parameter `name`, `trigger_name`, `trigger_type`, `bucket`, `events`, `prefix`, `suffix`, `start`, `name`, `operation`, `id`, `name`, `type`, `end`, `transition`, `ref_name`, `arguments`, `constants`, `name` changed to required of the interface `CreateWorkflow`
  - The request parameter `input` changed to required of the interface `StartWorkflowExecution`
  - Add the response parameters `node_name`, `execution_id`, `request_id` to the interface `ShowWorkflowExecution`
  - The request parameter `name`, `trigger_name`, `trigger_type`, `bucket`, `events`, `prefix`, `suffix`, `start`, `name`, `operation`, `id`, `name`, `type`, `end`, `transition`, `ref_name`, `arguments`, `constants`, `name` changed to required of the interface `UpdateWorkFlow`
  - Changes of the interface `ShowWorkFlow`:
    - Add the response parameters `lts_group_id`, `lts_stream_id`
    - The response parameter `name`, `trigger_name`, `trigger_type`, `bucket`, `events`, `prefix`, `suffix`, `start`, `name`, `operation`, `id`, `name`, `type`, `end`, `transition`, `ref_name`, `arguments`, `constants`, `name` changed to required
  - The request parameter `input` changed to required of the interface `StartSyncWorkflowExecution`

### HuaweiCloud SDK GSL

- _Features_
  - Support the following interfaces:
    - `BatchSetTags`
    - `ListTags`
    - `CreateTag`
    - `DeleteTag`
    - `BatchSetAttributes`
    - `ListAttributes`
    - `CreateAttribute`
    - `UpdateAttribute`
    - `EnableAttribute`
    - `DisableAttribute`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `tag_id` to the interface `ListSimCards`

### HuaweiCloud SDK Moderation

- _Features_
  - Support the interface `RunTextModeration`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `availabilityZoneId` to the interface `ListClusters`
  - Add the response parameter `availabilityZoneId` to the interface `ShowClusterDetails`
  - Add the response parameters `availability_zone_id`, `tags` to the interface `ListHosts`

# 3.0.91 2022-06-02

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `instance_id` to the interface `ListFlavors`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interface `ChangeGaussMySqlProxySpecification`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Meeting

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `maxAudienceParties`, `expireDate`, `commercialMaxAudienceParties` to the interface `SearchCorpVmr`

### HuaweiCloud SDK NAT

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListNatGateways`:
    - Modify the type `date-time` -> `string` of the request parameter `created_at`
    - Modify the type `date-time` -> `string` of the response parameter `created_at`
  - Modify the type `date-time` -> `string` of the response parameter `created_at` of the interface `UpdateNatGateway`
  - Modify the type `date-time` -> `string` of the response parameter `created_at` of the interface `ShowNatGateway`
  - Changes of the interface `ListNatGatewayDnatRules`:
    - Modify the type `date-time` -> `string` of the request parameter `created_at`
    - Modify the type `date-time` -> `string` of the response parameter `created_at`
  - Modify the type `date-time` -> `string` of the response parameter `created_at` of the interface `UpdateNatGatewayDnatRule`
  - Modify the type `date-time` -> `string` of the response parameter `created_at` of the interface `ShowNatGatewayDnatRule`
  - Changes of the interface `ListNatGatewaySnatRules`:
    - Modify the type `date-time` -> `string` of the request parameter `created_at`
    - Modify the type `date-time` -> `string` of the response parameter `created_at`
  - Modify the type `date-time` -> `string` of the response parameter `created_at` of the interface `UpdateNatGatewaySnatRule`
  - Modify the type `date-time` -> `string` of the response parameter `created_at` of the interface `ShowNatGatewaySnatRule`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `words_block_count`, `words_block_list` to the interface `RecognizeHealthCode`
  - Modify the type `float` -> `object` of the response parameter `confidence` of the interface `RecognizePcrTestRecord`

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the following interfaces:
    - `ListIssueCustomFields`
    - `ListIssuesSfV4`
    - `ListProjectIssuesRecordsV4`
    - `ListWorkitemStatusRecordsV4`
    - `ListWorkitems`
    - `ShowIssuesWrokFlowConfig`
    - `ShowWorkItemWrokflowConfig`
    - `ListAssociatedIssues`
    - `ListAssociatedWikis`
    - `ListIssueAssociatedCommits`
    - `ListAssociatedTestCases`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateIssueV4`:
    - Add the request parameter `new_custom_fields`
    - Add the response parameters `new_custom_fields`, `new_name`
  - Changes of the interface `ListIssuesV4`:
    - Add the request parameter `custom_fields`
    - Add the response parameters `new_custom_fields`, `new_name`
  - Add the response parameters `new_custom_fields`, `new_name` to the interface `ShowIssueV4`
  - Changes of the interface `UpdateIssueV4`:
    - Add the request parameter `new_custom_fields`
    - Add the response parameters `new_custom_fields`, `new_name`
  - Add the response parameters `new_custom_fields`, `new_name` to the interface `ListChildIssuesV4`
  - Changes of the interface `CreateSystemIssueV4`:
    - Add the request parameter `new_custom_fields`
    - Add the response parameters `new_custom_fields`, `new_name`

# 3.0.90 2022-05-26

### HuaweiCloud SDK BCS

- _Features_
  - Support the interfaces `HandleUnionMemberQuitList`, `BatchRemovePeersFromChannel`, `DeleteChannel`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `is_delete_ief`, `is_delete_lightpeer`, `ief_nodes_id` to the interface `DeleteBlockchain`
  - Changes of the interface `CreateNewBlockchain`:
    - Add the request parameter `cluster_platform_type`
    - Remove the request parameters `user_name`, `password`
    - Modify the type `int64` -> `string` of the request parameter `node_flavor`
    - Modify the type `int64` -> `string` of the request parameter `cce_flavor`
    - Modify the type `int64` -> `string` of the request parameter `init_node_pwd`
    - Modify the type `int64` -> `string` of the request parameter `az`
    - Modify the type `int64` -> `string` of the request parameter `cluster_platform_type`
  - Add the request parameter `CreateBlockchainCertByUserNameRequestBody` to the interface `CreateBlockchainCertByUserName`
  - Add the request parameter `file` to the interface `UnfreezeCert`
  - Add the request parameter `file` to the interface `FreezeCert`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `features`, `sub_status` to the interface `ListInstances`
  - Add the response parameters `features`, `transparent_client_ip_enable`, `sub_status` to the interface `ShowInstance`
  - Add the request parameter `execute_immediately` to the interface `ResizeInstance`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `volume_type`, `hw:passthrough` to the interface `AttachServerVolume`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the interfaces `ListComponentInfos`, `SwitchShard`, `ResizeInstanceFlavor`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `rate_limit`, `prefetch_block`, `filesplit_size` from the interface `ShowBackupPolicy`
  - Modify the type `object` -> `string` of the response parameter `memberof` of the interface `ListDbUsers`

### HuaweiCloud SDK KMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ValidateSignature`:
    - Add the response parameter `signature_valid`
    - Remove the response parameter `signature_vaild`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateAomMappingRules`:
    - Add the request parameter `deployments_prefix`
    - Add the response parameter `deployments_prefix`
  - Changes of the interface `UpdateAomMappingRules`:
    - Add the request parameter `deployments_prefix`
    - Add the response parameter `deployments_prefix`
  - Add the response parameter `deployments_prefix` to the interface `ShowAomMappingRules`
  - Add the response parameter `deployments_prefix` to the interface `ShowAomMappingRule`

### HuaweiCloud SDK Moderation

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `ocr_text`, `error_code`, `error_msg` to the interface `RunCheckResult`
  - Changes of the interface `RunImageBatchModeration`:
    - Add the request parameters `moderation_rule`, `ad_categories`, `show_ocr_text`
    - Add the response parameters `ocr_text`, `error_code`, `error_msg`
  - Add the request parameters `moderation_rule`, `ad_categories`, `show_ocr_text` to the interface `RunTaskSumbit`

# 3.0.89 2022-05-19

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `group_id` to the interface `ListEnvironmentVariablesV2`
  - Add the response parameters `update_time`, `create_time`, `id`, `name`, `sign_type`, `sign_key`, `sign_secret`, `sign_algorithm` to the interface `UpdateSignatureKeyV2`
  - Add the request parameter `loadbalancer_provider` to the interface `CreateInstanceV2`
  - Add the response parameter `loadbalancer_provider` to the interface `ListInstancesV2`
  - Add the response parameters `endpoint_service`, `endpoint_services`, `node_ips`, `publicips`, `privateips`, `loadbalancer_provider` to the interface `ShowDetailsOfInstanceV2`
  - Add the response parameters `endpoint_service`, `endpoint_services`, `node_ips`, `publicips`, `privateips`, `loadbalancer_provider` to the interface `UpdateInstanceV2`

### HuaweiCloud SDK CSE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `X-Enterprise-Project-ID` from the interface `ListEngines`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `dry_run` to the interface `ResizeServer`
  - Add the request parameter `dry_run` to the interface `ResizePostPaidServer`
  - Add the request parameter `dry_run` to the interface `AttachServerVolume`

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListClusters`:
    - Add the response parameters `GroupName`, `NodeNum`, `NodeSize`, `NodeSpecId`, `VmProductId`, `VmSpecCode`, `NodeProductId`, `RootVolumeSize`, `RootVolumeProductId`, `RootVolumeType`, `RootVolumeResourceSpecCode`, `RootVolumeResourceType`, `DataVolumeType`, `DataVolumeCount`, `DataVolumeSize`, `DataVolumeProductId`, `DataVolumeResourceSpecCode`, `DataVolumeResourceType`, `GroupName`, `NodeNum`, `NodeSize`, `NodeSpecId`, `VmProductId`, `VmSpecCode`, `NodeProductId`, `RootVolumeSize`, `RootVolumeProductId`, `RootVolumeType`, `RootVolumeResourceSpecCode`, `RootVolumeResourceType`, `DataVolumeType`, `DataVolumeCount`, `DataVolumeSize`, `DataVolumeProductId`, `DataVolumeResourceSpecCode`, `DataVolumeResourceType`
    - Remove the response parameters `groupName`, `nodeNum`, `nodeSize`, `nodeSpecId`, `vmProductId`, `vmSpecCode`, `nodeProductId`, `rootVolumeSize`, `rootVolumeProductId`, `rootVolumeType`, `rootVolumeResourceSpecCode`, `rootVolumeResourceType`, `dataVolumeType`, `dataVolumeCount`, `dataVolumeSize`, `dataVolumeProductId`, `dataVolumeResourceSpecCode`, `dataVolumeResourceType`, `groupName`, `nodeNum`, `nodeSize`, `nodeSpecId`, `vmProductId`, `vmSpecCode`, `nodeProductId`, `rootVolumeSize`, `rootVolumeProductId`, `rootVolumeType`, `rootVolumeResourceSpecCode`, `rootVolumeResourceType`, `dataVolumeType`, `dataVolumeCount`, `dataVolumeSize`, `dataVolumeProductId`, `dataVolumeResourceSpecCode`, `dataVolumeResourceType`
  - Changes of the interface `ShowClusterDetails`:
    - Add the response parameters `GroupName`, `NodeNum`, `NodeSize`, `NodeSpecId`, `VmProductId`, `VmSpecCode`, `NodeProductId`, `RootVolumeSize`, `RootVolumeProductId`, `RootVolumeType`, `RootVolumeResourceSpecCode`, `RootVolumeResourceType`, `DataVolumeType`, `DataVolumeCount`, `DataVolumeSize`, `DataVolumeProductId`, `DataVolumeResourceSpecCode`, `DataVolumeResourceType`, `GroupName`, `NodeNum`, `NodeSize`, `NodeSpecId`, `VmProductId`, `VmSpecCode`, `NodeProductId`, `RootVolumeSize`, `RootVolumeProductId`, `RootVolumeType`, `RootVolumeResourceSpecCode`, `RootVolumeResourceType`, `DataVolumeType`, `DataVolumeCount`, `DataVolumeSize`, `DataVolumeProductId`, `DataVolumeResourceSpecCode`, `DataVolumeResourceType`
    - Remove the response parameters `groupName`, `nodeNum`, `nodeSize`, `nodeSpecId`, `vmProductId`, `vmSpecCode`, `nodeProductId`, `rootVolumeSize`, `rootVolumeProductId`, `rootVolumeType`, `rootVolumeResourceSpecCode`, `rootVolumeResourceType`, `dataVolumeType`, `dataVolumeCount`, `dataVolumeSize`, `dataVolumeProductId`, `dataVolumeResourceSpecCode`, `dataVolumeResourceType`, `groupName`, `nodeNum`, `nodeSize`, `nodeSpecId`, `vmProductId`, `vmSpecCode`, `nodeProductId`, `rootVolumeSize`, `rootVolumeProductId`, `rootVolumeType`, `rootVolumeResourceSpecCode`, `rootVolumeResourceType`, `dataVolumeType`, `dataVolumeCount`, `dataVolumeSize`, `dataVolumeProductId`, `dataVolumeResourceSpecCode`, `dataVolumeResourceType`
  - The request parameter `data_volume_type`, `data_volume_count`, `data_volume_size` changed to required of the interface `UpdateClusterScaling`

### HuaweiCloud SDK VOD

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `M3U8` to the request parameter `video_type` to the interface `UploadMetaDataByUrl`
  - Add the response parameter `sign_url` to the interface `PublishAssets`
  - Add the response parameter `sign_url` to the interface `UnpublishAssets`
  - Add the response parameter `sign_url` to the interface `ShowAssetMeta`
  - Add the response parameter `sign_url` to the interface `ShowAssetDetail`
  - Add the response parameter `sign_url` to the interface `ShowTakeOverTaskDetails`
  - Add the response parameter `sign_url` to the interface `ShowTakeOverAssetDetails`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `neutron:VIP_PORT`, Remove the enum values `network:VIP_PORT` from the response parameter `device_owner` to the interface `ListPorts`
  - Add the enum values `neutron:VIP_PORT`, Remove the enum values `network:VIP_PORT` from the response parameter `device_owner` to the interface `UpdatePort`
  - Add the enum values `neutron:VIP_PORT`, Remove the enum values `network:VIP_PORT` from the response parameter `device_owner` to the interface `ShowPort`

# 3.0.88 2022-05-12

### HuaweiCloud SDK CodeHub

- _Features_
  - Support the interfaces `AddProtectBranchV2`, `AddTagV2`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateTask`:
    - Modify the type `string` -> `array` of the request parameter `bodys`
    - Modify the type `string` -> `object` of the request parameter `data`
    - Modify the type `string` -> `array` of the response parameter `bodys`
    - Modify the type `string` -> `object` of the response parameter `data`
  - Changes of the interface `ShowTask`:
    - Modify the type `string` -> `array` of the response parameter `bodys`
    - Modify the type `string` -> `object` of the response parameter `data`
  - Changes of the interface `UpdateCase`:
    - Modify the type `string` -> `array` of the request parameter `bodys`
    - Modify the type `string` -> `object` of the request parameter `data`
  - Changes of the interface `UpdateTemp`:
    - Modify the type `string` -> `array` of the request parameter `bodys`
    - Modify the type `string` -> `object` of the request parameter `data`

### HuaweiCloud SDK CSS

- _Features_
  - Support the interface `DownloadCert`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `nodes` to the interface `ListClusterDetails`
  - Add the response parameter `nodes` to the interface `ListClusters`

### HuaweiCloud SDK FRS

- _Features_
  - Support the following interfaces:
    - `DetectLiveByUrlIntl`
    - `DetectLiveByFileIntl`
    - `DetectLiveByBase64Intl`
    - `DetectFaceByFileIntl`
    - `DetectFaceByUrlIntl`
    - `DetectFaceByBase64Intl`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the following interfaces:
    - `ListBackups`
    - `CreateManualBackup`
    - `DeleteManualBackup`
    - `ListRestoreTimes`
    - `CreateRestoreInstance`
    - `CreateDatabase`
    - `CreateDbUser`
    - `CreateDatabaseSchemas`
    - `AllowDbPrivileges`
    - `SetDbUserPwd`
    - `ListDatabases`
    - `ListDbUsers`
    - `ListDatabaseSchemas`
    - `ShowBackupPolicy`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListSimCards`:
    - Add the request parameters `min_used_flow`, `max_used_flow`, `min_left_flow`, `max_left_flow`
    - Remove the request parameters `min_flow`, `max_flow`

### HuaweiCloud SDK IAM

- _Features_
  - Support the interface `ShowDomainRoleAssignments`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Moderation

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `RunImageModeration`:
    - Add the request parameter `show_ocr_text`
    - Add the response parameter `ocr_text`

### HuaweiCloud SDK OCR

- _Features_
  - Support the interface `RecognizeHealthCode`
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
  - Changes of the interface `RestoreExistInstance`:
    - Add the request parameter `RestoreExistingInstanceRequestBody`
    - Remove the request parameter `RestoreToExistingInstanceRequest`

### HuaweiCloud SDK RocketMQ

- _Features_
  - Support the service `RocketMQ`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.87 2022-05-05

### HuaweiCloud SDK Moderation

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `byte` -> `string` of the request parameter `image` of the interface `RunImageModeration`

### HuaweiCloud SDK RES

- _Features_
  - Support the interfaces `CreateResIntelligentScene`, `UpdateResIntelligentScene`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateResScene`:
    - Modify the type `int32` -> `int64` of the response parameter `created_at`
    - Modify the type `int32` -> `int64` of the response parameter `update_at`
  - Changes of the interface `ListResScenes`:
    - Modify the type `int32` -> `int64` of the response parameter `created_at`
    - Modify the type `string` -> `int64` of the response parameter `update_at`
  - Changes of the interface `ShowResScene`:
    - Modify the type `int32` -> `int64` of the response parameter `created_at`
    - Modify the type `string` -> `int64` of the response parameter `update_at`

# 3.0.86 2022-04-28

### HuaweiCloud SDK All

- _Features_
  - Support the cloud service collection package `huaweicloudsdkall`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `string` -> `int32` of the request parameter `priority` of the interface `AddOrUpdateServiceDiscoveryRules`
  - Modify the type `string` -> `int32` of the response parameter `priority` of the interface `ListServiceDiscoveryRules`

### HuaweiCloud SDK CSE

- _Features_
  - Support the service `Cloud Service Engine`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DevStar

- _Features_
  - Support the interface `ConfirmDeploymentJob`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `cci` to the interface `CreateDeploymentJobs`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the interfaces `CancelAsyncInvocation`, `StartSyncWorkflowExecution`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListFunctionStatistics`:
    - Modify the type `int32` -> `int64` of the response parameter `timestamp`
    - Modify the type `int32` -> `double` of the response parameter `value`
  - Changes of the interface `ListStatistics`:
    - Modify the type `int32` -> `int64` of the response parameter `timestamp`
    - Modify the type `int32` -> `double` of the response parameter `value`
  - Add the response parameter `enable_async_status_log` to the interface `ListFunctionAsyncInvokeConfig`
  - Add the response parameter `enable_async_status_log` to the interface `ShowFunctionAsyncInvokeConfig`
  - Changes of the interface `UpdateFunctionAsyncInvokeConfig`:
    - Add the request parameter `enable_async_status_log`
    - Add the response parameter `enable_async_status_log`
  - Changes of the interface `CreateWorkflow`:
    - Add the request parameters `mode`, `express_config`
    - Add the enum values `End` to the request parameter `type`
  - Changes of the interface `ShowWorkFlow`:
    - Add the response parameters `mode`, `express_config`
    - Add the enum values `End` to the response parameter `type`
  - Changes of the interface `UpdateWorkFlow`:
    - Add the request parameters `mode`, `express_config`
    - Add the enum values `End` to the request parameter `type`
  - Changes of the interface `ShowTenantMetric`:
    - Add the request parameters `start_time`, `end_time`
    - Modify the type `int32` -> `int64` of the response parameter `timestamp`
    - Modify the type `int32` -> `double` of the response parameter `value`
  - Changes of the interface `ShowWorkFlowMetric`:
    - Add the request parameters `start_time`, `end_time`
    - Modify the type `int32` -> `int64` of the response parameter `timestamp`
    - Modify the type `int32` -> `double` of the response parameter `value`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interface `ShowGaussMySqlProxyList`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateGaussMySqlReadonlyNode`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`
  - Remove the response parameters `size`, `order_id` from the interface `ExpandGaussMySqlInstanceVolume`
  - Changes of the interface `ListGaussMySqlDedicatedResources`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`
  - Add the request parameter `CloseMysqlProxyRequest` to the interface `DeleteGaussMySqlProxy`
  - Changes of the interface `CreateGaussMySqlProxy`:
    - Add the request parameters `proxy_name`, `proxy_mode`, `nodes_read_weight`
    - The request parameter `flavor_ref`, `node_num` changed to required
  - Add the request parameter `proxy_id` to the interface `ExpandGaussMySqlProxy`
  - Changes of the interface `ListGaussMySqlErrorLog`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`
    - The request parameter `node_id` changed to not required
  - Changes of the interface `ListGaussMySqlSlowLog`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`
  - Changes of the interface `ListGaussMySqlConfigurations`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`
  - Changes of the interface `ShowGaussMySqlJobInfo`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`
  - Changes of the interface `ListInstanceTags`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`
  - Changes of the interface `ListProjectTags`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`
  - Changes of the interface `BatchTagAction`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `x-auth-token`

### HuaweiCloud SDK Meeting

- _Features_
  - Support the interface `ShowDepartment`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `deptCodes` to the interface `SearchCorpDir`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - Fix the problem that the response body's type of the interface `RecognizeMyanmarDriverLicense` is incorrect.
- _Change_
  - None

### HuaweiCloud SDK WAF

- _Features_
  - Support the interfaces `DeleteIgnoreRule`, `CreateIgnoreRule`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `id`, `policyid`, `timestamp`, `description`, `status`, `url`, `rule`, `domain`, `url_logic`, `advanced` from the interface `ListIgnoreRule`
  - Add the response parameter `producer` to the interface `ListValueList`
  - Add the response parameters `process_time`, `request_body` to the interface `ListEvent`
  - Changes of the interface `ShowEvent`:
    - Add the response parameters `process_time`, `request_body`
    - Modify the type `string` -> `object` of the response parameter `headers`
    - Modify the type `string` -> `int32` of the response parameter `response_size`
    - Modify the type `string` -> `int64` of the response parameter `response_time`
  - Modify the type `string` -> `enum` of the response parameter `paid_type` of the interface `ListHost`
  - Add the response parameters `flag`, `http2_enable` to the interface `CreateHost`
  - Add the response parameter `protect_status` to the interface `UpdateHostProtectStatus`
  - Modify the type `string` -> `enum` of the response parameter `paid_type` of the interface `DeleteHost`
  - Modify the type `string` -> `enum` of the response parameter `protocol` of the interface `UpdateHost`
  - Add the response parameters `id`, `name`, `level`, `action`, `options`, `full_detection`, `hosts`, `bind_host`, `timestamp`, `extend` to the interface `DeletePolicy`
  - Add the response parameters `id`, `policyid`, `timestamp`, `description`, `status` to the interface `UpdatePolicyRuleStatus`
  - Add the response parameters `id`, `policyid`, `timestamp`, `description`, `status`, `url`, `category`, `index` to the interface `DeletePrivacyRule`
  - Add the response parameter `region` to the interface `DeletePremiumHost`

# 3.0.85 2022-04-21

### HuaweiCloud SDK AS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `iam_agency_name` to the interface `CreateScalingGroup`
  - Add the response parameter `iam_agency_name` to the interface `ListScalingGroups`
  - Add the request parameter `iam_agency_name` to the interface `UpdateScalingGroup`
  - Add the response parameter `iam_agency_name` to the interface `ShowScalingGroup`

### HuaweiCloud SDK BSS

- _Features_
  - Support the interface `ListConsumeSubCustomers`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `sub_service_type_code`, `sub_service_type_name`, `sub_resource_type_code`, `sub_resource_type_name`, `sub_resource_id`, `sub_resource_name` to the interface `ListCustomerBillsMonthlyBreakDown`

### HuaweiCloud SDK CloudDeploy

- _Features_
  - Support the interfaces `ListDeployTasks`, `ListDeployTaskHistoryByDate`, `ShowProjectSuccessRate`, `ListTaskSuccessRate`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `domain_name_info` to the interface `ShowInstance`

### HuaweiCloud SDK DWS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `tags` to the interface `ListClusters`
  - Remove the response parameters `cluster_id`, `size`, `name`, `description`, `finished`, `started`, `id`, `type`, `status` from the interface `ListSnapshotDetails`

### HuaweiCloud SDK IES

- _Features_
  - Support the service `Intelligent EdgeSite`
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
  - Remove the request parameter `restore_all_database` from the interface `RestoreToExistingInstance`

# 3.0.84 2022-04-14

### HuaweiCloud SDK Core

- _Features_
  - Support SK derived authentication
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `sources`, `origin_protocol`, `force_redirect`, `compress` to the interface `UpdateDomainFullConfig`
  - Changes of the interface `ShowDomainFullConfig`:
    - Add the response parameters `sources`, `origin_protocol`, `force_redirect`, `compress`
    - Modify the type `string` -> `int32` of the response parameter `certificate_source`

### HuaweiCloud SDK CloudBuild

- _Features_
  - Support the interface `ShowJobSuccessRatio`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CodeCheck

- _Features_
  - Support the interfaces `ShowTasksRulesets`, `CheckRulesetParameters`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CSMS

- _Features_
  - Support the `Cloud Secret Management Service`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `rename_commands` to the interface `UpdateInstance`

### HuaweiCloud SDK DRS

- _Features_
  - Support the interface `BatchSetSmn`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `X-Language` changed to not required of the interface `ShowQuotas`
  - The request parameter `X-Language` changed to not required of the interface `BatchCreateJobs`
  - The request parameter `X-Language` changed to not required of the interface `BatchValidateConnections`
  - The request parameter `X-Language` changed to not required of the interface `BatchValidateClustersConnections`
  - The request parameter `X-Language` changed to not required of the interface `BatchSetObjects`
  - The request parameter `X-Language` changed to not required of the interface `BatchCheckJobs`
  - The request parameter `X-Language` changed to not required of the interface `BatchCheckResults`
  - Changes of the interface `BatchSetSpeed`:
    - Add the request parameter `is_utc`
    - The request parameter `X-Language` changed to not required
  - The request parameter `X-Language` changed to not required of the interface `BatchShowParams`
  - The request parameter `X-Language` changed to not required of the interface `UpdateParams`
  - The request parameter `X-Language` changed to not required of the interface `BatchStartJobs`
  - The request parameter `X-Language` changed to not required of the interface `BatchRestoreTask`
  - The request parameter `X-Language` changed to not required of the interface `BatchStopJobs`
  - The request parameter `X-Language` changed to not required of the interface `BatchDeleteJobs`
  - Changes of the interface `BatchUpdateJob`:
    - The request parameter `X-Language` changed to not required
    - The request parameter `endpoints`, `protocol` changed to not required
  - The request parameter `X-Language` changed to not required of the interface `BatchResetPassword`
  - The request parameter `X-Language` changed to not required of the interface `BatchSetDefiner`
  - The request parameter `X-Language` changed to not required of the interface `CreateCompareTask`
  - The request parameter `X-Language` changed to not required of the interface `ListCompareResult`
  - The request parameter `X-Language` changed to not required of the interface `BatchListProgresses`
  - Changes of the interface `BatchListJobDetails`:
    - Add the response parameter `is_utc`
    - The request parameter `X-Language` changed to not required
    - Modify the type `string` -> `object` of the response parameter `alarm_notify`
  - Changes of the interface `ShowJobList`:
    - The request parameter `X-Language` changed to not required
    - Modify the type `string` -> `boolean` of the response parameter `billing_tag`
    - Modify the type `string` -> `boolean` of the response parameter `node_newFramework`
  - The request parameter `X-Language` changed to not required of the interface `BatchListJobStatus`
  - The request parameter `X-Language` changed to not required of the interface `BatchChangeData`
  - The request parameter `X-Language` changed to not required of the interface `BatchSwitchover`
  - The request parameter `X-Language` changed to not required of the interface `BatchListRposAndRtos`
  - The request parameter `X-Language` changed to not required of the interface `ShowMonitoringData`
  - The request parameter `X-Language` changed to not required of the interface `BatchListStructProcess`
  - The request parameter `X-Language` changed to not required of the interface `BatchListStructDetail`
  - The request parameter `X-Language` changed to not required of the interface `BatchUpdateUser`
  - The request parameter `X-Language` changed to not required of the interface `ListUsers`
  - Changes of the interface `BatchSetPolicy`:
    - Modify the type `string` -> `boolean` of the request parameter `export_snapshot`
    - The request parameter `X-Language` changed to not required
    - The request parameter `conflict_policy`, `filter_ddl_policy` changed to not required

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `ip_eq` to the interface `ListServersDetails`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `encrypted_user_data` to the interface `UpdateFunctionConfig`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the interfaces `RestartInstance`, `ShowInstanceConfiguration`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateInstance`:
    - Remove the request parameter `solution`
    - The request parameter `sharding_num`, `coordinator_num` changed to not required
  - Add the response parameter `count` to the interface `ListConfigurations`
  - Add the response parameter `total` to the interface `ListFlavors`

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListSimPricePlans`:
    - Modify the type `date` -> `date-time` of the response parameter `create_time`
    - Modify the type `date` -> `date-time` of the response parameter `active_time`
    - Modify the type `date` -> `date-time` of the response parameter `stop_time`

### HuaweiCloud SDK IEC

- _Features_
  - Support the following interfaces:
    - `ListRelatedRoutetables`
    - `ListRoutetables`
    - `CreateRoutetable`
    - `ShowRoutetable`
    - `UpdateRoutetable`
    - `DeleteRoutetable`
    - `AssociateSubnet`
    - `DisassociateSubnet`
    - `ListRoutes`
    - `CreateRoutes`
    - `UpdateRoutes`
    - `DeleteRoutes`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `action`, `priority` to the interface `ListSecurityGroups`
  - Add the response parameters `action`, `priority` to the interface `CreateSecurityGroup`
  - Add the response parameters `action`, `priority` to the interface `ShowSecurityGroup`
  - Add the response parameters `action`, `priority` to the interface `ListSecurityGroupRules`
  - Changes of the interface `CreateSecurityGroupRule`:
    - Add the request parameters `action`, `priority`
    - Add the response parameters `action`, `priority`
  - Add the response parameters `action`, `priority` to the interface `ShowSecurityGroupRule`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateAomMappingRules`:
    - The request parameter `target_log_group_id`, `target_log_group_name`, `target_log_stream_id`, `target_log_stream_name` changed to required
    - The request parameter `container_name` changed to not required
    - The response parameter `target_log_group_id`, `target_log_group_name`, `target_log_stream_id`, `target_log_stream_name` changed to required
    - The response parameter `container_name` changed to not required
  - Changes of the interface `ShowAomMappingRules`:
    - The response parameter `target_log_group_id`, `target_log_group_name`, `target_log_stream_id`, `target_log_stream_name` changed to required
    - The response parameter `container_name` changed to not required
  - Changes of the interface `CreateAomMappingRules`:
    - The request parameter `target_log_group_id`, `target_log_group_name`, `target_log_stream_id`, `target_log_stream_name` changed to required
    - The request parameter `container_name` changed to not required
    - The response parameter `target_log_group_id`, `target_log_group_name`, `target_log_stream_id`, `target_log_stream_name` changed to required
    - The response parameter `container_name` changed to not required
  - Changes of the interface `ShowAomMappingRule`:
    - The response parameter `target_log_group_id`, `target_log_group_name`, `target_log_stream_id`, `target_log_stream_name` changed to required
    - The response parameter `container_name` changed to not required
  - The request parameter `host_id_list` changed to required of the interface `ListHost`
  - The request parameter `host_group_id_list` changed to required of the interface `ListHostGroup`
  - The request parameter `access_config_name_list`, `host_group_name_list`, `log_group_name_list`, `log_stream_name_list` changed to required of the interface `ListAccessConfig`

### HuaweiCloud SDK Moderation

- _Features_
  - Support the interface `RunModerationAudio`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SCM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListCertificates`:
    - Add the request parameters `enterprise_project_id`, `deploy_support`
    - Add the response parameter `enterprise_project_id`
    - The response parameter `id`, `name`, `domain`, `sans`, `signature_algorithm`, `deploy_support`, `type`, `brand`, `expire_time`, `domain_type`, `validity_period`, `status`, `domain_count`, `wildcard_count`, `description`, `total_count` changed to required
  - Changes of the interface `ImportCertificate`:
    - Add the request parameter `enterprise_project_id`
    - The response parameter `certificate_id` changed to required
  - Changes of the interface `ShowCertificate`:
    - Add the response parameter `enterprise_project_id`
    - The response parameter `id`, `status`, `order_id`, `name`, `type`, `brand`, `push_support`, `revoke_reason`, `signature_algorithm`, `issue_time`, `not_before`, `not_after`, `validity_period`, `validation_method`, `domain_type`, `domain`, `sans`, `domain_count`, `wildcard_count` changed to required
  - The response parameter `certificate`, `certificate_chain`, `private_key` changed to required of the interface `ExportCertificate`

### HuaweiCloud SDK SMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `process_trace` to the interface `ListTasks`
  - Add the response parameter `process_trace` to the interface `ShowTask`
  - Add the request parameter `process_trace` to the interface `UpdateTask`
  - Changes of the interface `UpdateTaskSpeed`:
    - Add the request parameters `process_trace`, `compress_rate`
    - The request parameter `migrate_speed` changed to not required

# 3.0.83 2022-04-07

### HuaweiCloud SDK BSS

- _Features_
  - Support the interface `ListStoredValueCards`
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ListSubCustomerDiscounts`, `BatchSetSubCustomerDiscount`
  - Add the response parameters `resource_type_name`, `service_type_name` to the interface `ShowRefundOrderDetails`
  - Add the response parameter `service_type_name` to the interface `ListCustomerOrders`
  - Add the response parameters `service_type_name`, `service_type_name` to the interface `ShowCustomerOrderDetails`
  - Add the response parameters `resource_type_name`, `service_type_name` to the interface `ListPayPerUseCustomerResources`
  - Add the response parameters `service_type_name`, `resource_type_name` to the interface `ListCustomerOnDemandResources`
  - Add the response parameters `cloud_service_type_name`, `resource_type_name` to the interface `ListSubcustomerMonthlyBills`
  - Add the response parameters `cloud_service_type_name`, `resource_type_name`, `period_type` to the interface `ListCustomerselfResourceRecordDetails`
  - Add the response parameters `cloud_service_type_name`, `resource_type_name` to the interface `ListCustomerselfResourceRecords`
  - Add the response parameters `service_type_name`, `resource_type_name` to the interface `ShowCustomerMonthlySum`
  - Changes of the interface `ListCustomerBillsFeeRecords`:
    - Add the request parameters `bill_date_begin`, `bill_date_end`
    - Add the response parameters `service_type_name`, `resource_type_name`
  - Add the response parameters `resource_type_name`, `service_type_name` to the interface `ListUsageTypes`
  - Add the response parameters `service_type_name`, `resource_type_name` to the interface `ListSubCustomerBillDetail`
  - Add the response parameters `service_type_name`, `resource_type_name` to the interface `ListCustomerBillsMonthlyBreakDown`
  - Add the response parameter `service_type_name` to the interface `ListFreeResourceInfos`
  - Add the response parameter `service_type_name` to the interface `ListIncentiveDiscountPolicies`

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameters `kind`, `apiVersion`, `status` from the interface `UpdateNodePool`

### HuaweiCloud SDK DSC

- _Features_
  - Support the following interfaces:
    - `CreateDocWatermarkByAddress`
    - `ShowDocWatermarkByAddress`
    - `ShowImageWatermarkWithImage`
    - `CreateImageWatermarkByAddress`
    - `ShowImageWatermarkByAddress`
    - `ShowImageWatermarkWithImageByAddress`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateImageWatermark`:
    - Add the request parameter `image_watermark`
    - The request parameter `blind_watermark` changed to required

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `price_plan_list` from the interface `StopSimCard`
  - Remove the request parameter `price_plan_list` from the interface `ResetSimCard`

### HuaweiCloud SDK Meeting

- _Features_
  - Support the interface `StartMeeting`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OCR

- _Features_
  - Support the interface `RecognizeWaybillElectronic`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `print_code` to the interface `RecognizeVatInvoice`
  - Changes of the interface `RecognizeVehicleLicense`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`
  - Changes of the interface `RecognizeTaxiInvoice`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`
  - Add the response parameters `type`, `accumulated_scores`, `status`, `generation_date`, `current_time` to the interface `RecognizeDriverLicense`
  - Changes of the interface `RecognizeTrainTicket`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`
  - Changes of the interface `RecognizeBankcard`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ApplyConfigurationAsync`, `UpdateInstanceConfigurationAsync`, `DeleteSqlserverDatabaseEx`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the interfaces `ListConfigurations`, `ListDatastores`, `ListFlavors`, `ListStorageTypes`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateInstance`:
    - Add the request parameter `solution`
    - Add the enum values `centralization_standard` to the request parameter `mode`
    - Add the enum values `ESSD` to the request parameter `type`

# 3.0.82 2022-03-31

### HuaweiCloud SDK CC

- _Features_
  - Support the service `Cloud Connect`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - Support the interface `BatchShowNodesInformation`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.81 2022-03-25

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `responseStatus` to the interface `DeleteserviceDiscoveryRules`
  - Add the response parameter `responseStatus` to the interface `AddOrUpdateServiceDiscoveryRules`

### HuaweiCloud SDK CCM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListCertificateAuthority`:
    - Add the request parameters `sort_key`, `sort_dir`, `X-Auth-Token`
    - Remove the response parameters `ca_id`, `type`, `status`, `path_length`, `freeze_flag`, `gen_mode`, `serial_number`, `create_time`, `delete_time`, `not_before`, `not_after`, `distinguished_name`, `crl_configuration`, `issuer_id`, `issuer_name`, `key_algorithm`, `signature_algorithm`
    - Modify the type `string` -> `int32` of the request parameter `limit`
    - Modify the type `string` -> `int32` of the request parameter `offset`
    - The response parameter `total` changed to required
  - Changes of the interface `CreateCertificateAuthority`:
    - Add the request parameters `X-Auth-Token`, `key_usages`
    - Remove the request parameter `crl_dis_point`
    - Modify the type `string` -> `int32` of the request parameter `start_from`
    - The request parameter `enabled`, `common_name`, `country`, `locality`, `organization`, `organizational_unit`, `state`, `key_algorithm`, `type`, `type`, `value` changed to required
    - The response parameter `ca_id` changed to required
  - Changes of the interface `ShowCertificateAuthorityObsAgency`:
    - Add the request parameter `X-Auth-Token`
    - The response parameter `agency_granted` changed to required
  - Changes of the interface `CreateCertificateAuthorityObsAgency`:
    - Add the request parameter `X-Auth-Token`
    - The response parameter `agency_id` changed to required
  - Changes of the interface `ListCertificateAuthorityObsBucket`:
    - Add the request parameter `X-Auth-Token`
    - Modify the type `string` -> `int64` of the response parameter `create_time`
    - The response parameter `total`, `bucket_name`, `create_time` changed to required
  - Changes of the interface `ShowCertificateAuthorityQuota`:
    - Add the request parameter `X-Auth-Token`
    - Modify the type `enum` -> `string` of the response parameter `type`
    - The response parameter `type`, `used`, `quota` changed to required
  - Changes of the interface `ShowCertificateAuthority`:
    - Add the request parameter `X-Auth-Token`
    - Remove the response parameter `crl_dis_point`
    - Modify the type `string` -> `int64` of the response parameter `create_time`
    - Modify the type `string` -> `int64` of the response parameter `delete_time`
    - Modify the type `string` -> `int64` of the response parameter `not_before`
    - Modify the type `string` -> `int64` of the response parameter `not_after`
    - The response parameter `ca_id`, `type`, `status`, `path_length`, `freeze_flag`, `gen_mode`, `serial_number`, `create_time`, `delete_time`, `not_before`, `not_after`, `common_name`, `country`, `locality`, `organization`, `organizational_unit`, `state`, `enabled`, `issuer_id`, `issuer_name`, `key_algorithm`, `signature_algorithm` changed to required
  - Add the request parameter `X-Auth-Token` to the interface `DeleteCertificateAuthority`
  - Changes of the interface `IssueCertificateAuthorityCertificate`:
    - Add the request parameter `X-Auth-Token`
    - Modify the type `string` -> `int32` of the request parameter `start_from`
    - The request parameter `issuer_id`, `path_length`, `signature_algorithm`, `type`, `value` changed to required
  - Changes of the interface `ExportCertificateAuthorityCsr`:
    - Add the request parameter `X-Auth-Token`
    - The response parameter `csr` changed to required
  - Add the request parameter `X-Auth-Token` to the interface `DisableCertificateAuthority`
  - Add the request parameter `X-Auth-Token` to the interface `EnableCertificateAuthority`
  - Changes of the interface `ExportCertificateAuthorityCertificate`:
    - Add the request parameter `X-Auth-Token`
    - The response parameter `certificate`, `certificate_chain` changed to required
  - Changes of the interface `ImportCertificateAuthorityCertificate`:
    - Add the request parameter `X-Auth-Token`
    - The request parameter `certificate` changed to required
  - Add the request parameter `X-Auth-Token` to the interface `RestoreCertificateAuthority`
  - Changes of the interface `ListCertificate`:
    - Add the request parameters `sort_key`, `sort_dir`, `X-Auth-Token`
    - Remove the response parameters `certificate_id`, `status`, `freeze_flag`, `gen_mode`, `serial_number`, `create_time`, `not_before`, `not_after`, `distinguished_name`, `issuer_id`, `issuer_name`, `key_algorithm`, `signature_algorithm`
    - Modify the type `string` -> `int32` of the request parameter `limit`
    - Modify the type `string` -> `int32` of the request parameter `offset`
    - The response parameter `total` changed to required
  - Changes of the interface `CreateCertificate`:
    - Add the request parameter `X-Auth-Token`
    - Modify the type `string` -> `int32` of the request parameter `start_from`
    - The request parameter `common_name`, `country`, `locality`, `organization`, `organizational_unit`, `state`, `issuer_id`, `key_algorithm`, `signature_algorithm`, `type`, `value`, `type`, `value` changed to required
    - The response parameter `certificate_id` changed to required
  - Changes of the interface `CreateCertificateByCsr`:
    - Add the request parameters `X-Auth-Token`, `type`, `path_length`
    - Modify the type `string` -> `int32` of the request parameter `start_from`
    - The request parameter `csr`, `issuer_id`, `type`, `value`, `type`, `value` changed to required
    - The response parameter `certificate_id` changed to required
  - Changes of the interface `ParseCertificateSigningRequest`:
    - Add the request parameter `X-Auth-Token`
    - Add the response parameters `key_algorithm`, `key_algorithm_length`, `signature_algorithm`, `public_key`, `distinguished_name`
    - Remove the response parameters `total`, `certificates`
    - The request parameter `csr` changed to required
  - Changes of the interface `ShowCertificateQuota`:
    - Add the request parameter `X-Auth-Token`
    - Modify the type `enum` -> `string` of the response parameter `type`
    - The response parameter `type`, `used`, `quota` changed to required
  - Changes of the interface `ShowCertificate`:
    - Add the request parameter `X-Auth-Token`
    - Add the response parameter `delete_time`
    - Modify the type `string` -> `int64` of the response parameter `create_time`
    - Modify the type `string` -> `int64` of the response parameter `not_before`
    - Modify the type `string` -> `int64` of the response parameter `not_after`
    - The response parameter `certificate_id`, `status`, `freeze_flag`, `gen_mode`, `serial_number`, `create_time`, `not_before`, `not_after`, `common_name`, `country`, `locality`, `organization`, `organizational_unit`, `state`, `issuer_id`, `issuer_name`, `key_algorithm`, `signature_algorithm` changed to required
  - Add the request parameter `X-Auth-Token` to the interface `DeleteCertificate`
  - Changes of the interface `ExportCertificate`:
    - Add the request parameter `X-Auth-Token`
    - The request parameter `is_compressed`, `type` changed to required
  - Changes of the interface `RevokeCertificate`:
    - Add the request parameter `X-Auth-Token`
    - Remove the request parameter `cert_id`

### HuaweiCloud SDK CDN

- _Features_
  - Support the interfaces(v2):
    - `ShowDomainLocationStats`
    - `ShowDomainStats`
    - `ShowTopUrl`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DAS

- _Features_
  - Support the interface `ShowSqlExplain`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `group_name`, `replication_ip` to the interface `ListRedislog`

### HuaweiCloud SDK DNS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `routers` from the interface `ListPublicZones`
  - Add the request parameters `marker`, `limit`, `offset`, `line_id`, `tags`, `status`, `type`, `name`, `id`, `sort_key`, `sort_dir`, `search_mode` to the interface `ShowRecordSetByZone`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the following interfaces:
    - `ListWorkflows`
    - `CreateWorkflow`
    - `BatchDeleteWorkflows`
    - `ListWorkflowExecutions`
    - `StartWorkflowExecution`
    - `ShowWorkflowExecution`
    - `ShowWorkFlow`
    - `UpdateWorkFlow`
    - `ShowTenantMetric`
    - `ShowWorkFlowMetric`
    - `RetryWorkFlow`
    - `StopWorkFlow`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListSimCards`:
    - Add the request parameters `min_flow`, `max_flow`, `order_id`, `filter_downtime_period`
    - Modify the type `date` -> `date-time` of the response parameter `device_status_date`
    - Modify the type `date` -> `date-time` of the response parameter `expire_time`
  - Add the request parameter `price_plan_list` to the interface `StopSimCard`
  - Add the request parameter `price_plan_list` to the interface `ResetSimCard`
  - Changes of the interface `ShowSimCard`:
    - Modify the type `date` -> `date-time` of the response parameter `device_status_date`
    - Modify the type `date` -> `date-time` of the response parameter `expire_time`

### HuaweiCloud SDK IMS

- _Features_
  - Support the interfaces `ListVersions`, `ShowVersion`
- _Bug Fix_
  - None
- _Change_
  - The request parameter `os_type` changed to not required of the interface `CreateDataImage`

### HuaweiCloud SDK IoTDA

- _Features_
  - Support the interface `ResetFingerprint`
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
  - Changes of the interface `RecognizeVatInvoice`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`
  - Changes of the interface `RecognizeIdCard`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`
  - Changes of the interface `RecognizeDriverLicense`:
    - Add the request parameter `return_text_location`
    - Add the response parameter `text_location`

### HuaweiCloud SDK VSS

- _Features_
  - Support the following interfaces:
    - `ShowDomainSettings`
    - `UpdateDomainSettings`
    - `ListTaskHistories`
    - `ListPortResults`
    - `ListBusinessRisks`
    - `UpdateFalsePositive`
    - `CancelTasks`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `domain_id` to the interface `ListDomains`
  - Add the response parameter `hit_details` to the interface `ShowResults`

# 3.0.80 2022-03-10

### HuaweiCloud SDK BCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `operation_id` to the interface `BatchCreateChannels`
  - The request parameter `fabric_version` changed to not required of the interface `CreateNewBlockchain`

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `cluster_id` changed to not required of the interface `DeleteAddonInstance`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `X-Auth-Token` from the interface `ShowTopUrl`
  - Remove the request parameter `X-Auth-Token` from the interface `ShowDomainLocationStats`
  - Remove the request parameter `X-Auth-Token` from the interface `ShowDomainItemDetails`
  - Remove the request parameter `X-Auth-Token` from the interface `ShowDomainStats`
  - Remove the request parameter `X-Auth-Token` from the interface `ShowDomainItemLocationDetails`

### HuaweiCloud SDK DWS

- _Features_
  - Support the following interfaces:
    - `ListClusterDetails`
    - `DeleteCluster`
    - `ResetPassword`
    - `ListSnapshots`
    - `CreateSnapshot`
    - `RestartCluster`
    - `ListClusters`
    - `CreateCluster`
    - `RestoreCluster`
    - `ResizeCluster`
    - `ListNodeTypes`
    - `ListSnapshotDetails`
    - `DeleteSnapshot`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ELB

- _Features_
  - Support the following interfaces:
    - `ListLogtanks`
    - `CreateLogtank`
    - `ShowLogtank`
    - `UpdateLogtank`
    - `DeleteLogtank`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `https_cps` to the interface `ListFlavors`
  - Add the response parameter `https_cps` to the interface `ShowFlavor`
  - The request parameter `X-Auth-Token` changed to not required of the interface `ListLoadBalancers`
  - The request parameter `X-Auth-Token` changed to not required of the interface `CreateLoadBalancer`
  - The request parameter `X-Auth-Token` changed to not required of the interface `UpdateIpList`
  - The request parameter `X-Auth-Token` changed to not required of the interface `BatchDeleteIpList`

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `date` -> `date-time` of the response parameter `act_date` of the interface `ListSimCards`
  - Modify the type `date` -> `date-time` of the response parameter `act_date` of the interface `ShowSimCard`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `count` to the interface `ListLogs`

### HuaweiCloud SDK Meeting

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `sortLevel` to the interface `AddDepartment`
  - Add the request parameter `sortLevel` to the interface `UpdateDepartment`
  - Add the response parameters `sortLevel`, `sortLevel` to the interface `ShowDeptAndChildDept`
  - Add the response parameter `sortLevel` to the interface `SearchDepartmentByName`

# 3.0.79 2022-03-07

### HuaweiCloud SDK CCE

- _Features_
  - Support the interfaces `UpdateClusterEip`, `ShowClusterEndpoints`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CES

- _Features_
  - Support the following interfaces (V2):
    - `ListAlarms`
    - `CreateAlarm`
    - `DeleteAlarm`
    - `UpdateAlarmAction`
    - `ListAlarmResources`
    - `DeleteAlarmResources`
    - `AddAlarmResources`
    - `AddResourceGroupsResourcesBatch`
    - `DeleteResourceGroupsResourcesBatch`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `gaussdbv5`, `postgresql` to the request parameter `engine_type` to the interface `BatchCreateJobs`
  - Changes of the interface `BatchValidateConnections`:
    - Add the request parameter `kafka_security_config`
    - Add the enum values `postgresql` to the request parameter `db_type`
  - Changes of the interface `BatchUpdateUser`:
    - Add the request parameter `is_sync_object_privilege`
    - Add the response parameters `no_privileges`, `parent_account`, `no_parent_account`
  - Add the response parameters `no_privileges`, `parent_account`, `no_parent_account` to the interface `ListUsers`
  - Add the request parameters `topic_policy`, `topic`, `partition_policy`, `kafka_data_format`, `topic_name_format`, `partitions_num`, `replication_factor`, `is_fill_materialized_view`, `export_snapshot` to the interface `BatchSetPolicy`

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type of the request parameter `ip_version` of the interface `CreatePrePaidPublicip`: `integer` -> `enum`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `order_id` to the interface `ShrinkInstanceNode`

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `error_code` to the interface `ListEditingJob`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `request_id` from the interface `DownloadSlowlog`

# 3.0.78 2022-02-25

### HuaweiCloud SDK AS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `alarm_id` to the interface `ListAllScalingV2Policies`
  - Add the enum values `GPSSD` to the request parameter `volume_type` to the interface `CreateScalingConfig`
  - Add the response parameter `min` to the interface `ShowResourceQuota`
  - Add the response parameter `min` to the interface `ShowPolicyAndInstanceQuota`

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateBaremetalServerMetadata`:
    - Modify the type of the request body `MetaData` -> `UpdateBaremetalServerMetadataReq`
    - Remove the response parameter `key`

### HuaweiCloud SDK CDM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `from-connector-name`, `to-link-name` changed to required of the interface `ShowJobs`
  - The request parameter `from-connector-name`, `to-link-name` changed to required of the interface `UpdateJob`
  - Changes of the interface `CreateAndStartRandomClusterJob`:
    - The request parameter `from-connector-name`, `to-link-name` changed to required
    - Modify the type `int32` -> `float` of the response parameter `progress`
    - Modify the type `boolean` -> `string` of the response parameter `isStopingIncrement`
  - Add the response parameter `submissions` to the interface `StopJob`
  - The request parameter `from-connector-name`, `to-link-name` changed to required of the interface `CreateJob`
  - Changes of the interface `StartJob`:
    - Modify the type `int32` -> `float` of the response parameter `progress`
    - Modify the type `boolean` -> `string` of the response parameter `isStopingIncrement`
  - Modify the type `double` -> `float` of the response parameter `progress` of the interface `ShowJobStatus`
  - Modify the type `double` -> `float` of the response parameter `progress` of the interface `ShowSubmissions`

### HuaweiCloud SDK CDN

- _Features_
  - Support the interfaces `ShowDomainLocationStats`, `ShowDomainFullConfig`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowDomainStats`:
    - Add the request parameter `service_area`
    - Remove the request parameters `X-Auth-Token`, `country`, `district`, `isp`
    - Remove the response parameters `start_time`, `end_time`, `interval`, `action`, `stat_type`, `group_by`
  - Add the request parameter `https` to the interface `UpdateDomainFullConfig`

### HuaweiCloud SDK CloudIDE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `instance_domain_id`, `instance_user_id` to the interface `CreateInstance`
  - The request parameter `instance_user_domain_name`, `instance_user_name` changed to not required of the interface `CreateInstanceBy3rd`

### HuaweiCloud SDK CodeCheck

- _Features_
  - Support the interface `CheckRecord`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudRTC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `array` -> `string` of the request parameter `mid` of the interface `ListRtcClientQosDetails`

### HuaweiCloud SDK CodeHub

- _Features_
  - Support the interface `ShowStatisticCommitV3`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListProjectSets`:
    - Add the response parameters `CreateTime`, `UpdateTime`, `external_params`, `variables_no_file`
    - Remove the response parameters `create_time`, `update_time`, `group`
  - The request parameter `name` changed to required of the interface `UpdateProject`
  - Changes of the interface `ShowTask`:
    - Add the response parameters `parallel`, `contents`, `sort`, `related_temp_running_data`
    - Remove the response parameter `content`
  - Changes of the interface `UpdateTask`:
    - Add the request parameters `contents`, `sort`, `related_temp_running_data`
    - Add the response parameters `parallel`, `contents`, `sort`, `related_temp_running_data`
    - Remove the request parameter `content`
    - Remove the response parameter `content`
    - The request parameter `name` changed to required
  - Changes of the interface `ShowReport`:
    - Add the response parameters `performance`, `minNetworkTraffic`, `avgNetworkTraffic`, `maxNetworkTraffic`, `branchId`, `branchName`, `projectId`, `serviceId`
    - Remove the response parameters `progressState`, `statusValue`
    - Modify the type `float` -> `double` of the response parameter `averageRespTime`
    - Modify the type `float` -> `double` of the response parameter `avgRecBytes`
    - Modify the type `int32` -> `double` of the response parameter `avgSentBytes`
    - Modify the type `string` -> `double` of the response parameter `avgTranRespTime`
    - Modify the type `int32` -> `double` of the response parameter `currentThreadNum`
    - Modify the type `int32` -> `double` of the response parameter `errorCount`
    - Modify the type `int32` -> `double` of the response parameter `errorEventsCount`
    - Modify the type `int32` -> `double` of the response parameter `failedAssert`
    - Modify the type `int32` -> `double` of the response parameter `failedOthers`
    - Modify the type `int32` -> `double` of the response parameter `failedParsed`
    - Modify the type `int32` -> `double` of the response parameter `failedRefused`
    - Modify the type `int32` -> `double` of the response parameter `failedTimeout`
    - Modify the type `int32` -> `double` of the response parameter `max`
    - Modify the type `int32` -> `double` of the response parameter `maxRecBytes`
    - Modify the type `int32` -> `double` of the response parameter `maxRespTime`
    - Modify the type `int32` -> `double` of the response parameter `maxSentBytes`
    - Modify the type `int32` -> `double` of the response parameter `maxTranRespTime`
    - Modify the type `int32` -> `double` of the response parameter `min`
    - Modify the type `int32` -> `double` of the response parameter `requests`
    - Modify the type `int32` -> `double` of the response parameter `result`
    - Modify the type `int32` -> `double` of the response parameter `status`
    - Modify the type `int32` -> `double` of the response parameter `successCount`
    - Modify the type `int32` -> `double` of the response parameter `successRate`
    - Modify the type `int32` -> `double` of the response parameter `sum1xx`
    - Modify the type `int32` -> `double` of the response parameter `sum2xx`
    - Modify the type `int32` -> `double` of the response parameter `sum3xx`
    - Modify the type `int32` -> `double` of the response parameter `sum4xx`
    - Modify the type `int32` -> `double` of the response parameter `sum5xx`
    - Modify the type `int32` -> `double` of the response parameter `taskStatus`
    - Modify the type `int32` -> `double` of the response parameter `tp50`
    - Modify the type `int32` -> `double` of the response parameter `tp75`
    - Modify the type `int32` -> `double` of the response parameter `tp90`
    - Modify the type `int32` -> `double` of the response parameter `tp95`
    - Modify the type `int32` -> `double` of the response parameter `tp99`
    - Modify the type `float` -> `double` of the response parameter `tps`
    - Modify the type `string` -> `double` of the response parameter `tranTPS`
    - Modify the type `string` -> `double` of the response parameter `transactionSuccess`
    - Modify the type `int32` -> `double` of the response parameter `transactionalSuccessRate`
    - Modify the type `int32` -> `double` of the response parameter `transactionalTps`
    - Modify the type `int32` -> `double` of the response parameter `transactionalTpsSuccess`
    - Modify the type `string` -> `double` of the response parameter `transactions`
    - Modify the type `int32` -> `double` of the response parameter `vum`
    - Modify the type `float` -> `double` of the response parameter `avgResponseTime`
    - Modify the type `int32` -> `double` of the response parameter `caseRetry`
    - Modify the type `int32` -> `double` of the response parameter `completeNum`
    - Modify the type `int32` -> `double` of the response parameter `duration`
    - Modify the type `int32` -> `double` of the response parameter `executedNum`
    - Modify the type `int32` -> `double` of the response parameter `kpiCaseCount`
    - Modify the type `int32` -> `double` of the response parameter `kpiCaseExecuteCount`
    - Modify the type `int32` -> `double` of the response parameter `kpiCasePassCount`
    - Modify the type `int32` -> `double` of the response parameter `maxUsers`
    - Modify the type `int32` -> `double` of the response parameter `passNum`
    - Modify the type `int32` -> `double` of the response parameter `stage`
    - Modify the type `int32` -> `double` of the response parameter `totalNum`
  - Changes of the interface `UpdateCase`:
    - Add the request parameters `contents`, `sort`
    - Remove the request parameter `content`
  - Add the request parameter `contents` to the interface `CreateTemp`
  - Changes of the interface `UpdateTemp`:
    - Modify the type `array` -> `string` of the request parameter `bodys`
    - The request parameter `name` changed to required
  - Add the request parameter `is_quoted` to the interface `CreateVariable`
  - Changes of the interface `ShowHistoryRunInfo`:
    - Modify the type `int32` -> `double` of the response parameter `run_id`
    - Modify the type `int32` -> `double` of the response parameter `run_type`
    - Modify the type `int32` -> `double` of the response parameter `continue_time`

### HuaweiCloud SDK CSS

- _Features_
  - Support the following interfaces:
    - `UpdateFlavor`
    - `UpdateFlavorByType`
    - `UpdateShrinkNodes`
    - `UpdateShrinkCluster`
    - `ListLogsJob`
    - `ShowClusterDetail`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `id`, `instances` from the interface `UpdateExtendCluster`
  - Remove the request parameter `status` from the interface `StartConnectivityTest`

### HuaweiCloud SDK DDM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `group_id` to the interface `ExpandInstanceNodes`
  - Add the request parameter `group_id` to the interface `ShrinkInstanceNodes`
  - The request parameter `shard_unit` changed to not required of the interface `CreateDatabase`

### HuaweiCloud SDK DGC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListConnections`:
    - Add the response parameters `type`, `description`
    - Remove the response parameter `connectionType`
    - Modify the type `string` -> `int32` of the response parameter `total`
    - The response parameter `name` changed to required
  - Changes of the interface `CreateConnection`:
    - Add the request parameters `type`, `description`
    - Remove the request parameter `connectionType`
    - The request parameter `name` changed to required
  - Changes of the interface `ShowConnection`:
    - Add the response parameters `type`, `description`
    - Remove the response parameter `connectionType`
    - The response parameter `name` changed to required
  - Changes of the interface `UpdateConnection`:
    - Add the request parameters `type`, `description`
    - Remove the request parameter `connectionType`
    - The request parameter `name` changed to required
  - Changes of the interface `ExecuteScript`:
    - Add the response parameter `instanceId`
    - Remove the response parameter `jobId`
    - Modify the type `string` -> `object` of the request parameter `params`

### HuaweiCloud SDK ELB

- _Features_
  - Support the interfaces `BatchCreateMembers`, `BatchDeleteMembers`
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
  - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime` to the interface `ListFunctions`
  - Changes of the interface `CreateFunction`:
    - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the request parameter `runtime`
    - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime`
  - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime` to the interface `ShowFunctionCode`
  - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime` to the interface `UpdateFunctionCode`
  - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime` to the interface `ShowFunctionConfig`
  - Changes of the interface `UpdateFunctionConfig`:
    - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the request parameter `runtime`
    - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime`
  - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime` to the interface `ListFunctionVersions`
  - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime` to the interface `CreateFunctionVersion`
  - Add the enum values `Java11`, `Node.js14.18`, `Python3.9` to the request parameter `runtime` to the interface `CreateDependency`
  - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `PHP 7.3` from the request parameter `runtime` to the interface `UpdateDependency`
  - Add the enum values `Java8`, `Java11`, `Node.js6.10`, `Node.js8.10`, `Node.js10.16`, `Node.js12.13`, `Node.js14.18`, `Python2.7`, `Python3.6`, `Python3.9`, `Go1.8`, `Go1.x`, `PHP7.3`, Remove the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3` from the response parameter `runtime` to the interface `ImportFunction`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interfaces `UpdateAuditLog`, `ShowAuditLog`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Live

- _Features_
  - Support the interface `ListSingleStreamDetail`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK LTS

- _Features_
  - Support the interfaces `UpdateStructConfig`, `CreateStructConfig`, `ListStructTemplate`, `ListBreifStructTemplate`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `tag` to the interface `ListLogGroups`
  - Add the response parameter `tag` to the interface `ListLogStream`

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interfaces `BatchUpdateChildNickNames`, `ListIterationHistories`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `updated_time_interval`, `include_deleted` to the interface `ListProjectIterationsV4`
  - Add the request parameters `include_deleted`, `updated_time_interval` to the interface `ListIssuesV4`
  - Add the response parameters `description`, `order`, `accessories` to the interface `ShowIssueV4`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListSlowLogFile`, `StopInstance`, `StartupInstance`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SCM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `sans`, `signature_algorithm`, `deploy_support` to the interface `ListCertificates`
  - Add the request parameters `enc_certificate`, `enc_private_key` to the interface `ImportCertificate`
  - Changes of the interface `ShowCertificate`:
    - Add the response parameter `signature_algorithm`
    - Remove the response parameter `signature_algrithm`
  - Add the response parameters `enc_certificate`, `enc_private_key` to the interface `ExportCertificate`

### HuaweiCloud SDK VOD

- _Features_
  - Support the interface `ListDomainLogs`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `delete_type` to the interface `DeleteAssets`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `subnetpool_id` to the interface `NeutronListSubnets`

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListWhiteblackipRule`:
    - Add the response parameter `addr`
    - Remove the response parameter `ip`

# 3.0.77 2022-02-10

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateAlarmRule`:
    - Modify the type `string` -> `enum` of the request parameter `statistic`
    - The request parameter `alarm_level`, `comparison_operator`, `evaluation_periods`, `metric_name`, `namespace`, `period`, `statistic`, `threshold`, `unit` changed to not required

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListRateOnPeriodDetail`:
    - Add the request parameter `fee_installment_mode`
    - Add the response parameters `installment_official_website_amount`、`installment_period_type`、`installment_official_discount_amount`、`installment_amount`

### HuaweiCloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListProtectable`:
    - Modify the type `string` -> `boolean` of the response parameter `result`
    - Modify the type `string` -> `int32` of the response parameter `size`
  - Changes of the interface `ShowProtectable`:
    - Modify the type `string` -> `boolean` of the response parameter `result`
    - Modify the type `string` -> `int32` of the response parameter `size`

### HuaweiCloud SDK CCE

- _Features_
  - Support the interface `ShowVersion`
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `kind`, `apiVersion`, `metadata`, `spec`, `status` from the interface `CreateAddonInstance`
  - Add the response parameters `isStatic`, `privateIPv6IP` to the interface `ListNodes`
  - Add the request parameter `isStatic` to the interface `CreateNode`
  - Add the response parameters `isStatic`, `privateIPv6IP` to the interface `DeleteNode`
  - Add the response parameters `isStatic`, `privateIPv6IP` to the interface `ShowNode`
  - Add the response parameters `isStatic`, `privateIPv6IP` to the interface `UpdateNode`
  - Changes of the interface `RemoveNode`:
    - The request parameter `uid` changed to required
    - The response parameter `uid` changed to required
  - Changes of the interface `MigrateNode`:
    - The request parameter `uid` changed to required
    - The response parameter `uid` changed to required
  - Add the response parameter `isStatic` to the interface `ListNodePools`
  - Add the request parameter `isStatic` to the interface `CreateNodePool`
  - Add the response parameter `isStatic` to the interface `DeleteNodePool`
  - Add the response parameter `isStatic` to the interface `ShowNodePool`
  - Changes of the interface `UpdateNodePool`:
    - Add the request parameter `isStatic`
    - Add the response parameter `isStatic`

### HuaweiCloud SDK CSS

- _Features_
  - Support the following interfaces:
    - `UpdateOndemandClusterToPeriod`
    - `UpdateClusterName`
    - `ResetPassword`
    - `StartKibanaPublic`
    - `UpdateCloseKibana`
    - `UpdateAlterKibana`
    - `UpdatePublicKibanaWhitelist`
    - `StopPublicKibanaWhitelist`
    - `CreateCnf`
    - `UpdateCnf`
    - `StartPipeline`
    - `StopPipeline`
    - `AddFavorite`
    - `StartConnectivityTest`
    - `ListTemplates`
    - `ListConfs`
    - `ListPipelines`
    - `ListActions`
    - `ShowGetConfDetail`
    - `DeleteConf`
    - `DeleteTemplate`
    - `StartLogs`
    - `StopLogs`
    - `ShowGetLogSetting`
    - `UpdateLogSetting`
    - `StartLogAutoBackupPolicy`
    - `StopLogAutoBackupPolicy`
    - `CreateLogBackup`
    - `ShowLogBackup`
    - `CreateBindPublic`
    - `UpdateUnbindPublic`
    - `UpdatePublicBandWidth`
    - `StartPublicWhitelist`
    - `StopPublicWhitelist`
    - `StartVpecp`
    - `StopVpecp`
    - `ShowVpcepConnection`
    - `UpdateVpcepConnection`
    - `UpdateVpcepWhitelist`
    - `UpdateYmls`
    - `ListYmlsJob`
    - `ListYmls`
    - `ListClustersDetails`
    - `CreateCluster`
    - `DeleteCluster`
    - `RestartCluster`
    - `UpdateExtendCluster`
    - `UpdateExtendInstanceStorage`
    - `ListFlavors`
    - `ShowClusterTag`
    - `CreateClustersTags`
    - `ListClustersTags`
    - `UpdateBatchClustersTags`
    - `DeleteClustersTags`
    - `ShowIkThesaurus`
    - `CreateLoadIkThesaurus`
    - `DeleteIkThesaurus`
    - `StartAutoSetting`
    - `UpdateSnapshotSetting`
    - `ShowAutoCreatePolicy`
    - `CreateAutoCreatePolicy`
    - `CreateSnapshot`
    - `ListSnapshots`
    - `StopSnapshot`
    - `RestoreSnapshot`
    - `DeleteSnapshot`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - Support the interfaces `CreateOnlineMigrationTask`, `SetOnlineMigrationTask`, `BatchStopMigrationTasks`, `StopMigrationTaskSync`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DevStar

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowApplicationDependentResources`:
    - Add the request parameters `X-Auth-Token`, `limit`, `offset`
    - Add the response parameter `count`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateFunction`:
    - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the request parameter `runtime`
    - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime`
  - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime` to the interface `ListFunctions`
  - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime` to the interface `UpdateFunctionCode`
  - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime` to the interface `ShowFunctionCode`
  - Changes of the interface `UpdateFunctionConfig`:
    - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the request parameter `runtime`
    - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime`
  - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime` to the interface `ShowFunctionConfig`
  - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime` to the interface `CreateFunctionVersion`
  - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime` to the interface `ListFunctionVersions`
  - Add the enum values `Go1.x` to the request parameter `runtime` to the interface `CreateDependency`
  - Add the enum values `Go1.x` to the request parameter `runtime` to the interface `UpdateDependency`
  - Add the enum values `Java 8`, `Node.js 6.10`, `Node.js 8.10`, `Node.js 10.16`, `Node.js 12.13`, `Python 2.7`, `Python 3.6`, `Go 1.8`, `Go 1.x`, `PHP 7.3`, Remove the enum values `Python2.7`, `Python3.6`, `Go1.8`, `Java8`, `Node.js6.10`, `Node.js8.10`, `Custom`, `PHP7.3` from the response parameter `runtime` to the interface `ImportFunction`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `alias` to the interface `ShowGaussMySqlInstanceInfo`
  - Add the response parameter `job_id` to the interface `CreateGaussMySqlBackup`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `int32` -> `string` of the response parameter `port` of the interface `ListInstances`

### HuaweiCloud SDK Live

- _Features_
  - Support the interfaces `ListTranscodeTaskCount`, `ListAreaDetail`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `publish_domain` to the interface `ListRecordData`
  - Remove the request parameter `plan_record_time` from the interface `CreateRecordRule`
  - Remove the response parameter `plan_record_time` from the interface `ListRecordRules`
  - Remove the response parameter `plan_record_time` from the interface `ShowRecordRule`
  - Changes of the interface `UpdateRecordRule`:
    - Remove the request parameter `plan_record_time`
    - Remove the response parameter `plan_record_time`
  - Remove the request parameter `on_demand_callback_url` from the interface `CreateRecordCallbackConfig`
  - Remove the response parameter `on_demand_callback_url` from the interface `ListRecordCallbackConfigs`
  - Remove the response parameter `on_demand_callback_url` from the interface `ShowRecordCallbackConfig`
  - Remove the request parameter `on_demand_callback_url` from the interface `UpdateRecordCallbackConfig`

### HuaweiCloud SDK Meeting

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `existQos` to the interface `SearchQosParticipants`
  - Add the response parameter `existQos` to the interface `SearchQosParticipantDetail`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `restore_all_database` to the interface `RestoreToExistingInstance`
  - Remove the request parameter `is_open_recycle_policy` from the interface `StartRecyclePolicy`

# 3.0.76 2022-01-25

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `content_type` to the interface `CreateApiV2`
  - Add the response parameters `publish_time`, `roma_app_name`, `ld_api_id`, `api_group_info`, `content_type` to the interface `ShowDetailsOfApiV2`
  - Changes of the interface `UpdateApiV2`:
    - Add the request parameter `content_type`
    - Add the response parameters `publish_time`, `roma_app_name`, `ld_api_id`, `api_group_info`, `content_type`
  - Add the response parameter `content_type` to the interface `ListApiRuntimeDefinitionV2`
  - Changes of the interface `ListApiVersionDetailV2`:
    - Add the response parameters `roma_app_name`, `ld_api_id`, `api_group_info`, `content_type`
    - Modify the type `date-time` -> `string` of the response parameter `publish_time`

### HuaweiCloud SDK CDM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowJobs`:
    - Remove the response parameter `simple`
    - The response parameter `name`, `values` changed to required
  - The request parameter `name`, `values` changed to required of the interface `UpdateJob`
  - The request parameter `name`, `values` changed to required of the interface `CreateAndStartRandomClusterJob`
  - The request parameter `name`, `values` changed to required of the interface `CreateJob`
  - Remove the response parameter `config_status` from the interface `ListClusters`

### HuaweiCloud SDK CES

- _Features_
  - Support the interface `ListAlarmHistories`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CodeCheck

- _Features_
  - Support the interfaces `DeleteRuleset`, `SetDefaulTemplate`, `ShowTasklog`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `endpoint_id` to the interface `CreateTask`
  - Add the request parameter `custom_attributes` to the interface `CreateRuleset`
  - Changes of the interface `ListTemplateRules`:
    - Add the request parameter `tags`
    - Add the response parameter `rule_config_list`

### HuaweiCloud SDK DevStar

- _Features_
  - Support the interfaces `ShowRepositoryByCloudIde`, `ListTemplates`
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
  - Add the response parameter `session_user_id` to the interface `CreateLoginToken`

### HuaweiCloud SDK Kafka

- _Features_
  - Support the interface `ListEngineProducts`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `dr_enable` to the interface `ListInstances`
  - Add the response parameter `dr_enable` to the interface `ShowInstance`
  - Changes of the interface `ListProducts`:
    - Add the response parameters `Hourly`, `Monthly`
    - Remove the response parameters `hourly`, `honthly`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `language` from the interface `CreateSqlAlarmRule`
  - Remove the request parameter `language` from the interface `UpdateSqlAlarmRule`
  - Changes of the interface `ListSqlAlarmRules`:
    - Add the response parameters `template_name`, `status`
    - Remove the response parameter `language`
  - Remove the request parameters `language`, `eps_id`, `eps_name`, `is_time_range_relative` from the interface `CreateKeywordsAlarmRule`
  - Changes of the interface `UpdateKeywordsAlarmRule`:
    - Remove the request parameters `language`, `eps_id`, `eps_name`, `is_time_range_relative`
    - Remove the response parameters `eps_id`, `eps_name`, `is_time_range_relative`
  - Changes of the interface `ListKeywordsAlarmRules`:
    - Add the response parameters `template_name`, `status`
    - Remove the response parameters `language`, `eps_id`, `eps_name`, `is_time_range_relative`
  - Changes of the interface `ListAccessConfig`:
    - Add the request parameter `access_config_tag_list`
    - Add the response parameter `access_config_tag`
  - Changes of the interface `CreateAccessConfig`:
    - Add the request parameter `access_config_tag`
    - Add the response parameter `access_config_tag`
  - Changes of the interface `UpdateAccessConfig`:
    - Add the request parameter `access_config_tag`
    - Add the response parameter `access_config_tag`
  - Add the response parameter `access_config_tag` to the interface `DeleteAccessConfig`

### HuaweiCloud SDK Meeting

- _Features_
  - Support the authentication method via appId
  - Support the interfaces `ShowWebHookConfig`, `SetWebHookConfig`, `DeleteWebHookConfig`, `UpdateWebHookConfigStatus`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RabbitMQ

- _Features_
  - Support the interface `ListEngineProducts`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.75 2022-01-17

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - Fix the problem that the request body structure of the interface `CreateNodePool` is incorrect
- _Change_
  - None

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the interface `ListFunctionAsyncInvocations`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `used` to the interface `ShowGaussMySqlInstanceInfo`
  - Add the request parameter `monitor_switch` to the interface `UpdateInstanceMonitor`
  - Modify the type of the request parameter `period` of the interface `UpdateInstanceMonitor`: `string` -> `int32`
  - Remove the response parameter `mode` from the interface `ShowGaussMySqlProjectQuotas`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `ListApiVersionNew`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `az_desc` to the interface `ListFlavors`

### HuaweiCloud SDK ROMA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `id`, `roles` to the interface `AddUserToApp`
  - Remove the response parameters `apps`, `tasks` from the interface `DownloadAssetArchive`
  - Remove the request parameters `apps`, `tasks` from the interface `ImportAsset`
  - The request parameter `tasks` changed to required of the interface `DeleteAsset`
  - Add the response parameter `access_user` to the interface `ShowMqsInstance`

# 3.0.74 2022-01-10

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `coupon_max_use_quantity`, `coupon_group` to the interface `ListOrderCouponsByOrderId`

### HuaweiCloud SDK CCE

- _Features_
  - Support the interface `ShowQuotas`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `customSan`, `offloadCluster`, `cidrs`, `flavor`, `faultDomain` to the interface `CreateCluster`
  - Add the response parameters `customSan`, `offloadCluster`, `cidrs`, `flavor`, `faultDomain` to the interface `ListClusters`
  - Changes of the interface `UpdateCluster`:
    - Add the request parameters `customSan`, `containerNetwork`
    - Add the response parameters `customSan`, `offloadCluster`, `cidrs`, `flavor`, `faultDomain`
  - Add the response parameters `customSan`, `offloadCluster`, `cidrs`, `flavor`, `faultDomain` to the interface `ShowCluster`
  - Add the response parameters `customSan`, `offloadCluster`, `cidrs`, `flavor`, `faultDomain` to the interface `DeleteCluster`
  - Add the request parameters `faultDomain`, `offloadNode`, `offloadNode` to the interface `CreateNode`
  - Add the response parameters `faultDomain`, `offloadNode`, `offloadNode` to the interface `ListNodes`
  - Add the response parameters `faultDomain`, `offloadNode`, `offloadNode` to the interface `UpdateNode`
  - Add the response parameters `faultDomain`, `offloadNode`, `offloadNode` to the interface `ShowNode`
  - Add the response parameters `faultDomain`, `offloadNode`, `offloadNode` to the interface `DeleteNode`
  - Add the request parameters `podSecurityGroups`, `faultDomain`, `offloadNode`, `offloadNode` to the interface `CreateNodePool`
  - Add the response parameters `podSecurityGroups`, `faultDomain`, `offloadNode`, `offloadNode` to the interface `ListNodePools`
  - Changes of the interface `UpdateNodePool`:
    - Add the request parameters `podSecurityGroups`, `faultDomain`, `offloadNode`, `offloadNode`
    - Add the response parameters `podSecurityGroups`, `faultDomain`, `offloadNode`, `offloadNode`
  - Add the response parameters `podSecurityGroups`, `faultDomain`, `offloadNode`, `offloadNode` to the interface `ShowNodePool`
  - Add the response parameters `podSecurityGroups`, `faultDomain`, `offloadNode`, `offloadNode` to the interface `DeleteNodePool`

### HuaweiCloud SDK CDN

- _Features_
  - Support the interface `UpdateDomainFullConfig`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interface `ListStacks`
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ListStacksByTag`

### HuaweiCloud SDK Cloudtest

- _Features_
  - Support the interface `ShowPlanList`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowPlans`:
    - Modify the type `int64` -> `int32` of the request parameter `limit`
    - Modify the type `int64` -> `int32` of the request parameter `offset`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `ecs_tenant_private_ip` to the interface `ListMigrationTask`
  - Add the response parameter `ecs_tenant_private_ip` to the interface `ShowMigrationTask`
  - Add the response parameter `ecs_tenant_private_ip` to the interface `StopMigrationTask`

### HuaweiCloud SDK DDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `lb_ip_address` from the interface `ListInstances`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `delete_on_termination` to the interface `CreateServers`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `UpdateFunctionConfig`:
    - Add the request parameter `is_stateful_function`
    - Add the response parameter `is_stateful_function`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `lb_ip_address` to the interface `ListInstances`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `GaussDB(for openGauss)`, Remove the enum values `GaussDB(openGauss)` from the request parameter `type` to the interface `CreateInstance`
  - Remove the response parameter `related_instance` from the interface `ListInstances`

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The response parameter `active_at` changed to not required of the interface `GlanceListImages`
  - The response parameter `active_at` changed to not required of the interface `GlanceShowImage`
  - The response parameter `active_at` changed to not required of the interface `GlanceUpdateImage`

### HuaweiCloud SDK IoTAnalytics

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `site_id` changed to required of the interface `CreateDatasource`
  - The request parameter `site_id` changed to required of the interface `UpdateDataSource`

### HuaweiCloud SDK KPS

- _Features_
  - Support the `Key Pair Service`
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
  - Changes of the interface `StartInstanceSingleToHaAction`:
    - Add the request parameter `ad_domain_info`
    - Remove the request parameter `password`

### HuaweiCloud SDK ROMA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `connect_dn` from the interface `ShowMqsInstance`
  - Remove the response parameter `policies` from the interface `ListMqsInstanceTopics`
  - Add the response parameter `roma_app_type` to the interface `ShowDetailsOfAppV2`

### HuaweiCloud SDK VPCEP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `pool_id` to the interface `CreateEndpointService`
  - Add the response parameter `domain_id` to the interface `ListEndpointService`
  - Add the response parameter `pool_id` to the interface `UpdateEndpointService`
  - Add the response parameters `enable_status`, `specification_name` to the interface `ListEndpointInfoDetails`

### HuaweiCloud SDK VSS

- _Features_
  - Support the interfaces `AuthorizeDomains`, `ShowTasks`, `CreateTasks`, `ShowResults`
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `skip` to the response parameter `auth_status` to the interface `ListDomains`

# 3.0.73 2021-12-25

### HuaweiCloud SDK CDM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `id` to the interface `CreateLink`
  - Add the response parameters `endpointDomainName`, `isScheduleBootOff`, `failedReasons`, `components`, `createFrom`, `resourceId`, `flavorType`, `workSpaceId`, `trial` to the interface `ShowClusterDetail`
  - Add the request parameters `is_incre_job`, `flag`, `files_read`, `external_id`, `type`, `execute_start_date`, `delete_rows`, `enabled`, `bytes_written`, `id`, `is_use_sql`, `update_rows`, `group_name`, `bytes_read`, `execute_update_date`, `write_rows`, `files_writte`, `is_incrementing`, `execute_create_date`, `id`, `type`, `id`, `type`, `id`, `type` to the interface `UpdateJob`
  - Add the response parameters `is_incre_job`, `flag`, `files_read`, `external_id`, `type`, `execute_start_date`, `delete_rows`, `enabled`, `bytes_written`, `id`, `is_use_sql`, `update_rows`, `group_name`, `bytes_read`, `execute_update_date`, `write_rows`, `files_writte`, `is_incrementing`, `execute_create_date`, `id`, `type`, `id`, `type`, `id`, `type` to the interface `ShowJobs`
  - Changes of the interface `CreateAndStartRandomClusterJob`:
    - Add the request parameters `is_incre_job`, `flag`, `files_read`, `external_id`, `type`, `execute_start_date`, `delete_rows`, `enabled`, `bytes_written`, `id`, `is_use_sql`, `update_rows`, `group_name`, `bytes_read`, `execute_update_date`, `write_rows`, `files_writte`, `is_incrementing`, `execute_create_date`, `id`, `type`, `id`, `type`, `id`, `type`
    - Add the response parameter `submissions`
    - Remove the response parameters `name`, `validation-result`
  - Add the request parameters `is_incre_job`, `flag`, `files_read`, `external_id`, `type`, `execute_start_date`, `delete_rows`, `enabled`, `bytes_written`, `id`, `is_use_sql`, `update_rows`, `group_name`, `bytes_read`, `execute_update_date`, `write_rows`, `files_writte`, `is_incrementing`, `execute_create_date`, `id`, `type`, `id`, `type`, `id`, `type` to the interface `CreateJob`
  - Add the response parameter `execute-date` to the interface `StartJob`
  - Add the request parameter `id` to the interface `UpdateLink`
  - Add the response parameter `id` to the interface `ShowLink`
  - Changes of the interface `ListClusters`:
    - Add the response parameters `bakExpectedStartTime`, `bakKeepDay`, `createFrom`, `resourceId`, `flavorType`, `workSpaceId`, `trial`, `components`
    - Remove the response parameter `version`

### HuaweiCloud SDK CloudBuild

- _Features_
  - Support the interface `ShowHistoryDetails`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Cloudtest

- _Features_
  - Support the interfaces `ShowPlanJournals`, `ShowIssuesByPlanId`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CodeCheck

- _Features_
  - Support the interfaces `CheckParameters`, `ListTaskParameter`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `rule_desc` to the interface `ListRules`
  - Add the response parameters `is_devcloud_project_default`, `is_default_template` to the interface `ListRulesets`

### HuaweiCloud SDK CodeHub

- _Features_
  - Support the service `CodeHub`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `backup_format` to the interface `CopyInstance`

### HuaweiCloud SDK DevStar

- _Features_
  - Support the following interfaces:
    - `ShowApplicationV3`
    - `UpdateApplication`
    - `ShowApplicationDependentResources`
    - `DeleteApplicationV4`
    - `ShowApplicationResDeleteStatus`
    - `ListApplicationsV6`
    - `ShowDeploymentJobs`
    - `CreateDeploymentJobs`
    - `ShowPipelineLastStatusV2`
    - `ListPipelineTemplates`
    - `StartPipeline`
    - `ListProjectsV4`
    - `ShowRepositoryStatisticalDataV2`
    - `CheckRepositoryDuplicateName`
    - `ShowApplicationReleaseRepositories`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `dependents` to the interface `ShowTemplateV3`
  - Add the response parameters `dependents`, `dependent_services` to the interface `ListTemplatesV2`
  - Add the response parameter `show_type` to the interface `ShowJobDetail`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameter `updated_at` from the interface `NovaListServerActions`

### HuaweiCloud SDK IEF

- _Features_
  - Support the service `Intelligent EdgeFabric`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTAnalytics

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateDatasource`:
    - Add the request parameter `site_id`
    - Remove the request parameter `instance_id`
  - Changes of the interface `ShowAllDataSource`:
    - Add the response parameter `site_id`
    - Remove the response parameter `instance_id`
  - Changes of the interface `UpdateDataSource`:
    - Add the request parameter `site_id`
    - Add the response parameter `site_id`
    - Remove the request parameter `instance_id`
    - Remove the response parameter `instance_id`
  - Changes of the interface `ShowDataSource`:
    - Add the response parameter `site_id`
    - Remove the response parameter `instance_id`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `partition_num` changed to not required of the interface `CreatePostPaidInstance`
  - Add the response parameters `result`, `instance_id` to the interface `RestartManager`
  - Changes of the interface `ListProducts`:
    - Add the response parameters `hourly`, `honthly`
    - Remove the response parameters `Hourly`, `Monthly`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `offset`, `limit` to the interface `ListCharts`
  - Add the request parameters `offset`, `limit` to the interface `ListNotificationTemplates`

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateTranscodingTask`:
    - Add the request parameter `auto_volume_setting`
    - Add the enum values `original` to the request parameter `volume`
  - Add the response parameter `av_parameters` to the interface `ListTranscodingTask`
  - Add the request parameter `template_id` to the interface `CreateWatermarkTemplate`
  - Add the response parameter `template_id` to the interface `ListWatermarkTemplate`
  - Add the request parameter `template_id` to the interface `UpdateWatermarkTemplate`

### HuaweiCloud SDK MRS

- _Features_
  - Support the following interfaces:
    - `CreateScalingPolicy`
    - `ShowClusterDetails`
    - `UpdateClusterScaling`
    - `ListHosts`
    - `CreateAndExecuteJob`
    - `ListExecuteJob`
    - `ShowJobExes`
    - `DeleteJobExecution`
    - `CreateCluster`
    - `ShowAgencyMapping`
    - `UpdateAgencyMapping`
    - `ShowJobExeListNew`
    - `CreateExecuteJob`
    - `ShowSingleJobExe`
    - `StopJob`
    - `ShowSqlResultWithJob`
    - `BatchDeleteJobs`
    - `ExecuteSql`
    - `ShowSqlResult`
    - `CancelSql`
    - `ShowHdfsFileList`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `group_type`, `success_record_error_reason`, `skip_record_error_reason`, `save_prefix` to the interface `ListTasks`
  - Add the response parameters `group_type`, `success_record_error_reason`, `skip_record_error_reason`, `save_prefix` to the interface `ShowTask`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListApiVersion`, `ShowApiVersion`, `SearchQueryScaleComputeFlavors`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ROMA

- _Features_
  - Support the service `ROMA Connect`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SA

- _Features_
  - Support the service `Situation Awareness`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.72 2021-12-17

### HuaweiCloud SDK CCE

- _Features_
  - Support the interface `ShowVersion`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudIDE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ShowInstance`:
    - Add the response parameters `bundle_url`, `visitor_id`, `visitor_name`, `visitor_domain_name`
    - Remove the response parameters `action_list`, `role`, `role_id`, `sub_org`
  - Changes of the interface `ListOrgInstances`:
    - Add the response parameters `visitor_id`, `visitor_name`, `visitor_domain_name`
    - Remove the response parameters `action_list`, `role`, `role_id`, `sub_org`
  - Changes of the interface `ListInstances`:
    - Add the response parameters `visitor_id`, `visitor_name`, `visitor_domain_name`
    - Remove the response parameters `action_list`, `role`, `role_id`, `sub_org`

### HuaweiCloud SDK CloudRTC

- _Features_
  - Support the interfaces `ListRtcAbnormalEvents`, `ListRtcAbnormalEventDimension`
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
  - Changes of the interface `ListEvents`:
    - Modify the type `string` -> `int32` of the response parameter `event_count`
    - Modify the type `string` -> `int64` of the response parameter `latest_occur_time`
  - Modify the type `string` -> `double` of the response parameter `variance` of the interface `BatchListMetricData`
  - Modify the type `string` -> `int32` of the response parameter `type_statistics` of the interface `ListResourceGroup`
  - Changes of the interface `ListEventDetail`:
    - Modify the type `string` -> `array` of the response parameter `event_users`
    - Modify the type `string` -> `array` of the response parameter `event_sources`

### HuaweiCloud SDK IoTAnalytics

- _Features_
  - Support the service `IoTAnalytics`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `input`, `edit_settings` to the interface `CreateEditingJob`
  - Add the response parameters `input`, `edit_settings` to the interface `ListEditingJob`

### HuaweiCloud SDK OCR

- _Features_
  - Support the following interfaces:
    - `RecognizeThailandIdcard`
    - `RecognizeMyanmarIdcard`
    - `RecognizeMyanmarDriverLicense`
    - `RecognizeChileIdCard`
    - `RecognizeThailandLicensePlate`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.71 2021-12-10

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Update the enum values to `[AND, OR, NOT]` of the request parameter `relation` of the interface `ListEvents`

### HuaweiCloud SDK APM

- _Features_
  - Support the interfaces `ShowMasterAddress`, `ListAkSk`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK AS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `allowed_address_pairs` to the interface `ListScalingGroups`
  - Add the request parameter `allowed_address_pairs` to the interface `CreateScalingGroup`
  - Add the request parameter `allowed_address_pairs` to the interface `UpdateScalingGroup`
  - Add the response parameter `allowed_address_pairs` to the interface `ShowScalingGroup`

### HuaweiCloud SDK BCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type `int32` -> `int64` of the response parameter `node_cnt` of the interface `ShowBlockchainDetail`
  - Add the request parameters `limit`, `offset` to the interface `ShowBlockchainFlavors`

### HuaweiCloud SDK CGS

- _Features_
  - Support the `Container Guard Service`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interfaces `ShowExtensionAuthorization`, `CreateExtensionAuthorization`, `CheckInstanceAccess`, `UpdateInstanceActivity`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudRTC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `stream_id` to the interface `ListRtcClientQosDetails`

### HuaweiCloud SDK CloudTable

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `CreateCluster`:
    - The request parameter `availability_zone`, `cu_num`, `net_id`, `security_group_id`, `tsd_num`, `vpc_id`, `version`, `type` changed to required
    - The request parameter `enable_lemon`, `enable_openTSDB` changed to not required
  - Changes of the interface `ListClusters`:
    - Add the response parameter `actions`
    - Modify the type `string` -> `object` of the response parameter `action_progress`
  - Changes of the interface `ShowClusterDetail`:
    - Add the response parameter `openTSDB_link`
    - Remove the response parameters `opentsdb_link`, `tsd_public_endpoint`
    - Modify the type `int32` -> `string` of the response parameter `cu_num`
    - Modify the type `int32` -> `string` of the response parameter `tsd_num`
    - Modify the type `int32` -> `string` of the response parameter `lemon_num`

### HuaweiCloud SDK CodeCheck

- _Features_
  - Support the interfaces `ShowTaskCmetrics`, `ListTemplateRules`, `ListTaskRuleset`
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `is_access`, `trigger_type` to the interface `ShowTaskDetail`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `readonly_domain_name` to the interface `ListInstances`
  - Add the response parameter `readonly_domain_name` to the interface `ShowInstance`

### HuaweiCloud SDK DDM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `time_zone` to the interface `CreateInstance`
  - Add the response parameters `instanceId`, `instanceName`, `jobId` to the interface `RestartInstance`

### HuaweiCloud SDK DSC

- _Features_
  - Support the interface `ShowOpenApiCalledRecords`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `readonly_password` to the interface `CreateDocWatermark`
  - Changes of the interface `ShowScanJobs`:
    - Add the request parameter `offset`
    - Remove the request parameter `page`
  - Changes of the interface `ShowScanJobResults`:
    - Add the request parameter `offset`
    - Remove the request parameter `page`

### HuaweiCloud SDK FRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the response parameters `landmark`, `gender`, `yaw_angle`, `roll_angle`, `pitch_angle`, `headpose`, `smile`, `skin`, `ethnic` from the interface `DetectFaceByFile`
  - Remove the response parameters `landmark`, `gender`, `yaw_angle`, `roll_angle`, `pitch_angle`, `headpose`, `smile`, `skin`, `ethnic` from the interface `DetectFaceByUrl`
  - Remove the response parameters `landmark`, `gender`, `yaw_angle`, `roll_angle`, `pitch_angle`, `headpose`, `smile`, `skin`, `ethnic` from the interface `DetectFaceByBase64`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the following interfaces:
    - `ListInstanceTags`
    - `ListProjectTags`
    - `BatchTagAction`
    - `ShowInstanceMonitorExtend`
    - `UpdateInstanceMonitor`
- _Bug Fix_
  - None
- _Change_
  - Changes of the interface `ListGaussMySqlInstances`:
    - Add the request parameters `private_ip`, `tags`
    - Add the response parameter `tags`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `region` changed to required of the interface `ListFlavors`

### HuaweiCloud SDK GES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `CheckMetadata`

### HuaweiCloud SDK HiLens

- _Features_
  - Support the service `Huawei HiLens`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK KMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `encrypted_privatekey` to the interface `ImportKeyMaterial`

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `default_record_config` changed to required of the interface `CreateRecordRule`

### HuaweiCloud SDK LTS

- _Features_
  - Support the following interfaces:
    - `ListLogHistogram`
    - `ListHost`
    - `ListHostGroup`
    - `UpdateHostGroup`
    - `CreateHostGroup`
    - `DeleteHostGroup`
    - `ListAccessConfig`
    - `UpdateAccessConfig`
    - `CreateAccessConfig`
    - `DeleteAccessConfig`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `RestoreExistInstance`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RES

- _Features_
  - Support the service `Recommender System`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SWR

- _Features_
  - Support the interface `ListQuotas`
- _Bug Fix_
  - None
- _Change_
  - Modify the name `UpdateNamespaceAuthReq` -> `UpdateNamespaceAuthRequestBody` of the request body of the interface `UpdateNamespaceAuth`

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `to`, `from` changed to required of the interface `ListStatistics`
  - The request parameter `from`, `to` changed to required of the interface `ListQpsTimeline`
  - The request parameter `from`, `to` changed to required of the interface `ListBandwidthTimeline`
  - The request parameter `from`, `to` changed to required of the interface `ListTopAbnormal`
  - Add the response parameter `cookie` to the interface `ShowEvent`
  - Changes of the interface `CreatePremiumHost`:
    - Add the request parameter `Content-Type`
    - Modify the type `string` -> `enum` of the request parameter `type`
  - Add the request parameter `Content-Type` to the interface `ListPremiumHost`
  - Changes of the interface `UpdatePremiumHost`:
    - Add the request parameter `Content-Type`
    - Modify the type `string` -> `enum` of the response parameter `type`
  - Add the request parameter `Content-Type` to the interface `DeletePremiumHost`
  - Changes of the interface `ShowPremiumHost`:
    - Add the request parameter `Content-Type`
    - Modify the type `string` -> `enum` of the response parameter `type`
  - Add the request parameter `Content-Type` to the interface `UpdatePremiumHostProtectStatus`

# 3.0.70 2021-11-29

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `roma_app_type` to the interface `ResettingAppSecretV2`.

### HuaweiCloud SDK BCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type of the response parameter `values` of the interface `ListEntityMetric`: `object` -> `array`

### HuaweiCloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `provider_id` to the interface `ListBackups`.

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `cidrs` to the interface `ShowCluster`.

### HuaweiCloud SDK CloudTable

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the name of the request parameter of the interface `CreateCluster`: `enable_opentsdb` -> `enable_openTSDB`
  - Modify the name of the response parameter of the interface `ListClusters` and `ShowClusterDetail`: `enable_opentsdb` -> `enable_openTSDB`

### HuaweiCloud SDK DBSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the name of the response parameter of the interfaces `SwitchAgent` and `SwitchRiskRule`: `status` -> `result`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `port` to the interface `UpdateInstance`.

### HuaweiCloud SDK DSC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `start_time` to the interface `ShowScanJobs`.

### HuaweiCloud SDK EVS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `CinderExportToImage`.

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `os:scheduler_hints` to the interfaces `NovaShowServer` and `NovaListServersDetails`.

### HuaweiCloud SDK ELB

- _Features_
  - Support the following interfaces:
    - `ListApiVersions`
    - `ListSecurityPolicies`
    - `CreateSecurityPolicy`
    - `ShowSecurityPolicy`
    - `UpdateSecurityPolicy`
    - `DeleteSecurityPolicy`
    - `ListSystemSecurityPolicies`
    - `ListQuotaDetails`
    - `ChangeLoadbalancerChargeMode`
    - `BatchUpdatePoliciesPriority`
    - `UpdateIpList`
    - `BatchDeleteIpList`
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ShowQuotaDefaults`.
  - Add the response parameters `flavor_sold_out` and `lcu` to the interfaces `ListFlavors` and `ShowFlavor`, and remove the response parameter `availability_zone_ids`.
  - Add the response parameter `members_per_pool` to the interface `ShowQuota`.
  - Add the request parameters `enc_certificate` and `enc_private_key` to the interfaces `CreateCertificate` and `UpdateCertificate`.
  - Add the response parameters `enc_certificate` and `enc_private_key` to the interfaces `ListCertificates` and `ShowCertificate`.
  - Add the request parameters `prepaid_options`, `autoscaling` and `id` to the interface `CreateLoadBalancer`.
  - Add the request parameters `elb_virsubnet_type` and `autoscaling` and the response parameters `autoscaling` and `ip_version` to the interface `ListLoadBalancers`.
  - Add the request parameters `elb_virsubnet_type` and `autoscaling` and the response parameters `loadbalancer_id`, `order_id`, `autoscaling` and `ip_version` to the interface `UpdateLoadBalancer`.
  - Add the response parameters `autoscaling` and `ip_version` to the interface `ShowLoadBalancer`.
  - Add the response parameters `id`, `type` and `provisioning_status` to the interface `ShowLoadBalancerStatus`.
  - Add the request parameters `security_policy_id` and `enhance_l7policy_enable` to the interface `CreateListener`.
  - Add the request parameters `enhance_l7policy_enable` and `member_instance_id` and the response parameters `security_policy_id`, `transparent_client_ip_enable` and `enhance_l7policy_enable` to the interface `ListListeners`.
  - Add the request parameters `enhance_l7policy_enable` and `member_instance_id` and the response parameters `security_policy_id`, `transparent_client_ip_enable` and `enhance_l7policy_enable` to the interface `UpdateListener`.
  - Add the response parameters `security_policy_id`, `transparent_client_ip_enable` and `enhance_l7policy_enable` to the interface `ShowListener`.
  - Add the request parameters `listener_id` and `member_instance_id` to the interface `ListPools`.
  - Add the request parameters `ip_version` and `member_type` and the response parameters `member_type` and `instance_id` to the interface `ListMembers`.
  - Add the response parameters `member_type` and `instance_id` to the interfaces `UpdateMember`, `ShowMember` and `ListAllMembers`.
  - Add the request parameters `priority`, `redirect_url_config`, `fixed_response_config` and `conditions` to the interface `CreateL7Policy`.
  - Add the request parameter `priority` and the response parameters `redirect_url_config` and `fixed_response_config` to the interface `ListL7Policies`.
  - Add the request parameters `priority`, `redirect_url_config`, `fixed_response_config` and `rules` and the response parameters `member_type` and `instance_id` to the interface `UpdateL7Policy`.
  - Add the response parameters `redirect_url_config` and `fixed_response_config` to the interface `ShowL7Policy`.
  - Add the request parameter `conditions` to the interface `CreateL7Rule`.
  - Add the response parameter `conditions` to the interfaces `ListL7Rules` and `ShowL7Rule`.
  - Add the request and response parameter `conditions` to the interface `UpdateL7Rule`.

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `ListVersionAliases` to the interface `ListVersionAliases`.
  - Update the request parameter `name` to required of the interfaces  `CreateDependency` and `UpdateDependency`.
  - Update the request parameters `name` and `content` to required of the interface `CreateEvent`.

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `enable_force_switch` to the interface `CreateInstance`.

### HuaweiCloud SDK GES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type of the request parameter `graphSizeTypeIndex` of the interface `CreateGraph`: `integer` -> `string`

### HuaweiCloud SDK KMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Update the request parameter `key_alias` to required of the interface `CreateKey`.
  - Update the request parameter `key_id` to required of the interfaces `EnableKey`, `CancelKeyDeletion`, `ListKeys`, `ListKeyDetail`, `ShowPublicKey`, `ListGrants`, `DeleteImportedKeyMaterial`, `EnableKeyRotation`, `DisableKeyRotation` and `ShowKeyRotationStatus`.
  - Update the request parameters `key_id` and `pending_days` to required of the interface `DeleteKey`.
  - Add the request parameter `enterprise_project_id` to the interface `ListKeys`.
  - Update the request parameter `random_data_length` to required of the interface `CreateRandom`.
  - Update the request parameters `key_id` and `datakey_length` to required of the interfaces `CreateDatakey` and `CreateDatakeyWithoutPlaintext`.
  - Update the request parameters `key_id`, `plain_text` and `datakey_plain_length` to required of the interface `EncryptDatakey`.
  - Update the request parameters `key_id`, `cipher_text` and `datakey_cipher_length` to required of the interface `DecryptDatakey`.
  - Update the request parameters `key_id` and `key_alias` to required of the interface `UpdateKeyAlias`.
  - Update the request parameters `key_id` and `key_description` to required of the interface `UpdateKeyDescription`.
  - Update the request parameters `key_id`, `grantee_principal` and `operations` to required of the interface `CreateGrant`.
  - Update the request parameters `key_id` and `grant_id` to required of the interfaces `CancelGrant` and `CancelSelfGrant`.
  - Update the request parameters `key_id` and `plain_text` to required of the interface `EncryptData`.
  - Update the request parameter `cipher_text` to required of the interface `DecryptData`.
  - Update the request parameters `key_id` and `wrapping_algorithm` to required of the interface `CreateParametersForImport`.
  - Update the request parameters `key_id`, `import_token` and `encrypted_key_material` to required of the interface `ImportKeyMaterial`.
  - Update the request parameters `key_id` and `rotation_interval` to required of the interface `UpdateKeyRotationInterval`.
  - Add the request parameter `sequence` to the interface `CreateKmsTag`.

### HuaweiCloud SDK RDS

- _Features_
  - Support the following interfaces:
    - `ChangeProxyScale`
    - `SearchQueryScaleFlavors`
    - `ShowInformationAboutDatabaseProxy`
    - `StartDatabaseProxy`
    - `StopDatabaseProxy`
    - `UpdateReadWeight`
    - `ChangeTheDelayThreshold`
    - `ShowDrReplicaStatus`
- _Bug Fix_
  - None
- _Change_
  - Modify the type of the response parameter `size` of the interface `ListPostgresqlDatabases`: `int32` -> `int64`

### HuaweiCloud SDK SMS

- _Features_
  - None
- _Bug Fix_
  - Fix the problem that the enumeration value contains the Chinese description and causes the parameter error.
- _Change_
  - None

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `items` to the interface `ListIgnoreRule`.
  - Add the request parameter `attacks` to the interface `ListEvent`.
  - Add the response parameter `host_id` to the interface `ShowEvent`.
  - Add the response parameter `certificatename` to the interface `UpdateHost`.

# 3.0.69 2021-11-25

### HuaweiCloud SDK AOM

- _Features_
  - Support the service `Cloud Bastion Host`.
- _Bug Fix_
  - None
- _Change_
  - Modify the type of the response parameter `resources` of the interfaces `ListAlarmRule` and `ShowAlarmRule`: `string` -> `array`

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `CheckBackendConnectivity`.

### HuaweiCloud SDK APM

- _Features_
  - Support the service `Application Performance Management`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BCS

- _Features_
  - Support the service `Application Performance Management`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `statistic_type` and response parameter `bill_date` to the interface `ListCustomerselfResourceRecordDetails`.

### HuaweiCloud SDK CBH

- _Features_
  - Support the service `Cloud Bastion Host`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `platformVersion` to the interface `ShowCluster`.
  - Add the enumeration values `RollingBack` and `RollbackFailed` to the request parameter `status` of the interface `ListClusters`.

### HuaweiCloud SDK CloudRTC

- _Features_
  - Support the following interfaces:
    - `ListRtcRealtimeScaleDimension`
    - `ListRtcRealtimeQuality`
    - `ListRtcRealtimeNetwork`
    - `ListRtcHistoryUsage`
    - `ListRtcHistoryScale`
    - `ListRtcHistoryQuality`
    - `ListRtcClientQosDetails`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudTable

- _Features_
  - Support the service `CloudTable`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CodeCheck

- _Features_
  - Support CodeCheck service.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DAS

- _Features_
  - None
- _Bug Fix_
  - Correct the enumeration value of the request parameter `X-Language` of some interfaces.
- _Change_
  - None

### HuaweiCloud SDK DBSS

- _Features_
  - Support the `Database Security Service`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `tags` to the interfaces `CreateInstance` and `ListInstances`.

### HuaweiCloud SDK DeH

- _Features_
  - Support the service `Dedicated Host`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request and response parameter `alias` to the interfaces `CreatePrePaidPublicip` and `CreatePublicip`.
  - Add the response parameter `alias` to the interfaces `ShowPublicip` and `UpdatePublicip`.

### HuaweiCloud SDK GES

- _Features_
  - Support the interfaces `ResizeGraph`, `ExpandGraph` and `UploadFromObs`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK LTS

- _Features_
  - Support the following interfaces:
    - `CreateTransfer`
    - `DeleteTransfer`
    - `UpdateTransfer`
    - `ListTransfers`
    - `ListLogStreams`
    - `RegisterDmsKafkaInstance`
    - `CreateNotificationTemplate`
    - `UpdateNotificationTemplate`
    - `ListNotificationTemplates`
    - `DeleteNotificationTemplate`
    - `ShowNotificationTemplate`
    - `ListNotificationTemplate`
    - `UpdateAlarmRuleStatus`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK KMS

- _Features_
  - Support the interfaces of version `V2`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK NLP

- _Features_
  - Support the service `Natural Language Processing`.
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
  - Remove the response parameter `extracted_data` of the interface `RecognizeHandwriting`.

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `sort` to the interface `ListSlowlogStatistics`.

### HuaweiCloud SDK SIS

- _Features_
  - Support the `Voice Interaction Service`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SFSTurbo

- _Features_
  - Support the service `Scalable File Service - Turbo`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK TMS

- _Features_
  - Support the interface `ShowTagQuota`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VPCEP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type of the response parameters `created_at` and `updated_at` of the interfaces `ListServicePublicDetails`, `ListServiceDetails`, `ListServiceConnections`, `AcceptOrRejectEndpoint`, `ListEndpoints`, `UpdateEndpointWhite` and `ListEndpointInfoDetails`.
  - Update the request parameters `vpc_id` and `port_id` to required of the interface `CreateEndpointService`.
  - Remove the response parameter `error` of the interface `AcceptOrRejectEndpoint`.
  - Modify the type of the response parameter `updated` of the interfaces `ListVersionDetails` and `ListSpecifiedVersionDetails`: `datetime` -> `string`
  - Update the request parameter `action` to required of the interfaces `ListResourceInstances` and `BatchAddOrRemoveResourceInstance`.

### HuaweiCloud SDK WAF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `from` and `to` to the interface `ListEvent`.
  - Add the request parameter `name` to the interface `ListWhiteblackipRule`.

# 3.0.68 2021-11-12

### HuaweiCloud SDK AOM

- _Features_
  - Support the following interfaces:
    - `ListRangeQueryAomPromGet`
    - `ListRangeQueryAomPromPost`
    - `ListInstantQueryAomPromGet`
    - `ListInstantQueryAomPromPost`
    - `ListLabelValuesAomPromGet`
    - `ListLabelsAomPromGet`
    - `ListLabelsAomPromPost`
    - `ListMetadataAomPromGet`
    - `DeleteAlarmRules`
    - `ListLogItems`
    - `ListEvents`
    - `CountEvents`
    - `PushEvents`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `customSan` to the interface `UpdateNode`.

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `force_redirect_https` to the interface `UpdateHttpsInfo`.

### HuaweiCloud SDK CloudDeploy

- _Features_
  - Support the service `CloudDeploy`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the name of the response parameter of the interface `ListAuditLogs`: `total_count` -> `total_record`.

### HuaweiCloud SDK DSC

- _Features_
  - Support the interfaces `ShowScanJobs` and `ShowScanJobResults`.
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `marked_file_password` to the interface `CreateDocWatermark`.

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `offset` and `limit`.
  - Add the response parameters `id` and `spec_code`.

### HuaweiCloud SDK GES

- _Features_
  - Support `Graph Engine Service`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameters `sim_card_id`, `partner`, `package_type` and `sim_type` from the interface `ListProPricePlans`.
  - Remove the request parameter `tag_id` from the interface `ListSimCards`.
  - Remove the request parameter `sim_price_plan_id` from the interface `ListSimPricePlans`.
  - Remove the request parameter `price_plan_list` from the interfaces `StopSimCard` and `ResetSimCard`.
  - Remove the response parameters `sn`, `supply_code`, `bundle_id` and `test_type` from the interfaces `ShowSimCard` and `ListSimCards`.
  - Remove the response parameter `sim_price_plan_list` from the interface `StopSimCard`.
  - Remove the response parameter `order_id` from the interface `ListSimPools`.
  - Remove the response parameters `partner` and `partner_pid` from the interface `ListSimPricePlans`.

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `results` to the interface `ShowJob`.

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `country` and `protocol` to the interface `ListBandwidthDetail` and `ListUsersOfStream`.
  - Add the request parameter `protocol` to the interface `ListDomainTrafficDetail`, `ListDomainBandwidthPeak` and `ListDomainTrafficSummary`.
  - Add the request parameter `stream` to the interface `ListTranscodeData`.
  - Add the request parameters `stream`, `start_time` and `end_time` to the interface `ListHistoryStreams`.

### HuaweiCloud SDK LTS

- _Features_
  - Support the following interfaces:
    - `ShowStructTemplate`
    - `CreateStructTemplate`
    - `UpdateStructTemplate`
    - `DeleteStructTemplate`
    - `ShowAomMappingRules`
    - `CreateAomMappingRules`
    - `UpdateAomMappingRules`
    - `DeleteAomMappingRules`
    - `ShowAomMappingRule`
    - `ListNotificationTopics`
    - `CreateSqlAlarmRule`
    - `UpdateSqlAlarmRule`
    - `ListSqlAlarmRules`
    - `DeleteSqlAlarmRule`
    - `CreateKeywordsAlarmRule`
    - `UpdateKeywordsAlarmRule`
    - `ListKeywordsAlarmRules`
    - `DeleteKeywordsAlarmRule`
    - `ListActiveOrHistoryAlarms`
    - `DeleteActiveAlarms`
    - `ListCharts`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Meeting

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the request parameter `conferenceType` from the interface `CreateMeeting`.
  - Add the response parameter `cycleSubConfID` to the interface `CreateRecurringMeeting`.

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the name of the request parameter of the interface `CreateEditingJob`: `const` -> `consts`
  - Remove the request parameter `index`, and add the request parameters `overlay_input`, `const` and `mix` to the interface `CreateEditingJob`.
  - Add the response parameter `output` to the interface `ListEditingJob`.
  - Add the response parameters `hls_init_count` and `hls_init_interval`, add the optional value `EFFICIENCY` to the request parameter `video_enhance` of the interface `CreateTranscodingTask`.

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `job_id`, `user` and `queue` to the interface(V2) `GetJobExeListNew`.

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `confidence` to the interface `RecognizeGeneralTable`.

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interface `CreateSystemIssueV4`.
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `sequence` to the interface `ListIrs`.
  - Add the request parameter `status_id` to the interface `BatchUpdateIrs`.

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListSlowLogsNew`, `ListErrorLogsNew` and `UpgradeDbVersion`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VAS

- _Features_
  - Support `Video Analysis Service`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VPC

- _Features_
  - Support interfaces(V3): `AddVpcExtendCidr`、`RemoveVpcExtendCidr`、`ListVpcs`、`ShowVpc`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.67 2021-10-25

### HuaweiCloud SDK AOM

- _Features_
  - Support the following interfaces:
    - `ListServiceDiscoveryRules`
    - `DeleteserviceDiscoveryRules`
    - `AddAlarmRule`
    - `ListAlarmRule`
    - `UpdateAlarmRule`
    - `DeleteAlarmRule`
    - `ShowAlarmRule`
- _Bug Fix_
  - [Issue #43](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/43):Fix the issue of incorrect type of the response parameter `offset` of the interface `ListSeries`.
- _Change_
  - None

### HuaweiCloud SDK BCS

- _Features_
  - Support the interface `ShowBlockchainFlavors`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `account_manager_id` and `account_manager_name` to the interface `ListIndirectPartners`.

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `create_time` and response parameter `task_type` to the interface `ShowHistoryTaskDetails`.
  - Remove the request parameter `create_time` from the interface `ShowHistoryTasks`.

### HuaweiCloud SDK DNS

- _Features_
  - Support the interface `ShowDomainQuota`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `bandwidth_type` to the interface `CreateSharedBandwidth`.

### HuaweiCloud SDK FRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `single` to the interfaces `AddFacesByFile`, `AddFacesByBase64` and `AddFacesByUrl`.

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type of request and response parameters `num` and `size` of the interface `CreateInstance`: `integer` -> `string`.

### HuaweiCloud SDK GSL

- _Features_
  - Support the service `Global SIM Link`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ImageSearch

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the name of the request parameter of the interface `RunSearchPicture`: `isCrop` -> `is_crop`
  - Add the request parameter `box` to the interface `RunSearchPicture`.

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `current_task`, `image_name` and `process_percent` to the interface `ShowJob`.

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `status` to the interface `ListDevices`.
  - Add the request parameter `file_path` to the interface `CreateRuleAction`.

### HuaweiCloud SDK Meeting

- _Features_
  - Support the interfaces `ShowQosThreshold` and `SetQosThreshold`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OCR

- _Features_
  - Support the interfaces `RecognizeInsurancePolicy`, `RecognizeFinancialStatement` and `RecognizeQualificationCertificate`.
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
  - Add the response parameter `database_name` to the interface `ShowBackupDownloadLink`.
  - Add the response parameter `max_iops` and `expiration_time` to the interface `ListInstances`.

### HuaweiCloud SDK SDRS

- _Features_
  - Support the `Storage Disaster Recovery Service`.
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.66 2021-10-19

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `backup_id` to the interface `ShowMigrationTask`.
  - Add the following response parameters to the interface `ListMigrationTask`:
    - `source_instance_name`
    - `source_instance_id`
    - `target_instance_addrs`
    - `target_instance_id`
  - Modify the type of the response parameter `total_usec_sum` of the interface `ListDiagnosisTasks`: `integer` -> `double`

### HuaweiCloud SDK DSC

- _Features_
  - Support the service `Data Security Center`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK EIP

- _Features_
  - Support the following interfaces:
    - `ListCommonPools`
    - `ListPublicBorderGroups`
    - `ListPublicipPool`
    - `ShowPublicipPool`
    - `ListShareBandwidthTypes`
- _Bug Fix_
  - None
- _Change_
  - Add the request parameter `allow_share_bandwidth_type_any` to the interface `ListPublicips`.
  - Modify the type of the request parameter `limit` of the interface `NeutronListFloatingIps`.
  - Modify the name of the request body of the interface `NeutronUpdateFloatingIp`: `floatingip` -> `NeutronUpdateFloatingIpRequestBody`
  - Add the response parameter `allow_share_bandwidth_types` to the interface `ShowPublicip`.

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `hls_init_count` and `hls_init_interval` to the interface `CreateTranscodingTask`.

### HuaweiCloud SDK VPCEP

- _Features_
  - Support the service `VPC Endpoint`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VSS

- _Features_
  - Support the `Vulnerability Scan Service`.
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.65 2021-10-11

### HuaweiCloud SDK Core

- _Features_
  - Support uploading files.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK APIG

- _Features_
  - Support the interfaces:
    - `CreateAppCodeV2`
    - `CreateAppCodeAutoV2`
    - `ListAppCodesV2`
    - `ShowDetailsOfAppCodeV2`
    - `DeleteAppCodeV2`
    - `DebugApiV2`
    - `BatchPublishOrOfflineApiV2`
    - `ListApiVersionsV2`
    - `ChangeApiVersionV2`
    - `ListApiRuntimeDefinitionV2`
    - `ListApiVersionDetailV2`
    - `DeleteApiByVersionIdV2`
    - `ListAclStrategiesV2`
    - `BatchDeleteAclV2`
    - `CreateAclStrategyV2`
    - `ShowDetailsOfAclPolicyV2`
    - `UpdateAclStrategyV2`
    - `DeleteAclV2`
    - `BatchDeleteApiAclBindingV2`
    - `CreateApiAclBindingV2`
    - `DeleteApiAclBindingV2`
    - `ListAclPolicyBindedToApiV2`
    - `ListApisBindedToAclPolicyV2`
    - `ListApisUnbindedToAclPolicyV2`
    - `ListCustomAuthorizersV2`
    - `CreateCustomAuthorizerV2`
    - `ShowDetailsOfCustomAuthorizersV2`
    - `UpdateCustomAuthorizerV2`
    - `DeleteCustomAuthorizerV2`
    - `ExportApiDefinitionsV2`
    - `ImportApiDefinitionsV2`
    - `CreateVpcChannelV2`
    - `ListVpcChannelsV2`
    - `ShowDetailsOfVpcChannelV2`
    - `DeleteVpcChannelV2`
    - `UpdateVpcChannelV2`
    - `AddingBackendInstancesV2`
    - `ListBackendInstancesV2`
    - `DeleteBackendInstanceV2`
    - `ListLatelyApiStatisticsV2`
    - `ListLatelyGroupStatisticsV2`
    - `CreateGatewayResponseV2`
    - `ListGatewayResponsesV2`
    - `ShowDetailsOfGatewayResponseV2`
    - `UpdateGatewayResponseV2`
    - `DeleteGatewayResponseV2`
    - `ShowDetailsOfGatewayResponseTypeV2`
    - `UpdateGatewayResponseTypeV2`
    - `DeleteGatewayResponseTypeV2`
    - `ListTagsV2`
    - `CreateFeatureV2`
    - `ListFeaturesV2`
    - `CreateInstanceV2`
    - `ListInstancesV2`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ListSkuInventories`.

### HuaweiCloud SDK CampusGo

- _Features_
  - Support the service `CampusGo`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the following response parameters to the interface `ShowTask`:
    - `create_time`
    - `description`
    - `operate_mode`
    - `related_temp_running_data`
    - `run_status`
    - `update_time`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Set the request parameter `reverse_binding` to `optional` of the interface `DisassociateServerVirtualIp`.

### HuaweiCloud SDK FRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the optional value to `2,4,6,7,8,11,12,13,21` of the request parameter `attributes` of the interfaces `DetectFaceByFile`,`DetectFaceByBase64` and `DetectFaceByUrl`.

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `instance_mode` to the interface `ListInstances`.

### HuaweiCloud SDK IoTEdge

- _Features_
  - Support the service `IoTEdge`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Meeting

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type of response parameter of the interface `SearchCorpDir`: `number` -> `integer`

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameter `vpcId` to the interface `ListClusters`, and modify the type of the response parameter `start_time` of this interface: `string` -> `integer`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the request parameters `unchangeable_param`,`dry_run` and `count` to the interface `CreateInstance`.
  - Add the response parameter `enable_ssl` to the interface `CreateRestoreInstance`.

# 3.0.64 2021-09-29

### HuaweiCloud SDK BSS

- _Features_
  - Support the interface `ListSubCustomerBillDetail`.
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ListSubCustomerResFeeRecords` and `ListFreeResources`.
  - Modify the name of the interface: `ListParnterAdjustRecords` -> `ListPartnerAdjustRecords`

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add request body to the interface `CreateTemp`.

### HuaweiCloud SDK DNS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the type of the response parameter `resource_detail` of the interface `ListTag`: `string` -> `object`
  - Modify the type of the response parameter `masters` of the interfaces `CreatePrivateZone`,`UpdatePublicZone` and `DeletePublicZone`: `string` -> `array`
  - Modify the type of the request parameter `ttl` of the interfaces `CreatePrivateZone` and `UpdatePublicZone`: `string` -> `integer`
  - Modify the type of the request parameters `limit` and `offset` of the interfaces `ListRecordSets`,`ListRecordSetsWithLine` and `ListRecordSetsByZone`: `string` -> `integer`
  - Add the response parameter `tags` to the interfaces `CreatePrivateZone`,`ListRecordSetsByZone`,`ShowRecordSetWithLine`,`ListPtrRecords` and `ListPublicZones`.

### HuaweiCloud SDK ECS

- _Features_
  - Support the following interfaces:
    - `ListServerTags`
    - `BatchAttachSharableVolumes`
    - `ShowServerAutoRecovery`
    - `BatchResetServersPassword`
    - `ReinstallServerWithoutCloudInit`
    - `ChangeServerOsWithoutCloudInit`
    - `BatchUpdateServersName`
    - `ShowServerPassword`
    - `AssociateServerVirtualIp`
    - `MigrateServer`
    - `ShowServerBlockDevice`
    - `DisassociateServerVirtualIp`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the name of the following interfaces:
    - `ShowMysqlEngineVersion` -> `ShowGaussMySqlEngineVersion`
    - `ShowMysqlFlavors` -> `ShowGaussMySqlFlavors`
    - `CreateMysqlInstance` -> `CreateGaussMySqlInstance`
    - `ShowMysqlInstanceList` -> `ListGaussMySqlInstances`
    - `DeleteMysqlInstance` -> `DeleteGaussMySqlInstance`
    - `ShowMysqlInstanceInfo` -> `ShowGaussMySqlInstanceInfo`
    - `CreateMysqlReadonlyNode` -> `CreateGaussMySqlReadonlyNode`
    - `DeleteMysqlReadonlyNode` -> `DeleteGaussMySqlReadonlyNode`
    - `ExpandMysqlInstanceVolume` -> `ExpandGaussMySqlInstanceVolume`
    - `UpdateMysqlBackupPolicy` -> `UpdateGaussMySqlBackupPolicy`
    - `UpdateMysqlInstanceName` -> `UpdateGaussMySqlInstanceName`
    - `ResetMysqlPassword` -> `ResetGaussMySqlPassword`
    - `ChangeMysqlInstanceSpecification` -> `ChangeGaussMySqlInstanceSpecification`
    - `ListDedicatedResources`  -> `ListGaussMySqlDedicatedResources`
    - `CreateMysqlProxy` -> `CreateGaussMySqlProxy`
    - `DeleteMysqlProxy` -> `DeleteGaussMySqlProxy`
    - `ShowMysqlProxy` -> `ShowGaussMySqlProxy`
    - `ShowMysqlProxyFlavors` -> `ShowGaussMySqlProxyFlavors`
    - `ExpandMysqlProxy` -> `ExpandGaussMySqlProxy`
    - `ListMysqlErrorLog` -> `ListGaussMySqlErrorLog`
    - `ListMysqlSlowLog` -> `ListGaussMySqlSlowLog`
    - `ShowMysqlProjectQuotas` -> `ShowGaussMySqlProjectQuotas`
    - `ShowMysqlQuotas` -> `ShowGaussMySqlQuotas`
    - `SetMysqlQuotas` -> `SetGaussMySqlQuotas`
    - `UpdateMysqlQuotas` -> `UpdateGaussMySqlQuotas`
    - `CreateMysqlBackup` -> `CreateGaussMySqlBackup`
    - `ShowMysqlBackupList` -> `ShowGaussMySqlBackupList`
    - `ShowMysqlBackupPolicy` -> `ShowGaussMySqlBackupPolicy`
    - `ListMysqlConfigurations` -> `ListGaussMySqlConfigurations`
    - `ShowMysqlJobInfo` -> `ShowGaussMySqlJobInfo`

### HuaweiCloud SDK ProjectMan

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `id` and `name` to the interface `ListIssueRecordsV4`.
  - Add the response parameter `status` to the interface `ListProjectIterationsV4`.

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the optional value `bigmen` to the response parameter `group_type` of the interface `ListFlavors`.

# 3.0.63 2021-09-26

### HuaweiCloud SDK DRS

- _Features_
  - Support the interface `BatchSetPolicy`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Meeting

- _Features_
  - Support the interfaces `InviteOperateVideo`,`SetSsoConfig` and `ShowSsoConfig`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK MPC

- _Features_
  - Support the interfaces `CreateEditingJob`,`ListEditingJob` and `DeleteEditingJob`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK WAF

- _Features_
  - Support the following interfaces:
    - `ListIgnoreRule`
    - `ListStatistics`
    - `ListQpsTimeline`
    - `ListBandwidthTimeline`
    - `ListResponseCodeTimeline`
    - `ListTopAbnormal`
    - `ShowConsoleConfig`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.0.62 2021-09-24

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - Fix the issue that the interface `ListRecordContents` cannot be found.
- _Change_
  - None

# 3.0.61 2021-09-24

### HuaweiCloud SDK BSS

- _Features_
  - Support the interfaces `ListParnterAdjustRecords` and `ListFreeResourceInfos`.
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ListSubCustomerBillDetail`.

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Modify the name of the interface: `ListFreeResources` -> `ListFreeResourceUsages`

### HuaweiCloud SDK CCE

- _Features_
  - Support the interface `ShowQuotas`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Classroom

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the optional request parameter `testcases` to the interface `ApplyJudgement`.

### HuaweiCloud SDK Cloudtest

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Set the request parameter `testcase_number` to `optional`, and remove the request parameter of the interface `ShowTestCaseDetailV2`.

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the service `GaussDB(for openGauss)`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Live

- _Features_
  - Support the interface `ListRecordContents`.
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SWR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the response parameters `domain_id`, `scanned` and `tag_type` to the interface `ListRepositoryTags`.

# 3.0.60 2021-09-16

### HuaweiCloud SDK CCE

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameter `platformVersion` to the interface `ShowCluster`.

### HuaweiCloud SDK CDN

- _Features_
    - Support the interface `ShowDomainStats`.
- _Bug Fix_
    - Fix the issue of no response data when calling the interface `ShowDomainItemLocationDetails`.
- _Change_
    - None

### HuaweiCloud SDK CloudRTC
- _Features_
    - Support the service `CloudRTC`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DDM

- _Features_
    - Support the interfaces `ListSlowLog` and `ListReadWriteRatio`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK GSL

- _Features_
    - Support the service `Global SIM Link`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK IMS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the optional request parameter `__support_amd` to the interface `CreateDataImage`.
    - Add the response parameter `__support_amd` to the interface `ListImages`.

### HuaweiCloud SDK KMS

- _Features_
    - Support the interfaces `ShowPublicKey` and `Sign`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK OCR

- _Features_
    - Support the interface `RecognizeInvoiceVerification`.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.59 2021-09-10

### HuaweiCloud SDK BSS

- _Features_
    - Support the interfaces `ListSubCustomerBillDetail`, `ListResourceUsageSummary` and `ListResourceUsage`.
- _Bug Fix_
    - None
- _Change_
    - Remove the interface `ListResourceUsages`.

### HuaweiCloud SDK BSSINTL

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the interface `ListResourceUsages`.

### HuaweiCloud SDK CBS

- _Features_
    - Support the interfaces `CreateTbSession`, `ExecuteTbSession` and `DeleteTbSession`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CCE

- _Features_
    - Support the interfaces `AddNode` and `ResetNode`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CDN

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the following response parameters to the interface `CreateDomain`:
        - `range_status`
        - `follow_status`
        - `origin_status`
        - `auto_refresh_preheat`
    - Add the required request parameter `switch` and optional request parameter `redirect_type` to the interface `UpdateDomainMultiCertificates`.
    - Add the required request parameter `switch` and optional request parameter `redirect_type` to the interface `UpdateHttpsInfo`.
    - Add the optional request parameter `create_time` to the interface `ShowHistoryTasks`.

### HuaweiCloud SDK DAS

- _Features_
    - Support the `Data Admin Service`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DDS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameters `status` and `fail_reason` to the interface `ShowJobDetail`.

### HuaweiCloud SDK EVS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Set the request parameter `size` of the interface `CreateVolume` to `required`.

### HuaweiCloud SDK IVS

- _Features_
    - Support the service `Identity Verification Solution`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support the following interfaces:
        - `AddMaterial`
        - `CreateRecurringMeeting`
        - `UpdateRecurringMeeting`
        - `CancelRecurringMeeting`
        - `CancelRecurringSubMeeting`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK OCR

- _Features_
    - Support the interface `RecognizeInvoiceVerification`.
- _Bug Fix_
    - None
- _Change_
    - Add the optional request parameter `return_verification` to the interface `RecognizeIdCard`.

### HuaweiCloud SDK RDS

- _Features_
    - Support the interface `UpdateDatabase`.
- _Bug Fix_
    - None
- _Change_
    - Add the response parameter `alias` to the interface `ListInstances`.
    - Add the optional request parameter `comment` to the interface `CreateDatabase`.

# 3.0.58 2021-08-31

### HuaweiCloud SDK CodeCraft

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the request parameter `score` of the interfaces `CreateCompetitionScore` and `UpdateCompetitionScore`: `string` -> `double`.

### HuaweiCloud SDK CPTS

- _Features_
    - Support the service `CPTS`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK FRS

- _Features_
    - Support the following interfaces:
        - `DetectLiveByUrl`
        - `DetectLiveFaceByUrl`
        - `DetectLiveByFile`
        - `DetectLiveFaceByFile`
        - `DetectLiveByBase64`
        - `DetectLiveFaceByBase64`
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
    - Add the response parameters `video_frame_rate`,`audio_frame_rate`,`audio_bitrate` and `resolution`.

### HuaweiCloud SDK GaussDB

- _Features_
    - Support the service `GaussDB`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK MRS

- _Features_
    - Support the `MapReduce Service`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK SCM

- _Features_
    - Support the service `SSL Certificate Manager`.
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
    - Add the request parameters `enterprise_project_id`, `name` and `fuzzy_name` to the interface `ListTopics`.
    - Add the request parameters `protocol`, `status` and `endpoint` to the interface `ListSubscriptions`.

# 3.0.57 2021-08-25

### HuaweiCloud SDK CBS

- _Features_
    - Support the `Conversational Bot Service`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CodeCraft

- _Features_
    - Support the `Conversational Bot Service`.
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the request parameter `score` of the interfaces `CreateCompetitionScore` and `UpdateCompetitionScore`: `float` -> `string`

### HuaweiCloud SDK DDS

- _Features_
    - Support the following interfaces:
        - `ShowJobDetail`
        - `SwitchSlowlogDesensitization`
        - `ListFlavorInfos`
        - `UpdateInstanceRemark`
- _Bug Fix_
    - None
- _Change_
    - Add the response parameter `job_id` to the interfaces `RestoreInstance`, `CreateManualBackup` and `RestoreInstanceFromCollection`.
    - Add the response parameter `remark` to the interface `ListInstances`.

### HuaweiCloud SDK ECS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the following response parameters to the interface `ListServerInterfaces`:
        - `delete_on_termination`
        - `driver_mode`
        - `min_rate`
        - `multiqueue_num`
        - `pci_address`
    - Add the response parameters `cpu_options` and `hypervisor` to the interface `ListServersDetails`.

### HuaweiCloud SDK EIP

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request and response parameter `public_border_group` to the interface `BatchCreateSharedBandwidths`.
    - Add the response parameter `public_border_group` to the interface `AddPublicipsIntoSharedBandwidth`.

### HuaweiCloud SDK FRS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the name of the interface: `AuthorizeFaceRecognitionService` -> `ShowSubscribes`.

### HuaweiCloud SDK FunctionGraph

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameters `function_urn` and `type` to the interface `ExportFunction`.
    - -The optional value of the request parameter `filter` of the interface `ListStatistics` is modified to [`monitor_data`, `monthly_report`]

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
    - Support the following interfaces:
        - `ListDedicatedResources`
        - `ListFlavorInfos`
        - `ListConfigurationTemplates`
        - `ListInstancesByResourceTags`
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `dedicated_resource_id` to the interface `CreateInstance`.
    - Add the response parameter `dedicated_resource_id` to the interface `ListInstances`.

### HuaweiCloud SDK ImageSearch

- _Features_
    - Support the service `ImageSearch`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Live

- _Features_
    - Support the interface `RunRecord`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support the following interfaces:
        - `SearchStatisticConferenceInfo`
        - `SearchStatisticConferenceParticipant`
        - `SearchStatisticUserInfo`
        - `SearchStatisticResourceInfo`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK MPC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the request parameter `aspect_ratio` of the interface `CreateTransTemplate`.
    - Remove the request parameter `GOP_structure` and `sr_factor` of the interface `CreateTranscodingTask`.
    - Remove the request parameter `GOP_structure` and `sr_factor` of the interface `CreateTemplateGroup`.

### HuaweiCloud SDK RDS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the name of the response parameter of the interface `ListJobInfoDetail`: `taskDetail` -> `task_detail`
    - Add the response parameter `count` to the interface `ListJobInfoDetail`.

# 3.0.56 2021-08-17

### HuaweiCloud SDK AntiDDoS

- _Features_
    - Support the service `Anti-DDoS`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CCE

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the following response parameters to the interface `ListNodePools`:
        - `annotations`
        - `updateTimestamp`
        - `creationTimestamp`
        - `creatingNode`
        - `deletingNode`
        - `conditions`
        - `enterprise_project_id`
    - Add the response parameters `orderID` and `upgradefrom` to the interface `ListClusters`.

### HuaweiCloud SDK ECS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameter `ecs:instance_architecture` to the interface `ListServerResizeFlavors`.
    - Add the request parameters `tenancy` and `dedicated_host_id` to the interface `NovaCreateServers`.

### HuaweiCloud SDK ELB

- _Features_
    - None
- _Bug Fix_
    - Fix the problem of abnormal creation of LB.
- _Change_
    - None

### HuaweiCloud SDK Live

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the request parameter `key` from the interface `CreateRecordCallbackConfig`.
    - Add the response parameter `sign_type` to the interface `ListRecordCallbackConfigs`.
    - Add the response parameters `status_describe` and `service_area` to the interface `ShowDomain`.

### HuaweiCloud SDK RDS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `readonly` to the interfaces `AllowSqlserverDbUserPrivilege` and `RevokeSqlserverDbUserPrivilege`.

### HuaweiCloud SDK SMS

- _Features_
    - Support `Server Migration Service`.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.55 2021-08-10

### HuaweiCloud SDK Services

- _Features_
    - None
- _Bug Fix_
    - Delete unused packages in `requirements.txt` of each service.
- _Change_
    - None

### HuaweiCloud SDK AS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the request parameters `key` and `value` of the interface `ListResourceInstances` as required parameters.

### HuaweiCloud SDK CloudBuild

- _Features_
    - Support the service `CloudBuild`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK EIP

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the name of the response parameter of the interfaces `ListBandwidths` and `ShowPublicip`: `publicip_border_group` -> `public_border_group`

### HuaweiCloud SDK EVS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `server_id` to the interface `ListVolumes`.

### HuaweiCloud SDK FRS

- _Features_
    - Support the `Face Recognition Service`.
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
    - Remove the response parameter `order_id` from the interface `CreateDeployment`.

### HuaweiCloud SDK IEC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameters `permission_type`,`display_name`,`catalog` to the interface `KeystoneListPermissions`.
    - Add the request and response parameter `sso_type` to the interface `KeystoneCreateIdentityProvider`.

### HuaweiCloud SDK IMS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the request parameter `value` of the interface `UpdateImage` as a required parameter.

### HuaweiCloud SDK Kafka

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `new_partition_numbers` to the interface `UpdateInstanceTopic`.

### HuaweiCloud SDK LTS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `highlight` to the interface `ListLogs`.
    - Add the optional value `backwards` to the request parameter `search_type` of the interface `ListLogs`.

### HuaweiCloud SDK MPC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the response parameter `dynamic_range` from the interface `ListTranscodingTask`.
    - Remove the request parameter `tenant_id` from the interface `CreateTransTemplate`.
    - Remove the request parameters `percent` and `frame_type` from the interface `CreateThumbnailsTask`.
    - Remove the request parameter `black_enhance` from the interface `CreateTranscodingTask`.

### HuaweiCloud SDK OCR

- _Features_
    - Support the following interfaces:
        - `RecognizeGeneralText`
        - `RecognizeQuotaInvoice`
        - `RecognizeIdCard`
        - `RecognizeHandwriting`
        - `RecognizeVehicleLicense`
        - `RecognizeTransportationLicense`
        - `RecognizeTaxiInvoice`
        - `RecognizeAutoClassification`
        - `RecognizeTollInvoice`
        - `RecognizeMvsInvoice`
        - `RecognizeLicensePlate`
        - `RecognizeFlightItinerary`
        - `RecognizeBusinessLicense`
        - `RecognizeWebImage`
        - `RecognizeDriverLicense`
        - `RecognizeBusinessCard`
        - `RecognizeTrainTicket`
        - `RecognizeVin`
        - `RecognizePassport`
        - `RecognizeBankcard`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK SWR

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the following response parameters to the interface `ShowAccessDomain`:
        - `namespace`
        - `repository`
        - `access_domain`
        - `permit`
        - `deadline`
        - `description`
        - `creator_id`
        - `creator_name`
        - `created`
        - `updated`
        - `status`

### HuaweiCloud SDK VPC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `enable_dhcp` to the interface `NeutronListSubnets`.
    - Add the response parameter `security_groups_links` to the interface `NeutronListSecurityGroups`.

# 3.0.54 2021-07-27

### HuaweiCloud SDK Classroom

- _Features_
    - Support the interfaces `ApplyJudgement`,`ShowJudgementDetail`,`ShowJudgementFile`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Cloudtest

- _Features_
    - None
- _Bug Fix_
    - Fix the issue of failing to call the service `Cloudtest` with the endpoint `cn-north-1`.
- _Change_
    - None

### HuaweiCloud SDK IEC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameter `order_id` to the interface `CreateDeployment`.
    - Add the response parameter `with_prefix` to the interface `ListDeployments`.

# 3.0.53 2021-07-26

### HuaweiCloud SDK CDN

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the response parameters `urls`, `task_id` of the interface `ShowHistoryTasks`.
    - Remove the response parameters `task_id`, `process_reason`, modify the type of the request parameter `process_reason`:`integer`->`string`
    - Remove the request parameters `user_domain_id`, `task_id` of the interface `ShowTopUrl`.

### HuaweiCloud SDK CloudPipeline

- _Features_
    - Support the interface `ShowPlans`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Cloudtest

- _Features_
    - Support the interface `ListPipelineSimpleInfo`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DCS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `dcs_cluster_proxy2_node` to the interface `UpdateConfigurations`.

### HuaweiCloud SDK DDM

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the request parameter `extend_authority` of the interface `UpdateUser`.

### HuaweiCloud SDK DDS

- _Features_
    - Support the interface `UpdateClientNetwork`.
- _Bug Fix_
    - None
- _Change_
    - Change the request parameters `start_time`,`stop_time` from `optional` to `required` of the interface `SetBalancerWindow`.
    - Add the request parameter `port` and response parameter `port` to the interface `CreateInstance`.

### HuaweiCloud SDK FunctionGraph

- _Features_
    - Support the interface `EnableLtsLogs`.
- _Bug Fix_
    - None
- _Change_
    - Add the response parameters `concurrent_num`,`id`,`encrypted_user_data`.
    - Add the response parameters `func_vpc_id`,`encrypted_user_data`,`long_time`,`log_group_id`,`log_stream_id`,`type` to the interface `ListFunctions`, and remove the response parameters `version_description`,`last_modified_utc`,`dependencies` of this interface.
    - Remove the request parameter `name`,`last_modified`,`alias_urn` of the interface `UpdateVersionAlias`.
    - Add the response parameters `encrypted_user_data`,`long_time`,`log_group_id`,`log_stream_id`,`type` of the interface `ShowFunctionConfig`, and remove the response parameters `version_description`,`concurrency` of this interface.
    - Add the response parameters `encrypted_user_data`,`long_time`,`log_group_id`,`log_stream_id`,`type` to the interface `ListFunctionVersions`, and remove the response parameters `version_description`,`concurrency`,`depend_list`.
    - Add the response parameters `encrypted_user_data`,`long_time`,`log_group_id`,`log_stream_id`,`type` to the interface `ListFunctionVersions`, remove the response parameters `last_modified_utc`,`concurrency`.
    - Modify the type of the request parameter `size` of the interface `UpdateTrigger`: `string`->`integer`
    - Modify the type of the response parameter `size` of the interface `ShowDependency`: `string`->`integer`
    - Modify the type of the response parameter `size` of the interface `UpdateDependency`: `string`->`integer`

### HuaweiCloud SDK HSS

- _Features_
    - Support the interface `ListEvents`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK IEC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the request parameters `pool_id_v6`,`ipv6_bandwidth_enable` of the interface `CreateDeployment`.
    - Remove the response parameters `ipv6_enable`,`ipv6_bandwidth_enable`,`pool_id_v6` of the interface `ShowEdgeCloud`.
    - Remove the response parameters `shared`,`charge_mode` of the interface `ListSites`.

### HuaweiCloud SDK Live

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the response parameter `domain_source` of the interface `ShowDomain`.

### HuaweiCloud SDK Meeting

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameters `offset`,`limit` to the interface `ShowRecordingFileDownloadUrls`.

### HuaweiCloud SDK MPC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the response parameter `language` of the interface `ListTranscodeDetail`.
    - Remove the request parameter `project_id`,`tenant_project_id`,`domain_name`,`canonical_grant_id` of the interface `CreateThumbnailsTask`.
    - Add the response parameter `audit_report` to the interface `ListTranscodeDetail`.
    - Remove the response parameter `output_url` of the interface `QueryTranscodingsTask`.
    - Add the request parameter `audit` to the interface, and remove the request parameter `special_effect`,`quality_enhance`,`template_extend` of this interface.
    - Remove the response parameter `template_id`,`error` of the interface `ListWatermarkTemplate`.
    - Remove the request parameter `multidrm`,`preview_duration` of the interface `CreateVodTranscodingTask`.

### HuaweiCloud SDK VOD

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the request parameter `auto_publish` of the interface `CreateAssetByFileUpload`, and configure the optional values `0`,`1`.

### HuaweiCloud SDK WAF

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the response parameters `response_time`,`response_size` of the interface `ListEvent`: `string`->`integer`.

# 3.0.52 2021-07-16

### HuaweiCloud SDK AS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `description` to the interface `CreateScalingV2Policy`.
    - Add the response parameter `description` to the interfaces `ShowScalingV2Policy`, `ShowScalingGroup`.

### HuaweiCloud SDK DCS

- _Features_
    - Support more interfaces:
        - `CreateDiagnosisTask`
        - `CreateRedislog`
        - `CreateRedislogDownloadLink`
        - `ListDiagnosisTasks`
        - `ListRedislog`
        - `ListSlowlog`
        - `ShowDiagnosisTaskDetails`
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `include_delete` to the interface `ListInstances`.

### HuaweiCloud SDK IMS

- _Features_
    - None
- _Bug Fix_
    - [Issue 40](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/40): Fix the issue that the type of the response parameter `__lazyloading` is incorrectly defined.
- _Change_
    - None

# 3.0.51 2021-07-09

### HuaweiCloud SDK BMS

- _Features_
    - None
- _Bug Fix_
    - Fix the issue that the data structure of the response parameter `addresses` of the interface `ListBareMetalServers` is incorrectly defined.
- _Change_
    - None

### HuaweiCloud SDK CBR

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameters `smn_notify`,`threshold` to the interface `ListProtectable`.
    - Add the request parameter `add_policy_ids` and the response parameters `without_any_tag`,`smn_notify`,`threshold` to the interface `AssociateVaultPolicy`.

### HuaweiCloud SDK CCE

- _Features_
    - Support the interfaces `RemoveNode`,`MigrateNode`.
- _Bug Fix_
    - None
- _Change_
    - Add the request parameter `tobedeleted` to the interface `DeleteCluster`.

### HuaweiCloud SDK CCM

- _Features_
    - Support the `Cloud Certificate Manager` service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK CDN

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Change the request parameters `start_time`,`end_time` from optional to required of the interface `ShowTopUrl`, and add the optional value `outside_mainland_china` to the request parameter `domain_name`.
    - Add the request parameter `service_area` to the interface `ShowDomainItemDetails`.

### HuaweiCloud SDK DDM

- _Features_
    - Support the `Distributed Database Middleware` service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DNS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the response parameters `masters`, `zones` of the interface `CreatePublicZone`: `string`->`array`

### HuaweiCloud SDK EIP

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameter `publicip_border_group` to the interfaces `CreateSharedBandwidth`,`ListBandwidths`.

### HuaweiCloud SDK IMS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameters `__root_origin`,`checksum`,`size` to the interfaces `GlanceCreateImageMetadata`.
    - Remove the request parameters `deleted`, `deleted_at` of the interface `GlanceAddImageMember`, and add the following request parameters:
        - `__lazyloading`
        - `__os_feature_list`
        - `__root_origin`
        - `__sequence_num`
        - `__support_agent_list`
        - `__system__cmkid`
        - `active_at`
        - `hw_vif_multiqueue_enabled`
        - `max_ram`
        - `__image_location`
        - `__is_config_init`
        - `__account_code`

### HuaweiCloud SDK IoTDA

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameters `edge_node_ids`, `last_update_time` to the interface `ListRules`.

### HuaweiCloud SDK LTS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the response parameter `context` of the interface `ListStructuredLogsWithTimeRange`: `string`->`array`
    - Modify the name of the interfaces::
        - `UpdateLogContents`->`ListLogs`
        - `UpdateLogContents2`->`ListQueryStructuredLogs`
        - `UpdateLogContents3`->`ListStructuredLogsWithTimeRange`

### HuaweiCloud SDK Meeting

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the response parameters `startTime`、`endTime` of the interface `CreateMeeting`: `string`->`integer`
    - Modify the name of the request parameter of the interface `ShowWebinar`: `conferenceId`->`conference_id`

### HuaweiCloud SDK SWR

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add the response parameters `domain_id`,`priority` to the interface `ShowRepository`.
    - Add the response parameter `template` to the interface `CreateRetention`.

# 3.0.50 2021-06-29

### HuaweiCloud SDK CCE

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add a request parameter `storage` to interfaces `CreateNodePool`,`ShowNodePool`,`UpdateNodePool`,`DeleteNodePool`.

### HuaweiCloud SDK DRS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the parameter `selected` of the interface `BatchUpdateUser`: `string`->`boolean`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of the response parameter `port` of the interface `ListInstances`: `string`->`integer`.
    - Modify the name of response parameter of the interface `ListInstances`: `storage_engine`->`mode`
    - Remove a response parameter `node_name` and add a response parameter `time` to the interface `ListSlowLogs`.

### HuaweiCloud SDK NAT

- _Features_
    - None
- _Bug Fix_
    - Fix the issue that the request parameter `project_id` of the interface `ListNatGateways` is duplicated.
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of response parameters `port`,`node_num` of the interface `ShowInformationAboutDatabaseProxy`: `string`->`integer`

# 3.0.49 2021-06-25

### HuaweiCloud SDK APIG

- _Features_
    - Support more ineterfaces:
        - `ListGatewayResponsesV2`
        - `UpdateGatewayResponseV2`
        - `DeleteGatewayResponseV2`
        - `UpdateGatewayResponseTypeV2`
        - `DeleteGatewayResponseTypeV2`
        - `DeleteInstancesV2`
        - `UpdateInstanceV2`
        - `ListInstancesV2`
        - `RemoveEipV2`
        - `UpdateEngressEipV2`
        - `RemoveEngressEipV2`
        - `ListFeaturesV2`
        - `UpdateDomainV2`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK BMS

- _Features_
    - Support interface `ChangeBaremetalServerOs`.
- _Bug Fix_
    - None
- _Change_
    - Modify the name of reponse parameter of interface `ChangeBaremetalServerName`: `server_tags`->`sys_tags`.

### HuaweiCloud SDK CDN

- _Features_
    - Support interface `ShowQuota`.
- _Bug Fix_
    - None
- _Change_
    - Modify the type of request parameter `url` of interface `ShowHistoryTaskDetails`: `integer`->`string`.

### HuaweiCloud SDK DRS

- _Features_
    - Support interface `ShowQuotas`.
- _Bug Fix_
    - None
- _Change_
    - Modify the type of request parameters `is_transfer`,`selected` of interface `BatchUpdateUser`: `string`->`boolean`.

### HuaweiCloud SDK IAM

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add request parameters`permission_type`,`display_name`,`catalog`,`type` of interface `KeystoneListPermissions`.

### HuaweiCloud SDK LTS

- _Features_
    - Support `Log Tank Service`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support interface `InviteShare`.
- _Bug Fix_
    - None
- _Change_
    - Add request parameter `multiPicSaveOnly` to interface `SetMultiPicture`.
    - Add reponse parameter `leftReason` to interface `SearchHisMeetings`.

### HuaweiCloud SDK VOD

- _Features_
    - Support `Video on Demand` service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK WAF

- _Features_
    - Support `Web Application Firewall` service.
- _Bug Fix_
    - None
- _Change_
    - None

# 3.0.48 2021-06-21

### HuaweiCloud SDK BMS

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add response parameters `server_tags`,`enterprise_project_id`,`group` to interface `ChangeBaremetalServerName`.

### HuaweiCloud SDK CCE

- _Features_
    - None
- _Bug Fix_
    - [Issue 22](https://github.com/huaweicloud/huaweicloud-sdk-go-v3/issues/22): Modify the optional value of response parameter `status` of interface `ListAddonInstances`.
- _Change_
    - None

### HuaweiCloud SDK CDN

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Remove the request parameter `user_domain_id` of interface `ListDomains`.
    - Modify the name of interface: `ShowRefer` -> `ShowReferer`.

### HuaweiCloud SDK CloudPipeline

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Add request parameters to interface `ShowTemplateDetail`:
        - `template_url`
        - `create_time`
        - `last_modify_time`
        - `can_update`
        - `can_delete`
        - `need_hub`

### HuaweiCloud SDK Live

- _Features_
    - Support more interfaces:
        - `CreateRecordCallbackConfig`
        - `ShowRecordCallbackConfig`
        - `UpdateRecordCallbackConfig`
        - `DeleteRecordCallbackConfig`
        - `ListRecordCallbackConfigs`
        - `UpdateRecordRule`
        - `ShowRecordRule`
- _Bug Fix_
    - None
- _Change_
    - Modify the name of some interfaces:
        - `CreateRecordConfig` -> `CreateRecordRule`
        - `DeleteRecordConfig` -> `DeleteRecordRule`
        - `ListRecordConfigs` -> `ListRecordRules`
    - Remove some interfaces:
        - `ShowTraffic`
        - `ShowBandwidth`
        - `ShowOnlineUsers`

### HuaweiCloud SDK Kafka

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the type of response parameter `partitions` of interface `ShowGroups`: `array[string]` -> `array[integer]`

### HuaweiCloud SDK RabbitMQ

- _Features_
    - None
- _Bug Fix_
    - Fix the issue of compilation failure.
- _Change_
    - None

# 3.0.47 2021-06-10

### HuaweiCloud SDK BSS

- _Features_
    - Support interfaces `ListFreeResources`,`ListFreeResourceUsages`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK BSSINTL

- _Features_
    - Support interfaces `ListFreeResources`,`ListFreeResourceUsages`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Cloudtest

- _Features_
    - Support interfaces `CreateApiTestSuiteByRepoFile`,`ListEnvironments`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DRS

- _Features_
    - Support `Data Replication Service`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK FunctionGraph

- _Features_
    - Support interfaces
        - `ImportFunction`
        - `ExportFunction`
        - `AsyncInvokeReservedFunction`
        - `DeleteReservedInstanceById`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK Meeting

- _Features_
    - Support more interfaces
        - `CreateWebinar`
        - `ShowWebinar`
        - `UpdateWebinar`
        - `DeleteWebinar`
        - `ListOngoingWebinars`
        - `ListHistoryWebinars`
        - `ListUpComingWebinars`
        - `UploadFile`
        - `ShowRoomSetting`
        - `UpdateRoomSetting`
        - `SearchCorpResources`
- _Bug Fix_
    - None
- _Change_
    - Add a request parameter `vmrMode` to interface `SearchCorpVmr`.
    - Remove the interface `SearchMemberVmrByCloudLink`.

### HuaweiCloud SDK OSM

- _Features_
    - Support `Online Service Management`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - Support interfaces `SetBinlogClearPolicy`,`ShowBinlogClearPolicy`.
- _Bug Fix_
    - None
- _Change_
    - Add request parameters `offset`,`limit` to interface `ListOffSiteInstances`.

# 3.0.46 2021-06-04

### HuaweiCloud SDK CCE

- _Features_
    - None
- _Bug Fix_
    - [Issue 20](https://github.com/huaweicloud/huaweicloud-sdk-go-v3/issues/20): Fix the issue that the type of `extendParam`
      is defined incorrectly.
- _Change_
    - Add the request parameter `tobedeleted` to the interface `DeleteCluster`.

### HuaweiCloud SDK CDN

- _Features_
    - Support `Content Delivery Network` service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK DDS

- _Features_
    - Support the interface `ShowQuotas`
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK IEC

- _Features_
    - None
- _Bug Fix_
    - None
- _Change_
    - Modify the name of request parameter of the interface `CreatePublicIp`: `pool_id` -> `type`

### HuaweiCloud SDK IoTDA

- _Features_
    - Support interface `ListComplexQueryDevice`.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
    - Support `GaussDBforNoSQL` service.
- _Bug Fix_
    - None
- _Change_
    - None

### HuaweiCloud SDK RDS

- _Features_
    - Support the interface `ShowQuotas`
- _Bug Fix_
    - None
- _Change_
    - Modify the type of request parameter `restart` of the interface `StartInstanceRestartAction`: string -> object

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
