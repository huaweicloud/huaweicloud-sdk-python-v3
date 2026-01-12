# 3.1.20 2022-12-29

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListApiGroupsV2`新增响应参数 `verified_client_certificate_enabled`
  - 接口`ShowDetailsOfApiGroupV2`新增响应参数 `verified_client_certificate_enabled`
  - 接口`UpdateApiGroupV2`新增响应参数 `verified_client_certificate_enabled`
  - 接口`ShowDetailsOfApiV2`新增响应参数 `verified_client_certificate_enabled`
  - 接口`UpdateApiV2`新增响应参数 `verified_client_certificate_enabled`
  - 接口`ListApiVersionDetailV2`新增响应参数 `verified_client_certificate_enabled`
  - 接口`UpdateDomainV2`新增请求参数 `verified_client_certificate_enabled`
  - 接口`ShowDetailsOfDomainNameCertificateV2`新增响应参数 `id`、`name`、`type`、`instance_id`、`project_id`、`create_time`、`update_time`
  - 接口`ExportApiDefinitionsV2`新增请求参数 `oas_version`
  - 接口`ListVpcChannelsV2`新增响应参数 `instance_id`
  - 接口`ShowDetailsOfVpcChannelV2`新增响应参数 `instance_id`
  - 接口`UpdateVpcChannelV2`新增响应参数 `instance_id`
  - 接口`ListMetricData`请求参数`dim`新增枚举值`inbound_eip`、`outbound_eip`, 移除枚举值`inbound`、`outbound`
  - 接口`CreateInstanceV2`新增请求参数 `vpcep_service_name`
  - 接口`ShowDetailsOfInstanceV2`新增响应参数 `is_releasable`
  - 接口`UpdateInstanceV2`:
    - 新增请求参数 `vpcep_service_name`
    - 新增响应参数 `is_releasable`
  - 接口`CreateCertificateV2`新增请求参数 `trusted_root_ca`
  - 接口`BatchAssociateCertsV2`新增请求参数 `verified_client_certificate_enabled`
  - 接口`BatchDisassociateCertsV2`新增请求参数 `verified_client_certificate_enabled`
  - 接口`UpdateCertificateV2`新增请求参数 `trusted_root_ca`
  - 接口`BatchAssociateDomainsV2`新增请求参数 `verified_client_certificate_enabled`
  - 接口`BatchDisassociateDomainsV2`新增请求参数 `verified_client_certificate_enabled`
  - 接口`ListAttachedDomainsV2`新增响应参数 `verified_client_certificate_enabled`

### HuaweiCloud SDK CFW

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDnsServers`新增请求参数 `fw_instance_id`、`enterprise_project_id`
  - 接口`UpdateDnsServers`新增请求参数 `fw_instance_id`、`enterprise_project_id`
  - 接口`ListVpcProtects`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListRuleHitCount`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`DeleteAclRuleCount`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ChangeIpsSwitchUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListIpsSwitchStatusUsingGet`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListEastWestFirewall`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ChangeEwProtectStatus`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListFlowLogs`新增请求参数 `enterprise_project_id`
  - 接口`ListAccessControlLogs`新增请求参数 `enterprise_project_id`
  - 接口`ListAttackLogs`新增请求参数 `enterprise_project_id`
  - 接口`AddRuleAclUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`DeleteRuleAclUsingDelete`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`UpdateRuleAclUsingPut`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListRuleAclsUsingGet`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListRuleAclUsingPut`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`AddBlackWhiteListUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`DeleteBlackWhiteListUsingDelete`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`UpdateBlackWhiteListUsingPut`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListBlackWhiteListsUsingGet`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ChangeIpsProtectModeUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListIpsProtectModeUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListFirewallUsingGet`:
    - 新增请求参数 `enterprise_project_id`、`fw_instance_id`
    - 新增响应参数 `fw_instance_name`、`enterprise_project_id`
  - 接口`AddServiceSetUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`DeleteServiceSetUsingDelete`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListServiceSetDetails`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`UpdateServiceSetUsingPut`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`AddServiceItemsUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListServiceItemsDetails`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`DeleteServiceItemUsingDelete`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListParseDomainDetails`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`CountEips`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ChangeProtectEip`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListEipResources`:
    - 新增请求参数 `fw_instance_id`、`fw_key_word`、`eps_id`
    - 新增响应参数 `fw_instance_name`、`fw_instance_id`、`fw_enterprise_project_id`
  - 接口`DeleteAddressItemUsingDelete`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`AddAddressItemsUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListAddressItemsUsingGet`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`AddAddressSetInfoUsingPost`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListAddressSetListUsingGet`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`DeleteAddressSetInfoUsingDelete`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListAddressSetDetailUsingGet`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`UpdateAddressSetInfoUsingPut`新增请求参数 `enterprise_project_id`、`fw_instance_id`
  - 接口`ListServiceSet`新增请求参数 `enterprise_project_id`、`fw_instance_id`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClustersDetails`响应参数`size`类型调整 `string` -> `int32`
  - 接口`ShowClusterDetail`响应参数`size`类型调整 `string` -> `int32`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateBigkeyScanTask`响应参数`size`类型调整 `int32` -> `int64`
  - 接口`ShowBigkeyScanTaskDetails`响应参数`size`类型调整 `int32` -> `int64`
  - 接口`CreateHotkeyScanTask`响应参数`size`类型调整 `int32` -> `int64`
  - 接口`ShowHotkeyTaskDetails`响应参数`size`类型调整 `int32` -> `int64`

### HuaweiCloud SDK DNS

- _新增特性_
  - 支持接口`AssociateResolveRuleRouter`、`DisassociateResolveRuleRouter`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListPublicZones`移除响应参数 `total_count`
  - 接口`ListPrivateZones`移除响应参数 `total_count`
  - 接口`ListRecordSetsByZone`移除响应参数 `total_count`
  - 接口`ListRecordSets`移除响应参数 `total_count`
  - 接口`BatchDeleteRecordSetWithLine`移除响应参数 `total_count`
  - 接口`BatchUpdateRecordSetWithLine`移除响应参数 `total_count`
  - 接口`ListRecordSetsWithLine`移除响应参数 `total_count`
  - 接口`CreateRecordSetWithBatchLines`移除响应参数 `total_count`
  - 接口`ShowRecordSetByZone`移除响应参数 `total_count`
  - 接口`ListPtrRecords`移除响应参数 `total_count`
  - 接口`ListCustomLine`移除响应参数 `total_count`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchCreateJobs`新增请求参数 `charging_mode`、`period_order`
  - 接口`BatchCheckJobs`请求参数`precheck_mode`新增枚举值`forRetryJob`
  - 接口`BatchListJobDetails`新增响应参数 `period_order`、`object_infos`

### HuaweiCloud SDK DWS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClusterDetails`新增响应参数 `elb`
  - 接口`ListAlarmSubs`新增请求参数 `offset`、`limit`
  - 接口`ListEvents`新增请求参数 `offset`、`limit`
  - 接口`ListEventSubs`新增请求参数 `offset`、`limit`

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ChangeBandwidthToPeriod`新增请求参数 `extendParam`
  - 接口`ChangePublicipToPeriod`新增请求参数 `extendParam`
  - 接口`ListBandwidthPkg`:
    - 新增响应参数 `tenantId`
    - 移除响应参数 `tenant_id`
  - 接口`UpdateAssociatePublicip`请求参数`associate_instance_type`、`associate_instance_id`改为必填
  - 接口`AssociatePublicips`请求参数`associate_instance_type`、`associate_instance_id`改为必填

### HuaweiCloud SDK ELB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListLoadbalancersByTags`:
    - 移除请求参数 `without_any_tag`
    - 请求参数`values`改为必填
  - 接口`ListListenersByTags`:
    - 移除请求参数 `without_any_tag`
    - 请求参数`values`改为必填
  - 接口`ShowQuota`新增响应参数 `ipgroup_bindings`、`ipgroup_max_length`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstanceTags`新增响应参数 `total_count`

### HuaweiCloud SDK HiLens

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowNodes`移除响应参数 `id`、`name`、`description`、`created_at`、`cluster_id`、`cluster_node_state`、`cluster_node_type`、`firmware_name`、`upgrade_firmware_version`、`firmware_status`、`firmware_upgrade_record`、`state`、`type`、`active_status`、`cpu`、`host_ips`、`tags`
  - 接口`CreateNode`:
    - 移除请求参数 `log_group_id`
    - 请求参数`component`、`type`改为必填
  - 接口`ShowNode`:
    - 移除响应参数 `log_group_id`
    - 响应参数`firmware_upgrade_time`类型调整 `int32` -> `string`
    - 响应参数`component`、`type`改为必填
  - 接口`UpdateNode`:
    - 移除请求参数 `log_group_id`
    - 请求参数`component`、`type`改为必填
  - 接口`ShowUpgradeProgress`响应参数`status`类型调整 `string` -> `int32`
  - 接口`ShowResourceTags`:
    - 新增响应参数 `count`
    - 移除响应参数 `total`
  - 接口`ListSecrets`响应参数`count`类型调整 `string` -> `int32`
  - 接口`CreateSecret`:
    - 新增响应参数 `secret`
    - 移除响应参数 `id`、`name`、`description`、`project_id`、`created_at`、`updated_at`、`secrets`、`tags`
  - 接口`UpdateSecret`:
    - 新增响应参数 `secret`
    - 移除响应参数 `id`、`name`、`description`、`project_id`、`created_at`、`updated_at`、`secrets`、`tags`
  - 接口`ShowSkillOrderList`:
    - 响应参数`update_time`类型调整 `int32` -> `int64`
    - 响应参数`expire_time`类型调整 `int32` -> `int64`
    - 响应参数`order_limit`类型调整 `string` -> `int32`
  - 接口`CreateOrderForm`:
    - 新增响应参数 `order_id`
    - 移除请求参数 `data`、`total`
    - 移除响应参数 `data`、`total`
  - 接口`ShowSkillOrderInfo`:
    - 新增响应参数 `expiration_stop_flag`、`package_order_id`、`icon`、`commission_flag`、`product_info`、`package_id`、`measure_type`、`update_time`、`channel_limit`、`resource_step_size`、`cloud_service_type`、`developer_id`、`amount`、`format`、`resource_type`、`expire_time`、`measure_unit`、`skill_chip`、`versions`、`skill_name`、`skill_type`、`used_amount`、`charge_model`、`resource_spec_code`、`skill_id`、`skill_platform`、`order_limit`、`order_id`、`status`
    - 移除响应参数 `total`、`data`
  - 接口`DeleteDeployment`新增响应参数 `deployment_id`
  - 接口`UpdateDeploymentUsingPatch`移除响应参数 `deployment_tags`
  - 接口`ShowDeploymentPods`:
    - 新增响应参数 `start_resources`、`channel_resources`、`skill_project_id`
    - 移除响应参数 `app_docker_login`、`app_id`、`expire_time`、`image_url`、`license`、`modelKey`
    - 响应参数`host_network`、`restart_policy`、`app_url`、`name`改为必填
  - 接口`CreateWorkSpace`:
    - 新增响应参数 `workspace_id`
    - 移除响应参数 `name`

### HuaweiCloud SDK IMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowJob`新增响应参数 `sub_jobs_result`、`sub_jobs_list`
  - 接口`ShowJobProgress`新增响应参数 `sub_jobs_result`、`sub_jobs_list`

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchListEdgeApps`新增响应参数 `protocol`、`edge_app_name`
  - 接口`CreateEdgeApp`新增请求参数 `edge_app_name`、`protocol`
  - 接口`ShowEdgeApp`新增响应参数 `protocol`、`edge_app_name`
  - 接口`BatchListEdgeAppVersions`新增响应参数 `name`
  - 接口`CreateEdgeApplicationVersion`新增请求参数 `supplier`、`tpl_id`
  - 接口`ShowEdgeApplicationVersion`新增响应参数 `supplier`、`tpl_id`
  - 接口`UpdateEdgeApplicationVersion`:
    - 新增请求参数 `tpl_id`
    - 新增响应参数 `name`
  - 接口`UpdateEdgeApplicationVersionState`新增响应参数 `name`
  - 接口`CreateEdgeNode`新增请求参数 `os_type`、`reliability_level`、`network_access_point`、`offline_cache_configs`、`device_auth_info`
  - 接口`ShowEdgeNode`新增响应参数 `offline_cache_configs`、`device_auth_info`

### HuaweiCloud SDK MapDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCredential`:
    - 新增请求参数 `credential`
    - 移除请求参数 `description`

### HuaweiCloud SDK VOD

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateTranscodeTemplate`请求参数`name`改为非必填
  - 接口`UpdateTemplateGroupCollection`:
    - 请求参数`collection_id`改为必填
    - 请求参数`name`、`template_group_list`改为非必填

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListVpcs`新增响应参数 `tenant_id`、`created_at`、`updated_at`
  - 接口`CreateVpc`新增响应参数 `tenant_id`、`created_at`、`updated_at`
  - 接口`ShowVpc`新增响应参数 `tenant_id`、`created_at`、`updated_at`
  - 接口`UpdateVpc`新增响应参数 `tenant_id`、`created_at`、`updated_at`
  - 接口`ListSubnets`新增响应参数 `tenant_id`、`created_at`、`updated_at`
  - 接口`CreateSubnet`新增响应参数 `tenant_id`、`created_at`、`updated_at`
  - 接口`ShowSubnet`新增响应参数 `tenant_id`、`created_at`、`updated_at`
  - 接口`ListRouteTables`新增响应参数 `created_at`、`updated_at`
  - 接口`CreateRouteTable`新增响应参数 `created_at`、`updated_at`
  - 接口`ShowRouteTable`新增响应参数 `created_at`、`updated_at`
  - 接口`UpdateRouteTable`新增响应参数 `created_at`、`updated_at`
  - 接口`AssociateRouteTable`新增响应参数 `created_at`、`updated_at`
  - 接口`DisassociateRouteTable`新增响应参数 `created_at`、`updated_at`

# 3.1.19 2022-12-26

### HuaweiCloud SDK AOM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateWorkflow`:
    - 新增请求参数 `policy`
    - 移除请求参数 `citation_urns`、`information`、`alarm_name`
    - 移除响应参数 `param_name`、`domain_id`、`domain_name`
  - 接口`UpdateWorkflowTriggerStatus`请求参数`action`改为非必填
  - 接口`SearchWorkflowExecutionDetail`移除响应参数 `workflow_urn`、`headers`、`input`、`output`、`created_by`、`node_id`、`begin_time`、`end_time`、`function_execution_id`、`output`、`status`
  - 接口`ListAllScriptByName`:
    - 移除请求参数 `page_total`
    - 请求参数`order_by_column`改为必填
    - 请求参数`project_id`改为非必填
  - 接口`ListAllVersionByVersionId`:
    - 移除请求参数 `page_total`
    - 请求参数`order_by_column`改为必填
    - 请求参数`project_id`改为非必填
  - 接口`ListAllJobByName`:
    - 新增请求参数 `enterprise_project_id`
    - 新增响应参数 `is_latest_version`、`version_number`
    - 请求参数`order_by_column`改为必填
  - 接口`ListTemplateByJobId`请求参数`order_by_column`改为必填
  - 接口`SearchTemplateById`请求参数`share_type`改为非必填
  - 接口`ListWorkflow`:
    - 移除请求参数 `template_name_list`
    - 移除响应参数 `param_name`、`domain_id`、`domain_name`
  - 接口`ExecuteWorkflow`移除响应参数 `workflow_id`、`workflow_urn`、`status`、`headers`、`input`、`output`、`begin_time`、`end_time`、`last_update_time`、`created_by`、`execution_result_list`、`approve_user_name_list`、`project_id`、`workflow_edit_time`、`last_record_id_with_snapshot`
  - 接口`ListWorkflowExecutions`移除响应参数 `workflow_urn`、`node_id`、`begin_time`、`end_time`、`function_execution_id`、`output`、`status`
  - 接口`ListNotifiedHistories`请求参数`event_sn`改为必填
  - 接口`ShowActionRule`响应参数`type`类型调整 `string` -> `enum`
  - 接口`AddActionRule`请求参数`type`类型调整 `string` -> `enum`
  - 接口`UpdateActionRule`请求参数`type`类型调整 `string` -> `enum`
  - 接口`ListActionRule`响应参数`type`类型调整 `string` -> `enum`
  - 接口`AddEvent2alarmRule`请求参数`resource_provider`改为非必填
  - 接口`UpdateEventRule`请求参数`resource_provider`改为非必填
  - 接口`ListEvent2alarmRule`响应参数`resource_provider`改为非必填
  - 接口`CreateApp`请求参数`register_type`类型调整 `string` -> `enum`
  - 接口`UpdateApp`:
    - 移除响应参数 `aom_id`、`app_id`、`create_time`、`creator`、`description`、`display_name`、`eps_id`、`modified_time`、`modifier`、`name`、`register_type`
    - 请求参数`register_type`类型调整 `string` -> `enum`
  - 接口`UpdateComponent`移除请求参数 `model_id`、`model_type`
  - 接口`CreateEnv`:
    - 请求参数`component_id`、`os_type`改为必填
    - 请求参数`region`改为非必填
  - 接口`UpdateEnv`:
    - 请求参数`component_id`、`os_type`改为必填
    - 请求参数`region`改为非必填
  - 接口`ShowComponentByName`移除响应参数 `create_time`、`creator`、`description`、`modified_time`、`modifier`、`register_type`、`sub_app_id`

### HuaweiCloud SDK CBH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCbhInstance`:
    - 新增响应参数 `quotaDetail`、`publicip`、`expTime`、`startTime`、`endTime`、`releaseTime`、`instanceId`、`privateIp`、`taskStatus`、`vpcId`、`subnetId`、`securityGroupId`、`createinstanceStatus`、`failReason`、`instanceKey`、`orderId`、`periodNum`、`resourceId`、`alterPermit`、`publicId`、`bastionVersion`、`newBastionVersion`、`instanceStatus`、`instanceDescription`、`slaveZone`、`enterpriseProjectId`、`instanceType`、`haId`、`slaveZoneDisplay`、`webPort`、`vip`
    - 移除响应参数 `quota_detail`、`public_ip`、`exp_time`、`start_time`、`end_time`、`release_time`、`instance_id`、`private_ip`、`task_status`、`vpc_id`、`subnet_id`、`security_group_id`、`createinstance_status`、`fail_reason`、`instance_key`、`order_id`、`period_num`、`resource_id`、`alter_permit`、`public_id`、`bastion_version`、`new_bastion_version`、`instance_status`、`instance_description`
    - 响应参数`is_auto_renew`改为非必填
  - 接口`UpgradeCbhInstance`响应参数`task_id`、`order_id`改为非必填
  - 接口`ResetPassword`:
    - 新增响应参数 `request_info`
    - 移除响应参数 `code`、`description`、`task_id`、`order_id`
  - 接口`ShowAvailableZoneInfo`:
    - 新增响应参数 `availability_zone`
    - 移除响应参数 `availability_zones`
  - 接口`ResetLoginMethod`:
    - 新增响应参数 `request_info`
    - 移除响应参数 `code`、`description`、`task_id`、`order_id`
  - 接口`ChangeInstanceNetwork`:
    - 新增响应参数 `status`、`security_grp_status`、`public_eip_status`、`nics`
    - 移除响应参数 `type`、`security_groups`
    - 响应参数`firewall_status`改为必填
    - 响应参数`public_eip_statu`改为非必填
  - 接口`CreateInstance`请求参数`slave_availability_zone`改为非必填
  - 接口`ChangeInstanceOrder`:
    - 新增响应参数 `orderId`
    - 移除响应参数 `order_id`

### HuaweiCloud SDK DSC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowSpecification`:
    - 新增响应参数 `orderInfos`
    - 移除响应参数 `order_infos`
  - 接口`ListRuleGroups`新增响应参数 `is_default`

### HuaweiCloud SDK HSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListPorts`新增响应参数 `laddr`
  - 接口`ListProtectionServer`新增响应参数 `os_name`、`agent_status`
  - 接口`ShowBackupPolicyInfo`移除响应参数 `associated_vaults`
  - 接口`ListSecurityEvents`新增响应参数 `os_type`、`event_details`
  - 接口`ListAlarmWhiteList`新增响应参数 `enterprise_project_name`
  - 接口`ListVulHosts`移除响应参数 `repair_necessity`

### HuaweiCloud SDK Live

- _新增特性_
  - 支持接口`UpdateDomainIp6Switch`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowDomain`:
    - 新增请求参数 `enterprise_project_id`
    - 新增响应参数 `enterprise_project_id`、`is_ipv6`
  - 接口`UpdateDomain`:
    - 新增请求参数 `enterprise_project_id`
    - 新增响应参数 `enterprise_project_id`
  - 接口`CreateDomain`新增请求参数 `enterprise_project_id`

### HuaweiCloud SDK LTS

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateLogStream`移除请求参数 `enterprise_project_name`、`ttl_in_days`

### HuaweiCloud SDK MPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListTranscodingTask`:
    - 移除响应参数 `ref_frames_count`
    - 响应参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`CreateTranscodingTask`:
    - 移除请求参数 `ref_frames_count`、`aspect_ratio`
    - 请求参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`ListTemplate`:
    - 移除响应参数 `ref_frames_count`
    - 响应参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`CreateTransTemplate`:
    - 移除请求参数 `ref_frames_count`
    - 请求参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`UpdateTransTemplate`:
    - 移除请求参数 `ref_frames_count`
    - 请求参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`ListTemplateGroup`:
    - 移除响应参数 `ref_frames_count`、`aspect_ratio`
    - 响应参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`CreateTemplateGroup`:
    - 移除请求参数 `ref_frames_count`、`aspect_ratio`
    - 请求参数`name`改为必填
    - 请求参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`UpdateTemplateGroup`:
    - 移除请求参数 `ref_frames_count`、`aspect_ratio`
    - 请求参数`group_id`改为必填
    - 请求参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`UpdateBucketAuthorized`移除请求参数 `project_id`
  - 接口`CreateThumbnailsTask`移除请求参数 `aspect_ratio`
  - 接口`ListEditingJob`:
    - 移除响应参数 `ref_frames_count`、`ref_frames_count`
    - 响应参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`、`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填
  - 接口`CreateEditingJob`:
    - 移除请求参数 `ref_frames_count`、`ref_frames_count`
    - 请求参数`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`、`codec`、`sample_rate`、`PVC`、`hls_interval`、`dash_interval`改为非必填

### HuaweiCloud SDK VOD

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateTranscodeTemplate`请求参数`group_id`、`name`、`bitrate`、`frame_rate`、`video_codec`、`format`、`hls_interval`改为必填
  - 接口`ListTranscodeTemplate`响应参数`bitrate`、`frame_rate`、`video_codec`、`format`、`hls_interval`改为必填
  - 接口`CreateTranscodeTemplate`请求参数`name`、`bitrate`、`frame_rate`、`video_codec`、`format`、`hls_interval`改为必填
  - 接口`UpdateTemplateGroupCollection`请求参数`name`、`template_group_list`改为必填
  - 接口`CreateTemplateGroupCollection`请求参数`name`、`template_group_list`改为必填

# 3.1.18 2022-12-22

### HuaweiCloud SDK APIG

- _新增特性_
  - 支持接口`ListProjectInstanceTags`、`ListInstanceTags`、`BatchCreateOrDeleteInstanceTags`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持以下接口：
    - `ExpandInstanceStorage`
    - `ListClusterScaleInNumbers`
    - `ListDisasterRecover`
    - `CreateDisasterRecovery`
    - `DeleteDataSource`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShrinkCluster`:
    - 新增请求参数 `clusterShrinkReq`
    - 新增响应参数 `job_id`
    - 移除请求参数 `shrink_number`、`online`、`type`、`retry`、`force_backup`、`need_agency`
  - 接口`ExecuteRedistributionCluster`:
    - 新增请求参数 `redistributionReq`
    - 移除请求参数 `redis_mode`、`parallel_jobs`
  - 接口`CreateClusterWorkload`:
    - 新增请求参数 `workload_status`
    - 新增响应参数 `workload_res_code`、`workload_res_str`
    - 移除请求参数 `workload_switch`、`max_concurrency_num`
  - 接口`ListClusterWorkload`:
    - 新增响应参数 `workload_res_code`、`workload_res_str`
    - 响应参数`workload_switch`改为必填
  - 接口`CreateWorkloadPlan`:
    - 新增请求参数 `workloadPlan`
    - 新增响应参数 `workload_res_code`、`workload_res_str`
    - 移除请求参数 `plan_id`、`plan_name`、`logical_cluster_name`
  - 接口`AddWorkloadQueue`:
    - 新增请求参数 `workload_queue`
    - 新增响应参数 `workload_res_code`、`workload_res_str`
    - 移除请求参数 `workload_queue_name`、`logical_cluster_name`、`short_query_optimize`、`short_query_concurrency_num`、`workload_resource_item_list`
  - 接口`ListWorkloadQueue`新增响应参数 `workload_res_code`、`workload_res_str`
  - 接口`DeleteWorkloadQueue`:
    - 新增响应参数 `workload_res_code`、`workload_res_str`
    - 请求参数`logical_cluster_name`改为必填
  - 接口`CopySnapshot`:
    - 新增请求参数 `linkCopyReq`
    - 新增响应参数 `snapshot_id`
    - 移除请求参数 `backup_name`、`description`
  - 接口`ListAuditLog`移除响应参数 `version`、`configure_status`
  - 接口`CreateDataSource`:
    - 新增请求参数 `extDataSourceReq`
    - 新增响应参数 `id`、`job_id`
    - 移除请求参数 `data_source_id`、`type`、`data_source_name`、`user_name`、`user_pwd`、`description`、`reboot`、`connect_info`
  - 接口`UpdateDataSource`:
    - 新增请求参数 `reconfigure`
    - 新增响应参数 `job_id`
    - 移除请求参数 `database`、`agency`
  - 接口`ListSnapshotDetails`新增响应参数 `datastore`、`cluster_name`、`bak_expected_start_time`、`bak_keep_day`、`bak_period`、`db_user`、`progress`、`backup_key`、`prior_backup_key`、`base_backup_key`、`backup_device`、`total_backup_size`、`base_backup_name`、`support_inplace_restore`、`fine_grained_backup`、`backup_level`、`fine_grained_backup_detail`、`guest_agent_version`、`cluster_status`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowWorkflowExecutionForPage`:
    - 新增响应参数 `created_by`
    - 移除响应参数 `create_by`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持接口`ModifyVolume`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListAvailableFlavorInfos`新增请求参数 `offset`、`limit`

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateTag`请求参数`tag_name`改为必填
  - 接口`ListProPricePlans`移除请求参数 `sim_card_id`、`partner`、`package_type`、`sim_type`
  - 接口`ListSimCards`:
    - 移除请求参数 `expire_time_duration`、`traffic_warning_threshold`、`sim_status_in`
    - 移除响应参数 `sn`、`supply_code`、`bundle_id`、`test_type`
  - 接口`StopSimCard`:
    - 移除请求参数 `price_plan_list`
    - 移除响应参数 `sim_price_plan_list`
  - 接口`ResetSimCard`:
    - 移除请求参数 `price_plan_list`
    - 移除响应参数 `sim_price_plan_list`
  - 接口`ShowSimCard`移除响应参数 `sn`、`supply_code`、`bundle_id`、`test_type`
  - 接口`ListSimPricePlans`:
    - 移除请求参数 `sim_price_plan_id`
    - 移除响应参数 `partner`、`partner_pid`

### HuaweiCloud SDK IEF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListEdgeNodes`新增响应参数 `purchase_id`、`state_details`、`cert_remaining_valid_time`
  - 接口`UpdateEdgeNode`新增响应参数 `purchase_id`、`state_details`、`cert_remaining_valid_time`
  - 接口`ShowEdgeNodeDetail`新增响应参数 `purchase_id`、`state_details`、`cert_remaining_valid_time`
  - 接口`ListEdgeGroups`新增响应参数 `purchase_id`、`state_details`、`cert_remaining_valid_time`
  - 接口`UpdateEdgeGroup`新增响应参数 `purchase_id`、`state_details`、`cert_remaining_valid_time`
  - 接口`ShowEdgeGroupDetail`新增响应参数 `purchase_id`、`state_details`、`cert_remaining_valid_time`
  - 接口`UpdateEdgeGroupNodeBinding`新增响应参数 `purchase_id`、`state_details`、`cert_remaining_valid_time`

### HuaweiCloud SDK IMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CopyImageCrossRegion`新增请求参数 `vault_id`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 支持接口`SearchDevices`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateRule`新增请求参数 `device_side`
  - 接口`ListRules`新增响应参数 `device_side`
  - 接口`ShowRule`新增响应参数 `device_side`
  - 接口`UpdateRule`:
    - 新增请求参数 `device_side`
    - 新增响应参数 `device_side`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreatePostPaidInstance`新增请求参数 `sasl_enabled_mechanisms`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreatePostPaidInstance`新增请求参数 `enterprise_project_id`、`enable_acl`

### HuaweiCloud SDK SFSTurbo

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateShare`:
    - 新增请求参数 `CreateShareRequestBody`
    - 移除请求参数 `share`
  - 接口`ListShares`:
    - 请求参数`offset`类型调整 `int32` -> `int64`
    - 请求参数`limit`类型调整 `int32` -> `int64`
  - 接口`ExpandShare`:
    - 新增请求参数 `ExpandShareRequestBody`
    - 移除请求参数 `extend`
  - 接口`CreateSharedTag`:
    - 新增请求参数 `CreateSharedTagRequestBody`
    - 移除请求参数 `tag`
  - 接口`BatchAddSharedTags`:
    - 新增请求参数 `BatchAddSharedTagsRequestBody`
    - 移除请求参数 `add_shareed_tags`

# 3.1.17 2022-12-19

### HuaweiCloud SDK APM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowMonitorItemViewConfig`响应参数`function`改为必填
  - 接口`ShowTrend`请求参数`view_type`、`collector_name`、`metric_set`、`function`、`env_id`、`start_time`、`end_time`改为必填
  - 接口`ShowSumTable`请求参数`view_type`、`collector_name`、`metric_set`、`function`、`page`、`page_size`、`env_id`、`start_time`、`end_time`改为必填
  - 接口`ShowRawTable`:
    - 新增请求参数 `last_row_id`
    - 移除请求参数 `lastRowId`
    - 请求参数`function`改为必填
  - 接口`SearchAgent`:
    - 新增请求参数 `order_by_status`
    - 移除请求参数 `orderByStatus`

### HuaweiCloud SDK BCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowBlockchainDetail`新增响应参数 `order_fade_enabled`、`is_support_tc3`、`order_fade_cache`、`deploy_status`、`block_info`、`cluster_platform_type`、`status`、`status_detail`、`order_fade_enabled`
  - 接口`DeleteMemberInvite`新增响应参数 `result`
  - 接口`HandleNotification`新增响应参数 `result`
  - 接口`CreateNewBlockchain`:
    - 请求参数`node_flavor`类型调整 `string` -> `int64`
    - 请求参数`cce_flavor`类型调整 `string` -> `int64`
    - 请求参数`init_node_pwd`类型调整 `string` -> `int64`
    - 请求参数`az`类型调整 `string` -> `int64`
    - 请求参数`cluster_platform_type`类型调整 `string` -> `int64`
  - 接口`DownloadBlockchainCert`新增响应参数 `result`
  - 接口`DownloadBlockchainSdkConfig`新增响应参数 `result`
  - 接口`ListEntityMetric`新增响应参数 `filesystemUsage`
  - 接口`CreateBlockchainCertByUserName`新增响应参数 `result`

### HuaweiCloud SDK CBH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstanceOrder`请求参数`available_zone_id`改为非必填

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateVault`:
    - 请求参数`object_type`新增枚举值`workspace`
    - 响应参数`object_type`新增枚举值`workspace`
  - 接口`ListVault`响应参数`object_type`新增枚举值`workspace`
  - 接口`ShowVault`响应参数`object_type`新增枚举值`workspace`
  - 接口`UpdateVault`响应参数`object_type`新增枚举值`workspace`
  - 接口`ShowBackup`响应参数`resource_type`新增枚举值`OS::Workspace::DesktopV2`
  - 接口`ListBackups`:
    - 请求参数`resource_type`新增枚举值`OS::Workspace::DesktopV2`
    - 响应参数`resource_type`新增枚举值`OS::Workspace::DesktopV2`
  - 接口`ListProtectable`响应参数`object_type`新增枚举值`workspace`
  - 接口`ShowProtectable`响应参数`object_type`新增枚举值`workspace`
  - 接口`ShowVaultResourceInstances`响应参数`object_type`新增枚举值`workspace`

### HuaweiCloud SDK CC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateBandwidthPackage`新增请求参数 `interflow_mode`
  - 接口`ListInterRegionBandwidths`:
    - 新增响应参数 `inter_region_bandwidths`
    - 移除响应参数 `inter_region_bandwidth`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCluster`:
    - 新增请求参数 `vpcPermissions`
    - 新增响应参数 `orderId`
    - 移除请求参数 `vpcPermisssions`
    - 移除响应参数 `ordeId`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListServersDetails`新增请求参数 `server_id`

### HuaweiCloud SDK EIP

- _新增特性_
  - 支持接口`ShowResourcesJobDetail`、`ChangeBandwidthToPeriod`、`ChangePublicipToPeriod`
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
  - 接口`CreateFunction`:
    - 新增请求参数 `depend_version_list`、`func_vpc`
    - 新增响应参数 `depend_version_list`
  - 接口`UpdateFunctionCode`:
    - 新增请求参数 `depend_version_list`
    - 新增响应参数 `depend_version_list`
  - 接口`ShowFunctionCode`新增响应参数 `depend_version_list`
  - 接口`ShowFunctionConfig`新增响应参数 `depend_version_list`
  - 接口`ListReservedInstanceConfigs`:
    - 新增请求参数 `marker`、`limit`
    - 新增响应参数 `reserved_instances`
    - 移除响应参数 `reservedinstances`
  - 接口`ImportFunction`新增响应参数 `depend_version_list`
  - 接口`ListFunctionReservedInstances`:
    - 新增请求参数 `limit`
    - 移除请求参数 `maxitems`
  - 接口`ShowWorkflowExecutionForPage`:
    - 新增请求参数 `offset`、`limit`、`start_time`、`end_time`
    - 移除请求参数 `CreateWorkflowRequestBody`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`SetGaussMySqlProxyWeight`移除请求参数 `id`、`weight`
  - 接口`ShowGaussMySqlJobInfo`响应参数`status`新增枚举值`Pending`
  - 接口`ListScheduleJobs`:
    - 新增响应参数 `job_status`
    - 移除响应参数 `task_status`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListConfigurationDatastores`:
    - 新增响应参数 `datastore_name`
    - 移除响应参数 `datastore_type`
  - 接口`ModifyEpsQuotas`移除请求参数 `instance`、`vcpus`、`ram`
  - 接口`ListEpsQuotas`移除响应参数 `instance`、`vcpus`、`ram`、`instance`、`vcpus`、`ram`

### HuaweiCloud SDK HSS

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRiskConfigCheckRules`新增响应参数 `fix_status`、`enable_auto_fix`、`rule_params`
  - 接口`ListSecurityEvents`新增响应参数 `extend_info`
  - 接口`ListHostStatus`:
    - 新增响应参数 `enterprise_project_id`、`agent_create_time`、`agent_update_time`、`agent_version`、`upgrade_status`、`upgrade_result_code`、`upgradable`
    - 请求参数`region`改为必填
  - 接口`ListVulnerabilities`请求参数`vul_id`改为必填

