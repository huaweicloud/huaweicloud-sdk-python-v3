# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdklive.v1.live_client import LiveClient
from huaweicloudsdklive.v1.live_async_client import LiveAsyncClient

from huaweicloudsdklive.v1.model.app_quality_info import AppQualityInfo
from huaweicloudsdklive.v1.model.audio_selector_hls_selection import AudioSelectorHlsSelection
from huaweicloudsdklive.v1.model.audio_selector_lang_selection import AudioSelectorLangSelection
from huaweicloudsdklive.v1.model.audio_selector_pid_selection import AudioSelectorPidSelection
from huaweicloudsdklive.v1.model.audio_selector_settings import AudioSelectorSettings
from huaweicloudsdklive.v1.model.batch_show_ip_belongs_request import BatchShowIpBelongsRequest
from huaweicloudsdklive.v1.model.batch_show_ip_belongs_response import BatchShowIpBelongsResponse
from huaweicloudsdklive.v1.model.callback_url import CallbackUrl
from huaweicloudsdklive.v1.model.cdn_ip import CdnIp
from huaweicloudsdklive.v1.model.create_domain_mapping_request import CreateDomainMappingRequest
from huaweicloudsdklive.v1.model.create_domain_mapping_response import CreateDomainMappingResponse
from huaweicloudsdklive.v1.model.create_domain_request import CreateDomainRequest
from huaweicloudsdklive.v1.model.create_domain_response import CreateDomainResponse
from huaweicloudsdklive.v1.model.create_flows_request import CreateFlowsRequest
from huaweicloudsdklive.v1.model.create_flows_request_body import CreateFlowsRequestBody
from huaweicloudsdklive.v1.model.create_flows_response import CreateFlowsResponse
from huaweicloudsdklive.v1.model.create_harvest_task_info_req import CreateHarvestTaskInfoReq
from huaweicloudsdklive.v1.model.create_harvest_task_request import CreateHarvestTaskRequest
from huaweicloudsdklive.v1.model.create_harvest_task_response import CreateHarvestTaskResponse
from huaweicloudsdklive.v1.model.create_ott_channel_info_req import CreateOttChannelInfoReq
from huaweicloudsdklive.v1.model.create_ott_channel_info_req_record_settings import CreateOttChannelInfoReqRecordSettings
from huaweicloudsdklive.v1.model.create_ott_channel_info_request import CreateOttChannelInfoRequest
from huaweicloudsdklive.v1.model.create_ott_channel_info_response import CreateOttChannelInfoResponse
from huaweicloudsdklive.v1.model.create_record_callback_config_request import CreateRecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.create_record_callback_config_response import CreateRecordCallbackConfigResponse
from huaweicloudsdklive.v1.model.create_record_index_request import CreateRecordIndexRequest
from huaweicloudsdklive.v1.model.create_record_index_response import CreateRecordIndexResponse
from huaweicloudsdklive.v1.model.create_record_rule_request import CreateRecordRuleRequest
from huaweicloudsdklive.v1.model.create_record_rule_response import CreateRecordRuleResponse
from huaweicloudsdklive.v1.model.create_schedule_record_tasks_request import CreateScheduleRecordTasksRequest
from huaweicloudsdklive.v1.model.create_schedule_record_tasks_response import CreateScheduleRecordTasksResponse
from huaweicloudsdklive.v1.model.create_snapshot_config_request import CreateSnapshotConfigRequest
from huaweicloudsdklive.v1.model.create_snapshot_config_response import CreateSnapshotConfigResponse
from huaweicloudsdklive.v1.model.create_stream_forbidden_request import CreateStreamForbiddenRequest
from huaweicloudsdklive.v1.model.create_stream_forbidden_response import CreateStreamForbiddenResponse
from huaweicloudsdklive.v1.model.create_transcodings_template_request import CreateTranscodingsTemplateRequest
from huaweicloudsdklive.v1.model.create_transcodings_template_response import CreateTranscodingsTemplateResponse
from huaweicloudsdklive.v1.model.create_url_authchain_req import CreateUrlAuthchainReq
from huaweicloudsdklive.v1.model.create_url_authchain_request import CreateUrlAuthchainRequest
from huaweicloudsdklive.v1.model.create_url_authchain_response import CreateUrlAuthchainResponse
from huaweicloudsdklive.v1.model.dash_package_item import DashPackageItem
from huaweicloudsdklive.v1.model.decoupled_live_domain_info import DecoupledLiveDomainInfo
from huaweicloudsdklive.v1.model.default_record_config import DefaultRecordConfig
from huaweicloudsdklive.v1.model.delay_config import DelayConfig
from huaweicloudsdklive.v1.model.delete_domain_https_cert_request import DeleteDomainHttpsCertRequest
from huaweicloudsdklive.v1.model.delete_domain_https_cert_response import DeleteDomainHttpsCertResponse
from huaweicloudsdklive.v1.model.delete_domain_key_chain_request import DeleteDomainKeyChainRequest
from huaweicloudsdklive.v1.model.delete_domain_key_chain_response import DeleteDomainKeyChainResponse
from huaweicloudsdklive.v1.model.delete_domain_mapping_request import DeleteDomainMappingRequest
from huaweicloudsdklive.v1.model.delete_domain_mapping_response import DeleteDomainMappingResponse
from huaweicloudsdklive.v1.model.delete_domain_request import DeleteDomainRequest
from huaweicloudsdklive.v1.model.delete_domain_response import DeleteDomainResponse
from huaweicloudsdklive.v1.model.delete_flow_request import DeleteFlowRequest
from huaweicloudsdklive.v1.model.delete_flow_response import DeleteFlowResponse
from huaweicloudsdklive.v1.model.delete_harvest_task_request import DeleteHarvestTaskRequest
from huaweicloudsdklive.v1.model.delete_harvest_task_response import DeleteHarvestTaskResponse
from huaweicloudsdklive.v1.model.delete_ott_channel_info_request import DeleteOttChannelInfoRequest
from huaweicloudsdklive.v1.model.delete_ott_channel_info_response import DeleteOttChannelInfoResponse
from huaweicloudsdklive.v1.model.delete_publish_template_request import DeletePublishTemplateRequest
from huaweicloudsdklive.v1.model.delete_publish_template_response import DeletePublishTemplateResponse
from huaweicloudsdklive.v1.model.delete_record_callback_config_request import DeleteRecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.delete_record_callback_config_response import DeleteRecordCallbackConfigResponse
from huaweicloudsdklive.v1.model.delete_record_rule_request import DeleteRecordRuleRequest
from huaweicloudsdklive.v1.model.delete_record_rule_response import DeleteRecordRuleResponse
from huaweicloudsdklive.v1.model.delete_referer_chain_request import DeleteRefererChainRequest
from huaweicloudsdklive.v1.model.delete_referer_chain_response import DeleteRefererChainResponse
from huaweicloudsdklive.v1.model.delete_schedule_record_tasks_request import DeleteScheduleRecordTasksRequest
from huaweicloudsdklive.v1.model.delete_schedule_record_tasks_response import DeleteScheduleRecordTasksResponse
from huaweicloudsdklive.v1.model.delete_snapshot_config_request import DeleteSnapshotConfigRequest
from huaweicloudsdklive.v1.model.delete_snapshot_config_response import DeleteSnapshotConfigResponse
from huaweicloudsdklive.v1.model.delete_stream_forbidden_request import DeleteStreamForbiddenRequest
from huaweicloudsdklive.v1.model.delete_stream_forbidden_response import DeleteStreamForbiddenResponse
from huaweicloudsdklive.v1.model.delete_transcodings_template_request import DeleteTranscodingsTemplateRequest
from huaweicloudsdklive.v1.model.delete_transcodings_template_response import DeleteTranscodingsTemplateResponse
from huaweicloudsdklive.v1.model.domain_https_cert_info import DomainHttpsCertInfo
from huaweicloudsdklive.v1.model.domain_ipv6_switch_req import DomainIpv6SwitchReq
from huaweicloudsdklive.v1.model.domain_mapping import DomainMapping
from huaweicloudsdklive.v1.model.encoder_settings_expand import EncoderSettingsExpand
from huaweicloudsdklive.v1.model.encoder_settings_expand_audio_descriptions import EncoderSettingsExpandAudioDescriptions
from huaweicloudsdklive.v1.model.encryption import Encryption
from huaweicloudsdklive.v1.model.endpoint_item import EndpointItem
from huaweicloudsdklive.v1.model.flv_record_config import FLVRecordConfig
from huaweicloudsdklive.v1.model.failover_conditions import FailoverConditions
from huaweicloudsdklive.v1.model.flow_detail_resp_body import FlowDetailRespBody
from huaweicloudsdklive.v1.model.flow_output import FlowOutput
from huaweicloudsdklive.v1.model.flow_source import FlowSource
from huaweicloudsdklive.v1.model.flow_source_decryption import FlowSourceDecryption
from huaweicloudsdklive.v1.model.geo_blocking_config_info import GeoBlockingConfigInfo
from huaweicloudsdklive.v1.model.gm_certificate_info import GmCertificateInfo
from huaweicloudsdklive.v1.model.hls_record_config import HLSRecordConfig
from huaweicloudsdklive.v1.model.harvest_task_create_suc_rsp import HarvestTaskCreateSucRsp
from huaweicloudsdklive.v1.model.hls_package_item import HlsPackageItem
from huaweicloudsdklive.v1.model.http_header import HttpHeader
from huaweicloudsdklive.v1.model.ip_auth_info import IPAuthInfo
from huaweicloudsdklive.v1.model.input_audio_selector import InputAudioSelector
from huaweicloudsdklive.v1.model.input_stream_info import InputStreamInfo
from huaweicloudsdklive.v1.model.key_chain_info import KeyChainInfo
from huaweicloudsdklive.v1.model.list_delay_config_request import ListDelayConfigRequest
from huaweicloudsdklive.v1.model.list_delay_config_response import ListDelayConfigResponse
from huaweicloudsdklive.v1.model.list_flow_resp_item import ListFlowRespItem
from huaweicloudsdklive.v1.model.list_flows_request import ListFlowsRequest
from huaweicloudsdklive.v1.model.list_flows_response import ListFlowsResponse
from huaweicloudsdklive.v1.model.list_geo_blocking_config_request import ListGeoBlockingConfigRequest
from huaweicloudsdklive.v1.model.list_geo_blocking_config_response import ListGeoBlockingConfigResponse
from huaweicloudsdklive.v1.model.list_harvest_task_request import ListHarvestTaskRequest
from huaweicloudsdklive.v1.model.list_harvest_task_response import ListHarvestTaskResponse
from huaweicloudsdklive.v1.model.list_hls_config_request import ListHlsConfigRequest
from huaweicloudsdklive.v1.model.list_hls_config_response import ListHlsConfigResponse
from huaweicloudsdklive.v1.model.list_ip_auth_list_request import ListIpAuthListRequest
from huaweicloudsdklive.v1.model.list_ip_auth_list_response import ListIpAuthListResponse
from huaweicloudsdklive.v1.model.list_live_sample_logs_request import ListLiveSampleLogsRequest
from huaweicloudsdklive.v1.model.list_live_sample_logs_response import ListLiveSampleLogsResponse
from huaweicloudsdklive.v1.model.list_live_streams_online_request import ListLiveStreamsOnlineRequest
from huaweicloudsdklive.v1.model.list_live_streams_online_response import ListLiveStreamsOnlineResponse
from huaweicloudsdklive.v1.model.list_ott_channel_info_request import ListOttChannelInfoRequest
from huaweicloudsdklive.v1.model.list_ott_channel_info_response import ListOttChannelInfoResponse
from huaweicloudsdklive.v1.model.list_publish_template_request import ListPublishTemplateRequest
from huaweicloudsdklive.v1.model.list_publish_template_response import ListPublishTemplateResponse
from huaweicloudsdklive.v1.model.list_record_callback_configs_request import ListRecordCallbackConfigsRequest
from huaweicloudsdklive.v1.model.list_record_callback_configs_response import ListRecordCallbackConfigsResponse
from huaweicloudsdklive.v1.model.list_record_contents_request import ListRecordContentsRequest
from huaweicloudsdklive.v1.model.list_record_contents_response import ListRecordContentsResponse
from huaweicloudsdklive.v1.model.list_record_rules_request import ListRecordRulesRequest
from huaweicloudsdklive.v1.model.list_record_rules_response import ListRecordRulesResponse
from huaweicloudsdklive.v1.model.list_schedule_record_tasks_request import ListScheduleRecordTasksRequest
from huaweicloudsdklive.v1.model.list_schedule_record_tasks_response import ListScheduleRecordTasksResponse
from huaweicloudsdklive.v1.model.list_snapshot_configs_request import ListSnapshotConfigsRequest
from huaweicloudsdklive.v1.model.list_snapshot_configs_response import ListSnapshotConfigsResponse
from huaweicloudsdklive.v1.model.list_stream_forbidden_request import ListStreamForbiddenRequest
from huaweicloudsdklive.v1.model.list_stream_forbidden_response import ListStreamForbiddenResponse
from huaweicloudsdklive.v1.model.live_domain_create_req import LiveDomainCreateReq
from huaweicloudsdklive.v1.model.live_domain_modify_req import LiveDomainModifyReq
from huaweicloudsdklive.v1.model.live_request_args import LiveRequestArgs
from huaweicloudsdklive.v1.model.live_snapshot_config import LiveSnapshotConfig
from huaweicloudsdklive.v1.model.log_info import LogInfo
from huaweicloudsdklive.v1.model.mp4_record_config import MP4RecordConfig
from huaweicloudsdklive.v1.model.modify_delay_config import ModifyDelayConfig
from huaweicloudsdklive.v1.model.modify_flow_sources_request import ModifyFlowSourcesRequest
from huaweicloudsdklive.v1.model.modify_flow_sources_request_body import ModifyFlowSourcesRequestBody
from huaweicloudsdklive.v1.model.modify_flow_sources_response import ModifyFlowSourcesResponse
from huaweicloudsdklive.v1.model.modify_flow_start_request import ModifyFlowStartRequest
from huaweicloudsdklive.v1.model.modify_flow_start_response import ModifyFlowStartResponse
from huaweicloudsdklive.v1.model.modify_flow_stop_request import ModifyFlowStopRequest
from huaweicloudsdklive.v1.model.modify_flow_stop_response import ModifyFlowStopResponse
from huaweicloudsdklive.v1.model.modify_harvest_task_request import ModifyHarvestTaskRequest
from huaweicloudsdklive.v1.model.modify_harvest_task_request_body import ModifyHarvestTaskRequestBody
from huaweicloudsdklive.v1.model.modify_harvest_task_response import ModifyHarvestTaskResponse
from huaweicloudsdklive.v1.model.modify_hls_config import ModifyHlsConfig
from huaweicloudsdklive.v1.model.modify_ott_channel_encoder_settings import ModifyOttChannelEncoderSettings
from huaweicloudsdklive.v1.model.modify_ott_channel_encoder_settings_encoder_settings import ModifyOttChannelEncoderSettingsEncoderSettings
from huaweicloudsdklive.v1.model.modify_ott_channel_end_points_req import ModifyOttChannelEndPointsReq
from huaweicloudsdklive.v1.model.modify_ott_channel_general import ModifyOttChannelGeneral
from huaweicloudsdklive.v1.model.modify_ott_channel_info_encoder_settings_request import ModifyOttChannelInfoEncoderSettingsRequest
from huaweicloudsdklive.v1.model.modify_ott_channel_info_encoder_settings_response import ModifyOttChannelInfoEncoderSettingsResponse
from huaweicloudsdklive.v1.model.modify_ott_channel_info_end_points_request import ModifyOttChannelInfoEndPointsRequest
from huaweicloudsdklive.v1.model.modify_ott_channel_info_end_points_response import ModifyOttChannelInfoEndPointsResponse
from huaweicloudsdklive.v1.model.modify_ott_channel_info_general_request import ModifyOttChannelInfoGeneralRequest
from huaweicloudsdklive.v1.model.modify_ott_channel_info_general_response import ModifyOttChannelInfoGeneralResponse
from huaweicloudsdklive.v1.model.modify_ott_channel_info_input_request import ModifyOttChannelInfoInputRequest
from huaweicloudsdklive.v1.model.modify_ott_channel_info_input_response import ModifyOttChannelInfoInputResponse
from huaweicloudsdklive.v1.model.modify_ott_channel_info_record_settings_request import ModifyOttChannelInfoRecordSettingsRequest
from huaweicloudsdklive.v1.model.modify_ott_channel_info_record_settings_response import ModifyOttChannelInfoRecordSettingsResponse
from huaweicloudsdklive.v1.model.modify_ott_channel_info_stats_request import ModifyOttChannelInfoStatsRequest
from huaweicloudsdklive.v1.model.modify_ott_channel_info_stats_response import ModifyOttChannelInfoStatsResponse
from huaweicloudsdklive.v1.model.modify_ott_channel_input_req import ModifyOttChannelInputReq
from huaweicloudsdklive.v1.model.modify_ott_channel_record_settings import ModifyOttChannelRecordSettings
from huaweicloudsdklive.v1.model.modify_ott_channel_record_settings_record_settings import ModifyOttChannelRecordSettingsRecordSettings
from huaweicloudsdklive.v1.model.modify_ott_channel_state import ModifyOttChannelState
from huaweicloudsdklive.v1.model.modify_pull_sources_config import ModifyPullSourcesConfig
from huaweicloudsdklive.v1.model.mss_package_item import MssPackageItem
from huaweicloudsdklive.v1.model.obs_authority_config_v2 import ObsAuthorityConfigV2
from huaweicloudsdklive.v1.model.obs_file_addr import ObsFileAddr
from huaweicloudsdklive.v1.model.online_info import OnlineInfo
from huaweicloudsdklive.v1.model.package_request_args import PackageRequestArgs
from huaweicloudsdklive.v1.model.push_domain_application import PushDomainApplication
from huaweicloudsdklive.v1.model.quality_info import QualityInfo
from huaweicloudsdklive.v1.model.record_callback_config import RecordCallbackConfig
from huaweicloudsdklive.v1.model.record_callback_config_request import RecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.record_content_info_v2 import RecordContentInfoV2
from huaweicloudsdklive.v1.model.record_control_info import RecordControlInfo
from huaweicloudsdklive.v1.model.record_index_request_body import RecordIndexRequestBody
from huaweicloudsdklive.v1.model.record_obs_file_addr import RecordObsFileAddr
from huaweicloudsdklive.v1.model.record_request_args import RecordRequestArgs
from huaweicloudsdklive.v1.model.record_rule import RecordRule
from huaweicloudsdklive.v1.model.record_rule_request import RecordRuleRequest
from huaweicloudsdklive.v1.model.run_record_request import RunRecordRequest
from huaweicloudsdklive.v1.model.run_record_response import RunRecordResponse
from huaweicloudsdklive.v1.model.scte35_info_item import SCTE35InfoItem
from huaweicloudsdklive.v1.model.scte35_statistic_req import SCTE35StatisticReq
from huaweicloudsdklive.v1.model.scte35_statistic_rsp import SCTE35StatisticRsp
from huaweicloudsdklive.v1.model.schedule_record_tasks import ScheduleRecordTasks
from huaweicloudsdklive.v1.model.schedule_record_tasks_req import ScheduleRecordTasksReq
from huaweicloudsdklive.v1.model.secondary_sources_info import SecondarySourcesInfo
from huaweicloudsdklive.v1.model.set_referer_chain_info import SetRefererChainInfo
from huaweicloudsdklive.v1.model.set_referer_chain_request import SetRefererChainRequest
from huaweicloudsdklive.v1.model.set_referer_chain_response import SetRefererChainResponse
from huaweicloudsdklive.v1.model.show_channel_statistic_req import ShowChannelStatisticReq
from huaweicloudsdklive.v1.model.show_channel_statistic_request import ShowChannelStatisticRequest
from huaweicloudsdklive.v1.model.show_channel_statistic_response import ShowChannelStatisticResponse
from huaweicloudsdklive.v1.model.show_domain_https_cert_request import ShowDomainHttpsCertRequest
from huaweicloudsdklive.v1.model.show_domain_https_cert_response import ShowDomainHttpsCertResponse
from huaweicloudsdklive.v1.model.show_domain_key_chain_request import ShowDomainKeyChainRequest
from huaweicloudsdklive.v1.model.show_domain_key_chain_response import ShowDomainKeyChainResponse
from huaweicloudsdklive.v1.model.show_domain_request import ShowDomainRequest
from huaweicloudsdklive.v1.model.show_domain_response import ShowDomainResponse
from huaweicloudsdklive.v1.model.show_flow_detail_request import ShowFlowDetailRequest
from huaweicloudsdklive.v1.model.show_flow_detail_response import ShowFlowDetailResponse
from huaweicloudsdklive.v1.model.show_pull_sources_config_request import ShowPullSourcesConfigRequest
from huaweicloudsdklive.v1.model.show_pull_sources_config_response import ShowPullSourcesConfigResponse
from huaweicloudsdklive.v1.model.show_record_callback_config_request import ShowRecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.show_record_callback_config_response import ShowRecordCallbackConfigResponse
from huaweicloudsdklive.v1.model.show_record_rule_request import ShowRecordRuleRequest
from huaweicloudsdklive.v1.model.show_record_rule_response import ShowRecordRuleResponse
from huaweicloudsdklive.v1.model.show_referer_chain_request import ShowRefererChainRequest
from huaweicloudsdklive.v1.model.show_referer_chain_response import ShowRefererChainResponse
from huaweicloudsdklive.v1.model.show_transcodings_template_request import ShowTranscodingsTemplateRequest
from huaweicloudsdklive.v1.model.show_transcodings_template_response import ShowTranscodingsTemplateResponse
from huaweicloudsdklive.v1.model.source_rsp import SourceRsp
from huaweicloudsdklive.v1.model.sources_info import SourcesInfo
from huaweicloudsdklive.v1.model.stream_forbidden_list import StreamForbiddenList
from huaweicloudsdklive.v1.model.stream_forbidden_setting import StreamForbiddenSetting
from huaweicloudsdklive.v1.model.stream_selection_item import StreamSelectionItem
from huaweicloudsdklive.v1.model.stream_transcoding_template import StreamTranscodingTemplate
from huaweicloudsdklive.v1.model.timeshift_request_args import TimeshiftRequestArgs
from huaweicloudsdklive.v1.model.tls_certificate_info import TlsCertificateInfo
from huaweicloudsdklive.v1.model.update_delay_config_request import UpdateDelayConfigRequest
from huaweicloudsdklive.v1.model.update_delay_config_response import UpdateDelayConfigResponse
from huaweicloudsdklive.v1.model.update_domain_https_cert_request import UpdateDomainHttpsCertRequest
from huaweicloudsdklive.v1.model.update_domain_https_cert_response import UpdateDomainHttpsCertResponse
from huaweicloudsdklive.v1.model.update_domain_ip6_switch_request import UpdateDomainIp6SwitchRequest
from huaweicloudsdklive.v1.model.update_domain_ip6_switch_response import UpdateDomainIp6SwitchResponse
from huaweicloudsdklive.v1.model.update_domain_key_chain_request import UpdateDomainKeyChainRequest
from huaweicloudsdklive.v1.model.update_domain_key_chain_response import UpdateDomainKeyChainResponse
from huaweicloudsdklive.v1.model.update_domain_request import UpdateDomainRequest
from huaweicloudsdklive.v1.model.update_domain_response import UpdateDomainResponse
from huaweicloudsdklive.v1.model.update_geo_blocking_config_request import UpdateGeoBlockingConfigRequest
from huaweicloudsdklive.v1.model.update_geo_blocking_config_response import UpdateGeoBlockingConfigResponse
from huaweicloudsdklive.v1.model.update_harvest_job_status_request import UpdateHarvestJobStatusRequest
from huaweicloudsdklive.v1.model.update_harvest_job_status_request_body import UpdateHarvestJobStatusRequestBody
from huaweicloudsdklive.v1.model.update_harvest_job_status_response import UpdateHarvestJobStatusResponse
from huaweicloudsdklive.v1.model.update_hls_config_request import UpdateHlsConfigRequest
from huaweicloudsdklive.v1.model.update_hls_config_response import UpdateHlsConfigResponse
from huaweicloudsdklive.v1.model.update_ip_auth_list_request import UpdateIpAuthListRequest
from huaweicloudsdklive.v1.model.update_ip_auth_list_response import UpdateIpAuthListResponse
from huaweicloudsdklive.v1.model.update_obs_bucket_authority_public_request import UpdateObsBucketAuthorityPublicRequest
from huaweicloudsdklive.v1.model.update_obs_bucket_authority_public_response import UpdateObsBucketAuthorityPublicResponse
from huaweicloudsdklive.v1.model.update_publish_template_request import UpdatePublishTemplateRequest
from huaweicloudsdklive.v1.model.update_publish_template_response import UpdatePublishTemplateResponse
from huaweicloudsdklive.v1.model.update_pull_sources_config_request import UpdatePullSourcesConfigRequest
from huaweicloudsdklive.v1.model.update_pull_sources_config_response import UpdatePullSourcesConfigResponse
from huaweicloudsdklive.v1.model.update_record_callback_config_request import UpdateRecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.update_record_callback_config_response import UpdateRecordCallbackConfigResponse
from huaweicloudsdklive.v1.model.update_record_rule_request import UpdateRecordRuleRequest
from huaweicloudsdklive.v1.model.update_record_rule_response import UpdateRecordRuleResponse
from huaweicloudsdklive.v1.model.update_snapshot_config_request import UpdateSnapshotConfigRequest
from huaweicloudsdklive.v1.model.update_snapshot_config_response import UpdateSnapshotConfigResponse
from huaweicloudsdklive.v1.model.update_stream_forbidden_request import UpdateStreamForbiddenRequest
from huaweicloudsdklive.v1.model.update_stream_forbidden_response import UpdateStreamForbiddenResponse
from huaweicloudsdklive.v1.model.update_transcodings_template_request import UpdateTranscodingsTemplateRequest
from huaweicloudsdklive.v1.model.update_transcodings_template_response import UpdateTranscodingsTemplateResponse
from huaweicloudsdklive.v1.model.video_descriptions import VideoDescriptions
from huaweicloudsdklive.v1.model.video_format_var import VideoFormatVar
from huaweicloudsdklive.v1.model.vod_info_v2 import VodInfoV2
from huaweicloudsdklive.v1.model.vod_package_info import VodPackageInfo

