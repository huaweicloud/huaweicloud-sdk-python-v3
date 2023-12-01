# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkelb'")


class ElbClient(Client):
    def __init__(self):
        super(ElbClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkelb.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ElbClient":
                raise TypeError("client type error, support client type is ElbClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_add_available_zones(self, request):
        """新增负载均衡器可用区

        给负载均衡器新增可用区。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddAvailableZones
        :type request: :class:`huaweicloudsdkelb.v3.BatchAddAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchAddAvailableZonesResponse`
        """
        http_info = self._batch_add_available_zones_http_info(request)
        return self._call_api(**http_info)

    def batch_add_available_zones_invoker(self, request):
        http_info = self._batch_add_available_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_available_zones_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/availability-zone/batch-add",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddAvailableZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_create_members(self, request):
        """批量创建后端服务器

        在指定pool下批量创建后端服务器。一次最多创建200个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateMembers
        :type request: :class:`huaweicloudsdkelb.v3.BatchCreateMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchCreateMembersResponse`
        """
        http_info = self._batch_create_members_http_info(request)
        return self._call_api(**http_info)

    def batch_create_members_invoker(self, request):
        http_info = self._batch_create_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_members_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}/members/batch-add",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_delete_members(self, request):
        """批量删除后端服务器

        在指定pool下批量删除后端服务器。一次最多添加200个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteMembers
        :type request: :class:`huaweicloudsdkelb.v3.BatchDeleteMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchDeleteMembersResponse`
        """
        http_info = self._batch_delete_members_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_members_invoker(self, request):
        http_info = self._batch_delete_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_members_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}/members/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_remove_available_zones(self, request):
        """移除负载均衡器可用区

        移除负载均衡器的可用区。
        &gt; 移除可用区可能导致已有链接断开，请谨慎操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRemoveAvailableZones
        :type request: :class:`huaweicloudsdkelb.v3.BatchRemoveAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchRemoveAvailableZonesResponse`
        """
        http_info = self._batch_remove_available_zones_http_info(request)
        return self._call_api(**http_info)

    def batch_remove_available_zones_invoker(self, request):
        http_info = self._batch_remove_available_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_remove_available_zones_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/availability-zone/batch-remove",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRemoveAvailableZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_update_members(self, request):
        """批量更新后端服务器

        在指定pool下批量更新后端服务器。一次最多添加200个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateMembers
        :type request: :class:`huaweicloudsdkelb.v3.BatchUpdateMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchUpdateMembersResponse`
        """
        http_info = self._batch_update_members_http_info(request)
        return self._call_api(**http_info)

    def batch_update_members_invoker(self, request):
        http_info = self._batch_update_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_members_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}/members/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_update_policies_priority(self, request):
        """批量更新转发策略优先级

        批量更新转发策略的优先级。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdatePoliciesPriority
        :type request: :class:`huaweicloudsdkelb.v3.BatchUpdatePoliciesPriorityRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchUpdatePoliciesPriorityResponse`
        """
        http_info = self._batch_update_policies_priority_http_info(request)
        return self._call_api(**http_info)

    def batch_update_policies_priority_invoker(self, request):
        http_info = self._batch_update_policies_priority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_policies_priority_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/l7policies/batch-update-priority",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdatePoliciesPriorityResponse"
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
            ['application/json;charset=UTF-8'])

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

    def change_loadbalancer_charge_mode(self, request):
        """变更负载均衡器计费模式

        负载均衡器计费模式变更，当前支持的计费模式变更为：
        1. 按需计费转包周期计费；
        2. 按需按规格计费转按需按使用量计费；
        3. 按需按使用量计费转按需按规格计费；
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeLoadbalancerChargeMode
        :type request: :class:`huaweicloudsdkelb.v3.ChangeLoadbalancerChargeModeRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ChangeLoadbalancerChargeModeResponse`
        """
        http_info = self._change_loadbalancer_charge_mode_http_info(request)
        return self._call_api(**http_info)

    def change_loadbalancer_charge_mode_invoker(self, request):
        http_info = self._change_loadbalancer_charge_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_loadbalancer_charge_mode_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/loadbalancers/change-charge-mode",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeLoadbalancerChargeModeResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_certificate(self, request):
        """创建证书

        创建证书。用于HTTPS协议监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkelb.v3.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateCertificateResponse`
        """
        http_info = self._create_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_invoker(self, request):
        http_info = self._create_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_health_monitor(self, request):
        """创建健康检查

        创建健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHealthMonitor
        :type request: :class:`huaweicloudsdkelb.v3.CreateHealthMonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateHealthMonitorResponse`
        """
        http_info = self._create_health_monitor_http_info(request)
        return self._call_api(**http_info)

    def create_health_monitor_invoker(self, request):
        http_info = self._create_health_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_health_monitor_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/healthmonitors",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHealthMonitorResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_l7_policy(self, request):
        """创建转发策略

        创建七层转发策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateL7Policy
        :type request: :class:`huaweicloudsdkelb.v3.CreateL7PolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateL7PolicyResponse`
        """
        http_info = self._create_l7_policy_http_info(request)
        return self._call_api(**http_info)

    def create_l7_policy_invoker(self, request):
        http_info = self._create_l7_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_l7_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/l7policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateL7PolicyResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_l7_rule(self, request):
        """创建转发规则

        创建七层转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateL7Rule
        :type request: :class:`huaweicloudsdkelb.v3.CreateL7RuleRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateL7RuleResponse`
        """
        http_info = self._create_l7_rule_http_info(request)
        return self._call_api(**http_info)

    def create_l7_rule_invoker(self, request):
        http_info = self._create_l7_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_l7_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/l7policies/{l7policy_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateL7RuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_listener(self, request):
        """创建监听器

        创建监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateListener
        :type request: :class:`huaweicloudsdkelb.v3.CreateListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateListenerResponse`
        """
        http_info = self._create_listener_http_info(request)
        return self._call_api(**http_info)

    def create_listener_invoker(self, request):
        http_info = self._create_listener_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_listener_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/listeners",
            "request_type": request.__class__.__name__,
            "response_type": "CreateListenerResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_load_balancer(self, request):
        """创建负载均衡器

        创建负载均衡器。
        1. 若要创建内网IPv4负载均衡器，则需要设置vip_subnet_cidr_id。
        2. 若要创建公网IPv4负载均衡器，则需要设置publicip，以及设置vpc_id和vip_subnet_cidr_id这两个参数中的一个。
        3. 若要绑定有已有公网IPv4地址，
        则需要设置publicip_ids，以及设置vpc_id和vip_subnet_cidr_id这两个参数中的一个。
        4. 若要创建内网双栈负载均衡器，则需要设置ipv6_vip_virsubnet_id。
        5. 若要创建公网双栈负载均衡器，则需要设置ipv6_vip_virsubnet_id和ipv6_bandwidth。
        6. 不支持绑定已有未使用的内网IPv4、内网IPv6或公网IPv6地址。
        
        [&gt; 关于计费：
        - 若billing_info非空时，包周期。
        - 若billing_info为空，autoscaling.enable&#x3D;true时，弹性计费。
        - 若billing_info为空，autoscaling.enable&#x3D;false或未设置，charge_mode&#x3D;lcu，按量计费。
        - 若billing_info为空，autoscaling.enable&#x3D;false或未设置，charge_mode&#x3D;flavor，固定规格按需计费。](tag:hws)
        [&gt; 不支持创建IPv6地址负载均衡器](tag:dt,dt_test)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLoadBalancer
        :type request: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerResponse`
        """
        http_info = self._create_load_balancer_http_info(request)
        return self._call_api(**http_info)

    def create_load_balancer_invoker(self, request):
        http_info = self._create_load_balancer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_load_balancer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/loadbalancers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLoadBalancerResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_logtank(self, request):
        """创建云日志

        创建云日志。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLogtank
        :type request: :class:`huaweicloudsdkelb.v3.CreateLogtankRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateLogtankResponse`
        """
        http_info = self._create_logtank_http_info(request)
        return self._call_api(**http_info)

    def create_logtank_invoker(self, request):
        http_info = self._create_logtank_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_logtank_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/logtanks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogtankResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_master_slave_pool(self, request):
        """创建主备后端服务器组

        创建主备后端服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMasterSlavePool
        :type request: :class:`huaweicloudsdkelb.v3.CreateMasterSlavePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateMasterSlavePoolResponse`
        """
        http_info = self._create_master_slave_pool_http_info(request)
        return self._call_api(**http_info)

    def create_master_slave_pool_invoker(self, request):
        http_info = self._create_master_slave_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_master_slave_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/master-slave-pools",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMasterSlavePoolResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_member(self, request):
        """创建后端服务器

        创建后端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMember
        :type request: :class:`huaweicloudsdkelb.v3.CreateMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateMemberResponse`
        """
        http_info = self._create_member_http_info(request)
        return self._call_api(**http_info)

    def create_member_invoker(self, request):
        http_info = self._create_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_member_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_pool(self, request):
        """创建后端服务器组

        创建后端服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePool
        :type request: :class:`huaweicloudsdkelb.v3.CreatePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreatePoolResponse`
        """
        http_info = self._create_pool_http_info(request)
        return self._call_api(**http_info)

    def create_pool_invoker(self, request):
        http_info = self._create_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/pools",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePoolResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_security_policy(self, request):
        """创建自定义安全策略

        创建自定义安全策略。用于在创建HTTPS监听器时，请求参数中指定security_policy_id来设置监听器的自定义安全策略。
        
        [荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecurityPolicy
        :type request: :class:`huaweicloudsdkelb.v3.CreateSecurityPolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateSecurityPolicyResponse`
        """
        http_info = self._create_security_policy_http_info(request)
        return self._call_api(**http_info)

    def create_security_policy_invoker(self, request):
        http_info = self._create_security_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_security_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/security-policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecurityPolicyResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_certificate(self, request):
        """删除证书

        删除证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkelb.v3.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteCertificateResponse`
        """
        http_info = self._delete_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_invoker(self, request):
        http_info = self._delete_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_certificate_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def delete_health_monitor(self, request):
        """删除健康检查

        删除健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHealthMonitor
        :type request: :class:`huaweicloudsdkelb.v3.DeleteHealthMonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteHealthMonitorResponse`
        """
        http_info = self._delete_health_monitor_http_info(request)
        return self._call_api(**http_info)

    def delete_health_monitor_invoker(self, request):
        http_info = self._delete_health_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_health_monitor_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/healthmonitors/{healthmonitor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHealthMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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

    def delete_l7_policy(self, request):
        """删除转发策略

        删除七层转发策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteL7Policy
        :type request: :class:`huaweicloudsdkelb.v3.DeleteL7PolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteL7PolicyResponse`
        """
        http_info = self._delete_l7_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_l7_policy_invoker(self, request):
        http_info = self._delete_l7_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_l7_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/l7policies/{l7policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteL7PolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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

    def delete_l7_rule(self, request):
        """删除转发规则

        删除七层转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteL7Rule
        :type request: :class:`huaweicloudsdkelb.v3.DeleteL7RuleRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteL7RuleResponse`
        """
        http_info = self._delete_l7_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_l7_rule_invoker(self, request):
        http_info = self._delete_l7_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_l7_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteL7RuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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

    def delete_listener(self, request):
        """删除监听器

        删除监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteListener
        :type request: :class:`huaweicloudsdkelb.v3.DeleteListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteListenerResponse`
        """
        http_info = self._delete_listener_http_info(request)
        return self._call_api(**http_info)

    def delete_listener_invoker(self, request):
        http_info = self._delete_listener_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_listener_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def delete_listener_force(self, request):
        """级联删除监听器

        删除监听器且级联删除其下子资源（删除监听器、转发策略等，解绑后端服务器组）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteListenerForce
        :type request: :class:`huaweicloudsdkelb.v3.DeleteListenerForceRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteListenerForceResponse`
        """
        http_info = self._delete_listener_force_http_info(request)
        return self._call_api(**http_info)

    def delete_listener_force_invoker(self, request):
        http_info = self._delete_listener_force_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_listener_force_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/listeners/{listener_id}/force",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteListenerForceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def delete_load_balancer(self, request):
        """删除负载均衡器

        删除负载均衡器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLoadBalancer
        :type request: :class:`huaweicloudsdkelb.v3.DeleteLoadBalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteLoadBalancerResponse`
        """
        http_info = self._delete_load_balancer_http_info(request)
        return self._call_api(**http_info)

    def delete_load_balancer_invoker(self, request):
        http_info = self._delete_load_balancer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_load_balancer_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLoadBalancerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def delete_load_balancer_force(self, request):
        """级联删除负载均衡器

        删除负载均衡器且级联删除其下子资源（删除负载均衡器及其绑定的监听器、后端服务器组、后端服务器等一系列资源）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLoadBalancerForce
        :type request: :class:`huaweicloudsdkelb.v3.DeleteLoadBalancerForceRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteLoadBalancerForceResponse`
        """
        http_info = self._delete_load_balancer_force_http_info(request)
        return self._call_api(**http_info)

    def delete_load_balancer_force_invoker(self, request):
        http_info = self._delete_load_balancer_force_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_load_balancer_force_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/force-elb",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLoadBalancerForceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def delete_logtank(self, request):
        """删除云日志

        删除云日志。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogtank
        :type request: :class:`huaweicloudsdkelb.v3.DeleteLogtankRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteLogtankResponse`
        """
        http_info = self._delete_logtank_http_info(request)
        return self._call_api(**http_info)

    def delete_logtank_invoker(self, request):
        http_info = self._delete_logtank_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_logtank_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/logtanks/{logtank_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'logtank_id' in local_var_params:
            path_params['logtank_id'] = local_var_params['logtank_id']

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

    def delete_master_slave_pool(self, request):
        """删除主备后端服务器组

        删除主备后端服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMasterSlavePool
        :type request: :class:`huaweicloudsdkelb.v3.DeleteMasterSlavePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteMasterSlavePoolResponse`
        """
        http_info = self._delete_master_slave_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_master_slave_pool_invoker(self, request):
        http_info = self._delete_master_slave_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_master_slave_pool_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/master-slave-pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMasterSlavePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def delete_member(self, request):
        """删除后端服务器

        删除后端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMember
        :type request: :class:`huaweicloudsdkelb.v3.DeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteMemberResponse`
        """
        http_info = self._delete_member_http_info(request)
        return self._call_api(**http_info)

    def delete_member_invoker(self, request):
        http_info = self._delete_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_member_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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

    def delete_pool(self, request):
        """删除后端服务器组

        删除后端服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePool
        :type request: :class:`huaweicloudsdkelb.v3.DeletePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeletePoolResponse`
        """
        http_info = self._delete_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_pool_invoker(self, request):
        http_info = self._delete_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_pool_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def delete_security_policy(self, request):
        """删除自定义安全策略

        删除自定义安全策略。[荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecurityPolicy
        :type request: :class:`huaweicloudsdkelb.v3.DeleteSecurityPolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteSecurityPolicyResponse`
        """
        http_info = self._delete_security_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_security_policy_invoker(self, request):
        http_info = self._delete_security_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_security_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/security-policies/{security_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecurityPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_policy_id' in local_var_params:
            path_params['security_policy_id'] = local_var_params['security_policy_id']

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

    def list_all_members(self, request):
        """后端服务器全局列表

        查询当前租户下的后端服务器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllMembers
        :type request: :class:`huaweicloudsdkelb.v3.ListAllMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListAllMembersResponse`
        """
        http_info = self._list_all_members_http_info(request)
        return self._call_api(**http_info)

    def list_all_members_invoker(self, request):
        http_info = self._list_all_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_members_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'weight' in local_var_params:
            query_params.append(('weight', local_var_params['weight']))
            collection_formats['weight'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'subnet_cidr_id' in local_var_params:
            query_params.append(('subnet_cidr_id', local_var_params['subnet_cidr_id']))
            collection_formats['subnet_cidr_id'] = 'multi'
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
            collection_formats['address'] = 'multi'
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
            collection_formats['protocol_port'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
            collection_formats['operating_status'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
            collection_formats['pool_id'] = 'multi'
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'

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

    def list_availability_zones(self, request):
        """查询可用区列表

        返回租户创建LB时可使用的可用区集合列表情况。
        
        - 默认情况下，会返回一个可用区集合。
        在（如创建LB）设置可用区时，填写的可用区必须包含在可用区集合中、为这个可用区集合的子集。
        
        - 特殊场景下，部分客户要求负载均衡只能创建在指定可用区集合中，此时会返回客户定制的可用区集合。
        返回可用区集合可能为一个也可能为多个，比如列表有两个可用区集合\\[az1,az2\\],\\[az2,az3\\]。
        在创建负载均衡器时，可以选择创建在多个可用区，但所选的多个可用区必须同属于其中一个可用区集合，
        如可以选az2和az3，但不能选择az1和az3。你可以选择多个可用区，只要这些可用区在一个子集中
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkelb.v3.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListAvailabilityZonesResponse`
        """
        http_info = self._list_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zones_invoker(self, request):
        http_info = self._list_availability_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_availability_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/availability-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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

    def list_certificates(self, request):
        """查询证书列表

        查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkelb.v3.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListCertificatesResponse`
        """
        http_info = self._list_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_invoker(self, request):
        http_info = self._list_certificates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_certificates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
            collection_formats['domain'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'

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

    def list_flavors(self, request):
        """查询规格列表

        查询租户在当前region下可用的负载均衡规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkelb.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'shared' in local_var_params:
            query_params.append(('shared', local_var_params['shared']))

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

    def list_health_monitors(self, request):
        """查询健康检查列表

        健康检查列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHealthMonitors
        :type request: :class:`huaweicloudsdkelb.v3.ListHealthMonitorsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListHealthMonitorsResponse`
        """
        http_info = self._list_health_monitors_http_info(request)
        return self._call_api(**http_info)

    def list_health_monitors_invoker(self, request):
        http_info = self._list_health_monitors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_health_monitors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/healthmonitors",
            "request_type": request.__class__.__name__,
            "response_type": "ListHealthMonitorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'monitor_port' in local_var_params:
            query_params.append(('monitor_port', local_var_params['monitor_port']))
            collection_formats['monitor_port'] = 'multi'
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
            collection_formats['domain_name'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'delay' in local_var_params:
            query_params.append(('delay', local_var_params['delay']))
            collection_formats['delay'] = 'multi'
        if 'max_retries' in local_var_params:
            query_params.append(('max_retries', local_var_params['max_retries']))
            collection_formats['max_retries'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'max_retries_down' in local_var_params:
            query_params.append(('max_retries_down', local_var_params['max_retries_down']))
            collection_formats['max_retries_down'] = 'multi'
        if 'timeout' in local_var_params:
            query_params.append(('timeout', local_var_params['timeout']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'expected_codes' in local_var_params:
            query_params.append(('expected_codes', local_var_params['expected_codes']))
            collection_formats['expected_codes'] = 'multi'
        if 'url_path' in local_var_params:
            query_params.append(('url_path', local_var_params['url_path']))
            collection_formats['url_path'] = 'multi'
        if 'http_method' in local_var_params:
            query_params.append(('http_method', local_var_params['http_method']))
            collection_formats['http_method'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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

    def list_l7_policies(self, request):
        """查询转发策略列表

        查询七层转发策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListL7Policies
        :type request: :class:`huaweicloudsdkelb.v3.ListL7PoliciesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListL7PoliciesResponse`
        """
        http_info = self._list_l7_policies_http_info(request)
        return self._call_api(**http_info)

    def list_l7_policies_invoker(self, request):
        http_info = self._list_l7_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_l7_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/l7policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListL7PoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
            collection_formats['listener_id'] = 'multi'
        if 'position' in local_var_params:
            query_params.append(('position', local_var_params['position']))
            collection_formats['position'] = 'multi'
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
            collection_formats['action'] = 'multi'
        if 'redirect_url' in local_var_params:
            query_params.append(('redirect_url', local_var_params['redirect_url']))
            collection_formats['redirect_url'] = 'multi'
        if 'redirect_pool_id' in local_var_params:
            query_params.append(('redirect_pool_id', local_var_params['redirect_pool_id']))
            collection_formats['redirect_pool_id'] = 'multi'
        if 'redirect_listener_id' in local_var_params:
            query_params.append(('redirect_listener_id', local_var_params['redirect_listener_id']))
            collection_formats['redirect_listener_id'] = 'multi'
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'display_all_rules' in local_var_params:
            query_params.append(('display_all_rules', local_var_params['display_all_rules']))
        if 'priority' in local_var_params:
            query_params.append(('priority', local_var_params['priority']))
            collection_formats['priority'] = 'csv'

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

    def list_l7_rules(self, request):
        """查询转发规则列表

        查询转发规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListL7Rules
        :type request: :class:`huaweicloudsdkelb.v3.ListL7RulesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListL7RulesResponse`
        """
        http_info = self._list_l7_rules_http_info(request)
        return self._call_api(**http_info)

    def list_l7_rules_invoker(self, request):
        http_info = self._list_l7_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_l7_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/l7policies/{l7policy_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListL7RulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'compare_type' in local_var_params:
            query_params.append(('compare_type', local_var_params['compare_type']))
            collection_formats['compare_type'] = 'multi'
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'invert' in local_var_params:
            query_params.append(('invert', local_var_params['invert']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))
            collection_formats['value'] = 'multi'
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
            collection_formats['key'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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

    def list_listeners(self, request):
        """查询监听器列表

        查询监听器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListListeners
        :type request: :class:`huaweicloudsdkelb.v3.ListListenersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListListenersResponse`
        """
        http_info = self._list_listeners_http_info(request)
        return self._call_api(**http_info)

    def list_listeners_invoker(self, request):
        http_info = self._list_listeners_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_listeners_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/listeners",
            "request_type": request.__class__.__name__,
            "response_type": "ListListenersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
            collection_formats['protocol_port'] = 'multi'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'default_tls_container_ref' in local_var_params:
            query_params.append(('default_tls_container_ref', local_var_params['default_tls_container_ref']))
            collection_formats['default_tls_container_ref'] = 'multi'
        if 'client_ca_tls_container_ref' in local_var_params:
            query_params.append(('client_ca_tls_container_ref', local_var_params['client_ca_tls_container_ref']))
            collection_formats['client_ca_tls_container_ref'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'connection_limit' in local_var_params:
            query_params.append(('connection_limit', local_var_params['connection_limit']))
            collection_formats['connection_limit'] = 'multi'
        if 'default_pool_id' in local_var_params:
            query_params.append(('default_pool_id', local_var_params['default_pool_id']))
            collection_formats['default_pool_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'http2_enable' in local_var_params:
            query_params.append(('http2_enable', local_var_params['http2_enable']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'
        if 'tls_ciphers_policy' in local_var_params:
            query_params.append(('tls_ciphers_policy', local_var_params['tls_ciphers_policy']))
            collection_formats['tls_ciphers_policy'] = 'multi'
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'enable_member_retry' in local_var_params:
            query_params.append(('enable_member_retry', local_var_params['enable_member_retry']))
        if 'member_timeout' in local_var_params:
            query_params.append(('member_timeout', local_var_params['member_timeout']))
            collection_formats['member_timeout'] = 'multi'
        if 'client_timeout' in local_var_params:
            query_params.append(('client_timeout', local_var_params['client_timeout']))
            collection_formats['client_timeout'] = 'multi'
        if 'keepalive_timeout' in local_var_params:
            query_params.append(('keepalive_timeout', local_var_params['keepalive_timeout']))
            collection_formats['keepalive_timeout'] = 'multi'
        if 'transparent_client_ip_enable' in local_var_params:
            query_params.append(('transparent_client_ip_enable', local_var_params['transparent_client_ip_enable']))
        if 'proxy_protocol_enable' in local_var_params:
            query_params.append(('proxy_protocol_enable', local_var_params['proxy_protocol_enable']))
        if 'enhance_l7policy_enable' in local_var_params:
            query_params.append(('enhance_l7policy_enable', local_var_params['enhance_l7policy_enable']))
        if 'member_instance_id' in local_var_params:
            query_params.append(('member_instance_id', local_var_params['member_instance_id']))
            collection_formats['member_instance_id'] = 'csv'
        if 'protection_status' in local_var_params:
            query_params.append(('protection_status', local_var_params['protection_status']))
            collection_formats['protection_status'] = 'csv'

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

    def list_load_balancers(self, request):
        """查询负载均衡器列表

        查询负载均衡器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLoadBalancers
        :type request: :class:`huaweicloudsdkelb.v3.ListLoadBalancersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListLoadBalancersResponse`
        """
        http_info = self._list_load_balancers_http_info(request)
        return self._call_api(**http_info)

    def list_load_balancers_invoker(self, request):
        http_info = self._list_load_balancers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_load_balancers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/loadbalancers",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoadBalancersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
            collection_formats['operating_status'] = 'multi'
        if 'guaranteed' in local_var_params:
            query_params.append(('guaranteed', local_var_params['guaranteed']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'multi'
        if 'vip_port_id' in local_var_params:
            query_params.append(('vip_port_id', local_var_params['vip_port_id']))
            collection_formats['vip_port_id'] = 'multi'
        if 'vip_address' in local_var_params:
            query_params.append(('vip_address', local_var_params['vip_address']))
            collection_formats['vip_address'] = 'multi'
        if 'vip_subnet_cidr_id' in local_var_params:
            query_params.append(('vip_subnet_cidr_id', local_var_params['vip_subnet_cidr_id']))
            collection_formats['vip_subnet_cidr_id'] = 'multi'
        if 'ipv6_vip_port_id' in local_var_params:
            query_params.append(('ipv6_vip_port_id', local_var_params['ipv6_vip_port_id']))
            collection_formats['ipv6_vip_port_id'] = 'multi'
        if 'ipv6_vip_address' in local_var_params:
            query_params.append(('ipv6_vip_address', local_var_params['ipv6_vip_address']))
            collection_formats['ipv6_vip_address'] = 'multi'
        if 'ipv6_vip_virsubnet_id' in local_var_params:
            query_params.append(('ipv6_vip_virsubnet_id', local_var_params['ipv6_vip_virsubnet_id']))
            collection_formats['ipv6_vip_virsubnet_id'] = 'multi'
        if 'eips' in local_var_params:
            query_params.append(('eips', local_var_params['eips']))
            collection_formats['eips'] = 'multi'
        if 'publicips' in local_var_params:
            query_params.append(('publicips', local_var_params['publicips']))
            collection_formats['publicips'] = 'multi'
        if 'availability_zone_list' in local_var_params:
            query_params.append(('availability_zone_list', local_var_params['availability_zone_list']))
            collection_formats['availability_zone_list'] = 'multi'
        if 'l4_flavor_id' in local_var_params:
            query_params.append(('l4_flavor_id', local_var_params['l4_flavor_id']))
            collection_formats['l4_flavor_id'] = 'multi'
        if 'l4_scale_flavor_id' in local_var_params:
            query_params.append(('l4_scale_flavor_id', local_var_params['l4_scale_flavor_id']))
            collection_formats['l4_scale_flavor_id'] = 'multi'
        if 'l7_flavor_id' in local_var_params:
            query_params.append(('l7_flavor_id', local_var_params['l7_flavor_id']))
            collection_formats['l7_flavor_id'] = 'multi'
        if 'l7_scale_flavor_id' in local_var_params:
            query_params.append(('l7_scale_flavor_id', local_var_params['l7_scale_flavor_id']))
            collection_formats['l7_scale_flavor_id'] = 'multi'
        if 'billing_info' in local_var_params:
            query_params.append(('billing_info', local_var_params['billing_info']))
            collection_formats['billing_info'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'deletion_protection_enable' in local_var_params:
            query_params.append(('deletion_protection_enable', local_var_params['deletion_protection_enable']))
        if 'elb_virsubnet_type' in local_var_params:
            query_params.append(('elb_virsubnet_type', local_var_params['elb_virsubnet_type']))
            collection_formats['elb_virsubnet_type'] = 'csv'
        if 'autoscaling' in local_var_params:
            query_params.append(('autoscaling', local_var_params['autoscaling']))
            collection_formats['autoscaling'] = 'csv'
        if 'protection_status' in local_var_params:
            query_params.append(('protection_status', local_var_params['protection_status']))
            collection_formats['protection_status'] = 'csv'
        if 'global_eips' in local_var_params:
            query_params.append(('global_eips', local_var_params['global_eips']))
            collection_formats['global_eips'] = 'csv'
        if 'log_topic_id' in local_var_params:
            query_params.append(('log_topic_id', local_var_params['log_topic_id']))
        if 'log_group_id' in local_var_params:
            query_params.append(('log_group_id', local_var_params['log_group_id']))

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

    def list_logtanks(self, request):
        """查询云日志列表

        查询云日志列表。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogtanks
        :type request: :class:`huaweicloudsdkelb.v3.ListLogtanksRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListLogtanksResponse`
        """
        http_info = self._list_logtanks_http_info(request)
        return self._call_api(**http_info)

    def list_logtanks_invoker(self, request):
        http_info = self._list_logtanks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_logtanks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/logtanks",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogtanksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'csv'
        if 'log_group_id' in local_var_params:
            query_params.append(('log_group_id', local_var_params['log_group_id']))
            collection_formats['log_group_id'] = 'csv'
        if 'log_topic_id' in local_var_params:
            query_params.append(('log_topic_id', local_var_params['log_topic_id']))
            collection_formats['log_topic_id'] = 'csv'

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

    def list_master_slave_pools(self, request):
        """查询主备后端服务器组列表

        主备后端服务器组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMasterSlavePools
        :type request: :class:`huaweicloudsdkelb.v3.ListMasterSlavePoolsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListMasterSlavePoolsResponse`
        """
        http_info = self._list_master_slave_pools_http_info(request)
        return self._call_api(**http_info)

    def list_master_slave_pools_invoker(self, request):
        http_info = self._list_master_slave_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_master_slave_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/master-slave-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListMasterSlavePoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'healthmonitor_id' in local_var_params:
            query_params.append(('healthmonitor_id', local_var_params['healthmonitor_id']))
            collection_formats['healthmonitor_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'multi'
        if 'lb_algorithm' in local_var_params:
            query_params.append(('lb_algorithm', local_var_params['lb_algorithm']))
            collection_formats['lb_algorithm'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
            collection_formats['listener_id'] = 'csv'
        if 'member_instance_id' in local_var_params:
            query_params.append(('member_instance_id', local_var_params['member_instance_id']))
            collection_formats['member_instance_id'] = 'csv'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'

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

    def list_members(self, request):
        """查询后端服务器列表

        Pool下的后端服务器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMembers
        :type request: :class:`huaweicloudsdkelb.v3.ListMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListMembersResponse`
        """
        http_info = self._list_members_http_info(request)
        return self._call_api(**http_info)

    def list_members_invoker(self, request):
        http_info = self._list_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_members_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'weight' in local_var_params:
            query_params.append(('weight', local_var_params['weight']))
            collection_formats['weight'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'subnet_cidr_id' in local_var_params:
            query_params.append(('subnet_cidr_id', local_var_params['subnet_cidr_id']))
            collection_formats['subnet_cidr_id'] = 'multi'
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
            collection_formats['address'] = 'multi'
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
            collection_formats['protocol_port'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
            collection_formats['operating_status'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'member_type' in local_var_params:
            query_params.append(('member_type', local_var_params['member_type']))
            collection_formats['member_type'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'

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

    def list_pools(self, request):
        """查询后端服务器组列表

        后端服务器组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPools
        :type request: :class:`huaweicloudsdkelb.v3.ListPoolsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListPoolsResponse`
        """
        http_info = self._list_pools_http_info(request)
        return self._call_api(**http_info)

    def list_pools_invoker(self, request):
        http_info = self._list_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'healthmonitor_id' in local_var_params:
            query_params.append(('healthmonitor_id', local_var_params['healthmonitor_id']))
            collection_formats['healthmonitor_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'multi'
        if 'lb_algorithm' in local_var_params:
            query_params.append(('lb_algorithm', local_var_params['lb_algorithm']))
            collection_formats['lb_algorithm'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'member_deletion_protection_enable' in local_var_params:
            query_params.append(('member_deletion_protection_enable', local_var_params['member_deletion_protection_enable']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
            collection_formats['listener_id'] = 'csv'
        if 'member_instance_id' in local_var_params:
            query_params.append(('member_instance_id', local_var_params['member_instance_id']))
            collection_formats['member_instance_id'] = 'csv'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'protection_status' in local_var_params:
            query_params.append(('protection_status', local_var_params['protection_status']))
            collection_formats['protection_status'] = 'csv'

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

    def list_quota_details(self, request):
        """查询配额使用详情

        查询指定项目中负载均衡相关的各类资源的当前配额和已使用配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotaDetails
        :type request: :class:`huaweicloudsdkelb.v3.ListQuotaDetailsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListQuotaDetailsResponse`
        """
        http_info = self._list_quota_details_http_info(request)
        return self._call_api(**http_info)

    def list_quota_details_invoker(self, request):
        http_info = self._list_quota_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quota_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/quotas/details",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotaDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'quota_key' in local_var_params:
            query_params.append(('quota_key', local_var_params['quota_key']))
            collection_formats['quota_key'] = 'csv'

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

    def list_security_policies(self, request):
        """查询自定义安全策略列表

        查询自定义安全策略列表。[荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecurityPolicies
        :type request: :class:`huaweicloudsdkelb.v3.ListSecurityPoliciesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListSecurityPoliciesResponse`
        """
        http_info = self._list_security_policies_http_info(request)
        return self._call_api(**http_info)

    def list_security_policies_invoker(self, request):
        http_info = self._list_security_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_security_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/security-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecurityPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'protocols' in local_var_params:
            query_params.append(('protocols', local_var_params['protocols']))
            collection_formats['protocols'] = 'csv'
        if 'ciphers' in local_var_params:
            query_params.append(('ciphers', local_var_params['ciphers']))
            collection_formats['ciphers'] = 'csv'

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

    def list_system_security_policies(self, request):
        """查询系统安全策略列表

        查询系统安全策略列表。
        
        系统安全策略为预置的所有租户通用的安全策略，租户不可新增或修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSystemSecurityPolicies
        :type request: :class:`huaweicloudsdkelb.v3.ListSystemSecurityPoliciesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListSystemSecurityPoliciesResponse`
        """
        http_info = self._list_system_security_policies_http_info(request)
        return self._call_api(**http_info)

    def list_system_security_policies_invoker(self, request):
        http_info = self._list_system_security_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_system_security_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/system-security-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListSystemSecurityPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def show_certificate(self, request):
        """查询证书详情

        查询证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkelb.v3.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowCertificateResponse`
        """
        http_info = self._show_certificate_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_invoker(self, request):
        http_info = self._show_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_certificate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def show_flavor(self, request):
        """查询规格详情

        查询规格的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlavor
        :type request: :class:`huaweicloudsdkelb.v3.ShowFlavorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowFlavorResponse`
        """
        http_info = self._show_flavor_http_info(request)
        return self._call_api(**http_info)

    def show_flavor_invoker(self, request):
        http_info = self._show_flavor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flavor_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/flavors/{flavor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlavorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in local_var_params:
            path_params['flavor_id'] = local_var_params['flavor_id']

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

    def show_health_monitor(self, request):
        """查询健康检查详情

        查询健康检查详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHealthMonitor
        :type request: :class:`huaweicloudsdkelb.v3.ShowHealthMonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowHealthMonitorResponse`
        """
        http_info = self._show_health_monitor_http_info(request)
        return self._call_api(**http_info)

    def show_health_monitor_invoker(self, request):
        http_info = self._show_health_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_health_monitor_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/healthmonitors/{healthmonitor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHealthMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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

    def show_l7_policy(self, request):
        """查询转发策略详情

        查询七层转发策略详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowL7Policy
        :type request: :class:`huaweicloudsdkelb.v3.ShowL7PolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowL7PolicyResponse`
        """
        http_info = self._show_l7_policy_http_info(request)
        return self._call_api(**http_info)

    def show_l7_policy_invoker(self, request):
        http_info = self._show_l7_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_l7_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/l7policies/{l7policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowL7PolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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

    def show_l7_rule(self, request):
        """查询转发规则详情

        查询七层转发规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowL7Rule
        :type request: :class:`huaweicloudsdkelb.v3.ShowL7RuleRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowL7RuleResponse`
        """
        http_info = self._show_l7_rule_http_info(request)
        return self._call_api(**http_info)

    def show_l7_rule_invoker(self, request):
        http_info = self._show_l7_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_l7_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowL7RuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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

    def show_listener(self, request):
        """查询监听器详情

        监听器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowListener
        :type request: :class:`huaweicloudsdkelb.v3.ShowListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowListenerResponse`
        """
        http_info = self._show_listener_http_info(request)
        return self._call_api(**http_info)

    def show_listener_invoker(self, request):
        http_info = self._show_listener_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_listener_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def show_load_balancer(self, request):
        """查询负载均衡器详情

        查询负载均衡器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLoadBalancer
        :type request: :class:`huaweicloudsdkelb.v3.ShowLoadBalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowLoadBalancerResponse`
        """
        http_info = self._show_load_balancer_http_info(request)
        return self._call_api(**http_info)

    def show_load_balancer_invoker(self, request):
        http_info = self._show_load_balancer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_load_balancer_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLoadBalancerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def show_load_balancer_status(self, request):
        """查询负载均衡器状态树

        查询负载均衡器状态树，包括负载均衡器及其关联的子资源的状态信息。
        注意：该接口中的operating_status不一定与对应资源的operating_status相同。
        如：当Member的admin_state_up&#x3D;false且operating_status&#x3D;OFFLINE时，
        该接口返回member的operating_status&#x3D;DISABLE。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLoadBalancerStatus
        :type request: :class:`huaweicloudsdkelb.v3.ShowLoadBalancerStatusRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowLoadBalancerStatusResponse`
        """
        http_info = self._show_load_balancer_status_http_info(request)
        return self._call_api(**http_info)

    def show_load_balancer_status_invoker(self, request):
        http_info = self._show_load_balancer_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_load_balancer_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/statuses",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLoadBalancerStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def show_logtank(self, request):
        """查询云日志详情

        云日志详情。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogtank
        :type request: :class:`huaweicloudsdkelb.v3.ShowLogtankRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowLogtankResponse`
        """
        http_info = self._show_logtank_http_info(request)
        return self._call_api(**http_info)

    def show_logtank_invoker(self, request):
        http_info = self._show_logtank_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logtank_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/logtanks/{logtank_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'logtank_id' in local_var_params:
            path_params['logtank_id'] = local_var_params['logtank_id']

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

    def show_master_slave_pool(self, request):
        """查询主备后端服务器组详情

        主备后端服务器组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMasterSlavePool
        :type request: :class:`huaweicloudsdkelb.v3.ShowMasterSlavePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowMasterSlavePoolResponse`
        """
        http_info = self._show_master_slave_pool_http_info(request)
        return self._call_api(**http_info)

    def show_master_slave_pool_invoker(self, request):
        http_info = self._show_master_slave_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_master_slave_pool_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/master-slave-pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMasterSlavePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def show_member(self, request):
        """查询后端服务器详情

        后端服务器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMember
        :type request: :class:`huaweicloudsdkelb.v3.ShowMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowMemberResponse`
        """
        http_info = self._show_member_http_info(request)
        return self._call_api(**http_info)

    def show_member_invoker(self, request):
        http_info = self._show_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_member_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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

    def show_pool(self, request):
        """查询后端服务器组详情

        后端服务器组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPool
        :type request: :class:`huaweicloudsdkelb.v3.ShowPoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowPoolResponse`
        """
        http_info = self._show_pool_http_info(request)
        return self._call_api(**http_info)

    def show_pool_invoker(self, request):
        http_info = self._show_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pool_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def show_quota(self, request):
        """查询配额详情

        查询指定项目中负载均衡相关的各类资源的当前配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkelb.v3.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowQuotaResponse`
        """
        http_info = self._show_quota_http_info(request)
        return self._call_api(**http_info)

    def show_quota_invoker(self, request):
        http_info = self._show_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def show_security_policy(self, request):
        """查询自定义安全策略详情

        查询自定义安全策略详情。[荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecurityPolicy
        :type request: :class:`huaweicloudsdkelb.v3.ShowSecurityPolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowSecurityPolicyResponse`
        """
        http_info = self._show_security_policy_http_info(request)
        return self._call_api(**http_info)

    def show_security_policy_invoker(self, request):
        http_info = self._show_security_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_security_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/security-policies/{security_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecurityPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_policy_id' in local_var_params:
            path_params['security_policy_id'] = local_var_params['security_policy_id']

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

    def update_certificate(self, request):
        """更新证书

        更新证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCertificate
        :type request: :class:`huaweicloudsdkelb.v3.UpdateCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateCertificateResponse`
        """
        http_info = self._update_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_certificate_invoker(self, request):
        http_info = self._update_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_certificate_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_health_monitor(self, request):
        """更新健康检查

        更新健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHealthMonitor
        :type request: :class:`huaweicloudsdkelb.v3.UpdateHealthMonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateHealthMonitorResponse`
        """
        http_info = self._update_health_monitor_http_info(request)
        return self._call_api(**http_info)

    def update_health_monitor_invoker(self, request):
        http_info = self._update_health_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_health_monitor_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/healthmonitors/{healthmonitor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHealthMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_l7_policy(self, request):
        """更新转发策略

        更新七层转发策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateL7Policy
        :type request: :class:`huaweicloudsdkelb.v3.UpdateL7PolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateL7PolicyResponse`
        """
        http_info = self._update_l7_policy_http_info(request)
        return self._call_api(**http_info)

    def update_l7_policy_invoker(self, request):
        http_info = self._update_l7_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_l7_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/l7policies/{l7policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateL7PolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_l7_rule(self, request):
        """更新转发规则

        更新七层转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateL7Rule
        :type request: :class:`huaweicloudsdkelb.v3.UpdateL7RuleRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateL7RuleResponse`
        """
        http_info = self._update_l7_rule_http_info(request)
        return self._call_api(**http_info)

    def update_l7_rule_invoker(self, request):
        http_info = self._update_l7_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_l7_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateL7RuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_listener(self, request):
        """更新监听器

        更新监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateListener
        :type request: :class:`huaweicloudsdkelb.v3.UpdateListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateListenerResponse`
        """
        http_info = self._update_listener_http_info(request)
        return self._call_api(**http_info)

    def update_listener_invoker(self, request):
        http_info = self._update_listener_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_listener_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_load_balancer(self, request):
        """更新负载均衡器

        更新负载均衡器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLoadBalancer
        :type request: :class:`huaweicloudsdkelb.v3.UpdateLoadBalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateLoadBalancerResponse`
        """
        http_info = self._update_load_balancer_http_info(request)
        return self._call_api(**http_info)

    def update_load_balancer_invoker(self, request):
        http_info = self._update_load_balancer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_load_balancer_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLoadBalancerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_logtank(self, request):
        """更新云日志

        更新云日志。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLogtank
        :type request: :class:`huaweicloudsdkelb.v3.UpdateLogtankRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateLogtankResponse`
        """
        http_info = self._update_logtank_http_info(request)
        return self._call_api(**http_info)

    def update_logtank_invoker(self, request):
        http_info = self._update_logtank_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_logtank_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/logtanks/{logtank_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'logtank_id' in local_var_params:
            path_params['logtank_id'] = local_var_params['logtank_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_member(self, request):
        """更新后端服务器

        更新后端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMember
        :type request: :class:`huaweicloudsdkelb.v3.UpdateMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateMemberResponse`
        """
        http_info = self._update_member_http_info(request)
        return self._call_api(**http_info)

    def update_member_invoker(self, request):
        http_info = self._update_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_member_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_pool(self, request):
        """更新后端服务器组

        更新后端服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePool
        :type request: :class:`huaweicloudsdkelb.v3.UpdatePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdatePoolResponse`
        """
        http_info = self._update_pool_http_info(request)
        return self._call_api(**http_info)

    def update_pool_invoker(self, request):
        http_info = self._update_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_pool_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_security_policy(self, request):
        """更新自定义安全策略

        更新自定义安全策略。[荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecurityPolicy
        :type request: :class:`huaweicloudsdkelb.v3.UpdateSecurityPolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateSecurityPolicyResponse`
        """
        http_info = self._update_security_policy_http_info(request)
        return self._call_api(**http_info)

    def update_security_policy_invoker(self, request):
        http_info = self._update_security_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_security_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/security-policies/{security_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecurityPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_policy_id' in local_var_params:
            path_params['security_policy_id'] = local_var_params['security_policy_id']

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
            ['application/json;charset=UTF-8'])

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

    def list_api_versions(self, request):
        """查询API版本列表信息

        返回ELB当前所有可用的API版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkelb.v3.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def batch_delete_ip_list(self, request):
        """删除IP地址组的IP列表项

        批量删除IP地址组的IP列表信息。[荷兰region不支持该API](tag:dt,dt_test)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteIpList
        :type request: :class:`huaweicloudsdkelb.v3.BatchDeleteIpListRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchDeleteIpListResponse`
        """
        http_info = self._batch_delete_ip_list_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_ip_list_invoker(self, request):
        http_info = self._batch_delete_ip_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_ip_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/ipgroups/{ipgroup_id}/iplist/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteIpListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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
            ['application/json;charset=UTF-8'])

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

    def count_preoccupy_ip_num(self, request):
        """计算预占IP数

        计算以下几种场景的预占用IP数量：
        
        - 计算创建LB的第一个七层监听器后总占用IP数量：
        传入loadbalancer_id、l7_flavor_id为空、ip_target_enable不传或为false。
        
        - 计算LB规格变更或开启跨VPC后总占用IP数量：
        传入参数loadbalancer_id，及l7_flavor_id不为空或ip_target_enable为true。
        
        - 计算创建LB所需IP数量：传入参数availability_zone_id，
        及可选参数l7_flavor_id、ip_target_enable、ip_version，不能传loadbalancer_id。
        
        说明：
        - 计算出来的预占IP数大于等于最终实际占用的IP数。
        - 总占用IP数量，即整个LB所占用的IP数量。
        
        [不支持传入l7_flavor_id](tag:hcso,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountPreoccupyIpNum
        :type request: :class:`huaweicloudsdkelb.v3.CountPreoccupyIpNumRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CountPreoccupyIpNumResponse`
        """
        http_info = self._count_preoccupy_ip_num_http_info(request)
        return self._call_api(**http_info)

    def count_preoccupy_ip_num_invoker(self, request):
        http_info = self._count_preoccupy_ip_num_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_preoccupy_ip_num_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/preoccupy-ip-num",
            "request_type": request.__class__.__name__,
            "response_type": "CountPreoccupyIpNumResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'l7_flavor_id' in local_var_params:
            query_params.append(('l7_flavor_id', local_var_params['l7_flavor_id']))
        if 'ip_target_enable' in local_var_params:
            query_params.append(('ip_target_enable', local_var_params['ip_target_enable']))
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))
            collection_formats['availability_zone_id'] = 'multi'

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

    def create_ip_group(self, request):
        """创建IP地址组

        创建IP地址组。输入的ip可为ip地址或者CIDR子网，支持IPV4和IPV6。
        
        需要注意0.0.0.0与0.0.0.0/32视为重复，0:0:0:0:0:0:0:1与::1与::1/128视为重复，只会保存其中一个。
        
        [荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIpGroup
        :type request: :class:`huaweicloudsdkelb.v3.CreateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateIpGroupResponse`
        """
        http_info = self._create_ip_group_http_info(request)
        return self._call_api(**http_info)

    def create_ip_group_invoker(self, request):
        http_info = self._create_ip_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ip_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/ipgroups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIpGroupResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_ip_group(self, request):
        """删除IP地址组

        删除ip地址组。[荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIpGroup
        :type request: :class:`huaweicloudsdkelb.v3.DeleteIpGroupRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteIpGroupResponse`
        """
        http_info = self._delete_ip_group_http_info(request)
        return self._call_api(**http_info)

    def delete_ip_group_invoker(self, request):
        http_info = self._delete_ip_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ip_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elb/ipgroups/{ipgroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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

    def list_ip_groups(self, request):
        """查询IP地址组列表

        查询IP地址组列表。[荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpGroups
        :type request: :class:`huaweicloudsdkelb.v3.ListIpGroupsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListIpGroupsResponse`
        """
        http_info = self._list_ip_groups_http_info(request)
        return self._call_api(**http_info)

    def list_ip_groups_invoker(self, request):
        http_info = self._list_ip_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ip_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/ipgroups",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'ip_list' in local_var_params:
            query_params.append(('ip_list', local_var_params['ip_list']))
            collection_formats['ip_list'] = 'multi'

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

    def show_ip_group(self, request):
        """查询IP地址组详情

        获取IP地址组详情。[荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIpGroup
        :type request: :class:`huaweicloudsdkelb.v3.ShowIpGroupRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowIpGroupResponse`
        """
        http_info = self._show_ip_group_http_info(request)
        return self._call_api(**http_info)

    def show_ip_group_invoker(self, request):
        http_info = self._show_ip_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ip_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elb/ipgroups/{ipgroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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

    def update_ip_group(self, request):
        """更新IP地址组

        更新IP地址组，只支持全量更新IP。即IP地址组中的ip_list将被全量覆盖，不在请求参数中的IP地址将被移除。
        输入的ip可为ip地址或者CIDR子网，支持IPV4和IPV6。
        
        需要注意0.0.0.0与0.0.0.0/32视为重复，0:0:0:0:0:0:0:1与::1与::1/128视为重复，只会保存其中一个。
        
        [荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIpGroup
        :type request: :class:`huaweicloudsdkelb.v3.UpdateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateIpGroupResponse`
        """
        http_info = self._update_ip_group_http_info(request)
        return self._call_api(**http_info)

    def update_ip_group_invoker(self, request):
        http_info = self._update_ip_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ip_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elb/ipgroups/{ipgroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_ip_list(self, request):
        """更新IP地址组的IP列表项

        添加新的IP地址到IP地址组的IP列表信息，或更新已有IP地址的描述。[荷兰region不支持该API](tag:dt,dt_test)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIpList
        :type request: :class:`huaweicloudsdkelb.v3.UpdateIpListRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateIpListResponse`
        """
        http_info = self._update_ip_list_http_info(request)
        return self._call_api(**http_info)

    def update_ip_list_invoker(self, request):
        http_info = self._update_ip_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ip_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elb/ipgroups/{ipgroup_id}/iplist/create-or-update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIpListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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
            ['application/json;charset=UTF-8'])

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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
