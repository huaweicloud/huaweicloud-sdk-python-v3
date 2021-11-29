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
  - [Issue #43](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/43)：Fix the issue of incorrect type of the response parameter `offset` of the interface `ListSeries`.
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
    - Remove the response parameters `task_id`, `process_reason`, modify the type of the request parameter `process_reason`：`integer`->`string`
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
