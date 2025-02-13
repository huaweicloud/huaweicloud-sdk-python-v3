# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkcdn.v2.cdn_client import CdnClient
from huaweicloudsdkcdn.v2.cdn_async_client import CdnAsyncClient

from huaweicloudsdkcdn.v2.model.access_area_filter import AccessAreaFilter
from huaweicloudsdkcdn.v2.model.back_sources import BackSources
from huaweicloudsdkcdn.v2.model.batch_copy_configs import BatchCopyConfigs
from huaweicloudsdkcdn.v2.model.batch_copy_d_request_body import BatchCopyDRequestBody
from huaweicloudsdkcdn.v2.model.batch_copy_domain_request import BatchCopyDomainRequest
from huaweicloudsdkcdn.v2.model.batch_copy_domain_response import BatchCopyDomainResponse
from huaweicloudsdkcdn.v2.model.batch_copy_error_rsp import BatchCopyErrorRsp
from huaweicloudsdkcdn.v2.model.batch_copy_error_rsp_error import BatchCopyErrorRspError
from huaweicloudsdkcdn.v2.model.batch_copy_result_vo import BatchCopyResultVo
from huaweicloudsdkcdn.v2.model.batch_delete_tags_request import BatchDeleteTagsRequest
from huaweicloudsdkcdn.v2.model.batch_delete_tags_response import BatchDeleteTagsResponse
from huaweicloudsdkcdn.v2.model.browser_cache_rules import BrowserCacheRules
from huaweicloudsdkcdn.v2.model.browser_cache_rules_condition import BrowserCacheRulesCondition
from huaweicloudsdkcdn.v2.model.cache_rules import CacheRules
from huaweicloudsdkcdn.v2.model.cache_url_parameter_filter import CacheUrlParameterFilter
from huaweicloudsdkcdn.v2.model.cache_url_parameter_filter_get_body import CacheUrlParameterFilterGetBody
from huaweicloudsdkcdn.v2.model.cdn_ips import CdnIps
from huaweicloudsdkcdn.v2.model.certificates_get_body import CertificatesGetBody
from huaweicloudsdkcdn.v2.model.certificates_put_body import CertificatesPutBody
from huaweicloudsdkcdn.v2.model.client_cert import ClientCert
from huaweicloudsdkcdn.v2.model.common_remote_auth import CommonRemoteAuth
from huaweicloudsdkcdn.v2.model.compress import Compress
from huaweicloudsdkcdn.v2.model.configs import Configs
from huaweicloudsdkcdn.v2.model.configs_get_body import ConfigsGetBody
from huaweicloudsdkcdn.v2.model.create_domain_request import CreateDomainRequest
from huaweicloudsdkcdn.v2.model.create_domain_request_body import CreateDomainRequestBody
from huaweicloudsdkcdn.v2.model.create_domain_response import CreateDomainResponse
from huaweicloudsdkcdn.v2.model.create_domain_response_body_content import CreateDomainResponseBodyContent
from huaweicloudsdkcdn.v2.model.create_preheating_tasks_request import CreatePreheatingTasksRequest
from huaweicloudsdkcdn.v2.model.create_preheating_tasks_response import CreatePreheatingTasksResponse
from huaweicloudsdkcdn.v2.model.create_refresh_tasks_request import CreateRefreshTasksRequest
from huaweicloudsdkcdn.v2.model.create_refresh_tasks_response import CreateRefreshTasksResponse
from huaweicloudsdkcdn.v2.model.create_tags_request import CreateTagsRequest
from huaweicloudsdkcdn.v2.model.create_tags_request_body import CreateTagsRequestBody
from huaweicloudsdkcdn.v2.model.create_tags_response import CreateTagsResponse
from huaweicloudsdkcdn.v2.model.custom_args import CustomArgs
from huaweicloudsdkcdn.v2.model.delete_domain_request import DeleteDomainRequest
from huaweicloudsdkcdn.v2.model.delete_domain_response import DeleteDomainResponse
from huaweicloudsdkcdn.v2.model.delete_tags_request_body import DeleteTagsRequestBody
from huaweicloudsdkcdn.v2.model.disable_domain_request import DisableDomainRequest
from huaweicloudsdkcdn.v2.model.disable_domain_response import DisableDomainResponse
from huaweicloudsdkcdn.v2.model.domain_body import DomainBody
from huaweicloudsdkcdn.v2.model.domain_origin_host import DomainOriginHost
from huaweicloudsdkcdn.v2.model.domains import Domains
from huaweicloudsdkcdn.v2.model.domains_detail import DomainsDetail
from huaweicloudsdkcdn.v2.model.domains_with_port import DomainsWithPort
from huaweicloudsdkcdn.v2.model.download_region_carrier_excel_request import DownloadRegionCarrierExcelRequest
from huaweicloudsdkcdn.v2.model.download_region_carrier_excel_response import DownloadRegionCarrierExcelResponse
from huaweicloudsdkcdn.v2.model.download_statistics_excel_request import DownloadStatisticsExcelRequest
from huaweicloudsdkcdn.v2.model.download_statistics_excel_response import DownloadStatisticsExcelResponse
from huaweicloudsdkcdn.v2.model.enable_domain_request import EnableDomainRequest
from huaweicloudsdkcdn.v2.model.enable_domain_response import EnableDomainResponse
from huaweicloudsdkcdn.v2.model.ep_resource_tag import EpResourceTag
from huaweicloudsdkcdn.v2.model.err_msg import ErrMsg
from huaweicloudsdkcdn.v2.model.err_rsp import ErrRsp
from huaweicloudsdkcdn.v2.model.error_code_cache import ErrorCodeCache
from huaweicloudsdkcdn.v2.model.error_code_redirect_rules import ErrorCodeRedirectRules
from huaweicloudsdkcdn.v2.model.flexible_origins import FlexibleOrigins
from huaweicloudsdkcdn.v2.model.force_redirect import ForceRedirect
from huaweicloudsdkcdn.v2.model.force_redirect_config import ForceRedirectConfig
from huaweicloudsdkcdn.v2.model.hsts import Hsts
from huaweicloudsdkcdn.v2.model.hsts_query import HstsQuery
from huaweicloudsdkcdn.v2.model.http_get_body import HttpGetBody
from huaweicloudsdkcdn.v2.model.http_put_body import HttpPutBody
from huaweicloudsdkcdn.v2.model.http_response_header import HttpResponseHeader
from huaweicloudsdkcdn.v2.model.https_detail import HttpsDetail
from huaweicloudsdkcdn.v2.model.inherit_config import InheritConfig
from huaweicloudsdkcdn.v2.model.inherit_config_query import InheritConfigQuery
from huaweicloudsdkcdn.v2.model.ip_filter import IpFilter
from huaweicloudsdkcdn.v2.model.ip_frequency_limit import IpFrequencyLimit
from huaweicloudsdkcdn.v2.model.ip_frequency_limit_query import IpFrequencyLimitQuery
from huaweicloudsdkcdn.v2.model.list_cdn_domain_top_refers_request import ListCdnDomainTopRefersRequest
from huaweicloudsdkcdn.v2.model.list_cdn_domain_top_refers_response import ListCdnDomainTopRefersResponse
from huaweicloudsdkcdn.v2.model.list_domains_request import ListDomainsRequest
from huaweicloudsdkcdn.v2.model.list_domains_response import ListDomainsResponse
from huaweicloudsdkcdn.v2.model.log_object import LogObject
from huaweicloudsdkcdn.v2.model.modify_domain_config_request_body import ModifyDomainConfigRequestBody
from huaweicloudsdkcdn.v2.model.origin_request_header import OriginRequestHeader
from huaweicloudsdkcdn.v2.model.origin_request_url_rewrite import OriginRequestUrlRewrite
from huaweicloudsdkcdn.v2.model.preheating_task_request import PreheatingTaskRequest
from huaweicloudsdkcdn.v2.model.preheating_task_request_body import PreheatingTaskRequestBody
from huaweicloudsdkcdn.v2.model.quic import Quic
from huaweicloudsdkcdn.v2.model.quotas import Quotas
from huaweicloudsdkcdn.v2.model.referer_config import RefererConfig
from huaweicloudsdkcdn.v2.model.refresh_task_request import RefreshTaskRequest
from huaweicloudsdkcdn.v2.model.refresh_task_request_body import RefreshTaskRequestBody
from huaweicloudsdkcdn.v2.model.remote_auth_rule import RemoteAuthRule
from huaweicloudsdkcdn.v2.model.request_limit_rules import RequestLimitRules
from huaweicloudsdkcdn.v2.model.request_url_rewrite import RequestUrlRewrite
from huaweicloudsdkcdn.v2.model.set_charge_modes_body import SetChargeModesBody
from huaweicloudsdkcdn.v2.model.set_charge_modes_request import SetChargeModesRequest
from huaweicloudsdkcdn.v2.model.set_charge_modes_response import SetChargeModesResponse
from huaweicloudsdkcdn.v2.model.show_bandwidth_calc_request import ShowBandwidthCalcRequest
from huaweicloudsdkcdn.v2.model.show_bandwidth_calc_response import ShowBandwidthCalcResponse
from huaweicloudsdkcdn.v2.model.show_certificates_https_info_request import ShowCertificatesHttpsInfoRequest
from huaweicloudsdkcdn.v2.model.show_certificates_https_info_response import ShowCertificatesHttpsInfoResponse
from huaweicloudsdkcdn.v2.model.show_charge_modes_request import ShowChargeModesRequest
from huaweicloudsdkcdn.v2.model.show_charge_modes_response import ShowChargeModesResponse
from huaweicloudsdkcdn.v2.model.show_domain_detail_by_name_request import ShowDomainDetailByNameRequest
from huaweicloudsdkcdn.v2.model.show_domain_detail_by_name_response import ShowDomainDetailByNameResponse
from huaweicloudsdkcdn.v2.model.show_domain_full_config_request import ShowDomainFullConfigRequest
from huaweicloudsdkcdn.v2.model.show_domain_full_config_response import ShowDomainFullConfigResponse
from huaweicloudsdkcdn.v2.model.show_domain_location_stats_request import ShowDomainLocationStatsRequest
from huaweicloudsdkcdn.v2.model.show_domain_location_stats_response import ShowDomainLocationStatsResponse
from huaweicloudsdkcdn.v2.model.show_domain_stats_request import ShowDomainStatsRequest
from huaweicloudsdkcdn.v2.model.show_domain_stats_response import ShowDomainStatsResponse
from huaweicloudsdkcdn.v2.model.show_history_task_details_request import ShowHistoryTaskDetailsRequest
from huaweicloudsdkcdn.v2.model.show_history_task_details_response import ShowHistoryTaskDetailsResponse
from huaweicloudsdkcdn.v2.model.show_history_tasks_request import ShowHistoryTasksRequest
from huaweicloudsdkcdn.v2.model.show_history_tasks_response import ShowHistoryTasksResponse
from huaweicloudsdkcdn.v2.model.show_ip_info_request import ShowIpInfoRequest
from huaweicloudsdkcdn.v2.model.show_ip_info_response import ShowIpInfoResponse
from huaweicloudsdkcdn.v2.model.show_logs_request import ShowLogsRequest
from huaweicloudsdkcdn.v2.model.show_logs_response import ShowLogsResponse
from huaweicloudsdkcdn.v2.model.show_quota_request import ShowQuotaRequest
from huaweicloudsdkcdn.v2.model.show_quota_response import ShowQuotaResponse
from huaweicloudsdkcdn.v2.model.show_tags_request import ShowTagsRequest
from huaweicloudsdkcdn.v2.model.show_tags_response import ShowTagsResponse
from huaweicloudsdkcdn.v2.model.show_top_domain_names_request import ShowTopDomainNamesRequest
from huaweicloudsdkcdn.v2.model.show_top_domain_names_response import ShowTopDomainNamesResponse
from huaweicloudsdkcdn.v2.model.show_top_url_request import ShowTopUrlRequest
from huaweicloudsdkcdn.v2.model.show_top_url_response import ShowTopUrlResponse
from huaweicloudsdkcdn.v2.model.show_url_task_info_request import ShowUrlTaskInfoRequest
from huaweicloudsdkcdn.v2.model.show_url_task_info_response import ShowUrlTaskInfoResponse
from huaweicloudsdkcdn.v2.model.show_verify_domain_owner_info_request import ShowVerifyDomainOwnerInfoRequest
from huaweicloudsdkcdn.v2.model.show_verify_domain_owner_info_response import ShowVerifyDomainOwnerInfoResponse
from huaweicloudsdkcdn.v2.model.sni import Sni
from huaweicloudsdkcdn.v2.model.source_with_port import SourceWithPort
from huaweicloudsdkcdn.v2.model.sources import Sources
from huaweicloudsdkcdn.v2.model.sources_config import SourcesConfig
from huaweicloudsdkcdn.v2.model.sources_config_response_body import SourcesConfigResponseBody
from huaweicloudsdkcdn.v2.model.sources_domain_config import SourcesDomainConfig
from huaweicloudsdkcdn.v2.model.sources_request_body import SourcesRequestBody
from huaweicloudsdkcdn.v2.model.tag_map import TagMap
from huaweicloudsdkcdn.v2.model.tasks_object import TasksObject
from huaweicloudsdkcdn.v2.model.top_refer_summary import TopReferSummary
from huaweicloudsdkcdn.v2.model.top_url_summary import TopUrlSummary
from huaweicloudsdkcdn.v2.model.update_domain_full_config_request import UpdateDomainFullConfigRequest
from huaweicloudsdkcdn.v2.model.update_domain_full_config_response import UpdateDomainFullConfigResponse
from huaweicloudsdkcdn.v2.model.update_domain_multi_certificates_request import UpdateDomainMultiCertificatesRequest
from huaweicloudsdkcdn.v2.model.update_domain_multi_certificates_request_body import UpdateDomainMultiCertificatesRequestBody
from huaweicloudsdkcdn.v2.model.update_domain_multi_certificates_request_body_content import UpdateDomainMultiCertificatesRequestBodyContent
from huaweicloudsdkcdn.v2.model.update_domain_multi_certificates_response import UpdateDomainMultiCertificatesResponse
from huaweicloudsdkcdn.v2.model.update_domain_multi_certificates_response_body_content import UpdateDomainMultiCertificatesResponseBodyContent
from huaweicloudsdkcdn.v2.model.update_private_bucket_access_body import UpdatePrivateBucketAccessBody
from huaweicloudsdkcdn.v2.model.update_private_bucket_access_request import UpdatePrivateBucketAccessRequest
from huaweicloudsdkcdn.v2.model.update_private_bucket_access_response import UpdatePrivateBucketAccessResponse
from huaweicloudsdkcdn.v2.model.url_auth import UrlAuth
from huaweicloudsdkcdn.v2.model.url_auth_get_body import UrlAuthGetBody
from huaweicloudsdkcdn.v2.model.url_object import UrlObject
from huaweicloudsdkcdn.v2.model.url_rewrite_condition import UrlRewriteCondition
from huaweicloudsdkcdn.v2.model.urls import Urls
from huaweicloudsdkcdn.v2.model.user_agent_filter import UserAgentFilter
from huaweicloudsdkcdn.v2.model.verify_domain_owner_request import VerifyDomainOwnerRequest
from huaweicloudsdkcdn.v2.model.verify_domain_owner_request_body import VerifyDomainOwnerRequestBody
from huaweicloudsdkcdn.v2.model.verify_domain_owner_response import VerifyDomainOwnerResponse
from huaweicloudsdkcdn.v2.model.video_seek import VideoSeek
from huaweicloudsdkcdn.v2.model.web_socket_seek import WebSocketSeek

