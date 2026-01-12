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