### HuaweiCloud SDK IEF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListTags`响应参数`key`、`value`改为非必填
  - 接口`CreateTag`请求参数`key`、`value`改为非必填
  - 接口`ListEdgeNodes`响应参数`key`、`value`改为非必填
  - 接口`ShowEdgeNodeDetail`响应参数`key`、`value`改为非必填
  - 接口`UpdateEdgeNode`响应参数`key`、`value`改为非必填
  - 接口`CreateEdgeGroup`新增请求参数 `device_ids`
  - 接口`ListEdgeGroupCerts`:
    - 新增响应参数 `groupcerts`
    - 移除响应参数 `edge_groups`
  - 接口`ListDevices`响应参数`type`改为非必填
  - 接口`CreateDevice`请求参数`type`改为非必填
  - 接口`ShowDevice`响应参数`type`改为非必填
  - 接口`UpdateDevice`响应参数`type`改为非必填
  - 接口`ShowDeviceTwin`响应参数`type`改为非必填
  - 接口`UpdateDeviceTwin`:
    - 请求参数`twin`、`property_visitors`改为非必填
    - 响应参数`type`改为非必填
  - 接口`ListDeviceTemplates`响应参数`key`、`value`改为非必填
  - 接口`CreateDeviceTemplate`请求参数`key`、`value`改为非必填
  - 接口`ShowDeviceTemplate`响应参数`key`、`value`改为非必填
  - 接口`UpdateDeviceTemplateById`响应参数`key`、`value`改为非必填
  - 接口`ListResourceByTags`响应参数`key`、`value`改为非必填
  - 接口`BatchAddDeleteTags`请求参数`key`、`value`改为非必填
  - 接口`ListApps`响应参数`read_only`改为非必填
  - 接口`ShowAppDetail`响应参数`read_only`改为非必填
  - 接口`UpdateApp`响应参数`read_only`改为非必填
  - 接口`ListAppVersions`响应参数`read_only`改为非必填
  - 接口`CreateAppVersions`请求参数`read_only`改为非必填
  - 接口`ShowAppVersionDetail`响应参数`read_only`改为非必填
  - 接口`UpdateAppVersion`:
    - 请求参数`read_only`改为非必填
    - 响应参数`read_only`改为非必填
  - 接口`ListDeployments`响应参数`host_network`、`read_only`改为非必填
  - 接口`CreateDeployments`请求参数`host_network`、`read_only`改为非必填
  - 接口`ShowDeployment`响应参数`host_network`、`read_only`改为非必填
  - 接口`UpdateDeployment`:
    - 请求参数`replicas`、`host_network`、`read_only`改为非必填
    - 响应参数`host_network`、`read_only`改为非必填
  - 接口`ListPods`响应参数`host_network`、`read_only`改为非必填
  - 接口`CreateEncryptdatas`请求参数`description`改为非必填
  - 接口`UpdateEncryptdatas`请求参数`description`改为非必填
  - 接口`ListBatchJob`:
    - 新增响应参数 `task_total_count`、`task_success_count`、`task_failed_count`、`status_last_updated_at`、`description`
    - 移除响应参数 `task_count`、`success_count`、`failed_count`、`updated_at`
  - 接口`ShowBatchJob`:
    - 新增响应参数 `status_last_updated_at`
    - 移除响应参数 `updated_at`

### HuaweiCloud SDK Live

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateRecordCallbackConfig`新增请求参数 `key`
  - 接口`UpdateRecordCallbackConfig`:
    - 新增请求参数 `key`
    - 新增响应参数 `id`、`publish_domain`、`app`、`notify_callback_url`、`notify_event_subscription`、`sign_type`、`create_time`、`update_time`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateSqlAlarmRule`新增请求参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`CreateSqlAlarmRule`新增请求参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`ListSqlAlarmRules`新增响应参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`UpdateKeywordsAlarmRule`新增请求参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`CreateKeywordsAlarmRule`新增请求参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`ListKeywordsAlarmRules`新增响应参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`ListHost`请求参数`host_id_list`改为非必填
  - 接口`UpdateStructConfig`请求参数`is_analysis`、`is_analysis`改为非必填
  - 接口`CreateStructConfig`请求参数`is_analysis`、`is_analysis`改为非必填

### HuaweiCloud SDK OSM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListAuthorizations`新增响应参数 `resource_type_id`

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`StartInstanceRestartAction`请求参数`restart`改为必填

### HuaweiCloud SDK Workspace

- _新增特性_
  - 支持接口`ShowQuotas`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.16 2022-12-15

### HuaweiCloud SDK APM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowMonitorItemViewConfig`响应参数`function`改为必填
  - 接口`ShowTrend`请求参数`view_type`、`collector_name`、`metric_set`、`function`、`env_id`、`start_time`、`end_time`改为必填
  - 接口`ShowSumTable`请求参数`view_type`、`collector_name`、`metric_set`、`function`、`page`、`page_size`、`env_id`、`start_time`、`end_time`改为必填
  - 接口`ShowRawTable`:
    - 新增请求参数 `last_row_id`
    - 移除请求参数 `lastRowId`
    - 请求参数`function`改为必填
  - 接口`SearchAgent`:
    - 新增请求参数 `order_by_status`
    - 移除请求参数 `orderByStatus`

### HuaweiCloud SDK BCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowBlockchainDetail`新增响应参数 `order_fade_enabled`、`is_support_tc3`、`order_fade_cache`、`deploy_status`、`block_info`、`cluster_platform_type`、`status`、`status_detail`、`order_fade_enabled`
  - 接口`DeleteMemberInvite`新增响应参数 `result`
  - 接口`HandleNotification`新增响应参数 `result`
  - 接口`CreateNewBlockchain`:
    - 请求参数`node_flavor`类型调整 `string` -> `int64`
    - 请求参数`cce_flavor`类型调整 `string` -> `int64`
    - 请求参数`init_node_pwd`类型调整 `string` -> `int64`
    - 请求参数`az`类型调整 `string` -> `int64`
    - 请求参数`cluster_platform_type`类型调整 `string` -> `int64`
  - 接口`DownloadBlockchainCert`新增响应参数 `result`
  - 接口`DownloadBlockchainSdkConfig`新增响应参数 `result`
  - 接口`ListEntityMetric`新增响应参数 `filesystemUsage`
  - 接口`CreateBlockchainCertByUserName`新增响应参数 `result`

### HuaweiCloud SDK CBH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstanceOrder`请求参数`available_zone_id`改为非必填

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateVault`:
    - 请求参数`object_type`新增枚举值`workspace`
    - 响应参数`object_type`新增枚举值`workspace`
  - 接口`ListVault`响应参数`object_type`新增枚举值`workspace`
  - 接口`ShowVault`响应参数`object_type`新增枚举值`workspace`
  - 接口`UpdateVault`响应参数`object_type`新增枚举值`workspace`
  - 接口`ShowBackup`响应参数`resource_type`新增枚举值`OS::Workspace::DesktopV2`
  - 接口`ListBackups`:
    - 请求参数`resource_type`新增枚举值`OS::Workspace::DesktopV2`
    - 响应参数`resource_type`新增枚举值`OS::Workspace::DesktopV2`
  - 接口`ListProtectable`响应参数`object_type`新增枚举值`workspace`
  - 接口`ShowProtectable`响应参数`object_type`新增枚举值`workspace`
  - 接口`ShowVaultResourceInstances`响应参数`object_type`新增枚举值`workspace`

### HuaweiCloud SDK CC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateBandwidthPackage`新增请求参数 `interflow_mode`
  - 接口`ListInterRegionBandwidths`:
    - 新增响应参数 `inter_region_bandwidths`
    - 移除响应参数 `inter_region_bandwidth`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCluster`:
    - 新增请求参数 `vpcPermissions`
    - 新增响应参数 `orderId`
    - 移除请求参数 `vpcPermisssions`
    - 移除响应参数 `ordeId`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListServersDetails`新增请求参数 `server_id`

### HuaweiCloud SDK EIP

- _新增特性_
  - 支持接口`ShowResourcesJobDetail`、`ChangeBandwidthToPeriod`、`ChangePublicipToPeriod`
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
  - 接口`CreateFunction`:
    - 新增请求参数 `depend_version_list`、`func_vpc`
    - 新增响应参数 `depend_version_list`
  - 接口`UpdateFunctionCode`:
    - 新增请求参数 `depend_version_list`
    - 新增响应参数 `depend_version_list`
  - 接口`ShowFunctionCode`新增响应参数 `depend_version_list`
  - 接口`ShowFunctionConfig`新增响应参数 `depend_version_list`
  - 接口`ListReservedInstanceConfigs`:
    - 新增请求参数 `marker`、`limit`
    - 新增响应参数 `reserved_instances`
    - 移除响应参数 `reservedinstances`
  - 接口`ImportFunction`新增响应参数 `depend_version_list`
  - 接口`ListFunctionReservedInstances`:
    - 新增请求参数 `limit`
    - 移除请求参数 `maxitems`
  - 接口`ShowWorkflowExecutionForPage`:
    - 新增请求参数 `offset`、`limit`、`start_time`、`end_time`
    - 移除请求参数 `CreateWorkflowRequestBody`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`SetGaussMySqlProxyWeight`移除请求参数 `id`、`weight`
  - 接口`ShowGaussMySqlJobInfo`响应参数`status`新增枚举值`Pending`
  - 接口`ListScheduleJobs`:
    - 新增响应参数 `job_status`
    - 移除响应参数 `task_status`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListConfigurationDatastores`:
    - 新增响应参数 `datastore_name`
    - 移除响应参数 `datastore_type`
  - 接口`ModifyEpsQuotas`移除请求参数 `instance`、`vcpus`、`ram`
  - 接口`ListEpsQuotas`移除响应参数 `instance`、`vcpus`、`ram`、`instance`、`vcpus`、`ram`

### HuaweiCloud SDK HSS

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRiskConfigCheckRules`新增响应参数 `fix_status`、`enable_auto_fix`、`rule_params`
  - 接口`ListSecurityEvents`新增响应参数 `extend_info`
  - 接口`ListHostStatus`:
    - 新增响应参数 `enterprise_project_id`、`agent_create_time`、`agent_update_time`、`agent_version`、`upgrade_status`、`upgrade_result_code`、`upgradable`
    - 请求参数`region`改为必填
  - 接口`ListVulnerabilities`请求参数`vul_id`改为必填

### HuaweiCloud SDK IEF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListTags`响应参数`key`、`value`改为非必填
  - 接口`CreateTag`请求参数`key`、`value`改为非必填
  - 接口`ListEdgeNodes`响应参数`key`、`value`改为非必填
  - 接口`ShowEdgeNodeDetail`响应参数`key`、`value`改为非必填
  - 接口`UpdateEdgeNode`响应参数`key`、`value`改为非必填
  - 接口`CreateEdgeGroup`新增请求参数 `device_ids`
  - 接口`ListEdgeGroupCerts`:
    - 新增响应参数 `groupcerts`
    - 移除响应参数 `edge_groups`
  - 接口`ListDevices`响应参数`type`改为非必填
  - 接口`CreateDevice`请求参数`type`改为非必填
  - 接口`ShowDevice`响应参数`type`改为非必填
  - 接口`UpdateDevice`响应参数`type`改为非必填
  - 接口`ShowDeviceTwin`响应参数`type`改为非必填
  - 接口`UpdateDeviceTwin`:
    - 请求参数`twin`、`property_visitors`改为非必填
    - 响应参数`type`改为非必填
  - 接口`ListDeviceTemplates`响应参数`key`、`value`改为非必填
  - 接口`CreateDeviceTemplate`请求参数`key`、`value`改为非必填
  - 接口`ShowDeviceTemplate`响应参数`key`、`value`改为非必填
  - 接口`UpdateDeviceTemplateById`响应参数`key`、`value`改为非必填
  - 接口`ListResourceByTags`响应参数`key`、`value`改为非必填
  - 接口`BatchAddDeleteTags`请求参数`key`、`value`改为非必填
  - 接口`ListApps`响应参数`read_only`改为非必填
  - 接口`ShowAppDetail`响应参数`read_only`改为非必填
  - 接口`UpdateApp`响应参数`read_only`改为非必填
  - 接口`ListAppVersions`响应参数`read_only`改为非必填
  - 接口`CreateAppVersions`请求参数`read_only`改为非必填
  - 接口`ShowAppVersionDetail`响应参数`read_only`改为非必填
  - 接口`UpdateAppVersion`:
    - 请求参数`read_only`改为非必填
    - 响应参数`read_only`改为非必填
  - 接口`ListDeployments`响应参数`host_network`、`read_only`改为非必填
  - 接口`CreateDeployments`请求参数`host_network`、`read_only`改为非必填
  - 接口`ShowDeployment`响应参数`host_network`、`read_only`改为非必填
  - 接口`UpdateDeployment`:
    - 请求参数`replicas`、`host_network`、`read_only`改为非必填
    - 响应参数`host_network`、`read_only`改为非必填
  - 接口`ListPods`响应参数`host_network`、`read_only`改为非必填
  - 接口`CreateEncryptdatas`请求参数`description`改为非必填
  - 接口`UpdateEncryptdatas`请求参数`description`改为非必填
  - 接口`ListBatchJob`:
    - 新增响应参数 `task_total_count`、`task_success_count`、`task_failed_count`、`status_last_updated_at`、`description`
    - 移除响应参数 `task_count`、`success_count`、`failed_count`、`updated_at`
  - 接口`ShowBatchJob`:
    - 新增响应参数 `status_last_updated_at`
    - 移除响应参数 `updated_at`

### HuaweiCloud SDK Live

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateRecordCallbackConfig`新增请求参数 `key`
  - 接口`UpdateRecordCallbackConfig`:
    - 新增请求参数 `key`
    - 新增响应参数 `id`、`publish_domain`、`app`、`notify_callback_url`、`notify_event_subscription`、`sign_type`、`create_time`、`update_time`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateSqlAlarmRule`新增请求参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`CreateSqlAlarmRule`新增请求参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`ListSqlAlarmRules`新增响应参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`UpdateKeywordsAlarmRule`新增请求参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`CreateKeywordsAlarmRule`新增请求参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`ListKeywordsAlarmRules`新增响应参数 `trigger_condition_count`、`trigger_condition_frequency`、`whether_recovery_policy`、`recovery_policy`
  - 接口`ListHost`请求参数`host_id_list`改为非必填
  - 接口`UpdateStructConfig`请求参数`is_analysis`、`is_analysis`改为非必填
  - 接口`CreateStructConfig`请求参数`is_analysis`、`is_analysis`改为非必填

### HuaweiCloud SDK OSM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListAuthorizations`新增响应参数 `resource_type_id`

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`StartInstanceRestartAction`请求参数`restart`改为必填

### HuaweiCloud SDK Workspace

- _新增特性_
  - 支持接口`ShowQuotas`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.15 2022-12-08

### HuaweiCloud SDK MapDS

- _新增特性_
  - 支持地图数据服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持接口`GetExecutionPlan`、`DeleteExecutionPlan`、`DescribeExecutionPlan`、`GetStackMetadata`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListExecutionPlans`移除请求参数 `executor`
  - 接口`CreateExecutionPlan`移除请求参数 `executor`
  - 接口`ApplyExecutionPlan`移除请求参数 `executor`
  - 接口`ListStackEvents`:
    - 移除请求参数 `limit`、`marker`、`executor`
    - 移除响应参数 `next_marker`
  - 接口`ListStacks`移除请求参数 `executor`
  - 接口`CreateStack`移除请求参数 `executor`
  - 接口`GetStackTemplate`移除请求参数 `executor`
  - 接口`ListStackResources`:
    - 移除请求参数 `executor`
    - 移除响应参数 `create_time`、`update_time`
  - 接口`ListStackOutputs`:
    - 移除请求参数 `executor`、`limit`、`marker`
    - 移除响应参数 `next_marker`
  - 接口`DeployStack`移除请求参数 `executor`
  - 接口`DeleteStack`移除请求参数 `executor`

### HuaweiCloud SDK APM

- _新增特性_
  - 支持接口`SearchAgent`、`ChangeAgentStatus`、`DeleteAgent`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CBH

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCbhInstance`:
    - 新增响应参数 `public_ip`、`is_auto_renew`
    - 移除请求参数 `X-Auth-Token`
    - 移除响应参数 `publicip`
    - 响应参数`zh_cn`、`en_us`、`exp_time`、`start_time`、`end_time`、`release_time`、`instance_id`、`private_ip`、`task_status`、`vpc_id`、`subnet_id`、`security_group_id`、`createinstance_status`、`fail_reason`、`instance_key`、`order_id`、`period_num`、`resource_id`、`public_id`、`alter_permit`、`bastion_version`、`new_bastion_version`、`instance_status`、`instance_description`改为必填

### HuaweiCloud SDK CC

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateAddonInstance`请求参数`version`改为非必填
  - 接口`UpdateAddonInstance`请求参数`version`改为非必填

### HuaweiCloud SDK CFW

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListIpsSwitchStatusUsingGet`:
    - 新增响应参数 `id`、`virtual_patches_status`
    - 移除响应参数 `object_id`、`virtual_patches_stauts`
  - 接口`ChangeIpsSwitchUsingPost`请求参数`ips_type`改为必填
  - 接口`ListFirewallUsingGet`移除响应参数 `fw_instance_id`、`resource_id`、`name`、`ha_type`、`charge_mode`、`service_type`、`engine_type`、`flavor`、`protect_objects`、`status`、`description`、`is_old_firewall_instance`、`support_ipv6`、`feature_toggle`

### HuaweiCloud SDK CloudDeploy

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`StartDeployTask`请求参数`type`新增枚举值`enum`

### HuaweiCloud SDK DBSS

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchCreateJobsAsync`请求参数`name`、`job_type`、`engine_type`、`job_direction`、`task_type`、`net_type`、`enterprise_project_id`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`is_auto_renew`、`security_group_id`改为非必填
  - 接口`CreateJob`请求参数`name`、`job_type`、`engine_type`、`job_direction`、`task_type`、`net_type`、`enterprise_project_id`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`is_auto_renew`、`security_group_id`改为非必填
  - 接口`ListAsyncJobDetail`响应参数`name`、`job_type`、`engine_type`、`job_direction`、`task_type`、`net_type`、`enterprise_project_id`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`is_auto_renew`、`security_group_id`改为非必填
  - 接口`UpdateBatchAsyncJobs`请求参数`name`、`job_type`、`engine_type`、`job_direction`、`task_type`、`net_type`、`enterprise_project_id`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`is_auto_renew`、`security_group_id`改为非必填
  - 接口`ShowJobDetail`响应参数`name`、`job_type`、`engine_type`、`job_direction`、`task_type`、`net_type`、`enterprise_project_id`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`is_auto_renew`、`security_group_id`改为非必填
  - 接口`UpdateJob`请求参数`name`、`job_type`、`engine_type`、`job_direction`、`task_type`、`net_type`、`enterprise_project_id`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`、`is_auto_renew`、`security_group_id`改为非必填
  - 接口`ExecuteJobAction`:
    - 新增请求参数 `is_sync_re_edit`、`force_delete`
    - 请求参数`job_id`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`改为非必填
  - 接口`BatchExecuteJobActions`:
    - 新增请求参数 `is_sync_re_edit`、`force_delete`
    - 请求参数`job_id`、`ip`、`db_port`、`ssl_link`、`ssl_cert_name`、`ssl_cert_key`、`ssl_cert_check_sum`改为非必填

### HuaweiCloud SDK DSC

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持接口`ListHostOverview`、`ListHostDisk`、`ListHostNet`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK EIP

- _新增特性_
  - 支持以下接口：
    - `ListBandwidthPkg`
    - `CountPublicIp`
    - `ShowPublicIpType`
    - `CountPublicIpInstance`
    - `BatchCreatePublicips`
    - `BatchDeletePublicIp`
    - `BatchDisassociatePublicips`
    - `CountEipAvailableResources`
- _解决问题_
  - 无
- _特性变更_
  - 接口`AssociatePublicips`请求参数`associate_instance_type`移除枚举值``
  - 接口`UpdateAssociatePublicip`请求参数`associate_instance_type`移除枚举值``

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDependency`新增响应参数 `dep_id`
  - 接口`CreateDependencyVersion`新增响应参数 `dep_id`
  - 接口`UpdateFunctionConfig`新增请求参数 `enable_dynamic_memory`、`enable_auth_in_header`
  - 接口`ShowWorkflowExecutionForPage`:
    - 新增请求参数 `offset`、`limit`
    - 新增响应参数 `total`、`size`、`executions`
    - 移除请求参数 `page`、`page_size`
    - 移除响应参数 `pager`、`hisRecords`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListAvailableFlavorInfos`:
    - 新增请求参数 `x-auth-token`
    - 新增响应参数 `list`
    - 移除响应参数 `optional_flavor_list`
    - 响应参数`instance_id`、`instance_name`、`vcpus`、`ram`、`spec_code`、`az_status`、`region_status`、`total_count`改为必填
  - 接口`ShowSlowLogDesensitization`:
    - 新增请求参数 `x-auth-token`
    - 响应参数`desensitization_status`改为必填
  - 接口`ListProjectTags`响应参数`type`、`key`、`values`、`total_count`改为必填
  - 接口`ModifyEpsQuotas`请求参数`instance`、`vcpus`、`ram`改为必填
  - 接口`ListEpsQuotas`:
    - 移除响应参数 `enterprise_project_id`、`enterprise_project_name`、`quota`、`used`
    - 响应参数`total_count`改为必填

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ResizeInstance`新增请求参数 `publicip_id`

### HuaweiCloud SDK LTS

- _新增特性_
  - 支持接口`ListTimeLineTrafficStatistics`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持接口`DownloadAttachment`、`DeleteAttachment`、`ListStatusStatistic`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateIssueV4`新增响应参数 `user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`
  - 接口`ListIssuesSfV4`新增响应参数 `user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`
  - 接口`ListIssuesV4`新增响应参数 `user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`
  - 接口`UpdateIssueV4`新增响应参数 `user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`
  - 接口`ShowIssueV4`新增响应参数 `user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`
  - 接口`ListChildIssuesV4`新增响应参数 `user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`
  - 接口`ListProjectIssuesRecordsV4`新增响应参数 `user_id`、`user_num_id`
  - 接口`CreateSystemIssueV4`新增响应参数 `user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`、`user_id`、`user_num_id`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ShowSecondLevelMonitoring`、`SetSecondLevelMonitor`、`ShowAutoEnlargePolicy`、`SetAutoEnlargePolicy`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreatePostPaidInstance`请求参数`broker_num`改为必填
  - 接口`UpdateInstance`:
    - 新增请求参数 `enable_acl`
    - 移除请求参数 `retention_policy`
  - 接口`BatchUpdateConsumerGroup`新增响应参数 `job_id`
  - 接口`ShowGroup`:
    - 新增响应参数 `app_id`、`app_name`、`permissions`
    - 移除响应参数 `from_beginning`

### HuaweiCloud SDK TMS

- _新增特性_
  - 支持以下接口：
    - `ListResource`
    - `CreateResourceTag`
    - `DeleteResourceTag`
    - `ListTagKeys`
    - `ListTagValues`
    - `ShowResourceTag`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.14 2022-12-01

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerselfResourceRecords`新增响应参数 `formula`

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerselfResourceRecords`新增响应参数 `formula`

### HuaweiCloud SDK CFW

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListIpsSwitchStatusUsingGet`:
    - 新增响应参数 `data`
    - 移除响应参数 `object_id`、`basic_defense_status`、`virtual_patches_stauts`
  - 接口`ListEastWestFirewall`:
    - 新增响应参数 `protect_infos`
    - 移除响应参数 `protected_infos`
  - 接口`ListAttackLogs`请求参数`fw_instance_id`改为非必填
  - 接口`UpdateRuleAclUsingPut`新增请求参数 `type`
  - 接口`UpdateBlackWhiteListUsingPut`新增请求参数 `list_type`、`object_id`
  - 接口`ListFirewallUsingGet`:
    - 新增响应参数 `data`
    - 移除响应参数 `fw_instance_id`、`resource_id`、`name`、`ha_type`、`charge_mode`、`service_type`、`engine_type`、`flavor`、`protect_objects`、`status`、`description`、`is_old_firewall_instance`、`support_ipv6`、`feature_toggle`
  - 接口`ListServiceSetDetails`:
    - 新增响应参数 `data`
    - 移除响应参数 `id`、`name`、`description`
  - 接口`CountEips`:
    - 新增响应参数 `data`
    - 移除响应参数 `object_id`、`eip_total`、`eip_protected`
  - 接口`ListEipResources`:
    - 新增响应参数 `data`
    - 移除响应参数 `id`、`public_ip`、`status`、`public_ipv6`、`enterprise_project_id`、`device_id`、`device_name`、`device_owner`、`associate_instance_type`
  - 接口`UpdateAddressSetInfoUsingPut`新增请求参数 `address_type`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`CreateAcceptance`、`CreateRequest`、`ShowResult`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持接口`AsyncInvokeReservedFunction`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDependencies`响应参数`runtime`新增枚举值`http`
  - 接口`ListDependencyVersion`响应参数`runtime`新增枚举值`http`
  - 接口`CreateFunction`:
    - 请求参数`runtime`新增枚举值`http`
    - 响应参数`runtime`新增枚举值`http`
  - 接口`ListFunctions`响应参数`runtime`新增枚举值`http`
  - 接口`UpdateFunctionCode`响应参数`runtime`新增枚举值`http`
  - 接口`ShowFunctionCode`响应参数`runtime`新增枚举值`http`
  - 接口`UpdateFunctionConfig`:
    - 请求参数`runtime`新增枚举值`http`
    - 响应参数`runtime`新增枚举值`http`
  - 接口`ShowFunctionConfig`响应参数`runtime`新增枚举值`http`
  - 接口`UpdateFunctionMaxInstanceConfig`响应参数`runtime`新增枚举值`http`
  - 接口`ListReservedInstanceConfigs`:
    - 新增响应参数 `reservedinstances`、`page_info`、`count`
    - 移除响应参数 `function_urn`、`qualifier_type`、`qualifier_name`、`min_count`、`idle_mode`、`tactics_config`
  - 接口`CreateFunctionVersion`响应参数`runtime`新增枚举值`http`
  - 接口`ListFunctionVersions`响应参数`runtime`新增枚举值`http`
  - 接口`ImportFunction`响应参数`runtime`新增枚举值`http`

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListProPricePlans`新增请求参数 `sim_card_id`、`partner`、`package_type`、`sim_type`
  - 接口`ListSimCards`:
    - 新增请求参数 `expire_time_duration`、`traffic_warning_threshold`、`sim_status_in`
    - 新增响应参数 `sn`、`supply_code`、`bundle_id`、`test_type`
  - 接口`StopSimCard`:
    - 新增请求参数 `price_plan_list`
    - 新增响应参数 `sim_price_plan_list`
  - 接口`ResetSimCard`:
    - 新增请求参数 `price_plan_list`
    - 新增响应参数 `sim_price_plan_list`
  - 接口`ShowSimCard`新增响应参数 `sn`、`supply_code`、`bundle_id`、`test_type`
  - 接口`ListSimPools`新增响应参数 `order_id`
  - 接口`ListSimPricePlans`:
    - 新增请求参数 `sim_price_plan_id`
    - 新增响应参数 `partner`、`partner_pid`
  - 接口`CreateAttribute`新增响应参数 `id`

### HuaweiCloud SDK Image

- _新增特性_
  - 支持接口`RunQueryCustomTags`、`RunDeleteCustomTags`、`RunImageMediaTaggingDet`
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunImageMediaTagging`新增请求参数 `use_default_tags`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`CopyConfiguration`、`ListInstanceParamHistories`、`ListMsdtcHosts`、`BatchAddMsdtcs`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IEF

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListEdgeNodes`:
    - 新增响应参数 `identifier`
  - 接口`ShowEdgeNodeDetail`:
    - 新增响应参数 `identifier`
  - 接口`UpdateEdgeNode`:
    - 新增响应参数 `identifier`
  - 接口`UpdateNodeByDeviceId`:
    - 请求参数`relation`、`comment`改为非必填
    - 响应参数`relation`、`comment`改为非必填
  - 接口`ListApps`:
    - 新增响应参数 `run_as_user`
    - 响应参数`host_pid`类型调整 `string` -> `boolean`
  - 接口`ShowAppDetail`:
    - 新增响应参数 `run_as_user`
    - 响应参数`host_pid`类型调整 `string` -> `boolean`
  - 接口`UpdateApp`:
    - 新增响应参数 `run_as_user`
    - 响应参数`host_pid`类型调整 `string` -> `boolean`
  - 接口`ListAppVersions`:
    - 新增响应参数 `run_as_user`
    - 响应参数`host_pid`类型调整 `string` -> `boolean`
  - 接口`CreateAppVersions`:
    - 新增请求参数 `run_as_user`
    - 请求参数`host_pid`类型调整 `string` -> `boolean`
  - 接口`ShowAppVersionDetail`:
    - 新增响应参数 `run_as_user`
    - 响应参数`host_pid`类型调整 `string` -> `boolean`
  - 接口`UpdateAppVersion`:
    - 新增请求参数`run_as_user`
    - 新增响应参数 `run_as_user`
    - 请求参数`host_pid`类型调整 `string` -> `boolean`
    - 响应参数`host_pid`类型调整 `string` -> `boolean`
  - 接口`ListDeployments`:
    - 新增响应参数 `run_as_user`、`run_as_user`
  - 接口`CreateDeployments`新增请求参数 `run_as_user`、`run_as_user`
  - 接口`ShowDeployment`:
    - 新增响应参数 `run_as_user`、`run_as_user`
  - 接口`UpdateDeployment`:
    - 新增请求参数 `run_as_user`、`run_as_user`
    - 新增响应参数 `run_as_user`、`run_as_user`

# 3.1.13 2022-11-30

### HuaweiCloud SDK AOM

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`AddAlarmRule`请求参数`statistic`类型调整 `string` -> `enum`

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateApiV2`新增请求参数 `retry_count`、`retry_count`
  - 接口`UpdateApiV2`:
    - 新增请求参数 `retry_count`、`retry_count`
    - 新增响应参数 `retry_count`、`retry_count`
  - 接口`ShowDetailsOfApiV2`新增响应参数 `retry_count`、`retry_count`
  - 接口`ListApiVersionDetailV2`新增响应参数 `retry_count`、`retry_count`
  - 接口`AssociateDomainV2`新增请求参数 `is_http_redirect_to_https`
  - 接口`UpdateDomainV2`新增请求参数 `is_http_redirect_to_https`
  - 接口`ImportMicroservice`新增请求参数 `labels`
  - 接口`ListAttachedDomainsV2`新增响应参数 `is_http_redirect_to_https`

### HuaweiCloud SDK CPH

- _新增特性_
  - 支持接口`PushFile`、`InstallApk`、`UninstallApk`、`PushShareFiles`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`DeleteShareFiles`
  - 接口`ShowBandwidthDetail`响应参数`band_widths`、`request_id`改为非必填
  - 接口`UpdateBandwidth`响应参数`request_id`改为非必填
  - 接口`ListEncodeServers`响应参数`encode_servers`、`request_id`改为非必填
  - 接口`RestartEncodeServer`响应参数`jobs`、`request_id`改为非必填
  - 接口`ListJobs`响应参数`jobs`、`request_id`改为非必填
  - 接口`ShowJob`响应参数`error_msg`、`execute_msg`、`job_id`、`end_time`、`begin_time`、`error_code`、`status`、`request_id`改为非必填
  - 接口`ListCloudPhoneImages`响应参数`phone_images`、`request_id`改为非必填
  - 接口`ListCloudPhoneModels`:
    - 新增请求参数 `status`
    - 响应参数`phone_models`、`request_id`改为非必填
  - 接口`ListCloudPhones`响应参数`phones`、`request_id`改为非必填
  - 接口`CreateCloudPhoneServer`响应参数`order_id`、`product_id`、`request_id`改为非必填
  - 接口`ImportTraffic`响应参数`jobs`、`request_id`改为非必填
  - 接口`ShowCloudPhoneDetail`响应参数`phone_name`、`server_id`、`phone_id`、`image_id`、`vnc_enable`、`phone_model_name`、`status`、`access_infos`、`property`、`metadata`、`create_time`、`update_time`、`request_id`改为非必填
  - 接口`UpdatePhoneName`响应参数`request_id`改为非必填
  - 接口`BatchMigrateCloudPhone`响应参数`jobs`、`request_id`改为非必填
  - 接口`ResetCloudPhone`响应参数`jobs`、`request_id`改为非必填
  - 接口`RestartCloudPhone`响应参数`jobs`、`request_id`改为非必填
  - 接口`BatchImportCloudPhoneData`响应参数`jobs`、`request_id`改为非必填
  - 接口`StopCloudPhone`响应参数`jobs`、`request_id`改为非必填
  - 接口`BatchExportCloudPhoneData`响应参数`jobs`、`request_id`改为非必填
  - 接口`UpdateCloudPhoneProperty`响应参数`jobs`、`request_id`改为非必填
  - 接口`RunShellCommand`响应参数`jobs`、`request_id`改为非必填
  - 接口`PushShareApps`响应参数`jobs`、`request_id`改为非必填
  - 接口`DeleteShareApps`响应参数`jobs`、`request_id`改为非必填
  - 接口`DeleteShareFiles`:
    - 新增请求参数 `DeleteShareFilesRequestBody`
    - 移除请求参数 `PushShareFilesRequestBody`
    - 响应参数`jobs`、`request_id`改为非必填
  - 接口`RunSyncCommand`响应参数`jobs`、`request_id`改为非必填
  - 接口`ListCloudPhoneServerModels`响应参数`server_models`、`request_id`改为非必填
  - 接口`ListCloudPhoneServers`响应参数`servers`、`request_id`改为非必填
  - 接口`ShowCloudPhoneServerDetail`响应参数`server_name`、`availability_zone`、`server_id`、`server_model_name`、`phone_model_name`、`keypair_name`、`status`、`vpc_id`、`cidr`、`vpc_cidr`、`subnet_id`、`subnet_cidr`、`resource_project_id`、`metadata`、`intranet_ip`、`access_ip`、`server_ip`、`public_ip`、`band_width_name`、`band_width_id`、`band_width_size`、`band_width_charge_mode`、`band_width_share_type`、`create_time`、`update_time`、`volume_name`、`volume_id`、`volume_size`、`volume_type`、`create_time`、`update_time`、`network_version`、`security_groups`、`create_time`、`update_time`、`request_id`改为非必填
  - 接口`UpdateServerName`响应参数`request_id`改为非必填
  - 接口`RestartCloudPhoneServer`响应参数`jobs`、`request_id`改为非必填
  - 接口`ChangeCloudPhoneServerModel`响应参数`order_id`、`product_id`、`request_id`改为非必填
  - 接口`UpdateKeypair`响应参数`jobs`、`request_id`改为非必填
  - 接口`ListShareFiles`响应参数`jobs`、`request_id`改为非必填
  - 接口`CreateNet2CloudPhoneServer`响应参数`order_id`、`product_id`、`request_id`改为非必填

### HuaweiCloud SDK DDM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ExpandInstanceNodes`新增请求参数 `is_auto_pay`

