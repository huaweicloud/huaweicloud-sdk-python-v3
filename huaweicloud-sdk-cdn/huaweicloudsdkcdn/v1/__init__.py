# coding: utf-8

from __future__ import absolute_import

# import CdnClient
from huaweicloudsdkcdn.v1.cdn_client import CdnClient
from huaweicloudsdkcdn.v1.cdn_async_client import CdnAsyncClient
# import models into sdk package
from huaweicloudsdkcdn.v1.model.black_white_list_body import BlackWhiteListBody
from huaweicloudsdkcdn.v1.model.cache_config import CacheConfig
from huaweicloudsdkcdn.v1.model.cache_config_request import CacheConfigRequest
from huaweicloudsdkcdn.v1.model.cache_config_request_body import CacheConfigRequestBody
from huaweicloudsdkcdn.v1.model.cdn_ips import CdnIps
from huaweicloudsdkcdn.v1.model.compress_request import CompressRequest
from huaweicloudsdkcdn.v1.model.compress_response import CompressResponse
from huaweicloudsdkcdn.v1.model.compress_rules import CompressRules
from huaweicloudsdkcdn.v1.model.create_domain_request import CreateDomainRequest
from huaweicloudsdkcdn.v1.model.create_domain_request_body import CreateDomainRequestBody
from huaweicloudsdkcdn.v1.model.create_domain_response import CreateDomainResponse
from huaweicloudsdkcdn.v1.model.create_domain_response_body_content import CreateDomainResponseBodyContent
from huaweicloudsdkcdn.v1.model.create_preheating_tasks_request import CreatePreheatingTasksRequest
from huaweicloudsdkcdn.v1.model.create_preheating_tasks_response import CreatePreheatingTasksResponse
from huaweicloudsdkcdn.v1.model.create_refresh_tasks_request import CreateRefreshTasksRequest
from huaweicloudsdkcdn.v1.model.create_refresh_tasks_response import CreateRefreshTasksResponse
from huaweicloudsdkcdn.v1.model.delete_domain_request import DeleteDomainRequest
from huaweicloudsdkcdn.v1.model.delete_domain_response import DeleteDomainResponse
from huaweicloudsdkcdn.v1.model.disable_domain_request import DisableDomainRequest
from huaweicloudsdkcdn.v1.model.disable_domain_response import DisableDomainResponse
from huaweicloudsdkcdn.v1.model.domain_body import DomainBody
from huaweicloudsdkcdn.v1.model.domain_item_detail import DomainItemDetail
from huaweicloudsdkcdn.v1.model.domain_item_location_details import DomainItemLocationDetails
from huaweicloudsdkcdn.v1.model.domain_object import DomainObject
from huaweicloudsdkcdn.v1.model.domain_origin_host import DomainOriginHost
from huaweicloudsdkcdn.v1.model.domain_region import DomainRegion
from huaweicloudsdkcdn.v1.model.domain_region_isp_detail import DomainRegionIspDetail
from huaweicloudsdkcdn.v1.model.domains import Domains
from huaweicloudsdkcdn.v1.model.enable_domain_request import EnableDomainRequest
from huaweicloudsdkcdn.v1.model.enable_domain_response import EnableDomainResponse
from huaweicloudsdkcdn.v1.model.follow302_status_body import Follow302StatusBody
from huaweicloudsdkcdn.v1.model.follow302_status_request import Follow302StatusRequest
from huaweicloudsdkcdn.v1.model.force_redirect import ForceRedirect
from huaweicloudsdkcdn.v1.model.header_body import HeaderBody
from huaweicloudsdkcdn.v1.model.header_map import HeaderMap
from huaweicloudsdkcdn.v1.model.http_info_request import HttpInfoRequest
from huaweicloudsdkcdn.v1.model.http_info_request_body import HttpInfoRequestBody
from huaweicloudsdkcdn.v1.model.http_info_response_body import HttpInfoResponseBody
from huaweicloudsdkcdn.v1.model.https_detail import HttpsDetail
from huaweicloudsdkcdn.v1.model.list_domains_request import ListDomainsRequest
from huaweicloudsdkcdn.v1.model.list_domains_response import ListDomainsResponse
from huaweicloudsdkcdn.v1.model.log_object import LogObject
from huaweicloudsdkcdn.v1.model.origin_host_body import OriginHostBody
from huaweicloudsdkcdn.v1.model.origin_host_request import OriginHostRequest
from huaweicloudsdkcdn.v1.model.origin_range_body import OriginRangeBody
from huaweicloudsdkcdn.v1.model.origin_request import OriginRequest
from huaweicloudsdkcdn.v1.model.preheating_task_request import PreheatingTaskRequest
from huaweicloudsdkcdn.v1.model.preheating_task_request_preheating_task import PreheatingTaskRequestPreheatingTask
from huaweicloudsdkcdn.v1.model.range_status_request import RangeStatusRequest
from huaweicloudsdkcdn.v1.model.referer import Referer
from huaweicloudsdkcdn.v1.model.referer_body import RefererBody
from huaweicloudsdkcdn.v1.model.referer_rsp import RefererRsp
from huaweicloudsdkcdn.v1.model.refresh_task_request import RefreshTaskRequest
from huaweicloudsdkcdn.v1.model.refresh_task_request_refresh_task import RefreshTaskRequestRefreshTask
from huaweicloudsdkcdn.v1.model.resource_body import ResourceBody
from huaweicloudsdkcdn.v1.model.rules import Rules
from huaweicloudsdkcdn.v1.model.show_black_white_list_request import ShowBlackWhiteListRequest
from huaweicloudsdkcdn.v1.model.show_black_white_list_response import ShowBlackWhiteListResponse
from huaweicloudsdkcdn.v1.model.show_cache_rules_request import ShowCacheRulesRequest
from huaweicloudsdkcdn.v1.model.show_cache_rules_response import ShowCacheRulesResponse
from huaweicloudsdkcdn.v1.model.show_certificates_https_info_request import ShowCertificatesHttpsInfoRequest
from huaweicloudsdkcdn.v1.model.show_certificates_https_info_response import ShowCertificatesHttpsInfoResponse
from huaweicloudsdkcdn.v1.model.show_domain_detail_request import ShowDomainDetailRequest
from huaweicloudsdkcdn.v1.model.show_domain_detail_response import ShowDomainDetailResponse
from huaweicloudsdkcdn.v1.model.show_domain_item_details_request import ShowDomainItemDetailsRequest
from huaweicloudsdkcdn.v1.model.show_domain_item_details_response import ShowDomainItemDetailsResponse
from huaweicloudsdkcdn.v1.model.show_domain_item_location_details_request import ShowDomainItemLocationDetailsRequest
from huaweicloudsdkcdn.v1.model.show_domain_item_location_details_response import ShowDomainItemLocationDetailsResponse
from huaweicloudsdkcdn.v1.model.show_history_task_details_request import ShowHistoryTaskDetailsRequest
from huaweicloudsdkcdn.v1.model.show_history_task_details_response import ShowHistoryTaskDetailsResponse
from huaweicloudsdkcdn.v1.model.show_history_tasks_request import ShowHistoryTasksRequest
from huaweicloudsdkcdn.v1.model.show_history_tasks_response import ShowHistoryTasksResponse
from huaweicloudsdkcdn.v1.model.show_http_info_request import ShowHttpInfoRequest
from huaweicloudsdkcdn.v1.model.show_http_info_response import ShowHttpInfoResponse
from huaweicloudsdkcdn.v1.model.show_ip_info_request import ShowIpInfoRequest
from huaweicloudsdkcdn.v1.model.show_ip_info_response import ShowIpInfoResponse
from huaweicloudsdkcdn.v1.model.show_logs_request import ShowLogsRequest
from huaweicloudsdkcdn.v1.model.show_logs_response import ShowLogsResponse
from huaweicloudsdkcdn.v1.model.show_origin_host_request import ShowOriginHostRequest
from huaweicloudsdkcdn.v1.model.show_origin_host_response import ShowOriginHostResponse
from huaweicloudsdkcdn.v1.model.show_quota_request import ShowQuotaRequest
from huaweicloudsdkcdn.v1.model.show_quota_response import ShowQuotaResponse
from huaweicloudsdkcdn.v1.model.show_quota_response_body_quotas import ShowQuotaResponseBodyQuotas
from huaweicloudsdkcdn.v1.model.show_refer_request import ShowReferRequest
from huaweicloudsdkcdn.v1.model.show_refer_response import ShowReferResponse
from huaweicloudsdkcdn.v1.model.show_response_header_request import ShowResponseHeaderRequest
from huaweicloudsdkcdn.v1.model.show_response_header_response import ShowResponseHeaderResponse
from huaweicloudsdkcdn.v1.model.show_top_url_request import ShowTopUrlRequest
from huaweicloudsdkcdn.v1.model.show_top_url_response import ShowTopUrlResponse
from huaweicloudsdkcdn.v1.model.source_with_port import SourceWithPort
from huaweicloudsdkcdn.v1.model.sources import Sources
from huaweicloudsdkcdn.v1.model.tasks_object import TasksObject
from huaweicloudsdkcdn.v1.model.top_url_summary import TopUrlSummary
from huaweicloudsdkcdn.v1.model.update_black_white_list_request import UpdateBlackWhiteListRequest
from huaweicloudsdkcdn.v1.model.update_black_white_list_response import UpdateBlackWhiteListResponse
from huaweicloudsdkcdn.v1.model.update_cache_rules_request import UpdateCacheRulesRequest
from huaweicloudsdkcdn.v1.model.update_cache_rules_response import UpdateCacheRulesResponse
from huaweicloudsdkcdn.v1.model.update_domain_multi_certificates_request import UpdateDomainMultiCertificatesRequest
from huaweicloudsdkcdn.v1.model.update_domain_multi_certificates_request_body import UpdateDomainMultiCertificatesRequestBody
from huaweicloudsdkcdn.v1.model.update_domain_multi_certificates_request_body_content import UpdateDomainMultiCertificatesRequestBodyContent
from huaweicloudsdkcdn.v1.model.update_domain_multi_certificates_response import UpdateDomainMultiCertificatesResponse
from huaweicloudsdkcdn.v1.model.update_domain_multi_certificates_response_body_content import UpdateDomainMultiCertificatesResponseBodyContent
from huaweicloudsdkcdn.v1.model.update_domain_origin_request import UpdateDomainOriginRequest
from huaweicloudsdkcdn.v1.model.update_domain_origin_response import UpdateDomainOriginResponse
from huaweicloudsdkcdn.v1.model.update_follow302_switch_request import UpdateFollow302SwitchRequest
from huaweicloudsdkcdn.v1.model.update_follow302_switch_response import UpdateFollow302SwitchResponse
from huaweicloudsdkcdn.v1.model.update_https_info_request import UpdateHttpsInfoRequest
from huaweicloudsdkcdn.v1.model.update_https_info_response import UpdateHttpsInfoResponse
from huaweicloudsdkcdn.v1.model.update_origin_host_request import UpdateOriginHostRequest
from huaweicloudsdkcdn.v1.model.update_origin_host_response import UpdateOriginHostResponse
from huaweicloudsdkcdn.v1.model.update_private_bucket_access_body import UpdatePrivateBucketAccessBody
from huaweicloudsdkcdn.v1.model.update_private_bucket_access_request import UpdatePrivateBucketAccessRequest
from huaweicloudsdkcdn.v1.model.update_private_bucket_access_response import UpdatePrivateBucketAccessResponse
from huaweicloudsdkcdn.v1.model.update_range_switch_request import UpdateRangeSwitchRequest
from huaweicloudsdkcdn.v1.model.update_range_switch_response import UpdateRangeSwitchResponse
from huaweicloudsdkcdn.v1.model.update_refer_request import UpdateReferRequest
from huaweicloudsdkcdn.v1.model.update_refer_response import UpdateReferResponse
from huaweicloudsdkcdn.v1.model.update_response_header_request import UpdateResponseHeaderRequest
from huaweicloudsdkcdn.v1.model.update_response_header_response import UpdateResponseHeaderResponse
from huaweicloudsdkcdn.v1.model.url_object import UrlObject
