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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkhss'")


class HssAsyncClient(Client):
    def __init__(self):
        super(HssAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkhss.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "HssAsyncClient":
                raise TypeError("client type error, support client type is HssAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_hosts_group_async(self, request):
        """创建服务器组

        创建服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddHostsGroup
        :type request: :class:`huaweicloudsdkhss.v5.AddHostsGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddHostsGroupResponse`
        """
        http_info = self._add_hosts_group_http_info(request)
        return self._call_api(**http_info)

    def add_hosts_group_async_invoker(self, request):
        http_info = self._add_hosts_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_hosts_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/host-management/groups",
            "request_type": request.__class__.__name__,
            "response_type": "AddHostsGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def associate_policy_group_async(self, request):
        """部署策略组

        部署策略组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociatePolicyGroup
        :type request: :class:`huaweicloudsdkhss.v5.AssociatePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AssociatePolicyGroupResponse`
        """
        http_info = self._associate_policy_group_http_info(request)
        return self._call_api(**http_info)

    def associate_policy_group_async_invoker(self, request):
        http_info = self._associate_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_policy_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/policy/deploy",
            "request_type": request.__class__.__name__,
            "response_type": "AssociatePolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def batch_create_tags_async(self, request):
        """批量创建标签

        批量创建标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateTags
        :type request: :class:`huaweicloudsdkhss.v5.BatchCreateTagsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchCreateTagsResponse`
        """
        http_info = self._batch_create_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_tags_async_invoker(self, request):
        http_info = self._batch_create_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def batch_scan_swr_image_async(self, request):
        """镜像仓库镜像批量扫描

        镜像仓库镜像批量扫描
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchScanSwrImage
        :type request: :class:`huaweicloudsdkhss.v5.BatchScanSwrImageRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchScanSwrImageResponse`
        """
        http_info = self._batch_scan_swr_image_http_info(request)
        return self._call_api(**http_info)

    def batch_scan_swr_image_async_invoker(self, request):
        http_info = self._batch_scan_swr_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_scan_swr_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/image/batch-scan",
            "request_type": request.__class__.__name__,
            "response_type": "BatchScanSwrImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def change_blocked_ip_async(self, request):
        """解除已拦截IP

        解除已拦截IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeBlockedIp
        :type request: :class:`huaweicloudsdkhss.v5.ChangeBlockedIpRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeBlockedIpResponse`
        """
        http_info = self._change_blocked_ip_http_info(request)
        return self._call_api(**http_info)

    def change_blocked_ip_async_invoker(self, request):
        http_info = self._change_blocked_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_blocked_ip_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/event/blocked-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeBlockedIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def change_check_rule_action_async(self, request):
        """对未通过的配置检查项进行忽略/取消忽略/修复/验证操作

        对未通过的配置检查项进行忽略/取消忽略/修复/验证操作
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeCheckRuleAction
        :type request: :class:`huaweicloudsdkhss.v5.ChangeCheckRuleActionRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeCheckRuleActionResponse`
        """
        http_info = self._change_check_rule_action_http_info(request)
        return self._call_api(**http_info)

    def change_check_rule_action_async_invoker(self, request):
        http_info = self._change_check_rule_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_check_rule_action_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/baseline/check-rule/action",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeCheckRuleActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

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

    def change_event_async(self, request):
        """处理告警事件

        处理告警事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeEvent
        :type request: :class:`huaweicloudsdkhss.v5.ChangeEventRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeEventResponse`
        """
        http_info = self._change_event_http_info(request)
        return self._call_api(**http_info)

    def change_event_async_invoker(self, request):
        http_info = self._change_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/event/operate",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'container_id' in local_var_params:
            query_params.append(('container_id', local_var_params['container_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def change_hosts_group_async(self, request):
        """编辑服务器组

        编辑服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeHostsGroup
        :type request: :class:`huaweicloudsdkhss.v5.ChangeHostsGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeHostsGroupResponse`
        """
        http_info = self._change_hosts_group_http_info(request)
        return self._call_api(**http_info)

    def change_hosts_group_async_invoker(self, request):
        http_info = self._change_hosts_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_hosts_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/host-management/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeHostsGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def change_isolated_file_async(self, request):
        """恢复已隔离文件

        恢复已隔离文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeIsolatedFile
        :type request: :class:`huaweicloudsdkhss.v5.ChangeIsolatedFileRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeIsolatedFileResponse`
        """
        http_info = self._change_isolated_file_http_info(request)
        return self._call_api(**http_info)

    def change_isolated_file_async_invoker(self, request):
        http_info = self._change_isolated_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_isolated_file_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/event/isolated-file",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeIsolatedFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def change_vul_scan_policy_async(self, request):
        """修改漏洞扫描策略

        修改漏洞扫描策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeVulScanPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ChangeVulScanPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeVulScanPolicyResponse`
        """
        http_info = self._change_vul_scan_policy_http_info(request)
        return self._call_api(**http_info)

    def change_vul_scan_policy_async_invoker(self, request):
        http_info = self._change_vul_scan_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_vul_scan_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/vulnerability/scan-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeVulScanPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def change_vul_status_async(self, request):
        """修改漏洞的状态

        修改漏洞的状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeVulStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangeVulStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeVulStatusResponse`
        """
        http_info = self._change_vul_status_http_info(request)
        return self._call_api(**http_info)

    def change_vul_status_async_invoker(self, request):
        http_info = self._change_vul_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_vul_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/vulnerability/status",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeVulStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def create_quotas_order_async(self, request):
        """HSS服务创建订单订购配额

        HSS服务创建订单订购配额，只支持包周期计费模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateQuotasOrder
        :type request: :class:`huaweicloudsdkhss.v5.CreateQuotasOrderRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateQuotasOrderResponse`
        """
        http_info = self._create_quotas_order_http_info(request)
        return self._call_api(**http_info)

    def create_quotas_order_async_invoker(self, request):
        http_info = self._create_quotas_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_quotas_order_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/quotas/orders",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQuotasOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def create_vulnerability_scan_task_async(self, request):
        """创建漏洞扫描任务

        创建漏洞扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVulnerabilityScanTask
        :type request: :class:`huaweicloudsdkhss.v5.CreateVulnerabilityScanTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateVulnerabilityScanTaskResponse`
        """
        http_info = self._create_vulnerability_scan_task_http_info(request)
        return self._call_api(**http_info)

    def create_vulnerability_scan_task_async_invoker(self, request):
        http_info = self._create_vulnerability_scan_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vulnerability_scan_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vulnerability/scan-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVulnerabilityScanTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def delete_hosts_group_async(self, request):
        """删除服务器组

        删除服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHostsGroup
        :type request: :class:`huaweicloudsdkhss.v5.DeleteHostsGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteHostsGroupResponse`
        """
        http_info = self._delete_hosts_group_http_info(request)
        return self._call_api(**http_info)

    def delete_hosts_group_async_invoker(self, request):
        http_info = self._delete_hosts_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_hosts_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/host-management/groups",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHostsGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def delete_resource_instance_tag_async(self, request):
        """删除资源标签

        删除单个资源下的标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceInstanceTag
        :type request: :class:`huaweicloudsdkhss.v5.DeleteResourceInstanceTagRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteResourceInstanceTagResponse`
        """
        http_info = self._delete_resource_instance_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_instance_tag_async_invoker(self, request):
        http_info = self._delete_resource_instance_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_resource_instance_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/{resource_type}/{resource_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceInstanceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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

    def list_alarm_white_list_async(self, request):
        """查询告警白名单列表

        查询告警白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.ListAlarmWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAlarmWhiteListResponse`
        """
        http_info = self._list_alarm_white_list_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_white_list_async_invoker(self, request):
        http_info = self._list_alarm_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_white_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/white-list/alarm",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmWhiteListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'hash' in local_var_params:
            query_params.append(('hash', local_var_params['hash']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_app_change_histories_async(self, request):
        """获取软件信息的历史变动记录

        获取软件信息的历史变动记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppChangeHistories
        :type request: :class:`huaweicloudsdkhss.v5.ListAppChangeHistoriesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppChangeHistoriesResponse`
        """
        http_info = self._list_app_change_histories_http_info(request)
        return self._call_api(**http_info)

    def list_app_change_histories_async_invoker(self, request):
        http_info = self._list_app_change_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_change_histories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/app/change-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppChangeHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'variation_type' in local_var_params:
            query_params.append(('variation_type', local_var_params['variation_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_app_statistics_async(self, request):
        """查询软件列表

        查询软件列表，支持通过软件名称查询对应的服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListAppStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppStatisticsResponse`
        """
        http_info = self._list_app_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_app_statistics_async_invoker(self, request):
        http_info = self._list_app_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/app/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def list_apps_async(self, request):
        """查询软件的服务器列表

        查询软件的服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkhss.v5.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppsResponse`
        """
        http_info = self._list_apps_http_info(request)
        return self._call_api(**http_info)

    def list_apps_async_invoker(self, request):
        http_info = self._list_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'install_dir' in local_var_params:
            query_params.append(('install_dir', local_var_params['install_dir']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'part_match' in local_var_params:
            query_params.append(('part_match', local_var_params['part_match']))

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

    def list_auto_launch_change_histories_async(self, request):
        """获取自启动项的历史变动记录

        获取自启动项的历史变动记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAutoLaunchChangeHistories
        :type request: :class:`huaweicloudsdkhss.v5.ListAutoLaunchChangeHistoriesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAutoLaunchChangeHistoriesResponse`
        """
        http_info = self._list_auto_launch_change_histories_http_info(request)
        return self._call_api(**http_info)

    def list_auto_launch_change_histories_async_invoker(self, request):
        http_info = self._list_auto_launch_change_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_auto_launch_change_histories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/auto-launch/change-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutoLaunchChangeHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'auto_launch_name' in local_var_params:
            query_params.append(('auto_launch_name', local_var_params['auto_launch_name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'variation_type' in local_var_params:
            query_params.append(('variation_type', local_var_params['variation_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_auto_launch_statistics_async(self, request):
        """查询自启动项信息

        查询自启动信息，支持通过传入自启动名称查询启动类型和服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAutoLaunchStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListAutoLaunchStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAutoLaunchStatisticsResponse`
        """
        http_info = self._list_auto_launch_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_auto_launch_statistics_async_invoker(self, request):
        http_info = self._list_auto_launch_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_auto_launch_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/auto-launch/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutoLaunchStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def list_auto_launchs_async(self, request):
        """查询自启动项的服务列表

        查询自启动项的服务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAutoLaunchs
        :type request: :class:`huaweicloudsdkhss.v5.ListAutoLaunchsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAutoLaunchsResponse`
        """
        http_info = self._list_auto_launchs_http_info(request)
        return self._call_api(**http_info)

    def list_auto_launchs_async_invoker(self, request):
        http_info = self._list_auto_launchs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_auto_launchs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/auto-launchs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutoLaunchsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'part_match' in local_var_params:
            query_params.append(('part_match', local_var_params['part_match']))

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

    def list_blocked_ip_async(self, request):
        """查询已拦截IP列表

        查询已拦截IP列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBlockedIp
        :type request: :class:`huaweicloudsdkhss.v5.ListBlockedIpRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListBlockedIpResponse`
        """
        http_info = self._list_blocked_ip_http_info(request)
        return self._call_api(**http_info)

    def list_blocked_ip_async_invoker(self, request):
        http_info = self._list_blocked_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_blocked_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/blocked-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ListBlockedIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'src_ip' in local_var_params:
            query_params.append(('src_ip', local_var_params['src_ip']))
        if 'intercept_status' in local_var_params:
            query_params.append(('intercept_status', local_var_params['intercept_status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_container_nodes_async(self, request):
        """查询容器节点列表

        查询容器节点列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainerNodes
        :type request: :class:`huaweicloudsdkhss.v5.ListContainerNodesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainerNodesResponse`
        """
        http_info = self._list_container_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_container_nodes_async_invoker(self, request):
        http_info = self._list_container_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_container_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainerNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'container_tags' in local_var_params:
            query_params.append(('container_tags', local_var_params['container_tags']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_containers_async(self, request):
        """查询容器基本信息列表

        查询容器基本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainers
        :type request: :class:`huaweicloudsdkhss.v5.ListContainersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainersResponse`
        """
        http_info = self._list_containers_http_info(request)
        return self._call_api(**http_info)

    def list_containers_async_invoker(self, request):
        http_info = self._list_containers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_containers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'pod_name' in local_var_params:
            query_params.append(('pod_name', local_var_params['pod_name']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'cluster_container' in local_var_params:
            query_params.append(('cluster_container', local_var_params['cluster_container']))
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

    def list_host_groups_async(self, request):
        """查询服务器组列表

        查询服务器组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostGroups
        :type request: :class:`huaweicloudsdkhss.v5.ListHostGroupsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostGroupsResponse`
        """
        http_info = self._list_host_groups_http_info(request)
        return self._call_api(**http_info)

    def list_host_groups_async_invoker(self, request):
        http_info = self._list_host_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/host-management/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_host_protect_history_info_async(self, request):
        """查询主机静态网页防篡改防护动态

        查询主机静态网页防篡改防护动态：展示服务器名称、服务器ip、防护策略、检测时间、防护文件、事件描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostProtectHistoryInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListHostProtectHistoryInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostProtectHistoryInfoResponse`
        """
        http_info = self._list_host_protect_history_info_http_info(request)
        return self._call_api(**http_info)

    def list_host_protect_history_info_async_invoker(self, request):
        http_info = self._list_host_protect_history_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_protect_history_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/webtamper/static/protect-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostProtectHistoryInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'file_operation' in local_var_params:
            query_params.append(('file_operation', local_var_params['file_operation']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_host_rasp_protect_history_info_async(self, request):
        """查询主机动态网页防篡改防护动态

        查询主机动态网页防篡改防护动态：包含告警级别、服务器ip、服务器名称、威胁类型、告警时间、攻击源ip、攻击源url信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostRaspProtectHistoryInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListHostRaspProtectHistoryInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostRaspProtectHistoryInfoResponse`
        """
        http_info = self._list_host_rasp_protect_history_info_http_info(request)
        return self._call_api(**http_info)

    def list_host_rasp_protect_history_info_async_invoker(self, request):
        http_info = self._list_host_rasp_protect_history_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_rasp_protect_history_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/webtamper/rasp/protect-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostRaspProtectHistoryInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'alarm_level' in local_var_params:
            query_params.append(('alarm_level', local_var_params['alarm_level']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_host_status_async(self, request):
        """查询云服务器列表

        查询云服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListHostStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostStatusResponse`
        """
        http_info = self._list_host_status_http_info(request)
        return self._call_api(**http_info)

    def list_host_status_async_invoker(self, request):
        http_info = self._list_host_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/host-management/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'detect_result' in local_var_params:
            query_params.append(('detect_result', local_var_params['detect_result']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_status' in local_var_params:
            query_params.append(('host_status', local_var_params['host_status']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'ip_addr' in local_var_params:
            query_params.append(('ip_addr', local_var_params['ip_addr']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'has_intrusion' in local_var_params:
            query_params.append(('has_intrusion', local_var_params['has_intrusion']))
        if 'policy_group_id' in local_var_params:
            query_params.append(('policy_group_id', local_var_params['policy_group_id']))
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'refresh' in local_var_params:
            query_params.append(('refresh', local_var_params['refresh']))
        if 'above_version' in local_var_params:
            query_params.append(('above_version', local_var_params['above_version']))
        if 'outside_host' in local_var_params:
            query_params.append(('outside_host', local_var_params['outside_host']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'server_group' in local_var_params:
            query_params.append(('server_group', local_var_params['server_group']))
        if 'agent_upgradable' in local_var_params:
            query_params.append(('agent_upgradable', local_var_params['agent_upgradable']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_host_vuls_async(self, request):
        """查询单台服务器漏洞信息

        查询单台服务器漏洞信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostVuls
        :type request: :class:`huaweicloudsdkhss.v5.ListHostVulsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostVulsResponse`
        """
        http_info = self._list_host_vuls_http_info(request)
        return self._call_api(**http_info)

    def list_host_vuls_async_invoker(self, request):
        http_info = self._list_host_vuls_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_vuls_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/host/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostVulsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'repair_priority' in local_var_params:
            query_params.append(('repair_priority', local_var_params['repair_priority']))

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

    def list_image_local_async(self, request):
        """本地镜像列表查询

        本地镜像列表查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageLocal
        :type request: :class:`huaweicloudsdkhss.v5.ListImageLocalRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListImageLocalResponse`
        """
        http_info = self._list_image_local_http_info(request)
        return self._call_api(**http_info)

    def list_image_local_async_invoker(self, request):
        http_info = self._list_image_local_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_local_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/local-repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageLocalResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'image_version' in local_var_params:
            query_params.append(('image_version', local_var_params['image_version']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'scan_status' in local_var_params:
            query_params.append(('scan_status', local_var_params['scan_status']))
        if 'local_image_type' in local_var_params:
            query_params.append(('local_image_type', local_var_params['local_image_type']))
        if 'image_size' in local_var_params:
            query_params.append(('image_size', local_var_params['image_size']))
        if 'start_latest_update_time' in local_var_params:
            query_params.append(('start_latest_update_time', local_var_params['start_latest_update_time']))
        if 'end_latest_update_time' in local_var_params:
            query_params.append(('end_latest_update_time', local_var_params['end_latest_update_time']))
        if 'start_latest_scan_time' in local_var_params:
            query_params.append(('start_latest_scan_time', local_var_params['start_latest_scan_time']))
        if 'end_latest_scan_time' in local_var_params:
            query_params.append(('end_latest_scan_time', local_var_params['end_latest_scan_time']))
        if 'has_vul' in local_var_params:
            query_params.append(('has_vul', local_var_params['has_vul']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'container_id' in local_var_params:
            query_params.append(('container_id', local_var_params['container_id']))
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'pod_id' in local_var_params:
            query_params.append(('pod_id', local_var_params['pod_id']))
        if 'pod_name' in local_var_params:
            query_params.append(('pod_name', local_var_params['pod_name']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

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

    def list_image_risk_config_rules_async(self, request):
        """查询镜像指定安全配置项的检查项列表

        查询镜像指定安全配置项的检查项列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageRiskConfigRules
        :type request: :class:`huaweicloudsdkhss.v5.ListImageRiskConfigRulesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListImageRiskConfigRulesResponse`
        """
        http_info = self._list_image_risk_config_rules_http_info(request)
        return self._call_api(**http_info)

    def list_image_risk_config_rules_async_invoker(self, request):
        http_info = self._list_image_risk_config_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_risk_config_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/baseline/risk-configs/{check_name}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageRiskConfigRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'image_version' in local_var_params:
            query_params.append(('image_version', local_var_params['image_version']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'result_type' in local_var_params:
            query_params.append(('result_type', local_var_params['result_type']))
        if 'check_rule_name' in local_var_params:
            query_params.append(('check_rule_name', local_var_params['check_rule_name']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_image_risk_configs_async(self, request):
        """查询镜像安全配置检测结果列表

        查询镜像安全配置检测结果列表,当前支持检测CentOS 7、Debian 10、EulerOS和Ubuntu16镜像的系统配置项、SSH应用配置项。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageRiskConfigs
        :type request: :class:`huaweicloudsdkhss.v5.ListImageRiskConfigsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListImageRiskConfigsResponse`
        """
        http_info = self._list_image_risk_configs_http_info(request)
        return self._call_api(**http_info)

    def list_image_risk_configs_async_invoker(self, request):
        http_info = self._list_image_risk_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_risk_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/baseline/risk-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageRiskConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'image_version' in local_var_params:
            query_params.append(('image_version', local_var_params['image_version']))
        if 'check_name' in local_var_params:
            query_params.append(('check_name', local_var_params['check_name']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_image_vulnerabilities_async(self, request):
        """查询镜像的漏洞信息

        查询镜像的漏洞信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageVulnerabilities
        :type request: :class:`huaweicloudsdkhss.v5.ListImageVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListImageVulnerabilitiesResponse`
        """
        http_info = self._list_image_vulnerabilities_http_info(request)
        return self._call_api(**http_info)

    def list_image_vulnerabilities_async_invoker(self, request):
        http_info = self._list_image_vulnerabilities_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_vulnerabilities_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/{image_id}/vulnerabilities",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageVulnerabilitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'tag_name' in local_var_params:
            query_params.append(('tag_name', local_var_params['tag_name']))
        if 'repair_necessity' in local_var_params:
            query_params.append(('repair_necessity', local_var_params['repair_necessity']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_isolated_file_async(self, request):
        """查询已隔离文件列表

        查询已隔离文件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIsolatedFile
        :type request: :class:`huaweicloudsdkhss.v5.ListIsolatedFileRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListIsolatedFileResponse`
        """
        http_info = self._list_isolated_file_http_info(request)
        return self._call_api(**http_info)

    def list_isolated_file_async_invoker(self, request):
        http_info = self._list_isolated_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_isolated_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/isolated-file",
            "request_type": request.__class__.__name__,
            "response_type": "ListIsolatedFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'file_hash' in local_var_params:
            query_params.append(('file_hash', local_var_params['file_hash']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_jar_package_host_info_async(self, request):
        """查询指定中间件的服务器列表

        查询指定中间件的服务器列表，通过传入中间件名称参数，返回对应的中间件服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJarPackageHostInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListJarPackageHostInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListJarPackageHostInfoResponse`
        """
        http_info = self._list_jar_package_host_info_http_info(request)
        return self._call_api(**http_info)

    def list_jar_package_host_info_async_invoker(self, request):
        http_info = self._list_jar_package_host_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_jar_package_host_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/midwares/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListJarPackageHostInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'part_match' in local_var_params:
            query_params.append(('part_match', local_var_params['part_match']))

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

    def list_jar_package_statistics_async(self, request):
        """查询中间件列表

        查询中间件列表，支持通过中间件名称查询对应的服务器树
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJarPackageStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListJarPackageStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListJarPackageStatisticsResponse`
        """
        http_info = self._list_jar_package_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_jar_package_statistics_async_invoker(self, request):
        http_info = self._list_jar_package_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_jar_package_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/midwares",
            "request_type": request.__class__.__name__,
            "response_type": "ListJarPackageStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
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

    def list_password_complexity_async(self, request):
        """查询口令复杂度策略检测报告

        查询口令复杂度策略检测报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPasswordComplexity
        :type request: :class:`huaweicloudsdkhss.v5.ListPasswordComplexityRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPasswordComplexityResponse`
        """
        http_info = self._list_password_complexity_http_info(request)
        return self._call_api(**http_info)

    def list_password_complexity_async_invoker(self, request):
        http_info = self._list_password_complexity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_password_complexity_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/password-complexity",
            "request_type": request.__class__.__name__,
            "response_type": "ListPasswordComplexityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
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

    def list_policy_group_async(self, request):
        """查询策略组列表

        查询策略组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyGroup
        :type request: :class:`huaweicloudsdkhss.v5.ListPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPolicyGroupResponse`
        """
        http_info = self._list_policy_group_http_info(request)
        return self._call_api(**http_info)

    def list_policy_group_async_invoker(self, request):
        http_info = self._list_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/policy/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'container_mode' in local_var_params:
            query_params.append(('container_mode', local_var_params['container_mode']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_port_host_async(self, request):
        """资产指纹-端口-服务器列表

        具备该端口的主机/容器信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPortHost
        :type request: :class:`huaweicloudsdkhss.v5.ListPortHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPortHostResponse`
        """
        http_info = self._list_port_host_http_info(request)
        return self._call_api(**http_info)

    def list_port_host_async_invoker(self, request):
        http_info = self._list_port_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_port_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/ports/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListPortHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
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

    def list_port_statistics_async(self, request):
        """查询开放端口统计信息

        查询开放端口列表，支持通过传入端口或协议类型查询服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPortStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListPortStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPortStatisticsResponse`
        """
        http_info = self._list_port_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_port_statistics_async_invoker(self, request):
        http_info = self._list_port_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_port_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/port/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListPortStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'port_string' in local_var_params:
            query_params.append(('port_string', local_var_params['port_string']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def list_ports_async(self, request):
        """查询单服务器的开放端口列表

        查询单服务器的开放端口列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPorts
        :type request: :class:`huaweicloudsdkhss.v5.ListPortsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPortsResponse`
        """
        http_info = self._list_ports_http_info(request)
        return self._call_api(**http_info)

    def list_ports_async_invoker(self, request):
        http_info = self._list_ports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ports_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/ports",
            "request_type": request.__class__.__name__,
            "response_type": "ListPortsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def list_process_statistics_async(self, request):
        """查询进程列表

        查询进程列表，通过传入进程路径参数查询对应的服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProcessStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListProcessStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProcessStatisticsResponse`
        """
        http_info = self._list_process_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_process_statistics_async_invoker(self, request):
        http_info = self._list_process_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_process_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/process/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListProcessStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def list_processes_host_async(self, request):
        """资产指纹-进程-服务器列表

        具备该进程的主机/容器信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProcessesHost
        :type request: :class:`huaweicloudsdkhss.v5.ListProcessesHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProcessesHostResponse`
        """
        http_info = self._list_processes_host_http_info(request)
        return self._call_api(**http_info)

    def list_processes_host_async_invoker(self, request):
        http_info = self._list_processes_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_processes_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/processes/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListProcessesHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
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

    def list_protection_policy_async(self, request):
        """查询勒索病毒的防护策略列表

        查询勒索病毒的防护策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ListProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProtectionPolicyResponse`
        """
        http_info = self._list_protection_policy_http_info(request)
        return self._call_api(**http_info)

    def list_protection_policy_async_invoker(self, request):
        http_info = self._list_protection_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_protection_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/ransomware/protection/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListProtectionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
        if 'protect_policy_id' in local_var_params:
            query_params.append(('protect_policy_id', local_var_params['protect_policy_id']))
        if 'operating_system' in local_var_params:
            query_params.append(('operating_system', local_var_params['operating_system']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_protection_server_async(self, request):
        """查询勒索防护服务器列表

        查询勒索防护服务器列表，与云备份服务配合使用。因此使用勒索相关接口之前确保该局点有云备份服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectionServer
        :type request: :class:`huaweicloudsdkhss.v5.ListProtectionServerRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProtectionServerResponse`
        """
        http_info = self._list_protection_server_http_info(request)
        return self._call_api(**http_info)

    def list_protection_server_async_invoker(self, request):
        http_info = self._list_protection_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_protection_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/ransomware/server",
            "request_type": request.__class__.__name__,
            "response_type": "ListProtectionServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_status' in local_var_params:
            query_params.append(('host_status', local_var_params['host_status']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_quotas_detail_async(self, request):
        """查询配额详情

        查询配额详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotasDetail
        :type request: :class:`huaweicloudsdkhss.v5.ListQuotasDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListQuotasDetailResponse`
        """
        http_info = self._list_quotas_detail_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_detail_async_invoker(self, request):
        http_info = self._list_quotas_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/billing/quotas-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'quota_status' in local_var_params:
            query_params.append(('quota_status', local_var_params['quota_status']))
        if 'used_status' in local_var_params:
            query_params.append(('used_status', local_var_params['used_status']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_risk_config_check_rules_async(self, request):
        """查询指定安全配置项的检查项列表

        查询指定安全配置项的检查项列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRiskConfigCheckRules
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigCheckRulesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigCheckRulesResponse`
        """
        http_info = self._list_risk_config_check_rules_http_info(request)
        return self._call_api(**http_info)

    def list_risk_config_check_rules_async_invoker(self, request):
        http_info = self._list_risk_config_check_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_risk_config_check_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/risk-config/{check_name}/check-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRiskConfigCheckRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'result_type' in local_var_params:
            query_params.append(('result_type', local_var_params['result_type']))
        if 'check_rule_name' in local_var_params:
            query_params.append(('check_rule_name', local_var_params['check_rule_name']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
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

    def list_risk_config_hosts_async(self, request):
        """查询指定安全配置项的受影响服务器列表

        查询指定安全配置项的受影响服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRiskConfigHosts
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigHostsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigHostsResponse`
        """
        http_info = self._list_risk_config_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_risk_config_hosts_async_invoker(self, request):
        http_info = self._list_risk_config_hosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_risk_config_hosts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/risk-config/{check_name}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListRiskConfigHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
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

    def list_risk_configs_async(self, request):
        """查询租户的服务器安全配置检测结果列表

        查询租户的服务器安全配置检测结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRiskConfigs
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigsResponse`
        """
        http_info = self._list_risk_configs_http_info(request)
        return self._call_api(**http_info)

    def list_risk_configs_async_invoker(self, request):
        http_info = self._list_risk_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_risk_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/risk-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListRiskConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'check_name' in local_var_params:
            query_params.append(('check_name', local_var_params['check_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
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

    def list_security_events_async(self, request):
        """查入侵事件列表

        查入侵事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityEvents
        :type request: :class:`huaweicloudsdkhss.v5.ListSecurityEventsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListSecurityEventsResponse`
        """
        http_info = self._list_security_events_http_info(request)
        return self._call_api(**http_info)

    def list_security_events_async_invoker(self, request):
        http_info = self._list_security_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_security_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecurityEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'event_types' in local_var_params:
            query_params.append(('event_types', local_var_params['event_types']))
            collection_formats['event_types'] = 'csv'
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'event_class_ids' in local_var_params:
            query_params.append(('event_class_ids', local_var_params['event_class_ids']))
            collection_formats['event_class_ids'] = 'csv'
        if 'severity_list' in local_var_params:
            query_params.append(('severity_list', local_var_params['severity_list']))
            collection_formats['severity_list'] = 'csv'
        if 'attack_tag' in local_var_params:
            query_params.append(('attack_tag', local_var_params['attack_tag']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'tag_list' in local_var_params:
            query_params.append(('tag_list', local_var_params['tag_list']))
            collection_formats['tag_list'] = 'csv'
        if 'att_ck' in local_var_params:
            query_params.append(('att_ck', local_var_params['att_ck']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_swr_image_repository_async(self, request):
        """查询swr镜像仓库镜像列表

        查询swr镜像仓库镜像列表,如果需要从swr同步最新镜像，需要先调用“从swr同步镜像”接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSwrImageRepository
        :type request: :class:`huaweicloudsdkhss.v5.ListSwrImageRepositoryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListSwrImageRepositoryResponse`
        """
        http_info = self._list_swr_image_repository_http_info(request)
        return self._call_api(**http_info)

    def list_swr_image_repository_async_invoker(self, request):
        http_info = self._list_swr_image_repository_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_swr_image_repository_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/swr-repository",
            "request_type": request.__class__.__name__,
            "response_type": "ListSwrImageRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'image_version' in local_var_params:
            query_params.append(('image_version', local_var_params['image_version']))
        if 'latest_version' in local_var_params:
            query_params.append(('latest_version', local_var_params['latest_version']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'scan_status' in local_var_params:
            query_params.append(('scan_status', local_var_params['scan_status']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
        if 'image_size' in local_var_params:
            query_params.append(('image_size', local_var_params['image_size']))
        if 'start_latest_update_time' in local_var_params:
            query_params.append(('start_latest_update_time', local_var_params['start_latest_update_time']))
        if 'end_latest_update_time' in local_var_params:
            query_params.append(('end_latest_update_time', local_var_params['end_latest_update_time']))
        if 'start_latest_scan_time' in local_var_params:
            query_params.append(('start_latest_scan_time', local_var_params['start_latest_scan_time']))
        if 'end_latest_scan_time' in local_var_params:
            query_params.append(('end_latest_scan_time', local_var_params['end_latest_scan_time']))
        if 'has_malicious_file' in local_var_params:
            query_params.append(('has_malicious_file', local_var_params['has_malicious_file']))
        if 'has_unsafe_setting' in local_var_params:
            query_params.append(('has_unsafe_setting', local_var_params['has_unsafe_setting']))
        if 'has_vul' in local_var_params:
            query_params.append(('has_vul', local_var_params['has_vul']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_user_change_histories_async(self, request):
        """获取账户变动历史信息

        获取账户变动历史记录信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserChangeHistories
        :type request: :class:`huaweicloudsdkhss.v5.ListUserChangeHistoriesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListUserChangeHistoriesResponse`
        """
        http_info = self._list_user_change_histories_http_info(request)
        return self._call_api(**http_info)

    def list_user_change_histories_async_invoker(self, request):
        http_info = self._list_user_change_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_change_histories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/user/change-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserChangeHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'root_permission' in local_var_params:
            query_params.append(('root_permission', local_var_params['root_permission']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'change_type' in local_var_params:
            query_params.append(('change_type', local_var_params['change_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def list_user_statistics_async(self, request):
        """查询账号信息列表

        查询账号信息列表，支持通过传入账号名称参数查询对应的服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListUserStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListUserStatisticsResponse`
        """
        http_info = self._list_user_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_user_statistics_async_invoker(self, request):
        http_info = self._list_user_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/user/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def list_users_async(self, request):
        """查询账号的服务器列表

        查询账号的服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkhss.v5.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_async_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'login_permission' in local_var_params:
            query_params.append(('login_permission', local_var_params['login_permission']))
        if 'root_permission' in local_var_params:
            query_params.append(('root_permission', local_var_params['root_permission']))
        if 'user_group' in local_var_params:
            query_params.append(('user_group', local_var_params['user_group']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'part_match' in local_var_params:
            query_params.append(('part_match', local_var_params['part_match']))

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

    def list_vul_hosts_async(self, request):
        """查询单个漏洞影响的云服务器信息

        查询单个漏洞影响的云服务器信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulHosts
        :type request: :class:`huaweicloudsdkhss.v5.ListVulHostsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulHostsResponse`
        """
        http_info = self._list_vul_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_vul_hosts_async_invoker(self, request):
        http_info = self._list_vul_hosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_hosts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity_level' in local_var_params:
            query_params.append(('severity_level', local_var_params['severity_level']))
        if 'is_affect_business' in local_var_params:
            query_params.append(('is_affect_business', local_var_params['is_affect_business']))
        if 'repair_priority' in local_var_params:
            query_params.append(('repair_priority', local_var_params['repair_priority']))

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

    def list_vul_scan_task_async(self, request):
        """查询漏洞扫描任务列表

        查询漏洞扫描任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulScanTask
        :type request: :class:`huaweicloudsdkhss.v5.ListVulScanTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulScanTaskResponse`
        """
        http_info = self._list_vul_scan_task_http_info(request)
        return self._call_api(**http_info)

    def list_vul_scan_task_async_invoker(self, request):
        http_info = self._list_vul_scan_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_scan_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/scan-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulScanTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'scan_type' in local_var_params:
            query_params.append(('scan_type', local_var_params['scan_type']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'min_start_time' in local_var_params:
            query_params.append(('min_start_time', local_var_params['min_start_time']))
        if 'max_start_time' in local_var_params:
            query_params.append(('max_start_time', local_var_params['max_start_time']))

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

    def list_vul_scan_task_host_async(self, request):
        """查询漏洞扫描任务对应的主机列表

        查询漏洞扫描任务对应的主机列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulScanTaskHost
        :type request: :class:`huaweicloudsdkhss.v5.ListVulScanTaskHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulScanTaskHostResponse`
        """
        http_info = self._list_vul_scan_task_host_http_info(request)
        return self._call_api(**http_info)

    def list_vul_scan_task_host_async_invoker(self, request):
        http_info = self._list_vul_scan_task_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_scan_task_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/scan-task/{task_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulScanTaskHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'scan_status' in local_var_params:
            query_params.append(('scan_status', local_var_params['scan_status']))

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

    def list_vulnerabilities_async(self, request):
        """查询漏洞列表

        查询漏洞列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulnerabilities
        :type request: :class:`huaweicloudsdkhss.v5.ListVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulnerabilitiesResponse`
        """
        http_info = self._list_vulnerabilities_http_info(request)
        return self._call_api(**http_info)

    def list_vulnerabilities_async_invoker(self, request):
        http_info = self._list_vulnerabilities_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vulnerabilities_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/vulnerabilities",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulnerabilitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'repair_priority' in local_var_params:
            query_params.append(('repair_priority', local_var_params['repair_priority']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'cve_id' in local_var_params:
            query_params.append(('cve_id', local_var_params['cve_id']))
        if 'label_list' in local_var_params:
            query_params.append(('label_list', local_var_params['label_list']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))

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

    def list_vulnerability_cve_async(self, request):
        """漏洞对应cve信息

        漏洞对应cve信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulnerabilityCve
        :type request: :class:`huaweicloudsdkhss.v5.ListVulnerabilityCveRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulnerabilityCveResponse`
        """
        http_info = self._list_vulnerability_cve_http_info(request)
        return self._call_api(**http_info)

    def list_vulnerability_cve_async_invoker(self, request):
        http_info = self._list_vulnerability_cve_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vulnerability_cve_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/vulnerability/{vul_id}/cve",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulnerabilityCveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vul_id' in local_var_params:
            path_params['vul_id'] = local_var_params['vul_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def list_weak_password_users_async(self, request):
        """查询弱口令检测结果列表

        查询弱口令检测结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWeakPasswordUsers
        :type request: :class:`huaweicloudsdkhss.v5.ListWeakPasswordUsersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWeakPasswordUsersResponse`
        """
        http_info = self._list_weak_password_users_http_info(request)
        return self._call_api(**http_info)

    def list_weak_password_users_async_invoker(self, request):
        http_info = self._list_weak_password_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_weak_password_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/weak-password-users",
            "request_type": request.__class__.__name__,
            "response_type": "ListWeakPasswordUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
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

    def list_wtp_protect_host_async(self, request):
        """查询防护列表

        查询防护列表：查询网页防篡改主机防护状态列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWtpProtectHost
        :type request: :class:`huaweicloudsdkhss.v5.ListWtpProtectHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWtpProtectHostResponse`
        """
        http_info = self._list_wtp_protect_host_http_info(request)
        return self._call_api(**http_info)

    def list_wtp_protect_host_async_invoker(self, request):
        http_info = self._list_wtp_protect_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_wtp_protect_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/webtamper/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListWtpProtectHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def run_image_synchronize_async(self, request):
        """从SWR服务同步镜像列表

        从SWR服务同步镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageSynchronize
        :type request: :class:`huaweicloudsdkhss.v5.RunImageSynchronizeRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.RunImageSynchronizeResponse`
        """
        http_info = self._run_image_synchronize_http_info(request)
        return self._call_api(**http_info)

    def run_image_synchronize_async_invoker(self, request):
        http_info = self._run_image_synchronize_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_image_synchronize_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/image/synchronize",
            "request_type": request.__class__.__name__,
            "response_type": "RunImageSynchronizeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def set_rasp_switch_async(self, request):
        """开启/关闭动态网页防篡改防护

        开启/关闭动态网页防篡改防护，下发/清空动态网页防篡改策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetRaspSwitch
        :type request: :class:`huaweicloudsdkhss.v5.SetRaspSwitchRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SetRaspSwitchResponse`
        """
        http_info = self._set_rasp_switch_http_info(request)
        return self._call_api(**http_info)

    def set_rasp_switch_async_invoker(self, request):
        http_info = self._set_rasp_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_rasp_switch_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/webtamper/rasp/status",
            "request_type": request.__class__.__name__,
            "response_type": "SetRaspSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def set_wtp_protection_status_info_async(self, request):
        """开启关闭网页防篡改防护

        开启/关闭网页防篡改功能防护，下发/清空网页防篡改策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetWtpProtectionStatusInfo
        :type request: :class:`huaweicloudsdkhss.v5.SetWtpProtectionStatusInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SetWtpProtectionStatusInfoResponse`
        """
        http_info = self._set_wtp_protection_status_info_http_info(request)
        return self._call_api(**http_info)

    def set_wtp_protection_status_info_async_invoker(self, request):
        http_info = self._set_wtp_protection_status_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_wtp_protection_status_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/webtamper/static/status",
            "request_type": request.__class__.__name__,
            "response_type": "SetWtpProtectionStatusInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def show_asset_statistic_async(self, request):
        """统计资产信息，账号、端口、进程等

        资产统计信息，账号、端口、进程等
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAssetStatistic
        :type request: :class:`huaweicloudsdkhss.v5.ShowAssetStatisticRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAssetStatisticResponse`
        """
        http_info = self._show_asset_statistic_http_info(request)
        return self._call_api(**http_info)

    def show_asset_statistic_async_invoker(self, request):
        http_info = self._show_asset_statistic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_asset_statistic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def show_backup_policy_info_async(self, request):
        """查询HSS存储库绑定的备份策略信息

        查询HSS存储库绑定的备份策略信息,确保已经购买了勒索防护存储库，可以从cbr云备份服务进行验证，确保已经存在HSS_projectid命名的存储库已经购买
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackupPolicyInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowBackupPolicyInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowBackupPolicyInfoResponse`
        """
        http_info = self._show_backup_policy_info_http_info(request)
        return self._call_api(**http_info)

    def show_backup_policy_info_async_invoker(self, request):
        http_info = self._show_backup_policy_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_backup_policy_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/backup/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupPolicyInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def show_check_rule_detail_async(self, request):
        """查询配置检查项检测报告

        查询配置检查项检测报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCheckRuleDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowCheckRuleDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowCheckRuleDetailResponse`
        """
        http_info = self._show_check_rule_detail_http_info(request)
        return self._call_api(**http_info)

    def show_check_rule_detail_async_invoker(self, request):
        http_info = self._show_check_rule_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_check_rule_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/check-rule/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCheckRuleDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'check_name' in local_var_params:
            query_params.append(('check_name', local_var_params['check_name']))
        if 'check_type' in local_var_params:
            query_params.append(('check_type', local_var_params['check_type']))
        if 'check_rule_id' in local_var_params:
            query_params.append(('check_rule_id', local_var_params['check_rule_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))

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

    def show_image_check_rule_detail_async(self, request):
        """查询镜像配置检查项检测报告

        查询镜像配置检查项检测报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageCheckRuleDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowImageCheckRuleDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowImageCheckRuleDetailResponse`
        """
        http_info = self._show_image_check_rule_detail_http_info(request)
        return self._call_api(**http_info)

    def show_image_check_rule_detail_async_invoker(self, request):
        http_info = self._show_image_check_rule_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_check_rule_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/baseline/check-rule/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageCheckRuleDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'image_version' in local_var_params:
            query_params.append(('image_version', local_var_params['image_version']))
        if 'check_name' in local_var_params:
            query_params.append(('check_name', local_var_params['check_name']))
        if 'check_type' in local_var_params:
            query_params.append(('check_type', local_var_params['check_type']))
        if 'check_rule_id' in local_var_params:
            query_params.append(('check_rule_id', local_var_params['check_rule_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def show_productdata_offering_infos_async(self, request):
        """查询产商品信息

        查询产商品信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProductdataOfferingInfos
        :type request: :class:`huaweicloudsdkhss.v5.ShowProductdataOfferingInfosRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowProductdataOfferingInfosResponse`
        """
        http_info = self._show_productdata_offering_infos_http_info(request)
        return self._call_api(**http_info)

    def show_productdata_offering_infos_async_invoker(self, request):
        http_info = self._show_productdata_offering_infos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_productdata_offering_infos_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/product/productdata/offering-infos",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProductdataOfferingInfosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'site_code' in local_var_params:
            query_params.append(('site_code', local_var_params['site_code']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def show_resource_quotas_async(self, request):
        """查询配额信息

        查询配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceQuotas
        :type request: :class:`huaweicloudsdkhss.v5.ShowResourceQuotasRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowResourceQuotasResponse`
        """
        http_info = self._show_resource_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_resource_quotas_async_invoker(self, request):
        http_info = self._show_resource_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/billing/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def show_risk_config_detail_async(self, request):
        """查询指定安全配置项的检查结果

        查询指定安全配置项的检查结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRiskConfigDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowRiskConfigDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowRiskConfigDetailResponse`
        """
        http_info = self._show_risk_config_detail_http_info(request)
        return self._call_api(**http_info)

    def show_risk_config_detail_async_invoker(self, request):
        http_info = self._show_risk_config_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_risk_config_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/risk-config/{check_name}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRiskConfigDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
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

    def show_vul_scan_policy_async(self, request):
        """查询漏洞扫描策略

        查询漏洞扫描策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVulScanPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ShowVulScanPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowVulScanPolicyResponse`
        """
        http_info = self._show_vul_scan_policy_http_info(request)
        return self._call_api(**http_info)

    def show_vul_scan_policy_async_invoker(self, request):
        http_info = self._show_vul_scan_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vul_scan_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/scan-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVulScanPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def show_vul_statics_async(self, request):
        """查询漏洞管理统计数据

        查询漏洞管理统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVulStatics
        :type request: :class:`huaweicloudsdkhss.v5.ShowVulStaticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowVulStaticsResponse`
        """
        http_info = self._show_vul_statics_http_info(request)
        return self._call_api(**http_info)

    def show_vul_statics_async_invoker(self, request):
        http_info = self._show_vul_statics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vul_statics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVulStaticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def start_protection_async(self, request):
        """开启勒索病毒防护

        开启勒索病毒防护,请保证该region有cbr云备份服务，勒索服务与云备份服务有关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartProtection
        :type request: :class:`huaweicloudsdkhss.v5.StartProtectionRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.StartProtectionResponse`
        """
        http_info = self._start_protection_http_info(request)
        return self._call_api(**http_info)

    def start_protection_async_invoker(self, request):
        http_info = self._start_protection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_protection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/ransomware/protection/open",
            "request_type": request.__class__.__name__,
            "response_type": "StartProtectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def stop_protection_async(self, request):
        """关闭勒索病毒防护

        关闭勒索病毒防护
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopProtection
        :type request: :class:`huaweicloudsdkhss.v5.StopProtectionRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.StopProtectionResponse`
        """
        http_info = self._stop_protection_http_info(request)
        return self._call_api(**http_info)

    def stop_protection_async_invoker(self, request):
        http_info = self._stop_protection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_protection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/ransomware/protection/close",
            "request_type": request.__class__.__name__,
            "response_type": "StopProtectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def switch_hosts_protect_status_async(self, request):
        """切换防护状态

        切换防护状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchHostsProtectStatus
        :type request: :class:`huaweicloudsdkhss.v5.SwitchHostsProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchHostsProtectStatusResponse`
        """
        http_info = self._switch_hosts_protect_status_http_info(request)
        return self._call_api(**http_info)

    def switch_hosts_protect_status_async_invoker(self, request):
        http_info = self._switch_hosts_protect_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_hosts_protect_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/host-management/protection",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchHostsProtectStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def update_backup_policy_info_async(self, request):
        """修改存储库绑定的备份策略

        修改存储库绑定的备份策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBackupPolicyInfo
        :type request: :class:`huaweicloudsdkhss.v5.UpdateBackupPolicyInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateBackupPolicyInfoResponse`
        """
        http_info = self._update_backup_policy_info_http_info(request)
        return self._call_api(**http_info)

    def update_backup_policy_info_async_invoker(self, request):
        http_info = self._update_backup_policy_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_backup_policy_info_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/backup/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBackupPolicyInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def update_protection_policy_async(self, request):
        """修改勒索防护策略

        修改勒索防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.UpdateProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateProtectionPolicyResponse`
        """
        http_info = self._update_protection_policy_http_info(request)
        return self._call_api(**http_info)

    def update_protection_policy_async_invoker(self, request):
        http_info = self._update_protection_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_protection_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/ransomware/protection/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProtectionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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