### HuaweiCloud SDK DDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`AddReadonlyNode`请求参数`num`类型调整 `string` -> `int32`

### HuaweiCloud SDK EIP

- _新增特性_
  - 支持接口`DisassociatePublicips`、`AssociatePublicips`
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
  - 接口`ShowTenantMetric`新增请求参数 `metric_type`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ModifyPublicIp`请求参数`public_ip`、`public_ip_id`改为非必填
  - 接口`SwitchToMaster`新增请求参数 `SwitchToMasterDisasterRecoveryBody`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowBackupPolicy`新增响应参数 `enable_standby_backup`
  - 接口`SetBackupPolicy`新增请求参数 `enable_standby_backup`

### HuaweiCloud SDK MPC

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`UpdateClusterName`、`ShowAutoScalingPolicy`
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateAgencyMapping`响应参数`result`改为必填

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`响应参数`read_only_by_user`类型调整 `string` -> `boolean`

### HuaweiCloud SDK ROMA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateProduct`移除响应参数 `status`
  - 接口`ListProperties`移除响应参数 `bool_false`、`bool_true`
  - 接口`CreateProperty`移除请求参数 `bool_false`、`bool_true`
  - 接口`ShowProperty`移除响应参数 `bool_false`、`bool_true`
  - 接口`UpdateProperty`:
    - 移除请求参数 `bool_false`、`bool_true`
    - 移除响应参数 `bool_false`、`bool_true`
  - 接口`ListRequestProperties`移除响应参数 `bool_false`、`bool_true`
  - 接口`CreateRequestProperty`:
    - 移除请求参数 `bool_false`、`bool_true`
    - 移除响应参数 `bool_false`、`bool_true`
  - 接口`ShowRequestProperty`移除响应参数 `bool_false`、`bool_true`
  - 接口`UpdateRequestProperty`:
    - 移除请求参数 `bool_false`、`bool_true`
    - 移除响应参数 `bool_false`、`bool_true`
  - 接口`ListResponseProperties`移除响应参数 `bool_false`、`bool_true`
  - 接口`CreateResponseProperty`移除请求参数 `bool_false`、`bool_true`
  - 接口`ShowResponseProperty`移除响应参数 `bool_false`、`bool_true`
  - 接口`UpdateResponseProperty`:
    - 移除请求参数 `bool_false`、`bool_true`
    - 移除响应参数 `bool_false`、`bool_true`
  - 接口`CreateApiV2`新增请求参数 `cookie_param_name`、`alias_urn`、`cookie_param_name`、`alias_urn`、`cookie_param_name`
  - 接口`ShowDetailsOfApiV2`新增响应参数 `cookie_param_name`、`alias_urn`、`alias_urn`、`cookie_param_name`、`cookie_param_name`
  - 接口`UpdateApiV2`:
    - 新增请求参数 `cookie_param_name`、`alias_urn`、`cookie_param_name`、`alias_urn`、`cookie_param_name`
    - 新增响应参数 `cookie_param_name`、`alias_urn`、`alias_urn`、`cookie_param_name`、`cookie_param_name`
  - 接口`ListApiVersionDetailV2`新增响应参数 `cookie_param_name`、`alias_urn`、`alias_urn`、`cookie_param_name`、`cookie_param_name`
  - 接口`ListVpcChannelsV2`新增响应参数 `microservice_info`、`type`
  - 接口`ShowDetailsOfVpcChannelV2`新增响应参数 `microservice_info`、`type`
  - 接口`UpdateVpcChannelV2`新增响应参数 `microservice_info`、`type`
  - 接口`ListProjectVpcChannelsV2`新增响应参数 `microservice_info`、`type`
  - 接口`UpdateProjectVpcChannel`新增响应参数 `microservice_info`、`type`
  - 接口`ShowDetailsOfInstanceV2`新增响应参数 `ingress_ips`

### HuaweiCloud SDK SIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`PushTranscriberJobs`请求参数`property`新增枚举值`chinese_8k_general`
  - 接口`RunTts`请求参数`property`新增枚举值`chinese_huaxiaoru_common`、`chinese_huaxiaohan_common`、`chinese_huaxiaoning_common`、`chinese_huaxiaozhen_common`、`english_alvin_common`、`english_amy_common`

# 3.1.12 2022-11-24

### HuaweiCloud SDK DWR

- _新增特性_
  - 支持数据工坊服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持接口`ListStackEvents`、`ListStackResources`、`DeleteStack`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK APM

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`DeleteEnv`
  - 接口`ListAkSk`:
    - 响应参数`gmt_create`类型调整 `date` -> `string`
    - 响应参数`gmt_modify`类型调整 `date` -> `string`
  - 接口`SaveMonitorItemConfig`请求参数`monitor_item_id`、`env_id`改为必填
  - 接口`ListEnvMonitorItem`请求参数`x-business-id`
  - 接口`ShowTopologyTree`请求参数`business_id`改为非必填
  - 接口`ListEnvTags`:
    - 请求参数`business_id`改为必填
    - 响应参数`gmt_create`类型调整 `date` -> `string`
    - 响应参数`gmt_modify`类型调整 `date` -> `string`
  - 接口`ShowSpanSearch`请求参数`region`、`biz_id`改为必填
  - 接口`ShowRawTable`请求参数`view_type`、`collector_name`、`metric_set`、`title`、`table_direction`、`group_by`、`filter`、`span`、`span_field`、`page`、`page_size`、`search_word`、`instance_id`、`monitor_item_id`、`env_id`、`start_time`、`end_time`改为必填
  - 接口`ShowClobDetail`请求参数`env_id`、`clob_id`改为必填
  - 接口`ListEnvInstances`请求参数`env_id`、`page`、`page_size`改为必填
  - 接口`ShowAkSks`:
    - 响应参数`gmt_create`类型调整 `date` -> `string`
    - 响应参数`gmt_modify`类型调整 `date` -> `string`

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSubCustomerBillDetail`新增响应参数 `sub_service_type_code`、`sub_service_type_name`、`sub_resource_type_code`、`sub_resource_type_name`、`sub_resource_id`、`sub_resource_name`

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowBackup`新增响应参数 `children`
  - 接口`ListBackups`新增响应参数 `children`

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCluster`新增请求参数 `configurationsOverride`
  - 接口`ListClusters`新增响应参数 `configurationsOverride`
  - 接口`UpdateCluster`:
    - 新增请求参数 `eniNetwork`、`hostNetwork`
    - 新增响应参数 `configurationsOverride`
  - 接口`DeleteCluster`:
    - 新增请求参数 `delete_sfs30`
    - 新增响应参数 `configurationsOverride`
  - 接口`ShowCluster`新增响应参数 `configurationsOverride`
  - 接口`CreateNode`新增请求参数 `initializedConditions`
  - 接口`ListNodes`新增响应参数 `initializedConditions`
  - 接口`UpdateNode`新增响应参数 `initializedConditions`
  - 接口`DeleteNode`新增响应参数 `initializedConditions`
  - 接口`ShowNode`新增响应参数 `initializedConditions`
  - 接口`AddNode`新增请求参数 `initializedConditions`
  - 接口`ResetNode`新增请求参数 `initializedConditions`
  - 接口`CreateNodePool`新增请求参数 `customSecurityGroups`、`initializedConditions`
  - 接口`ListNodePools`新增响应参数 `customSecurityGroups`、`initializedConditions`
  - 接口`UpdateNodePool`:
    - 新增请求参数 `initializedConditions`
    - 新增响应参数 `customSecurityGroups`、`initializedConditions`
  - 接口`DeleteNodePool`新增响应参数 `customSecurityGroups`、`initializedConditions`
  - 接口`ShowNodePool`新增响应参数 `customSecurityGroups`、`initializedConditions`

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

- _新增特性_
  - 支持接口`UpgradeEngine`、`RetryEngine`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSS

- _新增特性_
  - 支持接口`UpdateInstance`、`ChangeMode`、`AddIndependentNode`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClustersDetails`新增响应参数 `totalSize`、`volume`
  - 接口`ShowClusterDetail`新增响应参数 `volume`
  - 接口`StartVpecp`请求参数`endpointWithDnsName`改为非必填

### HuaweiCloud SDK DAS

- _新增特性_
  - 支持以下接口：
    - `ShowSqlLimitSwitchStatus`
    - `ChangeSqlLimitSwitchStatus`
    - `ListSqlLimitRules`
    - `CreateSqlLimitRules`
    - `DeleteSqlLimitRules`
    - `ExportTopSqlTemplatesDetails`
    - `ShowSqlLimitJobInfo`
    - `ExportSlowSqlTemplatesDetails`
    - `ExportTopSqlTrendDetails`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowQuotas`响应参数`quotas`类型调整 `object` -> `array`

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持以下接口：
    - `ListAppliedInstances`
    - `ShowConfigurationAppliedHistory`
    - `ShowConfigurationModifyHistory`
    - `CompareConfiguration`
    - `CopyConfiguration`
    - `ResetConfiguration`
    - `ListTasks`
- _解决问题_
  - 无
- _特性变更_
  - 接口`AddReadonlyNode`新增请求参数 `is_auto_pay`

### HuaweiCloud SDK DNS

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持以下接口：
    - `CreateDependencyVersion`
    - `ListDependencyVersion`
    - `ShowDependencyVersion`
    - `DeleteDependencyVersion`
    - `ListReservedInstanceConfigs`
    - `ListFunctionReservedInstances`
    - `ListFunctionAsMetric`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`AsyncInvokeReservedFunction`
  - 接口`UpdateFunctionConfig`新增请求参数 `custom_image`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持以下接口：
    - `ResizeColdVolume`
    - `CreateColdVolume`
    - `ModifyPublicIp`
    - `SwitchSsl`
    - `SetAutoEnlargePolicy`
    - `RestartInstance`
    - `ShowApplicableInstances`
    - `ShowModifyHistory`
    - `ShowApplyHistory`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`新增请求参数 `restore_info`、`port`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeHealthCode`新增响应参数 `test_interval`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ShowDomainName`、`ShowDnsName`、`ShowReplicationStatus`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ROMA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDatasourceInfo`:
    - 新增请求参数 `ssl`
    - 移除请求参数 `custom_plugin_id`
    - 请求参数`datasource_name`、`datasource_type`、`app_id`改为必填
  - 接口`ListDatasources`新增响应参数 `ssl`
  - 接口`UpdateDatasourceInfo`:
    - 新增请求参数 `ssl`
    - 新增响应参数 `ssl`
    - 移除请求参数 `custom_plugin_id`
    - 请求参数`datasource_name`、`datasource_type`、`app_id`改为必填
  - 接口`ShowDataourceDetail`新增响应参数 `ssl`
  - 接口`StartTestDatasource`:
    - 新增请求参数 `ssl`
    - 移除请求参数 `custom_plugin_id`
    - 请求参数`datasource_name`、`datasource_type`、`app_id`改为必填
  - 接口`CreateCommonTask`:
    - 移除响应参数 `created_by`
    - 请求参数`task_name`、`task_type`、`source_datasource_id`、`target_datasource_id`、`task_detail`改为必填
  - 接口`UpdateTask`:
    - 移除响应参数 `created_by`
    - 请求参数`task_name`、`task_type`、`source_datasource_id`、`target_datasource_id`、`task_detail`改为必填
  - 接口`ShowTask`移除响应参数 `created_by`
  - 接口`BatchStartOrStopTasks`请求参数`action_id`改为必填
  - 接口`CreateMultiTasks`请求参数`task_name`、`operation_types`改为必填
  - 接口`UpdateMultiTasks`请求参数`operation_types`、`repulling_snapshot`改为必填
  - 接口`CreateMultiTaskMappings`请求参数`source_datasource_id`、`target_datasource_id`改为必填

### HuaweiCloud SDK SA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ImportEvents`:
    - 新增请求参数 `dest_ip`、`cve_ids`
    - 移除请求参数 `destc_ip`
    - 请求参数`first_observed_time`类型调整 `string` -> `date-time`
    - 请求参数`last_observed_time`类型调整 `string` -> `date-time`
    - 请求参数`create_time`类型调整 `string` -> `date-time`
    - 请求参数`arrive_time`类型调整 `string` -> `date-time`
    - 请求参数`release_time`类型调整 `string` -> `date-time`
    - 请求参数`start_time`类型调整 `string` -> `date-time`
    - 请求参数`modified`类型调整 `string` -> `date-time`

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持接口`CreatePrepaidCloudWaf`、`ChangePrepaidCloudWaf`、`ShowSubscriptionInfo`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.11 2022-11-17

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持应用编排服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DC

- _新增特性_
  - 支持云专线服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CFW

- _新增特性_
  - 支持云防火墙服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK APIG

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateVpcChannelV2`新增请求参数 `type`、`microservice_labels`
  - 接口`ListVpcChannelsV2`新增响应参数 `microservice_labels`
  - 接口`ShowDetailsOfVpcChannelV2`新增响应参数 `microservice_labels`
  - 接口`UpdateVpcChannelV2`:
    - 新增请求参数 `type`、`microservice_labels`
    - 新增响应参数 `microservice_labels`
  - 接口`CreateMemberGroup`新增请求参数 `microservice_labels`
  - 接口`ListMemberGroups`新增响应参数 `microservice_labels`
  - 接口`ShowDetailsOfMemberGroup`新增响应参数 `microservice_labels`
  - 接口`UpdateMemberGroup`:
    - 新增请求参数 `microservice_labels`
    - 新增响应参数 `microservice_labels`
  - 接口`CreateInstanceV2`新增请求参数 `tags`

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DeleteServerNics`请求参数`id`改为必填

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateSubEnterpriseAccount`请求参数`sub_customer_association_type`改为必填

### HuaweiCloud SDK CloudArtifact

- _新增特性_
  - 支持接口`ShowProjectReleaseFiles`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CloudDeploy

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDeployTaskByTemplate`请求参数`type`新增枚举值`encrypt`
  - 接口`StartDeployTask`:
    - 新增请求参数 `trigger_source`、`key`
    - 移除请求参数 `description`、`name`、`limits`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持以下接口：
    - `AddExtensionEvaluation`
    - `AddExtensionEvaluationReply`
    - `CheckMaliciousExtensionEvaluation`
    - `DeleteEvaluationReply`
    - `DeleteEvaluation`
    - `AddExtensionStar`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ResizeInstance`请求参数`new_capacity`类型调整 `integer` -> `int32`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchCreateJobs`请求参数`db_type`新增枚举值`gaussdbv5`、`postgresql`、`kafka`、`gaussdbv5ha`
  - 接口`BatchValidateConnections`请求参数`db_type`新增枚举值`gaussdbv5`、`kafka`、`gaussdbv5ha`
  - 接口`BatchUpdateJob`请求参数`db_type`新增枚举值`gaussdbv5`、`postgresql`、`kafka`、`gaussdbv5ha`
  - 接口`ListCompareResult`:
    - 新增响应参数 `line_compare_detail`、`content_compare_diff`、`compare_task_list`
    - 移除响应参数 `LineCompareDetail`、`ContentCompareDiff`、`CompareTaskList`
  - 接口`BatchListJobDetails`:
    - 新增响应参数 `is_multi_az`、`az_name`、`master_az`、`slave_az`、`node_role`
    - 响应参数`db_type`新增枚举值`gaussdbv5`、`postgresql`、`kafka`、`gaussdbv5ha`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RegisterServerMonitor`请求参数`monitorMetrics`类型调整 `string` -> `enum`

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DisassociatePublicips`请求参数`associate_instance_type`新增枚举值`VPN`
  - 接口`AssociatePublicips`请求参数`associate_instance_type`新增枚举值`VPN`

### HuaweiCloud SDK EPS

- _新增特性_
  - 支持接口`ListProviders`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持接口`ShowInstanceRole`、`SwitchToMaster`、`SwitchToSlave`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateMessage`新增请求参数 `ttl`
  - 接口`ListCertificates`新增请求参数 `Sp-Auth-Token`、`Stage-Auth-Token`
  - 接口`AddCertificate`:
    - 新增请求参数 `Sp-Auth-Token`、`Stage-Auth-Token`、`addCertificateRequestBody`
    - 移除请求参数 `AddCertificateRequestBody`
  - 接口`DeleteCertificate`新增请求参数 `Sp-Auth-Token`、`Stage-Auth-Token`
  - 接口`CheckCertificate`:
    - 新增请求参数 `Sp-Auth-Token`、`Stage-Auth-Token`、`checkCertificateRequestBody`
    - 移除请求参数 `CheckCertificateRequestBody`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ResetPassword`请求参数`new_password`改为必填

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeGeneralTable`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeVatInvoice`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeInvoiceVerification`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeGeneralText`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeWebImage`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeHealthCode`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeQuotaInvoice`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeIdCard`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeHandwriting`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeVehicleLicense`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeTransportationLicense`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeTaxiInvoice`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeAutoClassification`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeTollInvoice`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeMvsInvoice`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeLicensePlate`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeFlightItinerary`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeBusinessLicense`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeDriverLicense`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeBusinessCard`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeTrainTicket`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeVin`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizePassport`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeBankcard`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeInsurancePolicy`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeFinancialStatement`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeQualificationCertificate`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeThailandIdcard`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeMyanmarIdcard`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeMyanmarDriverLicense`:
    - 新增请求参数 `Enterprise-Project-Id`
    - 新增响应参数 `birth`、`birth`
    - 移除响应参数 `Birth`、`Birth`
  - 接口`RecognizeChileIdCard`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeThailandLicensePlate`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeWaybillElectronic`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizePcrTestRecord`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeIdDocument`:
    - 新增请求参数 `Enterprise-Project-Id`
    - 响应参数`result`类型调整 `object` -> `object`
  - 接口`RecognizeHkIdCard`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeCambodianIdCard`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeExitEntryPermit`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeMainlandTravelPermit`新增请求参数 `Enterprise-Project-Id`
  - 接口`RecognizeMacaoIdCard`新增请求参数 `Enterprise-Project-Id`

### HuaweiCloud SDK OSM

- _新增特性_
  - 支持接口`RevokeMessage`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ROMA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDeviceGroup`移除响应参数 `app_name`
  - 接口`ShowDeviceGroupTree`移除响应参数 `total`、`app_id`、`permissions`
  - 接口`UpdateDeviceGroup`移除响应参数 `app_name`
  - 接口`CreateDevice`新增请求参数 `user_name`
  - 接口`ListDevices`:
    - 新增响应参数 `device_id`
    - 移除响应参数 `plugin_id`
  - 接口`BatchFreezeDevices`新增响应参数 `device_id`、`device_id`
  - 接口`UpdateDevice`:
    - 新增响应参数 `device_id`
    - 移除响应参数 `plugin_id`
  - 接口`ShowDevice`:
    - 新增响应参数 `device_id`
    - 响应参数`status`类型调整 `enum` -> `integer`
    - 响应参数`online_status`类型调整 `enum` -> `integer`
    - 响应参数`device_type`类型调整 `enum` -> `integer`
    - 响应参数`plugin_id`类型调整 `enum` -> `integer`
  - 接口`ListSubsets`:
    - 新增响应参数 `device_id`
    - 移除响应参数 `plugin_id`
  - 接口`ResetAuthentication`新增请求参数 `ResetAuthenticationRequestBody`
  - 接口`UpdateProduct`:
    - 新增响应参数 `status`
    - 移除响应参数 `authentication`
  - 接口`ResetProductAuthentication`新增请求参数 `ResetProductAuthenticationRequestBody`
  - 接口`CreateRule`移除响应参数 `app_name`、`sql_field`、`sql_where`、`rule_express`
  - 接口`CreateProperty`新增请求参数 `enum_dict`、`method`
  - 接口`ListProperties`:
    - 新增响应参数 `enum_dict`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`UpdateProperty`:
    - 新增请求参数 `enum_dict`
    - 新增响应参数 `enum_dict`、`method`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`ShowProperty`:
    - 新增响应参数 `enum_dict`、`method`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`CreateRequestProperty`:
    - 新增请求参数 `enum_dict`、`method`
    - 新增响应参数 `enum_dict`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`ListRequestProperties`:
    - 新增响应参数 `enum_dict`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`UpdateRequestProperty`:
    - 新增请求参数 `enum_dict`
    - 新增响应参数 `enum_dict`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`ShowRequestProperty`:
    - 新增响应参数 `enum_dict`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`CreateResponseProperty`新增请求参数 `enum_dict`、`method`
  - 接口`ListResponseProperties`:
    - 新增响应参数 `enum_dict`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`UpdateResponseProperty`:
    - 新增请求参数 `enum_dict`
    - 新增响应参数 `enum_dict`
    - 响应参数`data_type`新增枚举值`boolean`、`array`
  - 接口`ShowResponseProperty`:
    - 新增响应参数 `enum_dict`
    - 响应参数`data_type`新增枚举值`boolean`、`array`

### HuaweiCloud SDK TMS

- _新增特性_
  - 支持接口`ListProviders`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK UGO

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunSqlConversion`:
    - 请求参数`target_db_type`新增枚举值`GaussDB Centralized`, 移除枚举值`GaussDB(for openGauss)`
    - 请求参数`target_db_version`新增枚举值`2.0`, 移除枚举值`2020`
  - 接口`ConfirmTargetDbType`:
    - 请求参数`target_db_type`类型调整 `string` -> `enum`
    - 请求参数`target_db_version`类型调整 `string` -> `enum`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateSubnet`:
    - 请求参数`opt_name`新增枚举值`addresstime`
    - 响应参数`opt_name`新增枚举值`addresstime`
  - 接口`ListSubnets`响应参数`opt_name`新增枚举值`addresstime`
  - 接口`ShowSubnet`响应参数`opt_name`新增枚举值`addresstime`
  - 接口`UpdateSubnet`请求参数`opt_name`新增枚举值`addresstime`

# 3.1.10 2022-11-14

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DeleteServerNics`响应参数`job_id`改为必填
  - 接口`UpdateBaremetalServerInterfaceAttachments`:
    - 请求参数`delete_on_termination`类型调整 `string` -> `boolean`
    - 请求参数`delete_on_termination`改为必填
  - 接口`ShowServerRemoteConsole`新增响应参数 `remote_console`

### HuaweiCloud SDK CPH

- _新增特性_
  - 支持接口`DeleteShareFiles`
- _解决问题_
  - 无
- _特性变更_
  - 接口`StopCloudPhone`:
    - 新增请求参数 `StopCloudPhoneRequestBody`
    - 移除请求参数 `StopCloudPhoneReuqestBody`
  - 接口`ShowCloudPhoneServerDetail`:
    - 新增响应参数 `server_name`、`availability_zone`、`server_id`、`server_model_name`、`phone_model_name`、`keypair_name`、`status`、`vpc_id`、`cidr`、`vpc_cidr`、`subnet_id`、`subnet_cidr`、`resource_project_id`、`metadata`、`addresses`、`network_version`、`create_time`、`update_time`
    - 移除响应参数 `servers`
  - 接口`CreateNet2CloudPhoneServer`移除请求参数 `br_cidr`

### HuaweiCloud SDK CSMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSecretTags`新增响应参数 `sys_tags`

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持以下接口：
    - `ShowSlowlogDesensitizationSwitch`
    - `ListRecycleInstances`
    - `CheckWeakPassword`
    - `ShowUpgradeDuration`
    - `ShowDiskUsage`
    - `ListSslCertDownloadAddress`
    - `DeleteAuditLog`
    - `ShowRecyclePolicy`
- _解决问题_
  - 无
- _特性变更_
  - 接口`SwitchSlowlogDesensitization`新增请求参数 `X-Language`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持接口`ShowWorkflowExecutionForPage`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListWorkflow`新增响应参数 `enable_stream_response`
  - 接口`UpdateWorkFlow`新增响应参数 `enable_stream_response`

### HuaweiCloud SDK GSL

- _新增特性_
  - 支持接口`ListBackPools`、`ListBackPoolMembers`
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
  - 接口`ListStreamForbidden`移除请求参数 `specify_project`
  - 接口`DeleteStreamForbidden`移除请求参数 `specify_project`
  - 接口`UpdateStreamForbidden`移除请求参数 `specify_project`
  - 接口`CreateStreamForbidden`移除请求参数 `specify_project`
  - 接口`ShowDomain`响应参数`service_area`移除枚举值`global`
  - 接口`UpdateDomain`响应参数`service_area`移除枚举值`global`
  - 接口`CreateDomain`请求参数`service_area`移除枚举值`global`
  - 接口`DeleteDomainMapping`移除请求参数 `specify_project`
  - 接口`CreateDomainMapping`移除请求参数 `specify_project`

### HuaweiCloud SDK MRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListHosts`新增响应参数 `resource_id`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ShowPostgresqlParamValue`、`UpdatePostgresqlParameterValue`、`ListDrRelations`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`请求参数`type`新增枚举值`ESSD`
  - 接口`ListInstances`响应参数`type`新增枚举值`ESSD`
  - 接口`CreateRestoreInstance`请求参数`type`新增枚举值`ESSD`
  - 接口`CreatePostgresqlDatabase`新增请求参数 `is_revoke_public_privilege`

### HuaweiCloud SDK VPCEP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListEndpoints`响应参数`Action`类型调整 `string` -> `array`
  - 接口`DeleteEndpointPolicy`响应参数`Action`类型调整 `string` -> `array`
  - 接口`UpdateEndpointPolicy`:
    - 请求参数`Action`类型调整 `string` -> `array`
    - 响应参数`Action`类型调整 `string` -> `array`

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持接口`MigrateCompositeHosts`、`ShowSourceIp`、`ListNoticeConfigs`、`UpdateAlertNoticeConfig`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstance`新增响应参数 `instance_name`
  - 接口`ShowLtsInfoConfig`新增响应参数 `enabled`、`ltsAttackStreamID`
  - 接口`UpdateLtsInfoConfig`:
    - 新增请求参数 `enabled`、`ltsAttackStreamID`
    - 新增响应参数 `enabled`、`ltsAttackStreamID`
    - 请求参数`enabale`改为非必填
  - 接口`ShowIpGroup`新增响应参数 `description`

# 3.1.9 2022-11-08

### HuaweiCloud SDK HSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListQuotasDetail`:
    - 新增响应参数 `on_demand_num`
    - 移除响应参数 `on_demand_numn`

### HuaweiCloud SDK Meeting

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`SearchMeetings`新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`CreateMeeting`:
    - 新增请求参数 `isHostCameraOn`、`isGuestCameraOn`
    - 新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`UpdateMeeting`:
    - 新增请求参数 `isHostCameraOn`、`isGuestCameraOn`
    - 新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`ShowMeetingDetail`新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`SearchOnlineMeetings`新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`ShowOnlineMeetingDetail`新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`SearchHisMeetings`新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`ShowHisMeetingDetail`新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`CreateRecurringMeeting`:
    - 新增请求参数 `isHostCameraOn`、`isGuestCameraOn`
    - 新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`
  - 接口`UpdateRecurringMeeting`:
    - 新增请求参数 `isHostCameraOn`、`isGuestCameraOn`
    - 新增响应参数 `onlineAttendeeAmount`、`isHostCameraOn`、`isGuestCameraOn`

# 3.1.8 2022-11-03

### HuaweiCloud SDK DevSecurity

- _新增特性_
  - 支持研发安全服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GA

- _新增特性_
  - 支持全球加速服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CloudDeploy

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDeployTasks`新增响应参数 `id`、`release_id`、`duration`、`execution_state`、`executor_id`、`executor_nick_name`、`steps`
  - 接口`ListHosts`新增响应参数 `update_time`、`lastest_connection_time`、`connection_status`、`owner_name`、`updator_id`、`create_time`、`nick_name`、`owner_id`、`updator_name`、`connection_result`
  - 接口`ListHostGroups`:
    - 新增响应参数 `updated_by`
    - 移除响应参数 `update_by`
  - 接口`ShowDeploymentGroupDetail`:
    - 新增响应参数 `updated_by`
    - 移除响应参数 `update_by`
  - 接口`ShowDeploymentHostDetail`新增响应参数 `update_time`、`lastest_connection_time`、`connection_status`、`owner_name`、`updator_id`、`create_time`、`nick_name`、`owner_id`、`updator_name`、`connection_result`
  - 接口`ShowDeployTaskDetail`新增响应参数 `id`、`release_id`、`duration`、`execution_state`、`executor_id`、`executor_nick_name`、`steps`
  - 接口`ListDeployTaskHistoryByDate`新增响应参数 `type`
  - 接口`ShowProjectSuccessRate`:
    - 新增响应参数 `start_date`、`end_date`
    - 移除响应参数 `start_time`、`end_time`
  - 接口`ListTaskSuccessRate`:
    - 新增响应参数 `start_date`、`end_date`
    - 移除响应参数 `start_time`、`end_time`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClustersDetails`:
    - 新增响应参数 `failedReason`
    - 移除响应参数 `failed_reasons`
  - 接口`ShowClusterDetail`:
    - 新增响应参数 `failedReason`
    - 移除响应参数 `failed_reasons`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchValidateConnections`响应参数`status`新增枚举值`true`、`false`
  - 接口`BatchValidateClustersConnections`响应参数`status`新增枚举值`true`、`false`
  - 接口`BatchCheckResults`响应参数`job_direction`新增枚举值`up`、`down`、`non-dbs`
  - 接口`BatchSetSpeed`响应参数`status`新增枚举值`success`、`failed`
  - 接口`ListCompareResult`:
    - 响应参数`object_type`新增枚举值`DB`、`TABLE`、`VIEW`、`EVENT`、`ROUTINE`、`INDEX`、`TRIGGER`、`SYNONYM`、`FUNCTION`、`PROCEDURE`、`TYPE`、`RULE`、`DEFAULT_TYPE`、`PLAN_GUIDE`、`CONSTRAINT`、`FILE_GROUP`、`PARTITION_FUNCTION`、`PARTITION_SCHEME`、`TABLE_COLLATION`
    - 响应参数`object_compare_result`新增枚举值`CONSISTENT`、`INCONSISTENT`、`COMPARING`、`WAITING_FOR_COMPARISON`、`FAILED_TO_COMPARE`、`TARGET_DB_NOT_EXIT`、`CAN_NOT_COMPARE`
    - 响应参数`line_compare_result`新增枚举值`CONSISTENT`、`INCONSISTENT`、`COMPARING`、`WAITING_FOR_COMPARISON`、`FAILED_TO_COMPARE`、`TARGET_DB_NOT_EXIT`、`CAN_NOT_COMPARE`
    - 响应参数`content_compare_result`新增枚举值`CONSISTENT`、`INCONSISTENT`、`COMPARING`、`WAITING_FOR_COMPARISON`、`FAILED_TO_COMPARE`、`TARGET_DB_NOT_EXIT`、`CAN_NOT_COMPARE`
    - 响应参数`compare_task_status`新增枚举值`RUNNING`、`WAITING_FOR_RUNNING`、`SUCCESSFUL`、`FAILED`、`CANCELLED`、`TIMEOUT_INTERRUPT`、`FULL_DOING`、`INCRE_DOING`
  - 接口`BatchListProgresses`响应参数`task_mode`新增枚举值`FULL_TRANS`、`FULL_INCR_TRANS`、`INCR_TRANS`
  - 接口`BatchListJobDetails`响应参数`status`新增枚举值`CREATING`、`CREATE_FAILED`、`CONFIGURATION`、`STARTJOBING`、`WAITING_FOR_START`、`START_JOB_FAILED`、`PAUSING`、`FULL_TRANSFER_STARTED`、`FULL_TRANSFER_FAILED`、`FULL_TRANSFER_COMPLETE`、`INCRE_TRANSFER_STARTED`、`INCRE_TRANSFER_FAILED`、`RELEASE_RESOURCE_STARTED`、`RELEASE_RESOURCE_FAILED`、`RELEASE_RESOURCE_COMPLETE`、`REBUILD_NODE_STARTED`、`REBUILD_NODE_FAILED`、`CHANGE_JOB_STARTED`、`CHANGE_JOB_FAILED`、`DELETED`、`CHILD_TRANSFER_STARTING`、`CHILD_TRANSFER_STARTED`、`CHILD_TRANSFER_COMPLETE`、`CHILD_TRANSFER_FAILED`、`RELEASE_CHILD_TRANSFER_STARTED`、`RELEASE_CHILD_TRANSFER_COMPLETE`、`NODE_UPGRADE_START`、`NODE_UPGRADE_COMPLETE`、`NODE_UPGRADE_FAILED`
  - 接口`ShowJobList`:
    - 请求参数`status`新增枚举值`PAUSING`、`REBUILD_NODE_STARTED`、`REBUILD_NODE_FAILED`、`DELETED`、`NODE_UPGRADE_START`、`NODE_UPGRADE_COMPLETE`、`NODE_UPGRADE_FAILED`
    - 响应参数`status`新增枚举值`CREATING`、`CREATE_FAILED`、`CONFIGURATION`、`STARTJOBING`、`WAITING_FOR_START`、`START_JOB_FAILED`、`PAUSING`、`FULL_TRANSFER_STARTED`、`FULL_TRANSFER_FAILED`、`FULL_TRANSFER_COMPLETE`、`INCRE_TRANSFER_STARTED`、`INCRE_TRANSFER_FAILED`、`RELEASE_RESOURCE_STARTED`、`RELEASE_RESOURCE_FAILED`、`RELEASE_RESOURCE_COMPLETE`、`REBUILD_NODE_STARTED`、`REBUILD_NODE_FAILED`、`CHANGE_JOB_STARTED`、`CHANGE_JOB_FAILED`、`DELETED`、`CHILD_TRANSFER_STARTING`、`CHILD_TRANSFER_STARTED`、`CHILD_TRANSFER_COMPLETE`、`CHILD_TRANSFER_FAILED`、`RELEASE_CHILD_TRANSFER_STARTED`、`RELEASE_CHILD_TRANSFER_COMPLETE`、`NODE_UPGRADE_START`、`NODE_UPGRADE_COMPLETE`、`NODE_UPGRADE_FAILED`
    - 响应参数`db_use_type`新增枚举值`migration`、`sync`、`cloudDataGuard`
    - 响应参数`task_type`新增枚举值`FULL_TRANS`、`FULL_INCR_TRANS`、`INCR_TRANS`
    - 响应参数`status`类型调整 `string` -> `enum`
  - 接口`BatchListJobStatus`响应参数`status`新增枚举值`CREATING`、`CREATE_FAILED`、`CONFIGURATION`、`STARTJOBING`、`WAITING_FOR_START`、`START_JOB_FAILED`、`PAUSING`、`FULL_TRANSFER_STARTED`、`FULL_TRANSFER_FAILED`、`FULL_TRANSFER_COMPLETE`、`INCRE_TRANSFER_STARTED`、`INCRE_TRANSFER_FAILED`、`RELEASE_RESOURCE_STARTED`、`RELEASE_RESOURCE_FAILED`、`RELEASE_RESOURCE_COMPLETE`、`REBUILD_NODE_STARTED`、`REBUILD_NODE_FAILED`、`CHANGE_JOB_STARTED`、`CHANGE_JOB_FAILED`、`DELETED`、`CHILD_TRANSFER_STARTING`、`CHILD_TRANSFER_STARTED`、`CHILD_TRANSFER_COMPLETE`、`CHILD_TRANSFER_FAILED`、`RELEASE_CHILD_TRANSFER_STARTED`、`RELEASE_CHILD_TRANSFER_COMPLETE`、`NODE_UPGRADE_START`、`NODE_UPGRADE_COMPLETE`、`NODE_UPGRADE_FAILED`
  - 接口`BatchSwitchover`:
    - 响应参数`mongo_ha_mode`新增枚举值`Sharding`、`ReplicaSet`、`ReplicaSingle`
    - 响应参数`cluster_mode`新增枚举值`Single`、`Ha`、`GR`、`Sharding`、`Sharding4.0+`、`ReplicaSet`、`Replica`、`ReplicaSingle`、`Cluster`、`Independent`、`Combined`、`Distributed`、`NoSharding`
    - 响应参数`job_direction`新增枚举值`up`、`down`、`non-dbs`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`NovaCreateServers`请求参数`destination_type`改为非必填

