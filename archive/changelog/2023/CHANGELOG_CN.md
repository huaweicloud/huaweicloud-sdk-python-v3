# 3.1.75 2023-12-27

### HuaweiCloud SDK AAD

- _新增特性_
  - 支持以下接口：
    - `CreateAadDomain`
    - `CreateCertificate`
    - `ModifyDomainWebSwitch`
    - `ListSourceIps`
    - `AddBlackWhiteIpList`
    - `DeleteBlackWhiteIpList`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListMetricData**
    - 响应参数变更
      - `* datapoints.timestamp: int32 -> int64`
  - **ListApisV2**
    - 请求参数变更
      - `+ return_data_mode: enum value [brief,include_group,include_group_backend]`

### HuaweiCloud SDK CodeArtsArtifact

- _新增特性_
  - 支持以下接口：
    - `BatchRestoreRepo`
    - `BatchDeleteTrashes`
    - `CreateMavenRepo`
    - `ShowProjectList`
    - `ModifyRepository`
    - `ShowRepositoryInfo`
    - `CreateDockerRepositories`
    - `DeleteRepository`
    - `ShowStorage`
    - `ShowMavenInfo`
    - `CreateProjectRelatedRepository`
    - `SearchByChecksum`
    - `SearchArtifacts`
    - `ResetUserPassword`
    - `ShowFileTree`
    - `ListArtifactoryComponent`
    - `ListAllRepositories`
    - `ShowAudit`
    - `ShowRepository`
    - `ListArtifactoryStorageStatistic`
    - `CreateAttention`
    - `ListAttentions`
    - `UpdateArtifactory`
    - `CreateArtifactory`
    - `DeleteArtifactFile`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListResourceInstances**
    - 响应参数变更
      - `+ resources.sys_tags`

### HuaweiCloud SDK DataArtsStudio

- _新增特性_
  - 支持接口`ListFactoryJobs`、`CreateFactoryJob`、`ListFactoryAlarmInfo`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`ShowInstanceSslDetail`、`UpdateSslSwitch`、`DownloadSslCert`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持接口`ShowClientNetwork`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateJob**
    - 请求参数变更
      - `+ singleNodeJobFlag`
      - `+ singleNodeJobType`
  - **ShowJob**
    - 响应参数变更
      - `+ singleNodeJobFlag`
      - `+ singleNodeJobType`
  - **UpdateJob**
    - 请求参数变更
      - `+ singleNodeJobFlag`
      - `+ singleNodeJobType`
  - **CreateSupplementdata**
    - 请求参数变更
      - `+ singleNodeJobFlag`
      - `+ singleNodeJobType`
      - `+ dependJobs.singleNodeJobFlag`
      - `+ dependJobs.singleNodeJobType`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持接口`ListJobs`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK HSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAssetStatistic**
    - 响应参数变更
      - `+ environment_num`
      - `+ core_conf_file_num`
  - **ListPorts**
    - 响应参数变更
      - `+ data_list.agent_id`
      - `+ data_list.container_id`
  - **ListSwrImageRepository**
    - 响应参数变更
      - `+ data_list.instance_name`
      - `+ data_list.instance_id`
      - `+ data_list.instance_url`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`CreateShrinkageJob`、`ShowShrinkCheckResult`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK MetaStudio

- _新增特性_
  - 支持以下接口：
    - `ListDigitalHumanVideo`
    - `ListInteractionRuleGroups`
    - `CreateInteractionRuleGroup`
    - `UpdateInteractionRuleGroup`
    - `DeleteInteractionRuleGroup`
    - `CheckTextLanguage`
    - `CreateFacialAnimations`
    - `ListFacialAnimationsData`
- _解决问题_
  - 无
- _特性变更_
  - **CreateFile**
    - 响应参数变更
      - `- file_id`
      - `- upload_url`
  - **ExecuteSmartLiveCommand**
    - 请求参数变更
      - `+ review_config`
      - `+ command: enum value [GET_CURRENT_PLAYING_SCRIPTS]`
  - **CreatePictureModelingByUrlJob**
    - 请求参数变更
      - `- X-User-Privilege`
  - **ListAssetSummary**
    - 响应参数变更
      - `+ asset_list.asset_type: enum value [AUDIO]`
  - **Create2DDigitalHumanVideo**
    - 请求参数变更
      - `+ review_config`
      - `+ callback_config`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
  - **Show2DDigitalHumanVideo**
    - 响应参数变更
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
  - **CreatePhotoDigitalHumanVideo**
    - 请求参数变更
      - `+ review_config`
      - `- video_config.disable_system_watermark`
  - **ShowPhotoDigitalHumanVideo**
    - 响应参数变更
      - `- video_config.disable_system_watermark`
  - **LiveEventReport**
    - 请求参数变更
      - `+ review_config`
  - **CreateTtsa**
    - 请求参数变更
      - `- X-User-Privilege`
      - `+ script_type`
      - `+ audio_file_download_url`
      - `+ job_type`
      - `- parent_job_id`
      - `- auto_motion`
  - **ListTtsaJobs**
    - 响应参数变更
      - `+ ttsa_jobs.job_type`
  - **ListTtsaData**
    - 响应参数变更
      - `+ start_time`
      - `+ end_time`
      - `+ is_tail`
  - **ListStyles**
    - 响应参数变更
      - `- styles.extra_meta.edit_value_items`
      - `- styles.extra_meta.edit_color_items`
      - `- styles.extra_meta.edit_components`
      - `- styles.extra_meta.modelling_algorithm`
  - **CreateDigitalHumanBusinessCard**
    - 请求参数变更
      - `+ introduction_type`
      - `+ introduction_audio_asset_id`
      - `+ review_config`
    - 响应参数变更
      - `- job_id`
  - **UpdateDigitalHumanBusinessCard**
    - 请求参数变更
      - `+ introduction_type`
      - `+ introduction_audio_asset_id`
      - `+ review_config`
    - 响应参数变更
      - `- job_id`
  - **ShowDigitalHumanBusinessCard**
    - 响应参数变更
      - `+ introduction_audio_asset_id`
      - `+ introduction_type`
  - **ShowSmartLive**
    - 响应参数变更
      - `+ stream_duration`
      - `+ block_reason`
      - `+ live_event_callback_config`
      - `+ state: enum value [BLOCKED]`
      - `+ rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **ListVideoScripts**
    - 请求参数变更
      - `+ name`
      - `+ script_catalog`
      - `+ view_mode`
    - 响应参数变更
      - `+ video_scripts.script_cover_url`
      - `+ video_scripts.script_type`
      - `+ video_scripts.text`
      - `- video_scripts.video_making_type`
      - `- video_scripts.human_image`
  - **ShowVideoScript**
    - 响应参数变更
      - `+ script_cover_url`
      - `+ review_config`
      - `- video_making_type`
      - `- human_image`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
      - `* shoot_scripts: list<ShootScriptItem> -> list<ShootScriptShowItem>`
  - **CreatePictureModelingJob**
    - 请求参数变更
      - `- X-User-Privilege`
    - 响应参数变更
      - `- model_asset_id`
      - `- job_id`
  - **ShowVideoMotionCaptureJob**
    - 响应参数变更
      - `+ input_info.rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **ShowAsset**
    - 响应参数变更
      - `+ reason`
      - `+ is_need_generate_cover`
      - `+ fail_type`
      - `+ asset_type: enum value [AUDIO]`
      - `+ system_properties.key: enum value [MATERIAL_IMG,MATERIAL_VIDEO,BUSSINESS_CARD_VIDEO,TO_BE_TRANSLATED_VIDEO]`
      - `+ files.state`
      - `+ files.reason`
      - `+ asset_extra_meta.voice_model_meta.speed_ratio`
      - `+ asset_extra_meta.voice_model_meta.volume_ratio`
      - `- asset_extra_meta.voice_model_meta.tts_mode`
      - `- asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.voice_model_meta.language: enum value [GER,fr,Kr,por,JPN,Ita,ESP,DBH,GT,GXH,HBH,SXH,SCH,YY,Russian,Filipino,Dutch,Indonesian,Vietnamese,Arabic,Turkish,Malay,Thai,Finnish]`
      - `+ asset_extra_meta.human_model_2d_meta.model_resolution`
      - `- asset_extra_meta.human_model_2d_meta.is_realtime_matting`
      - `+ asset_extra_meta.ppt_meta.error_info`
  - **UpdateDigitalAsset**
    - 请求参数变更
      - `+ is_need_generate_cover`
      - `+ review_config`
      - `+ asset_type: enum value [AUDIO]`
      - `+ system_properties.key: enum value [MATERIAL_IMG,MATERIAL_VIDEO,BUSSINESS_CARD_VIDEO,TO_BE_TRANSLATED_VIDEO]`
      - `+ asset_extra_meta.voice_model_meta.speed_ratio`
      - `+ asset_extra_meta.voice_model_meta.volume_ratio`
      - `- asset_extra_meta.voice_model_meta.tts_mode`
      - `- asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.voice_model_meta.language: enum value [GER,fr,Kr,por,JPN,Ita,ESP,DBH,GT,GXH,HBH,SXH,SCH,YY,Russian,Filipino,Dutch,Indonesian,Vietnamese,Arabic,Turkish,Malay,Thai,Finnish]`
      - `+ asset_extra_meta.human_model_2d_meta.model_resolution`
      - `- asset_extra_meta.human_model_2d_meta.is_realtime_matting`
      - `+ asset_extra_meta.ppt_meta.error_info`
    - 响应参数变更
      - `+ reason`
      - `+ is_need_generate_cover`
      - `+ fail_type`
      - `+ asset_type: enum value [AUDIO]`
      - `+ system_properties.key: enum value [MATERIAL_IMG,MATERIAL_VIDEO,BUSSINESS_CARD_VIDEO,TO_BE_TRANSLATED_VIDEO]`
      - `+ files.state`
      - `+ files.reason`
      - `+ asset_extra_meta.voice_model_meta.speed_ratio`
      - `+ asset_extra_meta.voice_model_meta.volume_ratio`
      - `- asset_extra_meta.voice_model_meta.tts_mode`
      - `- asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.voice_model_meta.language: enum value [GER,fr,Kr,por,JPN,Ita,ESP,DBH,GT,GXH,HBH,SXH,SCH,YY,Russian,Filipino,Dutch,Indonesian,Vietnamese,Arabic,Turkish,Malay,Thai,Finnish]`
      - `+ asset_extra_meta.human_model_2d_meta.model_resolution`
      - `- asset_extra_meta.human_model_2d_meta.is_realtime_matting`
      - `+ asset_extra_meta.ppt_meta.error_info`
  - **ListSmartLiveRooms**
    - 请求参数变更
      - `+ room_type`
    - 响应参数变更
      - `+ smart_live_rooms.room_type`
      - `+ smart_live_rooms.room_state`
      - `+ smart_live_rooms.error_info`
      - `+ smart_live_rooms.model_infos.backup_model_asset_ids`
  - **CreateSmartLiveRoom**
    - 请求参数变更
      - `+ stream_keys`
      - `+ backup_model_asset_ids`
      - `+ live_event_callback_config`
      - `+ review_config`
      - `+ shared_config`
      - `+ room_type: enum value [TEMPLATE]`
      - `+ play_policy.random_play_mode`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
      - `+ scene_scripts.layer_config.group_id`
      - `+ scene_scripts.layer_config.layer_type: enum value [TEXT]`
      - `+ interaction_rules.rule_index`
      - `+ interaction_rules.review_config`
      - `+ interaction_rules.trigger.layer_config`
      - `+ interaction_rules.trigger.reply_audios`
      - `+ interaction_rules.trigger.reply_mode: enum value [CALLBACK,SHOW_LAYER]`
  - **ShowSmartLiveRoom**
    - 响应参数变更
      - `+ backup_model_asset_ids`
      - `+ error_info`
      - `+ stream_keys`
      - `+ shared_config`
      - `+ live_event_callback_config`
      - `+ room_state`
      - `+ review_config`
      - `+ room_type: enum value [TEMPLATE]`
      - `+ play_policy.random_play_mode`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
      - `+ scene_scripts.layer_config.group_id`
      - `+ scene_scripts.layer_config.layer_type: enum value [TEXT]`
      - `+ interaction_rules.rule_index`
      - `+ interaction_rules.review_config`
      - `+ interaction_rules.trigger.layer_config`
      - `+ interaction_rules.trigger.reply_audios`
      - `+ interaction_rules.trigger.reply_mode: enum value [CALLBACK,SHOW_LAYER]`
  - **UpdateSmartLiveRoom**
    - 请求参数变更
      - `+ stream_keys`
      - `+ backup_model_asset_ids`
      - `+ live_event_callback_config`
      - `+ review_config`
      - `+ shared_config`
      - `+ room_type: enum value [TEMPLATE]`
      - `+ play_policy.random_play_mode`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
      - `+ scene_scripts.layer_config.group_id`
      - `+ scene_scripts.layer_config.layer_type: enum value [TEXT]`
      - `+ interaction_rules.rule_index`
      - `+ interaction_rules.review_config`
      - `+ interaction_rules.trigger.layer_config`
      - `+ interaction_rules.trigger.reply_audios`
      - `+ interaction_rules.trigger.reply_mode: enum value [CALLBACK,SHOW_LAYER]`
    - 响应参数变更
      - `+ backup_model_asset_ids`
      - `+ error_info`
      - `+ stream_keys`
      - `+ shared_config`
      - `+ live_event_callback_config`
      - `+ room_state`
      - `+ review_config`
      - `+ room_type: enum value [TEMPLATE]`
      - `+ play_policy.random_play_mode`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
      - `+ scene_scripts.layer_config.group_id`
      - `+ scene_scripts.layer_config.layer_type: enum value [TEXT]`
      - `+ interaction_rules.rule_index`
      - `+ interaction_rules.review_config`
      - `+ interaction_rules.trigger.layer_config`
      - `+ interaction_rules.trigger.reply_audios`
      - `+ interaction_rules.trigger.reply_mode: enum value [CALLBACK,SHOW_LAYER]`
  - **StartSmartLive**
    - 请求参数变更
      - `+ stream_keys`
      - `+ interaction_callback_url`
      - `+ live_event_callback_config`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
      - `+ play_policy.random_play_mode`
    - 响应参数变更
      - `+ live_warning_info`
      - `+ live_event_callback_config`
      - `+ rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **ListSmartLive**
    - 响应参数变更
      - `+ stream_duration`
      - `+ block_reason`
      - `+ live_event_callback_config`
      - `+ smart_live_jobs.live_event_callback_config`
      - `+ smart_live_jobs.stream_duration`
      - `+ smart_live_jobs.block_reason`
      - `+ smart_live_jobs.state: enum value [BLOCKED]`
      - `+ smart_live_jobs.rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **CreateVideoMotionCaptureJob**
    - 请求参数变更
      - `+ input_info.rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
    - 响应参数变更
      - `- rtc_room_info`
      - `- job_id`
      - `+ rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **ListVideoMotionCaptureJobs**
    - 响应参数变更
      - `+ video_motion_capture_jobs.input_info.rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **CreateDigitalAsset**
    - 请求参数变更
      - `+ is_need_generate_cover`
      - `+ review_config`
      - `+ asset_type: enum value [AUDIO]`
      - `+ system_properties.key: enum value [MATERIAL_IMG,MATERIAL_VIDEO,BUSSINESS_CARD_VIDEO,TO_BE_TRANSLATED_VIDEO]`
      - `+ asset_extra_meta.voice_model_meta.speed_ratio`
      - `+ asset_extra_meta.voice_model_meta.volume_ratio`
      - `- asset_extra_meta.voice_model_meta.tts_mode`
      - `- asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.voice_model_meta.language: enum value [GER,fr,Kr,por,JPN,Ita,ESP,DBH,GT,GXH,HBH,SXH,SCH,YY,Russian,Filipino,Dutch,Indonesian,Vietnamese,Arabic,Turkish,Malay,Thai,Finnish]`
      - `+ asset_extra_meta.human_model_2d_meta.model_resolution`
      - `- asset_extra_meta.human_model_2d_meta.is_realtime_matting`
      - `+ asset_extra_meta.ppt_meta.error_info`
  - **ListAssets**
    - 请求参数变更
      - `- asset_manage_type`
      - `- X-User-MePrivilege`
    - 响应参数变更
      - `+ reason`
      - `+ is_need_generate_cover`
      - `+ fail_type`
      - `+ assets.fail_type`
      - `+ assets.reason`
      - `+ assets.is_need_generate_cover`
      - `+ assets.asset_type: enum value [AUDIO]`
      - `+ assets.system_properties.key: enum value [MATERIAL_IMG,MATERIAL_VIDEO,BUSSINESS_CARD_VIDEO,TO_BE_TRANSLATED_VIDEO]`
      - `+ assets.files.state`
      - `+ assets.files.reason`
      - `+ assets.asset_extra_meta.voice_model_meta.speed_ratio`
      - `+ assets.asset_extra_meta.voice_model_meta.volume_ratio`
      - `- assets.asset_extra_meta.voice_model_meta.tts_mode`
      - `- assets.asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ assets.asset_extra_meta.voice_model_meta.language: enum value [GER,fr,Kr,por,JPN,Ita,ESP,DBH,GT,GXH,HBH,SXH,SCH,YY,Russian,Filipino,Dutch,Indonesian,Vietnamese,Arabic,Turkish,Malay,Thai,Finnish]`
      - `+ assets.asset_extra_meta.human_model_2d_meta.model_resolution`
      - `- assets.asset_extra_meta.human_model_2d_meta.is_realtime_matting`
      - `+ assets.asset_extra_meta.ppt_meta.error_info`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`SetInstancesNewDbShrink`、`StopBackup`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.74 2023-12-22

### HuaweiCloud SDK Config

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowTrackerConfig**
    - 响应参数变更
      - `+ channel.obs.bucket_prefix`
  - **CreateTrackerConfig**
    - 请求参数变更
      - `+ channel.obs.bucket_prefix`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowGroups**
    - 响应参数变更
      - `* group.group_message_offsets.lag: int32 -> int64`
  - **ShowInstanceTopicDetail**
    - 响应参数变更
      - `* partitions.replicas.lag: int32 -> int64`

# 3.1.73 2023-12-21

### HuaweiCloud SDK AS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateScalingConfig**
    - 请求参数变更
      - `+ instance_config.disk.iops`
      - `+ instance_config.disk.throughput`
      - `+ instance_config.disk.volume_type: enum value [GPSSD2,ESSD2]`
  - **ListScalingConfigs**
    - 响应参数变更
      - `+ scaling_configurations.instance_config.disk.iops`
      - `+ scaling_configurations.instance_config.disk.throughput`
      - `+ scaling_configurations.instance_config.disk.volume_type: enum value [GPSSD2,ESSD2]`
  - **ShowScalingConfig**
    - 响应参数变更
      - `+ scaling_configuration.instance_config.disk.iops`
      - `+ scaling_configuration.instance_config.disk.throughput`
      - `+ scaling_configuration.instance_config.disk.volume_type: enum value [GPSSD2,ESSD2]`

### HuaweiCloud SDK CloudPond

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListEdgeSites**
    - 响应参数变更
      - `+ edge_sites.location.zone_code`
      - `+ edge_sites.location.address`
  - **CreateEdgeSite**
    - 请求参数变更
      - `+ edge_site.location.address`
      - `+ edge_site.location.zone_code`
    - 响应参数变更
      - `+ edge_site.location.zone_code`
      - `+ edge_site.location.address`
  - **ShowEdgeSite**
    - 响应参数变更
      - `+ edge_site.location.zone_code`
      - `+ edge_site.location.address`
  - **UpdateEdgeSite**
    - 响应参数变更
      - `+ edge_site.location.zone_code`
      - `+ edge_site.location.address`

### HuaweiCloud SDK CloudTable

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateCloudTableCluster**
    - 请求参数变更
      - `+ cluster_name`
      - `+ datastore`
      - `+ availability_zone`
      - `+ nics`
      - `+ cluster_info`
      - `+ enterprise_project_id`
      - `+ vpc_id`
      - `+ dbuser`
      - `+ dbuserpwd`
      - `- cluster`
      - `* body: object<CreateClusterRequestBody> -> object<CreateClusterReqBody>`
    - 响应参数变更
      - `+ jobId`
      - `+ getJobEndpoint`
  - **CreateCluster**
    - 请求参数变更
      - `* cluster.instance.nics: list<Nics> -> list<nic>`

### HuaweiCloud SDK CodeArtsPipeline

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowPipelineRunDetail**
    - 响应参数变更
      - `* current_system_time: string -> int64`
      - `* stages.pre.endpoint_ids: string -> list<string>`

### HuaweiCloud SDK DC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateVifPeer**
    - 响应参数变更
      - `+ vif_peer.enable_nqa`
      - `+ vif_peer.enable_bfd`
  - **CreateVifPeer**
    - 响应参数变更
      - `+ vif_peer.enable_nqa`
      - `+ vif_peer.enable_bfd`
  - **ShowDirectConnect**
    - 响应参数变更
      - `+ direct_connect.signed_agreement_time`
      - `+ direct_connect.locales`
      - `+ direct_connect.support_feature`
      - `+ direct_connect.ies_id`
      - `+ direct_connect.reason`
      - `+ direct_connect.email`
      - `+ direct_connect.onestop_product_id`
      - `+ direct_connect.building_line_product_id`
      - `+ direct_connect.last_onestop_product_id`
      - `+ direct_connect.last_building_line_product_id`
      - `+ direct_connect.modified_bandwidth`
      - `+ direct_connect.change_mode`
      - `+ direct_connect.onestopdc_status`
      - `+ direct_connect.public_border_group`
      - `+ direct_connect.auto_renew`
      - `+ direct_connect.ratio_95peak`
      - `+ direct_connect.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connect.status: enum value [ORDERING,ACCEPT,REJECTED]`
  - **UpdateDirectConnect**
    - 响应参数变更
      - `+ direct_connect.signed_agreement_time`
      - `+ direct_connect.locales`
      - `+ direct_connect.support_feature`
      - `+ direct_connect.ies_id`
      - `+ direct_connect.reason`
      - `+ direct_connect.email`
      - `+ direct_connect.onestop_product_id`
      - `+ direct_connect.building_line_product_id`
      - `+ direct_connect.last_onestop_product_id`
      - `+ direct_connect.last_building_line_product_id`
      - `+ direct_connect.modified_bandwidth`
      - `+ direct_connect.change_mode`
      - `+ direct_connect.onestopdc_status`
      - `+ direct_connect.public_border_group`
      - `+ direct_connect.auto_renew`
      - `+ direct_connect.ratio_95peak`
      - `+ direct_connect.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connect.status: enum value [ORDERING,ACCEPT,REJECTED]`
  - **ListDirectConnects**
    - 响应参数变更
      - `+ direct_connects.signed_agreement_time`
      - `+ direct_connects.locales`
      - `+ direct_connects.support_feature`
      - `+ direct_connects.ies_id`
      - `+ direct_connects.reason`
      - `+ direct_connects.email`
      - `+ direct_connects.onestop_product_id`
      - `+ direct_connects.building_line_product_id`
      - `+ direct_connects.last_onestop_product_id`
      - `+ direct_connects.last_building_line_product_id`
      - `+ direct_connects.modified_bandwidth`
      - `+ direct_connects.change_mode`
      - `+ direct_connects.onestopdc_status`
      - `+ direct_connects.public_border_group`
      - `+ direct_connects.auto_renew`
      - `+ direct_connects.ratio_95peak`
      - `+ direct_connects.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connects.status: enum value [ORDERING,ACCEPT,REJECTED]`
  - **ListHostedDirectConnects**
    - 响应参数变更
      - `+ hosted_connects.port_type`
      - `+ hosted_connects.type`
      - `+ hosted_connects.status: enum value [PENDING_UPDATE,PENDING_CREATE]`
      - `- hosted_connects.status: enum value [PAID,APPLY,PENDING_SURVEY,DELETED,DENY,PENDING_PAY,ORDERING,ACCEPT,REJECTED]`
  - **CreateHostedDirectConnect**
    - 响应参数变更
      - `+ hosted_connect.port_type`
      - `+ hosted_connect.type`
      - `+ hosted_connect.status: enum value [PENDING_UPDATE,PENDING_CREATE]`
      - `- hosted_connect.status: enum value [PAID,APPLY,PENDING_SURVEY,DELETED,DENY,PENDING_PAY,ORDERING,ACCEPT,REJECTED]`
  - **ShowHostedDirectConnect**
    - 响应参数变更
      - `+ hosted_connect.port_type`
      - `+ hosted_connect.type`
      - `+ hosted_connect.status: enum value [PENDING_UPDATE,PENDING_CREATE]`
      - `- hosted_connect.status: enum value [PAID,APPLY,PENDING_SURVEY,DELETED,DENY,PENDING_PAY,ORDERING,ACCEPT,REJECTED]`
  - **UpdateHostedDirectConnect**
    - 响应参数变更
      - `+ hosted_connect.port_type`
      - `+ hosted_connect.type`
      - `+ hosted_connect.status: enum value [PENDING_UPDATE,PENDING_CREATE]`
      - `- hosted_connect.status: enum value [PAID,APPLY,PENDING_SURVEY,DELETED,DENY,PENDING_PAY,ORDERING,ACCEPT,REJECTED]`
  - **ShowVirtualGateway**
    - 响应参数变更
      - `+ virtual_gateway.device_id`
      - `+ virtual_gateway.redundant_device_id`
      - `+ virtual_gateway.public_border_group`
  - **UpdateVirtualGateway**
    - 响应参数变更
      - `+ virtual_gateway.device_id`
      - `+ virtual_gateway.redundant_device_id`
      - `+ virtual_gateway.public_border_group`
  - **ListVirtualGateways**
    - 响应参数变更
      - `+ virtual_gateways.device_id`
      - `+ virtual_gateways.redundant_device_id`
      - `+ virtual_gateways.public_border_group`
  - **CreateVirtualGateway**
    - 响应参数变更
      - `+ virtual_gateway.device_id`
      - `+ virtual_gateway.redundant_device_id`
      - `+ virtual_gateway.public_border_group`
  - **ShowVirtualInterface**
    - 响应参数变更
      - `+ virtual_interface.local_gateway_v4_ip`
      - `+ virtual_interface.remote_gateway_v4_ip`
      - `+ virtual_interface.ies_id`
      - `+ virtual_interface.reason`
      - `+ virtual_interface.rate_limit`
      - `+ virtual_interface.address_family`
      - `+ virtual_interface.local_gateway_v6_ip`
      - `+ virtual_interface.remote_gateway_v6_ip`
      - `+ virtual_interface.lgw_id`
      - `+ virtual_interface.gateway_id`
      - `+ virtual_interface.remote_ep_group`
      - `+ virtual_interface.service_ep_group`
      - `+ virtual_interface.bgp_route_limit`
      - `+ virtual_interface.priority`
      - `+ virtual_interface.vif_peers.enable_nqa`
      - `+ virtual_interface.vif_peers.enable_bfd`
  - **UpdateVirtualInterface**
    - 响应参数变更
      - `+ virtual_interface.local_gateway_v4_ip`
      - `+ virtual_interface.remote_gateway_v4_ip`
      - `+ virtual_interface.ies_id`
      - `+ virtual_interface.reason`
      - `+ virtual_interface.rate_limit`
      - `+ virtual_interface.address_family`
      - `+ virtual_interface.local_gateway_v6_ip`
      - `+ virtual_interface.remote_gateway_v6_ip`
      - `+ virtual_interface.lgw_id`
      - `+ virtual_interface.gateway_id`
      - `+ virtual_interface.remote_ep_group`
      - `+ virtual_interface.service_ep_group`
      - `+ virtual_interface.bgp_route_limit`
      - `+ virtual_interface.priority`
      - `+ virtual_interface.vif_peers.enable_nqa`
      - `+ virtual_interface.vif_peers.enable_bfd`
  - **ListVirtualInterfaces**
    - 响应参数变更
      - `+ virtual_interfaces.local_gateway_v4_ip`
      - `+ virtual_interfaces.remote_gateway_v4_ip`
      - `+ virtual_interfaces.ies_id`
      - `+ virtual_interfaces.reason`
      - `+ virtual_interfaces.rate_limit`
      - `+ virtual_interfaces.address_family`
      - `+ virtual_interfaces.local_gateway_v6_ip`
      - `+ virtual_interfaces.remote_gateway_v6_ip`
      - `+ virtual_interfaces.lgw_id`
      - `+ virtual_interfaces.gateway_id`
      - `+ virtual_interfaces.remote_ep_group`
      - `+ virtual_interfaces.service_ep_group`
      - `+ virtual_interfaces.bgp_route_limit`
      - `+ virtual_interfaces.priority`
      - `+ virtual_interfaces.vif_peers.enable_nqa`
      - `+ virtual_interfaces.vif_peers.enable_bfd`
  - **CreateVirtualInterface**
    - 响应参数变更
      - `+ virtual_interface.local_gateway_v4_ip`
      - `+ virtual_interface.remote_gateway_v4_ip`
      - `+ virtual_interface.ies_id`
      - `+ virtual_interface.reason`
      - `+ virtual_interface.rate_limit`
      - `+ virtual_interface.address_family`
      - `+ virtual_interface.local_gateway_v6_ip`
      - `+ virtual_interface.remote_gateway_v6_ip`
      - `+ virtual_interface.lgw_id`
      - `+ virtual_interface.gateway_id`
      - `+ virtual_interface.remote_ep_group`
      - `+ virtual_interface.service_ep_group`
      - `+ virtual_interface.bgp_route_limit`
      - `+ virtual_interface.priority`
      - `+ virtual_interface.vif_peers.enable_nqa`
      - `+ virtual_interface.vif_peers.enable_bfd`

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`ValidateDeletableReplica`
- _解决问题_
  - 无
- _特性变更_
  - **ShowExpireKeyScanInfo**
    - 请求参数变更
      - `+ offset`
      - `+ limit`
      - `+ status`

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateJob**
    - 请求参数变更
      - `+ nodes.execTimeOutRetry`
  - **ShowJob**
    - 响应参数变更
      - `+ nodes.execTimeOutRetry`
  - **UpdateJob**
    - 请求参数变更
      - `+ nodes.execTimeOutRetry`
  - **CreateSupplementdata**
    - 请求参数变更
      - `+ dependJobs.nodes.execTimeOutRetry`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BatchCreateJobs**
    - 请求参数变更
      - `+ jobs.engine_type: enum value [mysql-to-kafka,taurus-to-kafka,gaussdbv5ha-to-kafka]`
      - `+ jobs.source_endpoint.db_type: enum value [taurus]`
  - **BatchValidateConnections**
    - 请求参数变更
      - `+ jobs.db_type: enum value [taurus]`
  - **ShowJobList**
    - 请求参数变更
      - `+ engine_type: enum value [gaussdbv5,postgresql,mysql-to-kafka,taurus-to-kafka,gaussdbv5ha-to-kafka]`
  - **BatchUpdateJob**
    - 请求参数变更
      - `+ jobs.engine_type: enum value [gaussdbv5,postgresql,mysql-to-kafka,taurus-to-kafka,gaussdbv5ha-to-kafka]`
      - `+ jobs.source_endpoint.db_type: enum value [taurus]`
  - **BatchListJobDetails**
    - 响应参数变更
      - `+ results.source_endpoint.db_type: enum value [taurus]`
      - `+ results.inst_info.engine_type: enum value [gaussdbv5,postgresql,mysql-to-kafka,taurus-to-kafka,gaussdbv5ha-to-kafka]`
  - **ShowJobDetail**
    - 请求参数变更
      - `+ type: enum value [compare]`
      - `+ type: enum value [comapre]`
      - `+ query_type: enum value [diff]`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BatchCreateServerTags**
    - 请求参数变更
      - `* tags: list<ServerTag> -> list<BatchAddServerTag>`
  - **UpdateServer**
    - 请求参数变更
      - `+ server.user_data`

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`UpdateDisassociatePublicip`、`UpdateAssociatePublicip`

### HuaweiCloud SDK HSS

- _新增特性_
  - 支持以下接口：
    - `ListProcessesHost`
    - `ListPortHost`
    - `ChangeCheckRuleAction`
    - `ListVulScanTask`
    - `CreateVulnerabilityScanTask`
    - `ListVulScanTaskHost`
- _解决问题_
  - 无
- _特性变更_
  - **ShowAssetStatistic**
    - 请求参数变更
      - `+ category`
    - 响应参数变更
      - `+ web_app_num`
      - `+ database_num`
      - `+ web_service_num`
  - **ChangeVulScanPolicy**
    - 请求参数变更
      - `+ scan_vul_types`
  - **ListJarPackageHostInfo**
    - 请求参数变更
      - `+ part_match`
  - **ListUserStatistics**
    - 请求参数变更
      - `+ category`
  - **ListPortStatistics**
    - 请求参数变更
      - `+ category`
  - **ListProcessStatistics**
    - 请求参数变更
      - `+ category`
  - **ListAppStatistics**
    - 请求参数变更
      - `+ category`
  - **ListUsers**
    - 请求参数变更
      - `+ category`
      - `+ part_match`
    - 响应参数变更
      - `+ data_list.container_id`
      - `+ data_list.container_name`
  - **ListPorts**
    - 请求参数变更
      - `+ category`
  - **ListApps**
    - 请求参数变更
      - `+ category`
      - `+ part_match`
    - 响应参数变更
      - `+ data_list.container_id`
      - `+ data_list.container_name`
  - **ListAutoLaunchs**
    - 请求参数变更
      - `+ part_match`
  - **ListProtectionServer**
    - 响应参数变更
      - `+ data_list.agent_version`
  - **ListContainerNodes**
    - 请求参数变更
      - `+ container_tags`
    - 响应参数变更
      - `+ data_list.protect_interrupt`
      - `+ data_list.container_tags`
      - `+ data_list.private_ip`
      - `+ data_list.public_ip`
      - `+ data_list.resource_id`
      - `+ data_list.group_name`
      - `+ data_list.enterprise_project_name`
      - `+ data_list.detect_result`
      - `+ data_list.asset`
      - `+ data_list.vulnerability`
      - `+ data_list.intrusion`
      - `+ data_list.policy_group_id`
      - `+ data_list.policy_group_name`
  - **ListHostStatus**
    - 响应参数变更
      - `+ data_list.expire_time`
      - `+ data_list.protect_interrupt`
  - **BatchScanSwrImage**
    - 请求参数变更
      - `+ image_size`
      - `+ start_latest_update_time`
      - `+ end_latest_update_time`
      - `+ start_latest_scan_time`
      - `+ end_latest_scan_time`
      - `+ image_info_list.instance_id`
      - `+ image_info_list.instance_url`
  - **ListImageVulnerabilities**
    - 请求参数变更
      - `+ type`
    - 响应参数变更
      - `+ data_list.app_path`
  - **ListImageRiskConfigs**
    - 请求参数变更
      - `+ instance_id`
  - **ListImageRiskConfigRules**
    - 请求参数变更
      - `+ instance_id`
  - **ShowImageCheckRuleDetail**
    - 请求参数变更
      - `+ instance_id`
  - **ListAlarmWhiteList**
    - 响应参数变更
      - `+ data_list.white_field`
      - `+ data_list.field_value`
      - `+ data_list.judge_type`
  - **ListSwrImageRepository**
    - 请求参数变更
      - `+ instance_name`
      - `+ image_size`
      - `+ start_latest_update_time`
      - `+ end_latest_update_time`
      - `+ start_latest_scan_time`
      - `+ end_latest_scan_time`
      - `+ has_malicious_file`
      - `+ has_unsafe_setting`
      - `+ has_vul`
      - `+ instance_id`
    - 响应参数变更
      - `+ data_list.scan_failed_desc`
  - **ListSecurityEvents**
    - 请求参数变更
      - `+ public_ip`
      - `+ event_name`
    - 响应参数变更
      - `+ data_list.event_count`
  - **ChangeEvent**
    - 请求参数变更
      - `+ event_white_rule_list`

### HuaweiCloud SDK IEC

- _新增特性_
  - 支持接口`ListBandwidthTypes`、`CreateSubnet`、`CreateInstance`
- _解决问题_
  - 无
- _特性变更_
  - **ListSubnets**
    - 响应参数变更
      - `+ subnets.cidr_v6`
      - `+ subnets.ipv6_enable`
      - `+ subnets.pool_id`
      - `+ subnets.neutron_subnet_id_v6`
      - `+ subnets.gateway_ip_v6`
  - **ShowSubnet**
    - 响应参数变更
      - `+ subnet.cidr_v6`
      - `+ subnet.ipv6_enable`
      - `+ subnet.pool_id`
      - `+ subnet.neutron_subnet_id_v6`
      - `+ subnet.gateway_ip_v6`
  - **UpdateSubnet**
    - 请求参数变更
      - `+ subnet.ipv6_enable`
      - `+ subnet.pool_id`
    - 响应参数变更
      - `+ subnet.ipv6_enable`
      - `+ subnet.neutron_subnet_id_v6`
  - **CreateSecurityGroupRule**
    - 请求参数变更
      - `+ security_group_rule.ethertype: enum value [IPv6]`
  - **ListPorts**
    - 响应参数变更
      - `+ ports.ipv6_bandwidth_id`
      - `+ ports.binding:profile`
  - **CreatePort**
    - 响应参数变更
      - `+ port.ipv6_bandwidth_id`
      - `+ port.binding:profile`
  - **ShowPort**
    - 响应参数变更
      - `+ port.ipv6_bandwidth_id`
      - `+ port.binding:profile`
  - **UpdatePort**
    - 响应参数变更
      - `+ port.ipv6_bandwidth_id`
      - `+ port.binding:profile`
  - **CreatePublicIp**
    - 请求参数变更
      - `+ bandwidth`
  - **ShowEdgeCloud**
    - 响应参数变更
      - `+ stacks.resources.net_config.allowed_address_pairs`
      - `+ coverage.coverage_sites.demands.pool_id_v6`
      - `+ coverage.coverage_sites.demands.ipv6_bandwidth_enable`
  - **ListEdgeCloud**
    - 响应参数变更
      - `+ edgeclouds.coverage.coverage_sites.demands.pool_id_v6`
      - `+ edgeclouds.coverage.coverage_sites.demands.ipv6_bandwidth_enable`
  - **CreateDeployment**
    - 请求参数变更
      - `+ edgecloud.coverage.coverage_sites.demands.bandwidth_type`
      - `+ edgecloud.coverage.coverage_sites.demands.pool_id_v6`
      - `+ edgecloud.coverage.coverage_sites.demands.ipv6_bandwidth_enable`
      - `+ edgecloud.coverage.coverage_sites.demands.ipv6_bandwidth_type`
      - `+ edgecloud.stack.resources.net_config.allowed_address_pairs`
    - 响应参数变更
      - `+ locations.ipv6_enable`
      - `+ locations.ipv6_bandwidth_enable`
      - `+ locations.pool_id_v6`
  - **ListDeployments**
    - 响应参数变更
      - `+ deployments.distribution.ipv6_enable`
      - `+ deployments.distribution.ipv6_bandwidth_enable`
      - `+ deployments.distribution.pool_id_v6`
      - `+ deployments.edgecloud.stacks.resources.net_config.allowed_address_pairs`
      - `+ deployments.edgecloud.coverage.coverage_sites.demands.bandwidth_type`
      - `+ deployments.edgecloud.coverage.coverage_sites.demands.pool_id_v6`
      - `+ deployments.edgecloud.coverage.coverage_sites.demands.ipv6_bandwidth_enable`
      - `+ deployments.edgecloud.coverage.coverage_sites.demands.ipv6_bandwidth_type`

### HuaweiCloud SDK IVS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **DetectStandardByNameAndId**
    - 请求参数变更
      - `+ data.req_data.detail`
      - `+ data.req_data.crop`
  - **DetectStandardByIdCardImage**
    - 请求参数变更
      - `+ data.req_data.detail`
      - `+ data.req_data.crop`
  - **DetectStandardByVideoAndIdCardImage**
    - 请求参数变更
      - `+ data.req_data.detail`
  - **DetectStandardByVideoAndNameAndId**
    - 请求参数变更
      - `+ data.req_data.detail`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`SendKafkaMessage`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`CreatePartition`
  - **UpdateInstanceTopic**
    - 请求参数变更
      - `+ topics.new_partition_brokers`
  - **ListInstanceConsumerGroups**
    - 响应参数变更
      - `* groups.lag: int32 -> int64`
  - **ListInstances**
    - 请求参数变更
      - `+ status: enum value [UPGRADING,UPGRADINGFAILED]`

### HuaweiCloud SDK MPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateTranscodingTask**
    - 请求参数变更
      - `+ video_process.hls_storage_type`

### HuaweiCloud SDK SFSTurbo

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListFsTasks**
    - 响应参数变更
      - `* tasks: list<object> -> list<OneFsTaskResp>`
  - **ShowShare**
    - 响应参数变更
      - `+ tags`
      - `+ enterprise_project_id`
  - **DeleteBackendTarget**
    - 响应参数变更
      - `+ lifecycle: enum value [FAILED]`
  - **CreateShare**
    - 请求参数变更
      - `+ share.tags`
  - **ListShares**
    - 响应参数变更
      - `+ tags`
      - `+ enterprise_project_id`
      - `+ shares.enterprise_project_id`
      - `+ shares.tags`

### HuaweiCloud SDK TICS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAgentDetail**
    - 响应参数变更
      - `* agent_deploy.aom_flag: byte -> boolean`
      - `* agent_deploy.bcs_flag: byte -> boolean`
      - `* agent_deploy.high_avail: byte -> boolean`
      - `+ agent_deploy_detail.ief_instance_id`
      - `+ agent_deploy_node.agent_vpcep_eps_id`
      - `+ agent_deploy_node.league_server_ip_security_group_rule`
      - `+ agent_deploy_node.league_server_snat_ip`
      - `+ agent_deploy_node.server_to_agent_vpcep_epi_id`
      - `+ agent_deploy_node.server_to_agent_vpcep_epi_ip`
      - `+ agent_deploy_node.snat_rule_id`

### HuaweiCloud SDK VOD

- _新增特性_
  - 支持接口`ListAssetDailySummaryLog`、`UpdateStorageMode`、`ShowVodRetrieval`
- _解决问题_
  - 无
- _特性变更_
  - **ShowTakeOverAssetDetails**
    - 响应参数变更
      - `+ transcode_info.output.group_id`
      - `+ transcode_info.output.group_name`
  - **PublishAssets**
    - 响应参数变更
      - `+ asset_info_array.is_multi_transcode`
      - `+ asset_info_array.play_info_array.group_id`
      - `+ asset_info_array.play_info_array.group_name`
  - **UnpublishAssets**
    - 响应参数变更
      - `+ asset_info_array.is_multi_transcode`
      - `+ asset_info_array.play_info_array.group_id`
      - `+ asset_info_array.play_info_array.group_name`
  - **ShowAssetMeta**
    - 响应参数变更
      - `+ asset_info_array.is_multi_transcode`
      - `+ asset_info_array.play_info_array.group_id`
      - `+ asset_info_array.play_info_array.group_name`
  - **ShowAssetDetail**
    - 响应参数变更
      - `+ transcode_info.output.group_id`
      - `+ transcode_info.output.group_name`
  - **ShowTakeOverTaskDetails**
    - 响应参数变更
      - `+ assets.transcode_info.output.group_id`
      - `+ assets.transcode_info.output.group_name`

# 3.1.72 2023-12-14

### HuaweiCloud SDK BMS

- _新增特性_
  - 支持接口`DeleteBaremetalServer`
- _解决问题_
  - 无
- _特性变更_
  - **CreateBareMetalServers**
    - 请求参数变更
      - `+ server.root_volume.volumetype: enum value [GPSSD]`
      - `+ server.data_volumes.volumetype: enum value [GPSSD]`

### HuaweiCloud SDK CAE

- _新增特性_
  - 支持接口`ShowMonitorSystem`、`CreateMonitorSystem`、`UpdateMonitorSystem`
- _解决问题_
  - 无
- _特性变更_
  - **ListComponentConfigurations**
    - 响应参数变更
      - `+ items.data.spec.instrumentation`
      - `+ items.data.spec.apm_application`
      - `+ items.data.spec.type`
      - `+ items.data.spec.app_name`
      - `+ items.data.spec.instance_name`
      - `+ items.data.spec.env_name`
      - `- items.data.spec.image_pull_policy: enum value [Always,IfNotPresent]`
  - **CreateComponentConfiguration**
    - 请求参数变更
      - `+ items.data.spec.instrumentation`
      - `+ items.data.spec.apm_application`
      - `+ items.data.spec.type`
      - `+ items.data.spec.app_name`
      - `+ items.data.spec.instance_name`
      - `+ items.data.spec.env_name`
      - `- items.data.spec.image_pull_policy: enum value [Always,IfNotPresent]`

### HuaweiCloud SDK CES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListAlarmTemplates**
    - 请求参数变更
      - `+ template_type: enum value [system_event,custom_event,system_custom_event]`
  - **CreateAlarmTemplate**
    - 请求参数变更
      - `+ template_type`
      - `+ policies.period: enum value [0]`
  - **UpdateAlarmTemplate**
    - 请求参数变更
      - `+ policies.period: enum value [0]`

### HuaweiCloud SDK CFW

- _新增特性_
  - 支持接口`CreateFirewall`、`ListJob`、`DeleteFirewall`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CloudTable

- _新增特性_
  - 支持接口`CreateCloudTableCluster`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CodeArtsPipeline

- _新增特性_
  - 支持接口`ShowPipelineDetail`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Config

- _新增特性_
  - 支持以下接口：
    - `ListTrackedResources`
    - `CountTrackedResources`
    - `ListTrackedResourceTags`
    - `CollectTrackedResourcesSummary`
    - `ShowTrackedResourceDetail`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持接口`DeleteRouteFromEnhancedConnection`、`CreateRouteToEnhancedConnection`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持以下接口：
    - `ListLogicalClusterVolumes`
    - `ResizeClusterWithExistedNodes`
    - `RestartLogicalCluster`
    - `ListTopoRings`
    - `UpdateLogicalCluster`
    - `DeleteLogicalCluster`
    - `EnableLogicalCluster`
    - `ListClusterNodes`
    - `ConvertToLogicalCluster`
    - `RestoreRedistribution`
    - `StopRedistribution`
    - `ListLogicalClusterTasks`
    - `ListLogicalClusters`
    - `CreateLogicalCluster`
    - `DeleteClusterNodes`
    - `ListLogicalClusterRings`
    - `ListLtsLogs`
    - `ListQueries`
    - `ListTablesStatistic`
    - `ShowQueryDetail`
    - `DisableLtsLogs`
    - `EnableLtsLogs`
- _解决问题_
  - 无
- _特性变更_
  - **ListHostDisk**
    - 请求参数变更
      - `+ instance_id`
    - 响应参数变更
      - `+ instance_id`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowResInstanceInfo**
    - 响应参数变更
      - `+ resources.resource_detail.detailId`
      - `- resources.resource_detail.resource_id`
      - `- resources.resource_detail.func_urn`
      - `- resources.resource_detail.func_name`
      - `- resources.resource_detail.domain_id`
      - `- resources.resource_detail.namespace`
      - `- resources.resource_detail.project_name`
      - `- resources.resource_detail.package`
      - `- resources.resource_detail.runtime`
      - `- resources.resource_detail.timeout`
      - `- resources.resource_detail.handler`
      - `- resources.resource_detail.memory_size`
      - `- resources.resource_detail.gpu_memory`
      - `- resources.resource_detail.cpu`
      - `- resources.resource_detail.code_type`
      - `- resources.resource_detail.code_url`
      - `- resources.resource_detail.code_filename`
      - `- resources.resource_detail.code_size`
      - `- resources.resource_detail.user_data`
      - `- resources.resource_detail.encrypted_user_data`
      - `- resources.resource_detail.digest`
      - `- resources.resource_detail.version`
      - `- resources.resource_detail.image_name`
      - `- resources.resource_detail.xrole`
      - `- resources.resource_detail.app_xrole`
      - `- resources.resource_detail.description`
      - `- resources.resource_detail.last_modified`
      - `- resources.resource_detail.func_vpc_id`
      - `- resources.resource_detail.strategy_config`
      - `- resources.resource_detail.extend_config`
      - `- resources.resource_detail.initializer_handler`
      - `- resources.resource_detail.initializer_timeout`
      - `- resources.resource_detail.pre_stop_handler`
      - `- resources.resource_detail.pre_stop_timeout`
      - `- resources.resource_detail.enterprise_project_id`
      - `- resources.resource_detail.long_time`
      - `- resources.resource_detail.log_group_id`
      - `- resources.resource_detail.log_stream_id`
      - `- resources.resource_detail.type`
      - `- resources.resource_detail.fail_count`
      - `- resources.resource_detail.is_bridge_function`
      - `- resources.resource_detail.bind_bridge_funcUrns`
      - `* resources.resource_detail: object<ListFunctionResult> -> object<ListEnterpriseResourceDetail>`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateAsyncCommand**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **ShowAsyncDeviceCommand**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **BroadcastMessage**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **CreateCommand**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **ListProperties**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
    - 响应参数变更
      - `+ request_id`
  - **UpdateProperties**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
    - 响应参数变更
      - `+ request_id`
  - **CloseDeviceTunnel**
    - 请求参数变更
      - `+ Sp-Auth-Token`
  - **DeleteDeviceTunnel**
    - 请求参数变更
      - `+ Sp-Auth-Token`
  - **ShowDeviceTunnel**
    - 请求参数变更
      - `+ Sp-Auth-Token`
  - **AddTunnel**
    - 请求参数变更
      - `+ Sp-Auth-Token`
  - **ListDeviceTunnels**
    - 请求参数变更
      - `+ Sp-Auth-Token`
  - **ShowDeviceMessage**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **CreateMessage**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **ListDeviceMessages**
    - 请求参数变更
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`

### HuaweiCloud SDK Live

- _新增特性_
  - 支持以下接口：
    - `ListDelayConfig`
    - `UpdateDelayConfig`
    - `ShowPullSourcesConfig`
    - `UpdatePullSourcesConfig`
    - `ListGeoBlockingConfig`
    - `UpdateGeoBlockingConfig`
    - `CreateUrlAuthchain`
    - `ListIpAuthList`
    - `UpdateIpAuthList`
    - `ListPublishTemplate`
    - `UpdatePublishTemplate`
    - `DeletePublishTemplate`
- _解决问题_
  - 无
- _特性变更_
  - **ListRecordContents**
    - 请求参数变更
      - `+ record_type: enum value [PLAN_RECORD,ON_DEMAND_RECORD]`
    - 响应参数变更
      - `- record_contents.record_type: enum value [PLAN_RECORD,ON_DEMAND_RECORD]`

### HuaweiCloud SDK LTS

- _新增特性_
  - 支持接口`CreateAgencyAccess`
- _解决问题_
  - 无
- _特性变更_
  - **ListSqlAlarmRules**
    - 响应参数变更
      - `+ sql_alarm_rules.is_css_sql`
      - `+ sql_alarm_rules.notification_frequency`
      - `+ sql_alarm_rules.alarm_action_rule_name`
      - `+ sql_alarm_rules.status: enum value [RUNNING 启用,STOPPING 停止]`
      - `- sql_alarm_rules.status: enum value [RUNNING,STOPPING]`
      - `* sql_alarm_rules.frequency: object<Frequency> -> object<FrequencyRespBody>`
  - **UpdateSqlAlarmRule**
    - 请求参数变更
      - `+ is_css_sql`
      - `+ notification_frequency`
      - `+ alarm_action_rule_name`
      - `* frequency: object<Frequency> -> object<CreateSqlAlarmRuleFrequency>`
    - 响应参数变更
      - `+ is_css_sql`
      - `+ alarm_action_rule_name`
      - `+ notification_frequency`
      - `+ language: enum value [zh-cn,en-us]`
      - `* frequency: object<Frequency> -> object<FrequencyRespBody>`
  - **CreateSqlAlarmRule**
    - 请求参数变更
      - `+ is_css_sql`
      - `+ notification_frequency`
      - `+ alarm_action_rule_name`
      - `* frequency: object<Frequency> -> object<CreateSqlAlarmRuleFrequency>`
  - **ListKeywordsAlarmRules**
    - 响应参数变更
      - `+ keywords_alarm_rules.notification_frequency`
      - `+ keywords_alarm_rules.alarm_action_rule_name`
      - `+ keywords_alarm_rules.status: enum value [RUNNING  启用,STOPPING  停止]`
      - `- keywords_alarm_rules.status: enum value [RUNNING,STOPPING]`
  - **UpdateKeywordsAlarmRule**
    - 请求参数变更
      - `+ notification_frequency`
      - `+ alarm_action_rule_name`
    - 响应参数变更
      - `+ alarm_action_rule_name`
      - `+ notification_frequency`
      - `+ language: enum value [zh-cn,en-us]`
      - `- keywords_requests.search_time_range_unit: enum value [minute]`
      - `* keywords_requests: list<KeywordsRequest> -> list<KeywordsResBody>`
      - `* frequency: object<Frequency> -> object<FrequencyRespBody>`
  - **CreateKeywordsAlarmRule**
    - 请求参数变更
      - `+ notification_frequency`
      - `+ alarm_action_rule_name`
      - `+ keywords_alarm_level: enum value [Critical]`
      - `- keywords_alarm_level: enum value [CRITICAL]`

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`ShowMrsVersionMetadata`、`SwitchClusterTags`、`ShowTagStatus`、`ShowTagQuota`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK NAT

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateNatGatewayTag**
    - 请求参数变更
      - `+ tag.key`
      - `+ tag.value`
      - `* tag: object -> object<TagBody>`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListLogLtsConfigs`、`SetLogLtsConfigs`、`DeleteLogLtsConfigs`
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
  - **CreateRocketMqMigrationTask**
    - 请求参数变更
      - `+ topicConfigTable`
      - `+ subscriptionGroupTable`
      - `+ vhosts`
      - `+ queues`
      - `+ exchanges`
      - `+ bindings`
      - `* body: map<string, object> -> object<CreateRocketMqMigrationTaskReq>`

### HuaweiCloud SDK SecMaster

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListAlerts**
    - 请求参数变更
      - `* condition.conditions.data: list<object> -> list<string>`
      - `* condition.logics: list<object> -> list<string>`
  - **ListIncidents**
    - 请求参数变更
      - `* condition.conditions.data: list<object> -> list<string>`
      - `* condition.logics: list<object> -> list<string>`
  - **ListIndicators**
    - 请求参数变更
      - `* condition: string -> object`
  - **ListDataobjectRelations**
    - 请求参数变更
      - `* condition.conditions.data: list<object> -> list<string>`
      - `* condition.logics: list<object> -> list<string>`

### HuaweiCloud SDK SMS

- _新增特性_
  - 支持接口`ShowConsistencyResult`、`UpdateConsistencyResult`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateTaskStatus**
    - 请求参数变更
      - `+ is_need_consistency_check`
  - **ListServers**
    - 请求参数变更
      - `+ is_consistency_result_exist`
    - 响应参数变更
      - `+ source_servers.is_consistency_result_exist`

# 3.1.71 2023-12-07

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持接口`DeleteStackInstance`
- _解决问题_
  - 无
- _特性变更_
  - **ListStackSetOperations**
    - 响应参数变更
      - `+ stack_set_operations.action: enum value [UPDATE_STACK_INSTANCES]`
  - **ShowStackSetOperationMetadata**
    - 响应参数变更
      - `+ action: enum value [UPDATE_STACK_INSTANCES]`

### HuaweiCloud SDK APIG

- _新增特性_
  - 支持接口`CheckApiGroupsV2`
- _解决问题_
  - 无
- _特性变更_
  - **CreatePrepayResize**
    - 请求参数变更
      - `+ instance_id`
  - **ListPluginAttachableApis**
    - 请求参数变更
      - `* env_id: optional -> required`
  - **ListApisV2**
    - 请求参数变更
      - `+ return_data_mode`

### HuaweiCloud SDK CBH

- _新增特性_
  - 支持接口`LoginCbh`
- _解决问题_
  - 无
- _特性变更_
  - **ShowAvailableZoneInfo**
    - 响应参数变更
      - `* availability_zone: object<AvailabilityZones> -> list<AvailabilityZones>`

### HuaweiCloud SDK Cloudtest

- _新增特性_
  - 支持接口`ShowProjectDataDashboard`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CodeArtsPipeline

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowPipelineLog**
    - 请求参数变更
      - `- level`
      - `- job_run_id`

### HuaweiCloud SDK DataArtsStudio

- _新增特性_
  - 支持以下接口：
    - `SetFactoryJobTags`
    - `ListSecurityPermissionSets`
    - `CreateSecurityPermissionSet`
    - `ShowSecurityPermissionSet`
    - `UpdateSecurityPermissionSet`
    - `DeleteSecurityPermissionSet`
    - `ListSecurityPermissionSetMembers`
    - `CreateSecurityPermissionSetMember`
    - `BatchDeleteSecurityPermissionSetMembers`
    - `ListSecurityPermissionSetPermissions`
    - `CreateSecurityPermissionSetPermission`
    - `BatchDeleteSecurityPermissionSetPermissions`
    - `UpdateSecurityPermissionSetPermission`
    - `ListSecurityDataClassificationRules`
    - `CreateSecurityDataClassificationRule`
    - `ShowSecurityDataClassificationRule`
    - `UpdateSecurityDataClassificationRule`
    - `DeleteSecurityDataClassificationRule`
    - `BatchDeleteSecurityDataClassificationRule`
    - `UpdateSecurityRuleEnableStatus`
    - `ListSecurityDataClassificationRuleGroups`
    - `ShowSecurityDataClassificationRuleGroup`
- _解决问题_
  - 无
- _特性变更_
  - **DeleteApi**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **PublishApi**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowApplyDetail**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowMessageDetail**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowCatalogDetail**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **UpdateCatalog**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **CreateServiceCatalog**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **DeleteServiceCatalog**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **MigrateCatalog**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **MigrateApi**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **SearchIdByPath**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowPathById**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **PublishApiToInstance**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ExecuteApiToInstance**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **AuthorizeApiToInstance**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **AuthorizeActionApiToInstance**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **DeleteApp**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowAppInfo**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **UpdateApp**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowApisOverview**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowAppsOverview**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowApisDetail**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowAppsDetail**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **UpdateFactoryJobName**
    - 请求参数变更
      - `- x-Auth-Token`
  - **BatchApproveApply**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListApply**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ConfirmMessage**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListMessage**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListAllCatalogList**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListCatalogList**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowPathObjectById**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **DebugApi**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **SearchPublishInfo**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListInstanceList**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **SearchDebugInfo**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListApicInstances**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListApicGroups**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **CreateApp**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListApps**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListApisTop**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListAppsTop**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowApisDashboard**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowApiDashboard**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowAppsDashboard**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListApiTopN**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListApis**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **CreateApi**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ShowApi**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **UpdateApi**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **ListApiCatalogList**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **SearchAuthorizeApp**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`
  - **SearchBindApi**
    - 请求参数变更
      - `* Dlm-Type: required -> optional`

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowJobInstance**
    - 响应参数变更
      - `* planTime: int32 -> int64`
      - `* startTime: int32 -> int64`
      - `* endTime: int32 -> int64`
      - `* executeTime: int32 -> int64`
      - `* nodes.planTime: int32 -> int64`
      - `* nodes.startTime: int32 -> int64`
      - `* nodes.endTime: int32 -> int64`
      - `* nodes.executeTime: int32 -> int64`
  - **ListJobs**
    - 请求参数变更
      - `+ tags`

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持接口`ListJobAuthInfos`、`UpdateJobAuthInfo`、`CreateJobAuthInfo`、`DeleteJobAuthInfo`
- _解决问题_
  - 无
- _特性变更_
  - 废弃以下接口：
    - `ShowDliAgency`
    - `CreateDliAgency`
    - `DeleteResource`
    - `ShowResourceInfo`
    - `UpdateGroupOrResourceOwner`
    - `ShowBatchLog`
    - `ExportTable`
    - `ImportTable`
    - `ExportSqlJobResult`
    - `UpdateDatabaseOwner`
    - `DeleteDatabase`
    - `RegisterAuthorizedQueue`
    - `UpdateTableOwner`
    - `ShowTableContent`
    - `UpdateQueueCidr`
    - `BatchDeleteQueuePlans`
    - `ChangeQueuePlan`
    - `DeleteQueuePlan`
    - `DeleteAuthInfo`
    - `DeleteEnhancedConnectionRoutes`
    - `CreateEnhancedConnectionRoutes`
    - `RegisterBucket`
    - `CreateIefMessageChannel`
    - `UploadFiles`
    - `UploadPythonFiles`
    - `ListResources`
    - `UploadResources`
    - `UploadJars`
    - `ListDatabases`
    - `CreateDatabase`
    - `ListTableUsers`
    - `ChangeAuthorization`
    - `ListTablePrivileges`
    - `ListDatabaseUsers`
    - `ListQueueUsers`
    - `ListAllTables`
    - `CreateTable`
    - `DeleteTable`
    - `ShowDescribeTable`
    - `CreateQueuePlan`
    - `ListQueuePlans`
    - `UpdateAuthInfo`
    - `CreateAuthInfo`
    - `ListAuthInfo`
    - `ChangeFlinkJobStatusReport`
    - `RunIefJobActionCallBack`
    - `CreateIefSystemEvents`
    - `ListDatasourceConnections`
    - `CreateDatasourceConnection`
    - `DeleteDatasourceConnection`
    - `ShowDatasourceConnection`
    - `ShowSqlSampleTemplates`
    - `ShowPartitions`
    - `ShowFlinkMetric`

### HuaweiCloud SDK EC

- _新增特性_
  - 支持接口`ShowEquipmentWlan`、`UpdateEquipmentWlan`
- _解决问题_
  - 无
- _特性变更_
  - **ShowEquipmentInfo**
    - 响应参数变更
      - `+ type: enum value [soho]`
  - **UpdateEquipmentInfo**
    - 响应参数变更
      - `+ type: enum value [soho]`
  - **GenerateInitialConfiguration**
    - 响应参数变更
      - `+ url_config_content`
      - `+ script_config_content`
      - `- config_content`
  - **ShowEquipmentSpecificConfig**
    - 请求参数变更
      - `+ equipment_id`
      - `- equipment_type`
    - 响应参数变更
      - `- model`
  - **CreateEquipment**
    - 请求参数变更
      - `+ type: enum value [soho]`
    - 响应参数变更
      - `+ type: enum value [soho]`
  - **ListEquipments**
    - 响应参数变更
      - `+ equipments.type: enum value [soho]`
  - **ShowIegInfo**
    - 响应参数变更
      - `+ equipment_infos.type: enum value [soho]`
  - **UpdateIeg**
    - 响应参数变更
      - `+ equipment_infos.type: enum value [soho]`
  - **ListIeg**
    - 响应参数变更
      - `+ intelligent_enterprise_gateways.equipment_infos.type: enum value [soho]`

### HuaweiCloud SDK EG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDetailOfEvent**
    - 请求参数变更
      - `+ channel_id`
  - **DeleteChannel**
    - 请求参数变更
      - `+ enterprise_project_id`
  - **ShowDetailOfChannel**
    - 请求参数变更
      - `+ enterprise_project_id`
    - 响应参数变更
      - `+ eps_id`
  - **UpdateChannel**
    - 请求参数变更
      - `+ enterprise_project_id`
      - `+ eps_id`
      - `+ cross_account`
      - `+ policy`
    - 响应参数变更
      - `+ eps_id`
  - **CreateChannel**
    - 请求参数变更
      - `+ enterprise_project_id`
      - `+ eps_id`
      - `+ cross_account`
      - `+ policy`
    - 响应参数变更
      - `+ eps_id`
  - **ListChannels**
    - 请求参数变更
      - `+ eps_id`
    - 响应参数变更
      - `+ eps_id`
      - `+ items.eps_id`
  - **CreateSubscriptionTarget**
    - 请求参数变更
      - `+ eg_detail`
      - `- detail.url`
      - `- detail.agency_name`
      - `- detail.invocation_http_parameters`
      - `* detail: object<Detail> -> object`
  - **UpdateSubscriptionTarget**
    - 请求参数变更
      - `+ eg_detail`
      - `- detail.url`
      - `- detail.agency_name`
      - `- detail.invocation_http_parameters`
      - `* detail: object<Detail> -> object`
  - **ShowDetailOfConnection**
    - 响应参数变更
      - `+ kafka_detail.security_protocol`
  - **UpdateConnection**
    - 响应参数变更
      - `+ kafka_detail.security_protocol`
  - **UpdateSubscription**
    - 请求参数变更
      - `+ targets.eg_detail`
      - `- targets.detail.url`
      - `- targets.detail.agency_name`
      - `- targets.detail.invocation_http_parameters`
      - `* targets.detail: object<Detail> -> object`
  - **CreateConnection**
    - 请求参数变更
      - `+ kafka_detail.security_protocol`
    - 响应参数变更
      - `+ kafka_detail.security_protocol`
  - **ListConnections**
    - 响应参数变更
      - `+ items.kafka_detail.security_protocol`
  - **ShowEventStreaming**
    - 响应参数变更
      - `+ source.source_mobile_rocketmq`
      - `+ source.source_kafka.security_protocol`
      - `+ sink.sink_kafka`
      - `+ sink.name: enum value [HC.FunctionGraph,HC.Kafka]`
      - `- sink.name: enum value [HC.FG]`
  - **UpdateEventStreaming**
    - 请求参数变更
      - `+ source.source_mobile_rocketmq`
      - `+ source.source_kafka.security_protocol`
      - `+ sink.sink_kafka`
      - `+ sink.name: enum value [HC.FunctionGraph,HC.Kafka]`
      - `- sink.name: enum value [HC.FG]`
  - **CreateSubscription**
    - 请求参数变更
      - `+ targets.eg_detail`
      - `- targets.detail.url`
      - `- targets.detail.agency_name`
      - `- targets.detail.invocation_http_parameters`
      - `* targets.detail: object<Detail> -> object`
  - **CreateEventStreaming**
    - 请求参数变更
      - `+ source.source_mobile_rocketmq`
      - `+ source.source_kafka.security_protocol`
      - `+ sink.sink_kafka`
      - `+ sink.name: enum value [HC.FunctionGraph,HC.Kafka]`
      - `- sink.name: enum value [HC.FG]`
  - **ListEventStreaming**
    - 请求参数变更
      - `+ name`
      - `+ fuzzy_name`
    - 响应参数变更
      - `+ source.source_mobile_rocketmq`
      - `+ source.source_kafka.security_protocol`
      - `+ sink.sink_kafka`
      - `+ sink.name: enum value [HC.FunctionGraph,HC.Kafka]`
      - `- sink.name: enum value [HC.FG]`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `ShowDependcy`
    - `UpdateDependcy`
    - `DeleteDependency`
    - `AsyncInvokeReservedFunction`
    - `CreateDependency`
  - **ShowFuncReservedInstanceMetrics**
    - 请求参数变更
      - `+ marker`
      - `+ limit`
  - **ListFunctionApplications**
    - 请求参数变更
      - `+ limit`
      - `+ marker`
  - **ListStatistics**
    - 请求参数变更
      - `+ limit`
      - `+ marker`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ListGaussMySqlInstancesUnifyStatus`、`ShowGaussMySqlInstanceInfoUnifyStatus`、`ListGaussMySqlInstanceDetailInfoUnifyStatus`、`SwitchGaussMySqlProxySsl`
- _解决问题_
  - 无
- _特性变更_
  - **ShowGaussMySqlProxyList**
    - 响应参数变更
      - `+ proxy_list.proxy.ssl_option`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持接口`OfflineNodes`
- _解决问题_
  - 无
- _特性变更_
  - **ListLtsConfigs**
    - 响应参数变更
      - `* instance_lts_configs.instance.supported_log_types: string -> list<string>`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ResetDeviceSecret**
    - 请求参数变更
      - `+ secret_type`
    - 响应参数变更
      - `+ secret_type`
  - **ResetFingerprint**
    - 请求参数变更
      - `+ fingerprint_type`
    - 响应参数变更
      - `+ fingerprint_type`
  - **ShowDevice**
    - 响应参数变更
      - `+ auth_info.secondary_secret`
      - `+ auth_info.secondary_fingerprint`
      - `* auth_info: object<AuthInfo> -> object<AuthInfoRes>`
  - **UpdateDevice**
    - 响应参数变更
      - `+ auth_info.secondary_secret`
      - `+ auth_info.secondary_fingerprint`
      - `* auth_info: object<AuthInfo> -> object<AuthInfoRes>`
  - **AddDevice**
    - 响应参数变更
      - `+ auth_info.secondary_secret`
      - `+ auth_info.secondary_fingerprint`
      - `* auth_info: object<AuthInfo> -> object<AuthInfoRes>`

### HuaweiCloud SDK KooMessage

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateAimPersonalTemplate**
    - 请求参数变更
      - `+ pages.contents.button_type`

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`UpdateAutoScalingPolicy`、`CreateAutoScalingPolicy`、`DeleteAutoScalingPolicy`
- _解决问题_
  - 无
- _特性变更_
  - **ShowAutoScalingPolicy**
    - 响应参数变更
      - `+ auto_scaling_policy.tags`
      - `- auto_scaling_policy.exec_scripts`
      - `* auto_scaling_policy: object<AutoScalingPolicy> -> object<AutoScalingPolicyInfo>`

### HuaweiCloud SDK NAT

- _新增特性_
  - 支持以下接口：
    - `ListNatGatewayByTag`
    - `BatchCreateDeleteNatGatewayTag`
    - `ShowNatGatewayTag`
    - `CreateNatGatewayTag`
    - `DeleteNatGatewayTag`
    - `ListNatGatewayTag`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OMS

- _新增特性_
  - 支持接口`BatchUpdateTasks`
- _解决问题_
  - 无
- _特性变更_
  - **ShowSyncTask**
    - 响应参数变更
      - `+ dst_storage_policy`
      - `+ object_overwrite_mode`
  - **ListSyncTasks**
    - 响应参数变更
      - `+ tasks.object_overwrite_mode`
      - `+ tasks.dst_storage_policy`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 支持接口`ShowRocketMqConfigs`、`UpdateRocketMqConfigs`
- _解决问题_
  - 无
- _特性变更_
  - **ListInstances**
    - 请求参数变更
      - `+ status: enum value [UPGRADING,UPGRADINGFAILED]`

### HuaweiCloud SDK SFSTurbo

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **SetHpcCacheBackend**
    - 请求参数变更
      - `* update_hpc_cache.data.nas.type: object -> string`
      - `* update_hpc_cache.data.nas.url: object -> string`

# 3.1.70 2023-11-30

### HuaweiCloud SDK DIS

- _新增特性_
  - 支持数据接入服务
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
  - **ListPermissions**
    - 响应参数变更
      - `* : map<string, AuthModel> -> string`
  - **ListAccessCode**
    - 响应参数变更
      - `- access_codes.status: enum value [enable,unenable]`

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSubCustomerBillDetail**
    - 响应参数变更
      - `* fee_records.usage_amount: double -> bigdecimal`
      - `* fee_records.free_resource_usage: double -> bigdecimal`
      - `* fee_records.ri_usage: double -> bigdecimal`
      - `* fee_records.official_amount: double -> bigdecimal`
      - `* fee_records.official_discount_amount: double -> bigdecimal`
      - `* fee_records.payment_amount: double -> bigdecimal`
      - `* fee_records.cash_amount: double -> bigdecimal`
      - `* fee_records.credit_amount: double -> bigdecimal`
      - `* fee_records.coupon_amount: double -> bigdecimal`
      - `* fee_records.flexipurchase_coupon_amount: double -> bigdecimal`
      - `* fee_records.stored_value_card_amount: double -> bigdecimal`
      - `* fee_records.debt_amount: double -> bigdecimal`
      - `* fee_records.writeoff_amount: double -> bigdecimal`

### HuaweiCloud SDK CC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListBandwidthPackageTags**
    - 响应参数变更
      - `+ tags.values`
      - `- tags.value`
      - `* tags: list<Tag> -> list<MultivaluedTag>`

### HuaweiCloud SDK CCE

- _新增特性_
  - 支持以下接口：
    - `ShowClusterConfig`
    - `UpdateClusterLogConfig`
    - `ListPartitions`
    - `CreatePartition`
    - `ShowPartition`
    - `UpdatePartition`
    - `ShowNodePoolConfigurations`
    - `UpdateNodePoolConfiguration`
    - `ShowClusterConfigurationDetails`
    - `ListCharts`
    - `UploadChart`
    - `ShowChart`
    - `UpdateChart`
    - `DeleteChart`
    - `DownloadChart`
    - `ShowChartValues`
    - `ShowUserChartsQuotas`
    - `ListReleases`
    - `CreateRelease`
    - `ShowRelease`
    - `UpdateRelease`
    - `DeleteRelease`
    - `ShowReleaseHistory`
- _解决问题_
  - 无
- _特性变更_
  - **ResizeCluster**
    - 请求参数变更
      - `* extendParam: object<ResizeClusterRequestExtendParam> -> object`
  - **UpdateClusterEip**
    - 请求参数变更
      - `* spec: object -> object<MasterEIPRequestSpec>`
    - 响应参数变更
      - `* spec: object -> object<MasterEIPResponseSpec>`
  - **ShowClusterEndpoints**
    - 响应参数变更
      - `* spec: object -> object<OpenAPISpec>`
  - **ShowAddonInstance**
    - 响应参数变更
      - `- status.status: enum value [unknown]`
  - **UpdateAddonInstance**
    - 响应参数变更
      - `- status.status: enum value [unknown]`
  - **RollbackAddonInstance**
    - 响应参数变更
      - `- status.status: enum value [unknown]`
  - **ShowCluster**
    - 响应参数变更
      - `+ spec.enableMasterVolumeEncryption`
  - **UpdateCluster**
    - 响应参数变更
      - `+ spec.enableMasterVolumeEncryption`
  - **DeleteCluster**
    - 请求参数变更
      - `+ ondemand_node_policy`
      - `+ periodic_node_policy`
    - 响应参数变更
      - `+ spec.enableMasterVolumeEncryption`
  - **CreateAddonInstance**
    - 响应参数变更
      - `- status.status: enum value [unknown]`
  - **ListAddonInstances**
    - 响应参数变更
      - `- items.status.status: enum value [unknown]`
  - **CreateCluster**
    - 请求参数变更
      - `+ spec.enableMasterVolumeEncryption`
    - 响应参数变更
      - `+ spec.enableMasterVolumeEncryption`
  - **ListClusters**
    - 请求参数变更
      - `+ status: enum value [Hibernating,Hibernation,Awaking]`
    - 响应参数变更
      - `+ items.spec.enableMasterVolumeEncryption`
  - **ShowNode**
    - 响应参数变更
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
  - **UpdateNode**
    - 响应参数变更
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
  - **DeleteNode**
    - 响应参数变更
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
  - **CreateNode**
    - 请求参数变更
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
    - 响应参数变更
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
  - **ListNodes**
    - 响应参数变更
      - `+ items.spec.hostnameConfig`
      - `+ items.spec.extendParam.kubeReservedMem`
      - `+ items.spec.extendParam.systemReservedMem`
      - `+ items.spec.extendParam.init-node-password`
      - `- items.spec.extendParam.kube-reserved-mem`
      - `- items.spec.extendParam.system-reserved-mem`
  - **ShowNodePool**
    - 响应参数变更
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
  - **UpdateNodePool**
    - 响应参数变更
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
  - **DeleteNodePool**
    - 响应参数变更
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
  - **AddNode**
    - 请求参数变更
      - `+ nodeList.spec.hostnameConfig`
  - **ResetNode**
    - 请求参数变更
      - `+ nodeList.spec.hostnameConfig`
  - **CreateNodePool**
    - 请求参数变更
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
    - 响应参数变更
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
  - **ListNodePools**
    - 响应参数变更
      - `+ items.spec.nodeTemplate.hostnameConfig`
      - `+ items.spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ items.spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ items.spec.nodeTemplate.extendParam.init-node-password`
      - `- items.spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- items.spec.nodeTemplate.extendParam.system-reserved-mem`

### HuaweiCloud SDK CodeArtsPipeline

- _新增特性_
  - 支持接口`ShowPipelineLog`
- _解决问题_
  - 无
- _特性变更_
  - **UpdatePluginBaseInfo**
    - 请求参数变更
      - `+ plugin_composition_type`
  - **CreatePublisher**
    - 请求参数变更
      - `+ description`
  - **ListPublisher**
    - 响应参数变更
      - `+ total`
      - `+ offset`
      - `+ data`
      - `+ limit`
      - `- tenant_id`
      - `- website`
      - `- logo_url`
      - `- description`
      - `- last_update_user_id`
      - `- source_url`
      - `- is_delete`
      - `- last_update_time`
      - `- support_url`
      - `- user_id`
      - `- name`
      - `- en_name`
      - `- auth_status`
      - `- publisher_unique_id`
      - `- last_update_user_name`
  - **ListBasePluginsNewPost**
    - 响应参数变更
      - `+ data.business_type`
      - `+ data.display_name`
      - `+ data.unique_id`
      - `- data.businessType`
      - `- data.displayName`
      - `- data.uniqueId`
      - `+ data.plugins_list.publisher_unique_id`
      - `+ data.plugins_list.manifest_version`
      - `- data.plugins_list.publisherUniqueId`
      - `- data.plugins_list.manifestVersion`
  - **ListPlugins**
    - 响应参数变更
      - `+ data.plugin_name`
      - `+ data.display_name`
      - `+ data.version_description`
      - `+ data.version_attribution`
      - `+ data.unique_id`
      - `+ data.op_user`
      - `+ data.op_time`
      - `+ data.plugin_composition_type`
      - `+ data.plugin_attribution`
      - `+ data.workspace_id`
      - `+ data.business_type`
      - `+ data.business_type_display_name`
      - `+ data.icon_url`
      - `+ data.refer_count`
      - `+ data.usage_count`
      - `+ data.runtime_attribution`
      - `- data.pluginName`
      - `- data.displayName`
      - `- data.versionDescription`
      - `- data.versionAttribution`
      - `- data.uniqueId`
      - `- data.opUser`
      - `- data.opTime`
      - `- data.pluginCompositionType`
      - `- data.pluginAttribution`
      - `- data.workspaceId`
      - `- data.businessType`
      - `- data.businessTypeDisplayName`
      - `- data.iconUrl`
      - `- data.referCount`
      - `- data.usageCount`
      - `- data.runtimeAttribution`
      - `* data: list<object> -> list<PluginBasicVO>`
  - **ListPLuginVersion**
    - 响应参数变更
      - `+ data.plugin_name`
      - `+ data.display_name`
      - `+ data.version_description`
      - `+ data.version_attribution`
      - `+ data.unique_id`
      - `+ data.op_user`
      - `+ data.op_time`
      - `+ data.plugin_composition_type`
      - `+ data.plugin_attribution`
      - `+ data.workspace_id`
      - `+ data.business_type`
      - `+ data.business_type_display_name`
      - `+ data.icon_url`
      - `+ data.refer_count`
      - `+ data.usage_count`
      - `+ data.runtime_attribution`
      - `- data.pluginName`
      - `- data.displayName`
      - `- data.versionDescription`
      - `- data.versionAttribution`
      - `- data.uniqueId`
      - `- data.opUser`
      - `- data.opTime`
      - `- data.pluginCompositionType`
      - `- data.pluginAttribution`
      - `- data.workspaceId`
      - `- data.businessType`
      - `- data.businessTypeDisplayName`
      - `- data.iconUrl`
      - `- data.referCount`
      - `- data.usageCount`
      - `- data.runtimeAttribution`
      - `* data: list<object> -> list<PluginBasicVO>`
  - **ShowPublisher**
    - 响应参数变更
      - `+ publisher_detail_map`
      - `- body`
  - **CreateBasicPlugin**
    - 请求参数变更
      - `+ plugin_composition_type`
  - **UpdateBasicPlugin**
    - 请求参数变更
      - `+ plugin_composition_type`
  - **CreateStrategy**
    - 请求参数变更
      - `- type`
      - `- rules.type`
      - `- rules.name`
      - `- rules.layout_content`
      - `- rules.plugin_id`
      - `- rules.plugin_name`
      - `- rules.plugin_version`
      - `- rules.content`
  - **UpdateStrategy**
    - 请求参数变更
      - `- parent_id`
      - `- rules.type`
      - `- rules.name`
      - `- rules.layout_content`
      - `- rules.plugin_id`
      - `- rules.plugin_name`
      - `- rules.plugin_version`
      - `- rules.content`

### HuaweiCloud SDK DataArtsStudio

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **SearchAtomicIndexes**
    - 响应参数变更
      - `+ data.value`
  - **ShowAtomicIndexById**
    - 响应参数变更
      - `+ data.value`
  - **ListDerivativeIndexes**
    - 响应参数变更
      - `+ data.value`
  - **ShowDerivativeIndexById**
    - 响应参数变更
      - `+ data.value`
  - **ListCompoundMetrics**
    - 响应参数变更
      - `+ data.value`
  - **ShowCompoundMetricById**
    - 响应参数变更
      - `+ data.value`
  - **ListApiCatalogList**
    - 响应参数变更
      - `+ apis.publish_messages`
  - **ParseUserBehavior**
    - 请求参数变更
      - `+ params.filter.attribute: enum value [base.DataAsset.sourceType,typeName,classifications.name,tags.name,securityLevel.name,workspaceId]`
      - `+ params.filter.operator: enum value [IN,EQ]`
      - `* params.filter.value: object -> list<string>`
      - `* params.filter.condition: object<ConditionInfo> -> string`
  - **ShowDataSets**
    - 请求参数变更
      - `+ filter.attribute: enum value [base.DataAsset.sourceType,typeName,classifications.name,tags.name,securityLevel.name,workspaceId]`
      - `+ filter.operator: enum value [IN,EQ]`
      - `* filter.value: object -> list<string>`
      - `* filter.condition: object<ConditionInfo> -> string`
    - 响应参数变更
      - `* facets: object -> list<object>`
  - **ListApis**
    - 请求参数变更
      - `+ x-return-publish-messages`
    - 响应参数变更
      - `+ records.publish_messages`
  - **ShowApi**
    - 响应参数变更
      - `+ publish_messages`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSlowlog**
    - 响应参数变更
      - `+ total_num`

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持接口`ShowQuota`
- _解决问题_
  - 无
- _特性变更_
  - **ListQueueProperties**
    - 请求参数变更
      - `+ offset`
      - `+ limit`
      - `- page`
      - `- page_size`

### HuaweiCloud SDK EIP

- _新增特性_
  - 支持接口`BatchModifyBandwidth`、`ListEipBandwidths`、`ListBandwidthsLimit`、`UpdatePublicip`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持接口`ListInfluxdbSlowLogs`
- _解决问题_
  - 无
- _特性变更_
  - **ListLtsConfigs**
    - 响应参数变更
      - `+ instance_lts_configs.instance.supported_log_types`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RunQueryDocumentModerationJob**
    - 响应参数变更
      - `+ result.details.start_position`
      - `+ result.details.end_position`
      - `+ result.details.image_url`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`SetInstancesDbShrink`
- _解决问题_
  - 无
- _特性变更_
  - **UpgradeDbMajorVersion**
    - 响应参数变更
      - `+ job_id`
  - **ShowUpgradeDbMajorVersionStatus**
    - 响应参数变更
      - `+ check_expiration_time`
      - `- report_expiration_time`
  - **StartResizeFlavorAction**
    - 响应参数变更
      - `+ order_id`
  - **StartInstanceEnlargeVolumeAction**
    - 响应参数变更
      - `+ order_id`
  - **StartInstanceSingleToHaAction**
    - 响应参数变更
      - `+ order_id`
  - **ListHistoryDatabase**
    - 请求参数变更
      - `+ engine`
      - `- database_name`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 支持接口`ShowEngineInstanceExtendProductInfo`、`ResizeInstance`
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
  - **RecognizeFlashAsr**
    - 请求参数变更
      - `* obs_bucket_name: optional -> required`
      - `* obs_object_key: optional -> required`

# 3.1.69 2023-11-23

### HuaweiCloud SDK CFW

- _新增特性_
  - 支持接口`ListLogConfig`、`UpdateLogConfig`、`AddLogConfig`、`CreateEastWestFirewall`
- _解决问题_
  - 无
- _特性变更_
  - **ListFlowLogs**
    - 响应参数变更
      - `* data.records.start_time: int32 -> int64`
      - `* data.records.end_time: int32 -> int64`
      - `* data.records.src_port: string -> int32`
      - `* data.records.dst_port: string -> int32`
  - **ListAccessControlLogs**
    - 响应参数变更
      - `* data.records.hit_time: int32 -> int64`
      - `* data.records.src_port: string -> int32`
      - `* data.records.dst_port: string -> int32`
  - **ChangeIpsSwitchStatus**
    - 请求参数变更
      - `+ X-Language`
  - **ListAttackLogs**
    - 响应参数变更
      - `* data.records.event_time: string -> int64`
      - `* data.records.attack_rule_id: int32 -> string`
      - `* data.records.packet: object<Packet> -> string`

# 3.1.68 2023-11-23

### HuaweiCloud SDK AOM

- _新增特性_
  - 支持以下接口：
    - `ListPromInstance`
    - `CreatePromInstance`
    - `DeletePromInstance`
    - `CreateRecordingRule`
    - `ListPermissions`
    - `ListAccessCode`
    - `ListAgents`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CodeArtsPipeline

- _新增特性_
  - 支持以下接口：
    - `UpdatePluginBaseInfo`
    - `CreatePluginDraft`
    - `PublishPluginDraft`
    - `CreatePluginVersion`
    - `UpdatePluginDraft`
    - `CreatePublisher`
- _解决问题_
  - 无
- _特性变更_
  - **SwitchStrategy**
    - 响应参数变更
      - `+ rule_set_id`
      - `- rule_template_instance_id`
  - **SwitchOpenSourceStrategy**
    - 响应参数变更
      - `+ rule_set_id`
      - `- rule_template_instance_id`
  - **ShowPublisher**
    - 响应参数变更
      - `+ body`
  - **CreatePipelineNew**
    - 请求参数变更
      - `+ group_id`
      - `+ id`
      - `* schedules.days_of_week: string -> list<integer>`
  - **UpdateStrategy**
    - 响应参数变更
      - `+ rule_set_id`
      - `- rule_template_instance_id`
  - **UpdateOpenSourceStrategy**
    - 响应参数变更
      - `+ rule_set_id`
      - `- rule_template_instance_id`

### HuaweiCloud SDK CSE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpgradeEngineConfig**
    - 请求参数变更
      - `+ authType`
      - `- version`
  - **ShowEngine**
    - 响应参数变更
      - `+ specType`
      - `+ enterpriseProjectId`
      - `+ externalEntrypoint`
      - `+ beDefault`
      - `+ engineAdditionalActions`
      - `+ cceSpec`
      - `+ vmIds`
      - `+ latestVersion`
      - `+ createTime`
      - `+ createUser`
      - `+ authType`
      - `+ latestJobId`
      - `+ projectId`
      - `+ enterpriseProjectName`
      - `- auth_type`
      - `- create_time`
      - `- be_default`
      - `- enterprise_project_name`
      - `- latest_job_id`
      - `- spec_type`
      - `- external_entrypoint`
      - `- cce_spec`
      - `- enterprise_project_id`
      - `- latest_version`
      - `- project_id`
      - `- vm_ids`
      - `- engine_additional_actions`
      - `- create_user`
      - `+ reference.azList`
      - `+ reference.networkId`
      - `+ reference.subnetCidr`
      - `+ reference.subnetCidrV6`
      - `+ reference.subnetGateway`
      - `+ reference.publicIpId`
      - `+ reference.serviceLimit`
      - `+ reference.instanceLimit`
      - `- reference.az_list`
      - `- reference.network_id`
      - `- reference.subnet_cidr`
      - `- reference.subnet_cidr_v6`
      - `- reference.subnet_gateway`
      - `- reference.public_ip_id`
      - `- reference.service_limit`
      - `- reference.instance_limit`
  - **CreateEngine**
    - 请求参数变更
      - `+ vpcId`
  - **ListEngines**
    - 响应参数变更
      - `+ data.enterpriseProjectId`
      - `+ data.enterpriseProjectName`
      - `+ data.authType`
      - `+ data.externalAddress`
      - `+ data.serviceEndpoint`
      - `+ data.publicAddress`
      - `+ data.publicServiceEndpoint`
      - `+ data.totalInstance`
      - `+ data.usedInstance`
      - `+ data.availableInstance`
      - `+ data.latestVersion`
      - `+ data.createTime`
      - `+ data.dueTo`
      - `+ data.latestJobId`
      - `+ data.engineAdditionalActions`
      - `+ data.specType`
      - `- data.enterpris_project_id`
      - `- data.enterprise_project_name`
      - `- data.auth_type`
      - `- data.external_address`
      - `- data.service_endpoint`
      - `- data.public_address`
      - `- data.public_service_endpoint`
      - `- data.total_instance`
      - `- data.used_instance`
      - `- data.available_instance`
      - `- data.latest_version`
      - `- data.create_time`
      - `- data.due_to`
      - `- data.latest_job_id`
      - `- data.engine_additional_actions`
      - `- data.spec_type`
      - `+ data.reference.azList`
      - `+ data.reference.networkId`
      - `+ data.reference.subnetCidr`
      - `+ data.reference.subnetCidrV6`
      - `+ data.reference.subnetGateway`
      - `+ data.reference.publicIpId`
      - `+ data.reference.serviceLimit`
      - `+ data.reference.instanceLimit`
      - `- data.reference.az_list`
      - `- data.reference.network_id`
      - `- data.reference.subnet_cidr`
      - `- data.reference.subnet_cidr_v6`
      - `- data.reference.subnet_gateway`
      - `- data.reference.public_ip_id`
      - `- data.reference.service_limit`
      - `- data.reference.instance_limit`
  - **ShowEngineJob**
    - 响应参数变更
      - `+ createUser`
      - `+ startTime`
      - `+ endTime`
      - `+ engineId`
      - `- start_time`
      - `- engine_id`
      - `- end_time`
      - `- create_user`
      - `+ tasks.taskName`
      - `+ tasks.taskNames`
      - `+ tasks.startTime`
      - `+ tasks.endTime`
      - `+ tasks.taskExecutorBrief`
      - `- tasks.task_name`
      - `- tasks.task_names`
      - `- tasks.start_time`
      - `- tasks.end_time`
      - `- tasks.task_executor_brief`
      - `+ tasks.tasks.jobId`
      - `+ tasks.tasks.taskName`
      - `+ tasks.tasks.engineName`
      - `+ tasks.tasks.taskOrder`
      - `+ tasks.tasks.startTime`
      - `+ tasks.tasks.endTime`
      - `+ tasks.tasks.createTime`
      - `+ tasks.tasks.updateTime`
      - `+ tasks.tasks.taskExecutorBrief`
      - `- tasks.tasks.job_id`
      - `- tasks.tasks.task_name`
      - `- tasks.tasks.engine_name`
      - `- tasks.tasks.task_order`
      - `- tasks.tasks.start_time`
      - `- tasks.tasks.end_time`
      - `- tasks.tasks.create_time`
      - `- tasks.tasks.update_time`
      - `- tasks.tasks.task_executor_brief`
  - **CreateMicroserviceRouteRule**
    - 请求参数变更
      - `+ match.headers.<header>`
      - `- match.headers.aaaa`
      - `+ route.tags.<tag>`
      - `- route.tags.version`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListCerts**
    - 响应参数变更
      - `* defaultCerts: object<DefaultCertsResource> -> list<DefaultCertsResource>`
      - `* customCerts: object<CustomCertsResource> -> list<CustomCertsResource>`

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`LogoffWebCli`
- _解决问题_
  - 无
- _特性变更_
  - **ListSlowlog**
    - 响应参数变更
      - `+ slowlogs.database_id`
      - `+ slowlogs.username`

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持以下接口：
    - `ListLtsConfigs`
    - `UpdateLtsConfig`
    - `DeleteLtsConfig`
    - `ListLtsErrorLogs`
    - `ShowKillOpRuleRuleList`
    - `UpdateKillOpRule`
    - `CreateKillOpRule`
    - `DeleteKillOpRuleList`
    - `SwitchInstancePrimary`
    - `DeleteReadonlyNode`
    - `StopBackup`
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
  - **BatchDeleteJobs**
    - 请求参数变更
      - `+ jobs.is_show_breakpoint_position`
  - **BatchSetPolicy**
    - 请求参数变更
      - `+ jobs.file_and_position`
      - `+ jobs.gtid_set`
  - **BatchListProgresses**
    - 响应参数变更
      - `+ results.incre_trans_delay_millis`
  - **ShowJobList**
    - 请求参数变更
      - `+ instance_ids`
      - `+ instance_ip`

### HuaweiCloud SDK DRS

- _新增特性_
  - 支持接口`UploadJdbcDriver`、`ListJdbcDrivers`、`DeleteJdbcDriver`、`SyncJdbcDriver`
- _解决问题_
  - 无
- _特性变更_
  - **BatchCreateJobsAsync**
    - 请求参数变更
      - `+ jobs.policy_config.dml_types`
  - **ListAsyncJobDetail**
    - 响应参数变更
      - `+ jobs.connection_management`
      - `+ jobs.policy_config.dml_types`
  - **UpdateBatchAsyncJobs**
    - 请求参数变更
      - `+ jobs.params.policy_config.dml_types`
  - **ShowJobDetail**
    - 响应参数变更
      - `+ job.connection_management`
      - `+ job.policy_config.dml_types`
  - **UpdateJob**
    - 请求参数变更
      - `+ job.params.policy_config.dml_types`

### HuaweiCloud SDK ELB

- _新增特性_
  - 支持以下接口：
    - `BatchAddAvailableZones`
    - `BatchRemoveAvailableZones`
    - `ListMasterSlavePools`
    - `CreateMasterSlavePool`
    - `ShowMasterSlavePool`
    - `DeleteMasterSlavePool`
- _解决问题_
  - 无
- _特性变更_
  - **ShowLoadBalancer**
    - 响应参数变更
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.log_group_id`
      - `+ loadbalancer.log_topic_id`
  - **UpdateLoadBalancer**
    - 请求参数变更
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.ipv6_vip_address`
    - 响应参数变更
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.log_group_id`
      - `+ loadbalancer.log_topic_id`
  - **ListListeners**
    - 响应参数变更
      - `+ listeners.ssl_early_data_enable`
  - **CreateListener**
    - 请求参数变更
      - `+ listener.ssl_early_data_enable`
    - 响应参数变更
      - `+ listener.ssl_early_data_enable`
  - **ShowListener**
    - 响应参数变更
      - `+ listener.ssl_early_data_enable`
  - **UpdateListener**
    - 请求参数变更
      - `+ listener.ssl_early_data_enable`
    - 响应参数变更
      - `+ listener.ssl_early_data_enable`
  - **ListLoadBalancers**
    - 请求参数变更
      - `+ log_topic_id`
      - `+ log_group_id`
    - 响应参数变更
      - `+ loadbalancers.charge_mode`
      - `+ loadbalancers.log_group_id`
      - `+ loadbalancers.log_topic_id`
  - **CreateLoadBalancer**
    - 请求参数变更
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.ipv6_vip_address`
    - 响应参数变更
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.log_group_id`
      - `+ loadbalancer.log_topic_id`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持以下接口：
    - `ListAppTemplates`
    - `ShowAppTemplate`
    - `ListFunctionApplications`
    - `CreateFunctionApp`
    - `ShowFunctionApp`
    - `DeleteFunctionApp`
    - `CreateCallbackWorkflow`
- _解决问题_
  - 无
- _特性变更_
  - **ImportFunction**
    - 响应参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ListFunctions**
    - 响应参数变更
      - `+ functions.pre_stop_handler`
      - `+ functions.pre_stop_timeout`
  - **CreateFunction**
    - 请求参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
    - 响应参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ShowFunctionConfig**
    - 响应参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **UpdateFunctionConfig**
    - 请求参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
    - 响应参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **UpdateFunctionMaxInstanceConfig**
    - 响应参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ListBridgeFunctions**
    - 响应参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ShowResInstanceInfo**
    - 响应参数变更
      - `+ resources.resource_detail.pre_stop_handler`
      - `+ resources.resource_detail.pre_stop_timeout`
  - **CreateFunctionVersion**
    - 响应参数变更
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ListFunctionVersions**
    - 响应参数变更
      - `+ versions.pre_stop_handler`
      - `+ versions.pre_stop_timeout`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ShowRestoreTables`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持以下接口：
    - `ShowElbIpGroup`
    - `SwitchIpGroup`
    - `ListInstancesSession`
    - `DeleteInstancesSession`
    - `ListInstancesSessionStatistics`
    - `ResetParamGroupTemplate`
    - `ListRedisSlowLogs`
    - `ListCassandraSlowLogs`
    - `ListMongodbSlowLogs`
    - `ListLtsConfigs`
    - `SaveLtsConfigs`
    - `DeleteLtsConfigs`
    - `ListRestoreDatabases`
    - `ListRestoreTables`
    - `ListMongodbErrorLogs`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`ShowKafkaUserClientQuota`、`UpdateKafkaUserClientQuotaTask`、`CreateKafkaUserClientQuotaTask`、`DeleteKafkaUserClientQuotaTask`
- _解决问题_
  - 无
- _特性变更_
  - **ListInstances**
    - 请求参数变更
      - `+ status: enum value [DELETING,ERROR,CREATEFAILED,FREEZING,EXTENDING,SHRINKING,EXTENDEDFAILED,CONFIGURING,UPGRADING,UPGRADINGFAILED,ROLLBACK,ROLLBACKFAILED,VOLUMETYPECHANGING]`
      - `+ status: enum value [FAULTY,RESIZING,RESIZING FAILED]`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RecognizeIdCard**
    - 请求参数变更
      - `+ return_portrait_location`
    - 响应参数变更
      - `+ result.portrait_location`

### HuaweiCloud SDK OMS

- _新增特性_
  - 支持以下接口：
    - `ListSyncTasks`
    - `CreateSyncTask`
    - `ShowSyncTask`
    - `DeleteSyncTask`
    - `ListSyncTaskStatistic`
    - `StopSyncTask`
    - `StartSyncTask`
    - `ShowBucketObjects`
    - `ShowCdnInfo`
    - `ShowCloudType`
    - `ShowRegionInfo`
    - `ShowBucketList`
    - `ShowBucketRegion`
    - `CheckPrefix`
- _解决问题_
  - 无
- _特性变更_
  - **ShowTask**
    - 响应参数变更
      - `+ source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **ShowTaskGroup**
    - 响应参数变更
      - `+ source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **CreateTask**
    - 请求参数变更
      - `+ source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **ListTasks**
    - 响应参数变更
      - `+ tasks.source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **CreateTaskGroup**
    - 请求参数变更
      - `+ source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **ListTaskGroup**
    - 响应参数变更
      - `+ taskgroups.source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListInstancesDetails**
    - 请求参数变更
      - `+ status: enum value [DELETING,FREEZING,EXTENDING,SHRINKING,EXTENDEDFAILED,CONFIGURING,UPGRADING,UPGRADINGFAILED,ROLLBACK,ROLLBACKFAILED,VOLUMETYPECHANGING]`
      - `+ status: enum value [STARTING,CLOSING]`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持以下接口：
    - `UpgradeDbMajorVersion`
    - `ShowAvailableVersion`
    - `UpgradeDbMajorVersionPreCheck`
    - `ListInspectionHistories`
    - `ListUpgradeHistories`
    - `ShowUpgradeDbMajorVersionStatus`
    - `UpdateTdeStatus`
    - `ShowTdeStatus`
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
  - **ListInstances**
    - 请求参数变更
      - `+ status: enum value [DELETING,ERROR,CREATEFAILED,FREEZING,EXTENDING,SHRINKING,EXTENDEDFAILED,CONFIGURING,UPGRADING,UPGRADINGFAILED,ROLLBACK,ROLLBACKFAILED,VOLUMETYPECHANGING]`
      - `+ status: enum value [FAULTY,RESIZING,RESIZING FAILED]`

### HuaweiCloud SDK SCM

- _新增特性_
  - 支持接口`DeployCertificate`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SecMaster

- _新增特性_
  - 支持以下接口：
    - `ListDataclass`
    - `ListDataclassFields`
    - `ListWorkflows`
    - `CreateDataspace`
    - `CreatePipe`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ServiceStage

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateInstance**
    - 请求参数变更
      - `+ configuration.container_spec`
  - **ChangeInstance**
    - 请求参数变更
      - `+ configuration.container_spec`

### HuaweiCloud SDK VOD

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateAssetByFileUpload**
    - 请求参数变更
      - `+ thumbnail.quantity`
      - `+ thumbnail.quantity_time`
      - `+ thumbnail.type: enum value [quantity]`
  - **PublishAssetFromObs**
    - 请求参数变更
      - `+ thumbnail.quantity`
      - `+ thumbnail.quantity_time`
      - `+ thumbnail.type: enum value [quantity]`
  - **CreateAssetProcessTask**
    - 请求参数变更
      - `+ thumbnail.quantity`
      - `+ thumbnail.quantity_time`
      - `+ thumbnail.type: enum value [quantity]`
  - **ListTopStatistics**
    - 响应参数变更
      - `+ top_urls.duration_ms`
  - **UploadMetaDataByUrl**
    - 请求参数变更
      - `+ upload_metadatas.thumbnail.quantity`
      - `+ upload_metadatas.thumbnail.quantity_time`
      - `+ upload_metadatas.thumbnail.type: enum value [quantity]`
  - **ListAssetList**
    - 响应参数变更
      - `+ assets.duration_ms`
  - **ShowTakeOverAssetDetails**
    - 响应参数变更
      - `+ base_info.meta_data.duration_ms`
  - **PublishAssets**
    - 响应参数变更
      - `+ asset_info_array.base_info.meta_data.duration_ms`
  - **UnpublishAssets**
    - 响应参数变更
      - `+ asset_info_array.base_info.meta_data.duration_ms`
  - **ShowAssetMeta**
    - 响应参数变更
      - `+ asset_info_array.base_info.meta_data.duration_ms`
  - **ShowAssetDetail**
    - 响应参数变更
      - `+ base_info.meta_data.duration_ms`
      - `+ thumbnail_info.quantity`
  - **ShowTakeOverTaskDetails**
    - 响应参数变更
      - `+ assets.base_info.meta_data.duration_ms`

# 3.1.67 2023-11-16

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDomainFullConfig**
    - 响应参数变更
      - `+ configs.business_type`
      - `+ configs.service_area`
      - `+ configs.remark`
      - `+ configs.flexible_origin`
      - `+ configs.slice_etag_status`
      - `+ configs.origin_receive_timeout`
      - `+ configs.remote_auth`
      - `+ configs.websocket`
      - `+ configs.video_seek`
      - `+ configs.request_limit_rules`
      - `+ configs.ip_frequency_limit`
      - `+ configs.hsts`
      - `+ configs.quic`
      - `+ configs.url_auth.sign_method`
      - `+ configs.url_auth.match_type`
      - `+ configs.url_auth.inherit_config`
      - `+ configs.url_auth.key`
      - `+ configs.url_auth.backup_key`
      - `+ configs.url_auth.sign_arg`
      - `+ configs.https.expire_time`
      - `+ configs.https.certificate_type`
      - `+ configs.https.ocsp_stapling_status`
      - `+ configs.sources.weight`
      - `+ configs.sources.obs_bucket_type`
      - `+ configs.sources.bucket_access_key`
      - `+ configs.sources.bucket_secret_key`
      - `+ configs.sources.bucket_region`
      - `+ configs.sources.bucket_name`
      - `+ configs.compress.file_type`
      - `+ configs.user_agent_filter.ua_list`
  - **UpdateDomainFullConfig**
    - 请求参数变更
      - `+ configs.sources.weight`
      - `+ configs.sources.obs_bucket_type`
      - `+ configs.sources.bucket_access_key`
      - `+ configs.sources.bucket_secret_key`
      - `+ configs.sources.bucket_region`
      - `+ configs.sources.bucket_name`
      - `+ configs.compress.file_type`
      - `+ configs.user_agent_filter.ua_list`

### HuaweiCloud SDK CodeArtsBuild

- _新增特性_
  - 支持以下接口：
    - `DownloadBuildLog`
    - `DownloadTaskLog`
    - `ShowFlowGraph`
    - `ShowRecordDetail`
    - `ShowOutputInfo`
    - `StopJob`
    - `CreateBuildJob`
    - `UpdateBuildJob`
    - `ListTemplates`
    - `CreateTemplates`
    - `DeleteTemplates`
    - `ListNotice`
    - `UpdateNotice`
    - `DisableNotice`
    - `ListJobConfig`
- _解决问题_
  - 无
- _特性变更_
  - **ShowRecordInfo**
    - 响应参数变更
      - `+ result.duration`

### HuaweiCloud SDK CodeArtsPipeline

- _新增特性_
  - 支持以下接口：
    - `CreatePipelineTemplate`
    - `ShowProjectOpenSourceStrategy`
    - `ListProjectStrategy`
    - `ListProjectOpenSourceStrategy`
    - `ShowProjectStrategy`
    - `ShowRule`
    - `ListRule`
    - `UpdateRule`
    - `DeleteRule`
    - `CreateRule`
    - `CreateStrategy`
    - `UpdateStrategy`
    - `ShowStrategy`
    - `ListStrategy`
    - `DeleteStrategy`
    - `SwitchStrategy`
    - `CreateOpenSourceStrategy`
    - `UpdateOpenSourceStrategy`
    - `ShowOpenSourceStrategy`
    - `ListOpenSourceStrategy`
    - `DeleteOpenSourceStrategy`
    - `SwitchOpenSourceStrategy`
    - `CreatePipelineGroup`
    - `UpdatePipelineGroup`
    - `DeletePipelineGroup`
    - `ShowPipelineGroupTree`
    - `BatchMovePipelineToGroup`
    - `PublishPlugin`
    - `PublishPluginBind`
    - `UploadPluginIcon`
    - `UploadPublisherIcon`
    - `DeletePluginDraft`
    - `ListPublisher`
    - `ListAvailablePublisher`
    - `ListStagePlugins`
    - `ListBasePlugins`
    - `ListBasePluginsNewPost`
    - `ListPlugins`
    - `ShowPluginMetrics`
    - `ShowPluginInputs`
    - `ShowPluginOutputs`
    - `ListPLuginVersion`
    - `ShowPluginVersion`
    - `ListPluginVersionNumber`
    - `DeletePublisher`
    - `ShowPublisher`
    - `CreateBasicPlugin`
    - `UpdateBasicPlugin`
    - `DeleteBasicPlugin`
    - `UploadBasicPlugin`
    - `ShowBasicPlugin`
    - `UpdatePipelineTemplate`
    - `DeletePipelineTemplate`
- _解决问题_
  - 无
- _特性变更_
  - **ListPipelines**
    - 响应参数变更
      - `+ pipelines.project_name`
  - **CreatePipelineNew**
    - 请求参数变更
      - `+ variables`
      - `+ schedules`
      - `+ triggers`
      - `+ manifest_version`
      - `+ definition`
      - `+ project_name`

### HuaweiCloud SDK CSE

- _新增特性_
  - 支持以下接口：
    - `ListGovernancePolicy`
    - `CreateGovernancePolicy`
    - `ListGovernancePolicyByPolicyId`
    - `UpdateGovernancePolicy`
    - `DeleteGovernancePolicy`
    - `ListMicroserviceRouteRule`
    - `CreateMicroserviceRouteRule`
    - `DeleteMicroserviceRouteRule`
    - `ListGovernancePolicys`
    - `UpgradeEngineConfig`
    - `ResizeEngine`
    - `ListNacosNamespaces`
    - `UpdateNacosNamespaces`
    - `CreateNacosNamespaces`
    - `DeleteNacosNamespaces`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSecretTags**
    - 响应参数变更
      - `+ sys_tags.value`
      - `- sys_tags.values`
  - **ListNotificationRecords**
    - 请求参数变更
      - `+ limit`
      - `+ marker`

### HuaweiCloud SDK DataArtsStudio

- _新增特性_
  - 支持接口`UpdateFactoryJobName`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateVifPeer**
    - 响应参数变更
      - `+ vif_peer.receive_route_num`
  - **CreateVifPeer**
    - 响应参数变更
      - `+ vif_peer.receive_route_num`
  - **ShowVirtualInterface**
    - 响应参数变更
      - `+ virtual_interface.vif_peers.receive_route_num`
  - **UpdateVirtualInterface**
    - 响应参数变更
      - `+ virtual_interface.vif_peers.receive_route_num`
  - **ListVirtualInterfaces**
    - 响应参数变更
      - `+ virtual_interfaces.vif_peers.receive_route_num`
  - **CreateVirtualInterface**
    - 响应参数变更
      - `+ virtual_interface.vif_peers.receive_route_num`

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowScript**
    - 响应参数变更
      - `+ description`
      - `+ approvers`
      - `+ targetStatus`
      - `+ type: enum value [RDSSQL,PRESTO,ClickHouseSQL,HetuEngineSQL,PYTHON,ImpalaSQL,SparkPython]`
  - **UpdateScript**
    - 请求参数变更
      - `+ description`
      - `+ approvers`
      - `+ targetStatus`
      - `+ type: enum value [RDSSQL,PRESTO,ClickHouseSQL,HetuEngineSQL,PYTHON,ImpalaSQL,SparkPython]`
  - **CreateScript**
    - 请求参数变更
      - `+ description`
      - `+ approvers`
      - `+ targetStatus`
      - `+ type: enum value [RDSSQL,PRESTO,ClickHouseSQL,HetuEngineSQL,PYTHON,ImpalaSQL,SparkPython]`
  - **ListScripts**
    - 响应参数变更
      - `+ description`
      - `+ approvers`
      - `+ targetStatus`
      - `+ scripts.description`
      - `+ scripts.targetStatus`
      - `+ scripts.approvers`
      - `+ scripts.type: enum value [RDSSQL,PRESTO,ClickHouseSQL,HetuEngineSQL,PYTHON,ImpalaSQL,SparkPython]`

### HuaweiCloud SDK DLI

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowSqlJobStatus**
    - 响应参数变更
      - `+ result_format`
      - `+ result_path`

### HuaweiCloud SDK DNS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreatePrivateZone**
    - 请求参数变更
      - `+ router.status`
  - **AssociateRouter**
    - 请求参数变更
      - `+ router.status`
  - **DisassociateRouter**
    - 请求参数变更
      - `+ router.status`
  - **ShowPrivateZone**
    - 响应参数变更
      - `+ routers.status`

### HuaweiCloud SDK EdgeSec

- _新增特性_
  - 支持以下接口：
    - `ListCertificates`
    - `CreateCertificate`
    - `ShowCertificate`
    - `UpdateCertificate`
    - `DeleteCertificate`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持以下接口：
    - `ListFunctionTags`
    - `ListBridgeFunctions`
    - `ListBridgeVersions`
    - `UpdateFunctionCollectState`
    - `ListFunctionTemplate`
    - `ShowFunctionTemplate`
    - `ShowFuncReservedInstanceMetrics`
    - `ShowFunctionMetrics`
    - `EnableAsyncStatusLog`
    - `ShowProjectAsyncStatusLogInfo`
- _解决问题_
  - 无
- _特性变更_
  - **ListFunctions**
    - 响应参数变更
      - `+ functions.resource_id`
  - **ShowFunctionConfig**
    - 响应参数变更
      - `+ func_id`
      - `+ resource_id`
  - **UpdateFunctionConfig**
    - 响应参数变更
      - `+ func_id`
      - `+ resource_id`
  - **ShowResInstanceInfo**
    - 响应参数变更
      - `+ resources.resource_detail.resource_id`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateGaussMySqlInstance**
    - 响应参数变更
      - `* instance.volume.size: string -> int32`

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListFlowBySimCards**
    - 请求参数变更
      - `+ sim_card_ids`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowRuleAction**
    - 响应参数变更
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
  - **UpdateRuleAction**
    - 请求参数变更
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
    - 响应参数变更
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
  - **CreateRuleAction**
    - 请求参数变更
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
    - 响应参数变更
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
  - **ListRuleActions**
    - 响应参数变更
      - `+ actions.channel_detail.dms_kafka_forwarding.security_protocol`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListInstanceConsumerGroups**
    - 响应参数变更
      - `* groups.createdAt: int32 -> int64`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListTopnTrafficStatistics**
    - 响应参数变更
      - `+ results.cold_storage`

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`AddComponent`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizePeruIdCard`
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
  - 移除接口`ShowRabbitMqProductCores`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`RevokePostgresqlDbPrivilege`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ServiceStage

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ChangeInstance**
    - 请求参数变更
      - `+ configuration.env`
      - `+ configuration.storage`
      - `+ configuration.strategy`
      - `+ configuration.lifecycle`
      - `+ configuration.scheduler`
      - `+ configuration.probes`
      - `* configuration: map<string, object> -> object<InstanceConfiguration>`

### HuaweiCloud SDK Workspace

- _新增特性_
  - 支持接口`BatchAddDesktopsTags`、`BatchDeleteDesktopsTags`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.66 2023-11-13

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`ShowNodesInformation`、`DeleteCenterTask`、`DeleteDiagnosisTask`
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
  - **ListInstanceTopics**
    - 请求参数变更
      - `+ offset`
      - `+ limit`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **Createfavorite**
    - 请求参数变更
      - `+ is_global`
    - 响应参数变更
      - `+ is_global`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 支持接口`ShowRabbitMqProductCores`、`ShowCesHierarchy`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListPostgresqlListHistoryTables`、`ListHistoryDatabase`、`BatchRestorePostgreSqlTables`、`BatchRestoreDatabase`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListInstancesResourceMetrics`、`ListInstancesRecommendation`

# 3.1.65 2023-11-09

### HuaweiCloud SDK TICS

- _新增特性_
  - 支持可信智能计算服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK VPN

- _新增特性_
  - 支持虚拟专用网络服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ASM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowMesh**
    - 响应参数变更
      - `- spec.region`
      - `- spec.extendParams.clusters.region`
  - **DeleteMesh**
    - 响应参数变更
      - `- spec.region`
      - `- spec.extendParams.clusters.region`
  - **CreateMesh**
    - 请求参数变更
      - `- spec.region`
      - `- spec.extendParams.clusters.region`
    - 响应参数变更
      - `- spec.region`
      - `- spec.extendParams.clusters.region`
  - **ListMeshes**
    - 响应参数变更
      - `- items.spec.region`
      - `- items.spec.extendParams.clusters.region`

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAddonInstance**
    - 响应参数变更
      - `+ status.status: enum value [unknown]`
  - **UpdateAddonInstance**
    - 响应参数变更
      - `+ status.status: enum value [unknown]`
  - **RollbackAddonInstance**
    - 响应参数变更
      - `+ status.status: enum value [unknown]`
  - **ShowCluster**
    - 响应参数变更
      - `+ spec.serviceNetwork`
  - **UpdateCluster**
    - 响应参数变更
      - `+ spec.serviceNetwork`
  - **DeleteCluster**
    - 响应参数变更
      - `+ spec.serviceNetwork`
  - **CreateAddonInstance**
    - 响应参数变更
      - `+ status.status: enum value [unknown]`
  - **ListAddonInstances**
    - 响应参数变更
      - `+ items.status.status: enum value [unknown]`
  - **CreateCluster**
    - 请求参数变更
      - `+ spec.serviceNetwork`
    - 响应参数变更
      - `+ spec.serviceNetwork`
  - **ListClusters**
    - 响应参数变更
      - `+ items.spec.serviceNetwork`
  - **ShowNode**
    - 响应参数变更
      - `- status.phase: enum value [Installed,ShutDown]`
  - **UpdateNode**
    - 响应参数变更
      - `- status.phase: enum value [Installed,ShutDown]`
  - **DeleteNode**
    - 响应参数变更
      - `- status.phase: enum value [Installed,ShutDown]`
  - **CreateNode**
    - 响应参数变更
      - `- status.phase: enum value [Installed,ShutDown]`
  - **ListNodes**
    - 响应参数变更
      - `- items.status.phase: enum value [Installed,ShutDown]`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`CheckMigrationConnectivity`
  - **ListBackupRecords**
    - 响应参数变更
      - `+ backup_record_response.backup_format`
      - `+ backup_record_response.execution_at`

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持接口`ListQueueProperty`、`UpdateQueueProperty`、`CreateQueueProperty`、`DeleteQueueProperty`
- _解决问题_
  - 无
- _特性变更_
  - **ShowSqlJobStatus**
    - 响应参数变更
      - `+ user_conf`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowNextflowJob**
    - 响应参数变更
      - `+ priority`
  - **ListDrugJob**
    - 响应参数变更
      - `- jobs.priority`
  - **ShowSynthesisJob**
    - 响应参数变更
      - `- basic_info.priority`
  - **ShowFepJob**
    - 响应参数变更
      - `- basic_info.priority`
  - **ShowPocketDetectionJob**
    - 响应参数变更
      - `- basic_info.priority`
  - **ShowAdmetJob**
    - 响应参数变更
      - `- basic_info.priority`
      - `- models.value_range.lower_inclusive`
      - `- models.value_range.upper_inclusive`
      - `* models.value_range.lower: number -> float`
      - `* models.value_range.upper: number -> float`
      - `* models.value_range: object<ValueRange> -> object<ValueRange2>`
  - **ShowPocketMolDesignJob**
    - 响应参数变更
      - `- basic_info.priority`
      - `- model_list.value_range.lower_inclusive`
      - `- model_list.value_range.upper_inclusive`
      - `* model_list.value_range.lower: number -> float`
      - `* model_list.value_range.upper: number -> float`
      - `* model_list.value_range: object<ValueRange> -> object<ValueRange2>`
  - **ShowOptmJob**
    - 响应参数变更
      - `- basic_info.priority`
      - `- models.value_range.lower_inclusive`
      - `- models.value_range.upper_inclusive`
      - `* models.value_range.lower: number -> float`
      - `* models.value_range.upper: number -> float`
      - `* models.value_range: object<ValueRange> -> object<ValueRange2>`
  - **ShowDockingJob**
    - 响应参数变更
      - `- basic_info.priority`
  - **ListDrugModel**
    - 响应参数变更
      - `- models.value_range.lower_inclusive`
      - `- models.value_range.upper_inclusive`
      - `* models.value_range.lower: number -> float`
      - `* models.value_range.upper: number -> float`
      - `* models.value_range: object<ValueRange> -> object<ValueRange2>`

### HuaweiCloud SDK GES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListGraphs2**
    - 响应参数变更
      - `+ graphs.origin_graph_size_type_index`
      - `+ graphs.expand_time`
      - `+ graphs.resize_time`
      - `+ graphs.enable_multi_label`
  - **CreateGraph2**
    - 请求参数变更
      - `+ graph.enable_multi_label`
  - **ShowGraph2**
    - 响应参数变更
      - `+ graph.origin_graph_size_type_index`
      - `+ graph.expand_time`
      - `+ graph.resize_time`
      - `+ graph.enable_multi_label`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`ShowInstanceConfigs`、`ModifyInstanceConfigs`
- _解决问题_
  - 无
- _特性变更_
  - **BatchRestartOrDeleteInstances**
    - 请求参数变更
      - `+ all_failure`
      - `- allFailure`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BatchRestartOrDeleteInstances**
    - 请求参数变更
      - `+ all_failure`
      - `- allFailure`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BatchDeleteInstances**
    - 请求参数变更
      - `+ all_failure`
      - `- allFailure`
  - **DeleteRocketMqMigrationTask**
    - 请求参数变更
      - `+ task_ids`
      - `- taskIds`

### HuaweiCloud SDK SCM

- _新增特性_
  - 支持接口`BatchPushCertificate`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Workspace

- _新增特性_
  - 支持以下接口：
    - `BatchRebuildDesktopsSystemDisk`
    - `ShowDesktopNetwork`
    - `ChangeDesktopNetwork`
    - `ShowTagByDesktopId`
    - `CreateTag`
    - `DeleteTag`
    - `ListProjectTags`
    - `BatchChangeTags`
    - `ListDesktopByTags`
- _解决问题_
  - 无
- _特性变更_
  - **BatchDeleteDesktops**
    - 请求参数变更
      - `+ is_force_delete`
  - **ListDesktops**
    - 请求参数变更
      - `+ enterprise_project_id`
      - `+ desktop_type`
    - 响应参数变更
      - `+ desktops.attach_user_infos`
      - `+ desktops.enterprise_project_id`
      - `+ desktops.in_maintenance_mode`
  - **CreateDesktop**
    - 请求参数变更
      - `+ desktop_name`
      - `+ size`
      - `+ enterprise_project_id`
      - `+ desktop_type: enum value [SHARED]`
      - `+ desktops.user_phone`
  - **ApplyDesktopsInternet**
    - 请求参数变更
      - `+ enterprise_project_id`
  - **ListDesktopsEips**
    - 请求参数变更
      - `+ enterprise_project_id`
    - 响应参数变更
      - `+ eips.enterprise_project_id`
  - **ListUsersOfGroup**
    - 请求参数变更
      - `+ description`
      - `+ active_type`
    - 响应参数变更
      - `+ users.description`
  - **ListProducts**
    - 响应参数变更
      - `+ products.data_disk_size`
      - `+ products.default_desktop_num`
      - `+ products.max_apply_desktop_num`
  - **ListUsers**
    - 请求参数变更
      - `+ group_name`
  - **ListItaSubJobs**
    - 请求参数变更
      - `+ desktop_pool_id`
    - 响应参数变更
      - `+ jobs.desktop_name`
      - `+ jobs.ip_address`
      - `+ jobs.mac_address`
  - **ListWorkspaces**
    - 响应参数变更
      - `+ dc_vnc_ip`
  - **UpdateWorkspace**
    - 请求参数变更
      - `+ dc_vnc_ip`
    - 响应参数变更
      - `+ dc_vnc_ip`
  - **DeleteDesktop**
    - 请求参数变更
      - `+ is_force_delete`
  - **ShowDesktopDetail**
    - 响应参数变更
      - `+ desktop.user_list`
      - `+ desktop.user_group_list`
      - `+ desktop.attach_user_infos`
      - `+ desktop.attach_state`
      - `+ desktop.enterprise_project_id`
  - **ListDesktopsDetail**
    - 请求参数变更
      - `+ user_names`
      - `+ sort_field`
      - `+ sort_type`
      - `+ user_attached`
      - `+ enterprise_project_id`
      - `+ image_id`
      - `+ charge_mode`
      - `+ in_maintenance_mode`
      - `* desktop_id: string -> list<string>`
    - 响应参数变更
      - `+ desktops.user_list`
      - `+ desktops.user_group_list`
      - `+ desktops.attach_user_infos`
      - `+ desktops.attach_state`
      - `+ desktops.enterprise_project_id`

# 3.1.64 2023-11-02

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListApisV2**
    - 请求参数变更
      - `+ vpc_channel_name`

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListPostalAddress`、`UpdatePostal`、`CreatePostal`、`DeletePostal`
  - **ListCustomerselfResourceRecordDetails**
    - 响应参数变更
      - `+ monthly_records.id`

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListCustomerselfResourceRecordDetails**
    - 响应参数变更
      - `+ monthly_records.id`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`StartChat`、`SyncChat`、`SyncGetChatResult`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSMS

- _新增特性_
  - 支持接口`RotateSecret`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持以下接口：
    - `ShowConfigHistoryDetail`
    - `UpdateClientIpTransparentTransmission`
    - `UpdateInstanceConfig`
    - `ListInstanceOperations`
    - `ExportInstancesTask`
    - `ExportExcelJob`
    - `CreateResizeOrder`
    - `ShowExpireAutoScanConfig`
    - `UpdateExpireAutoScanConfig`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ShowNodesInformation`、`ShowBackUpInfo`、`CreateOrUpdateBackUpInfo`、`CreateConnectivityTest`

### HuaweiCloud SDK DNS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowPrivateZone**
    - 响应参数变更
      - `+ enterprise_project_id`
      - `+ proxy_pattern`

### HuaweiCloud SDK DRS

- _新增特性_
  - 支持接口`CollectPositionAsync`、`ShowPositionResult`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持以下接口：
    - `ExecuteClusterUpgradeAction`
    - `ListUpdatableVersion`
    - `ListUpdateRecord`
    - `CheckTableRestore`
    - `RestoreTable`
    - `ListSnapshotCrossRegion`
    - `ListSnapshotCrossRegionPolicy`
    - `AddSnapshotCrossRegionPolicy`
    - `DeleteSnapshotCrossRegionPolicy`
    - `StopWorkloadPlan`
    - `ShowWorkloadPlan`
    - `DeleteWorkloadPlan`
    - `StartWorkloadPlan`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持以下接口：
    - `ListNodes`
    - `ListScalingHistory`
    - `ListPolicyEvents`
    - `CreatePocketDetectionJob`
    - `ShowPocketDetectionJob`
    - `CreateAdmetJob`
    - `ShowAdmetJob`
    - `CreatePocketMolDesignJob`
    - `ShowPocketMolDesignJob`
    - `ListDrugModel`
    - `CreateDrugModel`
    - `UpdateDrugModel`
    - `DeleteDrugModel`
- _解决问题_
  - 无
- _特性变更_
  - **CreateDrugLigandSvg**
    - 请求参数变更
      - `+ scaffold`
  - **CreateNextflowJob**
    - 请求参数变更
      - `+ priority`
  - **CreateDrugLigandSimilarityGraphTask**
    - 请求参数变更
      - `+ mode: enum value [FREE]`
  - **ListDrugJob**
    - 响应参数变更
      - `+ jobs.priority`
  - **ShowSynthesisJob**
    - 响应参数变更
      - `+ basic_info.priority`
  - **ShowFepJob**
    - 响应参数变更
      - `+ part_failed_reason`
      - `+ basic_info.priority`
  - **ParseDrugReceptorInfo**
    - 响应参数变更
      - `* ligands.bounding_box: object<BoundingBoxDto> -> object<DrugBoundingBoxDto>`
  - **RecognizeDrugReceptorPocket**
    - 响应参数变更
      - `* pockets: list<BoundingBoxDto> -> list<DrugBoundingBoxDto>`
  - **CreateOptmJob**
    - 请求参数变更
      - `+ molecule_file`
      - `+ sampler_mixin_weight`
      - `+ model_ids`
      - `+ strong_constraints.id`
      - `+ binding_site.bounding_box.padding`
      - `* body: object<DrugFile> -> object<ReceptorDrugFile>`
      - `+ weak_constraints.id`
  - **ShowOptmJob**
    - 响应参数变更
      - `+ models`
      - `+ sampler_mixin_weight`
      - `+ molecule_file`
      - `+ basic_info.priority`
      - `+ strong_constraints.id`
      - `+ binding_site.bounding_box.padding`
      - `* body: object<DrugFile> -> object<ReceptorDrugFile>`
      - `+ weak_constraints.id`
  - **CreateDockingJob**
    - 请求参数变更
      - `+ receptors.bounding_box.padding`
      - `* body: object<DrugFile> -> object<ReceptorDrugFile>`
  - **ShowDockingJob**
    - 响应参数变更
      - `+ part_failed_reason`
      - `+ basic_info.priority`
      - `+ receptors.bounding_box.padding`
      - `* body: object<DrugFile> -> object<ReceptorDrugFile>`

### HuaweiCloud SDK ELB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListListeners**
    - 请求参数变更
      - `+ proxy_protocol_enable`
    - 响应参数变更
      - `+ listeners.proxy_protocol_enable`
      - `+ listeners.insert_headers.X-Forwarded-Proto`
      - `+ listeners.insert_headers.X-Real-IP`
      - `+ listeners.insert_headers.X-Forwarded-ELB-ID`
      - `+ listeners.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listeners.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listeners.insert_headers.X-Forwarded-TLS-Cipher`
  - **CreateListener**
    - 请求参数变更
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
    - 响应参数变更
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
  - **ShowListener**
    - 响应参数变更
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
  - **UpdateListener**
    - 请求参数变更
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
    - 响应参数变更
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
  - **CreatePool**
    - 请求参数变更
      - `+ pool.ip_version`
  - **UpdatePool**
    - 请求参数变更
      - `+ pool.any_port_enable`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持以下接口：
    - `ShowIntelligentDiagnosisAbnormalCountOfInstances`
    - `ShowIntelligentDiagnosisInstanceInfosPerMetric`
    - `ShrinkGaussMySqlProxy`
    - `ShowInstanceDatabaseVersion`
    - `CopyInstanceConfigurations`
    - `ShowAutoScalingPolicy`
    - `UpdateAutoScalingPolicy`
    - `CheckResource`
    - `UpdateInstanceConfigurations`
- _解决问题_
  - 无
- _特性变更_
  - **DeleteGaussMySqlBackup**
    - 响应参数变更
      - `+ backup_id`
      - `+ backup_name`
      - `- job_id`
  - **CreateGaussMySqlProxy**
    - 请求参数变更
      - `+ subnet_id`
  - **ShowGaussMySqlBackupList**
    - 请求参数变更
      - `+ name`
      - `+ instance_name`
    - 响应参数变更
      - `+ backups.instance_name`
      - `- backups.status: enum value [BUILDING,COMPLETED,FAILED,AVAILABLE]`
      - `- backups.type: enum value [auto,manual]`
  - **ShowGaussMySqlProxyList**
    - 响应参数变更
      - `+ proxy_list.proxy.subnet_id`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 支持接口`DeleteDatabase`
- _解决问题_
  - 无
- _特性变更_
  - **ListInstances**
    - 请求参数变更
      - `+ charge_mode`
  - **ListInstancesDetails**
    - 请求参数变更
      - `+ charge_mode`

### HuaweiCloud SDK HSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSwrImageRepository**
    - 响应参数变更
      - `+ data_list.scannable`
      - `- data_list.scanable`

### HuaweiCloud SDK KPS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ImportPrivateKey**
    - 响应参数变更
      - `+ keypair.user_id`
      - `+ keypair.key_protection`
      - `* keypair: object<KeypairBean> -> object<ImportPrivateKeyAction>`

### HuaweiCloud SDK NAT

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListNatGatewayDnatRules**
    - 响应参数变更
      - `+ dnat_rules.global_eip_id`
      - `+ dnat_rules.global_eip_address`
  - **CreateNatGatewayDnatRule**
    - 请求参数变更
      - `+ dnat_rule.global_eip_id`
    - 响应参数变更
      - `+ dnat_rule.global_eip_id`
      - `+ dnat_rule.global_eip_address`
  - **ShowNatGatewayDnatRule**
    - 响应参数变更
      - `+ dnat_rule.global_eip_id`
      - `+ dnat_rule.global_eip_address`
  - **UpdateNatGatewayDnatRule**
    - 请求参数变更
      - `+ dnat_rule.global_eip_id`
    - 响应参数变更
      - `+ dnat_rule.global_eip_id`
      - `+ dnat_rule.global_eip_address`
  - **BatchCreateNatGatewayDnatRules**
    - 请求参数变更
      - `+ dnat_rules.global_eip_id`
    - 响应参数变更
      - `+ dnat_rules.global_eip_id`
      - `+ dnat_rules.global_eip_address`
  - **ListNatGatewaySnatRules**
    - 响应参数变更
      - `+ snat_rules.global_eip_id`
      - `+ snat_rules.global_eip_address`
  - **CreateNatGatewaySnatRule**
    - 请求参数变更
      - `+ snat_rule.global_eip_id`
    - 响应参数变更
      - `+ snat_rule.global_eip_id`
      - `+ snat_rule.global_eip_address`
  - **ShowNatGatewaySnatRule**
    - 响应参数变更
      - `+ snat_rule.global_eip_id`
      - `+ snat_rule.global_eip_address`
  - **UpdateNatGatewaySnatRule**
    - 请求参数变更
      - `+ snat_rule.global_eip_id`
    - 响应参数变更
      - `+ snat_rule.global_eip_address`
      - `+ snat_rule.global_eip_id`
  - **ListNatGateways**
    - 响应参数变更
      - `+ nat_gateways.ngport_ip_address`
      - `+ nat_gateways.billing_info`
      - `+ nat_gateways.dnat_rules_limit`
      - `+ nat_gateways.snat_rule_public_ip_limit`
  - **CreateNatGateway**
    - 请求参数变更
      - `+ nat_gateway.ngport_ip_address`
    - 响应参数变更
      - `+ nat_gateway.ngport_ip_address`
      - `+ nat_gateway.billing_info`
      - `+ nat_gateway.dnat_rules_limit`
      - `+ nat_gateway.snat_rule_public_ip_limit`
  - **ShowNatGateway**
    - 响应参数变更
      - `+ nat_gateway.ngport_ip_address`
      - `+ nat_gateway.billing_info`
      - `+ nat_gateway.dnat_rules_limit`
      - `+ nat_gateway.snat_rule_public_ip_limit`
  - **UpdateNatGateway**
    - 响应参数变更
      - `+ nat_gateway.ngport_ip_address`
      - `+ nat_gateway.billing_info`
      - `+ nat_gateway.dnat_rules_limit`
      - `+ nat_gateway.snat_rule_public_ip_limit`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateRocketMqMigrationTask**
    - 请求参数变更
      - `* body: string -> map<string, object>`

### HuaweiCloud SDK SecMaster

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListIncidentTypes`
  - **ListAlertRuleMetrics**
    - 响应参数变更
      - `+ metric`
      - `+ category`
      - `- body`
  - **CreateBatchOrderAlerts**
    - 请求参数变更
      - `- incident_id`
      - `- event_content`
      - `- marked_evidence`
      - `- incident_content.type_category`
      - `- incident_content.evidence_list`
      - `- incident_content.note_list`
      - `- incident_content.attachment_list`
      - `- incident_content.description`
      - `- incident_content.incident_type.layoutId`
    - 响应参数变更
      - `* data: object<BatchOrderAlertResult> -> object<BatchOperateAlertResult>`
  - **ShowAlertRule**
    - 响应参数变更
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
  - **UpdateAlertRule**
    - 请求参数变更
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
    - 响应参数变更
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
  - **CreateAlertRuleSimulation**
    - 请求参数变更
      - `- query_type: enum value [CBSL]`
  - **ShowAlertRuleTemplate**
    - 响应参数变更
      - `- query_type: enum value [CBSL]`
  - **ListPlaybooks**
    - 请求参数变更
      - `- component_id`
      - `* offset: optional -> required`
      - `* limit: optional -> required`
  - **CreatePlaybook**
    - 请求参数变更
      - `- approve_role`
      - `- user_role`
      - `- edit_role`
      - `- owner_id`
  - **ListPlaybookActions**
    - 请求参数变更
      - `* limit: optional -> required`
      - `* offset: optional -> required`
    - 响应参数变更
      - `- data.sort_order`
  - **CreatePlaybookAction**
    - 响应参数变更
      - `- data.sort_order`
  - **UpdatePlaybookAction**
    - 响应参数变更
      - `- data.sort_order`
  - **ListDataobjectRelations**
    - 请求参数变更
      - `+ order: enum value [DESC,ASC]`
      - `* condition.conditions.data: list<string> -> list<object>`
      - `* condition.conditions: list<ConditonInfo> -> list<object>`
      - `* condition.logics: list<string> -> list<object>`
    - 响应参数变更
      - `+ success`
      - `+ data.data_object`
      - `+ data.dataclass_ref`
      - `+ data.format_version`
      - `+ data.version`
      - `+ data.workspace_id`
      - `- data.dataclass_id`
      - `- data.name`
      - `- data.type`
      - `- data.content`
      - `* data: list<DataobjectInfo> -> list<DataObjectDetail>`
  - **CreateDataobjectRelations**
    - 请求参数变更
      - `* body: object<CreateRelation> -> object<CreateDataobjectRelationsRequestBody>`
  - **DeleteDataobjectRelations**
    - 请求参数变更
      - `* body: object<CreateRelation> -> object<CreateDataobjectRelationsRequestBody>`
    - 响应参数变更
      - `- total`
      - `- offset`
      - `- success`
      - `- limit`
      - `- request_id`
      - `* data: object<DataResponse> -> object<BatchOperateDataobjectResult>`
  - **ListAlerts**
    - 请求参数变更
      - `+ order: enum value [DESC,ASC]`
      - `* condition.conditions.data: list<string> -> list<object>`
      - `* condition.conditions: list<ConditonInfo> -> list<object>`
      - `* condition.logics: list<string> -> list<object>`
    - 响应参数变更
      - `* data.data_object.network_list.src_port: string -> int32`
      - `* data.data_object.sla: int32 -> string`
      - `* data.data_object.simulation: boolean -> string`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
  - **DeleteAlert**
    - 请求参数变更
      - `+ batch_ids`
      - `- ids`
      - `* body: object<DeleteAlert> -> object<DeleteAlertRequestBody>`
    - 响应参数变更
      - `* data: object<DataResponse> -> object<BatchOperateAlertResult>`
  - **CreateAlert**
    - 请求参数变更
      - `+ data_object.domain_id`
      - `+ data_object.region_id`
      - `+ data_object.labels`
      - `+ data_object.creator`
      - `- data_object.label`
      - `- data_object.chop_phase`
      - `- data_object.ppdr_phase`
      - `- data_object.cteator`
      - `+ data_object.environment.cross_workspace_id`
      - `+ data_object.data_source.company_name`
      - `+ data_object.data_source.product_module`
      - `+ data_object.severity: enum value [Tips,Low,Medium,High,Fatal]`
      - `+ data_object.alert_type.category`
      - `+ data_object.alert_type.alert_type`
      - `* data_object.network_list.direction: object -> string`
      - `* data_object.network_list.src_port: string -> int32`
      - `+ data_object.network_list.src_geo.latitude`
      - `+ data_object.network_list.src_geo.longitude`
      - `+ data_object.network_list.src_geo.city_code`
      - `+ data_object.network_list.src_geo.country_code`
      - `+ data_object.network_list.dest_geo.latitude`
      - `+ data_object.network_list.dest_geo.longitude`
      - `+ data_object.network_list.dest_geo.city_code`
      - `+ data_object.network_list.dest_geo.country_code`
      - `+ data_object.resource_list.provider`
      - `+ data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `* data_object.simulation: boolean -> string`
      - `+ data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data_object.process.process_parent_name`
      - `+ data_object.process.process_parent_path`
      - `+ data_object.process.process_parent_pid`
      - `+ data_object.process.process_parent_uid`
      - `+ data_object.process.process_parent_cmdline`
      - `+ data_object.process.process_child_name`
      - `+ data_object.process.process_child_path`
      - `+ data_object.process.process_child_pid`
      - `+ data_object.process.process_child_uid`
      - `+ data_object.process.process_child_cmdline`
      - `+ data_object.process.process_launche_time`
      - `+ data_object.process.process_terminate_time`
      - `* data_object.process.process_pid: string -> int32`
      - `* data_object.process.process_uid: string -> int32`
      - `* data_object: object<CreateAlert> -> object<Alert>`
    - 响应参数变更
      - `- data.type`
      - `+ data.data_object.domain_id`
      - `+ data.data_object.region_id`
      - `+ data.data_object.labels`
      - `+ data.data_object.data_source`
      - `+ data.data_object.severity`
      - `+ data.data_object.creator`
      - `- data.data_object.datasource`
      - `- data.data_object.serverity`
      - `- data.data_object.chop_phase`
      - `- data.data_object.ppdr_phase`
      - `- data.data_object.cteator`
      - `+ data.data_object.environment.cross_workspace_id`
      - `+ data.data_object.alert_type.category`
      - `+ data.data_object.alert_type.alert_type`
      - `* data.data_object.network_list.direction: object -> string`
      - `* data.data_object.network_list.src_port: string -> int32`
      - `+ data.data_object.network_list.src_geo.latitude`
      - `+ data.data_object.network_list.src_geo.longitude`
      - `+ data.data_object.network_list.src_geo.city_code`
      - `+ data.data_object.network_list.src_geo.country_code`
      - `+ data.data_object.network_list.dest_geo.latitude`
      - `+ data.data_object.network_list.dest_geo.longitude`
      - `+ data.data_object.network_list.dest_geo.city_code`
      - `+ data.data_object.network_list.dest_geo.country_code`
      - `+ data.data_object.resource_list.provider`
      - `+ data.data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data.data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data.data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `* data.data_object.simulation: boolean -> string`
      - `+ data.data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data.data_object.process.process_parent_name`
      - `+ data.data_object.process.process_parent_path`
      - `+ data.data_object.process.process_parent_pid`
      - `+ data.data_object.process.process_parent_uid`
      - `+ data.data_object.process.process_parent_cmdline`
      - `+ data.data_object.process.process_child_name`
      - `+ data.data_object.process.process_child_path`
      - `+ data.data_object.process.process_child_pid`
      - `+ data.data_object.process.process_child_uid`
      - `+ data.data_object.process.process_child_cmdline`
      - `+ data.data_object.process.process_launche_time`
      - `+ data.data_object.process.process_terminate_time`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
  - **ShowAlert**
    - 响应参数变更
      - `- data.type`
      - `+ data.data_object.domain_id`
      - `+ data.data_object.region_id`
      - `+ data.data_object.labels`
      - `+ data.data_object.data_source`
      - `+ data.data_object.severity`
      - `+ data.data_object.creator`
      - `- data.data_object.datasource`
      - `- data.data_object.serverity`
      - `- data.data_object.chop_phase`
      - `- data.data_object.ppdr_phase`
      - `- data.data_object.cteator`
      - `+ data.data_object.environment.cross_workspace_id`
      - `* data.data_object.count: string -> int32`
      - `+ data.data_object.alert_type.category`
      - `+ data.data_object.alert_type.alert_type`
      - `* data.data_object.network_list.direction: object -> string`
      - `* data.data_object.network_list.src_port: string -> int32`
      - `+ data.data_object.network_list.src_geo.latitude`
      - `+ data.data_object.network_list.src_geo.longitude`
      - `+ data.data_object.network_list.src_geo.city_code`
      - `+ data.data_object.network_list.src_geo.country_code`
      - `+ data.data_object.network_list.dest_geo.latitude`
      - `+ data.data_object.network_list.dest_geo.longitude`
      - `+ data.data_object.network_list.dest_geo.city_code`
      - `+ data.data_object.network_list.dest_geo.country_code`
      - `+ data.data_object.resource_list.provider`
      - `+ data.data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data.data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data.data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `* data.data_object.simulation: boolean -> string`
      - `+ data.data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data.data_object.process.process_parent_name`
      - `+ data.data_object.process.process_parent_path`
      - `+ data.data_object.process.process_parent_pid`
      - `+ data.data_object.process.process_parent_uid`
      - `+ data.data_object.process.process_parent_cmdline`
      - `+ data.data_object.process.process_child_name`
      - `+ data.data_object.process.process_child_path`
      - `+ data.data_object.process.process_child_pid`
      - `+ data.data_object.process.process_child_uid`
      - `+ data.data_object.process.process_child_cmdline`
      - `+ data.data_object.process.process_launche_time`
      - `+ data.data_object.process.process_terminate_time`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
      - `* data.data_object: object<ShowAlertRsp> -> object<Alert>`
      - `* data: object<ShowAlertDetail> -> object<AlertDetail>`
  - **ChangeAlert**
    - 请求参数变更
      - `+ batch_ids`
      - `+ data_object.domain_id`
      - `+ data_object.region_id`
      - `+ data_object.labels`
      - `+ data_object.data_source`
      - `+ data_object.severity`
      - `+ data_object.creator`
      - `- data_object.datasource`
      - `- data_object.serverity`
      - `- data_object.chop_phase`
      - `- data_object.ppdr_phase`
      - `- data_object.cteator`
      - `+ data_object.environment.cross_workspace_id`
      - `+ data_object.alert_type.category`
      - `+ data_object.alert_type.alert_type`
      - `* data_object.network_list.direction: object -> string`
      - `* data_object.network_list.src_port: string -> int32`
      - `+ data_object.network_list.src_geo.latitude`
      - `+ data_object.network_list.src_geo.longitude`
      - `+ data_object.network_list.src_geo.city_code`
      - `+ data_object.network_list.src_geo.country_code`
      - `+ data_object.network_list.dest_geo.latitude`
      - `+ data_object.network_list.dest_geo.longitude`
      - `+ data_object.network_list.dest_geo.city_code`
      - `+ data_object.network_list.dest_geo.country_code`
      - `+ data_object.resource_list.provider`
      - `+ data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `* data_object.simulation: boolean -> string`
      - `+ data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data_object.process.process_parent_name`
      - `+ data_object.process.process_parent_path`
      - `+ data_object.process.process_parent_pid`
      - `+ data_object.process.process_parent_uid`
      - `+ data_object.process.process_parent_cmdline`
      - `+ data_object.process.process_child_name`
      - `+ data_object.process.process_child_path`
      - `+ data_object.process.process_child_pid`
      - `+ data_object.process.process_child_uid`
      - `+ data_object.process.process_child_cmdline`
      - `+ data_object.process.process_launche_time`
      - `+ data_object.process.process_terminate_time`
      - `* data_object.process.process_pid: string -> int32`
      - `* data_object.process.process_uid: string -> int32`
    - 响应参数变更
      - `- data.type`
      - `+ data.data_object.domain_id`
      - `+ data.data_object.region_id`
      - `+ data.data_object.labels`
      - `+ data.data_object.data_source`
      - `+ data.data_object.severity`
      - `+ data.data_object.creator`
      - `- data.data_object.datasource`
      - `- data.data_object.serverity`
      - `- data.data_object.chop_phase`
      - `- data.data_object.ppdr_phase`
      - `- data.data_object.cteator`
      - `+ data.data_object.environment.cross_workspace_id`
      - `+ data.data_object.alert_type.category`
      - `+ data.data_object.alert_type.alert_type`
      - `* data.data_object.network_list.direction: object -> string`
      - `* data.data_object.network_list.src_port: string -> int32`
      - `+ data.data_object.network_list.src_geo.latitude`
      - `+ data.data_object.network_list.src_geo.longitude`
      - `+ data.data_object.network_list.src_geo.city_code`
      - `+ data.data_object.network_list.src_geo.country_code`
      - `+ data.data_object.network_list.dest_geo.latitude`
      - `+ data.data_object.network_list.dest_geo.longitude`
      - `+ data.data_object.network_list.dest_geo.city_code`
      - `+ data.data_object.network_list.dest_geo.country_code`
      - `+ data.data_object.resource_list.provider`
      - `+ data.data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data.data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data.data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `* data.data_object.simulation: boolean -> string`
      - `+ data.data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data.data_object.process.process_parent_name`
      - `+ data.data_object.process.process_parent_path`
      - `+ data.data_object.process.process_parent_pid`
      - `+ data.data_object.process.process_parent_uid`
      - `+ data.data_object.process.process_parent_cmdline`
      - `+ data.data_object.process.process_child_name`
      - `+ data.data_object.process.process_child_path`
      - `+ data.data_object.process.process_child_pid`
      - `+ data.data_object.process.process_child_uid`
      - `+ data.data_object.process.process_child_cmdline`
      - `+ data.data_object.process.process_launche_time`
      - `+ data.data_object.process.process_terminate_time`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
  - **ListIncidents**
    - 请求参数变更
      - `+ order: enum value [DESC,ASC]`
      - `* condition.conditions.data: list<string> -> list<object>`
      - `* condition.conditions: list<ConditonInfo> -> list<object>`
      - `* condition.logics: list<string> -> list<object>`
    - 响应参数变更
      - `+ data.dataclass_ref`
      - `+ data.format_version`
      - `+ data.id`
      - `+ data.version`
      - `- data.dataclass_id`
      - `- data.layout_id`
      - `- data.name`
      - `- data.type`
      - `- data.dataclass`
      - `+ data.data_object.domain_id`
      - `+ data.data_object.region_id`
      - `+ data.data_object.labels`
      - `+ data.data_object.data_source`
      - `+ data.data_object.severity`
      - `+ data.data_object.creator`
      - `+ data.data_object.system_alert_table`
      - `- data.data_object.datasource`
      - `- data.data_object.serverity`
      - `- data.data_object.chop_phase`
      - `- data.data_object.ppdr_phase`
      - `- data.data_object.cteator`
      - `- data.data_object.system_incident_table`
      - `+ data.data_object.environment.cross_workspace_id`
      - `+ data.data_object.incident_type.category`
      - `+ data.data_object.incident_type.incident_type`
      - `* data.data_object.network_list.direction: object -> string`
      - `* data.data_object.network_list.src_port: string -> int32`
      - `+ data.data_object.network_list.src_geo.latitude`
      - `+ data.data_object.network_list.src_geo.longitude`
      - `+ data.data_object.network_list.src_geo.city_code`
      - `+ data.data_object.network_list.src_geo.country_code`
      - `+ data.data_object.network_list.dest_geo.latitude`
      - `+ data.data_object.network_list.dest_geo.longitude`
      - `+ data.data_object.network_list.dest_geo.city_code`
      - `+ data.data_object.network_list.dest_geo.country_code`
      - `+ data.data_object.resource_list.provider`
      - `+ data.data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data.data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data.data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `+ data.data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data.data_object.process.process_parent_name`
      - `+ data.data_object.process.process_parent_path`
      - `+ data.data_object.process.process_parent_pid`
      - `+ data.data_object.process.process_parent_uid`
      - `+ data.data_object.process.process_parent_cmdline`
      - `+ data.data_object.process.process_child_name`
      - `+ data.data_object.process.process_child_path`
      - `+ data.data_object.process.process_child_pid`
      - `+ data.data_object.process.process_child_uid`
      - `+ data.data_object.process.process_child_cmdline`
      - `+ data.data_object.process.process_launche_time`
      - `+ data.data_object.process.process_terminate_time`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
      - `* data: list<ListIncidentDetail> -> list<IncidentDetail>`
  - **DeleteIncident**
    - 请求参数变更
      - `+ batch_ids`
      - `- ids`
      - `* body: object<DeleteIncident> -> object<DeleteIncidentRequestBody>`
    - 响应参数变更
      - `* data: object<BatchOrderAlertResult> -> object`
  - **CreateIncident**
    - 请求参数变更
      - `+ data_object.domain_id`
      - `+ data_object.region_id`
      - `+ data_object.creator`
      - `+ data_object.system_alert_table`
      - `- data_object.serverity`
      - `- data_object.chop_phase`
      - `- data_object.ppdr_phase`
      - `- data_object.cteator`
      - `- data_object.system_incident_table`
      - `+ data_object.severity: enum value [Tips,Low,Medium,High,Fatal]`
      - `+ data_object.environment.cross_workspace_id`
      - `+ data_object.data_source.company_name`
      - `+ data_object.data_source.product_module`
      - `- data_object.incident_type.id`
      - `- data_object.incident_type.layoutId`
      - `* data_object.network_list.direction: object -> string`
      - `* data_object.network_list.src_port: string -> int32`
      - `+ data_object.network_list.src_geo.latitude`
      - `+ data_object.network_list.src_geo.longitude`
      - `+ data_object.network_list.src_geo.city_code`
      - `+ data_object.network_list.src_geo.country_code`
      - `+ data_object.network_list.dest_geo.latitude`
      - `+ data_object.network_list.dest_geo.longitude`
      - `+ data_object.network_list.dest_geo.city_code`
      - `+ data_object.network_list.dest_geo.country_code`
      - `+ data_object.resource_list.provider`
      - `+ data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `+ data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data_object.process.process_parent_name`
      - `+ data_object.process.process_parent_path`
      - `+ data_object.process.process_parent_pid`
      - `+ data_object.process.process_parent_uid`
      - `+ data_object.process.process_parent_cmdline`
      - `+ data_object.process.process_child_name`
      - `+ data_object.process.process_child_path`
      - `+ data_object.process.process_child_pid`
      - `+ data_object.process.process_child_uid`
      - `+ data_object.process.process_child_cmdline`
      - `+ data_object.process.process_launche_time`
      - `+ data_object.process.process_terminate_time`
      - `* data_object.process.process_pid: string -> int32`
      - `* data_object.process.process_uid: string -> int32`
      - `* data_object: object<CreateIncident> -> object<Incident>`
    - 响应参数变更
      - `+ data.dataclass_ref`
      - `+ data.format_version`
      - `+ data.id`
      - `+ data.version`
      - `- data.dataclass_id`
      - `- data.layout_id`
      - `- data.name`
      - `- data.type`
      - `- data.dataclass`
      - `+ data.data_object.domain_id`
      - `+ data.data_object.region_id`
      - `+ data.data_object.labels`
      - `+ data.data_object.data_source`
      - `+ data.data_object.severity`
      - `+ data.data_object.creator`
      - `+ data.data_object.system_alert_table`
      - `- data.data_object.datasource`
      - `- data.data_object.serverity`
      - `- data.data_object.chop_phase`
      - `- data.data_object.ppdr_phase`
      - `- data.data_object.cteator`
      - `- data.data_object.system_incident_table`
      - `+ data.data_object.environment.cross_workspace_id`
      - `+ data.data_object.incident_type.category`
      - `+ data.data_object.incident_type.incident_type`
      - `* data.data_object.network_list.direction: object -> string`
      - `* data.data_object.network_list.src_port: string -> int32`
      - `+ data.data_object.network_list.src_geo.latitude`
      - `+ data.data_object.network_list.src_geo.longitude`
      - `+ data.data_object.network_list.src_geo.city_code`
      - `+ data.data_object.network_list.src_geo.country_code`
      - `+ data.data_object.network_list.dest_geo.latitude`
      - `+ data.data_object.network_list.dest_geo.longitude`
      - `+ data.data_object.network_list.dest_geo.city_code`
      - `+ data.data_object.network_list.dest_geo.country_code`
      - `+ data.data_object.resource_list.provider`
      - `+ data.data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data.data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data.data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `+ data.data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data.data_object.process.process_parent_name`
      - `+ data.data_object.process.process_parent_path`
      - `+ data.data_object.process.process_parent_pid`
      - `+ data.data_object.process.process_parent_uid`
      - `+ data.data_object.process.process_parent_cmdline`
      - `+ data.data_object.process.process_child_name`
      - `+ data.data_object.process.process_child_path`
      - `+ data.data_object.process.process_child_pid`
      - `+ data.data_object.process.process_child_uid`
      - `+ data.data_object.process.process_child_cmdline`
      - `+ data.data_object.process.process_launche_time`
      - `+ data.data_object.process.process_terminate_time`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
  - **ShowIncident**
    - 响应参数变更
      - `+ data.dataclass_ref`
      - `+ data.format_version`
      - `+ data.id`
      - `+ data.version`
      - `- data.dataclass_id`
      - `- data.layout_id`
      - `- data.name`
      - `- data.type`
      - `- data.dataclass`
      - `+ data.data_object.domain_id`
      - `+ data.data_object.region_id`
      - `+ data.data_object.labels`
      - `+ data.data_object.data_source`
      - `+ data.data_object.severity`
      - `+ data.data_object.creator`
      - `+ data.data_object.system_alert_table`
      - `- data.data_object.datasource`
      - `- data.data_object.serverity`
      - `- data.data_object.chop_phase`
      - `- data.data_object.ppdr_phase`
      - `- data.data_object.cteator`
      - `- data.data_object.system_incident_table`
      - `+ data.data_object.environment.cross_workspace_id`
      - `* data.data_object.count: string -> int32`
      - `+ data.data_object.incident_type.category`
      - `+ data.data_object.incident_type.incident_type`
      - `* data.data_object.network_list.direction: object -> string`
      - `* data.data_object.network_list.src_port: string -> int32`
      - `+ data.data_object.network_list.src_geo.latitude`
      - `+ data.data_object.network_list.src_geo.longitude`
      - `+ data.data_object.network_list.src_geo.city_code`
      - `+ data.data_object.network_list.src_geo.country_code`
      - `+ data.data_object.network_list.dest_geo.latitude`
      - `+ data.data_object.network_list.dest_geo.longitude`
      - `+ data.data_object.network_list.dest_geo.city_code`
      - `+ data.data_object.network_list.dest_geo.country_code`
      - `+ data.data_object.resource_list.provider`
      - `+ data.data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data.data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data.data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `+ data.data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data.data_object.process.process_parent_name`
      - `+ data.data_object.process.process_parent_path`
      - `+ data.data_object.process.process_parent_pid`
      - `+ data.data_object.process.process_parent_uid`
      - `+ data.data_object.process.process_parent_cmdline`
      - `+ data.data_object.process.process_child_name`
      - `+ data.data_object.process.process_child_path`
      - `+ data.data_object.process.process_child_pid`
      - `+ data.data_object.process.process_child_uid`
      - `+ data.data_object.process.process_child_cmdline`
      - `+ data.data_object.process.process_launche_time`
      - `+ data.data_object.process.process_terminate_time`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
      - `* data.data_object: object<ShowIncident> -> object<Incident>`
      - `* data: object<ShowIncidentDetail> -> object<IncidentDetail>`
  - **ChangeIncident**
    - 请求参数变更
      - `+ batch_ids`
      - `+ data_object.domain_id`
      - `+ data_object.region_id`
      - `+ data_object.labels`
      - `+ data_object.data_source`
      - `+ data_object.severity`
      - `+ data_object.creator`
      - `+ data_object.system_alert_table`
      - `- data_object.datasource`
      - `- data_object.serverity`
      - `- data_object.chop_phase`
      - `- data_object.ppdr_phase`
      - `- data_object.cteator`
      - `- data_object.system_incident_table`
      - `+ data_object.environment.cross_workspace_id`
      - `+ data_object.incident_type.category`
      - `+ data_object.incident_type.incident_type`
      - `* data_object.network_list.direction: object -> string`
      - `* data_object.network_list.src_port: string -> int32`
      - `+ data_object.network_list.src_geo.latitude`
      - `+ data_object.network_list.src_geo.longitude`
      - `+ data_object.network_list.src_geo.city_code`
      - `+ data_object.network_list.src_geo.country_code`
      - `+ data_object.network_list.dest_geo.latitude`
      - `+ data_object.network_list.dest_geo.longitude`
      - `+ data_object.network_list.dest_geo.city_code`
      - `+ data_object.network_list.dest_geo.country_code`
      - `+ data_object.resource_list.provider`
      - `+ data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `+ data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data_object.process.process_parent_name`
      - `+ data_object.process.process_parent_path`
      - `+ data_object.process.process_parent_pid`
      - `+ data_object.process.process_parent_uid`
      - `+ data_object.process.process_parent_cmdline`
      - `+ data_object.process.process_child_name`
      - `+ data_object.process.process_child_path`
      - `+ data_object.process.process_child_pid`
      - `+ data_object.process.process_child_uid`
      - `+ data_object.process.process_child_cmdline`
      - `+ data_object.process.process_launche_time`
      - `+ data_object.process.process_terminate_time`
      - `* data_object.process.process_pid: string -> int32`
      - `* data_object.process.process_uid: string -> int32`
    - 响应参数变更
      - `+ data.dataclass_ref`
      - `+ data.format_version`
      - `+ data.id`
      - `+ data.version`
      - `- data.dataclass_id`
      - `- data.layout_id`
      - `- data.name`
      - `- data.type`
      - `- data.dataclass`
      - `+ data.data_object.domain_id`
      - `+ data.data_object.region_id`
      - `+ data.data_object.labels`
      - `+ data.data_object.data_source`
      - `+ data.data_object.severity`
      - `+ data.data_object.creator`
      - `+ data.data_object.system_alert_table`
      - `- data.data_object.datasource`
      - `- data.data_object.serverity`
      - `- data.data_object.chop_phase`
      - `- data.data_object.ppdr_phase`
      - `- data.data_object.cteator`
      - `- data.data_object.system_incident_table`
      - `+ data.data_object.environment.cross_workspace_id`
      - `+ data.data_object.incident_type.category`
      - `+ data.data_object.incident_type.incident_type`
      - `* data.data_object.network_list.direction: object -> string`
      - `* data.data_object.network_list.src_port: string -> int32`
      - `+ data.data_object.network_list.src_geo.latitude`
      - `+ data.data_object.network_list.src_geo.longitude`
      - `+ data.data_object.network_list.src_geo.city_code`
      - `+ data.data_object.network_list.src_geo.country_code`
      - `+ data.data_object.network_list.dest_geo.latitude`
      - `+ data.data_object.network_list.dest_geo.longitude`
      - `+ data.data_object.network_list.dest_geo.city_code`
      - `+ data.data_object.network_list.dest_geo.country_code`
      - `+ data.data_object.resource_list.provider`
      - `+ data.data_object.verification_state: enum value [Unknown,True_Positive,False_Positive]`
      - `+ data.data_object.handle_status: enum value [Open,Block,Closed]`
      - `+ data.data_object.ipdrr_phase: enum value [Prepartion,Detection and Analysis,Containm，Eradication& Recovery,Post-Incident-Activity]`
      - `+ data.data_object.close_reason: enum value [False detection,Resolved,Repeated,Other]`
      - `+ data.data_object.process.process_parent_name`
      - `+ data.data_object.process.process_parent_path`
      - `+ data.data_object.process.process_parent_pid`
      - `+ data.data_object.process.process_parent_uid`
      - `+ data.data_object.process.process_parent_cmdline`
      - `+ data.data_object.process.process_child_name`
      - `+ data.data_object.process.process_child_path`
      - `+ data.data_object.process.process_child_pid`
      - `+ data.data_object.process.process_child_uid`
      - `+ data.data_object.process.process_child_cmdline`
      - `+ data.data_object.process.process_launche_time`
      - `+ data.data_object.process.process_terminate_time`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
  - **ListIndicators**
    - 请求参数变更
      - `- order`
      - `- from_date`
      - `- to_date`
      - `+ from_date`
      - `+ to_date`
      - `- type`
    - 响应参数变更
      - `+ data.dataclass_ref`
      - `- data.dataclass_id`
      - `- data.type`
      - `- data.layout_id`
      - `- data.dataclass`
      - `+ data.data_object.update_time`
      - `+ data.data_object.create_time`
      - `+ data.data_object.environment`
      - `+ data.data_object.data_source`
      - `+ data.data_object.first_report_time`
      - `+ data.data_object.is_deleted`
      - `+ data.data_object.last_report_time`
      - `+ data.data_object.granular_marking`
      - `+ data.data_object.name`
      - `+ data.data_object.id`
      - `+ data.data_object.project_id`
      - `+ data.data_object.revoked`
      - `+ data.data_object.status`
      - `+ data.data_object.verdict`
      - `+ data.data_object.workspace_id`
      - `+ data.data_object.confidence`
      - `+ data.data_object.indicator_type.layout_id`
      - `- data.data_object.indicator_type.layoutId`
  - **CreateIndicator**
    - 请求参数变更
      - `- name`
      - `- format_version`
      - `- type`
      - `- trigger_flag`
      - `- data_object.type`
      - `+ data_object.indicator_type.layout_id`
      - `- data_object.indicator_type.layoutId`
      - `+ data_object.data_object.update_time`
      - `+ data_object.data_object.create_time`
      - `+ data_object.data_object.environment`
      - `+ data_object.data_object.data_source`
      - `+ data_object.data_object.first_report_time`
      - `+ data_object.data_object.is_deleted`
      - `+ data_object.data_object.last_report_time`
      - `+ data_object.data_object.granular_marking`
      - `+ data_object.data_object.name`
      - `+ data_object.data_object.id`
      - `+ data_object.data_object.project_id`
      - `+ data_object.data_object.revoked`
      - `+ data_object.data_object.status`
      - `+ data_object.data_object.verdict`
      - `+ data_object.data_object.workspace_id`
      - `+ data_object.data_object.confidence`
      - `+ data_object.data_object.indicator_type.layout_id`
      - `- data_object.data_object.indicator_type.layoutId`
    - 响应参数变更
      - `+ data.dataclass_ref`
      - `- data.dataclass_id`
      - `- data.type`
      - `- data.layout_id`
      - `- data.dataclass`
      - `+ data.data_object.update_time`
      - `+ data.data_object.create_time`
      - `+ data.data_object.environment`
      - `+ data.data_object.data_source`
      - `+ data.data_object.first_report_time`
      - `+ data.data_object.is_deleted`
      - `+ data.data_object.last_report_time`
      - `+ data.data_object.granular_marking`
      - `+ data.data_object.name`
      - `+ data.data_object.id`
      - `+ data.data_object.project_id`
      - `+ data.data_object.revoked`
      - `+ data.data_object.status`
      - `+ data.data_object.verdict`
      - `+ data.data_object.workspace_id`
      - `+ data.data_object.confidence`
      - `+ data.data_object.indicator_type.layout_id`
      - `- data.data_object.indicator_type.layoutId`
  - **ShowIndicatorDetail**
    - 响应参数变更
      - `+ data.dataclass_ref`
      - `- data.dataclass_id`
      - `- data.type`
      - `- data.layout_id`
      - `- data.dataclass`
      - `+ data.data_object.update_time`
      - `+ data.data_object.create_time`
      - `+ data.data_object.environment`
      - `+ data.data_object.data_source`
      - `+ data.data_object.first_report_time`
      - `+ data.data_object.is_deleted`
      - `+ data.data_object.last_report_time`
      - `+ data.data_object.granular_marking`
      - `+ data.data_object.name`
      - `+ data.data_object.id`
      - `+ data.data_object.project_id`
      - `+ data.data_object.revoked`
      - `+ data.data_object.status`
      - `+ data.data_object.verdict`
      - `+ data.data_object.workspace_id`
      - `+ data.data_object.confidence`
      - `+ data.data_object.indicator_type.layout_id`
      - `- data.data_object.indicator_type.layoutId`
  - **UpdateIndicator**
    - 请求参数变更
      - `- trigger_flag`
      - `+ data_object.update_time`
      - `+ data_object.create_time`
      - `+ data_object.environment`
      - `+ data_object.data_source`
      - `+ data_object.first_report_time`
      - `+ data_object.is_deleted`
      - `+ data_object.last_report_time`
      - `+ data_object.granular_marking`
      - `+ data_object.name`
      - `+ data_object.id`
      - `+ data_object.project_id`
      - `+ data_object.revoked`
      - `+ data_object.status`
      - `+ data_object.verdict`
      - `+ data_object.workspace_id`
      - `+ data_object.confidence`
      - `+ data_object.indicator_type.layout_id`
      - `- data_object.indicator_type.layoutId`
    - 响应参数变更
      - `+ data.dataclass_ref`
      - `- data.dataclass_id`
      - `- data.type`
      - `- data.layout_id`
      - `- data.dataclass`
      - `+ data.data_object.update_time`
      - `+ data.data_object.create_time`
      - `+ data.data_object.environment`
      - `+ data.data_object.data_source`
      - `+ data.data_object.first_report_time`
      - `+ data.data_object.is_deleted`
      - `+ data.data_object.last_report_time`
      - `+ data.data_object.granular_marking`
      - `+ data.data_object.name`
      - `+ data.data_object.id`
      - `+ data.data_object.project_id`
      - `+ data.data_object.revoked`
      - `+ data.data_object.status`
      - `+ data.data_object.verdict`
      - `+ data.data_object.workspace_id`
      - `+ data.data_object.confidence`
      - `+ data.data_object.indicator_type.layout_id`
      - `- data.data_object.indicator_type.layoutId`
  - **ShowPlaybookMonitors**
    - 请求参数变更
      - `+ version_query_type: enum value [ALL:全部，VALID:有效的，DELETED:已删除]`
    - 响应参数变更
      - `* data.total_instance_run_num: int32 -> float`
  - **CreateAlertRule**
    - 请求参数变更
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
    - 响应参数变更
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
  - **ListAlertRules**
    - 响应参数变更
      - `- accumulated_times`
      - `- records.accumulated_times`
      - `- records.query_type: enum value [CBSL]`
  - **ListAlertRuleTemplates**
    - 响应参数变更
      - `- records.query_type: enum value [CBSL]`
  - **CopyPlaybookVersion**
    - 响应参数变更
      - `- data.run_mode`
      - `- data.dataobject_id`
      - `- data.actions.sort_order`
  - **CreatePlaybookRule**
    - 请求参数变更
      - `+ rule.start_type`
      - `+ rule.end_type`
      - `+ rule.end_time`
      - `+ rule.only_once`
      - `+ rule.execution_type`
      - `- rule.repeat_count`
      - `* rule.logics: object -> list<string>`
  - **ListPlaybookInstances**
    - 请求参数变更
      - `- date_type`
      - `* limit: optional -> required`
      - `* offset: optional -> required`
  - **ShowPlaybookTopology**
    - 响应参数变更
      - `- action_instances.action.sort_order`
  - **ListPlaybookVersions**
    - 请求参数变更
      - `- approve_role`
    - 响应参数变更
      - `- data.run_mode`
      - `- data.dataobject_id`
  - **CreatePlaybookVersion**
    - 请求参数变更
      - `- actions.sort_order`
    - 响应参数变更
      - `- data.run_mode`
      - `- data.dataobject_id`
      - `- data.actions.sort_order`
  - **ShowPlaybookVersion**
    - 响应参数变更
      - `- data.run_mode`
      - `- data.dataobject_id`
      - `- data.actions.sort_order`
  - **UpdatePlaybookVersion**
    - 响应参数变更
      - `- data.run_mode`
      - `- data.dataobject_id`
      - `- data.actions.sort_order`
  - **UpdatePlaybookRule**
    - 请求参数变更
      - `+ rule.start_type`
      - `+ rule.end_type`
      - `+ rule.end_time`
      - `+ rule.only_once`
      - `+ rule.execution_type`
      - `- rule.repeat_count`
      - `* rule.logics: object -> list<string>`

# 3.1.63 2023-10-26

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持接口`ShowStackInstance`、`UpdateStackInstances`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDetailsOfApiV2**
    - 响应参数变更
      - `+ policy_functions.conditions.sys_param_name`
      - `+ policy_functions.conditions.cookie_param_name`
      - `+ policy_functions.conditions.frontend_authorizer_param_name`
      - `+ policy_functions.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
  - **UpdateApiV2**
    - 请求参数变更
      - `+ policy_mocks.conditions.sys_param_name`
      - `+ policy_mocks.conditions.cookie_param_name`
      - `+ policy_mocks.conditions.frontend_authorizer_param_name`
      - `+ policy_mocks.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
    - 响应参数变更
      - `+ policy_functions.conditions.sys_param_name`
      - `+ policy_functions.conditions.cookie_param_name`
      - `+ policy_functions.conditions.frontend_authorizer_param_name`
      - `+ policy_functions.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
  - **ListApiVersionDetailV2**
    - 响应参数变更
      - `+ policy_functions.conditions.sys_param_name`
      - `+ policy_functions.conditions.cookie_param_name`
      - `+ policy_functions.conditions.frontend_authorizer_param_name`
      - `+ policy_functions.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
  - **CreateApiV2**
    - 请求参数变更
      - `+ policy_mocks.conditions.sys_param_name`
      - `+ policy_mocks.conditions.cookie_param_name`
      - `+ policy_mocks.conditions.frontend_authorizer_param_name`
      - `+ policy_mocks.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
    - 响应参数变更
      - `+ policy_functions.conditions.sys_param_name`
      - `+ policy_functions.conditions.cookie_param_name`
      - `+ policy_functions.conditions.frontend_authorizer_param_name`
      - `+ policy_functions.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateBareMetalServers**
    - 请求参数变更
      - `+ server.extendparam.chargingMode: enum value [postPaid]`

### HuaweiCloud SDK CC

- _新增特性_
  - 支持接口`ListCentralNetworkCapabilities`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持以下接口：
    - `CreateRefreshTasks`
    - `CreatePreheatingTasks`
    - `ShowHistoryTasks`
    - `ShowHistoryTaskDetails`
    - `ShowUrlTaskInfo`
- _解决问题_
  - 无
- _特性变更_
  - **CreateRefreshTasks**
    - 请求参数变更
      - `+ refresh_task.zh_url_encode`
  - **CreatePreheatingTasks**
    - 请求参数变更
      - `+ preheating_task.zh_url_encode`

### HuaweiCloud SDK CodeArtsPipeline

- _新增特性_
  - 支持接口`CreatePipelineNew`、`RetryPipelineRun`、`AcceptManualReview`、`RejectManualReview`
- _解决问题_
  - 无
- _特性变更_
  - **ListPipelines**
    - 响应参数变更
      - `+ pipelines.latest_run.stage_status_list.id`
  - **CreatePipelineByTemplateId**
    - 请求参数变更
      - `+ variables`

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持以下接口：
    - `ShowBackgroundTaskProgress`
    - `ListCenterTask`
    - `StartInstanceResizeCheckJob`
    - `ShowBackUpInfo`
    - `CreateOrUpdateBackUpInfo`
    - `ShowExpireKeyScanInfo`
    - `ScanExpireKey`
    - `ListMigrationTaskLogs`
    - `CheckMigrationConnectivity`
    - `ExchangeInstanceIp`
    - `ExecuteCommandMobilization`
    - `LoginWebCli`
    - `UpdateMigrationTask`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DLI

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListBatches**
    - 请求参数变更
      - `+ job-name`
  - **CreateBatchJob**
    - 响应参数变更
      - `- req_body`

### HuaweiCloud SDK HSS

- _新增特性_
  - 支持以下接口：
    - `ListContainerNodes`
    - `ListBlockedIp`
    - `ChangeBlockedIp`
    - `ListIsolatedFile`
    - `ChangeIsolatedFile`
    - `ListSwrImageRepository`
    - `BatchScanSwrImage`
    - `ListImageVulnerabilities`
    - `ListVulnerabilityCve`
    - `RunImageSynchronize`
    - `ListImageRiskConfigs`
    - `ListImageRiskConfigRules`
    - `ShowImageCheckRuleDetail`
    - `ShowVulScanPolicy`
    - `ChangeVulScanPolicy`
    - `ShowVulStatics`
- _解决问题_
  - 无
- _特性变更_
  - **ListPortStatistics**
    - 请求参数变更
      - `+ port_string`
      - `+ sort_key`
      - `+ sort_dir`
    - 响应参数变更
      - `+ data_list.status`
  - **ListProtectionServer**
    - 响应参数变更
      - `+ data_list.host_source`
  - **ListHostStatus**
    - 请求参数变更
      - `+ has_intrusion`
      - `+ agent_upgradable`
  - **ListVulHosts**
    - 响应参数变更
      - `+ data_list.support_restore`
  - **ChangeVulStatus**
    - 请求参数变更
      - `+ backup_info_id`
      - `+ custom_backup_hosts`
  - **ListHostVuls**
    - 响应参数变更
      - `+ data_list.app_name`
      - `+ data_list.app_version`
      - `+ data_list.app_path`
      - `+ data_list.version`
      - `+ data_list.support_restore`
  - **ListHostProtectHistoryInfo**
    - 请求参数变更
      - `+ host_name`
      - `+ host_ip`
      - `+ file_path`
      - `+ file_operation`
  - **ListProtectionPolicy**
    - 响应参数变更
      - `+ data_list.deploy_mode`
      - `+ data_list.default_policy`
  - **ListSecurityEvents**
    - 请求参数变更
      - `+ severity_list`
      - `+ attack_tag`
      - `+ asset_value`
      - `+ tag_list`
      - `+ att_ck`
    - 响应参数变更
      - `+ data_list.description`
      - `+ data_list.event_abstract`
      - `+ data_list.tag_list`
      - `+ data_list.resource_info.container_status`
      - `+ data_list.resource_info.pod_uid`
      - `+ data_list.resource_info.pod_name`
      - `+ data_list.resource_info.namespace`
      - `+ data_list.resource_info.cluster_id`
      - `+ data_list.resource_info.cluster_name`
  - **ChangeEvent**
    - 请求参数变更
      - `+ operate_event_list.operate_detail_list.container_id`
      - `+ operate_event_list.operate_detail_list.container_name`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListProducts**
    - 请求参数变更
      - `+ product_name`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ResizeInstance**
    - 请求参数变更
      - `+ tenant_ips`
      - `+ second_tenant_subnet_id`
  - **ResizeEngineInstance**
    - 请求参数变更
      - `+ tenant_ips`
      - `+ second_tenant_subnet_id`

### HuaweiCloud SDK LakeFormation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateLakeFormationInstance**
    - 请求参数变更
      - `- order_id`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 支持接口`RunCreateAudioStreamModerationJob`、`RunCloseAudioStreamModerationJob`、`RunCreateVideoStreamModerationJob`、`RunCloseVideoStreamModerationJob`
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
  - **RecognizeGeneralTable**
    - 请求参数变更
      - `+ with_borders`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListInstanceDiagnosis`、`ListInstancesInfoDiagnosis`
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
  - **ShowGroup**
    - 响应参数变更
      - `+ group_desc`
  - **CreateConsumerGroupOrBatchDeleteConsumerGroup**
    - 请求参数变更
      - `+ group_desc`
  - **ListInstanceConsumerGroups**
    - 响应参数变更
      - `+ groups.group_desc`
  - **BatchUpdateConsumerGroup**
    - 请求参数变更
      - `+ groups.group_desc`

### HuaweiCloud SDK SFSTurbo

- _新增特性_
  - 支持以下接口：
    - `SetHpcCacheBackend`
    - `CreateHpcCacheTask`
    - `ShowHpcCacheTask`
    - `ListHpcCacheTasks`
    - `ListFsTasks`
    - `CreateFsTask`
    - `ShowFsTask`
    - `DeleteFsTask`
    - `ListBackendTargets`
    - `CreateBackendTarget`
    - `ShowBackendTargetInfo`
    - `DeleteBackendTarget`
    - `ShowFsDirUsage`
    - `ListPermRules`
    - `CreatePermRule`
    - `ShowPermRule`
    - `UpdatePermRule`
    - `DeletePermRule`
    - `UpdateHpcShare`
- _解决问题_
  - 无
- _特性变更_
  - **ListShares**
    - 响应参数变更
      - `* shares: list<Shares> -> list<ShareInfo>`

# 3.1.62 2023-10-19

### HuaweiCloud SDK APIG

- _新增特性_
  - 支持以下接口：
    - `CheckApisV2`
    - `ShowAppBoundAppQuota`
    - `CreateOrder`
    - `CreatePrepayResize`
    - `CreatePostPayResizeOrder`
    - `ShowRestrictionOfInstanceV2`
    - `ShowDetailsOfAppAcl`
    - `UpdateAppAcl`
    - `DeleteAppAcl`
    - `ListAppQuotas`
    - `CreateAppQuota`
    - `ShowAppQuota`
    - `UpdateAppQuota`
    - `DeleteAppQuota`
    - `ListAppQuotaBoundApps`
    - `AssociateAppsForAppQuota`
    - `DisassociateAppQuotaWithApp`
    - `ListAppQuotaBindableApps`
    - `UpdateEnvironmentVariableV2`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK AOM

- _新增特性_
  - 支持接口`CreateSubApp`、`UpdateSubApp`、`DeleteSubApp`
- _解决问题_
  - 无
- _特性变更_
  - **CreateApp**
    - 请求参数变更
      - `+ register_type: enum value [CONSOLE,SERVICE_DISCOVERY]`
      - `- register_type: enum value [CONSOLESERVICE_DISCOVERY]`
  - **UpdateApp**
    - 请求参数变更
      - `+ register_type: enum value [CONSOLE,SERVICE_DISCOVERY]`
      - `- register_type: enum value [CONSOLESERVICE_DISCOVERY]`
  - **CreateComponent**
    - 请求参数变更
      - `+ model_type: enum value [APPLICATION,SUB_APPLICATION]`
  - **CreateEnv**
    - 请求参数变更
      - `+ env_type: enum value [DEV,TEST,PRE,ONLINE]`
      - `+ os_type: enum value [LINUX,WINDOWS]`
      - `+ register_type: enum value [API,CONSOLE,SERVICE_DISCOVERY]`
  - **ListResourceUnderNode**
    - 请求参数变更
      - `+ ci_type: enum value [APPLICATION,SUB_APPLICATION,COMPONENT,ENVIRONMENT]`
  - **UpdateEnv**
    - 请求参数变更
      - `+ env_type: enum value [DEV,TEST,PRE,ONLINE]`
      - `+ os_type: enum value [LINUX,WINDOWS]`
      - `+ register_type: enum value [API,CONSOLE,SERVICE_DISCOVERY]`

### HuaweiCloud SDK CAE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListComponentConfigurations**
    - 响应参数变更
      - `* items.data.spec.log_paths: list<object> -> list<string>`
      - `* items.data.spec.metrics: list<object> -> list<string>`
      - `+ items.data.spec.triggers.type: enum value [cron]`
      - `+ items.data.spec.triggers.metadata.period_type`
      - `+ items.data.spec.triggers.metadata.schedulers`
      - `- items.data.spec.triggers.metadata.type: enum value [Utilization]`
      - `* items.data.spec.triggers.metadata: object -> object<ScalingTriggerMeta>`
      - `* items.data.spec.postStart.exec.command: list<object> -> list<string>`
      - `* items.data.spec.livenessProbe.exec.command: list<object> -> list<string>`
      - `* items.data.spec.items.access_control.black: list<object> -> list<string>`
      - `* items.data.spec.items.access_control.white: list<object> -> list<string>`
  - **CreateComponentConfiguration**
    - 请求参数变更
      - `* items.data.spec.log_paths: list<object> -> list<string>`
      - `* items.data.spec.metrics: list<object> -> list<string>`
      - `+ items.data.spec.triggers.type: enum value [cron]`
      - `+ items.data.spec.triggers.metadata.period_type`
      - `+ items.data.spec.triggers.metadata.schedulers`
      - `- items.data.spec.triggers.metadata.type: enum value [Utilization]`
      - `* items.data.spec.triggers.metadata: object -> object<ScalingTriggerMeta>`
      - `* items.data.spec.postStart.exec.command: list<object> -> list<string>`
      - `* items.data.spec.livenessProbe.exec.command: list<object> -> list<string>`
      - `* items.data.spec.items.access_control.black: list<object> -> list<string>`
      - `* items.data.spec.items.access_control.white: list<object> -> list<string>`

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListAgent**
    - 请求参数变更
      - `* agent_id: string -> list<string>`
  - **ListVault**
    - 请求参数变更
      - `* id: string -> list<string>`

### HuaweiCloud SDK CC

- _新增特性_
  - 支持以下接口：
    - `TagCloudConnection`
    - `UntagCloudConnection`
    - `ListCloudConnectionTags`
    - `ListCloudConnectionsByTags`
    - `TagBandwidthPackage`
    - `UntagBandwidthPackage`
    - `ListBandwidthPackageTags`
    - `ListBandwidthPackagesByTags`
    - `ListCentralNetworks`
    - `CreateCentralNetwork`
    - `ShowCentralNetwork`
    - `UpdateCentralNetwork`
    - `DeleteCentralNetwork`
    - `TagCentralNetwork`
    - `UntagCentralNetwork`
    - `ListCentralNetworkTags`
    - `ListCentralNetworkPolicies`
    - `CreateCentralNetworkPolicy`
    - `ApplyCentralNetworkPolicy`
    - `DeleteCentralNetworkPolicy`
    - `ListCentralNetworkPolicyChangeSet`
    - `ListCentralNetworkConnections`
    - `UpdateCentralNetworkConnection`
    - `ListCentralNetworkGdgwAttachments`
    - `CreateCentralNetworkGdgwAttachment`
    - `ShowCentralNetworkGdgwAttachment`
    - `UpdateCentralNetworkGdgwAttachment`
    - `ListCentralNetworkAttachments`
    - `DeleteCentralNetworkAttachment`
    - `ListCentralNetworkQuotas`
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `ListDomainTags`
    - `DeleteTag`
    - `BatchCreateDeleteTags`
    - `ListResourceByFilterTag`
    - `ListTags`
    - `CreateTag`
  - **ListCloudConnections**
    - 请求参数变更
      - `* id: list<string> -> list<UUIDDef>`
  - **ListCloudConnectionRoutes**
    - 请求参数变更
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`
  - **ListAuthorisations**
    - 请求参数变更
      - `* id: list<string> -> list<UUIDDef>`
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`
  - **ListPermissions**
    - 请求参数变更
      - `* id: list<string> -> list<UUIDDef>`
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`
  - **ListCloudConnectionQuotas**
    - 请求参数变更
      - `+ cloud_connection_id`
      - `+ region_id`
  - **ListNetworkInstances**
    - 请求参数变更
      - `* id: list<string> -> list<UUIDDef>`
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`
  - **ListBandwidthPackages**
    - 请求参数变更
      - `+ cloud_connection_id`
      - `* id: list<string> -> list<UUIDDef>`
  - **ListInterRegionBandwidths**
    - 请求参数变更
      - `* id: list<string> -> list<UUIDDef>`
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`

### HuaweiCloud SDK CCM

- _新增特性_
  - 支持接口`CreateCertificateAuthorityOrder`
- _解决问题_
  - 无
- _特性变更_
  - **ExportCertificate**
    - 响应参数变更
      - `+ signed_and_enveloped_data`
  - **ShowCertificateAuthority**
    - 响应参数变更
      - `+ charging_mode`
      - `+ free_quota`
  - **IssueCertificateAuthorityCertificate**
    - 请求参数变更
      - `+ type`
      - `+ distinguished_name`
      - `+ key_algorithm`
      - `+ key_usages`
      - `+ crl_configuration`
  - **CreateCertificateAuthority**
    - 请求参数变更
      - `+ ca_id`
  - **ListCertificateAuthority**
    - 响应参数变更
      - `+ charging_mode`
      - `+ free_quota`
      - `+ certificate_authorities.free_quota`
      - `+ certificate_authorities.charging_mode`

### HuaweiCloud SDK CFW

- _新增特性_
  - 支持以下接口：
    - `ListDomainSets`
    - `AddDomainSet`
    - `UpdateDomainSet`
    - `DeleteDomainSet`
    - `ListFirewallList`
    - `BatchUpdateAclRuleActions`
    - `ListRuleAclTags`
    - `AddDomains`
    - `DeleteDomains`
    - `ListDomains`
    - `BatchDeleteAclRules`
    - `BatchDeleteServiceItems`
    - `BatchDeleteAddressItems`
- _解决问题_
  - 无
- _特性变更_
  - **ListFlowLogs**
    - 请求参数变更
      - `+ dst_host`
    - 响应参数变更
      - `+ data.records.dst_host`
  - **ListAccessControlLogs**
    - 请求参数变更
      - `+ dst_host`
      - `+ rule_name`
      - `+ action`
    - 响应参数变更
      - `+ data.records.src_region_id`
      - `+ data.records.src_region_name`
      - `+ data.records.dst_region_id`
      - `+ data.records.dst_region_name`
      - `+ data.records.dst_host`
  - **ListBlackWhiteLists**
    - 响应参数变更
      - `+ data.records.description`
  - **ListDomainParseDetail**
    - 请求参数变更
      - `+ address_type`
  - **UpdateDnsServers**
    - 请求参数变更
      - `+ health_check_domain_name`
  - **ListDnsServers**
    - 响应参数变更
      - `+ data.health_check_domain_name`
  - **ListAttackLogs**
    - 请求参数变更
      - `+ dst_host`
      - `+ log_type`
    - 响应参数变更
      - `+ data.records.dst_host`
      - `+ data.records.src_region_id`
      - `+ data.records.src_region_name`
      - `+ data.records.dst_region_id`
      - `+ data.records.dst_region_name`
  - **UpdateAclRule**
    - 请求参数变更
      - `+ tag`
      - `+ source.region_list_json`
      - `+ source.region_list`
      - `+ source.domain_set_id`
      - `+ source.domain_set_name`
      - `+ source.ip_address`
      - `+ source.address_group`
      - `+ source.address_group_names`
      - `+ service.custom_service`
      - `+ service.service_group`
      - `+ service.service_group_names`
  - **ListAclRules**
    - 请求参数变更
      - `+ tags_id`
      - `+ source`
      - `+ destination`
      - `+ service`
    - 响应参数变更
      - `+ data.records.tag`
      - `+ data.records.source.region_list_json`
      - `+ data.records.source.region_list`
      - `+ data.records.source.domain_set_id`
      - `+ data.records.source.domain_set_name`
      - `+ data.records.source.ip_address`
      - `+ data.records.source.address_group`
      - `+ data.records.source.address_group_names`
      - `+ data.records.service.custom_service`
      - `+ data.records.service.service_group`
      - `+ data.records.service.service_group_names`
  - **AddBlackWhiteList**
    - 请求参数变更
      - `+ description`
  - **UpdateBlackWhiteList**
    - 请求参数变更
      - `+ description`
  - **ListEipCount**
    - 响应参数变更
      - `+ data.eip_protected_self`
  - **ChangeEipStatus**
    - 响应参数变更
      - `+ data.object_id`
      - `+ data.fail_eip_id_list`
      - `- data.id`
      - `* data: object<IdObject> -> object<EIPSwitchStatusVO>`
  - **ListEastWestFirewall**
    - 响应参数变更
      - `+ data.mode`
      - `+ data.ew_vpc_route_limit`
      - `+ data.er_associated_subnet.ipv6_enable`
      - `+ data.protect_infos.protected_resource_mode`
  - **AddAclRule**
    - 请求参数变更
      - `+ rules.tag`
      - `+ rules.source.region_list_json`
      - `+ rules.source.region_list`
      - `+ rules.source.domain_set_id`
      - `+ rules.source.domain_set_name`
      - `+ rules.source.ip_address`
      - `+ rules.source.address_group`
      - `+ rules.source.address_group_names`
      - `+ rules.service.custom_service`
      - `+ rules.service.service_group`
      - `+ rules.service.service_group_names`
  - **ListEips**
    - 请求参数变更
      - `+ tags`
    - 响应参数变更
      - `+ data.records.object_id`
      - `+ data.records.tags`
      - `+ data.records.domain_id`
      - `+ data.records.owner`
      - `+ data.records.fw_domain_id`
  - **AddAddressItem**
    - 响应参数变更
      - `+ data.covered_ip`
  - **ListFirewallDetail**
    - 响应参数变更
      - `+ data.records.resource_id`
      - `+ data.records.support_url_filtering`
      - `+ data.records.flavor.session_concurrent`
      - `+ data.records.flavor.session_create`
      - `+ data.records.flavor.total_rule_count`
      - `+ data.records.flavor.used_rule_count`
      - `+ data.records.flavor.vpc_bandwith`

### HuaweiCloud SDK CodeArtsBuild

- _新增特性_
  - 支持以下接口：
    - `DownloadLogByRecordId`
    - `ShowRecordInfo`
    - `StopBuildJob`
    - `DeleteBuildJob`
    - `DisableBuildJob`
    - `ResumeBuildJob`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DataArtsStudio

- _新增特性_
  - 支持接口`ShowTags`、`ParseUserBehavior`、`ShowDataSets`、`BatchSyncMetadata`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持以下接口：
    - `CreateConnectivityTest`
    - `ShowReplicationStates`
    - `ListAclAccounts`
    - `CreateAclAccount`
    - `UpdateAclAccountPassWord`
    - `ResetAclAccountPassWord`
    - `UpdateAclAccountRole`
    - `UpdateAclAccountRemark`
    - `DeleteAclAccount`
    - `ShowConfigTemplate`
    - `UpdateConfigTemplate`
    - `DeleteConfigTemplate`
- _解决问题_
  - 无
- _特性变更_
  - **ListConfigTemplates**
    - 响应参数变更
      - `+ templates`
      - `- config_templates`
  - **CreateRedislog**
    - 请求参数变更
      - `+ query_time: enum value [0,1,3,7]`
  - **ListInstances**
    - 响应参数变更
      - `+ instances.features.support_audit_log`
  - **ShowInstance**
    - 响应参数变更
      - `+ features.support_audit_log`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ReinstallServerWithCloudInit**
    - 请求参数变更
      - `+ os-reinstall.metadata.BYOL`
  - **ChangeServerOsWithCloudInit**
    - 请求参数变更
      - `+ os-change.metadata.BYOL`
  - **ChangeServerOsWithoutCloudInit**
    - 请求参数变更
      - `+ os-change.metadata.BYOL`

### HuaweiCloud SDK EG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **PutOfficialEvents**
    - 响应参数变更
      - `- failed_count`
      - `- events`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持以下接口：
    - `UpdateProxyNewConfigurations`
    - `CopyConfigurations`
    - `ListConfigurationsDifferences`
    - `ListConfigurationsInstances`
    - `ListModifyHistory`
    - `ListEnterpriseProjects`
    - `SwitchAccessControl`
    - `CreateAccessControl`
    - `DeleteScheduleTasK`
    - `ListInstanceConfigurations`
    - `ShowGaussMySqlIncrementalBackupList`
    - `UpdateBackupOffsitePolicy`
    - `CreateRestoreTables`
- _解决问题_
  - 无
- _特性变更_
  - **ListGaussMySqlDatabase**
    - 请求参数变更
      - `+ name`
      - `+ charset`

### HuaweiCloud SDK LakeFormation

- _新增特性_
  - 支持以下接口：
    - `UpdateLakeFormationInstanceDefault`
    - `UpdateLakeFormationInstanceScale`
    - `ShowAccessService`
    - `AuthorizeAccessService`
    - `ListAccessClientInfos`
    - `CreateAccessClient`
    - `ShowAccessClient`
    - `UpdateAccessClient`
    - `DeleteAccessClient`
    - `ShowAgency`
    - `CreateAgency`
    - `DeleteAgency`
    - `ListFunctionNames`
    - `BatchCheckPermission`
    - `ListPrincipals`
    - `AssociatePrincipals`
    - `RevokePrincipals`
    - `UpdatePrincipals`
    - `ShowCredential`
    - `ListConfigs`
    - `ListUsers`
    - `AssociateRoles`
    - `RevokeRoles`
    - `UpdateRoles`
    - `ListUserRoles`
    - `ListPartitionNamesWithoutLimit`
    - `DeleteAgreement`
- _解决问题_
  - 无
- _特性变更_
  - **ShowDatabase**
    - 响应参数变更
      - `+ owner_auth_source_type`
  - **UpdateDatabase**
    - 请求参数变更
      - `+ owner_auth_source_type`
    - 响应参数变更
      - `+ owner_auth_source_type`
  - **ListCatalogs**
    - 响应参数变更
      - `+ owner`
      - `+ owner_source`
      - `+ owner_type`
  - **CreateCatalog**
    - 请求参数变更
      - `+ branch_name`
      - `+ owner`
      - `+ owner_type`
      - `+ owner_source`
    - 响应参数变更
      - `+ owner`
      - `+ owner_source`
      - `+ owner_type`
  - **ShowCatalog**
    - 响应参数变更
      - `+ owner`
      - `+ owner_source`
      - `+ owner_type`
  - **UpdateCatalog**
    - 请求参数变更
      - `+ branch_name`
      - `+ owner`
      - `+ owner_type`
      - `+ owner_source`
    - 响应参数变更
      - `+ owner`
      - `+ owner_source`
      - `+ owner_type`
  - **ShowRole**
    - 响应参数变更
      - `+ role_name`
      - `+ principal_source`
      - `+ description`
      - `- role`
      - `- user_roles`
  - **UpdateRole**
    - 响应参数变更
      - `+ principal_source: enum value [AGENTTENANT]`
  - **ListLakeFormationInstances**
    - 响应参数变更
      - `+ default_instance`
      - `+ instances.default_instance`
      - `+ instances.status: enum value [RESOURCE_PREPARATION,RUNNING,RESOURCE_RELEASE,DELETED,RESOURCE_PREPARATION_FAIL,FROZEN_RELEASABLE,FROZEN_UNRELEASABLE,RECOVERING,DELETING,SCALING,SCALE_FAIL]`
  - **CreateLakeFormationInstance**
    - 请求参数变更
      - `+ order_id`
      - `+ charge_mode: enum value [prePaid]`
      - `+ specs.product_id`
    - 响应参数变更
      - `+ scale_progress`
      - `+ charge_mode`
      - `+ default_instance`
      - `+ resource_progress`
      - `+ resource_expected_duration`
      - `+ scale_expected_duration`
      - `+ status: enum value [RESOURCE_PREPARATION,RUNNING,RESOURCE_RELEASE,DELETED,RESOURCE_PREPARATION_FAIL,FROZEN_RELEASABLE,FROZEN_UNRELEASABLE,RECOVERING,DELETING,SCALING,SCALE_FAIL]`
      - `+ specs.product_id`
  - **UpdateLakeFormationInstance**
    - 响应参数变更
      - `+ default_instance`
      - `+ status: enum value [RESOURCE_PREPARATION,RUNNING,RESOURCE_RELEASE,DELETED,RESOURCE_PREPARATION_FAIL,FROZEN_RELEASABLE,FROZEN_UNRELEASABLE,RECOVERING,DELETING,SCALING,SCALE_FAIL]`
  - **ShowLakeFormationInstance**
    - 响应参数变更
      - `+ scale_progress`
      - `+ charge_mode`
      - `+ default_instance`
      - `+ resource_progress`
      - `+ resource_expected_duration`
      - `+ scale_expected_duration`
      - `+ status: enum value [RESOURCE_PREPARATION,RUNNING,RESOURCE_RELEASE,DELETED,RESOURCE_PREPARATION_FAIL,FROZEN_RELEASABLE,FROZEN_UNRELEASABLE,RECOVERING,DELETING,SCALING,SCALE_FAIL]`
      - `+ specs.product_id`
  - **ListSpecs**
    - 响应参数变更
      - `+ spec_codes.usage_value`
      - `+ spec_codes.free_usage_value`
  - **CreateDatabase**
    - 请求参数变更
      - `+ owner_auth_source_type`
    - 响应参数变更
      - `+ owner_auth_source_type`
  - **ListDatabases**
    - 响应参数变更
      - `+ owner_auth_source_type`
      - `+ databases.owner_auth_source_type`
  - **ShowFunction**
    - 响应参数变更
      - `+ owner_auth_source_type`
  - **UpdateFunction**
    - 请求参数变更
      - `+ owner_auth_source_type`
    - 响应参数变更
      - `+ owner_auth_source_type`
  - **CreateRole**
    - 响应参数变更
      - `+ principal_source: enum value [AGENTTENANT]`
  - **ListRoles**
    - 响应参数变更
      - `+ roles.principal_source: enum value [AGENTTENANT]`
  - **ListAllFunctions**
    - 响应参数变更
      - `+ owner_auth_source_type`
      - `+ functions.owner_auth_source_type`
  - **CreateFunction**
    - 请求参数变更
      - `+ owner_auth_source_type`
    - 响应参数变更
      - `+ owner_auth_source_type`
  - **ListFunctions**
    - 响应参数变更
      - `+ owner_auth_source_type`
      - `+ functions.owner_auth_source_type`
  - **CreateTable**
    - 请求参数变更
      - `+ ignore_obs_checked`
  - **UpdateTable**
    - 请求参数变更
      - `+ table.ignore_obs_checked`
  - **ShowSyncPolicy**
    - 响应参数变更
      - `+ policy_deltas.change_type`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListStructuredLogsWithTimeRange**
    - 响应参数变更
      - `+ result`
      - `- context`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListEngineProducts**
    - 响应参数变更
      - `+ products.properties.product_alias`

### HuaweiCloud SDK SIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`RunAudioAssessment`、`RunMultiModalAssessment`

### HuaweiCloud SDK VPC

- _新增特性_
  - 支持接口`BatchCreateSecurityGroupRules`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.61 2023-10-12

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持以下接口：
    - `ListStackSets`
    - `CreateStackSet`
    - `ShowStackSetTemplate`
    - `ListStackSetOperations`
    - `ShowStackSetMetadata`
    - `ListStackInstances`
    - `CreateStackInstance`
    - `DeleteStackInstance`
    - `DeployStackSet`
    - `DeleteStackSet`
    - `UpdateStackSet`
    - `ShowStackSetOperationMetadata`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK AS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateScalingConfig**
    - 请求参数变更
      - `+ source_scaling_configuration_id`

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateBareMetalServers**
    - 请求参数变更
      - `* server.server_tags: map<string, list<SystemTags>> -> list<SystemTags>`

### HuaweiCloud SDK BSS

- _新增特性_
  - 支持接口`ListSubCustomerNewTag`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CAE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListApplications**
    - 响应参数变更
      - `- items.annotations`
  - **CreateApplication**
    - 请求参数变更
      - `- metadata.annotations`
    - 响应参数变更
      - `- metadata.annotations`
  - **ShowApplication**
    - 响应参数变更
      - `- metadata.annotations`
  - **ListComponentConfigurations**
    - 响应参数变更
      - `+ items.data.spec`
      - `+ items.data.metadata`
      - `* items.data: object -> object<ListComponentConfigurationsResponseData>`
  - **CreateComponentConfiguration**
    - 请求参数变更
      - `+ items.data.spec`
      - `+ items.data.metadata`
      - `* items.data: object -> object<ConfigurationData>`
  - **ListComponentSnapshots**
    - 响应参数变更
      - `- items.description`
      - `+ items.context.runtime: enum value [Java17,Nodejs14,Nodejs16]`
  - **ShowComponent**
    - 响应参数变更
      - `+ spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`
  - **UpdateComponent**
    - 请求参数变更
      - `+ spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`
  - **CreateComponent**
    - 响应参数变更
      - `+ spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`
  - **ListComponents**
    - 响应参数变更
      - `+ items.spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowHistoryTasks**
    - 请求参数变更
      - `+ task_type`
  - **ShowUrlTaskInfo**
    - 响应参数变更
      - `+ result.mode`

### HuaweiCloud SDK CES

- _新增特性_
  - 支持以下接口：
    - `BatchUpdateNotificationMasks`
    - `BatchUpdateNotificationMaskTime`
    - `UpdateNotificationMasks`
    - `BatchDeleteNotificationMasks`
    - `ListNotificationMasks`
    - `ListNotificationMaskResources`
    - `ListOneClickAlarms`
    - `CreateOneClickAlarm`
    - `ListOneClickAlarmRules`
    - `BatchUpdateOneClickAlarmsEnabledState`
    - `BatchDeleteOneClickAlarms`
    - `UpdateOneClickAlarmNotifications`
    - `BatchUpdateOneClickAlarmPoliciesEnabledState`
    - `UpdateAlarmNotifications`
    - `ListCesTargetProjectTags`
- _解决问题_
  - 无
- _特性变更_
  - **ListAlarmHistories**
    - 响应参数变更
      - `+ alarm_histories.condition.suppress_duration: enum value [86400]`
  - **ListAgentInvocations**
    - 请求参数变更
      - `- instance_name`
      - `+ invocation_type: enum value [RETRY]`
    - 响应参数变更
      - `+ invocations.invocation_type: enum value [RETRY]`
  - **ListAgentStatus**
    - 响应参数变更
      - `+ agent_status.extensions.version`

### HuaweiCloud SDK CodeArtsDeploy

- _新增特性_
  - 支持接口`ShowExecutionParams`
- _解决问题_
  - 无
- _特性变更_
  - **ListAllApp**
    - 请求参数变更
      - `+ states`
      - `+ group_id`

### HuaweiCloud SDK Config

- _新增特性_
  - 支持以下接口：
    - `ListOrganizationConformancePacks`
    - `CreateOrganizationConformancePack`
    - `ShowOrganizationConformancePack`
    - `DeleteOrganizationConformancePack`
    - `ListOrganizationConformancePackStatuses`
    - `ShowOrganizationConformancePackDetailedStatuses`
- _解决问题_
  - 无
- _特性变更_
  - **ShowConfigurationAggregatorSourcesStatus**
    - 响应参数变更
      - `+ aggregated_source_statuses.source_name`
  - **ShowConformancePack**
    - 响应参数变更
      - `+ created_by`
  - **CreateConformancePack**
    - 响应参数变更
      - `+ created_by`
  - **ListConformancePacks**
    - 响应参数变更
      - `+ created_by`
      - `+ value.created_by`
  - **ShowAggregatePolicyStateComplianceSummary**
    - 响应参数变更
      - `+ results.group_account_name`
  - **ListAggregateComplianceByPolicyAssignment**
    - 响应参数变更
      - `+ aggregate_policy_assignments.account_name`

### HuaweiCloud SDK CSS

- _新增特性_
  - 支持以下接口：
    - `DeleteConfig`
    - `StopHotPipeline`
    - `ListCerts`
    - `ListElbs`
    - `EnableOrDisableElb`
    - `ShowElbDetail`
    - `CreateElbListener`
    - `UpdateEsListener`
    - `ListElbCerts`
    - `ListAiOps`
    - `CreateAiOps`
    - `DeleteAiOps`
    - `ListSmnTopics`
    - `UpgradeCore`
    - `ListImages`
    - `UpgradeDetail`
    - `RetryUpgradeTask`
    - `UpdateAzByInstanceType`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateShrinkNodes**
    - 请求参数变更
      - `+ migrate_data`
  - **CreateCnf**
    - 请求参数变更
      - `+ sensitive_words`
  - **UpdateCnf**
    - 请求参数变更
      - `+ sensitive_words`
  - **ShowClusterDetail**
    - 响应参数变更
      - `+ bandwidthResourceId`
      - `+ instances.resourceId`
      - `+ instances.volume.resourceIds`
      - `+ publicKibanaResp.bandwidthResourceId`
  - **ListClustersDetails**
    - 响应参数变更
      - `+ clusters.bandwidthResourceId`
      - `+ clusters.instances.resourceId`
      - `+ clusters.instances.volume.resourceIds`
      - `+ clusters.publicKibanaResp.bandwidthResourceId`

### HuaweiCloud SDK CTS

- _新增特性_
  - 支持以下接口：
    - `ListOperations`
    - `BatchCreateResourceTags`
    - `BatchDeleteResourceTags`
    - `ListUserResources`
    - `CheckObsBuckets`
    - `ListTraceResources`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DataArtsStudio

- _新增特性_
  - 支持以下接口：
    - `StopFactorySupplementDataInstance`
    - `ShowFactorySupplementData`
    - `CreateFactorySupplementDataInstance`
    - `ShowFactoryEnv`
    - `CreateFactoryEnv`
- _解决问题_
  - 无
- _特性变更_
  - **PublishApi**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowApplyDetail**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowMessageDetail**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowCatalogDetail**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **UpdateCatalog**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **CreateServiceCatalog**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **DeleteServiceCatalog**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **MigrateCatalog**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **MigrateApi**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **SearchIdByPath**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowPathById**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **PublishApiToInstance**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ExecuteApiToInstance**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **AuthorizeApiToInstance**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **AuthorizeActionApiToInstance**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **DeleteApp**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowAppInfo**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **UpdateApp**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowApisOverview**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowAppsOverview**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowApisDetail**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowAppsDetail**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **BatchApproveApply**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListApply**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ConfirmMessage**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListMessage**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListAllCatalogList**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListApiCatalogList**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListCatalogList**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowPathObjectById**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
    - 响应参数变更
      - `+ paths.name`
  - **DebugApi**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **SearchPublishInfo**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ListInstanceList**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **SearchDebugInfo**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ListApicInstances**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ListApicGroups**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **CreateApp**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ListApps**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ListApisTop**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ListAppsTop**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowApisDashboard**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowApiDashboard**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowAppsDashboard**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ListApiTopN**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ListApis**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **CreateApi**
    - 请求参数变更
      - `* workspace: optional -> required`
  - **ShowApi**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **UpdateApi**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **SearchAuthorizeApp**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **SearchBindApi**
    - 请求参数变更
      - `+ Dlm-Type`
      - `* workspace: optional -> required`

### HuaweiCloud SDK DC

- _新增特性_
  - 支持以下接口：
    - `UpdateVifPeer`
    - `DeleteVifPeer`
    - `CreateVifPeer`
    - `ShowQuotas`
    - `ListSwitchoverTestRecords`
    - `SwitchoverTest`
- _解决问题_
  - 无
- _特性变更_
  - **DeleteResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [dc-lag]`
  - **ListProjectTags**
    - 请求参数变更
      - `+ resource_type: enum value [dc-lag]`
  - **ShowResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [dc-lag]`
  - **CreateResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [dc-lag]`
  - **BatchCreateResourceTags**
    - 请求参数变更
      - `+ resource_type: enum value [dc-lag]`
  - **ShowDirectConnect**
    - 请求参数变更
      - `- limit`
      - `- marker`
    - 响应参数变更
      - `- direct_connect.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connect.charge_mode: enum value [port]`
  - **UpdateDirectConnect**
    - 响应参数变更
      - `- direct_connect.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connect.charge_mode: enum value [port]`
  - **ListDirectConnects**
    - 响应参数变更
      - `- direct_connects.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connects.charge_mode: enum value [port]`
  - **ShowVirtualGateway**
    - 响应参数变更
      - `- virtual_gateway.type: enum value [default]`
  - **UpdateVirtualGateway**
    - 响应参数变更
      - `- virtual_gateway.type: enum value [default]`
  - **ListVirtualGateways**
    - 请求参数变更
      - `+ enterprise_project_id`
    - 响应参数变更
      - `- virtual_gateways.type: enum value [default]`
  - **CreateVirtualGateway**
    - 响应参数变更
      - `- virtual_gateway.type: enum value [default]`
  - **ShowVirtualInterface**
    - 响应参数变更
      - `+ virtual_interface.service_type: enum value [GDGW]`
      - `- virtual_interface.service_type: enum value [vpc,GDWW]`
  - **UpdateVirtualInterface**
    - 响应参数变更
      - `+ virtual_interface.service_type: enum value [GDGW]`
      - `- virtual_interface.service_type: enum value [vpc,GDWW]`
  - **ListVirtualInterfaces**
    - 响应参数变更
      - `+ virtual_interfaces.service_type: enum value [GDGW]`
      - `- virtual_interfaces.service_type: enum value [vpc,GDWW]`
  - **CreateVirtualInterface**
    - 请求参数变更
      - `+ virtual_interface.service_type: enum value [GDGW]`
      - `- virtual_interface.service_type: enum value [GDWW]`
    - 响应参数变更
      - `+ virtual_interface.service_type: enum value [GDGW]`
      - `- virtual_interface.service_type: enum value [vpc,GDWW]`
  - **ListTagResourceInstances**
    - 请求参数变更
      - `+ resource_type: enum value [dc-lag]`

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RunOnce**
    - 响应参数变更
      - `* instanceId: string -> int64`

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持以下接口：
    - `SaveClusterDescriptionInfo`
    - `ExecuteDatabaseOmUserAction`
    - `ShowInstance`
    - `ShowDatabaseOmUserStatus`
    - `ListConfigurationsAuditRecords`
    - `ShowClusterRedistribution`
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
  - **ReinstallServerWithoutCloudInit**
    - 请求参数变更
      - `+ os-reinstall.metadata.BYOL`
  - **ListFlavors**
    - 响应参数变更
      - `+ flavors.os_extra_specs.quota:vif_max_num`
      - `+ flavors.os_extra_specs.quota:sub_network_interface_max_num`
  - **ListResizeFlavors**
    - 响应参数变更
      - `+ flavors.extra_specs.quota:vif_max_num`
      - `+ flavors.extra_specs.quota:sub_network_interface_max_num`

### HuaweiCloud SDK EG

- _新增特性_
  - 支持接口`PutOfficialEvents`
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
  - 移除接口`ShowFunctionUrl`、`UpdateFunctionUrl`、`CreateFunctionUrl`、`DeleteFunctionUrl`
  - **ListAsyncInvocations**
    - 响应参数变更
      - `+ next_marker`
      - `+ count`
  - **ListActiveAsyncInvocations**
    - 响应参数变更
      - `+ next_marker`
      - `+ count`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListInstances**
    - 响应参数变更
      - `+ instances.datastore.complete_version`
      - `+ instances.datastore.hotfix_versions`
  - **ListInstancesDetails**
    - 响应参数变更
      - `+ instances.datastore.complete_version`
      - `+ instances.datastore.hotfix_versions`

### HuaweiCloud SDK ImageSearch

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RunAddData**
    - 请求参数变更
      - `* optional_params.category: int -> int32`
    - 响应参数变更
      - `* data.image_info.objects.category: number -> integer`
  - **RunDeleteData**
    - 响应参数变更
      - `* data.delete_info.total_num: int -> int32`
      - `* data.delete_info.delete_num: int -> int32`
  - **RunSearch**
    - 请求参数变更
      - `* optional_params.category: int -> int32`
    - 响应参数变更
      - `* data.image_info.category: number -> integer`
      - `* data.image_info.objects.category: number -> integer`
      - `* data.search_info.total_num: int -> int32`
      - `* data.search_info.return_num: int -> int32`
      - `* data.search_info.search_time: long -> int32`
  - **RunCheckData**
    - 响应参数变更
      - `* data.check_info.total_num: int -> int32`
      - `* data.check_info.return_num: int -> int32`

### HuaweiCloud SDK IMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowJob**
    - 响应参数变更
      - `+ entities.addition_error_code`
      - `+ entities.addition_error_msg`
      - `+ entities.error_code`
      - `+ entities.error`
      - `+ entities.alarm_code`

### HuaweiCloud SDK LakeFormation

- _新增特性_
  - 支持接口`ListLakeFormationInstanceTags`、`ListQuotas`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK MetaStudio

- _新增特性_
  - 支持接口`CreatePhotoDetection`、`ShowPhotoDetection`
- _解决问题_
  - 无
- _特性变更_
  - **CreateSmartLiveRoom**
    - 请求参数变更
      - `- video_config.codec: enum value [VP9]`
  - **ShowSmartLiveRoom**
    - 响应参数变更
      - `- video_config.codec: enum value [VP9]`
  - **UpdateSmartLiveRoom**
    - 请求参数变更
      - `- video_config.codec: enum value [VP9]`
    - 响应参数变更
      - `- video_config.codec: enum value [VP9]`
  - **StartSmartLive**
    - 请求参数变更
      - `- video_config.codec: enum value [VP9]`
  - **Create2DDigitalHumanVideo**
    - 请求参数变更
      - `- video_config.codec: enum value [VP9]`
  - **Show2DDigitalHumanVideo**
    - 响应参数变更
      - `- video_config.codec: enum value [VP9]`
  - **CreateVideoScripts**
    - 请求参数变更
      - `- video_config.codec: enum value [VP9]`
  - **ShowVideoScript**
    - 响应参数变更
      - `- video_config.codec: enum value [VP9]`
  - **UpdateVideoScript**
    - 请求参数变更
      - `- video_config.codec: enum value [VP9]`

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeColombiaIdCard`
- _解决问题_
  - 无
- _特性变更_
  - **RecognizeVehicleLicense**
    - 响应参数变更
      - `+ result.energy_type`
      - `+ result.front`
      - `+ result.back`
  - **RecognizeWebImage**
    - 请求参数变更
      - `+ detect_text_direction`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持以下接口：
    - `ListPostgresqlHbaInfo`
    - `ModifyPostgresqlHbaConf`
    - `AddPostgresqlHbaConf`
    - `DeletePostgresqlHbaConf`
    - `ListPostgresqlHbaInfoHistory`
- _解决问题_
  - 无
- _特性变更_
  - **UpgradeDbVersionNew**
    - 请求参数变更
      - `+ is_delayed`
      - `- delay`

### HuaweiCloud SDK ServiceStage

- _新增特性_
  - 支持以下接口：
    - `ListAuthorizations`
    - `ShowRedirectUrl`
    - `CreateOAuth`
    - `CreatePersonalAuth`
    - `CreatePasswordAuth`
    - `DeleteAuthorize`
    - `ListNamespaces`
    - `ShowProjectDetail`
    - `ListProjects`
    - `CreateProject`
    - `ListBranches`
    - `ListTags`
    - `CreateTag`
    - `DeleteTag`
    - `ListCommits`
    - `ListHooks`
    - `CreateHook`
    - `DeleteHook`
    - `ListTrees`
    - `ShowContent`
    - `UpdateFile`
    - `CreateFile`
    - `DeleteFile`
    - `ListTemplates`
    - `ListRuntimes`
    - `ListFlavors`
    - `ListEnvironments`
    - `CreateEnvironment`
    - `ShowEnvironmentDetail`
    - `ChangeEnvironment`
    - `DeleteEnvironment`
    - `ListApplications`
    - `CreateApplication`
    - `ShowApplicationDetail`
    - `ChangeApplication`
    - `DeleteApplication`
    - `ShowApplicationConfiguration`
    - `ChangeApplicationConfiguration`
    - `DeleteApplicationConfiguration`
    - `ListComponents`
    - `CreateComponent`
    - `ShowComponentDetail`
    - `ChangeComponent`
    - `DeleteComponent`
    - `ListInstances`
    - `CreateInstance`
    - `ShowInstanceDetail`
    - `ChangeInstance`
    - `DeleteInstance`
    - `UpdateInstanceAction`
    - `ListInstanceSnapshots`
    - `ShowJobDetail`
- _解决问题_
  - 无
- _特性变更_
  - **ModifyComponent**
    - 请求参数变更
      - `+ external_accesses.protocol`
      - `- external_accesses.prorocol`
  - **CreateComponent**
    - 请求参数变更
      - `+ external_accesses`
  - **ShowComponentsInApplication**
    - 响应参数变更
      - `+ components.external_accesses.protocol`
      - `- components.external_accesses.prorocol`
  - **ShowComponents**
    - 响应参数变更
      - `+ components.external_accesses.protocol`
      - `- components.external_accesses.prorocol`

### HuaweiCloud SDK SMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowCertKey**
    - 请求参数变更
      - `+ enable_ca_cert`
    - 响应参数变更
      - `+ target_mgmt_private_key`
      - `+ target_data_cert`
      - `+ target_data_private_key`
      - `+ target_mgmt_cert`
      - `+ ca`

### HuaweiCloud SDK VPC

- _新增特性_
  - 支持以下接口：
    - `ListTrafficMirrorSessions`
    - `CreateTrafficMirrorSession`
    - `ShowTrafficMirrorSession`
    - `UpdateTrafficMirrorSession`
    - `DeleteTrafficMirrorSession`
    - `RemoveSourcesFromTrafficMirrorSession`
    - `AddSourcesToTrafficMirrorSession`
    - `ListTrafficMirrorFilters`
    - `CreateTrafficMirrorFilter`
    - `ShowTrafficMirrorFilter`
    - `UpdateTrafficMirrorFilter`
    - `DeleteTrafficMirrorFilter`
    - `ListTrafficMirrorFilterRules`
    - `CreateTrafficMirrorFilterRule`
    - `ShowTrafficMirrorFilterRule`
    - `UpdateTrafficMirrorFilterRule`
    - `DeleteTrafficMirrorFilterRule`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK WorkspaceApp

- _新增特性_
  - 支持以下接口：
    - `CreateOrUpdateStoragePolicyStatement`
    - `ShowPublishableApp`
    - `UploadAppIcon`
    - `ListSessionByUserName`
    - `LogoffUserSession`
    - `ListSessionType`
- _解决问题_
  - 无
- _特性变更_
  - **ListStoragePolicyStatement**
    - 响应参数变更
      - `+ roam_actions`
      - `+ actions`
      - `+ policy_statement_id`
      - `+ items.roam_actions`
  - **UpdateAppGroup**
    - 响应参数变更
      - `+ app_type`
  - **ListAppConnection**
    - 请求参数变更
      - `* limit: required -> optional`
      - `* offset: required -> optional`
  - **ListUserConnection**
    - 请求参数变更
      - `* limit: required -> optional`
      - `* offset: required -> optional`
  - **UpdateServerGroup**
    - 请求参数变更
      - `+ storage_mount_policy`
      - `+ app_type`
      - `+ route_policy.cpu_threshold`
      - `+ route_policy.mem_threshold`
  - **ListProduct**
    - 响应参数变更
      - `+ products.expire_time`
      - `+ products.support_gpu_type`
  - **CreateAppGroup**
    - 请求参数变更
      - `+ app_type`
    - 响应参数变更
      - `+ app_type`
  - **ListAppGroup**
    - 请求参数变更
      - `+ app_type`
      - `* limit: required -> optional`
      - `* offset: required -> optional`
    - 响应参数变更
      - `+ app_type`
      - `+ items.app_type`
  - **ListPublishedApp**
    - 请求参数变更
      - `* limit: required -> optional`
      - `* offset: required -> optional`
  - **PublishApp**
    - 请求参数变更
      - `+ accounts.telephone_number`
  - **AddAppGroupAuthorization**
    - 请求参数变更
      - `+ accounts.telephone_number`
  - **ListAppGroupAuthorization**
    - 请求参数变更
      - `* limit: required -> optional`
      - `* offset: required -> optional`
  - **BatchDeleteAppGroupAuthorization**
    - 请求参数变更
      - `+ accounts.telephone_number`
  - **ListStorageAssignment**
    - 响应参数变更
      - `+ roam_actions`
      - `+ actions`
      - `+ policy_statement_id`
      - `+ items.policy_statement.roam_actions`
  - **ListServers**
    - 请求参数变更
      - `* offset: required -> optional`
      - `* limit: required -> optional`
    - 响应参数变更
      - `+ items.product_info.expire_time`
      - `+ items.product_info.support_gpu_type`
      - `+ items.vm_status: enum value [BUILD_IMAGE]`
      - `+ items.task_status: enum value [build_image]`
  - **CreateServerGroup**
    - 请求参数变更
      - `+ app_type`
      - `+ extra_session_type`
      - `+ extra_session_size`
      - `+ route_policy.cpu_threshold`
      - `+ route_policy.mem_threshold`
    - 响应参数变更
      - `+ app_type`
      - `+ extra_session_size`
      - `+ extra_session_type`
      - `+ storage_mount_policy`
      - `+ product_info.expire_time`
      - `+ product_info.support_gpu_type`
  - **ListServerGroups**
    - 请求参数变更
      - `+ app_type`
      - `* offset: required -> optional`
      - `* limit: required -> optional`
    - 响应参数变更
      - `+ app_type`
      - `+ extra_session_size`
      - `+ extra_session_type`
      - `+ storage_mount_policy`
      - `+ items.extra_session_type`
      - `+ items.extra_session_size`
      - `+ items.app_type`
      - `+ items.storage_mount_policy`
      - `+ items.product_info.expire_time`
      - `+ items.product_info.support_gpu_type`
  - **ListPolicyGroup**
    - 请求参数变更
      - `* offset: required -> optional`
      - `* limit: required -> optional`
  - **ListPolicyTemplate**
    - 请求参数变更
      - `* offset: required -> optional`
      - `* limit: required -> optional`

# 3.1.60 2023-09-19

### HuaweiCloud SDK IdentityCenterStore

- _新增特性_
  - 支持服务`IdentityCenterStore`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateBareMetalServers**
    - 请求参数变更
      - `* server.server_tags: list<SystemTags> -> map<string, list<SystemTags>>`

### HuaweiCloud SDK CAE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateComponentConfiguration**
    - 请求参数变更
      - `+ items.type: enum value [customMetric]`

### HuaweiCloud SDK CPH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`BatchMigrateCloudPhone`、`CreateCloudPhoneServer`
  - **PushShareApps**
    - 响应参数变更
      - `+ jobs`
      - `+ request_id`
  - **DeleteShareApps**
    - 响应参数变更
      - `+ jobs`
      - `+ request_id`
  - **PushShareFiles**
    - 响应参数变更
      - `+ jobs`
      - `+ request_id`
  - **ListCloudPhones**
    - 响应参数变更
      - `+ count`
  - **ShowCloudPhoneDetail**
    - 响应参数变更
      - `+ access_infos.phone_ipv6`
      - `+ access_infos.server_ipv6`
  - **ListCloudPhoneServerModels**
    - 响应参数变更
      - `+ server_models.free_size`
  - **CreateNet2CloudPhoneServer**
    - 请求参数变更
      - `+ nics.ipv6_enable`
      - `+ nics.ipv6_bandwidth`
  - **ListEncodeServers**
    - 响应参数变更
      - `+ encode_servers.encode_server_ipv6`
      - `+ encode_servers.access_infos.server_ipv6`
  - **ListCloudPhoneServers**
    - 响应参数变更
      - `+ count`

### HuaweiCloud SDK CTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateTracker**
    - 请求参数变更
      - `+ is_organization_tracker`
      - `+ management_event_selector`
  - **CreateTracker**
    - 请求参数变更
      - `+ is_organization_tracker`
      - `+ management_event_selector`
    - 响应参数变更
      - `+ is_organization_tracker`
      - `+ management_event_selector`
  - **ListTrackers**
    - 响应参数变更
      - `+ trackers.is_organization_tracker`
      - `+ trackers.management_event_selector`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持接口`ListActiveAsyncInvocations`
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
  - **CreateInstance**
    - 请求参数变更
      - `+ availability_zone_detail`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListInstanceTopics**
    - 响应参数变更
      - `+ topic_max_partitions`

### HuaweiCloud SDK Live

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateTranscodingsTemplate**
    - 请求参数变更
      - `+ quality_info.bitrate_adaptive`
      - `+ quality_info.i_frame_policy`
  - **CreateTranscodingsTemplate**
    - 请求参数变更
      - `+ quality_info.bitrate_adaptive`
      - `+ quality_info.i_frame_policy`
  - **ShowTranscodingsTemplate**
    - 响应参数变更
      - `+ templates.quality_info.bitrate_adaptive`
      - `+ templates.quality_info.i_frame_policy`

### HuaweiCloud SDK LTS

- _新增特性_
  - 支持以下接口：
    - `ShowLogConvergeConfig`
    - `ShowAdminConfig`
    - `UpdateSwitch`
    - `ShowMemberGroupAndStream`
    - `UpdateLogConvergeConfig`
- _解决问题_
  - 无
- _特性变更_
  - **ListCharts**
    - 响应参数变更
      - `+ config.can_sort`
      - `+ config.can_search`
      - `+ config.page_size`
      - `* config: object -> object<ChartConfig>`
  - **ShowNotificationTemplate**
    - 响应参数变更
      - `+ create_time`
      - `+ project_id`
      - `+ templates`
      - `+ modify_time`
      - `+ name`
      - `+ source`
      - `+ type`
      - `+ locale`
      - `+ desc`
      - `- body`
  - **DeleteTransfer**
    - 响应参数变更
      - `+ log_transfer_info.log_transfer_detail.obs_period`
      - `+ log_transfer_info.log_transfer_detail.obs_encrypted_id`
      - `+ log_transfer_info.log_transfer_detail.obs_prefix_name`
      - `+ log_transfer_info.log_transfer_detail.obs_period_unit`
      - `+ log_transfer_info.log_transfer_detail.obs_transfer_path`
      - `+ log_transfer_info.log_transfer_detail.obs_eps_id`
      - `+ log_transfer_info.log_transfer_detail.obs_bucket_name`
      - `+ log_transfer_info.log_transfer_detail.obs_encrypted_enable`
      - `+ log_transfer_info.log_transfer_detail.obs_dir_pre_fix_name`
      - `+ log_transfer_info.log_transfer_detail.dis_id`
      - `+ log_transfer_info.log_transfer_detail.dis_name`
      - `+ log_transfer_info.log_transfer_detail.kafka_id`
      - `+ log_transfer_info.log_transfer_detail.kafka_topic`
      - `+ log_transfer_info.log_transfer_detail.obs_time_zone`
      - `+ log_transfer_info.log_transfer_detail.obs_time_zone_id`
      - `+ log_transfer_info.log_transfer_detail.tags`
      - `* log_transfer_info.log_transfer_detail: object -> object<TransferDetail>`
  - **ListTransfers**
    - 响应参数变更
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_period`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_encrypted_id`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_prefix_name`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_period_unit`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_transfer_path`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_eps_id`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_bucket_name`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_encrypted_enable`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_dir_pre_fix_name`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.dis_id`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.dis_name`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.kafka_id`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.kafka_topic`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_time_zone`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.obs_time_zone_id`
      - `+ log_transfers.log_transfer_info.log_transfer_detail.tags`
      - `* log_transfers.log_transfer_info.log_transfer_detail: object -> object<TransferDetail>`
  - **UpdateTransfer**
    - 响应参数变更
      - `+ log_transfer_info.log_transfer_detail.obs_period`
      - `+ log_transfer_info.log_transfer_detail.obs_encrypted_id`
      - `+ log_transfer_info.log_transfer_detail.obs_prefix_name`
      - `+ log_transfer_info.log_transfer_detail.obs_period_unit`
      - `+ log_transfer_info.log_transfer_detail.obs_transfer_path`
      - `+ log_transfer_info.log_transfer_detail.obs_eps_id`
      - `+ log_transfer_info.log_transfer_detail.obs_bucket_name`
      - `+ log_transfer_info.log_transfer_detail.obs_encrypted_enable`
      - `+ log_transfer_info.log_transfer_detail.obs_dir_pre_fix_name`
      - `+ log_transfer_info.log_transfer_detail.dis_id`
      - `+ log_transfer_info.log_transfer_detail.dis_name`
      - `+ log_transfer_info.log_transfer_detail.kafka_id`
      - `+ log_transfer_info.log_transfer_detail.kafka_topic`
      - `+ log_transfer_info.log_transfer_detail.obs_time_zone`
      - `+ log_transfer_info.log_transfer_detail.obs_time_zone_id`
      - `+ log_transfer_info.log_transfer_detail.tags`
      - `* log_transfer_info.log_transfer_detail: object -> object<TransferDetail>`
  - **CreateTransfer**
    - 响应参数变更
      - `+ log_transfer_info.log_transfer_detail.obs_period`
      - `+ log_transfer_info.log_transfer_detail.obs_encrypted_id`
      - `+ log_transfer_info.log_transfer_detail.obs_prefix_name`
      - `+ log_transfer_info.log_transfer_detail.obs_period_unit`
      - `+ log_transfer_info.log_transfer_detail.obs_transfer_path`
      - `+ log_transfer_info.log_transfer_detail.obs_eps_id`
      - `+ log_transfer_info.log_transfer_detail.obs_bucket_name`
      - `+ log_transfer_info.log_transfer_detail.obs_encrypted_enable`
      - `+ log_transfer_info.log_transfer_detail.obs_dir_pre_fix_name`
      - `+ log_transfer_info.log_transfer_detail.dis_id`
      - `+ log_transfer_info.log_transfer_detail.dis_name`
      - `+ log_transfer_info.log_transfer_detail.kafka_id`
      - `+ log_transfer_info.log_transfer_detail.kafka_topic`
      - `+ log_transfer_info.log_transfer_detail.obs_time_zone`
      - `+ log_transfer_info.log_transfer_detail.obs_time_zone_id`
      - `+ log_transfer_info.log_transfer_detail.tags`
      - `* log_transfer_info.log_transfer_detail: object -> object<TransferDetail>`
  - **ListNotificationTemplates**
    - 响应参数变更
      - `+ create_time`
      - `+ project_id`
      - `+ templates`
      - `+ modify_time`
      - `+ name`
      - `+ source`
      - `+ type`
      - `+ locale`
      - `+ desc`
      - `- body`
  - **UpdateSqlAlarmRule**
    - 请求参数变更
      - `+ frequency.type`
      - `+ frequency.cron_expr`
      - `+ frequency.hour_of_day`
      - `+ frequency.day_of_week`
      - `+ frequency.fixed_rate`
      - `+ frequency.fixed_rate_unit`
      - `* frequency: object -> object<Frequency>`
      - `+ notification_save_rule.language`
      - `+ notification_save_rule.timezone`
      - `+ notification_save_rule.user_name`
      - `+ notification_save_rule.topics`
      - `+ notification_save_rule.template_name`
      - `* notification_save_rule: object -> object<SqlNotificationSaveRule>`
    - 响应参数变更
      - `+ frequency.type`
      - `+ frequency.cron_expr`
      - `+ frequency.hour_of_day`
      - `+ frequency.day_of_week`
      - `+ frequency.fixed_rate`
      - `+ frequency.fixed_rate_unit`
      - `* frequency: object -> object<Frequency>`
  - **CreateSqlAlarmRule**
    - 请求参数变更
      - `+ frequency.type`
      - `+ frequency.cron_expr`
      - `+ frequency.hour_of_day`
      - `+ frequency.day_of_week`
      - `+ frequency.fixed_rate`
      - `+ frequency.fixed_rate_unit`
      - `* frequency: object -> object<Frequency>`
      - `+ notification_save_rule.language`
      - `+ notification_save_rule.timezone`
      - `+ notification_save_rule.user_name`
      - `+ notification_save_rule.topics`
      - `+ notification_save_rule.template_name`
      - `* notification_save_rule: object -> object<SqlNotificationSaveRule>`
  - **ListSqlAlarmRules**
    - 响应参数变更
      - `+ sql_alarm_rules.frequency.type`
      - `+ sql_alarm_rules.frequency.cron_expr`
      - `+ sql_alarm_rules.frequency.hour_of_day`
      - `+ sql_alarm_rules.frequency.day_of_week`
      - `+ sql_alarm_rules.frequency.fixed_rate`
      - `+ sql_alarm_rules.frequency.fixed_rate_unit`
      - `* sql_alarm_rules.frequency: object -> object<Frequency>`
  - **UpdateKeywordsAlarmRule**
    - 请求参数变更
      - `+ frequency.type`
      - `+ frequency.cron_expr`
      - `+ frequency.hour_of_day`
      - `+ frequency.day_of_week`
      - `+ frequency.fixed_rate`
      - `+ frequency.fixed_rate_unit`
      - `* frequency: object -> object<Frequency>`
      - `+ notification_save_rule.language`
      - `+ notification_save_rule.timezone`
      - `+ notification_save_rule.user_name`
      - `+ notification_save_rule.topics`
      - `+ notification_save_rule.template_name`
      - `* notification_save_rule: object -> object<SqlNotificationSaveRule>`
  - **CreateKeywordsAlarmRule**
    - 请求参数变更
      - `+ notification_save_rule.language`
      - `+ notification_save_rule.timezone`
      - `+ notification_save_rule.user_name`
      - `+ notification_save_rule.topics`
      - `+ notification_save_rule.template_name`
      - `* notification_save_rule: object -> object<SqlNotificationSaveRule>`
  - **ListKeywordsAlarmRules**
    - 响应参数变更
      - `+ keywords_alarm_rules.frequency.type`
      - `+ keywords_alarm_rules.frequency.cron_expr`
      - `+ keywords_alarm_rules.frequency.hour_of_day`
      - `+ keywords_alarm_rules.frequency.day_of_week`
      - `+ keywords_alarm_rules.frequency.fixed_rate`
      - `+ keywords_alarm_rules.frequency.fixed_rate_unit`
      - `* keywords_alarm_rules.frequency: object -> object<Frequency>`

### HuaweiCloud SDK MetaStudio

- _新增特性_
  - 支持以下接口：
    - `Create2DDigitalHumanVideo`
    - `Show2DDigitalHumanVideo`
    - `Cancel2DDigitalHumanVideo`
    - `ListDigitalHumanBusinessCard`
    - `CreateDigitalHumanBusinessCard`
    - `ShowDigitalHumanBusinessCard`
    - `UpdateDigitalHumanBusinessCard`
    - `DeleteDigitalHumanBusinessCard`
    - `CreatePhotoDigitalHumanVideo`
    - `ShowPhotoDigitalHumanVideo`
    - `CancelPhotoDigitalHumanVideo`
    - `ListSmartLiveRooms`
    - `CreateSmartLiveRoom`
    - `ShowSmartLiveRoom`
    - `UpdateSmartLiveRoom`
    - `DeleteSmartLiveRoom`
    - `ListSmartLive`
    - `StartSmartLive`
    - `ShowSmartLive`
    - `StopSmartLive`
    - `ExecuteSmartLiveCommand`
    - `LiveEventReport`
    - `ListVideoScripts`
    - `CreateVideoScripts`
    - `ShowVideoScript`
    - `UpdateVideoScript`
    - `DeleteVideoScript`
- _解决问题_
  - 无
- _特性变更_
  - **CreatePictureModelingByUrlJob**
    - 请求参数变更
      - `+ X-User-Privilege`

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`ExpandCluster`、`ShrinkCluster`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeVehicleCertificate`、`RecognizeAcceptanceBill`、`RecognizeRealEstateCertificate`、`RecognizeVietnamIdCard`
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
  - **UpdateConsumerGroup**
    - 请求参数变更
      - `* body: object<ConsumerGroup> -> object<UpdateConsumerGroup>`
  - **CreateRocketMqMigrationTask**
    - 响应参数变更
      - `+ task_id`

### HuaweiCloud SDK SMS

- _新增特性_
  - 支持接口`ShowPrivacyAgreements`、`CreatePrivacyAgreements`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.59 2023-09-14

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateBareMetalServers**
    - 请求参数变更
      - `+ server.nics.allowed_address_pairs`

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateVault**
    - 请求参数变更
      - `- vault.billing.promotion_info`
      - `- vault.billing.purchase_mode`
      - `- vault.billing.order_id`
  - **CreatePostPaidVault**
    - 请求参数变更
      - `- vault.billing.promotion_info`
      - `- vault.billing.purchase_mode`
      - `- vault.billing.order_id`

### HuaweiCloud SDK CES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateEvents**
    - 请求参数变更
      - `- detail.dimensions`
  - **ListEventDetail**
    - 响应参数变更
      - `* event_info.detail.dimensions: object<MetricsDimension> -> list<MetricsDimension>`
      - `* event_info.detail: object<EventItemDetail> -> object<ShowEventItemDetail>`

### HuaweiCloud SDK CodeArtsDeploy

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAppDetailById**
    - 响应参数变更
      - `* result.arrange_infos: object -> list<TaskV2Info>`
  - **ListNewHosts**
    - 响应参数变更
      - `+ result.permission.can_copy`
      - `- result.permission.can_connection_test`
      - `* result.permission: object<PermissionHostDetail> -> object<PermissionHostDetailNew>`
  - **ShowHostDetail**
    - 响应参数变更
      - `* result.proxy_host: string -> object<HostInfoDetail>`
      - `+ result.permission.can_copy`
      - `- result.permission.can_connection_test`
      - `* result.permission: object<PermissionHostDetail> -> object<PermissionHostDetailNew>`

### HuaweiCloud SDK CPTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAgentConfig**
    - 响应参数变更
      - `+ result.elasticsearch_enable`
      - `+ result.elasticsearch_shadow_type`
      - `+ result.elasticsearch_shadow_repository`
  - **UpdateAgentHealthStatus**
    - 响应参数变更
      - `+ result.result.elasticsearch_enable`
      - `+ result.result.elasticsearch_shadow_type`
      - `+ result.result.elasticsearch_shadow_repository`

### HuaweiCloud SDK CSMS

- _新增特性_
  - 支持以下接口：
    - `ListSecretEvents`
    - `CreateSecretEvent`
    - `ShowSecretEvent`
    - `UpdateSecretEvent`
    - `DeleteSecretEvent`
    - `ListNotificationRecords`
    - `UpdateVersion`
- _解决问题_
  - 无
- _特性变更_
  - **ListSecrets**
    - 请求参数变更
      - `+ event_name`
    - 响应参数变更
      - `+ secrets.secret_type`
      - `+ secrets.auto_rotation`
      - `+ secrets.rotation_period`
      - `+ secrets.rotation_config`
      - `+ secrets.rotation_time`
      - `+ secrets.next_rotation_time`
      - `+ secrets.event_subscriptions`
      - `+ secrets.enterprise_project_id`
  - **CreateSecret**
    - 请求参数变更
      - `+ secret_type`
      - `+ auto_rotation`
      - `+ rotation_period`
      - `+ rotation_config`
      - `+ event_subscriptions`
      - `+ enterprise_project_id`
    - 响应参数变更
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **ShowSecret**
    - 响应参数变更
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **UpdateSecret**
    - 请求参数变更
      - `+ auto_rotation`
      - `+ rotation_period`
      - `+ event_subscriptions`
    - 响应参数变更
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **UploadSecretBlob**
    - 响应参数变更
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **ListSecretVersions**
    - 响应参数变更
      - `+ version_metadatas.expire_time`
  - **CreateSecretVersion**
    - 请求参数变更
      - `+ expire_time`
    - 响应参数变更
      - `+ version_metadata.expire_time`
  - **DeleteSecretForSchedule**
    - 响应参数变更
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **RestoreSecret**
    - 响应参数变更
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **ListSecretTags**
    - 响应参数变更
      - `* sys_tags: list<TagItem> -> list<SysTag>`
  - **ListProjectSecretsTags**
    - 响应参数变更
      - `* tags: list<Tag> -> list<TagResponse>`
  - **ShowSecretVersion**
    - 响应参数变更
      - `+ version.version_metadata.expire_time`
  - **ListResourceInstances**
    - 请求参数变更
      - `* matches: list<TagItem> -> list<TagMatches>`
    - 响应参数变更
      - `- resources.sys_tags`
      - `+ resources.resource_detail.secret_type`
      - `+ resources.resource_detail.auto_rotation`
      - `+ resources.resource_detail.rotation_period`
      - `+ resources.resource_detail.rotation_config`
      - `+ resources.resource_detail.rotation_time`
      - `+ resources.resource_detail.next_rotation_time`
      - `+ resources.resource_detail.event_subscriptions`
      - `+ resources.resource_detail.enterprise_project_id`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListFlavors**
    - 响应参数变更
      - `+ flavors.replica_count`

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateResource**
    - 请求参数变更
      - `+ jobRelation`
      - `+ dependPackages`
      - `+ id`
      - `+ type: enum value [pyFile]`
  - **ShowResource**
    - 响应参数变更
      - `+ jobRelation`
      - `+ dependPackages`
      - `+ id`
      - `+ type: enum value [pyFile]`
  - **UpdateResource**
    - 请求参数变更
      - `+ jobRelation`
      - `+ dependPackages`
      - `+ id`
      - `+ type: enum value [pyFile]`
  - **ListConnections**
    - 请求参数变更
      - `+ limit`
      - `+ offset`
      - `+ connectionName`
  - **ListScripts**
    - 请求参数变更
      - `+ limit`
      - `+ offset`
      - `+ scriptName`
  - **ListJobs**
    - 请求参数变更
      - `+ limit`
      - `+ offset`
      - `+ jobType`
      - `+ jobName`
  - **ListSupplementdata**
    - 请求参数变更
      - `+ sort`
      - `+ page`
      - `+ size`
      - `+ name`
      - `+ userName`
      - `+ status`
      - `+ startDate`
      - `+ endDate`
    - 响应参数变更
      - `* rows.endDate: number -> int64`
      - `* rows.startDate: number -> int64`
      - `* rows.submittedDate: number -> int64`
      - `+ rows.supplement_data_instance_time.days`
      - `+ rows.supplement_data_instance_time.time_of_day`
      - `+ rows.supplement_data_run_time.time_of_day`
      - `+ rows.supplement_data_run_time.day_of_week`
      - `+ rows.supplement_data_run_time.day_of_month`
  - **CreateSupplementdata**
    - 请求参数变更
      - `+ supplement_data_run_time`
      - `+ supplement_data_instance_time`

### HuaweiCloud SDK EVS

- _新增特性_
  - 支持接口`ModifyVolumeQoS`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持接口`ShowFunctionUrl`、`UpdateFunctionUrl`、`CreateFunctionUrl`、`DeleteFunctionUrl`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateFuncSnapshot**
    - 请求参数变更
      - `+ action: enum value [enable,disable]`
  - **CreateFunction**
    - 请求参数变更
      - `+ custom_image`
      - `+ code_type: enum value [Custom-Image-Swr]`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ListAuditLogDownloadLink`
- _解决问题_
  - 无
- _特性变更_
  - **CreateGaussMySqlInstance**
    - 响应参数变更
      - `+ instance.volume`

### HuaweiCloud SDK Image

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `RunImageDescription`
    - `RunImageSuperResolution`
    - `CreateVideoTaggingMediaTask`
    - `ShowVideoTaggingMediaTask`
    - `CreateImageHighresolutionMattingTask`
    - `ShowImageHighresolutionMattingTask`

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 支持以下接口：
    - `CreateSchedule`
    - `UpdateSchedule`
    - `DeleteSchedule`
    - `ExecuteDeviceControlsSet`
    - `ExecuteDeviceControlsRelease`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`UpdateInstanceConsumerGroup`、`UpdateInstanceUser`
- _解决问题_
  - 无
- _特性变更_
  - **CreateKafkaConsumerGroup**
    - 请求参数变更
      - `+ group_desc`
  - **CreateInstanceUser**
    - 请求参数变更
      - `+ user_desc`
  - **ShowInstanceUsers**
    - 响应参数变更
      - `+ users.user_desc`
  - **ShowInstanceMessages**
    - 请求参数变更
      - `+ keyword`

### HuaweiCloud SDK KPS

- _新增特性_
  - 支持接口`ImportPrivateKey`、`ExportPrivateKey`、`BatchAssociateKeypair`、`ClearPrivateKey`
- _解决问题_
  - 无
- _特性变更_
  - **ListKeypairDetail**
    - 响应参数变更
      - `+ keypair.key_id`
      - `+ keypair.algorithm`
  - **ListFailedTask**
    - 请求参数变更
      - `* limit: string -> int32`
      - `* offset: string -> int32`
  - **AssociateKeypair**
    - 请求参数变更
      - `+ server.port`
    - 响应参数变更
      - `+ error_msg`
      - `+ error_code`
      - `+ server_id`
      - `+ status`
  - **DisassociateKeypair**
    - 响应参数变更
      - `+ error_msg`
      - `+ error_code`
      - `+ server_id`
      - `+ status`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListCharts**
    - 响应参数变更
      - `- config.can_sort`
      - `- config.can_search`
      - `- config.page_size`
  - **ShowNotificationTemplate**
    - 响应参数变更
      - `+ body`
      - `- create_time`
      - `- project_id`
      - `- templates`
      - `- modify_time`
      - `- name`
      - `- source`
      - `- type`
      - `- locale`
      - `- desc`
  - **ListLogStream**
    - 请求参数变更
      - `- tag`
    - 响应参数变更
      - `* log_streams: list<LogStream> -> list<LogStreamResBody>`
  - **ListStructuredLogsWithTimeRange**
    - 响应参数变更
      - `+ context`
      - `- body`
  - **DeleteTransfer**
    - 响应参数变更
      - `- log_transfer_info.log_transfer_detail.obs_period`
      - `- log_transfer_info.log_transfer_detail.obs_encrypted_id`
      - `- log_transfer_info.log_transfer_detail.obs_prefix_name`
      - `- log_transfer_info.log_transfer_detail.obs_period_unit`
      - `- log_transfer_info.log_transfer_detail.obs_transfer_path`
      - `- log_transfer_info.log_transfer_detail.obs_eps_id`
      - `- log_transfer_info.log_transfer_detail.obs_bucket_name`
      - `- log_transfer_info.log_transfer_detail.obs_encrypted_enable`
      - `- log_transfer_info.log_transfer_detail.obs_dir_pre_fix_name`
      - `- log_transfer_info.log_transfer_detail.dis_id`
      - `- log_transfer_info.log_transfer_detail.dis_name`
      - `- log_transfer_info.log_transfer_detail.kafka_id`
      - `- log_transfer_info.log_transfer_detail.kafka_topic`
      - `- log_transfer_info.log_transfer_detail.obs_time_zone`
      - `- log_transfer_info.log_transfer_detail.obs_time_zone_id`
      - `- log_transfer_info.log_transfer_detail.tags`
  - **ListTransfers**
    - 响应参数变更
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_period`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_encrypted_id`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_prefix_name`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_period_unit`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_transfer_path`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_eps_id`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_bucket_name`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_encrypted_enable`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_dir_pre_fix_name`
      - `- log_transfers.log_transfer_info.log_transfer_detail.dis_id`
      - `- log_transfers.log_transfer_info.log_transfer_detail.dis_name`
      - `- log_transfers.log_transfer_info.log_transfer_detail.kafka_id`
      - `- log_transfers.log_transfer_info.log_transfer_detail.kafka_topic`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_time_zone`
      - `- log_transfers.log_transfer_info.log_transfer_detail.obs_time_zone_id`
      - `- log_transfers.log_transfer_info.log_transfer_detail.tags`
  - **UpdateTransfer**
    - 响应参数变更
      - `- log_transfer_info.log_transfer_detail.obs_period`
      - `- log_transfer_info.log_transfer_detail.obs_encrypted_id`
      - `- log_transfer_info.log_transfer_detail.obs_prefix_name`
      - `- log_transfer_info.log_transfer_detail.obs_period_unit`
      - `- log_transfer_info.log_transfer_detail.obs_transfer_path`
      - `- log_transfer_info.log_transfer_detail.obs_eps_id`
      - `- log_transfer_info.log_transfer_detail.obs_bucket_name`
      - `- log_transfer_info.log_transfer_detail.obs_encrypted_enable`
      - `- log_transfer_info.log_transfer_detail.obs_dir_pre_fix_name`
      - `- log_transfer_info.log_transfer_detail.dis_id`
      - `- log_transfer_info.log_transfer_detail.dis_name`
      - `- log_transfer_info.log_transfer_detail.kafka_id`
      - `- log_transfer_info.log_transfer_detail.kafka_topic`
      - `- log_transfer_info.log_transfer_detail.obs_time_zone`
      - `- log_transfer_info.log_transfer_detail.obs_time_zone_id`
      - `- log_transfer_info.log_transfer_detail.tags`
  - **CreateTransfer**
    - 响应参数变更
      - `- log_transfer_info.log_transfer_detail.obs_period`
      - `- log_transfer_info.log_transfer_detail.obs_encrypted_id`
      - `- log_transfer_info.log_transfer_detail.obs_prefix_name`
      - `- log_transfer_info.log_transfer_detail.obs_period_unit`
      - `- log_transfer_info.log_transfer_detail.obs_transfer_path`
      - `- log_transfer_info.log_transfer_detail.obs_eps_id`
      - `- log_transfer_info.log_transfer_detail.obs_bucket_name`
      - `- log_transfer_info.log_transfer_detail.obs_encrypted_enable`
      - `- log_transfer_info.log_transfer_detail.obs_dir_pre_fix_name`
      - `- log_transfer_info.log_transfer_detail.dis_id`
      - `- log_transfer_info.log_transfer_detail.dis_name`
      - `- log_transfer_info.log_transfer_detail.kafka_id`
      - `- log_transfer_info.log_transfer_detail.kafka_topic`
      - `- log_transfer_info.log_transfer_detail.obs_time_zone`
      - `- log_transfer_info.log_transfer_detail.obs_time_zone_id`
      - `- log_transfer_info.log_transfer_detail.tags`
  - **ListNotificationTemplates**
    - 响应参数变更
      - `+ body`
      - `- create_time`
      - `- project_id`
      - `- templates`
      - `- modify_time`
      - `- name`
      - `- source`
      - `- type`
      - `- locale`
      - `- desc`
  - **UpdateSqlAlarmRule**
    - 请求参数变更
      - `- frequency.type`
      - `- frequency.cron_expr`
      - `- frequency.hour_of_day`
      - `- frequency.day_of_week`
      - `- frequency.fixed_rate`
      - `- frequency.fixed_rate_unit`
      - `- notification_save_rule.language`
      - `- notification_save_rule.timezone`
      - `- notification_save_rule.user_name`
      - `- notification_save_rule.topics`
      - `- notification_save_rule.template_name`
    - 响应参数变更
      - `- frequency.type`
      - `- frequency.cron_expr`
      - `- frequency.hour_of_day`
      - `- frequency.day_of_week`
      - `- frequency.fixed_rate`
      - `- frequency.fixed_rate_unit`
  - **CreateSqlAlarmRule**
    - 请求参数变更
      - `- frequency.type`
      - `- frequency.cron_expr`
      - `- frequency.hour_of_day`
      - `- frequency.day_of_week`
      - `- frequency.fixed_rate`
      - `- frequency.fixed_rate_unit`
      - `- notification_save_rule.language`
      - `- notification_save_rule.timezone`
      - `- notification_save_rule.user_name`
      - `- notification_save_rule.topics`
      - `- notification_save_rule.template_name`
  - **ListSqlAlarmRules**
    - 响应参数变更
      - `- sql_alarm_rules.frequency.type`
      - `- sql_alarm_rules.frequency.cron_expr`
      - `- sql_alarm_rules.frequency.hour_of_day`
      - `- sql_alarm_rules.frequency.day_of_week`
      - `- sql_alarm_rules.frequency.fixed_rate`
      - `- sql_alarm_rules.frequency.fixed_rate_unit`
  - **UpdateKeywordsAlarmRule**
    - 请求参数变更
      - `- frequency.type`
      - `- frequency.cron_expr`
      - `- frequency.hour_of_day`
      - `- frequency.day_of_week`
      - `- frequency.fixed_rate`
      - `- frequency.fixed_rate_unit`
      - `- notification_save_rule.language`
      - `- notification_save_rule.timezone`
      - `- notification_save_rule.user_name`
      - `- notification_save_rule.topics`
      - `- notification_save_rule.template_name`
  - **CreateKeywordsAlarmRule**
    - 请求参数变更
      - `- notification_save_rule.language`
      - `- notification_save_rule.timezone`
      - `- notification_save_rule.user_name`
      - `- notification_save_rule.topics`
      - `- notification_save_rule.template_name`
  - **ListKeywordsAlarmRules**
    - 响应参数变更
      - `- keywords_alarm_rules.frequency.type`
      - `- keywords_alarm_rules.frequency.cron_expr`
      - `- keywords_alarm_rules.frequency.hour_of_day`
      - `- keywords_alarm_rules.frequency.day_of_week`
      - `- keywords_alarm_rules.frequency.fixed_rate`
      - `- keywords_alarm_rules.frequency.fixed_rate_unit`

### HuaweiCloud SDK Meeting

- _新增特性_
  - 支持接口`DeleteToken`
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
  - **RunCreateVideoModerationJob**
    - 请求参数变更
      - `+ biz_type`
  - **RunCreateAudioModerationJob**
    - 请求参数变更
      - `+ biz_type`
  - **RunTextModeration**
    - 请求参数变更
      - `+ biz_type`
  - **CheckImageModeration**
    - 请求参数变更
      - `+ biz_type`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`RestoreTablesNew`、`UpgradeDbVersionNew`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.58 2023-09-07

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持接口`DeleteStackEnhanced`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK AS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListScalingActivityLogs**
    - 响应参数变更
      - `* scaling_activity_log.scaling_value: string -> int32`
  - **CreateScalingPolicy**
    - 请求参数变更
      - `+ scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **UpdateScalingPolicy**
    - 请求参数变更
      - `+ scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ShowScalingPolicy**
    - 响应参数变更
      - `+ scaling_policy.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policy.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ListScalingPolicies**
    - 响应参数变更
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **CreateScalingV2Policy**
    - 请求参数变更
      - `+ scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ListAllScalingV2Policies**
    - 响应参数变更
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **UpdateScalingV2Policy**
    - 请求参数变更
      - `+ scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ShowScalingV2Policy**
    - 响应参数变更
      - `+ scaling_policy.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policy.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ListScalingV2Policies**
    - 响应参数变更
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ListScalingActivityV2Logs**
    - 响应参数变更
      - `* scaling_activity_log.scaling_value: string -> int32`
  - **CreateScalingGroup**
    - 请求参数变更
      - `+ lbaas_listeners.protocol_version`
  - **ListScalingGroups**
    - 响应参数变更
      - `+ scaling_groups.lbaas_listeners.protocol_version`
  - **UpdateScalingGroup**
    - 请求参数变更
      - `+ lbaas_listeners.protocol_version`
  - **ShowScalingGroup**
    - 响应参数变更
      - `+ scaling_group.lbaas_listeners.protocol_version`

### HuaweiCloud SDK CAE

- _新增特性_
  - 支持接口`ListEips`、`UpdateEip`
- _解决问题_
  - 无
- _特性变更_
  - **ShowApplication**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Application]`
  - **CreateAgency**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Agency]`
  - **ListAgencies**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Agency]`
  - **ListEnvironments**
    - 响应参数变更
      - `+ kind`
      - `- Kind`
      - `+ api_version: enum value [v1]`
  - **CreateEnvironment**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Environment]`
  - **CreateApplication**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Application]`
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Application]`
  - **ListApplications**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Application]`
  - **ListComponentConfigurations**
    - 响应参数变更
      - `+ items.type: enum value [customMetric]`
  - **CreateComponentConfiguration**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [ComponentConfiguration]`
  - **ListComponentEvents**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [ComponentEvent]`
  - **ListComponentInstances**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [ComponentConfiguration]`
  - **ListVolumes**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Volume]`
  - **CreateVolume**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Volume]`
  - **DeleteVolume**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
  - **UpdateCertificate**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Certificate]`
  - **ListComponentSnapshots**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [ComponentSnapshot]`
  - **ShowJob**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Job]`
  - **ListDomains**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
  - **CreateDomain**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Domain]`
    - 响应参数变更
      - `+ api_version: enum value [v1]`
  - **ListCertificates**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Certificate]`
  - **CreateCertificate**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Certificate]`
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Certificate]`
  - **ListTimerRules**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
  - **CreateTimerRule**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
  - **UpdateTimerRule**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
  - **ShowExecutionResult**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
  - **ShowComponent**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
  - **UpdateComponent**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
  - **ExecuteAction**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Action]`
  - **CreateComponent**
    - 请求参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
  - **ListComponents**
    - 响应参数变更
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`

### HuaweiCloud SDK CES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateEvents**
    - 请求参数变更
      - `+ detail.dimensions`
  - **ListEventDetail**
    - 响应参数变更
      - `- dimensions`
      - `+ event_info.detail.dimensions`

### HuaweiCloud SDK CPTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAgentConfig**
    - 响应参数变更
      - `+ result.pulsar_enable`
      - `+ result.pulsar_shadow_topic_prefix`
      - `+ result.mock_rule_list.response_header`
      - `+ result.mock_rule_list.response_body`
      - `+ result.mock_rule_list.response_time`
      - `+ result.mock_rule_list.response_code`
  - **UpdateAgentHealthStatus**
    - 响应参数变更
      - `+ result.result.pulsar_enable`
      - `+ result.result.pulsar_shadow_topic_prefix`
      - `+ result.result.mock_rule_list.response_header`
      - `+ result.result.mock_rule_list.response_body`
      - `+ result.result.mock_rule_list.response_time`
      - `+ result.result.mock_rule_list.response_code`

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **StartJob**
    - 请求参数变更
      - `+ jobParams.type`
      - `- jobParams.paramType`
  - **RunOnce**
    - 请求参数变更
      - `+ jobParams.type`
      - `- jobParams.paramType`
  - **ListJobInstances**
    - 请求参数变更
      - `+ limit`
      - `+ offset`
      - `+ minPlanTime`
      - `+ maxPlanTime`
      - `+ status`
      - `+ preciseQuery`
      - `+ jobName`
      - `+ instanceType`
    - 响应参数变更
      - `+ instances.submitTime`
      - `+ instances.instanceId`
      - `+ instances.jobId`
      - `+ instances.jobInstanceName`
      - `+ instances.instanceType`
      - `+ instances.version`
      - `+ instances.ignoreSuccess`
      - `+ instances.forceSuccess`
      - `- instances.instancesId`
      - `+ instances.status: enum value [waiting,running,success,fail,running-exception,pause,manual-stop]`
      - `* instances.planTime: int32 -> int64`
      - `* instances.startTime: int32 -> int64`
      - `* instances.endTime: int32 -> int64`
      - `* instances.executeTime: int32 -> int64`
  - **ListJobs**
    - 响应参数变更
      - `- schedule`
      - `- nodes`
      - `- basicConfig`
      - `- name`
      - `- params`
      - `- jobType`
      - `- directory`
      - `+ jobs.owner`
      - `+ jobs.priority`
      - `+ jobs.status`
      - `+ jobs.createUser`
      - `+ jobs.createTime`
      - `+ jobs.startTime`
      - `+ jobs.endTime`
      - `+ jobs.lastInstanceStatus`
      - `+ jobs.lastInstanceEndTime`
      - `+ jobs.lastUpdateTime`
      - `+ jobs.lastUpdateUser`
      - `+ jobs.path`
      - `+ jobs.singleNodeJobFlag`
      - `+ jobs.flinkJobInfo`
      - `+ jobs.alarms`
      - `- jobs.nodes`
      - `- jobs.schedule`
      - `- jobs.params`
      - `- jobs.directory`
      - `- jobs.basicConfig`
      - `- jobs.jobType: enum value [BATCH,REAL_TIME]`
      - `* jobs: list<JobInfo> -> list<JobResult>`
  - **CreateJob**
    - 请求参数变更
      - `+ logPath`
      - `+ lastUpdateUser`
      - `+ approvers`
      - `+ processType`
      - `+ targetStatus`
      - `- jobType`
      - `+ schedule.type`
      - `- schedule.scheType`
      - `+ params.type`
      - `- params.paramType`
      - `+ nodes.type`
      - `+ nodes.preNodeName`
      - `+ nodes.conditions`
      - `+ nodes.properties`
      - `- nodes.nodeType`
      - `- nodes.preNodeNames`
      - `- nodes.condition`
      - `- nodes.nodeProperties`
      - `+ nodes.failPolicy: enum value [FAIL_CHILD]`
      - `* nodes.location.x: int32 -> string`
      - `* nodes.location.y: int32 -> string`
      - `+ nodes.cronTrigger.expressionTimeZone`
      - `+ nodes.cronTrigger.period`
      - `+ nodes.cronTrigger.concurrent`
      - `* nodes.cronTrigger.dependJobs.jobs: string -> list<string>`
      - `- nodes.cronTrigger.dependJobs.dependFailPolicy: enum value [FAIL,IGNORE,SUSPEND]`
      - `* nodes.cronTrigger.dependJobs: list<DependJob> -> list<DependJobs>`
      - `* nodes.cronTrigger: object<Cron> -> object<CronTrigger>`
  - **ShowJob**
    - 响应参数变更
      - `+ logPath`
      - `+ lastUpdateUser`
      - `+ approvers`
      - `+ processType`
      - `+ targetStatus`
      - `- jobType`
      - `+ schedule.type`
      - `- schedule.scheType`
      - `+ params.type`
      - `- params.paramType`
      - `+ nodes.type`
      - `+ nodes.preNodeName`
      - `+ nodes.conditions`
      - `+ nodes.properties`
      - `- nodes.nodeType`
      - `- nodes.preNodeNames`
      - `- nodes.condition`
      - `- nodes.nodeProperties`
      - `+ nodes.failPolicy: enum value [FAIL_CHILD]`
      - `* nodes.location.x: int32 -> string`
      - `* nodes.location.y: int32 -> string`
      - `+ nodes.cronTrigger.expressionTimeZone`
      - `+ nodes.cronTrigger.period`
      - `+ nodes.cronTrigger.concurrent`
      - `* nodes.cronTrigger.dependJobs.jobs: string -> list<string>`
      - `- nodes.cronTrigger.dependJobs.dependFailPolicy: enum value [FAIL,IGNORE,SUSPEND]`
      - `* nodes.cronTrigger.dependJobs: list<DependJob> -> list<DependJobs>`
      - `* nodes.cronTrigger: object<Cron> -> object<CronTrigger>`
  - **UpdateJob**
    - 请求参数变更
      - `+ logPath`
      - `+ lastUpdateUser`
      - `+ approvers`
      - `+ processType`
      - `+ targetStatus`
      - `- jobType`
      - `+ schedule.type`
      - `- schedule.scheType`
      - `+ params.type`
      - `- params.paramType`
      - `+ nodes.type`
      - `+ nodes.preNodeName`
      - `+ nodes.conditions`
      - `+ nodes.properties`
      - `- nodes.nodeType`
      - `- nodes.preNodeNames`
      - `- nodes.condition`
      - `- nodes.nodeProperties`
      - `+ nodes.failPolicy: enum value [FAIL_CHILD]`
      - `* nodes.location.x: int32 -> string`
      - `* nodes.location.y: int32 -> string`
      - `+ nodes.cronTrigger.expressionTimeZone`
      - `+ nodes.cronTrigger.period`
      - `+ nodes.cronTrigger.concurrent`
      - `* nodes.cronTrigger.dependJobs.jobs: string -> list<string>`
      - `- nodes.cronTrigger.dependJobs.dependFailPolicy: enum value [FAIL,IGNORE,SUSPEND]`
      - `* nodes.cronTrigger.dependJobs: list<DependJob> -> list<DependJobs>`
      - `* nodes.cronTrigger: object<Cron> -> object<CronTrigger>`
  - **CreateSupplementdata**
    - 请求参数变更
      - `+ logPath`
      - `+ lastUpdateUser`
      - `+ approvers`
      - `+ processType`
      - `+ targetStatus`
      - `- jobType`
      - `+ dependJobs.processType`
      - `+ dependJobs.lastUpdateUser`
      - `+ dependJobs.logPath`
      - `+ dependJobs.targetStatus`
      - `+ dependJobs.approvers`
      - `- dependJobs.jobType`
      - `+ dependJobs.schedule.type`
      - `- dependJobs.schedule.scheType`
      - `+ dependJobs.params.type`
      - `- dependJobs.params.paramType`
      - `+ dependJobs.nodes.type`
      - `+ dependJobs.nodes.preNodeName`
      - `+ dependJobs.nodes.conditions`
      - `+ dependJobs.nodes.properties`
      - `- dependJobs.nodes.nodeType`
      - `- dependJobs.nodes.preNodeNames`
      - `- dependJobs.nodes.condition`
      - `- dependJobs.nodes.nodeProperties`
      - `+ dependJobs.nodes.failPolicy: enum value [FAIL_CHILD]`
      - `* dependJobs.nodes.location.x: int32 -> string`
      - `* dependJobs.nodes.location.y: int32 -> string`
      - `+ dependJobs.nodes.cronTrigger.expressionTimeZone`
      - `+ dependJobs.nodes.cronTrigger.period`
      - `+ dependJobs.nodes.cronTrigger.concurrent`
      - `* dependJobs.nodes.cronTrigger.dependJobs.jobs: string -> list<string>`
      - `- dependJobs.nodes.cronTrigger.dependJobs.dependFailPolicy: enum value [FAIL,IGNORE,SUSPEND]`
      - `* dependJobs.nodes.cronTrigger.dependJobs: list<DependJob> -> list<DependJobs>`
      - `* dependJobs.nodes.cronTrigger: object<Cron> -> object<CronTrigger>`

### HuaweiCloud SDK DRS

- _新增特性_
  - 支持以下接口：
    - `StopJobAction`
    - `ShowDataProgress`
    - `UpdateDataProgress`
    - `ShowDataProcessingRulesResult`
    - `CheckDataFilter`
    - `ShowDataFilteringResult`
    - `CollectColumns`
    - `ShowColumnInfoResult`
    - `BatchStopJobsAction`
    - `ExportOperationInfo`
    - `BatchTagAction`
    - `ListProjectTags`
    - `ShowInstanceTags`
    - `UpdateStartPosition`
    - `ShowMonitorData`
    - `ShowSupportObjectType`
    - `ShowIncrementComponentsDetail`
    - `CollectDbObjectsInfo`
    - `ShowDbObjectsList`
- _解决问题_
  - 无
- _特性变更_
  - **ShowDbObjectTemplateResult**
    - 请求参数变更
      - `+ type: enum value [change]`
  - **ShowUpdateObjectSavingStatus**
    - 请求参数变更
      - `+ X-Language: enum value [en-us,zh-cn]`
  - **ShowObjectMapping**
    - 请求参数变更
      - `+ X-Language: enum value [en-us,zh-cn]`
  - **ListJobs**
    - 请求参数变更
      - `+ instance_ids`
      - `+ instance_ip`
  - **ShowDbObjectCollectionStatus**
    - 请求参数变更
      - `+ X-Language: enum value [en-us,zh-cn]`
  - **UpdateBatchAsyncJobs**
    - 请求参数变更
      - `+ jobs.type: enum value [re_create,expired_days]`
  - **UpdateJob**
    - 请求参数变更
      - `+ job.type: enum value [re_create,expired_days]`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListInstancesResourceMetrics`、`ListInstancesRecommendation`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.57 2023-08-31

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListCustomerselfResourceRecordDetails**
    - 请求参数变更
      - `+ query_type`
      - `+ bill_cycle_begin`
      - `+ bill_cycle_end`

### HuaweiCloud SDK CAE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListComponentConfigurations**
    - 响应参数变更
      - `+ items.type: enum value [apm2,log]`
  - **CreateComponentConfiguration**
    - 请求参数变更
      - `+ items.type: enum value [apm2,log]`
  - **ListVolumes**
    - 响应参数变更
      - `+ items.resource_sub_type: enum value [sfs3.0]`
  - **CreateVolume**
    - 请求参数变更
      - `+ spec.resource_sub_type: enum value [sfs3.0]`
  - **UpdateCertificate**
    - 请求参数变更
      - `- spec.policy`
  - **ListDomains**
    - 响应参数变更
      - `- items.metadata.zone_id`
      - `- items.metadata.zone_type`
  - **CreateDomain**
    - 响应参数变更
      - `- items.metadata.zone_id`
      - `- items.metadata.zone_type`
  - **ListCertificates**
    - 响应参数变更
      - `- items.spec.policy`
  - **CreateCertificate**
    - 请求参数变更
      - `- spec.policy`
    - 响应参数变更
      - `- items.spec.policy`
  - **CreateComponent**
    - 请求参数变更
      - `+ spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`

### HuaweiCloud SDK CCE

- _新增特性_
  - 支持接口`RollbackAddonInstance`、`ResizeCluster`、`BatchCreateClusterTags`、`BatchDeleteClusterTags`
- _解决问题_
  - 无
- _特性变更_
  - **ShowAddonInstance**
    - 响应参数变更
      - `+ status.isRollbackable`
      - `+ status.previousVersion`
      - `+ status.status: enum value [rollbackFailed]`
  - **UpdateAddonInstance**
    - 响应参数变更
      - `+ status.isRollbackable`
      - `+ status.previousVersion`
      - `+ status.status: enum value [rollbackFailed]`
  - **CreateAddonInstance**
    - 响应参数变更
      - `+ status.isRollbackable`
      - `+ status.previousVersion`
      - `+ status.status: enum value [rollbackFailed]`
  - **ListAddonInstances**
    - 响应参数变更
      - `+ items.status.isRollbackable`
      - `+ items.status.previousVersion`
      - `+ items.status.status: enum value [rollbackFailed]`

### HuaweiCloud SDK CCM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **IssueCertificateAuthorityCertificate**
    - 请求参数变更
      - `+ enterprise_project_id`
  - **CreateCertificateByCsr**
    - 请求参数变更
      - `+ enterprise_project_id`

### HuaweiCloud SDK CES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowResourceGroup**
    - 响应参数变更
      - `+ resources.event_type`
  - **ListResourceGroup**
    - 响应参数变更
      - `+ resource_groups.type`
      - `+ resource_groups.relation_ids`
      - `+ resource_groups.resources`
  - **ListEventDetail**
    - 响应参数变更
      - `+ dimensions`

### HuaweiCloud SDK CES

- _新增特性_
  - 支持以下接口：
    - `ListDashboardInfos`
    - `CreateOneDashboard`
    - `UpdateDashboard`
    - `DeleteDashboards`
    - `ListDashboardWidgets`
    - `CreateDashboardWidgets`
    - `ShowWidget`
    - `DeleteOneWidget`
    - `BatchUpdateWidgets`
- _解决问题_
  - 无
- _特性变更_
  - **ListAlarmRulePolicies**
    - 响应参数变更
      - `+ policies.extra_info`
      - `+ policies.type`
      - `* policies: list<Policy> -> list<ListPolicy>`
  - **UpdateAlarmRulePolicies**
    - 请求参数变更
      - `+ policies.type`
      - `* policies: list<Policy> -> list<UpdatePolicy>`
    - 响应参数变更
      - `+ policies.type`
      - `* policies: list<Policy> -> list<UpdatePolicy>`
  - **ListAlarmTemplates**
    - 响应参数变更
      - `- alarm_templates.association_alarm_total`
      - `- alarm_templates.policy_total`
      - `- alarm_templates.policy_statistics`
      - `- alarm_templates.association_resource_groups`
  - **ShowAlarmTemplate**
    - 响应参数变更
      - `- association_alarm_total`

### HuaweiCloud SDK CodeArtsDeploy

- _新增特性_
  - 支持以下接口：
    - `ListHostClusters`
    - `CreateHostCluster`
    - `ShowHostClusterDetail`
    - `ListNewHosts`
    - `CreateHost`
    - `ShowHostDetail`
    - `ListEnvironments`
    - `CreateEnvironment`
    - `ShowEnvironmentDetail`
    - `DeleteEnvironment`
    - `ImportHostToEnvironment`
    - `DeleteHostFromEnvironment`
    - `ListAllApp`
    - `CreateApp`
    - `ShowAppDetailById`
    - `DeleteApplication`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DAS

- _新增特性_
  - 支持接口`CreateTuning`、`ShowTuning`
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
  - **ShowInstance**
    - 响应参数变更
      - `+ available_zones`

### HuaweiCloud SDK DGC

- _新增特性_
  - 支持接口`ListSupplementdata`、`CreateSupplementdata`、`StopSupplementdata`
- _解决问题_
  - 无
- _特性变更_
  - **ShowJob**
    - 响应参数变更
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **UpdateJob**
    - 请求参数变更
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **CreateJob**
    - 请求参数变更
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **ListJobs**
    - 响应参数变更
      - `* jobs.basicConfig.priority: string -> int32`
      - `* jobs.basicConfig.instanceTimeout: string -> int32`

### HuaweiCloud SDK DLF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowJob**
    - 响应参数变更
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **UpdateJob**
    - 请求参数变更
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **CreateJob**
    - 请求参数变更
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **ListJobs**
    - 响应参数变更
      - `* jobs.basicConfig.priority: string -> int32`
      - `* jobs.basicConfig.instanceTimeout: string -> int32`

### HuaweiCloud SDK DLI

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSqlJobs**
    - 响应参数变更
      - `+ jobs.cpu_cost`
      - `+ jobs.output_byte`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowJob**
    - 响应参数变更
      - `+ entities.server_id`
      - `+ entities.nic_id`
  - **CreateServers**
    - 请求参数变更
      - `+ server.extendparam.CB_CSBS_BACKUP`

### HuaweiCloud SDK ER

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BatchCreateResourceTags**
    - 请求参数变更
      - `- sys_tags`
  - **ShowStaticRoute**
    - 响应参数变更
      - `- route.attachments.priority`
  - **UpdateStaticRoute**
    - 响应参数变更
      - `- route.attachments.priority`
  - **ListStaticRoutes**
    - 响应参数变更
      - `- routes.attachments.priority`
  - **CreateStaticRoute**
    - 响应参数变更
      - `- route.attachments.priority`
  - **ListEffectiveRoutes**
    - 响应参数变更
      - `- routes.address_group_id`
      - `- routes.next_hops.priority`

### HuaweiCloud SDK FRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **DetectFaceByFile**
    - 响应参数变更
      - `+ faces.attributes.gender`
  - **DetectFaceByFileIntl**
    - 响应参数变更
      - `+ faces.attributes.gender`
  - **DetectFaceByUrl**
    - 响应参数变更
      - `+ faces.attributes.gender`
  - **DetectFaceByUrlIntl**
    - 响应参数变更
      - `+ faces.attributes.gender`
  - **DetectFaceByBase64**
    - 响应参数变更
      - `+ faces.attributes.gender`
  - **DetectFaceByBase64Intl**
    - 响应参数变更
      - `+ faces.attributes.gender`

### HuaweiCloud SDK GES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ExportGraph2**
    - 请求参数变更
      - `+ paginate`

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **StopSimCard**
    - 请求参数变更
      - `+ iccid`
  - **ResetSimCard**
    - 请求参数变更
      - `+ iccid`
  - **ShowSimCard**
    - 请求参数变更
      - `+ iccid`
  - **EnableSimCard**
    - 请求参数变更
      - `+ iccid`
  - **ShowRealNamed**
    - 请求参数变更
      - `+ iccid`
  - **StartStopNet**
    - 请求参数变更
      - `+ iccid`
  - **SetExceedCutNet**
    - 请求参数变更
      - `+ iccid`
  - **RegisterImei**
    - 请求参数变更
      - `+ iccid`
  - **DeleteRealName**
    - 请求参数变更
      - `+ iccid`
  - **SetSpeedValue**
    - 请求参数变更
      - `+ iccid`
  - **ListSimPricePlans**
    - 请求参数变更
      - `+ iccid`
  - **BatchSetTags**
    - 请求参数变更
      - `+ iccids`
  - **BatchSetAttributes**
    - 请求参数变更
      - `+ attributes.iccid`
  - **ShowMonthUsages**
    - 请求参数变更
      - `+ iccids`
    - 响应参数变更
      - `+ month_usages.iccid`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateInstanceByEngine**
    - 请求参数变更
      - `- engine_version: enum value [1.1.0,2.7]`
  - **CreatePostPaidInstance**
    - 请求参数变更
      - `- engine_version: enum value [1.1.0,2.7]`

### HuaweiCloud SDK KooMessage

- _新增特性_
  - 支持接口`ShowTemplateVideoThumbnail`、`SetPrimaryVideoThumbnail`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`ShowMrsVersionList`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeSmartDocumentRecognizer`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RAM

- _新增特性_
  - 支持接口`ListResourceTypes`
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
  - **ListInstances**
    - 响应参数变更
      - `+ instances.public_dns_names`

### HuaweiCloud SDK ServiceStage

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ChangeResourceInEnvironment**
    - 响应参数变更
      - `+ deploy_mode`

# 3.1.56 2023-08-24

HuaweiCloud SDK APIG

- 新增特性
  - 支持以下接口：
    - ListEndpointConnections
    - AcceptOrRejectEndpointConnections
    - ListEndpointPermissions
    - AddEndpointPermissions
    - DeleteEndpointPermissions
- 解决问题
  - 无
- 特性变更
  - AssociateSignatureKeyV2
    - 响应参数变更
      - + bindings.req_method
  - ListSignatureKeysBindedToApiV2
    - 响应参数变更
      - + bindings.req_method
  - ListApisNotBoundWithSignatureKeyV2
    - 响应参数变更
      - + apis.req_method
  - ListApisBindedToSignatureKeyV2
    - 响应参数变更
      - + bindings.req_method
  - ListApisBindedToRequestThrottlingPolicyV2
    - 响应参数变更
      - + apis.req_method
  - ListApisUnbindedToRequestThrottlingPolicyV2
    - 响应参数变更
      - + apis.req_method
  - ListApiRuntimeDefinitionV2
    - 响应参数变更
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - ListApisBindedToAclPolicyV2
    - 响应参数变更
      - + apis.req_method
  - ListApisUnbindedToAclPolicyV2
    - 响应参数变更
      - + apis.req_method
  - ShowDetailsOfCustomAuthorizersV2
    - 响应参数变更
      - + network_type
  - UpdateCustomAuthorizerV2
    - 请求参数变更
      - + network_type
    - 响应参数变更
      - + network_type
  - ListInstancesV2
    - 响应参数变更
      - + instances.cbc_operation_locks
      - + instances.status: enum value [Resizing,ResizeFailed,ResizeTimeout]
      - + instances.instance_status: enum value [42,43,44]
      - + instances.spec: enum value [PLATINUM_X2,PLATINUM_X3,PLATINUM_X4,PLATINUM_X5,PLATINUM_X6,PLATINUM_X7,PLATINUM_X8]
  - CreateInstanceV2
    - 请求参数变更
      - + spec_id: enum value [PLATINUM_X2,PLATINUM_X3,PLATINUM_X4,PLATINUM_X5,PLATINUM_X6,PLATINUM_X7,PLATINUM_X8]
  - ShowDetailsOfInstanceV2
    - 响应参数变更
      - + cbc_operation_locks
      - + status: enum value [Resizing,ResizeFailed,ResizeTimeout]
      - + instance_status: enum value [42,43,44]
      - + spec: enum value [PLATINUM_X2,PLATINUM_X3,PLATINUM_X4,PLATINUM_X5,PLATINUM_X6,PLATINUM_X7,PLATINUM_X8]
  - UpdateInstanceV2
    - 响应参数变更
      - + cbc_operation_locks
      - + status: enum value [Resizing,ResizeFailed,ResizeTimeout]
      - + instance_status: enum value [42,43,44]
      - + spec: enum value [PLATINUM_X2,PLATINUM_X3,PLATINUM_X4,PLATINUM_X5,PLATINUM_X6,PLATINUM_X7,PLATINUM_X8]
  - ShowDetailsOfApiV2
    - 响应参数变更
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - UpdateApiV2
    - 请求参数变更
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
    - 响应参数变更
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - ListApiVersionDetailV2
    - 响应参数变更
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - CreateCustomAuthorizerV2
    - 请求参数变更
      - + network_type
    - 响应参数变更
      - + network_type
  - ListCustomAuthorizersV2
    - 响应参数变更
      - + network_type
      - + authorizer_list.network_type
  - CreateApiV2
    - 请求参数变更
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
    - 响应参数变更
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - ListApisV2
    - 响应参数变更
      - + apis.content_type: enum value [multipart/form-data]
      - - apis.content_type: enum value [multipart/form-date]

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RestoreBackup**
    - 请求参数变更
      - `+ restore.details`

### HuaweiCloud SDK CCM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowCertificateAuthority**
    - 响应参数变更
      - `+ enterprise_project_id`
  - **ShowCertificate**
    - 响应参数变更
      - `+ enterprise_project_id`
  - **CreateCertificateAuthority**
    - 请求参数变更
      - `+ enterprise_project_id`
  - **ListCertificateAuthority**
    - 响应参数变更
      - `+ enterprise_project_id`
      - `+ certificate_authorities.enterprise_project_id`
  - **CreateCertificate**
    - 请求参数变更
      - `+ enterprise_project_id`
  - **ListCertificate**
    - 响应参数变更
      - `+ enterprise_project_id`
      - `+ certificates.enterprise_project_id`

### HuaweiCloud SDK CPTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAgentConfig**
    - 响应参数变更
      - `+ result.clickhouse_enable`
      - `+ result.clickhouse_shadow_type`
      - `+ result.clickhouse_shadow_repository`
  - **UpdateAgentHealthStatus**
    - 响应参数变更
      - `+ result.result.clickhouse_enable`
      - `+ result.result.clickhouse_shadow_type`
      - `+ result.result.clickhouse_shadow_repository`

### HuaweiCloud SDK EG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateSubscriptionTarget**
    - 请求参数变更
      - `+ detail.url`
      - `+ detail.agency_name`
      - `+ detail.invocation_http_parameters`
      - `* detail: object -> object<Detail>`
  - **UpdateSubscriptionTarget**
    - 请求参数变更
      - `+ detail.url`
      - `+ detail.agency_name`
      - `+ detail.invocation_http_parameters`
      - `* detail: object -> object<Detail>`
  - **UpdateSubscription**
    - 请求参数变更
      - `+ targets.detail.url`
      - `+ targets.detail.agency_name`
      - `+ targets.detail.invocation_http_parameters`
      - `* targets.detail: object -> object<Detail>`
  - **CreateSubscription**
    - 请求参数变更
      - `+ targets.detail.url`
      - `+ targets.detail.agency_name`
      - `+ targets.detail.invocation_http_parameters`
      - `* targets.detail: object -> object<Detail>`

### HuaweiCloud SDK ER

- _新增特性_
  - 支持接口`AcceptAttachment`、`RejectAttachment`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK HSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListJarPackageHostInfo**
    - 响应参数变更
      - `* data_list.record_time: int32 -> int64`

### HuaweiCloud SDK IMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **GlanceListImages**
    - 响应参数变更
      - `- __root_origin`
      - `- min_disk`
      - `- __image_source_type`
      - `- container_format`
      - `- __image_size`
      - `- __support_xen_gpu_type`
      - `- protected`
      - `- __support_kvm_gpu_type`
      - `- max_ram`
      - `- id`
      - `- __isregistered`
      - `- __lazyloading`
      - `- __data_origin`
      - `- hw_firmware_type`
      - `- __os_type`
      - `- hw_vif_multiqueue_enabled`
      - `- visibility`
      - `- virtual_env_type`
      - `- __image_location`
      - `- __support_kvm`
      - `- __support_highperformance`
      - `- tags`
      - `- __backup_id`
      - `- __platform`
      - `- enterprise_project_id`
      - `- size`
      - `- __support_arm`
      - `- __support_diskintensive`
      - `- __os_version`
      - `- name`
      - `- active_at`
      - `- status`
      - `- schema`
      - `- __is_offshelved`
      - `- __support_kvm_infiniband`
      - `- created_at`
      - `- __originalimagename`
      - `- __support_agent_list`
      - `- __support_amd`
      - `- file`
      - `- updated_at`
      - `- __productcode`
      - `- checksum`
      - `- __support_fc_inject`
      - `- __description`
      - `- min_ram`
      - `- owner`
      - `- __imagetype`
      - `- __support_xen`
      - `- __is_config_init`
      - `- __account_code`
      - `- __system__cmkid`
      - `- __os_bit`
      - `- __support_xen_hana`
      - `- disk_format`
      - `- self`
      - `- __support_largememory`
      - `- __os_feature_list`
      - `- virtual_size`
      - `- __sequence_num`
      - `+ images._sys_enterprise_project_id`
      - `* images: list<GlanceShowImageResponseBody> -> list<GlanceShowImageListResponseBody>`

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 支持以下接口：
    - `BatchListAppConfigsTemplates`
    - `AddAppConfigsTemplates`
    - `ShowAppConfigsTemplate`
    - `DeleteAppConfigsTemplate`
    - `AddGeneralAppConfigsTemplate`
    - `ShowModuleShadow`
    - `UpdateModuleShadow`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateModule**
    - 请求参数变更
      - `+ desired_state`

### HuaweiCloud SDK KooMessage

- _新增特性_
  - 支持以下接口：
    - `ListAimMsgTemplate`
    - `CreateAimMsgTemplate`
    - `ShowAimMsgTemplateVariable`
    - `SendAimBatchMessages`
    - `SendAimBatchDifferentMessages`
    - `DeleteAimMsgSignature`
    - `ShowAimMsgTemplateDetail`
    - `UpdateAimMsgTemplate`
    - `DeleteAimMsgTemplate`
    - `ListAimMsgSignature`
    - `AddAimMsgSignature`
    - `ListAimMsgApp`
    - `CreateSmsApp`
    - `ListAimMsgAppDetail`
    - `UpdateAimMsgApp`
    - `ShowAimMsgSignatureFileInfo`
    - `UploadAimMsgSignatureFile`
    - `ListAimMsgSignatureDetail`
    - `UpdateAimMsgSignature`
- _解决问题_
  - 无
- _特性变更_
  - **ListAimResolveDetails**
    - 请求参数变更
      - `+ task_name`
    - 响应参数变更
      - `+ resolve_details.task_name`
  - **ListResolveTasks**
    - 请求参数变更
      - `+ task_name`
    - 响应参数变更
      - `+ resolve_tasks.task_name`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateLogStream**
    - 请求参数变更
      - `* tags: object<tagsBody> -> list<tagsBody>`

### HuaweiCloud SDK NAT

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListNatGateways**
    - 响应参数变更
      - `+ nat_gateways.session_conf`
  - **CreateNatGateway**
    - 请求参数变更
      - `+ nat_gateway.session_conf`
    - 响应参数变更
      - `+ nat_gateway.session_conf`
  - **ShowNatGateway**
    - 响应参数变更
      - `+ nat_gateway.session_conf`
  - **UpdateNatGateway**
    - 请求参数变更
      - `+ nat_gateway.session_conf`
    - 响应参数变更
      - `+ nat_gateway.session_conf`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RecognizeVatInvoice**
    - 请求参数变更
      - `+ page_num`
    - 响应参数变更
      - `+ result.invoice_tag`
      - `+ result.sum_amount`
      - `+ result.sum_tax`

### HuaweiCloud SDK OSM

- _新增特性_
  - 支持接口`ShowLoginType`
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
  - **RunTts**
    - 请求参数变更
      - `+ config.property: enum value [chinese_huaxiaoman_common,chinese_huaxiaofang_common,chinese_huaxiaojun_common]`

### HuaweiCloud SDK VPC

# 3.1.55 2023-08-21

### HuaweiCloud SDK EdgeSec

- _新增特性_
  - 支持边缘安全服务
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
  - **ListEdgeNodes**
    - 请求参数变更
      - `+ group_id`
  - **UpdateDeviceTwin**
    - 响应参数变更
      - `- property_visitors.register_type`
      - `- property_visitors.access_mode`
      - `- property_visitors.register_index`
      - `- property_visitors.register_num`
      - `- property_visitors.scale_index`
      - `- property_visitors.original_datatype`
      - `- property_visitors.expected_datatype`
      - `- property_visitors.is_registerswap`
      - `- property_visitors.is_swap`
      - `- property_visitors.sample_interval`
      - `- property_visitors.data_min`
      - `- property_visitors.data_max`
      - `- property_visitors.node_id`
      - `- property_visitors.browse_name`
      - `* property_visitors: object<ValueInPropertyVisitors> -> map<string, ValueInPropertyVisitors>`
      - `- twin.excepted`
      - `- twin.actual`
      - `- twin.metadata`
      - `- twin.optional`
      - `* twin: object<ValueInTwinResponse> -> map<string, ValueInTwinResponse>`
  - **ListAppVersions**
    - 响应参数变更
      - `+ versions.configs.dns_policy`
  - **CreateAppVersions**
    - 请求参数变更
      - `+ version.configs.dns_policy`
    - 响应参数变更
      - `+ version.configs.dns_policy`
  - **ShowAppVersionDetail**
    - 响应参数变更
      - `+ version.configs.dns_policy`
  - **UpdateAppVersion**
    - 请求参数变更
      - `+ version.configs.dns_policy`
    - 响应参数变更
      - `+ version.configs.dns_policy`
  - **ListPods**
    - 请求参数变更
      - `+ plugin_instance_name`
    - 响应参数变更
      - `+ pods.configs.dns_policy`
  - **ListApps**
    - 响应参数变更
      - `+ apps.app_versions.configs.dns_policy`
  - **CreateApp**
    - 响应参数变更
      - `+ app.app_versions.configs.dns_policy`
  - **ShowAppDetail**
    - 响应参数变更
      - `+ app.app_versions.configs.dns_policy`
  - **UpdateApp**
    - 响应参数变更
      - `+ app.app_versions.configs.dns_policy`
  - **ListDeployments**
    - 响应参数变更
      - `+ deployments.template.configs.dns_policy`
  - **CreateDeployments**
    - 请求参数变更
      - `+ deployment.template.configs.dns_policy`
    - 响应参数变更
      - `+ template.configs.dns_policy`
  - **ShowDeployment**
    - 响应参数变更
      - `+ template.configs.dns_policy`
  - **UpdateDeployment**
    - 请求参数变更
      - `+ deployment.template.configs.dns_policy`
    - 响应参数变更
      - `+ template.configs.dns_policy`

### HuaweiCloud SDK LTS

- _新增特性_
  - 支持接口`DeleteDashboard`
- _解决问题_
  - 无
- _特性变更_
  - **CreateDashBoard**
    - 响应参数变更
      - `* last_update_time: string -> int64`
      - `* useSystemTemplate: string -> boolean`
  - **CreateLogStream**
    - 请求参数变更
      - `- enterprise_project_name`
      - `- log_stream_name: enum value [lts-stream-13ci]`
      - `* ttl_in_days: string -> int32`
      - `* tags: list<tagsBody> -> object<tagsBody>`
  - **ListAccessConfig**
    - 响应参数变更
      - `+ cluster_id`
      - `+ result.cluster_id`
  - **UpdateAccessConfig**
    - 请求参数变更
      - `+ cluster_id`
    - 响应参数变更
      - `+ cluster_id`
  - **CreateAccessConfig**
    - 请求参数变更
      - `+ cluster_id`
    - 响应参数变更
      - `+ cluster_id`
  - **DeleteAccessConfig**
    - 响应参数变更
      - `+ cluster_id`
      - `+ result.cluster_id`

# 3.1.54 2023-08-17

### HuaweiCloud SDK AOS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateStack**
    - 请求参数变更
      - `+ agencies.agency_urn`
  - **GetStackMetadata**
    - 响应参数变更
      - `+ agencies.agency_urn`
  - **CreateStack**
    - 请求参数变更
      - `+ agencies.agency_urn`

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListApiRuntimeDefinitionV2**
    - 响应参数变更
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
  - **ShowDetailsOfApiV2**
    - 响应参数变更
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
  - **UpdateApiV2**
    - 请求参数变更
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
    - 响应参数变更
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
  - **ListApiVersionDetailV2**
    - 响应参数变更
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
  - **CreateApiV2**
    - 请求参数变更
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
    - 响应参数变更
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
  - **ListApisV2**
    - 响应参数变更
      - `+ apis.req_protocol: enum value [GRPCS]`
      - `+ apis.backend_type: enum value [GRPC]`
      - `+ apis.backend_api.req_protocol: enum value [GRPCS]`

### HuaweiCloud SDK CloudRTC

- _新增特性_
  - 支持接口`ListRtcAbnormalEvent`、`ListRtcEvent`、`ListObsBuckets`、`ListObsBucketObjects`、`UpdateObsBucketAuthority`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Cloudtest

- _新增特性_
  - 支持接口`ShowUserExecuteTestCaseInfo`、`ShowTestCaseAndDefectInfo`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`ShowNodesInformation`
- _解决问题_
  - 无
- _特性变更_
  - **ShowInstance**
    - 响应参数变更
      - `+ cloud_service_type_code`
      - `+ inquery_spec_code`
      - `+ cloud_resource_type_code`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateServers**
    - 请求参数变更
      - `+ server.root_volume.iops`
      - `+ server.root_volume.throughput`
      - `+ server.root_volume.volumetype: enum value [GPSSD2,ESSD2]`
      - `+ server.data_volumes.iops`
      - `+ server.data_volumes.throughput`
      - `+ server.data_volumes.volumetype: enum value [GPSSD2,ESSD2]`
  - **CreatePostPaidServers**
    - 请求参数变更
      - `+ server.data_volumes.iops`
      - `+ server.data_volumes.throughput`
      - `+ server.data_volumes.volumetype: enum value [GPSSD2,ESSD2]`
      - `+ server.root_volume.iops`
      - `+ server.root_volume.throughput`
      - `+ server.root_volume.volumetype: enum value [GPSSD2,ESSD2]`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowEnv**
    - 响应参数变更
      - `+ public_bucket_path`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ModifyGaussMysqlDns`、`CreateGaussMysqlDns`
- _解决问题_
  - 无
- _特性变更_
  - **ShowGaussMySqlInstanceInfo**
    - 响应参数变更
      - `+ instance.private_dns_names`
  - **ListGaussMySqlInstanceDetailInfo**
    - 响应参数变更
      - `+ instances.private_dns_names`

### HuaweiCloud SDK ImageSearch

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `RunCreateInstance`
    - `RunModifyPicture`
    - `RunAddPicture`
    - `RunDeletePicture`
    - `RunSearchPicture`
    - `RunCheckPicture`
    - `RunQueryInstance`
    - `RunDeleteInstance`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BatchRestartOrDeleteInstances**
    - 请求参数变更
      - `+ allFailure`
      - `- all_failure`
  - **CreateInstanceByEngine**
    - 请求参数变更
      - `- engine_version: enum value [2.3.0]`
  - **CreatePostPaidInstance**
    - 请求参数变更
      - `- engine_version: enum value [2.3.0]`

### HuaweiCloud SDK Live

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSnapshotConfigs**
    - 响应参数变更
      - `* body: object<LiveSnapshotConfig> -> list<LiveSnapshotConfig>`

### HuaweiCloud SDK MetaStudio

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListAssetSummary**
    - 响应参数变更
      - `+ asset_list.asset_type: enum value [MUSIC]`
  - **ShowAsset**
    - 响应参数变更
      - `+ asset_type: enum value [MUSIC]`
      - `+ asset_state: enum value [BLOCK]`
      - `+ asset_extra_meta.human_model_2d_meta`
  - **UpdateDigitalAsset**
    - 请求参数变更
      - `+ asset_type: enum value [MUSIC]`
      - `+ asset_extra_meta.human_model_2d_meta`
    - 响应参数变更
      - `+ asset_type: enum value [MUSIC]`
      - `+ asset_state: enum value [BLOCK]`
      - `+ asset_extra_meta.human_model_2d_meta`
  - **CreateDigitalAsset**
    - 请求参数变更
      - `+ asset_type: enum value [MATERIAL,MUSIC]`
      - `+ asset_extra_meta.human_model_2d_meta`
  - **ListAssets**
    - 请求参数变更
      - `+ X-User-MePrivilege`
      - `+ action_editable`
    - 响应参数变更
      - `+ assets.asset_type: enum value [MUSIC]`
      - `+ assets.asset_state: enum value [BLOCK]`
      - `+ assets.asset_extra_meta.human_model_2d_meta`

### HuaweiCloud SDK MPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateThumbnailsTask**
    - 请求参数变更
      - `+ thumbnail_para.dots_ms`
      - `+ thumbnail_para.type: enum value [DOTS_MS]`
  - **CreateTranscodingTask**
    - 请求参数变更
      - `+ thumbnail.params.dots_ms`
      - `+ thumbnail.params.type: enum value [DOTS_MS]`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BatchRestartOrDeleteInstances**
    - 请求参数变更
      - `+ allFailure`
      - `- all_failure`
  - **CreatePostPaidInstanceByEngine**
    - 请求参数变更
      - `- engine_version: enum value [3.7.17]`
  - **CreatePostPaidInstance**
    - 请求参数变更
      - `- engine_version: enum value [3.7.17]`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BatchDeleteInstances**
    - 请求参数变更
      - `+ allFailure`
      - `- all_failure`
  - **CreatePostPaidInstance**
    - 请求参数变更
      - `- engine_version: enum value [5.x]`

### HuaweiCloud SDK ServiceStage

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ModifyApplication**
    - 请求参数变更
      - `+ enterprise_project_id`
  - **CreateEnvironment**
    - 响应参数变更
      - `+ project_id`
      - `- resources`
  - **ShowEnvironments**
    - 响应参数变更
      - `+ environments.project_id`
  - **ShowEnvironmentInfo**
    - 响应参数变更
      - `+ project_id`
  - **ModifyEnvironment**
    - 请求参数变更
      - `- enterprise_project_id`
    - 响应参数变更
      - `+ project_id`
  - **ShowComponentInfo**
    - 响应参数变更
      - `+ affinity.az`
      - `+ affinity.node`
      - `+ affinity.component`
      - `- affinity.kind`
      - `- affinity.condition`
      - `- affinity.weight`
      - `- affinity.match_expressions`
  - **ModifyComponent**
    - 请求参数变更
      - `+ affinity.az`
      - `+ affinity.node`
      - `+ affinity.component`
      - `- affinity.kind`
      - `- affinity.condition`
      - `- affinity.weight`
      - `- affinity.match_expressions`
    - 响应参数变更
      - `- component_id`
  - **CreateComponent**
    - 请求参数变更
      - `+ affinity.az`
      - `+ affinity.node`
      - `+ affinity.component`
      - `- affinity.kind`
      - `- affinity.condition`
      - `- affinity.weight`
      - `- affinity.match_expressions`
  - **ShowComponentsInApplication**
    - 响应参数变更
      - `+ components.external_accesses`
  - **ShowComponents**
    - 响应参数变更
      - `+ components.external_accesses`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateSecurityGroupRule**
    - 请求参数变更
      - `+ security_group_rule.remote_address_group_id`
  - **NeutronCreateSecurityGroupRule**
    - 请求参数变更
      - `+ security_group_rule.remote_address_group_id`

# 3.1.53 2023-08-10

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSubCustomerBillDetail**
    - 响应参数变更
      - `+ fee_records.id`

### HuaweiCloud SDK DNS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListPrivateZones**
    - 请求参数变更
      - `* type: optional -> required`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持以下接口：
    - `DownloadData`
    - `ListDrugJob`
    - `CancelDrugJob`
    - `DeleteDrugJob`
    - `CreateOptmJob`
    - `ShowOptmJob`
    - `CreateSynthesisJob`
    - `ShowSynthesisJob`
    - `CreateDockingJob`
    - `ShowDockingJob`
    - `CreateFepJob`
    - `ShowFepJob`
    - `CreateDrugLigandSvg`
    - `CreateDrugLigandSdf`
    - `RunDrugReceptorPreprocess`
    - `ParseDrugReceptorInfo`
    - `RecognizeDrugReceptorPocket`
    - `RunDrugLigandToSmilesConversion`
    - `CreateDrugLigandInteraction2dSvg`
    - `CheckDrugLigandDifference`
    - `CreateDrugLigandPreviewTask`
    - `ShowDrugLigandPreviewTask`
    - `DeleteDrugLigandPreviewTask`
    - `CreateDrugLigandSimilarityGraphTask`
    - `ShowDrugLigandSimilarityGraphTask`
    - `DeleteDrugLigandSimilarityGraphTask`
- _解决问题_
  - 无
- _特性变更_
  - **ListComputingResourceFlavors**
    - 响应参数变更
      - `+ flavors.az`
  - **StartAutoJob**
    - 响应参数变更
      - `+ max_platform_flavor`
      - `+ app_infos.app_resource`
  - **ListComputingResources**
    - 响应参数变更
      - `+ resources.evs_resource_id`
  - **ExecuteJob**
    - 响应参数变更
      - `+ max_platform_flavor`
      - `+ app_infos.app_resource`
  - **CreateAutoJob**
    - 响应参数变更
      - `+ max_platform_flavor`
      - `+ app_infos.app_resource`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`UpdateProxyPort`、`DescribeBackupEncryptStatus`、`ModifyBackupEncryptStatus`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateProxySessionConsistence**
    - 请求参数变更
      - `+ consistence_mode`
  - **CreateGaussMySqlInstance**
    - 请求参数变更
      - `* datastore: object<MysqlDatastore> -> object<MysqlDatastoreInReq>`
    - 响应参数变更
      - `* instance.datastore: object<MysqlDatastore> -> object<MysqlDatastoreInRes>`
  - **ShowGaussMySqlBackupList**
    - 响应参数变更
      - `- backups.datastore.kernel_version`
      - `* backups.datastore: object<MysqlDatastore> -> object<MysqlDatastoreInBackup>`
  - **ShowGaussMySqlProxyList**
    - 响应参数变更
      - `+ proxy_list.proxy.consistence_mode`

### HuaweiCloud SDK GSL

- _新增特性_
  - 支持接口`ListWorkOrders`、`ListWorkOrderDetails`
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
  - **ListInstanceConsumerGroups**
    - 响应参数变更
      - `+ groups.createdAt`
      - `+ groups.group_desc`
      - `+ groups.lag`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RecognizeMyanmarIdcard**
    - 请求参数变更
      - `+ return_translation`
    - 响应参数变更
      - `+ result.translation_info`

### HuaweiCloud SDK RAM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`SearchDistinctSharedResources`、`SearchDistinctPrincipals`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListXellogFiles`、`CreateXelLogDownload`
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
  - **ShowOneTopic**
    - 响应参数变更
      - `+ message_type`
  - **ShowTopicStatus**
    - 响应参数变更
      - `+ max_offset`
      - `+ min_offset`
  - **ShowInstance**
    - 响应参数变更
      - `+ grpc_address`
      - `+ public_grpc_address`
  - **CreateTopicOrBatchDeleteTopic**
    - 请求参数变更
      - `+ message_type`
  - **ListRocketInstanceTopics**
    - 响应参数变更
      - `+ message_type`
      - `+ topics.message_type`
  - **ListMessages**
    - 响应参数变更
      - `* messages.reconsume_times: string -> int32`
      - `* messages.queue_id: string -> int32`
      - `* messages.queue_offset: string -> int32`
  - **ExportDlqMessage**
    - 响应参数变更
      - `* reconsume_times: string -> int32`
      - `* queue_id: string -> int32`
      - `* queue_offset: string -> int32`
  - **CreatePostPaidInstance**
    - 请求参数变更
      - `+ engine_version: enum value [5.x]`
  - **ListInstances**
    - 响应参数变更
      - `+ grpc_address`
      - `+ public_grpc_address`
      - `+ instances.grpc_address`
      - `+ instances.public_grpc_address`
  - **ShowConsumerListOrDetails**
    - 响应参数变更
      - `+ lag`
      - `+ max_offset`
      - `+ consumer_offset`

# 3.1.52 2023-08-03

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListCustomerselfResourceRecords**
    - 响应参数变更
      - `+ fee_records.id`

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListCustomerselfResourceRecords**
    - 响应参数变更
      - `+ fee_records.id`

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowNode**
    - 响应参数变更
      - `- spec.extendParam.enterprise_project_id`
  - **UpdateNode**
    - 响应参数变更
      - `- spec.extendParam.enterprise_project_id`
  - **DeleteNode**
    - 响应参数变更
      - `- spec.extendParam.enterprise_project_id`
  - **CreateNode**
    - 请求参数变更
      - `- spec.extendParam.enterprise_project_id`
    - 响应参数变更
      - `- spec.extendParam.enterprise_project_id`
  - **ListNodes**
    - 响应参数变更
      - `- items.spec.extendParam.enterprise_project_id`
  - **ShowNodePool**
    - 响应参数变更
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
  - **UpdateNodePool**
    - 响应参数变更
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
  - **DeleteNodePool**
    - 响应参数变更
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
  - **CreateNodePool**
    - 请求参数变更
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
    - 响应参数变更
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
  - **ListNodePools**
    - 响应参数变更
      - `- items.spec.nodeTemplate.extendParam.enterprise_project_id`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDomainDetailByName**
    - 响应参数变更
      - `- domain.sources.weight`
      - `* domain.sources: list<SourcesConfig> -> list<SourcesDomainConfig>`
  - **ShowDomainFullConfig**
    - 响应参数变更
      - `+ configs.remark`
      - `+ configs.ip_frequency_limit`
      - `+ configs.hsts`
      - `+ configs.quic`
      - `+ configs.url_auth.inherit_config`
      - `+ configs.sources.bucket_access_key`
      - `+ configs.sources.bucket_secret_key`
      - `+ configs.sources.bucket_region`
      - `+ configs.sources.bucket_name`
      - `+ configs.request_limit_rules.priority`
      - `+ configs.request_limit_rules.match_type`
      - `+ configs.request_limit_rules.match_value`
  - **UpdateDomainFullConfig**
    - 请求参数变更
      - `+ configs.remark`
      - `+ configs.ip_frequency_limit`
      - `+ configs.hsts`
      - `+ configs.quic`
      - `+ configs.url_auth.inherit_config`
      - `+ configs.sources.bucket_access_key`
      - `+ configs.sources.bucket_secret_key`
      - `+ configs.sources.bucket_region`
      - `+ configs.sources.bucket_name`
      - `+ configs.request_limit_rules.priority`
      - `+ configs.request_limit_rules.match_type`
      - `+ configs.request_limit_rules.match_value`

### HuaweiCloud SDK Config

- _新增特性_
  - 支持以下接口：
    - `ListConformancePacks`
    - `CreateConformancePack`
    - `ShowConformancePack`
    - `DeleteConformancePack`
    - `CollectConformancePackComplianceSummary`
    - `ListConformancePackComplianceByPackId`
    - `ListConformancePackComplianceDetailsByPackId`
    - `ListConformancePackComplianceScores`
    - `ListBuiltInConformancePackTemplates`
    - `ShowBuiltInConformancePackTemplate`
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
  - **ShowAgentConfig**
    - 请求参数变更
      - `+ alias`

### HuaweiCloud SDK CTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **DeleteTracker**
    - 请求参数变更
      - `+ tracker_type: enum value [system]`

### HuaweiCloud SDK EG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDetailOfEventSource**
    - 响应参数变更
      - `+ error_info`
  - **UpdateEventSource**
    - 响应参数变更
      - `+ error_info`
  - **CreateEventSource**
    - 响应参数变更
      - `+ error_info`
  - **ListEventSources**
    - 响应参数变更
      - `+ error_info`
      - `+ items.error_info`
  - **CreateSubscriptionTarget**
    - 请求参数变更
      - `+ smn_detail`
      - `+ dead_letter_queue`
    - 响应参数变更
      - `+ dead_letter_queue`
  - **ShowDetailOfSubscriptionTarget**
    - 响应参数变更
      - `+ dead_letter_queue`
  - **UpdateSubscriptionTarget**
    - 请求参数变更
      - `+ smn_detail`
      - `+ dead_letter_queue`
    - 响应参数变更
      - `+ dead_letter_queue`
  - **ShowDetailOfConnection**
    - 响应参数变更
      - `+ error_info`
  - **UpdateConnection**
    - 响应参数变更
      - `+ error_info`
  - **UpdateEndpoint**
    - 响应参数变更
      - `+ error_info`
  - **ShowDetailOfSubscription**
    - 响应参数变更
      - `+ dead_letter_queue`
      - `+ targets.dead_letter_queue`
  - **UpdateSubscription**
    - 请求参数变更
      - `+ targets.smn_detail`
      - `+ targets.dead_letter_queue`
    - 响应参数变更
      - `+ dead_letter_queue`
      - `+ targets.dead_letter_queue`
  - **CreateConnection**
    - 响应参数变更
      - `+ error_info`
  - **ListConnections**
    - 请求参数变更
      - `+ instance_id`
    - 响应参数变更
      - `+ error_info`
      - `+ items.error_info`
  - **CreateEndpoint**
    - 响应参数变更
      - `+ error_info`
  - **ListEndpoints**
    - 请求参数变更
      - `+ subnet_id`
    - 响应参数变更
      - `+ error_info`
      - `+ items.error_info`
  - **ShowEventStreaming**
    - 响应参数变更
      - `+ source.source_kafka.seek_to: enum value [latest,earliest]`
      - `+ source.source_kafka.sasl_mechanism: enum value [SCRAM-SHA-512,PLAIN]`
  - **UpdateEventStreaming**
    - 请求参数变更
      - `+ source.source_kafka.seek_to: enum value [latest,earliest]`
      - `+ source.source_kafka.sasl_mechanism: enum value [SCRAM-SHA-512,PLAIN]`
  - **CreateSubscription**
    - 请求参数变更
      - `+ targets.smn_detail`
      - `+ targets.dead_letter_queue`
    - 响应参数变更
      - `+ dead_letter_queue`
      - `+ targets.dead_letter_queue`
  - **ListSubscriptions**
    - 响应参数变更
      - `+ dead_letter_queue`
      - `+ items.targets.dead_letter_queue`
  - **ListTriggers**
    - 响应参数变更
      - `+ dead_letter_queue`
      - `+ items.targets.dead_letter_queue`
  - **ListWorkflowTriggers**
    - 响应参数变更
      - `+ dead_letter_queue`
      - `+ items.targets.dead_letter_queue`
  - **CreateEventStreaming**
    - 请求参数变更
      - `+ source.source_kafka.seek_to: enum value [latest,earliest]`
      - `+ source.source_kafka.sasl_mechanism: enum value [SCRAM-SHA-512,PLAIN]`
  - **ListEventStreaming**
    - 响应参数变更
      - `+ source.source_kafka.seek_to: enum value [latest,earliest]`
      - `+ source.source_kafka.sasl_mechanism: enum value [SCRAM-SHA-512,PLAIN]`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`ModifyGaussMySqlProxyRouteMode`
- _解决问题_
  - 无
- _特性变更_
  - **ShowGaussMySqlEngineVersion**
    - 响应参数变更
      - `+ datastores.version`
      - `+ datastores.kernel_version`
  - **CreateGaussMySqlProxy**
    - 请求参数变更
      - `+ route_mode`
  - **CreateGaussMySqlInstance**
    - 请求参数变更
      - `+ datastore.kernel_version`
    - 响应参数变更
      - `+ instance.datastore.kernel_version`
  - **ShowGaussMySqlBackupList**
    - 响应参数变更
      - `+ backups.datastore.kernel_version`
  - **ShowGaussMySqlProxyList**
    - 响应参数变更
      - `+ proxy_list.proxy.route_mode`
      - `+ proxy_list.proxy.balance_route_mode_enabled`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListInstances**
    - 响应参数变更
      - `+ instances.backup_used_space`
  - **ListComponentInfos**
    - 请求参数变更
      - `+ component_type`
      - `+ availability_zone_id`
    - 响应参数变更
      - `+ nodes.name`
      - `+ nodes.availability_zone_id`
      - `+ nodes.description`
      - `+ nodes.status`
      - `+ nodes.components.distributed_id`
  - **ListInstancesDetails**
    - 响应参数变更
      - `+ instances.backup_used_space`

### HuaweiCloud SDK KooMessage

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **DeleteTemplateMaterial**
    - 响应参数变更
      - `+ data`
  - **DeleteAimPersonalTemplate**
    - 响应参数变更
      - `+ data`
  - **UnfreezePub**
    - 响应参数变更
      - `+ data.pub_id`
      - `- data.data`
  - **FreezePub**
    - 响应参数变更
      - `+ data.pub_id`
      - `- data.data`
  - **ListAimResolveDetails**
    - 响应参数变更
      - `* resolve_details.resolved_status: object -> string`
  - **CreateResolveTask**
    - 请求参数变更
      - `- params.sms_params`
      - `* params: list<CreateResolveTaskParam> -> list<CreateShortChainParam>`
  - **ListAimTemplates**
    - 响应参数变更
      - `+ templates.factory_info.version`
  - **CreateVmsTemplate**
    - 请求参数变更
      - `- reminders`

### HuaweiCloud SDK MetaStudio

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListSelfPrivileges`
  - **CreateFile**
    - 响应参数变更
      - `+ file_id`
      - `+ upload_url`
  - **ListAssetSummary**
    - 响应参数变更
      - `+ asset_list.asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
  - **CreateTtsa**
    - 请求参数变更
      - `+ X-App-UserId`
      - `+ X-User-Privilege`
  - **ListTtsaJobs**
    - 请求参数变更
      - `+ X-App-UserId`
  - **ListTtsaData**
    - 响应参数变更
      - `+ motions.eyes`
      - `* motions.root: list<object> -> list<number>`
      - `* motions.joints: list<object> -> list<number>`
  - **CreatePictureModelingJob**
    - 响应参数变更
      - `+ model_asset_id`
      - `+ job_id`
  - **ListPictureModelingJobs**
    - 请求参数变更
      - `+ sort_dir: enum value [asc,desc]`
  - **DeleteAsset**
    - 请求参数变更
      - `+ mode`
  - **ShowAsset**
    - 响应参数变更
      - `+ asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ asset_extra_meta.voice_model_meta.tts_mode`
      - `+ asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.human_model_meta.model_properties`
  - **UpdateDigitalAsset**
    - 请求参数变更
      - `+ asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ asset_extra_meta.voice_model_meta.tts_mode`
      - `+ asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.human_model_meta.model_properties`
    - 响应参数变更
      - `+ asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ asset_extra_meta.voice_model_meta.tts_mode`
      - `+ asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.human_model_meta.model_properties`
  - **ListStyles**
    - 请求参数变更
      - `+ sort_dir: enum value [asc,desc]`
    - 响应参数变更
      - `+ styles.extra_meta.model_id`
  - **CreateVideoMotionCaptureJob**
    - 响应参数变更
      - `+ rtc_room_info`
      - `+ job_id`
  - **CreateDigitalAsset**
    - 请求参数变更
      - `+ asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ asset_extra_meta.voice_model_meta.tts_mode`
      - `+ asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.human_model_meta.model_properties`
  - **ListAssets**
    - 请求参数变更
      - `+ language`
      - `- lanuage`
      - `+ sort_dir: enum value [asc,desc]`
    - 响应参数变更
      - `+ assets.asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ assets.system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ assets.asset_extra_meta.voice_model_meta.tts_mode`
      - `+ assets.asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ assets.asset_extra_meta.human_model_meta.model_properties`

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`ListDataConnector`、`CreateDataConnector`、`UpdateDataConnector`、`DeleteDataConnector`
- _解决问题_
  - 无
- _特性变更_
  - **CreateCluster**
    - 请求参数变更
      - `+ charge_info.period_type`
      - `+ charge_info.period_num`
      - `+ charge_info.is_auto_pay`
  - **RunJobFlow**
    - 请求参数变更
      - `+ charge_info.period_type`
      - `+ charge_info.period_num`
      - `+ charge_info.is_auto_pay`

### HuaweiCloud SDK OSM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`CreateAuthorization`
  - **CreateMessages**
    - 请求参数变更
      - `- message.is_authorized`
      - `- message.authorization_content`
  - **CreateCases**
    - 请求参数变更
      - `- is_authorized`
      - `- authorization_content`
  - **ShowCaseDetail**
    - 响应参数变更
      - `- incident_detail_info.is_authorized`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowIssueV4**
    - 响应参数变更
      - `+ find_release_dev`
      - `+ release_dev`
      - `+ env`

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListDatastores**
    - 请求参数变更
      - `+ database_name: enum value [MariaDB]`
  - **ListConfigurations**
    - 响应参数变更
      - `+ configurations.datastore_name: enum value [mariadb]`
  - **CreateConfiguration**
    - 请求参数变更
      - `+ datastore.type: enum value [MariaDB]`
    - 响应参数变更
      - `+ configuration.datastore_name: enum value [mariadb]`
  - **ShowConfiguration**
    - 响应参数变更
      - `+ datastore_name: enum value [mariadb]`
  - **ShowInstanceConfiguration**
    - 响应参数变更
      - `+ datastore_name: enum value [mariadb]`
  - **ListFlavors**
    - 请求参数变更
      - `+ database_name: enum value [MariaDB]`
  - **ListStorageTypes**
    - 请求参数变更
      - `+ database_name: enum value [MariaDB]`
  - **ListInstances**
    - 请求参数变更
      - `+ datastore_type: enum value [MariaDB]`
    - 响应参数变更
      - `+ instances.datastore.type: enum value [MariaDB]`
  - **CreateInstance**
    - 请求参数变更
      - `+ datastore.type: enum value [MariaDB]`
    - 响应参数变更
      - `+ instance.datastore.type: enum value [MariaDB]`
  - **CreateRestoreInstance**
    - 请求参数变更
      - `+ datastore.type: enum value [MariaDB]`
    - 响应参数变更
      - `+ instance.datastore.type: enum value [MariaDB]`
  - **ListBackups**
    - 响应参数变更
      - `+ backups.datastore.type: enum value [MariaDB]`
  - **ListOffSiteBackups**
    - 响应参数变更
      - `+ backups.datastore.type: enum value [MariaDB]`
  - **ListOffSiteInstances**
    - 响应参数变更
      - `+ offsite_backup_instances.datastore.type: enum value [MariaDB]`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListMessageTrace**
    - 请求参数变更
      - `* msg_id: optional -> required`
  - **ListMessages**
    - 请求参数变更
      - `+ key`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListPorts**
    - 请求参数变更
      - `+ enable_efi`
    - 响应参数变更
      - `+ ports.enable_efi`
  - **CreatePort**
    - 响应参数变更
      - `+ port.enable_efi`
  - **ShowPort**
    - 响应参数变更
      - `+ port.enable_efi`
  - **UpdatePort**
    - 响应参数变更
      - `+ port.enable_efi`

# 3.1.51 2023-07-31

### HuaweiCloud SDK CAE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ExecuteAction**
    - 请求参数变更
      - `+ spec.build`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateIssueV4**
    - 响应参数变更
      - `+ find_release_dev`
      - `+ order`
      - `+ release_dev`
      - `+ env`
  - **ListIssuesV4**
    - 响应参数变更
      - `+ find_release_dev`
      - `+ order`
      - `+ release_dev`
      - `+ env`
      - `+ issues.order`
      - `+ issues.release_dev`
      - `+ issues.find_release_dev`
      - `+ issues.env`
  - **ListChildIssuesV4**
    - 响应参数变更
      - `+ find_release_dev`
      - `+ order`
      - `+ release_dev`
      - `+ env`
      - `+ issues.order`
      - `+ issues.release_dev`
      - `+ issues.find_release_dev`
      - `+ issues.env`

### HuaweiCloud SDK Workspace

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateDesktop**
    - 请求参数变更
      - `- security_groups.name`
      - `* security_groups: list<SecurityGroup> -> list<SecurityGroupInfo>`
  - **ShowDesktopDetail**
    - 响应参数变更
      - `- desktop.security_groups.name`
      - `* desktop.security_groups: list<SecurityGroup> -> list<SecurityGroupInfo>`
  - **ListDesktopsDetail**
    - 响应参数变更
      - `- desktops.security_groups.name`
      - `* desktops.security_groups: list<SecurityGroup> -> list<SecurityGroupInfo>`

# 3.1.50 2023-07-27

### HuaweiCloud SDK Cloudtest

- _新增特性_
  - 支持接口`ListTestCases`、`ListTestCaseHistories`、`ListBranches`、`ShowApiTestcaseHistories`
- _解决问题_
  - 无
- _特性变更_
  - **ShowPlans**
    - 响应参数变更
      - `* expire_day: string -> int32`
  - **ShowPlanList**
    - 响应参数变更
      - `* expire_day: string -> int32`

### HuaweiCloud SDK CodeHub

- _新增特性_
  - 支持接口`CreateMergeRequestDiscussion`、`CreateMergeRequestDiscussionNote`、`ShowReviewSetting`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DRS

- _新增特性_
  - 支持以下接口：
    - `DownloadBatchCreateTemplate`
    - `ImportBatchCreateJobs`
    - `CopyJob`
    - `ShowMetering`
    - `ShowDirtyData`
    - `ShowComparePolicy`
    - `ShowHealthCompareJobList`
    - `ShowProgressData`
    - `ShowObjectMapping`
    - `ShowActions`
    - `ValidateJobName`
    - `ShowEnterpriseProject`
- _解决问题_
  - 无
- _特性变更_
  - **DownloadDbObjectTemplate**
    - 请求参数变更
      - `+ file_import_db_level`
  - **UploadDbObjectTemplate**
    - 请求参数变更
      - `+ file_import_db_level`
  - **ListAsyncJobs**
    - 响应参数变更
      - `+ jobs.status: enum value [AUTO_PARAM_VALIDATE_SUCCESS,COMMIT_SUCCESS]`
      - `- jobs.status: enum value [ASYNC_JOB_CREATING,ASYNC_JOB_CREATE_FAILED,ASYNC_JOB_COMPLETED]`
  - **CreateJob**
    - 请求参数变更
      - `+ job.node_info.base_info`
    - 响应参数变更
      - `+ is_clone_job`
      - `+ create_time`
      - `+ name`
      - `+ id`
      - `+ status`
      - `+ job.is_clone_job`
  - **BatchCreateJobsAsync**
    - 请求参数变更
      - `+ jobs.node_info.base_info`
  - **ListAsyncJobDetail**
    - 响应参数变更
      - `+ jobs.support_import_file_resp`
      - `+ jobs.instance_features`
      - `+ jobs.task_version`
      - `+ jobs.node_info.base_info`
  - **UpdateBatchAsyncJobs**
    - 请求参数变更
      - `+ jobs.type: enum value [policy]`
      - `- jobs.type: enum value [policy_config]`
      - `+ jobs.params.node_info.base_info`
  - **ShowJobDetail**
    - 请求参数变更
      - `+ type: enum value [file]`
    - 响应参数变更
      - `+ job.support_import_file_resp`
      - `+ job.instance_features`
      - `+ job.task_version`
      - `+ job.node_info.base_info`
  - **UpdateJob**
    - 请求参数变更
      - `+ job.type: enum value [policy]`
      - `- job.type: enum value [policy_config]`
      - `+ job.params.node_info.base_info`

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **AttachShareBandwidth**
    - 响应参数变更
      - `+ publicip.vnic.vtep`
      - `+ publicip.vnic.vni`
      - `+ publicip.vnic.port_profile`
  - **DetachShareBandwidth**
    - 响应参数变更
      - `+ publicip.vnic.vtep`
      - `+ publicip.vnic.vni`
      - `+ publicip.vnic.port_profile`
  - **EnableNat64**
    - 响应参数变更
      - `+ publicip.vnic.vtep`
      - `+ publicip.vnic.vni`
      - `+ publicip.vnic.port_profile`
  - **DisableNat64**
    - 响应参数变更
      - `+ publicip.vnic.vtep`
      - `+ publicip.vnic.vni`
      - `+ publicip.vnic.port_profile`
  - **AttachBatchPublicIp**
    - 响应参数变更
      - `+ publicips.publicip.vnic.vtep`
      - `+ publicips.publicip.vnic.vni`
      - `+ publicips.publicip.vnic.port_profile`
  - **DetachBatchPublicIp**
    - 响应参数变更
      - `+ publicips.publicip.vnic.vtep`
      - `+ publicips.publicip.vnic.vni`
      - `+ publicips.publicip.vnic.port_profile`

### HuaweiCloud SDK ER

- _新增特性_
  - 支持以下接口：
    - `BatchCreateResourceTags`
    - `ShowQuotas`
    - `ListFlowLogs`
    - `CreateFlowLog`
    - `ShowFlowLog`
    - `UpdateFlowLog`
    - `DeleteFlowLog`
    - `EnableFlowLog`
    - `DisableFlowLog`
- _解决问题_
  - 无
- _特性变更_
  - **ListProjectTags**
    - 请求参数变更
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
    - 响应参数变更
      - `+ tags`
  - **DeleteResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
  - **ShowResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
    - 响应参数变更
      - `+ tags`
  - **CreateResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
  - **ListEnterpriseRouters**
    - 请求参数变更
      - `+ owned_by_self`
  - **ShowStaticRoute**
    - 响应参数变更
      - `+ route.attachments.priority`
  - **UpdateStaticRoute**
    - 响应参数变更
      - `+ route.attachments.priority`
  - **ListStaticRoutes**
    - 响应参数变更
      - `+ routes.attachments.priority`
  - **CreateStaticRoute**
    - 响应参数变更
      - `+ route.attachments.priority`
  - **ListEffectiveRoutes**
    - 响应参数变更
      - `+ routes.address_group_id`
      - `+ routes.next_hops.priority`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateTags**
    - 请求参数变更
      - `+ tags.key`
      - `+ tags.value`
      - `* tags: list<Kv> -> list<KvItem>`
  - **DeleteTags**
    - 请求参数变更
      - `+ tags.key`
      - `+ tags.value`
      - `* tags: list<Kv> -> list<KvItem>`
  - **ShowResInstanceInfo**
    - 请求参数变更
      - `+ matches.key`
      - `+ matches.value`
      - `* matches: list<Kv> -> list<KvItem>`
    - 响应参数变更
      - `+ resources.tags.key`
      - `+ resources.tags.value`
      - `* resources.tags: list<Kv> -> list<KvItem>`

### HuaweiCloud SDK GA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListRegions**
    - 响应参数变更
      - `+ regions`
      - `- area_regions`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持接口`ShowInstanceBiactiveRegions`
- _解决问题_
  - 无
- _特性变更_
  - **ListConfigurations**
    - 响应参数变更
      - `+ quota`
      - `+ configurations.mode`
  - **ListConfigurationTemplates**
    - 响应参数变更
      - `+ quota`
      - `+ configurations.mode`
  - **ShowInstanceConfiguration**
    - 响应参数变更
      - `+ mode`
      - `+ id`
  - **ListConfigurationDatastores**
    - 响应参数变更
      - `+ datastores.mode`
  - **ShowQuotas**
    - 请求参数变更
      - `+ datastore_type`
      - `+ mode`
  - **ListInstances**
    - 响应参数变更
      - `+ instances.datastore.whole_version`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 支持接口`DownloadBackup`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK HSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListPorts**
    - 请求参数变更
      - `* host_id: optional -> required`
  - **ListVulnerabilities**
    - 响应参数变更
      - `+ data_list.verify_num`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 支持以下接口：
    - `ListDeviceTunnels`
    - `AddTunnel`
    - `ShowDeviceTunnel`
    - `CloseDeviceTunnel`
    - `DeleteDeviceTunnel`
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
  - **CreateInstanceByEngine**
    - 请求参数变更
      - `+ disk_encrypted_enable`
      - `+ disk_encrypted_key`

### HuaweiCloud SDK LTS

- _新增特性_
  - 支持接口`UpdateLogStream`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateLogGroup**
    - 请求参数变更
      - `+ tags`
  - **CreateLogGroup**
    - 请求参数变更
      - `+ tags`
  - **CreateLogStream**
    - 请求参数变更
      - `+ enterprise_project_name`
      - `+ ttl_in_days`
      - `+ tags`
      - `+ log_stream_name: enum value [lts-stream-13ci]`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowInstanceExtendProductInfo**
    - 响应参数变更
      - `+ monthly`
      - `+ hourly`
      - `- engine`
      - `- versions`
      - `- products`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ValidateConsumedMessage**
    - 请求参数变更
      - `+ engine: enum value [reliability]`
  - **ListInstances**
    - 请求参数变更
      - `+ engine: enum value [reliability]`

### HuaweiCloud SDK SMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowConfigSetting**
    - 响应参数变更
      - `* configurations: string -> list<ConfigBody>`

# 3.1.49 2023-07-20

### HuaweiCloud SDK CloudRTC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateIndividualStreamJob**
    - 请求参数变更
      - `- publish_param`
  - **UpdateIndividualStreamJob**
    - 请求参数变更
      - `- publish_param`
  - **CreateMixJob**
    - 请求参数变更
      - `- publish_param`

### HuaweiCloud SDK EIP

- _新增特性_
  - 支持以下接口：
    - `AttachShareBandwidth`
    - `AttachBatchPublicIp`
    - `DetachShareBandwidth`
    - `DetachBatchPublicIp`
    - `EnableNat64`
    - `DisableNat64`
    - `ListBandwidth`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ER

- _新增特性_
  - 支持以下接口：
    - `BatchCreateResourceTags`
    - `ShowQuotas`
    - `ListFlowLogs`
    - `CreateFlowLog`
    - `ShowFlowLog`
    - `UpdateFlowLog`
    - `DeleteFlowLog`
    - `EnableFlowLog`
    - `DisableFlowLog`
- _解决问题_
  - 无
- _特性变更_
  - **ListProjectTags**
    - 请求参数变更
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
    - 响应参数变更
      - `+ tags`
  - **DeleteResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
  - **ShowResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
    - 响应参数变更
      - `+ tags`
  - **CreateResourceTag**
    - 请求参数变更
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
  - **ListEnterpriseRouters**
    - 请求参数变更
      - `+ owned_by_self`
  - **ShowStaticRoute**
    - 响应参数变更
      - `+ route.attachments.priority`
  - **UpdateStaticRoute**
    - 响应参数变更
      - `+ route.attachments.priority`
  - **ListStaticRoutes**
    - 响应参数变更
      - `+ routes.attachments.priority`
  - **CreateStaticRoute**
    - 响应参数变更
      - `+ route.attachments.priority`
  - **ListEffectiveRoutes**
    - 响应参数变更
      - `+ routes.address_group_id`
      - `+ routes.next_hops.priority`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 支持接口`DeleteBatchTask`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`ListTopicPartitions`、`ListTopicProducers`
- _解决问题_
  - 无
- _特性变更_
  - **ListProducts**
    - 请求参数变更
      - `+ engine: enum value [kafka]`
  - **UpdateInstanceTopic**
    - 请求参数变更
      - `+ topics.topic_other_configs`
      - `+ topics.topic_desc`
  - **CreateInstanceTopic**
    - 请求参数变更
      - `+ topic_other_configs`
      - `+ topic_desc`
    - 响应参数变更
      - `+ id`
  - **ListInstanceTopics**
    - 请求参数变更
      - `- offset`
      - `- limit`
    - 响应参数变更
      - `+ topics.topic_other_configs`
      - `+ topics.topic_desc`
      - `+ topics.created_at`
  - **ListInstances**
    - 请求参数变更
      - `+ engine: enum value [kafka]`
  - **ResizeEngineInstance**
    - 请求参数变更
      - `+ engine: enum value [kafka]`

### HuaweiCloud SDK MetaStudio

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreatePictureModelingJob**
    - 请求参数变更
      - `- model_asset_id`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowInstanceExtendProductInfo**
    - 请求参数变更
      - `+ engine: enum value [rabbitmq]`
    - 响应参数变更
      - `+ engine`
      - `+ versions`
      - `+ products`
      - `- monthly`
      - `- hourly`
  - **ListProducts**
    - 请求参数变更
      - `+ engine: enum value [rabbitmq]`
  - **ResizeEngineInstance**
    - 请求参数变更
      - `+ engine: enum value [rabbitmq]`
  - **ShowEngineInstanceExtendProductInfo**
    - 请求参数变更
      - `+ engine: enum value [rabbitmq]`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListInstancesSupportFastRestore`
- _解决问题_
  - 无
- _特性变更_
  - **RestoreTables**
    - 请求参数变更
      - `+ is_fast_restore`

# 3.1.48 2023-07-13

### HuaweiCloud SDK OROAS

- _新增特性_
  - 支持运筹优化算法服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK AS

- _新增特性_
  - 支持接口`ListGroupScheduledTasks`、`CreateGroupScheduledTask`、`UpdateGroupScheduledTask`、`DeleteGroupScheduledTask`
- _解决问题_
  - 无
- _特性变更_
  - **CreateScalingPolicy**
    - 请求参数变更
      - `+ scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **UpdateScalingPolicy**
    - 请求参数变更
      - `+ scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ShowScalingPolicy**
    - 响应参数变更
      - `+ scaling_policy.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policy.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ListScalingPolicies**
    - 响应参数变更
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **CreateScalingV2Policy**
    - 请求参数变更
      - `+ scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ListAllScalingV2Policies**
    - 响应参数变更
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **UpdateScalingV2Policy**
    - 请求参数变更
      - `+ scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ShowScalingV2Policy**
    - 响应参数变更
      - `+ scaling_policy.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policy.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ListScalingV2Policies**
    - 响应参数变更
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`

### HuaweiCloud SDK AntiDDoS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowNewTaskStatus**
    - 请求参数变更
      - `* task_id: optional -> required`

### HuaweiCloud SDK CAE

- _新增特性_
  - 支持以下接口：
    - `ListDomains`
    - `CreateDomain`
    - `DeleteDomain`
    - `ListCertificates`
    - `CreateCertificate`
    - `UpdateCertificate`
    - `DeleteCertificate`
    - `ListTimerRules`
    - `CreateTimerRule`
    - `UpdateTimerRule`
    - `DeleteTimerRule`
    - `ShowExecutionResult`
- _解决问题_
  - 无
- _特性变更_
  - **DeleteVolume**
    - 响应参数变更
      - `+ kind`
      - `+ api_version`
      - `+ items`
  - **ListAgencies**
    - 响应参数变更
      - `+ agencies`
      - `- items`
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Agency]`
  - **CreateAgency**
    - 请求参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Agency]`
      - `- metadata.name: enum value [cae_trust]`
  - **ListEnvironments**
    - 响应参数变更
      - `- items.type`
      - `- items.status: enum value [error]`
  - **CreateEnvironment**
    - 请求参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Environment]`
      - `- metadata.type`
    - 响应参数变更
      - `+ job_id`
      - `- metadata`
      - `- kind`
      - `- api_version`
  - **CreateApplication**
    - 请求参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Application]`
  - **ListApplications**
    - 响应参数变更
      - `+ items.annotations`
      - `+ items.created_at`
      - `+ items.updated_at`
  - **ListComponentSnapshots**
    - 响应参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [ComponentSnapshot]`
      - `+ items.context.app_id`
      - `+ items.context.available_replica`
      - `+ items.context.build`
      - `+ items.context.build_id`
      - `+ items.context.build_log_id`
      - `+ items.context.env_id`
      - `+ items.context.id`
      - `+ items.context.image_url`
      - `+ items.context.job_id`
      - `+ items.context.log_group_id`
      - `+ items.context.log_stream_id`
      - `+ items.context.name`
      - `+ items.context.operation`
      - `+ items.context.operation_status`
      - `+ items.context.replica`
      - `+ items.context.resource_limit`
      - `+ items.context.runtime`
      - `+ items.context.source`
      - `+ items.context.status`
      - `+ items.context.version`
      - `+ items.context.created_at`
      - `+ items.context.updated_at`
      - `* items.context: object -> object<ComponentSnapshotContext>`
  - **ListComponentConfigurations**
    - 响应参数变更
      - `- kind: enum value [Configuration]`
      - `+ items.type: enum value [rds,cse,env,access,scaling,volume,healthCheck,lifecycle]`
  - **CreateComponentConfiguration**
    - 请求参数变更
      - `- kind: enum value [Configuration]`
      - `+ items.type: enum value [rds,cse,env,access,scaling,volume,healthCheck,lifecycle]`
  - **ListComponentEvents**
    - 响应参数变更
      - `- kind: enum value [ComponentEvent]`
      - `+ items.involved_object_kind`
      - `- items.involved_object: enum value [Component,ComponentInstance,ComponentScaling]`
  - **ListComponentInstances**
    - 响应参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [ComponentInstance]`
  - **ListVolumes**
    - 请求参数变更
      - `+ resource_type: enum value [obs]`
    - 响应参数变更
      - `- kind: enum value [Volume]`
      - `- items.resource_type: enum value [obs]`
  - **CreateVolume**
    - 请求参数变更
      - `- kind: enum value [Volume]`
      - `- spec.resource_type: enum value [obs]`
  - **RetryJob**
    - 请求参数变更
      - `+ X-Enterprise-Project-ID`
      - `+ X-Environment-ID`
  - **ShowJob**
    - 请求参数变更
      - `+ X-Environment-ID`
    - 响应参数变更
      - `- kind: enum value [Job]`
      - `+ spec.progress`
  - **ShowComponent**
    - 响应参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Component]`
      - `- metadata.jod_id`
      - `- metadata.status`
      - `- metadata.type`
      - `+ spec.resource_limit`
      - `+ spec.build_log_id`
      - `- spec.log_strategy`
      - `+ spec.runtime: enum value [Docker,Java8,Java11,Tomcat8,Tomcat9,Python3,Nodejs8,Php7]`
  - **UpdateComponent**
    - 请求参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Component]`
      - `- metadata.created_at`
      - `- metadata.id`
      - `- metadata.jod_id`
      - `- metadata.status`
      - `- metadata.type`
      - `- metadata.updated_at`
      - `* metadata: object<Metadata> -> object<UpdateComponentRequestMetadata>`
      - `+ spec.runtime`
      - `+ spec.replica`
      - `- spec.log_strategy`
  - **ExecuteAction**
    - 请求参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Action]`
      - `* spec.source: object<Source> -> object<ActionOnComponentSource>`
  - **CreateComponent**
    - 请求参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Component]`
    - 响应参数变更
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Component]`
      - `- metadata.jod_id`
      - `- metadata.status`
      - `- metadata.type`
      - `+ spec.resource_limit`
      - `- spec.access_info`
      - `- spec.build_id`
      - `- spec.image_url`
      - `- spec.job_id`
      - `- spec.log_strategy`
      - `+ spec.runtime: enum value [Docker,Java8,Java11,Tomcat8,Tomcat9,Python3,Nodejs8,Php7]`
      - `* spec: object<ComponentSpec> -> object<CreateComponentSpec>`
  - **ListComponents**
    - 响应参数变更
      - `+ items.created_at`
      - `+ items.updated_at`
      - `- items.status`
      - `+ items.spec.resource_limit`
      - `+ items.spec.build_log_id`
      - `- items.spec.log_strategy`
      - `+ items.spec.runtime: enum value [Docker,Java8,Java11,Tomcat8,Tomcat9,Python3,Nodejs8,Php7]`

### HuaweiCloud SDK SIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **PushTranscriberJobs**
    - 请求参数变更
      - `+ Enterprise-Project-Id`

### HuaweiCloud SDK VPC

- _新增特性_
  - 支持以下接口：
    - `ListApiVersion`
    - `NeutronListPorts`
    - `NeutronCreatePort`
    - `NeutronShowPort`
    - `NeutronUpdatePort`
    - `NeutronDeletePort`
    - `NeutronListNetworks`
    - `NeutronCreateNetwork`
    - `NeutronShowNetwork`
    - `NeutronUpdateNetwork`
    - `NeutronDeleteNetwork`
    - `NeutronListSubnets`
    - `NeutronCreateSubnet`
    - `NeutronShowSubnet`
    - `NeutronUpdateSubnet`
    - `NeutronDeleteSubnet`
    - `NeutronListRouters`
    - `NeutronCreateRouter`
    - `NeutronShowRouter`
    - `NeutronUpdateRouter`
    - `NeutronDeleteRouter`
    - `NeutronAddRouterInterface`
    - `NeutronRemoveRouterInterface`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.47 2023-07-06

### HuaweiCloud SDK CodeCheck

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - `CodeCheck`更名为`CodeArtsCheck`

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpgradeCluster**
    - 响应参数变更
      - `+ metadata`
      - `+ spec`
      - `- uid`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDomainDetailByName**
    - 响应参数变更
      - `+ domain.sources.weight`
  - **ShowDomainFullConfig**
    - 响应参数变更
      - `+ configs.business_type`
      - `+ configs.service_area`
      - `+ configs.sources.weight`
  - **UpdateDomainFullConfig**
    - 请求参数变更
      - `+ configs.business_type`
      - `+ configs.service_area`
      - `+ configs.sources.weight`

### HuaweiCloud SDK EVS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateVolume**
    - 请求参数变更
      - `+ volume.iops`
      - `+ volume.throughput`
      - `+ volume.volume_type: enum value [GPSSD2,ESSD2]`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **DeleteGaussMySqlReadonlyNode**
    - 响应参数变更
      - `+ order_id`
  - **DeleteGaussMySqlInstance**
    - 响应参数变更
      - `+ order_id`
  - **ShowSqlFilterRule**
    - 请求参数变更
      - `+ sql_type`
      - `- type`

### HuaweiCloud SDK HSS

- _新增特性_
  - 支持接口`ListJarPackageStatistics`、`ListJarPackageHostInfo`、`ListHostVuls`
- _解决问题_
  - 无
- _特性变更_
  - **ListProtectionServer**
    - 响应参数变更
      - `+ data_list.version`
      - `+ data_list.vault_id`
      - `+ data_list.vault_name`
      - `+ data_list.vault_size`
      - `+ data_list.vault_used`
      - `+ data_list.vault_allocated`
      - `+ data_list.vault_charging_mode`
      - `+ data_list.vault_status`
      - `+ data_list.backup_policy_id`
      - `+ data_list.backup_policy_name`
      - `+ data_list.backup_policy_enabled`
      - `+ data_list.resources_num`
  - **UpdateProtectionPolicy**
    - 请求参数变更
      - `+ process_whitelist`
  - **ListProtectionPolicy**
    - 请求参数变更
      - `+ protect_policy_id`
    - 响应参数变更
      - `+ data_list.process_whitelist`
  - **ListRiskConfigs**
    - 请求参数变更
      - `+ group_id`
  - **ListHostStatus**
    - 响应参数变更
      - `+ data_list.open_time`
  - **ListVulnerabilities**
    - 请求参数变更
      - `+ repair_priority`
      - `+ handle_status`
      - `+ cve_id`
      - `+ label_list`
      - `+ status`
      - `+ asset_value`
      - `+ group_name`
    - 响应参数变更
      - `+ data_list.cve_list`
      - `+ data_list.patch_url`
      - `+ data_list.repair_priority`
      - `+ data_list.hosts_num`
      - `+ data_list.repair_success_num`
      - `+ data_list.fixed_num`
      - `+ data_list.ignored_num`
  - **ListVulHosts**
    - 请求参数变更
      - `+ asset_value`
      - `+ group_name`
      - `+ handle_status`
      - `+ severity_level`
      - `+ is_affect_business`
    - 响应参数变更
      - `+ data_list.agent_id`
      - `+ data_list.app_path`
      - `+ data_list.region_name`
      - `+ data_list.public_ip`
      - `+ data_list.private_ip`
      - `+ data_list.group_id`
      - `+ data_list.group_name`
      - `+ data_list.os_type`
      - `+ data_list.asset_value`
      - `+ data_list.is_affect_business`
      - `+ data_list.first_scan_time`
      - `+ data_list.scan_time`
  - **ChangeVulStatus**
    - 请求参数变更
      - `+ remark`
      - `+ select_type`
      - `+ type`
      - `+ host_data_list`
  - **ListHostProtectHistoryInfo**
    - 响应参数变更
      - `+ data_list.file_operation`
      - `+ data_list.host_name`
      - `+ data_list.host_ip`
  - **ListHostRaspProtectHistoryInfo**
    - 响应参数变更
      - `+ data_list.host_ip`
      - `+ data_list.host_name`
  - **ListHostGroups**
    - 响应参数变更
      - `+ data_list.is_outside`
  - **StartProtection**
    - 请求参数变更
      - `+ backup_resources`
      - `+ create_protection_policy.process_whitelist`
  - **ListSecurityEvents**
    - 请求参数变更
      - `+ event_class_ids`
  - **ChangeEvent**
    - 请求参数变更
      - `+ container_name`
      - `+ container_id`

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowPointTemplate**
    - 响应参数变更
      - `* : string -> binary`
  - **ShowPoints**
    - 响应参数变更
      - `* : string -> binary`
  - **DownloadAppVersion**
    - 响应参数变更
      - `* : string -> binary`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateSqlAlarmRule**
    - 请求参数变更
      - `+ notification_save_rule.template_name`
  - **CreateSqlAlarmRule**
    - 请求参数变更
      - `+ notification_save_rule.template_name`
  - **UpdateKeywordsAlarmRule**
    - 请求参数变更
      - `+ notification_save_rule.template_name`
  - **CreateKeywordsAlarmRule**
    - 请求参数变更
      - `+ notification_save_rule.template_name`
  - **ListAccessConfig**
    - 响应参数变更
      - `+ log_split`
      - `+ binary_collect`
      - `+ result.log_split`
      - `+ result.binary_collect`
      - `+ result.access_config_type: enum value [K8S_CCE]`
      - `+ result.access_config_detail.stdout`
      - `+ result.access_config_detail.stderr`
      - `+ result.access_config_detail.pathType`
      - `+ result.access_config_detail.namespaceRegex`
      - `+ result.access_config_detail.podNameRegex`
      - `+ result.access_config_detail.containerNameRegex`
      - `+ result.access_config_detail.includeLabels`
      - `+ result.access_config_detail.excludeLabels`
      - `+ result.access_config_detail.includeEnvs`
      - `+ result.access_config_detail.excludeEnvs`
      - `+ result.access_config_detail.logLabels`
      - `+ result.access_config_detail.logEnvs`
      - `+ result.access_config_detail.includeK8sLabels`
      - `+ result.access_config_detail.excludeK8sLabels`
      - `+ result.access_config_detail.logK8s`
      - `* result.access_config_detail.format.single: object<AccessConfigFormatSingle> -> object<AccessConfigFormatSingleCreate>`
      - `* result.access_config_detail.format.multi: object<AccessConfigFormatMutil> -> object<AccessConfigFormatMutilCreate>`
      - `* result.access_config_detail.format: object<AccessConfigFormat> -> object<AccessConfigFormatCreate>`
      - `* result.access_config_detail.windows_log_info: object<AccessConfigWindowsLogInfo> -> object<AccessConfigWindowsLogInfoCreate>`
      - `* result.access_config_detail: object<AccessConfigDeatil> -> object<AccessConfigDeatilCreate>`
  - **UpdateAccessConfig**
    - 请求参数变更
      - `+ log_split`
      - `+ binary_collect`
      - `+ access_config_detail.stdout`
      - `+ access_config_detail.stderr`
      - `+ access_config_detail.pathType`
      - `+ access_config_detail.namespaceRegex`
      - `+ access_config_detail.podNameRegex`
      - `+ access_config_detail.containerNameRegex`
      - `+ access_config_detail.includeLabels`
      - `+ access_config_detail.excludeLabels`
      - `+ access_config_detail.includeEnvs`
      - `+ access_config_detail.excludeEnvs`
      - `+ access_config_detail.logLabels`
      - `+ access_config_detail.logEnvs`
      - `+ access_config_detail.includeK8sLabels`
      - `+ access_config_detail.excludeK8sLabels`
      - `+ access_config_detail.logK8s`
      - `* access_config_detail.format.single: object<AccessConfigFormatSingle> -> object<AccessConfigFormatSingleCreate>`
      - `* access_config_detail.format.multi: object<AccessConfigFormatMutil> -> object<AccessConfigFormatMutilCreate>`
      - `* access_config_detail.format: object<AccessConfigFormat> -> object<AccessConfigFormatCreate>`
      - `* access_config_detail.windows_log_info: object<AccessConfigWindowsLogInfo> -> object<AccessConfigWindowsLogInfoCreate>`
      - `* access_config_detail: object<AccessConfigDeatil> -> object<AccessConfigDeatilCreate>`
    - 响应参数变更
      - `+ log_split`
      - `+ binary_collect`
      - `+ access_config_type: enum value [K8S_CCE]`
      - `+ access_config_detail.stdout`
      - `+ access_config_detail.stderr`
      - `+ access_config_detail.pathType`
      - `+ access_config_detail.namespaceRegex`
      - `+ access_config_detail.podNameRegex`
      - `+ access_config_detail.containerNameRegex`
      - `+ access_config_detail.includeLabels`
      - `+ access_config_detail.excludeLabels`
      - `+ access_config_detail.includeEnvs`
      - `+ access_config_detail.excludeEnvs`
      - `+ access_config_detail.logLabels`
      - `+ access_config_detail.logEnvs`
      - `+ access_config_detail.includeK8sLabels`
      - `+ access_config_detail.excludeK8sLabels`
      - `+ access_config_detail.logK8s`
      - `* access_config_detail.format.single: object<AccessConfigFormatSingle> -> object<AccessConfigFormatSingleCreate>`
      - `* access_config_detail.format.multi: object<AccessConfigFormatMutil> -> object<AccessConfigFormatMutilCreate>`
      - `* access_config_detail.format: object<AccessConfigFormat> -> object<AccessConfigFormatCreate>`
      - `* access_config_detail.windows_log_info: object<AccessConfigWindowsLogInfo> -> object<AccessConfigWindowsLogInfoCreate>`
      - `* access_config_detail: object<AccessConfigDeatil> -> object<AccessConfigDeatilCreate>`
  - **CreateAccessConfig**
    - 请求参数变更
      - `+ binary_collect`
      - `+ log_split`
      - `+ access_config_type: enum value [K8S_CCE]`
      - `+ access_config_detail.stdout`
      - `+ access_config_detail.stderr`
      - `+ access_config_detail.pathType`
      - `+ access_config_detail.namespaceRegex`
      - `+ access_config_detail.podNameRegex`
      - `+ access_config_detail.containerNameRegex`
      - `+ access_config_detail.includeLabels`
      - `+ access_config_detail.excludeLabels`
      - `+ access_config_detail.includeEnvs`
      - `+ access_config_detail.excludeEnvs`
      - `+ access_config_detail.logLabels`
      - `+ access_config_detail.logEnvs`
      - `+ access_config_detail.includeK8sLabels`
      - `+ access_config_detail.excludeK8sLabels`
      - `+ access_config_detail.logK8s`
    - 响应参数变更
      - `+ log_split`
      - `+ binary_collect`
      - `+ access_config_type: enum value [K8S_CCE]`
      - `+ access_config_detail.stdout`
      - `+ access_config_detail.stderr`
      - `+ access_config_detail.pathType`
      - `+ access_config_detail.namespaceRegex`
      - `+ access_config_detail.podNameRegex`
      - `+ access_config_detail.containerNameRegex`
      - `+ access_config_detail.includeLabels`
      - `+ access_config_detail.excludeLabels`
      - `+ access_config_detail.includeEnvs`
      - `+ access_config_detail.excludeEnvs`
      - `+ access_config_detail.logLabels`
      - `+ access_config_detail.logEnvs`
      - `+ access_config_detail.includeK8sLabels`
      - `+ access_config_detail.excludeK8sLabels`
      - `+ access_config_detail.logK8s`
      - `* access_config_detail.format.single: object<AccessConfigFormatSingle> -> object<AccessConfigFormatSingleCreate>`
      - `* access_config_detail.format.multi: object<AccessConfigFormatMutil> -> object<AccessConfigFormatMutilCreate>`
      - `* access_config_detail.format: object<AccessConfigFormat> -> object<AccessConfigFormatCreate>`
      - `* access_config_detail.windows_log_info: object<AccessConfigWindowsLogInfo> -> object<AccessConfigWindowsLogInfoCreate>`
      - `* access_config_detail: object<AccessConfigDeatil> -> object<AccessConfigDeatilCreate>`
  - **DeleteAccessConfig**
    - 响应参数变更
      - `+ log_split`
      - `+ binary_collect`
      - `+ result.log_split`
      - `+ result.binary_collect`
      - `+ result.access_config_type: enum value [K8S_CCE]`
      - `+ result.access_config_detail.stdout`
      - `+ result.access_config_detail.stderr`
      - `+ result.access_config_detail.pathType`
      - `+ result.access_config_detail.namespaceRegex`
      - `+ result.access_config_detail.podNameRegex`
      - `+ result.access_config_detail.containerNameRegex`
      - `+ result.access_config_detail.includeLabels`
      - `+ result.access_config_detail.excludeLabels`
      - `+ result.access_config_detail.includeEnvs`
      - `+ result.access_config_detail.excludeEnvs`
      - `+ result.access_config_detail.logLabels`
      - `+ result.access_config_detail.logEnvs`
      - `+ result.access_config_detail.includeK8sLabels`
      - `+ result.access_config_detail.excludeK8sLabels`
      - `+ result.access_config_detail.logK8s`
      - `* result.access_config_detail.format.single: object<AccessConfigFormatSingle> -> object<AccessConfigFormatSingleCreate>`
      - `* result.access_config_detail.format.multi: object<AccessConfigFormatMutil> -> object<AccessConfigFormatMutilCreate>`
      - `* result.access_config_detail.format: object<AccessConfigFormat> -> object<AccessConfigFormatCreate>`
      - `* result.access_config_detail.windows_log_info: object<AccessConfigWindowsLogInfo> -> object<AccessConfigWindowsLogInfoCreate>`
      - `* result.access_config_detail: object<AccessConfigDeatil> -> object<AccessConfigDeatilCreate>`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RunCreateVideoModerationJob**
    - 请求参数变更
      - `+ data.language`

### HuaweiCloud SDK RAM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **AssociateResourceShare**
    - 响应参数变更
      - `+ resource_share_associations.status_message`
  - **DisassociateResourceShare**
    - 响应参数变更
      - `+ resource_share_associations.status_message`
  - **SearchResourceShareAssociations**
    - 响应参数变更
      - `+ resource_share_associations.status_message`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSecurityGroupRules**
    - 请求参数变更
      - `+ remote_ip_prefix`

# 3.1.46 2023-06-29

### HuaweiCloud SDK IdentityCenter

- _新增特性_
  - 支持IAM 身份中心服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK WorkspaceApp

- _新增特性_
  - 支持云应用服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Config

- _新增特性_
  - 支持配置审计服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持接口`ListTemplateVersions`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **DeleteTag**
    - 请求参数变更
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **ListCloudConnections**
    - 请求参数变更
      - `+ used_scene`
    - 响应参数变更
      - `+ cloud_connections.tags`
  - **CreateCloudConnection**
    - 响应参数变更
      - `+ cloud_connection.tags`
  - **ShowCloudConnection**
    - 响应参数变更
      - `+ cloud_connection.tags`
  - **UpdateCloudConnection**
    - 响应参数变更
      - `+ cloud_connection.tags`
  - **ListDomainTags**
    - 请求参数变更
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **BatchCreateDeleteTags**
    - 请求参数变更
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **ListTags**
    - 请求参数变更
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **CreateTag**
    - 请求参数变更
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **ListQuotas**
    - 请求参数变更
      - `* quota_type: optional -> required`
  - **CreateBandwidthPackage**
    - 请求参数变更
      - `+ bandwidth_package.spec_code`
  - **ListResourceByFilterTag**
    - 请求参数变更
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`ExecuteClusterSwitchover`、`ShowJobInfo`
- _解决问题_
  - 无
- _特性变更_
  - **ListConfigTemplates**
    - 响应参数变更
      - `+ config_templates.created_at`
  - **CreateInstance**
    - 请求参数变更
      - `+ template_id`

### HuaweiCloud SDK DSC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateProductOrder**
    - 请求参数变更
      - `+ charging_mode`
      - `+ cloud_service_type`
      - `+ composite_product_id`
      - `+ discount_id`
      - `+ is_auto_renew`
      - `+ period_num`
      - `+ period_type`
      - `+ product_infos`
      - `+ promotion_activity_id`
      - `+ promotion_info`
      - `+ region_id`
      - `- chargingMode`
      - `- cloudServiceType`
      - `- compositeProductId`
      - `- discountId`
      - `- isAutoRenew`
      - `- periodNum`
      - `- periodType`
      - `- productInfos`
      - `- promotionActivityId`
      - `- promotionInfo`
      - `- regionId`
  - **ShowSpecification**
    - 响应参数变更
      - `* orderInfos.productInfo: list<ProductInfoBean> -> object<ProductInfo>`
  - **ChangeRule**
    - 请求参数变更
      - `* body: object<RuleRequest> -> object<RuleChangeRequest>`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `ListDrugJob`
    - `CancelDrugJob`
    - `DeleteDrugJob`
    - `CreateOptmJob`
    - `ShowOptmJob`
    - `CreateSynthesisJob`
    - `ShowSynthesisJob`
    - `CreateDockingJob`
    - `ShowDockingJob`
    - `CreateFepJob`
    - `ShowFepJob`

### HuaweiCloud SDK GA

- _新增特性_
  - 支持以下接口：
    - `ListIpGroups`
    - `CreateIpGroup`
    - `ShowIpGroup`
    - `UpdateIpGroup`
    - `DeleteIpGroup`
    - `AddIpGroupIp`
    - `RemoveIpGroupIp`
    - `AssociateListener`
    - `DisassociateListener`
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
  - **CreateCommand**
    - 响应参数变更
      - `+ error_msg`
      - `+ error_code`
  - **ListProperties**
    - 响应参数变更
      - `+ error_msg`
      - `+ error_code`
  - **UpdateProperties**
    - 响应参数变更
      - `+ error_msg`
      - `+ error_code`

### HuaweiCloud SDK ServiceStage

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ShowComponentConfigurations`、`CreateComponentConfiguration`、`ShowComponentConfiguration`、`CompareComponentConfiguration`
  - **ModifyApplicationConfiguration**
    - 响应参数变更
      - `+ environment_id`
      - `+ application_id`
      - `* configuration: list<object> -> object`
  - **ShowComponentInfo**
    - 响应参数变更
      - `- host_aliases`
      - `- dns_policy`
      - `- enable_sermant_injection`
      - `- workload_name`
      - `- workload_kind`
      - `- dns_config`
      - `- pod_labels`
      - `- security_context`
      - `- deploy_strategy.rolling_release.termination_seconds`
      - `- deploy_strategy.rolling_release.fail_strategy`
      - `- deploy_strategy.gray_release.deployment_mode`
      - `- deploy_strategy.gray_release.replica_surge_mode`
      - `- deploy_strategy.gray_release.rule_match_mode`
      - `- deploy_strategy.gray_release.rules`
      - `- liveness_probe.period_seconds`
      - `- liveness_probe.success_threshold`
      - `- liveness_probe.failure_threshold`
      - `- liveness_probe.http_headers`
  - **ModifyComponent**
    - 请求参数变更
      - `- pod_labels`
      - `- enable_sermant_injection`
      - `- host_aliases`
      - `- dns_policy`
      - `- dns_config`
      - `- security_context`
      - `- workload_kind`
      - `- deploy_strategy.rolling_release.termination_seconds`
      - `- deploy_strategy.rolling_release.fail_strategy`
      - `- deploy_strategy.gray_release.deployment_mode`
      - `- deploy_strategy.gray_release.replica_surge_mode`
      - `- deploy_strategy.gray_release.rule_match_mode`
      - `- deploy_strategy.gray_release.rules`
      - `- liveness_probe.period_seconds`
      - `- liveness_probe.success_threshold`
      - `- liveness_probe.failure_threshold`
      - `- liveness_probe.http_headers`
  - **CreateComponent**
    - 请求参数变更
      - `- workload_name`
      - `- pod_labels`
      - `- enterprise_project_id`
      - `- enable_sermant_injection`
      - `- host_aliases`
      - `- dns_policy`
      - `- dns_config`
      - `- security_context`
      - `- workload_kind`
      - `- deploy_strategy.rolling_release.termination_seconds`
      - `- deploy_strategy.rolling_release.fail_strategy`
      - `- deploy_strategy.gray_release.deployment_mode`
      - `- deploy_strategy.gray_release.replica_surge_mode`
      - `- deploy_strategy.gray_release.rule_match_mode`
      - `- deploy_strategy.gray_release.rules`
      - `- liveness_probe.period_seconds`
      - `- liveness_probe.success_threshold`
      - `- liveness_probe.failure_threshold`
      - `- liveness_probe.http_headers`
  - **ShowComponentsInApplication**
    - 响应参数变更
      - `+ components.platform_type`
  - **ShowComponents**
    - 响应参数变更
      - `+ components.platform_type`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAddressGroup**
    - 响应参数变更
      - `+ address_group.tags`
  - **UpdateAddressGroup**
    - 响应参数变更
      - `+ address_group.tags`
  - **ListAddressGroup**
    - 响应参数变更
      - `+ address_groups.tags`
  - **CreateAddressGroup**
    - 响应参数变更
      - `+ address_group.tags`

### HuaweiCloud SDK VPCEP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **AddOrRemoveServicePermissions**
    - 请求参数变更
      - `+ permission_type`
    - 响应参数变更
      - `+ permission_type`
  - **UpdateEndpointService**
    - 响应参数变更
      - `- cidr_type`
  - **ListServicePermissionsDetails**
    - 响应参数变更
      - `+ permissions.permission_type`
  - **BatchAddEndpointServicePermissions**
    - 请求参数变更
      - `+ permission_type`
    - 响应参数变更
      - `+ permissions.permission_type`
  - **BatchRemoveEndpointServicePermissions**
    - 响应参数变更
      - `+ permissions.permission_type`
  - **UpdateEndpointServicePermissionDesc**
    - 响应参数变更
      - `+ permissions.permission_type`
  - **CreateEndpointService**
    - 响应参数变更
      - `- cidr_type`

### HuaweiCloud SDK VSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CancelTasks**
    - 响应参数变更
      - `+ task_status: enum value [ready]`
  - **CreateTasks**
    - 响应参数变更
      - `+ task_status: enum value [ready]`
  - **ShowTasks**
    - 响应参数变更
      - `+ task_status: enum value [ready]`
  - **ListTaskHistories**
    - 响应参数变更
      - `+ data.task_status: enum value [ready]`

### HuaweiCloud SDK Workspace

- _新增特性_
  - 支持以下接口：
    - `BatchLogoffDesktops`
    - `ListDesktopsEips`
    - `ApplyDesktopsInternet`
    - `AssociateDesktopsEip`
    - `BatchDisassociateDesktopsEip`
    - `ListUnusedDesktops`
    - `ListUsedDesktopInfo`
    - `ListUserGroups`
    - `CreateUserGroup`
    - `BatchDeleteUserGroups`
    - `UpdateUserGroup`
    - `DeleteUserGroup`
    - `RunActionsOnGroup`
    - `ListUsersOfGroup`
    - `BatchCreateUsers`
    - `ResetRandomPassword`
- _解决问题_
  - 无
- _特性变更_
  - **ListDesktops**
    - 请求参数变更
      - `+ pool_id`
  - **CreateDesktop**
    - 请求参数变更
      - `+ eip`
      - `+ security_groups.name`
      - `* security_groups: list<SecurityGroupInfo> -> list<SecurityGroup>`
  - **ResizeDesktop**
    - 响应参数变更
      - `+ job_id`
      - `* jobs: list<ResizeDesktopJobResult> -> list<ResizeDesktopJobResponse>`
  - **CreateAccessPolicy**
    - 请求参数变更
      - `+ policy_objects_list.object_type: enum value [USERGROUP]`
  - **ListAccessPolicyObjects**
    - 响应参数变更
      - `+ policy_objects_list.object_type: enum value [USERGROUP]`
      - `* policy_objects_list: list<AccessPolicyObjectInfo> -> list<AccessPolicyObject>`
  - **UpdateAccessPolicyObjects**
    - 请求参数变更
      - `+ policy_objects_list.object_type: enum value [USERGROUP]`
  - **ListProducts**
    - 响应参数变更
      - `- products.package_type`
  - **CreateDesktopUser**
    - 请求参数变更
      - `+ active_type`
      - `+ user_phone`
      - `+ password`
      - `* body: object<CreateUserReq> -> object<CreateUserRequest>`
  - **ListUsers**
    - 请求参数变更
      - `+ active_type`
    - 响应参数变更
      - `+ users.user_phone`
      - `+ users.active_type`
      - `+ users.is_pre_user`
  - **UpdateUserInfo**
    - 请求参数变更
      - `+ user_phone`
      - `+ active_type`
  - **ListUserDetail**
    - 响应参数变更
      - `+ user_detail.user_phone`
      - `+ user_detail.active_type`
      - `+ user_detail.is_pre_user`
  - **ShowAssistAuthConfig**
    - 响应参数变更
      - `+ otp_config_info.apply_rule`
  - **UpdateAssistAuthMethodConfig**
    - 请求参数变更
      - `+ otp_config_info.apply_rule`
  - **ShowDesktopDetail**
    - 响应参数变更
      - `+ desktop.internet_mode`
      - `+ desktop.is_attaching_eip`
      - `+ desktop.security_groups.name`
      - `* desktop.security_groups: list<SecurityGroupInfo> -> list<SecurityGroup>`
  - **ListDesktopsDetail**
    - 请求参数变更
      - `+ pool_id`
    - 响应参数变更
      - `+ desktops.internet_mode`
      - `+ desktops.is_attaching_eip`
      - `+ desktops.security_groups.name`
      - `* desktops.security_groups: list<SecurityGroupInfo> -> list<SecurityGroup>`

# 3.1.45 2023-06-21

### HuaweiCloud SDK DataArtsStudio

- _新增特性_
  - 支持数据治理中心服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK KooMessage

- _新增特性_
  - 支持云消息服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **DeleteGatewayResponseTypeV2**
    - 请求参数变更
      - `+ response_type: enum value [THIRD_AUTH_FAILURE,THIRD_AUTH_IDENTITIES_FAILURE,THIRD_AUTH_CONF_FAILURE]`
  - **ShowDetailsOfGatewayResponseTypeV2**
    - 请求参数变更
      - `+ response_type: enum value [THIRD_AUTH_FAILURE,THIRD_AUTH_IDENTITIES_FAILURE,THIRD_AUTH_CONF_FAILURE]`
  - **UpdateGatewayResponseTypeV2**
    - 请求参数变更
      - `+ response_type: enum value [THIRD_AUTH_FAILURE,THIRD_AUTH_IDENTITIES_FAILURE,THIRD_AUTH_CONF_FAILURE]`
  - **ShowPlugin**
    - 响应参数变更
      - `+ plugin_type: enum value [third_auth]`
  - **UpdatePlugin**
    - 请求参数变更
      - `+ plugin_type: enum value [third_auth]`
    - 响应参数变更
      - `+ plugin_type: enum value [third_auth]`
  - **CreatePlugin**
    - 请求参数变更
      - `+ plugin_type: enum value [third_auth]`
    - 响应参数变更
      - `+ plugin_type: enum value [third_auth]`
  - **ListPlugins**
    - 响应参数变更
      - `+ plugins.plugin_type: enum value [third_auth]`
  - **AttachApiToPlugin**
    - 响应参数变更
      - `+ attached_plugins.plugin_type: enum value [third_auth]`
  - **AttachPluginToApi**
    - 响应参数变更
      - `+ attached_plugins.plugin_type: enum value [third_auth]`
  - **ListApiAttachedPlugins**
    - 响应参数变更
      - `+ plugins.plugin_type: enum value [third_auth]`
  - **ListApiAttachablePlugins**
    - 响应参数变更
      - `+ plugins.plugin_type: enum value [third_auth]`
  - **ShowDetailsOfVpcChannelV2**
    - 响应参数变更
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
  - **UpdateVpcChannelV2**
    - 请求参数变更
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
    - 响应参数变更
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
  - **ImportMicroservice**
    - 请求参数变更
      - `+ cce_service_info`
      - `+ service_type: enum value [CCE_SERVICE]`
      - `+ cce_info.label_key`
      - `+ cce_info.label_value`
  - **CreateVpcChannelV2**
    - 请求参数变更
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
    - 响应参数变更
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
  - **ListVpcChannelsV2**
    - 响应参数变更
      - `+ vpc_channels.microservice_info.cce_service_info`
      - `+ vpc_channels.microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ vpc_channels.microservice_info.cce_info.label_key`
      - `+ vpc_channels.microservice_info.cce_info.label_value`

### HuaweiCloud SDK Classroom

- _新增特性_
  - 支持以下接口：
    - `ListPackages`
    - `ShowPackageDetail`
    - `ListExercises`
    - `ShowExerciseDetail`
    - `ExecuteExercise`
    - `ListAllDifficults`
    - `ListMyKnowledgePoints`
- _解决问题_
  - 无
- _特性变更_
  - **ApplyJudgement**
    - 请求参数变更
      - `+ runtime_type: enum value [javaScript]`

### HuaweiCloud SDK CloudRTC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateAutoRecord**
    - 响应参数变更
      - `- auto_record_mode`
      - `- app_id`
  - **CreateMixJob**
    - 响应参数变更
      - `+ mix_param.encode_template: enum value [1920*1080_30_4620,1920*1080_30_3150,1920*1080_15_3460,1920*1080_15_2080,1280*720_30_3420,1280*720_30_1710,1280*720_15_2260,1280*720_15_1130,640*480_30_1000,640*480_30_1500,640*480_15_500,480*360_30_490,480*360_15_320]`
      - `- mix_param.encode_template: enum value [1920x1080_30_4620,1920x1080_15_3460,1280x720_30_3420,1280x720_15_2260]`
  - **ShowMixJob**
    - 响应参数变更
      - `+ mix_param.encode_template: enum value [1920*1080_30_4620,1920*1080_30_3150,1920*1080_15_3460,1920*1080_15_2080,1280*720_30_3420,1280*720_30_1710,1280*720_15_2260,1280*720_15_1130,640*480_30_1000,640*480_30_1500,640*480_15_500,480*360_30_490,480*360_15_320]`
      - `- mix_param.encode_template: enum value [1920x1080_30_4620,1920x1080_15_3460,1280x720_30_3420,1280x720_15_2260]`
  - **UpdateMixJob**
    - 响应参数变更
      - `+ mix_param.encode_template: enum value [1920*1080_30_4620,1920*1080_30_3150,1920*1080_15_3460,1920*1080_15_2080,1280*720_30_3420,1280*720_30_1710,1280*720_15_2260,1280*720_15_1130,640*480_30_1000,640*480_30_1500,640*480_15_500,480*360_30_490,480*360_15_320]`
      - `- mix_param.encode_template: enum value [1920x1080_30_4620,1920x1080_15_3460,1280x720_30_3420,1280x720_15_2260]`

### HuaweiCloud SDK CloudTable

- _新增特性_
  - 支持以下接口：
    - `EnableComponent`
    - `ExpandClusterComponent`
    - `RebootCloudTableCluster`
    - `ShowClusterSetting`
    - `UpdateClusterSetting`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DNS

- _新增特性_
  - 支持接口`ShowDomainQuota`
- _解决问题_
  - 无
- _特性变更_
  - **ShowRecordSetWithLine**
    - 响应参数变更
      - `+ bundle`
  - **SetRecordSetsStatus**
    - 响应参数变更
      - `+ bundle`
  - **BatchUpdateRecordSetWithLine**
    - 响应参数变更
      - `+ bundle`
      - `+ recordsets.bundle`
  - **BatchDeleteRecordSetWithLine**
    - 响应参数变更
      - `+ bundle`
      - `+ recordsets.bundle`
  - **CreateRecordSetWithBatchLines**
    - 响应参数变更
      - `+ bundle`
      - `+ recordsets.bundle`

### HuaweiCloud SDK DWS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListAvailableDisasterClusters**
    - 请求参数变更
      - `* primary_cluster_id: optional -> required`
      - `* standby_az_code: optional -> required`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持以下接口：
    - `ListDrugJob`
    - `CancelDrugJob`
    - `DeleteDrugJob`
    - `CreateOptmJob`
    - `ShowOptmJob`
    - `CreateSynthesisJob`
    - `ShowSynthesisJob`
    - `CreateDockingJob`
    - `ShowDockingJob`
    - `CreateFepJob`
    - `ShowFepJob`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateDbInstance**
    - 响应参数变更
      - `+ instance.ha.consistency_protocol`

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateEdgeNode**
    - 请求参数变更
      - `+ npu_library_path`
      - `+ device_data_format`
      - `+ automatic_upgrade`
      - `+ device_data_record`
      - `+ metric_report`
      - `+ base_path.offline_cache_configs`
    - 响应参数变更
      - `+ device_data_record`
      - `+ device_data_format`
      - `+ metric_report`
      - `+ automatic_upgrade`
      - `+ base_path.offline_cache_configs`
  - **ShowEdgeNode**
    - 响应参数变更
      - `+ device_data_record`
      - `+ device_data_format`
      - `+ metric_report`
      - `+ npu_library_path`
      - `+ automatic_upgrade`
      - `+ base_path.offline_cache_configs`
  - **CreateEdgeApplicationVersion**
    - 请求参数变更
      - `+ container_settings.npu_type`
      - `+ container_settings.vnpu_template`
    - 响应参数变更
      - `+ container_settings.npu_type`
      - `+ container_settings.vnpu_template`
  - **ShowEdgeApplicationVersion**
    - 响应参数变更
      - `+ container_settings.npu_type`
      - `+ container_settings.vnpu_template`
  - **UpdateEdgeApplicationVersion**
    - 请求参数变更
      - `+ container_settings.npu_type`
      - `+ container_settings.vnpu_template`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListPredefinedTag`、`ListSimplifiedInstances`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.44 2023-06-15

### HuaweiCloud SDK CloudDeploy

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - `CloudDeploy`更名为`CodeArtsDeploy`

### HuaweiCloud SDK CCM

- _新增特性_
  - 支持以下接口：
    - `BatchCreateCaTags`
    - `BatchDeleteCaTags`
    - `ListCaTags`
    - `CreateCaTag`
    - `ListDomainCaTags`
    - `ListCaResourceInstances`
    - `CountCaResourceInstances`
    - `BatchCreateCertTags`
    - `BatchDeleteCertTags`
    - `ListCertTags`
    - `CreateCertTag`
    - `ListDomainCertTags`
    - `ListCertResourceInstances`
    - `CountCertResourceInstances`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持以下接口：
    - `ShowDatabaseAuthority`
    - `UpdateDatabaseAuthority`
    - `SyncIamUsers`
    - `ListDatabaseUsers`
    - `ShowDatabaseUser`
    - `UpdateDatabaseUserInfo`
    - `ShowDisasterProgress`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateAlarmSub**
    - 请求参数变更
      - `* enable: string -> int32`
    - 响应参数变更
      - `* enable: string -> int32`
  - **DeleteAlarmSub**
    - 响应参数变更
      - `* enable: string -> int32`
  - **ShowDisasterDetail**
    - 响应参数变更
      - `+ disaster_recovery`
      - `- start_time`
      - `- dr_type`
      - `- create_time`
      - `- name`
      - `- standby_cluster`
      - `- id`
      - `- dr_sync_period`
      - `- status`
      - `- primary_cluster`
  - **CreateAlarmSub**
    - 请求参数变更
      - `* enable: string -> int32`
    - 响应参数变更
      - `* enable: string -> int32`
  - **ListAlarmSubs**
    - 响应参数变更
      - `* alarm_subscriptions.enable: string -> int32`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListGaussMySqlErrorLog`、`ListGaussMySqlSlowLog`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateBatchTask**
    - 响应参数变更
      - `- task_progress.device_in_progress`
      - `- task_progress.rejected`
  - **ListBatchTasks**
    - 响应参数变更
      - `- batchtasks.task_progress.device_in_progress`
      - `- batchtasks.task_progress.rejected`
  - **ShowBatchTask**
    - 响应参数变更
      - `- batchtask.task_progress.device_in_progress`
      - `- batchtask.task_progress.rejected`

### HuaweiCloud SDK MRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListClusters**
    - 响应参数变更
      - `+ clusters.eipId`
      - `+ clusters.eipAddress`
      - `+ clusters.eipv6Address`
  - **ShowClusterDetails**
    - 响应参数变更
      - `+ cluster.eipId`
      - `+ cluster.eipAddress`
      - `+ cluster.eipv6Address`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RecognizeGeneralText**
    - 请求参数变更
      - `+ single_orientation_mode`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ModifyCollation`
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
  - **SendDlqMessage**
    - 请求参数变更
      - `+ engine: enum value [reliability]`
  - **CreateRocketMqMigrationTask**
    - 请求参数变更
      - `+ type: enum value [kafka]`

### HuaweiCloud SDK SIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowVocabularies**
    - 请求参数变更
      - `+ offset`
      - `+ limit`

# 3.1.43 2023-06-08

### HuaweiCloud SDK iDME

- _新增特性_
  - 工业数字模型驱动引擎
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK BCS

- _新增特性_
  - 支持接口`ListBcsEvents`、`ListBcsEventsStatistic`
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
  - **UpdateIndirectPartnerAccount**
    - 请求参数变更
      - `* amount: double -> bigdecimal`
  - **ListCustomerBillsMonthlyBreakDown**
    - 响应参数变更
      - `* details.past_months_amortized_amount: double -> bigdecimal`
      - `* details.amortized_cash_amount: double -> bigdecimal`
  - **ListIssuedCouponQuotas**
    - 响应参数变更
      - `* quotas.balance: double -> bigdecimal`

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowNode**
    - 响应参数变更
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
  - **UpdateNode**
    - 响应参数变更
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
  - **DeleteNode**
    - 响应参数变更
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
  - **CreateNode**
    - 请求参数变更
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
    - 响应参数变更
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
  - **ListNodes**
    - 响应参数变更
      - `+ items.spec.extendParam.kube-reserved-mem`
      - `+ items.spec.extendParam.system-reserved-mem`
  - **ShowNodePool**
    - 响应参数变更
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
  - **UpdateNodePool**
    - 响应参数变更
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
  - **DeleteNodePool**
    - 响应参数变更
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
  - **CreateNodePool**
    - 请求参数变更
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
    - 响应参数变更
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
  - **ListNodePools**
    - 响应参数变更
      - `+ items.spec.type: enum value [pm]`
      - `+ items.spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ items.spec.nodeTemplate.extendParam.system-reserved-mem`

### HuaweiCloud SDK CloudDeploy

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateDeploymentGroup**
    - 请求参数变更
      - `+ is_proxy_mode`

### HuaweiCloud SDK DNS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListRecordSetsByZone**
    - 请求参数变更
      - `+ search_mode`
  - **CreateRecordSet**
    - 请求参数变更
      - `* body: object<CreateRecordSetReq> -> object<CreateRecordSetRequestBody>`
  - **CreateRecordSetWithLine**
    - 请求参数变更
      - `* body: object<CreateRecordSetWithLineReq> -> object<CreateRecordSetWithLineRequestBody>`
  - **ListPublicZones**
    - 请求参数变更
      - `+ search_mode`
  - **ListPrivateZones**
    - 请求参数变更
      - `+ search_mode`
  - **ListRecordSets**
    - 请求参数变更
      - `+ search_mode`

### HuaweiCloud SDK ECS

- _新增特性_
  - 支持接口`ChangeServerChargeMode`
- _解决问题_
  - 无
- _特性变更_
  - **CreateServers**
    - 请求参数变更
      - `+ server.nics.allowed_address_pairs`
  - **CreatePostPaidServers**
    - 请求参数变更
      - `+ server.nics.allowed_address_pairs`

### HuaweiCloud SDK ELB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListListeners**
    - 响应参数变更
      - `+ listeners.port_ranges`
  - **CreateListener**
    - 请求参数变更
      - `+ listener.port_ranges`
    - 响应参数变更
      - `+ listener.port_ranges`
  - **ShowListener**
    - 响应参数变更
      - `+ listener.port_ranges`
  - **UpdateListener**
    - 响应参数变更
      - `+ listener.port_ranges`
  - **ListPools**
    - 响应参数变更
      - `+ pools.any_port_enable`
  - **CreatePool**
    - 请求参数变更
      - `+ pool.any_port_enable`
    - 响应参数变更
      - `+ pool.any_port_enable`
  - **ShowPool**
    - 响应参数变更
      - `+ pool.any_port_enable`
  - **UpdatePool**
    - 响应参数变更
      - `+ pool.any_port_enable`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 支持以下接口：
    - `UpdateFuncSnapshot`
    - `ShowFuncSnapshotState`
    - `ShowResInstanceInfo`
    - `ShowProjectTagsList`
    - `CreateTags`
    - `DeleteTags`
    - `CreateVpcEndpoint`
    - `DeleteVpcEndpoint`
- _解决问题_
  - 无
- _特性变更_
  - **ListStatistics**
    - 响应参数变更
      - `* count.value: int32 -> number`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 支持以下接口：
    - `ListInstancesDetails`
    - `CreateDbInstance`
    - `ListParamGroupTemplates`
    - `ShowInstanceParamGroup`
    - `ListDbFlavors`
    - `ListDbBackups`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 支持接口`RetryBatchTask`、`StopBatchTask`
- _解决问题_
  - 无
- _特性变更_
  - **CreateBatchTask**
    - 响应参数变更
      - `+ task_progress.removed`
      - `+ task_progress.device_in_progress`
      - `+ task_progress.rejected`
  - **ListBatchTasks**
    - 响应参数变更
      - `+ batchtasks.task_progress.removed`
      - `+ batchtasks.task_progress.device_in_progress`
      - `+ batchtasks.task_progress.rejected`
  - **ShowBatchTask**
    - 请求参数变更
      - `+ task_detail_status`
      - `+ target`
    - 响应参数变更
      - `+ batchtask.task_progress.removed`
      - `+ batchtask.task_progress.device_in_progress`
      - `+ batchtask.task_progress.rejected`

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`ListAvailableZones`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持接口`AddIssueWorkHours`、`ListProjectWorkHoursType`
- _解决问题_
  - 无
- _特性变更_
  - **ShowProjectWorkHours**
    - 响应参数变更
      - `+ work_hours.work_hours_created_time`
      - `+ work_hours.work_hours_updated_time`
  - **ListProjectWorkHours**
    - 响应参数变更
      - `+ work_hours.work_hours_created_time`
      - `+ work_hours.work_hours_updated_time`
  - **ListIssueCustomFields**
    - 请求参数变更
      - `+ included_not_in_use`
    - 响应参数变更
      - `+ datas.create_time`
  - **ListIssuesV4**
    - 请求参数变更
      - `+ created_time_interval`
      - `+ closed_time_interval`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListInstanceTags`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 支持接口`SendDlqMessage`、`ValidateConsumedMessage`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`SendRocketMqDlqMessage`、`ValidateRocketMqConsumedMessage`
  - **CreateInstanceByEngine**
    - 请求参数变更
      - `+ product_id: enum value [c6.4u8g.cluster.small]`

### HuaweiCloud SDK TMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListResource**
    - 响应参数变更
      - `+ resources.tags`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowAddressGroup**
    - 响应参数变更
      - `+ address_group.enterprise_project_id`
  - **UpdateAddressGroup**
    - 响应参数变更
      - `+ address_group.enterprise_project_id`
  - **ListAddressGroup**
    - 请求参数变更
      - `+ enterprise_project_id`
    - 响应参数变更
      - `+ address_groups.enterprise_project_id`
  - **CreateAddressGroup**
    - 请求参数变更
      - `+ address_group.enterprise_project_id`
    - 响应参数变更
      - `+ address_group.enterprise_project_id`

# 3.1.42 2023-06-01

### HuaweiCloud SDK BSS

- _新增特性_
  - 支持接口`ListMultiAccountTransferCoupons`、`ListMultiAccountRetrieveCoupons`、`ClaimEnterpriseMultiAccountCoupon`、`ReclaimEnterpriseMultiAccountCoupon`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateCustomerAccountAmount**
    - 请求参数变更
      - `* amount: double -> bigdecimal`
  - **ReclaimIndirectPartnerAccount**
    - 请求参数变更
      - `* amount: double -> bigdecimal`
  - **ReclaimToPartnerAccount**
    - 请求参数变更
      - `* amount: double -> bigdecimal`
  - **ListPartnerCouponsRecord**
    - 响应参数变更
      - `* records.operation_amount: double -> bigdecimal`
  - **ListCustomersBalancesDetail**
    - 响应参数变更
      - `* customer_balances.debt_amount: double -> bigdecimal`
      - `* customer_balances.amount: double -> bigdecimal`
  - **ShowCustomerMonthlySum**
    - 响应参数变更
      - `* consume_amount: double -> bigdecimal`
      - `* debt_amount: double -> bigdecimal`
      - `* coupon_amount: double -> bigdecimal`
      - `* flexipurchase_coupon_amount: double -> bigdecimal`
      - `* stored_value_card_amount: double -> bigdecimal`
      - `* cash_amount: double -> bigdecimal`
      - `* credit_amount: double -> bigdecimal`
      - `* writeoff_amount: double -> bigdecimal`
      - `* bill_sums.official_amount: double -> bigdecimal`
      - `* bill_sums.official_discount_amount: double -> bigdecimal`
      - `* bill_sums.truncated_amount: double -> bigdecimal`
      - `* bill_sums.consume_amount: double -> bigdecimal`
      - `* bill_sums.coupon_amount: double -> bigdecimal`
      - `* bill_sums.flexipurchase_coupon_amount: double -> bigdecimal`
      - `* bill_sums.stored_value_card_amount: double -> bigdecimal`
      - `* bill_sums.debt_amount: double -> bigdecimal`
      - `* bill_sums.writeoff_amount: double -> bigdecimal`
      - `* bill_sums.cash_amount: double -> bigdecimal`
      - `* bill_sums.credit_amount: double -> bigdecimal`
  - **UpdateCouponQuotas**
    - 请求参数变更
      - `* quota_amount: double -> bigdecimal`
  - **ListCouponQuotasRecords**
    - 响应参数变更
      - `* records.amount: double -> bigdecimal`
  - **ReclaimCouponQuotas**
    - 响应参数变更
      - `* simple_quota_infos.quota_balance: double -> bigdecimal`
  - **ShowCustomerAccountBalances**
    - 响应参数变更
      - `* debt_amount: double -> bigdecimal`
      - `* account_balances.amount: double -> bigdecimal`
      - `* account_balances.designated_amount: double -> bigdecimal`
      - `* account_balances.credit_amount: double -> bigdecimal`
  - **ListFreeResourceUsages**
    - 响应参数变更
      - `* free_resources.amount: double -> bigdecimal`
      - `* free_resources.original_amount: double -> bigdecimal`
  - **ListIssuedPartnerCoupons**
    - 响应参数变更
      - `* user_coupons.face_value: double -> bigdecimal`
      - `* user_coupons.balance: double -> bigdecimal`
  - **ListOnDemandResourceRatings**
    - 响应参数变更
      - `* amount: double -> bigdecimal`
      - `* discount_amount: double -> bigdecimal`
      - `* official_website_amount: double -> bigdecimal`
      - `* product_rating_results.amount: double -> bigdecimal`
      - `* product_rating_results.discount_amount: double -> bigdecimal`
      - `* product_rating_results.official_website_amount: double -> bigdecimal`
  - **ListSubcustomerMonthlyBills**
    - 响应参数变更
      - `* bill_sums.amount: double -> bigdecimal`
      - `* bill_sums.debt_amount: double -> bigdecimal`
      - `* bill_sums.adjustment_amount: double -> bigdecimal`
      - `* bill_sums.discount_amount: double -> bigdecimal`
      - `* bill_sums.account_details.amount: double -> bigdecimal`
  - **ListCustomerBillsMonthlyBreakDown**
    - 响应参数变更
      - `* details.usage: double -> bigdecimal`
      - `* details.free_resource_usage: double -> bigdecimal`
      - `* details.ri_usage: double -> bigdecimal`
      - `* details.consume_amount: double -> bigdecimal`
      - `* details.current_month_amortized_amount: double -> bigdecimal`
      - `* details.future_months_amortized_amount: double -> bigdecimal`
      - `* details.amortized_credit_amount: double -> bigdecimal`
      - `* details.amortized_coupon_amount: double -> bigdecimal`
      - `* details.amortized_flexipurchase_coupon_amount: double -> bigdecimal`
      - `* details.amortized_stored_value_card_amount: double -> bigdecimal`
      - `* details.amortized_bonus_amount: double -> bigdecimal`
  - **ListQuotaCoupons**
    - 响应参数变更
      - `* quotas.quota_value: double -> bigdecimal`
      - `* quotas.balance: double -> bigdecimal`
  - **ListIssuedCouponQuotas**
    - 响应参数变更
      - `* quotas.quota_value: double -> bigdecimal`

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListFreeResourceUsages**
    - 响应参数变更
      - `* free_resources.amount: double -> bigdecimal`
      - `* free_resources.original_amount: double -> bigdecimal`
  - **ListOnDemandResourceRatings**
    - 响应参数变更
      - `* amount: double -> bigdecimal`
      - `* discount_amount: double -> bigdecimal`
      - `* official_website_amount: double -> bigdecimal`
      - `* product_rating_results.amount: double -> bigdecimal`
      - `* product_rating_results.discount_amount: double -> bigdecimal`
      - `* product_rating_results.official_website_amount: double -> bigdecimal`

### HuaweiCloud SDK CBH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowNetworkConfiguration**
    - 请求参数变更
      - `+ nics.ip_address`
  - **ChangeInstanceNetwork**
    - 请求参数变更
      - `+ nics.ip_address`
  - **CreateInstance**
    - 请求参数变更
      - `+ server.nics.ip_address`

### HuaweiCloud SDK CBR

- _新增特性_
  - 支持接口`ShowSummary`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CBS

- _新增特性_
  - 支持接口`PostRequests`
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
  - **ShowAddonInstance**
    - 响应参数变更
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
  - **UpdateAddonInstance**
    - 请求参数变更
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
    - 响应参数变更
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
  - **CreateAddonInstance**
    - 请求参数变更
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
    - 响应参数变更
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
  - **ListAddonInstances**
    - 响应参数变更
      - `+ items.metadata.alias`
      - `* items.metadata: object<Metadata> -> object<AddonMetadata>`
  - **ListAddonTemplates**
    - 响应参数变更
      - `+ items.metadata.alias`
      - `* items.metadata: object<Metadata> -> object<AddonMetadata>`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowLogs**
    - 请求参数变更
      - `+ start_time`
      - `+ end_time`
      - `- query_date`
  - **ShowDomainFullConfig**
    - 请求参数变更
      - `+ show_special_configs`
    - 响应参数变更
      - `- configs.error_code_cache.code: enum value [400,403,404,405,414,500,501,502,503,504]`
      - `+ configs.flexible_origin.back_sources.http_port`
      - `+ configs.flexible_origin.back_sources.https_port`
  - **UpdateDomainFullConfig**
    - 请求参数变更
      - `- configs.error_code_cache.code: enum value [400,403,404,405,414,500,501,502,503,504]`
      - `+ configs.flexible_origin.back_sources.http_port`
      - `+ configs.flexible_origin.back_sources.https_port`

### HuaweiCloud SDK CPTS

- _新增特性_
  - 支持以下接口：
    - `UpdateDirectory`
    - `DeleteDirectory`
    - `ListTaskCases`
    - `CreateNewTask`
    - `CreateNewCase`
    - `ShowCase`
    - `UpdateNewCase`
    - `DeleteNewCase`
    - `ShowMergeReportLogsOutline`
    - `ShowTaskCaseAwChart`
    - `ShowMergeCaseDetail`
    - `ShowMergeTaskCase`
    - `BatchUpdateTaskStatus`
    - `CreateDirectory`
    - `DeleteNewTask`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateCase**
    - 请求参数变更
      - `+ directory_id`
      - `+ setup_contents`
      - `+ user_replicas`
      - `+ collect_log_policy`
      - `+ link_app_list`
      - `+ case_info`
      - `+ contents.content.content.rtmp_url`
      - `+ contents.content.content.flv_url`
      - `+ contents.content.content.bitrate_type`
      - `+ contents.content.content.duration`
      - `+ contents.content.content.retry_delay`
      - `+ contents.content.content.retry_time`
  - **UpdateTemp**
    - 请求参数变更
      - `+ contents.content.content.rtmp_url`
      - `+ contents.content.content.flv_url`
      - `+ contents.content.content.bitrate_type`
      - `+ contents.content.content.duration`
      - `+ contents.content.content.retry_delay`
      - `+ contents.content.content.retry_time`
  - **ShowTask**
    - 响应参数变更
      - `+ taskInfo.case_list.directory_id`
      - `+ taskInfo.case_list.setup_contents`
      - `+ taskInfo.case_list.user_replicas`
      - `+ taskInfo.case_list.collect_log_policy`
      - `+ taskInfo.case_list.link_app_list`
      - `+ taskInfo.case_list.case_info`
      - `+ taskInfo.case_list.contents.content.content.rtmp_url`
      - `+ taskInfo.case_list.contents.content.content.flv_url`
      - `+ taskInfo.case_list.contents.content.content.bitrate_type`
      - `+ taskInfo.case_list.contents.content.content.duration`
      - `+ taskInfo.case_list.contents.content.content.retry_delay`
      - `+ taskInfo.case_list.contents.content.content.retry_time`
  - **UpdateTask**
    - 请求参数变更
      - `+ case_list.directory_id`
      - `+ case_list.setup_contents`
      - `+ case_list.user_replicas`
      - `+ case_list.collect_log_policy`
      - `+ case_list.link_app_list`
      - `+ case_list.case_info`
      - `+ case_list.contents.content.content.rtmp_url`
      - `+ case_list.contents.content.content.flv_url`
      - `+ case_list.contents.content.content.bitrate_type`
      - `+ case_list.contents.content.content.duration`
      - `+ case_list.contents.content.content.retry_delay`
      - `+ case_list.contents.content.content.retry_time`
    - 响应参数变更
      - `+ taskInfo.case_list.directory_id`
      - `+ taskInfo.case_list.setup_contents`
      - `+ taskInfo.case_list.user_replicas`
      - `+ taskInfo.case_list.collect_log_policy`
      - `+ taskInfo.case_list.link_app_list`
      - `+ taskInfo.case_list.case_info`
      - `+ taskInfo.case_list.contents.content.content.rtmp_url`
      - `+ taskInfo.case_list.contents.content.content.flv_url`
      - `+ taskInfo.case_list.contents.content.content.bitrate_type`
      - `+ taskInfo.case_list.contents.content.content.duration`
      - `+ taskInfo.case_list.contents.content.content.retry_delay`
      - `+ taskInfo.case_list.contents.content.content.retry_time`
  - **UpdateTaskRelatedTestCase**
    - 响应参数变更
      - `+ taskInfo.case_list.directory_id`
      - `+ taskInfo.case_list.setup_contents`
      - `+ taskInfo.case_list.user_replicas`
      - `+ taskInfo.case_list.collect_log_policy`
      - `+ taskInfo.case_list.link_app_list`
      - `+ taskInfo.case_list.case_info`
      - `+ taskInfo.case_list.contents.content.content.rtmp_url`
      - `+ taskInfo.case_list.contents.content.content.flv_url`
      - `+ taskInfo.case_list.contents.content.content.bitrate_type`
      - `+ taskInfo.case_list.contents.content.content.duration`
      - `+ taskInfo.case_list.contents.content.content.retry_delay`
      - `+ taskInfo.case_list.contents.content.content.retry_time`

### HuaweiCloud SDK DNS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RestorePtrRecord**
    - 请求参数变更
      - `* ptrdname: string -> object`
  - **ShowRecordSet**
    - 响应参数变更
      - `+ bundle`
  - **CreateEipRecordSet**
    - 响应参数变更
      - `+ enterprise_project_id`
  - **ShowPtrRecordSet**
    - 响应参数变更
      - `+ enterprise_project_id`
  - **ShowResourceTag**
    - 响应参数变更
      - `+ enterpriseProjectOrDefault`
  - **ListPrivateZones**
    - 请求参数变更
      - `* type: required -> optional`

### HuaweiCloud SDK EG

- _新增特性_
  - 支持以下接口：
    - `ShowDetailOfEventTrace`
    - `ShowDetailOfEvent`
    - `ListTracedEvents`
    - `PutOfficialEvents`
    - `ListEventStreaming`
    - `CreateEventStreaming`
    - `ShowEventStreaming`
    - `UpdateEventStreaming`
    - `DeleteEventStreaming`
    - `ResumeEventStreaming`
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
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
  - **ShowDetailOfEventSource**
    - 响应参数变更
      - `+ provider_type: enum value [PARTNER]`
  - **UpdateEventSource**
    - 响应参数变更
      - `+ provider_type: enum value [PARTNER]`
  - **ShowDetailOfChannel**
    - 响应参数变更
      - `+ provider_type: enum value [PARTNER]`
  - **UpdateChannel**
    - 响应参数变更
      - `+ provider_type: enum value [PARTNER]`
  - **UpdateSubscriptionSource**
    - 请求参数变更
      - `+ provider_type: enum value [PARTNER]`
  - **ShowDetailOfConnection**
    - 响应参数变更
      - `+ type`
      - `+ kafka_detail`
  - **UpdateConnection**
    - 响应参数变更
      - `+ type`
      - `+ kafka_detail`
  - **CreateEventSource**
    - 响应参数变更
      - `+ provider_type: enum value [PARTNER]`
  - **ListEventSources**
    - 请求参数变更
      - `+ provider_type: enum value [PARTNER]`
    - 响应参数变更
      - `+ items.provider_type: enum value [PARTNER]`
  - **CreateChannel**
    - 响应参数变更
      - `+ provider_type: enum value [PARTNER]`
  - **ListChannels**
    - 请求参数变更
      - `+ provider_type: enum value [PARTNER]`
    - 响应参数变更
      - `+ items.provider_type: enum value [PARTNER]`
  - **CreateSubscriptionTarget**
    - 请求参数变更
      - `+ kafka_detail`
  - **UpdateSubscriptionTarget**
    - 请求参数变更
      - `+ kafka_detail`
  - **CreateConnection**
    - 请求参数变更
      - `+ type`
      - `+ kafka_detail`
    - 响应参数变更
      - `+ type`
      - `+ kafka_detail`
  - **ListConnections**
    - 响应参数变更
      - `+ type`
      - `+ kafka_detail`
      - `+ items.type`
      - `+ items.kafka_detail`
  - **ListEventTarget**
    - 请求参数变更
      - `+ support_types`
  - **UpdateSubscription**
    - 请求参数变更
      - `+ sources.provider_type: enum value [PARTNER]`
      - `+ targets.kafka_detail`
  - **CreateSubscription**
    - 请求参数变更
      - `+ sources.provider_type: enum value [PARTNER]`
      - `+ targets.kafka_detail`
  - **ListSubscriptions**
    - 请求参数变更
      - `+ connection_id`

### HuaweiCloud SDK ELB

- _新增特性_
  - 支持接口`DeleteLoadBalancerForce`、`DeleteListenerForce`、`BatchUpdateMembers`
- _解决问题_
  - 无
- _特性变更_
  - **ShowQuota**
    - 响应参数变更
      - `+ quota.condition_per_policy`
      - `+ quota.listeners_per_pool`
      - `+ quota.listeners_per_loadbalancer`
      - `* quota.ipgroup_bindings: string -> int32`
      - `* quota.ipgroup_max_length: string -> int32`
  - **ShowLoadBalancer**
    - 响应参数变更
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
  - **UpdateLoadBalancer**
    - 请求参数变更
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
    - 响应参数变更
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
  - **ListListeners**
    - 请求参数变更
      - `+ protection_status`
    - 响应参数变更
      - `+ listeners.protection_status`
      - `+ listeners.protection_reason`
      - `+ listeners.gzip_enable`
  - **CreateListener**
    - 请求参数变更
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
    - 响应参数变更
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
  - **ShowListener**
    - 响应参数变更
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
  - **UpdateListener**
    - 请求参数变更
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
    - 响应参数变更
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
  - **ListPools**
    - 请求参数变更
      - `+ protection_status`
    - 响应参数变更
      - `+ pools.protection_status`
      - `+ pools.protection_reason`
  - **CreatePool**
    - 请求参数变更
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
    - 响应参数变更
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
  - **ShowPool**
    - 响应参数变更
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
  - **UpdatePool**
    - 请求参数变更
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
    - 响应参数变更
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
  - **UpdateMember**
    - 请求参数变更
      - `+ member.protocol_port`
  - **ListLoadBalancers**
    - 请求参数变更
      - `+ protection_status`
      - `+ global_eips`
    - 响应参数变更
      - `+ loadbalancers.protection_status`
      - `+ loadbalancers.protection_reason`
  - **CreateLoadBalancer**
    - 请求参数变更
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
    - 响应参数变更
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
  - **ListL7Policies**
    - 响应参数变更
      - `+ l7policies.redirect_pools_extend_config`
      - `- l7policies.redirect_pools_config`
  - **CreateL7Policy**
    - 请求参数变更
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`
    - 响应参数变更
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`
  - **ShowL7Policy**
    - 响应参数变更
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`
  - **UpdateL7Policy**
    - 请求参数变更
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`
    - 响应参数变更
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateGaussMySqlInstance**
    - 请求参数变更
      - `+ restore_point`

### HuaweiCloud SDK IEC

- _新增特性_
  - 支持以下接口：
    - `ListCloudImages`
    - `RegisterImage`
    - `CreateImage`
    - `ShowVolumeTypes`
    - `RebuildImage`
    - `DeleteImage`
    - `UpdateBandwidth`
    - `DeleteBandwidth`
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
  - **ListInstanceTopics**
    - 请求参数变更
      - `+ offset`
      - `+ limit`
  - **ListInstances**
    - 请求参数变更
      - `+ offset`
      - `+ limit`

### HuaweiCloud SDK MPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListEditingJobs`、`CreateEditingJobs`、`DeleteEditingJobs`

### HuaweiCloud SDK Organizations

- _新增特性_
  - 支持接口`ListQuotas`
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
  - **ShowIssueV4**
    - 响应参数变更
      - `+ story_point`
  - **SearchIssues**
    - 响应参数变更
      - `+ issue_list.due_date`
  - **ListIssueCommentsV4**
    - 响应参数变更
      - `+ comments.timestamp`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreatePostPaidInstanceByEngine**
    - 请求参数变更
      - `+ bss_param`
  - **CreatePostPaidInstance**
    - 请求参数变更
      - `+ bss_param`
  - **ListInstancesDetails**
    - 请求参数变更
      - `+ offset`
      - `+ limit`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListEngineFlavors`、`BatchDeleteManualBackup`、`DeleteJob`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 支持以下接口：
    - `SendRocketMqDlqMessage`
    - `ValidateRocketMqConsumedMessage`
    - `ListRocketMqMigrationTask`
    - `CreateRocketMqMigrationTask`
    - `DeleteRocketMqMigrationTask`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SMN

- _新增特性_
  - 支持以下接口：
    - `UpdateSubscription`
    - `ListLogtank`
    - `CreateLogtank`
    - `UpdateLogtank`
    - `DeleteLogtank`
- _解决问题_
  - 无
- _特性变更_
  - **ListTopicDetails**
    - 响应参数变更
      - `+ topic_id`
  - **ListTopics**
    - 请求参数变更
      - `+ topic_id`
    - 响应参数变更
      - `+ topics.topic_id`
  - **ListTopicAttributes**
    - 响应参数变更
      - `+ attributes.access_policy`
      - `+ attributes.introduction`
      - `- attributes.Version`
      - `- attributes.Id`
      - `- attributes.Statement`
  - **AddSubscription**
    - 请求参数变更
      - `+ extension`

### HuaweiCloud SDK VOD

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateAssetByFileUpload**
    - 请求参数变更
      - `+ review.interval`
      - `+ review.politics`
      - `+ review.terrorism`
      - `+ review.porn`
  - **PublishAssetFromObs**
    - 请求参数变更
      - `+ review.interval`
      - `+ review.politics`
      - `+ review.terrorism`
      - `+ review.porn`
  - **CreateAssetReviewTask**
    - 请求参数变更
      - `+ review.interval`
      - `+ review.politics`
      - `+ review.terrorism`
      - `+ review.porn`
    - 响应参数变更
      - `+ review.interval`
      - `+ review.politics`
      - `+ review.terrorism`
      - `+ review.porn`
  - **UploadMetaDataByUrl**
    - 请求参数变更
      - `+ upload_metadatas.review.interval`
      - `+ upload_metadatas.review.politics`
      - `+ upload_metadatas.review.terrorism`
      - `+ upload_metadatas.review.porn`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateVpcPeering**
    - 请求参数变更
      - `+ peering.description`

# 3.1.41 2023-05-25

### HuaweiCloud SDK CBH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowNetworkConfiguration**
    - 请求参数变更
      - `- nics.ip_address`
  - **CreateInstanceOrder**
    - 请求参数变更
      - `- product_infos.resource_size_measure_id`
      - `- product_infos.resource_size`
  - **ChangeInstanceNetwork**
    - 请求参数变更
      - `- nics.ip_address`
  - **CreateInstance**
    - 请求参数变更
      - `+ server.enterprise_project_id`
      - `- server.nics.ip_address`
      - `- server.public_ip.eip`

### HuaweiCloud SDK CBR

- _新增特性_
  - 支持以下接口：
    - `ImportCheckpoint`
    - `ListExternalVault`
    - `BatchUpdateVault`
    - `SetVaultResource`
    - `ShowMetadata`
    - `CheckAgent`
    - `ListProjects`
    - `ListDomainProjects`
    - `ShowDomain`
    - `ShowMigrateStatus`
    - `MigrateDomain`
    - `ShowStorageUsage`
    - `UpdateOrder`
    - `CreatePostPaidVault`
    - `UpdateBackup`
- _解决问题_
  - 无
- _特性变更_
  - **CreateVault**
    - 请求参数变更
      - `+ vault.threshold`
      - `+ vault.smn_notify`
      - `+ vault.backup_name_prefix`
      - `+ vault.demand_billing`
    - 响应参数变更
      - `+ vault.backup_name_prefix`
      - `+ vault.demand_billing`
      - `+ vault.cbc_delete_count`
      - `+ vault.frozen`

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowCluster**
    - 响应参数变更
      - `+ metadata.alias`
  - **UpdateCluster**
    - 请求参数变更
      - `+ metadata`
    - 响应参数变更
      - `+ metadata.alias`
  - **DeleteCluster**
    - 响应参数变更
      - `+ metadata.alias`
  - **MigrateNode**
    - 请求参数变更
      - `+ spec.runtime`
    - 响应参数变更
      - `+ spec.runtime`
  - **CreateCluster**
    - 请求参数变更
      - `+ metadata.alias`
    - 响应参数变更
      - `+ metadata.alias`
  - **ListClusters**
    - 响应参数变更
      - `+ items.metadata.alias`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDomainDetailByName**
    - 响应参数变更
      - `+ domain.domain_name`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListMigrationTask**
    - 响应参数变更
      - `- task_name`
      - `- target_instance_id`
      - `- target_instance_address`
      - `- target_instance_name`
      - `- migrate_type`
      - `- created_at`
      - `- source_instance_id`
      - `- task_id`
      - `- data_source`
      - `- migration_method`
      - `- source_instance_name`
      - `- status`
  - **ListConfigTemplates**
    - 响应参数变更
      - `* template_num: number -> integer`
  - **ListInstances**
    - 响应参数变更
      - `+ instances.updated_at`
  - **ListBackgroundTask**
    - 响应参数变更
      - `- updated_at`
      - `- created_at`
      - `- status`
  - **ListFlavors**
    - 响应参数变更
      - `+ flavors.flavors_available_zones.unit`
      - `+ flavors.flavors_available_zones.available_zones`

### HuaweiCloud SDK ECS

- _新增特性_
  - 支持接口`ListFlavorSellPolicies`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListPublicipsByTags**
    - 响应参数变更
      - `+ resources.resource_detail`
      - `- resources.resouce_detail`
  - **AddPublicipsIntoSharedBandwidth**
    - 响应参数变更
      - `+ bandwidth.enable_bandwidth_rules`
      - `+ bandwidth.rule_quota`
      - `+ bandwidth.bandwidth_rules`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`UpdateProxyConnectionPoolType`、`RestoreOldInstance`、`ShowBackupRestoreTime`
- _解决问题_
  - 无
- _特性变更_
  - **ShowGaussMySqlProxyList**
    - 响应参数变更
      - `+ proxy_list.proxy.connection_pool_type`
      - `+ proxy_list.proxy.switch_connection_pool_type_enabled`

### HuaweiCloud SDK IAM

- _新增特性_
  - 支持接口`AssociateRoleToAgencyOnEnterpriseProject`、`RevokeRoleFromAgencyOnEnterpriseProject`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Image

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`CreateVideoObjectMaskingTask`、`ShowVideoObjectMaskingTask`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`DeleteConnector`、`CreateDeleteConnectorOrder`、`CreateKafkaConsumerGroup`、`CloseKafkaManager`
- _解决问题_
  - 无
- _特性变更_
  - **ShowInstance**
    - 响应参数变更
      - `+ kafka_manager_enable`
  - **ListInstances**
    - 响应参数变更
      - `+ kafka_manager_enable`
      - `+ instances.kafka_manager_enable`

### HuaweiCloud SDK Live

- _新增特性_
  - 支持接口`BatchShowIpBelongs`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK MSGSMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowSignatureFile**
    - 响应参数变更
      - `+ file_desc`
  - **UpdateApp**
    - 响应参数变更
      - `- app_secret`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreatePostPaidInstanceByEngine**
    - 请求参数变更
      - `+ engine_version: enum value [3.8.35]`
  - **CreatePostPaidInstance**
    - 请求参数变更
      - `+ engine_version: enum value [3.8.35]`

### HuaweiCloud SDK RAM

- _新增特性_
  - 支持接口`ListQuota`
- _解决问题_
  - 无
- _特性变更_
  - **AssociateResourceShare**
    - 响应参数变更
      - `+ resource_share_associations.external`
  - **DisassociateResourceShare**
    - 响应参数变更
      - `+ resource_share_associations.external`
  - **SearchResourceShareAssociations**
    - 响应参数变更
      - `+ resource_share_associations.external`
  - **CreateResourceShare**
    - 请求参数变更
      - `+ allow_external_principals`
    - 响应参数变更
      - `+ resource_share.allow_external_principals`
  - **SearchResourceShares**
    - 响应参数变更
      - `+ resource_shares.allow_external_principals`
  - **UpdateResourceShare**
    - 请求参数变更
      - `+ allow_external_principals`
    - 响应参数变更
      - `+ resource_share.allow_external_principals`

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSqlserverDatabases**
    - 请求参数变更
      - `+ recover_model`

### HuaweiCloud SDK RMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowPolicyAssignment**
    - 响应参数变更
      - `+ created_by`
  - **UpdatePolicyAssignment**
    - 响应参数变更
      - `+ created_by`
  - **ShowAggregatePolicyAssignmentDetail**
    - 响应参数变更
      - `+ created_by`
  - **CreatePolicyAssignments**
    - 响应参数变更
      - `+ created_by`
  - **ListPolicyAssignments**
    - 响应参数变更
      - `+ created_by`
      - `+ value.created_by`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateVpc**
    - 请求参数变更
      - `+ vpc.tags`
  - **CreateSubnet**
    - 请求参数变更
      - `+ subnet.tags`
    - **ShowAddressGroup**
    - 响应参数变更
      - `+ address_group.max_capacity`
      - `+ address_group.status`
      - `+ address_group.status_message`
  - **UpdateAddressGroup**
    - 请求参数变更
      - `+ address_group.max_capacity`
    - 响应参数变更
      - `+ address_group.max_capacity`
      - `+ address_group.status`
      - `+ address_group.status_message`
  - **ListAddressGroup**
    - 响应参数变更
      - `+ address_groups.max_capacity`
      - `+ address_groups.status`
      - `+ address_groups.status_message`
  - **CreateAddressGroup**
    - 请求参数变更
      - `+ address_group.max_capacity`
    - 响应参数变更
      - `+ address_group.max_capacity`
      - `+ address_group.status`
      - `+ address_group.status_message`

### HuaweiCloud SDK VPCEP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListServiceDescribeDetails**
    - 响应参数变更
      - `+ enable_policy`
  - **ListServiceDetails**
    - 响应参数变更
      - `- vip_port_id`
  - **UpdateEndpointService**
    - 请求参数变更
      - `- vip_port_id`
    - 响应参数变更
      - `- vip_port_id`
  - **ListServicePublicDetails**
    - 响应参数变更
      - `+ endpoint_services.enable_policy`
  - **CreateEndpointService**
    - 请求参数变更
      - `- vip_port_id`
    - 响应参数变更
      - `- vip_port_id`
  - **ListEndpointService**
    - 响应参数变更
      - `- endpoint_services.vip_port_id`

# 3.1.40 2023-05-18

### HuaweiCloud SDK CBR

- _新增特性_
  - 支持以下接口：
    - `AddAgentPath`
    - `ShowAgent`
    - `UpdateAgent`
    - `UnregisterAgent`
    - `ListAgent`
    - `RegisterAgent`
    - `RemoveAgentPath`
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
  - **ShowNode**
    - 响应参数变更
      - `+ status.lastProbeTime`
  - **UpdateNode**
    - 响应参数变更
      - `+ status.lastProbeTime`
  - **DeleteNode**
    - 响应参数变更
      - `+ status.lastProbeTime`
  - **CreateNode**
    - 响应参数变更
      - `+ status.lastProbeTime`
  - **ListNodes**
    - 响应参数变更
      - `+ items.status.lastProbeTime`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateRefreshTasks**
    - 请求参数变更
      - `* refresh_task.mode: boolean -> string`
  - **ShowDomainFullConfig**
    - 响应参数变更
      - `+ configs.flexible_origin`
      - `+ configs.slice_etag_status`
      - `+ configs.origin_receive_timeout`
      - `+ configs.remote_auth`
      - `+ configs.websocket`
      - `+ configs.video_seek`
      - `+ configs.request_limit_rules`
      - `+ configs.url_auth.sign_method`
      - `+ configs.url_auth.match_type`
      - `+ configs.url_auth.key`
      - `+ configs.url_auth.backup_key`
      - `+ configs.url_auth.sign_arg`
      - `+ configs.https.expire_time`
      - `+ configs.https.certificate_type`
      - `+ configs.https.ocsp_stapling_status`
      - `+ configs.sources.obs_bucket_type`
      - `+ configs.compress.file_type`
      - `+ configs.user_agent_filter.ua_list`
  - **UpdateDomainFullConfig**
    - 请求参数变更
      - `+ configs.flexible_origin`
      - `+ configs.slice_etag_status`
      - `+ configs.origin_receive_timeout`
      - `+ configs.remote_auth`
      - `+ configs.websocket`
      - `+ configs.video_seek`
      - `+ configs.request_limit_rules`
      - `+ configs.url_auth.sign_method`
      - `+ configs.url_auth.match_type`
      - `+ configs.url_auth.backup_key`
      - `+ configs.url_auth.sign_arg`
      - `+ configs.https.certificate_type`
      - `+ configs.https.ocsp_stapling_status`
      - `+ configs.sources.obs_bucket_type`
      - `+ configs.compress.file_type`
      - `+ configs.user_agent_filter.ua_list`
  - **ShowDomainDetailByName**
    - 响应参数变更
      - `+ domain.sources.obs_bucket_type`

### HuaweiCloud SDK CloudPipeline

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowInstanceStatus**
    - 请求参数变更
      - `- X-Language`
  - **StopPipelineNew**
    - 请求参数变更
      - `- X-Language`
  - **RemovePipeline**
    - 请求参数变更
      - `- X-Language`
  - **RunPipeline**
    - 请求参数变更
      - `- X-Language`
  - **BatchShowPipelinesLatestStatus**
    - 请求参数变更
      - `- X-Language`
  - **ListPipelines**
    - 请求参数变更
      - `- X-Language`
  - **DeletePipeline**
    - 请求参数变更
      - `- X-Language`
  - **StopPipelineRun**
    - 请求参数变更
      - `- X-Language`
  - **ListPipelineRuns**
    - 请求参数变更
      - `- X-Language`
  - **StartNewPipeline**
    - 请求参数变更
      - `- X-Language`
  - **BatchShowPipelinesStatus**
    - 请求参数变更
      - `- X-Language`
  - **ListPipelineSimpleInfo**
    - 请求参数变更
      - `- X-Language`
  - **ShowPipleineStatus**
    - 请求参数变更
      - `- X-Language`
  - **ListPipleineBuildResult**
    - 请求参数变更
      - `- X-Language`
  - **ListPipelineTemplates**
    - 请求参数变更
      - `- X-Language`
  - **CreatePipelineByTemplateId**
    - 请求参数变更
      - `- X-Language`
  - **ShowTemplateDetail**
    - 请求参数变更
      - `- X-Language`
  - **CreatePipelineByTemplate**
    - 请求参数变更
      - `- X-Language`
  - **ShowPipelineRunDetail**
    - 请求参数变更
      - `- X-Language`
  - **ListTemplates**
    - 请求参数变更
      - `- X-Language`

### HuaweiCloud SDK CPTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateTaskStatus**
    - 请求参数变更
      - `+ enterprise_project_id`
  - **UpdateAgentHealthStatus**
    - 响应参数变更
      - `+ result.result.kafka_enable`
      - `+ result.result.kafka_shadow_topic_prefix`
      - `+ result.result.app_log_level`
      - `+ result.result.app_log_path`
      - `+ result.result.mock_rule_list`

### HuaweiCloud SDK CSE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpgradeEngine**
    - 响应参数变更
      - `+ jobId`
      - `- job_id`
  - **RetryEngine**
    - 响应参数变更
      - `+ jobId`
      - `- job_id`
  - **DownloadKie**
    - 响应参数变更
      - `+ data.id`
  - **CreateEngine**
    - 响应参数变更
      - `+ jobId`
      - `- job_id`
  - **DeleteEngine**
    - 响应参数变更
      - `+ jobId`
      - `- job_id`

### HuaweiCloud SDK DAS

- _新增特性_
  - 支持接口`CreateShareConnections`、`CancelShareConnections`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持接口`ListAvailableDisasterClusters`、`CheckDisasterName`、`ShowDisasterDetail`、`UpdateDisasterInfo`
- _解决问题_
  - 无
- _特性变更_
  - **CreateCluster**
    - 请求参数变更
      - `+ cluster.tags`

### HuaweiCloud SDK ECS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateServers**
    - 请求参数变更
      - `+ server.root_volume.metadata`
      - `- server.root_volume.extendparam.__system__encrypted`
      - `- server.root_volume.extendparam.__system__cmkid`
      - `+ server.data_volumes.delete_on_termination`
  - **CreatePostPaidServers**
    - 请求参数变更
      - `+ server.data_volumes.delete_on_termination`
      - `+ server.root_volume.metadata`
      - `- server.root_volume.extendparam.__system__encrypted`
      - `- server.root_volume.extendparam.__system__cmkid`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 支持接口`UpdateGaussMySqlDatabaseUserComment`、`UpdateGaussMySqlDatabaseComment`、`ListLtsSlowlogDetails`、`ListLtsErrorLogDetails`
- _解决问题_
  - 无
- _特性变更_
  - **ListGaussMySqlDatabaseUser**
    - 响应参数变更
      - `+ users.comment`
  - **CreateGaussMySqlDatabaseUser**
    - 请求参数变更
      - `+ users.comment`
  - **ListGaussMySqlDatabase**
    - 响应参数变更
      - `+ databases.comment`
  - **CreateGaussMySqlDatabase**
    - 请求参数变更
      - `+ databases.comment`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **BroadcastMessage**
    - 请求参数变更
      - `+ ttl`
      - `+ message_id`
  - **ShowDeviceGroup**
    - 响应参数变更
      - `+ dynamic_group_rule`
      - `+ group_type`
  - **UpdateDeviceGroup**
    - 响应参数变更
      - `+ dynamic_group_rule`
      - `+ group_type`
  - **SearchDevices**
    - 响应参数变更
      - `+ devices.groups`
  - **AddDeviceGroup**
    - 请求参数变更
      - `+ group_type`
      - `+ dynamic_group_rule`
    - 响应参数变更
      - `+ dynamic_group_rule`
      - `+ group_type`
  - **ListDeviceGroups**
    - 请求参数变更
      - `+ group_type`
      - `+ name`
    - 响应参数变更
      - `+ device_groups.group_type`
      - `* device_groups: list<DeviceGroupResponsSummery> -> list<DeviceGroupResponseSummary>`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持接口`ListTemplates`、`SearchIssues`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.39 2023-05-11

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持接口`ContinueDeployStack`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowVaultResourceInstances**
    - 响应参数变更
      - `* resources.resource_detail: list<Vault> -> object<InstancesResourceDetail>`
  - **ListPolicies**
    - 响应参数变更
      - `+ policies.operation_definition.full_backup_interval`
  - **CreatePolicy**
    - 请求参数变更
      - `+ policy.operation_definition.full_backup_interval`
    - 响应参数变更
      - `+ policy.operation_definition.full_backup_interval`
  - **ShowPolicy**
    - 响应参数变更
      - `+ policy.operation_definition.full_backup_interval`
  - **UpdatePolicy**
    - 请求参数变更
      - `+ policy.operation_definition.full_backup_interval`
    - 响应参数变更
      - `+ policy.operation_definition.full_backup_interval`
  - **CreateVault**
    - 请求参数变更
      - `- vault.billing.extra_info`

### HuaweiCloud SDK CBS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ExecuteGetFramsListByImagesId**
    - 请求参数变更
      - `+ offset`
      - `+ limit`

### HuaweiCloud SDK CloudPipeline

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListPipelineTemplates**
    - 响应参数变更
      - `+ total`
      - `+ offset`
      - `+ templates`
      - `+ limit`
      - `- is_system`
      - `- is_show_source`
      - `- create_time`
      - `- icon`
      - `- description`
      - `- language`
      - `- domain_id`
      - `- is_collect`
      - `- update_time`
      - `- name`
      - `- manifest_version`
      - `- creator_id`
      - `- updater_id`
      - `- stages`
      - `- creator_name`
      - `- id`
      - `- region`

### HuaweiCloud SDK DGC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ExportConnections**
    - 请求参数变更
      - `+ workspace`
  - **ExportJob**
    - 请求参数变更
      - `+ workspace`
  - **StopJob**
    - 请求参数变更
      - `+ workspace`
  - **StopJobInstance**
    - 请求参数变更
      - `+ workspace`
  - **RestoreJobInstance**
    - 请求参数变更
      - `+ workspace`
  - **CancelScript**
    - 请求参数变更
      - `+ workspace`
  - **DeleteConnction**
    - 请求参数变更
      - `+ workspace`
  - **ShowConnection**
    - 请求参数变更
      - `+ workspace`
  - **UpdateConnection**
    - 请求参数变更
      - `+ workspace`
  - **ExportJobList**
    - 请求参数变更
      - `+ workspace`
  - **ImportJob**
    - 请求参数变更
      - `+ workspace`
  - **DeleteScript**
    - 请求参数变更
      - `+ workspace`
  - **ShowScript**
    - 请求参数变更
      - `+ workspace`
  - **UpdateScript**
    - 请求参数变更
      - `+ workspace`
  - **ExecuteScript**
    - 请求参数变更
      - `+ workspace`
  - **CreateResource**
    - 请求参数变更
      - `+ workspace`
  - **DeleteResource**
    - 请求参数变更
      - `+ workspace`
  - **ShowResource**
    - 请求参数变更
      - `+ workspace`
  - **UpdateResource**
    - 请求参数变更
      - `+ workspace`
  - **CreateConnection**
    - 请求参数变更
      - `+ workspace`
  - **ListConnections**
    - 请求参数变更
      - `+ workspace`
  - **ImportConnections**
    - 请求参数变更
      - `+ workspace`
  - **ShowFileInfo**
    - 请求参数变更
      - `+ workspace`
  - **StartJob**
    - 请求参数变更
      - `+ workspace`
  - **RunOnce**
    - 请求参数变更
      - `+ workspace`
  - **ShowJobStatus**
    - 请求参数变更
      - `+ workspace`
  - **ListJobInstances**
    - 请求参数变更
      - `+ workspace`
  - **ShowJobInstance**
    - 请求参数变更
      - `+ workspace`
  - **ListSystemTasks**
    - 请求参数变更
      - `+ workspace`
  - **CreateScript**
    - 请求参数变更
      - `+ workspace`
  - **ListScripts**
    - 请求参数变更
      - `+ workspace`
  - **ListScriptResults**
    - 请求参数变更
      - `+ workspace`
  - **DeleteJob**
    - 请求参数变更
      - `+ workspace`
  - **ShowJob**
    - 请求参数变更
      - `+ workspace`
  - **UpdateJob**
    - 请求参数变更
      - `+ workspace`
  - **CreateJob**
    - 请求参数变更
      - `+ workspace`
  - **ListJobs**
    - 请求参数变更
      - `+ workspace`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowMonitoringData**
    - 响应参数变更
      - `+ results.data_guard_minitor.migration_bytes_per_second`
  - **BatchListJobDetails**
    - 响应参数变更
      - `+ results.data_transformation`
      - `+ results.tags`

### HuaweiCloud SDK ECS

- _新增特性_
  - 支持接口`NovaAttachInterface`
- _解决问题_
  - 无
- _特性变更_
  - **ReinstallServerWithoutCloudInit**
    - 请求参数变更
      - `+ os-reinstall.metadata`
  - **ChangeServerOsWithoutCloudInit**
    - 请求参数变更
      - `+ os-change.metadata`
  - **ReinstallServerWithCloudInit**
    - 请求参数变更
      - `+ os-reinstall.metadata.__system__encrypted`
      - `+ os-reinstall.metadata.__system__cmkid`
  - **ChangeServerOsWithCloudInit**
    - 请求参数变更
      - `+ os-change.metadata.__system__encrypted`
      - `+ os-change.metadata.__system__cmkid`
  - **CreateServers**
    - 请求参数变更
      - `+ server.root_volume.extendparam.__system__encrypted`
      - `+ server.root_volume.extendparam.__system__cmkid`
  - **CreatePostPaidServers**
    - 请求参数变更
      - `+ server.root_volume.extendparam.__system__encrypted`
      - `+ server.root_volume.extendparam.__system__cmkid`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持接口`CreateSynthesisTask`、`ShowSynthesisTaskResult`、`CreateCustomPropsTask`、`ShowCustomPropsTaskResult`
- _解决问题_
  - 无
- _特性变更_
  - **CreateCpiTask**
    - 请求参数变更
      - `+ custom_props`
  - **CreateGenerationTask**
    - 请求参数变更
      - `+ custom_props`
  - **CreateOptimizationTask**
    - 请求参数变更
      - `+ custom_props`
  - **ShowCpiTaskResult**
    - 响应参数变更
      - `+ task_data.custom_props`
      - `+ result.custom_props`
  - **ShowGenerationTaskResult**
    - 响应参数变更
      - `+ task_data.custom_props`
      - `+ result.initial_dataset_size`
      - `+ result.strong_constraints`
      - `+ result.weak_constraints`
      - `+ result.binding_site`
      - `+ result.custom_props`
  - **ShowOptimizationTaskResult**
    - 响应参数变更
      - `+ task_data.custom_props`
      - `+ result.strong_constraints`
      - `+ result.weak_constraints`
      - `+ result.binding_site`
      - `+ result.custom_props`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListGaussMySqlInstances**
    - 请求参数变更
      - `+ readonly_private_ip`
      - `+ proxy_ip`
    - 响应参数变更
      - `+ instances.readonly_private_ips`
      - `+ instances.proxy_ips`

### HuaweiCloud SDK Image

- _新增特性_
  - 支持接口`CreateVideoTaggingMediaTask`、`ShowVideoTaggingMediaTask`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListImages**
    - 请求参数变更
      - `+ __imagetype: enum value [market]`

### HuaweiCloud SDK Live

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateRecordIndex**
    - 响应参数变更
      - `+ width`
      - `- weight`
  - **ListAreaDetail**
    - 请求参数变更
      - `* play_domains: required -> optional`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **UpdateAomMappingRules**
    - 请求参数变更
      - `* body: object<AomMappingRequestInfo> -> object<UpdateAomMappingRequest>`

### HuaweiCloud SDK MPC

- _新增特性_
  - 支持接口`ListEditingJobs`、`CreateEditingJobs`、`DeleteEditingJobs`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OSM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListOrderIncident**
    - 请求参数变更
      - `+ xCustomerId`
    - 响应参数变更
      - `* incidentInfoList.incidentTypeName: object -> string`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`UpdatePostgresqlDbUserComment`、`UpdatePostgresqlDatabase`、`DeletePostgresqlDbUser`、`DeletePostgresqlDatabase`
- _解决问题_
  - 无
- _特性变更_
  - **CreatePostgresqlDatabase**
    - 请求参数变更
      - `+ comment`
  - **CreatePostgresqlDbUser**
    - 请求参数变更
      - `+ comment`
  - **ListPostgresqlDatabases**
    - 响应参数变更
      - `+ databases.comment`
  - **ListPostgresqlDbUserPaginated**
    - 响应参数变更
      - `+ users.comment`

### HuaweiCloud SDK RMS

- _新增特性_
  - 支持接口`ShowAggregatePolicyStateComplianceSummary`、`ListAggregateComplianceByPolicyAssignment`、`ShowAggregateComplianceDetailsByPolicyAssignment`、`ShowAggregatePolicyAssignmentDetail`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK SFSTurbo

- _新增特性_
  - 支持以下接口：
    - `ShowFsDirQuota`
    - `UpdateFsDirQuota`
    - `CreateFsDirQuota`
    - `DeleteFsDirQuota`
    - `ShowFsDir`
    - `CreateFsDir`
    - `DeleteFsDir`
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
  - **RunSqlConversion**
    - 请求参数变更
      - `+ target_db_type: enum value [GaussDB Primary/Standby]`
  - **ConfirmTargetDbType**
    - 请求参数变更
      - `- target_db_type: enum value [RDS for MySQL,GaussDB(for MySQL),RDS for PostgreSQL]`
      - `- target_db_version: enum value [5.7,8.0,11,Enhanced Edition]`

# 3.1.38 2023-04-27

### HuaweiCloud SDK MSGSMS

- _新增特性_
  - 支持消息&短信服务
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
  - **ListResourceUnderNode**
    - 请求参数变更
      - `+ marker`
      - `- maker`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDomainFullConfig**
    - 响应参数变更
      - `+ configs.ipv6_accelerate`
      - `+ configs.origin_range_status`

### HuaweiCloud SDK CFW

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListIpsProtectModeUsingPost**
    - 响应参数变更
      - `+ data`
      - `- object_id`
      - `- status`

### HuaweiCloud SDK CSMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListResourceInstances**
    - 响应参数变更
      - `+ resources.sys_tags`

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`ResetPassword`、`UpdateInstanceBandwidth`、`ListConfigTemplates`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DLI

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateBatchJob**
    - 请求参数变更
      - `+ catalog_name`
  - **ShowJobTemplate**
    - 响应参数变更
      - `+ body.catalog_name`
  - **ListJobTemplates**
    - 响应参数变更
      - `+ templates.body.catalog_name`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持以下接口：
    - `ListIamUsers`
    - `ListIamGroups`
    - `ListIamGroupUsers`
    - `ListScaleOutPolicy`
    - `CreateScaleOutPolicy`
    - `ShowScaleOutPolicy`
    - `UpdateScaleOutPolicy`
    - `DeleteScaleOutPolicy`
    - `StartScaleOutPolicy`
    - `StopScaleOutPolicy`
    - `ShowScaleInPolicy`
    - `UpdateScaleInPolicy`
    - `InstallNextflow`
    - `ShowNextflow`
    - `UninstallNextflow`
    - `CleanNextflowCache`
    - `ListNextflowVersion`
    - `ListNextflowJob`
    - `CreateNextflowJob`
    - `ShowNextflowJob`
    - `DeleteNextflowJob`
    - `RetryNextflowJob`
    - `ShowNextflowJobLog`
    - `StopNextflowJob`
    - `ShowNextflowJobReports`
    - `ListNextflowTask`
    - `ShowNextflowTaskDetail`
    - `ShowNextflowTaskLog`
    - `ListNextflowWorkflow`
    - `CreateNextflowWorkflow`
    - `ShowNextflowWorkflow`
    - `UpdateNextflowWorkflow`
    - `DeleteNextflowWorkflow`
- _解决问题_
  - 无
- _特性变更_
  - **PublishData**
    - 响应参数变更
      - `+ id`
      - `- asset_id`
  - **PublishImage**
    - 响应参数变更
      - `+ id`
      - `- asset_id`
  - **PublishApp**
    - 响应参数变更
      - `+ id`
      - `- asset_id`
  - **PublishWorkflow**
    - 响应参数变更
      - `+ id`
      - `- asset_id`
  - **ListImageTag**
    - 响应参数变更
      - `+ tags.path`
  - **CreateApp**
    - 请求参数变更
      - `* body: object<AppDto> -> object<AppReq>`
  - **UpdateApp**
    - 请求参数变更
      - `* body: object<AppDto> -> object<AppReq>`
  - **ListData**
    - 响应参数变更
      - `- path`
      - `- allowed_operate`
      - `- size`
      - `- create_time`
      - `- name`
      - `- download_url`
      - `- deletable`
      - `- type`
      - `- content`
      - `- datas.content`
      - `- datas.download_url`
      - `* datas: list<DataRsp> -> list<DataSummaryRsp>`
  - **ListObsBucketObject**
    - 请求参数变更
      - `+ search_key`

### HuaweiCloud SDK Image

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`RunQueryCustomTags`、`RunDeleteCustomTags`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateInstanceByEngine**
    - 请求参数变更
      - `+ kafka_security_protocol`
      - `+ sasl_enabled_mechanisms`
  - **ShowInstance**
    - 响应参数变更
      - `+ kafka_security_protocol`
      - `+ sasl_enabled_mechanisms: enum value [PLAIN,SCRAM-SHA-512]`
  - **CreatePostPaidInstance**
    - 请求参数变更
      - `+ kafka_security_protocol`
      - `+ sasl_enabled_mechanisms: enum value [PLAIN,SCRAM-SHA-512]`
  - **ListInstances**
    - 响应参数变更
      - `+ kafka_security_protocol`
      - `+ instances.kafka_security_protocol`
      - `+ instances.sasl_enabled_mechanisms: enum value [PLAIN,SCRAM-SHA-512]`

### HuaweiCloud SDK KMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListKeys**
    - 响应参数变更
      - `+ key_details.partition_type`
  - **ListKeyDetail**
    - 响应参数变更
      - `+ key_info.partition_type`
  - **ListRetirableGrants**
    - 响应参数变更
      - `+ total`
  - **ListKmsByTags**
    - 响应参数变更
      - `+ resources.resource_detail.partition_type`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListLogHistogram**
    - 请求参数变更
      - `+ is_iterative`
    - 响应参数变更
      - `+ isQueryComplete`
  - **Createfavorite**
    - 响应参数变更
      - `* create_time: string -> int64`
  - **ListLogStream**
    - 响应参数变更
      - `+ log_streams.is_favorite`
  - **ListLogs**
    - 请求参数变更
      - `+ is_iterative`
    - 响应参数变更
      - `+ isQueryComplete`
  - **UpdateStructTemplate**
    - 请求参数变更
      - `* rule: list<rule> -> object<rule>`
  - **CreateStructTemplate**
    - 请求参数变更
      - `* rule: list<rule> -> object<rule>`
  - **ListHistorySql**
    - 请求参数变更
      - `+ log_group_id`
      - `+ log_stream_id`

### HuaweiCloud SDK Organizations

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreatePolicy**
    - 请求参数变更
      - `+ type: enum value [tag_policy]`
  - **EnablePolicyType**
    - 请求参数变更
      - `+ policy_type: enum value [tag_policy]`
  - **DisablePolicyType**
    - 请求参数变更
      - `+ policy_type: enum value [tag_policy]`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowConsumerListOrDetails**
    - 响应参数变更
      - `* total: int64 -> int32`

### HuaweiCloud SDK SMS

- _新增特性_
  - 支持以下接口：
    - `ListApiVersion`
    - `ShowApiVersion`
    - `ShowConfig`
    - `UpdateNetworkCheckInfo`
    - `ShowConfigSetting`
    - `UploadSpecialConfigurationSetting`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.37 2023-04-20

### HuaweiCloud SDK AOM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListAllVersionByVersionId**
    - 响应参数变更
      - `+ elements.job_reference_number`
      - `+ elements.job_reference_name`
      - `- elements.reference_number`
      - `- elements.script_reference`

### HuaweiCloud SDK AOS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **GetStackTemplate**
    - 请求参数变更
      - `- executor`
  - **ListStackEvents**
    - 请求参数变更
      - `- executor`
  - **ListStackOutputs**
    - 请求参数变更
      - `- executor`
  - **DeleteStack**
    - 请求参数变更
      - `- executor`
  - **DeleteExecutionPlan**
    - 请求参数变更
      - `- executor`
  - **ApplyExecutionPlan**
    - 请求参数变更
      - `- executor`
  - **GetExecutionPlan**
    - 请求参数变更
      - `- executor`
  - **ListStackResources**
    - 请求参数变更
      - `- executor`
  - **ListExecutionPlans**
    - 请求参数变更
      - `- executor`
  - **CreateExecutionPlan**
    - 请求参数变更
      - `- executor`
  - **GetExecutionPlanMetadata**
    - 请求参数变更
      - `- executor`
  - **GetStackMetadata**
    - 请求参数变更
      - `- executor`
  - **ListStacks**
    - 请求参数变更
      - `- executor`
  - **CreateStack**
    - 请求参数变更
      - `- executor`
  - **DeployStack**
    - 请求参数变更
      - `- executor`

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListCustomerselfResourceRecordDetails**
    - 响应参数变更
      - `+ monthly_records.pre_order_id`
      - `+ monthly_records.az_code_infos`

### HuaweiCloud SDK CBS

- _新增特性_
  - 支持以下接口：
    - `ExecuteGetVideosList`
    - `ExecuteCreateVideo`
    - `ExecuteUpdateVideoById`
    - `ExecuteDeleteVideoById`
    - `ExecuteGetVideoInfoById`
    - `ExecuteUpdateVideoInfoById`
    - `ExecuteComposeVideo`
    - `ExecuteComposeVideoOndemand`
    - `ExecuteGetCharacters`
    - `ExecuteGetCharacterInfoById`
    - `ExecuteUploadPpt`
    - `ExecuteUploadImage`
    - `ExecuteUpdateImageName`
    - `ExecuteDeleteimageById`
    - `ExecuteGetImagesList`
    - `ExecutePostCreateImages`
    - `ExecuteGetFramsListByImagesId`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持接口`ShowDomainFullConfig`、`UpdateDomainFullConfig`
- _解决问题_
  - 无
- _特性变更_
  - **ShowDomainFullConfig**
    - 响应参数变更
      - `+ configs.origin_follow302_status`
      - `+ configs.cache_rules`
      - `+ configs.ip_filter`
      - `+ configs.referer`
      - `+ configs.force_redirect.redirect_code`
  - **UpdateDomainFullConfig**
    - 请求参数变更
      - `+ configs.origin_follow302_status`
      - `+ configs.cache_rules`
      - `+ configs.ip_filter`
      - `+ configs.referer`
      - `+ configs.force_redirect.redirect_code`

### HuaweiCloud SDK CloudPipeline

- _新增特性_
  - 支持接口`ListPipelineTemplates`、`ShowPipelineTemplateDetail`、`CreatePipelineByTemplateId`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListLogsJob**
    - 请求参数变更
      - `+ start`
      - `+ limit`
  - **ShowVpcepConnection**
    - 请求参数变更
      - `+ start`
      - `+ limit`
  - **ListYmlsJob**
    - 请求参数变更
      - `+ start`
      - `+ limit`

### HuaweiCloud SDK DCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateRedislogDownloadLink**
    - 响应参数变更
      - `+ backup_id`

### HuaweiCloud SDK DDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateConfiguration**
    - 响应参数变更
      - `+ configuration`
      - `- datastore_version`
      - `- created`
      - `- name`
      - `- description`
      - `- id`
      - `- datastore_name`
      - `- updated`

### HuaweiCloud SDK DLF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowJob**
    - 响应参数变更
      - `+ lastUpdateUser`
      - `+ id`
  - **UpdateJob**
    - 请求参数变更
      - `+ lastUpdateUser`
      - `+ id`
  - **CreateJob**
    - 请求参数变更
      - `+ lastUpdateUser`
      - `+ id`
  - **ListJobs**
    - 响应参数变更
      - `+ lastUpdateUser`
      - `+ id`
      - `+ jobs.id`
      - `+ jobs.lastUpdateUser`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowJobList**
    - 响应参数变更
      - `+ jobs.job_action`
      - `+ jobs.children.job_action`
  - **BatchListJobDetails**
    - 响应参数变更
      - `+ results.original_job_direction`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ImportFunction**
    - 响应参数变更
      - `+ gpu_memory`
      - `+ func_vpc.security_groups`
  - **ListFunctions**
    - 响应参数变更
      - `+ functions.gpu_memory`
      - `+ functions.is_bridge_function`
      - `+ functions.bind_bridge_funcUrns`
  - **CreateFunction**
    - 请求参数变更
      - `+ gpu_memory`
      - `+ log_config`
      - `+ network_controller`
      - `+ func_vpc.security_groups`
    - 响应参数变更
      - `+ gpu_memory`
      - `+ func_vpc.security_groups`
  - **ShowFunctionConfig**
    - 响应参数变更
      - `+ gpu_memory`
      - `+ ephemeral_storage`
      - `+ func_vpc.security_groups`
  - **UpdateFunctionConfig**
    - 请求参数变更
      - `+ gpu_memory`
      - `+ ephemeral_storage`
      - `+ log_config`
      - `+ network_controller`
      - `+ restore_hook_handler`
      - `+ restore_hook_timeout`
      - `+ func_vpc.security_groups`
    - 响应参数变更
      - `+ gpu_memory`
      - `+ ephemeral_storage`
      - `+ func_vpc.security_groups`
  - **UpdateFunctionMaxInstanceConfig**
    - 响应参数变更
      - `+ func_vpc.security_groups`
  - **CreateFunctionVersion**
    - 响应参数变更
      - `+ func_vpc.security_groups`

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateDbUser**
    - 请求参数变更
      - `+ is_login_only`

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListSimCards**
    - 请求参数变更
      - `+ price_plan_id`

### HuaweiCloud SDK Image

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `CreateVideoTranslateTask`
    - `ShowVideoTranslateTask`
    - `CreateImageTranslateTask`
    - `ShowImageTranslateTask`
    - `CreateVideoCoverAnalysisTask`
    - `ShowVideoCoverAnalysisTask`
    - `CreateVideoSummarizationAnalysisTask`
    - `ShowVideoSummarizationAnalysisTask`
    - `CreateVideoShotSplitTask`
    - `ShowVideoShotSplitTask`
  - **CreateImageHighresolutionMattingTask**
    - 请求参数变更
      - `- input.data.bucket`
      - `- input.data.path`
  - **ShowImageHighresolutionMattingTask**
    - 响应参数变更
      - `- input.data.bucket`
      - `- input.data.path`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 支持接口`BroadcastMessage`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 支持以下接口：
    - `BatchListOtTemplates`
    - `AddOtTemplates`
    - `ShowOtTemplate`
    - `DeleteOtTemplate`
    - `AddGeneralOtTemplate`
    - `UpdateModuleState`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Meeting

- _新增特性_
  - 支持接口`BatchShowUserDetails`
- _解决问题_
  - 无
- _特性变更_
  - **UpdateWebinar**
    - 请求参数变更
      - `+ enableRecording`
  - **CreateWebinar**
    - 请求参数变更
      - `+ enableRecording`
    - 响应参数变更
      - `+ enableRecording`
  - **ShowWebinar**
    - 响应参数变更
      - `+ enableRecording`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RecognizeDriverLicense**
    - 响应参数变更
      - `+ result.front`
      - `+ result.back`
  - **RecognizeThailandIdcard**
    - 响应参数变更
      - `+ result.type`
      - `+ result.name_en`
      - `+ result.ref_number`
      - `+ result.confidence.name_en`
      - `+ result.confidence.ref_number`

### HuaweiCloud SDK RDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListRestoreTimes**
    - 响应参数变更
      - `* restore_time.start_time: int32 -> int64`
      - `* restore_time.end_time: int32 -> int64`
  - **ListOffSiteRestoreTimes**
    - 响应参数变更
      - `* restore_time.start_time: int32 -> int64`
      - `* restore_time.end_time: int32 -> int64`
  - **RestoreToExistingInstance**
    - 请求参数变更
      - `* source.restore_time: int32 -> int64`
  - **RestoreExistInstance**
    - 请求参数变更
      - `* source.restore_time: int32 -> int64`
  - **CreateInstance**
    - 请求参数变更
      - `* restore_point.restore_time: int32 -> int64`
    - 响应参数变更
      - `* instance.restore_point.restore_time: int32 -> int64`
  - **CreateRestoreInstance**
    - 请求参数变更
      - `* restore_point.restore_time: int32 -> int64`
    - 响应参数变更
      - `* instance.restore_point.restore_time: int32 -> int64`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 支持接口`ShowConsumerConnections`
- _解决问题_
  - 无
- _特性变更_
  - **ShowConsumerListOrDetails**
    - 响应参数变更
      - `+ total`
      - `+ brokers`
  - **ShowUser**
    - 响应参数变更
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
  - **UpdateUser**
    - 请求参数变更
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
    - 响应参数变更
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
  - **UpdateInstance**
    - 请求参数变更
      - `+ enable_publicip`
      - `+ publicip_id`
  - **CreateUser**
    - 请求参数变更
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
    - 响应参数变更
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
  - **ListUser**
    - 响应参数变更
      - `- users.default_group_perm: enum value [PUB,PUB|SUB]`
      - `- users.group_perms.perm: enum value [PUB,PUB|SUB]`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListVpcsByTags**
    - 响应参数变更
      - `+ resources.resource_detail`
      - `- resources.resouce_detail`
  - **ListSubnetsByTags**
    - 响应参数变更
      - `+ resources.resource_detail`
      - `- resources.resouce_detail`
  - **UpdateRouteTable**
    - 请求参数变更
      - `+ routetable.routes.add`
      - `+ routetable.routes.mod`
      - `+ routetable.routes.del`
      - `* routetable.routes: map<string, list<RouteTableRoute>> -> object<RouteTableRouteAction>`

### HuaweiCloud SDK VPCEP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListServiceDescribeDetails**
    - 响应参数变更
      - `+ public_border_group`
  - **ListServiceDetails**
    - 响应参数变更
      - `+ enable_policy`
      - `+ tcp_proxy: enum value [proxy_vni]`
  - **UpdateEndpointService**
    - 请求参数变更
      - `+ tcp_proxy`
    - 响应参数变更
      - `+ enable_policy`
      - `+ tcp_proxy: enum value [proxy_vni]`
  - **ListEndpointInfoDetails**
    - 响应参数变更
      - `+ endpoint_pool_id`
      - `+ public_border_group`
  - **CreateEndpointService**
    - 请求参数变更
      - `+ enable_policy`
      - `+ tcp_proxy: enum value [proxy_vni]`
    - 响应参数变更
      - `+ enable_policy`
      - `+ tcp_proxy: enum value [proxy_vni]`
  - **ListEndpointService**
    - 响应参数变更
      - `+ endpoint_services.enable_policy`
      - `+ endpoint_services.tcp_proxy: enum value [proxy_vni]`
  - **CreateEndpoint**
    - 响应参数变更
      - `+ endpoint_pool_id`
      - `+ public_border_group`
      - `+ ip`

# 3.1.36 2023-04-13

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListCustomerselfResourceRecordDetails**
    - 响应参数变更
      - `+ monthly_records.pre_order_id`
      - `+ monthly_records.az_code_infos`

### HuaweiCloud SDK Cloudtest

- _新增特性_
  - 支持接口`ShowReport`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CPTS

- _新增特性_
  - 支持接口`UpdateAgentHealthStatus`、`ShowAgentConfig`
- _解决问题_
  - 无
- _特性变更_
  - **ShowReport**
    - 响应参数变更
      - `* result.brokens.commonTimestamps: list<integer> -> list<string>`

### HuaweiCloud SDK EVS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowVolume**
    - 响应参数变更
      - `+ volume.iops`
      - `+ volume.throughput`
  - **ListVolumes**
    - 响应参数变更
      - `+ volumes.iops`
      - `+ volumes.throughput`

### HuaweiCloud SDK IES

- _新增特性_
  - 支持接口`ListRacks`、`ShowRack`、`ListStoragePools`、`ShowStoragePool`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Image

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `CreateVideoSynthesisTask`
    - `ShowVideoSynthesisTask`
    - `CreateImageToVideoTask`
    - `ShowImageToVideoTask`
    - `CreateVideoCuttingTask`
    - `ShowVideoCuttingTask`
    - `RunImageWisedesignCrop`
    - `RunImageWisedesignInpainting`
  - **RunImageTagging**
    - 响应参数变更
      - `+ result.tags.instances.bounding_box.width`
      - `+ result.tags.instances.bounding_box.height`
      - `+ result.tags.instances.bounding_box.top_left_x`
      - `+ result.tags.instances.bounding_box.top_left_y`
      - `* result.tags.instances.bounding_box: object -> object<ImageTaggingBoundingBox>`
  - **RunImageMediaTagging**
    - 响应参数变更
      - `+ result.tags.instances.bounding_box.width`
      - `+ result.tags.instances.bounding_box.height`
      - `+ result.tags.instances.bounding_box.top_left_x`
      - `+ result.tags.instances.bounding_box.top_left_y`
      - `* result.tags.instances.bounding_box: object -> object<BoundingBox>`
      - `* result.tags.instances: list<ImageTaggingInstance> -> list<ImageMediaTaggingInstance>`
  - **RunImageMediaTaggingDet**
    - 响应参数变更
      - `+ result.tags.instances.bounding_box.width`
      - `+ result.tags.instances.bounding_box.height`
      - `+ result.tags.instances.bounding_box.top_left_x`
      - `+ result.tags.instances.bounding_box.top_left_y`
      - `* result.tags.instances.bounding_box: object -> object<BoundingBox>`
  - **ShowVideoShotSplitTask**
    - 响应参数变更
      - `- state: enum value [SUCCEEDED,FAILED,RUNNING]`
  - **CreateVideoTranslateTask**
    - 请求参数变更
      - `* body: object<VideoTranslateRequestBody> -> object<CreateVideoTranslateTaskRequestBody>`
  - **CreateImageHighresolutionMattingTask**
    - 请求参数变更
      - `* input.data: list<TaskInputData> -> list<ImageHighresolutionMattingInputData>`
      - `* input: object<TaskInput> -> object<ImageHighresolutionMattingInput>`
  - **ShowImageHighresolutionMattingTask**
    - 响应参数变更
      - `* input.data: list<TaskInputData> -> list<ImageHighresolutionMattingInputData>`
      - `* input: object<TaskInput> -> object<ImageHighresolutionMattingInput>`
  - **CreateImageTranslateTask**
    - 请求参数变更
      - `* input.data: list<TaskInputData> -> list<ImageTranslateTaskInputData>`
      - `* input: object<TaskInput> -> object<ImageTranslateTaskInput>`
      - `* body: object<ImageTranslateRequestBody> -> object<CreateImageTranslateRequestBody>`
  - **ShowImageTranslateTask**
    - 响应参数变更
      - `* input.data: list<TaskInputData> -> list<ImageTranslateTaskInputData>`
      - `* input: object<TaskInput> -> object<ImageTranslateTaskInput>`
  - **CreateVideoCoverAnalysisTask**
    - 请求参数变更
      - `* input.data: list<TaskInputData> -> list<VideoCoverAnalysisTaskInputData>`
      - `* input: object<TaskInput> -> object<VideoCoverAnalysisTaskInput>`
      - `* body: object<VideoCoverAnalysisCreateTaskRequestBody> -> object<CreateVideoCoverAnalysisTaskRequestBody>`
  - **ShowVideoCoverAnalysisTask**
    - 响应参数变更
      - `* input.data: list<TaskInputData> -> list<VideoCoverAnalysisTaskInputData>`
      - `* input: object<TaskInput> -> object<VideoCoverAnalysisTaskInput>`
  - **CreateVideoSummarizationAnalysisTask**
    - 请求参数变更
      - `* input.data: list<TaskInputData> -> list<VideoSummarizationTaskInputData>`
      - `* input: object<TaskInput> -> object<VideoSummarizationTaskInput>`
      - `* body: object<VideoSummarizationCreateTaskRequestBody> -> object<CreateVideoSummarizationTaskRequestBody>`
  - **ShowVideoSummarizationAnalysisTask**
    - 响应参数变更
      - `* input.data: list<TaskInputData> -> list<VideoSummarizationTaskInputData>`
      - `* input: object<TaskInput> -> object<VideoSummarizationTaskInput>`
  - **CreateVideoObjectMaskingTask**
    - 请求参数变更
      - `* input.data: list<TaskInputData> -> list<ObjectMaskingTaskInputData>`
      - `* input: object<TaskInput> -> object<ObjectMaskingTaskInput>`
  - **ShowVideoObjectMaskingTask**
    - 响应参数变更
      - `* input.data: list<TaskInputData> -> list<ObjectMaskingTaskInputData>`
      - `* input: object<TaskInput> -> object<ObjectMaskingTaskInput>`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`BatchDeleteGroup`
- _解决问题_
  - 无
- _特性变更_
  - **ResizeEngineInstance**
    - 请求参数变更
      - `+ publicip_id`

### HuaweiCloud SDK Live

- _新增特性_
  - 支持以下接口：
    - `ListSnapshotConfigs`
    - `UpdateSnapshotConfig`
    - `CreateSnapshotConfig`
    - `DeleteSnapshotConfig`
    - `ShowDomainKeyChain`
    - `UpdateDomainKeyChain`
    - `DeleteDomainKeyChain`
    - `ShowDomainHttpsCert`
    - `UpdateDomainHttpsCert`
    - `DeleteDomainHttpsCert`
    - `UpdateObsBucketAuthorityPublic`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OSM

- _新增特性_
  - 支持接口`ListDiagnoseResources`、`ListOrderIncident`
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
  - **RecognizeShortAudio**
    - 请求参数变更
      - `+ config.property: enum value [english_8k_common,english_16k_common]`
  - **CollectTranscriberJob**
    - 响应参数变更
      - `+ job_id`

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持接口`CreateCloudWafPostPaidResource`、`DeleteCloudWafPostPaidResource`
- _解决问题_
  - 无
- _特性变更_
  - **ListCustomRules**
    - 响应参数变更
      - `+ items.name`

# 3.1.35 2023-04-06

### HuaweiCloud SDK CCM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ExportCertificate**
    - 请求参数变更
      - `+ password`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateRefreshTasks**
    - 请求参数变更
      - `+ refresh_task.mode`

### HuaweiCloud SDK CES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListAlarmHistories**
    - 响应参数变更
      - `+ alarm_histories.type: enum value [DNSHealthCheck,RESOURCE_GROUP,MULTI_INSTANCE,ALL_INSTANCE]`
  - **ListAlarmRules**
    - 响应参数变更
      - `+ alarms.type: enum value [EVENT.SYS,EVENT.CUSTOM,DNSHealthCheck,RESOURCE_GROUP,MULTI_INSTANCE,ALL_INSTANCE]`
  - **CreateAlarmRules**
    - 请求参数变更
      - `+ type: enum value [EVENT.SYS,EVENT.CUSTOM,DNSHealthCheck,RESOURCE_GROUP,MULTI_INSTANCE,ALL_INSTANCE]`

### HuaweiCloud SDK DeH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListServersDedicatedHost**
    - 响应参数变更
      - `- servers.addresses.vpc_id`
      - `* servers.addresses: object<RespAddresses> -> map<string, list<RespAddr>>`

### HuaweiCloud SDK GSL

- _新增特性_
  - 支持接口`SendSms`、`ListSmsDetails`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Image

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`CreateTextToImageTask`、`ShowTextToImageTask`、`CreateImageVariationTask`、`ShowImageVariationTask`

### HuaweiCloud SDK MRS

- _新增特性_
  - 支持接口`RunJobFlow`
- _解决问题_
  - 无
- _特性变更_
  - **CreateCluster**
    - 请求参数变更
      - `+ log_uri`
      - `+ component_configs`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **RecognizeFinancialStatement**
    - 请求参数变更
      - `+ return_rectification_matrix`
    - 响应参数变更
      - `+ result.rectification_matrix`

### HuaweiCloud SDK RAM

- _新增特性_
  - 支持接口`ListResourceShareTags`、`ListResourceSharesByTags`、`SearchResourceShareCountByTags`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.34 2023-03-30

### HuaweiCloud SDK BSS

- _新增特性_
  - 支持接口`ListRenewRateOnPeriod`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 支持接口`ListRenewRateOnPeriod`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListBackups**
    - 请求参数变更
      - `+ incremental`
  - **ListVault**
    - 响应参数变更
      - `+ vaults.billing.object_type: enum value [vmware,rds,file]`
  - **CreateVault**
    - 请求参数变更
      - `+ vault.billing.object_type: enum value [vmware,rds,file]`
    - 响应参数变更
      - `+ vault.billing.object_type: enum value [vmware,rds,file]`
  - **ShowVault**
    - 响应参数变更
      - `+ vault.billing.object_type: enum value [vmware,rds,file]`
  - **UpdateVault**
    - 响应参数变更
      - `+ vault.billing.object_type: enum value [vmware,rds,file]`
  - **ShowVaultResourceInstances**
    - 响应参数变更
      - `+ resources.resource_detail.billing.object_type: enum value [vmware,rds,file]`
  - **ListProtectable**
    - 响应参数变更
      - `+ instances.protectable.vault.billing.object_type: enum value [vmware,rds,file]`
  - **ShowProtectable**
    - 响应参数变更
      - `+ instance.protectable.vault.billing.object_type: enum value [vmware,rds,file]`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`CreateApply`、`CreateEvent`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **CreateAutoCreatePolicy**
    - 请求参数变更
      - `+ indices`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListUsers**
    - 响应参数变更
      - `* user_list.privileges: list<string> -> string`
  - **BatchUpdateUser**
    - 响应参数变更
      - `* results.user_list.privileges: list<string> -> string`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持接口`ShowAdmetProperties`
- _解决问题_
  - 无
- _特性变更_
  - **CreateGenerationTask**
    - 请求参数变更
      - `- strong_constraints.requirement`
  - **CreateOptimizationTask**
    - 请求参数变更
      - `- strong_constraints.requirement`
  - **ShowGenerationTaskResult**
    - 响应参数变更
      - `- task_data.strong_constraints.requirement`
  - **ShowOptimizationTaskResult**
    - 响应参数变更
      - `- task_data.strong_constraints.requirement`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListOtaPackageInfo**
    - 请求参数变更
      - `- Sp-Auth-Token`
  - **CreateOtaPackage**
    - 请求参数变更
      - `- Sp-Auth-Token`
  - **DeleteOtaPackage**
    - 请求参数变更
      - `- Sp-Auth-Token`
  - **ShowOtaPackage**
    - 请求参数变更
      - `- Sp-Auth-Token`
  - **ShowRuleAction**
    - 响应参数变更
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
  - **UpdateRuleAction**
    - 请求参数变更
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
    - 响应参数变更
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
  - **CreateRuleAction**
    - 请求参数变更
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
    - 响应参数变更
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
  - **ListRuleActions**
    - 响应参数变更
      - `+ actions.channel_detail.http_forwarding.signature_enable`
      - `+ actions.channel_detail.http_forwarding.token`
  - **ShowRule**
    - 响应参数变更
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
  - **UpdateRule**
    - 请求参数变更
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
    - 响应参数变更
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
  - **CreateRule**
    - 请求参数变更
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
    - 响应参数变更
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
  - **ListRules**
    - 响应参数变更
      - `+ rules.actions.device_alarm.dimension`
      - `+ rules.condition_group.conditions.device_linkage_status_condition`
      - `+ rules.condition_group.conditions.device_property_condition.filters.in_values`

### HuaweiCloud SDK NAT

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListPrivateDnats**
    - 响应参数变更
      - `* page_info.current_count: number -> integer`
  - **ListPrivateNats**
    - 响应参数变更
      - `* page_info.current_count: number -> integer`
  - **ListPrivateSnats**
    - 响应参数变更
      - `* page_info.current_count: number -> integer`
  - **ListTransitIps**
    - 响应参数变更
      - `* page_info.current_count: number -> integer`

### HuaweiCloud SDK Organizations

- _新增特性_
  - 支持以下接口：
    - `ShowCreateAccountStatus`
    - `ShowEffectivePolicies`
    - `ListTagPolicyServices`
    - `ListTagResources`
    - `CreateTagResource`
    - `DeleteTagResource`
    - `ListResourceInstances`
    - `ShowResourceInstancesCount`
    - `ListResourceTags`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OSM

- _新增特性_
  - 支持接口`ShowConfiguration`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RAM

- _新增特性_
  - 支持接口`BatchCreateResourceShareTags`、`BatchDeleteResourceShareTags`
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
  - **PublishAssetFromObs**
    - 请求参数变更
      - `+ video_type: enum value [RMVB,WEBM]`

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持接口`ShowValueList`、`ShowPrivacyRule`、`ShowAntitamperRule`、`ShowWhiteBlackIpRule`
- _解决问题_
  - 无
- _特性变更_
  - **ShowCcRule**
    - 响应参数变更
      - `+ name`
      - `* mode: number -> int32`
  - **UpdateCcRule**
    - 请求参数变更
      - `+ name`
    - 响应参数变更
      - `+ name`
      - `* mode: number -> int32`
  - **DeleteCcRule**
    - 响应参数变更
      - `+ name`
      - `* mode: number -> int32`
  - **ShowCustomRule**
    - 响应参数变更
      - `+ time`
  - **UpdateCustomRule**
    - 响应参数变更
      - `+ time`
  - **DeleteCustomRule**
    - 响应参数变更
      - `+ time`
  - **ListAntileakageRules**
    - 响应参数变更
      - `+ items.description`
  - **CreateCcRule**
    - 请求参数变更
      - `+ name`
    - 响应参数变更
      - `+ name`
      - `* mode: number -> int32`
  - **ListCcRules**
    - 响应参数变更
      - `+ items.name`
  - **CreateCustomRule**
    - 响应参数变更
      - `+ time`
  - **ListCustomRules**
    - 响应参数变更
      - `+ items.time`

# 3.1.33 2023-03-23

### HuaweiCloud SDK CCE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowNode**
    - 响应参数变更
      - `+ spec.extendParam.agency_name`
  - **UpdateNode**
    - 响应参数变更
      - `+ spec.extendParam.agency_name`
  - **DeleteNode**
    - 响应参数变更
      - `+ spec.extendParam.agency_name`
  - **CreateNode**
    - 请求参数变更
      - `+ spec.extendParam.agency_name`
    - 响应参数变更
      - `+ spec.extendParam.agency_name`
  - **ListNodes**
    - 响应参数变更
      - `+ items.spec.extendParam.agency_name`
  - **ShowNodePool**
    - 响应参数变更
      - `+ spec.nodeTemplate.extendParam.agency_name`
  - **UpdateNodePool**
    - 响应参数变更
      - `+ spec.nodeTemplate.extendParam.agency_name`
  - **DeleteNodePool**
    - 响应参数变更
      - `+ spec.nodeTemplate.extendParam.agency_name`
  - **CreateNodePool**
    - 请求参数变更
      - `+ spec.nodeTemplate.extendParam.agency_name`
    - 响应参数变更
      - `+ spec.nodeTemplate.extendParam.agency_name`
  - **ListNodePools**
    - 响应参数变更
      - `+ items.spec.nodeTemplate.extendParam.agency_name`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowDomainDetailByName**
    - 响应参数变更
      - `- domain.banned_reason`
      - `- domain.locked_reason`
      - `- domain.enterprise_project_id`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`UploadFilePublisher`、`ShowExtensionTestingResult`、`PublishExtension`
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
  - **CreateMigrationTask**
    - 请求参数变更
      - `+ backup_files.file_source: enum value [backup_record]`
  - **ShowMigrationTask**
    - 响应参数变更
      - `+ backup_files.file_source: enum value [backup_record]`
  - **StopMigrationTask**
    - 响应参数变更
      - `+ backup_files.file_source: enum value [backup_record]`

### HuaweiCloud SDK DDS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowReplSetName**
    - 响应参数变更
      - `+ name`
  - **UpdateReplSetName**
    - 响应参数变更
      - `+ job_id`

### HuaweiCloud SDK DLI

- _新增特性_
  - 支持以下接口：
    - `AuthorizeResource`
    - `ListAuthInfo`
    - `UpdateAuthInfo`
    - `CreateAuthInfo`
    - `DeleteAuthInfo`
    - `DeleteEnhancedConnectionRoutes`
    - `CreateEnhancedConnectionRoutes`
    - `ListElasticResourcePoolScaleRecords`
    - `ShowSqlTemplates`
    - `CreateSqlTemplates`
    - `ShowSqlSampleTemplates`
    - `UpdateSqlTemplates`
    - `DeleteSqlTemplates`
    - `ListJobTemplates`
    - `CreateJobTemplates`
    - `ShowJobTemplate`
    - `UpdateJobTemplates`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`CreateDownloadJob`
  - **ShowBatchInfo**
    - 响应参数变更
      - `* appId: list<string> -> string`
  - **ChangeQueuePlan**
    - 请求参数变更
      - `+ repeat_day: enum value [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY]`
      - `- repeat_day: enum value [ MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]`
  - **DisassociateConnectionQueue**
    - 请求参数变更
      - `+ elastic_resource_pools`
      - `- queues: enum value [q1,q2]`
  - **AssociateConnectionQueue**
    - 请求参数变更
      - `+ elastic_resource_pools`
  - **ListBatches**
    - 响应参数变更
      - `* sessions.appId: list<string> -> string`
  - **CreateBatchJob**
    - 请求参数变更
      - `+ className`
      - `+ pyFiles`
      - `+ driverMemory`
      - `+ driverCores`
      - `+ executorMemory`
      - `+ executorCores`
      - `+ numExecutors`
      - `- class_name`
      - `- python_files`
      - `- driver_memory`
      - `- driver_cores`
      - `- executor_memory`
      - `- executor_cores`
      - `- num_executors`
      - `- catalog_name`
      - `* conf: list<object> -> map<string, object>`
      - `+ feature: enum value [ai,custom]`
      - `- feature: enum value [ ai, custom]`
      - `* body: object<CreateBatchJobReq> -> object<BatchJobInfo>`
    - 响应参数变更
      - `* appId: list<string> -> string`
  - **CreateTable**
    - 请求参数变更
      - `+ tags`
  - **ListQueues**
    - 响应参数变更
      - `* queues: list<ListQueuesRespQueues> -> list<QueueDetails>`
  - **CreateQueuePlan**
    - 请求参数变更
      - `+ repeat_day: enum value [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY]`
      - `- repeat_day: enum value [ MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]`
  - **ListQueuePlans**
    - 响应参数变更
      - `+ plans.repeat_day: enum value [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY]`
      - `- plans.repeat_day: enum value [ MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]`
  - **ShowEnhancedConnection**
    - 响应参数变更
      - `+ elastic_resource_pools`
  - **ListElasticResourcePools**
    - 请求参数变更
      - `+ status: enum value [AVAILABLE,SCALING,CREATING,FAILED]`
      - `+ status: enum value [AVAILABLE，SCALING，CREATING，FAILED]`
  - **CreateFlinkJar**
    - 请求参数变更
      - `* body: object<CreateFlinkdefinedJobsReq> -> object<CreateFlinkJarRequestBody>`
  - **UpdateFlinkJar**
    - 请求参数变更
      - `* body: object<UpdateFlinkdefinedJobsResp> -> object<UpdateFlinkJarRequestBody>`
  - **ListEnhancedConnections**
    - 请求参数变更
      - `* limit: string -> int32`
      - `* offset: string -> int32`
    - 响应参数变更
      - `+ connections.elastic_resource_pools`
  - **CreateFlinkTemplate**
    - 请求参数变更
      - `+ job_type: enum value [flink_sql_job,flink_opensource_sql_job]`
      - `- job_type: enum value [flink_sql_job，flink_opensource_sql_job]`
      - `* body: object<CreateTemplateReq> -> object<CreateFlinkTemplateRequestBody>`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持以下接口：
    - `CreateCpiTask`
    - `ShowCpiTaskResult`
    - `CreateGenerationTask`
    - `ShowGenerationTaskResult`
    - `CreateOptimizationTask`
    - `ShowOptimizationTaskResult`
    - `CreateSearchTask`
    - `ShowSearchTaskResult`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK NAT

- _新增特性_
  - 支持以下接口：
    - `ListPrivateNats`
    - `CreatePrivateNat`
    - `ShowPrivateNat`
    - `UpdatePrivateNat`
    - `DeletePrivateNat`
    - `ListPrivateDnats`
    - `CreatePrivateDnat`
    - `ShowPrivateDnat`
    - `UpdatePrivateDnat`
    - `DeletePrivateDnat`
    - `ListPrivateSnats`
    - `CreatePrivateSnat`
    - `ShowPrivateSnat`
    - `UpdatePrivateSnat`
    - `DeletePrivateSnat`
    - `ListTransitIps`
    - `CreateTransitIp`
    - `ShowTransitIp`
    - `DeleteTransitIp`
    - `ListPrivateNatsByTags`
    - `ListPrivateNatTags`
    - `ShowPrivateNatTags`
    - `CreatePrivateNatTag`
    - `BatchCreateDeletePrivateNatTags`
    - `DeletePrivateNatTag`
    - `ListTransitIpsByTags`
    - `ListTransitIpTags`
    - `ShowTransitIpTags`
    - `CreateTransitIpTag`
    - `BatchCreateDeleteTransitIpTags`
    - `DeleteTransitIpTag`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK Organizations

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
    - `ShowCreateAccountStatus`
    - `ShowEffectivePolicies`
    - `ListTagPolicyServices`
    - `ListTagResources`
    - `CreateTagResource`
    - `DeleteTagResource`
    - `ListResourceInstances`
    - `ShowResourceInstancesCount`
    - `ListResourceTags`
    - `CreateAccount`

### HuaweiCloud SDK RabbitMQ

- _新增特性_
  - 支持接口`ShowEngineInstanceExtendProductInfo`、`ResizeEngineInstance`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK WAF

- _新增特性_
  - 支持以下接口：
    - `ListCcRules`
    - `CreateCcRule`
    - `ShowCcRule`
    - `UpdateCcRule`
    - `DeleteCcRule`
    - `ListCustomRules`
    - `CreateCustomRule`
    - `ShowCustomRule`
    - `UpdateCustomRule`
    - `DeleteCustomRule`
    - `ListAnticrawlerRules`
    - `UpdateAnticrawlerRuleType`
    - `CreateAnticrawlerRule`
    - `ShowAnticrawlerRule`
    - `UpdateAnticrawlerRule`
    - `DeleteAnticrawlerRule`
    - `ListPunishmentRules`
    - `CreatePunishmentRule`
    - `ShowPunishmentRule`
    - `UpdatePunishmentRule`
    - `DeletePunishmentRule`
    - `ListAntileakageRules`
    - `CreateAntileakageRule`
    - `ShowAntileakageRule`
    - `UpdateAntileakageRule`
    - `DeleteAntileakageRule`
    - `UpdateAntiTamperRuleRefresh`
    - `ShowGeoipRule`
    - `ShowIgnoreRule`
    - `UpdateIgnoreRule`
- _解决问题_
  - 无
- _特性变更_
  - **ListHost**
    - 响应参数变更
      - `- items.paid_type: enum value [prePaid]`
  - **DeleteHost**
    - 响应参数变更
      - `- paid_type: enum value [prePaid]`

# 3.1.32 2023-03-16

### HuaweiCloud SDK Organizations

- _新增特性_
  - 支持组织云服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK APIG

- _新增特性_
  - 支持接口`UpdateIngressEipV2`、`AddIngressEipV2`、`RemoveIngressEipV2`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowJobInfos**
    - 响应参数变更
      - `* begin_time: date-time -> string`
      - `* end_time: date-time -> string`
      - `* entities.sub_jobs.begin_time: date-time -> string`
      - `* entities.sub_jobs.end_time: date-time -> string`

### HuaweiCloud SDK CBH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListQuotaStatus**
    - 响应参数变更
      - `* quota: string -> int32`
      - `* eip_quota: string -> int32`
  - **StopCbhInstance**
    - 请求参数变更
      - `- reboot`
  - **ShowNetworkConfiguration**
    - 请求参数变更
      - `+ server_id`
  - **CreateInstanceOrder**
    - 请求参数变更
      - `- end_time`
      - `- relative_resource_id`
      - `- product_infos.available_zone_id`
  - **ChangeInstanceNetwork**
    - 请求参数变更
      - `+ server_id`
  - **ListCbhInstance**
    - 响应参数变更
      - `- instance.is_auto_renew`
  - **CreateInstance**
    - 请求参数变更
      - `- server.image_ref`
      - `- server.name`
      - `- server.personality`
      - `- server.user_data`
      - `- server.admin_password`
      - `- server.key_name`
      - `- server.count`
      - `- server.root_volume`
      - `- server.data_volumes`
      - `- server.extend_param`
      - `- server.metadata`
      - `- server.region_id`
      - `- server.resource_spec_code`
      - `- server.end_time`

### HuaweiCloud SDK CDN

- _新增特性_
  - 支持接口`ListDomains`、`ShowDomainDetailByName`
- _解决问题_
  - 无
- _特性变更_
  - **ListDomains**
    - 请求参数变更
      - `+ show_tags`
      - `+ exact_match`
    - 响应参数变更
      - `+ domains.tags`

### HuaweiCloud SDK CPH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ShowBandwidthDetail**
    - 请求参数变更
      - `+ offset`
      - `+ limit`
  - **ListJobs**
    - 请求参数变更
      - `+ offset`
      - `+ limit`
  - **ListCloudPhoneModels**
    - 请求参数变更
      - `+ offset`
      - `+ limit`
  - **CreateCloudPhoneServer**
    - 响应参数变更
      - `+ server_ids`
  - **CreateNet2CloudPhoneServer**
    - 响应参数变更
      - `+ server_ids`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持以下接口：
    - `ListMessageStatistics`
    - `ListNotice`
    - `BatchDeleteNotice`
    - `BatchUpdateNotice`
    - `ImportUser`
    - `ListGlobalWorkflowStatistic`
- _解决问题_
  - 无
- _特性变更_
  - **ListDatabaseData**
    - 响应参数变更
      - `* objects: list<map<string, object>> -> list<map<string, string>>`
  - **ImportDatabaseData**
    - 响应参数变更
      - `- creator`
      - `- create_time`
      - `- total_count`
      - `- end_time`
      - `- name`
      - `- finish_count`
      - `- type`
      - `- failed_reason`
      - `- status`
  - **ShowDataJob**
    - 响应参数变更
      - `+ additions`
  - **UpdateJobConfig**
    - 请求参数变更
      - `- job_retain_number`
  - **ShowMessageClearRule**
    - 响应参数变更
      - `- message_retain_time`
  - **UpdateMessageClearRule**
    - 请求参数变更
      - `- message_retain_number`
      - `- message_retain_time`
  - **ShowOverview**
    - 响应参数变更
      - `+ is_arrears`
  - **UpdatePerformanceResource**
    - 请求参数变更
      - `+ schedulable`
  - **ShowEnv**
    - 响应参数变更
      - `+ enable_cold_archive`
  - **ShowUser**
    - 响应参数变更
      - `+ source`
  - **ShowAsset**
    - 响应参数变更
      - `+ versions.description`
      - `- versions.descritpion`
  - **ShowAssetVersion**
    - 响应参数变更
      - `+ version.description`
      - `- version.descritpion`
  - **CreateBackup**
    - 请求参数变更
      - `+ storage_type`
  - **ListBackup**
    - 响应参数变更
      - `+ backups.storage_type`
      - `+ backups.archive_days`
  - **ShowData**
    - 请求参数变更
      - `+ X-Need-Content`
    - 响应参数变更
      - `+ content`
  - **ListDataJob**
    - 响应参数变更
      - `- creator`
      - `- create_time`
      - `- total_count`
      - `- end_time`
      - `- name`
      - `- id`
      - `- finish_count`
      - `- type`
      - `- failed_reason`
      - `- status`
      - `+ data_jobs.additions`
  - **ShowProjectTraceData**
    - 响应参数变更
      - `- allowed_operate`
      - `- deletable`
  - **UpdateMessageReceiveConfig**
    - 请求参数变更
      - `- scope`
      - `- language`
      - `- resource_types`
  - **ShowMessageEmailConfig**
    - 响应参数变更
      - `- password`
  - **UpdateMessageEmailConfig**
    - 请求参数变更
      - `- server`
      - `- subject_prefix`
      - `- password`
      - `- user_name`
      - `- language`
      - `- email`
  - **ListUser**
    - 响应参数变更
      - `+ source`
      - `+ users.source`
  - **ShowTaskInstanceMetricData**
    - 响应参数变更
      - `- metric_name`
      - `- resource_id`
  - **ListPerformanceResourceStat**
    - 响应参数变更
      - `+ performance_resources.schedulable`
  - **ListAsset**
    - 响应参数变更
      - `+ assets.versions.description`
      - `- assets.versions.descritpion`
  - **ListStar**
    - 响应参数变更
      - `+ assets.versions.description`
      - `- assets.versions.descritpion`
  - **ListData**
    - 响应参数变更
      - `+ content`
      - `+ datas.content`
  - **ShowProjectTrace**
    - 响应参数变更
      - `- allowed_operate`
      - `- deletable`
      - `- datas.allowed_operate`
      - `- datas.deletable`
      - `* datas: list<DataRsp> -> list<TraceDataRsp>`
  - **ListComputingResources**
    - 响应参数变更
      - `+ resources.failure_reason`
      - `- resources.ip`
      - `- resources.period_num`
  - **ListDatabaseResource**
    - 响应参数变更
      - `+ resources.failure_reason`
  - **ListPerformanceResources**
    - 响应参数变更
      - `+ resources.running_job_count`
      - `+ resources.failure_reason`
      - `+ resources.schedulable`
  - **ListStorageResources**
    - 响应参数变更
      - `- resources.id`
      - `- resources.name`
  - **ExecuteJob**
    - 请求参数变更
      - `+ tasks.io_acc_type`
  - **CreateAutoJob**
    - 请求参数变更
      - `+ tasks.io_acc_type`
  - **UpdateJob**
    - 请求参数变更
      - `+ tasks.io_acc_type`
  - **ShowJob**
    - 响应参数变更
      - `+ still_running_tasks`
      - `+ task_runtime_info.sub_tasks.pod_create_time`
      - `+ task_runtime_info.sub_tasks.pod_start_time`
      - `+ task_runtime_info.sub_tasks.job_failed_times`
      - `+ tasks.io_acc_type`
  - **UpdateAutoJob**
    - 请求参数变更
      - `+ tasks.io_acc_type`
  - **ShowAutoJob**
    - 响应参数变更
      - `+ tasks.io_acc_type`
  - **ShowWorkflow**
    - 响应参数变更
      - `+ tasks.io_acc_type`

### HuaweiCloud SDK EIP

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **ListBandwidthPkg**
    - 请求参数变更
      - `+ limit`
      - `+ marker`
      - `+ offset`
  - **ListCommonPools**
    - 请求参数变更
      - `+ limit`
      - `+ offset`
  - **ListShareBandwidthTypes**
    - 请求参数变更
      - `+ marker`
      - `+ offset`

### HuaweiCloud SDK IAM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - **KeystoneListMappings**
    - 响应参数变更
      - `* mappings.rules.local.groups: object -> string`
  - **KeystoneShowMapping**
    - 响应参数变更
      - `* mapping.rules.local.groups: object -> string`
  - **KeystoneCreateMapping**
    - 请求参数变更
      - `* mapping.rules.local.groups: object -> string`
    - 响应参数变更
      - `* mapping.rules.local.groups: object -> string`
  - **KeystoneUpdateMapping**
    - 请求参数变更
      - `* mapping.rules.local.groups: object -> string`
    - 响应参数变更
      - `* mapping.rules.local.groups: object -> string`

### HuaweiCloud SDK Image

- _新增特性_
  - 支持接口`CreateVideoObjectMaskingTask`、`ShowVideoObjectMaskingTask`
- _解决问题_
  - 无
- _特性变更_
  - **CreateTextToImageTask**
    - 请求参数变更
      - `+ config.common.inference.image_nums`
      - `+ config.common.inference.resolution: enum value [512*768,768*512,512*512]`
  - **ShowTextToImageTask**
    - 响应参数变更
      - `+ config.common.inference.image_nums`
      - `+ config.common.inference.resolution: enum value [512*768,768*512,512*512]`
  - **CreateImageVariationTask**
    - 请求参数变更
      - `+ config.common.inference.image_nums`
      - `+ config.common.inference.resolution: enum value [512*768,768*512,512*512]`
  - **ShowImageVariationTask**
    - 响应参数变更
      - `+ config.common.inference.image_nums`
      - `+ config.common.inference.resolution: enum value [512*768,768*512,512*512]`

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 支持以下接口：
    - `BatchListDcDs`
    - `CreateDs`
    - `ShowDcDs`
    - `UpdateDcDs`
    - `DeleteDcDs`
    - `SynchronizeDcConfigs`
    - `BatchListDcDevices`
    - `BatchListDcPoints`
    - `CreateDcPoint`
    - `ShowDcPoint`
    - `UpdateDcPoint`
    - `DeleteDcPoint`
    - `ImportPoints`
    - `ShowPointTemplate`
    - `ShowPoints`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IVS

- _新增特性_
  - 支持接口`DetectStandardByVideoAndIdCardImage`、`DetectStandardByVideoAndNameAndId`
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
  - **RecognizeMvsInvoice**
    - 请求参数变更
      - `+ return_text_location`
      - `+ return_confidence`
      - `+ type`
    - 响应参数变更
      - `+ result.buyer_address`
      - `+ result.buyer_phone`
      - `+ result.licence_plate_number`
      - `+ result.registration_number`
      - `+ result.dept_motor_vehicles`
      - `+ result.auction_org_name`
      - `+ result.auction_org_address`
      - `+ result.auction_org_id`
      - `+ result.auction_org_bank_account`
      - `+ result.auction_org_phone`
      - `+ result.used_vehicle_market_name`
      - `+ result.used_vehicle_market_id`
      - `+ result.used_vehicle_market_address`
      - `+ result.used_vehicle_market_bank_account`
      - `+ result.used_vehicle_market_phone`
      - `+ result.remark`
      - `+ result.drawer_name`
      - `+ result.type`
      - `+ result.text_location`
      - `+ result.confidence`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListRecycleInstances`、`ShowRecyclePolicy`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.31 2023-03-14

### HuaweiCloud SDK Image

- _新增特性_
  - 支持接口`CreateTextToImageTask`、`ShowTextToImageTask`、`CreateImageVariationTask`、`ShowImageVariationTask`
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`RunImageWisedesignColorfilter`、`RunImageWisedesignCombine`

# 3.1.30 2023-03-09

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持以下接口：
    - `ListTemplates`
    - `DeleteTemplate`
    - `ShowTemplateMetadata`
    - `UpdateTemplateMetadata`
    - `ShowTemplateVersionContent`
    - `DeleteTemplateVersion`
    - `ShowTemplateVersionMetadata`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListExecutionPlans`:
    - 响应参数`status`新增枚举值`APPLY_IN_PROGRESS`
    - 响应参数`stack_name`、`execution_plan_name`改为必填
  - 接口`GetExecutionPlan`响应参数`action`移除枚举值`IN_PLACE_UPDATE`
  - 接口`GetExecutionPlanMetadata`响应参数`stack_name`、`execution_plan_name`改为必填
  - 接口`ListStackResources`新增响应参数 `resource_attributes`
  - 接口`EstimateExecutionPlanPrice`:
    - 新增响应参数 `unsupported_message`
    - 响应参数`sale_price`类型调整 `object` -> `double`
    - 响应参数`discount`类型调整 `object` -> `double`
    - 响应参数`original_price`类型调整 `object` -> `double`
    - 响应参数`period_type`移除枚举值`WEEK`

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`ShowCategoryList`、`ListPublisher`
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
  - 接口`UpdateDevice`新增响应参数 `connection_status_update_time`、`active_time`
  - 接口`ShowDevice`新增响应参数 `connection_status_update_time`、`active_time`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeAutoClassification`新增请求参数 `extended_parameters`

# 3.1.29 2023-03-07

### HuaweiCloud SDK VOD

- _新增特性_
  - 支持接口`ModifySubtitle`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.28 2023-03-02

### HuaweiCloud SDK AOM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateWorkflow`:
    - 移除请求参数 `trigger`
    - 响应参数`template_i18n`类型调整
  - 接口`ListWorkflow`响应参数`template_i18n`类型调整

### HuaweiCloud SDK BCS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`BatchInviteMembersToChannel`新增响应参数 `result`
  - 接口`ListNotifications`响应参数`node_count`类型调整 `string` -> `int32`
  - 接口`ListMembers`响应参数`node_count`类型调整 `string` -> `int32`
  - 接口`DownloadBlockchainCert`移除响应参数 `result`
  - 接口`DownloadBlockchainSdkConfig`移除响应参数 `result`
  - 接口`CreateBlockchainCertByUserName`移除响应参数 `result`

### HuaweiCloud SDK BMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListBareMetalServers`:
    - 响应参数`status`新增枚举值`HARD_REBOOT`、`DELETED`
    - 响应参数`OS-EXT-STS:vm_state`移除枚举值`suspended`
  - 接口`CreateBareMetalServers`:
    - 新增请求参数 `chargingMode`
    - 移除请求参数 `chargingmode`
  - 接口`ChangeBaremetalServerName`响应参数`OS-EXT-STS:vm_state`移除枚举值`SUSPENDED`
  - 接口`ListBareMetalServerDetails`:
    - 响应参数`status`新增枚举值`HARD_REBOOT`、`DELETED`
    - 响应参数`OS-EXT-STS:vm_state`移除枚举值`suspended`

### HuaweiCloud SDK CDN

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowDomainFullConfig`:
    - 响应参数`error_code`类型调整 `string` -> `int32`
    - 响应参数`target_code`类型调整 `string` -> `int32`
  - 接口`UpdateDomainFullConfig`:
    - 请求参数`error_code`类型调整 `string` -> `int32`
    - 请求参数`target_code`类型调整 `string` -> `int32`

### HuaweiCloud SDK CodeHub

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCommits`新增请求参数 `page`、`per_page`

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持接口`ShowReplSetName`、`UpdateReplSetName`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DRIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListV2xEdges`新增响应参数 `ip`

### HuaweiCloud SDK EG

- _新增特性_
  - 支持以下接口：
    - `CheckPutEvents`
    - `ListObsBuckets`
    - `ListWorkflowTriggers`
    - `ListPubMetrics`
    - `ListSubMetrics`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateEventSource`请求参数`type`新增枚举值`ROCKETMQ`
  - 接口`CreateChannel`请求参数`name`改为必填
  - 接口`ListSubscriptions`:
    - 新增响应参数 `used`
    - 响应参数`transform`类型调整
  - 接口`CreateSubscription`:
    - 新增响应参数 `used`
    - 请求参数`transform`类型调整
    - 请求参数`detail`改为必填
    - 响应参数`transform`类型调整
  - 接口`ShowDetailOfSubscription`:
    - 新增响应参数 `used`
    - 响应参数`transform`类型调整
  - 接口`UpdateSubscription`:
    - 新增响应参数 `used`
    - 请求参数`transform`类型调整
    - 请求参数`detail`改为必填
    - 响应参数`transform`类型调整
  - 接口`CreateSubscriptionTarget`:
    - 请求参数`transform`类型调整
    - 请求参数`detail`改为必填
    - 响应参数`transform`类型调整
  - 接口`ShowDetailOfSubscriptionTarget`响应参数`transform`类型调整
  - 接口`UpdateSubscriptionTarget`:
    - 请求参数`transform`类型调整
    - 请求参数`detail`改为必填
    - 响应参数`transform`类型调整
  - 接口`CreateConnection`请求参数`vpc_id`、`subnet_id`改为必填
  - 接口`ListAgencies`请求参数`type`新增枚举值`EG_RESTORE_AGENCY`
  - 接口`CreateAgencies`请求参数`type`新增枚举值`EG_RESTORE_AGENCY`
  - 接口`ListQuotas`:
    - 请求参数`type`新增枚举值`SOURCE_ROCKETMQ`
    - 响应参数`type`新增枚举值`SOURCE_ROCKETMQ`
  - 接口`ListTriggers`:
    - 新增响应参数 `used`
    - 响应参数`transform`类型调整

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateTrigger`:
    - 新增请求参数 `event_data`
    - 新增响应参数 `trigger_id`、`trigger_type_code`、`trigger_status`、`event_data`、`last_updated_time`、`created_time`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 支持以下接口：
    - `ResetDbUserPassword`
    - `ModifyDbUserPrivilege`
    - `ListDbUsers`
    - `CreateDbUser`
    - `DeleteDbUser`
    - `ListInstanceDatabases`
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
  - 接口`ListSimCards`新增请求参数 `order_ids`

### HuaweiCloud SDK Image

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 支持接口`ListOtaPackageInfo`、`CreateOtaPackage`、`ShowOtaPackage`、`DeleteOtaPackage`
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
  - 接口`ListInstanceConsumerGroups`:
    - 新增响应参数 `groups`
    - 移除响应参数 `group_ids`、`next_offset`、`previous_offset`

### HuaweiCloud SDK MRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateCluster`新增请求参数 `external_datasources`、`effective_days`
  - 接口`ShowAutoScalingPolicy`新增响应参数 `effective_days`

### HuaweiCloud SDK ProjectMan

- _新增特性_
  - 支持接口`ListSpecIssueStayTimes`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListSslCertDownloadLink`
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateConfiguration`新增响应参数 `configuration`
  - 接口`UpdatePostgresqlInstanceAlias`请求参数`alias`改为非必填
  - 接口`UpdateDatabase`请求参数`comment`改为非必填

# 3.1.27 2023-02-23

### HuaweiCloud SDK BSS

- _新增特性_
  - 支持接口`ListCustomerAccountChangeRecords`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CBR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListVault`响应参数`value`改为必填
  - 接口`CreateVault`:
    - 请求参数`value`改为必填
    - 响应参数`value`改为必填
  - 接口`ShowVault`响应参数`value`改为必填
  - 接口`UpdateVault`:
    - 请求参数`value`改为必填
    - 响应参数`value`改为必填
  - 接口`ListProtectable`响应参数`value`改为必填
  - 接口`ShowProtectable`响应参数`value`改为必填
  - 接口`ShowVaultResourceInstances`响应参数`value`改为必填

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateRequest`:
    - 新增请求参数 `request_type`、`above_text`、`following_text`
    - 新增响应参数 `dispatched_task_number`
    - 请求参数`signature`改为非必填
  - 接口`ShowResult`新增响应参数 `request_type`

### HuaweiCloud SDK CPH

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ChangeCloudPhoneServerModel`新增请求参数 `phone_model_name`

### HuaweiCloud SDK CSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateLoadIkThesaurus`请求参数`mainObject`、`stopObject`、`synonymObject`改为非必填

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持接口`ShrinkInstanceNodes`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持接口`CreateClusterV2`
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
  - 接口`ListRoutingRules`新增请求参数 `active`
  - 接口`CreateRuleAction`新增请求参数 `mysql_forwarding`
  - 接口`ListRuleActions`新增响应参数 `mysql_forwarding`
  - 接口`UpdateRuleAction`:
    - 新增请求参数 `mysql_forwarding`
    - 新增响应参数 `mysql_forwarding`
  - 接口`ShowRuleAction`新增响应参数 `mysql_forwarding`

### HuaweiCloud SDK LakeFormation

- _新增特性_
  - 支持接口`BatchUpdateLakeFormationInstanceTags`、`CreateLakeFormationInstance`、`ListPolicy`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowLakeFormationInstance`移除响应参数 `key`、`value`
  - 接口`SetPartitionColumnStatistics`移除响应参数 `column_statistics_desc`、`column_statistics_objects`

### HuaweiCloud SDK MRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowJobExeListNew`:
    - 请求参数`job_state`新增枚举值`FAILED`、`KILLED`、`NEW`、`NEW_SAVING`、`SUBMITTED`、`ACCEPTED`、`RUNNING`、`FINISHED`, 移除枚举值`FAILED：失败`、`KILLED：已终止`、`NEW：已创建`、`NEW_SAVING：已创建保存中`、`SUBMITTED：已提交`、`ACCEPTED：已接受`、`RUNNING：运行中`、`FINISHED：已完成`
    - 请求参数`job_result`新增枚举值`FAILED`、`KILLED`、`UNDEFINED`、`SUCCEEDED`, 移除枚举值`FAILED：执行失败的作业。`、`KILLED：执行中被手动终止的作业。`、`UNDEFINED：正在执行的作业。`、`SUCCEEDED：执行成功的作业。`
  - 接口`ShowHdfsFileList`请求参数`sort_key`新增枚举值`path_suffix`、`length`、`modification_time`, 移除枚举值`path_suffix：文件或目录名称`、`length：文件大小`、`modification_time：修改时间`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`UpdateDbUserPrivilege`
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`新增请求参数 `X-Client-Token`

### HuaweiCloud SDK SCM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ImportCertificate`请求参数`certificate_chain`改为非必填
  - 接口`ExportCertificate`新增响应参数 `entire_certificate`

### HuaweiCloud SDK WAF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdatePremiumHost`新增请求参数 `flag`

# 3.1.26 2023-02-16

### HuaweiCloud SDK AOM

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateApp`移除响应参数 `id`
  - 接口`ListResourceUnderNode`:
    - 新增请求参数 `ci_ids`
    - 请求参数`ci_id`改为非必填

### HuaweiCloud SDK CloudIDE

- _新增特性_
  - 支持接口`CreateLogin`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListExtensions`移除响应参数 `id`、`property_name`、`property_value`、`extension_version_id`、`created_at`、`updated_at`
  - 接口`ShowExtensionDetail`移除响应参数 `id`、`property_name`、`property_value`、`extension_version_id`、`created_at`、`updated_at`

### HuaweiCloud SDK CSS

- _新增特性_
  - 支持接口`ChangeSecurityGroup`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ChangeMode`:
    - 新增请求参数 `changeModeReq`
    - 移除请求参数 `changeModeRequestBody`
  - 接口`AddIndependentNode`:
    - 新增请求参数 `IndependentReq`
    - 移除请求参数 `IndependentRequestBody`

### HuaweiCloud SDK CTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateTracker`新增请求参数 `compress_type`、`is_sort_by_service`
  - 接口`CreateTracker`新增请求参数 `compress_type`、`is_sort_by_service`
  - 接口`ListTrackers`新增响应参数 `compress_type`、`is_sort_by_service`

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`CreateCustomTemplate`、`CreateAutoExpireScanTask`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DRIS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowHistoryTrafficEvents`新增响应参数 `esn`

### HuaweiCloud SDK DWS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListClusterSnapshots`新增请求参数 `project_id`、`cluster_id`、`limit`、`offset`、`sort_key`、`sort_dir`

### HuaweiCloud SDK FRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DetectLiveByUrl`新增请求参数 `nod_threshold`
  - 接口`DetectLiveByUrlIntl`新增请求参数 `nod_threshold`
  - 接口`DetectLiveByFile`新增请求参数 `nod_threshold`
  - 接口`DetectLiveByFileIntl`新增请求参数 `nod_threshold`
  - 接口`DetectLiveByBase64`新增请求参数 `nod_threshold`
  - 接口`DetectLiveByBase64Intl`新增请求参数 `nod_threshold`

### HuaweiCloud SDK GaussDB

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`AddDatabasePermission`请求参数`host`改为必填

### HuaweiCloud SDK Image

- _新增特性_
  - 支持接口`RunImageSuperResolution`、`RunRecaptureDetect`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK OSM

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 支持接口`CreateInstanceByEngine`、`BatchCreateOrDeleteRocketmqTag`、`ShowRocketmqTags`、`ShowRocketmqProjectTags`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增请求参数 `limit`、`offset`
  - 接口`ShowConsumerListOrDetails`新增请求参数 `limit`、`offset`
  - 接口`ListConsumerGroupOfTopic`新增请求参数 `limit`、`offset`

### HuaweiCloud SDK WAF

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateHost`:
    - 请求参数`tls`移除枚举值`TLS v1.3`
    - 响应参数`tls`移除枚举值`TLS v1.3`
  - 接口`ShowHost`响应参数`tls`移除枚举值`TLS v1.3`
  - 接口`CreatePremiumHost`响应参数`tls`移除枚举值`TLS v1.3`
  - 接口`ShowPremiumHost`响应参数`tls`移除枚举值`TLS v1.3`
  - 接口`UpdatePremiumHost`:
    - 请求参数`tls`移除枚举值`TLS v1.3`
    - 响应参数`tls`移除枚举值`TLS v1.3`

# 3.1.25 2023-02-09

### HuaweiCloud SDK LakeFormation

- _新增特性_
  - 支持湖仓构建服务
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK CloudArtifact

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - `制品仓库 CloudArtifact`更名为`制品仓库 CodeArtsArtifact`

### HuaweiCloud SDK CloudBuild

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - `编译构建 CloudBuild`更名为`编译构建 CodeArts Build`

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RenewalResources`新增响应参数 `fail_resource_infos`
  - 接口`CancelResourcesSubscription`新增响应参数 `fail_resource_infos`

### HuaweiCloud SDK DBSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`SwitchRiskRule`:
    - 新增响应参数 `status`
    - 移除响应参数 `result`

### HuaweiCloud SDK DDS

- _新增特性_
  - 支持接口`ListLtsSlowLogs`
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
  - 接口`ListAsyncInvocations`新增响应参数 `error_code`

### HuaweiCloud SDK GaussDBforNoSQL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowPauseResumeStutus`:
    - 新增请求参数 `X-Auth-Token`
    - 新增响应参数 `master_instance_id`、`slave_instance_id`、`data_sync_indicators`、`rto_and_rpo_indicators`
    - 移除请求参数 `x-auth-token`

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRuleActions`新增响应参数 `roma_forwarding`、`influxdb_forwarding`、`functiongraph_forwarding`、`mrs_kafka_forwarding`、`dms_rocketmq_forwarding`
  - 接口`CreateRuleAction`新增请求参数 `roma_forwarding`、`influxdb_forwarding`、`functiongraph_forwarding`、`mrs_kafka_forwarding`、`dms_rocketmq_forwarding`
  - 接口`UpdateRuleAction`:
    - 新增请求参数 `roma_forwarding`、`influxdb_forwarding`、`functiongraph_forwarding`、`mrs_kafka_forwarding`、`dms_rocketmq_forwarding`
    - 新增响应参数 `roma_forwarding`、`influxdb_forwarding`、`functiongraph_forwarding`、`mrs_kafka_forwarding`、`dms_rocketmq_forwarding`
  - 接口`ShowRuleAction`新增响应参数 `roma_forwarding`、`influxdb_forwarding`、`functiongraph_forwarding`、`mrs_kafka_forwarding`、`dms_rocketmq_forwarding`

### HuaweiCloud SDK OCR

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeTollInvoice`:
    - 新增请求参数 `return_text_location`
    - 新增响应参数 `text_location`

### HuaweiCloud SDK RDS

- _新增特性_
  - 支持接口`ListErrorlogForLts`、`ListSlowlogForLts`、`ListSlowLogStatisticsForLts`
- _解决问题_
  - 无
- _特性变更_
  - 无

# 3.1.24 2023-02-02

### HuaweiCloud SDK AOS

- _新增特性_
  - 支持接口`UpdateStack`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ApplyExecutionPlan`新增请求参数 `executor`
  - 接口`ListStackEvents`:
    - 新增请求参数 `filter`、`field`
    - 移除响应参数 `resource_id_key`、`resource_id_value`、`resource_name`、`resource_type`、`time`、`event_type`、`event_message`、`elapsed_seconds`
  - 接口`GetStackMetadata`响应参数`stack_name`改为必填
  - 接口`CreateStack`新增请求参数 `executor`
  - 接口`ListStackResources`:
    - 新增响应参数 `index_key`
    - 响应参数`resource_status`移除枚举值`DELETION_SKIPPED`
  - 接口`DeployStack`新增请求参数 `executor`

### HuaweiCloud SDK BSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RenewalResources`新增响应参数 `fail_resource_infos`
  - 接口`CancelResourcesSubscription`新增响应参数 `fail_resource_infos`

### HuaweiCloud SDK CloudPipeline

- _新增特性_
  - 支持以下接口：
    - `RunPipeline`
    - `BatchShowPipelinesLatestStatus`
    - `ShowPipelineRunDetail`
    - `ListPipelines`
    - `DeletePipeline`
    - `StopPipelineRun`
    - `ListPipelineRuns`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK GaussDBforopenGauss

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateInstance`请求参数`type`新增枚举值`GaussDB`
  - 接口`ListInstances`请求参数`datastore_type`新增枚举值`GaussDB`
  - 接口`ListBackups`响应参数`type`新增枚举值`GaussDB`

### HuaweiCloud SDK GSL

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListBackPools`新增请求参数 `all_billing_cycle`
  - 接口`ListSimPools`新增请求参数 `all_billing_cycle`

### HuaweiCloud SDK IMS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateImage`请求参数`type`新增枚举值`IsoImage`

### HuaweiCloud SDK Kafka

- _新增特性_
  - 支持接口`CreateInstanceByEngine`、`ShowEngineInstanceExtendProductInfo`、`ResizeEngineInstance`、`CreateReassignmentTask`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListInstances`新增响应参数 `sasl_enabled_mechanisms`
  - 接口`CreatePostPaidInstance`请求参数`kafka_manager_user`、`kafka_manager_password`改为非必填
  - 接口`ShowInstance`新增响应参数 `sasl_enabled_mechanisms`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunTextModeration`新增请求参数 `white_glossaries`

# 3.1.23 2023-01-19

### HuaweiCloud SDK CCM

- _新增特性_
  - 支持接口`EnableCertificateAuthorityCrl`、`DisableCertificateAuthorityCrl`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCertificate`新增响应参数 `enc_cert_info`
  - 接口`ShowCertificate`新增响应参数 `enc_cert_info`
  - 接口`ExportCertificate`:
    - 新增请求参数 `is_sm_standard`
    - 新增响应参数 `enc_certificate`、`enc_private_key`、`enc_sm2_enveloped_key`

### HuaweiCloud SDK DWS

- _新增特性_
  - 支持接口`ListMonitorIndicatorData`、`ListMonitorIndicators`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK HSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListRiskConfigCheckRules`:
    - 新增响应参数 `enable_fix`、`enable_click`
    - 移除响应参数 `fix_status`、`enable_auto_fix`
  - 接口`ShowCheckRuleDetail`新增请求参数 `check_type`
  - 接口`SwitchHostsProtectStatus`请求参数`version`、`host_id_list`改为必填

### HuaweiCloud SDK IoTDA

- _新增特性_
  - 支持接口`UploadBatchTaskFile`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowEdgeNode`新增响应参数 `virtual_ipv6_address`

# 3.1.22 2023-01-12

### HuaweiCloud SDK APIG

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListApiGroupsV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`UpdateApiGroupV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`ShowDetailsOfApiGroupV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`UpdateApiV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`ShowDetailsOfApiV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`BatchPublishOrOfflineApiV2`:
    - 新增请求参数 `group_id`
    - 请求参数`env_id`改为必填
  - 接口`ListApiVersionDetailV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`CreateInstanceV2`新增请求参数 `bandwidth_charging_mode`、`ingress_bandwidth_size`、`ingress_bandwidth_charging_mode`
  - 接口`UpdateInstanceV2`新增响应参数 `bandwidth_charging_mode`、`ingress_bandwidth_charging_mode`
  - 接口`ShowDetailsOfInstanceV2`新增响应参数 `bandwidth_charging_mode`、`ingress_bandwidth_charging_mode`
  - 接口`AddEngressEipV2`新增请求参数 `bandwidth_charging_mode`
  - 接口`UpdateEngressEipV2`新增请求参数 `bandwidth_charging_mode`
  - 接口`ImportMicroservice`请求参数`version`改为非必填
  - 接口`CreateCertificateV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`ListCertificatesV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`UpdateCertificateV2`新增响应参数 `is_has_trusted_root_ca`
  - 接口`ShowDetailsOfCertificateV2`新增响应参数 `is_has_trusted_root_ca`

### HuaweiCloud SDK BSS

- _新增特性_
  - 支持接口`ListFreeResourcesUsageRecords`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerselfResourceRecordDetails`新增响应参数 `sub_service_type_code`、`sub_service_type_name`、`sub_resource_type_code`、`sub_resource_type_name`、`sub_resource_id`、`sub_resource_name`
  - 接口`ListCustomerselfResourceRecords`新增响应参数 `sub_service_type_code`、`sub_service_type_name`、`sub_resource_type_code`、`sub_resource_type_name`、`sub_resource_id`、`sub_resource_name`
  - 接口`ListCosts`请求参数`operator`改为必填

### HuaweiCloud SDK BSSINTL

- _新增特性_
  - 支持接口`ListFreeResourcesUsageRecords`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCustomerselfResourceRecordDetails`新增响应参数 `sub_service_type_code`、`sub_service_type_name`、`sub_resource_type_code`、`sub_resource_type_name`、`sub_resource_id`、`sub_resource_name`
  - 接口`ListCustomerselfResourceRecords`新增响应参数 `sub_service_type_code`、`sub_service_type_name`、`sub_resource_type_code`、`sub_resource_type_name`、`sub_resource_id`、`sub_resource_name`
  - 接口`ListCosts`请求参数`operator`改为必填

### HuaweiCloud SDK CES

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListAlarmHistories`:
    - 新增响应参数 `data_points`
    - 移除响应参数 `datapoints`

### HuaweiCloud SDK DRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDbObjects`新增响应参数 `object_scope`
  - 接口`ShowDbObjectCollectionStatus`新增响应参数 `object_scope`

### HuaweiCloud SDK eiHealth

- _新增特性_
  - 支持以下接口：
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
- _解决问题_
  - 无
- _特性变更_
  - 移除接口`ListRecentJob`
  - 接口`ListAsset`移除响应参数 `latest_version`
  - 接口`ShowAsset`移除响应参数 `latest_version`
  - 接口`ShowAssetVersion`新增响应参数 `failed_reason`、`labels`、`picture`
  - 接口`ListStar`移除响应参数 `latest_version`
  - 接口`CreateDatabaseData`请求参数`column`改为必填
  - 接口`UpdateDatabaseData`请求参数`column`改为必填
  - 接口`ListData`新增响应参数 `deletable`
  - 接口`ShowData`新增响应参数 `deletable`
  - 接口`ListDataJob`新增响应参数 `failed_reason`
  - 接口`UpdateProject`新增请求参数 `storage_quota`
  - 接口`ShowProject`新增响应参数 `storage_quota`
  - 接口`ShowProjectTrace`移除响应参数 `path`、`name`、`type`、`size`、`create_time`、`download_url`
  - 接口`ShowProjectTraceData`新增响应参数 `allowed_operate`、`deletable`
  - 接口`ListComputingResources`:
    - 新增响应参数 `node_labels`
    - 移除请求参数 `label`、`offset`、`limit`
  - 接口`UpdateJobConfig`移除请求参数 `job_retain_time`
  - 接口`ShowJobConfig`移除响应参数 `job_retain_time`
  - 接口`ListLabel`移除响应参数 `count`
  - 接口`BatchUpdateNodeLabel`移除请求参数 `name`
  - 接口`DeleteUser`移除请求参数 `user_id_type`
  - 接口`ShowTaskInstances`新增响应参数 `host_name`

### HuaweiCloud SDK FRS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DetectLiveByUrl`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectLiveByUrlIntl`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectLiveFaceByUrl`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectLiveByFile`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectLiveByFileIntl`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectLiveFaceByFile`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectLiveByBase64`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectLiveByBase64Intl`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectLiveFaceByBase64`新增请求参数 `Enterprise-Project-Id`
  - 接口`SearchFaceByFaceId`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectFaceByFile`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectFaceByFileIntl`新增请求参数 `Enterprise-Project-Id`
  - 接口`UpdateFace`新增请求参数 `Enterprise-Project-Id`
  - 接口`DeleteFaceByExternalImageId`新增请求参数 `Enterprise-Project-Id`
  - 接口`ShowFacesByLimit`新增请求参数 `Enterprise-Project-Id`
  - 接口`CompareFaceByFile`新增请求参数 `Enterprise-Project-Id`
  - 接口`DeleteFaceByFaceId`新增请求参数 `Enterprise-Project-Id`
  - 接口`ShowFacesByFaceId`新增请求参数 `Enterprise-Project-Id`
  - 接口`AddFacesByBase64`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectFaceByUrl`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectFaceByUrlIntl`新增请求参数 `Enterprise-Project-Id`
  - 接口`DeleteFaceSet`新增请求参数 `Enterprise-Project-Id`
  - 接口`ShowFaceSet`新增请求参数 `Enterprise-Project-Id`
  - 接口`CompareFaceByBase64`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectFaceByBase64`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectFaceByBase64Intl`新增请求参数 `Enterprise-Project-Id`
  - 接口`CreateFaceSet`新增请求参数 `Enterprise-Project-Id`
  - 接口`ShowAllFaceSets`新增请求参数 `Enterprise-Project-Id`
  - 接口`SearchFaceByFile`新增请求参数 `Enterprise-Project-Id`
  - 接口`AddFacesByUrl`新增请求参数 `Enterprise-Project-Id`
  - 接口`AddFacesByFile`新增请求参数 `Enterprise-Project-Id`
  - 接口`SearchFaceByUrl`新增请求参数 `Enterprise-Project-Id`
  - 接口`SearchFaceByBase64`新增请求参数 `Enterprise-Project-Id`
  - 接口`CompareFaceByUrl`新增请求参数 `Enterprise-Project-Id`
  - 接口`BatchDeleteFaces`新增请求参数 `Enterprise-Project-Id`

### HuaweiCloud SDK HSS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`UpdateProtectionPolicy`请求参数`policy_id`、`policy_name`、`protection_mode`、`bait_protection_status`、`protection_directory`、`protection_type`、`operating_system`改为必填
  - 接口`StartProtection`请求参数`operating_system`、`ransom_protection_status`、`backup_protection_status`、`policy_id`、`pattern`、`agent_id_list`、`host_id_list`改为必填
  - 接口`StopProtection`请求参数`host_id_list`、`agent_id_list`、`close_protection_type`改为必填
  - 接口`UpdateBackupPolicyInfo`请求参数`policy_id`、`pattern`改为必填
  - 接口`ListQuotasDetail`新增响应参数 `enterprise_project_id`、`enterprise_project_name`
  - 接口`ListSecurityEvents`新增响应参数 `host_status`、`agent_status`、`protect_status`、`asset_value`、`keyword`、`hash`
  - 接口`ChangeEvent`:
    - 新增请求参数 `keyword`、`hash`
    - 移除请求参数 `description`
  - 接口`DeleteHostsGroup`请求参数`group_id`改为非必填
  - 接口`AddHostsGroup`请求参数`group_name`、`host_id_list`改为必填
  - 接口`AssociatePolicyGroup`请求参数`target_policy_group_id`改为必填
  - 接口`ChangeVulStatus`请求参数`operate_type`、`vul_id`、`host_id_list`改为必填
  - 接口`SetWtpProtectionStatusInfo`:
    - 新增请求参数 `charging_mode`
    - 移除请求参数 `payment_mode`

### HuaweiCloud SDK IVS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`DetectStandardByIdCardImage`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectStandardByNameAndId`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectExtentionByNameAndId`新增请求参数 `Enterprise-Project-Id`
  - 接口`DetectExtentionByIdCardImage`新增请求参数 `Enterprise-Project-Id`

### HuaweiCloud SDK OCR

- _新增特性_
  - 支持接口`RecognizeCustomTemplate`
- _解决问题_
  - 无
- _特性变更_
  - 接口`RecognizeGeneralTable`:
    - 新增请求参数 `return_char_location`、`return_rectification_matrix`
    - 新增响应参数 `char_list`
  - 接口`RecognizeGeneralText`新增请求参数 `language`
  - 接口`RecognizeWebImage`:
    - 新增响应参数 `extracted_data`
    - 移除响应参数 `extracted_data`、`contact_info`、`image_size`、`height`、`width`、`name`、`phone`、`province`、`city`、`district`、`detail_address`

### HuaweiCloud SDK RocketMQ

- _新增特性_
  - 支持接口`ListRocketInstanceTopics`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowOneTopic`新增响应参数 `name`

# 3.1.21 2023-01-05

### HuaweiCloud SDK CPH

- _新增特性_
  - 支持以下接口：
    - `ListProjectTags`
    - `ListResourceTags`
    - `ListResourceInstances`
    - `BatchCreateTags`
    - `BatchDeleteTags`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListCloudPhoneServers`新增响应参数 `enterprise_project_id`
  - 接口`ShowCloudPhoneServerDetail`新增响应参数 `enterprise_project_id`

### HuaweiCloud SDK DCS

- _新增特性_
  - 支持接口`ListConfigHistories`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DNS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 移除以下接口：
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
  - 接口`CreatePrivateZone`:
    - 新增请求参数 `proxy_pattern`
    - 新增响应参数 `proxy_pattern`
  - 接口`ListPrivateZones`新增响应参数 `proxy_pattern`

### HuaweiCloud SDK DRIS

- _新增特性_
  - 支持接口`BatchShowRadars`
- _解决问题_
  - 无
- _特性变更_
  - 无

### HuaweiCloud SDK DRS

- _新增特性_
  - 支持接口`ShowDbObjectCollectionStatus`、`ShowUpdateObjectSavingStatus`、`CollectDbObjectsAsync`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListDbObjects`:
    - 新增请求参数 `db_names`
    - 新增响应参数 `status`、`id`

### HuaweiCloud SDK DWS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListNodeTypes`新增响应参数 `count`、`datastore_type`、`available_zones`、`ram`、`vcpus`、`datastores`、`volume`、`elastic_volume_specs`

### HuaweiCloud SDK FunctionGraph

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListFunctionTriggers`响应参数`trigger_status`新增枚举值`DISABLED`, 移除枚举值`DISABLE`
  - 接口`UpdateTrigger`请求参数`trigger_status`新增枚举值`DISABLED`, 移除枚举值`DISABLE`
  - 接口`ShowFunctionTrigger`响应参数`trigger_status`新增枚举值`DISABLED`, 移除枚举值`DISABLE`
  - 接口`CreateWorkflow`新增请求参数 `enable_stream_response`
  - 接口`UpdateWorkFlow`新增请求参数 `enable_stream_response`
  - 接口`ShowWorkFlow`新增响应参数 `enable_stream_response`

### HuaweiCloud SDK HiLens

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ShowNodes`新增响应参数 `deployment_num`
  - 接口`ShowNode`新增响应参数 `cluster_node_type`
  - 接口`ShowUpgradeProgress`新增请求参数 `offset`、`limit`
  - 接口`ListTasks`新增请求参数 `offset`、`limit`
  - 接口`ShowDeploymentPods`新增请求参数 `offset`、`limit`
  - 接口`ListWorkSpaces`新增请求参数 `offset`、`limit`

### HuaweiCloud SDK IoTEdge

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateEdgeNode`请求参数`app_version`改为非必填
  - 接口`ShowEdgeNode`新增响应参数 `reliability_level`

### HuaweiCloud SDK Live

- _新增特性_
  - 支持接口`ListUpStreamDetail`
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListBandwidthDetail`:
    - 新增请求参数 `service_type`
    - 请求参数`play_domains`改为必填
  - 接口`ListDomainTrafficDetail`:
    - 新增请求参数 `service_type`
    - 请求参数`play_domains`改为必填
  - 接口`ListDomainBandwidthPeak`:
    - 新增请求参数 `service_type`
    - 请求参数`play_domains`改为必填
  - 接口`ListDomainTrafficSummary`:
    - 新增请求参数 `service_type`
    - 请求参数`play_domains`改为必填
  - 接口`ListUsersOfStream`新增请求参数 `service_type`
  - 接口`ShowUpBandwidth`新增请求参数 `type`

### HuaweiCloud SDK LTS

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`CreateSearchCriterias`:
    - 新增请求参数 `eps_id`
    - 移除请求参数 `epsId`
  - 接口`DeleteSearchCriterias`:
    - 新增请求参数 `eps_id`
    - 移除请求参数 `epsId`

### HuaweiCloud SDK Moderation

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`RunTextModeration`新增请求参数 `white_glossary_names`

### HuaweiCloud SDK VPC

- _新增特性_
  - 无
- _解决问题_
  - 无
- _特性变更_
  - 接口`ListPorts`:
    - 新增请求参数 `security_groups`
    - 请求参数`fixed_ips`类型调整 `string` -> `array`

