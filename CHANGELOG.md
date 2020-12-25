## 3.0.27-beta 2020-12-25
## HuaweiCloud SDK DCS
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Query parameter in interface `ListInstances` modification: id → instance_id.

## HuaweiCloud SDK RMS
 - ### Features
    - Support more interfaces: `Resources` related interfaces and `Region` related interfaces. 
 - ### Bug Fix
    - None
 - ### Change
    - None


## 3.0.26-beta 2020-12-23
## HuaweiCloud SDK Core
 - ### Features
    - Support Endpoint Resolver: it's supported to use {Service}Region when initializing {ServiceClient} which can automatically backfill endpoint. After choosing a region, the projectId/domainId will be backfilled automatically.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK BSS
 - ### Features
    - Support more interfaces: ListMeasureUnits.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK CES
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Update interface: ShowMetricData

## HuaweiCloud SDK DLI
 - ### Features
    - Support Data Lake Insight service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Live
 - ### Features
    - Support more interfaces: ShowStreamPortrait.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK MPC
 - ### Features
    - Support more interfaces: QualityEnhanceTemplate related interfaces and MergeChannelsTask related interfaces.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK RDS
 - ### Features
    - Support Relational Database Service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK SMN
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Update field type in message_template_name.


## 3.0.25-beta 2020-12-15
## HuaweiCloud SDK CCE
 - ### Features
    - Support Cloud Container Engine service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK ELB
 - ### Features
    - None
 - ### Bug Fix
    - Fix the problem that sending request to interface `CreateListener` returns empty response.
    - Fix the problem that sending request to interface `CreateListener` returns response with wrong type. 
 - ### Change
    - None

## HuaweiCloud SDK FunctionGraph
 - ### Features
    - Support more interfaces: UpdateFunctionReservedInstances.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Meeting
 - ### Features
    - Support more interfaces: CreatePortalRefNonce.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK NAT
 - ### Features
    - None
 - ### Bug Fix
    - Fix the problem that using interface `BatchCreateNatGatewayDnatRules` failed. 
 - ### Change
    - None


## 3.0.24-beta 2020-12-04
## HuaweiCloud SDK SMN
 - ### Features
    - Support Simple Message Notification service.
 - ### Bug Fix
    - None
 - ### Change
    - None


## 3.0.23-beta 2020-11-30
## HuaweiCloud SDK BCS
 - ### Features
    - Support BlockChain Service.
 - ### Bug Fix
    - None
 - ### Change
    - None 

## HuaweiCloud SDK BMS
 - ### Features
    - Support Bare Metal Server service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK BSS
 - ### Features
    - Support more interfaces: ListUsageTypes, ModPeriodToOnDemand.
 - ### Bug Fix
    - None
 - ### Change
    - None 

## HuaweiCloud SDK CBR
 - ### Features
    - Support more interfaces: MigrateVaultResource.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK CES
 - ### Features
    - Support more interfaces: 
     - ListEvents
     - ListEventDetail
     - CreateResourceGroup
     - UpdateResourceGroup
     - DeleteResourceGroup
     - ListResourceGroup
     - UpdateAlarm
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK ECS
 - ### Features
    - None 
 - ### Bug Fix
    - None
 - ### Change
    - [Issue 21](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/21) Open related interface.

## HuaweiCloud SDK IAM
 - ### Features
    - Support more interfaces.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Live
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Name of service client modification: LiveAPIClient → LiveClient.

## HuaweiCloud SDK Meeting
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Property of interface `CreateMeeting` adjustment: increase property `callInRestriction`.
    - Property of interface `EditMeeting` adjustment: increase property `callInRestriction`.


## 3.0.22-beta 2020-11-17
## HuaweiCloud SDK DMS
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Type of property adjustment: type of property `created` and type of `eff_date` are changed from `string` to `integer64`.  

## HuaweiCloud SDK ECS
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Property adjustment:  increase property `dry_run` in interfaces `CreatePostPaidServers` and `CreateServers` which means whether parameters will be checked before sending real requests. 