### HuaweiCloud SDK EPS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`MigrateResource`新增请求参数 `region_id`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ShowGaussMySqlProxy`
  - 接口`CreateGaussMySqlInstance`新增请求参数 `lower_case_table_names`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeGeneralText`:
    - 新增请求参数 `character_mode`
    - 新增响应参数 `confidence`、`char_list`
  - 接口`RecognizeThailandIdcard`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.7 2022-11-02

### HuaweiCloud SDK APIG

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateAclStrategyV2`:
    - 请求参数`acl_type`类型调整 `string` -> `enum`
    - 请求参数`entity_type`类型调整 `string` -> `enum`
  - 接口`UpdateAclStrategyV2`:
    - 请求参数`acl_type`类型调整 `string` -> `enum`
    - 请求参数`entity_type`类型调整 `string` -> `enum`
  - 接口`ListAclPolicyBindedToApiV2`响应参数`entity_type`新增枚举值`DOMAIN_ID`
  - 接口`CreateVpcChannelV2`:
    - 新增请求参数 `member_groups`、`microservice_info`、`dict_code`
    - 请求参数`port`、`balance_strategy`、`member_type`改为必填
  - 接口`ListVpcChannelsV2`:
    - 新增请求参数 `dict_code`、`member_host`、`member_port`、`member_group_name`、`member_group_id`
    - 新增响应参数 `microservice_info`、`type`、`dict_code`、`microservice_version`、`microservice_port`
    - 响应参数`port`、`balance_strategy`、`member_type`改为必填
  - 接口`ShowDetailsOfVpcChannelV2`:
    - 新增响应参数 `microservice_info`、`type`、`dict_code`、`microservice_version`、`microservice_port`
    - 响应参数`port`、`balance_strategy`、`member_type`改为必填
  - 接口`UpdateVpcChannelV2`:
    - 新增请求参数 `member_groups`、`microservice_info`、`dict_code`
    - 新增响应参数 `microservice_info`、`type`、`dict_code`、`microservice_version`、`microservice_port`
    - 请求参数`port`、`balance_strategy`、`member_type`改为必填
    - 响应参数`port`、`balance_strategy`、`member_type`改为必填
  - 接口`ListBackendInstancesV2`新增请求参数 `member_group_name`、`member_group_id`、`precise_search`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowUrlTaskInfo`:
    - 响应参数`modify_time`类型调整 `int32` -> `int64`
    - 响应参数`create_time`类型调整 `int32` -> `int64`

### HuaweiCloud SDK ECS

- _新增特性_
  - 支持接口`UpdateServerBlockDevice`、`RegisterServerMonitor`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`UpdateTransactionSplitStatus`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowGaussMySqlProxy`新增响应参数 `transaction_split`
  - 接口`ShowGaussMySqlProxyList`新增响应参数 `transaction_split`

### HuaweiCloud SDK MRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateScalingPolicy`:
    - 新增请求参数 `autoScalingPolicyReqV11`
    - 移除请求参数 `auto_scaling_policy_req_V11`
  - 接口`CreateCluster`:
    - 新增请求参数 `createClusterReqV11`
    - 移除请求参数 `cluster_req`
  - 接口`ListClusters`移除响应参数 `name`、`uri`、`parameters`、`nodes`、`active_master`、`fail_action`、`before_component_start`、`start_time`、`state`
  - 接口`UpdateClusterScaling`:
    - 新增请求参数 `clusterScalingReq`
    - 移除请求参数 `cluster_scaling_req`
  - 接口`ShowClusterDetails`移除响应参数 `name`、`uri`、`parameters`、`nodes`、`active_master`、`fail_action`、`before_component_start`、`start_time`、`state`
  - 接口`CreateClusterTag`:
    - 新增请求参数 `createTagReq`
    - 移除请求参数 `CreateTagRequest`
  - 接口`BatchCreateClusterTags`:
    - 新增请求参数 `batchCreateClusterTagsReq`
    - 移除请求参数 `BatchCreateClusterTagsRequest`
  - 接口`BatchDeleteClusterTags`移除请求参数 `key`、`value`
  - 接口`ListClustersByTags`:
    - 新增请求参数 `listResourceReq`
    - 移除请求参数 `ListResourceRequest`
    - 接口`CreateCluster`移除请求参数 `key`、`value`、`auto_scaling_enable`、`min_capacity`、`max_capacity`、`resources_plans`、`rules`、`exec_scripts`、`name`、`uri`、`parameters`、`nodes`、`active_master`、`fail_action`、`before_component_start`、`action_stages`、`job_type`、`job_name`、`jar_path`、`arguments`、`input`、`output`、`job_log`、`hive_script_path`、`hql`、`shutdown_cluster`、`submit_job_once_cluster_run`、`file_action`
  - 接口`CreateExecuteJob`:
    - 新增请求参数 `jobExecution`
    - 移除请求参数 `job_execution_dto`
    - 移除响应参数 `job_submit_result`
  - 接口`BatchDeleteJobs`:
    - 新增请求参数 `jobBatchDelete`
    - 移除请求参数 `job_batch_delete`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListPostgresqlExtension`、`CreatePostgresqlExtension`、`DeletePostgresqlExtension`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`PushTranscriberJobs`请求参数`property`新增枚举值`sichuan_8k_common`
  - 接口`RunTts`请求参数`property`新增枚举值`chinese_huaxiaolong_common`、`chinese_huaxiaorui_common`

# 3.1.6 2022-10-27

### HuaweiCloud SDK BMS

- _新增特性_
  - 支持接口`DeleteServerNics`、`UpdateBaremetalServerInterfaceAttachments`、`AddServerNics`、`ShowServerRemoteConsole`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowUrlTaskInfo`响应参数`id`类型调整 `int32` -> `int64`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`ListExtensions`、`ShowExtensionDetail`、`ShowExtensionEvaluation`、`ShowExtensionEvaluationStar`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CodeHub

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListMergeRequest`:
    - 新增响应参数 `merge_requests`
    - 移除响应参数 `mergeRequests`
  - 接口`ShowMergeRequest`:
    - 新增响应参数 `approval_merge_request_approvers`、`closed_at`、`created_at`、`devcloud_source_branch`、`is_source_branch_exist`、`merge_request_assignee_list`、`merge_request_diff`、`merge_status`、`source_branch`、`target_branch`、`updated_at`
    - 移除响应参数 `approvalMergeRequestApprovers`、`closedAt`、`createdAt`、`devcloudSourceBranch`、`isSourceBranchExist`、`mergeRequestAssigneeList`、`mergeRequestDiff`、`mergeStatus`、`sourceBranch`、`targetBranch`、`updatedAt`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowInstance`:
    - 响应参数`begin_time`类型调整 `string` -> `int64`
    - 响应参数`end_time`类型调整 `string` -> `int64`
    - 响应参数`current_time`类型调整 `string` -> `int64`
    - 响应参数`next_expand_time`类型调整 `string` -> `int64`
    - 响应参数`expand_effect_time`类型调整 `string` -> `int64`
    - 响应参数`expand_interval_time`类型调整 `string` -> `int64`
  - 接口`ResizeInstance`请求参数`new_capacity`类型调整 `int32` -> `integer`
  - 接口`ListMigrationTask`新增响应参数 `target_instance_address`、`migration_method`、`task_name`、`target_instance_id`、`source_instance_name`、`target_instance_name`、`migrate_type`、`created_at`、`source_instance_id`、`task_id`、`data_source`、`status`
  - 接口`ListRedislog`:
    - 新增响应参数 `backup_id`
    - 移除响应参数 `backupId`
  - 接口`ListBackgroundTask`新增响应参数 `enable_show`

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持以下接口：
    - `AddReadonlyNode`
    - `UpgradeDatabaseVersion`
    - `ShowSecondLevelMonitoringStatus`
    - `SwitchSecondLevelMonitoring`
    - `ChangeOpsWindow`
    - `SetRecyclePolicy`
    - `ExpandReplicasetNode`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListConfigurations`新增响应参数 `node_type`
  - 接口`ListInstances`新增响应参数 `patch_available`
  - 接口`ResizeInstanceVolume`新增请求参数 `node_ids`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateServers`新增请求参数 `X-Client-Token`、`batch_create_in_multi_az`
  - 接口`CreatePostPaidServers`新增请求参数 `X-Client-Token`

### HuaweiCloud SDK ELB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateListener`请求参数`tls_ciphers_policy`新增枚举值`tls-1-1`、`tls-1-2`、`tls-1-2-strict`, 移除枚举值` tls-1-1`、` tls-1-2`、` tls-1-2-strict`
  - 接口`DeleteListener`移除请求参数 `cascade`
  - 接口`DeleteLoadbalancer`移除请求参数 `cascade`
  - 接口`ListApiVersions`:
    - 新增响应参数 `versions`
    - 移除响应参数 `id`、`status`
  - 接口`CreateLoadBalancer`移除请求参数 `global_eip_ids`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持接口`ShowRestorableList`、`ListRestoreTime`、`DeleteBackup`、`RestoreExistingInstance`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK HSS

- _新增特性_
  - 支持以下接口：
    - `ListUsers`
    - `ListUserChangeHistories`
    - `ShowResourceQuotas`
    - `ListQuotasDetail`
    - `SwitchHostsProtectStatus`
    - `BatchCreateTags`
    - `DeleteResourceInstanceTag`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRiskConfigs`:
    - 新增请求参数 `check_name`
    - 移除请求参数 `check_type`
  - 接口`ShowCheckRuleDetail`:
    - 新增请求参数 `check_name`
    - 移除请求参数 `check_type`
  - 接口`ListHostStatus`:
    - 新增请求参数 `server_group`
    - 请求参数`region`改为非必填
  - 接口`ListVulnerabilities`:
    - 新增响应参数 `severity_level`
    - 响应参数`repair_necessity`类型调整 `int32` -> `string`

### HuaweiCloud SDK IEF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ShowEdgeNodeUpgradeDetails`
  - 接口`UpdateNodeByDeviceId`新增请求参数 `ief-instance-id`
  - 接口`ListPods`移除响应参数 `affinity`、`updated_at`
  - 接口`CreateEncryptdatas`移除响应参数 `encrypt_data`
  - 接口`ListEncryptdatas`:
    - 新增响应参数 `encrypt_datas`
    - 移除响应参数 `encrypt_data`
  - 接口`UpdateEncryptdatas`移除响应参数 `encrypt_data`
  - 接口`ListNodeEncryptdatas`:
    - 新增响应参数 `encrypt_datas`
    - 移除响应参数 `encrypt_data`

### HuaweiCloud SDK IMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListTags`请求参数`__imagetype`新增枚举值`market`
  - 接口`GlanceListImages`:
    - 请求参数`__imagetype`新增枚举值`market`
    - 响应参数`__imagetype`新增枚举值`market`
  - 接口`GlanceShowImage`响应参数`__imagetype`新增枚举值`market`
  - 接口`GlanceUpdateImage`响应参数`__imagetype`新增枚举值`market`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateMessage`新增请求参数 `properties`
  - 接口`ListDeviceMessages`新增响应参数 `properties`
  - 接口`ShowDeviceMessage`新增响应参数 `properties`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreatePostPaidInstance`:
    - 新增请求参数 `disk_encrypted_enable`、`disk_encrypted_key`
    - 请求参数`engine_version`新增枚举值`2.7`

### HuaweiCloud SDK Meeting

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunCreateVideoModerationJob`的请求参数`frame_interval`类型变更 `float` -> `integer`
  - 接口`RunQueryAudioModerationJob`的响应参数`start_time`、`end_time`类型变更 `integer` -> `float`
  - 接口`RunQueryVideoModerationJob`
    - 响应参数`time`类型变更 `integer` -> `float`
    - 响应参数`start_time`、`end_time`类型变更 `integer` -> `float`

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `read_only_by_user`
  - 接口`CreateDbUser`新增请求参数 `hosts`、`databases`

### HuaweiCloud SDK SCM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCertificates`响应参数`enterprise_project_id`改为必填
  - 接口`ShowCertificate`新增响应参数 `fingerprint`

### HuaweiCloud SDK SFSTurbo

- _新增特性_
  - 支持接口`ChangeShareName`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.5 2022-09-28

### HuaweiCloud SDK APM

- _新增特性_
  - 支持接口`DeleteEnv`、`DeleteApp`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateAkSk`新增响应参数 `sk`
  - 接口`DeleteAkSk`新增响应参数 `sk`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDomains`新增响应参数 `domain_id`
  - 接口`CreateDomain`:
    - 新增请求参数 `domain_id`
    - 新增响应参数 `domain_id`
  - 接口`ShowDomainDetail`新增响应参数 `domain_id`
  - 接口`DeleteDomain`新增响应参数 `domain_id`
  - 接口`EnableDomain`新增响应参数 `domain_id`
  - 接口`DisableDomain`新增响应参数 `domain_id`
  - 接口`UpdateDomainOrigin`:
    - 新增请求参数 `domain_id`
    - 新增响应参数 `domain_id`
  - 接口`ShowDomainFullConfig`新增响应参数 `origin_range_status`、`user_agent_filter`、`origin_request_url_rewrite`、`error_code_redirect_rules`
  - 接口`UpdateDomainFullConfig`新增请求参数 `origin_range_status`、`user_agent_filter`、`origin_request_url_rewrite`、`error_code_redirect_rules`

### HuaweiCloud SDK CloudRTC

- _新增特性_
  - 支持接口`RemoveUsers`、`RemoveRoom`、`UpdateIndividualStreamJob`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CPTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListVariables`新增响应参数 `variable_mode`、`share_mode`
  - 接口`UpdateTask`:
    - 新增请求参数 `name`、`conditions`、`is_disabled`
    - 新增响应参数 `taskInfo`
    - 移除请求参数 `case_name`
    - 移除响应参数 `taskinfo`
    - 请求参数`check_end_length`类型调整 `string` -> `object`
    - 请求参数`check_end_str`类型调整 `string` -> `object`
    - 请求参数`check_end_type`类型调整 `string` -> `object`
  - 接口`ShowTask`:
    - 新增响应参数 `taskInfo`
    - 移除响应参数 `taskinfo`
  - 接口`ShowReport`新增响应参数 `respTimeRange`、`progressState`、`createBy`、`statusValue`
  - 接口`UpdateCase`新增请求参数 `case_id`、`name`、`case_type`、`increase_setting`、`stages`、`status`、`temp_id`、`sort`
  - 接口`UpdateTemp`:
    - 请求参数`check_end_length`类型调整 `string` -> `object`
    - 请求参数`check_end_str`类型调整 `string` -> `object`
    - 请求参数`check_end_type`类型调整 `string` -> `object`
  - 接口`UpdateTaskRelatedTestCase`:
    - 新增响应参数 `taskInfo`
    - 移除响应参数 `taskinfo`
  - 接口`ShowHistoryRunInfo`新增响应参数 `end_time`、`parallel`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowInstance`:
    - 响应参数`begin_time`类型调整 `string` -> `int64`
    - 响应参数`end_time`类型调整 `string` -> `int64`
    - 响应参数`current_time`类型调整 `string` -> `int64`
    - 响应参数`next_expand_time`类型调整 `string` -> `int64`
    - 响应参数`expand_effect_time`类型调整 `string` -> `int64`
    - 响应参数`expand_interval_time`类型调整 `string` -> `int64`
  - 接口`ResizeInstance`请求参数`new_capacity`类型调整 `int32` -> `integer`
  - 接口`ListMigrationTask`新增响应参数 `target_instance_address`、`migration_method`、`task_name`、`target_instance_id`、`source_instance_name`、`target_instance_name`、`migrate_type`、`created_at`、`source_instance_id`、`task_id`、`data_source`、`status`
  - 接口`ListRedislog`:
    - 新增响应参数 `backup_id`
    - 移除响应参数 `backupId`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListFlavors`请求参数`region`改为必填

### HuaweiCloud SDK IEF

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateEdgeNode`:
    - 新增请求参数 `UpdateEdgeNodeRequestBody`
    - 移除请求参数 `UpdateEdgeNodeBody`
  - 接口`EnableDisableEdgeNodes`:
    - 新增请求参数 `EnableDisableEdgeNodesRequestBody`
    - 移除请求参数 `node`
  - 接口`ListApps`新增响应参数 `host_pid`
  - 接口`UpdateApp`新增响应参数 `host_pid`
  - 接口`ShowAppDetail`新增响应参数 `host_pid`
  - 接口`CreateAppVersions`新增请求参数 `host_pid`
  - 接口`ListAppVersions`新增响应参数 `host_pid`
  - 接口`UpdateAppVersion`:
    - 新增请求参数 `host_pid`
    - 新增响应参数 `host_pid`
  - 接口`ShowAppVersionDetail`新增响应参数 `host_pid`

### HuaweiCloud SDK Live

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowTranscodingsTemplate`响应参数`width`、`height`改为非必填
  - 接口`UpdateTranscodingsTemplate`:
    - 新增请求参数 `trans_type`
    - 请求参数`width`、`height`改为非必填
  - 接口`CreateTranscodingsTemplate`:
    - 新增请求参数 `trans_type`
    - 请求参数`width`、`height`改为非必填

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeHealthCode`新增响应参数 `type`、`idcard_number`、`phone_number`、`province`、`city`、`vaccination_status`、`pcr_test_result`、`pcr_test_organization`、`pcr_test_time`、`pcr_sampling_time`、`reached_city`

### HuaweiCloud SDK VPCEP

- _新增特性_
  - 支持以下接口：
    - `UpdateEndpointServiceName`
    - `UpdateEndpointConnectionsDesc`
    - `BatchAddEndpointServicePermissions`
    - `BatchRemoveEndpointServicePermissions`
    - `UpdateEndpointServicePermissionDesc`
    - `UpdateEndpointPolicy`
    - `DeleteEndpointPolicy`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateEndpointService`:
    - 新增请求参数 `description`
    - 新增响应参数 `description`
  - 接口`ListEndpointService`:
    - 新增请求参数 `public_border_group`
    - 新增响应参数 `description`、`public_border_group`
    - 响应参数`service_type`类型调整 `string` -> `enum`
    - 响应参数`server_type`类型调整 `enum` -> `string`
  - 接口`UpdateEndpointService`:
    - 新增请求参数 `description`
    - 新增响应参数 `description`
  - 接口`ListServiceDetails`:
    - 新增响应参数 `description`
    - 响应参数`service_type`类型调整 `string` -> `enum`
  - 接口`ListServiceConnections`移除响应参数 `id`、`marker_id`、`created_at`、`updated_at`、`domain_id`、`status`
  - 接口`AcceptOrRejectEndpoint`新增响应参数 `description`
  - 接口`ListServicePermissionsDetails`移除响应参数 `id`、`permission`、`created_at`
  - 接口`CreateEndpoint`:
    - 新增请求参数 `description`
    - 新增响应参数 `specification_name`、`description`、`policy_statement`、`enable_status`
  - 接口`ListEndpoints`:
    - 新增请求参数 `public_border_group`
    - 新增响应参数 `description`、`policy_statement`、`endpoint_pool_id`、`public_border_group`
  - 接口`ListEndpointInfoDetails`新增响应参数 `description`、`policy_statement`
  - 接口`ListVersionDetails`移除响应参数 `status`、`id`、`updated`、`version`、`min_version`、`links`
  - 接口`ListSpecifiedVersionDetails`移除响应参数 `status`、`id`、`updated`、`version`、`min_version`、`links`
  - 接口`ListResourceInstances`:
    - 新增请求参数 `sys_tags`、`without_any_tag`
    - 移除请求参数 `key`、`value`、`key`、`value`、`key`、`value`、`key`、`value`

# 3.1.4 2022-09-26

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDependency`新增响应参数 `version`、`last_modified`
  - 接口`ListDependencies`新增响应参数 `version`、`last_modified`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `disk_encrypted_key`、`public_management_connect_address`、`subnet_cidr`、`subnet_name`、`enable_acl`
  - 接口`ShowInstance`新增响应参数 `disk_encrypted_key`、`public_management_connect_address`、`subnet_cidr`、`subnet_name`、`enable_acl`
  - 接口`ResizeInstance`新增请求参数 `oper_type`、`new_broker_num`、`new_product_id`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 修复接口`CheckImageModeration`响应参数类型错误的问题
- _特性变更_
  - 无

# 3.1.3 2022-09-22

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateApiV2`新增请求参数 `network_type`、`alias_urn`、`network_type`、`alias_urn`
  - 接口`ShowDetailsOfApiV2`新增响应参数 `network_type`、`alias_urn`、`network_type`、`alias_urn`
  - 接口`UpdateApiV2`:
    - 新增请求参数 `network_type`、`alias_urn`、`network_type`、`alias_urn`
    - 新增响应参数 `network_type`、`alias_urn`、`network_type`、`alias_urn`
  - 接口`ListApiVersionDetailV2`新增响应参数 `network_type`、`alias_urn`、`network_type`、`alias_urn`
  - 接口`UpdateDomainV2`移除响应参数 `url_domain`、`id`、`status`、`min_ssl_version`
  - 接口`ListApisUnbindedToAclPolicyV2`新增响应参数 `req_uri`、`auth_type`
  - 接口`ListCustomAuthorizersV2`新增响应参数 `authorizer_version`、`authorizer_alias_uri`
  - 接口`CreateCustomAuthorizerV2`新增请求参数 `authorizer_version`、`authorizer_alias_uri`
  - 接口`ShowDetailsOfCustomAuthorizersV2`新增响应参数 `authorizer_version`、`authorizer_alias_uri`
  - 接口`UpdateCustomAuthorizerV2`:
    - 新增请求参数 `authorizer_version`、`authorizer_alias_uri`
    - 新增响应参数 `authorizer_version`、`authorizer_alias_uri`
  - 接口`ExportApiDefinitionsV2`请求参数`env_id`改为必填
  - 接口`ListTagsV2`:
    - 新增响应参数 `tags`
    - 移除响应参数 `responses`
  - 接口`CreateFeatureV2`移除响应参数 `id`、`name`、`enable`、`config`、`instance_id`、`update_time`
  - 接口`ShowDetailsOfInstanceV2`新增响应参数 `ingress_ip_v6`
  - 接口`UpdateInstanceV2`新增响应参数 `ingress_ip_v6`

### HuaweiCloud SDK CES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateEvents`新增请求参数 `event_type`
  - 接口`ListEventDetail`新增响应参数 `event_type`

### HuaweiCloud SDK CloudPipeline

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ShowAgentStatus`、`RegisterAgent`

### HuaweiCloud SDK CodeCheck

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CheckRecord`新增响应参数 `check_end_time`
  - 接口`ShowTaskDefects`新增响应参数 `events`
  - 接口`CheckParameters`移除响应参数 `name`、`cfg_key`、`default_value`、`option_value`、`is_required`、`description`、`type`、`status`
  - 接口`CheckRulesetParameters`新增响应参数 `value`

### HuaweiCloud SDK CPTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListProjectSets`:
    - 新增响应参数 `source`
    - 移除响应参数 `status`
  - 接口`ShowTaskSet`新增响应参数 `parallel`

### HuaweiCloud SDK CTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListTrackers`新增响应参数 `group_id`、`stream_id`

### HuaweiCloud SDK DDM

- _新增特性_
  - 支持接口`ResetAdministrator`、`ValidateWeakPassword`、`ResizeFlavor`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`新增请求参数 `admin_user_name`、`admin_user_password`
  - 接口`ShowInstance`新增响应参数 `admin_user_name`
  - 接口`ListSlowLog`新增响应参数 `host`

### HuaweiCloud SDK DevStar

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowApplicationV3`响应参数`deploy_type`新增枚举值`none`
  - 接口`ShowApplicationDependentResources`新增响应参数 `subscribe_guide`
  - 接口`ListApplicationsV6`响应参数`deploy_type`新增枚举值`none`
  - 接口`ShowApplicationReleaseRepositories`新增响应参数 `category_name`
  - 接口`ShowTemplateV3`新增响应参数 `subscribe_guide`
  - 接口`ListTemplatesV2`新增响应参数 `subscribe_guide`
  - 接口`ListTemplates`新增响应参数 `subscribe_guide`

### HuaweiCloud SDK EG

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListEventSources` 移除响应参数 `id`、`name`、`label`、`description`、`provider_type`、`event_types`、`created_time`、`updated_time`、`channel_id`、`channel_name`
  - 接口`CreateEventSource`:
    - 新增请求参数 `type`、`detail`
    - 新增响应参数 `event_types`、`type`、`detail`、`status`
  - 接口`ShowDetailOfEventSource` 新增响应参数 `event_types`、`type`、`detail`、`status`
  - 接口`UpdateEventSource`:
    - 新增请求参数 `detail`
    - 新增响应参数 `event_types`、`type`、`detail`、`status`
  - 接口`ListEventTarget`移除响应参数 `name`、`label`、`metadata`
  - 接口`ListSubscriptions`新增响应参数 `connection_id`
  - 接口`CreateSubscription`:
    - 新增请求参数 `connection_id`
    - 新增响应参数 `connection_id`
  - 接口`ShowDetailOfSubscription` 新增响应参数 `connection_id`
  - 接口`UpdateSubscription`:
    - 新增请求参数 `connection_id`
    - 新增响应参数 `connection_id`
  - 接口`CreateSubscriptionTarget`:
    - 新增请求参数 `connection_id`
    - 新增响应参数 `connection_id`
  - 接口`ShowDetailOfSubscriptionTarget` 新增响应参数 `connection_id`
  - 接口`UpdateSubscriptionTarget`:
    - 新增请求参数 `connection_id`
    - 新增响应参数 `connection_id`
  - 接口`ListQuotas`:
    - 请求参数`type`新增枚举值`CONNECTION`、`PRIVATE_ENDPOINT`、`SOURCE_RABBITMQ`
    - 响应参数`type`新增枚举值`CONNECTION`、`PRIVATE_ENDPOINT`、`SOURCE_RABBITMQ`
    - 响应参数`max`类型调整 `string` -> `int32`
    - 响应参数`min`类型调整 `string` -> `int32`
    - 响应参数`quota`类型调整 `string` -> `int32`
    - 响应参数`used`类型调整 `string` -> `int32`

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreatePublicip`新增请求参数 `port_id`
  - 接口`CreatePrePaidPublicip`新增请求参数 `port_id`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ListGaussMySqlInstanceDetailInfo`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDeviceMessages`新增响应参数 `error_info`
  - 接口`ShowDeviceMessage`新增响应参数 `error_info`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 支持接口`CheckImageModeration`
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunCreateAudioModerationJob`请求参数`url`、`categories`改为必填

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeIdCard`:
    - 新增请求参数 `detect_copy`
    - 新增响应参数 `detect_copy_result`

### HuaweiCloud SDK OMS

- _新增特性_
  - 支持以下接口：
    - `ListTaskGroup`
    - `CreateTaskGroup`
    - `ShowTaskGroup`
    - `DeleteTaskGroup`
    - `StopTaskGroup`
    - `StartTaskGroup`
    - `RetryTaskGroup`
    - `UpdateTaskGroup`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListTasks`新增响应参数 `enable_metadata_migration`、`object_overwrite_mode`、`consistency_check`、`enable_requester_pays`
  - 接口`CreateTask`:
    - 新增请求参数 `enable_metadata_migration`、`object_overwrite_mode`、`consistency_check`、`enable_requester_pays`
    - 新增响应参数 `id`、`task_name`
  - 接口`ShowTask`:
    - 新增响应参数 `enable_metadata_migration`、`object_overwrite_mode`、`consistency_check`、`enable_requester_pays`
    - 请求参数`task_id`类型调整 `int64` -> `string`
  - 接口`DeleteTask`请求参数`task_id`类型调整 `int64` -> `string`
  - 接口`StopTask`请求参数`task_id`类型调整 `int64` -> `string`
  - 接口`StartTask`请求参数`task_id`类型调整 `int64` -> `string`
  - 接口`UpdateBandwidthPolicy`请求参数`task_id`类型调整 `int64` -> `string`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持接口`DownloadImageFile`、`ListScrumProjectStatuses`、`UploadAttachments`
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
  - 接口`BatchRestartOrDeleteInstances`请求参数`all_failure`新增枚举值`rabbitmq`, 移除枚举值`true`、`false`

### HuaweiCloud SDK SMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListTemplates`移除响应参数 `disks`
  - 接口`ShowTemplate`移除响应参数 `disks`
  - 接口`UpdateMigproject`移除请求参数 `disks`
  - 接口`ShowMigproject`移除响应参数 `disks`

### HuaweiCloud SDK VOD

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`PublishAssets`新增响应参数 `pack_type`、`pack_type`
  - 接口`UnpublishAssets`新增响应参数 `pack_type`、`pack_type`
  - 接口`ShowAssetMeta`新增响应参数 `pack_type`、`pack_type`
  - 接口`ShowAssetDetail`新增响应参数 `pack_type`、`pack_type`
  - 接口`ShowTakeOverTaskDetails`新增响应参数 `pack_type`、`pack_type`
  - 接口`ShowTakeOverAssetDetails`新增响应参数 `pack_type`、`pack_type`

### HuaweiCloud SDK WAF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DeleteIgnoreRule`新增响应参数 `rule`

# 3.1.2 2022-09-15

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerselfResourceRecordDetails`新增响应参数 `root_resource_id`、`parent_resource_id`、`trade_id`、`product_spec_desc`

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持接口`ShowTags`、`CreateTags`、`BatchDeleteTags`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowUrlTaskInfo`:
    - 新增响应参数 `result`
    - 移除响应参数 `results`
  - 接口`ShowDomainFullConfig`新增响应参数 `error_code_cache`
  - 接口`UpdateDomainFullConfig`新增请求参数 `error_code_cache`

### HuaweiCloud SDK CodeHub

- _新增特性_
  - 支持以下接口：
    - `ListFilesByQuery`
    - `ListBranchesByRepositoryId`
    - `CreateNewBranch`
    - `AssociateIssues`
    - `ListMergeRequest`
    - `ShowMergeRequest`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSubfiles`:
    - 新增响应参数 `error`、`result`、`status`
    - 移除响应参数 `trees`、`total`
  - 接口`ShowStatisticalData`:
    - 新增响应参数 `error`、`result`、`status`
    - 移除响应参数 `repoName`、`commitCount`、`repoSize`、`lastCommitTime`、`codeLines`、`branchCount`、`archiveUrl`
  - 接口`CreateCommit`请求参数`force`类型调整 `string` -> `boolean`
  - 接口`AddProtectBranchV2`:
    - 请求参数`push_access_level`类型调整 `int32` -> `enum`
    - 请求参数`merge_access_level`类型调整 `int32` -> `enum`

### HuaweiCloud SDK CSE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UploadKie`新增响应参数 `create_revision`、`update_revision`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateCloseKibana`新增请求参数 `CloseKibanaPublicReq`
  - 接口`CreateCluster`新增请求参数 `payInfo`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowInstance`新增响应参数 `enterprise_project_name`、`update_at`、`product_type`、`storage_type`、`launched_at`、`cache_mode`、`support_slow_log_flag`、`db_number`、`replica_count`、`sharding_count`、`bandwidth_info`
  - 接口`ListRedislog`新增响应参数 `backupId`
  - 接口`ShowIpWhitelist`新增响应参数 `instance_id`
  - 接口`UpdateIpWhitelist`新增请求参数 `instance_id`
  - 接口`ListBackgroundTask`新增响应参数 `updated_at`、`created_at`、`status`

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持接口`CreateDownloadJob`、`UpdateTableOwner`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListGlobalValues`:
    - 新增响应参数 `is_sensitive`
    - 响应参数`id`类型调整 `int32` -> `string`
  - 接口`CreateGlobleValue`:
    - 新增请求参数 `CreateGlobalValueReq`
    - 移除请求参数 `createGlobaleValueReq`
  - 接口`UpdateGlobalValue`移除请求参数 `var_name`
  - 接口`CreateIefSystemEvents`移除请求参数 `event_type`、`operation`、`timestamp`、`topic`、`name`、`attributes`
  - 接口`ListJobs`:
    - 新增请求参数 `owner`、`tags`
    - 新增响应参数 `message`、`end_time`
    - 移除响应参数 `key`、`value`
  - 接口`ImportData`请求参数`partition_spec`类型调整 `object` -> `string`
  - 接口`RunJob`移除请求参数 `key`、`value`
  - 接口`ShowDetailInfo`移除响应参数 `key`、`value`
  - 接口`ShowJobStatus`移除响应参数 `key`、`value`
  - 接口`CreateDatabase`移除请求参数 `key`、`value`
  - 接口`ListAllTables`响应参数`create_time`类型调整 `int64` -> `int32`
  - 接口`ShowObjectUser`移除请求参数 `limit`、`offset`
  - 接口`CreateFlinkJar`移除请求参数 `key`、`value`
  - 接口`UpdateFlinkJar`新增请求参数 `job_type`
  - 接口`ListFlinkJobs`:
    - 新增响应参数 `user_name`
    - 移除响应参数 `username`
  - 接口`CreateFlinkSql`移除请求参数 `key`、`value`
  - 接口`CreateFlinkTemplate`:
    - 移除请求参数 `key`、`value`
    - 请求参数`job_type`类型调整 `string` -> `enum`
  - 接口`ListResources`响应参数`update_time`类型调整 `int32` -> `int64`
  - 接口`UploadResources`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`、`key`、`value`
    - 请求参数`group`改为必填
  - 接口`UploadFiles`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`
    - 请求参数`group`改为必填
  - 接口`UploadJars`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`
    - 请求参数`group`改为必填
  - 接口`UploadPythonFiles`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`
    - 请求参数`group`改为必填
  - 接口`ListBatches`:
    - 新增请求参数 `end`、`order`、`start`
    - 新增响应参数 `duration`
  - 接口`CreateBatchJob`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`
    - 请求参数`queue`改为非必填
  - 接口`ListElasticResourcePools`:
    - 响应参数`update_time`类型调整 `int32` -> `int64`
    - 响应参数`create_time`类型调整 `int32` -> `int64`
  - 接口`ListEnhancedConnections`新增请求参数 `tags`
  - 接口`CreateEnhancedConnection`移除请求参数 `key`、`value`
  - 接口`ListDatasourceConnections`:
    - 新增请求参数 `tags`
    - 移除响应参数 `is_success`、`message`、`connection_id`、`destination`、`state`、`process`、`name`、`connection_url`、`cluster_name`、`service`、`create_time`
  - 接口`CreateDatasourceConnection`移除请求参数 `key`、`value`
  - 接口`ShowDatasourceConnection`:
    - 新增响应参数 `queueList`
    - 移除响应参数 `available_queue_info`
  - 接口`ListQueues`:
    - 新增响应参数 `resource_type`
    - 移除请求参数 `page-size`、`current-page`、`order`
    - 移除响应参数 `queue_resource_type`、`cu_spec`、`cu_scale_out_limit`、`cu_scale_in_limit`、`elastic_resource_pool_name`
    - 响应参数`queue_id`类型调整 `string` -> `int64`
    - 响应参数`labels`类型调整 `array` -> `string`
  - 接口`CreateQueue`移除请求参数 `key`、`value`
  - 接口`ShowQueueDetail`:
    - 新增响应参数 `queue_name`、`cu_count`、`charging_mode`
    - 移除请求参数 `queue_type`
    - 移除响应参数 `queueName`、`cuCount`、`chargingMode`、`queueType`、`resource_type`、`cu_spec`、`cu_scale_out_limit`、`cu_scale_in_limit`、`elastic_resource_pool_name`
    - 响应参数`queue_id`类型调整 `string` -> `int64`
  - 接口`RunQueueAction`:
    - 新增请求参数 `RunQueueActionReq`
    - 移除请求参数 `body`
  - 接口`CreateQueuePlan`请求参数`repeat_day`改为非必填
  - 接口`ChangeQueuePlan`请求参数`repeat_day`改为非必填

