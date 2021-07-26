# coding: utf-8

from __future__ import absolute_import

# import LiveClient
from huaweicloudsdklive.v1.live_client import LiveClient
from huaweicloudsdklive.v1.live_async_client import LiveAsyncClient
# import models into sdk package
from huaweicloudsdklive.v1.model.app_quality_info import AppQualityInfo
from huaweicloudsdklive.v1.model.create_domain_mapping_request import CreateDomainMappingRequest
from huaweicloudsdklive.v1.model.create_domain_mapping_response import CreateDomainMappingResponse
from huaweicloudsdklive.v1.model.create_domain_request import CreateDomainRequest
from huaweicloudsdklive.v1.model.create_domain_response import CreateDomainResponse
from huaweicloudsdklive.v1.model.create_record_callback_config_request import CreateRecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.create_record_callback_config_response import CreateRecordCallbackConfigResponse
from huaweicloudsdklive.v1.model.create_record_rule_request import CreateRecordRuleRequest
from huaweicloudsdklive.v1.model.create_record_rule_response import CreateRecordRuleResponse
from huaweicloudsdklive.v1.model.create_stream_forbidden_request import CreateStreamForbiddenRequest
from huaweicloudsdklive.v1.model.create_stream_forbidden_response import CreateStreamForbiddenResponse
from huaweicloudsdklive.v1.model.create_transcodings_template_request import CreateTranscodingsTemplateRequest
from huaweicloudsdklive.v1.model.create_transcodings_template_response import CreateTranscodingsTemplateResponse
from huaweicloudsdklive.v1.model.decoupled_live_domain_info import DecoupledLiveDomainInfo
from huaweicloudsdklive.v1.model.default_record_config import DefaultRecordConfig
from huaweicloudsdklive.v1.model.delete_domain_mapping_request import DeleteDomainMappingRequest
from huaweicloudsdklive.v1.model.delete_domain_mapping_response import DeleteDomainMappingResponse
from huaweicloudsdklive.v1.model.delete_domain_request import DeleteDomainRequest
from huaweicloudsdklive.v1.model.delete_domain_response import DeleteDomainResponse
from huaweicloudsdklive.v1.model.delete_record_callback_config_request import DeleteRecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.delete_record_callback_config_response import DeleteRecordCallbackConfigResponse
from huaweicloudsdklive.v1.model.delete_record_rule_request import DeleteRecordRuleRequest
from huaweicloudsdklive.v1.model.delete_record_rule_response import DeleteRecordRuleResponse
from huaweicloudsdklive.v1.model.delete_stream_forbidden_request import DeleteStreamForbiddenRequest
from huaweicloudsdklive.v1.model.delete_stream_forbidden_response import DeleteStreamForbiddenResponse
from huaweicloudsdklive.v1.model.delete_transcodings_template_request import DeleteTranscodingsTemplateRequest
from huaweicloudsdklive.v1.model.delete_transcodings_template_response import DeleteTranscodingsTemplateResponse
from huaweicloudsdklive.v1.model.domain_mapping import DomainMapping
from huaweicloudsdklive.v1.model.flv_record_config import FLVRecordConfig
from huaweicloudsdklive.v1.model.hls_record_config import HLSRecordConfig
from huaweicloudsdklive.v1.model.list_live_sample_logs_request import ListLiveSampleLogsRequest
from huaweicloudsdklive.v1.model.list_live_sample_logs_response import ListLiveSampleLogsResponse
from huaweicloudsdklive.v1.model.list_live_streams_online_request import ListLiveStreamsOnlineRequest
from huaweicloudsdklive.v1.model.list_live_streams_online_response import ListLiveStreamsOnlineResponse
from huaweicloudsdklive.v1.model.list_record_callback_configs_request import ListRecordCallbackConfigsRequest
from huaweicloudsdklive.v1.model.list_record_callback_configs_response import ListRecordCallbackConfigsResponse
from huaweicloudsdklive.v1.model.list_record_rules_request import ListRecordRulesRequest
from huaweicloudsdklive.v1.model.list_record_rules_response import ListRecordRulesResponse
from huaweicloudsdklive.v1.model.list_stream_forbidden_request import ListStreamForbiddenRequest
from huaweicloudsdklive.v1.model.list_stream_forbidden_response import ListStreamForbiddenResponse
from huaweicloudsdklive.v1.model.live_domain_create_req import LiveDomainCreateReq
from huaweicloudsdklive.v1.model.live_domain_modify_req import LiveDomainModifyReq
from huaweicloudsdklive.v1.model.log_info import LogInfo
from huaweicloudsdklive.v1.model.mp4_record_config import MP4RecordConfig
from huaweicloudsdklive.v1.model.online_info import OnlineInfo
from huaweicloudsdklive.v1.model.plan_record_time import PlanRecordTime
from huaweicloudsdklive.v1.model.quality_info import QualityInfo
from huaweicloudsdklive.v1.model.record_callback_config import RecordCallbackConfig
from huaweicloudsdklive.v1.model.record_callback_config_request import RecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.record_obs_file_addr import RecordObsFileAddr
from huaweicloudsdklive.v1.model.record_rule import RecordRule
from huaweicloudsdklive.v1.model.record_rule_request import RecordRuleRequest
from huaweicloudsdklive.v1.model.show_domain_request import ShowDomainRequest
from huaweicloudsdklive.v1.model.show_domain_response import ShowDomainResponse
from huaweicloudsdklive.v1.model.show_record_callback_config_request import ShowRecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.show_record_callback_config_response import ShowRecordCallbackConfigResponse
from huaweicloudsdklive.v1.model.show_record_rule_request import ShowRecordRuleRequest
from huaweicloudsdklive.v1.model.show_record_rule_response import ShowRecordRuleResponse
from huaweicloudsdklive.v1.model.show_transcodings_template_request import ShowTranscodingsTemplateRequest
from huaweicloudsdklive.v1.model.show_transcodings_template_response import ShowTranscodingsTemplateResponse
from huaweicloudsdklive.v1.model.stream_forbidden_list import StreamForbiddenList
from huaweicloudsdklive.v1.model.stream_forbidden_setting import StreamForbiddenSetting
from huaweicloudsdklive.v1.model.stream_transcoding_template import StreamTranscodingTemplate
from huaweicloudsdklive.v1.model.update_domain_request import UpdateDomainRequest
from huaweicloudsdklive.v1.model.update_domain_response import UpdateDomainResponse
from huaweicloudsdklive.v1.model.update_record_callback_config_request import UpdateRecordCallbackConfigRequest
from huaweicloudsdklive.v1.model.update_record_callback_config_response import UpdateRecordCallbackConfigResponse
from huaweicloudsdklive.v1.model.update_record_rule_request import UpdateRecordRuleRequest
from huaweicloudsdklive.v1.model.update_record_rule_response import UpdateRecordRuleResponse
from huaweicloudsdklive.v1.model.update_stream_forbidden_request import UpdateStreamForbiddenRequest
from huaweicloudsdklive.v1.model.update_stream_forbidden_response import UpdateStreamForbiddenResponse
from huaweicloudsdklive.v1.model.update_transcodings_template_request import UpdateTranscodingsTemplateRequest
from huaweicloudsdklive.v1.model.update_transcodings_template_response import UpdateTranscodingsTemplateResponse
from huaweicloudsdklive.v1.model.video_format_var import VideoFormatVar