## HuaweiCloud SDK NAT
 - ### Features
    - Support NAT Gateway service.
 - ### Bug Fix
    - None
 - ### Change
    - None 

## HuaweiCloud SDK Kafka
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Name of interface adjustment: UpdateInstanceCrossVPCIP → UpdateInstanceCrossVpcIp

## HuaweiCloud SDK RMS
 - ### Features
    - Support Resource Manager Service.
 - ### Bug Fix
    - None
 - ### Change
    - None 

## HuaweiCloud SDK VPC
 - ### Features
    - Support more interfaces: interfaces related to Network ACLs. 
 - ### Bug Fix
    - None
 - ### Change
    - None


## 3.0.21-beta 2020-11-11
## HuaweiCloud SDK Core
 - ### Features
    - None
 - ### Bug Fix
    - Fix the problem of parameter conversion error when special characters exclude `-` and `_` are in query paramters.
 - ### Change
    - None

## HuaweiCloud SDK CBR
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Interface adjustment: property `object_type` in interface `CreateVault` support key `turbo`.
    - Interface adjustment: property `description` in interface `UpdatePolicy` is removed.

## HuaweiCloud SDK CES
 - ### Features
    - Add examples of interface response and adjust some filed description.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK CloudPipeline
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Modify the name of generated Client class: devcloudpipeline_client → cloudpipeline_client, devcloudpipeline_async_client → cloudpipeline_async_client

## HuaweiCloud SDK DevStar
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Modify interface parameters and adjust sample code.


## 3.0.20-beta 2020-11-02
## HuaweiCloud SDK CES
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Interface adjustment: property `alarm_type` in class `CreateAlarmRequestBody` support key `RESOURCE_GROUP`.
    - Interface adjustment: property `meta_data` in class `ListAlarmHistoriesResponse` only returns total number of alarm histories.

## HuaweiCloud SDK ELB
 - ### Features
    - None
 - ### Bug Fix
    - Modify wrong parameter in class `CreateL7ruleRequestBody`.
 - ### Change
    - None


## 3.0.19-beta 2020-10-31
## HuaweiCloud SDK CBR
 - ### Features
    - Support more interfaces: interfaces related to `TAG`.
 - ### Bug Fix
    - [Issue 17](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/17) fix the problem of interface: ListBackups.
 - ### Change
    - None

## HuaweiCloud SDK CTS
 - ### Features
    - Support more interface: ListQuotas
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK EPS
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Adjust interfaces' names, replace abbreviations of `EP` with `EnterpriseProject`, the involved interfaces are:
     1. ListEP → ListEnterpriseProject
     2. CreateEP → CreateEnterpriseProject
     3. ShowEP → ShowEnterpriseProject
     4. ModifyEP → ModifyEnterpriseProject
     5. EnableEP → EnableEnterpriseProject
     6. ShowEPQuota → ShowEnterpriseProjectQuota
     7. ShowResourceBindEP → ShowResourceBindEnterpriseProject
     8. DisableEP → DisableEnterpriseProject

## HuaweiCloud SDK FunctionGraph
 - ### Features
    - Support more interfaces: UpdateTrigger, ListFunctionStatistics, ListStatistics, ListQuotas
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Iam
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Adjust interfaces' names, the involved interfaces are:
     1. KeystoneCreateUserTokenByPasswordAndMFA → KeystoneCreateUserTokenByPasswordAndMfa
     2. CreateUnscopeTokenByIDPInitiated → CreateUnscopeTokenByIdpInitiated

## HuaweiCloud SDK ProjectMan
 - ### Features
    - Support more interfaces: iteration information, user information, project members, project information, project indicators, project statistics, etc.
 - ### Bug Fix
    - None
 - ### Change
    - None


## 3.0.18-beta 2020-10-20
## HuaweiCloud SDK DCS
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Remove redundant `Dcs` in interfaces.