### HuaweiCloud SDK EVS

- _新增特性_
  - 支持以下接口：
    - `ShowVersion`
    - `ListVersions`
    - `CinderShowVolumeTransfer`
    - `CinderDeleteVolumeTransfer`
    - `CinderListVolumeTransfers`
    - `CinderCreateVolumeTransfer`
    - `CinderAcceptVolumeTransfer`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IEF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListApps`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`UpdateApp`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`ShowAppDetail`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`ListAppVersions`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`CreateAppVersions`新增请求参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`UpdateAppVersion`:
    - 新增请求参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
    - 新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`ShowAppVersionDetail`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateLogStream`新增请求参数 `ttl_in_days`
  - 接口`ListStructuredLogsWithTimeRange`新增请求参数 `whether_to_rows`
  - 接口`UpdateStructTemplate`请求参数`isAnalysis`改为非必填
  - 接口`CreateStructTemplate`请求参数`isAnalysis`改为非必填

### HuaweiCloud SDK Moderation

- _新增特性_
  - 支持接口`RunCreateVideoModerationJob`、`RunQueryVideoModerationJob`
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunCreateAudioModerationJob`请求参数`url`改为非必填

# 3.1.1 2022-09-08

### HuaweiCloud SDK IAM

- _新增特性_
  - 支持自定义认证凭据 `IamCredentials`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerselfResourceRecordDetails`新增响应参数 `root_resource_id`、`parent_resource_id`、`trade_id`、`product_spec_desc`

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持接口`ShowTags`、`CreateTags`、`BatchDeleteTags`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowUrlTaskInfo`:
    - 新增响应参数 `result`
    - 移除响应参数 `results`
  - 接口`ShowDomainFullConfig`新增响应参数 `error_code_cache`
  - 接口`UpdateDomainFullConfig`新增请求参数 `error_code_cache`

### HuaweiCloud SDK CodeHub

- _新增特性_
  - 支持以下接口：
    - `ListFilesByQuery`
    - `ListBranchesByRepositoryId`
    - `CreateNewBranch`
    - `AssociateIssues`
    - `ListMergeRequest`
    - `ShowMergeRequest`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSubfiles`:
    - 新增响应参数 `error`、`result`、`status`
    - 移除响应参数 `trees`、`total`
  - 接口`ShowStatisticalData`:
    - 新增响应参数 `error`、`result`、`status`
    - 移除响应参数 `repoName`、`commitCount`、`repoSize`、`lastCommitTime`、`codeLines`、`branchCount`、`archiveUrl`
  - 接口`CreateCommit`请求参数`force`类型调整 `string` -> `boolean`
  - 接口`AddProtectBranchV2`:
    - 请求参数`push_access_level`类型调整 `int32` -> `enum`
    - 请求参数`merge_access_level`类型调整 `int32` -> `enum`

### HuaweiCloud SDK CSE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UploadKie`新增响应参数 `create_revision`、`update_revision`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateCloseKibana`新增请求参数 `CloseKibanaPublicReq`
  - 接口`CreateCluster`新增请求参数 `payInfo`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowInstance`新增响应参数 `enterprise_project_name`、`update_at`、`product_type`、`storage_type`、`launched_at`、`cache_mode`、`support_slow_log_flag`、`db_number`、`replica_count`、`sharding_count`、`bandwidth_info`
  - 接口`ListRedislog`新增响应参数 `backupId`
  - 接口`ShowIpWhitelist`新增响应参数 `instance_id`
  - 接口`UpdateIpWhitelist`新增请求参数 `instance_id`
  - 接口`ListBackgroundTask`新增响应参数 `updated_at`、`created_at`、`status`

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持接口`CreateDownloadJob`、`UpdateTableOwner`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListGlobalValues`:
    - 新增响应参数 `is_sensitive`
    - 响应参数`id`类型调整 `int32` -> `string`
  - 接口`CreateGlobleValue`:
    - 新增请求参数 `CreateGlobalValueReq`
    - 移除请求参数 `createGlobaleValueReq`
  - 接口`UpdateGlobalValue`移除请求参数 `var_name`
  - 接口`CreateIefSystemEvents`移除请求参数 `event_type`、`operation`、`timestamp`、`topic`、`name`、`attributes`
  - 接口`ListJobs`:
    - 新增请求参数 `owner`、`tags`
    - 新增响应参数 `message`、`end_time`
    - 移除响应参数 `key`、`value`
  - 接口`ImportData`请求参数`partition_spec`类型调整 `object` -> `string`
  - 接口`RunJob`移除请求参数 `key`、`value`
  - 接口`ShowDetailInfo`移除响应参数 `key`、`value`
  - 接口`ShowJobStatus`移除响应参数 `key`、`value`
  - 接口`CreateDatabase`移除请求参数 `key`、`value`
  - 接口`ListAllTables`响应参数`create_time`类型调整 `int64` -> `int32`
  - 接口`ShowObjectUser`移除请求参数 `limit`、`offset`
  - 接口`CreateFlinkJar`移除请求参数 `key`、`value`
  - 接口`UpdateFlinkJar`新增请求参数 `job_type`
  - 接口`ListFlinkJobs`:
    - 新增响应参数 `user_name`
    - 移除响应参数 `username`
  - 接口`CreateFlinkSql`移除请求参数 `key`、`value`
  - 接口`CreateFlinkTemplate`:
    - 移除请求参数 `key`、`value`
    - 请求参数`job_type`类型调整 `string` -> `enum`
  - 接口`ListResources`响应参数`update_time`类型调整 `int32` -> `int64`
  - 接口`UploadResources`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`、`key`、`value`
    - 请求参数`group`改为必填
  - 接口`UploadFiles`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`
    - 请求参数`group`改为必填
  - 接口`UploadJars`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`
    - 请求参数`group`改为必填
  - 接口`UploadPythonFiles`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`
    - 请求参数`group`改为必填
  - 接口`ListBatches`:
    - 新增请求参数 `end`、`order`、`start`
    - 新增响应参数 `duration`
  - 接口`CreateBatchJob`:
    - 新增请求参数 `USER-ID`
    - 移除请求参数 `USER_ID`
    - 请求参数`queue`改为非必填
  - 接口`ListElasticResourcePools`:
    - 响应参数`update_time`类型调整 `int32` -> `int64`
    - 响应参数`create_time`类型调整 `int32` -> `int64`
  - 接口`ListEnhancedConnections`新增请求参数 `tags`
  - 接口`CreateEnhancedConnection`移除请求参数 `key`、`value`
  - 接口`ListDatasourceConnections`:
    - 新增请求参数 `tags`
    - 移除响应参数 `is_success`、`message`、`connection_id`、`destination`、`state`、`process`、`name`、`connection_url`、`cluster_name`、`service`、`create_time`
  - 接口`CreateDatasourceConnection`移除请求参数 `key`、`value`
  - 接口`ShowDatasourceConnection`:
    - 新增响应参数 `queueList`
    - 移除响应参数 `available_queue_info`
  - 接口`ListQueues`:
    - 新增响应参数 `resource_type`
    - 移除请求参数 `page-size`、`current-page`、`order`
    - 移除响应参数 `queue_resource_type`、`cu_spec`、`cu_scale_out_limit`、`cu_scale_in_limit`、`elastic_resource_pool_name`
    - 响应参数`queue_id`类型调整 `string` -> `int64`
    - 响应参数`labels`类型调整 `array` -> `string`
  - 接口`CreateQueue`移除请求参数 `key`、`value`
  - 接口`ShowQueueDetail`:
    - 新增响应参数 `queue_name`、`cu_count`、`charging_mode`
    - 移除请求参数 `queue_type`
    - 移除响应参数 `queueName`、`cuCount`、`chargingMode`、`queueType`、`resource_type`、`cu_spec`、`cu_scale_out_limit`、`cu_scale_in_limit`、`elastic_resource_pool_name`
    - 响应参数`queue_id`类型调整 `string` -> `int64`
  - 接口`RunQueueAction`:
    - 新增请求参数 `RunQueueActionReq`
    - 移除请求参数 `body`
  - 接口`CreateQueuePlan`请求参数`repeat_day`改为非必填
  - 接口`ChangeQueuePlan`请求参数`repeat_day`改为非必填

### HuaweiCloud SDK EVS

- _新增特性_
  - 支持以下接口：
    - `ShowVersion`
    - `ListVersions`
    - `CinderShowVolumeTransfer`
    - `CinderDeleteVolumeTransfer`
    - `CinderListVolumeTransfers`
    - `CinderCreateVolumeTransfer`
    - `CinderAcceptVolumeTransfer`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IEF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListApps`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`UpdateApp`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`ShowAppDetail`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`ListAppVersions`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`CreateAppVersions`新增请求参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`UpdateAppVersion`:
    - 新增请求参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
    - 新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`
  - 接口`ShowAppVersionDetail`新增响应参数 `cpu`、`memory`、`gpu`、`npu`、`cpu`、`memory`、`gpu`、`npu`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateLogStream`新增请求参数 `ttl_in_days`
  - 接口`ListStructuredLogsWithTimeRange`新增请求参数 `whether_to_rows`
  - 接口`UpdateStructTemplate`请求参数`isAnalysis`改为非必填
  - 接口`CreateStructTemplate`请求参数`isAnalysis`改为非必填

### HuaweiCloud SDK Moderation

- _新增特性_
  - 支持接口`RunCreateVideoModerationJob`、`RunQueryVideoModerationJob`
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunCreateAudioModerationJob`请求参数`url`改为非必填

# 3.0.108 2022-09-01

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerOrders`新增请求参数 `indirect_partner_id`
  - 接口`ShowCustomerOrderDetails`新增请求参数 `indirect_partner_id`
  - 接口`ListCustomerOnDemandResources`新增请求参数 `indirect_partner_id`

### HuaweiCloud SDK CC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCloudConnections`响应参数`used_scene`移除枚举值`er`
  - 接口`CreateCloudConnection`移除请求参数 `used_scene`
  - 接口`ShowCloudConnection`响应参数`used_scene`移除枚举值`er`
  - 接口`UpdateCloudConnection`响应参数`used_scene`移除枚举值`er`
  - 接口`ListNetworkInstances`响应参数`type`移除枚举值`er`
  - 接口`CreateNetworkInstance`请求参数`type`移除枚举值`er`
  - 接口`ShowNetworkInstance`响应参数`type`移除枚举值`er`
  - 接口`UpdateNetworkInstance`响应参数`type`移除枚举值`er`

### HuaweiCloud SDK CDM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowJobs`响应参数`id`、`type`改为非必填
  - 接口`UpdateJob`请求参数`id`、`type`改为非必填
  - 接口`CreateAndStartRandomClusterJob`请求参数`id`、`type`改为非必填
  - 接口`CreateJob`请求参数`id`、`type`改为非必填

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCluster`新增响应参数 `ordeId`
  - 接口`ShowClusterDetail`:
    - 新增响应参数 `vpcepIp`、`elbWhiteListResp`
    - 移除响应参数 `elbWhiteList`、`action`
  - 接口`UpdateUnbindPublic`移除请求参数 `isAutoPay`
  - 接口`ListYmlsJob`:
    - 新增响应参数 `configList`
    - 移除响应参数 `configurations`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDependency`移除响应参数 `version`、`last_modified`
  - 接口`ListDependencies`移除响应参数 `version`、`last_modified`

### HuaweiCloud SDK IAM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateDomainProtectPolicy`:
    - 新增请求参数 `allow_user`、`mobile`、`admin_check`、`email`、`scene`
    - 移除响应参数 `operation_protection`
  - 接口`ShowDomainProtectPolicy`移除响应参数 `operation_protection`
  - 接口`UpdateDomainPasswordPolicy`请求参数`maximum_consecutive_identical_chars`、`minimum_password_age`、`minimum_password_length`、`number_of_recent_passwords_disallowed`、`password_not_username_or_invert`、`password_validity_period`、`password_char_combination`改为非必填
  - 接口`UpdateDomainLoginPolicy`请求参数`account_validity_period`、`custom_info_for_login`、`lockout_duration`、`login_failed_times`、`period_with_login_failures`、`session_timeout`、`show_recent_login_info`改为非必填
  - 接口`ShowDomainQuota`请求参数`type`新增枚举值`mapping`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`UpdateDbUserComment`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDbUser`新增请求参数 `comment`

### HuaweiCloud SDK WAF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListStatistics`:
    - 请求参数`hosts`类型调整 `array` -> `string`
    - 请求参数`instances`类型调整 `array` -> `string`
  - 接口`ListQpsTimeline`:
    - 请求参数`hosts`类型调整 `array` -> `string`
    - 请求参数`instances`类型调整 `array` -> `string`
  - 接口`ListBandwidthTimeline`请求参数`instances`类型调整 `array` -> `string`
  - 接口`ListTopAbnormal`:
    - 请求参数`hosts`类型调整 `array` -> `string`
    - 请求参数`instances`类型调整 `array` -> `string`
  - 接口`ListOverviewsClassification`:
    - 请求参数`hosts`类型调整 `array` -> `string`
    - 请求参数`instances`类型调整 `array` -> `string`

# 3.0.107 2022-08-29

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreatePostPaidServers`新增请求参数 `batch_create_in_multi_az`

### HuaweiCloud SDK IMS

- _新增特性_
  - 支持接口`ShowJobProgress`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`SetReadOnlySwitch`
- _解决问题_
  - 无
- _特性变更_
  - 接口`StartFailover`新增请求参数 `FailoverRequestBody`

# 3.0.106 2022-08-25

### HuaweiCloud SDK CDM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateJob`:
    - 新增请求参数 `rows_written`、`rows_read`、`files_written`、`extended-configs`、`value`、`extended-configs`、`value`、`extended-configs`、`value`
    - 移除请求参数 `files_writte`、`values`、`values`、`values`
  - 接口`ShowJobs`:
    - 新增响应参数 `rows_written`、`rows_read`、`files_written`、`extended-configs`、`value`、`extended-configs`、`value`、`extended-configs`、`value`
    - 移除响应参数 `files_writte`、`values`、`values`、`values`
  - 接口`CreateAndStartRandomClusterJob`:
    - 新增请求参数 `rows_written`、`rows_read`、`files_written`、`extended-configs`、`value`、`extended-configs`、`value`、`extended-configs`、`value`
    - 移除请求参数 `files_writte`、`values`、`values`、`values`
  - 接口`CreateJob`:
    - 新增请求参数 `rows_written`、`rows_read`、`files_written`、`extended-configs`、`value`、`extended-configs`、`value`、`extended-configs`、`value`
    - 移除请求参数 `files_writte`、`values`、`values`、`values`

### HuaweiCloud SDK DLI

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateFlinkSql`新增请求参数 `flink_version`
  - 接口`UpdateFlinkSql`新增请求参数 `flink_version`
  - 接口`CreateElasticResourcePool`请求参数`key`、`value`改为必填
  - 接口`ListElasticResourcePools`新增响应参数 `elastic_resource_pool_name`、`manager`、`label`
  - 接口`ListQueues`:
    - 新增请求参数 `page-size`、`current-page`、`order`
    - 新增响应参数 `queue_id`、`elastic_resource_pool_name`

### HuaweiCloud SDK ELB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `ListMasterSlavePools`
    - `CreateMasterSlavePool`
    - `ShowMasterSlavePool`
    - `DeleteMasterSlavePool`
  - 接口`ListLoadBalancers`新增响应参数 `waf_failure_action`
  - 接口`CreateLoadBalancer`新增请求参数 `waf_failure_action`
  - 接口`ShowLoadBalancer`新增响应参数 `waf_failure_action`
  - 接口`UpdateLoadBalancer`:
    - 新增请求参数 `waf_failure_action`
    - 新增响应参数 `waf_failure_action`
    - 移除请求参数 `cloud_service_console_url`
  - 接口`ListCertificates`新增响应参数 `enc_certificate`、`enc_private_key`
  - 接口`CreateCertificate`新增请求参数 `enc_certificate`、`enc_private_key`
  - 接口`ShowCertificate`新增响应参数 `enc_certificate`、`enc_private_key`
  - 接口`UpdateCertificate`:
    - 新增请求参数 `enc_certificate`、`enc_private_key`
    - 新增响应参数 `enc_certificate`、`enc_private_key`
  - 接口`ListListeners`新增响应参数 `sni_match_algo`
  - 接口`CreateListener`新增请求参数 `sni_match_algo`
  - 接口`ShowListener`新增响应参数 `sni_match_algo`
  - 接口`UpdateListener`:
    - 新增请求参数 `sni_match_algo`
    - 新增响应参数 `sni_match_algo`
  - 接口`ListMembers`新增请求参数 `instance_id`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeWebImage`:
    - 新增请求参数 `detect_font`
    - 新增响应参数 `font_list`、`font_scores`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`SetDatabaseUserPrivilege`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK VOD

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CheckMd5Duplication`请求参数`size`类型调整 `int32` -> `int64`

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持接口`ListRequestTimeline`
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateGeoipRule`新增响应参数 `description`

# 3.0.105 2022-08-22

### HuaweiCloud SDK Live

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateRecordIndex`请求参数`object`类型调整 `uri` -> `string`

# 3.0.104 2022-08-18

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 支持接口`ListIndirectPartners`、`ListCosts`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSubCustomers`新增请求参数 `indirect_partner_id`
  - 接口`CreateSubCustomer`新增请求参数 `indirect_partner_id`
  - 接口`ShowSubCustomerBudget`新增请求参数 `indirect_partner_id`
  - 接口`UpdateSubCustomerBudget`新增请求参数 `indirect_partner_id`
  - 接口`FreezeSubCustomers`新增请求参数 `indirect_partner_id`
  - 接口`UnfreezeSubCustomers`新增请求参数 `indirect_partner_id`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListProjectTemplates`新增响应参数 `arch`

### HuaweiCloud SDK CPH

- _新增特性_
  - 支持云手机服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持接口`AssociateQueueToElasticResourcePool`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ChangeFlinkJobStatusReport`请求参数`msg_confirm_topic`改为非必填
  - 接口`CreateFlinkJar`移除请求参数 `key`、`value`
  - 接口`UpdateFlinkJar`移除请求参数 `key`、`value`
  - 接口`CreateFlinkSql`移除请求参数 `key`、`value`
  - 接口`UpdateFlinkSql`移除请求参数 `key`、`value`
  - 接口`CreateQueue`新增请求参数 `elastic_resource_pool_name`
  - 接口`ListQueues`响应参数`labels`类型调整 `string` -> `array`
  - 接口`ShowQueueDetail`新增响应参数 `queue_id`、`elastic_resource_pool_name`
  - 接口`CreateQueuePlan`请求参数`repeat_day`改为必填
  - 接口`ChangeQueuePlan`请求参数`repeat_day`改为必填

### HuaweiCloud SDK ECS

- _新增特性_
  - 支持接口`ListServersByTag`
- _解决问题_
  - 无
- _特性变更_
  - 接口`NovaCreateServers`请求参数`destination_type`改为必填

### HuaweiCloud SDK EG

- _新增特性_
  - 支持事件网格服务
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
  - 接口`CreateFunction`:
    - 新增响应参数 `enable_dynamic_memory`、`is_stateful_function`、`enable_auth_in_header`、`custom_image`
    - 请求参数`file`、`link`改为必填
    - 响应参数`user_id`类型调整 `int32` -> `string`
    - 响应参数`user_group_id`类型调整 `int32` -> `string`
    - 响应参数`concurrent_num`改为必填
    - 响应参数`mount_share_path`改为非必填
  - 接口`ListFunctions`:
    - 新增响应参数 `fail_count`
    - 移除请求参数 `X-Auth-Token`
    - 响应参数`concurrent_num`改为必填
  - 接口`ShowFunctionCode`:
    - 移除响应参数 `id`
    - 响应参数`file`、`link`、`concurrent_num`改为必填
  - 接口`UpdateFunctionCode`:
    - 移除响应参数 `id`
    - 请求参数`file`、`link`改为必填
    - 响应参数`file`、`link`、`concurrent_num`改为必填
  - 接口`ShowFunctionConfig`:
    - 新增响应参数 `is_stateful_function`、`enable_auth_in_header`、`custom_image`
    - 移除响应参数 `id`
    - 响应参数`user_id`类型调整 `int32` -> `string`
    - 响应参数`user_group_id`类型调整 `int32` -> `string`
    - 响应参数`concurrent_num`改为必填
    - 响应参数`mount_share_path`改为非必填
  - 接口`UpdateFunctionConfig`:
    - 新增响应参数 `enable_auth_in_header`、`custom_image`
    - 移除请求参数 `X-Auth-Token`
    - 移除响应参数 `id`
    - 请求参数`user_id`类型调整 `int32` -> `string`
    - 请求参数`user_group_id`类型调整 `int32` -> `string`
    - 请求参数`concurrent_num`改为必填
    - 请求参数`mount_share_path`改为非必填
    - 响应参数`user_id`类型调整 `int32` -> `string`
    - 响应参数`user_group_id`类型调整 `int32` -> `string`
    - 响应参数`concurrent_num`改为必填
    - 响应参数`mount_share_path`改为非必填
  - 接口`UpdateFunctionMaxInstanceConfig`:
    - 移除响应参数 `id`
    - 响应参数`user_id`类型调整 `int32` -> `string`
    - 响应参数`user_group_id`类型调整 `int32` -> `string`
    - 响应参数`concurrent_num`改为必填
    - 响应参数`mount_share_path`改为非必填
  - 接口`CreateFunctionVersion`:
    - 移除响应参数 `id`
    - 响应参数`user_id`类型调整 `int32` -> `string`
    - 响应参数`user_group_id`类型调整 `int32` -> `string`
    - 响应参数`concurrent_num`改为必填
    - 响应参数`mount_share_path`改为非必填
  - 接口`ListFunctionVersions`:
    - 新增响应参数 `is_stateful_function`、`enable_auth_in_header`、`custom_image`、`reserved_instance_idle_mode`
    - 移除响应参数 `log_group_id`、`log_stream_id`
    - 响应参数`concurrent_num`改为必填
  - 接口`CreateFunctionTrigger`请求参数`trigger_type_code`新增枚举值`SMN`、`RABBITMQ`、`DEDICATEDGATEWAY`、`OPENSOURCEKAFKA`、`APIC`、`GAUSSMONGO`、`EVENTGRID`
  - 接口`ListFunctionTriggers`:
    - 响应参数`trigger_type_code`新增枚举值`RABBITMQ`、`DEDICATEDGATEWAY`、`OPENSOURCEKAFKA`、`APIC`、`GAUSSMONGO`、`EVENTGRID`
    - 响应参数`trigger_status`新增枚举值`DISABLE`, 移除枚举值`DISABLED`
  - 接口`DeleteFunctionTrigger`请求参数`trigger_type_code`新增枚举值`RABBITMQ`、`DEDICATEDGATEWAY`、`OPENSOURCEKAFKA`、`APIC`、`GAUSSMONGO`、`EVENTGRID`
  - 接口`ShowFunctionTrigger`:
    - 请求参数`trigger_type_code`新增枚举值`RABBITMQ`、`DEDICATEDGATEWAY`、`OPENSOURCEKAFKA`、`APIC`、`GAUSSMONGO`、`EVENTGRID`
    - 响应参数`trigger_type_code`新增枚举值`RABBITMQ`、`DEDICATEDGATEWAY`、`OPENSOURCEKAFKA`、`APIC`、`GAUSSMONGO`、`EVENTGRID`
    - 响应参数`trigger_status`新增枚举值`DISABLE`, 移除枚举值`DISABLED`
  - 接口`UpdateTrigger`:
    - 请求参数`trigger_status`新增枚举值`DISABLE`, 移除枚举值`DISABLED`
    - 请求参数`trigger_type_code`新增枚举值`RABBITMQ`、`DEDICATEDGATEWAY`、`OPENSOURCEKAFKA`、`APIC`、`GAUSSMONGO`、`EVENTGRID`
    - 请求参数`trigger_status`改为非必填
  - 接口`ListStatistics`响应参数`value`类型调整 `float` -> `int32`
  - 接口`UpdateFunctionReservedInstancesCount`:
    - 新增请求参数 `UpdateFunctionReservedInstancesCountRequestBody`
    - 新增响应参数 `idle_mode`、`tactics_config`
    - 移除请求参数 `UpdateFunctionReservedInstancesRequestBody`
  - 接口`CreateDependency`:
    - 新增响应参数 `version`、`last_modified`
    - 响应参数`runtime`类型调整 `enum` -> `string`
  - 接口`ListDependencies`:
    - 新增请求参数 `maxitems`、`ispublic`
    - 新增响应参数 `version`、`last_modified`
    - 响应参数`count`类型调整 `int32` -> `int64`
  - 接口`ShowDependcy`:
    - 新增响应参数 `version`、`last_modified`
    - 响应参数`runtime`类型调整 `enum` -> `string`
  - 接口`UpdateDependcy`:
    - 新增请求参数 `UpdateDependcyRequestBody`
    - 移除请求参数 `UpdateDependencyRequestBody`
    - 响应参数`runtime`类型调整 `enum` -> `string`
  - 接口`CreateEvent`移除响应参数 `content`、`last_modified`
  - 接口`UpdateEvent`移除响应参数 `content`、`last_modified`
  - 接口`ImportFunction`:
    - 新增请求参数 `package`
    - 移除请求参数 `X-Auth-Token`
    - 响应参数`concurrent_num`改为必填
  - 接口`EnableLtsLogs`新增请求参数 `X-Auth-Token`
  - 接口`ShowLtsLogDetails`新增响应参数 `group_name`
  - 接口`CancelAsyncInvocation`请求参数`request_id`改为必填
  - 接口`CreateWorkflow`:
    - 新增请求参数 `duration`
    - 请求参数`trigger_type`新增枚举值`SMN`、`APIG`、`APIG_DE`
  - 接口`ListWorkflow`:
    - 新增请求参数 `enterprise_project`、`mode`
    - 移除响应参数 `id`、`workflow_urn`、`name`、`description`、`created_time`、`updated_time`、`created_by`
  - 接口`StartWorkflowExecution`新增请求参数 `X-WorkflowRun-MergeFnParameters`
  - 接口`ListWorkflowExecutions`移除响应参数 `workflow_id`、`workflow_urn`、`execution_id`、`status`、`begin_time`、`end_time`、`last_update_time`、`created_by`
  - 接口`ShowWorkflowExecution`:
    - 新增请求参数 `X-Get-Workflow-Full-History-Data`
    - 响应参数`workflow_urn`类型调整 `string` -> `object`
  - 接口`ShowWorkFlow`:
    - 移除响应参数 `name`、`description`、`triggers`、`start`、`functions`、`states`、`constants`、`retries`、`mode`、`express_config`、`enterprise_project_id`
    - 响应参数`workflow_urn`类型调整 `string` -> `object`
    - 响应参数`id`、`workflow_urn`、`created_time`、`updated_time`、`created_by`改为必填
  - 接口`UpdateWorkFlow`:
    - 新增请求参数 `duration`
    - 请求参数`trigger_type`新增枚举值`SMN`、`APIG`、`APIG_DE`
    - 响应参数`workflow_urn`类型调整 `string` -> `object`
    - 响应参数`id`、`workflow_urn`、`name`、`description`、`created_time`、`updated_time`、`created_by`改为必填

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeIdCard`:
    - 新增请求参数 `detect_reproduce`
    - 新增响应参数 `detect_reproduce_result`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateIssueV4`:
    - 新增请求参数 `field_name`
    - 新增响应参数 `field_name`
  - 接口`ListIssuesV4`新增响应参数 `field_name`
  - 接口`UpdateIssueV4`:
    - 新增请求参数 `field_name`
    - 新增响应参数 `field_name`
  - 接口`ListChildIssuesV4`新增响应参数 `field_name`
  - 接口`CreateSystemIssueV4`:
    - 新增请求参数 `field_name`
    - 新增响应参数 `field_name`

### HuaweiCloud SDK ROMA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListNotification`新增请求参数 `limit`、`offset`

### HuaweiCloud SDK VOD

- _新增特性_
  - 支持以下接口：
    - `ListTranscodeTemplate`
    - `UpdateTranscodeTemplate`
    - `CreateTranscodeTemplate`
    - `DeleteTranscodeTemplate`
    - `ListTemplateGroupCollection`
    - `UpdateTemplateGroupCollection`
    - `CreateTemplateGroupCollection`
    - `DeleteTemplateGroupCollection`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK WAF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListIgnoreRule`:
    - 新增响应参数 `domain`
    - 移除响应参数 `domains`
  - 接口`ListGeoipRule`新增响应参数 `policyid`
  - 接口`UpdateGeoipRule`新增请求参数 `description`

# 3.0.103 2022-08-11

### HuaweiCloud SDK APM

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK BSS

- _新增特性_
  - 支持接口`ListCosts`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持接口`ShowUrlTaskInfo`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowDomainFullConfig`新增响应参数 `ipv6_accelerate`
  - 接口`UpdateDomainFullConfig`新增请求参数 `ipv6_accelerate`

### HuaweiCloud SDK CSMS

- _新增特性_
  - 支持接口`UploadSecretBlob`、`DownloadSecretBlob`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListGraphs`新增响应参数 `enableHyG`、`trafficIpList`、`cryptAlgorithm`、`enableHttps`、`tags`
  - 接口`ShowGraph`新增响应参数 `enableHyG`、`trafficIpList`、`cryptAlgorithm`、`enableHttps`、`tags`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreatePostPaidInstance`:
    - 新增请求参数 `broker_num`
    - 请求参数`specification`新增枚举值`c6.2u4g.cluster`、`c6.4u8g.cluster`、`c6.8u16g.cluster`、`c6.12u24g.cluster`、`c6.16u32g.cluster`
    - 请求参数`partition_num`新增枚举值`250`、`500`、`1000`、`1500`、`2000`
    - 请求参数`storage_spec_code`新增枚举值`dms.physical.storage.high.v2`、`dms.physical.storage.ultra.v2`
    - 请求参数`specification`改为非必填
  - 接口`ListInstances`新增响应参数 `description`、`access_user`、`ssl_two_way_enable`、`cert_replaced`、`public_boundwidth`、`agent_enable`、`public_access_enabled`、`node_num`、`new_spec_billing_enable`、`broker_num`
  - 接口`ShowInstance`新增响应参数 `description`、`access_user`、`ssl_two_way_enable`、`cert_replaced`、`public_boundwidth`、`agent_enable`、`public_access_enabled`、`node_num`、`new_spec_billing_enable`、`broker_num`
  - 接口`ShowInstanceExtendProductInfo`请求参数`engine`改为非必填
  - 接口`ShowPartitionBeginningMessage`:
    - 新增响应参数 `offset`
    - 移除响应参数 `message_offset`
  - 接口`ShowPartitionEndMessage`:
    - 新增响应参数 `offset`
    - 移除响应参数 `message_offset`
  - 接口`ListEngineProducts`新增响应参数 `product_alias`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 支持接口`RunCreateAudioModerationJob`、`RunQueryAudioModerationJob`
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunImageModeration`移除请求参数 `ad_glossaries`

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeMacaoIdCard`
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
  - 接口`CreateRestoreInstance`移除请求参数 `count`

### HuaweiCloud SDK SWR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListNamespaces`新增请求参数 `filter`
  - 接口`ListReposDetails`新增请求参数 `limit`、`offset`、`order_column`、`order_type`
  - 接口`ListRepositoryTags`新增请求参数 `filter`
  - 接口`ListSharedReposDetails`新增请求参数 `namespace`、`name`、`center`、`limit`、`offset`、`order_column`、`order_type`
  - 接口`ListRetentionHistories`:
    - 新增请求参数 `filter`
    - 移除请求参数 `offset`、`limit`

