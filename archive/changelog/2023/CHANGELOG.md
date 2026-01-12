# 3.1.75 2023-12-27

### HuaweiCloud SDK AAD

- _Features_
  - Support the following APIs:
    - `CreateAadDomain`
    - `CreateCertificate`
    - `ModifyDomainWebSwitch`
    - `ListSourceIps`
    - `AddBlackWhiteIpList`
    - `DeleteBlackWhiteIpList`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListMetricData**
    - changes of response param
      - `* datapoints.timestamp: int32 -> int64`
  - **ListApisV2**
    - changes of request param
      - `+ return_data_mode: enum value [brief,include_group,include_group_backend]`

### HuaweiCloud SDK CodeArtsArtifact

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CSMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListResourceInstances**
    - changes of response param
      - `+ resources.sys_tags`

### HuaweiCloud SDK DataArtsStudio

- _Features_
  - Support the APIs `ListFactoryJobs`, `CreateFactoryJob`, `ListFactoryAlarmInfo`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - Support the APIs `ShowInstanceSslDetail`, `UpdateSslSwitch`, `DownloadSslCert`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DDS

- _Features_
  - Support the API `ShowClientNetwork`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DGC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateJob**
    - changes of request param
      - `+ singleNodeJobFlag`
      - `+ singleNodeJobType`
  - **ShowJob**
    - changes of response param
      - `+ singleNodeJobFlag`
      - `+ singleNodeJobType`
  - **UpdateJob**
    - changes of request param
      - `+ singleNodeJobFlag`
      - `+ singleNodeJobType`
  - **CreateSupplementdata**
    - changes of request param
      - `+ singleNodeJobFlag`
      - `+ singleNodeJobType`
      - `+ dependJobs.singleNodeJobFlag`
      - `+ dependJobs.singleNodeJobType`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the API `ListJobs`
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
  - **ShowAssetStatistic**
    - changes of response param
      - `+ environment_num`
      - `+ core_conf_file_num`
  - **ListPorts**
    - changes of response param
      - `+ data_list.agent_id`
      - `+ data_list.container_id`
  - **ListSwrImageRepository**
    - changes of response param
      - `+ data_list.instance_name`
      - `+ data_list.instance_id`
      - `+ data_list.instance_url`

### HuaweiCloud SDK Kafka

- _Features_
  - Support the APIs `CreateShrinkageJob`, `ShowShrinkCheckResult`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK MetaStudio

- _Features_
  - Support the following APIs:
    - `ListDigitalHumanVideo`
    - `ListInteractionRuleGroups`
    - `CreateInteractionRuleGroup`
    - `UpdateInteractionRuleGroup`
    - `DeleteInteractionRuleGroup`
    - `CheckTextLanguage`
    - `CreateFacialAnimations`
    - `ListFacialAnimationsData`
- _Bug Fix_
  - None
- _Change_
  - **CreateFile**
    - changes of response param
      - `- file_id`
      - `- upload_url`
  - **ExecuteSmartLiveCommand**
    - changes of request param
      - `+ review_config`
      - `+ command: enum value [GET_CURRENT_PLAYING_SCRIPTS]`
  - **CreatePictureModelingByUrlJob**
    - changes of request param
      - `- X-User-Privilege`
  - **ListAssetSummary**
    - changes of response param
      - `+ asset_list.asset_type: enum value [AUDIO]`
  - **Create2DDigitalHumanVideo**
    - changes of request param
      - `+ review_config`
      - `+ callback_config`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
  - **Show2DDigitalHumanVideo**
    - changes of response param
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
  - **CreatePhotoDigitalHumanVideo**
    - changes of request param
      - `+ review_config`
      - `- video_config.disable_system_watermark`
  - **ShowPhotoDigitalHumanVideo**
    - changes of response param
      - `- video_config.disable_system_watermark`
  - **LiveEventReport**
    - changes of request param
      - `+ review_config`
  - **CreateTtsa**
    - changes of request param
      - `- X-User-Privilege`
      - `+ script_type`
      - `+ audio_file_download_url`
      - `+ job_type`
      - `- parent_job_id`
      - `- auto_motion`
  - **ListTtsaJobs**
    - changes of response param
      - `+ ttsa_jobs.job_type`
  - **ListTtsaData**
    - changes of response param
      - `+ start_time`
      - `+ end_time`
      - `+ is_tail`
  - **ListStyles**
    - changes of response param
      - `- styles.extra_meta.edit_value_items`
      - `- styles.extra_meta.edit_color_items`
      - `- styles.extra_meta.edit_components`
      - `- styles.extra_meta.modelling_algorithm`
  - **CreateDigitalHumanBusinessCard**
    - changes of request param
      - `+ introduction_type`
      - `+ introduction_audio_asset_id`
      - `+ review_config`
    - changes of response param
      - `- job_id`
  - **UpdateDigitalHumanBusinessCard**
    - changes of request param
      - `+ introduction_type`
      - `+ introduction_audio_asset_id`
      - `+ review_config`
    - changes of response param
      - `- job_id`
  - **ShowDigitalHumanBusinessCard**
    - changes of response param
      - `+ introduction_audio_asset_id`
      - `+ introduction_type`
  - **ShowSmartLive**
    - changes of response param
      - `+ stream_duration`
      - `+ block_reason`
      - `+ live_event_callback_config`
      - `+ state: enum value [BLOCKED]`
      - `+ rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **ListVideoScripts**
    - changes of request param
      - `+ name`
      - `+ script_catalog`
      - `+ view_mode`
    - changes of response param
      - `+ video_scripts.script_cover_url`
      - `+ video_scripts.script_type`
      - `+ video_scripts.text`
      - `- video_scripts.video_making_type`
      - `- video_scripts.human_image`
  - **ShowVideoScript**
    - changes of response param
      - `+ script_cover_url`
      - `+ review_config`
      - `- video_making_type`
      - `- human_image`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
      - `* shoot_scripts: list<ShootScriptItem> -> list<ShootScriptShowItem>`
  - **CreatePictureModelingJob**
    - changes of request param
      - `- X-User-Privilege`
    - changes of response param
      - `- model_asset_id`
      - `- job_id`
  - **ShowVideoMotionCaptureJob**
    - changes of response param
      - `+ input_info.rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **ShowAsset**
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of request param
      - `+ room_type`
    - changes of response param
      - `+ smart_live_rooms.room_type`
      - `+ smart_live_rooms.room_state`
      - `+ smart_live_rooms.error_info`
      - `+ smart_live_rooms.model_infos.backup_model_asset_ids`
  - **CreateSmartLiveRoom**
    - changes of request param
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
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of request param
      - `+ stream_keys`
      - `+ interaction_callback_url`
      - `+ live_event_callback_config`
      - `+ video_config.subtitle_config`
      - `- video_config.disable_system_watermark`
      - `+ video_config.codec: enum value [VP9]`
      - `+ play_policy.random_play_mode`
    - changes of response param
      - `+ live_warning_info`
      - `+ live_event_callback_config`
      - `+ rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **ListSmartLive**
    - changes of response param
      - `+ stream_duration`
      - `+ block_reason`
      - `+ live_event_callback_config`
      - `+ smart_live_jobs.live_event_callback_config`
      - `+ smart_live_jobs.stream_duration`
      - `+ smart_live_jobs.block_reason`
      - `+ smart_live_jobs.state: enum value [BLOCKED]`
      - `+ smart_live_jobs.rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **CreateVideoMotionCaptureJob**
    - changes of request param
      - `+ input_info.rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
    - changes of response param
      - `- rtc_room_info`
      - `- job_id`
      - `+ rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **ListVideoMotionCaptureJobs**
    - changes of response param
      - `+ video_motion_capture_jobs.input_info.rtc_room_info.users.user_type: enum value [INFERENCE_USER,END_USER]`
  - **CreateDigitalAsset**
    - changes of request param
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
    - changes of request param
      - `- asset_manage_type`
      - `- X-User-MePrivilege`
    - changes of response param
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

- _Features_
  - Support the APIs `SetInstancesNewDbShrink`, `StopBackup`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.74 2023-12-22

### HuaweiCloud SDK Config

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowTrackerConfig**
    - changes of response param
      - `+ channel.obs.bucket_prefix`
  - **CreateTrackerConfig**
    - changes of request param
      - `+ channel.obs.bucket_prefix`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowGroups**
    - changes of response param
      - `* group.group_message_offsets.lag: int32 -> int64`
  - **ShowInstanceTopicDetail**
    - changes of response param
      - `* partitions.replicas.lag: int32 -> int64`

# 3.1.73 2023-12-21

### HuaweiCloud SDK AS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateScalingConfig**
    - changes of request param
      - `+ instance_config.disk.iops`
      - `+ instance_config.disk.throughput`
      - `+ instance_config.disk.volume_type: enum value [GPSSD2,ESSD2]`
  - **ListScalingConfigs**
    - changes of response param
      - `+ scaling_configurations.instance_config.disk.iops`
      - `+ scaling_configurations.instance_config.disk.throughput`
      - `+ scaling_configurations.instance_config.disk.volume_type: enum value [GPSSD2,ESSD2]`
  - **ShowScalingConfig**
    - changes of response param
      - `+ scaling_configuration.instance_config.disk.iops`
      - `+ scaling_configuration.instance_config.disk.throughput`
      - `+ scaling_configuration.instance_config.disk.volume_type: enum value [GPSSD2,ESSD2]`

### HuaweiCloud SDK CloudPond

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListEdgeSites**
    - changes of response param
      - `+ edge_sites.location.zone_code`
      - `+ edge_sites.location.address`
  - **CreateEdgeSite**
    - changes of request param
      - `+ edge_site.location.address`
      - `+ edge_site.location.zone_code`
    - changes of response param
      - `+ edge_site.location.zone_code`
      - `+ edge_site.location.address`
  - **ShowEdgeSite**
    - changes of response param
      - `+ edge_site.location.zone_code`
      - `+ edge_site.location.address`
  - **UpdateEdgeSite**
    - changes of response param
      - `+ edge_site.location.zone_code`
      - `+ edge_site.location.address`

### HuaweiCloud SDK CloudTable

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateCloudTableCluster**
    - changes of request param
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
    - changes of response param
      - `+ jobId`
      - `+ getJobEndpoint`
  - **CreateCluster**
    - changes of request param
      - `* cluster.instance.nics: list<Nics> -> list<nic>`

### HuaweiCloud SDK CodeArtsPipeline

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowPipelineRunDetail**
    - changes of response param
      - `* current_system_time: string -> int64`
      - `* stages.pre.endpoint_ids: string -> list<string>`

### HuaweiCloud SDK DC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateVifPeer**
    - changes of response param
      - `+ vif_peer.enable_nqa`
      - `+ vif_peer.enable_bfd`
  - **CreateVifPeer**
    - changes of response param
      - `+ vif_peer.enable_nqa`
      - `+ vif_peer.enable_bfd`
  - **ShowDirectConnect**
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
      - `+ hosted_connects.port_type`
      - `+ hosted_connects.type`
      - `+ hosted_connects.status: enum value [PENDING_UPDATE,PENDING_CREATE]`
      - `- hosted_connects.status: enum value [PAID,APPLY,PENDING_SURVEY,DELETED,DENY,PENDING_PAY,ORDERING,ACCEPT,REJECTED]`
  - **CreateHostedDirectConnect**
    - changes of response param
      - `+ hosted_connect.port_type`
      - `+ hosted_connect.type`
      - `+ hosted_connect.status: enum value [PENDING_UPDATE,PENDING_CREATE]`
      - `- hosted_connect.status: enum value [PAID,APPLY,PENDING_SURVEY,DELETED,DENY,PENDING_PAY,ORDERING,ACCEPT,REJECTED]`
  - **ShowHostedDirectConnect**
    - changes of response param
      - `+ hosted_connect.port_type`
      - `+ hosted_connect.type`
      - `+ hosted_connect.status: enum value [PENDING_UPDATE,PENDING_CREATE]`
      - `- hosted_connect.status: enum value [PAID,APPLY,PENDING_SURVEY,DELETED,DENY,PENDING_PAY,ORDERING,ACCEPT,REJECTED]`
  - **UpdateHostedDirectConnect**
    - changes of response param
      - `+ hosted_connect.port_type`
      - `+ hosted_connect.type`
      - `+ hosted_connect.status: enum value [PENDING_UPDATE,PENDING_CREATE]`
      - `- hosted_connect.status: enum value [PAID,APPLY,PENDING_SURVEY,DELETED,DENY,PENDING_PAY,ORDERING,ACCEPT,REJECTED]`
  - **ShowVirtualGateway**
    - changes of response param
      - `+ virtual_gateway.device_id`
      - `+ virtual_gateway.redundant_device_id`
      - `+ virtual_gateway.public_border_group`
  - **UpdateVirtualGateway**
    - changes of response param
      - `+ virtual_gateway.device_id`
      - `+ virtual_gateway.redundant_device_id`
      - `+ virtual_gateway.public_border_group`
  - **ListVirtualGateways**
    - changes of response param
      - `+ virtual_gateways.device_id`
      - `+ virtual_gateways.redundant_device_id`
      - `+ virtual_gateways.public_border_group`
  - **CreateVirtualGateway**
    - changes of response param
      - `+ virtual_gateway.device_id`
      - `+ virtual_gateway.redundant_device_id`
      - `+ virtual_gateway.public_border_group`
  - **ShowVirtualInterface**
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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

- _Features_
  - Support the API `ValidateDeletableReplica`
- _Bug Fix_
  - None
- _Change_
  - **ShowExpireKeyScanInfo**
    - changes of request param
      - `+ offset`
      - `+ limit`
      - `+ status`

### HuaweiCloud SDK DGC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateJob**
    - changes of request param
      - `+ nodes.execTimeOutRetry`
  - **ShowJob**
    - changes of response param
      - `+ nodes.execTimeOutRetry`
  - **UpdateJob**
    - changes of request param
      - `+ nodes.execTimeOutRetry`
  - **CreateSupplementdata**
    - changes of request param
      - `+ dependJobs.nodes.execTimeOutRetry`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BatchCreateJobs**
    - changes of request param
      - `+ jobs.engine_type: enum value [mysql-to-kafka,taurus-to-kafka,gaussdbv5ha-to-kafka]`
      - `+ jobs.source_endpoint.db_type: enum value [taurus]`
  - **BatchValidateConnections**
    - changes of request param
      - `+ jobs.db_type: enum value [taurus]`
  - **ShowJobList**
    - changes of request param
      - `+ engine_type: enum value [gaussdbv5,postgresql,mysql-to-kafka,taurus-to-kafka,gaussdbv5ha-to-kafka]`
  - **BatchUpdateJob**
    - changes of request param
      - `+ jobs.engine_type: enum value [gaussdbv5,postgresql,mysql-to-kafka,taurus-to-kafka,gaussdbv5ha-to-kafka]`
      - `+ jobs.source_endpoint.db_type: enum value [taurus]`
  - **BatchListJobDetails**
    - changes of response param
      - `+ results.source_endpoint.db_type: enum value [taurus]`
      - `+ results.inst_info.engine_type: enum value [gaussdbv5,postgresql,mysql-to-kafka,taurus-to-kafka,gaussdbv5ha-to-kafka]`
  - **ShowJobDetail**
    - changes of request param
      - `+ type: enum value [compare]`
      - `+ type: enum value [comapre]`
      - `+ query_type: enum value [diff]`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BatchCreateServerTags**
    - changes of request param
      - `* tags: list<ServerTag> -> list<BatchAddServerTag>`
  - **UpdateServer**
    - changes of request param
      - `+ server.user_data`

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the APIs `UpdateDisassociatePublicip`, `UpdateAssociatePublicip`

### HuaweiCloud SDK HSS

- _Features_
  - Support the following APIs:
    - `ListProcessesHost`
    - `ListPortHost`
    - `ChangeCheckRuleAction`
    - `ListVulScanTask`
    - `CreateVulnerabilityScanTask`
    - `ListVulScanTaskHost`
- _Bug Fix_
  - None
- _Change_
  - **ShowAssetStatistic**
    - changes of request param
      - `+ category`
    - changes of response param
      - `+ web_app_num`
      - `+ database_num`
      - `+ web_service_num`
  - **ChangeVulScanPolicy**
    - changes of request param
      - `+ scan_vul_types`
  - **ListJarPackageHostInfo**
    - changes of request param
      - `+ part_match`
  - **ListUserStatistics**
    - changes of request param
      - `+ category`
  - **ListPortStatistics**
    - changes of request param
      - `+ category`
  - **ListProcessStatistics**
    - changes of request param
      - `+ category`
  - **ListAppStatistics**
    - changes of request param
      - `+ category`
  - **ListUsers**
    - changes of request param
      - `+ category`
      - `+ part_match`
    - changes of response param
      - `+ data_list.container_id`
      - `+ data_list.container_name`
  - **ListPorts**
    - changes of request param
      - `+ category`
  - **ListApps**
    - changes of request param
      - `+ category`
      - `+ part_match`
    - changes of response param
      - `+ data_list.container_id`
      - `+ data_list.container_name`
  - **ListAutoLaunchs**
    - changes of request param
      - `+ part_match`
  - **ListProtectionServer**
    - changes of response param
      - `+ data_list.agent_version`
  - **ListContainerNodes**
    - changes of request param
      - `+ container_tags`
    - changes of response param
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
    - changes of response param
      - `+ data_list.expire_time`
      - `+ data_list.protect_interrupt`
  - **BatchScanSwrImage**
    - changes of request param
      - `+ image_size`
      - `+ start_latest_update_time`
      - `+ end_latest_update_time`
      - `+ start_latest_scan_time`
      - `+ end_latest_scan_time`
      - `+ image_info_list.instance_id`
      - `+ image_info_list.instance_url`
  - **ListImageVulnerabilities**
    - changes of request param
      - `+ type`
    - changes of response param
      - `+ data_list.app_path`
  - **ListImageRiskConfigs**
    - changes of request param
      - `+ instance_id`
  - **ListImageRiskConfigRules**
    - changes of request param
      - `+ instance_id`
  - **ShowImageCheckRuleDetail**
    - changes of request param
      - `+ instance_id`
  - **ListAlarmWhiteList**
    - changes of response param
      - `+ data_list.white_field`
      - `+ data_list.field_value`
      - `+ data_list.judge_type`
  - **ListSwrImageRepository**
    - changes of request param
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
    - changes of response param
      - `+ data_list.scan_failed_desc`
  - **ListSecurityEvents**
    - changes of request param
      - `+ public_ip`
      - `+ event_name`
    - changes of response param
      - `+ data_list.event_count`
  - **ChangeEvent**
    - changes of request param
      - `+ event_white_rule_list`

### HuaweiCloud SDK IEC

- _Features_
  - Support the APIs `ListBandwidthTypes`, `CreateSubnet`, `CreateInstance`
- _Bug Fix_
  - None
- _Change_
  - **ListSubnets**
    - changes of response param
      - `+ subnets.cidr_v6`
      - `+ subnets.ipv6_enable`
      - `+ subnets.pool_id`
      - `+ subnets.neutron_subnet_id_v6`
      - `+ subnets.gateway_ip_v6`
  - **ShowSubnet**
    - changes of response param
      - `+ subnet.cidr_v6`
      - `+ subnet.ipv6_enable`
      - `+ subnet.pool_id`
      - `+ subnet.neutron_subnet_id_v6`
      - `+ subnet.gateway_ip_v6`
  - **UpdateSubnet**
    - changes of request param
      - `+ subnet.ipv6_enable`
      - `+ subnet.pool_id`
    - changes of response param
      - `+ subnet.ipv6_enable`
      - `+ subnet.neutron_subnet_id_v6`
  - **CreateSecurityGroupRule**
    - changes of request param
      - `+ security_group_rule.ethertype: enum value [IPv6]`
  - **ListPorts**
    - changes of response param
      - `+ ports.ipv6_bandwidth_id`
      - `+ ports.binding:profile`
  - **CreatePort**
    - changes of response param
      - `+ port.ipv6_bandwidth_id`
      - `+ port.binding:profile`
  - **ShowPort**
    - changes of response param
      - `+ port.ipv6_bandwidth_id`
      - `+ port.binding:profile`
  - **UpdatePort**
    - changes of response param
      - `+ port.ipv6_bandwidth_id`
      - `+ port.binding:profile`
  - **CreatePublicIp**
    - changes of request param
      - `+ bandwidth`
  - **ShowEdgeCloud**
    - changes of response param
      - `+ stacks.resources.net_config.allowed_address_pairs`
      - `+ coverage.coverage_sites.demands.pool_id_v6`
      - `+ coverage.coverage_sites.demands.ipv6_bandwidth_enable`
  - **ListEdgeCloud**
    - changes of response param
      - `+ edgeclouds.coverage.coverage_sites.demands.pool_id_v6`
      - `+ edgeclouds.coverage.coverage_sites.demands.ipv6_bandwidth_enable`
  - **CreateDeployment**
    - changes of request param
      - `+ edgecloud.coverage.coverage_sites.demands.bandwidth_type`
      - `+ edgecloud.coverage.coverage_sites.demands.pool_id_v6`
      - `+ edgecloud.coverage.coverage_sites.demands.ipv6_bandwidth_enable`
      - `+ edgecloud.coverage.coverage_sites.demands.ipv6_bandwidth_type`
      - `+ edgecloud.stack.resources.net_config.allowed_address_pairs`
    - changes of response param
      - `+ locations.ipv6_enable`
      - `+ locations.ipv6_bandwidth_enable`
      - `+ locations.pool_id_v6`
  - **ListDeployments**
    - changes of response param
      - `+ deployments.distribution.ipv6_enable`
      - `+ deployments.distribution.ipv6_bandwidth_enable`
      - `+ deployments.distribution.pool_id_v6`
      - `+ deployments.edgecloud.stacks.resources.net_config.allowed_address_pairs`
      - `+ deployments.edgecloud.coverage.coverage_sites.demands.bandwidth_type`
      - `+ deployments.edgecloud.coverage.coverage_sites.demands.pool_id_v6`
      - `+ deployments.edgecloud.coverage.coverage_sites.demands.ipv6_bandwidth_enable`
      - `+ deployments.edgecloud.coverage.coverage_sites.demands.ipv6_bandwidth_type`

### HuaweiCloud SDK IVS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **DetectStandardByNameAndId**
    - changes of request param
      - `+ data.req_data.detail`
      - `+ data.req_data.crop`
  - **DetectStandardByIdCardImage**
    - changes of request param
      - `+ data.req_data.detail`
      - `+ data.req_data.crop`
  - **DetectStandardByVideoAndIdCardImage**
    - changes of request param
      - `+ data.req_data.detail`
  - **DetectStandardByVideoAndNameAndId**
    - changes of request param
      - `+ data.req_data.detail`

### HuaweiCloud SDK Kafka

- _Features_
  - Support the API `SendKafkaMessage`
- _Bug Fix_
  - None
- _Change_
  - Remove the API `CreatePartition`
  - **UpdateInstanceTopic**
    - changes of request param
      - `+ topics.new_partition_brokers`
  - **ListInstanceConsumerGroups**
    - changes of response param
      - `* groups.lag: int32 -> int64`
  - **ListInstances**
    - changes of request param
      - `+ status: enum value [UPGRADING,UPGRADINGFAILED]`

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateTranscodingTask**
    - changes of request param
      - `+ video_process.hls_storage_type`

### HuaweiCloud SDK SFSTurbo

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListFsTasks**
    - changes of response param
      - `* tasks: list<object> -> list<OneFsTaskResp>`
  - **ShowShare**
    - changes of response param
      - `+ tags`
      - `+ enterprise_project_id`
  - **DeleteBackendTarget**
    - changes of response param
      - `+ lifecycle: enum value [FAILED]`
  - **CreateShare**
    - changes of request param
      - `+ share.tags`
  - **ListShares**
    - changes of response param
      - `+ tags`
      - `+ enterprise_project_id`
      - `+ shares.enterprise_project_id`
      - `+ shares.tags`

### HuaweiCloud SDK TICS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowAgentDetail**
    - changes of response param
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

- _Features_
  - Support the APIs `ListAssetDailySummaryLog`, `UpdateStorageMode`, `ShowVodRetrieval`
- _Bug Fix_
  - None
- _Change_
  - **ShowTakeOverAssetDetails**
    - changes of response param
      - `+ transcode_info.output.group_id`
      - `+ transcode_info.output.group_name`
  - **PublishAssets**
    - changes of response param
      - `+ asset_info_array.is_multi_transcode`
      - `+ asset_info_array.play_info_array.group_id`
      - `+ asset_info_array.play_info_array.group_name`
  - **UnpublishAssets**
    - changes of response param
      - `+ asset_info_array.is_multi_transcode`
      - `+ asset_info_array.play_info_array.group_id`
      - `+ asset_info_array.play_info_array.group_name`
  - **ShowAssetMeta**
    - changes of response param
      - `+ asset_info_array.is_multi_transcode`
      - `+ asset_info_array.play_info_array.group_id`
      - `+ asset_info_array.play_info_array.group_name`
  - **ShowAssetDetail**
    - changes of response param
      - `+ transcode_info.output.group_id`
      - `+ transcode_info.output.group_name`
  - **ShowTakeOverTaskDetails**
    - changes of response param
      - `+ assets.transcode_info.output.group_id`
      - `+ assets.transcode_info.output.group_name`

# 3.1.72 2023-12-14

### HuaweiCloud SDK BMS

- _Features_
  - Support the API `DeleteBaremetalServer`
- _Bug Fix_
  - None
- _Change_
  - **CreateBareMetalServers**
    - changes of request param
      - `+ server.root_volume.volumetype: enum value [GPSSD]`
      - `+ server.data_volumes.volumetype: enum value [GPSSD]`

### HuaweiCloud SDK CAE

- _Features_
  - Support the APIs `ShowMonitorSystem`, `CreateMonitorSystem`, `UpdateMonitorSystem`
- _Bug Fix_
  - None
- _Change_
  - **ListComponentConfigurations**
    - changes of response param
      - `+ items.data.spec.instrumentation`
      - `+ items.data.spec.apm_application`
      - `+ items.data.spec.type`
      - `+ items.data.spec.app_name`
      - `+ items.data.spec.instance_name`
      - `+ items.data.spec.env_name`
      - `- items.data.spec.image_pull_policy: enum value [Always,IfNotPresent]`
  - **CreateComponentConfiguration**
    - changes of request param
      - `+ items.data.spec.instrumentation`
      - `+ items.data.spec.apm_application`
      - `+ items.data.spec.type`
      - `+ items.data.spec.app_name`
      - `+ items.data.spec.instance_name`
      - `+ items.data.spec.env_name`
      - `- items.data.spec.image_pull_policy: enum value [Always,IfNotPresent]`

### HuaweiCloud SDK CES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListAlarmTemplates**
    - changes of request param
      - `+ template_type: enum value [system_event,custom_event,system_custom_event]`
  - **CreateAlarmTemplate**
    - changes of request param
      - `+ template_type`
      - `+ policies.period: enum value [0]`
  - **UpdateAlarmTemplate**
    - changes of request param
      - `+ policies.period: enum value [0]`

### HuaweiCloud SDK CFW

- _Features_
  - Support the APIs `CreateFirewall`, `ListJob`, `DeleteFirewall`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CloudTable

- _Features_
  - Support the API `CreateCloudTableCluster`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CodeArtsPipeline

- _Features_
  - Support the API `ShowPipelineDetail`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Config

- _Features_
  - Support the following APIs:
    - `ListTrackedResources`
    - `CountTrackedResources`
    - `ListTrackedResourceTags`
    - `CollectTrackedResourcesSummary`
    - `ShowTrackedResourceDetail`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DLI

- _Features_
  - Support the APIs `DeleteRouteFromEnhancedConnection`, `CreateRouteToEnhancedConnection`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - **ListHostDisk**
    - changes of request param
      - `+ instance_id`
    - changes of response param
      - `+ instance_id`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowResInstanceInfo**
    - changes of response param
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

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateAsyncCommand**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **ShowAsyncDeviceCommand**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **BroadcastMessage**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **CreateCommand**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **ListProperties**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
    - changes of response param
      - `+ request_id`
  - **UpdateProperties**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
    - changes of response param
      - `+ request_id`
  - **CloseDeviceTunnel**
    - changes of request param
      - `+ Sp-Auth-Token`
  - **DeleteDeviceTunnel**
    - changes of request param
      - `+ Sp-Auth-Token`
  - **ShowDeviceTunnel**
    - changes of request param
      - `+ Sp-Auth-Token`
  - **AddTunnel**
    - changes of request param
      - `+ Sp-Auth-Token`
  - **ListDeviceTunnels**
    - changes of request param
      - `+ Sp-Auth-Token`
  - **ShowDeviceMessage**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **CreateMessage**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`
  - **ListDeviceMessages**
    - changes of request param
      - `+ Stage-Auth-Token`
      - `+ Sp-Auth-Token`

### HuaweiCloud SDK Live

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - **ListRecordContents**
    - changes of request param
      - `+ record_type: enum value [PLAN_RECORD,ON_DEMAND_RECORD]`
    - changes of response param
      - `- record_contents.record_type: enum value [PLAN_RECORD,ON_DEMAND_RECORD]`

### HuaweiCloud SDK LTS

- _Features_
  - Support the API `CreateAgencyAccess`
- _Bug Fix_
  - None
- _Change_
  - **ListSqlAlarmRules**
    - changes of response param
      - `+ sql_alarm_rules.is_css_sql`
      - `+ sql_alarm_rules.notification_frequency`
      - `+ sql_alarm_rules.alarm_action_rule_name`
      - `+ sql_alarm_rules.status: enum value [RUNNING 启用,STOPPING 停止]`
      - `- sql_alarm_rules.status: enum value [RUNNING,STOPPING]`
      - `* sql_alarm_rules.frequency: object<Frequency> -> object<FrequencyRespBody>`
  - **UpdateSqlAlarmRule**
    - changes of request param
      - `+ is_css_sql`
      - `+ notification_frequency`
      - `+ alarm_action_rule_name`
      - `* frequency: object<Frequency> -> object<CreateSqlAlarmRuleFrequency>`
    - changes of response param
      - `+ is_css_sql`
      - `+ alarm_action_rule_name`
      - `+ notification_frequency`
      - `+ language: enum value [zh-cn,en-us]`
      - `* frequency: object<Frequency> -> object<FrequencyRespBody>`
  - **CreateSqlAlarmRule**
    - changes of request param
      - `+ is_css_sql`
      - `+ notification_frequency`
      - `+ alarm_action_rule_name`
      - `* frequency: object<Frequency> -> object<CreateSqlAlarmRuleFrequency>`
  - **ListKeywordsAlarmRules**
    - changes of response param
      - `+ keywords_alarm_rules.notification_frequency`
      - `+ keywords_alarm_rules.alarm_action_rule_name`
      - `+ keywords_alarm_rules.status: enum value [RUNNING  启用,STOPPING  停止]`
      - `- keywords_alarm_rules.status: enum value [RUNNING,STOPPING]`
  - **UpdateKeywordsAlarmRule**
    - changes of request param
      - `+ notification_frequency`
      - `+ alarm_action_rule_name`
    - changes of response param
      - `+ alarm_action_rule_name`
      - `+ notification_frequency`
      - `+ language: enum value [zh-cn,en-us]`
      - `- keywords_requests.search_time_range_unit: enum value [minute]`
      - `* keywords_requests: list<KeywordsRequest> -> list<KeywordsResBody>`
      - `* frequency: object<Frequency> -> object<FrequencyRespBody>`
  - **CreateKeywordsAlarmRule**
    - changes of request param
      - `+ notification_frequency`
      - `+ alarm_action_rule_name`
      - `+ keywords_alarm_level: enum value [Critical]`
      - `- keywords_alarm_level: enum value [CRITICAL]`

### HuaweiCloud SDK MRS

- _Features_
  - Support the API `ShowMrsVersionMetadata`, `SwitchClusterTags`, `ShowTagStatus`, `ShowTagQuota`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK NAT

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateNatGatewayTag**
    - changes of request param
      - `+ tag.key`
      - `+ tag.value`
      - `* tag: object -> object<TagBody>`

### HuaweiCloud SDK RDS

- _Features_
  - Support the APIs `ListLogLtsConfigs`, `SetLogLtsConfigs`, `DeleteLogLtsConfigs`
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
  - **CreateRocketMqMigrationTask**
    - changes of request param
      - `+ topicConfigTable`
      - `+ subscriptionGroupTable`
      - `+ vhosts`
      - `+ queues`
      - `+ exchanges`
      - `+ bindings`
      - `* body: map<string, object> -> object<CreateRocketMqMigrationTaskReq>`

### HuaweiCloud SDK SecMaster

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListAlerts**
    - changes of request param
      - `* condition.conditions.data: list<object> -> list<string>`
      - `* condition.logics: list<object> -> list<string>`
  - **ListIncidents**
    - changes of request param
      - `* condition.conditions.data: list<object> -> list<string>`
      - `* condition.logics: list<object> -> list<string>`
  - **ListIndicators**
    - changes of request param
      - `* condition: string -> object`
  - **ListDataobjectRelations**
    - changes of request param
      - `* condition.conditions.data: list<object> -> list<string>`
      - `* condition.logics: list<object> -> list<string>`

### HuaweiCloud SDK SMS

- _Features_
  - Support the APIs `ShowConsistencyResult`, `UpdateConsistencyResult`
- _Bug Fix_
  - None
- _Change_
  - **UpdateTaskStatus**
    - changes of request param
      - `+ is_need_consistency_check`
  - **ListServers**
    - changes of request param
      - `+ is_consistency_result_exist`
    - changes of response param
      - `+ source_servers.is_consistency_result_exist`

# 3.1.71 2023-12-07

### HuaweiCloud SDK AOS

- _Features_
  - Support the API `DeleteStackInstance`
- _Bug Fix_
  - None
- _Change_
  - **ListStackSetOperations**
    - changes of response param
      - `+ stack_set_operations.action: enum value [UPDATE_STACK_INSTANCES]`
  - **ShowStackSetOperationMetadata**
    - changes of response param
      - `+ action: enum value [UPDATE_STACK_INSTANCES]`

### HuaweiCloud SDK APIG

- _Features_
  - Support the API `CheckApiGroupsV2`
- _Bug Fix_
  - None
- _Change_
  - **CreatePrepayResize**
    - changes of request param
      - `+ instance_id`
  - **ListPluginAttachableApis**
    - changes of request param
      - `* env_id: optional -> required`
  - **ListApisV2**
    - changes of request param
      - `+ return_data_mode`

### HuaweiCloud SDK CBH

- _Features_
  - Support the API `LoginCbh`
- _Bug Fix_
  - None
- _Change_
  - **ShowAvailableZoneInfo**
    - changes of response param
      - `* availability_zone: object<AvailabilityZones> -> list<AvailabilityZones>`

### HuaweiCloud SDK Cloudtest

- _Features_
  - Support the API `ShowProjectDataDashboard`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CodeArtsPipeline

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowPipelineLog**
    - changes of request param
      - `- level`
      - `- job_run_id`

### HuaweiCloud SDK DataArtsStudio

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - **DeleteApi**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **PublishApi**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowApplyDetail**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowMessageDetail**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowCatalogDetail**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **UpdateCatalog**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **CreateServiceCatalog**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **DeleteServiceCatalog**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **MigrateCatalog**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **MigrateApi**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **SearchIdByPath**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowPathById**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **PublishApiToInstance**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ExecuteApiToInstance**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **AuthorizeApiToInstance**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **AuthorizeActionApiToInstance**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **DeleteApp**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowAppInfo**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **UpdateApp**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowApisOverview**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowAppsOverview**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowApisDetail**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowAppsDetail**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **UpdateFactoryJobName**
    - changes of request param
      - `- x-Auth-Token`
  - **BatchApproveApply**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListApply**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ConfirmMessage**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListMessage**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListAllCatalogList**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListCatalogList**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowPathObjectById**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **DebugApi**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **SearchPublishInfo**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListInstanceList**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **SearchDebugInfo**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListApicInstances**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListApicGroups**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **CreateApp**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListApps**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListApisTop**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListAppsTop**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowApisDashboard**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowApiDashboard**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowAppsDashboard**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListApiTopN**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListApis**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **CreateApi**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ShowApi**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **UpdateApi**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **ListApiCatalogList**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **SearchAuthorizeApp**
    - changes of request param
      - `* Dlm-Type: required -> optional`
  - **SearchBindApi**
    - changes of request param
      - `* Dlm-Type: required -> optional`

### HuaweiCloud SDK DGC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowJobInstance**
    - changes of response param
      - `* planTime: int32 -> int64`
      - `* startTime: int32 -> int64`
      - `* endTime: int32 -> int64`
      - `* executeTime: int32 -> int64`
      - `* nodes.planTime: int32 -> int64`
      - `* nodes.startTime: int32 -> int64`
      - `* nodes.endTime: int32 -> int64`
      - `* nodes.executeTime: int32 -> int64`
  - **ListJobs**
    - changes of request param
      - `+ tags`

### HuaweiCloud SDK DLI

- _Features_
  - Support the APIs `ListJobAuthInfos`, `UpdateJobAuthInfo`, `CreateJobAuthInfo`, `DeleteJobAuthInfo`
- _Bug Fix_
  - None
- _Change_
  - Deprecate the following APIs:
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

- _Features_
  - Support the APIs `ShowEquipmentWlan`, `UpdateEquipmentWlan`
- _Bug Fix_
  - None
- _Change_
  - **ShowEquipmentInfo**
    - changes of response param
      - `+ type: enum value [soho]`
  - **UpdateEquipmentInfo**
    - changes of response param
      - `+ type: enum value [soho]`
  - **GenerateInitialConfiguration**
    - changes of response param
      - `+ url_config_content`
      - `+ script_config_content`
      - `- config_content`
  - **ShowEquipmentSpecificConfig**
    - changes of request param
      - `+ equipment_id`
      - `- equipment_type`
    - changes of response param
      - `- model`
  - **CreateEquipment**
    - changes of request param
      - `+ type: enum value [soho]`
    - changes of response param
      - `+ type: enum value [soho]`
  - **ListEquipments**
    - changes of response param
      - `+ equipments.type: enum value [soho]`
  - **ShowIegInfo**
    - changes of response param
      - `+ equipment_infos.type: enum value [soho]`
  - **UpdateIeg**
    - changes of response param
      - `+ equipment_infos.type: enum value [soho]`
  - **ListIeg**
    - changes of response param
      - `+ intelligent_enterprise_gateways.equipment_infos.type: enum value [soho]`

### HuaweiCloud SDK EG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDetailOfEvent**
    - changes of request param
      - `+ channel_id`
  - **DeleteChannel**
    - changes of request param
      - `+ enterprise_project_id`
  - **ShowDetailOfChannel**
    - changes of request param
      - `+ enterprise_project_id`
    - changes of response param
      - `+ eps_id`
  - **UpdateChannel**
    - changes of request param
      - `+ enterprise_project_id`
      - `+ eps_id`
      - `+ cross_account`
      - `+ policy`
    - changes of response param
      - `+ eps_id`
  - **CreateChannel**
    - changes of request param
      - `+ enterprise_project_id`
      - `+ eps_id`
      - `+ cross_account`
      - `+ policy`
    - changes of response param
      - `+ eps_id`
  - **ListChannels**
    - changes of request param
      - `+ eps_id`
    - changes of response param
      - `+ eps_id`
      - `+ items.eps_id`
  - **CreateSubscriptionTarget**
    - changes of request param
      - `+ eg_detail`
      - `- detail.url`
      - `- detail.agency_name`
      - `- detail.invocation_http_parameters`
      - `* detail: object<Detail> -> object`
  - **UpdateSubscriptionTarget**
    - changes of request param
      - `+ eg_detail`
      - `- detail.url`
      - `- detail.agency_name`
      - `- detail.invocation_http_parameters`
      - `* detail: object<Detail> -> object`
  - **ShowDetailOfConnection**
    - changes of response param
      - `+ kafka_detail.security_protocol`
  - **UpdateConnection**
    - changes of response param
      - `+ kafka_detail.security_protocol`
  - **UpdateSubscription**
    - changes of request param
      - `+ targets.eg_detail`
      - `- targets.detail.url`
      - `- targets.detail.agency_name`
      - `- targets.detail.invocation_http_parameters`
      - `* targets.detail: object<Detail> -> object`
  - **CreateConnection**
    - changes of request param
      - `+ kafka_detail.security_protocol`
    - changes of response param
      - `+ kafka_detail.security_protocol`
  - **ListConnections**
    - changes of response param
      - `+ items.kafka_detail.security_protocol`
  - **ShowEventStreaming**
    - changes of response param
      - `+ source.source_mobile_rocketmq`
      - `+ source.source_kafka.security_protocol`
      - `+ sink.sink_kafka`
      - `+ sink.name: enum value [HC.FunctionGraph,HC.Kafka]`
      - `- sink.name: enum value [HC.FG]`
  - **UpdateEventStreaming**
    - changes of request param
      - `+ source.source_mobile_rocketmq`
      - `+ source.source_kafka.security_protocol`
      - `+ sink.sink_kafka`
      - `+ sink.name: enum value [HC.FunctionGraph,HC.Kafka]`
      - `- sink.name: enum value [HC.FG]`
  - **CreateSubscription**
    - changes of request param
      - `+ targets.eg_detail`
      - `- targets.detail.url`
      - `- targets.detail.agency_name`
      - `- targets.detail.invocation_http_parameters`
      - `* targets.detail: object<Detail> -> object`
  - **CreateEventStreaming**
    - changes of request param
      - `+ source.source_mobile_rocketmq`
      - `+ source.source_kafka.security_protocol`
      - `+ sink.sink_kafka`
      - `+ sink.name: enum value [HC.FunctionGraph,HC.Kafka]`
      - `- sink.name: enum value [HC.FG]`
  - **ListEventStreaming**
    - changes of request param
      - `+ name`
      - `+ fuzzy_name`
    - changes of response param
      - `+ source.source_mobile_rocketmq`
      - `+ source.source_kafka.security_protocol`
      - `+ sink.sink_kafka`
      - `+ sink.name: enum value [HC.FunctionGraph,HC.Kafka]`
      - `- sink.name: enum value [HC.FG]`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following APIs:
    - `ShowDependcy`
    - `UpdateDependcy`
    - `DeleteDependency`
    - `AsyncInvokeReservedFunction`
    - `CreateDependency`
  - **ShowFuncReservedInstanceMetrics**
    - changes of request param
      - `+ marker`
      - `+ limit`
  - **ListFunctionApplications**
    - changes of request param
      - `+ limit`
      - `+ marker`
  - **ListStatistics**
    - changes of request param
      - `+ limit`
      - `+ marker`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the APIs `ListGaussMySqlInstancesUnifyStatus`, `ShowGaussMySqlInstanceInfoUnifyStatus`, `ListGaussMySqlInstanceDetailInfoUnifyStatus`, `SwitchGaussMySqlProxySsl`
- _Bug Fix_
  - None
- _Change_
  - **ShowGaussMySqlProxyList**
    - changes of response param
      - `+ proxy_list.proxy.ssl_option`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the API `OfflineNodes`
- _Bug Fix_
  - None
- _Change_
  - **ListLtsConfigs**
    - changes of response param
      - `* instance_lts_configs.instance.supported_log_types: string -> list<string>`

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ResetDeviceSecret**
    - changes of request param
      - `+ secret_type`
    - changes of response param
      - `+ secret_type`
  - **ResetFingerprint**
    - changes of request param
      - `+ fingerprint_type`
    - changes of response param
      - `+ fingerprint_type`
  - **ShowDevice**
    - changes of response param
      - `+ auth_info.secondary_secret`
      - `+ auth_info.secondary_fingerprint`
      - `* auth_info: object<AuthInfo> -> object<AuthInfoRes>`
  - **UpdateDevice**
    - changes of response param
      - `+ auth_info.secondary_secret`
      - `+ auth_info.secondary_fingerprint`
      - `* auth_info: object<AuthInfo> -> object<AuthInfoRes>`
  - **AddDevice**
    - changes of response param
      - `+ auth_info.secondary_secret`
      - `+ auth_info.secondary_fingerprint`
      - `* auth_info: object<AuthInfo> -> object<AuthInfoRes>`

### HuaweiCloud SDK KooMessage

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateAimPersonalTemplate**
    - changes of request param
      - `+ pages.contents.button_type`

### HuaweiCloud SDK MRS

- _Features_
  - Support the APIs `UpdateAutoScalingPolicy`, `CreateAutoScalingPolicy`, `DeleteAutoScalingPolicy`
- _Bug Fix_
  - None
- _Change_
  - **ShowAutoScalingPolicy**
    - changes of response param
      - `+ auto_scaling_policy.tags`
      - `- auto_scaling_policy.exec_scripts`
      - `* auto_scaling_policy: object<AutoScalingPolicy> -> object<AutoScalingPolicyInfo>`

### HuaweiCloud SDK NAT

- _Features_
  - Support the following APIs:
    - `ListNatGatewayByTag`
    - `BatchCreateDeleteNatGatewayTag`
    - `ShowNatGatewayTag`
    - `CreateNatGatewayTag`
    - `DeleteNatGatewayTag`
    - `ListNatGatewayTag`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OMS

- _Features_
  - Support the API `BatchUpdateTasks`
- _Bug Fix_
  - None
- _Change_
  - **ShowSyncTask**
    - changes of response param
      - `+ dst_storage_policy`
      - `+ object_overwrite_mode`
  - **ListSyncTasks**
    - changes of response param
      - `+ tasks.object_overwrite_mode`
      - `+ tasks.dst_storage_policy`

### HuaweiCloud SDK RocketMQ

- _Features_
  - Support the APIs `ShowRocketMqConfigs`, `UpdateRocketMqConfigs`
- _Bug Fix_
  - None
- _Change_
  - **ListInstances**
    - changes of request param
      - `+ status: enum value [UPGRADING,UPGRADINGFAILED]`

### HuaweiCloud SDK SFSTurbo

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **SetHpcCacheBackend**
    - changes of request param
      - `* update_hpc_cache.data.nas.type: object -> string`
      - `* update_hpc_cache.data.nas.url: object -> string`

# 3.1.70 2023-11-30

### HuaweiCloud SDK DIS

- _Features_
  - Support `DIS`
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
  - **ListPermissions**
    - changes of response param
      - `* : map<string, AuthModel> -> string`
  - **ListAccessCode**
    - changes of response param
      - `- access_codes.status: enum value [enable,unenable]`

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSubCustomerBillDetail**
    - changes of response param
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

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListBandwidthPackageTags**
    - changes of response param
      - `+ tags.values`
      - `- tags.value`
      - `* tags: list<Tag> -> list<MultivaluedTag>`

### HuaweiCloud SDK CCE

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - **ResizeCluster**
    - changes of request param
      - `* extendParam: object<ResizeClusterRequestExtendParam> -> object`
  - **UpdateClusterEip**
    - changes of request param
      - `* spec: object -> object<MasterEIPRequestSpec>`
    - changes of response param
      - `* spec: object -> object<MasterEIPResponseSpec>`
  - **ShowClusterEndpoints**
    - changes of response param
      - `* spec: object -> object<OpenAPISpec>`
  - **ShowAddonInstance**
    - changes of response param
      - `- status.status: enum value [unknown]`
  - **UpdateAddonInstance**
    - changes of response param
      - `- status.status: enum value [unknown]`
  - **RollbackAddonInstance**
    - changes of response param
      - `- status.status: enum value [unknown]`
  - **ShowCluster**
    - changes of response param
      - `+ spec.enableMasterVolumeEncryption`
  - **UpdateCluster**
    - changes of response param
      - `+ spec.enableMasterVolumeEncryption`
  - **DeleteCluster**
    - changes of request param
      - `+ ondemand_node_policy`
      - `+ periodic_node_policy`
    - changes of response param
      - `+ spec.enableMasterVolumeEncryption`
  - **CreateAddonInstance**
    - changes of response param
      - `- status.status: enum value [unknown]`
  - **ListAddonInstances**
    - changes of response param
      - `- items.status.status: enum value [unknown]`
  - **CreateCluster**
    - changes of request param
      - `+ spec.enableMasterVolumeEncryption`
    - changes of response param
      - `+ spec.enableMasterVolumeEncryption`
  - **ListClusters**
    - changes of request param
      - `+ status: enum value [Hibernating,Hibernation,Awaking]`
    - changes of response param
      - `+ items.spec.enableMasterVolumeEncryption`
  - **ShowNode**
    - changes of response param
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
  - **UpdateNode**
    - changes of response param
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
  - **DeleteNode**
    - changes of response param
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
  - **CreateNode**
    - changes of request param
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
    - changes of response param
      - `+ spec.hostnameConfig`
      - `+ spec.extendParam.kubeReservedMem`
      - `+ spec.extendParam.systemReservedMem`
      - `+ spec.extendParam.init-node-password`
      - `- spec.extendParam.kube-reserved-mem`
      - `- spec.extendParam.system-reserved-mem`
  - **ListNodes**
    - changes of response param
      - `+ items.spec.hostnameConfig`
      - `+ items.spec.extendParam.kubeReservedMem`
      - `+ items.spec.extendParam.systemReservedMem`
      - `+ items.spec.extendParam.init-node-password`
      - `- items.spec.extendParam.kube-reserved-mem`
      - `- items.spec.extendParam.system-reserved-mem`
  - **ShowNodePool**
    - changes of response param
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
  - **UpdateNodePool**
    - changes of response param
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
  - **DeleteNodePool**
    - changes of response param
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
  - **AddNode**
    - changes of request param
      - `+ nodeList.spec.hostnameConfig`
  - **ResetNode**
    - changes of request param
      - `+ nodeList.spec.hostnameConfig`
  - **CreateNodePool**
    - changes of request param
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
    - changes of response param
      - `+ spec.nodeTemplate.hostnameConfig`
      - `+ spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ spec.nodeTemplate.extendParam.init-node-password`
      - `- spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- spec.nodeTemplate.extendParam.system-reserved-mem`
  - **ListNodePools**
    - changes of response param
      - `+ items.spec.nodeTemplate.hostnameConfig`
      - `+ items.spec.nodeTemplate.extendParam.kubeReservedMem`
      - `+ items.spec.nodeTemplate.extendParam.systemReservedMem`
      - `+ items.spec.nodeTemplate.extendParam.init-node-password`
      - `- items.spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `- items.spec.nodeTemplate.extendParam.system-reserved-mem`

### HuaweiCloud SDK CodeArtsPipeline

- _Features_
  - Support the API `ShowPipelineLog`
- _Bug Fix_
  - None
- _Change_
  - **UpdatePluginBaseInfo**
    - changes of request param
      - `+ plugin_composition_type`
  - **CreatePublisher**
    - changes of request param
      - `+ description`
  - **ListPublisher**
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
      - `+ publisher_detail_map`
      - `- body`
  - **CreateBasicPlugin**
    - changes of request param
      - `+ plugin_composition_type`
  - **UpdateBasicPlugin**
    - changes of request param
      - `+ plugin_composition_type`
  - **CreateStrategy**
    - changes of request param
      - `- type`
      - `- rules.type`
      - `- rules.name`
      - `- rules.layout_content`
      - `- rules.plugin_id`
      - `- rules.plugin_name`
      - `- rules.plugin_version`
      - `- rules.content`
  - **UpdateStrategy**
    - changes of request param
      - `- parent_id`
      - `- rules.type`
      - `- rules.name`
      - `- rules.layout_content`
      - `- rules.plugin_id`
      - `- rules.plugin_name`
      - `- rules.plugin_version`
      - `- rules.content`

### HuaweiCloud SDK DataArtsStudio

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **SearchAtomicIndexes**
    - changes of response param
      - `+ data.value`
  - **ShowAtomicIndexById**
    - changes of response param
      - `+ data.value`
  - **ListDerivativeIndexes**
    - changes of response param
      - `+ data.value`
  - **ShowDerivativeIndexById**
    - changes of response param
      - `+ data.value`
  - **ListCompoundMetrics**
    - changes of response param
      - `+ data.value`
  - **ShowCompoundMetricById**
    - changes of response param
      - `+ data.value`
  - **ListApiCatalogList**
    - changes of response param
      - `+ apis.publish_messages`
  - **ParseUserBehavior**
    - changes of request param
      - `+ params.filter.attribute: enum value [base.DataAsset.sourceType,typeName,classifications.name,tags.name,securityLevel.name,workspaceId]`
      - `+ params.filter.operator: enum value [IN,EQ]`
      - `* params.filter.value: object -> list<string>`
      - `* params.filter.condition: object<ConditionInfo> -> string`
  - **ShowDataSets**
    - changes of request param
      - `+ filter.attribute: enum value [base.DataAsset.sourceType,typeName,classifications.name,tags.name,securityLevel.name,workspaceId]`
      - `+ filter.operator: enum value [IN,EQ]`
      - `* filter.value: object -> list<string>`
      - `* filter.condition: object<ConditionInfo> -> string`
    - changes of response param
      - `* facets: object -> list<object>`
  - **ListApis**
    - changes of request param
      - `+ x-return-publish-messages`
    - changes of response param
      - `+ records.publish_messages`
  - **ShowApi**
    - changes of response param
      - `+ publish_messages`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSlowlog**
    - changes of response param
      - `+ total_num`

### HuaweiCloud SDK DLI

- _Features_
  - Support the API `ShowQuota`
- _Bug Fix_
  - None
- _Change_
  - **ListQueueProperties**
    - changes of request param
      - `+ offset`
      - `+ limit`
      - `- page`
      - `- page_size`

### HuaweiCloud SDK EIP

- _Features_
  - Support the APIs `BatchModifyBandwidth`, `ListEipBandwidths`, `ListBandwidthsLimit`, `UpdatePublicip`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the API `ListInfluxdbSlowLogs`
- _Bug Fix_
  - None
- _Change_
  - **ListLtsConfigs**
    - changes of response param
      - `+ instance_lts_configs.instance.supported_log_types`

### HuaweiCloud SDK Moderation

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RunQueryDocumentModerationJob**
    - changes of response param
      - `+ result.details.start_position`
      - `+ result.details.end_position`
      - `+ result.details.image_url`

### HuaweiCloud SDK RDS

- _Features_
  - Support the API `SetInstancesDbShrink`
- _Bug Fix_
  - None
- _Change_
  - **UpgradeDbMajorVersion**
    - changes of response param
      - `+ job_id`
  - **ShowUpgradeDbMajorVersionStatus**
    - changes of response param
      - `+ check_expiration_time`
      - `- report_expiration_time`
  - **StartResizeFlavorAction**
    - changes of response param
      - `+ order_id`
  - **StartInstanceEnlargeVolumeAction**
    - changes of response param
      - `+ order_id`
  - **StartInstanceSingleToHaAction**
    - changes of response param
      - `+ order_id`
  - **ListHistoryDatabase**
    - changes of request param
      - `+ engine`
      - `- database_name`

### HuaweiCloud SDK RocketMQ

- _Features_
  - Support the APIs `ShowEngineInstanceExtendProductInfo`, `ResizeInstance`
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
  - **RecognizeFlashAsr**
    - changes of request param
      - `* obs_bucket_name: optional -> required`
      - `* obs_object_key: optional -> required`

# 3.1.69 2023-11-23

### HuaweiCloud SDK CFW

- _Features_
  - Support the APIs `ListLogConfig`, `UpdateLogConfig`, `AddLogConfig`, `CreateEastWestFirewall`
- _Bug Fix_
  - None
- _Change_
  - **ListFlowLogs**
    - changes of response param
      - `* data.records.start_time: int32 -> int64`
      - `* data.records.end_time: int32 -> int64`
      - `* data.records.src_port: string -> int32`
      - `* data.records.dst_port: string -> int32`
  - **ListAccessControlLogs**
    - changes of response param
      - `* data.records.hit_time: int32 -> int64`
      - `* data.records.src_port: string -> int32`
      - `* data.records.dst_port: string -> int32`
  - **ChangeIpsSwitchStatus**
    - changes of request param
      - `+ X-Language`
  - **ListAttackLogs**
    - changes of response param
      - `* data.records.event_time: string -> int64`
      - `* data.records.attack_rule_id: int32 -> string`
      - `* data.records.packet: object<Packet> -> string`

# 3.1.68 2023-11-23

### HuaweiCloud SDK AOM

- _Features_
  - Support the following APIs:
    - `ListPromInstance`
    - `CreatePromInstance`
    - `DeletePromInstance`
    - `CreateRecordingRule`
    - `ListPermissions`
    - `ListAccessCode`
    - `ListAgents`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CodeArtsPipeline

- _Features_
  - Support the following APIs:
    - `UpdatePluginBaseInfo`
    - `CreatePluginDraft`
    - `PublishPluginDraft`
    - `CreatePluginVersion`
    - `UpdatePluginDraft`
    - `CreatePublisher`
- _Bug Fix_
  - None
- _Change_
  - **SwitchStrategy**
    - changes of response param
      - `+ rule_set_id`
      - `- rule_template_instance_id`
  - **SwitchOpenSourceStrategy**
    - changes of response param
      - `+ rule_set_id`
      - `- rule_template_instance_id`
  - **ShowPublisher**
    - changes of response param
      - `+ body`
  - **CreatePipelineNew**
    - changes of request param
      - `+ group_id`
      - `+ id`
      - `* schedules.days_of_week: string -> list<integer>`
  - **UpdateStrategy**
    - changes of response param
      - `+ rule_set_id`
      - `- rule_template_instance_id`
  - **UpdateOpenSourceStrategy**
    - changes of response param
      - `+ rule_set_id`
      - `- rule_template_instance_id`

### HuaweiCloud SDK CSE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpgradeEngineConfig**
    - changes of request param
      - `+ authType`
      - `- version`
  - **ShowEngine**
    - changes of response param
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
    - changes of request param
      - `+ vpcId`
  - **ListEngines**
    - changes of response param
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
    - changes of response param
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
    - changes of request param
      - `+ match.headers.<header>`
      - `- match.headers.aaaa`
      - `+ route.tags.<tag>`
      - `- route.tags.version`

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListCerts**
    - changes of response param
      - `* defaultCerts: object<DefaultCertsResource> -> list<DefaultCertsResource>`
      - `* customCerts: object<CustomCertsResource> -> list<CustomCertsResource>`

### HuaweiCloud SDK DCS

- _Features_
  - Support the API `LogoffWebCli`
- _Bug Fix_
  - None
- _Change_
  - **ListSlowlog**
    - changes of response param
      - `+ slowlogs.database_id`
      - `+ slowlogs.username`

### HuaweiCloud SDK DDS

- _Features_
  - Support the following APIs:
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
  - **BatchDeleteJobs**
    - changes of request param
      - `+ jobs.is_show_breakpoint_position`
  - **BatchSetPolicy**
    - changes of request param
      - `+ jobs.file_and_position`
      - `+ jobs.gtid_set`
  - **BatchListProgresses**
    - changes of response param
      - `+ results.incre_trans_delay_millis`
  - **ShowJobList**
    - changes of request param
      - `+ instance_ids`
      - `+ instance_ip`

### HuaweiCloud SDK DRS

- _Features_
  - Support the APIs `UploadJdbcDriver`, `ListJdbcDrivers`, `DeleteJdbcDriver`, `SyncJdbcDriver`
- _Bug Fix_
  - None
- _Change_
  - **BatchCreateJobsAsync**
    - changes of request param
      - `+ jobs.policy_config.dml_types`
  - **ListAsyncJobDetail**
    - changes of response param
      - `+ jobs.connection_management`
      - `+ jobs.policy_config.dml_types`
  - **UpdateBatchAsyncJobs**
    - changes of request param
      - `+ jobs.params.policy_config.dml_types`
  - **ShowJobDetail**
    - changes of response param
      - `+ job.connection_management`
      - `+ job.policy_config.dml_types`
  - **UpdateJob**
    - changes of request param
      - `+ job.params.policy_config.dml_types`

### HuaweiCloud SDK ELB

- _Features_
  - Support the following APIs:
    - `BatchAddAvailableZones`
    - `BatchRemoveAvailableZones`
    - `ListMasterSlavePools`
    - `CreateMasterSlavePool`
    - `ShowMasterSlavePool`
    - `DeleteMasterSlavePool`
- _Bug Fix_
  - None
- _Change_
  - **ShowLoadBalancer**
    - changes of response param
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.log_group_id`
      - `+ loadbalancer.log_topic_id`
  - **UpdateLoadBalancer**
    - changes of request param
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.ipv6_vip_address`
    - changes of response param
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.log_group_id`
      - `+ loadbalancer.log_topic_id`
  - **ListListeners**
    - changes of response param
      - `+ listeners.ssl_early_data_enable`
  - **CreateListener**
    - changes of request param
      - `+ listener.ssl_early_data_enable`
    - changes of response param
      - `+ listener.ssl_early_data_enable`
  - **ShowListener**
    - changes of response param
      - `+ listener.ssl_early_data_enable`
  - **UpdateListener**
    - changes of request param
      - `+ listener.ssl_early_data_enable`
    - changes of response param
      - `+ listener.ssl_early_data_enable`
  - **ListLoadBalancers**
    - changes of request param
      - `+ log_topic_id`
      - `+ log_group_id`
    - changes of response param
      - `+ loadbalancers.charge_mode`
      - `+ loadbalancers.log_group_id`
      - `+ loadbalancers.log_topic_id`
  - **CreateLoadBalancer**
    - changes of request param
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.ipv6_vip_address`
    - changes of response param
      - `+ loadbalancer.charge_mode`
      - `+ loadbalancer.log_group_id`
      - `+ loadbalancer.log_topic_id`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the following APIs:
    - `ListAppTemplates`
    - `ShowAppTemplate`
    - `ListFunctionApplications`
    - `CreateFunctionApp`
    - `ShowFunctionApp`
    - `DeleteFunctionApp`
    - `CreateCallbackWorkflow`
- _Bug Fix_
  - None
- _Change_
  - **ImportFunction**
    - changes of response param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ListFunctions**
    - changes of response param
      - `+ functions.pre_stop_handler`
      - `+ functions.pre_stop_timeout`
  - **CreateFunction**
    - changes of request param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
    - changes of response param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ShowFunctionConfig**
    - changes of response param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **UpdateFunctionConfig**
    - changes of request param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
    - changes of response param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **UpdateFunctionMaxInstanceConfig**
    - changes of response param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ListBridgeFunctions**
    - changes of response param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ShowResInstanceInfo**
    - changes of response param
      - `+ resources.resource_detail.pre_stop_handler`
      - `+ resources.resource_detail.pre_stop_timeout`
  - **CreateFunctionVersion**
    - changes of response param
      - `+ pre_stop_handler`
      - `+ pre_stop_timeout`
  - **ListFunctionVersions**
    - changes of response param
      - `+ versions.pre_stop_handler`
      - `+ versions.pre_stop_timeout`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the API `ShowRestoreTables`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Kafka

- _Features_
  - Support the APIs `ShowKafkaUserClientQuota`, `UpdateKafkaUserClientQuotaTask`, `CreateKafkaUserClientQuotaTask`, `DeleteKafkaUserClientQuotaTask`
- _Bug Fix_
  - None
- _Change_
  - **ListInstances**
    - changes of request param
      - `+ status: enum value [DELETING,ERROR,CREATEFAILED,FREEZING,EXTENDING,SHRINKING,EXTENDEDFAILED,CONFIGURING,UPGRADING,UPGRADINGFAILED,ROLLBACK,ROLLBACKFAILED,VOLUMETYPECHANGING]`
      - `+ status: enum value [FAULTY,RESIZING,RESIZING FAILED]`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RecognizeIdCard**
    - changes of request param
      - `+ return_portrait_location`
    - changes of response param
      - `+ result.portrait_location`

### HuaweiCloud SDK OMS

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - **ShowTask**
    - changes of response param
      - `+ source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **ShowTaskGroup**
    - changes of response param
      - `+ source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **CreateTask**
    - changes of request param
      - `+ source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **ListTasks**
    - changes of response param
      - `+ tasks.source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **CreateTaskGroup**
    - changes of request param
      - `+ source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`
  - **ListTaskGroup**
    - changes of response param
      - `+ taskgroups.source_cdn.authentication_type: enum value [TENCENT_COS_A,TENCENT_COS_B,TENCENT_COS_C,TENCENT_COS_D]`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListInstancesDetails**
    - changes of request param
      - `+ status: enum value [DELETING,FREEZING,EXTENDING,SHRINKING,EXTENDEDFAILED,CONFIGURING,UPGRADING,UPGRADINGFAILED,ROLLBACK,ROLLBACKFAILED,VOLUMETYPECHANGING]`
      - `+ status: enum value [STARTING,CLOSING]`

### HuaweiCloud SDK RDS

- _Features_
  - Support the following APIs:
    - `UpgradeDbMajorVersion`
    - `ShowAvailableVersion`
    - `UpgradeDbMajorVersionPreCheck`
    - `ListInspectionHistories`
    - `ListUpgradeHistories`
    - `ShowUpgradeDbMajorVersionStatus`
    - `UpdateTdeStatus`
    - `ShowTdeStatus`
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
  - **ListInstances**
    - changes of request param
      - `+ status: enum value [DELETING,ERROR,CREATEFAILED,FREEZING,EXTENDING,SHRINKING,EXTENDEDFAILED,CONFIGURING,UPGRADING,UPGRADINGFAILED,ROLLBACK,ROLLBACKFAILED,VOLUMETYPECHANGING]`
      - `+ status: enum value [FAULTY,RESIZING,RESIZING FAILED]`

### HuaweiCloud SDK SCM

- _Features_
  - Support the API `DeployCertificate`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SecMaster

- _Features_
  - Support the following APIs:
    - `ListDataclass`
    - `ListDataclassFields`
    - `ListWorkflows`
    - `CreateDataspace`
    - `CreatePipe`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ServiceStage

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateInstance**
    - changes of request param
      - `+ configuration.container_spec`
  - **ChangeInstance**
    - changes of request param
      - `+ configuration.container_spec`

### HuaweiCloud SDK VOD

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateAssetByFileUpload**
    - changes of request param
      - `+ thumbnail.quantity`
      - `+ thumbnail.quantity_time`
      - `+ thumbnail.type: enum value [quantity]`
  - **PublishAssetFromObs**
    - changes of request param
      - `+ thumbnail.quantity`
      - `+ thumbnail.quantity_time`
      - `+ thumbnail.type: enum value [quantity]`
  - **CreateAssetProcessTask**
    - changes of request param
      - `+ thumbnail.quantity`
      - `+ thumbnail.quantity_time`
      - `+ thumbnail.type: enum value [quantity]`
  - **ListTopStatistics**
    - changes of response param
      - `+ top_urls.duration_ms`
  - **UploadMetaDataByUrl**
    - changes of request param
      - `+ upload_metadatas.thumbnail.quantity`
      - `+ upload_metadatas.thumbnail.quantity_time`
      - `+ upload_metadatas.thumbnail.type: enum value [quantity]`
  - **ListAssetList**
    - changes of response param
      - `+ assets.duration_ms`
  - **ShowTakeOverAssetDetails**
    - changes of response param
      - `+ base_info.meta_data.duration_ms`
  - **PublishAssets**
    - changes of response param
      - `+ asset_info_array.base_info.meta_data.duration_ms`
  - **UnpublishAssets**
    - changes of response param
      - `+ asset_info_array.base_info.meta_data.duration_ms`
  - **ShowAssetMeta**
    - changes of response param
      - `+ asset_info_array.base_info.meta_data.duration_ms`
  - **ShowAssetDetail**
    - changes of response param
      - `+ base_info.meta_data.duration_ms`
      - `+ thumbnail_info.quantity`
  - **ShowTakeOverTaskDetails**
    - changes of response param
      - `+ assets.base_info.meta_data.duration_ms`

# 3.1.67 2023-11-16

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDomainFullConfig**
    - changes of response param
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
    - changes of request param
      - `+ configs.sources.weight`
      - `+ configs.sources.obs_bucket_type`
      - `+ configs.sources.bucket_access_key`
      - `+ configs.sources.bucket_secret_key`
      - `+ configs.sources.bucket_region`
      - `+ configs.sources.bucket_name`
      - `+ configs.compress.file_type`
      - `+ configs.user_agent_filter.ua_list`

### HuaweiCloud SDK CodeArtsBuild

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - **ShowRecordInfo**
    - changes of response param
      - `+ result.duration`

### HuaweiCloud SDK CodeArtsPipeline

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - **ListPipelines**
    - changes of response param
      - `+ pipelines.project_name`
  - **CreatePipelineNew**
    - changes of request param
      - `+ variables`
      - `+ schedules`
      - `+ triggers`
      - `+ manifest_version`
      - `+ definition`
      - `+ project_name`

### HuaweiCloud SDK CSE

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CSMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSecretTags**
    - changes of response param
      - `+ sys_tags.value`
      - `- sys_tags.values`
  - **ListNotificationRecords**
    - changes of request param
      - `+ limit`
      - `+ marker`

### HuaweiCloud SDK DataArtsStudio

- _Features_
  - Support the API `UpdateFactoryJobName`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateVifPeer**
    - changes of response param
      - `+ vif_peer.receive_route_num`
  - **CreateVifPeer**
    - changes of response param
      - `+ vif_peer.receive_route_num`
  - **ShowVirtualInterface**
    - changes of response param
      - `+ virtual_interface.vif_peers.receive_route_num`
  - **UpdateVirtualInterface**
    - changes of response param
      - `+ virtual_interface.vif_peers.receive_route_num`
  - **ListVirtualInterfaces**
    - changes of response param
      - `+ virtual_interfaces.vif_peers.receive_route_num`
  - **CreateVirtualInterface**
    - changes of response param
      - `+ virtual_interface.vif_peers.receive_route_num`

### HuaweiCloud SDK DGC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowScript**
    - changes of response param
      - `+ description`
      - `+ approvers`
      - `+ targetStatus`
      - `+ type: enum value [RDSSQL,PRESTO,ClickHouseSQL,HetuEngineSQL,PYTHON,ImpalaSQL,SparkPython]`
  - **UpdateScript**
    - changes of request param
      - `+ description`
      - `+ approvers`
      - `+ targetStatus`
      - `+ type: enum value [RDSSQL,PRESTO,ClickHouseSQL,HetuEngineSQL,PYTHON,ImpalaSQL,SparkPython]`
  - **CreateScript**
    - changes of request param
      - `+ description`
      - `+ approvers`
      - `+ targetStatus`
      - `+ type: enum value [RDSSQL,PRESTO,ClickHouseSQL,HetuEngineSQL,PYTHON,ImpalaSQL,SparkPython]`
  - **ListScripts**
    - changes of response param
      - `+ description`
      - `+ approvers`
      - `+ targetStatus`
      - `+ scripts.description`
      - `+ scripts.targetStatus`
      - `+ scripts.approvers`
      - `+ scripts.type: enum value [RDSSQL,PRESTO,ClickHouseSQL,HetuEngineSQL,PYTHON,ImpalaSQL,SparkPython]`

### HuaweiCloud SDK DLI

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowSqlJobStatus**
    - changes of response param
      - `+ result_format`
      - `+ result_path`

### HuaweiCloud SDK DNS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreatePrivateZone**
    - changes of request param
      - `+ router.status`
  - **AssociateRouter**
    - changes of request param
      - `+ router.status`
  - **DisassociateRouter**
    - changes of request param
      - `+ router.status`
  - **ShowPrivateZone**
    - changes of response param
      - `+ routers.status`

### HuaweiCloud SDK EdgeSec

- _Features_
  - Support the following APIs:
    - `ListCertificates`
    - `CreateCertificate`
    - `ShowCertificate`
    - `UpdateCertificate`
    - `DeleteCertificate`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the following APIs:
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
- _Bug Fix_
  - None
- _Change_
  - **ListFunctions**
    - changes of response param
      - `+ functions.resource_id`
  - **ShowFunctionConfig**
    - changes of response param
      - `+ func_id`
      - `+ resource_id`
  - **UpdateFunctionConfig**
    - changes of response param
      - `+ func_id`
      - `+ resource_id`
  - **ShowResInstanceInfo**
    - changes of response param
      - `+ resources.resource_detail.resource_id`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateGaussMySqlInstance**
    - changes of response param
      - `* instance.volume.size: string -> int32`

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListFlowBySimCards**
    - changes of request param
      - `+ sim_card_ids`

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowRuleAction**
    - changes of response param
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
  - **UpdateRuleAction**
    - changes of request param
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
    - changes of response param
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
  - **CreateRuleAction**
    - changes of request param
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
    - changes of response param
      - `+ channel_detail.dms_kafka_forwarding.security_protocol`
  - **ListRuleActions**
    - changes of response param
      - `+ actions.channel_detail.dms_kafka_forwarding.security_protocol`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListInstanceConsumerGroups**
    - changes of response param
      - `* groups.createdAt: int32 -> int64`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListTopnTrafficStatistics**
    - changes of response param
      - `+ results.cold_storage`

### HuaweiCloud SDK MRS

- _Features_
  - Support the API `AddComponent`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OCR

- _Features_
  - Support the API `RecognizePeruIdCard`
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
  - Remove the API `ShowRabbitMqProductCores`

### HuaweiCloud SDK RDS

- _Features_
  - Support the API `RevokePostgresqlDbPrivilege`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ServiceStage

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ChangeInstance**
    - changes of request param
      - `+ configuration.env`
      - `+ configuration.storage`
      - `+ configuration.strategy`
      - `+ configuration.lifecycle`
      - `+ configuration.scheduler`
      - `+ configuration.probes`
      - `* configuration: map<string, object> -> object<InstanceConfiguration>`

### HuaweiCloud SDK Workspace

- _Features_
  - Support the APIs `BatchAddDesktopsTags`, `BatchDeleteDesktopsTags`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.66 2023-11-13

### HuaweiCloud SDK DCS

- _Features_
  - Support the interfaces `ShowNodesInformation`, `DeleteCenterTask`, `DeleteDiagnosisTask`
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
  - **ListInstanceTopics**
    - changes of request param
      - `+ offset`
      - `+ limit`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **Createfavorite**
    - changes of request param
      - `+ is_global`
    - changes of response param
      - `+ is_global`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - Support the interfaces `ShowRabbitMqProductCores`, `ShowCesHierarchy`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListPostgresqlListHistoryTables`, `ListHistoryDatabase`, `BatchRestorePostgreSqlTables`, `BatchRestoreDatabase`
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ListInstancesResourceMetrics`, `ListInstancesRecommendation`

# 3.1.65 2023-11-09

### HuaweiCloud SDK TICS

- _Features_
  - Support `TICS`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK VPN

- _Features_
  - Support `VPN`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ASM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowMesh**
    - changes of response param
      - `- spec.region`
      - `- spec.extendParams.clusters.region`
  - **DeleteMesh**
    - changes of response param
      - `- spec.region`
      - `- spec.extendParams.clusters.region`
  - **CreateMesh**
    - changes of request param
      - `- spec.region`
      - `- spec.extendParams.clusters.region`
    - changes of response param
      - `- spec.region`
      - `- spec.extendParams.clusters.region`
  - **ListMeshes**
    - changes of response param
      - `- items.spec.region`
      - `- items.spec.extendParams.clusters.region`

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowAddonInstance**
    - changes of response param
      - `+ status.status: enum value [unknown]`
  - **UpdateAddonInstance**
    - changes of response param
      - `+ status.status: enum value [unknown]`
  - **RollbackAddonInstance**
    - changes of response param
      - `+ status.status: enum value [unknown]`
  - **ShowCluster**
    - changes of response param
      - `+ spec.serviceNetwork`
  - **UpdateCluster**
    - changes of response param
      - `+ spec.serviceNetwork`
  - **DeleteCluster**
    - changes of response param
      - `+ spec.serviceNetwork`
  - **CreateAddonInstance**
    - changes of response param
      - `+ status.status: enum value [unknown]`
  - **ListAddonInstances**
    - changes of response param
      - `+ items.status.status: enum value [unknown]`
  - **CreateCluster**
    - changes of request param
      - `+ spec.serviceNetwork`
    - changes of response param
      - `+ spec.serviceNetwork`
  - **ListClusters**
    - changes of response param
      - `+ items.spec.serviceNetwork`
  - **ShowNode**
    - changes of response param
      - `- status.phase: enum value [Installed,ShutDown]`
  - **UpdateNode**
    - changes of response param
      - `- status.phase: enum value [Installed,ShutDown]`
  - **DeleteNode**
    - changes of response param
      - `- status.phase: enum value [Installed,ShutDown]`
  - **CreateNode**
    - changes of response param
      - `- status.phase: enum value [Installed,ShutDown]`
  - **ListNodes**
    - changes of response param
      - `- items.status.phase: enum value [Installed,ShutDown]`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `CheckMigrationConnectivity`
  - **ListBackupRecords**
    - changes of response param
      - `+ backup_record_response.backup_format`
      - `+ backup_record_response.execution_at`

### HuaweiCloud SDK DLI

- _Features_
  - Support the interfaces `ListQueueProperty`, `UpdateQueueProperty`, `CreateQueueProperty`, `DeleteQueueProperty`
- _Bug Fix_
  - None
- _Change_
  - **ShowSqlJobStatus**
    - changes of response param
      - `+ user_conf`

### HuaweiCloud SDK eiHealth

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowNextflowJob**
    - changes of response param
      - `+ priority`
  - **ListDrugJob**
    - changes of response param
      - `- jobs.priority`
  - **ShowSynthesisJob**
    - changes of response param
      - `- basic_info.priority`
  - **ShowFepJob**
    - changes of response param
      - `- basic_info.priority`
  - **ShowPocketDetectionJob**
    - changes of response param
      - `- basic_info.priority`
  - **ShowAdmetJob**
    - changes of response param
      - `- basic_info.priority`
      - `- models.value_range.lower_inclusive`
      - `- models.value_range.upper_inclusive`
      - `* models.value_range.lower: number -> float`
      - `* models.value_range.upper: number -> float`
      - `* models.value_range: object<ValueRange> -> object<ValueRange2>`
  - **ShowPocketMolDesignJob**
    - changes of response param
      - `- basic_info.priority`
      - `- model_list.value_range.lower_inclusive`
      - `- model_list.value_range.upper_inclusive`
      - `* model_list.value_range.lower: number -> float`
      - `* model_list.value_range.upper: number -> float`
      - `* model_list.value_range: object<ValueRange> -> object<ValueRange2>`
  - **ShowOptmJob**
    - changes of response param
      - `- basic_info.priority`
      - `- models.value_range.lower_inclusive`
      - `- models.value_range.upper_inclusive`
      - `* models.value_range.lower: number -> float`
      - `* models.value_range.upper: number -> float`
      - `* models.value_range: object<ValueRange> -> object<ValueRange2>`
  - **ShowDockingJob**
    - changes of response param
      - `- basic_info.priority`
  - **ListDrugModel**
    - changes of response param
      - `- models.value_range.lower_inclusive`
      - `- models.value_range.upper_inclusive`
      - `* models.value_range.lower: number -> float`
      - `* models.value_range.upper: number -> float`
      - `* models.value_range: object<ValueRange> -> object<ValueRange2>`

### HuaweiCloud SDK GES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListGraphs2**
    - changes of response param
      - `+ graphs.origin_graph_size_type_index`
      - `+ graphs.expand_time`
      - `+ graphs.resize_time`
      - `+ graphs.enable_multi_label`
  - **CreateGraph2**
    - changes of request param
      - `+ graph.enable_multi_label`
  - **ShowGraph2**
    - changes of response param
      - `+ graph.origin_graph_size_type_index`
      - `+ graph.expand_time`
      - `+ graph.resize_time`
      - `+ graph.enable_multi_label`

### HuaweiCloud SDK Kafka

- _Features_
  - Support the interfaces `ShowInstanceConfigs`, `ModifyInstanceConfigs`
- _Bug Fix_
  - None
- _Change_
  - **BatchRestartOrDeleteInstances**
    - changes of request param
      - `+ all_failure`
      - `- allFailure`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BatchRestartOrDeleteInstances**
    - changes of request param
      - `+ all_failure`
      - `- allFailure`

### HuaweiCloud SDK RocketMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BatchDeleteInstances**
    - changes of request param
      - `+ all_failure`
      - `- allFailure`
  - **DeleteRocketMqMigrationTask**
    - changes of request param
      - `+ task_ids`
      - `- taskIds`

### HuaweiCloud SDK SCM

- _Features_
  - Support the interface `BatchPushCertificate`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Workspace

- _Features_
  - Support the following interfaces：
    - `BatchRebuildDesktopsSystemDisk`
    - `ShowDesktopNetwork`
    - `ChangeDesktopNetwork`
    - `ShowTagByDesktopId`
    - `CreateTag`
    - `DeleteTag`
    - `ListProjectTags`
    - `BatchChangeTags`
    - `ListDesktopByTags`
- _Bug Fix_
  - None
- _Change_
  - **BatchDeleteDesktops**
    - changes of request param
      - `+ is_force_delete`
  - **ListDesktops**
    - changes of request param
      - `+ enterprise_project_id`
      - `+ desktop_type`
    - changes of response param
      - `+ desktops.attach_user_infos`
      - `+ desktops.enterprise_project_id`
      - `+ desktops.in_maintenance_mode`
  - **CreateDesktop**
    - changes of request param
      - `+ desktop_name`
      - `+ size`
      - `+ enterprise_project_id`
      - `+ desktop_type: enum value [SHARED]`
      - `+ desktops.user_phone`
  - **ApplyDesktopsInternet**
    - changes of request param
      - `+ enterprise_project_id`
  - **ListDesktopsEips**
    - changes of request param
      - `+ enterprise_project_id`
    - changes of response param
      - `+ eips.enterprise_project_id`
  - **ListUsersOfGroup**
    - changes of request param
      - `+ description`
      - `+ active_type`
    - changes of response param
      - `+ users.description`
  - **ListProducts**
    - changes of response param
      - `+ products.data_disk_size`
      - `+ products.default_desktop_num`
      - `+ products.max_apply_desktop_num`
  - **ListUsers**
    - changes of request param
      - `+ group_name`
  - **ListItaSubJobs**
    - changes of request param
      - `+ desktop_pool_id`
    - changes of response param
      - `+ jobs.desktop_name`
      - `+ jobs.ip_address`
      - `+ jobs.mac_address`
  - **ListWorkspaces**
    - changes of response param
      - `+ dc_vnc_ip`
  - **UpdateWorkspace**
    - changes of request param
      - `+ dc_vnc_ip`
    - changes of response param
      - `+ dc_vnc_ip`
  - **DeleteDesktop**
    - changes of request param
      - `+ is_force_delete`
  - **ShowDesktopDetail**
    - changes of response param
      - `+ desktop.user_list`
      - `+ desktop.user_group_list`
      - `+ desktop.attach_user_infos`
      - `+ desktop.attach_state`
      - `+ desktop.enterprise_project_id`
  - **ListDesktopsDetail**
    - changes of request param
      - `+ user_names`
      - `+ sort_field`
      - `+ sort_type`
      - `+ user_attached`
      - `+ enterprise_project_id`
      - `+ image_id`
      - `+ charge_mode`
      - `+ in_maintenance_mode`
      - `* desktop_id: string -> list<string>`
    - changes of response param
      - `+ desktops.user_list`
      - `+ desktops.user_group_list`
      - `+ desktops.attach_user_infos`
      - `+ desktops.attach_state`
      - `+ desktops.enterprise_project_id`

# 3.1.64 2023-11-02

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListApisV2**
    - changes of request param
      - `+ vpc_channel_name`

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ListPostalAddress`, `UpdatePostal`, `CreatePostal`, `DeletePostal`
  - **ListCustomerselfResourceRecordDetails**
    - changes of response param
      - `+ monthly_records.id`

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListCustomerselfResourceRecordDetails**
    - changes of response param
      - `+ monthly_records.id`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interfaces `StartChat`, `SyncChat`, `SyncGetChatResult`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CSMS

- _Features_
  - Support the interface `RotateSecret`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - Support the following interfaces：
    - `ShowConfigHistoryDetail`
    - `UpdateClientIpTransparentTransmission`
    - `UpdateInstanceConfig`
    - `ListInstanceOperations`
    - `ExportInstancesTask`
    - `ExportExcelJob`
    - `CreateResizeOrder`
    - `ShowExpireAutoScanConfig`
    - `UpdateExpireAutoScanConfig`
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ShowNodesInformation`, `ShowBackUpInfo`, `CreateOrUpdateBackUpInfo`, `CreateConnectivityTest`

### HuaweiCloud SDK DNS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowPrivateZone**
    - changes of response param
      - `+ enterprise_project_id`
      - `+ proxy_pattern`

### HuaweiCloud SDK DRS

- _Features_
  - Support the interfaces `CollectPositionAsync`, `ShowPositionResult`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **CreateDrugLigandSvg**
    - changes of request param
      - `+ scaffold`
  - **CreateNextflowJob**
    - changes of request param
      - `+ priority`
  - **CreateDrugLigandSimilarityGraphTask**
    - changes of request param
      - `+ mode: enum value [FREE]`
  - **ListDrugJob**
    - changes of response param
      - `+ jobs.priority`
  - **ShowSynthesisJob**
    - changes of response param
      - `+ basic_info.priority`
  - **ShowFepJob**
    - changes of response param
      - `+ part_failed_reason`
      - `+ basic_info.priority`
  - **ParseDrugReceptorInfo**
    - changes of response param
      - `* ligands.bounding_box: object<BoundingBoxDto> -> object<DrugBoundingBoxDto>`
  - **RecognizeDrugReceptorPocket**
    - changes of response param
      - `* pockets: list<BoundingBoxDto> -> list<DrugBoundingBoxDto>`
  - **CreateOptmJob**
    - changes of request param
      - `+ molecule_file`
      - `+ sampler_mixin_weight`
      - `+ model_ids`
      - `+ strong_constraints.id`
      - `+ binding_site.bounding_box.padding`
      - `* body: object<DrugFile> -> object<ReceptorDrugFile>`
      - `+ weak_constraints.id`
  - **ShowOptmJob**
    - changes of response param
      - `+ models`
      - `+ sampler_mixin_weight`
      - `+ molecule_file`
      - `+ basic_info.priority`
      - `+ strong_constraints.id`
      - `+ binding_site.bounding_box.padding`
      - `* body: object<DrugFile> -> object<ReceptorDrugFile>`
      - `+ weak_constraints.id`
  - **CreateDockingJob**
    - changes of request param
      - `+ receptors.bounding_box.padding`
      - `* body: object<DrugFile> -> object<ReceptorDrugFile>`
  - **ShowDockingJob**
    - changes of response param
      - `+ part_failed_reason`
      - `+ basic_info.priority`
      - `+ receptors.bounding_box.padding`
      - `* body: object<DrugFile> -> object<ReceptorDrugFile>`

### HuaweiCloud SDK ELB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListListeners**
    - changes of request param
      - `+ proxy_protocol_enable`
    - changes of response param
      - `+ listeners.proxy_protocol_enable`
      - `+ listeners.insert_headers.X-Forwarded-Proto`
      - `+ listeners.insert_headers.X-Real-IP`
      - `+ listeners.insert_headers.X-Forwarded-ELB-ID`
      - `+ listeners.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listeners.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listeners.insert_headers.X-Forwarded-TLS-Cipher`
  - **CreateListener**
    - changes of request param
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
    - changes of response param
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
  - **ShowListener**
    - changes of response param
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
  - **UpdateListener**
    - changes of request param
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
    - changes of response param
      - `+ listener.proxy_protocol_enable`
      - `+ listener.insert_headers.X-Forwarded-Proto`
      - `+ listener.insert_headers.X-Real-IP`
      - `+ listener.insert_headers.X-Forwarded-ELB-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Certificate-ID`
      - `+ listener.insert_headers.X-Forwarded-TLS-Protocol`
      - `+ listener.insert_headers.X-Forwarded-TLS-Cipher`
  - **CreatePool**
    - changes of request param
      - `+ pool.ip_version`
  - **UpdatePool**
    - changes of request param
      - `+ pool.any_port_enable`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the following interfaces：
    - `ShowIntelligentDiagnosisAbnormalCountOfInstances`
    - `ShowIntelligentDiagnosisInstanceInfosPerMetric`
    - `ShrinkGaussMySqlProxy`
    - `ShowInstanceDatabaseVersion`
    - `CopyInstanceConfigurations`
    - `ShowAutoScalingPolicy`
    - `UpdateAutoScalingPolicy`
    - `CheckResource`
    - `UpdateInstanceConfigurations`
- _Bug Fix_
  - None
- _Change_
  - **DeleteGaussMySqlBackup**
    - changes of response param
      - `+ backup_id`
      - `+ backup_name`
      - `- job_id`
  - **CreateGaussMySqlProxy**
    - changes of request param
      - `+ subnet_id`
  - **ShowGaussMySqlBackupList**
    - changes of request param
      - `+ name`
      - `+ instance_name`
    - changes of response param
      - `+ backups.instance_name`
      - `- backups.status: enum value [BUILDING,COMPLETED,FAILED,AVAILABLE]`
      - `- backups.type: enum value [auto,manual]`
  - **ShowGaussMySqlProxyList**
    - changes of response param
      - `+ proxy_list.proxy.subnet_id`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the interface `DeleteDatabase`
- _Bug Fix_
  - None
- _Change_
  - **ListInstances**
    - changes of request param
      - `+ charge_mode`
  - **ListInstancesDetails**
    - changes of request param
      - `+ charge_mode`

### HuaweiCloud SDK HSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSwrImageRepository**
    - changes of response param
      - `+ data_list.scannable`
      - `- data_list.scanable`

### HuaweiCloud SDK KPS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ImportPrivateKey**
    - changes of response param
      - `+ keypair.user_id`
      - `+ keypair.key_protection`
      - `* keypair: object<KeypairBean> -> object<ImportPrivateKeyAction>`

### HuaweiCloud SDK NAT

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListNatGatewayDnatRules**
    - changes of response param
      - `+ dnat_rules.global_eip_id`
      - `+ dnat_rules.global_eip_address`
  - **CreateNatGatewayDnatRule**
    - changes of request param
      - `+ dnat_rule.global_eip_id`
    - changes of response param
      - `+ dnat_rule.global_eip_id`
      - `+ dnat_rule.global_eip_address`
  - **ShowNatGatewayDnatRule**
    - changes of response param
      - `+ dnat_rule.global_eip_id`
      - `+ dnat_rule.global_eip_address`
  - **UpdateNatGatewayDnatRule**
    - changes of request param
      - `+ dnat_rule.global_eip_id`
    - changes of response param
      - `+ dnat_rule.global_eip_id`
      - `+ dnat_rule.global_eip_address`
  - **BatchCreateNatGatewayDnatRules**
    - changes of request param
      - `+ dnat_rules.global_eip_id`
    - changes of response param
      - `+ dnat_rules.global_eip_id`
      - `+ dnat_rules.global_eip_address`
  - **ListNatGatewaySnatRules**
    - changes of response param
      - `+ snat_rules.global_eip_id`
      - `+ snat_rules.global_eip_address`
  - **CreateNatGatewaySnatRule**
    - changes of request param
      - `+ snat_rule.global_eip_id`
    - changes of response param
      - `+ snat_rule.global_eip_id`
      - `+ snat_rule.global_eip_address`
  - **ShowNatGatewaySnatRule**
    - changes of response param
      - `+ snat_rule.global_eip_id`
      - `+ snat_rule.global_eip_address`
  - **UpdateNatGatewaySnatRule**
    - changes of request param
      - `+ snat_rule.global_eip_id`
    - changes of response param
      - `+ snat_rule.global_eip_address`
      - `+ snat_rule.global_eip_id`
  - **ListNatGateways**
    - changes of response param
      - `+ nat_gateways.ngport_ip_address`
      - `+ nat_gateways.billing_info`
      - `+ nat_gateways.dnat_rules_limit`
      - `+ nat_gateways.snat_rule_public_ip_limit`
  - **CreateNatGateway**
    - changes of request param
      - `+ nat_gateway.ngport_ip_address`
    - changes of response param
      - `+ nat_gateway.ngport_ip_address`
      - `+ nat_gateway.billing_info`
      - `+ nat_gateway.dnat_rules_limit`
      - `+ nat_gateway.snat_rule_public_ip_limit`
  - **ShowNatGateway**
    - changes of response param
      - `+ nat_gateway.ngport_ip_address`
      - `+ nat_gateway.billing_info`
      - `+ nat_gateway.dnat_rules_limit`
      - `+ nat_gateway.snat_rule_public_ip_limit`
  - **UpdateNatGateway**
    - changes of response param
      - `+ nat_gateway.ngport_ip_address`
      - `+ nat_gateway.billing_info`
      - `+ nat_gateway.dnat_rules_limit`
      - `+ nat_gateway.snat_rule_public_ip_limit`

### HuaweiCloud SDK RocketMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateRocketMqMigrationTask**
    - changes of request param
      - `* body: string -> map<string, object>`

### HuaweiCloud SDK SecMaster

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ListIncidentTypes`
  - **ListAlertRuleMetrics**
    - changes of response param
      - `+ metric`
      - `+ category`
      - `- body`
  - **CreateBatchOrderAlerts**
    - changes of request param
      - `- incident_id`
      - `- event_content`
      - `- marked_evidence`
      - `- incident_content.type_category`
      - `- incident_content.evidence_list`
      - `- incident_content.note_list`
      - `- incident_content.attachment_list`
      - `- incident_content.description`
      - `- incident_content.incident_type.layoutId`
    - changes of response param
      - `* data: object<BatchOrderAlertResult> -> object<BatchOperateAlertResult>`
  - **ShowAlertRule**
    - changes of response param
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
  - **UpdateAlertRule**
    - changes of request param
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
    - changes of response param
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
  - **CreateAlertRuleSimulation**
    - changes of request param
      - `- query_type: enum value [CBSL]`
  - **ShowAlertRuleTemplate**
    - changes of response param
      - `- query_type: enum value [CBSL]`
  - **ListPlaybooks**
    - changes of request param
      - `- component_id`
      - `* offset: optional -> required`
      - `* limit: optional -> required`
  - **CreatePlaybook**
    - changes of request param
      - `- approve_role`
      - `- user_role`
      - `- edit_role`
      - `- owner_id`
  - **ListPlaybookActions**
    - changes of request param
      - `* limit: optional -> required`
      - `* offset: optional -> required`
    - changes of response param
      - `- data.sort_order`
  - **CreatePlaybookAction**
    - changes of response param
      - `- data.sort_order`
  - **UpdatePlaybookAction**
    - changes of response param
      - `- data.sort_order`
  - **ListDataobjectRelations**
    - changes of request param
      - `+ order: enum value [DESC,ASC]`
      - `* condition.conditions.data: list<string> -> list<object>`
      - `* condition.conditions: list<ConditonInfo> -> list<object>`
      - `* condition.logics: list<string> -> list<object>`
    - changes of response param
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
    - changes of request param
      - `* body: object<CreateRelation> -> object<CreateDataobjectRelationsRequestBody>`
  - **DeleteDataobjectRelations**
    - changes of request param
      - `* body: object<CreateRelation> -> object<CreateDataobjectRelationsRequestBody>`
    - changes of response param
      - `- total`
      - `- offset`
      - `- success`
      - `- limit`
      - `- request_id`
      - `* data: object<DataResponse> -> object<BatchOperateDataobjectResult>`
  - **ListAlerts**
    - changes of request param
      - `+ order: enum value [DESC,ASC]`
      - `* condition.conditions.data: list<string> -> list<object>`
      - `* condition.conditions: list<ConditonInfo> -> list<object>`
      - `* condition.logics: list<string> -> list<object>`
    - changes of response param
      - `* data.data_object.network_list.src_port: string -> int32`
      - `* data.data_object.sla: int32 -> string`
      - `* data.data_object.simulation: boolean -> string`
      - `* data.data_object.process.process_pid: string -> int32`
      - `* data.data_object.process.process_uid: string -> int32`
  - **DeleteAlert**
    - changes of request param
      - `+ batch_ids`
      - `- ids`
      - `* body: object<DeleteAlert> -> object<DeleteAlertRequestBody>`
    - changes of response param
      - `* data: object<DataResponse> -> object<BatchOperateAlertResult>`
  - **CreateAlert**
    - changes of request param
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
    - changes of response param
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
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of request param
      - `+ order: enum value [DESC,ASC]`
      - `* condition.conditions.data: list<string> -> list<object>`
      - `* condition.conditions: list<ConditonInfo> -> list<object>`
      - `* condition.logics: list<string> -> list<object>`
    - changes of response param
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
    - changes of request param
      - `+ batch_ids`
      - `- ids`
      - `* body: object<DeleteIncident> -> object<DeleteIncidentRequestBody>`
    - changes of response param
      - `* data: object<BatchOrderAlertResult> -> object`
  - **CreateIncident**
    - changes of request param
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
    - changes of response param
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
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of request param
      - `- order`
      - `- from_date`
      - `- to_date`
      - `+ from_date`
      - `+ to_date`
      - `- type`
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of request param
      - `+ version_query_type: enum value [ALL:全部，VALID:有效的，DELETED:已删除]`
    - changes of response param
      - `* data.total_instance_run_num: int32 -> float`
  - **CreateAlertRule**
    - changes of request param
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
    - changes of response param
      - `- accumulated_times`
      - `- query_type: enum value [CBSL]`
  - **ListAlertRules**
    - changes of response param
      - `- accumulated_times`
      - `- records.accumulated_times`
      - `- records.query_type: enum value [CBSL]`
  - **ListAlertRuleTemplates**
    - changes of response param
      - `- records.query_type: enum value [CBSL]`
  - **CopyPlaybookVersion**
    - changes of response param
      - `- data.run_mode`
      - `- data.dataobject_id`
      - `- data.actions.sort_order`
  - **CreatePlaybookRule**
    - changes of request param
      - `+ rule.start_type`
      - `+ rule.end_type`
      - `+ rule.end_time`
      - `+ rule.only_once`
      - `+ rule.execution_type`
      - `- rule.repeat_count`
      - `* rule.logics: object -> list<string>`
  - **ListPlaybookInstances**
    - changes of request param
      - `- date_type`
      - `* limit: optional -> required`
      - `* offset: optional -> required`
  - **ShowPlaybookTopology**
    - changes of response param
      - `- action_instances.action.sort_order`
  - **ListPlaybookVersions**
    - changes of request param
      - `- approve_role`
    - changes of response param
      - `- data.run_mode`
      - `- data.dataobject_id`
  - **CreatePlaybookVersion**
    - changes of request param
      - `- actions.sort_order`
    - changes of response param
      - `- data.run_mode`
      - `- data.dataobject_id`
      - `- data.actions.sort_order`
  - **ShowPlaybookVersion**
    - changes of response param
      - `- data.run_mode`
      - `- data.dataobject_id`
      - `- data.actions.sort_order`
  - **UpdatePlaybookVersion**
    - changes of response param
      - `- data.run_mode`
      - `- data.dataobject_id`
      - `- data.actions.sort_order`
  - **UpdatePlaybookRule**
    - changes of request param
      - `+ rule.start_type`
      - `+ rule.end_type`
      - `+ rule.end_time`
      - `+ rule.only_once`
      - `+ rule.execution_type`
      - `- rule.repeat_count`
      - `* rule.logics: object -> list<string>`

# 3.1.63 2023-10-26

### HuaweiCloud SDK AOS

- _Features_
  - Support the interfaces `ShowStackInstance`, `UpdateStackInstances`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDetailsOfApiV2**
    - changes of response param
      - `+ policy_functions.conditions.sys_param_name`
      - `+ policy_functions.conditions.cookie_param_name`
      - `+ policy_functions.conditions.frontend_authorizer_param_name`
      - `+ policy_functions.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
  - **UpdateApiV2**
    - changes of request param
      - `+ policy_mocks.conditions.sys_param_name`
      - `+ policy_mocks.conditions.cookie_param_name`
      - `+ policy_mocks.conditions.frontend_authorizer_param_name`
      - `+ policy_mocks.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
    - changes of response param
      - `+ policy_functions.conditions.sys_param_name`
      - `+ policy_functions.conditions.cookie_param_name`
      - `+ policy_functions.conditions.frontend_authorizer_param_name`
      - `+ policy_functions.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
  - **ListApiVersionDetailV2**
    - changes of response param
      - `+ policy_functions.conditions.sys_param_name`
      - `+ policy_functions.conditions.cookie_param_name`
      - `+ policy_functions.conditions.frontend_authorizer_param_name`
      - `+ policy_functions.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
  - **CreateApiV2**
    - changes of request param
      - `+ policy_mocks.conditions.sys_param_name`
      - `+ policy_mocks.conditions.cookie_param_name`
      - `+ policy_mocks.conditions.frontend_authorizer_param_name`
      - `+ policy_mocks.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`
    - changes of response param
      - `+ policy_functions.conditions.sys_param_name`
      - `+ policy_functions.conditions.cookie_param_name`
      - `+ policy_functions.conditions.frontend_authorizer_param_name`
      - `+ policy_functions.conditions.condition_origin: enum value [system,cookie,frontend_authorizer]`

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateBareMetalServers**
    - changes of request param
      - `+ server.extendparam.chargingMode: enum value [postPaid]`

### HuaweiCloud SDK CC

- _Features_
  - Support the interface `ListCentralNetworkCapabilities`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CDN

- _Features_
  - Support the following interfaces：
    - `CreateRefreshTasks`
    - `CreatePreheatingTasks`
    - `ShowHistoryTasks`
    - `ShowHistoryTaskDetails`
    - `ShowUrlTaskInfo`
- _Bug Fix_
  - None
- _Change_
  - **CreateRefreshTasks**
    - changes of request param
      - `+ refresh_task.zh_url_encode`
  - **CreatePreheatingTasks**
    - changes of request param
      - `+ preheating_task.zh_url_encode`

### HuaweiCloud SDK CodeArtsPipeline

- _Features_
  - Support the interfaces `CreatePipelineNew`, `RetryPipelineRun`, `AcceptManualReview`, `RejectManualReview`
- _Bug Fix_
  - None
- _Change_
  - **ListPipelines**
    - changes of response param
      - `+ pipelines.latest_run.stage_status_list.id`
  - **CreatePipelineByTemplateId**
    - changes of request param
      - `+ variables`

### HuaweiCloud SDK DCS

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DLI

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListBatches**
    - changes of request param
      - `+ job-name`
  - **CreateBatchJob**
    - changes of response param
      - `- req_body`

### HuaweiCloud SDK HSS

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListPortStatistics**
    - changes of request param
      - `+ port_string`
      - `+ sort_key`
      - `+ sort_dir`
    - changes of response param
      - `+ data_list.status`
  - **ListProtectionServer**
    - changes of response param
      - `+ data_list.host_source`
  - **ListHostStatus**
    - changes of request param
      - `+ has_intrusion`
      - `+ agent_upgradable`
  - **ListVulHosts**
    - changes of response param
      - `+ data_list.support_restore`
  - **ChangeVulStatus**
    - changes of request param
      - `+ backup_info_id`
      - `+ custom_backup_hosts`
  - **ListHostVuls**
    - changes of response param
      - `+ data_list.app_name`
      - `+ data_list.app_version`
      - `+ data_list.app_path`
      - `+ data_list.version`
      - `+ data_list.support_restore`
  - **ListHostProtectHistoryInfo**
    - changes of request param
      - `+ host_name`
      - `+ host_ip`
      - `+ file_path`
      - `+ file_operation`
  - **ListProtectionPolicy**
    - changes of response param
      - `+ data_list.deploy_mode`
      - `+ data_list.default_policy`
  - **ListSecurityEvents**
    - changes of request param
      - `+ severity_list`
      - `+ attack_tag`
      - `+ asset_value`
      - `+ tag_list`
      - `+ att_ck`
    - changes of response param
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
    - changes of request param
      - `+ operate_event_list.operate_detail_list.container_id`
      - `+ operate_event_list.operate_detail_list.container_name`

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListProducts**
    - changes of request param
      - `+ product_name`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ResizeInstance**
    - changes of request param
      - `+ tenant_ips`
      - `+ second_tenant_subnet_id`
  - **ResizeEngineInstance**
    - changes of request param
      - `+ tenant_ips`
      - `+ second_tenant_subnet_id`

### HuaweiCloud SDK LakeFormation

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateLakeFormationInstance**
    - changes of request param
      - `- order_id`

### HuaweiCloud SDK Moderation

- _Features_
  - Support the interfaces `RunCreateAudioStreamModerationJob`, `RunCloseAudioStreamModerationJob`, `RunCreateVideoStreamModerationJob`, `RunCloseVideoStreamModerationJob`
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
  - **RecognizeGeneralTable**
    - changes of request param
      - `+ with_borders`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListInstanceDiagnosis`, `ListInstancesInfoDiagnosis`
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
  - **ShowGroup**
    - changes of response param
      - `+ group_desc`
  - **CreateConsumerGroupOrBatchDeleteConsumerGroup**
    - changes of request param
      - `+ group_desc`
  - **ListInstanceConsumerGroups**
    - changes of response param
      - `+ groups.group_desc`
  - **BatchUpdateConsumerGroup**
    - changes of request param
      - `+ groups.group_desc`

### HuaweiCloud SDK SFSTurbo

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListShares**
    - changes of response param
      - `* shares: list<Shares> -> list<ShareInfo>`

# 3.1.62 2023-10-19

### HuaweiCloud SDK APIG

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK AOM

- _Features_
  - Support the interfaces `CreateSubApp`, `UpdateSubApp`, `DeleteSubApp`
- _Bug Fix_
  - None
- _Change_
  - **CreateApp**
    - changes of request param
      - `+ register_type: enum value [CONSOLE,SERVICE_DISCOVERY]`
      - `- register_type: enum value [CONSOLESERVICE_DISCOVERY]`
  - **UpdateApp**
    - changes of request param
      - `+ register_type: enum value [CONSOLE,SERVICE_DISCOVERY]`
      - `- register_type: enum value [CONSOLESERVICE_DISCOVERY]`
  - **CreateComponent**
    - changes of request param
      - `+ model_type: enum value [APPLICATION,SUB_APPLICATION]`
  - **CreateEnv**
    - changes of request param
      - `+ env_type: enum value [DEV,TEST,PRE,ONLINE]`
      - `+ os_type: enum value [LINUX,WINDOWS]`
      - `+ register_type: enum value [API,CONSOLE,SERVICE_DISCOVERY]`
  - **ListResourceUnderNode**
    - changes of request param
      - `+ ci_type: enum value [APPLICATION,SUB_APPLICATION,COMPONENT,ENVIRONMENT]`
  - **UpdateEnv**
    - changes of request param
      - `+ env_type: enum value [DEV,TEST,PRE,ONLINE]`
      - `+ os_type: enum value [LINUX,WINDOWS]`
      - `+ register_type: enum value [API,CONSOLE,SERVICE_DISCOVERY]`

### HuaweiCloud SDK CAE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListComponentConfigurations**
    - changes of response param
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
    - changes of request param
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

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListAgent**
    - changes of request param
      - `* agent_id: string -> list<string>`
  - **ListVault**
    - changes of request param
      - `* id: string -> list<string>`

### HuaweiCloud SDK CC

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
    - `ListDomainTags`
    - `DeleteTag`
    - `BatchCreateDeleteTags`
    - `ListResourceByFilterTag`
    - `ListTags`
    - `CreateTag`
  - **ListCloudConnections**
    - changes of request param
      - `* id: list<string> -> list<UUIDDef>`
  - **ListCloudConnectionRoutes**
    - changes of request param
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`
  - **ListAuthorisations**
    - changes of request param
      - `* id: list<string> -> list<UUIDDef>`
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`
  - **ListPermissions**
    - changes of request param
      - `* id: list<string> -> list<UUIDDef>`
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`
  - **ListCloudConnectionQuotas**
    - changes of request param
      - `+ cloud_connection_id`
      - `+ region_id`
  - **ListNetworkInstances**
    - changes of request param
      - `* id: list<string> -> list<UUIDDef>`
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`
  - **ListBandwidthPackages**
    - changes of request param
      - `+ cloud_connection_id`
      - `* id: list<string> -> list<UUIDDef>`
  - **ListInterRegionBandwidths**
    - changes of request param
      - `* id: list<string> -> list<UUIDDef>`
      - `* cloud_connection_id: list<string> -> list<UUIDDef>`

### HuaweiCloud SDK CCM

- _Features_
  - Support the interface `CreateCertificateAuthorityOrder`
- _Bug Fix_
  - None
- _Change_
  - **ExportCertificate**
    - changes of response param
      - `+ signed_and_enveloped_data`
  - **ShowCertificateAuthority**
    - changes of response param
      - `+ charging_mode`
      - `+ free_quota`
  - **IssueCertificateAuthorityCertificate**
    - changes of request param
      - `+ type`
      - `+ distinguished_name`
      - `+ key_algorithm`
      - `+ key_usages`
      - `+ crl_configuration`
  - **CreateCertificateAuthority**
    - changes of request param
      - `+ ca_id`
  - **ListCertificateAuthority**
    - changes of response param
      - `+ charging_mode`
      - `+ free_quota`
      - `+ certificate_authorities.free_quota`
      - `+ certificate_authorities.charging_mode`

### HuaweiCloud SDK CFW

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListFlowLogs**
    - changes of request param
      - `+ dst_host`
    - changes of response param
      - `+ data.records.dst_host`
  - **ListAccessControlLogs**
    - changes of request param
      - `+ dst_host`
      - `+ rule_name`
      - `+ action`
    - changes of response param
      - `+ data.records.src_region_id`
      - `+ data.records.src_region_name`
      - `+ data.records.dst_region_id`
      - `+ data.records.dst_region_name`
      - `+ data.records.dst_host`
  - **ListBlackWhiteLists**
    - changes of response param
      - `+ data.records.description`
  - **ListDomainParseDetail**
    - changes of request param
      - `+ address_type`
  - **UpdateDnsServers**
    - changes of request param
      - `+ health_check_domain_name`
  - **ListDnsServers**
    - changes of response param
      - `+ data.health_check_domain_name`
  - **ListAttackLogs**
    - changes of request param
      - `+ dst_host`
      - `+ log_type`
    - changes of response param
      - `+ data.records.dst_host`
      - `+ data.records.src_region_id`
      - `+ data.records.src_region_name`
      - `+ data.records.dst_region_id`
      - `+ data.records.dst_region_name`
  - **UpdateAclRule**
    - changes of request param
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
    - changes of request param
      - `+ tags_id`
      - `+ source`
      - `+ destination`
      - `+ service`
    - changes of response param
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
    - changes of request param
      - `+ description`
  - **UpdateBlackWhiteList**
    - changes of request param
      - `+ description`
  - **ListEipCount**
    - changes of response param
      - `+ data.eip_protected_self`
  - **ChangeEipStatus**
    - changes of response param
      - `+ data.object_id`
      - `+ data.fail_eip_id_list`
      - `- data.id`
      - `* data: object<IdObject> -> object<EIPSwitchStatusVO>`
  - **ListEastWestFirewall**
    - changes of response param
      - `+ data.mode`
      - `+ data.ew_vpc_route_limit`
      - `+ data.er_associated_subnet.ipv6_enable`
      - `+ data.protect_infos.protected_resource_mode`
  - **AddAclRule**
    - changes of request param
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
    - changes of request param
      - `+ tags`
    - changes of response param
      - `+ data.records.object_id`
      - `+ data.records.tags`
      - `+ data.records.domain_id`
      - `+ data.records.owner`
      - `+ data.records.fw_domain_id`
  - **AddAddressItem**
    - changes of response param
      - `+ data.covered_ip`
  - **ListFirewallDetail**
    - changes of response param
      - `+ data.records.resource_id`
      - `+ data.records.support_url_filtering`
      - `+ data.records.flavor.session_concurrent`
      - `+ data.records.flavor.session_create`
      - `+ data.records.flavor.total_rule_count`
      - `+ data.records.flavor.used_rule_count`
      - `+ data.records.flavor.vpc_bandwith`

### HuaweiCloud SDK CodeArtsBuild

- _Features_
  - Support the following interfaces：
    - `DownloadLogByRecordId`
    - `ShowRecordInfo`
    - `StopBuildJob`
    - `DeleteBuildJob`
    - `DisableBuildJob`
    - `ResumeBuildJob`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DataArtsStudio

- _Features_
  - Support the interfaces `ShowTags`, `ParseUserBehavior`, `ShowDataSets`, `BatchSyncMetadata`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListConfigTemplates**
    - changes of response param
      - `+ templates`
      - `- config_templates`
  - **CreateRedislog**
    - changes of request param
      - `+ query_time: enum value [0,1,3,7]`
  - **ListInstances**
    - changes of response param
      - `+ instances.features.support_audit_log`
  - **ShowInstance**
    - changes of response param
      - `+ features.support_audit_log`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ReinstallServerWithCloudInit**
    - changes of request param
      - `+ os-reinstall.metadata.BYOL`
  - **ChangeServerOsWithCloudInit**
    - changes of request param
      - `+ os-change.metadata.BYOL`
  - **ChangeServerOsWithoutCloudInit**
    - changes of request param
      - `+ os-change.metadata.BYOL`

### HuaweiCloud SDK EG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **PutOfficialEvents**
    - changes of response param
      - `- failed_count`
      - `- events`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListGaussMySqlDatabase**
    - changes of request param
      - `+ name`
      - `+ charset`

### HuaweiCloud SDK LakeFormation

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ShowDatabase**
    - changes of response param
      - `+ owner_auth_source_type`
  - **UpdateDatabase**
    - changes of request param
      - `+ owner_auth_source_type`
    - changes of response param
      - `+ owner_auth_source_type`
  - **ListCatalogs**
    - changes of response param
      - `+ owner`
      - `+ owner_source`
      - `+ owner_type`
  - **CreateCatalog**
    - changes of request param
      - `+ branch_name`
      - `+ owner`
      - `+ owner_type`
      - `+ owner_source`
    - changes of response param
      - `+ owner`
      - `+ owner_source`
      - `+ owner_type`
  - **ShowCatalog**
    - changes of response param
      - `+ owner`
      - `+ owner_source`
      - `+ owner_type`
  - **UpdateCatalog**
    - changes of request param
      - `+ branch_name`
      - `+ owner`
      - `+ owner_type`
      - `+ owner_source`
    - changes of response param
      - `+ owner`
      - `+ owner_source`
      - `+ owner_type`
  - **ShowRole**
    - changes of response param
      - `+ role_name`
      - `+ principal_source`
      - `+ description`
      - `- role`
      - `- user_roles`
  - **UpdateRole**
    - changes of response param
      - `+ principal_source: enum value [AGENTTENANT]`
  - **ListLakeFormationInstances**
    - changes of response param
      - `+ default_instance`
      - `+ instances.default_instance`
      - `+ instances.status: enum value [RESOURCE_PREPARATION,RUNNING,RESOURCE_RELEASE,DELETED,RESOURCE_PREPARATION_FAIL,FROZEN_RELEASABLE,FROZEN_UNRELEASABLE,RECOVERING,DELETING,SCALING,SCALE_FAIL]`
  - **CreateLakeFormationInstance**
    - changes of request param
      - `+ order_id`
      - `+ charge_mode: enum value [prePaid]`
      - `+ specs.product_id`
    - changes of response param
      - `+ scale_progress`
      - `+ charge_mode`
      - `+ default_instance`
      - `+ resource_progress`
      - `+ resource_expected_duration`
      - `+ scale_expected_duration`
      - `+ status: enum value [RESOURCE_PREPARATION,RUNNING,RESOURCE_RELEASE,DELETED,RESOURCE_PREPARATION_FAIL,FROZEN_RELEASABLE,FROZEN_UNRELEASABLE,RECOVERING,DELETING,SCALING,SCALE_FAIL]`
      - `+ specs.product_id`
  - **UpdateLakeFormationInstance**
    - changes of response param
      - `+ default_instance`
      - `+ status: enum value [RESOURCE_PREPARATION,RUNNING,RESOURCE_RELEASE,DELETED,RESOURCE_PREPARATION_FAIL,FROZEN_RELEASABLE,FROZEN_UNRELEASABLE,RECOVERING,DELETING,SCALING,SCALE_FAIL]`
  - **ShowLakeFormationInstance**
    - changes of response param
      - `+ scale_progress`
      - `+ charge_mode`
      - `+ default_instance`
      - `+ resource_progress`
      - `+ resource_expected_duration`
      - `+ scale_expected_duration`
      - `+ status: enum value [RESOURCE_PREPARATION,RUNNING,RESOURCE_RELEASE,DELETED,RESOURCE_PREPARATION_FAIL,FROZEN_RELEASABLE,FROZEN_UNRELEASABLE,RECOVERING,DELETING,SCALING,SCALE_FAIL]`
      - `+ specs.product_id`
  - **ListSpecs**
    - changes of response param
      - `+ spec_codes.usage_value`
      - `+ spec_codes.free_usage_value`
  - **CreateDatabase**
    - changes of request param
      - `+ owner_auth_source_type`
    - changes of response param
      - `+ owner_auth_source_type`
  - **ListDatabases**
    - changes of response param
      - `+ owner_auth_source_type`
      - `+ databases.owner_auth_source_type`
  - **ShowFunction**
    - changes of response param
      - `+ owner_auth_source_type`
  - **UpdateFunction**
    - changes of request param
      - `+ owner_auth_source_type`
    - changes of response param
      - `+ owner_auth_source_type`
  - **CreateRole**
    - changes of response param
      - `+ principal_source: enum value [AGENTTENANT]`
  - **ListRoles**
    - changes of response param
      - `+ roles.principal_source: enum value [AGENTTENANT]`
  - **ListAllFunctions**
    - changes of response param
      - `+ owner_auth_source_type`
      - `+ functions.owner_auth_source_type`
  - **CreateFunction**
    - changes of request param
      - `+ owner_auth_source_type`
    - changes of response param
      - `+ owner_auth_source_type`
  - **ListFunctions**
    - changes of response param
      - `+ owner_auth_source_type`
      - `+ functions.owner_auth_source_type`
  - **CreateTable**
    - changes of request param
      - `+ ignore_obs_checked`
  - **UpdateTable**
    - changes of request param
      - `+ table.ignore_obs_checked`
  - **ShowSyncPolicy**
    - changes of response param
      - `+ policy_deltas.change_type`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListStructuredLogsWithTimeRange**
    - changes of response param
      - `+ result`
      - `- context`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListEngineProducts**
    - changes of response param
      - `+ products.properties.product_alias`

### HuaweiCloud SDK SIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `RunAudioAssessment`, `RunMultiModalAssessment`

### HuaweiCloud SDK VPC

- _Features_
  - Support the interface `BatchCreateSecurityGroupRules`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.61 2023-10-12

### HuaweiCloud SDK AOS

- _Features_
  - Support the following interfaces：
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
  - **CreateScalingConfig**
    - changes of request param
      - `+ source_scaling_configuration_id`

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateBareMetalServers**
    - changes of request param
      - `* server.server_tags: map<string, list<SystemTags>> -> list<SystemTags>`

### HuaweiCloud SDK BSS

- _Features_
  - Support the interface `ListSubCustomerNewTag`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CAE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListApplications**
    - changes of response param
      - `- items.annotations`
  - **CreateApplication**
    - changes of request param
      - `- metadata.annotations`
    - changes of response param
      - `- metadata.annotations`
  - **ShowApplication**
    - changes of response param
      - `- metadata.annotations`
  - **ListComponentConfigurations**
    - changes of response param
      - `+ items.data.spec`
      - `+ items.data.metadata`
      - `* items.data: object -> object<ListComponentConfigurationsResponseData>`
  - **CreateComponentConfiguration**
    - changes of request param
      - `+ items.data.spec`
      - `+ items.data.metadata`
      - `* items.data: object -> object<ConfigurationData>`
  - **ListComponentSnapshots**
    - changes of response param
      - `- items.description`
      - `+ items.context.runtime: enum value [Java17,Nodejs14,Nodejs16]`
  - **ShowComponent**
    - changes of response param
      - `+ spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`
  - **UpdateComponent**
    - changes of request param
      - `+ spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`
  - **CreateComponent**
    - changes of response param
      - `+ spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`
  - **ListComponents**
    - changes of response param
      - `+ items.spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowHistoryTasks**
    - changes of request param
      - `+ task_type`
  - **ShowUrlTaskInfo**
    - changes of response param
      - `+ result.mode`

### HuaweiCloud SDK CES

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListAlarmHistories**
    - changes of response param
      - `+ alarm_histories.condition.suppress_duration: enum value [86400]`
  - **ListAgentInvocations**
    - changes of request param
      - `- instance_name`
      - `+ invocation_type: enum value [RETRY]`
    - changes of response param
      - `+ invocations.invocation_type: enum value [RETRY]`
  - **ListAgentStatus**
    - changes of response param
      - `+ agent_status.extensions.version`

### HuaweiCloud SDK CodeArtsDeploy

- _Features_
  - Support the interface `ShowExecutionParams`
- _Bug Fix_
  - None
- _Change_
  - **ListAllApp**
    - changes of request param
      - `+ states`
      - `+ group_id`

### HuaweiCloud SDK Config

- _Features_
  - Support the following interfaces：
    - `ListOrganizationConformancePacks`
    - `CreateOrganizationConformancePack`
    - `ShowOrganizationConformancePack`
    - `DeleteOrganizationConformancePack`
    - `ListOrganizationConformancePackStatuses`
    - `ShowOrganizationConformancePackDetailedStatuses`
- _Bug Fix_
  - None
- _Change_
  - **ShowConfigurationAggregatorSourcesStatus**
    - changes of response param
      - `+ aggregated_source_statuses.source_name`
  - **ShowConformancePack**
    - changes of response param
      - `+ created_by`
  - **CreateConformancePack**
    - changes of response param
      - `+ created_by`
  - **ListConformancePacks**
    - changes of response param
      - `+ created_by`
      - `+ value.created_by`
  - **ShowAggregatePolicyStateComplianceSummary**
    - changes of response param
      - `+ results.group_account_name`
  - **ListAggregateComplianceByPolicyAssignment**
    - changes of response param
      - `+ aggregate_policy_assignments.account_name`

### HuaweiCloud SDK CSS

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **UpdateShrinkNodes**
    - changes of request param
      - `+ migrate_data`
  - **CreateCnf**
    - changes of request param
      - `+ sensitive_words`
  - **UpdateCnf**
    - changes of request param
      - `+ sensitive_words`
  - **ShowClusterDetail**
    - changes of response param
      - `+ bandwidthResourceId`
      - `+ instances.resourceId`
      - `+ instances.volume.resourceIds`
      - `+ publicKibanaResp.bandwidthResourceId`
  - **ListClustersDetails**
    - changes of response param
      - `+ clusters.bandwidthResourceId`
      - `+ clusters.instances.resourceId`
      - `+ clusters.instances.volume.resourceIds`
      - `+ clusters.publicKibanaResp.bandwidthResourceId`

### HuaweiCloud SDK CTS

- _Features_
  - Support the following interfaces：
    - `ListOperations`
    - `BatchCreateResourceTags`
    - `BatchDeleteResourceTags`
    - `ListUserResources`
    - `CheckObsBuckets`
    - `ListTraceResources`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DataArtsStudio

- _Features_
  - Support the following interfaces：
    - `StopFactorySupplementDataInstance`
    - `ShowFactorySupplementData`
    - `CreateFactorySupplementDataInstance`
    - `ShowFactoryEnv`
    - `CreateFactoryEnv`
- _Bug Fix_
  - None
- _Change_
  - **PublishApi**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowApplyDetail**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowMessageDetail**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowCatalogDetail**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **UpdateCatalog**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **CreateServiceCatalog**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **DeleteServiceCatalog**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **MigrateCatalog**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **MigrateApi**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **SearchIdByPath**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowPathById**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **PublishApiToInstance**
    - changes of request param
      - `* workspace: optional -> required`
  - **ExecuteApiToInstance**
    - changes of request param
      - `* workspace: optional -> required`
  - **AuthorizeApiToInstance**
    - changes of request param
      - `* workspace: optional -> required`
  - **AuthorizeActionApiToInstance**
    - changes of request param
      - `* workspace: optional -> required`
  - **DeleteApp**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowAppInfo**
    - changes of request param
      - `* workspace: optional -> required`
  - **UpdateApp**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowApisOverview**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowAppsOverview**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowApisDetail**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowAppsDetail**
    - changes of request param
      - `* workspace: optional -> required`
  - **BatchApproveApply**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListApply**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ConfirmMessage**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListMessage**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListAllCatalogList**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListApiCatalogList**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ListCatalogList**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **ShowPathObjectById**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
    - changes of response param
      - `+ paths.name`
  - **DebugApi**
    - changes of request param
      - `* workspace: optional -> required`
  - **SearchPublishInfo**
    - changes of request param
      - `* workspace: optional -> required`
  - **ListInstanceList**
    - changes of request param
      - `* workspace: optional -> required`
  - **SearchDebugInfo**
    - changes of request param
      - `* workspace: optional -> required`
  - **ListApicInstances**
    - changes of request param
      - `* workspace: optional -> required`
  - **ListApicGroups**
    - changes of request param
      - `* workspace: optional -> required`
  - **CreateApp**
    - changes of request param
      - `* workspace: optional -> required`
  - **ListApps**
    - changes of request param
      - `* workspace: optional -> required`
  - **ListApisTop**
    - changes of request param
      - `* workspace: optional -> required`
  - **ListAppsTop**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowApisDashboard**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowApiDashboard**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowAppsDashboard**
    - changes of request param
      - `* workspace: optional -> required`
  - **ListApiTopN**
    - changes of request param
      - `* workspace: optional -> required`
  - **ListApis**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **CreateApi**
    - changes of request param
      - `* workspace: optional -> required`
  - **ShowApi**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **UpdateApi**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **SearchAuthorizeApp**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`
  - **SearchBindApi**
    - changes of request param
      - `+ Dlm-Type`
      - `* workspace: optional -> required`

### HuaweiCloud SDK DC

- _Features_
  - Support the following interfaces：
    - `UpdateVifPeer`
    - `DeleteVifPeer`
    - `CreateVifPeer`
    - `ShowQuotas`
    - `ListSwitchoverTestRecords`
    - `SwitchoverTest`
- _Bug Fix_
  - None
- _Change_
  - **DeleteResourceTag**
    - changes of request param
      - `+ resource_type: enum value [dc-lag]`
  - **ListProjectTags**
    - changes of request param
      - `+ resource_type: enum value [dc-lag]`
  - **ShowResourceTag**
    - changes of request param
      - `+ resource_type: enum value [dc-lag]`
  - **CreateResourceTag**
    - changes of request param
      - `+ resource_type: enum value [dc-lag]`
  - **BatchCreateResourceTags**
    - changes of request param
      - `+ resource_type: enum value [dc-lag]`
  - **ShowDirectConnect**
    - changes of request param
      - `- limit`
      - `- marker`
    - changes of response param
      - `- direct_connect.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connect.charge_mode: enum value [port]`
  - **UpdateDirectConnect**
    - changes of response param
      - `- direct_connect.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connect.charge_mode: enum value [port]`
  - **ListDirectConnects**
    - changes of response param
      - `- direct_connects.type: enum value [onestop_standard,onestop_hosted]`
      - `- direct_connects.charge_mode: enum value [port]`
  - **ShowVirtualGateway**
    - changes of response param
      - `- virtual_gateway.type: enum value [default]`
  - **UpdateVirtualGateway**
    - changes of response param
      - `- virtual_gateway.type: enum value [default]`
  - **ListVirtualGateways**
    - changes of request param
      - `+ enterprise_project_id`
    - changes of response param
      - `- virtual_gateways.type: enum value [default]`
  - **CreateVirtualGateway**
    - changes of response param
      - `- virtual_gateway.type: enum value [default]`
  - **ShowVirtualInterface**
    - changes of response param
      - `+ virtual_interface.service_type: enum value [GDGW]`
      - `- virtual_interface.service_type: enum value [vpc,GDWW]`
  - **UpdateVirtualInterface**
    - changes of response param
      - `+ virtual_interface.service_type: enum value [GDGW]`
      - `- virtual_interface.service_type: enum value [vpc,GDWW]`
  - **ListVirtualInterfaces**
    - changes of response param
      - `+ virtual_interfaces.service_type: enum value [GDGW]`
      - `- virtual_interfaces.service_type: enum value [vpc,GDWW]`
  - **CreateVirtualInterface**
    - changes of request param
      - `+ virtual_interface.service_type: enum value [GDGW]`
      - `- virtual_interface.service_type: enum value [GDWW]`
    - changes of response param
      - `+ virtual_interface.service_type: enum value [GDGW]`
      - `- virtual_interface.service_type: enum value [vpc,GDWW]`
  - **ListTagResourceInstances**
    - changes of request param
      - `+ resource_type: enum value [dc-lag]`

### HuaweiCloud SDK DGC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RunOnce**
    - changes of response param
      - `* instanceId: string -> int64`

### HuaweiCloud SDK DWS

- _Features_
  - Support the following interfaces：
    - `SaveClusterDescriptionInfo`
    - `ExecuteDatabaseOmUserAction`
    - `ShowInstance`
    - `ShowDatabaseOmUserStatus`
    - `ListConfigurationsAuditRecords`
    - `ShowClusterRedistribution`
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
  - **ReinstallServerWithoutCloudInit**
    - changes of request param
      - `+ os-reinstall.metadata.BYOL`
  - **ListFlavors**
    - changes of response param
      - `+ flavors.os_extra_specs.quota:vif_max_num`
      - `+ flavors.os_extra_specs.quota:sub_network_interface_max_num`
  - **ListResizeFlavors**
    - changes of response param
      - `+ flavors.extra_specs.quota:vif_max_num`
      - `+ flavors.extra_specs.quota:sub_network_interface_max_num`

### HuaweiCloud SDK EG

- _Features_
  - Support the interface `PutOfficialEvents`
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
  - Remove the interfaces `ShowFunctionUrl`, `UpdateFunctionUrl`, `CreateFunctionUrl`, `DeleteFunctionUrl`
  - **ListAsyncInvocations**
    - changes of response param
      - `+ next_marker`
      - `+ count`
  - **ListActiveAsyncInvocations**
    - changes of response param
      - `+ next_marker`
      - `+ count`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListInstances**
    - changes of response param
      - `+ instances.datastore.complete_version`
      - `+ instances.datastore.hotfix_versions`
  - **ListInstancesDetails**
    - changes of response param
      - `+ instances.datastore.complete_version`
      - `+ instances.datastore.hotfix_versions`

### HuaweiCloud SDK ImageSearch

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RunAddData**
    - changes of request param
      - `* optional_params.category: int -> int32`
    - changes of response param
      - `* data.image_info.objects.category: number -> integer`
  - **RunDeleteData**
    - changes of response param
      - `* data.delete_info.total_num: int -> int32`
      - `* data.delete_info.delete_num: int -> int32`
  - **RunSearch**
    - changes of request param
      - `* optional_params.category: int -> int32`
    - changes of response param
      - `* data.image_info.category: number -> integer`
      - `* data.image_info.objects.category: number -> integer`
      - `* data.search_info.total_num: int -> int32`
      - `* data.search_info.return_num: int -> int32`
      - `* data.search_info.search_time: long -> int32`
  - **RunCheckData**
    - changes of response param
      - `* data.check_info.total_num: int -> int32`
      - `* data.check_info.return_num: int -> int32`

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowJob**
    - changes of response param
      - `+ entities.addition_error_code`
      - `+ entities.addition_error_msg`
      - `+ entities.error_code`
      - `+ entities.error`
      - `+ entities.alarm_code`

### HuaweiCloud SDK LakeFormation

- _Features_
  - Support the interfaces `ListLakeFormationInstanceTags`, `ListQuotas`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK MetaStudio

- _Features_
  - Support the interfaces `CreatePhotoDetection`, `ShowPhotoDetection`
- _Bug Fix_
  - None
- _Change_
  - **CreateSmartLiveRoom**
    - changes of request param
      - `- video_config.codec: enum value [VP9]`
  - **ShowSmartLiveRoom**
    - changes of response param
      - `- video_config.codec: enum value [VP9]`
  - **UpdateSmartLiveRoom**
    - changes of request param
      - `- video_config.codec: enum value [VP9]`
    - changes of response param
      - `- video_config.codec: enum value [VP9]`
  - **StartSmartLive**
    - changes of request param
      - `- video_config.codec: enum value [VP9]`
  - **Create2DDigitalHumanVideo**
    - changes of request param
      - `- video_config.codec: enum value [VP9]`
  - **Show2DDigitalHumanVideo**
    - changes of response param
      - `- video_config.codec: enum value [VP9]`
  - **CreateVideoScripts**
    - changes of request param
      - `- video_config.codec: enum value [VP9]`
  - **ShowVideoScript**
    - changes of response param
      - `- video_config.codec: enum value [VP9]`
  - **UpdateVideoScript**
    - changes of request param
      - `- video_config.codec: enum value [VP9]`

### HuaweiCloud SDK OCR

- _Features_
  - Support the interface `RecognizeColombiaIdCard`
- _Bug Fix_
  - None
- _Change_
  - **RecognizeVehicleLicense**
    - changes of response param
      - `+ result.energy_type`
      - `+ result.front`
      - `+ result.back`
  - **RecognizeWebImage**
    - changes of request param
      - `+ detect_text_direction`

### HuaweiCloud SDK RDS

- _Features_
  - Support the following interfaces：
    - `ListPostgresqlHbaInfo`
    - `ModifyPostgresqlHbaConf`
    - `AddPostgresqlHbaConf`
    - `DeletePostgresqlHbaConf`
    - `ListPostgresqlHbaInfoHistory`
- _Bug Fix_
  - None
- _Change_
  - **UpgradeDbVersionNew**
    - changes of request param
      - `+ is_delayed`
      - `- delay`

### HuaweiCloud SDK ServiceStage

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ModifyComponent**
    - changes of request param
      - `+ external_accesses.protocol`
      - `- external_accesses.prorocol`
  - **CreateComponent**
    - changes of request param
      - `+ external_accesses`
  - **ShowComponentsInApplication**
    - changes of response param
      - `+ components.external_accesses.protocol`
      - `- components.external_accesses.prorocol`
  - **ShowComponents**
    - changes of response param
      - `+ components.external_accesses.protocol`
      - `- components.external_accesses.prorocol`

### HuaweiCloud SDK SMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowCertKey**
    - changes of request param
      - `+ enable_ca_cert`
    - changes of response param
      - `+ target_mgmt_private_key`
      - `+ target_data_cert`
      - `+ target_data_private_key`
      - `+ target_mgmt_cert`
      - `+ ca`

### HuaweiCloud SDK VPC

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK WorkspaceApp

- _Features_
  - Support the following interfaces：
    - `CreateOrUpdateStoragePolicyStatement`
    - `ShowPublishableApp`
    - `UploadAppIcon`
    - `ListSessionByUserName`
    - `LogoffUserSession`
    - `ListSessionType`
- _Bug Fix_
  - None
- _Change_
  - **ListStoragePolicyStatement**
    - changes of response param
      - `+ roam_actions`
      - `+ actions`
      - `+ policy_statement_id`
      - `+ items.roam_actions`
  - **UpdateAppGroup**
    - changes of response param
      - `+ app_type`
  - **ListAppConnection**
    - changes of request param
      - `* limit: required -> optional`
      - `* offset: required -> optional`
  - **ListUserConnection**
    - changes of request param
      - `* limit: required -> optional`
      - `* offset: required -> optional`
  - **UpdateServerGroup**
    - changes of request param
      - `+ storage_mount_policy`
      - `+ app_type`
      - `+ route_policy.cpu_threshold`
      - `+ route_policy.mem_threshold`
  - **ListProduct**
    - changes of response param
      - `+ products.expire_time`
      - `+ products.support_gpu_type`
  - **CreateAppGroup**
    - changes of request param
      - `+ app_type`
    - changes of response param
      - `+ app_type`
  - **ListAppGroup**
    - changes of request param
      - `+ app_type`
      - `* limit: required -> optional`
      - `* offset: required -> optional`
    - changes of response param
      - `+ app_type`
      - `+ items.app_type`
  - **ListPublishedApp**
    - changes of request param
      - `* limit: required -> optional`
      - `* offset: required -> optional`
  - **PublishApp**
    - changes of request param
      - `+ accounts.telephone_number`
  - **AddAppGroupAuthorization**
    - changes of request param
      - `+ accounts.telephone_number`
  - **ListAppGroupAuthorization**
    - changes of request param
      - `* limit: required -> optional`
      - `* offset: required -> optional`
  - **BatchDeleteAppGroupAuthorization**
    - changes of request param
      - `+ accounts.telephone_number`
  - **ListStorageAssignment**
    - changes of response param
      - `+ roam_actions`
      - `+ actions`
      - `+ policy_statement_id`
      - `+ items.policy_statement.roam_actions`
  - **ListServers**
    - changes of request param
      - `* offset: required -> optional`
      - `* limit: required -> optional`
    - changes of response param
      - `+ items.product_info.expire_time`
      - `+ items.product_info.support_gpu_type`
      - `+ items.vm_status: enum value [BUILD_IMAGE]`
      - `+ items.task_status: enum value [build_image]`
  - **CreateServerGroup**
    - changes of request param
      - `+ app_type`
      - `+ extra_session_type`
      - `+ extra_session_size`
      - `+ route_policy.cpu_threshold`
      - `+ route_policy.mem_threshold`
    - changes of response param
      - `+ app_type`
      - `+ extra_session_size`
      - `+ extra_session_type`
      - `+ storage_mount_policy`
      - `+ product_info.expire_time`
      - `+ product_info.support_gpu_type`
  - **ListServerGroups**
    - changes of request param
      - `+ app_type`
      - `* offset: required -> optional`
      - `* limit: required -> optional`
    - changes of response param
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
    - changes of request param
      - `* offset: required -> optional`
      - `* limit: required -> optional`
  - **ListPolicyTemplate**
    - changes of request param
      - `* offset: required -> optional`
      - `* limit: required -> optional`

# 3.1.60 2023-09-19

### HuaweiCloud SDK IdentityCenterStore

- _Features_
  - Support the service `IdentityCenterStore`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateBareMetalServers**
    - changes of request param
      - `* server.server_tags: list<SystemTags> -> map<string, list<SystemTags>>`

### HuaweiCloud SDK CAE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateComponentConfiguration**
    - changes of request param
      - `+ items.type: enum value [customMetric]`

### HuaweiCloud SDK CPH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `BatchMigrateCloudPhone`, `CreateCloudPhoneServer`
  - **PushShareApps**
    - changes of response param
      - `+ jobs`
      - `+ request_id`
  - **DeleteShareApps**
    - changes of response param
      - `+ jobs`
      - `+ request_id`
  - **PushShareFiles**
    - changes of response param
      - `+ jobs`
      - `+ request_id`
  - **ListCloudPhones**
    - changes of response param
      - `+ count`
  - **ShowCloudPhoneDetail**
    - changes of response param
      - `+ access_infos.phone_ipv6`
      - `+ access_infos.server_ipv6`
  - **ListCloudPhoneServerModels**
    - changes of response param
      - `+ server_models.free_size`
  - **CreateNet2CloudPhoneServer**
    - changes of request param
      - `+ nics.ipv6_enable`
      - `+ nics.ipv6_bandwidth`
  - **ListEncodeServers**
    - changes of response param
      - `+ encode_servers.encode_server_ipv6`
      - `+ encode_servers.access_infos.server_ipv6`
  - **ListCloudPhoneServers**
    - changes of response param
      - `+ count`

### HuaweiCloud SDK CTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateTracker**
    - changes of request param
      - `+ is_organization_tracker`
      - `+ management_event_selector`
  - **CreateTracker**
    - changes of request param
      - `+ is_organization_tracker`
      - `+ management_event_selector`
    - changes of response param
      - `+ is_organization_tracker`
      - `+ management_event_selector`
  - **ListTrackers**
    - changes of response param
      - `+ trackers.is_organization_tracker`
      - `+ trackers.management_event_selector`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the interface `ListActiveAsyncInvocations`
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
  - **CreateInstance**
    - changes of request param
      - `+ availability_zone_detail`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListInstanceTopics**
    - changes of response param
      - `+ topic_max_partitions`

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateTranscodingsTemplate**
    - changes of request param
      - `+ quality_info.bitrate_adaptive`
      - `+ quality_info.i_frame_policy`
  - **CreateTranscodingsTemplate**
    - changes of request param
      - `+ quality_info.bitrate_adaptive`
      - `+ quality_info.i_frame_policy`
  - **ShowTranscodingsTemplate**
    - changes of response param
      - `+ templates.quality_info.bitrate_adaptive`
      - `+ templates.quality_info.i_frame_policy`

### HuaweiCloud SDK LTS

- _Features_
  - Support the following interfaces：
    - `ShowLogConvergeConfig`
    - `ShowAdminConfig`
    - `UpdateSwitch`
    - `ShowMemberGroupAndStream`
    - `UpdateLogConvergeConfig`
- _Bug Fix_
  - None
- _Change_
  - **ListCharts**
    - changes of response param
      - `+ config.can_sort`
      - `+ config.can_search`
      - `+ config.page_size`
      - `* config: object -> object<ChartConfig>`
  - **ShowNotificationTemplate**
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of request param
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
    - changes of response param
      - `+ frequency.type`
      - `+ frequency.cron_expr`
      - `+ frequency.hour_of_day`
      - `+ frequency.day_of_week`
      - `+ frequency.fixed_rate`
      - `+ frequency.fixed_rate_unit`
      - `* frequency: object -> object<Frequency>`
  - **CreateSqlAlarmRule**
    - changes of request param
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
    - changes of response param
      - `+ sql_alarm_rules.frequency.type`
      - `+ sql_alarm_rules.frequency.cron_expr`
      - `+ sql_alarm_rules.frequency.hour_of_day`
      - `+ sql_alarm_rules.frequency.day_of_week`
      - `+ sql_alarm_rules.frequency.fixed_rate`
      - `+ sql_alarm_rules.frequency.fixed_rate_unit`
      - `* sql_alarm_rules.frequency: object -> object<Frequency>`
  - **UpdateKeywordsAlarmRule**
    - changes of request param
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
    - changes of request param
      - `+ notification_save_rule.language`
      - `+ notification_save_rule.timezone`
      - `+ notification_save_rule.user_name`
      - `+ notification_save_rule.topics`
      - `+ notification_save_rule.template_name`
      - `* notification_save_rule: object -> object<SqlNotificationSaveRule>`
  - **ListKeywordsAlarmRules**
    - changes of response param
      - `+ keywords_alarm_rules.frequency.type`
      - `+ keywords_alarm_rules.frequency.cron_expr`
      - `+ keywords_alarm_rules.frequency.hour_of_day`
      - `+ keywords_alarm_rules.frequency.day_of_week`
      - `+ keywords_alarm_rules.frequency.fixed_rate`
      - `+ keywords_alarm_rules.frequency.fixed_rate_unit`
      - `* keywords_alarm_rules.frequency: object -> object<Frequency>`

### HuaweiCloud SDK MetaStudio

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **CreatePictureModelingByUrlJob**
    - changes of request param
      - `+ X-User-Privilege`

### HuaweiCloud SDK MRS

- _Features_
  - Support the interfaces `ExpandCluster`, `ShrinkCluster`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OCR

- _Features_
  - Support the interfaces `RecognizeVehicleCertificate`, `RecognizeAcceptanceBill`, `RecognizeRealEstateCertificate`, `RecognizeVietnamIdCard`
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
  - **UpdateConsumerGroup**
    - changes of request param
      - `* body: object<ConsumerGroup> -> object<UpdateConsumerGroup>`
  - **CreateRocketMqMigrationTask**
    - changes of response param
      - `+ task_id`

### HuaweiCloud SDK SMS

- _Features_
  - Support the interfaces `ShowPrivacyAgreements`, `CreatePrivacyAgreements`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.59 2023-09-14

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateBareMetalServers**
    - changes of request param
      - `+ server.nics.allowed_address_pairs`

### HuaweiCloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateVault**
    - changes of request param
      - `- vault.billing.promotion_info`
      - `- vault.billing.purchase_mode`
      - `- vault.billing.order_id`
  - **CreatePostPaidVault**
    - changes of request param
      - `- vault.billing.promotion_info`
      - `- vault.billing.purchase_mode`
      - `- vault.billing.order_id`

### HuaweiCloud SDK CES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateEvents**
    - changes of request param
      - `- detail.dimensions`
  - **ListEventDetail**
    - changes of response param
      - `* event_info.detail.dimensions: object<MetricsDimension> -> list<MetricsDimension>`
      - `* event_info.detail: object<EventItemDetail> -> object<ShowEventItemDetail>`

### HuaweiCloud SDK CodeArtsDeploy

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowAppDetailById**
    - changes of response param
      - `* result.arrange_infos: object -> list<TaskV2Info>`
  - **ListNewHosts**
    - changes of response param
      - `+ result.permission.can_copy`
      - `- result.permission.can_connection_test`
      - `* result.permission: object<PermissionHostDetail> -> object<PermissionHostDetailNew>`
  - **ShowHostDetail**
    - changes of response param
      - `* result.proxy_host: string -> object<HostInfoDetail>`
      - `+ result.permission.can_copy`
      - `- result.permission.can_connection_test`
      - `* result.permission: object<PermissionHostDetail> -> object<PermissionHostDetailNew>`

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowAgentConfig**
    - changes of response param
      - `+ result.elasticsearch_enable`
      - `+ result.elasticsearch_shadow_type`
      - `+ result.elasticsearch_shadow_repository`
  - **UpdateAgentHealthStatus**
    - changes of response param
      - `+ result.result.elasticsearch_enable`
      - `+ result.result.elasticsearch_shadow_type`
      - `+ result.result.elasticsearch_shadow_repository`

### HuaweiCloud SDK CSMS

- _Features_
  - Support the following interfaces：
    - `ListSecretEvents`
    - `CreateSecretEvent`
    - `ShowSecretEvent`
    - `UpdateSecretEvent`
    - `DeleteSecretEvent`
    - `ListNotificationRecords`
    - `UpdateVersion`
- _Bug Fix_
  - None
- _Change_
  - **ListSecrets**
    - changes of request param
      - `+ event_name`
    - changes of response param
      - `+ secrets.secret_type`
      - `+ secrets.auto_rotation`
      - `+ secrets.rotation_period`
      - `+ secrets.rotation_config`
      - `+ secrets.rotation_time`
      - `+ secrets.next_rotation_time`
      - `+ secrets.event_subscriptions`
      - `+ secrets.enterprise_project_id`
  - **CreateSecret**
    - changes of request param
      - `+ secret_type`
      - `+ auto_rotation`
      - `+ rotation_period`
      - `+ rotation_config`
      - `+ event_subscriptions`
      - `+ enterprise_project_id`
    - changes of response param
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **ShowSecret**
    - changes of response param
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **UpdateSecret**
    - changes of request param
      - `+ auto_rotation`
      - `+ rotation_period`
      - `+ event_subscriptions`
    - changes of response param
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **UploadSecretBlob**
    - changes of response param
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **ListSecretVersions**
    - changes of response param
      - `+ version_metadatas.expire_time`
  - **CreateSecretVersion**
    - changes of request param
      - `+ expire_time`
    - changes of response param
      - `+ version_metadata.expire_time`
  - **DeleteSecretForSchedule**
    - changes of response param
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **RestoreSecret**
    - changes of response param
      - `+ secret.secret_type`
      - `+ secret.auto_rotation`
      - `+ secret.rotation_period`
      - `+ secret.rotation_config`
      - `+ secret.rotation_time`
      - `+ secret.next_rotation_time`
      - `+ secret.event_subscriptions`
      - `+ secret.enterprise_project_id`
  - **ListSecretTags**
    - changes of response param
      - `* sys_tags: list<TagItem> -> list<SysTag>`
  - **ListProjectSecretsTags**
    - changes of response param
      - `* tags: list<Tag> -> list<TagResponse>`
  - **ShowSecretVersion**
    - changes of response param
      - `+ version.version_metadata.expire_time`
  - **ListResourceInstances**
    - changes of request param
      - `* matches: list<TagItem> -> list<TagMatches>`
    - changes of response param
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

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListFlavors**
    - changes of response param
      - `+ flavors.replica_count`

### HuaweiCloud SDK DGC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateResource**
    - changes of request param
      - `+ jobRelation`
      - `+ dependPackages`
      - `+ id`
      - `+ type: enum value [pyFile]`
  - **ShowResource**
    - changes of response param
      - `+ jobRelation`
      - `+ dependPackages`
      - `+ id`
      - `+ type: enum value [pyFile]`
  - **UpdateResource**
    - changes of request param
      - `+ jobRelation`
      - `+ dependPackages`
      - `+ id`
      - `+ type: enum value [pyFile]`
  - **ListConnections**
    - changes of request param
      - `+ limit`
      - `+ offset`
      - `+ connectionName`
  - **ListScripts**
    - changes of request param
      - `+ limit`
      - `+ offset`
      - `+ scriptName`
  - **ListJobs**
    - changes of request param
      - `+ limit`
      - `+ offset`
      - `+ jobType`
      - `+ jobName`
  - **ListSupplementdata**
    - changes of request param
      - `+ sort`
      - `+ page`
      - `+ size`
      - `+ name`
      - `+ userName`
      - `+ status`
      - `+ startDate`
      - `+ endDate`
    - changes of response param
      - `* rows.endDate: number -> int64`
      - `* rows.startDate: number -> int64`
      - `* rows.submittedDate: number -> int64`
      - `+ rows.supplement_data_instance_time.days`
      - `+ rows.supplement_data_instance_time.time_of_day`
      - `+ rows.supplement_data_run_time.time_of_day`
      - `+ rows.supplement_data_run_time.day_of_week`
      - `+ rows.supplement_data_run_time.day_of_month`
  - **CreateSupplementdata**
    - changes of request param
      - `+ supplement_data_run_time`
      - `+ supplement_data_instance_time`

### HuaweiCloud SDK EVS

- _Features_
  - Support the interface `ModifyVolumeQoS`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the interfaces `ShowFunctionUrl`, `UpdateFunctionUrl`, `CreateFunctionUrl`, `DeleteFunctionUrl`
- _Bug Fix_
  - None
- _Change_
  - **UpdateFuncSnapshot**
    - changes of request param
      - `+ action: enum value [enable,disable]`
  - **CreateFunction**
    - changes of request param
      - `+ custom_image`
      - `+ code_type: enum value [Custom-Image-Swr]`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interface `ListAuditLogDownloadLink`
- _Bug Fix_
  - None
- _Change_
  - **CreateGaussMySqlInstance**
    - changes of response param
      - `+ instance.volume`

### HuaweiCloud SDK Image

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
    - `RunImageDescription`
    - `RunImageSuperResolution`
    - `CreateVideoTaggingMediaTask`
    - `ShowVideoTaggingMediaTask`
    - `CreateImageHighresolutionMattingTask`
    - `ShowImageHighresolutionMattingTask`

### HuaweiCloud SDK IoTEdge

- _Features_
  - Support the following interfaces：
    - `CreateSchedule`
    - `UpdateSchedule`
    - `DeleteSchedule`
    - `ExecuteDeviceControlsSet`
    - `ExecuteDeviceControlsRelease`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Kafka

- _Features_
  - Support the interfaces `UpdateInstanceConsumerGroup`, `UpdateInstanceUser`
- _Bug Fix_
  - None
- _Change_
  - **CreateKafkaConsumerGroup**
    - changes of request param
      - `+ group_desc`
  - **CreateInstanceUser**
    - changes of request param
      - `+ user_desc`
  - **ShowInstanceUsers**
    - changes of response param
      - `+ users.user_desc`
  - **ShowInstanceMessages**
    - changes of request param
      - `+ keyword`

### HuaweiCloud SDK KPS

- _Features_
  - Support the interfaces `ImportPrivateKey`, `ExportPrivateKey`, `BatchAssociateKeypair`, `ClearPrivateKey`
- _Bug Fix_
  - None
- _Change_
  - **ListKeypairDetail**
    - changes of response param
      - `+ keypair.key_id`
      - `+ keypair.algorithm`
  - **ListFailedTask**
    - changes of request param
      - `* limit: string -> int32`
      - `* offset: string -> int32`
  - **AssociateKeypair**
    - changes of request param
      - `+ server.port`
    - changes of response param
      - `+ error_msg`
      - `+ error_code`
      - `+ server_id`
      - `+ status`
  - **DisassociateKeypair**
    - changes of response param
      - `+ error_msg`
      - `+ error_code`
      - `+ server_id`
      - `+ status`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListCharts**
    - changes of response param
      - `- config.can_sort`
      - `- config.can_search`
      - `- config.page_size`
  - **ShowNotificationTemplate**
    - changes of response param
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
    - changes of request param
      - `- tag`
    - changes of response param
      - `* log_streams: list<LogStream> -> list<LogStreamResBody>`
  - **ListStructuredLogsWithTimeRange**
    - changes of response param
      - `+ context`
      - `- body`
  - **DeleteTransfer**
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of response param
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
    - changes of request param
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
    - changes of response param
      - `- frequency.type`
      - `- frequency.cron_expr`
      - `- frequency.hour_of_day`
      - `- frequency.day_of_week`
      - `- frequency.fixed_rate`
      - `- frequency.fixed_rate_unit`
  - **CreateSqlAlarmRule**
    - changes of request param
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
    - changes of response param
      - `- sql_alarm_rules.frequency.type`
      - `- sql_alarm_rules.frequency.cron_expr`
      - `- sql_alarm_rules.frequency.hour_of_day`
      - `- sql_alarm_rules.frequency.day_of_week`
      - `- sql_alarm_rules.frequency.fixed_rate`
      - `- sql_alarm_rules.frequency.fixed_rate_unit`
  - **UpdateKeywordsAlarmRule**
    - changes of request param
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
    - changes of request param
      - `- notification_save_rule.language`
      - `- notification_save_rule.timezone`
      - `- notification_save_rule.user_name`
      - `- notification_save_rule.topics`
      - `- notification_save_rule.template_name`
  - **ListKeywordsAlarmRules**
    - changes of response param
      - `- keywords_alarm_rules.frequency.type`
      - `- keywords_alarm_rules.frequency.cron_expr`
      - `- keywords_alarm_rules.frequency.hour_of_day`
      - `- keywords_alarm_rules.frequency.day_of_week`
      - `- keywords_alarm_rules.frequency.fixed_rate`
      - `- keywords_alarm_rules.frequency.fixed_rate_unit`

### HuaweiCloud SDK Meeting

- _Features_
  - Support the interface `DeleteToken`
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
  - **RunCreateVideoModerationJob**
    - changes of request param
      - `+ biz_type`
  - **RunCreateAudioModerationJob**
    - changes of request param
      - `+ biz_type`
  - **RunTextModeration**
    - changes of request param
      - `+ biz_type`
  - **CheckImageModeration**
    - changes of request param
      - `+ biz_type`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `RestoreTablesNew`, `UpgradeDbVersionNew`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.58 2023-09-07

### HuaweiCloud SDK AOS

- _Features_
  - Support the interface `DeleteStackEnhanced`
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
  - **ListScalingActivityLogs**
    - changes of response param
      - `* scaling_activity_log.scaling_value: string -> int32`
  - **CreateScalingPolicy**
    - changes of request param
      - `+ scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **UpdateScalingPolicy**
    - changes of request param
      - `+ scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ShowScalingPolicy**
    - changes of response param
      - `+ scaling_policy.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policy.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ListScalingPolicies**
    - changes of response param
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **CreateScalingV2Policy**
    - changes of request param
      - `+ scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ListAllScalingV2Policies**
    - changes of response param
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **UpdateScalingV2Policy**
    - changes of request param
      - `+ scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ShowScalingV2Policy**
    - changes of response param
      - `+ scaling_policy.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policy.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ListScalingV2Policies**
    - changes of response param
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
  - **ListScalingActivityV2Logs**
    - changes of response param
      - `* scaling_activity_log.scaling_value: string -> int32`
  - **CreateScalingGroup**
    - changes of request param
      - `+ lbaas_listeners.protocol_version`
  - **ListScalingGroups**
    - changes of response param
      - `+ scaling_groups.lbaas_listeners.protocol_version`
  - **UpdateScalingGroup**
    - changes of request param
      - `+ lbaas_listeners.protocol_version`
  - **ShowScalingGroup**
    - changes of response param
      - `+ scaling_group.lbaas_listeners.protocol_version`

### HuaweiCloud SDK CAE

- _Features_
  - Support the interfaces `ListEips`, `UpdateEip`
- _Bug Fix_
  - None
- _Change_
  - **ShowApplication**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Application]`
  - **CreateAgency**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Agency]`
  - **ListAgencies**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Agency]`
  - **ListEnvironments**
    - changes of response param
      - `+ kind`
      - `- Kind`
      - `+ api_version: enum value [v1]`
  - **CreateEnvironment**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Environment]`
  - **CreateApplication**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Application]`
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Application]`
  - **ListApplications**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Application]`
  - **ListComponentConfigurations**
    - changes of response param
      - `+ items.type: enum value [customMetric]`
  - **CreateComponentConfiguration**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [ComponentConfiguration]`
  - **ListComponentEvents**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [ComponentEvent]`
  - **ListComponentInstances**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [ComponentConfiguration]`
  - **ListVolumes**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Volume]`
  - **CreateVolume**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Volume]`
  - **DeleteVolume**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
  - **UpdateCertificate**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Certificate]`
  - **ListComponentSnapshots**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [ComponentSnapshot]`
  - **ShowJob**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Job]`
  - **ListDomains**
    - changes of response param
      - `+ api_version: enum value [v1]`
  - **CreateDomain**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Domain]`
    - changes of response param
      - `+ api_version: enum value [v1]`
  - **ListCertificates**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Certificate]`
  - **CreateCertificate**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Certificate]`
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Certificate]`
  - **ListTimerRules**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
  - **CreateTimerRule**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
  - **UpdateTimerRule**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
  - **ShowExecutionResult**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [TimerRule]`
  - **ShowComponent**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
  - **UpdateComponent**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
  - **ExecuteAction**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Action]`
  - **CreateComponent**
    - changes of request param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`
  - **ListComponents**
    - changes of response param
      - `+ api_version: enum value [v1]`
      - `+ kind: enum value [Component]`

### HuaweiCloud SDK CES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateEvents**
    - changes of request param
      - `+ detail.dimensions`
  - **ListEventDetail**
    - changes of response param
      - `- dimensions`
      - `+ event_info.detail.dimensions`

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowAgentConfig**
    - changes of response param
      - `+ result.pulsar_enable`
      - `+ result.pulsar_shadow_topic_prefix`
      - `+ result.mock_rule_list.response_header`
      - `+ result.mock_rule_list.response_body`
      - `+ result.mock_rule_list.response_time`
      - `+ result.mock_rule_list.response_code`
  - **UpdateAgentHealthStatus**
    - changes of response param
      - `+ result.result.pulsar_enable`
      - `+ result.result.pulsar_shadow_topic_prefix`
      - `+ result.result.mock_rule_list.response_header`
      - `+ result.result.mock_rule_list.response_body`
      - `+ result.result.mock_rule_list.response_time`
      - `+ result.result.mock_rule_list.response_code`

### HuaweiCloud SDK DGC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **StartJob**
    - changes of request param
      - `+ jobParams.type`
      - `- jobParams.paramType`
  - **RunOnce**
    - changes of request param
      - `+ jobParams.type`
      - `- jobParams.paramType`
  - **ListJobInstances**
    - changes of request param
      - `+ limit`
      - `+ offset`
      - `+ minPlanTime`
      - `+ maxPlanTime`
      - `+ status`
      - `+ preciseQuery`
      - `+ jobName`
      - `+ instanceType`
    - changes of response param
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
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of request param
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
    - changes of request param
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

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ShowDbObjectTemplateResult**
    - changes of request param
      - `+ type: enum value [change]`
  - **ShowUpdateObjectSavingStatus**
    - changes of request param
      - `+ X-Language: enum value [en-us,zh-cn]`
  - **ShowObjectMapping**
    - changes of request param
      - `+ X-Language: enum value [en-us,zh-cn]`
  - **ListJobs**
    - changes of request param
      - `+ instance_ids`
      - `+ instance_ip`
  - **ShowDbObjectCollectionStatus**
    - changes of request param
      - `+ X-Language: enum value [en-us,zh-cn]`
  - **UpdateBatchAsyncJobs**
    - changes of request param
      - `+ jobs.type: enum value [re_create,expired_days]`
  - **UpdateJob**
    - changes of request param
      - `+ job.type: enum value [re_create,expired_days]`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListInstancesResourceMetrics`, `ListInstancesRecommendation`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.57 2023-08-31

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListCustomerselfResourceRecordDetails**
    - changes of request param
      - `+ query_type`
      - `+ bill_cycle_begin`
      - `+ bill_cycle_end`

### HuaweiCloud SDK CAE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListComponentConfigurations**
    - changes of response param
      - `+ items.type: enum value [apm2,log]`
  - **CreateComponentConfiguration**
    - changes of request param
      - `+ items.type: enum value [apm2,log]`
  - **ListVolumes**
    - changes of response param
      - `+ items.resource_sub_type: enum value [sfs3.0]`
  - **CreateVolume**
    - changes of request param
      - `+ spec.resource_sub_type: enum value [sfs3.0]`
  - **UpdateCertificate**
    - changes of request param
      - `- spec.policy`
  - **ListDomains**
    - changes of response param
      - `- items.metadata.zone_id`
      - `- items.metadata.zone_type`
  - **CreateDomain**
    - changes of response param
      - `- items.metadata.zone_id`
      - `- items.metadata.zone_type`
  - **ListCertificates**
    - changes of response param
      - `- items.spec.policy`
  - **CreateCertificate**
    - changes of request param
      - `- spec.policy`
    - changes of response param
      - `- items.spec.policy`
  - **CreateComponent**
    - changes of request param
      - `+ spec.runtime: enum value [Java17,Nodejs14,Nodejs16]`

### HuaweiCloud SDK CCE

- _Features_
  - Support the interfaces `RollbackAddonInstance`, `ResizeCluster`, `BatchCreateClusterTags`, `BatchDeleteClusterTags`
- _Bug Fix_
  - None
- _Change_
  - **ShowAddonInstance**
    - changes of response param
      - `+ status.isRollbackable`
      - `+ status.previousVersion`
      - `+ status.status: enum value [rollbackFailed]`
  - **UpdateAddonInstance**
    - changes of response param
      - `+ status.isRollbackable`
      - `+ status.previousVersion`
      - `+ status.status: enum value [rollbackFailed]`
  - **CreateAddonInstance**
    - changes of response param
      - `+ status.isRollbackable`
      - `+ status.previousVersion`
      - `+ status.status: enum value [rollbackFailed]`
  - **ListAddonInstances**
    - changes of response param
      - `+ items.status.isRollbackable`
      - `+ items.status.previousVersion`
      - `+ items.status.status: enum value [rollbackFailed]`

### HuaweiCloud SDK CCM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **IssueCertificateAuthorityCertificate**
    - changes of request param
      - `+ enterprise_project_id`
  - **CreateCertificateByCsr**
    - changes of request param
      - `+ enterprise_project_id`

### HuaweiCloud SDK CES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowResourceGroup**
    - changes of response param
      - `+ resources.event_type`
  - **ListResourceGroup**
    - changes of response param
      - `+ resource_groups.type`
      - `+ resource_groups.relation_ids`
      - `+ resource_groups.resources`
  - **ListEventDetail**
    - changes of response param
      - `+ dimensions`

### HuaweiCloud SDK CES

- _Features_
  - Support the following interfaces：
    - `ListDashboardInfos`
    - `CreateOneDashboard`
    - `UpdateDashboard`
    - `DeleteDashboards`
    - `ListDashboardWidgets`
    - `CreateDashboardWidgets`
    - `ShowWidget`
    - `DeleteOneWidget`
    - `BatchUpdateWidgets`
- _Bug Fix_
  - None
- _Change_
  - **ListAlarmRulePolicies**
    - changes of response param
      - `+ policies.extra_info`
      - `+ policies.type`
      - `* policies: list<Policy> -> list<ListPolicy>`
  - **UpdateAlarmRulePolicies**
    - changes of request param
      - `+ policies.type`
      - `* policies: list<Policy> -> list<UpdatePolicy>`
    - changes of response param
      - `+ policies.type`
      - `* policies: list<Policy> -> list<UpdatePolicy>`
  - **ListAlarmTemplates**
    - changes of response param
      - `- alarm_templates.association_alarm_total`
      - `- alarm_templates.policy_total`
      - `- alarm_templates.policy_statistics`
      - `- alarm_templates.association_resource_groups`
  - **ShowAlarmTemplate**
    - changes of response param
      - `- association_alarm_total`

### HuaweiCloud SDK CodeArtsDeploy

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DAS

- _Features_
  - Support the interfaces `CreateTuning`, `ShowTuning`
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
  - **ShowInstance**
    - changes of response param
      - `+ available_zones`

### HuaweiCloud SDK DGC

- _Features_
  - Support the interfaces `ListSupplementdata`, `CreateSupplementdata`, `StopSupplementdata`
- _Bug Fix_
  - None
- _Change_
  - **ShowJob**
    - changes of response param
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **UpdateJob**
    - changes of request param
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **CreateJob**
    - changes of request param
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **ListJobs**
    - changes of response param
      - `* jobs.basicConfig.priority: string -> int32`
      - `* jobs.basicConfig.instanceTimeout: string -> int32`

### HuaweiCloud SDK DLF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowJob**
    - changes of response param
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **UpdateJob**
    - changes of request param
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **CreateJob**
    - changes of request param
      - `* basicConfig.priority: string -> int32`
      - `* basicConfig.instanceTimeout: string -> int32`
  - **ListJobs**
    - changes of response param
      - `* jobs.basicConfig.priority: string -> int32`
      - `* jobs.basicConfig.instanceTimeout: string -> int32`

### HuaweiCloud SDK DLI

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSqlJobs**
    - changes of response param
      - `+ jobs.cpu_cost`
      - `+ jobs.output_byte`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowJob**
    - changes of response param
      - `+ entities.server_id`
      - `+ entities.nic_id`
  - **CreateServers**
    - changes of request param
      - `+ server.extendparam.CB_CSBS_BACKUP`

### HuaweiCloud SDK ER

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BatchCreateResourceTags**
    - changes of request param
      - `- sys_tags`
  - **ShowStaticRoute**
    - changes of response param
      - `- route.attachments.priority`
  - **UpdateStaticRoute**
    - changes of response param
      - `- route.attachments.priority`
  - **ListStaticRoutes**
    - changes of response param
      - `- routes.attachments.priority`
  - **CreateStaticRoute**
    - changes of response param
      - `- route.attachments.priority`
  - **ListEffectiveRoutes**
    - changes of response param
      - `- routes.address_group_id`
      - `- routes.next_hops.priority`

### HuaweiCloud SDK FRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **DetectFaceByFile**
    - changes of response param
      - `+ faces.attributes.gender`
  - **DetectFaceByFileIntl**
    - changes of response param
      - `+ faces.attributes.gender`
  - **DetectFaceByUrl**
    - changes of response param
      - `+ faces.attributes.gender`
  - **DetectFaceByUrlIntl**
    - changes of response param
      - `+ faces.attributes.gender`
  - **DetectFaceByBase64**
    - changes of response param
      - `+ faces.attributes.gender`
  - **DetectFaceByBase64Intl**
    - changes of response param
      - `+ faces.attributes.gender`

### HuaweiCloud SDK GES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ExportGraph2**
    - changes of request param
      - `+ paginate`

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **StopSimCard**
    - changes of request param
      - `+ iccid`
  - **ResetSimCard**
    - changes of request param
      - `+ iccid`
  - **ShowSimCard**
    - changes of request param
      - `+ iccid`
  - **EnableSimCard**
    - changes of request param
      - `+ iccid`
  - **ShowRealNamed**
    - changes of request param
      - `+ iccid`
  - **StartStopNet**
    - changes of request param
      - `+ iccid`
  - **SetExceedCutNet**
    - changes of request param
      - `+ iccid`
  - **RegisterImei**
    - changes of request param
      - `+ iccid`
  - **DeleteRealName**
    - changes of request param
      - `+ iccid`
  - **SetSpeedValue**
    - changes of request param
      - `+ iccid`
  - **ListSimPricePlans**
    - changes of request param
      - `+ iccid`
  - **BatchSetTags**
    - changes of request param
      - `+ iccids`
  - **BatchSetAttributes**
    - changes of request param
      - `+ attributes.iccid`
  - **ShowMonthUsages**
    - changes of request param
      - `+ iccids`
    - changes of response param
      - `+ month_usages.iccid`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateInstanceByEngine**
    - changes of request param
      - `- engine_version: enum value [1.1.0,2.7]`
  - **CreatePostPaidInstance**
    - changes of request param
      - `- engine_version: enum value [1.1.0,2.7]`

### HuaweiCloud SDK KooMessage

- _Features_
  - Support the interfaces `ShowTemplateVideoThumbnail`, `SetPrimaryVideoThumbnail`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK MRS

- _Features_
  - Support the interface `ShowMrsVersionList`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OCR

- _Features_
  - Support the interface `RecognizeSmartDocumentRecognizer`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RAM

- _Features_
  - Support the interface `ListResourceTypes`
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
  - **ListInstances**
    - changes of response param
      - `+ instances.public_dns_names`

### HuaweiCloud SDK ServiceStage

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ChangeResourceInEnvironment**
    - changes of response param
      - `+ deploy_mode`

# 3.1.56 2023-08-24

HuaweiCloud SDK APIG

- Features
  - Support the following interfaces：
    - ListEndpointConnections
    - AcceptOrRejectEndpointConnections
    - ListEndpointPermissions
    - AddEndpointPermissions
    - DeleteEndpointPermissions
- Bug Fix
  - None
- Change
  - AssociateSignatureKeyV2
    - changes of response param
      - + bindings.req_method
  - ListSignatureKeysBindedToApiV2
    - changes of response param
      - + bindings.req_method
  - ListApisNotBoundWithSignatureKeyV2
    - changes of response param
      - + apis.req_method
  - ListApisBindedToSignatureKeyV2
    - changes of response param
      - + bindings.req_method
  - ListApisBindedToRequestThrottlingPolicyV2
    - changes of response param
      - + apis.req_method
  - ListApisUnbindedToRequestThrottlingPolicyV2
    - changes of response param
      - + apis.req_method
  - ListApiRuntimeDefinitionV2
    - changes of response param
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - ListApisBindedToAclPolicyV2
    - changes of response param
      - + apis.req_method
  - ListApisUnbindedToAclPolicyV2
    - changes of response param
      - + apis.req_method
  - ShowDetailsOfCustomAuthorizersV2
    - changes of response param
      - + network_type
  - UpdateCustomAuthorizerV2
    - changes of request param
      - + network_type
    - changes of response param
      - + network_type
  - ListInstancesV2
    - changes of response param
      - + instances.cbc_operation_locks
      - + instances.status: enum value [Resizing,ResizeFailed,ResizeTimeout]
      - + instances.instance_status: enum value [42,43,44]
      - + instances.spec: enum value [PLATINUM_X2,PLATINUM_X3,PLATINUM_X4,PLATINUM_X5,PLATINUM_X6,PLATINUM_X7,PLATINUM_X8]
  - CreateInstanceV2
    - changes of request param
      - + spec_id: enum value [PLATINUM_X2,PLATINUM_X3,PLATINUM_X4,PLATINUM_X5,PLATINUM_X6,PLATINUM_X7,PLATINUM_X8]
  - ShowDetailsOfInstanceV2
    - changes of response param
      - + cbc_operation_locks
      - + status: enum value [Resizing,ResizeFailed,ResizeTimeout]
      - + instance_status: enum value [42,43,44]
      - + spec: enum value [PLATINUM_X2,PLATINUM_X3,PLATINUM_X4,PLATINUM_X5,PLATINUM_X6,PLATINUM_X7,PLATINUM_X8]
  - UpdateInstanceV2
    - changes of response param
      - + cbc_operation_locks
      - + status: enum value [Resizing,ResizeFailed,ResizeTimeout]
      - + instance_status: enum value [42,43,44]
      - + spec: enum value [PLATINUM_X2,PLATINUM_X3,PLATINUM_X4,PLATINUM_X5,PLATINUM_X6,PLATINUM_X7,PLATINUM_X8]
  - ShowDetailsOfApiV2
    - changes of response param
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - UpdateApiV2
    - changes of request param
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
    - changes of response param
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - ListApiVersionDetailV2
    - changes of response param
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - CreateCustomAuthorizerV2
    - changes of request param
      - + network_type
    - changes of response param
      - + network_type
  - ListCustomAuthorizersV2
    - changes of response param
      - + network_type
      - + authorizer_list.network_type
  - CreateApiV2
    - changes of request param
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
    - changes of response param
      - + content_type: enum value [multipart/form-data]
      - - content_type: enum value [multipart/form-date]
  - ListApisV2
    - changes of response param
      - + apis.content_type: enum value [multipart/form-data]
      - - apis.content_type: enum value [multipart/form-date]

### HuaweiCloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RestoreBackup**
    - changes of request param
      - `+ restore.details`

### HuaweiCloud SDK CCM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowCertificateAuthority**
    - changes of response param
      - `+ enterprise_project_id`
  - **ShowCertificate**
    - changes of response param
      - `+ enterprise_project_id`
  - **CreateCertificateAuthority**
    - changes of request param
      - `+ enterprise_project_id`
  - **ListCertificateAuthority**
    - changes of response param
      - `+ enterprise_project_id`
      - `+ certificate_authorities.enterprise_project_id`
  - **CreateCertificate**
    - changes of request param
      - `+ enterprise_project_id`
  - **ListCertificate**
    - changes of response param
      - `+ enterprise_project_id`
      - `+ certificates.enterprise_project_id`

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowAgentConfig**
    - changes of response param
      - `+ result.clickhouse_enable`
      - `+ result.clickhouse_shadow_type`
      - `+ result.clickhouse_shadow_repository`
  - **UpdateAgentHealthStatus**
    - changes of response param
      - `+ result.result.clickhouse_enable`
      - `+ result.result.clickhouse_shadow_type`
      - `+ result.result.clickhouse_shadow_repository`

### HuaweiCloud SDK EG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateSubscriptionTarget**
    - changes of request param
      - `+ detail.url`
      - `+ detail.agency_name`
      - `+ detail.invocation_http_parameters`
      - `* detail: object -> object<Detail>`
  - **UpdateSubscriptionTarget**
    - changes of request param
      - `+ detail.url`
      - `+ detail.agency_name`
      - `+ detail.invocation_http_parameters`
      - `* detail: object -> object<Detail>`
  - **UpdateSubscription**
    - changes of request param
      - `+ targets.detail.url`
      - `+ targets.detail.agency_name`
      - `+ targets.detail.invocation_http_parameters`
      - `* targets.detail: object -> object<Detail>`
  - **CreateSubscription**
    - changes of request param
      - `+ targets.detail.url`
      - `+ targets.detail.agency_name`
      - `+ targets.detail.invocation_http_parameters`
      - `* targets.detail: object -> object<Detail>`

### HuaweiCloud SDK ER

- _Features_
  - Support the interfaces `AcceptAttachment`, `RejectAttachment`
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
  - **ListJarPackageHostInfo**
    - changes of response param
      - `* data_list.record_time: int32 -> int64`

### HuaweiCloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **GlanceListImages**
    - changes of response param
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

- _Features_
  - Support the following interfaces：
    - `BatchListAppConfigsTemplates`
    - `AddAppConfigsTemplates`
    - `ShowAppConfigsTemplate`
    - `DeleteAppConfigsTemplate`
    - `AddGeneralAppConfigsTemplate`
    - `ShowModuleShadow`
    - `UpdateModuleShadow`
- _Bug Fix_
  - None
- _Change_
  - **UpdateModule**
    - changes of request param
      - `+ desired_state`

### HuaweiCloud SDK KooMessage

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListAimResolveDetails**
    - changes of request param
      - `+ task_name`
    - changes of response param
      - `+ resolve_details.task_name`
  - **ListResolveTasks**
    - changes of request param
      - `+ task_name`
    - changes of response param
      - `+ resolve_tasks.task_name`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateLogStream**
    - changes of request param
      - `* tags: object<tagsBody> -> list<tagsBody>`

### HuaweiCloud SDK NAT

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListNatGateways**
    - changes of response param
      - `+ nat_gateways.session_conf`
  - **CreateNatGateway**
    - changes of request param
      - `+ nat_gateway.session_conf`
    - changes of response param
      - `+ nat_gateway.session_conf`
  - **ShowNatGateway**
    - changes of response param
      - `+ nat_gateway.session_conf`
  - **UpdateNatGateway**
    - changes of request param
      - `+ nat_gateway.session_conf`
    - changes of response param
      - `+ nat_gateway.session_conf`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RecognizeVatInvoice**
    - changes of request param
      - `+ page_num`
    - changes of response param
      - `+ result.invoice_tag`
      - `+ result.sum_amount`
      - `+ result.sum_tax`

### HuaweiCloud SDK OSM

- _Features_
  - Support the interface `ShowLoginType`
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
  - **RunTts**
    - changes of request param
      - `+ config.property: enum value [chinese_huaxiaoman_common,chinese_huaxiaofang_common,chinese_huaxiaojun_common]`

### HuaweiCloud SDK VPC

# 3.1.55 2023-08-21

### HuaweiCloud SDK EdgeSec

- _Features_
  - Support `EdgeSec`
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
  - **ListEdgeNodes**
    - changes of request param
      - `+ group_id`
  - **UpdateDeviceTwin**
    - changes of response param
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
    - changes of response param
      - `+ versions.configs.dns_policy`
  - **CreateAppVersions**
    - changes of request param
      - `+ version.configs.dns_policy`
    - changes of response param
      - `+ version.configs.dns_policy`
  - **ShowAppVersionDetail**
    - changes of response param
      - `+ version.configs.dns_policy`
  - **UpdateAppVersion**
    - changes of request param
      - `+ version.configs.dns_policy`
    - changes of response param
      - `+ version.configs.dns_policy`
  - **ListPods**
    - changes of request param
      - `+ plugin_instance_name`
    - changes of response param
      - `+ pods.configs.dns_policy`
  - **ListApps**
    - changes of response param
      - `+ apps.app_versions.configs.dns_policy`
  - **CreateApp**
    - changes of response param
      - `+ app.app_versions.configs.dns_policy`
  - **ShowAppDetail**
    - changes of response param
      - `+ app.app_versions.configs.dns_policy`
  - **UpdateApp**
    - changes of response param
      - `+ app.app_versions.configs.dns_policy`
  - **ListDeployments**
    - changes of response param
      - `+ deployments.template.configs.dns_policy`
  - **CreateDeployments**
    - changes of request param
      - `+ deployment.template.configs.dns_policy`
    - changes of response param
      - `+ template.configs.dns_policy`
  - **ShowDeployment**
    - changes of response param
      - `+ template.configs.dns_policy`
  - **UpdateDeployment**
    - changes of request param
      - `+ deployment.template.configs.dns_policy`
    - changes of response param
      - `+ template.configs.dns_policy`

### HuaweiCloud SDK LTS

- _Features_
  - Support the interface `DeleteDashboard`
- _Bug Fix_
  - None
- _Change_
  - **CreateDashBoard**
    - changes of response param
      - `* last_update_time: string -> int64`
      - `* useSystemTemplate: string -> boolean`
  - **CreateLogStream**
    - changes of request param
      - `- enterprise_project_name`
      - `- log_stream_name: enum value [lts-stream-13ci]`
      - `* ttl_in_days: string -> int32`
      - `* tags: list<tagsBody> -> object<tagsBody>`
  - **ListAccessConfig**
    - changes of response param
      - `+ cluster_id`
      - `+ result.cluster_id`
  - **UpdateAccessConfig**
    - changes of request param
      - `+ cluster_id`
    - changes of response param
      - `+ cluster_id`
  - **CreateAccessConfig**
    - changes of request param
      - `+ cluster_id`
    - changes of response param
      - `+ cluster_id`
  - **DeleteAccessConfig**
    - changes of response param
      - `+ cluster_id`
      - `+ result.cluster_id`

# 3.1.54 2023-08-17

### HuaweiCloud SDK AOS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateStack**
    - changes of request param
      - `+ agencies.agency_urn`
  - **GetStackMetadata**
    - changes of response param
      - `+ agencies.agency_urn`
  - **CreateStack**
    - changes of request param
      - `+ agencies.agency_urn`

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListApiRuntimeDefinitionV2**
    - changes of response param
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
  - **ShowDetailsOfApiV2**
    - changes of response param
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
  - **UpdateApiV2**
    - changes of request param
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
    - changes of response param
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
  - **ListApiVersionDetailV2**
    - changes of response param
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
  - **CreateApiV2**
    - changes of request param
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
    - changes of response param
      - `+ req_protocol: enum value [GRPCS]`
      - `+ backend_type: enum value [GRPC]`
      - `+ policy_https.req_protocol: enum value [GRPCS]`
      - `+ backend_api.req_protocol: enum value [GRPCS]`
  - **ListApisV2**
    - changes of response param
      - `+ apis.req_protocol: enum value [GRPCS]`
      - `+ apis.backend_type: enum value [GRPC]`
      - `+ apis.backend_api.req_protocol: enum value [GRPCS]`

### HuaweiCloud SDK CloudRTC

- _Features_
  - Support the interfaces `ListRtcAbnormalEvent`, `ListRtcEvent`, `ListObsBuckets`, `ListObsBucketObjects`, `UpdateObsBucketAuthority`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Cloudtest

- _Features_
  - Support the interfaces `ShowUserExecuteTestCaseInfo`, `ShowTestCaseAndDefectInfo`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DCS

- _Features_
  - Support the interface `ShowNodesInformation`
- _Bug Fix_
  - None
- _Change_
  - **ShowInstance**
    - changes of response param
      - `+ cloud_service_type_code`
      - `+ inquery_spec_code`
      - `+ cloud_resource_type_code`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateServers**
    - changes of request param
      - `+ server.root_volume.iops`
      - `+ server.root_volume.throughput`
      - `+ server.root_volume.volumetype: enum value [GPSSD2,ESSD2]`
      - `+ server.data_volumes.iops`
      - `+ server.data_volumes.throughput`
      - `+ server.data_volumes.volumetype: enum value [GPSSD2,ESSD2]`
  - **CreatePostPaidServers**
    - changes of request param
      - `+ server.data_volumes.iops`
      - `+ server.data_volumes.throughput`
      - `+ server.data_volumes.volumetype: enum value [GPSSD2,ESSD2]`
      - `+ server.root_volume.iops`
      - `+ server.root_volume.throughput`
      - `+ server.root_volume.volumetype: enum value [GPSSD2,ESSD2]`

### HuaweiCloud SDK eiHealth

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowEnv**
    - changes of response param
      - `+ public_bucket_path`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interfaces `ModifyGaussMysqlDns`, `CreateGaussMysqlDns`
- _Bug Fix_
  - None
- _Change_
  - **ShowGaussMySqlInstanceInfo**
    - changes of response param
      - `+ instance.private_dns_names`
  - **ListGaussMySqlInstanceDetailInfo**
    - changes of response param
      - `+ instances.private_dns_names`

### HuaweiCloud SDK ImageSearch

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
    - `RunCreateInstance`
    - `RunModifyPicture`
    - `RunAddPicture`
    - `RunDeletePicture`
    - `RunSearchPicture`
    - `RunCheckPicture`
    - `RunQueryInstance`
    - `RunDeleteInstance`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BatchRestartOrDeleteInstances**
    - changes of request param
      - `+ allFailure`
      - `- all_failure`
  - **CreateInstanceByEngine**
    - changes of request param
      - `- engine_version: enum value [2.3.0]`
  - **CreatePostPaidInstance**
    - changes of request param
      - `- engine_version: enum value [2.3.0]`

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSnapshotConfigs**
    - changes of response param
      - `* body: object<LiveSnapshotConfig> -> list<LiveSnapshotConfig>`

### HuaweiCloud SDK MetaStudio

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListAssetSummary**
    - changes of response param
      - `+ asset_list.asset_type: enum value [MUSIC]`
  - **ShowAsset**
    - changes of response param
      - `+ asset_type: enum value [MUSIC]`
      - `+ asset_state: enum value [BLOCK]`
      - `+ asset_extra_meta.human_model_2d_meta`
  - **UpdateDigitalAsset**
    - changes of request param
      - `+ asset_type: enum value [MUSIC]`
      - `+ asset_extra_meta.human_model_2d_meta`
    - changes of response param
      - `+ asset_type: enum value [MUSIC]`
      - `+ asset_state: enum value [BLOCK]`
      - `+ asset_extra_meta.human_model_2d_meta`
  - **CreateDigitalAsset**
    - changes of request param
      - `+ asset_type: enum value [MATERIAL,MUSIC]`
      - `+ asset_extra_meta.human_model_2d_meta`
  - **ListAssets**
    - changes of request param
      - `+ X-User-MePrivilege`
      - `+ action_editable`
    - changes of response param
      - `+ assets.asset_type: enum value [MUSIC]`
      - `+ assets.asset_state: enum value [BLOCK]`
      - `+ assets.asset_extra_meta.human_model_2d_meta`

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateThumbnailsTask**
    - changes of request param
      - `+ thumbnail_para.dots_ms`
      - `+ thumbnail_para.type: enum value [DOTS_MS]`
  - **CreateTranscodingTask**
    - changes of request param
      - `+ thumbnail.params.dots_ms`
      - `+ thumbnail.params.type: enum value [DOTS_MS]`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BatchRestartOrDeleteInstances**
    - changes of request param
      - `+ allFailure`
      - `- all_failure`
  - **CreatePostPaidInstanceByEngine**
    - changes of request param
      - `- engine_version: enum value [3.7.17]`
  - **CreatePostPaidInstance**
    - changes of request param
      - `- engine_version: enum value [3.7.17]`

### HuaweiCloud SDK RocketMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BatchDeleteInstances**
    - changes of request param
      - `+ allFailure`
      - `- all_failure`
  - **CreatePostPaidInstance**
    - changes of request param
      - `- engine_version: enum value [5.x]`

### HuaweiCloud SDK ServiceStage

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ModifyApplication**
    - changes of request param
      - `+ enterprise_project_id`
  - **CreateEnvironment**
    - changes of response param
      - `+ project_id`
      - `- resources`
  - **ShowEnvironments**
    - changes of response param
      - `+ environments.project_id`
  - **ShowEnvironmentInfo**
    - changes of response param
      - `+ project_id`
  - **ModifyEnvironment**
    - changes of request param
      - `- enterprise_project_id`
    - changes of response param
      - `+ project_id`
  - **ShowComponentInfo**
    - changes of response param
      - `+ affinity.az`
      - `+ affinity.node`
      - `+ affinity.component`
      - `- affinity.kind`
      - `- affinity.condition`
      - `- affinity.weight`
      - `- affinity.match_expressions`
  - **ModifyComponent**
    - changes of request param
      - `+ affinity.az`
      - `+ affinity.node`
      - `+ affinity.component`
      - `- affinity.kind`
      - `- affinity.condition`
      - `- affinity.weight`
      - `- affinity.match_expressions`
    - changes of response param
      - `- component_id`
  - **CreateComponent**
    - changes of request param
      - `+ affinity.az`
      - `+ affinity.node`
      - `+ affinity.component`
      - `- affinity.kind`
      - `- affinity.condition`
      - `- affinity.weight`
      - `- affinity.match_expressions`
  - **ShowComponentsInApplication**
    - changes of response param
      - `+ components.external_accesses`
  - **ShowComponents**
    - changes of response param
      - `+ components.external_accesses`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateSecurityGroupRule**
    - changes of request param
      - `+ security_group_rule.remote_address_group_id`
  - **NeutronCreateSecurityGroupRule**
    - changes of request param
      - `+ security_group_rule.remote_address_group_id`

# 3.1.53 2023-08-10

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSubCustomerBillDetail**
    - changes of response param
      - `+ fee_records.id

### HuaweiCloud SDK DNS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListPrivateZones**
    - changes of request param
      - `* type: optional -> required`

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListComputingResourceFlavors**
    - changes of response param
      - `+ flavors.az`
  - **StartAutoJob**
    - changes of response param
      - `+ max_platform_flavor`
      - `+ app_infos.app_resource`
  - **ListComputingResources**
    - changes of response param
      - `+ resources.evs_resource_id`
  - **ExecuteJob**
    - changes of response param
      - `+ max_platform_flavor`
      - `+ app_infos.app_resource`
  - **CreateAutoJob**
    - changes of response param
      - `+ max_platform_flavor`
      - `+ app_infos.app_resource`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interfaces `UpdateProxyPort`, `DescribeBackupEncryptStatus`, `ModifyBackupEncryptStatus`
- _Bug Fix_
  - None
- _Change_
  - **UpdateProxySessionConsistence**
    - changes of request param
      - `+ consistence_mode`
  - **CreateGaussMySqlInstance**
    - changes of request param
      - `* datastore: object<MysqlDatastore> -> object<MysqlDatastoreInReq>`
    - changes of response param
      - `* instance.datastore: object<MysqlDatastore> -> object<MysqlDatastoreInRes>`
  - **ShowGaussMySqlBackupList**
    - changes of response param
      - `- backups.datastore.kernel_version`
      - `* backups.datastore: object<MysqlDatastore> -> object<MysqlDatastoreInBackup>`
  - **ShowGaussMySqlProxyList**
    - changes of response param
      - `+ proxy_list.proxy.consistence_mode`

### HuaweiCloud SDK GSL

- _Features_
  - Support the interfaces `ListWorkOrders`, `ListWorkOrderDetails`
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
  - **ListInstanceConsumerGroups**
    - changes of response param
      - `+ groups.createdAt`
      - `+ groups.group_desc`
      - `+ groups.lag`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RecognizeMyanmarIdcard**
    - changes of request param
      - `+ return_translation`
    - changes of response param
      - `+ result.translation_info`

### HuaweiCloud SDK RAM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `SearchDistinctSharedResources`, `SearchDistinctPrincipals`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListXellogFiles`, `CreateXelLogDownload`
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
  - **ShowOneTopic**
    - changes of response param
      - `+ message_type`
  - **ShowTopicStatus**
    - changes of response param
      - `+ max_offset`
      - `+ min_offset`
  - **ShowInstance**
    - changes of response param
      - `+ grpc_address`
      - `+ public_grpc_address`
  - **CreateTopicOrBatchDeleteTopic**
    - changes of request param
      - `+ message_type`
  - **ListRocketInstanceTopics**
    - changes of response param
      - `+ message_type`
      - `+ topics.message_type`
  - **ListMessages**
    - changes of response param
      - `* messages.reconsume_times: string -> int32`
      - `* messages.queue_id: string -> int32`
      - `* messages.queue_offset: string -> int32`
  - **ExportDlqMessage**
    - changes of response param
      - `* reconsume_times: string -> int32`
      - `* queue_id: string -> int32`
      - `* queue_offset: string -> int32`
  - **CreatePostPaidInstance**
    - changes of request param
      - `+ engine_version: enum value [5.x]`
  - **ListInstances**
    - changes of response param
      - `+ grpc_address`
      - `+ public_grpc_address`
      - `+ instances.grpc_address`
      - `+ instances.public_grpc_address`
  - **ShowConsumerListOrDetails**
    - changes of response param
      - `+ lag`
      - `+ max_offset`
      - `+ consumer_offset`

# 3.1.52 2023-08-03

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListCustomerselfResourceRecords**
    - changes of response param
      - `+ fee_records.id`

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListCustomerselfResourceRecords**
    - changes of response param
      - `+ fee_records.id`

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowNode**
    - changes of response param
      - `- spec.extendParam.enterprise_project_id`
  - **UpdateNode**
    - changes of response param
      - `- spec.extendParam.enterprise_project_id`
  - **DeleteNode**
    - changes of response param
      - `- spec.extendParam.enterprise_project_id`
  - **CreateNode**
    - changes of request param
      - `- spec.extendParam.enterprise_project_id`
    - changes of response param
      - `- spec.extendParam.enterprise_project_id`
  - **ListNodes**
    - changes of response param
      - `- items.spec.extendParam.enterprise_project_id`
  - **ShowNodePool**
    - changes of response param
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
  - **UpdateNodePool**
    - changes of response param
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
  - **DeleteNodePool**
    - changes of response param
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
  - **CreateNodePool**
    - changes of request param
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
    - changes of response param
      - `- spec.nodeTemplate.extendParam.enterprise_project_id`
  - **ListNodePools**
    - changes of response param
      - `- items.spec.nodeTemplate.extendParam.enterprise_project_id`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDomainDetailByName**
    - changes of response param
      - `- domain.sources.weight`
      - `* domain.sources: list<SourcesConfig> -> list<SourcesDomainConfig>`
  - **ShowDomainFullConfig**
    - changes of response param
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
    - changes of request param
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

- _Features_
  - Support the following interfaces：
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
  - **ShowAgentConfig**
    - changes of request param
      - `+ alias`

### HuaweiCloud SDK CTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **DeleteTracker**
    - changes of request param
      - `+ tracker_type: enum value [system]`

### HuaweiCloud SDK EG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDetailOfEventSource**
    - changes of response param
      - `+ error_info`
  - **UpdateEventSource**
    - changes of response param
      - `+ error_info`
  - **CreateEventSource**
    - changes of response param
      - `+ error_info`
  - **ListEventSources**
    - changes of response param
      - `+ error_info`
      - `+ items.error_info`
  - **CreateSubscriptionTarget**
    - changes of request param
      - `+ smn_detail`
      - `+ dead_letter_queue`
    - changes of response param
      - `+ dead_letter_queue`
  - **ShowDetailOfSubscriptionTarget**
    - changes of response param
      - `+ dead_letter_queue`
  - **UpdateSubscriptionTarget**
    - changes of request param
      - `+ smn_detail`
      - `+ dead_letter_queue`
    - changes of response param
      - `+ dead_letter_queue`
  - **ShowDetailOfConnection**
    - changes of response param
      - `+ error_info`
  - **UpdateConnection**
    - changes of response param
      - `+ error_info`
  - **UpdateEndpoint**
    - changes of response param
      - `+ error_info`
  - **ShowDetailOfSubscription**
    - changes of response param
      - `+ dead_letter_queue`
      - `+ targets.dead_letter_queue`
  - **UpdateSubscription**
    - changes of request param
      - `+ targets.smn_detail`
      - `+ targets.dead_letter_queue`
    - changes of response param
      - `+ dead_letter_queue`
      - `+ targets.dead_letter_queue`
  - **CreateConnection**
    - changes of response param
      - `+ error_info`
  - **ListConnections**
    - changes of request param
      - `+ instance_id`
    - changes of response param
      - `+ error_info`
      - `+ items.error_info`
  - **CreateEndpoint**
    - changes of response param
      - `+ error_info`
  - **ListEndpoints**
    - changes of request param
      - `+ subnet_id`
    - changes of response param
      - `+ error_info`
      - `+ items.error_info`
  - **ShowEventStreaming**
    - changes of response param
      - `+ source.source_kafka.seek_to: enum value [latest,earliest]`
      - `+ source.source_kafka.sasl_mechanism: enum value [SCRAM-SHA-512,PLAIN]`
  - **UpdateEventStreaming**
    - changes of request param
      - `+ source.source_kafka.seek_to: enum value [latest,earliest]`
      - `+ source.source_kafka.sasl_mechanism: enum value [SCRAM-SHA-512,PLAIN]`
  - **CreateSubscription**
    - changes of request param
      - `+ targets.smn_detail`
      - `+ targets.dead_letter_queue`
    - changes of response param
      - `+ dead_letter_queue`
      - `+ targets.dead_letter_queue`
  - **ListSubscriptions**
    - changes of response param
      - `+ dead_letter_queue`
      - `+ items.targets.dead_letter_queue`
  - **ListTriggers**
    - changes of response param
      - `+ dead_letter_queue`
      - `+ items.targets.dead_letter_queue`
  - **ListWorkflowTriggers**
    - changes of response param
      - `+ dead_letter_queue`
      - `+ items.targets.dead_letter_queue`
  - **CreateEventStreaming**
    - changes of request param
      - `+ source.source_kafka.seek_to: enum value [latest,earliest]`
      - `+ source.source_kafka.sasl_mechanism: enum value [SCRAM-SHA-512,PLAIN]`
  - **ListEventStreaming**
    - changes of response param
      - `+ source.source_kafka.seek_to: enum value [latest,earliest]`
      - `+ source.source_kafka.sasl_mechanism: enum value [SCRAM-SHA-512,PLAIN]`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interface `ModifyGaussMySqlProxyRouteMode`
- _Bug Fix_
  - None
- _Change_
  - **ShowGaussMySqlEngineVersion**
    - changes of response param
      - `+ datastores.version`
      - `+ datastores.kernel_version`
  - **CreateGaussMySqlProxy**
    - changes of request param
      - `+ route_mode`
  - **CreateGaussMySqlInstance**
    - changes of request param
      - `+ datastore.kernel_version`
    - changes of response param
      - `+ instance.datastore.kernel_version`
  - **ShowGaussMySqlBackupList**
    - changes of response param
      - `+ backups.datastore.kernel_version`
  - **ShowGaussMySqlProxyList**
    - changes of response param
      - `+ proxy_list.proxy.route_mode`
      - `+ proxy_list.proxy.balance_route_mode_enabled`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListInstances**
    - changes of response param
      - `+ instances.backup_used_space`
  - **ListComponentInfos**
    - changes of request param
      - `+ component_type`
      - `+ availability_zone_id`
    - changes of response param
      - `+ nodes.name`
      - `+ nodes.availability_zone_id`
      - `+ nodes.description`
      - `+ nodes.status`
      - `+ nodes.components.distributed_id`
  - **ListInstancesDetails**
    - changes of response param
      - `+ instances.backup_used_space`

### HuaweiCloud SDK KooMessage

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **DeleteTemplateMaterial**
    - changes of response param
      - `+ data`
  - **DeleteAimPersonalTemplate**
    - changes of response param
      - `+ data`
  - **UnfreezePub**
    - changes of response param
      - `+ data.pub_id`
      - `- data.data`
  - **FreezePub**
    - changes of response param
      - `+ data.pub_id`
      - `- data.data`
  - **ListAimResolveDetails**
    - changes of response param
      - `* resolve_details.resolved_status: object -> string`
  - **CreateResolveTask**
    - changes of request param
      - `- params.sms_params`
      - `* params: list<CreateResolveTaskParam> -> list<CreateShortChainParam>`
  - **ListAimTemplates**
    - changes of response param
      - `+ templates.factory_info.version`
  - **CreateVmsTemplate**
    - changes of request param
      - `- reminders`

### HuaweiCloud SDK MetaStudio

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `ListSelfPrivileges`
  - **CreateFile**
    - changes of response param
      - `+ file_id`
      - `+ upload_url`
  - **ListAssetSummary**
    - changes of response param
      - `+ asset_list.asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
  - **CreateTtsa**
    - changes of request param
      - `+ X-App-UserId`
      - `+ X-User-Privilege`
  - **ListTtsaJobs**
    - changes of request param
      - `+ X-App-UserId`
  - **ListTtsaData**
    - changes of response param
      - `+ motions.eyes`
      - `* motions.root: list<object> -> list<number>`
      - `* motions.joints: list<object> -> list<number>`
  - **CreatePictureModelingJob**
    - changes of response param
      - `+ model_asset_id`
      - `+ job_id`
  - **ListPictureModelingJobs**
    - changes of request param
      - `+ sort_dir: enum value [asc,desc]`
  - **DeleteAsset**
    - changes of request param
      - `+ mode`
  - **ShowAsset**
    - changes of response param
      - `+ asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ asset_extra_meta.voice_model_meta.tts_mode`
      - `+ asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.human_model_meta.model_properties`
  - **UpdateDigitalAsset**
    - changes of request param
      - `+ asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ asset_extra_meta.voice_model_meta.tts_mode`
      - `+ asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.human_model_meta.model_properties`
    - changes of response param
      - `+ asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ asset_extra_meta.voice_model_meta.tts_mode`
      - `+ asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.human_model_meta.model_properties`
  - **ListStyles**
    - changes of request param
      - `+ sort_dir: enum value [asc,desc]`
    - changes of response param
      - `+ styles.extra_meta.model_id`
  - **CreateVideoMotionCaptureJob**
    - changes of response param
      - `+ rtc_room_info`
      - `+ job_id`
  - **CreateDigitalAsset**
    - changes of request param
      - `+ asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ asset_extra_meta.voice_model_meta.tts_mode`
      - `+ asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ asset_extra_meta.human_model_meta.model_properties`
  - **ListAssets**
    - changes of request param
      - `+ language`
      - `- lanuage`
      - `+ sort_dir: enum value [asc,desc]`
    - changes of response param
      - `+ assets.asset_type: enum value [HUMAN_MODEL_2D,BUSINESS_CARD_TEMPLET]`
      - `+ assets.system_properties.key: enum value [CREATED_BY_PLATFORM]`
      - `+ assets.asset_extra_meta.voice_model_meta.tts_mode`
      - `+ assets.asset_extra_meta.voice_model_meta.external_voice_meta`
      - `+ assets.asset_extra_meta.human_model_meta.model_properties`

### HuaweiCloud SDK MRS

- _Features_
  - Support the interfaces `ListDataConnector`, `CreateDataConnector`, `UpdateDataConnector`, `DeleteDataConnector`
- _Bug Fix_
  - None
- _Change_
  - **CreateCluster**
    - changes of request param
      - `+ charge_info.period_type`
      - `+ charge_info.period_num`
      - `+ charge_info.is_auto_pay`
  - **RunJobFlow**
    - changes of request param
      - `+ charge_info.period_type`
      - `+ charge_info.period_num`
      - `+ charge_info.is_auto_pay`

### HuaweiCloud SDK OSM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `CreateAuthorization`
  - **CreateMessages**
    - changes of request param
      - `- message.is_authorized`
      - `- message.authorization_content`
  - **CreateCases**
    - changes of request param
      - `- is_authorized`
      - `- authorization_content`
  - **ShowCaseDetail**
    - changes of response param
      - `- incident_detail_info.is_authorized`

### HuaweiCloud SDK ProjectMan

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowIssueV4**
    - changes of response param
      - `+ find_release_dev`
      - `+ release_dev`
      - `+ env`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListDatastores**
    - changes of request param
      - `+ database_name: enum value [MariaDB]`
  - **ListConfigurations**
    - changes of response param
      - `+ configurations.datastore_name: enum value [mariadb]`
  - **CreateConfiguration**
    - changes of request param
      - `+ datastore.type: enum value [MariaDB]`
    - changes of response param
      - `+ configuration.datastore_name: enum value [mariadb]`
  - **ShowConfiguration**
    - changes of response param
      - `+ datastore_name: enum value [mariadb]`
  - **ShowInstanceConfiguration**
    - changes of response param
      - `+ datastore_name: enum value [mariadb]`
  - **ListFlavors**
    - changes of request param
      - `+ database_name: enum value [MariaDB]`
  - **ListStorageTypes**
    - changes of request param
      - `+ database_name: enum value [MariaDB]`
  - **ListInstances**
    - changes of request param
      - `+ datastore_type: enum value [MariaDB]`
    - changes of response param
      - `+ instances.datastore.type: enum value [MariaDB]`
  - **CreateInstance**
    - changes of request param
      - `+ datastore.type: enum value [MariaDB]`
    - changes of response param
      - `+ instance.datastore.type: enum value [MariaDB]`
  - **CreateRestoreInstance**
    - changes of request param
      - `+ datastore.type: enum value [MariaDB]`
    - changes of response param
      - `+ instance.datastore.type: enum value [MariaDB]`
  - **ListBackups**
    - changes of response param
      - `+ backups.datastore.type: enum value [MariaDB]`
  - **ListOffSiteBackups**
    - changes of response param
      - `+ backups.datastore.type: enum value [MariaDB]`
  - **ListOffSiteInstances**
    - changes of response param
      - `+ offsite_backup_instances.datastore.type: enum value [MariaDB]`

### HuaweiCloud SDK RocketMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListMessageTrace**
    - changes of request param
      - `* msg_id: optional -> required`
  - **ListMessages**
    - changes of request param
      - `+ key`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListPorts**
    - changes of request param
      - `+ enable_efi`
    - changes of response param
      - `+ ports.enable_efi`
  - **CreatePort**
    - changes of response param
      - `+ port.enable_efi`
  - **ShowPort**
    - changes of response param
      - `+ port.enable_efi`
  - **UpdatePort**
    - changes of response param
      - `+ port.enable_efi`

# 3.1.51 2023-07-31

### HuaweiCloud SDK CAE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ExecuteAction**
    - changes of request param
      - `+ spec.build`

### HuaweiCloud SDK ProjectMan

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateIssueV4**
    - changes of response param
      - `+ find_release_dev`
      - `+ order`
      - `+ release_dev`
      - `+ env`
  - **ListIssuesV4**
    - changes of response param
      - `+ find_release_dev`
      - `+ order`
      - `+ release_dev`
      - `+ env`
      - `+ issues.order`
      - `+ issues.release_dev`
      - `+ issues.find_release_dev`
      - `+ issues.env`
  - **ListChildIssuesV4**
    - changes of response param
      - `+ find_release_dev`
      - `+ order`
      - `+ release_dev`
      - `+ env`
      - `+ issues.order`
      - `+ issues.release_dev`
      - `+ issues.find_release_dev`
      - `+ issues.env`

### HuaweiCloud SDK Workspace

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateDesktop**
    - changes of request param
      - `- security_groups.name`
      - `* security_groups: list<SecurityGroup> -> list<SecurityGroupInfo>`
  - **ShowDesktopDetail**
    - changes of response param
      - `- desktop.security_groups.name`
      - `* desktop.security_groups: list<SecurityGroup> -> list<SecurityGroupInfo>`
  - **ListDesktopsDetail**
    - changes of response param
      - `- desktops.security_groups.name`
      - `* desktops.security_groups: list<SecurityGroup> -> list<SecurityGroupInfo>`

# 3.1.50 2023-07-27

### HuaweiCloud SDK Cloudtest

- _Features_
  - Support the interfaces `ListTestCases`, `ListTestCaseHistories`, `ListBranches`, `ShowApiTestcaseHistories`
- _Bug Fix_
  - None
- _Change_
  - **ShowPlans**
    - changes of response param
      - `* expire_day: string -> int32`
  - **ShowPlanList**
    - changes of response param
      - `* expire_day: string -> int32`

### HuaweiCloud SDK CodeHub

- _Features_
  - Support the interfaces `CreateMergeRequestDiscussion`, `CreateMergeRequestDiscussionNote`, `ShowReviewSetting`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DRS

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **DownloadDbObjectTemplate**
    - changes of request param
      - `+ file_import_db_level`
  - **UploadDbObjectTemplate**
    - changes of request param
      - `+ file_import_db_level`
  - **ListAsyncJobs**
    - changes of response param
      - `+ jobs.status: enum value [AUTO_PARAM_VALIDATE_SUCCESS,COMMIT_SUCCESS]`
      - `- jobs.status: enum value [ASYNC_JOB_CREATING,ASYNC_JOB_CREATE_FAILED,ASYNC_JOB_COMPLETED]`
  - **CreateJob**
    - changes of request param
      - `+ job.node_info.base_info`
    - changes of response param
      - `+ is_clone_job`
      - `+ create_time`
      - `+ name`
      - `+ id`
      - `+ status`
      - `+ job.is_clone_job`
  - **BatchCreateJobsAsync**
    - changes of request param
      - `+ jobs.node_info.base_info`
  - **ListAsyncJobDetail**
    - changes of response param
      - `+ jobs.support_import_file_resp`
      - `+ jobs.instance_features`
      - `+ jobs.task_version`
      - `+ jobs.node_info.base_info`
  - **UpdateBatchAsyncJobs**
    - changes of request param
      - `+ jobs.type: enum value [policy]`
      - `- jobs.type: enum value [policy_config]`
      - `+ jobs.params.node_info.base_info`
  - **ShowJobDetail**
    - changes of request param
      - `+ type: enum value [file]`
    - changes of response param
      - `+ job.support_import_file_resp`
      - `+ job.instance_features`
      - `+ job.task_version`
      - `+ job.node_info.base_info`
  - **UpdateJob**
    - changes of request param
      - `+ job.type: enum value [policy]`
      - `- job.type: enum value [policy_config]`
      - `+ job.params.node_info.base_info`

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **AttachShareBandwidth**
    - changes of response param
      - `+ publicip.vnic.vtep`
      - `+ publicip.vnic.vni`
      - `+ publicip.vnic.port_profile`
  - **DetachShareBandwidth**
    - changes of response param
      - `+ publicip.vnic.vtep`
      - `+ publicip.vnic.vni`
      - `+ publicip.vnic.port_profile`
  - **EnableNat64**
    - changes of response param
      - `+ publicip.vnic.vtep`
      - `+ publicip.vnic.vni`
      - `+ publicip.vnic.port_profile`
  - **DisableNat64**
    - changes of response param
      - `+ publicip.vnic.vtep`
      - `+ publicip.vnic.vni`
      - `+ publicip.vnic.port_profile`
  - **AttachBatchPublicIp**
    - changes of response param
      - `+ publicips.publicip.vnic.vtep`
      - `+ publicips.publicip.vnic.vni`
      - `+ publicips.publicip.vnic.port_profile`
  - **DetachBatchPublicIp**
    - changes of response param
      - `+ publicips.publicip.vnic.vtep`
      - `+ publicips.publicip.vnic.vni`
      - `+ publicips.publicip.vnic.port_profile`

### HuaweiCloud SDK ER

- _Features_
  - Support the following interfaces：
    - `BatchCreateResourceTags`
    - `ShowQuotas`
    - `ListFlowLogs`
    - `CreateFlowLog`
    - `ShowFlowLog`
    - `UpdateFlowLog`
    - `DeleteFlowLog`
    - `EnableFlowLog`
    - `DisableFlowLog`
- _Bug Fix_
  - None
- _Change_
  - **ListProjectTags**
    - changes of request param
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
    - changes of response param
      - `+ tags`
  - **DeleteResourceTag**
    - changes of request param
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
  - **ShowResourceTag**
    - changes of request param
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
    - changes of response param
      - `+ tags`
  - **CreateResourceTag**
    - changes of request param
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
  - **ListEnterpriseRouters**
    - changes of request param
      - `+ owned_by_self`
  - **ShowStaticRoute**
    - changes of response param
      - `+ route.attachments.priority`
  - **UpdateStaticRoute**
    - changes of response param
      - `+ route.attachments.priority`
  - **ListStaticRoutes**
    - changes of response param
      - `+ routes.attachments.priority`
  - **CreateStaticRoute**
    - changes of response param
      - `+ route.attachments.priority`
  - **ListEffectiveRoutes**
    - changes of response param
      - `+ routes.address_group_id`
      - `+ routes.next_hops.priority`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateTags**
    - changes of request param
      - `+ tags.key`
      - `+ tags.value`
      - `* tags: list<Kv> -> list<KvItem>`
  - **DeleteTags**
    - changes of request param
      - `+ tags.key`
      - `+ tags.value`
      - `* tags: list<Kv> -> list<KvItem>`
  - **ShowResInstanceInfo**
    - changes of request param
      - `+ matches.key`
      - `+ matches.value`
      - `* matches: list<Kv> -> list<KvItem>`
    - changes of response param
      - `+ resources.tags.key`
      - `+ resources.tags.value`
      - `* resources.tags: list<Kv> -> list<KvItem>`

### HuaweiCloud SDK GA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListRegions**
    - changes of response param
      - `+ regions`
      - `- area_regions`

### HuaweiCloud SDK GaussDBforNoSQL

- _Features_
  - Support the interface `ShowInstanceBiactiveRegions`
- _Bug Fix_
  - None
- _Change_
  - **ListConfigurations**
    - changes of response param
      - `+ quota`
      - `+ configurations.mode`
  - **ListConfigurationTemplates**
    - changes of response param
      - `+ quota`
      - `+ configurations.mode`
  - **ShowInstanceConfiguration**
    - changes of response param
      - `+ mode`
      - `+ id`
  - **ListConfigurationDatastores**
    - changes of response param
      - `+ datastores.mode`
  - **ShowQuotas**
    - changes of request param
      - `+ datastore_type`
      - `+ mode`
  - **ListInstances**
    - changes of response param
      - `+ instances.datastore.whole_version`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the interface `DownloadBackup`
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
  - **ListPorts**
    - changes of request param
      - `* host_id: optional -> required`
  - **ListVulnerabilities**
    - changes of response param
      - `+ data_list.verify_num`

### HuaweiCloud SDK IoTDA

- _Features_
  - Support the following interfaces：
    - `ListDeviceTunnels`
    - `AddTunnel`
    - `ShowDeviceTunnel`
    - `CloseDeviceTunnel`
    - `DeleteDeviceTunnel`
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
  - **CreateInstanceByEngine**
    - changes of request param
      - `+ disk_encrypted_enable`
      - `+ disk_encrypted_key`

### HuaweiCloud SDK LTS

- _Features_
  - Support the interface `UpdateLogStream`
- _Bug Fix_
  - None
- _Change_
  - **UpdateLogGroup**
    - changes of request param
      - `+ tags`
  - **CreateLogGroup**
    - changes of request param
      - `+ tags`
  - **CreateLogStream**
    - changes of request param
      - `+ enterprise_project_name`
      - `+ ttl_in_days`
      - `+ tags`
      - `+ log_stream_name: enum value [lts-stream-13ci]`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowInstanceExtendProductInfo**
    - changes of response param
      - `+ monthly`
      - `+ hourly`
      - `- engine`
      - `- versions`
      - `- products`

### HuaweiCloud SDK RocketMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ValidateConsumedMessage**
    - changes of request param
      - `+ engine: enum value [reliability]`
  - **ListInstances**
    - changes of request param
      - `+ engine: enum value [reliability]`

### HuaweiCloud SDK SMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowConfigSetting**
    - changes of response param
      - `* configurations: string -> list<ConfigBody>`

# 3.1.49 2023-07-20

### HuaweiCloud SDK CloudRTC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateIndividualStreamJob**
    - changes of request param
      - `- publish_param`
  - **UpdateIndividualStreamJob**
    - changes of request param
      - `- publish_param`
  - **CreateMixJob**
    - changes of request param
      - `- publish_param`

### HuaweiCloud SDK EIP

- _Features_
  - Support the following interfaces：
    - `AttachShareBandwidth`
    - `AttachBatchPublicIp`
    - `DetachShareBandwidth`
    - `DetachBatchPublicIp`
    - `EnableNat64`
    - `DisableNat64`
    - `ListBandwidth`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ER

- _Features_
  - Support the following interfaces：
    - `BatchCreateResourceTags`
    - `ShowQuotas`
    - `ListFlowLogs`
    - `CreateFlowLog`
    - `ShowFlowLog`
    - `UpdateFlowLog`
    - `DeleteFlowLog`
    - `EnableFlowLog`
    - `DisableFlowLog`
- _Bug Fix_
  - None
- _Change_
  - **ListProjectTags**
    - changes of request param
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
    - changes of response param
      - `+ tags`
  - **DeleteResourceTag**
    - changes of request param
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
  - **ShowResourceTag**
    - changes of request param
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
    - changes of response param
      - `+ tags`
  - **CreateResourceTag**
    - changes of request param
      - `+ resource_type: enum value [ecn-attachment,connect-attachment,cfw-attachment]`
  - **ListEnterpriseRouters**
    - changes of request param
      - `+ owned_by_self`
  - **ShowStaticRoute**
    - changes of response param
      - `+ route.attachments.priority`
  - **UpdateStaticRoute**
    - changes of response param
      - `+ route.attachments.priority`
  - **ListStaticRoutes**
    - changes of response param
      - `+ routes.attachments.priority`
  - **CreateStaticRoute**
    - changes of response param
      - `+ route.attachments.priority`
  - **ListEffectiveRoutes**
    - changes of response param
      - `+ routes.address_group_id`
      - `+ routes.next_hops.priority`

### HuaweiCloud SDK IoTDA

- _Features_
  - Support the interface `DeleteBatchTask`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Kafka

- _Features_
  - Support the interfaces `ListTopicPartitions`, `ListTopicProducers`
- _Bug Fix_
  - None
- _Change_
  - **ListProducts**
    - changes of request param
      - `+ engine: enum value [kafka]`
  - **UpdateInstanceTopic**
    - changes of request param
      - `+ topics.topic_other_configs`
      - `+ topics.topic_desc`
  - **CreateInstanceTopic**
    - changes of request param
      - `+ topic_other_configs`
      - `+ topic_desc`
    - changes of response param
      - `+ id`
  - **ListInstanceTopics**
    - changes of request param
      - `- offset`
      - `- limit`
    - changes of response param
      - `+ topics.topic_other_configs`
      - `+ topics.topic_desc`
      - `+ topics.created_at`
  - **ListInstances**
    - changes of request param
      - `+ engine: enum value [kafka]`
  - **ResizeEngineInstance**
    - changes of request param
      - `+ engine: enum value [kafka]`

### HuaweiCloud SDK MetaStudio

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreatePictureModelingJob**
    - changes of request param
      - `- model_asset_id`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowInstanceExtendProductInfo**
    - changes of request param
      - `+ engine: enum value [rabbitmq]`
    - changes of response param
      - `+ engine`
      - `+ versions`
      - `+ products`
      - `- monthly`
      - `- hourly`
  - **ListProducts**
    - changes of request param
      - `+ engine: enum value [rabbitmq]`
  - **ResizeEngineInstance**
    - changes of request param
      - `+ engine: enum value [rabbitmq]`
  - **ShowEngineInstanceExtendProductInfo**
    - changes of request param
      - `+ engine: enum value [rabbitmq]`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `ListInstancesSupportFastRestore`
- _Bug Fix_
  - None
- _Change_
  - **RestoreTables**
    - changes of request param
      - `+ is_fast_restore`

# 3.1.48 2023-07-13

### HuaweiCloud SDK OROAS

- _Features_
  - Support `OROAS`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK AS

- _Features_
  - Support the interfaces `ListGroupScheduledTasks`, `CreateGroupScheduledTask`, `UpdateGroupScheduledTask`, `DeleteGroupScheduledTask`
- _Bug Fix_
  - None
- _Change_
  - **CreateScalingPolicy**
    - changes of request param
      - `+ scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **UpdateScalingPolicy**
    - changes of request param
      - `+ scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ShowScalingPolicy**
    - changes of response param
      - `+ scaling_policy.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policy.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ListScalingPolicies**
    - changes of response param
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **CreateScalingV2Policy**
    - changes of request param
      - `+ scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ListAllScalingV2Policies**
    - changes of response param
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **UpdateScalingV2Policy**
    - changes of request param
      - `+ scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ShowScalingV2Policy**
    - changes of response param
      - `+ scaling_policy.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policy.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`
  - **ListScalingV2Policies**
    - changes of response param
      - `+ scaling_policies.scheduled_policy.recurrence_type: enum value [DAILY,WEEKLY,MONTHLY]`
      - `- scaling_policies.scheduled_policy.recurrence_type: enum value [Daily,Weekly,Monthly]`

### HuaweiCloud SDK AntiDDoS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowNewTaskStatus**
    - changes of request param
      - `* task_id: optional -> required`

### HuaweiCloud SDK CAE

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **DeleteVolume**
    - changes of response param
      - `+ kind`
      - `+ api_version`
      - `+ items`
  - **ListAgencies**
    - changes of response param
      - `+ agencies`
      - `- items`
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Agency]`
  - **CreateAgency**
    - changes of request param
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Agency]`
      - `- metadata.name: enum value [cae_trust]`
  - **ListEnvironments**
    - changes of response param
      - `- items.type`
      - `- items.status: enum value [error]`
  - **CreateEnvironment**
    - changes of request param
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Environment]`
      - `- metadata.type`
    - changes of response param
      - `+ job_id`
      - `- metadata`
      - `- kind`
      - `- api_version`
  - **CreateApplication**
    - changes of request param
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Application]`
  - **ListApplications**
    - changes of response param
      - `+ items.annotations`
      - `+ items.created_at`
      - `+ items.updated_at`
  - **ListComponentSnapshots**
    - changes of response param
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
    - changes of response param
      - `- kind: enum value [Configuration]`
      - `+ items.type: enum value [rds,cse,env,access,scaling,volume,healthCheck,lifecycle]`
  - **CreateComponentConfiguration**
    - changes of request param
      - `- kind: enum value [Configuration]`
      - `+ items.type: enum value [rds,cse,env,access,scaling,volume,healthCheck,lifecycle]`
  - **ListComponentEvents**
    - changes of response param
      - `- kind: enum value [ComponentEvent]`
      - `+ items.involved_object_kind`
      - `- items.involved_object: enum value [Component,ComponentInstance,ComponentScaling]`
  - **ListComponentInstances**
    - changes of response param
      - `- api_version: enum value [v1]`
      - `- kind: enum value [ComponentInstance]`
  - **ListVolumes**
    - changes of request param
      - `+ resource_type: enum value [obs]`
    - changes of response param
      - `- kind: enum value [Volume]`
      - `- items.resource_type: enum value [obs]`
  - **CreateVolume**
    - changes of request param
      - `- kind: enum value [Volume]`
      - `- spec.resource_type: enum value [obs]`
  - **RetryJob**
    - changes of request param
      - `+ X-Enterprise-Project-ID`
      - `+ X-Environment-ID`
  - **ShowJob**
    - changes of request param
      - `+ X-Environment-ID`
    - changes of response param
      - `- kind: enum value [Job]`
      - `+ spec.progress`
  - **ShowComponent**
    - changes of response param
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
    - changes of request param
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
    - changes of request param
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Action]`
      - `* spec.source: object<Source> -> object<ActionOnComponentSource>`
  - **CreateComponent**
    - changes of request param
      - `- api_version: enum value [v1]`
      - `- kind: enum value [Component]`
    - changes of response param
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
    - changes of response param
      - `+ items.created_at`
      - `+ items.updated_at`
      - `- items.status`
      - `+ items.spec.resource_limit`
      - `+ items.spec.build_log_id`
      - `- items.spec.log_strategy`
      - `+ items.spec.runtime: enum value [Docker,Java8,Java11,Tomcat8,Tomcat9,Python3,Nodejs8,Php7]`

### HuaweiCloud SDK SIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **PushTranscriberJobs**
    - changes of request param
      - `+ Enterprise-Project-Id`

### HuaweiCloud SDK VPC

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.47 2023-07-06

### HuaweiCloud SDK CodeCheck

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - `CodeCheck` is renamed to `CodeArtsCheck`

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpgradeCluster**
    - changes of response param
      - `+ metadata`
      - `+ spec`
      - `- uid`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDomainDetailByName**
    - changes of response param
      - `+ domain.sources.weight`
  - **ShowDomainFullConfig**
    - changes of response param
      - `+ configs.business_type`
      - `+ configs.service_area`
      - `+ configs.sources.weight`
  - **UpdateDomainFullConfig**
    - changes of request param
      - `+ configs.business_type`
      - `+ configs.service_area`
      - `+ configs.sources.weight`

### HuaweiCloud SDK EVS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateVolume**
    - changes of request param
      - `+ volume.iops`
      - `+ volume.throughput`
      - `+ volume.volume_type: enum value [GPSSD2,ESSD2]`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **DeleteGaussMySqlReadonlyNode**
    - changes of response param
      - `+ order_id`
  - **DeleteGaussMySqlInstance**
    - changes of response param
      - `+ order_id`
  - **ShowSqlFilterRule**
    - changes of request param
      - `+ sql_type`
      - `- type`

### HuaweiCloud SDK HSS

- _Features_
  - Support the interfaces `ListJarPackageStatistics`, `ListJarPackageHostInfo`, `ListHostVuls`
- _Bug Fix_
  - None
- _Change_
  - **ListProtectionServer**
    - changes of response param
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
    - changes of request param
      - `+ process_whitelist`
  - **ListProtectionPolicy**
    - changes of request param
      - `+ protect_policy_id`
    - changes of response param
      - `+ data_list.process_whitelist`
  - **ListRiskConfigs**
    - changes of request param
      - `+ group_id`
  - **ListHostStatus**
    - changes of response param
      - `+ data_list.open_time`
  - **ListVulnerabilities**
    - changes of request param
      - `+ repair_priority`
      - `+ handle_status`
      - `+ cve_id`
      - `+ label_list`
      - `+ status`
      - `+ asset_value`
      - `+ group_name`
    - changes of response param
      - `+ data_list.cve_list`
      - `+ data_list.patch_url`
      - `+ data_list.repair_priority`
      - `+ data_list.hosts_num`
      - `+ data_list.repair_success_num`
      - `+ data_list.fixed_num`
      - `+ data_list.ignored_num`
  - **ListVulHosts**
    - changes of request param
      - `+ asset_value`
      - `+ group_name`
      - `+ handle_status`
      - `+ severity_level`
      - `+ is_affect_business`
    - changes of response param
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
    - changes of request param
      - `+ remark`
      - `+ select_type`
      - `+ type`
      - `+ host_data_list`
  - **ListHostProtectHistoryInfo**
    - changes of response param
      - `+ data_list.file_operation`
      - `+ data_list.host_name`
      - `+ data_list.host_ip`
  - **ListHostRaspProtectHistoryInfo**
    - changes of response param
      - `+ data_list.host_ip`
      - `+ data_list.host_name`
  - **ListHostGroups**
    - changes of response param
      - `+ data_list.is_outside`
  - **StartProtection**
    - changes of request param
      - `+ backup_resources`
      - `+ create_protection_policy.process_whitelist`
  - **ListSecurityEvents**
    - changes of request param
      - `+ event_class_ids`
  - **ChangeEvent**
    - changes of request param
      - `+ container_name`
      - `+ container_id`

### HuaweiCloud SDK IoTEdge

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowPointTemplate**
    - changes of response param
      - `* : string -> binary`
  - **ShowPoints**
    - changes of response param
      - `* : string -> binary`
  - **DownloadAppVersion**
    - changes of response param
      - `* : string -> binary`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateSqlAlarmRule**
    - changes of request param
      - `+ notification_save_rule.template_name`
  - **CreateSqlAlarmRule**
    - changes of request param
      - `+ notification_save_rule.template_name`
  - **UpdateKeywordsAlarmRule**
    - changes of request param
      - `+ notification_save_rule.template_name`
  - **CreateKeywordsAlarmRule**
    - changes of request param
      - `+ notification_save_rule.template_name`
  - **ListAccessConfig**
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of response param
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

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RunCreateVideoModerationJob**
    - changes of request param
      - `+ data.language`

### HuaweiCloud SDK RAM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **AssociateResourceShare**
    - changes of response param
      - `+ resource_share_associations.status_message`
  - **DisassociateResourceShare**
    - changes of response param
      - `+ resource_share_associations.status_message`
  - **SearchResourceShareAssociations**
    - changes of response param
      - `+ resource_share_associations.status_message`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSecurityGroupRules**
    - changes of request param
      - `+ remote_ip_prefix`

# 3.1.46 2023-06-29

### HuaweiCloud SDK IdentityCenter

- _Features_
  - Support `IdentityCenter`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK WorkspaceApp

- _Features_
  - Support `WorkspaceApp`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Config

- _Features_
  - Support `Config`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK AOS

- _Features_
  - Support the interface `ListTemplateVersions`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **DeleteTag**
    - changes of request param
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **ListCloudConnections**
    - changes of request param
      - `+ used_scene`
    - changes of response param
      - `+ cloud_connections.tags`
  - **CreateCloudConnection**
    - changes of response param
      - `+ cloud_connection.tags`
  - **ShowCloudConnection**
    - changes of response param
      - `+ cloud_connection.tags`
  - **UpdateCloudConnection**
    - changes of response param
      - `+ cloud_connection.tags`
  - **ListDomainTags**
    - changes of request param
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **BatchCreateDeleteTags**
    - changes of request param
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **ListTags**
    - changes of request param
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **CreateTag**
    - changes of request param
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`
  - **ListQuotas**
    - changes of request param
      - `* quota_type: optional -> required`
  - **CreateBandwidthPackage**
    - changes of request param
      - `+ bandwidth_package.spec_code`
  - **ListResourceByFilterTag**
    - changes of request param
      - `+ resource_type: enum value [cloud-connection,bandwidth-package]`
      - `+ resource_type: enum value [cc,bwp]`

### HuaweiCloud SDK DCS

- _Features_
  - Support the interfaces `ExecuteClusterSwitchover`, `ShowJobInfo`
- _Bug Fix_
  - None
- _Change_
  - **ListConfigTemplates**
    - changes of response param
      - `+ config_templates.created_at`
  - **CreateInstance**
    - changes of request param
      - `+ template_id`

### HuaweiCloud SDK DSC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateProductOrder**
    - changes of request param
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
    - changes of response param
      - `* orderInfos.productInfo: list<ProductInfoBean> -> object<ProductInfo>`
  - **ChangeRule**
    - changes of request param
      - `* body: object<RuleRequest> -> object<RuleChangeRequest>`

### HuaweiCloud SDK eiHealth

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
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

- _Features_
  - Support the following interfaces：
    - `ListIpGroups`
    - `CreateIpGroup`
    - `ShowIpGroup`
    - `UpdateIpGroup`
    - `DeleteIpGroup`
    - `AddIpGroupIp`
    - `RemoveIpGroupIp`
    - `AssociateListener`
    - `DisassociateListener`
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
  - **CreateCommand**
    - changes of response param
      - `+ error_msg`
      - `+ error_code`
  - **ListProperties**
    - changes of response param
      - `+ error_msg`
      - `+ error_code`
  - **UpdateProperties**
    - changes of response param
      - `+ error_msg`
      - `+ error_code`

### HuaweiCloud SDK ServiceStage

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ShowComponentConfigurations`, `CreateComponentConfiguration`, `ShowComponentConfiguration`, `CompareComponentConfiguration`
  - **ModifyApplicationConfiguration**
    - changes of response param
      - `+ environment_id`
      - `+ application_id`
      - `* configuration: list<object> -> object`
  - **ShowComponentInfo**
    - changes of response param
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
    - changes of request param
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
    - changes of request param
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
    - changes of response param
      - `+ components.platform_type`
  - **ShowComponents**
    - changes of response param
      - `+ components.platform_type`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowAddressGroup**
    - changes of response param
      - `+ address_group.tags`
  - **UpdateAddressGroup**
    - changes of response param
      - `+ address_group.tags`
  - **ListAddressGroup**
    - changes of response param
      - `+ address_groups.tags`
  - **CreateAddressGroup**
    - changes of response param
      - `+ address_group.tags`

### HuaweiCloud SDK VPCEP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **AddOrRemoveServicePermissions**
    - changes of request param
      - `+ permission_type`
    - changes of response param
      - `+ permission_type`
  - **UpdateEndpointService**
    - changes of response param
      - `- cidr_type`
  - **ListServicePermissionsDetails**
    - changes of response param
      - `+ permissions.permission_type`
  - **BatchAddEndpointServicePermissions**
    - changes of request param
      - `+ permission_type`
    - changes of response param
      - `+ permissions.permission_type`
  - **BatchRemoveEndpointServicePermissions**
    - changes of response param
      - `+ permissions.permission_type`
  - **UpdateEndpointServicePermissionDesc**
    - changes of response param
      - `+ permissions.permission_type`
  - **CreateEndpointService**
    - changes of response param
      - `- cidr_type`

### HuaweiCloud SDK VSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CancelTasks**
    - changes of response param
      - `+ task_status: enum value [ready]`
  - **CreateTasks**
    - changes of response param
      - `+ task_status: enum value [ready]`
  - **ShowTasks**
    - changes of response param
      - `+ task_status: enum value [ready]`
  - **ListTaskHistories**
    - changes of response param
      - `+ data.task_status: enum value [ready]`

### HuaweiCloud SDK Workspace

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListDesktops**
    - changes of request param
      - `+ pool_id`
  - **CreateDesktop**
    - changes of request param
      - `+ eip`
      - `+ security_groups.name`
      - `* security_groups: list<SecurityGroupInfo> -> list<SecurityGroup>`
  - **ResizeDesktop**
    - changes of response param
      - `+ job_id`
      - `* jobs: list<ResizeDesktopJobResult> -> list<ResizeDesktopJobResponse>`
  - **CreateAccessPolicy**
    - changes of request param
      - `+ policy_objects_list.object_type: enum value [USERGROUP]`
  - **ListAccessPolicyObjects**
    - changes of response param
      - `+ policy_objects_list.object_type: enum value [USERGROUP]`
      - `* policy_objects_list: list<AccessPolicyObjectInfo> -> list<AccessPolicyObject>`
  - **UpdateAccessPolicyObjects**
    - changes of request param
      - `+ policy_objects_list.object_type: enum value [USERGROUP]`
  - **ListProducts**
    - changes of response param
      - `- products.package_type`
  - **CreateDesktopUser**
    - changes of request param
      - `+ active_type`
      - `+ user_phone`
      - `+ password`
      - `* body: object<CreateUserReq> -> object<CreateUserRequest>`
  - **ListUsers**
    - changes of request param
      - `+ active_type`
    - changes of response param
      - `+ users.user_phone`
      - `+ users.active_type`
      - `+ users.is_pre_user`
  - **UpdateUserInfo**
    - changes of request param
      - `+ user_phone`
      - `+ active_type`
  - **ListUserDetail**
    - changes of response param
      - `+ user_detail.user_phone`
      - `+ user_detail.active_type`
      - `+ user_detail.is_pre_user`
  - **ShowAssistAuthConfig**
    - changes of response param
      - `+ otp_config_info.apply_rule`
  - **UpdateAssistAuthMethodConfig**
    - changes of request param
      - `+ otp_config_info.apply_rule`
  - **ShowDesktopDetail**
    - changes of response param
      - `+ desktop.internet_mode`
      - `+ desktop.is_attaching_eip`
      - `+ desktop.security_groups.name`
      - `* desktop.security_groups: list<SecurityGroupInfo> -> list<SecurityGroup>`
  - **ListDesktopsDetail**
    - changes of request param
      - `+ pool_id`
    - changes of response param
      - `+ desktops.internet_mode`
      - `+ desktops.is_attaching_eip`
      - `+ desktops.security_groups.name`
      - `* desktops.security_groups: list<SecurityGroupInfo> -> list<SecurityGroup>`

# 3.1.45 2023-06-21

### HuaweiCloud SDK DataArtsStudio

- _Features_
  - Support the service `DataArtsStudio`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK KooMessage

- _Features_
  - Support the service `KooMessage`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK APIG

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **DeleteGatewayResponseTypeV2**
    - changes of request param
      - `+ response_type: enum value [THIRD_AUTH_FAILURE,THIRD_AUTH_IDENTITIES_FAILURE,THIRD_AUTH_CONF_FAILURE]`
  - **ShowDetailsOfGatewayResponseTypeV2**
    - changes of request param
      - `+ response_type: enum value [THIRD_AUTH_FAILURE,THIRD_AUTH_IDENTITIES_FAILURE,THIRD_AUTH_CONF_FAILURE]`
  - **UpdateGatewayResponseTypeV2**
    - changes of request param
      - `+ response_type: enum value [THIRD_AUTH_FAILURE,THIRD_AUTH_IDENTITIES_FAILURE,THIRD_AUTH_CONF_FAILURE]`
  - **ShowPlugin**
    - changes of response param
      - `+ plugin_type: enum value [third_auth]`
  - **UpdatePlugin**
    - changes of request param
      - `+ plugin_type: enum value [third_auth]`
    - changes of response param
      - `+ plugin_type: enum value [third_auth]`
  - **CreatePlugin**
    - changes of request param
      - `+ plugin_type: enum value [third_auth]`
    - changes of response param
      - `+ plugin_type: enum value [third_auth]`
  - **ListPlugins**
    - changes of response param
      - `+ plugins.plugin_type: enum value [third_auth]`
  - **AttachApiToPlugin**
    - changes of response param
      - `+ attached_plugins.plugin_type: enum value [third_auth]`
  - **AttachPluginToApi**
    - changes of response param
      - `+ attached_plugins.plugin_type: enum value [third_auth]`
  - **ListApiAttachedPlugins**
    - changes of response param
      - `+ plugins.plugin_type: enum value [third_auth]`
  - **ListApiAttachablePlugins**
    - changes of response param
      - `+ plugins.plugin_type: enum value [third_auth]`
  - **ShowDetailsOfVpcChannelV2**
    - changes of response param
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
  - **UpdateVpcChannelV2**
    - changes of request param
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
    - changes of response param
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
  - **ImportMicroservice**
    - changes of request param
      - `+ cce_service_info`
      - `+ service_type: enum value [CCE_SERVICE]`
      - `+ cce_info.label_key`
      - `+ cce_info.label_value`
  - **CreateVpcChannelV2**
    - changes of request param
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
    - changes of response param
      - `+ microservice_info.cce_service_info`
      - `+ microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ microservice_info.cce_info.label_key`
      - `+ microservice_info.cce_info.label_value`
  - **ListVpcChannelsV2**
    - changes of response param
      - `+ vpc_channels.microservice_info.cce_service_info`
      - `+ vpc_channels.microservice_info.service_type: enum value [CCE_SERVICE]`
      - `+ vpc_channels.microservice_info.cce_info.label_key`
      - `+ vpc_channels.microservice_info.cce_info.label_value`

### HuaweiCloud SDK Classroom

- _Features_
  - Support the following interfaces：
    - `ListPackages`
    - `ShowPackageDetail`
    - `ListExercises`
    - `ShowExerciseDetail`
    - `ExecuteExercise`
    - `ListAllDifficults`
    - `ListMyKnowledgePoints`
- _Bug Fix_
  - None
- _Change_
  - **ApplyJudgement**
    - changes of request param
      - `+ runtime_type: enum value [javaScript]`

### HuaweiCloud SDK CloudRTC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateAutoRecord**
    - changes of response param
      - `- auto_record_mode`
      - `- app_id`
  - **CreateMixJob**
    - changes of response param
      - `+ mix_param.encode_template: enum value [1920*1080_30_4620,1920*1080_30_3150,1920*1080_15_3460,1920*1080_15_2080,1280*720_30_3420,1280*720_30_1710,1280*720_15_2260,1280*720_15_1130,640*480_30_1000,640*480_30_1500,640*480_15_500,480*360_30_490,480*360_15_320]`
      - `- mix_param.encode_template: enum value [1920x1080_30_4620,1920x1080_15_3460,1280x720_30_3420,1280x720_15_2260]`
  - **ShowMixJob**
    - changes of response param
      - `+ mix_param.encode_template: enum value [1920*1080_30_4620,1920*1080_30_3150,1920*1080_15_3460,1920*1080_15_2080,1280*720_30_3420,1280*720_30_1710,1280*720_15_2260,1280*720_15_1130,640*480_30_1000,640*480_30_1500,640*480_15_500,480*360_30_490,480*360_15_320]`
      - `- mix_param.encode_template: enum value [1920x1080_30_4620,1920x1080_15_3460,1280x720_30_3420,1280x720_15_2260]`
  - **UpdateMixJob**
    - changes of response param
      - `+ mix_param.encode_template: enum value [1920*1080_30_4620,1920*1080_30_3150,1920*1080_15_3460,1920*1080_15_2080,1280*720_30_3420,1280*720_30_1710,1280*720_15_2260,1280*720_15_1130,640*480_30_1000,640*480_30_1500,640*480_15_500,480*360_30_490,480*360_15_320]`
      - `- mix_param.encode_template: enum value [1920x1080_30_4620,1920x1080_15_3460,1280x720_30_3420,1280x720_15_2260]`

### HuaweiCloud SDK CloudTable

- _Features_
  - Support the following interfaces：
    - `EnableComponent`
    - `ExpandClusterComponent`
    - `RebootCloudTableCluster`
    - `ShowClusterSetting`
    - `UpdateClusterSetting`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DNS

- _Features_
  - Support the interface `ShowDomainQuota`
- _Bug Fix_
  - None
- _Change_
  - **ShowRecordSetWithLine**
    - changes of response param
      - `+ bundle`
  - **SetRecordSetsStatus**
    - changes of response param
      - `+ bundle`
  - **BatchUpdateRecordSetWithLine**
    - changes of response param
      - `+ bundle`
      - `+ recordsets.bundle`
  - **BatchDeleteRecordSetWithLine**
    - changes of response param
      - `+ bundle`
      - `+ recordsets.bundle`
  - **CreateRecordSetWithBatchLines**
    - changes of response param
      - `+ bundle`
      - `+ recordsets.bundle`

### HuaweiCloud SDK DWS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListAvailableDisasterClusters**
    - changes of request param
      - `* primary_cluster_id: optional -> required`
      - `* standby_az_code: optional -> required`

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the following interfaces：
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
  - **CreateDbInstance**
    - changes of response param
      - `+ instance.ha.consistency_protocol`

### HuaweiCloud SDK IoTEdge

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateEdgeNode**
    - changes of request param
      - `+ npu_library_path`
      - `+ device_data_format`
      - `+ automatic_upgrade`
      - `+ device_data_record`
      - `+ metric_report`
      - `+ base_path.offline_cache_configs`
    - changes of response param
      - `+ device_data_record`
      - `+ device_data_format`
      - `+ metric_report`
      - `+ automatic_upgrade`
      - `+ base_path.offline_cache_configs`
  - **ShowEdgeNode**
    - changes of response param
      - `+ device_data_record`
      - `+ device_data_format`
      - `+ metric_report`
      - `+ npu_library_path`
      - `+ automatic_upgrade`
      - `+ base_path.offline_cache_configs`
  - **CreateEdgeApplicationVersion**
    - changes of request param
      - `+ container_settings.npu_type`
      - `+ container_settings.vnpu_template`
    - changes of response param
      - `+ container_settings.npu_type`
      - `+ container_settings.vnpu_template`
  - **ShowEdgeApplicationVersion**
    - changes of response param
      - `+ container_settings.npu_type`
      - `+ container_settings.vnpu_template`
  - **UpdateEdgeApplicationVersion**
    - changes of request param
      - `+ container_settings.npu_type`
      - `+ container_settings.vnpu_template`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListPredefinedTag`, `ListSimplifiedInstances`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.44 2023-06-15

### HuaweiCloud SDK CloudDeploy

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - `CloudDeploy` is renamed to `CodeArtsDeploy`

### HuaweiCloud SDK CCM

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - Support the following interfaces：
    - `ShowDatabaseAuthority`
    - `UpdateDatabaseAuthority`
    - `SyncIamUsers`
    - `ListDatabaseUsers`
    - `ShowDatabaseUser`
    - `UpdateDatabaseUserInfo`
    - `ShowDisasterProgress`
- _Bug Fix_
  - None
- _Change_
  - **UpdateAlarmSub**
    - changes of request param
      - `* enable: string -> int32`
    - changes of response param
      - `* enable: string -> int32`
  - **DeleteAlarmSub**
    - changes of response param
      - `* enable: string -> int32`
  - **ShowDisasterDetail**
    - changes of response param
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
    - changes of request param
      - `* enable: string -> int32`
    - changes of response param
      - `* enable: string -> int32`
  - **ListAlarmSubs**
    - changes of response param
      - `* alarm_subscriptions.enable: string -> int32`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ListGaussMySqlErrorLog`, `ListGaussMySqlSlowLog`

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateBatchTask**
    - changes of response param
      - `- task_progress.device_in_progress`
      - `- task_progress.rejected`
  - **ListBatchTasks**
    - changes of response param
      - `- batchtasks.task_progress.device_in_progress`
      - `- batchtasks.task_progress.rejected`
  - **ShowBatchTask**
    - changes of response param
      - `- batchtask.task_progress.device_in_progress`
      - `- batchtask.task_progress.rejected`

### HuaweiCloud SDK MRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListClusters**
    - changes of response param
      - `+ clusters.eipId`
      - `+ clusters.eipAddress`
      - `+ clusters.eipv6Address`
  - **ShowClusterDetails**
    - changes of response param
      - `+ cluster.eipId`
      - `+ cluster.eipAddress`
      - `+ cluster.eipv6Address`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RecognizeGeneralText**
    - changes of request param
      - `+ single_orientation_mode`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `ModifyCollation`
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
  - **SendDlqMessage**
    - changes of request param
      - `+ engine: enum value [reliability]`
  - **CreateRocketMqMigrationTask**
    - changes of request param
      - `+ type: enum value [kafka]`

### HuaweiCloud SDK SIS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowVocabularies**
    - changes of request param
      - `+ offset`
      - `+ limit`

# 3.1.43 2023-06-08

### HuaweiCloud SDK iDME

- _Features_
  - Support the service `Industrial Digital Model Engine`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BCS

- _Features_
  - Support the interfaces `ListBcsEvents`, `ListBcsEventsStatistic`
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
  - **UpdateIndirectPartnerAccount**
    - changes of request param
      - `* amount: double -> bigdecimal`
  - **ListCustomerBillsMonthlyBreakDown**
    - changes of response param
      - `* details.past_months_amortized_amount: double -> bigdecimal`
      - `* details.amortized_cash_amount: double -> bigdecimal`
  - **ListIssuedCouponQuotas**
    - changes of response param
      - `* quotas.balance: double -> bigdecimal`

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowNode**
    - changes of response param
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
  - **UpdateNode**
    - changes of response param
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
  - **DeleteNode**
    - changes of response param
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
  - **CreateNode**
    - changes of request param
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
    - changes of response param
      - `+ spec.extendParam.kube-reserved-mem`
      - `+ spec.extendParam.system-reserved-mem`
  - **ListNodes**
    - changes of response param
      - `+ items.spec.extendParam.kube-reserved-mem`
      - `+ items.spec.extendParam.system-reserved-mem`
  - **ShowNodePool**
    - changes of response param
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
  - **UpdateNodePool**
    - changes of response param
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
  - **DeleteNodePool**
    - changes of response param
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
  - **CreateNodePool**
    - changes of request param
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
    - changes of response param
      - `+ spec.type: enum value [pm]`
      - `+ spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ spec.nodeTemplate.extendParam.system-reserved-mem`
  - **ListNodePools**
    - changes of response param
      - `+ items.spec.type: enum value [pm]`
      - `+ items.spec.nodeTemplate.extendParam.kube-reserved-mem`
      - `+ items.spec.nodeTemplate.extendParam.system-reserved-mem`

### HuaweiCloud SDK CloudDeploy

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateDeploymentGroup**
    - changes of request param
      - `+ is_proxy_mode`

### HuaweiCloud SDK DNS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListRecordSetsByZone**
    - changes of request param
      - `+ search_mode`
  - **CreateRecordSet**
    - changes of request param
      - `* body: object<CreateRecordSetReq> -> object<CreateRecordSetRequestBody>`
  - **CreateRecordSetWithLine**
    - changes of request param
      - `* body: object<CreateRecordSetWithLineReq> -> object<CreateRecordSetWithLineRequestBody>`
  - **ListPublicZones**
    - changes of request param
      - `+ search_mode`
  - **ListPrivateZones**
    - changes of request param
      - `+ search_mode`
  - **ListRecordSets**
    - changes of request param
      - `+ search_mode`

### HuaweiCloud SDK ECS

- _Features_
  - Support the interface `ChangeServerChargeMode`
- _Bug Fix_
  - None
- _Change_
  - **CreateServers**
    - changes of request param
      - `+ server.nics.allowed_address_pairs`
  - **CreatePostPaidServers**
    - changes of request param
      - `+ server.nics.allowed_address_pairs`

### HuaweiCloud SDK ELB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListListeners**
    - changes of response param
      - `+ listeners.port_ranges`
  - **CreateListener**
    - changes of request param
      - `+ listener.port_ranges`
    - changes of response param
      - `+ listener.port_ranges`
  - **ShowListener**
    - changes of response param
      - `+ listener.port_ranges`
  - **UpdateListener**
    - changes of response param
      - `+ listener.port_ranges`
  - **ListPools**
    - changes of response param
      - `+ pools.any_port_enable`
  - **CreatePool**
    - changes of request param
      - `+ pool.any_port_enable`
    - changes of response param
      - `+ pool.any_port_enable`
  - **ShowPool**
    - changes of response param
      - `+ pool.any_port_enable`
  - **UpdatePool**
    - changes of response param
      - `+ pool.any_port_enable`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - Support the following interfaces：
    - `UpdateFuncSnapshot`
    - `ShowFuncSnapshotState`
    - `ShowResInstanceInfo`
    - `ShowProjectTagsList`
    - `CreateTags`
    - `DeleteTags`
    - `CreateVpcEndpoint`
    - `DeleteVpcEndpoint`
- _Bug Fix_
  - None
- _Change_
  - **ListStatistics**
    - changes of response param
      - `* count.value: int32 -> number`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - Support the following interfaces：
    - `ListInstancesDetails`
    - `CreateDbInstance`
    - `ListParamGroupTemplates`
    - `ShowInstanceParamGroup`
    - `ListDbFlavors`
    - `ListDbBackups`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTDA

- _Features_
  - Support the interfaces `RetryBatchTask`, `StopBatchTask`
- _Bug Fix_
  - None
- _Change_
  - **CreateBatchTask**
    - changes of response param
      - `+ task_progress.removed`
      - `+ task_progress.device_in_progress`
      - `+ task_progress.rejected`
  - **ListBatchTasks**
    - changes of response param
      - `+ batchtasks.task_progress.removed`
      - `+ batchtasks.task_progress.device_in_progress`
      - `+ batchtasks.task_progress.rejected`
  - **ShowBatchTask**
    - changes of request param
      - `+ task_detail_status`
      - `+ target`
    - changes of response param
      - `+ batchtask.task_progress.removed`
      - `+ batchtask.task_progress.device_in_progress`
      - `+ batchtask.task_progress.rejected`

### HuaweiCloud SDK MRS

- _Features_
  - Support the interface `ListAvailableZones`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interfaces `AddIssueWorkHours`, `ListProjectWorkHoursType`
- _Bug Fix_
  - None
- _Change_
  - **ShowProjectWorkHours**
    - changes of response param
      - `+ work_hours.work_hours_created_time`
      - `+ work_hours.work_hours_updated_time`
  - **ListProjectWorkHours**
    - changes of response param
      - `+ work_hours.work_hours_created_time`
      - `+ work_hours.work_hours_updated_time`
  - **ListIssueCustomFields**
    - changes of request param
      - `+ included_not_in_use`
    - changes of response param
      - `+ datas.create_time`
  - **ListIssuesV4**
    - changes of request param
      - `+ created_time_interval`
      - `+ closed_time_interval`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interface `ListInstanceTags`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RocketMQ

- _Features_
  - Support the interfaces `SendDlqMessage`, `ValidateConsumedMessage`
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `SendRocketMqDlqMessage`, `ValidateRocketMqConsumedMessage`
  - **CreateInstanceByEngine**
    - changes of request param
      - `+ product_id: enum value [c6.4u8g.cluster.small]`

### HuaweiCloud SDK TMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListResource**
    - changes of response param
      - `+ resources.tags`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowAddressGroup**
    - changes of response param
      - `+ address_group.enterprise_project_id`
  - **UpdateAddressGroup**
    - changes of response param
      - `+ address_group.enterprise_project_id`
  - **ListAddressGroup**
    - changes of request param
      - `+ enterprise_project_id`
    - changes of response param
      - `+ address_groups.enterprise_project_id`
  - **CreateAddressGroup**
    - changes of request param
      - `+ address_group.enterprise_project_id`
    - changes of response param
      - `+ address_group.enterprise_project_id`

# 3.1.42 2023-06-01

### HuaweiCloud SDK BSS

- _Features_
  - Support the interfaces `ListMultiAccountTransferCoupons`, `ListMultiAccountRetrieveCoupons`, `ClaimEnterpriseMultiAccountCoupon`, `ReclaimEnterpriseMultiAccountCoupon`
- _Bug Fix_
  - None
- _Change_
  - **UpdateCustomerAccountAmount**
    - changes of request param
      - `* amount: double -> bigdecimal`
  - **ReclaimIndirectPartnerAccount**
    - changes of request param
      - `* amount: double -> bigdecimal`
  - **ReclaimToPartnerAccount**
    - changes of request param
      - `* amount: double -> bigdecimal`
  - **ListPartnerCouponsRecord**
    - changes of response param
      - `* records.operation_amount: double -> bigdecimal`
  - **ListCustomersBalancesDetail**
    - changes of response param
      - `* customer_balances.debt_amount: double -> bigdecimal`
      - `* customer_balances.amount: double -> bigdecimal`
  - **ShowCustomerMonthlySum**
    - changes of response param
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
    - changes of request param
      - `* quota_amount: double -> bigdecimal`
  - **ListCouponQuotasRecords**
    - changes of response param
      - `* records.amount: double -> bigdecimal`
  - **ReclaimCouponQuotas**
    - changes of response param
      - `* simple_quota_infos.quota_balance: double -> bigdecimal`
  - **ShowCustomerAccountBalances**
    - changes of response param
      - `* debt_amount: double -> bigdecimal`
      - `* account_balances.amount: double -> bigdecimal`
      - `* account_balances.designated_amount: double -> bigdecimal`
      - `* account_balances.credit_amount: double -> bigdecimal`
  - **ListFreeResourceUsages**
    - changes of response param
      - `* free_resources.amount: double -> bigdecimal`
      - `* free_resources.original_amount: double -> bigdecimal`
  - **ListIssuedPartnerCoupons**
    - changes of response param
      - `* user_coupons.face_value: double -> bigdecimal`
      - `* user_coupons.balance: double -> bigdecimal`
  - **ListOnDemandResourceRatings**
    - changes of response param
      - `* amount: double -> bigdecimal`
      - `* discount_amount: double -> bigdecimal`
      - `* official_website_amount: double -> bigdecimal`
      - `* product_rating_results.amount: double -> bigdecimal`
      - `* product_rating_results.discount_amount: double -> bigdecimal`
      - `* product_rating_results.official_website_amount: double -> bigdecimal`
  - **ListSubcustomerMonthlyBills**
    - changes of response param
      - `* bill_sums.amount: double -> bigdecimal`
      - `* bill_sums.debt_amount: double -> bigdecimal`
      - `* bill_sums.adjustment_amount: double -> bigdecimal`
      - `* bill_sums.discount_amount: double -> bigdecimal`
      - `* bill_sums.account_details.amount: double -> bigdecimal`
  - **ListCustomerBillsMonthlyBreakDown**
    - changes of response param
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
    - changes of response param
      - `* quotas.quota_value: double -> bigdecimal`
      - `* quotas.balance: double -> bigdecimal`
  - **ListIssuedCouponQuotas**
    - changes of response param
      - `* quotas.quota_value: double -> bigdecimal`

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListFreeResourceUsages**
    - changes of response param
      - `* free_resources.amount: double -> bigdecimal`
      - `* free_resources.original_amount: double -> bigdecimal`
  - **ListOnDemandResourceRatings**
    - changes of response param
      - `* amount: double -> bigdecimal`
      - `* discount_amount: double -> bigdecimal`
      - `* official_website_amount: double -> bigdecimal`
      - `* product_rating_results.amount: double -> bigdecimal`
      - `* product_rating_results.discount_amount: double -> bigdecimal`
      - `* product_rating_results.official_website_amount: double -> bigdecimal`

### HuaweiCloud SDK CBH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowNetworkConfiguration**
    - changes of request param
      - `+ nics.ip_address`
  - **ChangeInstanceNetwork**
    - changes of request param
      - `+ nics.ip_address`
  - **CreateInstance**
    - changes of request param
      - `+ server.nics.ip_address`

### HuaweiCloud SDK CBR

- _Features_
  - Support the interface `ShowSummary`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CBS

- _Features_
  - Support the interface `PostRequests`
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
  - **ShowAddonInstance**
    - changes of response param
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
  - **UpdateAddonInstance**
    - changes of request param
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
    - changes of response param
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
  - **CreateAddonInstance**
    - changes of request param
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
    - changes of response param
      - `+ metadata.alias`
      - `* metadata: object<Metadata> -> object<AddonMetadata>`
  - **ListAddonInstances**
    - changes of response param
      - `+ items.metadata.alias`
      - `* items.metadata: object<Metadata> -> object<AddonMetadata>`
  - **ListAddonTemplates**
    - changes of response param
      - `+ items.metadata.alias`
      - `* items.metadata: object<Metadata> -> object<AddonMetadata>`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowLogs**
    - changes of request param
      - `+ start_time`
      - `+ end_time`
      - `- query_date`
  - **ShowDomainFullConfig**
    - changes of request param
      - `+ show_special_configs`
    - changes of response param
      - `- configs.error_code_cache.code: enum value [400,403,404,405,414,500,501,502,503,504]`
      - `+ configs.flexible_origin.back_sources.http_port`
      - `+ configs.flexible_origin.back_sources.https_port`
  - **UpdateDomainFullConfig**
    - changes of request param
      - `- configs.error_code_cache.code: enum value [400,403,404,405,414,500,501,502,503,504]`
      - `+ configs.flexible_origin.back_sources.http_port`
      - `+ configs.flexible_origin.back_sources.https_port`

### HuaweiCloud SDK CPTS

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **UpdateCase**
    - changes of request param
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
    - changes of request param
      - `+ contents.content.content.rtmp_url`
      - `+ contents.content.content.flv_url`
      - `+ contents.content.content.bitrate_type`
      - `+ contents.content.content.duration`
      - `+ contents.content.content.retry_delay`
      - `+ contents.content.content.retry_time`
  - **ShowTask**
    - changes of response param
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
    - changes of request param
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
    - changes of response param
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
    - changes of response param
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

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RestorePtrRecord**
    - changes of request param
      - `* ptrdname: string -> object`
  - **ShowRecordSet**
    - changes of response param
      - `+ bundle`
  - **CreateEipRecordSet**
    - changes of response param
      - `+ enterprise_project_id`
  - **ShowPtrRecordSet**
    - changes of response param
      - `+ enterprise_project_id`
  - **ShowResourceTag**
    - changes of response param
      - `+ enterpriseProjectOrDefault`
  - **ListPrivateZones**
    - changes of request param
      - `* type: required -> optional`

### HuaweiCloud SDK EG

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
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
    - changes of response param
      - `+ provider_type: enum value [PARTNER]`
  - **UpdateEventSource**
    - changes of response param
      - `+ provider_type: enum value [PARTNER]`
  - **ShowDetailOfChannel**
    - changes of response param
      - `+ provider_type: enum value [PARTNER]`
  - **UpdateChannel**
    - changes of response param
      - `+ provider_type: enum value [PARTNER]`
  - **UpdateSubscriptionSource**
    - changes of request param
      - `+ provider_type: enum value [PARTNER]`
  - **ShowDetailOfConnection**
    - changes of response param
      - `+ type`
      - `+ kafka_detail`
  - **UpdateConnection**
    - changes of response param
      - `+ type`
      - `+ kafka_detail`
  - **CreateEventSource**
    - changes of response param
      - `+ provider_type: enum value [PARTNER]`
  - **ListEventSources**
    - changes of request param
      - `+ provider_type: enum value [PARTNER]`
    - changes of response param
      - `+ items.provider_type: enum value [PARTNER]`
  - **CreateChannel**
    - changes of response param
      - `+ provider_type: enum value [PARTNER]`
  - **ListChannels**
    - changes of request param
      - `+ provider_type: enum value [PARTNER]`
    - changes of response param
      - `+ items.provider_type: enum value [PARTNER]`
  - **CreateSubscriptionTarget**
    - changes of request param
      - `+ kafka_detail`
  - **UpdateSubscriptionTarget**
    - changes of request param
      - `+ kafka_detail`
  - **CreateConnection**
    - changes of request param
      - `+ type`
      - `+ kafka_detail`
    - changes of response param
      - `+ type`
      - `+ kafka_detail`
  - **ListConnections**
    - changes of response param
      - `+ type`
      - `+ kafka_detail`
      - `+ items.type`
      - `+ items.kafka_detail`
  - **ListEventTarget**
    - changes of request param
      - `+ support_types`
  - **UpdateSubscription**
    - changes of request param
      - `+ sources.provider_type: enum value [PARTNER]`
      - `+ targets.kafka_detail`
  - **CreateSubscription**
    - changes of request param
      - `+ sources.provider_type: enum value [PARTNER]`
      - `+ targets.kafka_detail`
  - **ListSubscriptions**
    - changes of request param
      - `+ connection_id`

### HuaweiCloud SDK ELB

- _Features_
  - Support the interfaces `DeleteLoadBalancerForce`, `DeleteListenerForce`, `BatchUpdateMembers`
- _Bug Fix_
  - None
- _Change_
  - **ShowQuota**
    - changes of response param
      - `+ quota.condition_per_policy`
      - `+ quota.listeners_per_pool`
      - `+ quota.listeners_per_loadbalancer`
      - `* quota.ipgroup_bindings: string -> int32`
      - `* quota.ipgroup_max_length: string -> int32`
  - **ShowLoadBalancer**
    - changes of response param
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
  - **UpdateLoadBalancer**
    - changes of request param
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
    - changes of response param
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
  - **ListListeners**
    - changes of request param
      - `+ protection_status`
    - changes of response param
      - `+ listeners.protection_status`
      - `+ listeners.protection_reason`
      - `+ listeners.gzip_enable`
  - **CreateListener**
    - changes of request param
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
    - changes of response param
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
  - **ShowListener**
    - changes of response param
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
  - **UpdateListener**
    - changes of request param
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
    - changes of response param
      - `+ listener.protection_status`
      - `+ listener.protection_reason`
      - `+ listener.gzip_enable`
  - **ListPools**
    - changes of request param
      - `+ protection_status`
    - changes of response param
      - `+ pools.protection_status`
      - `+ pools.protection_reason`
  - **CreatePool**
    - changes of request param
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
    - changes of response param
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
  - **ShowPool**
    - changes of response param
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
  - **UpdatePool**
    - changes of request param
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
    - changes of response param
      - `+ pool.protection_status`
      - `+ pool.protection_reason`
  - **UpdateMember**
    - changes of request param
      - `+ member.protocol_port`
  - **ListLoadBalancers**
    - changes of request param
      - `+ protection_status`
      - `+ global_eips`
    - changes of response param
      - `+ loadbalancers.protection_status`
      - `+ loadbalancers.protection_reason`
  - **CreateLoadBalancer**
    - changes of request param
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
    - changes of response param
      - `+ loadbalancer.protection_status`
      - `+ loadbalancer.protection_reason`
  - **ListL7Policies**
    - changes of response param
      - `+ l7policies.redirect_pools_extend_config`
      - `- l7policies.redirect_pools_config`
  - **CreateL7Policy**
    - changes of request param
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`
    - changes of response param
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`
  - **ShowL7Policy**
    - changes of response param
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`
  - **UpdateL7Policy**
    - changes of request param
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`
    - changes of response param
      - `+ l7policy.redirect_pools_extend_config`
      - `- l7policy.redirect_pools_config`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateGaussMySqlInstance**
    - changes of request param
      - `+ restore_point`

### HuaweiCloud SDK IEC

- _Features_
  - Support the following interfaces：
    - `ListCloudImages`
    - `RegisterImage`
    - `CreateImage`
    - `ShowVolumeTypes`
    - `RebuildImage`
    - `DeleteImage`
    - `UpdateBandwidth`
    - `DeleteBandwidth`
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
  - **ListInstanceTopics**
    - changes of request param
      - `+ offset`
      - `+ limit`
  - **ListInstances**
    - changes of request param
      - `+ offset`
      - `+ limit`

### HuaweiCloud SDK MPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `ListEditingJobs`, `CreateEditingJobs`, `DeleteEditingJobs`

### HuaweiCloud SDK Organizations

- _Features_
  - Support the interface `ListQuotas`
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
  - **ShowIssueV4**
    - changes of response param
      - `+ story_point`
  - **SearchIssues**
    - changes of response param
      - `+ issue_list.due_date`
  - **ListIssueCommentsV4**
    - changes of response param
      - `+ comments.timestamp`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreatePostPaidInstanceByEngine**
    - changes of request param
      - `+ bss_param`
  - **CreatePostPaidInstance**
    - changes of request param
      - `+ bss_param`
  - **ListInstancesDetails**
    - changes of request param
      - `+ offset`
      - `+ limit`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `ListEngineFlavors`, `BatchDeleteManualBackup`, `DeleteJob`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RocketMQ

- _Features_
  - Support the following interfaces：
    - `SendRocketMqDlqMessage`
    - `ValidateRocketMqConsumedMessage`
    - `ListRocketMqMigrationTask`
    - `CreateRocketMqMigrationTask`
    - `DeleteRocketMqMigrationTask`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SMN

- _Features_
  - Support the following interfaces：
    - `UpdateSubscription`
    - `ListLogtank`
    - `CreateLogtank`
    - `UpdateLogtank`
    - `DeleteLogtank`
- _Bug Fix_
  - None
- _Change_
  - **ListTopicDetails**
    - changes of response param
      - `+ topic_id`
  - **ListTopics**
    - changes of request param
      - `+ topic_id`
    - changes of response param
      - `+ topics.topic_id`
  - **ListTopicAttributes**
    - changes of response param
      - `+ attributes.access_policy`
      - `+ attributes.introduction`
      - `- attributes.Version`
      - `- attributes.Id`
      - `- attributes.Statement`
  - **AddSubscription**
    - changes of request param
      - `+ extension`

### HuaweiCloud SDK VOD

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateAssetByFileUpload**
    - changes of request param
      - `+ review.interval`
      - `+ review.politics`
      - `+ review.terrorism`
      - `+ review.porn`
  - **PublishAssetFromObs**
    - changes of request param
      - `+ review.interval`
      - `+ review.politics`
      - `+ review.terrorism`
      - `+ review.porn`
  - **CreateAssetReviewTask**
    - changes of request param
      - `+ review.interval`
      - `+ review.politics`
      - `+ review.terrorism`
      - `+ review.porn`
    - changes of response param
      - `+ review.interval`
      - `+ review.politics`
      - `+ review.terrorism`
      - `+ review.porn`
  - **UploadMetaDataByUrl**
    - changes of request param
      - `+ upload_metadatas.review.interval`
      - `+ upload_metadatas.review.politics`
      - `+ upload_metadatas.review.terrorism`
      - `+ upload_metadatas.review.porn`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateVpcPeering**
    - changes of request param
      - `+ peering.description`

# 3.1.41 2023-05-25

### HuaweiCloud SDK CBH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowNetworkConfiguration**
    - changes of request param
      - `- nics.ip_address`
  - **CreateInstanceOrder**
    - changes of request param
      - `- product_infos.resource_size_measure_id`
      - `- product_infos.resource_size`
  - **ChangeInstanceNetwork**
    - changes of request param
      - `- nics.ip_address`
  - **CreateInstance**
    - changes of request param
      - `+ server.enterprise_project_id`
      - `- server.nics.ip_address`
      - `- server.public_ip.eip`

### HuaweiCloud SDK CBR

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **CreateVault**
    - changes of request param
      - `+ vault.threshold`
      - `+ vault.smn_notify`
      - `+ vault.backup_name_prefix`
      - `+ vault.demand_billing`
    - changes of response param
      - `+ vault.backup_name_prefix`
      - `+ vault.demand_billing`
      - `+ vault.cbc_delete_count`
      - `+ vault.frozen`

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowCluster**
    - changes of response param
      - `+ metadata.alias`
  - **UpdateCluster**
    - changes of request param
      - `+ metadata`
    - changes of response param
      - `+ metadata.alias`
  - **DeleteCluster**
    - changes of response param
      - `+ metadata.alias`
  - **MigrateNode**
    - changes of request param
      - `+ spec.runtime`
    - changes of response param
      - `+ spec.runtime`
  - **CreateCluster**
    - changes of request param
      - `+ metadata.alias`
    - changes of response param
      - `+ metadata.alias`
  - **ListClusters**
    - changes of response param
      - `+ items.metadata.alias`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDomainDetailByName**
    - changes of response param
      - `+ domain.domain_name`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListMigrationTask**
    - changes of response param
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
    - changes of response param
      - `* template_num: number -> integer`
  - **ListInstances**
    - changes of response param
      - `+ instances.updated_at`
  - **ListBackgroundTask**
    - changes of response param
      - `- updated_at`
      - `- created_at`
      - `- status`
  - **ListFlavors**
    - changes of response param
      - `+ flavors.flavors_available_zones.unit`
      - `+ flavors.flavors_available_zones.available_zones`

### HuaweiCloud SDK ECS

- _Features_
  - Support the interface `ListFlavorSellPolicies`
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
  - **ListPublicipsByTags**
    - changes of response param
      - `+ resources.resource_detail`
      - `- resources.resouce_detail`
  - **AddPublicipsIntoSharedBandwidth**
    - changes of response param
      - `+ bandwidth.enable_bandwidth_rules`
      - `+ bandwidth.rule_quota`
      - `+ bandwidth.bandwidth_rules`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interfaces `UpdateProxyConnectionPoolType`, `RestoreOldInstance`, `ShowBackupRestoreTime`
- _Bug Fix_
  - None
- _Change_
  - **ShowGaussMySqlProxyList**
    - changes of response param
      - `+ proxy_list.proxy.connection_pool_type`
      - `+ proxy_list.proxy.switch_connection_pool_type_enabled`

### HuaweiCloud SDK IAM

- _Features_
  - Support the interfaces `AssociateRoleToAgencyOnEnterpriseProject`, `RevokeRoleFromAgencyOnEnterpriseProject`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Image

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `CreateVideoObjectMaskingTask`, `ShowVideoObjectMaskingTask`

### HuaweiCloud SDK Kafka

- _Features_
  - Support the interfaces `DeleteConnector`, `CreateDeleteConnectorOrder`, `CreateKafkaConsumerGroup`, `CloseKafkaManager`
- _Bug Fix_
  - None
- _Change_
  - **ShowInstance**
    - changes of response param
      - `+ kafka_manager_enable`
  - **ListInstances**
    - changes of response param
      - `+ kafka_manager_enable`
      - `+ instances.kafka_manager_enable`

### HuaweiCloud SDK Live

- _Features_
  - Support the interface `BatchShowIpBelongs`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK MSGSMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowSignatureFile**
    - changes of response param
      - `+ file_desc`
  - **UpdateApp**
    - changes of response param
      - `- app_secret`

### HuaweiCloud SDK RabbitMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreatePostPaidInstanceByEngine**
    - changes of request param
      - `+ engine_version: enum value [3.8.35]`
  - **CreatePostPaidInstance**
    - changes of request param
      - `+ engine_version: enum value [3.8.35]`

### HuaweiCloud SDK RAM

- _Features_
  - Support the interface `ListQuota`
- _Bug Fix_
  - None
- _Change_
  - **AssociateResourceShare**
    - changes of response param
      - `+ resource_share_associations.external`
  - **DisassociateResourceShare**
    - changes of response param
      - `+ resource_share_associations.external`
  - **SearchResourceShareAssociations**
    - changes of response param
      - `+ resource_share_associations.external`
  - **CreateResourceShare**
    - changes of request param
      - `+ allow_external_principals`
    - changes of response param
      - `+ resource_share.allow_external_principals`
  - **SearchResourceShares**
    - changes of response param
      - `+ resource_shares.allow_external_principals`
  - **UpdateResourceShare**
    - changes of request param
      - `+ allow_external_principals`
    - changes of response param
      - `+ resource_share.allow_external_principals`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSqlserverDatabases**
    - changes of request param
      - `+ recover_model`

### HuaweiCloud SDK RMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowPolicyAssignment**
    - changes of response param
      - `+ created_by`
  - **UpdatePolicyAssignment**
    - changes of response param
      - `+ created_by`
  - **ShowAggregatePolicyAssignmentDetail**
    - changes of response param
      - `+ created_by`
  - **CreatePolicyAssignments**
    - changes of response param
      - `+ created_by`
  - **ListPolicyAssignments**
    - changes of response param
      - `+ created_by`
      - `+ value.created_by`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateVpc**
    - changes of request param
      - `+ vpc.tags`
  - **CreateSubnet**
    - changes of request param
      - `+ subnet.tags`
    - **ShowAddressGroup**
    - changes of response param
      - `+ address_group.max_capacity`
      - `+ address_group.status`
      - `+ address_group.status_message`
  - **UpdateAddressGroup**
    - changes of request param
      - `+ address_group.max_capacity`
    - changes of response param
      - `+ address_group.max_capacity`
      - `+ address_group.status`
      - `+ address_group.status_message`
  - **ListAddressGroup**
    - changes of response param
      - `+ address_groups.max_capacity`
      - `+ address_groups.status`
      - `+ address_groups.status_message`
  - **CreateAddressGroup**
    - changes of request param
      - `+ address_group.max_capacity`
    - changes of response param
      - `+ address_group.max_capacity`
      - `+ address_group.status`
      - `+ address_group.status_message`

### HuaweiCloud SDK VPCEP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListServiceDescribeDetails**
    - changes of response param
      - `+ enable_policy`
  - **ListServiceDetails**
    - changes of response param
      - `- vip_port_id`
  - **UpdateEndpointService**
    - changes of request param
      - `- vip_port_id`
    - changes of response param
      - `- vip_port_id`
  - **ListServicePublicDetails**
    - changes of response param
      - `+ endpoint_services.enable_policy`
  - **CreateEndpointService**
    - changes of request param
      - `- vip_port_id`
    - changes of response param
      - `- vip_port_id`
  - **ListEndpointService**
    - changes of response param
      - `- endpoint_services.vip_port_id`

# 3.1.40 2023-05-18

### HuaweiCloud SDK CBR

- _Features_
  - Support the following interfaces：
    - `AddAgentPath`
    - `ShowAgent`
    - `UpdateAgent`
    - `UnregisterAgent`
    - `ListAgent`
    - `RegisterAgent`
    - `RemoveAgentPath`
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
  - **ShowNode**
    - changes of response param
      - `+ status.lastProbeTime`
  - **UpdateNode**
    - changes of response param
      - `+ status.lastProbeTime`
  - **DeleteNode**
    - changes of response param
      - `+ status.lastProbeTime`
  - **CreateNode**
    - changes of response param
      - `+ status.lastProbeTime`
  - **ListNodes**
    - changes of response param
      - `+ items.status.lastProbeTime`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateRefreshTasks**
    - changes of request param
      - `* refresh_task.mode: boolean -> string`
  - **ShowDomainFullConfig**
    - changes of response param
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
    - changes of request param
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
    - changes of response param
      - `+ domain.sources.obs_bucket_type`

### HuaweiCloud SDK CloudPipeline

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowInstanceStatus**
    - changes of request param
      - `- X-Language`
  - **StopPipelineNew**
    - changes of request param
      - `- X-Language`
  - **RemovePipeline**
    - changes of request param
      - `- X-Language`
  - **RunPipeline**
    - changes of request param
      - `- X-Language`
  - **BatchShowPipelinesLatestStatus**
    - changes of request param
      - `- X-Language`
  - **ListPipelines**
    - changes of request param
      - `- X-Language`
  - **DeletePipeline**
    - changes of request param
      - `- X-Language`
  - **StopPipelineRun**
    - changes of request param
      - `- X-Language`
  - **ListPipelineRuns**
    - changes of request param
      - `- X-Language`
  - **StartNewPipeline**
    - changes of request param
      - `- X-Language`
  - **BatchShowPipelinesStatus**
    - changes of request param
      - `- X-Language`
  - **ListPipelineSimpleInfo**
    - changes of request param
      - `- X-Language`
  - **ShowPipleineStatus**
    - changes of request param
      - `- X-Language`
  - **ListPipleineBuildResult**
    - changes of request param
      - `- X-Language`
  - **ListPipelineTemplates**
    - changes of request param
      - `- X-Language`
  - **CreatePipelineByTemplateId**
    - changes of request param
      - `- X-Language`
  - **ShowTemplateDetail**
    - changes of request param
      - `- X-Language`
  - **CreatePipelineByTemplate**
    - changes of request param
      - `- X-Language`
  - **ShowPipelineRunDetail**
    - changes of request param
      - `- X-Language`
  - **ListTemplates**
    - changes of request param
      - `- X-Language`

### HuaweiCloud SDK CPTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateTaskStatus**
    - changes of request param
      - `+ enterprise_project_id`
  - **UpdateAgentHealthStatus**
    - changes of response param
      - `+ result.result.kafka_enable`
      - `+ result.result.kafka_shadow_topic_prefix`
      - `+ result.result.app_log_level`
      - `+ result.result.app_log_path`
      - `+ result.result.mock_rule_list`

### HuaweiCloud SDK CSE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpgradeEngine**
    - changes of response param
      - `+ jobId`
      - `- job_id`
  - **RetryEngine**
    - changes of response param
      - `+ jobId`
      - `- job_id`
  - **DownloadKie**
    - changes of response param
      - `+ data.id`
  - **CreateEngine**
    - changes of response param
      - `+ jobId`
      - `- job_id`
  - **DeleteEngine**
    - changes of response param
      - `+ jobId`
      - `- job_id`

### HuaweiCloud SDK DAS

- _Features_
  - Support the interfaces `CreateShareConnections`, `CancelShareConnections`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DWS

- _Features_
  - Support the interfaces `ListAvailableDisasterClusters`, `CheckDisasterName`, `ShowDisasterDetail`, `UpdateDisasterInfo`
- _Bug Fix_
  - None
- _Change_
  - **CreateCluster**
    - changes of request param
      - `+ cluster.tags`

### HuaweiCloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateServers**
    - changes of request param
      - `+ server.root_volume.metadata`
      - `- server.root_volume.extendparam.__system__encrypted`
      - `- server.root_volume.extendparam.__system__cmkid`
      - `+ server.data_volumes.delete_on_termination`
  - **CreatePostPaidServers**
    - changes of request param
      - `+ server.data_volumes.delete_on_termination`
      - `+ server.root_volume.metadata`
      - `- server.root_volume.extendparam.__system__encrypted`
      - `- server.root_volume.extendparam.__system__cmkid`

### HuaweiCloud SDK GaussDB

- _Features_
  - Support the interfaces `UpdateGaussMySqlDatabaseUserComment`, `UpdateGaussMySqlDatabaseComment`, `ListLtsSlowlogDetails`, `ListLtsErrorLogDetails`
- _Bug Fix_
  - None
- _Change_
  - **ListGaussMySqlDatabaseUser**
    - changes of response param
      - `+ users.comment`
  - **CreateGaussMySqlDatabaseUser**
    - changes of request param
      - `+ users.comment`
  - **ListGaussMySqlDatabase**
    - changes of response param
      - `+ databases.comment`
  - **CreateGaussMySqlDatabase**
    - changes of request param
      - `+ databases.comment`

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **BroadcastMessage**
    - changes of request param
      - `+ ttl`
      - `+ message_id`
  - **ShowDeviceGroup**
    - changes of response param
      - `+ dynamic_group_rule`
      - `+ group_type`
  - **UpdateDeviceGroup**
    - changes of response param
      - `+ dynamic_group_rule`
      - `+ group_type`
  - **SearchDevices**
    - changes of response param
      - `+ devices.groups`
  - **AddDeviceGroup**
    - changes of request param
      - `+ group_type`
      - `+ dynamic_group_rule`
    - changes of response param
      - `+ dynamic_group_rule`
      - `+ group_type`
  - **ListDeviceGroups**
    - changes of request param
      - `+ group_type`
      - `+ name`
    - changes of response param
      - `+ device_groups.group_type`
      - `* device_groups: list<DeviceGroupResponsSummery> -> list<DeviceGroupResponseSummary>`

### HuaweiCloud SDK ProjectMan

- _Features_
  - Support the interfaces `ListTemplates`, `SearchIssues`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.39 2023-05-11

### HuaweiCloud SDK AOS

- _Features_
  - Support the interface `ContinueDeployStack`
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
  - **ShowVaultResourceInstances**
    - changes of response param
      - `* resources.resource_detail: list<Vault> -> object<InstancesResourceDetail>`
  - **ListPolicies**
    - changes of response param
      - `+ policies.operation_definition.full_backup_interval`
  - **CreatePolicy**
    - changes of request param
      - `+ policy.operation_definition.full_backup_interval`
    - changes of response param
      - `+ policy.operation_definition.full_backup_interval`
  - **ShowPolicy**
    - changes of response param
      - `+ policy.operation_definition.full_backup_interval`
  - **UpdatePolicy**
    - changes of request param
      - `+ policy.operation_definition.full_backup_interval`
    - changes of response param
      - `+ policy.operation_definition.full_backup_interval`
  - **CreateVault**
    - changes of request param
      - `- vault.billing.extra_info`

### HuaweiCloud SDK CBS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ExecuteGetFramsListByImagesId**
    - changes of request param
      - `+ offset`
      - `+ limit`

### HuaweiCloud SDK CloudPipeline

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListPipelineTemplates**
    - changes of response param
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

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ExportConnections**
    - changes of request param
      - `+ workspace`
  - **ExportJob**
    - changes of request param
      - `+ workspace`
  - **StopJob**
    - changes of request param
      - `+ workspace`
  - **StopJobInstance**
    - changes of request param
      - `+ workspace`
  - **RestoreJobInstance**
    - changes of request param
      - `+ workspace`
  - **CancelScript**
    - changes of request param
      - `+ workspace`
  - **DeleteConnction**
    - changes of request param
      - `+ workspace`
  - **ShowConnection**
    - changes of request param
      - `+ workspace`
  - **UpdateConnection**
    - changes of request param
      - `+ workspace`
  - **ExportJobList**
    - changes of request param
      - `+ workspace`
  - **ImportJob**
    - changes of request param
      - `+ workspace`
  - **DeleteScript**
    - changes of request param
      - `+ workspace`
  - **ShowScript**
    - changes of request param
      - `+ workspace`
  - **UpdateScript**
    - changes of request param
      - `+ workspace`
  - **ExecuteScript**
    - changes of request param
      - `+ workspace`
  - **CreateResource**
    - changes of request param
      - `+ workspace`
  - **DeleteResource**
    - changes of request param
      - `+ workspace`
  - **ShowResource**
    - changes of request param
      - `+ workspace`
  - **UpdateResource**
    - changes of request param
      - `+ workspace`
  - **CreateConnection**
    - changes of request param
      - `+ workspace`
  - **ListConnections**
    - changes of request param
      - `+ workspace`
  - **ImportConnections**
    - changes of request param
      - `+ workspace`
  - **ShowFileInfo**
    - changes of request param
      - `+ workspace`
  - **StartJob**
    - changes of request param
      - `+ workspace`
  - **RunOnce**
    - changes of request param
      - `+ workspace`
  - **ShowJobStatus**
    - changes of request param
      - `+ workspace`
  - **ListJobInstances**
    - changes of request param
      - `+ workspace`
  - **ShowJobInstance**
    - changes of request param
      - `+ workspace`
  - **ListSystemTasks**
    - changes of request param
      - `+ workspace`
  - **CreateScript**
    - changes of request param
      - `+ workspace`
  - **ListScripts**
    - changes of request param
      - `+ workspace`
  - **ListScriptResults**
    - changes of request param
      - `+ workspace`
  - **DeleteJob**
    - changes of request param
      - `+ workspace`
  - **ShowJob**
    - changes of request param
      - `+ workspace`
  - **UpdateJob**
    - changes of request param
      - `+ workspace`
  - **CreateJob**
    - changes of request param
      - `+ workspace`
  - **ListJobs**
    - changes of request param
      - `+ workspace`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowMonitoringData**
    - changes of response param
      - `+ results.data_guard_minitor.migration_bytes_per_second`
  - **BatchListJobDetails**
    - changes of response param
      - `+ results.data_transformation`
      - `+ results.tags`

### HuaweiCloud SDK ECS

- _Features_
  - Support the interface `NovaAttachInterface`
- _Bug Fix_
  - None
- _Change_
  - **ReinstallServerWithoutCloudInit**
    - changes of request param
      - `+ os-reinstall.metadata`
  - **ChangeServerOsWithoutCloudInit**
    - changes of request param
      - `+ os-change.metadata`
  - **ReinstallServerWithCloudInit**
    - changes of request param
      - `+ os-reinstall.metadata.__system__encrypted`
      - `+ os-reinstall.metadata.__system__cmkid`
  - **ChangeServerOsWithCloudInit**
    - changes of request param
      - `+ os-change.metadata.__system__encrypted`
      - `+ os-change.metadata.__system__cmkid`
  - **CreateServers**
    - changes of request param
      - `+ server.root_volume.extendparam.__system__encrypted`
      - `+ server.root_volume.extendparam.__system__cmkid`
  - **CreatePostPaidServers**
    - changes of request param
      - `+ server.root_volume.extendparam.__system__encrypted`
      - `+ server.root_volume.extendparam.__system__cmkid`

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the interfaces `CreateSynthesisTask`, `ShowSynthesisTaskResult`, `CreateCustomPropsTask`, `ShowCustomPropsTaskResult`
- _Bug Fix_
  - None
- _Change_
  - **CreateCpiTask**
    - changes of request param
      - `+ custom_props`
  - **CreateGenerationTask**
    - changes of request param
      - `+ custom_props`
  - **CreateOptimizationTask**
    - changes of request param
      - `+ custom_props`
  - **ShowCpiTaskResult**
    - changes of response param
      - `+ task_data.custom_props`
      - `+ result.custom_props`
  - **ShowGenerationTaskResult**
    - changes of response param
      - `+ task_data.custom_props`
      - `+ result.initial_dataset_size`
      - `+ result.strong_constraints`
      - `+ result.weak_constraints`
      - `+ result.binding_site`
      - `+ result.custom_props`
  - **ShowOptimizationTaskResult**
    - changes of response param
      - `+ task_data.custom_props`
      - `+ result.strong_constraints`
      - `+ result.weak_constraints`
      - `+ result.binding_site`
      - `+ result.custom_props`

### HuaweiCloud SDK GaussDB

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListGaussMySqlInstances**
    - changes of request param
      - `+ readonly_private_ip`
      - `+ proxy_ip`
    - changes of response param
      - `+ instances.readonly_private_ips`
      - `+ instances.proxy_ips`

### HuaweiCloud SDK Image

- _Features_
  - Support the interfaces `CreateVideoTaggingMediaTask`, `ShowVideoTaggingMediaTask`
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
  - **ListImages**
    - changes of request param
      - `+ __imagetype: enum value [market]`

### HuaweiCloud SDK Live

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateRecordIndex**
    - changes of response param
      - `+ width`
      - `- weight`
  - **ListAreaDetail**
    - changes of request param
      - `* play_domains: required -> optional`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **UpdateAomMappingRules**
    - changes of request param
      - `* body: object<AomMappingRequestInfo> -> object<UpdateAomMappingRequest>`

### HuaweiCloud SDK MPC

- _Features_
  - Support the interfaces `ListEditingJobs`, `CreateEditingJobs`, `DeleteEditingJobs`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OSM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListOrderIncident**
    - changes of request param
      - `+ xCustomerId`
    - changes of response param
      - `* incidentInfoList.incidentTypeName: object -> string`

### HuaweiCloud SDK RDS

- _Features_
  - Support the interfaces `UpdatePostgresqlDbUserComment`, `UpdatePostgresqlDatabase`, `DeletePostgresqlDbUser`, `DeletePostgresqlDatabase`
- _Bug Fix_
  - None
- _Change_
  - **CreatePostgresqlDatabase**
    - changes of request param
      - `+ comment`
  - **CreatePostgresqlDbUser**
    - changes of request param
      - `+ comment`
  - **ListPostgresqlDatabases**
    - changes of response param
      - `+ databases.comment`
  - **ListPostgresqlDbUserPaginated**
    - changes of response param
      - `+ users.comment`

### HuaweiCloud SDK RMS

- _Features_
  - Support the interfaces `ShowAggregatePolicyStateComplianceSummary`, `ListAggregateComplianceByPolicyAssignment`, `ShowAggregateComplianceDetailsByPolicyAssignment`, `ShowAggregatePolicyAssignmentDetail`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK SFSTurbo

- _Features_
  - Support the following interfaces：
    - `ShowFsDirQuota`
    - `UpdateFsDirQuota`
    - `CreateFsDirQuota`
    - `DeleteFsDirQuota`
    - `ShowFsDir`
    - `CreateFsDir`
    - `DeleteFsDir`
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
  - **RunSqlConversion**
    - changes of request param
      - `+ target_db_type: enum value [GaussDB Primary/Standby]`
  - **ConfirmTargetDbType**
    - changes of request param
      - `- target_db_type: enum value [RDS for MySQL,GaussDB(for MySQL),RDS for PostgreSQL]`
      - `- target_db_version: enum value [5.7,8.0,11,Enhanced Edition]`

# 3.1.38 2023-04-27

### HuaweiCloud SDK MSGSMS

- _Features_
  - Support the service `MSG&SMS`
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
  - **ListResourceUnderNode**
    - changes of request param
      - `+ marker`
      - `- maker`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDomainFullConfig**
    - changes of response param
      - `+ configs.ipv6_accelerate`
      - `+ configs.origin_range_status`

### HuaweiCloud SDK CFW

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListIpsProtectModeUsingPost**
    - changes of response param
      - `+ data`
      - `- object_id`
      - `- status`

### HuaweiCloud SDK CSMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListResourceInstances**
    - changes of response param
      - `+ resources.sys_tags`

### HuaweiCloud SDK DCS

- _Features_
  - Support the interfaces `ResetPassword`, `UpdateInstanceBandwidth`, `ListConfigTemplates`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK DLI

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateBatchJob**
    - changes of request param
      - `+ catalog_name`
  - **ShowJobTemplate**
    - changes of response param
      - `+ body.catalog_name`
  - **ListJobTemplates**
    - changes of response param
      - `+ templates.body.catalog_name`

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **PublishData**
    - changes of response param
      - `+ id`
      - `- asset_id`
  - **PublishImage**
    - changes of response param
      - `+ id`
      - `- asset_id`
  - **PublishApp**
    - changes of response param
      - `+ id`
      - `- asset_id`
  - **PublishWorkflow**
    - changes of response param
      - `+ id`
      - `- asset_id`
  - **ListImageTag**
    - changes of response param
      - `+ tags.path`
  - **CreateApp**
    - changes of request param
      - `* body: object<AppDto> -> object<AppReq>`
  - **UpdateApp**
    - changes of request param
      - `* body: object<AppDto> -> object<AppReq>`
  - **ListData**
    - changes of response param
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
    - changes of request param
      - `+ search_key`

### HuaweiCloud SDK Image

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `RunQueryCustomTags`, `RunDeleteCustomTags`

### HuaweiCloud SDK Kafka

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateInstanceByEngine**
    - changes of request param
      - `+ kafka_security_protocol`
      - `+ sasl_enabled_mechanisms`
  - **ShowInstance**
    - changes of response param
      - `+ kafka_security_protocol`
      - `+ sasl_enabled_mechanisms: enum value [PLAIN,SCRAM-SHA-512]`
  - **CreatePostPaidInstance**
    - changes of request param
      - `+ kafka_security_protocol`
      - `+ sasl_enabled_mechanisms: enum value [PLAIN,SCRAM-SHA-512]`
  - **ListInstances**
    - changes of response param
      - `+ kafka_security_protocol`
      - `+ instances.kafka_security_protocol`
      - `+ instances.sasl_enabled_mechanisms: enum value [PLAIN,SCRAM-SHA-512]`

### HuaweiCloud SDK KMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListKeys**
    - changes of response param
      - `+ key_details.partition_type`
  - **ListKeyDetail**
    - changes of response param
      - `+ key_info.partition_type`
  - **ListRetirableGrants**
    - changes of response param
      - `+ total`
  - **ListKmsByTags**
    - changes of response param
      - `+ resources.resource_detail.partition_type`

### HuaweiCloud SDK LTS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListLogHistogram**
    - changes of request param
      - `+ is_iterative`
    - changes of response param
      - `+ isQueryComplete`
  - **Createfavorite**
    - changes of response param
      - `* create_time: string -> int64`
  - **ListLogStream**
    - changes of response param
      - `+ log_streams.is_favorite`
  - **ListLogs**
    - changes of request param
      - `+ is_iterative`
    - changes of response param
      - `+ isQueryComplete`
  - **UpdateStructTemplate**
    - changes of request param
      - `* rule: list<rule> -> object<rule>`
  - **CreateStructTemplate**
    - changes of request param
      - `* rule: list<rule> -> object<rule>`
  - **ListHistorySql**
    - changes of request param
      - `+ log_group_id`
      - `+ log_stream_id`

### HuaweiCloud SDK Organizations

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreatePolicy**
    - changes of request param
      - `+ type: enum value [tag_policy]`
  - **EnablePolicyType**
    - changes of request param
      - `+ policy_type: enum value [tag_policy]`
  - **DisablePolicyType**
    - changes of request param
      - `+ policy_type: enum value [tag_policy]`

### HuaweiCloud SDK RocketMQ

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowConsumerListOrDetails**
    - changes of response param
      - `* total: int64 -> int32`

### HuaweiCloud SDK SMS

- _Features_
  - Support the following interfaces：
    - `ListApiVersion`
    - `ShowApiVersion`
    - `ShowConfig`
    - `UpdateNetworkCheckInfo`
    - `ShowConfigSetting`
    - `UploadSpecialConfigurationSetting`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.37 2023-04-20

### HuaweiCloud SDK AOM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListAllVersionByVersionId**
    - changes of response param
      - `+ elements.job_reference_number`
      - `+ elements.job_reference_name`
      - `- elements.reference_number`
      - `- elements.script_reference`

### HuaweiCloud SDK AOS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **GetStackTemplate**
    - changes of request param
      - `- executor`
  - **ListStackEvents**
    - changes of request param
      - `- executor`
  - **ListStackOutputs**
    - changes of request param
      - `- executor`
  - **DeleteStack**
    - changes of request param
      - `- executor`
  - **DeleteExecutionPlan**
    - changes of request param
      - `- executor`
  - **ApplyExecutionPlan**
    - changes of request param
      - `- executor`
  - **GetExecutionPlan**
    - changes of request param
      - `- executor`
  - **ListStackResources**
    - changes of request param
      - `- executor`
  - **ListExecutionPlans**
    - changes of request param
      - `- executor`
  - **CreateExecutionPlan**
    - changes of request param
      - `- executor`
  - **GetExecutionPlanMetadata**
    - changes of request param
      - `- executor`
  - **GetStackMetadata**
    - changes of request param
      - `- executor`
  - **ListStacks**
    - changes of request param
      - `- executor`
  - **CreateStack**
    - changes of request param
      - `- executor`
  - **DeployStack**
    - changes of request param
      - `- executor`

### HuaweiCloud SDK BSSINTL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListCustomerselfResourceRecordDetails**
    - changes of response param
      - `+ monthly_records.pre_order_id`
      - `+ monthly_records.az_code_infos`

### HuaweiCloud SDK CBS

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CDN

- _Features_
  - Support the interfaces `ShowDomainFullConfig`, `UpdateDomainFullConfig`
- _Bug Fix_
  - None
- _Change_
  - **ShowDomainFullConfig**
    - changes of response param
      - `+ configs.origin_follow302_status`
      - `+ configs.cache_rules`
      - `+ configs.ip_filter`
      - `+ configs.referer`
      - `+ configs.force_redirect.redirect_code`
  - **UpdateDomainFullConfig**
    - changes of request param
      - `+ configs.origin_follow302_status`
      - `+ configs.cache_rules`
      - `+ configs.ip_filter`
      - `+ configs.referer`
      - `+ configs.force_redirect.redirect_code`

### HuaweiCloud SDK CloudPipeline

- _Features_
  - Support the interfaces `ListPipelineTemplates`, `ShowPipelineTemplateDetail`, `CreatePipelineByTemplateId`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListLogsJob**
    - changes of request param
      - `+ start`
      - `+ limit`
  - **ShowVpcepConnection**
    - changes of request param
      - `+ start`
      - `+ limit`
  - **ListYmlsJob**
    - changes of request param
      - `+ start`
      - `+ limit`

### HuaweiCloud SDK DCS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateRedislogDownloadLink**
    - changes of response param
      - `+ backup_id`

### HuaweiCloud SDK DDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateConfiguration**
    - changes of response param
      - `+ configuration`
      - `- datastore_version`
      - `- created`
      - `- name`
      - `- description`
      - `- id`
      - `- datastore_name`
      - `- updated`

### HuaweiCloud SDK DLF

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowJob**
    - changes of response param
      - `+ lastUpdateUser`
      - `+ id`
  - **UpdateJob**
    - changes of request param
      - `+ lastUpdateUser`
      - `+ id`
  - **CreateJob**
    - changes of request param
      - `+ lastUpdateUser`
      - `+ id`
  - **ListJobs**
    - changes of response param
      - `+ lastUpdateUser`
      - `+ id`
      - `+ jobs.id`
      - `+ jobs.lastUpdateUser`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowJobList**
    - changes of response param
      - `+ jobs.job_action`
      - `+ jobs.children.job_action`
  - **BatchListJobDetails**
    - changes of response param
      - `+ results.original_job_direction`

### HuaweiCloud SDK FunctionGraph

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ImportFunction**
    - changes of response param
      - `+ gpu_memory`
      - `+ func_vpc.security_groups`
  - **ListFunctions**
    - changes of response param
      - `+ functions.gpu_memory`
      - `+ functions.is_bridge_function`
      - `+ functions.bind_bridge_funcUrns`
  - **CreateFunction**
    - changes of request param
      - `+ gpu_memory`
      - `+ log_config`
      - `+ network_controller`
      - `+ func_vpc.security_groups`
    - changes of response param
      - `+ gpu_memory`
      - `+ func_vpc.security_groups`
  - **ShowFunctionConfig**
    - changes of response param
      - `+ gpu_memory`
      - `+ ephemeral_storage`
      - `+ func_vpc.security_groups`
  - **UpdateFunctionConfig**
    - changes of request param
      - `+ gpu_memory`
      - `+ ephemeral_storage`
      - `+ log_config`
      - `+ network_controller`
      - `+ restore_hook_handler`
      - `+ restore_hook_timeout`
      - `+ func_vpc.security_groups`
    - changes of response param
      - `+ gpu_memory`
      - `+ ephemeral_storage`
      - `+ func_vpc.security_groups`
  - **UpdateFunctionMaxInstanceConfig**
    - changes of response param
      - `+ func_vpc.security_groups`
  - **CreateFunctionVersion**
    - changes of response param
      - `+ func_vpc.security_groups`

### HuaweiCloud SDK GaussDBforopenGauss

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateDbUser**
    - changes of request param
      - `+ is_login_only`

### HuaweiCloud SDK GSL

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListSimCards**
    - changes of request param
      - `+ price_plan_id`

### HuaweiCloud SDK Image

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
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
    - changes of request param
      - `- input.data.bucket`
      - `- input.data.path`
  - **ShowImageHighresolutionMattingTask**
    - changes of response param
      - `- input.data.bucket`
      - `- input.data.path`

### HuaweiCloud SDK IoTDA

- _Features_
  - Support the interface `BroadcastMessage`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IoTEdge

- _Features_
  - Support the following interfaces：
    - `BatchListOtTemplates`
    - `AddOtTemplates`
    - `ShowOtTemplate`
    - `DeleteOtTemplate`
    - `AddGeneralOtTemplate`
    - `UpdateModuleState`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Meeting

- _Features_
  - Support the interface `BatchShowUserDetails`
- _Bug Fix_
  - None
- _Change_
  - **UpdateWebinar**
    - changes of request param
      - `+ enableRecording`
  - **CreateWebinar**
    - changes of request param
      - `+ enableRecording`
    - changes of response param
      - `+ enableRecording`
  - **ShowWebinar**
    - changes of response param
      - `+ enableRecording`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RecognizeDriverLicense**
    - changes of response param
      - `+ result.front`
      - `+ result.back`
  - **RecognizeThailandIdcard**
    - changes of response param
      - `+ result.type`
      - `+ result.name_en`
      - `+ result.ref_number`
      - `+ result.confidence.name_en`
      - `+ result.confidence.ref_number`

### HuaweiCloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListRestoreTimes**
    - changes of response param
      - `* restore_time.start_time: int32 -> int64`
      - `* restore_time.end_time: int32 -> int64`
  - **ListOffSiteRestoreTimes**
    - changes of response param
      - `* restore_time.start_time: int32 -> int64`
      - `* restore_time.end_time: int32 -> int64`
  - **RestoreToExistingInstance**
    - changes of request param
      - `* source.restore_time: int32 -> int64`
  - **RestoreExistInstance**
    - changes of request param
      - `* source.restore_time: int32 -> int64`
  - **CreateInstance**
    - changes of request param
      - `* restore_point.restore_time: int32 -> int64`
    - changes of response param
      - `* instance.restore_point.restore_time: int32 -> int64`
  - **CreateRestoreInstance**
    - changes of request param
      - `* restore_point.restore_time: int32 -> int64`
    - changes of response param
      - `* instance.restore_point.restore_time: int32 -> int64`

### HuaweiCloud SDK RocketMQ

- _Features_
  - Support the interface `ShowConsumerConnections`
- _Bug Fix_
  - None
- _Change_
  - **ShowConsumerListOrDetails**
    - changes of response param
      - `+ total`
      - `+ brokers`
  - **ShowUser**
    - changes of response param
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
  - **UpdateUser**
    - changes of request param
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
    - changes of response param
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
  - **UpdateInstance**
    - changes of request param
      - `+ enable_publicip`
      - `+ publicip_id`
  - **CreateUser**
    - changes of request param
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
    - changes of response param
      - `- default_group_perm: enum value [PUB,PUB|SUB]`
      - `- group_perms.perm: enum value [PUB,PUB|SUB]`
  - **ListUser**
    - changes of response param
      - `- users.default_group_perm: enum value [PUB,PUB|SUB]`
      - `- users.group_perms.perm: enum value [PUB,PUB|SUB]`

### HuaweiCloud SDK VPC

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListVpcsByTags**
    - changes of response param
      - `+ resources.resource_detail`
      - `- resources.resouce_detail`
  - **ListSubnetsByTags**
    - changes of response param
      - `+ resources.resource_detail`
      - `- resources.resouce_detail`
  - **UpdateRouteTable**
    - changes of request param
      - `+ routetable.routes.add`
      - `+ routetable.routes.mod`
      - `+ routetable.routes.del`
      - `* routetable.routes: map<string, list<RouteTableRoute>> -> object<RouteTableRouteAction>`

### HuaweiCloud SDK VPCEP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListServiceDescribeDetails**
    - changes of response param
      - `+ public_border_group`
  - **ListServiceDetails**
    - changes of response param
      - `+ enable_policy`
      - `+ tcp_proxy: enum value [proxy_vni]`
  - **UpdateEndpointService**
    - changes of request param
      - `+ tcp_proxy`
    - changes of response param
      - `+ enable_policy`
      - `+ tcp_proxy: enum value [proxy_vni]`
  - **ListEndpointInfoDetails**
    - changes of response param
      - `+ endpoint_pool_id`
      - `+ public_border_group`
  - **CreateEndpointService**
    - changes of request param
      - `+ enable_policy`
      - `+ tcp_proxy: enum value [proxy_vni]`
    - changes of response param
      - `+ enable_policy`
      - `+ tcp_proxy: enum value [proxy_vni]`
  - **ListEndpointService**
    - changes of response param
      - `+ endpoint_services.enable_policy`
      - `+ endpoint_services.tcp_proxy: enum value [proxy_vni]`
  - **CreateEndpoint**
    - changes of response param
      - `+ endpoint_pool_id`
      - `+ public_border_group`
      - `+ ip`

# 3.1.36 2023-04-13

### HuaweiCloud SDK BSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListCustomerselfResourceRecordDetails**
    - changes of response param
      - `+ monthly_records.pre_order_id`
      - `+ monthly_records.az_code_infos`

### HuaweiCloud SDK Cloudtest

- _Features_
  - Support the interface `ShowReport`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CPTS

- _Features_
  - Support the interfaces `UpdateAgentHealthStatus`, `ShowAgentConfig`
- _Bug Fix_
  - None
- _Change_
  - **ShowReport**
    - changes of response param
      - `* result.brokens.commonTimestamps: list<integer> -> list<string>`

### HuaweiCloud SDK EVS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowVolume**
    - changes of response param
      - `+ volume.iops`
      - `+ volume.throughput`
  - **ListVolumes**
    - changes of response param
      - `+ volumes.iops`
      - `+ volumes.throughput`

### HuaweiCloud SDK IES

- _Features_
  - Support the interfaces `ListRacks`, `ShowRack`, `ListStoragePools`, `ShowStoragePool`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Image

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
    - `CreateVideoSynthesisTask`
    - `ShowVideoSynthesisTask`
    - `CreateImageToVideoTask`
    - `ShowImageToVideoTask`
    - `CreateVideoCuttingTask`
    - `ShowVideoCuttingTask`
    - `RunImageWisedesignCrop`
    - `RunImageWisedesignInpainting`
  - **RunImageTagging**
    - changes of response param
      - `+ result.tags.instances.bounding_box.width`
      - `+ result.tags.instances.bounding_box.height`
      - `+ result.tags.instances.bounding_box.top_left_x`
      - `+ result.tags.instances.bounding_box.top_left_y`
      - `* result.tags.instances.bounding_box: object -> object<ImageTaggingBoundingBox>`
  - **RunImageMediaTagging**
    - changes of response param
      - `+ result.tags.instances.bounding_box.width`
      - `+ result.tags.instances.bounding_box.height`
      - `+ result.tags.instances.bounding_box.top_left_x`
      - `+ result.tags.instances.bounding_box.top_left_y`
      - `* result.tags.instances.bounding_box: object -> object<BoundingBox>`
      - `* result.tags.instances: list<ImageTaggingInstance> -> list<ImageMediaTaggingInstance>`
  - **RunImageMediaTaggingDet**
    - changes of response param
      - `+ result.tags.instances.bounding_box.width`
      - `+ result.tags.instances.bounding_box.height`
      - `+ result.tags.instances.bounding_box.top_left_x`
      - `+ result.tags.instances.bounding_box.top_left_y`
      - `* result.tags.instances.bounding_box: object -> object<BoundingBox>`
  - **ShowVideoShotSplitTask**
    - changes of response param
      - `- state: enum value [SUCCEEDED,FAILED,RUNNING]`
  - **CreateVideoTranslateTask**
    - changes of request param
      - `* body: object<VideoTranslateRequestBody> -> object<CreateVideoTranslateTaskRequestBody>`
  - **CreateImageHighresolutionMattingTask**
    - changes of request param
      - `* input.data: list<TaskInputData> -> list<ImageHighresolutionMattingInputData>`
      - `* input: object<TaskInput> -> object<ImageHighresolutionMattingInput>`
  - **ShowImageHighresolutionMattingTask**
    - changes of response param
      - `* input.data: list<TaskInputData> -> list<ImageHighresolutionMattingInputData>`
      - `* input: object<TaskInput> -> object<ImageHighresolutionMattingInput>`
  - **CreateImageTranslateTask**
    - changes of request param
      - `* input.data: list<TaskInputData> -> list<ImageTranslateTaskInputData>`
      - `* input: object<TaskInput> -> object<ImageTranslateTaskInput>`
      - `* body: object<ImageTranslateRequestBody> -> object<CreateImageTranslateRequestBody>`
  - **ShowImageTranslateTask**
    - changes of response param
      - `* input.data: list<TaskInputData> -> list<ImageTranslateTaskInputData>`
      - `* input: object<TaskInput> -> object<ImageTranslateTaskInput>`
  - **CreateVideoCoverAnalysisTask**
    - changes of request param
      - `* input.data: list<TaskInputData> -> list<VideoCoverAnalysisTaskInputData>`
      - `* input: object<TaskInput> -> object<VideoCoverAnalysisTaskInput>`
      - `* body: object<VideoCoverAnalysisCreateTaskRequestBody> -> object<CreateVideoCoverAnalysisTaskRequestBody>`
  - **ShowVideoCoverAnalysisTask**
    - changes of response param
      - `* input.data: list<TaskInputData> -> list<VideoCoverAnalysisTaskInputData>`
      - `* input: object<TaskInput> -> object<VideoCoverAnalysisTaskInput>`
  - **CreateVideoSummarizationAnalysisTask**
    - changes of request param
      - `* input.data: list<TaskInputData> -> list<VideoSummarizationTaskInputData>`
      - `* input: object<TaskInput> -> object<VideoSummarizationTaskInput>`
      - `* body: object<VideoSummarizationCreateTaskRequestBody> -> object<CreateVideoSummarizationTaskRequestBody>`
  - **ShowVideoSummarizationAnalysisTask**
    - changes of response param
      - `* input.data: list<TaskInputData> -> list<VideoSummarizationTaskInputData>`
      - `* input: object<TaskInput> -> object<VideoSummarizationTaskInput>`
  - **CreateVideoObjectMaskingTask**
    - changes of request param
      - `* input.data: list<TaskInputData> -> list<ObjectMaskingTaskInputData>`
      - `* input: object<TaskInput> -> object<ObjectMaskingTaskInput>`
  - **ShowVideoObjectMaskingTask**
    - changes of response param
      - `* input.data: list<TaskInputData> -> list<ObjectMaskingTaskInputData>`
      - `* input: object<TaskInput> -> object<ObjectMaskingTaskInput>`

### HuaweiCloud SDK Kafka

- _Features_
  - Support the interface `BatchDeleteGroup`
- _Bug Fix_
  - None
- _Change_
  - **ResizeEngineInstance**
    - changes of request param
      - `+ publicip_id`

### HuaweiCloud SDK Live

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OSM

- _Features_
  - Support the interfaces `ListDiagnoseResources`, `ListOrderIncident`
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
  - **RecognizeShortAudio**
    - changes of request param
      - `+ config.property: enum value [english_8k_common,english_16k_common]`
  - **CollectTranscriberJob**
    - changes of response param
      - `+ job_id`

### HuaweiCloud SDK WAF

- _Features_
  - Support the interfaces `CreateCloudWafPostPaidResource`, `DeleteCloudWafPostPaidResource`
- _Bug Fix_
  - None
- _Change_
  - **ListCustomRules**
    - changes of response param
      - `+ items.name`

# 3.1.35 2023-04-06

### HuaweiCloud SDK CCM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ExportCertificate**
    - changes of request param
      - `+ password`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateRefreshTasks**
    - changes of request param
      - `+ refresh_task.mode`

### HuaweiCloud SDK CES

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListAlarmHistories**
    - changes of response param
      - `+ alarm_histories.type: enum value [DNSHealthCheck,RESOURCE_GROUP,MULTI_INSTANCE,ALL_INSTANCE]`
  - **ListAlarmRules**
    - changes of response param
      - `+ alarms.type: enum value [EVENT.SYS,EVENT.CUSTOM,DNSHealthCheck,RESOURCE_GROUP,MULTI_INSTANCE,ALL_INSTANCE]`
  - **CreateAlarmRules**
    - changes of request param
      - `+ type: enum value [EVENT.SYS,EVENT.CUSTOM,DNSHealthCheck,RESOURCE_GROUP,MULTI_INSTANCE,ALL_INSTANCE]`

### HuaweiCloud SDK DeH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListServersDedicatedHost**
    - changes of response param
      - `- servers.addresses.vpc_id`
      - `* servers.addresses: object<RespAddresses> -> map<string, list<RespAddr>>`

### HuaweiCloud SDK GSL

- _Features_
  - Support the interfaces `SendSms`, `ListSmsDetails`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Image

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `CreateTextToImageTask`, `ShowTextToImageTask`, `CreateImageVariationTask`, `ShowImageVariationTask`

### HuaweiCloud SDK MRS

- _Features_
  - Support the interface `RunJobFlow`
- _Bug Fix_
  - None
- _Change_
  - **CreateCluster**
    - changes of request param
      - `+ log_uri`
      - `+ component_configs`

### HuaweiCloud SDK OCR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **RecognizeFinancialStatement**
    - changes of request param
      - `+ return_rectification_matrix`
    - changes of response param
      - `+ result.rectification_matrix`

### HuaweiCloud SDK RAM

- _Features_
  - Support the interfaces `ListResourceShareTags`, `ListResourceSharesByTags`, `SearchResourceShareCountByTags`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.34 2023-03-30

### HuaweiCloud SDK BSS

- _Features_
  - Support the interface `ListRenewRateOnPeriod`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BSSINTL

- _Features_
  - Support the interface `ListRenewRateOnPeriod`
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
  - **ListBackups**
    - changes of request param
      - `+ incremental`
  - **ListVault**
    - changes of response param
      - `+ vaults.billing.object_type: enum value [vmware,rds,file]`
  - **CreateVault**
    - changes of request param
      - `+ vault.billing.object_type: enum value [vmware,rds,file]`
    - changes of response param
      - `+ vault.billing.object_type: enum value [vmware,rds,file]`
  - **ShowVault**
    - changes of response param
      - `+ vault.billing.object_type: enum value [vmware,rds,file]`
  - **UpdateVault**
    - changes of response param
      - `+ vault.billing.object_type: enum value [vmware,rds,file]`
  - **ShowVaultResourceInstances**
    - changes of response param
      - `+ resources.resource_detail.billing.object_type: enum value [vmware,rds,file]`
  - **ListProtectable**
    - changes of response param
      - `+ instances.protectable.vault.billing.object_type: enum value [vmware,rds,file]`
  - **ShowProtectable**
    - changes of response param
      - `+ instance.protectable.vault.billing.object_type: enum value [vmware,rds,file]`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interfaces `CreateApply`, `CreateEvent`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK CSS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateAutoCreatePolicy**
    - changes of request param
      - `+ indices`

### HuaweiCloud SDK DRS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListUsers**
    - changes of response param
      - `* user_list.privileges: list<string> -> string`
  - **BatchUpdateUser**
    - changes of response param
      - `* results.user_list.privileges: list<string> -> string`

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the interface `ShowAdmetProperties`
- _Bug Fix_
  - None
- _Change_
  - **CreateGenerationTask**
    - changes of request param
      - `- strong_constraints.requirement`
  - **CreateOptimizationTask**
    - changes of request param
      - `- strong_constraints.requirement`
  - **ShowGenerationTaskResult**
    - changes of response param
      - `- task_data.strong_constraints.requirement`
  - **ShowOptimizationTaskResult**
    - changes of response param
      - `- task_data.strong_constraints.requirement`

### HuaweiCloud SDK IoTDA

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListOtaPackageInfo**
    - changes of request param
      - `- Sp-Auth-Token`
  - **CreateOtaPackage**
    - changes of request param
      - `- Sp-Auth-Token`
  - **DeleteOtaPackage**
    - changes of request param
      - `- Sp-Auth-Token`
  - **ShowOtaPackage**
    - changes of request param
      - `- Sp-Auth-Token`
  - **ShowRuleAction**
    - changes of response param
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
  - **UpdateRuleAction**
    - changes of request param
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
    - changes of response param
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
  - **CreateRuleAction**
    - changes of request param
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
    - changes of response param
      - `+ channel_detail.http_forwarding.signature_enable`
      - `+ channel_detail.http_forwarding.token`
  - **ListRuleActions**
    - changes of response param
      - `+ actions.channel_detail.http_forwarding.signature_enable`
      - `+ actions.channel_detail.http_forwarding.token`
  - **ShowRule**
    - changes of response param
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
  - **UpdateRule**
    - changes of request param
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
    - changes of response param
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
  - **CreateRule**
    - changes of request param
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
    - changes of response param
      - `+ actions.device_alarm.dimension`
      - `+ condition_group.conditions.device_linkage_status_condition`
      - `+ condition_group.conditions.device_property_condition.filters.in_values`
  - **ListRules**
    - changes of response param
      - `+ rules.actions.device_alarm.dimension`
      - `+ rules.condition_group.conditions.device_linkage_status_condition`
      - `+ rules.condition_group.conditions.device_property_condition.filters.in_values`

### HuaweiCloud SDK NAT

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListPrivateDnats**
    - changes of response param
      - `* page_info.current_count: number -> integer`
  - **ListPrivateNats**
    - changes of response param
      - `* page_info.current_count: number -> integer`
  - **ListPrivateSnats**
    - changes of response param
      - `* page_info.current_count: number -> integer`
  - **ListTransitIps**
    - changes of response param
      - `* page_info.current_count: number -> integer`

### HuaweiCloud SDK Organizations

- _Features_
  - Support the following interfaces：
    - `ShowCreateAccountStatus`
    - `ShowEffectivePolicies`
    - `ListTagPolicyServices`
    - `ListTagResources`
    - `CreateTagResource`
    - `DeleteTagResource`
    - `ListResourceInstances`
    - `ShowResourceInstancesCount`
    - `ListResourceTags`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK OSM

- _Features_
  - Support the interface `ShowConfiguration`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK RAM

- _Features_
  - Support the interfaces `BatchCreateResourceShareTags`, `BatchDeleteResourceShareTags`
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
  - **PublishAssetFromObs**
    - changes of request param
      - `+ video_type: enum value [RMVB,WEBM]`

### HuaweiCloud SDK WAF

- _Features_
  - Support the interfaces `ShowValueList`, `ShowPrivacyRule`, `ShowAntitamperRule`, `ShowWhiteBlackIpRule`
- _Bug Fix_
  - None
- _Change_
  - **ShowCcRule**
    - changes of response param
      - `+ name`
      - `* mode: number -> int32`
  - **UpdateCcRule**
    - changes of request param
      - `+ name`
    - changes of response param
      - `+ name`
      - `* mode: number -> int32`
  - **DeleteCcRule**
    - changes of response param
      - `+ name`
      - `* mode: number -> int32`
  - **ShowCustomRule**
    - changes of response param
      - `+ time`
  - **UpdateCustomRule**
    - changes of response param
      - `+ time`
  - **DeleteCustomRule**
    - changes of response param
      - `+ time`
  - **ListAntileakageRules**
    - changes of response param
      - `+ items.description`
  - **CreateCcRule**
    - changes of request param
      - `+ name`
    - changes of response param
      - `+ name`
      - `* mode: number -> int32`
  - **ListCcRules**
    - changes of response param
      - `+ items.name`
  - **CreateCustomRule**
    - changes of response param
      - `+ time`
  - **ListCustomRules**
    - changes of response param
      - `+ items.time`

# 3.1.33 2023-03-23

### HuaweiCloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowNode**
    - changes of response param
      - `+ spec.extendParam.agency_name`
  - **UpdateNode**
    - changes of response param
      - `+ spec.extendParam.agency_name`
  - **DeleteNode**
    - changes of response param
      - `+ spec.extendParam.agency_name`
  - **CreateNode**
    - changes of request param
      - `+ spec.extendParam.agency_name`
    - changes of response param
      - `+ spec.extendParam.agency_name`
  - **ListNodes**
    - changes of response param
      - `+ items.spec.extendParam.agency_name`
  - **ShowNodePool**
    - changes of response param
      - `+ spec.nodeTemplate.extendParam.agency_name`
  - **UpdateNodePool**
    - changes of response param
      - `+ spec.nodeTemplate.extendParam.agency_name`
  - **DeleteNodePool**
    - changes of response param
      - `+ spec.nodeTemplate.extendParam.agency_name`
  - **CreateNodePool**
    - changes of request param
      - `+ spec.nodeTemplate.extendParam.agency_name`
    - changes of response param
      - `+ spec.nodeTemplate.extendParam.agency_name`
  - **ListNodePools**
    - changes of response param
      - `+ items.spec.nodeTemplate.extendParam.agency_name`

### HuaweiCloud SDK CDN

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowDomainDetailByName**
    - changes of response param
      - `- domain.banned_reason`
      - `- domain.locked_reason`
      - `- domain.enterprise_project_id`

### HuaweiCloud SDK CloudIDE

- _Features_
  - Support the interfaces `UploadFilePublisher`, `ShowExtensionTestingResult`, `PublishExtension`
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
  - **CreateMigrationTask**
    - changes of request param
      - `+ backup_files.file_source: enum value [backup_record]`
  - **ShowMigrationTask**
    - changes of response param
      - `+ backup_files.file_source: enum value [backup_record]`
  - **StopMigrationTask**
    - changes of response param
      - `+ backup_files.file_source: enum value [backup_record]`

### HuaweiCloud SDK DDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowReplSetName**
    - changes of response param
      - `+ name`
  - **UpdateReplSetName**
    - changes of response param
      - `+ job_id`

### HuaweiCloud SDK DLI

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - Remove the interface `CreateDownloadJob`
  - **ShowBatchInfo**
    - changes of response param
      - `* appId: list<string> -> string`
  - **ChangeQueuePlan**
    - changes of request param
      - `+ repeat_day: enum value [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY]`
      - `- repeat_day: enum value [ MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]`
  - **DisassociateConnectionQueue**
    - changes of request param
      - `+ elastic_resource_pools`
      - `- queues: enum value [q1,q2]`
  - **AssociateConnectionQueue**
    - changes of request param
      - `+ elastic_resource_pools`
  - **ListBatches**
    - changes of response param
      - `* sessions.appId: list<string> -> string`
  - **CreateBatchJob**
    - changes of request param
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
    - changes of response param
      - `* appId: list<string> -> string`
  - **CreateTable**
    - changes of request param
      - `+ tags`
  - **ListQueues**
    - changes of response param
      - `* queues: list<ListQueuesRespQueues> -> list<QueueDetails>`
  - **CreateQueuePlan**
    - changes of request param
      - `+ repeat_day: enum value [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY]`
      - `- repeat_day: enum value [ MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]`
  - **ListQueuePlans**
    - changes of response param
      - `+ plans.repeat_day: enum value [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY]`
      - `- plans.repeat_day: enum value [ MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]`
  - **ShowEnhancedConnection**
    - changes of response param
      - `+ elastic_resource_pools`
  - **ListElasticResourcePools**
    - changes of request param
      - `+ status: enum value [AVAILABLE,SCALING,CREATING,FAILED]`
      - `+ status: enum value [AVAILABLE，SCALING，CREATING，FAILED]`
  - **CreateFlinkJar**
    - changes of request param
      - `* body: object<CreateFlinkdefinedJobsReq> -> object<CreateFlinkJarRequestBody>`
  - **UpdateFlinkJar**
    - changes of request param
      - `* body: object<UpdateFlinkdefinedJobsResp> -> object<UpdateFlinkJarRequestBody>`
  - **ListEnhancedConnections**
    - changes of request param
      - `* limit: string -> int32`
      - `* offset: string -> int32`
    - changes of response param
      - `+ connections.elastic_resource_pools`
  - **CreateFlinkTemplate**
    - changes of request param
      - `+ job_type: enum value [flink_sql_job,flink_opensource_sql_job]`
      - `- job_type: enum value [flink_sql_job，flink_opensource_sql_job]`
      - `* body: object<CreateTemplateReq> -> object<CreateFlinkTemplateRequestBody>`

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the following interfaces：
    - `CreateCpiTask`
    - `ShowCpiTaskResult`
    - `CreateGenerationTask`
    - `ShowGenerationTaskResult`
    - `CreateOptimizationTask`
    - `ShowOptimizationTaskResult`
    - `CreateSearchTask`
    - `ShowSearchTaskResult`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK NAT

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK Organizations

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
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

- _Features_
  - Support the interfaces `ShowEngineInstanceExtendProductInfo`, `ResizeEngineInstance`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK WAF

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - **ListHost**
    - changes of response param
      - `- items.paid_type: enum value [prePaid]`
  - **DeleteHost**
    - changes of response param
      - `- paid_type: enum value [prePaid]`

# 3.1.32 2023-03-16

### HuaweiCloud SDK Organizations

- _Features_
  - Support the service `Organizations`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK APIG

- _Features_
  - Support the interfaces `UpdateIngressEipV2`, `AddIngressEipV2`, `RemoveIngressEipV2`
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK BMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowJobInfos**
    - changes of response param
      - `* begin_time: date-time -> string`
      - `* end_time: date-time -> string`
      - `* entities.sub_jobs.begin_time: date-time -> string`
      - `* entities.sub_jobs.end_time: date-time -> string`

### HuaweiCloud SDK CBH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListQuotaStatus**
    - changes of response param
      - `* quota: string -> int32`
      - `* eip_quota: string -> int32`
  - **StopCbhInstance**
    - changes of request param
      - `- reboot`
  - **ShowNetworkConfiguration**
    - changes of request param
      - `+ server_id`
  - **CreateInstanceOrder**
    - changes of request param
      - `- end_time`
      - `- relative_resource_id`
      - `- product_infos.available_zone_id`
  - **ChangeInstanceNetwork**
    - changes of request param
      - `+ server_id`
  - **ListCbhInstance**
    - changes of response param
      - `- instance.is_auto_renew`
  - **CreateInstance**
    - changes of request param
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

- _Features_
  - Support the interfaces `ListDomains`, `ShowDomainDetailByName`
- _Bug Fix_
  - None
- _Change_
  - **ListDomains**
    - changes of request param
      - `+ show_tags`
      - `+ exact_match`
    - changes of response param
      - `+ domains.tags`

### HuaweiCloud SDK CPH

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowBandwidthDetail**
    - changes of request param
      - `+ offset`
      - `+ limit`
  - **ListJobs**
    - changes of request param
      - `+ offset`
      - `+ limit`
  - **ListCloudPhoneModels**
    - changes of request param
      - `+ offset`
      - `+ limit`
  - **CreateCloudPhoneServer**
    - changes of response param
      - `+ server_ids`
  - **CreateNet2CloudPhoneServer**
    - changes of response param
      - `+ server_ids`

### HuaweiCloud SDK eiHealth

- _Features_
  - Support the following interfaces：
    - `ListMessageStatistics`
    - `ListNotice`
    - `BatchDeleteNotice`
    - `BatchUpdateNotice`
    - `ImportUser`
    - `ListGlobalWorkflowStatistic`
- _Bug Fix_
  - None
- _Change_
  - **ListDatabaseData**
    - changes of response param
      - `* objects: list<map<string, object>> -> list<map<string, string>>`
  - **ImportDatabaseData**
    - changes of response param
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
    - changes of response param
      - `+ additions`
  - **UpdateJobConfig**
    - changes of request param
      - `- job_retain_number`
  - **ShowMessageClearRule**
    - changes of response param
      - `- message_retain_time`
  - **UpdateMessageClearRule**
    - changes of request param
      - `- message_retain_number`
      - `- message_retain_time`
  - **ShowOverview**
    - changes of response param
      - `+ is_arrears`
  - **UpdatePerformanceResource**
    - changes of request param
      - `+ schedulable`
  - **ShowEnv**
    - changes of response param
      - `+ enable_cold_archive`
  - **ShowUser**
    - changes of response param
      - `+ source`
  - **ShowAsset**
    - changes of response param
      - `+ versions.description`
      - `- versions.descritpion`
  - **ShowAssetVersion**
    - changes of response param
      - `+ version.description`
      - `- version.descritpion`
  - **CreateBackup**
    - changes of request param
      - `+ storage_type`
  - **ListBackup**
    - changes of response param
      - `+ backups.storage_type`
      - `+ backups.archive_days`
  - **ShowData**
    - changes of request param
      - `+ X-Need-Content`
    - changes of response param
      - `+ content`
  - **ListDataJob**
    - changes of response param
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
    - changes of response param
      - `- allowed_operate`
      - `- deletable`
  - **UpdateMessageReceiveConfig**
    - changes of request param
      - `- scope`
      - `- language`
      - `- resource_types`
  - **ShowMessageEmailConfig**
    - changes of response param
      - `- password`
  - **UpdateMessageEmailConfig**
    - changes of request param
      - `- server`
      - `- subject_prefix`
      - `- password`
      - `- user_name`
      - `- language`
      - `- email`
  - **ListUser**
    - changes of response param
      - `+ source`
      - `+ users.source`
  - **ShowTaskInstanceMetricData**
    - changes of response param
      - `- metric_name`
      - `- resource_id`
  - **ListPerformanceResourceStat**
    - changes of response param
      - `+ performance_resources.schedulable`
  - **ListAsset**
    - changes of response param
      - `+ assets.versions.description`
      - `- assets.versions.descritpion`
  - **ListStar**
    - changes of response param
      - `+ assets.versions.description`
      - `- assets.versions.descritpion`
  - **ListData**
    - changes of response param
      - `+ content`
      - `+ datas.content`
  - **ShowProjectTrace**
    - changes of response param
      - `- allowed_operate`
      - `- deletable`
      - `- datas.allowed_operate`
      - `- datas.deletable`
      - `* datas: list<DataRsp> -> list<TraceDataRsp>`
  - **ListComputingResources**
    - changes of response param
      - `+ resources.failure_reason`
      - `- resources.ip`
      - `- resources.period_num`
  - **ListDatabaseResource**
    - changes of response param
      - `+ resources.failure_reason`
  - **ListPerformanceResources**
    - changes of response param
      - `+ resources.running_job_count`
      - `+ resources.failure_reason`
      - `+ resources.schedulable`
  - **ListStorageResources**
    - changes of response param
      - `- resources.id`
      - `- resources.name`
  - **ExecuteJob**
    - changes of request param
      - `+ tasks.io_acc_type`
  - **CreateAutoJob**
    - changes of request param
      - `+ tasks.io_acc_type`
  - **UpdateJob**
    - changes of request param
      - `+ tasks.io_acc_type`
  - **ShowJob**
    - changes of response param
      - `+ still_running_tasks`
      - `+ task_runtime_info.sub_tasks.pod_create_time`
      - `+ task_runtime_info.sub_tasks.pod_start_time`
      - `+ task_runtime_info.sub_tasks.job_failed_times`
      - `+ tasks.io_acc_type`
  - **UpdateAutoJob**
    - changes of request param
      - `+ tasks.io_acc_type`
  - **ShowAutoJob**
    - changes of response param
      - `+ tasks.io_acc_type`
  - **ShowWorkflow**
    - changes of response param
      - `+ tasks.io_acc_type`

### HuaweiCloud SDK EIP

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListBandwidthPkg**
    - changes of request param
      - `+ limit`
      - `+ marker`
      - `+ offset`
  - **ListCommonPools**
    - changes of request param
      - `+ limit`
      - `+ offset`
  - **ListShareBandwidthTypes**
    - changes of request param
      - `+ marker`
      - `+ offset`

### HuaweiCloud SDK IAM

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **KeystoneListMappings**
    - changes of response param
      - `* mappings.rules.local.groups: object -> string`
  - **KeystoneShowMapping**
    - changes of response param
      - `* mapping.rules.local.groups: object -> string`
  - **KeystoneCreateMapping**
    - changes of request param
      - `* mapping.rules.local.groups: object -> string`
    - changes of response param
      - `* mapping.rules.local.groups: object -> string`
  - **KeystoneUpdateMapping**
    - changes of request param
      - `* mapping.rules.local.groups: object -> string`
    - changes of response param
      - `* mapping.rules.local.groups: object -> string`

### HuaweiCloud SDK Image

- _Features_
  - Support the interfaces `CreateVideoObjectMaskingTask`, `ShowVideoObjectMaskingTask`
- _Bug Fix_
  - None
- _Change_
  - **CreateTextToImageTask**
    - changes of request param
      - `+ config.common.inference.image_nums`
      - `+ config.common.inference.resolution: enum value [512*768,768*512,512*512]`
  - **ShowTextToImageTask**
    - changes of response param
      - `+ config.common.inference.image_nums`
      - `+ config.common.inference.resolution: enum value [512*768,768*512,512*512]`
  - **CreateImageVariationTask**
    - changes of request param
      - `+ config.common.inference.image_nums`
      - `+ config.common.inference.resolution: enum value [512*768,768*512,512*512]`
  - **ShowImageVariationTask**
    - changes of response param
      - `+ config.common.inference.image_nums`
      - `+ config.common.inference.resolution: enum value [512*768,768*512,512*512]`

### HuaweiCloud SDK IoTEdge

- _Features_
  - Support the following interfaces：
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
- _Bug Fix_
  - None
- _Change_
  - None

### HuaweiCloud SDK IVS

- _Features_
  - Support the interfaces `DetectStandardByVideoAndIdCardImage`, `DetectStandardByVideoAndNameAndId`
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
  - **RecognizeMvsInvoice**
    - changes of request param
      - `+ return_text_location`
      - `+ return_confidence`
      - `+ type`
    - changes of response param
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

- _Features_
  - Support the interfaces `ListRecycleInstances`, `ShowRecyclePolicy`
- _Bug Fix_
  - None
- _Change_
  - None

# 3.1.31 2023-03-14

### HuaweiCloud SDK Image

- _Features_
  - Support the interfaces `CreateTextToImageTask`, `ShowTextToImageTask`, `CreateImageVariationTask`, `ShowImageVariationTask`
- _Bug Fix_
  - None
- _Change_
  - Remove the interfaces `RunImageWisedesignColorfilter`, `RunImageWisedesignCombine`

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