## HuaweiCloud SDK ELB
 - ### Features
    - Support more interfaces of version v2.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK IoTDA
 - ### Features
    - Support more interfaces related to rules.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Meeting
 - ### Features
    - Support more interfaces.
 - ### Bug Fix
    - None
 - ### Change
    - None


## 3.0.17-beta 2020-10-14
## HuaweiCloud SDK BSS
 - ### Features
    - Partner center supports exporting product catalog prices.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK DCS
 - ### Features
    - Support more interfaces.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Live
 - ### Features
    - Support more interfaces of version v2 of Live.
 - ### Bug Fix
    - None
 - ### Change
    - None


## 3.0.16-beta 2020-10-12
## HuaweiCloud SDK CTS
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Delete deprecated interfaces of version v1.

## HuaweiCloud SDK DevStar
 - ### Features
    - None
 - ### Bug Fix
    - Modify the credential type of DevStarClient: the correct credential type is GlobalCredentials.
 - ### Change
    - None


## 3.0.15-beta 2020-09-30
## HuaweiCloud SDK ELB
 - ### Features
    - Support Elastic Load Balance service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK EIP
 - ### Features
    - Support Elastic IP service.
 - ### Bug Fix
    - None
 - ### Change
    - None


## 3.0.14-beta 2020-09-24
## HuaweiCloud SDK BSS
 - ### Features
    - None
 - ### Bug Fix
    - Fix the problem that the class `BssClient` cannot be loaded.
 - ### Change
    - None

## HuaweiCloud SDK TestHub
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - The original service name `TestHub` has been changed to `CloudTest`, because `TestHub` couldn't be published in SDK Center successfully. 


## 3.0.13-beta 2020-09-16
## HuaweiCloud SDK ECS
 - ### Features
    - None
 - ### Bug Fix
    - Fix parameter type of interfaces.
 - ### Change
    - None

## HuaweiCloud SDK BSS
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Update interfaces.

## HuaweiCloud SDK Live
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Adjust descriptions of banned interface.


## 3.0.12-beta 2020-09-11
## HuaweiCloud SDK Meeting
 - ### Features
    - None
 - ### Bug Fix
    - Fix failed to create credentials
 - ### Change
    - None

# 3.0.11-beta 2020-09-09
## HuaweiCloud SDK DMS
 - ### Features
    - Support Distributed Message Services, provide Kafka premium instances and RabbitMQ premium instances with dedicated resources.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Meeting
 - ### Features
    - Support more APIs: Meeting Control / Meeting Management.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK VPC
 - ### Features
    - None
 - ### Bug Fix
    - Fix the problem that security group related interfaces have wrong data type.
 - ### Change
    - None


# 3.0.10-beta 2020-09-04
## HuaweiCloud SDK Core 
 - ### Features
    - None
 - ### Bug Fix
    - Fix the problem that the enumeration code cannot be generated for integer enumeration parameters without format defined in yaml.
 - ### Change
    - Modify User Agent of Http Request header.


# 3.0.9-beta 2020-08-28
## HuaweiCloud SDK Core
 - ### Features
    - None
 - ### Bug Fix
    - Solve the problem of losing innermost type when data types are nested in multiple layers.
 - ### Change
    - None

## HuaweiCloud SDK BSS
 - ### Features
    - Support Business Support System service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK CloudPipeline
 - ### Features
    - Support CloudPipeline service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK FunctionGraph
 - ### Features
    - None
 - ### Bug Fix
    - None
 - ### Change
    - Modify service name, change abbreviation FGS to full name FunctionGraph.

## HuaweiCloud SDK IAM
 - ### Features
    - Support more APIs: consistency of console related APIs.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK IoTDA
 - ### Features
    - Support more APIs: batch operation related APIs and asynchronous related APIs.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Meeting
 - ### Features
    - Support more APIs: meeting minutes related APIs.
 - ### Bug Fix
    - None
 - ### Change
    - None
    
## HuaweiCloud SDK ProjectMan
 - ### Features
    - Support Project Management service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK VPC
 - ### Features
    - Support more APIs: security group, security group rules, available IP count related APIs.
 - ### Bug Fix
    - None
 - ### Change
    - None