### HuaweiCloud SDK WAF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DeleteIgnoreRule`:
    - 新增响应参数 `advanced`
    - 移除响应参数 `rule`
  - 接口`CreateIgnoreRule`:
    - 新增请求参数 `advanced`
    - 新增响应参数 `advanced`
  - 接口`ListIgnoreRule`新增响应参数 `advanced`
  - 接口`ListStatistics`:
    - 移除响应参数 `host`
    - 请求参数`instances`类型调整 `string` -> `array`
    - 请求参数`hosts`类型调整 `string` -> `array`
  - 接口`ListQpsTimeline`:
    - 请求参数`instances`类型调整 `string` -> `array`
    - 请求参数`hosts`类型调整 `string` -> `array`
  - 接口`ListBandwidthTimeline`请求参数`instances`类型调整 `string` -> `array`
  - 接口`ListTopAbnormal`:
    - 请求参数`instances`类型调整 `string` -> `array`
    - 请求参数`hosts`类型调整 `string` -> `array`
  - 接口`ListOverviewsClassification`:
    - 请求参数`instances`类型调整 `string` -> `array`
    - 请求参数`hosts`类型调整 `string` -> `array`
  - 接口`ShowConsoleConfig`新增响应参数 `geoip_enable`、`load_balance_enable`、`ipv6_protection_enable`、`policy_sharing_enable`、`ip_group`、`robot_action_enable`、`http2_enable`、`timeout_config_enable`
  - 接口`CreateValueList`新增响应参数 `producer`
  - 接口`ListValueList`响应参数`type`类型调整 `string` -> `enum`
  - 接口`UpdateValueList`移除响应参数 `timestamp`
  - 接口`ListEvent`新增响应参数 `payload_location`
  - 接口`CreateHost`:
    - 新增请求参数 `web_tag`、`exclusive_ip`、`paid_type`、`lb_algorithm`、`weight`
    - 新增响应参数 `lb_algorithm`、`web_tag`、`block_page`、`extend`、`weight`、`ipv6`
  - 接口`ListHost`:
    - 新增响应参数 `region`、`web_tag`、`ipv6`
    - 移除响应参数 `timeout_config`
  - 接口`ListHostRoute`响应参数`back_protocol`类型调整 `string` -> `enum`
  - 接口`DeleteHost`新增响应参数 `web_tag`、`ipv6`
  - 接口`UpdateHost`:
    - 新增请求参数 `web_tag`、`exclusive_ip`、`paid_type`、`circuit_breaker`
    - 新增响应参数 `projectid`、`extend`、`traffic_mark`、`circuit_breaker`、`access_progress`、`weight`、`ipv6`
    - 移除请求参数 `lb_algorithm`
    - 移除响应参数 `ipv6_enable`
    - 响应参数`protocol`类型调整 `enum` -> `string`
    - 响应参数`web_tag`类型调整 `boolean` -> `string`
    - 响应参数`lb_algorithm`类型调整 `string` -> `enum`
  - 接口`ShowHost`新增响应参数 `domainid`、`projectid`、`enterprise_project_id`、`locked`、`tls`、`cipher`、`block_page`、`extend`、`traffic_mark`、`circuit_breaker`、`lb_algorithm`、`web_tag`、`flag`、`description`、`http2_enable`、`access_progress`、`weight`
  - 接口`CreatePolicy`新增响应参数 `robot_action`、`modulex_options`
  - 接口`ListPolicy`新增响应参数 `robot_action`、`modulex_options`、`hosts`
  - 接口`DeletePolicy`新增响应参数 `robot_action`、`modulex_options`
  - 接口`UpdatePolicyProtectHost`新增响应参数 `robot_action`、`modulex_options`、`hosts`
  - 接口`UpdatePolicy`:
    - 新增请求参数 `level`、`full_detection`、`robot_action`、`modulex_options`、`hosts`、`bind_host`、`extend`
    - 新增响应参数 `robot_action`、`modulex_options`
  - 接口`ShowPolicy`新增响应参数 `robot_action`、`modulex_options`、`hosts`
  - 接口`UpdatePolicyRuleStatus`请求参数`ruletype`新增枚举值`custom`、`ignore`
  - 接口`CreateWhiteblackipRule`:
    - 新增请求参数 `ip_group_id`
    - 新增响应参数 `name`、`ip_group`、`status`、`description`
    - 请求参数`addr`改为非必填
  - 接口`ListWhiteblackipRule`新增响应参数 `name`、`ip_group`
  - 接口`DeleteWhiteBlackIpRule`新增响应参数 `ip_group`
  - 接口`UpdateWhiteblackipRule`:
    - 新增请求参数 `ip_group_id`
    - 新增响应参数 `name`、`ip_group`
    - 请求参数`addr`改为非必填
  - 接口`CreatePrivacyRule`新增响应参数 `timestamp`、`status`、`description`
  - 接口`ListPrivacyRule`新增响应参数 `description`
  - 接口`UpdatePrivacyRule`新增响应参数 `timestamp`、`status`、`description`
  - 接口`CreateGeoipRule`:
    - 新增请求参数 `name`、`status`
    - 新增响应参数 `name`、`status`
  - 接口`ListGeoipRule`新增响应参数 `name`、`status`
  - 接口`DeleteGeoipRule`新增响应参数 `name`、`status`
  - 接口`UpdateGeoipRule`:
    - 新增请求参数 `name`
    - 新增响应参数 `name`
  - 接口`ListCertificates`移除响应参数 `content`、`key`
  - 接口`ListCompositeHosts`:
    - 新增响应参数 `hostid`、`web_tag`、`access_progress`、`premium_waf_instances`、`description`、`exclusive_ip`、`region`
    - 移除响应参数 `pci_dss`、`pci_3ds`、`cname`、`is_dual_az`、`ipv6`
  - 接口`ShowCompositeHost`:
    - 新增响应参数 `hostid`、`web_tag`、`access_progress`、`premium_waf_instances`、`description`、`exclusive_ip`、`region`
    - 移除响应参数 `pci_dss`、`pci_3ds`、`cname`、`is_dual_az`、`ipv6`
  - 接口`CreatePremiumHost`:
    - 新增请求参数 `block_page`、`description`、`weight`
    - 新增响应参数 `server`、`proxy`、`locked`、`timestamp`、`tls`、`cipher`、`extend`、`flag`、`description`、`enterprise_project_id`、`protect_status`、`access_status`、`block_page`
    - 响应参数`protocol`类型调整 `string` -> `enum`
  - 接口`ListPremiumHost`:
    - 新增响应参数 `extend`、`region`、`description`、`web_tag`、`hostid`
    - 移除响应参数 `mode`、`pool_ids`
  - 接口`DeletePremiumHost`:
    - 新增响应参数 `extend`、`description`、`web_tag`、`host_id`
    - 移除响应参数 `mode`、`pool_ids`
  - 接口`UpdatePremiumHost`:
    - 新增响应参数 `description`、`projectid`、`enterprise_project_id`、`web_tag`、`lb_algorithm`、`access_progress`、`weight`
    - 移除请求参数 `flag`、`extend`
    - 移除响应参数 `mode`、`pool_ids`、`project_id`、`access_code`
  - 接口`ShowPremiumHost`:
    - 新增响应参数 `description`、`projectid`、`enterprise_project_id`、`web_tag`、`access_progress`、`weight`
    - 移除响应参数 `mode`、`pool_ids`、`project_id`、`access_code`
  - 接口`UpdateCertificate`:
    - 新增请求参数 `content`、`key`
    - 请求参数`name`改为必填

# 3.0.102 2022-08-08

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持以下接口:
    - `UpdateSqlFilterControl`
    - `ShowSqlFilterControl`
    - `SetSqlFilterRule`
    - `ShowSqlFilterRule`
    - `DeleteSqlFilterRule`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.0.101 2022-08-02

### HuaweiCloud SDK CCM

- _新增特性_
  - 支持接口`RevokeCertificateAuthority`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCertificate`新增请求参数 `extended_key_usage`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowGaussMySqlFlavors`新增响应参数 `flavors`
  - 接口`ShowGaussMySqlInstanceInfo`新增响应参数 `instance`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持接口`UpgradeDbVersion`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `patch_available`

### HuaweiCloud SDK Image

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunImageDescription`移除请求参数 `language`

### HuaweiCloud SDK Live

- _新增特性_
  - 支持接口`CreateRecordIndex`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持接口`CreateProjectDomain`、`ListProjectDomains`、`UpdateProjectDomain`、`CancelProjectDomain`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeShortAudio`请求参数`audio_format`新增枚举值`auto`

# 3.0.100 2022-07-28

### HuaweiCloud SDK CBS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`CreateTbSession`、`ExecuteTbSession`、`DeleteTbSession`
  - 接口`CollectHotQuestions`请求参数`top`类型调整 `string` -> `int32`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchCreateJobs`请求参数`db_type`、`db_type`、`key`、`value`、`key`、`value`改为非必填
  - 接口`BatchSetObjects`请求参数`id`、`object_type`、`object_name`改为非必填
  - 接口`BatchUpdateJob`请求参数`name`、`alarm_to_user`、`db_type`、`db_type`、`node_type`、`engine_type`、`net_type`、`store_db_info`、`key`、`value`改为非必填
  - 接口`BatchListJobDetails`响应参数`db_type`、`db_type`、`db_type`、`db_type`改为非必填
  - 接口`BatchChangeData`请求参数`id`、`select`改为非必填

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ShowDedicatedResourceInfo`、`SetGaussMySqlProxyWeight`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowGaussMySqlProxy`新增响应参数 `proxy`、`master_node`、`readonly_nodes`
  - 接口`ShowGaussMySqlProxyList`新增响应参数 `proxy_list`
  - 接口`ShowGaussMySqlProxyFlavors`新增响应参数 `proxy_flavor_groups`
  - 接口`ShowGaussMySqlBackupList`:
    - 响应参数`status`新增枚举值`BUILDING`、`COMPLETED`、`FAILED`、`AVAILABLE`
    - 响应参数`type`新增枚举值`auto`、`manual`
    - 响应参数`backup_level`新增枚举值`0`、`1`、`2`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`:
    - 新增请求参数 `period_type`、`period_num`、`is_auto_renew`、`is_auto_pay`
    - 请求参数`charge_mode`新增枚举值`prePaid`
  - 接口`RunInstanceAction`新增请求参数 `is_auto_pay`
  - 接口`CreateRestoreInstance`:
    - 新增请求参数 `period_type`、`period_num`、`is_auto_renew`、`is_auto_pay`
    - 请求参数`charge_mode`新增枚举值`prePaid`
  - 接口`ResizeInstanceFlavor`请求参数`is_auto_pay`类型调整 `string` -> `boolean`

### HuaweiCloud SDK GSL

- _新增特性_
  - 支持接口`ShowMonthUsages`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK KMS

- _新增特性_
  - 支持以下接口：
    - `ListKeyStores`
    - `CreateKeyStore`
    - `ShowKeyStore`
    - `DeleteKeyStore`
    - `EnableKeyStore`
    - `DisableKeyStore`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateKey`新增请求参数 `keystore_id`
  - 接口`ListKeys`新增响应参数 `keystore_id`、`key_label`
  - 接口`ListKeyDetail`新增响应参数 `keystore_id`、`key_label`
  - 接口`ListKmsByTags`新增响应参数 `keystore_id`、`key_label`

### HuaweiCloud SDK NLP

- _新增特性_
  - 支持接口`RunConstituencyParser`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.0.99 2022-07-21

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListLatelyApiStatisticsV2`响应参数`status`类型调整 `string` -> `int32`

### HuaweiCloud SDK CES

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListAlarmHistories`:
    - 新增响应参数 `datapoints`
    - 移除响应参数 `data_points`、`type`、`notification_list`、`type`、`notification_list`
    - 响应参数`status`类型调整 `string` -> `enum`
    - 响应参数`level`类型调整 `int32` -> `enum`
    - 响应参数`type`类型调整 `string` -> `enum`
    - 响应参数`period`类型调整 `integer` -> `enum`
    - 响应参数`value`类型调整 `float` -> `double`
    - 响应参数`suppress_duration`类型调整 `integer` -> `enum`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`ShowInstanceStatusInfo`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`移除请求参数 `instance_user_domain_name`、`instance_user_name`
  - 接口`CreateInstanceBy3rd`移除请求参数 `instance_user_domain_name`、`instance_user_name`

### HuaweiCloud SDK HSS

- _新增特性_
  - 支持以下接口：
    - `ListHostStatus`
    - `ListPasswordComplexity`
    - `ListRiskConfigCheckRules`
    - `ListRiskConfigHosts`
    - `ListRiskConfigs`
    - `ListSecurityEvents`
    - `ListVulnerabilities`
    - `ListWeakPasswordUsers`
    - `ShowCheckRuleDetail`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Image

- _新增特性_
  - 支持接口`RunImageDescription`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`NeutronListSecurityGroupRules`新增响应参数 `security_group_rules_links`

# 3.0.98 2022-07-14

### HuaweiCloud SDK Core

- _新增特性_
  - 支持联邦认证
  - 支持认证信息管理
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK VCM

- _新增特性_
  - 支持视频内容审核服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerBillsMonthlyBreakDown`新增响应参数 `effective_tag_pairs`、`cost_unit_pairs`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateDomainFullConfig`新增请求参数 `tls_version`
  - 接口`ShowDomainFullConfig`新增响应参数 `tls_version`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowInstance`新增响应参数 `tags`、`cpu_type`

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListPublicips`响应参数`create_time`类型调整 `date-time` -> `string`
  - 接口`ShowPublicip`响应参数`create_time`类型调整 `date-time` -> `string`

### HuaweiCloud SDK Image

- _新增特性_
  - 支持接口`RunImageMediaTagging`、`RunImageMainObjectDetection`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListPorts`新增响应参数 `port_filter`、`ovs_hybrid_plug`
  - 接口`UpdatePort`新增响应参数 `port_filter`、`ovs_hybrid_plug`
  - 接口`ShowPort`新增响应参数 `port_filter`、`ovs_hybrid_plug`
  - 接口`CreateSecurityGroup`新增响应参数 `remote_address_group_id`
  - 接口`ListSecurityGroups`新增响应参数 `remote_address_group_id`
  - 接口`ShowSecurityGroup`新增响应参数 `remote_address_group_id`
  - 接口`ListSecurityGroupRules`新增响应参数 `remote_address_group_id`
  - 接口`ShowSecurityGroupRule`新增响应参数 `remote_address_group_id`
  - 接口`NeutronListSecurityGroups`新增响应参数 `remote_address_group_id`
  - 接口`NeutronUpdateSecurityGroup`新增响应参数 `remote_address_group_id`
  - 接口`NeutronShowSecurityGroup`新增响应参数 `remote_address_group_id`
  - 接口`NeutronListSecurityGroupRules`新增响应参数 `remote_address_group_id`
  - 接口`NeutronShowSecurityGroupRule`新增响应参数 `remote_address_group_id`

# 3.0.97 2022-07-07

### HuaweiCloud SDK APM

- _新增特性_
  - 支持接口`SearchApplication`、`SaveMonitorItemConfig`、`ListEnvMonitorItem`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CCE

- _新增特性_
  - 支持接口`UpdateClusterEip`、`ShowClusterEndpoints`、`ShowVersion`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListNodes`:
    - 新增响应参数 `isStatic`、`privateIPv6IP`
    - 响应参数`key`、`effect`改为必填
  - 接口`CreateNode`:
    - 新增请求参数 `isStatic`
    - 请求参数`key`、`effect`改为必填
  - 接口`ShowNode`:
    - 新增响应参数 `isStatic`、`privateIPv6IP`
    - 响应参数`key`、`effect`改为必填
  - 接口`DeleteNode`:
    - 新增响应参数 `isStatic`、`privateIPv6IP`
    - 响应参数`key`、`effect`改为必填
  - 接口`UpdateNode`:
    - 新增响应参数 `isStatic`、`privateIPv6IP`
    - 响应参数`key`、`effect`改为必填
  - 接口`AddNode`请求参数`key`、`effect`改为必填
  - 接口`ResetNode`请求参数`key`、`effect`改为必填
  - 接口`ListNodePools`:
    - 新增响应参数 `isStatic`
    - 响应参数`key`、`effect`改为必填
  - 接口`CreateNodePool`:
    - 新增请求参数 `isStatic`
    - 请求参数`key`、`effect`改为必填
  - 接口`ShowNodePool`:
    - 新增响应参数 `isStatic`
    - 响应参数`key`、`effect`改为必填
  - 接口`DeleteNodePool`:
    - 新增响应参数 `isStatic`
    - 响应参数`key`、`effect`改为必填
  - 接口`UpdateNodePool`:
    - 新增响应参数 `isStatic`
    - 请求参数`key`、`effect`改为必填
    - 响应参数`key`、`effect`改为必填

### HuaweiCloud SDK CloudRTC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateMixJob`新增请求参数 `filling_policy`
  - 接口`UpdateMixJob`:
    - 新增请求参数 `filling_policy`
    - 新增响应参数 `filling_policy`
  - 接口`ShowMixJob`新增响应参数 `filling_policy`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClustersDetails`移除响应参数 `CREATING`
  - 接口`ShowClusterDetail`移除响应参数 `CREATING`
  - 接口`UpdateUnbindPublic`新增请求参数 `unBindPublicReq`
  - 接口`ListYmlsJob`:
    - 新增响应参数 `configurations`
    - 移除响应参数 `configList`
  - 接口`ListYmls`:
    - 新增响应参数 `configurations`
    - 移除响应参数 `configList`

### HuaweiCloud SDK CTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateNotification`:
    - 新增请求参数 `filter`
    - 新增响应参数 `filter`
  - 接口`CreateNotification`新增请求参数 `filter`
  - 接口`ListNotifications`新增响应参数 `filter`

### HuaweiCloud SDK ELB

- _新增特性_
  - 支持接口`ListMasterSlavePools`、`CreateMasterSlavePool`、`ShowMasterSlavePool`、`DeleteMasterSlavePool`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSystemSecurityPolicies`:
    - 响应参数`protocols`类型调整 `array` -> `string`
    - 响应参数`ciphers`类型调整 `array` -> `string`
  - 接口`ListQuotaDetails`新增请求参数 `X-Auth-Token`
  - 接口`ListAvailabilityZones`新增请求参数 `public_border_group`
  - 接口`CreateLoadBalancer`:
    - 新增请求参数 `id`、`global_eip_ids`
    - 移除请求参数 `min_l4_flavor_id`
    - 请求参数`X-Auth-Token`改为必填
  - 接口`ListLoadBalancers`:
    - 新增响应参数 `global_eips`、`public_border_group`
    - 移除响应参数 `min_l4_flavor_id`
    - 请求参数`X-Auth-Token`改为必填
  - 接口`UpdateLoadBalancer`:
    - 新增请求参数 `cloud_service_console_url`
    - 新增响应参数 `global_eips`、`public_border_group`
    - 移除请求参数 `min_l4_flavor_id`
    - 移除响应参数 `min_l4_flavor_id`
  - 接口`ShowLoadBalancer`:
    - 新增响应参数 `global_eips`、`public_border_group`
    - 移除响应参数 `min_l4_flavor_id`
  - 接口`ChangeLoadbalancerChargeMode`新增请求参数 `X-Auth-Token`
  - 接口`CreateCertificate`移除请求参数 `enc_certificate`、`enc_private_key`
  - 接口`ListCertificates`移除响应参数 `enc_certificate`、`enc_private_key`
  - 接口`UpdateCertificate`:
    - 移除请求参数 `enc_certificate`、`enc_private_key`
    - 移除响应参数 `enc_certificate`、`enc_private_key`
  - 接口`ShowCertificate`移除响应参数 `enc_certificate`、`enc_private_key`
  - 接口`CreateListener`新增请求参数 `quic_config`
  - 接口`ListListeners`新增响应参数 `quic_config`
  - 接口`UpdateListener`:
    - 新增请求参数 `quic_config`
    - 新增响应参数 `quic_config`
  - 接口`ShowListener`新增响应参数 `quic_config`
  - 接口`CreatePool`新增请求参数 `vpc_id`、`type`
  - 接口`ListPools`:
    - 新增请求参数 `vpc_id`、`type`
    - 新增响应参数 `created_at`、`updated_at`、`vpc_id`、`type`
  - 接口`UpdatePool`:
    - 新增请求参数 `X-Auth-Token`、`vpc_id`、`type`
    - 新增响应参数 `created_at`、`updated_at`、`vpc_id`、`type`
  - 接口`ShowPool`新增响应参数 `created_at`、`updated_at`、`vpc_id`、`type`
  - 接口`CreateMember`请求参数`project_id`类型调整 `enum` -> `string`
  - 接口`ListMembers`:
    - 新增响应参数 `status`、`loadbalancers`、`created_at`、`updated_at`
    - 移除请求参数 `instance_id`
  - 接口`UpdateMember`新增响应参数 `status`、`loadbalancers`、`created_at`、`updated_at`
  - 接口`ShowMember`新增响应参数 `status`、`loadbalancers`、`created_at`、`updated_at`
  - 接口`ListAllMembers`新增响应参数 `status`、`loadbalancers`、`created_at`、`updated_at`
  - 接口`ListHealthMonitors`新增响应参数 `created_at`、`updated_at`
  - 接口`UpdateHealthMonitor`新增响应参数 `created_at`、`updated_at`
  - 接口`ShowHealthMonitor`新增响应参数 `created_at`、`updated_at`
  - 接口`CreateL7Policy`新增请求参数 `redirect_pools_config`
  - 接口`ListL7Policies`新增响应参数 `redirect_pools_config`、`created_at`、`updated_at`
  - 接口`UpdateL7Policy`:
    - 新增请求参数 `redirect_pools_config`
    - 新增响应参数 `redirect_pools_config`、`created_at`、`updated_at`
  - 接口`ShowL7Policy`新增响应参数 `redirect_pools_config`、`created_at`、`updated_at`
  - 接口`BatchUpdatePoliciesPriority`新增请求参数 `X-Auth-Token`
  - 接口`ListL7Rules`新增响应参数 `created_at`、`updated_at`
  - 接口`UpdateL7Rule`新增响应参数 `created_at`、`updated_at`
  - 接口`ShowL7Rule`新增响应参数 `created_at`、`updated_at`
  - 接口`UpdateIpList`:
    - 移除请求参数 `name`、`ip_list`、`description`
    - 请求参数`X-Auth-Token`改为必填
  - 接口`BatchDeleteIpList`:
    - 新增请求参数 `BatchDeleteIpListRequestBody`
    - 移除请求参数 `BatchDeleteIpGroupIpListRequestBody`
    - 请求参数`X-Auth-Token`改为必填
  - 接口`BatchCreateMembers`:
    - 新增请求参数 `BatchCreateMembersRequestBody`
    - 新增响应参数 `status`
    - 移除请求参数 `BatchCreateMemberRequestBody`
  - 接口`BatchDeleteMembers`:
    - 新增请求参数 `BatchDeleteMembersRequestBody`
    - 移除请求参数 `BatchDeleteMemberRequestBody`
  - 接口`UpdateLogtank`:
    - 新增请求参数 `UpdateLogtankRequestBody`
    - 移除请求参数 `logtank`

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `CreateAccessCode`
    - `ShowProtocolMappings`
    - `UploadProtocolMappings`
    - `BatchUpdateConfigs`
    - `ShowExternalEntity`
  - 接口`CreateEdgeApp`请求参数`function_type`新增枚举值`COMPOSITE_APPLICATION`、`DATA_COLLECTION`
  - 接口`BatchListEdgeAppVersions`新增响应参数 `sdk_version`、`deploy_multi_instance`
  - 接口`CreateEdgeApplicationVersion`新增请求参数 `sdk_version`、`deploy_multi_instance`、`ext_devices`、`tcp_socket`、`period_seconds`、`failure_threshold`、`tcp_socket`、`period_seconds`、`failure_threshold`
  - 接口`UpdateEdgeApplicationVersion`:
    - 新增请求参数 `deploy_multi_instance`、`sdk_version`、`ext_devices`、`tcp_socket`、`period_seconds`、`failure_threshold`、`tcp_socket`、`period_seconds`、`failure_threshold`
    - 新增响应参数 `sdk_version`、`deploy_multi_instance`
    - 请求参数`arch`改为非必填
  - 接口`ShowEdgeApplicationVersion`新增响应参数 `deploy_multi_instance`、`sdk_version`、`tcp_socket`、`period_seconds`、`failure_threshold`、`tcp_socket`、`period_seconds`、`failure_threshold`、`ext_devices`
  - 接口`UpdateEdgeApplicationVersionState`新增响应参数 `sdk_version`、`deploy_multi_instance`
  - 接口`CreateEdgeNode`新增请求参数 `edge_node_id`、`verify_code`、`time_out`、`arch`、`base_path`、`hardware_model`
  - 接口`ShowEdgeNode`新增响应参数 `ha_config`、`hardware_model`
  - 接口`CreateInstallCmd`新增请求参数 `CreateInstallCmdRequestBody`
  - 接口`BatchListModules`:
    - 新增响应参数 `control_status`、`container_settings`
    - 响应参数`state`新增枚举值`DELETE_SUCCESS`、`STOPPED`
    - 响应参数`function_type`新增枚举值`GATEWAY_MANAGER`、`COMPOSITE_APPLICATION`、`DATA_COLLECTION`
  - 接口`CreateModule`新增请求参数 `module_name`、`container_settings`
  - 接口`UpdateModule`:
    - 新增请求参数 `module_name`、`container_settings`
    - 新增响应参数 `control_status`
    - 请求参数`app_version`改为非必填
    - 响应参数`state`新增枚举值`DELETE_SUCCESS`、`STOPPED`
    - 响应参数`function_type`新增枚举值`GATEWAY_MANAGER`、`COMPOSITE_APPLICATION`、`DATA_COLLECTION`
  - 接口`ShowModule`:
    - 新增响应参数 `control_status`、`container_settings`
    - 响应参数`state`新增枚举值`DELETE_SUCCESS`、`STOPPED`
    - 响应参数`function_type`新增枚举值`GATEWAY_MANAGER`、`COMPOSITE_APPLICATION`、`DATA_COLLECTION`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeVatInvoice`新增响应参数 `title`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`SetSensitiveSlowLog`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RMS

- _新增特性_
  - 支持接口`ListSchemas`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeShortAudio`请求参数`property`新增枚举值`chinese_16k_travel`
  - 接口`PushTranscriberJobs`请求参数`property`新增枚举值`chinese_16k_media`
  - 接口`CollectTranscriberJob`新增响应参数 `audio_duration`
  - 接口`RunTts`请求参数`property`新增枚举值`chinese_huaxiaomei_common`、`chinese_huaxiaofei_common`

# 3.0.96 2022-06-30

### HuaweiCloud SDK UGO

- _新增特性_
  - 支持数据库和应用迁移服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`SendVerificationMessageCode`请求参数`mobile_phone`改为必填

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`SendVerificationMessageCode`请求参数`email`改为必填

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowDomainFullConfig`新增响应参数 `cache_url_parameter_filter`
  - 接口`UpdateDomainFullConfig`新增请求参数 `cache_url_parameter_filter`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`UploadExtensionFile`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DNS

- _新增特性_
  - 支持接口`CreateRecordSetWithBatchLines`、`BatchUpdateRecordSetWithLine`、`BatchDeleteRecordSetWithLine`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateRecordSetWithLine`请求参数`records`改为非必填

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持接口`UpdateFunctionMaxInstanceConfig`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `lb_port`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListComponentInfos`新增响应参数 `total_count`

### HuaweiCloud SDK IEF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateTag`:
    - 新增请求参数 `CreateTagRequestBody`
    - 移除请求参数 `tag`
  - 接口`ListEdgeNodes`新增请求参数 `sort`、`state`

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeHkIdCard`、`RecognizeCambodianIdCard`、`RecognizeExitEntryPermit`、`RecognizeMainlandTravelPermit`
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeGeneralText`响应参数`direction`类型调整 `int32` -> `float`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持接口`CreateProjectModule`、`ListProjectModules`、`UpdateProjectModule`、`DeleteProjectModule`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK UGO

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`MigrateSqlStatement`
  - 接口`ListApiVersions`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`id`、`links`、`version`、`status`、`updated`改为必填
  - 接口`ShowApiVersionInfo`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`id`、`links`、`version`、`status`、`updated`改为必填

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持接口`ListOverviewsClassification`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListStatistics`新增响应参数 `host`
  - 接口`ListHost`新增响应参数 `timeout_config`
  - 接口`ShowHost`新增响应参数 `timeout_config`
  - 接口`UpdateHost`:
    - 新增请求参数 `block_page`、`traffic_mark`、`flag`、`extend`、`http2_enable`、`ipv6_enable`、`lb_algorithm`、`timeout_config`
    - 新增响应参数 `http2_enable`、`ipv6_enable`、`lb_algorithm`、`timeout_config`
  - 接口`UpdatePremiumHost`:
    - 新增请求参数 `mode`、`locked`、`protect_status`、`access_status`、`timestamp`、`pool_ids`、`block_page`、`traffic_mark`、`flag`、`extend`、`circuit_breaker`、`timeout_config`
    - 新增响应参数 `timeout_config`
  - 接口`ShowPremiumHost`新增响应参数 `timeout_config`

# 3.0.95 2022-06-25

### HuaweiCloud SDK Core

- _新增特性_
  - 无
- _解决问题_
  - 修复云服务包依赖低版本的`huaweicloudsdkcore`导致`ModuleNotFoundError`的问题
- _特性变更_
  - 无

### HuaweiCloud SDK CodeCheck

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowTaskDetail`新增响应参数 `cyclomatic_complexity_per_file`、`file_duplication_ratio`

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持以下接口：
    - `ShowEntityConfiguration`
    - `UpdateEntityConfiguration`
    - `ShowConfigurationParameter`
    - `UpdateConfigurationParameter`
    - `DeleteConfiguration`
    - `ListConfigurations`
    - `CreateConfiguration`
    - `SwitchConfiguration`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`新增请求参数 `configurations`、`charge_info`
  - 接口`ResizeInstanceVolume`:
    - 新增请求参数 `is_auto_pay`
    - 新增响应参数 `order_id`
  - 接口`AddShardingNode`:
    - 新增请求参数 `is_auto_pay`
    - 新增响应参数 `order_id`
  - 接口`ResizeInstance`:
    - 新增请求参数 `is_auto_pay`
    - 新增响应参数 `order_id`
  - 接口`RestoreNewInstance`新增请求参数 `configurations`、`charge_info`

# 3.0.94 2022-06-23

### HuaweiCloud SDK Core

- _新增特性_
  - 支持自定义配置Region
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持数据湖探索服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UploadKie`:
    - 新增请求参数 `upload_file`
    - 移除请求参数 `UploadFile`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCluster`:
    - 新增请求参数 `httpsEnable`、`authorityEnable`、`adminPwd`
    - 请求参数`availability_zone`改为必填
  - 接口`ListClustersDetails`:
    - 新增响应参数 `publicKibanaResp`、`elbWhiteList`、`publicIp`、`bandwidthSize`、`diskEncrypted`、`backupAvailable`、`enterpriseProjectId`、`ip`
    - 移除响应参数 `enterprise_project_id`
  - 接口`ShowClusterDetail`:
    - 新增响应参数 `publicKibanaResp`、`elbWhiteList`、`publicIp`、`vpcId`、`subnetId`、`securityGroupId`、`bandwidthSize`、`diskEncrypted`、`backupAvailable`、`enterpriseProjectId`、`period`、`ip`
    - 移除响应参数 `enterprise_project_id`
  - 接口`ListFlavors`:
    - 新增响应参数 `type`、`availableAZ`
  - 接口`StartVpecp`:
    - 请求参数`endpointWithDnsName`类型调整 `string` -> `boolean`
  - 接口`CreateCluster`:
    - 新增请求参数 `payInfo`
    - 新增响应参数 `cluster`
    - 移除响应参数 `schema`
  - 接口`RestartCluster`:
    - 新增请求参数 `RestartClusterRequestBody`
    - 移除请求参数 `X-Auth-Token`、`RollingRestartReq`

### HuaweiCloud SDK DRS

- _新增特性_
  - 支持接口`ListAvailableZone`、`UpdateTuningParams`
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchCreateJobs`新增请求参数 `master_az`、`slave_az`
  - 接口`BatchSetPolicy`新增请求参数 `slot_name`

### HuaweiCloud SDK ELB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListQuotaDetails`:
    - 新增请求参数 `quota_key`
    - 移除请求参数 `type`
  - 接口`ListListeners`:
    - 新增请求参数 `loadbalancer_id`、`connection_limit`、`admin_state_up`、`http2_enable`、`enterprise_project_id`
    - 移除请求参数 `member_timeout`、`client_timeout`、`keepalive_timeout`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `subnet_id`
  - 接口`ExpandInstanceNode`新增请求参数 `subnet_id`

### HuaweiCloud SDK VSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`AuthorizeDomains`:
    - 新增响应参数 `usage_notice`
    - 请求参数`auth_mode`新增枚举值`free`

# 3.0.93 2022-06-19

### HuaweiCloud SDK AOM

- _新增特性_
  - 无
- _解决问题_
  - 修复接口`ListRangeQueryAomPromGet`的响应参数`data`类型错误的问题
- _特性变更_
  - 无

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeIdDocument`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RMS

- _新增特性_
  - 支持接口`RunQuery`、`CreateStoredQuery`、`ListStoredQueries`、`ShowStoredQuery`、`UpdateStoredQuery`、`DeleteStoredQuery`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CheckProductHealthy`请求参数`domain_id`、`project_id`、`region`、`company_name`、`product_name`改为必填
  - 接口`ImportEvents`:
    - 请求参数`type`、`domain_id`、`business`、`checkitem_id`、`checkpoint_id`、`spec_id`、`patch_id`改为必填
    - 请求参数`type`、`domain_id`、`product_feature`、`arrive_time`、`verification_state`改为非必填

### HuaweiCloud SDK VSS

- _新增特性_
  - 支持接口`ShowReportStatus`、`DownloadTaskReport`、`ExecuteGenerateReport`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.0.92 2022-06-09

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCluster`:
    - 新增响应参数 `schema`
    - 移除响应参数 `id`、`name`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateFunctionCode`响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`ShowFunctionCode`响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`UpdateFunctionConfig`:
    - 新增请求参数 `domain_names`
    - 新增响应参数 `domain_names`
    - 响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`ShowFunctionConfig`响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`CreateFunctionVersion`响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`ListStatistics`新增请求参数 `option`
  - 接口`CreateDependency`响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`ListDependencies`响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`UpdateDependency`响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`ShowDependency`响应参数`runtime`类型调整 `string` -> `enum`
  - 接口`UpdateEvent`请求参数`content`改为必填
  - 接口`ListFunctionAsyncInvocations`新增请求参数 `marker`
  - 接口`BatchDeleteWorkflows`请求参数`workflow_urns`改为必填
  - 接口`CreateWorkflow`请求参数`name`、`trigger_name`、`trigger_type`、`bucket`、`events`、`prefix`、`suffix`、`start`、`name`、`operation`、`id`、`name`、`type`、`end`、`transition`、`ref_name`、`arguments`、`constants`、`name`改为必填
  - 接口`StartWorkflowExecution`请求参数`input`改为必填
  - 接口`ShowWorkflowExecution`新增响应参数 `node_name`、`execution_id`、`request_id`
  - 接口`UpdateWorkFlow`请求参数`name`、`trigger_name`、`trigger_type`、`bucket`、`events`、`prefix`、`suffix`、`start`、`name`、`operation`、`id`、`name`、`type`、`end`、`transition`、`ref_name`、`arguments`、`constants`、`name`改为必填
  - 接口`ShowWorkFlow`:
    - 新增响应参数 `lts_group_id`、`lts_stream_id`
    - 响应参数`name`、`trigger_name`、`trigger_type`、`bucket`、`events`、`prefix`、`suffix`、`start`、`name`、`operation`、`id`、`name`、`type`、`end`、`transition`、`ref_name`、`arguments`、`constants`、`name`改为必填
  - 接口`StartSyncWorkflowExecution`请求参数`input`改为必填

### HuaweiCloud SDK GSL

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSimCards`新增请求参数 `tag_id`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 支持接口`RunTextModeration`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK MRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClusters`新增响应参数 `availabilityZoneId`
  - 接口`ShowClusterDetails`新增响应参数 `availabilityZoneId`
  - 接口`ListHosts`新增响应参数 `availability_zone_id`、`tags`

# 3.0.91 2022-06-02

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListFlavors`新增请求参数 `instance_id`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ChangeGaussMySqlProxySpecification`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Meeting

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`SearchCorpVmr`新增响应参数 `maxAudienceParties`、`expireDate`、`commercialMaxAudienceParties`

