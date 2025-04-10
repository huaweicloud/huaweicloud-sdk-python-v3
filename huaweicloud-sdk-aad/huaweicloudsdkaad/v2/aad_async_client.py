# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaad'")


class AadAsyncClient(Client):
    def __init__(self):
        super(AadAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaad.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "AadAsyncClient":
                raise TypeError("client type error, support client type is AadAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def add_waf_white_ip_rule_async(self, request):
        r"""防护策略web-cc黑白名单-创建黑白名单规则

        防护策略web-cc黑白名单-创建黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddWafWhiteIpRule
        :type request: :class:`huaweicloudsdkaad.v2.AddWafWhiteIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.AddWafWhiteIpRuleResponse`
        """
        http_info = self._add_waf_white_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def add_waf_white_ip_rule_async_invoker(self, request):
        http_info = self._add_waf_white_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_waf_white_ip_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/aad/policies/waf/blackwhite-list",
            "request_type": request.__class__.__name__,
            "response_type": "AddWafWhiteIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_domain_async(self, request):
        r"""创建防护域名

        创建防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDomain
        :type request: :class:`huaweicloudsdkaad.v2.CreateDomainRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.CreateDomainResponse`
        """
        http_info = self._create_domain_http_info(request)
        return self._call_api(**http_info)

    def create_domain_async_invoker(self, request):
        http_info = self._create_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_domain_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/aad/domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_domain_async(self, request):
        r"""删除防护域名

        删除防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomain
        :type request: :class:`huaweicloudsdkaad.v2.DeleteDomainRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.DeleteDomainResponse`
        """
        http_info = self._delete_domain_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_async_invoker(self, request):
        http_info = self._delete_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/aad/domains",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_waf_white_ip_rule_async(self, request):
        r"""防护策略web-cc黑白名单-删除黑白名单规则

        防护策略web-cc黑白名单-删除黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWafWhiteIpRule
        :type request: :class:`huaweicloudsdkaad.v2.DeleteWafWhiteIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.DeleteWafWhiteIpRuleResponse`
        """
        http_info = self._delete_waf_white_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_waf_white_ip_rule_async_invoker(self, request):
        http_info = self._delete_waf_white_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_waf_white_ip_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/aad/policies/waf/blackwhite-list",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWafWhiteIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_d_do_s_attack_event_async(self, request):
        r"""查询DDoS攻击事件列表

        查询DDoS攻击事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDDoSAttackEvent
        :type request: :class:`huaweicloudsdkaad.v2.ListDDoSAttackEventRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListDDoSAttackEventResponse`
        """
        http_info = self._list_d_do_s_attack_event_http_info(request)
        return self._call_api(**http_info)

    def list_d_do_s_attack_event_async_invoker(self, request):
        http_info = self._list_d_do_s_attack_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_d_do_s_attack_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/aad/instances/{instance_id}/ddos-info/attack/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListDDoSAttackEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_d_do_s_connection_number_async(self, request):
        r"""查询新建连接数和并发连接数

        查询新建连接数和并发连接数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDDoSConnectionNumber
        :type request: :class:`huaweicloudsdkaad.v2.ListDDoSConnectionNumberRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListDDoSConnectionNumberResponse`
        """
        http_info = self._list_d_do_s_connection_number_http_info(request)
        return self._call_api(**http_info)

    def list_d_do_s_connection_number_async_invoker(self, request):
        http_info = self._list_d_do_s_connection_number_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_d_do_s_connection_number_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/instances/{instance_id}/ddos-info/flow/connection-numbers",
            "request_type": request.__class__.__name__,
            "response_type": "ListDDoSConnectionNumberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_d_do_s_flow_async(self, request):
        r"""查询DDoS攻击防护BPS/PPS流量

        查询DDoS攻击防护BPS/PPS流量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDDoSFlow
        :type request: :class:`huaweicloudsdkaad.v2.ListDDoSFlowRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListDDoSFlowResponse`
        """
        http_info = self._list_d_do_s_flow_http_info(request)
        return self._call_api(**http_info)

    def list_d_do_s_flow_async_invoker(self, request):
        http_info = self._list_d_do_s_flow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_d_do_s_flow_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/instances/{instance_id}/ddos-info/flow",
            "request_type": request.__class__.__name__,
            "response_type": "ListDDoSFlowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_frequency_control_rule_async(self, request):
        r"""查询频率控制规则列表

        查询频率控制规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFrequencyControlRule
        :type request: :class:`huaweicloudsdkaad.v2.ListFrequencyControlRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListFrequencyControlRuleResponse`
        """
        http_info = self._list_frequency_control_rule_http_info(request)
        return self._call_api(**http_info)

    def list_frequency_control_rule_async_invoker(self, request):
        http_info = self._list_frequency_control_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_frequency_control_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/policies/waf/frequency-control-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListFrequencyControlRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_domains_async(self, request):
        r"""查询实例关联的域名信息

        查询实例关联的域名信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceDomains
        :type request: :class:`huaweicloudsdkaad.v2.ListInstanceDomainsRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListInstanceDomainsResponse`
        """
        http_info = self._list_instance_domains_http_info(request)
        return self._call_api(**http_info)

    def list_instance_domains_async_invoker(self, request):
        http_info = self._list_instance_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/instances/{instance_id}/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_waf_attack_event_async(self, request):
        r"""查询攻击事件列表

        查询攻击事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWafAttackEvent
        :type request: :class:`huaweicloudsdkaad.v2.ListWafAttackEventRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListWafAttackEventResponse`
        """
        http_info = self._list_waf_attack_event_http_info(request)
        return self._call_api(**http_info)

    def list_waf_attack_event_async_invoker(self, request):
        http_info = self._list_waf_attack_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_waf_attack_event_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/domains/waf-info/attack/event",
            "request_type": request.__class__.__name__,
            "response_type": "ListWafAttackEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domains' in local_var_params:
            query_params.append(('domains', local_var_params['domains']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'overseas_type' in local_var_params:
            query_params.append(('overseas_type', local_var_params['overseas_type']))
        if 'sip' in local_var_params:
            query_params.append(('sip', local_var_params['sip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_waf_bandwidth_async(self, request):
        r"""带宽曲线

        带宽曲线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWafBandwidth
        :type request: :class:`huaweicloudsdkaad.v2.ListWafBandwidthRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListWafBandwidthResponse`
        """
        http_info = self._list_waf_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def list_waf_bandwidth_async_invoker(self, request):
        http_info = self._list_waf_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_waf_bandwidth_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/domains/waf-info/flow/bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "ListWafBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domains' in local_var_params:
            query_params.append(('domains', local_var_params['domains']))
        if 'value_type' in local_var_params:
            query_params.append(('value_type', local_var_params['value_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'overseas_type' in local_var_params:
            query_params.append(('overseas_type', local_var_params['overseas_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_waf_custom_rule_async(self, request):
        r"""查询精准防护规则

        查询精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWafCustomRule
        :type request: :class:`huaweicloudsdkaad.v2.ListWafCustomRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListWafCustomRuleResponse`
        """
        http_info = self._list_waf_custom_rule_http_info(request)
        return self._call_api(**http_info)

    def list_waf_custom_rule_async_invoker(self, request):
        http_info = self._list_waf_custom_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_waf_custom_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/policies/waf/custom-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListWafCustomRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'overseas_type' in local_var_params:
            query_params.append(('overseas_type', local_var_params['overseas_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_waf_geo_ip_rule_async(self, request):
        r"""查询区域封禁规则

        查询区域封禁规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWafGeoIpRule
        :type request: :class:`huaweicloudsdkaad.v2.ListWafGeoIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListWafGeoIpRuleResponse`
        """
        http_info = self._list_waf_geo_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def list_waf_geo_ip_rule_async_invoker(self, request):
        http_info = self._list_waf_geo_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_waf_geo_ip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/policies/waf/geoip-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListWafGeoIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'overseas_type' in local_var_params:
            query_params.append(('overseas_type', local_var_params['overseas_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_waf_qps_async(self, request):
        r"""查询请求QPS

        查询请求QPS
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWafQps
        :type request: :class:`huaweicloudsdkaad.v2.ListWafQpsRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListWafQpsResponse`
        """
        http_info = self._list_waf_qps_http_info(request)
        return self._call_api(**http_info)

    def list_waf_qps_async_invoker(self, request):
        http_info = self._list_waf_qps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_waf_qps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/domains/waf-info/flow/qps",
            "request_type": request.__class__.__name__,
            "response_type": "ListWafQpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domains' in local_var_params:
            query_params.append(('domains', local_var_params['domains']))
        if 'value_type' in local_var_params:
            query_params.append(('value_type', local_var_params['value_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'overseas_type' in local_var_params:
            query_params.append(('overseas_type', local_var_params['overseas_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_waf_white_ip_rule_async(self, request):
        r"""防护策略web-cc黑白名单-查询黑白名单规则

        防护策略web-cc黑白名单-查询黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWafWhiteIpRule
        :type request: :class:`huaweicloudsdkaad.v2.ListWafWhiteIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListWafWhiteIpRuleResponse`
        """
        http_info = self._list_waf_white_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def list_waf_white_ip_rule_async_invoker(self, request):
        http_info = self._list_waf_white_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_waf_white_ip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/policies/waf/blackwhite-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListWafWhiteIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'overseas_type' in local_var_params:
            query_params.append(('overseas_type', local_var_params['overseas_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_white_black_ip_rule_async(self, request):
        r"""查询DDoS攻击防护的黑白名单列表

        查询DDoS攻击防护的黑白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWhiteBlackIpRule
        :type request: :class:`huaweicloudsdkaad.v2.ListWhiteBlackIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ListWhiteBlackIpRuleResponse`
        """
        http_info = self._list_white_black_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def list_white_black_ip_rule_async_invoker(self, request):
        http_info = self._list_white_black_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_white_black_ip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/policies/ddos/blackwhite-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListWhiteBlackIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_domain_certificate_async(self, request):
        r"""查询域名关联的证书信息

        查询域名关联的证书信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainCertificate
        :type request: :class:`huaweicloudsdkaad.v2.ShowDomainCertificateRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ShowDomainCertificateResponse`
        """
        http_info = self._show_domain_certificate_http_info(request)
        return self._call_api(**http_info)

    def show_domain_certificate_async_invoker(self, request):
        http_info = self._show_domain_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_certificate_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/domains/{domain_id}/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_flow_block_async(self, request):
        r"""查询流量封禁信息

        查询流量封禁信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlowBlock
        :type request: :class:`huaweicloudsdkaad.v2.ShowFlowBlockRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ShowFlowBlockResponse`
        """
        http_info = self._show_flow_block_http_info(request)
        return self._call_api(**http_info)

    def show_flow_block_async_invoker(self, request):
        http_info = self._show_flow_block_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_flow_block_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/policies/ddos/flow-block",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlowBlockResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_waf_policy_async(self, request):
        r"""查询WEB防护策略配置

        查询WEB防护策略配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWafPolicy
        :type request: :class:`huaweicloudsdkaad.v2.ShowWafPolicyRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ShowWafPolicyResponse`
        """
        http_info = self._show_waf_policy_http_info(request)
        return self._call_api(**http_info)

    def show_waf_policy_async_invoker(self, request):
        http_info = self._show_waf_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_waf_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/policies/waf",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWafPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'overseas_type' in local_var_params:
            query_params.append(('overseas_type', local_var_params['overseas_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_waf_qps_async(self, request):
        r"""查询CC攻击防护请求QPS

        查询CC攻击防护请求QPS
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWafQps
        :type request: :class:`huaweicloudsdkaad.v2.ShowWafQpsRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.ShowWafQpsResponse`
        """
        http_info = self._show_waf_qps_http_info(request)
        return self._call_api(**http_info)

    def show_waf_qps_async_invoker(self, request):
        http_info = self._show_waf_qps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_waf_qps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aad/domains/waf-info/flow/request/peak",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWafQpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'domains' in local_var_params:
            query_params.append(('domains', local_var_params['domains']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'overseas_type' in local_var_params:
            query_params.append(('overseas_type', local_var_params['overseas_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upgrade_instance_spec_async(self, request):
        r"""修改实例规格

        修改实例规格
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeInstanceSpec
        :type request: :class:`huaweicloudsdkaad.v2.UpgradeInstanceSpecRequest`
        :rtype: :class:`huaweicloudsdkaad.v2.UpgradeInstanceSpecResponse`
        """
        http_info = self._upgrade_instance_spec_http_info(request)
        return self._call_api(**http_info)

    def upgrade_instance_spec_async_invoker(self, request):
        http_info = self._upgrade_instance_spec_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_instance_spec_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/aad/instance",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeInstanceSpecResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	        async_request=True)