# 3.0.8-beta 2020-8-14
## HuaweiCloud SDK Core
 - ### Features
    - Support temporary AK/SK authentication mode.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK APIG
 - ### Features
    - Support API Gateway service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK CloudIDE
 - ### Features
    - Support Cloud IDE service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK KMS
 - ### Features
    - Support Key Management Service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK Live
 - ### Features
    - Support Live Service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK MPC
 - ### Features
    - Support Media Processing Center.
 - ### Bug Fix
    - None
 - ### Change
    - None

## HuaweiCloud SDK ServiceStage
 - ### Features
    - Support ServiceStage.
 - ### Bug Fix
    - None
 - ### Change
    - None


# __3.0.7-beta__ __2020-07-30__
## __HuaweiCloud SDK CBR__
 - ### Features
    - Support Cloud Backup and Recovery Service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## __HuaweiCloud SDK ECS__
 - ### Features
    - Publish new interfaces, such as ChangeServerOs and ResetServerPassword.
 - ### Bug Fix
    - None
 - ### Change
    - None

## __HuaweiCloud SDK VPC__
 - ### Features
    - Support interfaces of version v3.
 - ### Bug Fix
    - None
 - ### Change
    - None


# __3.0.6-beta__ __2020-07-15__
## __HuaweiCloud SDK Core__
 - ### Features
    - Support file upload and download.
 - ### Bug Fix
    - None
 - ### Change
    - None

## __Example__
 - ### Features
    - None
 - ### Bug Fix
    - [Issue #1](https://github.com/huaweicloud/huaweicloud-sdk-python-v3/issues/1): Fix test vpc example.
 - ### Change
    - None

## __HuaweiCloud SDK IAM__
  - ### Features
    - None
  - ### Bug Fix
    - Fix parsing failure of response body of interface keystoneListVersions.
  - ### Change
    - None
 
 ## __HuaweiCloud SDK IoTDA__
  - ### Features
     - None
  - ### Bug Fix
     - None
  - ### Change
     - Support related interfaces of application management.
    
## __HuaweiCloud SDK Meeting__
  - ### Features
    - Support cloud meeting management and control services.
  - ### Bug Fix
    - None
  - ### Change
    - None

## __HuaweiCloud SDK EPS__
 - ### Features
    - Support Enterprise Project Management Service.
 - ### Bug Fix
    - None
 - ### Change
    - None

## __HuaweiCloud SDK EVS__
 - ### Features
    - None
 - ### Bug Fix
    - [Issue #3](https://github.com/huaweicloud/huaweicloud-sdk-java-v3/issues/3): Fix call error of interface ShowVolume.
 - ### Change
    - None

## HuaweiCloud SDK TMS
 - ### Features
    - Support Tag Management Service.
 - ### Bug Fix
    - None
 - ### Change
    - None


# __3.0.5-beta__ __2020-6-30__
## __HuaweiCloud SDK Core__
  - ### Features
    - None
  - ### Bug Fix
    - None
  - ### Change
    - Use with_http_handler to replace with_enable_http_log to support users to customize the request log output in the troubleshooting scenario.

## __HuaweiCloud SDK CTS__
  - ### Features
    - Support Cloud Trace Service.
  - ### Bug Fix
    - None
  - ### Change
    - None
    
## __HuaweiCloud SDK EVS__
  - ### Features
    - None
  - ### Bug Fix
    - None
  - ### Change
    - Support full service interface.

## __HuaweiCloud SDK IoTDA__
  - ### Features
    - Support IoT Device Access Service.
  - ### Bug Fix
    - None
  - ### Change
    - None


# __3.0.3-beta__ __2020-06-15__
## __HuaweiCloud SDK Core__
  - ### Features
    - Support async client.
    - Support logs.
    - Support enable http logs for troubleshooting.
  - ### Bug Fix
    - None
  - ### Change
    - None