### HuaweiCloud SDK NAT

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListNatGateways`:
    - 请求参数`created_at`类型调整 `date-time` -> `string`
    - 响应参数`created_at`类型调整 `date-time` -> `string`
  - 接口`UpdateNatGateway`响应参数`created_at`类型调整 `date-time` -> `string`
  - 接口`ShowNatGateway`响应参数`created_at`类型调整 `date-time` -> `string`
  - 接口`ListNatGatewayDnatRules`:
    - 请求参数`created_at`类型调整 `date-time` -> `string`
    - 响应参数`created_at`类型调整 `date-time` -> `string`
  - 接口`UpdateNatGatewayDnatRule`响应参数`created_at`类型调整 `date-time` -> `string`
  - 接口`ShowNatGatewayDnatRule`响应参数`created_at`类型调整 `date-time` -> `string`
  - 接口`ListNatGatewaySnatRules`:
    - 请求参数`created_at`类型调整 `date-time` -> `string`
    - 响应参数`created_at`类型调整 `date-time` -> `string`
  - 接口`UpdateNatGatewaySnatRule`响应参数`created_at`类型调整 `date-time` -> `string`
  - 接口`ShowNatGatewaySnatRule`响应参数`created_at`类型调整 `date-time` -> `string`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeHealthCode`新增响应参数 `words_block_count`、`words_block_list`
  - 接口`RecognizePcrTestRecord`响应参数`confidence`类型调整 `float` -> `object`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateIssueV4`:
    - 新增请求参数 `new_custom_fields`
    - 新增响应参数 `new_custom_fields`、`new_name`
  - 接口`ListIssuesV4`:
    - 新增请求参数 `custom_fields`
    - 新增响应参数 `new_custom_fields`、`new_name`
  - 接口`ShowIssueV4`新增响应参数 `new_custom_fields`、`new_name`
  - 接口`UpdateIssueV4`:
    - 新增请求参数 `new_custom_fields`
    - 新增响应参数 `new_custom_fields`、`new_name`
  - 接口`ListChildIssuesV4`新增响应参数 `new_custom_fields`、`new_name`
  - 接口`CreateSystemIssueV4`:
    - 新增请求参数 `new_custom_fields`
    - 新增响应参数 `new_custom_fields`、`new_name`

# 3.0.90 2022-05-26

### HuaweiCloud SDK BCS

- _新增特性_
  - 支持接口`HandleUnionMemberQuitList`、`BatchRemovePeersFromChannel`、`DeleteChannel`
- _解决问题_
  - 无
- _特性变更_
  - 接口`DeleteBlockchain`新增请求参数 `is_delete_ief`、`is_delete_lightpeer`、`ief_nodes_id`
  - 接口`CreateNewBlockchain`:
    - 新增请求参数 `cluster_platform_type`
    - 移除请求参数 `user_name`、`password`
    - 请求参数`node_flavor`类型调整 `int64` -> `string`
    - 请求参数`cce_flavor`类型调整 `int64` -> `string`
    - 请求参数`init_node_pwd`类型调整 `int64` -> `string`
    - 请求参数`az`类型调整 `int64` -> `string`
    - 请求参数`cluster_platform_type`类型调整 `int64` -> `string`
  - 接口`CreateBlockchainCertByUserName`新增请求参数 `CreateBlockchainCertByUserNameRequestBody`
  - 接口`UnfreezeCert`新增请求参数 `file`
  - 接口`FreezeCert`新增请求参数 `file`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `features`、`sub_status`
  - 接口`ShowInstance`新增响应参数 `features`、`transparent_client_ip_enable`、`sub_status`
  - 接口`ResizeInstance`新增请求参数 `execute_immediately`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`AttachServerVolume`新增请求参数 `volume_type`、`hw:passthrough`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 支持接口`ListComponentInfos`、`SwitchShard`、`ResizeInstanceFlavor`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowBackupPolicy`移除响应参数 `rate_limit`、`prefetch_block`、`filesplit_size`
  - 接口`ListDbUsers`响应参数`memberof`类型调整 `object` -> `string`

### HuaweiCloud SDK KMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ValidateSignature`:
    - 新增响应参数 `signature_valid`
    - 移除响应参数 `signature_vaild`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateAomMappingRules`:
    - 新增请求参数 `deployments_prefix`
    - 新增响应参数 `deployments_prefix`
  - 接口`UpdateAomMappingRules`:
    - 新增请求参数 `deployments_prefix`
    - 新增响应参数 `deployments_prefix`
  - 接口`ShowAomMappingRules`新增响应参数 `deployments_prefix`
  - 接口`ShowAomMappingRule`新增响应参数 `deployments_prefix`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunCheckResult`新增响应参数 `ocr_text`、`error_code`、`error_msg`
  - 接口`RunImageBatchModeration`:
    - 新增请求参数 `moderation_rule`、`ad_categories`、`show_ocr_text`
    - 新增响应参数 `ocr_text`、`error_code`、`error_msg`
  - 接口`RunTaskSumbit`新增请求参数 `moderation_rule`、`ad_categories`、`show_ocr_text`

# 3.0.89 2022-05-19

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListEnvironmentVariablesV2`新增请求参数 `group_id`
  - 接口`UpdateSignatureKeyV2`新增响应参数 `update_time`、`create_time`、`id`、`name`、`sign_type`、`sign_key`、`sign_secret`、`sign_algorithm`
  - 接口`CreateInstanceV2`新增请求参数 `loadbalancer_provider`
  - 接口`ListInstancesV2`新增响应参数 `loadbalancer_provider`
  - 接口`ShowDetailsOfInstanceV2`新增响应参数 `endpoint_service`、`endpoint_services`、`node_ips`、`publicips`、`privateips`、`loadbalancer_provider`
  - 接口`UpdateInstanceV2`新增响应参数 `endpoint_service`、`endpoint_services`、`node_ips`、`publicips`、`privateips`、`loadbalancer_provider`

### HuaweiCloud SDK CSE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListEngines`移除请求参数 `X-Enterprise-Project-ID`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ResizeServer`新增请求参数 `dry_run`
  - 接口`ResizePostPaidServer`新增请求参数 `dry_run`
  - 接口`AttachServerVolume`新增请求参数 `dry_run`

### HuaweiCloud SDK MRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClusters`:
    - 新增响应参数 `GroupName`、`NodeNum`、`NodeSize`、`NodeSpecId`、`VmProductId`、`VmSpecCode`、`NodeProductId`、`RootVolumeSize`、`RootVolumeProductId`、`RootVolumeType`、`RootVolumeResourceSpecCode`、`RootVolumeResourceType`、`DataVolumeType`、`DataVolumeCount`、`DataVolumeSize`、`DataVolumeProductId`、`DataVolumeResourceSpecCode`、`DataVolumeResourceType`、`GroupName`、`NodeNum`、`NodeSize`、`NodeSpecId`、`VmProductId`、`VmSpecCode`、`NodeProductId`、`RootVolumeSize`、`RootVolumeProductId`、`RootVolumeType`、`RootVolumeResourceSpecCode`、`RootVolumeResourceType`、`DataVolumeType`、`DataVolumeCount`、`DataVolumeSize`、`DataVolumeProductId`、`DataVolumeResourceSpecCode`、`DataVolumeResourceType`
    - 移除响应参数 `groupName`、`nodeNum`、`nodeSize`、`nodeSpecId`、`vmProductId`、`vmSpecCode`、`nodeProductId`、`rootVolumeSize`、`rootVolumeProductId`、`rootVolumeType`、`rootVolumeResourceSpecCode`、`rootVolumeResourceType`、`dataVolumeType`、`dataVolumeCount`、`dataVolumeSize`、`dataVolumeProductId`、`dataVolumeResourceSpecCode`、`dataVolumeResourceType`、`groupName`、`nodeNum`、`nodeSize`、`nodeSpecId`、`vmProductId`、`vmSpecCode`、`nodeProductId`、`rootVolumeSize`、`rootVolumeProductId`、`rootVolumeType`、`rootVolumeResourceSpecCode`、`rootVolumeResourceType`、`dataVolumeType`、`dataVolumeCount`、`dataVolumeSize`、`dataVolumeProductId`、`dataVolumeResourceSpecCode`、`dataVolumeResourceType`
  - 接口`ShowClusterDetails`:
    - 新增响应参数 `GroupName`、`NodeNum`、`NodeSize`、`NodeSpecId`、`VmProductId`、`VmSpecCode`、`NodeProductId`、`RootVolumeSize`、`RootVolumeProductId`、`RootVolumeType`、`RootVolumeResourceSpecCode`、`RootVolumeResourceType`、`DataVolumeType`、`DataVolumeCount`、`DataVolumeSize`、`DataVolumeProductId`、`DataVolumeResourceSpecCode`、`DataVolumeResourceType`、`GroupName`、`NodeNum`、`NodeSize`、`NodeSpecId`、`VmProductId`、`VmSpecCode`、`NodeProductId`、`RootVolumeSize`、`RootVolumeProductId`、`RootVolumeType`、`RootVolumeResourceSpecCode`、`RootVolumeResourceType`、`DataVolumeType`、`DataVolumeCount`、`DataVolumeSize`、`DataVolumeProductId`、`DataVolumeResourceSpecCode`、`DataVolumeResourceType`
    - 移除响应参数 `groupName`、`nodeNum`、`nodeSize`、`nodeSpecId`、`vmProductId`、`vmSpecCode`、`nodeProductId`、`rootVolumeSize`、`rootVolumeProductId`、`rootVolumeType`、`rootVolumeResourceSpecCode`、`rootVolumeResourceType`、`dataVolumeType`、`dataVolumeCount`、`dataVolumeSize`、`dataVolumeProductId`、`dataVolumeResourceSpecCode`、`dataVolumeResourceType`、`groupName`、`nodeNum`、`nodeSize`、`nodeSpecId`、`vmProductId`、`vmSpecCode`、`nodeProductId`、`rootVolumeSize`、`rootVolumeProductId`、`rootVolumeType`、`rootVolumeResourceSpecCode`、`rootVolumeResourceType`、`dataVolumeType`、`dataVolumeCount`、`dataVolumeSize`、`dataVolumeProductId`、`dataVolumeResourceSpecCode`、`dataVolumeResourceType`
  - 接口`UpdateClusterScaling` 的请求参数 `data_volume_type`、`data_volume_count`、`data_volume_size`改为必填

### HuaweiCloud SDK VOD

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UploadMetaDataByUrl`请求参数`video_type`新增枚举值`M3U8`
  - 接口`PublishAssets`新增响应参数 `sign_url`
  - 接口`UnpublishAssets`新增响应参数 `sign_url`
  - 接口`ShowAssetMeta`新增响应参数 `sign_url`
  - 接口`ShowAssetDetail`新增响应参数 `sign_url`
  - 接口`ShowTakeOverTaskDetails`新增响应参数 `sign_url`
  - 接口`ShowTakeOverAssetDetails`新增响应参数 `sign_url`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListPorts`响应参数`device_owner`新增枚举值`neutron:VIP_PORT`, 移除枚举值`network:VIP_PORT`
  - 接口`UpdatePort`响应参数`device_owner`新增枚举值`neutron:VIP_PORT`, 移除枚举值`network:VIP_PORT`
  - 接口`ShowPort`响应参数`device_owner`新增枚举值`neutron:VIP_PORT`, 移除枚举值`network:VIP_PORT`

# 3.0.88 2022-05-12

### HuaweiCloud SDK CodeHub

- _新增特性_
  - 支持接口`AddProtectBranchV2`、`AddTagV2`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CPTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateTask`:
    - 请求参数`bodys`类型调整 `string` -> `array`
    - 请求参数`data`类型调整 `string` -> `object`
    - 响应参数`bodys`类型调整 `string` -> `array`
    - 响应参数`data`类型调整 `string` -> `object`
  - 接口`ShowTask`:
    - 响应参数`bodys`类型调整 `string` -> `array`
    - 响应参数`data`类型调整 `string` -> `object`
  - 接口`UpdateCase`:
    - 请求参数`bodys`类型调整 `string` -> `array`
    - 请求参数`data`类型调整 `string` -> `object`
  - 接口`UpdateTemp`:
    - 请求参数`bodys`类型调整 `string` -> `array`
    - 请求参数`data`类型调整 `string` -> `object`

### HuaweiCloud SDK CSS

- _新增特性_
  - 支持接口`DownloadCert`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClusterDetails`新增响应参数 `nodes`
  - 接口`ListClusters`新增响应参数 `nodes`

### HuaweiCloud SDK FRS

- _新增特性_
  - 支持以下接口：
    - `DetectLiveByUrlIntl`
    - `DetectLiveByFileIntl`
    - `DetectLiveByBase64Intl`
    - `DetectFaceByFileIntl`
    - `DetectFaceByUrlIntl`
    - `DetectFaceByBase64Intl`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSimCards`:
    - 新增请求参数 `min_used_flow`、`max_used_flow`、`min_left_flow`、`max_left_flow`
    - 移除请求参数 `min_flow`、`max_flow`

### HuaweiCloud SDK IAM

- _新增特性_
  - 支持接口`ShowDomainRoleAssignments`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunImageModeration`:
    - 新增请求参数 `show_ocr_text`
    - 新增响应参数 `ocr_text`

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeHealthCode`
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
  - 接口`RestoreExistInstance`:
    - 新增请求参数 `RestoreExistingInstanceRequestBody`
    - 移除请求参数 `RestoreToExistingInstanceRequest`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 支持分布式消息服务RocketMQ版
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.0.87 2022-05-05

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunImageModeration`请求参数`image`类型调整 `byte` -> `string`

### HuaweiCloud SDK RES

- _新增特性_
  - 支持接口`CreateResIntelligentScene`、`UpdateResIntelligentScene`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateResScene`:
    - 响应参数`created_at`类型调整 `int32` -> `int64`
    - 响应参数`update_at`类型调整 `int32` -> `int64`
  - 接口`ListResScenes`:
    - 响应参数`created_at`类型调整 `int32` -> `int64`
    - 响应参数`update_at`类型调整 `string` -> `int64`
  - 接口`ShowResScene`:
    - 响应参数`created_at`类型调整 `int32` -> `int64`
    - 响应参数`update_at`类型调整 `string` -> `int64`

# 3.0.86 2022-04-28

### HuaweiCloud SDK All

- _新增特性_
  - 支持云服务集合包 `huaweicloudsdkall`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK AOM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`AddOrUpdateServiceDiscoveryRules`请求参数`priority`类型调整 `string` -> `int32`
  - 接口`ListServiceDiscoveryRules`响应参数`priority`类型调整 `string` -> `int32`

### HuaweiCloud SDK CSE

- _新增特性_
  - 支持微服务引擎
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DevStar

- _新增特性_
  - 支持接口`ConfirmDeploymentJob`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDeploymentJobs`新增请求参数 `cci`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持接口`CancelAsyncInvocation`、`StartSyncWorkflowExecution`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListFunctionStatistics`:
    - 响应参数`timestamp`类型调整 `int32` -> `int64`
    - 响应参数`value`类型调整 `int32` -> `double`
  - 接口`ListStatistics`:
    - 响应参数`timestamp`类型调整 `int32` -> `int64`
    - 响应参数`value`类型调整 `int32` -> `double`
  - 接口`ListFunctionAsyncInvokeConfig`新增响应参数 `enable_async_status_log`
  - 接口`ShowFunctionAsyncInvokeConfig`新增响应参数 `enable_async_status_log`
  - 接口`UpdateFunctionAsyncInvokeConfig`:
    - 新增请求参数 `enable_async_status_log`
    - 新增响应参数 `enable_async_status_log`
  - 接口`CreateWorkflow`:
    - 新增请求参数 `mode`、`express_config`
    - 请求参数`type`新增枚举值`End`
  - 接口`ShowWorkFlow`:
    - 新增响应参数 `mode`、`express_config`
    - 响应参数`type`新增枚举值`End`
  - 接口`UpdateWorkFlow`:
    - 新增请求参数 `mode`、`express_config`
    - 请求参数`type`新增枚举值`End`
  - 接口`ShowTenantMetric`:
    - 新增请求参数 `start_time`、`end_time`
    - 响应参数`timestamp`类型调整 `int32` -> `int64`
    - 响应参数`value`类型调整 `int32` -> `double`
  - 接口`ShowWorkFlowMetric`:
    - 新增请求参数 `start_time`、`end_time`
    - 响应参数`timestamp`类型调整 `int32` -> `int64`
    - 响应参数`value`类型调整 `int32` -> `double`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ShowGaussMySqlProxyList`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateGaussMySqlReadonlyNode`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`
  - 接口`ExpandGaussMySqlInstanceVolume`移除响应参数 `size`、`order_id`
  - 接口`ListGaussMySqlDedicatedResources`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`
  - 接口`DeleteGaussMySqlProxy`新增请求参数 `CloseMysqlProxyRequest`
  - 接口`CreateGaussMySqlProxy`:
    - 新增请求参数 `proxy_name`、`proxy_mode`、`nodes_read_weight`
    - 请求参数`flavor_ref`、`node_num`改为必填
  - 接口`ExpandGaussMySqlProxy`新增请求参数 `proxy_id`
  - 接口`ListGaussMySqlErrorLog`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`
    - 请求参数`node_id`改为非必填
  - 接口`ListGaussMySqlSlowLog`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`
  - 接口`ListGaussMySqlConfigurations`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`
  - 接口`ShowGaussMySqlJobInfo`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`
  - 接口`ListInstanceTags`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`
  - 接口`ListProjectTags`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`
  - 接口`BatchTagAction`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `x-auth-token`

### HuaweiCloud SDK Meeting

- _新增特性_
  - 支持接口`ShowDepartment`
- _解决问题_
  - 无
- _特性变更_
  - 接口`SearchCorpDir`新增响应参数 `deptCodes`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 修复接口`RecognizeMyanmarDriverLicense`的响应体类型错误的问题
- _特性变更_
  - 无

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持接口`DeleteIgnoreRule`、`CreateIgnoreRule`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListIgnoreRule`移除响应参数 `id`、`policyid`、`timestamp`、`description`、`status`、`url`、`rule`、`domain`、`url_logic`、`advanced`
  - 接口`ListValueList`新增响应参数 `producer`
  - 接口`ListEvent`新增响应参数 `process_time`、`request_body`
  - 接口`ShowEvent`:
    - 新增响应参数 `process_time`、`request_body`
    - 响应参数`headers`类型调整 `string` -> `object`
    - 响应参数`response_size`类型调整 `string` -> `int32`
    - 响应参数`response_time`类型调整 `string` -> `int64`
  - 接口`ListHost`响应参数`paid_type`类型调整 `string` -> `enum`
  - 接口`CreateHost`新增响应参数 `flag`、`http2_enable`
  - 接口`UpdateHostProtectStatus`新增响应参数 `protect_status`
  - 接口`DeleteHost`响应参数`paid_type`类型调整 `string` -> `enum`
  - 接口`UpdateHost`响应参数`protocol`类型调整 `string` -> `enum`
  - 接口`DeletePolicy`新增响应参数 `id`、`name`、`level`、`action`、`options`、`full_detection`、`hosts`、`bind_host`、`timestamp`、`extend`
  - 接口`UpdatePolicyRuleStatus`新增响应参数 `id`、`policyid`、`timestamp`、`description`、`status`
  - 接口`DeletePrivacyRule`新增响应参数 `id`、`policyid`、`timestamp`、`description`、`status`、`url`、`category`、`index`
  - 接口`DeletePremiumHost`新增响应参数 `region`

# 3.0.85 2022-04-21

### HuaweiCloud SDK AS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateScalingGroup`新增请求参数 `iam_agency_name`
  - 接口`ListScalingGroups`新增响应参数 `iam_agency_name`
  - 接口`UpdateScalingGroup`新增请求参数 `iam_agency_name`
  - 接口`ShowScalingGroup`新增响应参数 `iam_agency_name`

### HuaweiCloud SDK BSS

- _新增特性_
  - 支持接口`ListConsumeSubCustomers`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerBillsMonthlyBreakDown`新增响应参数 `sub_service_type_code`、`sub_service_type_name`、`sub_resource_type_code`、`sub_resource_type_name`、`sub_resource_id`、`sub_resource_name`

### HuaweiCloud SDK CloudDeploy

- _新增特性_
  - 支持接口`ListDeployTasks`、`ListDeployTaskHistoryByDate`、`ShowProjectSuccessRate`、`ListTaskSuccessRate`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowInstance`新增响应参数 `domain_name_info`

### HuaweiCloud SDK DWS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClusters`新增响应参数 `tags`
  - 接口`ListSnapshotDetails`移除响应参数 `cluster_id`、`size`、`name`、`description`、`finished`、`started`、`id`、`type`、`status`

### HuaweiCloud SDK IES

- _新增特性_
  - 支持智能边缘小站服务
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
  - 接口`RestoreToExistingInstance`移除请求参数`restore_all_database`

# 3.0.84 2022-04-14

### HuaweiCloud SDK Core

- _新增特性_
  - 支持SK衍生认证方式
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateDomainFullConfig`新增请求参数 `sources`、`origin_protocol`、`force_redirect`、`compress`
  - 接口`ShowDomainFullConfig`:
    - 新增响应参数 `sources`、`origin_protocol`、`force_redirect`、`compress`
    - 响应参数`certificate_source`类型调整 `string` -> `int32`

### HuaweiCloud SDK CloudBuild

- _新增特性_
  - 支持接口`ShowJobSuccessRatio`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CodeCheck

- _新增特性_
  - 支持接口`ShowTasksRulesets`、`CheckRulesetParameters`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSMS

- _新增特性_
  - 支持云凭据管理服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateInstance`新增请求参数 `rename_commands`

### HuaweiCloud SDK DRS

- _新增特性_
  - 支持接口`BatchSetSmn`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowQuotas`请求参数`X-Language`改为非必填
  - 接口`BatchCreateJobs`请求参数`X-Language`改为非必填
  - 接口`BatchValidateConnections`请求参数`X-Language`改为非必填
  - 接口`BatchValidateClustersConnections`请求参数`X-Language`改为非必填
  - 接口`BatchSetObjects`请求参数`X-Language`改为非必填
  - 接口`BatchCheckJobs`请求参数`X-Language`改为非必填
  - 接口`BatchCheckResults`请求参数`X-Language`改为非必填
  - 接口`BatchSetSpeed`:
    - 新增请求参数 `is_utc`
    - 请求参数`X-Language`改为非必填
  - 接口`BatchShowParams`请求参数`X-Language`改为非必填
  - 接口`UpdateParams`请求参数`X-Language`改为非必填
  - 接口`BatchStartJobs`请求参数`X-Language`改为非必填
  - 接口`BatchRestoreTask`请求参数`X-Language`改为非必填
  - 接口`BatchStopJobs`请求参数`X-Language`改为非必填
  - 接口`BatchDeleteJobs`请求参数`X-Language`改为非必填
  - 接口`BatchUpdateJob`:
    - 请求参数`X-Language`改为非必填
    - 请求参数`endpoints`、`protocol`改为非必填
  - 接口`BatchResetPassword`请求参数`X-Language`改为非必填
  - 接口`BatchSetDefiner`请求参数`X-Language`改为非必填
  - 接口`CreateCompareTask`请求参数`X-Language`改为非必填
  - 接口`ListCompareResult`请求参数`X-Language`改为非必填
  - 接口`BatchListProgresses`请求参数`X-Language`改为非必填
  - 接口`BatchListJobDetails`:
    - 新增响应参数 `is_utc`
    - 请求参数`X-Language`改为非必填
    - 响应参数`alarm_notify`类型调整 `string` -> `object`
  - 接口`ShowJobList`:
    - 请求参数`X-Language`改为非必填
    - 响应参数`billing_tag`类型调整 `string` -> `boolean`
    - 响应参数`node_newFramework`类型调整 `string` -> `boolean`
  - 接口`BatchListJobStatus`请求参数`X-Language`改为非必填
  - 接口`BatchChangeData`请求参数`X-Language`改为非必填
  - 接口`BatchSwitchover`请求参数`X-Language`改为非必填
  - 接口`BatchListRposAndRtos`请求参数`X-Language`改为非必填
  - 接口`ShowMonitoringData`请求参数`X-Language`改为非必填
  - 接口`BatchListStructProcess`请求参数`X-Language`改为非必填
  - 接口`BatchListStructDetail`请求参数`X-Language`改为非必填
  - 接口`BatchUpdateUser`请求参数`X-Language`改为非必填
  - 接口`ListUsers`请求参数`X-Language`改为非必填
  - 接口`BatchSetPolicy`:
    - 请求参数`export_snapshot`类型调整 `string` -> `boolean`
    - 请求参数`X-Language`改为非必填
    - 请求参数`conflict_policy`、`filter_ddl_policy`改为非必填

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListServersDetails`新增请求参数 `ip_eq`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateFunctionConfig`新增请求参数 `encrypted_user_data`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 支持接口`RestartInstance`、`ShowInstanceConfiguration`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`:
    - 移除请求参数 `solution`
    - 请求参数`sharding_num`、`coordinator_num`改为非必填
  - 接口`ListConfigurations`新增响应参数 `count`
  - 接口`ListFlavors`新增响应参数 `total`

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSimPricePlans`:
    - 响应参数`create_time`类型调整 `date` -> `date-time`
    - 响应参数`active_time`类型调整 `date` -> `date-time`
    - 响应参数`stop_time`类型调整 `date` -> `date-time`

### HuaweiCloud SDK IEC

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSecurityGroups`新增响应参数 `action`、`priority`
  - 接口`CreateSecurityGroup`新增响应参数 `action`、`priority`
  - 接口`ShowSecurityGroup`新增响应参数 `action`、`priority`
  - 接口`ListSecurityGroupRules`新增响应参数 `action`、`priority`
  - 接口`CreateSecurityGroupRule`:
    - 新增请求参数 `action`、`priority`
    - 新增响应参数 `action`、`priority`
  - 接口`ShowSecurityGroupRule`新增响应参数 `action`、`priority`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateAomMappingRules`:
    - 请求参数`target_log_group_id`、`target_log_group_name`、`target_log_stream_id`、`target_log_stream_name`改为必填
    - 请求参数`container_name`改为非必填
    - 响应参数`target_log_group_id`、`target_log_group_name`、`target_log_stream_id`、`target_log_stream_name`改为必填
    - 响应参数`container_name`改为非必填
  - 接口`ShowAomMappingRules`:
    - 响应参数`target_log_group_id`、`target_log_group_name`、`target_log_stream_id`、`target_log_stream_name`改为必填
    - 响应参数`container_name`改为非必填
  - 接口`CreateAomMappingRules`:
    - 请求参数`target_log_group_id`、`target_log_group_name`、`target_log_stream_id`、`target_log_stream_name`改为必填
    - 请求参数`container_name`改为非必填
    - 响应参数`target_log_group_id`、`target_log_group_name`、`target_log_stream_id`、`target_log_stream_name`改为必填
    - 响应参数`container_name`改为非必填
  - 接口`ShowAomMappingRule`:
    - 响应参数`target_log_group_id`、`target_log_group_name`、`target_log_stream_id`、`target_log_stream_name`改为必填
    - 响应参数`container_name`改为非必填
  - 接口`ListHost`请求参数`host_id_list`改为必填
  - 接口`ListHostGroup`请求参数`host_group_id_list`改为必填
  - 接口`ListAccessConfig`请求参数`access_config_name_list`、`host_group_name_list`、`log_group_name_list`、`log_stream_name_list`改为必填

### HuaweiCloud SDK Moderation

- _新增特性_
  - 支持接口`RunModerationAudio`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SCM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCertificates`:
    - 新增请求参数 `enterprise_project_id`、`deploy_support`
    - 新增响应参数 `enterprise_project_id`
    - 响应参数`id`、`name`、`domain`、`sans`、`signature_algorithm`、`deploy_support`、`type`、`brand`、`expire_time`、`domain_type`、`validity_period`、`status`、`domain_count`、`wildcard_count`、`description`、`total_count`改为必填
  - 接口`ImportCertificate`:
    - 新增请求参数 `enterprise_project_id`
    - 响应参数`certificate_id`改为必填
  - 接口`ShowCertificate`:
    - 新增响应参数 `enterprise_project_id`
    - 响应参数`id`、`status`、`order_id`、`name`、`type`、`brand`、`push_support`、`revoke_reason`、`signature_algorithm`、`issue_time`、`not_before`、`not_after`、`validity_period`、`validation_method`、`domain_type`、`domain`、`sans`、`domain_count`、`wildcard_count`改为必填
  - 接口`ExportCertificate`响应参数`certificate`、`certificate_chain`、`private_key`改为必填

### HuaweiCloud SDK SMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListTasks`新增响应参数 `process_trace`
  - 接口`ShowTask`新增响应参数 `process_trace`
  - 接口`UpdateTask`新增请求参数 `process_trace`
  - 接口`UpdateTaskSpeed`:
    - 新增请求参数 `process_trace`、`compress_rate`
    - 请求参数`migrate_speed`改为非必填

# 3.0.83 2022-04-07

### HuaweiCloud SDK BSS

- _新增特性_
  - 支持接口`ListStoredValueCards`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListSubCustomerDiscounts`、`BatchSetSubCustomerDiscount`
  - 接口`ShowRefundOrderDetails`新增响应参数 `resource_type_name`、`service_type_name`
  - 接口`ListCustomerOrders`新增响应参数 `service_type_name`
  - 接口`ShowCustomerOrderDetails`新增响应参数 `service_type_name`、`service_type_name`
  - 接口`ListPayPerUseCustomerResources`新增响应参数 `resource_type_name`、`service_type_name`
  - 接口`ListCustomerOnDemandResources`新增响应参数 `service_type_name`、`resource_type_name`
  - 接口`ListSubcustomerMonthlyBills`新增响应参数 `cloud_service_type_name`、`resource_type_name`
  - 接口`ListCustomerselfResourceRecordDetails`新增响应参数 `cloud_service_type_name`、`resource_type_name`、`period_type`
  - 接口`ListCustomerselfResourceRecords`新增响应参数 `cloud_service_type_name`、`resource_type_name`
  - 接口`ShowCustomerMonthlySum`新增响应参数 `service_type_name`、`resource_type_name`
  - 接口`ListCustomerBillsFeeRecords`:
    - 新增请求参数 `bill_date_begin`、`bill_date_end`
    - 新增响应参数 `service_type_name`、`resource_type_name`
  - 接口`ListUsageTypes`新增响应参数 `resource_type_name`、`service_type_name`
  - 接口`ListSubCustomerBillDetail`新增响应参数 `service_type_name`、`resource_type_name`
  - 接口`ListCustomerBillsMonthlyBreakDown`新增响应参数 `service_type_name`、`resource_type_name`
  - 接口`ListFreeResourceInfos`新增响应参数 `service_type_name`
  - 接口`ListIncentiveDiscountPolicies`新增响应参数 `service_type_name`

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateNodePool`移除请求参数 `kind`、`apiVersion`、`status`

### HuaweiCloud SDK DSC

- _新增特性_
  - 支持以下接口：
    - `CreateDocWatermarkByAddress`
    - `ShowDocWatermarkByAddress`
    - `ShowImageWatermarkWithImage`
    - `CreateImageWatermarkByAddress`
    - `ShowImageWatermarkByAddress`
    - `ShowImageWatermarkWithImageByAddress`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateImageWatermark`:
    - 新增请求参数 `image_watermark`
    - 请求参数`blind_watermark`改为必填

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`StopSimCard`移除请求参数 `price_plan_list`
  - 接口`ResetSimCard`移除请求参数 `price_plan_list`

### HuaweiCloud SDK Meeting

- _新增特性_
  - 支持接口`StartMeeting`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeWaybillElectronic`
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeVatInvoice`新增响应参数 `print_code`
  - 接口`RecognizeVehicleLicense`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`
  - 接口`RecognizeTaxiInvoice`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`
  - 接口`RecognizeDriverLicense`新增响应参数 `type`、`accumulated_scores`、`status`、`generation_date`、`current_time`
  - 接口`RecognizeTrainTicket`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`
  - 接口`RecognizeBankcard`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ApplyConfigurationAsync`、`UpdateInstanceConfigurationAsync`、`DeleteSqlserverDatabaseEx`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 支持接口`ListConfigurations`、`ListDatastores`、`ListFlavors`、`ListStorageTypes`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`:
    - 新增请求参数 `solution`
    - 请求参数`mode`新增枚举值`centralization_standard`
    - 请求参数`type`新增枚举值`ESSD`

# 3.0.82 2022-03-31

### HuaweiCloud SDK CC

- _新增特性_
  - 支持云连接服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`BatchShowNodesInformation`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.0.81 2022-03-25

### HuaweiCloud SDK AOM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DeleteserviceDiscoveryRules`新增响应参数 `responseStatus`
  - 接口`AddOrUpdateServiceDiscoveryRules`新增响应参数 `responseStatus`

### HuaweiCloud SDK CCM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCertificateAuthority`:
    - 新增请求参数 `sort_key`、`sort_dir`、`X-Auth-Token`
    - 移除响应参数 `ca_id`、`type`、`status`、`path_length`、`freeze_flag`、`gen_mode`、`serial_number`、`create_time`、`delete_time`、`not_before`、`not_after`、`distinguished_name`、`crl_configuration`、`issuer_id`、`issuer_name`、`key_algorithm`、`signature_algorithm`
    - 请求参数`limit`类型调整 `string` -> `int32`
    - 请求参数`offset`类型调整 `string` -> `int32`
    - 响应参数`total`改为必填
  - 接口`CreateCertificateAuthority`:
    - 新增请求参数 `X-Auth-Token`、`key_usages`
    - 移除请求参数 `crl_dis_point`
    - 请求参数`start_from`类型调整 `string` -> `int32`
    - 请求参数`enabled`、`common_name`、`country`、`locality`、`organization`、`organizational_unit`、`state`、`key_algorithm`、`type`、`type`、`value`改为必填
    - 响应参数`ca_id`改为必填
  - 接口`ShowCertificateAuthorityObsAgency`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`agency_granted`改为必填
  - 接口`CreateCertificateAuthorityObsAgency`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`agency_id`改为必填
  - 接口`ListCertificateAuthorityObsBucket`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`create_time`类型调整 `string` -> `int64`
    - 响应参数`total`、`bucket_name`、`create_time`改为必填
  - 接口`ShowCertificateAuthorityQuota`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`type`类型调整 `enum` -> `string`
    - 响应参数`type`、`used`、`quota`改为必填
  - 接口`ShowCertificateAuthority`:
    - 新增请求参数 `X-Auth-Token`
    - 移除响应参数 `crl_dis_point`
    - 响应参数`create_time`类型调整 `string` -> `int64`
    - 响应参数`delete_time`类型调整 `string` -> `int64`
    - 响应参数`not_before`类型调整 `string` -> `int64`
    - 响应参数`not_after`类型调整 `string` -> `int64`
    - 响应参数`ca_id`、`type`、`status`、`path_length`、`freeze_flag`、`gen_mode`、`serial_number`、`create_time`、`delete_time`、`not_before`、`not_after`、`common_name`、`country`、`locality`、`organization`、`organizational_unit`、`state`、`enabled`、`issuer_id`、`issuer_name`、`key_algorithm`、`signature_algorithm`改为必填
  - 接口`DeleteCertificateAuthority`新增请求参数 `X-Auth-Token`
  - 接口`IssueCertificateAuthorityCertificate`:
    - 新增请求参数 `X-Auth-Token`
    - 请求参数`start_from`类型调整 `string` -> `int32`
    - 请求参数`issuer_id`、`path_length`、`signature_algorithm`、`type`、`value`改为必填
  - 接口`ExportCertificateAuthorityCsr`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`csr`改为必填
  - 接口`DisableCertificateAuthority`新增请求参数 `X-Auth-Token`
  - 接口`EnableCertificateAuthority`新增请求参数 `X-Auth-Token`
  - 接口`ExportCertificateAuthorityCertificate`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`certificate`、`certificate_chain`改为必填
  - 接口`ImportCertificateAuthorityCertificate`:
    - 新增请求参数 `X-Auth-Token`
    - 请求参数`certificate`改为必填
  - 接口`RestoreCertificateAuthority`新增请求参数 `X-Auth-Token`
  - 接口`ListCertificate`:
    - 新增请求参数 `sort_key`、`sort_dir`、`X-Auth-Token`
    - 移除响应参数 `certificate_id`、`status`、`freeze_flag`、`gen_mode`、`serial_number`、`create_time`、`not_before`、`not_after`、`distinguished_name`、`issuer_id`、`issuer_name`、`key_algorithm`、`signature_algorithm`
    - 请求参数`limit`类型调整 `string` -> `int32`
    - 请求参数`offset`类型调整 `string` -> `int32`
    - 响应参数`total`改为必填
  - 接口`CreateCertificate`:
    - 新增请求参数 `X-Auth-Token`
    - 请求参数`start_from`类型调整 `string` -> `int32`
    - 请求参数`common_name`、`country`、`locality`、`organization`、`organizational_unit`、`state`、`issuer_id`、`key_algorithm`、`signature_algorithm`、`type`、`value`、`type`、`value`改为必填
    - 响应参数`certificate_id`改为必填
  - 接口`CreateCertificateByCsr`:
    - 新增请求参数 `X-Auth-Token`、`type`、`path_length`
    - 请求参数`start_from`类型调整 `string` -> `int32`
    - 请求参数`csr`、`issuer_id`、`type`、`value`、`type`、`value`改为必填
    - 响应参数`certificate_id`改为必填
  - 接口`ParseCertificateSigningRequest`:
    - 新增请求参数 `X-Auth-Token`
    - 新增响应参数 `key_algorithm`、`key_algorithm_length`、`signature_algorithm`、`public_key`、`distinguished_name`
    - 移除响应参数 `total`、`certificates`
    - 请求参数`csr`改为必填
  - 接口`ShowCertificateQuota`:
    - 新增请求参数 `X-Auth-Token`
    - 响应参数`type`类型调整 `enum` -> `string`
    - 响应参数`type`、`used`、`quota`改为必填
  - 接口`ShowCertificate`:
    - 新增请求参数 `X-Auth-Token`
    - 新增响应参数 `delete_time`
    - 响应参数`create_time`类型调整 `string` -> `int64`
    - 响应参数`not_before`类型调整 `string` -> `int64`
    - 响应参数`not_after`类型调整 `string` -> `int64`
    - 响应参数`certificate_id`、`status`、`freeze_flag`、`gen_mode`、`serial_number`、`create_time`、`not_before`、`not_after`、`common_name`、`country`、`locality`、`organization`、`organizational_unit`、`state`、`issuer_id`、`issuer_name`、`key_algorithm`、`signature_algorithm`改为必填
  - 接口`DeleteCertificate`新增请求参数 `X-Auth-Token`
  - 接口`ExportCertificate`:
    - 新增请求参数 `X-Auth-Token`
    - 请求参数`is_compressed`、`type`改为必填
  - 接口`RevokeCertificate`:
    - 新增请求参数 `X-Auth-Token`
    - 移除请求参数 `cert_id`

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持V2版本接口：
    - `ShowDomainLocationStats`
    - `ShowDomainStats`
    - `ShowTopUrl`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DAS

- _新增特性_
  - 支持接口 `ShowSqlExplain`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRedislog`新增响应参数 `group_name`、`replication_ip`

### HuaweiCloud SDK DNS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListPublicZones`移除响应参数 `routers`
  - 接口`ShowRecordSetByZone`新增请求参数 `marker`、`limit`、`offset`、`line_id`、`tags`、`status`、`type`、`name`、`id`、`sort_key`、`sort_dir`、`search_mode`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSimCards`:
    - 新增请求参数 `min_flow`、`max_flow`、`order_id`、`filter_downtime_period`
    - 响应参数`device_status_date`类型调整 `date` -> `date-time`
    - 响应参数`expire_time`类型调整 `date` -> `date-time`
  - 接口`StopSimCard`新增请求参数 `price_plan_list`
  - 接口`ResetSimCard`新增请求参数 `price_plan_list`
  - 接口`ShowSimCard`:
    - 响应参数`device_status_date`类型调整 `date` -> `date-time`
    - 响应参数`expire_time`类型调整 `date` -> `date-time`

### HuaweiCloud SDK IMS

- _新增特性_
  - 支持接口`ListVersions`、`ShowVersion`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDataImage`请求参数`os_type`改为非必填

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 支持接口 `ResetFingerprint`
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
  - 接口`RecognizeVatInvoice`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`
  - 接口`RecognizeIdCard`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`
  - 接口`RecognizeDriverLicense`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`

### HuaweiCloud SDK VSS

- _新增特性_
  - 支持以下接口：
    - `ShowDomainSettings`
    - `UpdateDomainSettings`
    - `ListTaskHistories`
    - `ListPortResults`
    - `ListBusinessRisks`
    - `UpdateFalsePositive`
    - `CancelTasks`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDomains`新增请求参数 `domain_id`
  - 接口`ShowResults`新增响应参数 `hit_details`

# 3.0.80 2022-03-10

### HuaweiCloud SDK BCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchCreateChannels`新增响应参数 `operation_id`
  - 接口`CreateNewBlockchain`请求参数`fabric_version`改为非必填

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DeleteAddonInstance`请求参数`cluster_id`改为非必填

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowTopUrl`移除请求参数 `X-Auth-Token`
  - 接口`ShowDomainLocationStats`移除请求参数 `X-Auth-Token`
  - 接口`ShowDomainItemDetails`移除请求参数 `X-Auth-Token`
  - 接口`ShowDomainStats`移除请求参数 `X-Auth-Token`
  - 接口`ShowDomainItemLocationDetails`移除请求参数 `X-Auth-Token`

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ELB

- _新增特性_
  - 支持以下接口：
    - `ListLogtanks`
    - `CreateLogtank`
    - `ShowLogtank`
    - `UpdateLogtank`
    - `DeleteLogtank`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListFlavors`新增响应参数 `https_cps`
  - 接口`ShowFlavor`新增响应参数 `https_cps`
  - 接口`ListLoadBalancers`请求参数`X-Auth-Token`改为非必填
  - 接口`CreateLoadBalancer`请求参数`X-Auth-Token`改为非必填
  - 接口`UpdateIpList`请求参数`X-Auth-Token`改为非必填
  - 接口`BatchDeleteIpList`请求参数`X-Auth-Token`改为非必填

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListSimCards`响应参数`act_date`类型调整 `date` -> `date-time`
  - 接口`ShowSimCard`响应参数`act_date`类型调整 `date` -> `date-time`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListLogs`新增响应参数 `count`

### HuaweiCloud SDK Meeting

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`AddDepartment`新增请求参数 `sortLevel`
  - 接口`UpdateDepartment`新增请求参数 `sortLevel`
  - 接口`ShowDeptAndChildDept`新增响应参数 `sortLevel`、`sortLevel`
  - 接口`SearchDepartmentByName`新增响应参数 `sortLevel`

# 3.0.79 2022-03-07

### HuaweiCloud SDK CCE

- _新增特性_
  - 支持接口`UpdateClusterEip`、`ShowClusterEndpoints`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CES

- _新增特性_
  - 支持以下接口 (V2)：
    - `ListAlarms`
    - `CreateAlarm`
    - `DeleteAlarm`
    - `UpdateAlarmAction`
    - `ListAlarmResources`
    - `DeleteAlarmResources`
    - `AddAlarmResources`
    - `AddResourceGroupsResourcesBatch`
    - `DeleteResourceGroupsResourcesBatch`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchCreateJobs`请求参数`engine_type`新增枚举值`gaussdbv5`、`postgresql`
  - 接口`BatchValidateConnections`:
    - 新增请求参数 `kafka_security_config`
    - 请求参数`db_type`新增枚举值`postgresql`
  - 接口`BatchUpdateUser`:
    - 新增请求参数 `is_sync_object_privilege`
    - 新增响应参数 `no_privileges`、`parent_account`、`no_parent_account`
  - 接口`ListUsers`新增响应参数 `no_privileges`、`parent_account`、`no_parent_account`
  - 接口`BatchSetPolicy`新增请求参数 `topic_policy`、`topic`、`partition_policy`、`kafka_data_format`、`topic_name_format`、`partitions_num`、`replication_factor`、`is_fill_materialized_view`、`export_snapshot`

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreatePrePaidPublicip`的请求参数`ip_version`类型变更： `integer` -> `enum`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShrinkInstanceNode`新增响应参数 `order_id`

### HuaweiCloud SDK MPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListEditingJob`新增响应参数 `error_code`

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DownloadSlowlog`移除请求参数 `request_id`

# 3.0.78 2022-02-25

### HuaweiCloud SDK AS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListAllScalingV2Policies`新增请求参数 `alarm_id`
  - 接口`CreateScalingConfig`请求参数`volume_type`新增枚举值`GPSSD`
  - 接口`ShowResourceQuota`新增响应参数 `min`
  - 接口`ShowPolicyAndInstanceQuota`新增响应参数 `min`

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateBaremetalServerMetadata`:
    - 请求体类型修改 `MetaData` -> `UpdateBaremetalServerMetadataReq`
    - 移除响应参数 `key`

### HuaweiCloud SDK CDM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowJobs`响应参数`from-connector-name`、`to-link-name`改为必填
  - 接口`UpdateJob`请求参数`from-connector-name`、`to-link-name`改为必填
  - 接口`CreateAndStartRandomClusterJob`:
    - 请求参数`from-connector-name`、`to-link-name`改为必填
    - 响应参数`progress`类型调整 `int32` -> `float`
    - 响应参数`isStopingIncrement`类型调整 `boolean` -> `string`
  - 接口`StopJob`新增响应参数 `submissions`
  - 接口`CreateJob`请求参数`from-connector-name`、`to-link-name`改为必填
  - 接口`StartJob`:
    - 响应参数`progress`类型调整 `int32` -> `float`
    - 响应参数`isStopingIncrement`类型调整 `boolean` -> `string`
  - 接口`ShowJobStatus`响应参数`progress`类型调整 `double` -> `float`
  - 接口`ShowSubmissions`响应参数`progress`类型调整 `double` -> `float`

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持接口`ShowDomainLocationStats`、`ShowDomainFullConfig`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowDomainStats`:
    - 新增请求参数 `service_area`
    - 移除请求参数 `X-Auth-Token`、`country`、`district`、`isp`
    - 移除响应参数 `start_time`、`end_time`、`interval`、`action`、`stat_type`、`group_by`
  - 接口`UpdateDomainFullConfig`新增请求参数 `https`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`新增请求参数 `instance_domain_id`、`instance_user_id`
  - 接口`CreateInstanceBy3rd`请求参数`instance_user_domain_name`、`instance_user_name`改为非必填

### HuaweiCloud SDK CodeCheck

- _新增特性_
  - 支持接口`CheckRecord`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CloudRTC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRtcClientQosDetails`请求参数`mid`类型调整 `array` -> `string`

### HuaweiCloud SDK CodeHub

- _新增特性_
  - 支持接口`ShowStatisticCommitV3`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CPTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListProjectSets`:
    - 新增响应参数 `CreateTime`、`UpdateTime`、`external_params`、`variables_no_file`
    - 移除响应参数 `create_time`、`update_time`、`group`
  - 接口`UpdateProject`请求参数`name`改为必填
  - 接口`ShowTask`:
    - 新增响应参数 `parallel`、`contents`、`sort`、`related_temp_running_data`
    - 移除响应参数 `content`
  - 接口`UpdateTask`:
    - 新增请求参数 `contents`、`sort`、`related_temp_running_data`
    - 新增响应参数 `parallel`、`contents`、`sort`、`related_temp_running_data`
    - 移除请求参数 `content`
    - 移除响应参数 `content`
    - 请求参数`name`改为必填
  - 接口`ShowReport`:
    - 新增响应参数 `performance`、`minNetworkTraffic`、`avgNetworkTraffic`、`maxNetworkTraffic`、`branchId`、`branchName`、`projectId`、`serviceId`
    - 移除响应参数 `progressState`、`statusValue`
    - 响应参数`averageRespTime`类型调整 `float` -> `double`
    - 响应参数`avgRecBytes`类型调整 `float` -> `double`
    - 响应参数`avgSentBytes`类型调整 `int32` -> `double`
    - 响应参数`avgTranRespTime`类型调整 `string` -> `double`
    - 响应参数`currentThreadNum`类型调整 `int32` -> `double`
    - 响应参数`errorCount`类型调整 `int32` -> `double`
    - 响应参数`errorEventsCount`类型调整 `int32` -> `double`
    - 响应参数`failedAssert`类型调整 `int32` -> `double`
    - 响应参数`failedOthers`类型调整 `int32` -> `double`
    - 响应参数`failedParsed`类型调整 `int32` -> `double`
    - 响应参数`failedRefused`类型调整 `int32` -> `double`
    - 响应参数`failedTimeout`类型调整 `int32` -> `double`
    - 响应参数`max`类型调整 `int32` -> `double`
    - 响应参数`maxRecBytes`类型调整 `int32` -> `double`
    - 响应参数`maxRespTime`类型调整 `int32` -> `double`
    - 响应参数`maxSentBytes`类型调整 `int32` -> `double`
    - 响应参数`maxTranRespTime`类型调整 `int32` -> `double`
    - 响应参数`min`类型调整 `int32` -> `double`
    - 响应参数`requests`类型调整 `int32` -> `double`
    - 响应参数`result`类型调整 `int32` -> `double`
    - 响应参数`status`类型调整 `int32` -> `double`
    - 响应参数`successCount`类型调整 `int32` -> `double`
    - 响应参数`successRate`类型调整 `int32` -> `double`
    - 响应参数`sum1xx`类型调整 `int32` -> `double`
    - 响应参数`sum2xx`类型调整 `int32` -> `double`
    - 响应参数`sum3xx`类型调整 `int32` -> `double`
    - 响应参数`sum4xx`类型调整 `int32` -> `double`
    - 响应参数`sum5xx`类型调整 `int32` -> `double`
    - 响应参数`taskStatus`类型调整 `int32` -> `double`
    - 响应参数`tp50`类型调整 `int32` -> `double`
    - 响应参数`tp75`类型调整 `int32` -> `double`
    - 响应参数`tp90`类型调整 `int32` -> `double`
    - 响应参数`tp95`类型调整 `int32` -> `double`
    - 响应参数`tp99`类型调整 `int32` -> `double`
    - 响应参数`tps`类型调整 `float` -> `double`
    - 响应参数`tranTPS`类型调整 `string` -> `double`
    - 响应参数`transactionSuccess`类型调整 `string` -> `double`
    - 响应参数`transactionalSuccessRate`类型调整 `int32` -> `double`
    - 响应参数`transactionalTps`类型调整 `int32` -> `double`
    - 响应参数`transactionalTpsSuccess`类型调整 `int32` -> `double`
    - 响应参数`transactions`类型调整 `string` -> `double`
    - 响应参数`vum`类型调整 `int32` -> `double`
    - 响应参数`avgResponseTime`类型调整 `float` -> `double`
    - 响应参数`caseRetry`类型调整 `int32` -> `double`
    - 响应参数`completeNum`类型调整 `int32` -> `double`
    - 响应参数`duration`类型调整 `int32` -> `double`
    - 响应参数`executedNum`类型调整 `int32` -> `double`
    - 响应参数`kpiCaseCount`类型调整 `int32` -> `double`
    - 响应参数`kpiCaseExecuteCount`类型调整 `int32` -> `double`
    - 响应参数`kpiCasePassCount`类型调整 `int32` -> `double`
    - 响应参数`maxUsers`类型调整 `int32` -> `double`
    - 响应参数`passNum`类型调整 `int32` -> `double`
    - 响应参数`stage`类型调整 `int32` -> `double`
    - 响应参数`totalNum`类型调整 `int32` -> `double`
  - 接口`UpdateCase`:
    - 新增请求参数 `contents`、`sort`
    - 移除请求参数 `content`
  - 接口`CreateTemp`新增请求参数 `contents`
  - 接口`UpdateTemp`:
    - 请求参数`bodys`类型调整 `array` -> `string`
    - 请求参数`name`改为必填
  - 接口`CreateVariable`新增请求参数 `is_quoted`
  - 接口`ShowHistoryRunInfo`:
    - 响应参数`run_id`类型调整 `int32` -> `double`
    - 响应参数`run_type`类型调整 `int32` -> `double`
    - 响应参数`continue_time`类型调整 `int32` -> `double`

### HuaweiCloud SDK CSS

- _新增特性_
  - 支持以下接口：
    - `UpdateFlavor`
    - `UpdateFlavorByType`
    - `UpdateShrinkNodes`
    - `UpdateShrinkCluster`
    - `ListLogsJob`
    - `ShowClusterDetail`
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateExtendCluster`移除响应参数 `id`、`instances`
  - 接口`StartConnectivityTest`移除请求参数 `status`

### HuaweiCloud SDK DDM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ExpandInstanceNodes`新增请求参数 `group_id`
  - 接口`ShrinkInstanceNodes`新增请求参数 `group_id`
  - 接口`CreateDatabase`请求参数`shard_unit`改为非必填

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListConnections`:
    - 新增响应参数 `type`、`description`
    - 移除响应参数 `connectionType`
    - 响应参数`total`类型调整 `string` -> `int32`
    - 响应参数`name`改为必填
  - 接口`CreateConnection`:
    - 新增请求参数 `type`、`description`
    - 移除请求参数 `connectionType`
    - 请求参数`name`改为必填
  - 接口`ShowConnection`:
    - 新增响应参数 `type`、`description`
    - 移除响应参数 `connectionType`
    - 响应参数`name`改为必填
  - 接口`UpdateConnection`:
    - 新增请求参数 `type`、`description`
    - 移除请求参数 `connectionType`
    - 请求参数`name`改为必填
  - 接口`ExecuteScript`:
    - 新增响应参数 `instanceId`
    - 移除响应参数 `jobId`
    - 请求参数`params`类型调整 `string` -> `object`

### HuaweiCloud SDK ELB

- _新增特性_
  - 支持接口`BatchCreateMembers`、`BatchDeleteMembers`
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
  - 接口`ListFunctions`响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
  - 接口`CreateFunction`:
    - 请求参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
    - 响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
  - 接口`ShowFunctionCode`响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
  - 接口`UpdateFunctionCode`响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
  - 接口`ShowFunctionConfig`响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
  - 接口`UpdateFunctionConfig`:
    - 请求参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
    - 响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
  - 接口`ListFunctionVersions`响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
  - 接口`CreateFunctionVersion`响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`
  - 接口`CreateDependency`请求参数`runtime`新增枚举值`Java11`、`Node.js14.18`、`Python3.9`
  - 接口`UpdateDependency`请求参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`PHP 7.3`
  - 接口`ImportFunction`响应参数`runtime`新增枚举值`Java8`、`Java11`、`Node.js6.10`、`Node.js8.10`、`Node.js10.16`、`Node.js12.13`、`Node.js14.18`、`Python2.7`、`Python3.6`、`Python3.9`、`Go1.8`、`Go1.x`、`PHP7.3`, 移除枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`UpdateAuditLog`、`ShowAuditLog`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Live

- _新增特性_
  - 支持接口`ListSingleStreamDetail`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK LTS

- _新增特性_
  - 支持接口`UpdateStructConfig`、`CreateStructConfig`、`ListStructTemplate`、`ListBreifStructTemplate`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListLogGroups`新增响应参数 `tag`
  - 接口`ListLogStream`新增响应参数 `tag`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持接口`BatchUpdateChildNickNames`、`ListIterationHistories`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListProjectIterationsV4`新增请求参数 `updated_time_interval`、`include_deleted`
  - 接口`ListIssuesV4`新增请求参数 `include_deleted`、`updated_time_interval`
  - 接口`ShowIssueV4`新增响应参数 `description`、`order`、`accessories`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListSlowLogFile`、`StopInstance`、`StartupInstance`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SCM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCertificates`新增响应参数 `sans`、`signature_algorithm`、`deploy_support`
  - 接口`ImportCertificate`新增请求参数 `enc_certificate`、`enc_private_key`
  - 接口`ShowCertificate`:
    - 新增响应参数 `signature_algorithm`
    - 移除响应参数 `signature_algrithm`
  - 接口`ExportCertificate`新增响应参数 `enc_certificate`、`enc_private_key`

### HuaweiCloud SDK VOD

- _新增特性_
  - 支持接口`ListDomainLogs`
- _解决问题_
  - 无
- _特性变更_
  - 接口`DeleteAssets`新增请求参数 `delete_type`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`NeutronListSubnets`新增响应参数`subnetpool_id`

### HuaweiCloud SDK WAF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListWhiteblackipRule`:
    - 新增响应参数 `addr`
    - 移除响应参数 `ip`

# 3.0.77 2022-02-10

### HuaweiCloud SDK AOM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateAlarmRule`:
    - 请求参数`statistic`类型调整 `string` -> `enum`
    - 请求参数`alarm_level`、`comparison_operator`、`evaluation_periods`、`metric_name`、`namespace`、`period`、`statistic`、`threshold`、`unit`改为非必填

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRateOnPeriodDetail`:
    - 新增请求参数 `fee_installment_mode`
    - 新增响应参数 `installment_official_website_amount`、`installment_period_type`、`installment_official_discount_amount`、`installment_amount`

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListProtectable`:
    - 响应参数`result`类型调整 `string` -> `boolean`
    - 响应参数`size`类型调整 `string` -> `int32`
  - 接口`ShowProtectable`:
    - 响应参数`result`类型调整 `string` -> `boolean`
    - 响应参数`size`类型调整 `string` -> `int32`

### HuaweiCloud SDK CCE

- _新增特性_
  - 支持接口`ShowVersion`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateAddonInstance`移除响应参数 `kind`、`apiVersion`、`metadata`、`spec`、`status`
  - 接口`ListNodes`新增响应参数 `isStatic`、`privateIPv6IP`
  - 接口`CreateNode`新增请求参数 `isStatic`
  - 接口`DeleteNode`新增响应参数 `isStatic`、`privateIPv6IP`
  - 接口`ShowNode`新增响应参数 `isStatic`、`privateIPv6IP`
  - 接口`UpdateNode`新增响应参数 `isStatic`、`privateIPv6IP`
  - 接口`RemoveNode`:
    - 请求参数`uid`改为必填
    - 响应参数`uid`改为必填
  - 接口`MigrateNode`:
    - 请求参数`uid`改为必填
    - 响应参数`uid`改为必填
  - 接口`ListNodePools`新增响应参数 `isStatic`
  - 接口`CreateNodePool`新增请求参数 `isStatic`
  - 接口`DeleteNodePool`新增响应参数 `isStatic`
  - 接口`ShowNodePool`新增响应参数 `isStatic`
  - 接口`UpdateNodePool`:
    - 新增请求参数 `isStatic`
    - 新增响应参数 `isStatic`

### HuaweiCloud SDK CSS

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`CreateOnlineMigrationTask`、`SetOnlineMigrationTask`、`BatchStopMigrationTasks`、`StopMigrationTaskSync`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DevStar

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowApplicationDependentResources`:
    - 新增请求参数 `X-Auth-Token`、`limit`、`offset`
    - 新增响应参数 `count`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateFunction`:
    - 请求参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
    - 响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
  - 接口`ListFunctions`响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
  - 接口`UpdateFunctionCode`响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
  - 接口`ShowFunctionCode`响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
  - 接口`UpdateFunctionConfig`:
    - 请求参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
    - 响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
  - 接口`ShowFunctionConfig`响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
  - 接口`CreateFunctionVersion`响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
  - 接口`ListFunctionVersions`响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`
  - 接口`CreateDependency`请求参数`runtime`新增枚举值`Go1.x`
  - 接口`UpdateDependency`请求参数`runtime`新增枚举值`Go1.x`
  - 接口`ImportFunction`响应参数`runtime`新增枚举值`Java 8`、`Node.js 6.10`、`Node.js 8.10`、`Node.js 10.16`、`Node.js 12.13`、`Python 2.7`、`Python 3.6`、`Go 1.8`、`Go 1.x`、`PHP 7.3`, 移除枚举值`Python2.7`、`Python3.6`、`Go1.8`、`Java8`、`Node.js6.10`、`Node.js8.10`、`Custom`、`PHP7.3`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowGaussMySqlInstanceInfo`新增响应参数`alias`
  - 接口`CreateGaussMySqlBackup`新增响应参数`job_id`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`响应参数`port`类型调整 `int32` -> `string`

### HuaweiCloud SDK Live

- _新增特性_
  - 支持接口`ListTranscodeTaskCount`、`ListAreaDetail`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRecordData`新增请求参数 `publish_domain`
  - 接口`CreateRecordRule`移除请求参数 `plan_record_time`
  - 接口`ListRecordRules`移除响应参数 `plan_record_time`
  - 接口`ShowRecordRule`移除响应参数 `plan_record_time`
  - 接口`UpdateRecordRule`:
    - 移除请求参数 `plan_record_time`
    - 移除响应参数 `plan_record_time`
  - 接口`CreateRecordCallbackConfig`移除请求参数 `on_demand_callback_url`
  - 接口`ListRecordCallbackConfigs`移除响应参数 `on_demand_callback_url`
  - 接口`ShowRecordCallbackConfig`移除响应参数 `on_demand_callback_url`
  - 接口`UpdateRecordCallbackConfig`移除请求参数 `on_demand_callback_url`

### HuaweiCloud SDK Meeting

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`SearchQosParticipants`新增响应参数 `existQos`
  - 接口`SearchQosParticipantDetail`新增响应参数 `existQos`

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RestoreToExistingInstance`新增请求参数`restore_all_database`
  - 接口`StartRecyclePolicy`移除请求参数`is_open_recycle_policy`

# 3.0.76 2022-01-25

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateApiV2`新增请求参数 `content_type`
  - 接口`ShowDetailsOfApiV2`新增响应参数 `publish_time`、`roma_app_name`、`ld_api_id`、`api_group_info`、`content_type`
  - 接口`UpdateApiV2`:
    - 新增请求参数 `content_type`
    - 新增响应参数 `publish_time`、`roma_app_name`、`ld_api_id`、`api_group_info`、`content_type`
  - 接口`ListApiRuntimeDefinitionV2`新增响应参数 `content_type`
  - 接口`ListApiVersionDetailV2`:
    - 新增响应参数 `roma_app_name`、`ld_api_id`、`api_group_info`、`content_type`
    - 响应参数`publish_time`类型调整 `date-time` -> `string`

### HuaweiCloud SDK CDM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowJobs`:
    - 移除响应参数 `simple`
    - 响应参数`name`、`values`改为必填
  - 接口`UpdateJob`请求参数`name`、`values`改为必填
  - 接口`CreateAndStartRandomClusterJob`请求参数`name`、`values`改为必填
  - 接口`CreateJob`请求参数`name`、`values`改为必填
  - 接口`ListClusters`移除响应参数 `config_status`

### HuaweiCloud SDK CES

- _新增特性_
  - 支持接口`ListAlarmHistories`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CodeCheck

- _新增特性_
  - 支持接口`DeleteRuleset`、`SetDefaulTemplate`、`ShowTasklog`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateTask`新增请求参数 `endpoint_id`
  - 接口`CreateRuleset`新增请求参数 `custom_attributes`
  - 接口`ListTemplateRules`:
    - 新增请求参数 `tags`
    - 新增响应参数 `rule_config_list`

### HuaweiCloud SDK DevStar

- _新增特性_
  - 支持接口`ShowRepositoryByCloudIde`、`ListTemplates`
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
  - 接口`CreateLoginToken`新增响应参数`session_user_id`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`ListEngineProducts`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `dr_enable`
  - 接口`ShowInstance`新增响应参数 `dr_enable`
  - 接口`ListProducts`:
    - 新增响应参数 `Hourly`、`Monthly`
    - 移除响应参数 `hourly`、`honthly`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateSqlAlarmRule`移除请求参数 `language`
  - 接口`UpdateSqlAlarmRule`移除请求参数 `language`
  - 接口`ListSqlAlarmRules`:
    - 新增响应参数 `template_name`、`status`
    - 移除响应参数 `language`
  - 接口`CreateKeywordsAlarmRule`移除请求参数 `language`、`eps_id`、`eps_name`、`is_time_range_relative`
  - 接口`UpdateKeywordsAlarmRule`:
    - 移除请求参数 `language`、`eps_id`、`eps_name`、`is_time_range_relative`
    - 移除响应参数 `eps_id`、`eps_name`、`is_time_range_relative`
  - 接口`ListKeywordsAlarmRules`:
    - 新增响应参数 `template_name`、`status`
    - 移除响应参数 `language`、`eps_id`、`eps_name`、`is_time_range_relative`
  - 接口`ListAccessConfig`:
    - 新增请求参数 `access_config_tag_list`
    - 新增响应参数 `access_config_tag`
  - 接口`CreateAccessConfig`:
    - 新增请求参数 `access_config_tag`
    - 新增响应参数 `access_config_tag`
  - 接口`UpdateAccessConfig`:
    - 新增请求参数 `access_config_tag`
    - 新增响应参数 `access_config_tag`
  - 接口`DeleteAccessConfig`新增响应参数 `access_config_tag`

### HuaweiCloud SDK Meeting

- _新增特性_
  - 支持appId鉴权方式
  - 支持接口`ShowWebHookConfig`、`SetWebHookConfig`、`DeleteWebHookConfig`、`UpdateWebHookConfigStatus`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 支持接口`ListEngineProducts`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.0.75 2022-01-17

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 修复接口`CreateNodePool`的请求体结构错误的问题
- _特性变更_
  - 无

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持接口`ListFunctionAsyncInvocations`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowGaussMySqlInstanceInfo`新增响应参数`used`
  - 接口`UpdateInstanceMonitor`新增请求参数`monitor_switch`
  - 接口`UpdateInstanceMonitor`的请求参数`period`类型修改： `string` -> `int32`
  - 接口`ShowGaussMySqlProjectQuotas`移除响应参数`mode`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListApiVersionNew`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListFlavors`新增响应参数 `az_desc`

### HuaweiCloud SDK ROMA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`AddUserToApp`新增请求参数 `id`、`roles`
  - 接口`DownloadAssetArchive`移除响应参数 `apps`、`tasks`
  - 接口`ImportAsset`移除请求参数 `apps`、`tasks`
  - 接口`DeleteAsset`请求参数`tasks`改为必填
  - 接口`ShowMqsInstance`新增响应参数`access_user`

# 3.0.74 2022-01-10

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListOrderCouponsByOrderId`新增响应参数 `coupon_max_use_quantity`、`coupon_group`

### HuaweiCloud SDK CCE

- _新增特性_
  - 支持接口`ShowQuotas`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCluster`新增请求参数 `customSan`、`offloadCluster`、`cidrs`、`flavor`、`faultDomain`
  - 接口`ListClusters`新增响应参数 `customSan`、`offloadCluster`、`cidrs`、`flavor`、`faultDomain`
  - 接口`UpdateCluster`:
    - 新增请求参数 `customSan`、`containerNetwork`
    - 新增响应参数 `customSan`、`offloadCluster`、`cidrs`、`flavor`、`faultDomain`
  - 接口`ShowCluster`新增响应参数 `customSan`、`offloadCluster`、`cidrs`、`flavor`、`faultDomain`
  - 接口`DeleteCluster`新增响应参数 `customSan`、`offloadCluster`、`cidrs`、`flavor`、`faultDomain`
  - 接口`CreateNode`新增请求参数 `faultDomain`、`offloadNode`、`offloadNode`
  - 接口`ListNodes`新增响应参数 `faultDomain`、`offloadNode`、`offloadNode`
  - 接口`UpdateNode`新增响应参数 `faultDomain`、`offloadNode`、`offloadNode`
  - 接口`ShowNode`新增响应参数 `faultDomain`、`offloadNode`、`offloadNode`
  - 接口`DeleteNode`新增响应参数 `faultDomain`、`offloadNode`、`offloadNode`
  - 接口`CreateNodePool`新增请求参数 `podSecurityGroups`、`faultDomain`、`offloadNode`、`offloadNode`
  - 接口`ListNodePools`新增响应参数 `podSecurityGroups`、`faultDomain`、`offloadNode`、`offloadNode`
  - 接口`UpdateNodePool`:
    - 新增请求参数 `podSecurityGroups`、`faultDomain`、`offloadNode`、`offloadNode`
    - 新增响应参数 `podSecurityGroups`、`faultDomain`、`offloadNode`、`offloadNode`
  - 接口`ShowNodePool`新增响应参数 `podSecurityGroups`、`faultDomain`、`offloadNode`、`offloadNode`
  - 接口`DeleteNodePool`新增响应参数 `podSecurityGroups`、`faultDomain`、`offloadNode`、`offloadNode`

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持接口`UpdateDomainFullConfig`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`ListStacks`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListStacksByTag`

### HuaweiCloud SDK Cloudtest

- _新增特性_
  - 支持接口`ShowPlanList`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowPlans`:
    - 请求参数`limit`类型调整 `int64` -> `int32`
    - 请求参数`offset`类型调整 `int64` -> `int32`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListMigrationTask`新增响应参数 `ecs_tenant_private_ip`
  - 接口`ShowMigrationTask`新增响应参数 `ecs_tenant_private_ip`
  - 接口`StopMigrationTask`新增响应参数 `ecs_tenant_private_ip`

### HuaweiCloud SDK DDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`移除响应参数`lb_ip_address`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateServers`新增请求参数 `delete_on_termination`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateFunctionConfig`:
    - 新增请求参数 `is_stateful_function`
    - 新增响应参数 `is_stateful_function`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `lb_ip_address`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`请求参数`type`新增枚举值`GaussDB(for openGauss)`, 移除枚举值`GaussDB(openGauss)`
  - 接口`ListInstances`移除响应参数 `related_instance`

### HuaweiCloud SDK IMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`GlanceListImages`响应参数`active_at`改为非必填
  - 接口`GlanceShowImage`响应参数`active_at`改为非必填
  - 接口`GlanceUpdateImage`响应参数`active_at`改为非必填

### HuaweiCloud SDK IoTAnalytics

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateDatasource`请求参数`site_id`改为必填
  - 接口`UpdateDataSource`请求参数`site_id`改为必填

### HuaweiCloud SDK KPS

- _新增特性_
  - 支持数据加密服务-密钥对管理
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
  - 接口`StartInstanceSingleToHaAction`:
    - 新增请求参数 `ad_domain_info`
    - 移除请求参数 `password`

### HuaweiCloud SDK ROMA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowMqsInstance`移除响应参数 `connect_dn`
  - 接口`ListMqsInstanceTopics`移除响应参数 `policies`
  - 接口`ShowDetailsOfAppV2`新增响应参数 `roma_app_type`

### HuaweiCloud SDK VPCEP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateEndpointService`新增响应参数 `pool_id`
  - 接口`ListEndpointService`新增响应参数 `domain_id`
  - 接口`UpdateEndpointService`新增响应参数 `pool_id`
  - 接口`ListEndpointInfoDetails`新增响应参数 `enable_status`、`specification_name`

### HuaweiCloud SDK VSS

- _新增特性_
  - 支持接口`AuthorizeDomains`、`ShowTasks`、`CreateTasks`、`ShowResults`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDomains`响应参数`auth_status`新增枚举值`skip`

