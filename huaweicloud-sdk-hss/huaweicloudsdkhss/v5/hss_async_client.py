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

    def add_baseline_white_list_async(self, request):
        r"""新增基线白名单

        新增基线白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddBaselineWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.AddBaselineWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddBaselineWhiteListResponse`
        """
        http_info = self._add_baseline_white_list_http_info(request)
        return self._call_api(**http_info)

    def add_baseline_white_list_async_invoker(self, request):
        http_info = self._add_baseline_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_baseline_white_list_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/baseline/whitelist",
            "request_type": request.__class__.__name__,
            "response_type": "AddBaselineWhiteListResponse"
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

    def add_cce_integration_protection_async(self, request):
        r"""新建cce集成防护配置

        新建cce集成防护配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddCceIntegrationProtection
        :type request: :class:`huaweicloudsdkhss.v5.AddCceIntegrationProtectionRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddCceIntegrationProtectionResponse`
        """
        http_info = self._add_cce_integration_protection_http_info(request)
        return self._call_api(**http_info)

    def add_cce_integration_protection_async_invoker(self, request):
        http_info = self._add_cce_integration_protection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_cce_integration_protection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/protection-enable",
            "request_type": request.__class__.__name__,
            "response_type": "AddCceIntegrationProtectionResponse"
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

    def add_hosts_group_async(self, request):
        r"""创建服务器组

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

    def add_login_white_list_async(self, request):
        r"""添加登录白名单

        添加登录白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddLoginWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.AddLoginWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddLoginWhiteListResponse`
        """
        http_info = self._add_login_white_list_http_info(request)
        return self._call_api(**http_info)

    def add_login_white_list_async_invoker(self, request):
        http_info = self._add_login_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_login_white_list_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/event/white-list/login",
            "request_type": request.__class__.__name__,
            "response_type": "AddLoginWhiteListResponse"
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

    def add_policy_async(self, request):
        r"""添加防护策略

        添加防护策略：创建防护策略，包含策略名称、相关规则开启状态、防护动作以及检测规则配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddPolicy
        :type request: :class:`huaweicloudsdkhss.v5.AddPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddPolicyResponse`
        """
        http_info = self._add_policy_http_info(request)
        return self._call_api(**http_info)

    def add_policy_async_invoker(self, request):
        http_info = self._add_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/rasp/policy",
            "request_type": request.__class__.__name__,
            "response_type": "AddPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))

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

    def add_protection_policy_async(self, request):
        r"""添加防护策略

        添加防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.AddProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddProtectionPolicyResponse`
        """
        http_info = self._add_protection_policy_http_info(request)
        return self._call_api(**http_info)

    def add_protection_policy_async_invoker(self, request):
        http_info = self._add_protection_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_protection_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/ransomware/protection/policy",
            "request_type": request.__class__.__name__,
            "response_type": "AddProtectionPolicyResponse"
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

    def add_system_user_white_list_async(self, request):
        r"""添加系统用户白名单

        添加系统用户白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddSystemUserWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.AddSystemUserWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddSystemUserWhiteListResponse`
        """
        http_info = self._add_system_user_white_list_http_info(request)
        return self._call_api(**http_info)

    def add_system_user_white_list_async_invoker(self, request):
        http_info = self._add_system_user_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_system_user_white_list_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/event/white-list/userlist",
            "request_type": request.__class__.__name__,
            "response_type": "AddSystemUserWhiteListResponse"
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

    def batch_add_accounts_async(self, request):
        r"""批量添加账号

        批量添加账号
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddAccounts
        :type request: :class:`huaweicloudsdkhss.v5.BatchAddAccountsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchAddAccountsResponse`
        """
        http_info = self._batch_add_accounts_http_info(request)
        return self._call_api(**http_info)

    def batch_add_accounts_async_invoker(self, request):
        http_info = self._batch_add_accounts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_accounts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/setting/account/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddAccountsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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
        r"""批量创建标签

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
        r"""镜像仓库镜像批量扫描

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

    def batch_start_protection_async(self, request):
        r"""批量开启勒索病毒防护2.0

        批量开启勒索病毒防护，若开启备份防护，请保证该region有cbr云备份服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartProtection
        :type request: :class:`huaweicloudsdkhss.v5.BatchStartProtectionRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchStartProtectionResponse`
        """
        http_info = self._batch_start_protection_http_info(request)
        return self._call_api(**http_info)

    def batch_start_protection_async_invoker(self, request):
        http_info = self._batch_start_protection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_protection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/ransomware/protection/batch-open",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartProtectionResponse"
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

    def change_agent_auto_upgrade_status_async(self, request):
        r"""开启或关闭“Agent自动升级”配置开关

        开启或关闭“Agent自动升级”配置开关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAgentAutoUpgradeStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangeAgentAutoUpgradeStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeAgentAutoUpgradeStatusResponse`
        """
        http_info = self._change_agent_auto_upgrade_status_http_info(request)
        return self._call_api(**http_info)

    def change_agent_auto_upgrade_status_async_invoker(self, request):
        http_info = self._change_agent_auto_upgrade_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_agent_auto_upgrade_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/setting/config/agent-auto-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAgentAutoUpgradeStatusResponse"
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

    def change_auto_open_quota_status_async(self, request):
        r"""开启或关闭“自动绑定配额”配置开关

        开启或关闭“自动绑定配额”配置开关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAutoOpenQuotaStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangeAutoOpenQuotaStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeAutoOpenQuotaStatusResponse`
        """
        http_info = self._change_auto_open_quota_status_http_info(request)
        return self._call_api(**http_info)

    def change_auto_open_quota_status_async_invoker(self, request):
        http_info = self._change_auto_open_quota_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_auto_open_quota_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/setting/config/auto-open-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAutoOpenQuotaStatusResponse"
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

    def change_baseline_white_list_async(self, request):
        r"""修改基线白名单

        修改基线白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeBaselineWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.ChangeBaselineWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeBaselineWhiteListResponse`
        """
        http_info = self._change_baseline_white_list_http_info(request)
        return self._call_api(**http_info)

    def change_baseline_white_list_async_invoker(self, request):
        http_info = self._change_baseline_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_baseline_white_list_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/baseline/whitelist",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeBaselineWhiteListResponse"
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

    def change_blocked_ip_async(self, request):
        r"""解除已拦截IP

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
        r"""对未通过的配置检查项进行忽略/取消忽略/修复/验证操作

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
        if 'check_cce' in local_var_params:
            query_params.append(('check_cce', local_var_params['check_cce']))
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

    def change_cluster_events_async(self, request):
        r"""修改告警状态

        修改告警状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeClusterEvents
        :type request: :class:`huaweicloudsdkhss.v5.ChangeClusterEventsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeClusterEventsResponse`
        """
        http_info = self._change_cluster_events_http_info(request)
        return self._call_api(**http_info)

    def change_cluster_events_async_invoker(self, request):
        http_info = self._change_cluster_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_cluster_events_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/cluster-protect/events",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeClusterEventsResponse"
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

    def change_cluster_protection_policy_async(self, request):
        r"""修改集群防护策略

        修改集群防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeClusterProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ChangeClusterProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeClusterProtectionPolicyResponse`
        """
        http_info = self._change_cluster_protection_policy_http_info(request)
        return self._call_api(**http_info)

    def change_cluster_protection_policy_async_invoker(self, request):
        http_info = self._change_cluster_protection_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_cluster_protection_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/cluster-protect/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeClusterProtectionPolicyResponse"
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

    def change_event_async(self, request):
        r"""处理告警事件

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
        r"""编辑服务器组

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
        r"""恢复已隔离文件

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

    def change_malware_collect_status_async(self, request):
        r"""开启或关闭恶意软件云查样本收集配置

        开启或关闭恶意软件云查样本收集配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeMalwareCollectStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangeMalwareCollectStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeMalwareCollectStatusResponse`
        """
        http_info = self._change_malware_collect_status_http_info(request)
        return self._call_api(**http_info)

    def change_malware_collect_status_async_invoker(self, request):
        http_info = self._change_malware_collect_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_malware_collect_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/setting/malware/collect",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeMalwareCollectStatusResponse"
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

    def change_password_complexity_status_async(self, request):
        r"""对口令复杂度检测未通过的主机进行忽略/取消忽略

        对口令复杂度检测未通过的主机进行忽略/取消忽略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangePasswordComplexityStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangePasswordComplexityStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangePasswordComplexityStatusResponse`
        """
        http_info = self._change_password_complexity_status_http_info(request)
        return self._call_api(**http_info)

    def change_password_complexity_status_async_invoker(self, request):
        http_info = self._change_password_complexity_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_password_complexity_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/baseline/password-complexity/action",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePasswordComplexityStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def change_policy_switch_status_async(self, request):
        r"""修改指定策略的总开关，将该策略的所有主机都打开或者关闭此策略

        修改指定策略的总开关，将该策略的所有主机都打开或者关闭此策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangePolicySwitchStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangePolicySwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangePolicySwitchStatusResponse`
        """
        http_info = self._change_policy_switch_status_http_info(request)
        return self._call_api(**http_info)

    def change_policy_switch_status_async_invoker(self, request):
        http_info = self._change_policy_switch_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_policy_switch_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/policy/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePolicySwitchStatusResponse"
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
        r"""修改漏洞的状态

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

    def create_cluster_protection_policy_async(self, request):
        r"""新建集群防护策略

        新建集群防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateClusterProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.CreateClusterProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateClusterProtectionPolicyResponse`
        """
        http_info = self._create_cluster_protection_policy_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_protection_policy_async_invoker(self, request):
        http_info = self._create_cluster_protection_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cluster_protection_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/cluster-protect/policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterProtectionPolicyResponse"
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

    def create_clusters_info_async(self, request):
        r"""同步集群信息

        同步集群信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateClustersInfo
        :type request: :class:`huaweicloudsdkhss.v5.CreateClustersInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateClustersInfoResponse`
        """
        http_info = self._create_clusters_info_http_info(request)
        return self._call_api(**http_info)

    def create_clusters_info_async_invoker(self, request):
        http_info = self._create_clusters_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_clusters_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/kubernetes/save-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClustersInfoResponse"
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

    def create_container_network_policy_async(self, request):
        r"""容器集群网络添加配置策略

        容器集群网络添加配置策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateContainerNetworkPolicy
        :type request: :class:`huaweicloudsdkhss.v5.CreateContainerNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateContainerNetworkPolicyResponse`
        """
        http_info = self._create_container_network_policy_http_info(request)
        return self._call_api(**http_info)

    def create_container_network_policy_async_invoker(self, request):
        http_info = self._create_container_network_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_container_network_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateContainerNetworkPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def create_decoy_port_policy_async(self, request):
        r"""新增动态端口蜜罐策略

        新增动态端口蜜罐策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDecoyPortPolicy
        :type request: :class:`huaweicloudsdkhss.v5.CreateDecoyPortPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateDecoyPortPolicyResponse`
        """
        http_info = self._create_decoy_port_policy_http_info(request)
        return self._call_api(**http_info)

    def create_decoy_port_policy_async_invoker(self, request):
        http_info = self._create_decoy_port_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_decoy_port_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/honeypot-port/policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDecoyPortPolicyResponse"
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

    def create_global_asset_scan_task_async(self, request):
        r"""创建全局资产扫描任务

        创建全局资产扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGlobalAssetScanTask
        :type request: :class:`huaweicloudsdkhss.v5.CreateGlobalAssetScanTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateGlobalAssetScanTaskResponse`
        """
        http_info = self._create_global_asset_scan_task_http_info(request)
        return self._call_api(**http_info)

    def create_global_asset_scan_task_async_invoker(self, request):
        http_info = self._create_global_asset_scan_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_global_asset_scan_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/asset/assign-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGlobalAssetScanTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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
        r"""HSS服务创建订单订购配额

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

    def create_security_group_policy_async(self, request):
        r"""创建安全组策略

        创建安全组策略(云原生网络模型)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroupPolicy
        :type request: :class:`huaweicloudsdkhss.v5.CreateSecurityGroupPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateSecurityGroupPolicyResponse`
        """
        http_info = self._create_security_group_policy_http_info(request)
        return self._call_api(**http_info)

    def create_security_group_policy_async_invoker(self, request):
        http_info = self._create_security_group_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_security_group_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/{namespace}/security-group-policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecurityGroupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def delete_account_async(self, request):
        r"""删除账号

        删除账号
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAccount
        :type request: :class:`huaweicloudsdkhss.v5.DeleteAccountRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteAccountResponse`
        """
        http_info = self._delete_account_http_info(request)
        return self._call_api(**http_info)

    def delete_account_async_invoker(self, request):
        http_info = self._delete_account_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_account_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/setting/account/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']
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

    def delete_baseline_white_list_async(self, request):
        r"""删除基线白名单

        删除基线白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBaselineWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.DeleteBaselineWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteBaselineWhiteListResponse`
        """
        http_info = self._delete_baseline_white_list_http_info(request)
        return self._call_api(**http_info)

    def delete_baseline_white_list_async_invoker(self, request):
        http_info = self._delete_baseline_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_baseline_white_list_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/baseline/whitelist",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBaselineWhiteListResponse"
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

    def delete_cluster_protection_policy_async(self, request):
        r"""删除集群防护策略

        删除集群防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteClusterProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeleteClusterProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteClusterProtectionPolicyResponse`
        """
        http_info = self._delete_cluster_protection_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_protection_policy_async_invoker(self, request):
        http_info = self._delete_cluster_protection_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cluster_protection_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/cluster-protect/policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClusterProtectionPolicyResponse"
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

    def delete_container_network_policy_async(self, request):
        r"""容器集群网络删除配置策略

        容器集群网络删除配置策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteContainerNetworkPolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeleteContainerNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteContainerNetworkPolicyResponse`
        """
        http_info = self._delete_container_network_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_container_network_policy_async_invoker(self, request):
        http_info = self._delete_container_network_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_container_network_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteContainerNetworkPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def delete_decoy_port_host_policy_async(self, request):
        r"""关闭主机动态端口蜜罐策略

        关闭主机动态端口蜜罐策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDecoyPortHostPolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeleteDecoyPortHostPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteDecoyPortHostPolicyResponse`
        """
        http_info = self._delete_decoy_port_host_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_decoy_port_host_policy_async_invoker(self, request):
        http_info = self._delete_decoy_port_host_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_decoy_port_host_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/honeypot-port/host-policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDecoyPortHostPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def delete_decoy_port_policy_async(self, request):
        r"""删除动态端口蜜罐策略

        删除动态端口蜜罐策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDecoyPortPolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeleteDecoyPortPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteDecoyPortPolicyResponse`
        """
        http_info = self._delete_decoy_port_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_decoy_port_policy_async_invoker(self, request):
        http_info = self._delete_decoy_port_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_decoy_port_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/honeypot-port/policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDecoyPortPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_hosts_group_async(self, request):
        r"""删除服务器组

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

    def delete_isolated_file_async(self, request):
        r"""删除已隔离文件

        删除已隔离文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIsolatedFile
        :type request: :class:`huaweicloudsdkhss.v5.DeleteIsolatedFileRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteIsolatedFileResponse`
        """
        http_info = self._delete_isolated_file_http_info(request)
        return self._call_api(**http_info)

    def delete_isolated_file_async_invoker(self, request):
        http_info = self._delete_isolated_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_isolated_file_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/event/isolated-file",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIsolatedFileResponse"
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

    def delete_policy_async(self, request):
        r"""删除防护策略

        删除防护策略：删除策略，已经在使用的防护策略不能删除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeletePolicyResponse`
        """
        http_info = self._delete_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_async_invoker(self, request):
        http_info = self._delete_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/rasp/policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))

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

    def delete_protection_policy_async(self, request):
        r"""删除防护策略

        删除防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeleteProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteProtectionPolicyResponse`
        """
        http_info = self._delete_protection_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_protection_policy_async_invoker(self, request):
        http_info = self._delete_protection_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_protection_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/ransomware/protection/policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProtectionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))

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

    def delete_resource_instance_tag_async(self, request):
        r"""删除资源标签

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

    def delete_security_group_policy_async(self, request):
        r"""删除安全组策略

        删除安全组策略(云原生网络模型)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroupPolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeleteSecurityGroupPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteSecurityGroupPolicyResponse`
        """
        http_info = self._delete_security_group_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_security_group_policy_async_invoker(self, request):
        http_info = self._delete_security_group_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_security_group_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/security-group-policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecurityGroupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def download_asset_file_async(self, request):
        r"""导出资产指纹请求

        导出资产指纹请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadAssetFile
        :type request: :class:`huaweicloudsdkhss.v5.DownloadAssetFileRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DownloadAssetFileResponse`
        """
        http_info = self._download_asset_file_http_info(request)
        return self._call_api(**http_info)

    def download_asset_file_async_invoker(self, request):
        http_info = self._download_asset_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_asset_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/asset/export",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAssetFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def export_container_list_async(self, request):
        r"""创建容器导出任务

        创建容器导出任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportContainerList
        :type request: :class:`huaweicloudsdkhss.v5.ExportContainerListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ExportContainerListResponse`
        """
        http_info = self._export_container_list_http_info(request)
        return self._call_api(**http_info)

    def export_container_list_async_invoker(self, request):
        http_info = self._export_container_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_container_list_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/export-task",
            "request_type": request.__class__.__name__,
            "response_type": "ExportContainerListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'export_size' in local_var_params:
            query_params.append(('export_size', local_var_params['export_size']))

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

    def list_accounts_async(self, request):
        r"""查询多账号列表

        查询多账号列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccounts
        :type request: :class:`huaweicloudsdkhss.v5.ListAccountsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAccountsResponse`
        """
        http_info = self._list_accounts_http_info(request)
        return self._call_api(**http_info)

    def list_accounts_async_invoker(self, request):
        http_info = self._list_accounts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_accounts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/setting/account/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccountsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_agent_auto_upgrade_status_async(self, request):
        r"""查询“Agent自动升级”配置开关状态

        查询“Agent自动升级”配置开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgentAutoUpgradeStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListAgentAutoUpgradeStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAgentAutoUpgradeStatusResponse`
        """
        http_info = self._list_agent_auto_upgrade_status_http_info(request)
        return self._call_api(**http_info)

    def list_agent_auto_upgrade_status_async_invoker(self, request):
        http_info = self._list_agent_auto_upgrade_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agent_auto_upgrade_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/config/agent-auto-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentAutoUpgradeStatusResponse"
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

    def list_agent_install_script_async(self, request):
        r"""查询agent安装脚本

        查询agent安装脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgentInstallScript
        :type request: :class:`huaweicloudsdkhss.v5.ListAgentInstallScriptRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAgentInstallScriptResponse`
        """
        http_info = self._list_agent_install_script_http_info(request)
        return self._call_api(**http_info)

    def list_agent_install_script_async_invoker(self, request):
        http_info = self._list_agent_install_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agent_install_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/agent-install-script",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentInstallScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'os_arch' in local_var_params:
            query_params.append(('os_arch', local_var_params['os_arch']))
        if 'outside_host' in local_var_params:
            query_params.append(('outside_host', local_var_params['outside_host']))
        if 'outside_group_id' in local_var_params:
            query_params.append(('outside_group_id', local_var_params['outside_group_id']))
        if 'batch_install' in local_var_params:
            query_params.append(('batch_install', local_var_params['batch_install']))
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

    def list_alarm_white_list_async(self, request):
        r"""查询告警白名单列表

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

    def list_antivirus_handle_history_async(self, request):
        r"""查询病毒扫描历史处置记录列表

        查询病毒扫描历史处置记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAntivirusHandleHistory
        :type request: :class:`huaweicloudsdkhss.v5.ListAntivirusHandleHistoryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAntivirusHandleHistoryResponse`
        """
        http_info = self._list_antivirus_handle_history_http_info(request)
        return self._call_api(**http_info)

    def list_antivirus_handle_history_async_invoker(self, request):
        http_info = self._list_antivirus_handle_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_antivirus_handle_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/handle-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListAntivirusHandleHistoryResponse"
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
        if 'malware_name' in local_var_params:
            query_params.append(('malware_name', local_var_params['malware_name']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'severity_list' in local_var_params:
            query_params.append(('severity_list', local_var_params['severity_list']))
            collection_formats['severity_list'] = 'csv'
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'handle_method' in local_var_params:
            query_params.append(('handle_method', local_var_params['handle_method']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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
        r"""获取软件信息的历史变动记录

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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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
        r"""查询软件列表

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
        r"""查询软件的服务器列表

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

    def list_auto_kill_virus_status_async(self, request):
        r"""查询程序自动隔离查杀状态

        查询程序自动隔离查杀状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAutoKillVirusStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListAutoKillVirusStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAutoKillVirusStatusResponse`
        """
        http_info = self._list_auto_kill_virus_status_http_info(request)
        return self._call_api(**http_info)

    def list_auto_kill_virus_status_async_invoker(self, request):
        http_info = self._list_auto_kill_virus_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_auto_kill_virus_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/virus-kill",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutoKillVirusStatusResponse"
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

    def list_auto_launch_change_histories_async(self, request):
        r"""获取自启动项的历史变动记录

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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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
        r"""查询自启动项信息

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
        r"""查询自启动项的服务列表

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

    def list_auto_open_quota_status_async(self, request):
        r"""查询“自动绑定配额”配置开关状态

        查询“自动绑定配额”配置开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAutoOpenQuotaStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListAutoOpenQuotaStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAutoOpenQuotaStatusResponse`
        """
        http_info = self._list_auto_open_quota_status_http_info(request)
        return self._call_api(**http_info)

    def list_auto_open_quota_status_async_invoker(self, request):
        http_info = self._list_auto_open_quota_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_auto_open_quota_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/config/auto-open-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutoOpenQuotaStatusResponse"
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

    def list_backup_vaults_async(self, request):
        r"""查询备份存储库列表

        查询备份存储库列表，若进行绑定主机，则需要额外判断，同时满足以下条件：1、存储库状态为“可用”状态；2、备份策略状态为“已启用”；3、存储库有剩余可用备份容量；4、存储库绑定的服务器数量少于256。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackupVaults
        :type request: :class:`huaweicloudsdkhss.v5.ListBackupVaultsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListBackupVaultsResponse`
        """
        http_info = self._list_backup_vaults_http_info(request)
        return self._call_api(**http_info)

    def list_backup_vaults_async_invoker(self, request):
        http_info = self._list_backup_vaults_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backup_vaults_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/ransomware/optional/vaults",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupVaultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'vault_name' in local_var_params:
            query_params.append(('vault_name', local_var_params['vault_name']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))

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

    def list_baseline_white_lists_async(self, request):
        r"""查询基线白名单列表

        查询基线白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBaselineWhiteLists
        :type request: :class:`huaweicloudsdkhss.v5.ListBaselineWhiteListsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListBaselineWhiteListsResponse`
        """
        http_info = self._list_baseline_white_lists_http_info(request)
        return self._call_api(**http_info)

    def list_baseline_white_lists_async_invoker(self, request):
        http_info = self._list_baseline_white_lists_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_baseline_white_lists_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/whitelists",
            "request_type": request.__class__.__name__,
            "response_type": "ListBaselineWhiteListsResponse"
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
        if 'check_rule_name' in local_var_params:
            query_params.append(('check_rule_name', local_var_params['check_rule_name']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'rule_type' in local_var_params:
            query_params.append(('rule_type', local_var_params['rule_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))

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
        r"""查询已拦截IP列表

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

    def list_cce_cluster_config_async(self, request):
        r"""获取集群配置

        获取集群配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCceClusterConfig
        :type request: :class:`huaweicloudsdkhss.v5.ListCceClusterConfigRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListCceClusterConfigResponse`
        """
        http_info = self._list_cce_cluster_config_http_info(request)
        return self._call_api(**http_info)

    def list_cce_cluster_config_async_invoker(self, request):
        http_info = self._list_cce_cluster_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cce_cluster_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/configs/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListCceClusterConfigResponse"
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

    def list_cce_cluster_detect_risk_async(self, request):
        r"""批量获取容器集群风险信息

        批量获取容器集群风险信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCceClusterDetectRisk
        :type request: :class:`huaweicloudsdkhss.v5.ListCceClusterDetectRiskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListCceClusterDetectRiskResponse`
        """
        http_info = self._list_cce_cluster_detect_risk_http_info(request)
        return self._call_api(**http_info)

    def list_cce_cluster_detect_risk_async_invoker(self, request):
        http_info = self._list_cce_cluster_detect_risk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cce_cluster_detect_risk_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/risks/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListCceClusterDetectRiskResponse"
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

    def list_check_feature_rule_async(self, request):
        r"""查询检测规则列表

        查询检测规则列表：查询默认检测规则信息，包含14种检测规则，默认都不开启
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCheckFeatureRule
        :type request: :class:`huaweicloudsdkhss.v5.ListCheckFeatureRuleRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListCheckFeatureRuleResponse`
        """
        http_info = self._list_check_feature_rule_http_info(request)
        return self._call_api(**http_info)

    def list_check_feature_rule_async_invoker(self, request):
        http_info = self._list_check_feature_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_check_feature_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/rasp/rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListCheckFeatureRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))

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

    def list_cluster_audit_logs_async(self, request):
        r"""查询k8s集群审计日志列表

        查询k8s集群审计日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterAuditLogs
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterAuditLogsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterAuditLogsResponse`
        """
        http_info = self._list_cluster_audit_logs_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_audit_logs_async_invoker(self, request):
        http_info = self._list_cluster_audit_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_audit_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes/cluster/audit-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterAuditLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'verb' in local_var_params:
            query_params.append(('verb', local_var_params['verb']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'line_num' in local_var_params:
            query_params.append(('line_num', local_var_params['line_num']))

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

    def list_cluster_event_logs_async(self, request):
        r"""查询k8s集群事件列表

        查询k8s集群事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterEventLogs
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterEventLogsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterEventLogsResponse`
        """
        http_info = self._list_cluster_event_logs_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_event_logs_async_invoker(self, request):
        http_info = self._list_cluster_event_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_event_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes/cluster/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterEventLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'reason' in local_var_params:
            query_params.append(('reason', local_var_params['reason']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'line_num' in local_var_params:
            query_params.append(('line_num', local_var_params['line_num']))

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

    def list_cluster_events_async(self, request):
        r"""获取所有集群中告警事件

        获取所有集群中告警事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterEvents
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterEventsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterEventsResponse`
        """
        http_info = self._list_cluster_events_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_events_async_invoker(self, request):
        http_info = self._list_cluster_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/cluster-protect/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterEventsResponse"
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
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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

    def list_cluster_protect_overview_async(self, request):
        r"""集群防护概览

        集群防护概览
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterProtectOverview
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterProtectOverviewRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterProtectOverviewResponse`
        """
        http_info = self._list_cluster_protect_overview_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_protect_overview_async_invoker(self, request):
        http_info = self._list_cluster_protect_overview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_protect_overview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/cluster-protect/overview",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterProtectOverviewResponse"
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

    def list_cluster_protect_policy_templates_async(self, request):
        r"""查询集群组件防护策略模板列表

        查询集群防护策略模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterProtectPolicyTemplates
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterProtectPolicyTemplatesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterProtectPolicyTemplatesResponse`
        """
        http_info = self._list_cluster_protect_policy_templates_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_protect_policy_templates_async_invoker(self, request):
        http_info = self._list_cluster_protect_policy_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_protect_policy_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/clusters/protection-policy-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterProtectPolicyTemplatesResponse"
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
        if 'template_name' in local_var_params:
            query_params.append(('template_name', local_var_params['template_name']))
        if 'template_type' in local_var_params:
            query_params.append(('template_type', local_var_params['template_type']))
        if 'target_kind' in local_var_params:
            query_params.append(('target_kind', local_var_params['target_kind']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))

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

    def list_cluster_protection_default_policy_async(self, request):
        r"""获取集群防护默认策略列表

        获取集群防护默认策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterProtectionDefaultPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterProtectionDefaultPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterProtectionDefaultPolicyResponse`
        """
        http_info = self._list_cluster_protection_default_policy_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_protection_default_policy_async_invoker(self, request):
        http_info = self._list_cluster_protection_default_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_protection_default_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/cluster-protect/default-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterProtectionDefaultPolicyResponse"
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

    def list_cluster_protection_info_async(self, request):
        r"""查询集群防护信息

        查询集群防护信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterProtectionInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterProtectionInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterProtectionInfoResponse`
        """
        http_info = self._list_cluster_protection_info_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_protection_info_async_invoker(self, request):
        http_info = self._list_cluster_protection_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_protection_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/cluster-protect/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterProtectionInfoResponse"
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

    def list_cluster_protection_item_async(self, request):
        r"""获取集群所有防护项

        获取集群所有防护项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterProtectionItem
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterProtectionItemRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterProtectionItemResponse`
        """
        http_info = self._list_cluster_protection_item_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_protection_item_async_invoker(self, request):
        http_info = self._list_cluster_protection_item_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_protection_item_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/cluster-protect/protection-item",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterProtectionItemResponse"
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

    def list_cluster_protection_policy_async(self, request):
        r"""获取集群防护策略列表

        获取集群防护策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterProtectionPolicyResponse`
        """
        http_info = self._list_cluster_protection_policy_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_protection_policy_async_invoker(self, request):
        http_info = self._list_cluster_protection_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_protection_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/cluster-protect/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterProtectionPolicyResponse"
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
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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

    def list_cluster_protection_policy_detail_async(self, request):
        r"""查看指定策略的详情

        查看指定策略的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterProtectionPolicyDetail
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterProtectionPolicyDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterProtectionPolicyDetailResponse`
        """
        http_info = self._list_cluster_protection_policy_detail_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_protection_policy_detail_async_invoker(self, request):
        http_info = self._list_cluster_protection_policy_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_protection_policy_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/cluster-protect/policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterProtectionPolicyDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def list_common_tips_async(self, request):
        r"""获取部分提示信息

        获取部分提示信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCommonTips
        :type request: :class:`huaweicloudsdkhss.v5.ListCommonTipsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListCommonTipsResponse`
        """
        http_info = self._list_common_tips_http_info(request)
        return self._call_api(**http_info)

    def list_common_tips_async_invoker(self, request):
        http_info = self._list_common_tips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_common_tips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/common/tips",
            "request_type": request.__class__.__name__,
            "response_type": "ListCommonTipsResponse"
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
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_container_cmd_logs_async(self, request):
        r"""查询容器内运行的命令列表

        查询容器内运行的命令列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainerCmdLogs
        :type request: :class:`huaweicloudsdkhss.v5.ListContainerCmdLogsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainerCmdLogsResponse`
        """
        http_info = self._list_container_cmd_logs_http_info(request)
        return self._call_api(**http_info)

    def list_container_cmd_logs_async_invoker(self, request):
        http_info = self._list_container_cmd_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_container_cmd_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/cmd-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainerCmdLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
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
        if 'cmd' in local_var_params:
            query_params.append(('cmd', local_var_params['cmd']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
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

    def list_container_image_logs_async(self, request):
        r"""查询容器镜像操作日志

        查询容器镜像操作日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainerImageLogs
        :type request: :class:`huaweicloudsdkhss.v5.ListContainerImageLogsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainerImageLogsResponse`
        """
        http_info = self._list_container_image_logs_http_info(request)
        return self._call_api(**http_info)

    def list_container_image_logs_async_invoker(self, request):
        http_info = self._list_container_image_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_container_image_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/image/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainerImageLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))
        if 'source_ip' in local_var_params:
            query_params.append(('source_ip', local_var_params['source_ip']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
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

    def list_container_images_async(self, request):
        r"""查询容器镜像列表

        查询容器镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainerImages
        :type request: :class:`huaweicloudsdkhss.v5.ListContainerImagesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainerImagesResponse`
        """
        http_info = self._list_container_images_http_info(request)
        return self._call_api(**http_info)

    def list_container_images_async_invoker(self, request):
        http_info = self._list_container_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_container_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainerImagesResponse"
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
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

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

    def list_container_logs_async(self, request):
        r"""查询容器日志列表

        查询容器日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainerLogs
        :type request: :class:`huaweicloudsdkhss.v5.ListContainerLogsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainerLogsResponse`
        """
        http_info = self._list_container_logs_http_info(request)
        return self._call_api(**http_info)

    def list_container_logs_async_invoker(self, request):
        http_info = self._list_container_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_container_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainerLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'pod_name' in local_var_params:
            query_params.append(('pod_name', local_var_params['pod_name']))
        if 'pod_id' in local_var_params:
            query_params.append(('pod_id', local_var_params['pod_id']))
        if 'pod_ip' in local_var_params:
            query_params.append(('pod_ip', local_var_params['pod_ip']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'container_id' in local_var_params:
            query_params.append(('container_id', local_var_params['container_id']))
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'content' in local_var_params:
            query_params.append(('content', local_var_params['content']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'line_num' in local_var_params:
            query_params.append(('line_num', local_var_params['line_num']))

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

    def list_container_network_clusters_async(self, request):
        r"""查询容器防护的集群信息

        查询容器防护的集群信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainerNetworkClusters
        :type request: :class:`huaweicloudsdkhss.v5.ListContainerNetworkClustersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainerNetworkClustersResponse`
        """
        http_info = self._list_container_network_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_container_network_clusters_async_invoker(self, request):
        http_info = self._list_container_network_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_container_network_clusters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/cluster",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainerNetworkClustersResponse"
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

    def list_container_network_node_list_async(self, request):
        r"""查询容器集群VPC网络的节点列表

        查询容器集群网络的策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainerNetworkNodeList
        :type request: :class:`huaweicloudsdkhss.v5.ListContainerNetworkNodeListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainerNetworkNodeListResponse`
        """
        http_info = self._list_container_network_node_list_http_info(request)
        return self._call_api(**http_info)

    def list_container_network_node_list_async_invoker(self, request):
        http_info = self._list_container_network_node_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_container_network_node_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/node",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainerNetworkNodeListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'query_field' in local_var_params:
            query_params.append(('query_field', local_var_params['query_field']))
        if 'query_value' in local_var_params:
            query_params.append(('query_value', local_var_params['query_value']))

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

    def list_container_network_policy_async(self, request):
        r"""查询容器集群网络的策略列表

        查询容器集群网络的策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListContainerNetworkPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ListContainerNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListContainerNetworkPolicyResponse`
        """
        http_info = self._list_container_network_policy_http_info(request)
        return self._call_api(**http_info)

    def list_container_network_policy_async_invoker(self, request):
        http_info = self._list_container_network_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_container_network_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListContainerNetworkPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

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

    def list_container_nodes_async(self, request):
        r"""查询容器节点列表

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
        r"""查询容器基本信息列表

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

    def list_decoy_port_policy_async(self, request):
        r"""查看动态端口蜜罐策略

        查看动态端口蜜罐策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDecoyPortPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ListDecoyPortPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListDecoyPortPolicyResponse`
        """
        http_info = self._list_decoy_port_policy_http_info(request)
        return self._call_api(**http_info)

    def list_decoy_port_policy_async_invoker(self, request):
        http_info = self._list_decoy_port_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_decoy_port_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/honeypot-port/policy-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListDecoyPortPolicyResponse"
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

    def list_download_exported_file_async(self, request):
        r"""下载导出文件

        下载导出文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDownloadExportedFile
        :type request: :class:`huaweicloudsdkhss.v5.ListDownloadExportedFileRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListDownloadExportedFileResponse`
        """
        http_info = self._list_download_exported_file_http_info(request)
        return self._call_api(**http_info)

    def list_download_exported_file_async_invoker(self, request):
        http_info = self._list_download_exported_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_download_exported_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/download/{file_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListDownloadExportedFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

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

    def list_event_att_ck_async(self, request):
        r"""查询ATT&CK攻击阶段统计列表

        查询ATT&amp;CK攻击阶段统计列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEventAttCk
        :type request: :class:`huaweicloudsdkhss.v5.ListEventAttCkRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListEventAttCkResponse`
        """
        http_info = self._list_event_att_ck_http_info(request)
        return self._call_api(**http_info)

    def list_event_att_ck_async_invoker(self, request):
        http_info = self._list_event_att_ck_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_att_ck_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/att-ck",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventAttCkResponse"
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
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
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
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
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

    def list_event_handle_history_async(self, request):
        r"""查询告警事件历史处置记录列表

        查询告警事件历史处置记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEventHandleHistory
        :type request: :class:`huaweicloudsdkhss.v5.ListEventHandleHistoryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListEventHandleHistoryResponse`
        """
        http_info = self._list_event_handle_history_http_info(request)
        return self._call_api(**http_info)

    def list_event_handle_history_async_invoker(self, request):
        http_info = self._list_event_handle_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_handle_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/handle-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventHandleHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'attack_tag' in local_var_params:
            query_params.append(('attack_tag', local_var_params['attack_tag']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'event_class_ids' in local_var_params:
            query_params.append(('event_class_ids', local_var_params['event_class_ids']))
            collection_formats['event_class_ids'] = 'csv'
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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

    def list_global_asset_scan_task_async(self, request):
        r"""查询资产全局扫描任务状态

        查询资产全局扫描任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGlobalAssetScanTask
        :type request: :class:`huaweicloudsdkhss.v5.ListGlobalAssetScanTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListGlobalAssetScanTaskResponse`
        """
        http_info = self._list_global_asset_scan_task_http_info(request)
        return self._call_api(**http_info)

    def list_global_asset_scan_task_async_invoker(self, request):
        http_info = self._list_global_asset_scan_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_global_asset_scan_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/assign-task",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalAssetScanTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def list_handle_vuls_async(self, request):
        r"""处理的漏洞

        查询今日处理漏洞/累计处理漏洞
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHandleVuls
        :type request: :class:`huaweicloudsdkhss.v5.ListHandleVulsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHandleVulsResponse`
        """
        http_info = self._list_handle_vuls_http_info(request)
        return self._call_api(**http_info)

    def list_handle_vuls_async_invoker(self, request):
        http_info = self._list_handle_vuls_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_handle_vuls_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/handle/vulnerabilities",
            "request_type": request.__class__.__name__,
            "response_type": "ListHandleVulsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))
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
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'handle_circle' in local_var_params:
            query_params.append(('handle_circle', local_var_params['handle_circle']))
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

    def list_host_groups_async(self, request):
        r"""查询服务器组列表

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

    def list_host_status_async(self, request):
        r"""查询云服务器列表

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
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'has_intrusion' in local_var_params:
            query_params.append(('has_intrusion', local_var_params['has_intrusion']))
        if 'has_vul' in local_var_params:
            query_params.append(('has_vul', local_var_params['has_vul']))
        if 'has_baseline' in local_var_params:
            query_params.append(('has_baseline', local_var_params['has_baseline']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'policy_group_id' in local_var_params:
            query_params.append(('policy_group_id', local_var_params['policy_group_id']))
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'refresh' in local_var_params:
            query_params.append(('refresh', local_var_params['refresh']))
        if 'get_common_login_locations' in local_var_params:
            query_params.append(('get_common_login_locations', local_var_params['get_common_login_locations']))
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
        if 'install_mode' in local_var_params:
            query_params.append(('install_mode', local_var_params['install_mode']))
        if 'binding_key' in local_var_params:
            query_params.append(('binding_key', local_var_params['binding_key']))
        if 'protect_interrupt' in local_var_params:
            query_params.append(('protect_interrupt', local_var_params['protect_interrupt']))
        if 'incluster' in local_var_params:
            query_params.append(('incluster', local_var_params['incluster']))
        if 'protect_degradation' in local_var_params:
            query_params.append(('protect_degradation', local_var_params['protect_degradation']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
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

    def list_image_handle_affect_vulnerabilities_async(self, request):
        r"""查询镜像漏洞处置操作影响的漏洞列表

        查询镜像漏洞处置操作影响的漏洞列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageHandleAffectVulnerabilities
        :type request: :class:`huaweicloudsdkhss.v5.ListImageHandleAffectVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListImageHandleAffectVulnerabilitiesResponse`
        """
        http_info = self._list_image_handle_affect_vulnerabilities_http_info(request)
        return self._call_api(**http_info)

    def list_image_handle_affect_vulnerabilities_async_invoker(self, request):
        http_info = self._list_image_handle_affect_vulnerabilities_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_handle_affect_vulnerabilities_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/image/vulnerability/handle-affect-vulnerabilities",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageHandleAffectVulnerabilitiesResponse"
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
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))

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

    def list_image_local_async(self, request):
        r"""本地镜像列表查询

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
        r"""查询镜像指定安全配置项的检查项列表

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
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
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
        r"""查询镜像安全配置检测结果列表

        查询镜像安全配置检测结果列表，当前支持检测CentOS 7、Debian 10、EulerOS和Ubuntu16镜像的系统配置项、SSH应用配置项。
        
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
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
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
        r"""查询镜像的漏洞信息

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
        r"""查询已隔离文件列表

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
        if 'isolation_status' in local_var_params:
            query_params.append(('isolation_status', local_var_params['isolation_status']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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
        r"""查询指定中间件的服务器列表

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

    def list_jar_package_info_async(self, request):
        r"""资产管理-主机管理-指纹类型-中间件

        资产管理-主机管理-指纹类型-中间件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJarPackageInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListJarPackageInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListJarPackageInfoResponse`
        """
        http_info = self._list_jar_package_info_http_info(request)
        return self._call_api(**http_info)

    def list_jar_package_info_async_invoker(self, request):
        http_info = self._list_jar_package_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_jar_package_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/{host_id}/jar-package",
            "request_type": request.__class__.__name__,
            "response_type": "ListJarPackageInfoResponse"
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
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
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

    def list_jar_package_statistics_async(self, request):
        r"""查询中间件列表

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

    def list_k8s_cron_jobs_async(self, request):
        r"""查询cronjobs基本信息列表

        查询cronjobs基本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListK8sCronJobs
        :type request: :class:`huaweicloudsdkhss.v5.ListK8sCronJobsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListK8sCronJobsResponse`
        """
        http_info = self._list_k8s_cron_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_k8s_cron_jobs_async_invoker(self, request):
        http_info = self._list_k8s_cron_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_k8s_cron_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/cronjobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListK8sCronJobsResponse"
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
        if 'cronjob_name' in local_var_params:
            query_params.append(('cronjob_name', local_var_params['cronjob_name']))
        if 'namespace_name' in local_var_params:
            query_params.append(('namespace_name', local_var_params['namespace_name']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_k8s_daemon_sets_async(self, request):
        r"""查询daemonsets基本信息列表

        查询daemonsets基本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListK8sDaemonSets
        :type request: :class:`huaweicloudsdkhss.v5.ListK8sDaemonSetsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListK8sDaemonSetsResponse`
        """
        http_info = self._list_k8s_daemon_sets_http_info(request)
        return self._call_api(**http_info)

    def list_k8s_daemon_sets_async_invoker(self, request):
        http_info = self._list_k8s_daemon_sets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_k8s_daemon_sets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/daemonsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListK8sDaemonSetsResponse"
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
        if 'daemonset_name' in local_var_params:
            query_params.append(('daemonset_name', local_var_params['daemonset_name']))
        if 'namespace_name' in local_var_params:
            query_params.append(('namespace_name', local_var_params['namespace_name']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_k8s_deployments_async(self, request):
        r"""查询deployment基本信息列表

        查询deployment基本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListK8sDeployments
        :type request: :class:`huaweicloudsdkhss.v5.ListK8sDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListK8sDeploymentsResponse`
        """
        http_info = self._list_k8s_deployments_http_info(request)
        return self._call_api(**http_info)

    def list_k8s_deployments_async_invoker(self, request):
        http_info = self._list_k8s_deployments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_k8s_deployments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "ListK8sDeploymentsResponse"
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
        if 'deployment_name' in local_var_params:
            query_params.append(('deployment_name', local_var_params['deployment_name']))
        if 'namespace_name' in local_var_params:
            query_params.append(('namespace_name', local_var_params['namespace_name']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_k8s_jobs_async(self, request):
        r"""查询jobs基本信息列表

        查询jobs基本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListK8sJobs
        :type request: :class:`huaweicloudsdkhss.v5.ListK8sJobsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListK8sJobsResponse`
        """
        http_info = self._list_k8s_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_k8s_jobs_async_invoker(self, request):
        http_info = self._list_k8s_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_k8s_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListK8sJobsResponse"
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
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'namespace_name' in local_var_params:
            query_params.append(('namespace_name', local_var_params['namespace_name']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_k8s_pods_async(self, request):
        r"""查询pod基本信息列表

        查询pod基本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListK8sPods
        :type request: :class:`huaweicloudsdkhss.v5.ListK8sPodsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListK8sPodsResponse`
        """
        http_info = self._list_k8s_pods_http_info(request)
        return self._call_api(**http_info)

    def list_k8s_pods_async_invoker(self, request):
        http_info = self._list_k8s_pods_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_k8s_pods_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/pods",
            "request_type": request.__class__.__name__,
            "response_type": "ListK8sPodsResponse"
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
        if 'pod_name' in local_var_params:
            query_params.append(('pod_name', local_var_params['pod_name']))
        if 'namespace_name' in local_var_params:
            query_params.append(('namespace_name', local_var_params['namespace_name']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))

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

    def list_k8s_stateful_sets_async(self, request):
        r"""查询statefulset基本信息列表

        查询statefulset基本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListK8sStatefulSets
        :type request: :class:`huaweicloudsdkhss.v5.ListK8sStatefulSetsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListK8sStatefulSetsResponse`
        """
        http_info = self._list_k8s_stateful_sets_http_info(request)
        return self._call_api(**http_info)

    def list_k8s_stateful_sets_async_invoker(self, request):
        http_info = self._list_k8s_stateful_sets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_k8s_stateful_sets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/statefulsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListK8sStatefulSetsResponse"
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
        if 'statefulset_name' in local_var_params:
            query_params.append(('statefulset_name', local_var_params['statefulset_name']))
        if 'namespace_name' in local_var_params:
            query_params.append(('namespace_name', local_var_params['namespace_name']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_kernel_module_host_info_async(self, request):
        r"""资产管理-资产指纹-内核模块的服务器列表

        资产管理-资产指纹-内核模块的服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKernelModuleHostInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListKernelModuleHostInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListKernelModuleHostInfoResponse`
        """
        http_info = self._list_kernel_module_host_info_http_info(request)
        return self._call_api(**http_info)

    def list_kernel_module_host_info_async_invoker(self, request):
        http_info = self._list_kernel_module_host_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_kernel_module_host_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/host/kernel-module",
            "request_type": request.__class__.__name__,
            "response_type": "ListKernelModuleHostInfoResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
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

    def list_kernel_module_info_async(self, request):
        r"""资产管理-主机管理-指纹类型-内核模块

        资产管理-主机管理-指纹类型-内核模块
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKernelModuleInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListKernelModuleInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListKernelModuleInfoResponse`
        """
        http_info = self._list_kernel_module_info_http_info(request)
        return self._call_api(**http_info)

    def list_kernel_module_info_async_invoker(self, request):
        http_info = self._list_kernel_module_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_kernel_module_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/{host_id}/kernel-module",
            "request_type": request.__class__.__name__,
            "response_type": "ListKernelModuleInfoResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_kernel_module_statistics_async(self, request):
        r"""资产管理-资产指纹-内核模块左侧树

        资产管理-资产指纹-内核模块左侧树
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKernelModuleStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListKernelModuleStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListKernelModuleStatisticsResponse`
        """
        http_info = self._list_kernel_module_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_kernel_module_statistics_async_invoker(self, request):
        http_info = self._list_kernel_module_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_kernel_module_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/statistics/kernel-module",
            "request_type": request.__class__.__name__,
            "response_type": "ListKernelModuleStatisticsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_kubernetes_cluster_details_async(self, request):
        r"""查询容器Kubernetes集群列表

        查询容器Kubernetes集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKubernetesClusterDetails
        :type request: :class:`huaweicloudsdkhss.v5.ListKubernetesClusterDetailsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListKubernetesClusterDetailsResponse`
        """
        http_info = self._list_kubernetes_cluster_details_http_info(request)
        return self._call_api(**http_info)

    def list_kubernetes_cluster_details_async_invoker(self, request):
        http_info = self._list_kubernetes_cluster_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_kubernetes_cluster_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListKubernetesClusterDetailsResponse"
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
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'load_agent_info' in local_var_params:
            query_params.append(('load_agent_info', local_var_params['load_agent_info']))
        if 'scene' in local_var_params:
            query_params.append(('scene', local_var_params['scene']))

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

    def list_kubernetes_endpoint_details_async(self, request):
        r"""查询容器Kubernetes端点列表

        查询容器Kubernetes端点列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKubernetesEndpointDetails
        :type request: :class:`huaweicloudsdkhss.v5.ListKubernetesEndpointDetailsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListKubernetesEndpointDetailsResponse`
        """
        http_info = self._list_kubernetes_endpoint_details_http_info(request)
        return self._call_api(**http_info)

    def list_kubernetes_endpoint_details_async_invoker(self, request):
        http_info = self._list_kubernetes_endpoint_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_kubernetes_endpoint_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListKubernetesEndpointDetailsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

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

    def list_kubernetes_service_details_async(self, request):
        r"""查询容器Kubernetes服务列表

        查询容器Kubernetes服务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKubernetesServiceDetails
        :type request: :class:`huaweicloudsdkhss.v5.ListKubernetesServiceDetailsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListKubernetesServiceDetailsResponse`
        """
        http_info = self._list_kubernetes_service_details_http_info(request)
        return self._call_api(**http_info)

    def list_kubernetes_service_details_async_invoker(self, request):
        http_info = self._list_kubernetes_service_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_kubernetes_service_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/services",
            "request_type": request.__class__.__name__,
            "response_type": "ListKubernetesServiceDetailsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

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

    def list_login_common_ip_async(self, request):
        r"""查询常用登录IP信息

        查询常用登录IP信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoginCommonIp
        :type request: :class:`huaweicloudsdkhss.v5.ListLoginCommonIpRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListLoginCommonIpResponse`
        """
        http_info = self._list_login_common_ip_http_info(request)
        return self._call_api(**http_info)

    def list_login_common_ip_async_invoker(self, request):
        http_info = self._list_login_common_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_login_common_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/login-common-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoginCommonIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'ip_addr' in local_var_params:
            query_params.append(('ip_addr', local_var_params['ip_addr']))

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

    def list_login_common_location_async(self, request):
        r"""查询常用登录地信息

        查询常用登录地信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoginCommonLocation
        :type request: :class:`huaweicloudsdkhss.v5.ListLoginCommonLocationRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListLoginCommonLocationResponse`
        """
        http_info = self._list_login_common_location_http_info(request)
        return self._call_api(**http_info)

    def list_login_common_location_async_invoker(self, request):
        http_info = self._list_login_common_location_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_login_common_location_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/login-common-location",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoginCommonLocationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'area_code' in local_var_params:
            query_params.append(('area_code', local_var_params['area_code']))

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

    def list_login_white_ip_async(self, request):
        r"""查询SSH登录IP白名单列表

        查询SSH登录IP白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoginWhiteIp
        :type request: :class:`huaweicloudsdkhss.v5.ListLoginWhiteIpRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListLoginWhiteIpResponse`
        """
        http_info = self._list_login_white_ip_http_info(request)
        return self._call_api(**http_info)

    def list_login_white_ip_async_invoker(self, request):
        http_info = self._list_login_white_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_login_white_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/login-white-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoginWhiteIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'white_ip' in local_var_params:
            query_params.append(('white_ip', local_var_params['white_ip']))

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

    def list_login_white_list_async(self, request):
        r"""查询登录白名单列表

        查询登录白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoginWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.ListLoginWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListLoginWhiteListResponse`
        """
        http_info = self._list_login_white_list_http_info(request)
        return self._call_api(**http_info)

    def list_login_white_list_async_invoker(self, request):
        http_info = self._list_login_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_login_white_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/white-list/login",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoginWhiteListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'login_ip' in local_var_params:
            query_params.append(('login_ip', local_var_params['login_ip']))
        if 'login_user_name' in local_var_params:
            query_params.append(('login_user_name', local_var_params['login_user_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_malware_collect_status_async(self, request):
        r"""查询恶意软件云查样本收集配置开关状态

        查询恶意软件云查样本收集配置开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMalwareCollectStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListMalwareCollectStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListMalwareCollectStatusResponse`
        """
        http_info = self._list_malware_collect_status_http_info(request)
        return self._call_api(**http_info)

    def list_malware_collect_status_async_invoker(self, request):
        http_info = self._list_malware_collect_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_malware_collect_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/malware/collect",
            "request_type": request.__class__.__name__,
            "response_type": "ListMalwareCollectStatusResponse"
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

    def list_namespaces_async(self, request):
        r"""获取集群下的namespace

        获取集群下的namespace
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNamespaces
        :type request: :class:`huaweicloudsdkhss.v5.ListNamespacesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListNamespacesResponse`
        """
        http_info = self._list_namespaces_http_info(request)
        return self._call_api(**http_info)

    def list_namespaces_async_invoker(self, request):
        http_info = self._list_namespaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_namespaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/namespace",
            "request_type": request.__class__.__name__,
            "response_type": "ListNamespacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_operation_logs_by_vault_name_async(self, request):
        r"""查询备份恢复任务列表

        查询备份恢复任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOperationLogsByVaultName
        :type request: :class:`huaweicloudsdkhss.v5.ListOperationLogsByVaultNameRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListOperationLogsByVaultNameResponse`
        """
        http_info = self._list_operation_logs_by_vault_name_http_info(request)
        return self._call_api(**http_info)

    def list_operation_logs_by_vault_name_async_invoker(self, request):
        http_info = self._list_operation_logs_by_vault_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_operation_logs_by_vault_name_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/ransomware/backup/operation-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListOperationLogsByVaultNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))

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

    def list_organization_tree_async(self, request):
        r"""查询账号组织

        查询账号组织
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOrganizationTree
        :type request: :class:`huaweicloudsdkhss.v5.ListOrganizationTreeRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListOrganizationTreeResponse`
        """
        http_info = self._list_organization_tree_http_info(request)
        return self._call_api(**http_info)

    def list_organization_tree_async_invoker(self, request):
        http_info = self._list_organization_tree_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_organization_tree_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/setting/account/organization-tree",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrganizationTreeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_refresh' in local_var_params:
            query_params.append(('is_refresh', local_var_params['is_refresh']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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
        r"""查询口令复杂度策略检测报告

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
        if 'result_type' in local_var_params:
            query_params.append(('result_type', local_var_params['result_type']))
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

    def list_plugin_install_script_async(self, request):
        r"""获取docker插件安装脚本

        获取docker插件安装脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPluginInstallScript
        :type request: :class:`huaweicloudsdkhss.v5.ListPluginInstallScriptRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPluginInstallScriptResponse`
        """
        http_info = self._list_plugin_install_script_http_info(request)
        return self._call_api(**http_info)

    def list_plugin_install_script_async_invoker(self, request):
        http_info = self._list_plugin_install_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugin_install_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/docker-plugin-install-script",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginInstallScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'outside_host' in local_var_params:
            query_params.append(('outside_host', local_var_params['outside_host']))
        if 'batch_install' in local_var_params:
            query_params.append(('batch_install', local_var_params['batch_install']))
        if 'plugin' in local_var_params:
            query_params.append(('plugin', local_var_params['plugin']))
        if 'operate_type' in local_var_params:
            query_params.append(('operate_type', local_var_params['operate_type']))

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

    def list_plugins_async(self, request):
        r"""查询插件列表

        查询插件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlugins
        :type request: :class:`huaweicloudsdkhss.v5.ListPluginsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPluginsResponse`
        """
        http_info = self._list_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_plugins_async_invoker(self, request):
        http_info = self._list_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginsResponse"
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
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'detect_result' in local_var_params:
            query_params.append(('detect_result', local_var_params['detect_result']))
        if 'host_status' in local_var_params:
            query_params.append(('host_status', local_var_params['host_status']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'ip_addr' in local_var_params:
            query_params.append(('ip_addr', local_var_params['ip_addr']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'policy_group_id' in local_var_params:
            query_params.append(('policy_group_id', local_var_params['policy_group_id']))
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'refresh' in local_var_params:
            query_params.append(('refresh', local_var_params['refresh']))
        if 'above_version' in local_var_params:
            query_params.append(('above_version', local_var_params['above_version']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'plugin' in local_var_params:
            query_params.append(('plugin', local_var_params['plugin']))
        if 'outside_host' in local_var_params:
            query_params.append(('outside_host', local_var_params['outside_host']))

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

    def list_policies_async(self, request):
        r"""查询主机策略列表

        查询主机策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicies
        :type request: :class:`huaweicloudsdkhss.v5.ListPoliciesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPoliciesResponse`
        """
        http_info = self._list_policies_http_info(request)
        return self._call_api(**http_info)

    def list_policies_async_invoker(self, request):
        http_info = self._list_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/host-management/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoliciesResponse"
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
        if 'agent_id' in local_var_params:
            query_params.append(('agent_id', local_var_params['agent_id']))

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

    def list_port_host_async(self, request):
        r"""资产指纹-端口-服务器列表

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
        r"""查询开放端口统计信息

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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'port_string' in local_var_params:
            query_params.append(('port_string', local_var_params['port_string']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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
        r"""查询单服务器的开放端口列表

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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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
        r"""查询进程列表

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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

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
        r"""资产指纹-进程-服务器列表

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

    def list_project_tags_async(self, request):
        r"""查询租户当前项目下所有用过的标签

        查询租户当前项目下所有用过的标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkhss.v5.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_async_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_protection_policy_async(self, request):
        r"""查询勒索病毒的防护策略列表

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
        r"""查询勒索防护服务器列表

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

    def list_protection_servers_async(self, request):
        r"""查询防护服务器列表

        查询防护服务器列表：查询防护服务器相关数据，包含服务器名称、ip地址、操作系统、服务器组名称、防护策略、防护状态、微服务防护状态、RASP防护状态、RASP攻击数量信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectionServers
        :type request: :class:`huaweicloudsdkhss.v5.ListProtectionServersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProtectionServersResponse`
        """
        http_info = self._list_protection_servers_http_info(request)
        return self._call_api(**http_info)

    def list_protection_servers_async_invoker(self, request):
        http_info = self._list_protection_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_protection_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/rasp/servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListProtectionServersResponse"
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
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'app_status' in local_var_params:
            query_params.append(('app_status', local_var_params['app_status']))

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

    def list_query_export_task_async(self, request):
        r"""查询导出任务信息

        查询导出任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQueryExportTask
        :type request: :class:`huaweicloudsdkhss.v5.ListQueryExportTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListQueryExportTaskResponse`
        """
        http_info = self._list_query_export_task_http_info(request)
        return self._call_api(**http_info)

    def list_query_export_task_async_invoker(self, request):
        http_info = self._list_query_export_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_query_export_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/export-task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryExportTaskResponse"
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
        r"""查询配额详情

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

    def list_ransomware_protection_nodes_async(self, request):
        r"""查询勒索防护服务器列表2.0

        查询勒索防护服务器列表，与云备份服务配合使用。因此使用勒索相关接口之前确保该局点有云备份服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRansomwareProtectionNodes
        :type request: :class:`huaweicloudsdkhss.v5.ListRansomwareProtectionNodesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRansomwareProtectionNodesResponse`
        """
        http_info = self._list_ransomware_protection_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_ransomware_protection_nodes_async_invoker(self, request):
        http_info = self._list_ransomware_protection_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ransomware_protection_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/ransomware/servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListRansomwareProtectionNodesResponse"
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
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'host_status' in local_var_params:
            query_params.append(('host_status', local_var_params['host_status']))
        if 'ransom_protection_status' in local_var_params:
            query_params.append(('ransom_protection_status', local_var_params['ransom_protection_status']))
        if 'protect_policy_name' in local_var_params:
            query_params.append(('protect_policy_name', local_var_params['protect_policy_name']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))

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

    def list_rasp_events_async(self, request):
        r"""查询应用防护事件列表

        查询应用防护事件列表：展示防护事件相关信息，包含告警级别、服务器名称、告警名称、告警时间、攻击源ip、攻击源url数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRaspEvents
        :type request: :class:`huaweicloudsdkhss.v5.ListRaspEventsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRaspEventsResponse`
        """
        http_info = self._list_rasp_events_http_info(request)
        return self._call_api(**http_info)

    def list_rasp_events_async_invoker(self, request):
        http_info = self._list_rasp_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_rasp_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/rasp/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListRaspEventsResponse"
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
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'attack_tag' in local_var_params:
            query_params.append(('attack_tag', local_var_params['attack_tag']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))

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

    def list_rasp_policies_async(self, request):
        r"""查询防护策略列表

        查询防护策略列表：查询创建的防护策略信息，包含防护策略名称、检测规则、关联服务器数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRaspPolicies
        :type request: :class:`huaweicloudsdkhss.v5.ListRaspPoliciesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRaspPoliciesResponse`
        """
        http_info = self._list_rasp_policies_http_info(request)
        return self._call_api(**http_info)

    def list_rasp_policies_async_invoker(self, request):
        http_info = self._list_rasp_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_rasp_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/rasp/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListRaspPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))

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
        r"""查询指定安全配置项的检查项列表

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
        r"""查询指定安全配置项的受影响服务器列表

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
        r"""查询租户的服务器安全配置检测结果列表

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
        r"""查入侵事件列表

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
        if 'auto_block' in local_var_params:
            query_params.append(('auto_block', local_var_params['auto_block']))

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

    def list_security_group_policies_async(self, request):
        r"""查询云原生网络模式2.0的集群已配置的安全组策略

        查询云原生网络模式2.0的集群已配置的安全组策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroupPolicies
        :type request: :class:`huaweicloudsdkhss.v5.ListSecurityGroupPoliciesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListSecurityGroupPoliciesResponse`
        """
        http_info = self._list_security_group_policies_http_info(request)
        return self._call_api(**http_info)

    def list_security_group_policies_async_invoker(self, request):
        http_info = self._list_security_group_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_security_group_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/security-group-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecurityGroupPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
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

    def list_security_groups_async(self, request):
        r"""查询企业项目下所有的安全组列表

        查询企业项目下所有的安全组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroups
        :type request: :class:`huaweicloudsdkhss.v5.ListSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListSecurityGroupsResponse`
        """
        http_info = self._list_security_groups_http_info(request)
        return self._call_api(**http_info)

    def list_security_groups_async_invoker(self, request):
        http_info = self._list_security_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_security_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecurityGroupsResponse"
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

    def list_swr_image_repository_async(self, request):
        r"""查询swr镜像仓库镜像列表-接口已废弃，不再推荐使用

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

    def list_system_user_white_list_async(self, request):
        r"""查询系统用白名单列表

        查询系统用户白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSystemUserWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.ListSystemUserWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListSystemUserWhiteListResponse`
        """
        http_info = self._list_system_user_white_list_http_info(request)
        return self._call_api(**http_info)

    def list_system_user_white_list_async_invoker(self, request):
        http_info = self._list_system_user_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_system_user_white_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/white-list/userlist",
            "request_type": request.__class__.__name__,
            "response_type": "ListSystemUserWhiteListResponse"
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
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'system_user_name' in local_var_params:
            query_params.append(('system_user_name', local_var_params['system_user_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_two_factor_login_host_async(self, request):
        r"""查询双因子主机列表

        查询双因子主机列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTwoFactorLoginHost
        :type request: :class:`huaweicloudsdkhss.v5.ListTwoFactorLoginHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListTwoFactorLoginHostResponse`
        """
        http_info = self._list_two_factor_login_host_http_info(request)
        return self._call_api(**http_info)

    def list_two_factor_login_host_async_invoker(self, request):
        http_info = self._list_two_factor_login_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_two_factor_login_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/two-factor-login/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListTwoFactorLoginHostResponse"
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
        if 'display_name' in local_var_params:
            query_params.append(('display_name', local_var_params['display_name']))
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

    def list_user_change_histories_async(self, request):
        r"""获取账户变动历史信息

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
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'root_permission' in local_var_params:
            query_params.append(('root_permission', local_var_params['root_permission']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'change_type' in local_var_params:
            query_params.append(('change_type', local_var_params['change_type']))
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

    def list_user_statistics_async(self, request):
        r"""查询账号信息列表

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
        r"""查询账号的服务器列表

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

    def list_vul_handle_history_async(self, request):
        r"""查询漏洞历史处置记录列表

        查询漏洞历史处置记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulHandleHistory
        :type request: :class:`huaweicloudsdkhss.v5.ListVulHandleHistoryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulHandleHistoryResponse`
        """
        http_info = self._list_vul_handle_history_http_info(request)
        return self._call_api(**http_info)

    def list_vul_handle_history_async_invoker(self, request):
        http_info = self._list_vul_handle_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_handle_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/handle-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulHandleHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'vul_type' in local_var_params:
            query_params.append(('vul_type', local_var_params['vul_type']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
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

    def list_vul_host_apps_async(self, request):
        r"""查询受影响服务器详情-软件列表

        查询受影响服务器详情-软件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulHostApps
        :type request: :class:`huaweicloudsdkhss.v5.ListVulHostAppsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulHostAppsResponse`
        """
        http_info = self._list_vul_host_apps_http_info(request)
        return self._call_api(**http_info)

    def list_vul_host_apps_async_invoker(self, request):
        http_info = self._list_vul_host_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_host_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/{host_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulHostAppsResponse"
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
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'container_id' in local_var_params:
            query_params.append(('container_id', local_var_params['container_id']))
        if 'is_container' in local_var_params:
            query_params.append(('is_container', local_var_params['is_container']))

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

    def list_vul_host_backups_async(self, request):
        r"""查询可回滚的备份列表

        查询可回滚的备份列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulHostBackups
        :type request: :class:`huaweicloudsdkhss.v5.ListVulHostBackupsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulHostBackupsResponse`
        """
        http_info = self._list_vul_host_backups_http_info(request)
        return self._call_api(**http_info)

    def list_vul_host_backups_async_invoker(self, request):
        http_info = self._list_vul_host_backups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_host_backups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/backup/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulHostBackupsResponse"
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

    def list_vul_host_process_async(self, request):
        r"""查询受影响服务器详情-进程列表

        查询受影响服务器详情-进程列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulHostProcess
        :type request: :class:`huaweicloudsdkhss.v5.ListVulHostProcessRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulHostProcessResponse`
        """
        http_info = self._list_vul_host_process_http_info(request)
        return self._call_api(**http_info)

    def list_vul_host_process_async_invoker(self, request):
        http_info = self._list_vul_host_process_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_host_process_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/{host_id}/process",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulHostProcessResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'container_id' in local_var_params:
            query_params.append(('container_id', local_var_params['container_id']))

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

    def list_vul_host_vaults_async(self, request):
        r"""查询处理对应的主机存储库的列表

        查询处理对应的主机存储库的列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulHostVaults
        :type request: :class:`huaweicloudsdkhss.v5.ListVulHostVaultsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulHostVaultsResponse`
        """
        http_info = self._list_vul_host_vaults_http_info(request)
        return self._call_api(**http_info)

    def list_vul_host_vaults_async_invoker(self, request):
        http_info = self._list_vul_host_vaults_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_host_vaults_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/backup/host-vaults",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulHostVaultsResponse"
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
        if 'backup_info_id' in local_var_params:
            query_params.append(('backup_info_id', local_var_params['backup_info_id']))

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
        r"""漏洞对应cve信息

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
        r"""查询弱口令检测结果列表

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

    def list_web_app_and_service_statistics_async(self, request):
        r"""资产管理-资产指纹-左侧WebAppAndService名称树信息

        资产管理-资产指纹-左侧WebAppAndService名称树信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebAppAndServiceStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListWebAppAndServiceStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebAppAndServiceStatisticsResponse`
        """
        http_info = self._list_web_app_and_service_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_web_app_and_service_statistics_async_invoker(self, request):
        http_info = self._list_web_app_and_service_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_app_and_service_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/web-app-and-service-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebAppAndServiceStatisticsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'catalogue' in local_var_params:
            query_params.append(('catalogue', local_var_params['catalogue']))

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

    def list_web_app_and_services_async(self, request):
        r"""资产管理-资产指纹-右侧WebAppAndService资产信息

        资产管理-资产指纹-右侧WebAppAndService资产信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebAppAndServices
        :type request: :class:`huaweicloudsdkhss.v5.ListWebAppAndServicesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebAppAndServicesResponse`
        """
        http_info = self._list_web_app_and_services_http_info(request)
        return self._call_api(**http_info)

    def list_web_app_and_services_async_invoker(self, request):
        http_info = self._list_web_app_and_services_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_app_and_services_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/web-app-and-services",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebAppAndServicesResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'catalogue' in local_var_params:
            query_params.append(('catalogue', local_var_params['catalogue']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'install_dir' in local_var_params:
            query_params.append(('install_dir', local_var_params['install_dir']))
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

    def list_web_framework_host_info_async(self, request):
        r"""资产管理-资产指纹-Web框架的服务器列表

        资产管理-资产指纹-Web框架的服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebFrameworkHostInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListWebFrameworkHostInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebFrameworkHostInfoResponse`
        """
        http_info = self._list_web_framework_host_info_http_info(request)
        return self._call_api(**http_info)

    def list_web_framework_host_info_async_invoker(self, request):
        http_info = self._list_web_framework_host_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_framework_host_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/host/web-framework",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebFrameworkHostInfoResponse"
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
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
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

    def list_web_framework_info_async(self, request):
        r"""资产管理-主机管理-指纹类型-Web框架

        资产管理-主机管理-指纹类型-Web框架
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebFrameworkInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListWebFrameworkInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebFrameworkInfoResponse`
        """
        http_info = self._list_web_framework_info_http_info(request)
        return self._call_api(**http_info)

    def list_web_framework_info_async_invoker(self, request):
        http_info = self._list_web_framework_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_framework_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/{host_id}/web-framework",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebFrameworkInfoResponse"
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
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
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

    def list_web_framework_statistics_async(self, request):
        r"""资产管理-资产指纹-Web框架左侧树

        资产管理-资产指纹-Web框架左侧树
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebFrameworkStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListWebFrameworkStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebFrameworkStatisticsResponse`
        """
        http_info = self._list_web_framework_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_web_framework_statistics_async_invoker(self, request):
        http_info = self._list_web_framework_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_framework_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/statistics/web-framework",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebFrameworkStatisticsResponse"
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
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
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

    def list_web_site_host_info_async(self, request):
        r"""资产管理-资产指纹-Web站点的服务器列表

        资产管理-资产指纹-Web站点的服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebSiteHostInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListWebSiteHostInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebSiteHostInfoResponse`
        """
        http_info = self._list_web_site_host_info_http_info(request)
        return self._call_api(**http_info)

    def list_web_site_host_info_async_invoker(self, request):
        http_info = self._list_web_site_host_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_site_host_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/host/web-site",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebSiteHostInfoResponse"
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
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
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

    def list_web_site_info_async(self, request):
        r"""资产管理-主机管理-指纹类型-Web站点

        资产管理-主机管理-指纹类型-Web站点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebSiteInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListWebSiteInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebSiteInfoResponse`
        """
        http_info = self._list_web_site_info_http_info(request)
        return self._call_api(**http_info)

    def list_web_site_info_async_invoker(self, request):
        http_info = self._list_web_site_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_site_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/{host_id}/web-site",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebSiteInfoResponse"
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
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
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

    def list_web_site_statistics_async(self, request):
        r"""资产管理-资产指纹-Web站点左侧树

        资产管理-资产指纹-Web站点左侧树
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebSiteStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListWebSiteStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebSiteStatisticsResponse`
        """
        http_info = self._list_web_site_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_web_site_statistics_async_invoker(self, request):
        http_info = self._list_web_site_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_site_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/statistics/web-site",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebSiteStatisticsResponse"
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
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def list_work_loads_async(self, request):
        r"""查询集群下某一命名空间下的工作负载

        查询集群下某一命名空间下的工作负载
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkLoads
        :type request: :class:`huaweicloudsdkhss.v5.ListWorkLoadsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWorkLoadsResponse`
        """
        http_info = self._list_work_loads_http_info(request)
        return self._call_api(**http_info)

    def list_work_loads_async_invoker(self, request):
        http_info = self._list_work_loads_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_work_loads_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/{namespace}/workloads",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkLoadsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'workload_type' in local_var_params:
            query_params.append(('workload_type', local_var_params['workload_type']))

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

    def modify_decoy_port_policy_async(self, request):
        r"""编辑动态端口蜜罐策略

        编辑动态端口蜜罐策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyDecoyPortPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ModifyDecoyPortPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ModifyDecoyPortPolicyResponse`
        """
        http_info = self._modify_decoy_port_policy_http_info(request)
        return self._call_api(**http_info)

    def modify_decoy_port_policy_async_invoker(self, request):
        http_info = self._modify_decoy_port_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_decoy_port_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/honeypot-port/policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyDecoyPortPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def remove_alarm_white_list_async(self, request):
        r"""删除告警白名单

        删除告警白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveAlarmWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.RemoveAlarmWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.RemoveAlarmWhiteListResponse`
        """
        http_info = self._remove_alarm_white_list_http_info(request)
        return self._call_api(**http_info)

    def remove_alarm_white_list_async_invoker(self, request):
        http_info = self._remove_alarm_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_alarm_white_list_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/event/white-list/alarm",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveAlarmWhiteListResponse"
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

    def remove_login_white_list_async(self, request):
        r"""删除登录白名单

        删除登录白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveLoginWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.RemoveLoginWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.RemoveLoginWhiteListResponse`
        """
        http_info = self._remove_login_white_list_http_info(request)
        return self._call_api(**http_info)

    def remove_login_white_list_async_invoker(self, request):
        http_info = self._remove_login_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_login_white_list_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/event/white-list/login",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveLoginWhiteListResponse"
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

    def remove_system_user_white_list_async(self, request):
        r"""删除系统用户白名单

        删除系统用户白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveSystemUserWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.RemoveSystemUserWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.RemoveSystemUserWhiteListResponse`
        """
        http_info = self._remove_system_user_white_list_http_info(request)
        return self._call_api(**http_info)

    def remove_system_user_white_list_async_invoker(self, request):
        http_info = self._remove_system_user_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_system_user_white_list_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/event/white-list/userlist",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveSystemUserWhiteListResponse"
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

    def restore_vul_host_backup_async(self, request):
        r"""用备份进行回滚

        用备份进行回滚
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreVulHostBackup
        :type request: :class:`huaweicloudsdkhss.v5.RestoreVulHostBackupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.RestoreVulHostBackupResponse`
        """
        http_info = self._restore_vul_host_backup_http_info(request)
        return self._call_api(**http_info)

    def restore_vul_host_backup_async_invoker(self, request):
        http_info = self._restore_vul_host_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_vul_host_backup_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/vulnerability/backup/{backup_id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreVulHostBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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

    def run_host_asset_manual_collect_async(self, request):
        r"""采集单主机资产指纹

        采集单主机资产指纹
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunHostAssetManualCollect
        :type request: :class:`huaweicloudsdkhss.v5.RunHostAssetManualCollectRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.RunHostAssetManualCollectResponse`
        """
        http_info = self._run_host_asset_manual_collect_http_info(request)
        return self._call_api(**http_info)

    def run_host_asset_manual_collect_async_invoker(self, request):
        http_info = self._run_host_asset_manual_collect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_host_asset_manual_collect_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/asset/manual-collect/{type}",
            "request_type": request.__class__.__name__,
            "response_type": "RunHostAssetManualCollectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def run_image_synchronize_async(self, request):
        r"""从SWR服务同步镜像列表

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

    def set_malware_reminders_async(self, request):
        r"""设置提示信息配置

        设置提示信息配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetMalwareReminders
        :type request: :class:`huaweicloudsdkhss.v5.SetMalwareRemindersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SetMalwareRemindersResponse`
        """
        http_info = self._set_malware_reminders_http_info(request)
        return self._call_api(**http_info)

    def set_malware_reminders_async_invoker(self, request):
        http_info = self._set_malware_reminders_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_malware_reminders_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/setting/malware/reminders",
            "request_type": request.__class__.__name__,
            "response_type": "SetMalwareRemindersResponse"
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

    def set_two_factor_login_config_async(self, request):
        r"""设置双因子登录配置

        设置双因子登录配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetTwoFactorLoginConfig
        :type request: :class:`huaweicloudsdkhss.v5.SetTwoFactorLoginConfigRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SetTwoFactorLoginConfigResponse`
        """
        http_info = self._set_two_factor_login_config_http_info(request)
        return self._call_api(**http_info)

    def set_two_factor_login_config_async_invoker(self, request):
        http_info = self._set_two_factor_login_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_two_factor_login_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/setting/two-factor-login/config",
            "request_type": request.__class__.__name__,
            "response_type": "SetTwoFactorLoginConfigResponse"
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

    def show_agent_statistics_status_async(self, request):
        r"""资产管理-概览-资产状态-主机Agent状态

        资产管理-概览-资产状态-主机Agent状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgentStatisticsStatus
        :type request: :class:`huaweicloudsdkhss.v5.ShowAgentStatisticsStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAgentStatisticsStatusResponse`
        """
        http_info = self._show_agent_statistics_status_http_info(request)
        return self._call_api(**http_info)

    def show_agent_statistics_status_async_invoker(self, request):
        http_info = self._show_agent_statistics_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agent_statistics_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/overview/status/agent",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgentStatisticsStatusResponse"
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

    def show_app_rasp_switch_status_async(self, request):
        r"""查询应用防护开启状态

        查询应用防护开启状态：查询单台服务器的应用防护功能开启状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppRaspSwitchStatus
        :type request: :class:`huaweicloudsdkhss.v5.ShowAppRaspSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAppRaspSwitchStatusResponse`
        """
        http_info = self._show_app_rasp_switch_status_http_info(request)
        return self._call_api(**http_info)

    def show_app_rasp_switch_status_async_invoker(self, request):
        http_info = self._show_app_rasp_switch_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_rasp_switch_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/rasp/{host_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppRaspSwitchStatusResponse"
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
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))

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

    def show_asset_statistic_async(self, request):
        r"""统计资产信息，账号、端口、进程等

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
        r"""查询HSS存储库绑定的备份策略信息

        查询HSS存储库绑定的备份策略信息，确保已经购买了勒索防护存储库，可以从cbr云备份服务进行验证，确保已经存在HSS_projectid命名的存储库已经购买
        
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

    def show_baseline_scan_status_async(self, request):
        r"""查询基线扫描手动检测结果

        查询基线扫描手动检测结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBaselineScanStatus
        :type request: :class:`huaweicloudsdkhss.v5.ShowBaselineScanStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowBaselineScanStatusResponse`
        """
        http_info = self._show_baseline_scan_status_http_info(request)
        return self._call_api(**http_info)

    def show_baseline_scan_status_async_invoker(self, request):
        http_info = self._show_baseline_scan_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_baseline_scan_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/scan-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBaselineScanStatusResponse"
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

    def show_baseline_white_list_async(self, request):
        r"""查询基线白名单

        查询基线白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBaselineWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.ShowBaselineWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowBaselineWhiteListResponse`
        """
        http_info = self._show_baseline_white_list_http_info(request)
        return self._call_api(**http_info)

    def show_baseline_white_list_async_invoker(self, request):
        http_info = self._show_baseline_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_baseline_white_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/whitelist",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBaselineWhiteListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def show_check_rule_detail_async(self, request):
        r"""查询配置检查项检测报告

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

    def show_cluster_asset_statistics_async(self, request):
        r"""查询集群资产统计数量

        查询集群资产统计数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterAssetStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowClusterAssetStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowClusterAssetStatisticsResponse`
        """
        http_info = self._show_cluster_asset_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_asset_statistics_async_invoker(self, request):
        http_info = self._show_cluster_asset_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_asset_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/cluster/asset/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterAssetStatisticsResponse"
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

    def show_cluster_protect_policy_template_async(self, request):
        r"""查询集群组件防护策略模板

        查询集群防护策略模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterProtectPolicyTemplate
        :type request: :class:`huaweicloudsdkhss.v5.ShowClusterProtectPolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowClusterProtectPolicyTemplateResponse`
        """
        http_info = self._show_cluster_protect_policy_template_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_protect_policy_template_async_invoker(self, request):
        http_info = self._show_cluster_protect_policy_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_protect_policy_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/clusters/protection-policy-templates/{policy_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterProtectPolicyTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_template_id' in local_var_params:
            path_params['policy_template_id'] = local_var_params['policy_template_id']

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

    def show_common_port_async(self, request):
        r"""呈现某一端口详细信息

        呈现某一端口详细信息，如本地端口：80，类型：TCP，危险程度：正常，端口描述：常用于SSH(SecureShell)-远程登录协议，用于安全登录文件传输（SCP，SFTP）及端口重新定向。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCommonPort
        :type request: :class:`huaweicloudsdkhss.v5.ShowCommonPortRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowCommonPortResponse`
        """
        http_info = self._show_common_port_http_info(request)
        return self._call_api(**http_info)

    def show_common_port_async_invoker(self, request):
        http_info = self._show_common_port_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_common_port_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/common-port-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommonPortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'categoty' in local_var_params:
            query_params.append(('categoty', local_var_params['categoty']))

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

    def show_container_network_info_async(self, request):
        r"""查询容器集群网络的网络信息

        查询容器集群网络的网络信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowContainerNetworkInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowContainerNetworkInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowContainerNetworkInfoResponse`
        """
        http_info = self._show_container_network_info_http_info(request)
        return self._call_api(**http_info)

    def show_container_network_info_async_invoker(self, request):
        http_info = self._show_container_network_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_container_network_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/network-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowContainerNetworkInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def show_container_node_statistics_async(self, request):
        r"""查询容器节点防护总览数据

        查询容器节点防护总览数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowContainerNodeStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowContainerNodeStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowContainerNodeStatisticsResponse`
        """
        http_info = self._show_container_node_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_container_node_statistics_async_invoker(self, request):
        http_info = self._show_container_node_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_container_node_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/node-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowContainerNodeStatisticsResponse"
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

    def show_container_protection_status_async(self, request):
        r"""资产管理-概览-资产状态-容器节点防护状态

        资产管理-概览-资产状态-容器节点防护状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowContainerProtectionStatus
        :type request: :class:`huaweicloudsdkhss.v5.ShowContainerProtectionStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowContainerProtectionStatusResponse`
        """
        http_info = self._show_container_protection_status_http_info(request)
        return self._call_api(**http_info)

    def show_container_protection_status_async_invoker(self, request):
        http_info = self._show_container_protection_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_container_protection_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/overview/status/container/protection",
            "request_type": request.__class__.__name__,
            "response_type": "ShowContainerProtectionStatusResponse"
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

    def show_decoy_port_policy_details_async(self, request):
        r"""查看动态端口蜜罐策略详情

        查看动态端口蜜罐策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDecoyPortPolicyDetails
        :type request: :class:`huaweicloudsdkhss.v5.ShowDecoyPortPolicyDetailsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowDecoyPortPolicyDetailsResponse`
        """
        http_info = self._show_decoy_port_policy_details_http_info(request)
        return self._call_api(**http_info)

    def show_decoy_port_policy_details_async_invoker(self, request):
        http_info = self._show_decoy_port_policy_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_decoy_port_policy_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/honeypot-port/policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDecoyPortPolicyDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def show_event_attack_tag_async(self, request):
        r"""查询攻击标识分布统计列表

        查询攻击标识分布统计列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEventAttackTag
        :type request: :class:`huaweicloudsdkhss.v5.ShowEventAttackTagRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowEventAttackTagResponse`
        """
        http_info = self._show_event_attack_tag_http_info(request)
        return self._call_api(**http_info)

    def show_event_attack_tag_async_invoker(self, request):
        http_info = self._show_event_attack_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_event_attack_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/event/attack-tag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEventAttackTagResponse"
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
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
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
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
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

    def show_host_asset_manual_collect_status_async(self, request):
        r"""查询单主机资产指纹采集状态

        查询单主机资产指纹采集状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHostAssetManualCollectStatus
        :type request: :class:`huaweicloudsdkhss.v5.ShowHostAssetManualCollectStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowHostAssetManualCollectStatusResponse`
        """
        http_info = self._show_host_asset_manual_collect_status_http_info(request)
        return self._call_api(**http_info)

    def show_host_asset_manual_collect_status_async_invoker(self, request):
        http_info = self._show_host_asset_manual_collect_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_host_asset_manual_collect_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/manual-collect/{type}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHostAssetManualCollectStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def show_host_protection_status_async(self, request):
        r"""资产管理-概览-资产状态-Agent状态

        资产管理-概览-资产状态-Agent状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHostProtectionStatus
        :type request: :class:`huaweicloudsdkhss.v5.ShowHostProtectionStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowHostProtectionStatusResponse`
        """
        http_info = self._show_host_protection_status_http_info(request)
        return self._call_api(**http_info)

    def show_host_protection_status_async_invoker(self, request):
        http_info = self._show_host_protection_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_host_protection_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/overview/status/host/protection",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHostProtectionStatusResponse"
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

    def show_image_asset_statistics_async(self, request):
        r"""容器资产-镜像统计

        容器资产-镜像统计
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageAssetStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowImageAssetStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowImageAssetStatisticsResponse`
        """
        http_info = self._show_image_asset_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_image_asset_statistics_async_invoker(self, request):
        http_info = self._show_image_asset_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_asset_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/asset/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageAssetStatisticsResponse"
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

    def show_image_check_rule_detail_async(self, request):
        r"""查询镜像配置检查项检测报告

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
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
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

    def show_k8s_container_detail_async(self, request):
        r"""查询容器详细信息

        查询容器详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowK8sContainerDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowK8sContainerDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowK8sContainerDetailResponse`
        """
        http_info = self._show_k8s_container_detail_http_info(request)
        return self._call_api(**http_info)

    def show_k8s_container_detail_async_invoker(self, request):
        http_info = self._show_k8s_container_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_k8s_container_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/container/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowK8sContainerDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'container_id' in local_var_params:
            query_params.append(('container_id', local_var_params['container_id']))

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

    def show_k8s_pod_detail_async(self, request):
        r"""查询pod详细信息

        查询pod详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowK8sPodDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowK8sPodDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowK8sPodDetailResponse`
        """
        http_info = self._show_k8s_pod_detail_http_info(request)
        return self._call_api(**http_info)

    def show_k8s_pod_detail_async_invoker(self, request):
        http_info = self._show_k8s_pod_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_k8s_pod_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/{pod_name}/pod/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowK8sPodDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pod_name' in local_var_params:
            path_params['pod_name'] = local_var_params['pod_name']

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

    def show_kubernetes_endpoint_info_async(self, request):
        r"""查询容器Kubernetes端点详情

        查询容器Kubernetes端点详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKubernetesEndpointInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowKubernetesEndpointInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowKubernetesEndpointInfoResponse`
        """
        http_info = self._show_kubernetes_endpoint_info_http_info(request)
        return self._call_api(**http_info)

    def show_kubernetes_endpoint_info_async_invoker(self, request):
        http_info = self._show_kubernetes_endpoint_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kubernetes_endpoint_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/endpoint/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKubernetesEndpointInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def show_kubernetes_service_info_async(self, request):
        r"""查询容器Kubernetes服务详情

        查询容器Kubernetes服务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKubernetesServiceInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowKubernetesServiceInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowKubernetesServiceInfoResponse`
        """
        http_info = self._show_kubernetes_service_info_http_info(request)
        return self._call_api(**http_info)

    def show_kubernetes_service_info_async_invoker(self, request):
        http_info = self._show_kubernetes_service_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kubernetes_service_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/kubernetes/service/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKubernetesServiceInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def show_latest_export_task_by_type_async(self, request):
        r"""查询导出任务信息-按查询条件

        查询导出任务信息-按查询条件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLatestExportTaskByType
        :type request: :class:`huaweicloudsdkhss.v5.ShowLatestExportTaskByTypeRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowLatestExportTaskByTypeResponse`
        """
        http_info = self._show_latest_export_task_by_type_http_info(request)
        return self._call_api(**http_info)

    def show_latest_export_task_by_type_async_invoker(self, request):
        http_info = self._show_latest_export_task_by_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_latest_export_task_by_type_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/export-task",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLatestExportTaskByTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'export_task_type' in local_var_params:
            query_params.append(('export_task_type', local_var_params['export_task_type']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def show_malware_reminders_async(self, request):
        r"""获取提示信息配置

        获取提示信息配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMalwareReminders
        :type request: :class:`huaweicloudsdkhss.v5.ShowMalwareRemindersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowMalwareRemindersResponse`
        """
        http_info = self._show_malware_reminders_http_info(request)
        return self._call_api(**http_info)

    def show_malware_reminders_async_invoker(self, request):
        http_info = self._show_malware_reminders_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_malware_reminders_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/malware/reminders",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMalwareRemindersResponse"
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

    def show_network_statistics_async(self, request):
        r"""集群网络策略总览

        集群网络策略总览
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNetworkStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowNetworkStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowNetworkStatisticsResponse`
        """
        http_info = self._show_network_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_network_statistics_async_invoker(self, request):
        http_info = self._show_network_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_network_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/network-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNetworkStatisticsResponse"
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

    def show_os_statistics_info_async(self, request):
        r"""资产管理-概览-资产状态-操作系统统计信息

        资产管理-概览-资产状态-操作系统统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOsStatisticsInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowOsStatisticsInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowOsStatisticsInfoResponse`
        """
        http_info = self._show_os_statistics_info_http_info(request)
        return self._call_api(**http_info)

    def show_os_statistics_info_async_invoker(self, request):
        http_info = self._show_os_statistics_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_os_statistics_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/overview/status/os",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOsStatisticsInfoResponse"
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

    def show_page_notices_async(self, request):
        r"""获取页面通知信息

        获取页面通知信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPageNotices
        :type request: :class:`huaweicloudsdkhss.v5.ShowPageNoticesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowPageNoticesResponse`
        """
        http_info = self._show_page_notices_http_info(request)
        return self._call_api(**http_info)

    def show_page_notices_async_invoker(self, request):
        http_info = self._show_page_notices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_page_notices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/setting/page-notices",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPageNoticesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page_location' in local_var_params:
            query_params.append(('page_location', local_var_params['page_location']))

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

    def show_policy_switch_status_async(self, request):
        r"""查询指定策略的总开关

        查询指定策略的总开关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPolicySwitchStatus
        :type request: :class:`huaweicloudsdkhss.v5.ShowPolicySwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowPolicySwitchStatusResponse`
        """
        http_info = self._show_policy_switch_status_http_info(request)
        return self._call_api(**http_info)

    def show_policy_switch_status_async_invoker(self, request):
        http_info = self._show_policy_switch_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_policy_switch_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/policy/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicySwitchStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))

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

    def show_productdata_offering_infos_async(self, request):
        r"""查询产商品信息

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

    def show_quota_statistics_info_async(self, request):
        r"""资产管理-概览-资产状态-防护配额统计信息

        资产管理-概览-资产状态-防护配额统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotaStatisticsInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowQuotaStatisticsInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowQuotaStatisticsInfoResponse`
        """
        http_info = self._show_quota_statistics_info_http_info(request)
        return self._call_api(**http_info)

    def show_quota_statistics_info_async_invoker(self, request):
        http_info = self._show_quota_statistics_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quota_statistics_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/asset/overview/status/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaStatisticsInfoResponse"
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

    def show_rasp_policy_detail_async(self, request):
        r"""查询防护策略详情

        查询防护策略详情：查询防护策略配置的相关检测规则信息，包含14种检测规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRaspPolicyDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowRaspPolicyDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowRaspPolicyDetailResponse`
        """
        http_info = self._show_rasp_policy_detail_http_info(request)
        return self._call_api(**http_info)

    def show_rasp_policy_detail_async_invoker(self, request):
        http_info = self._show_rasp_policy_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rasp_policy_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/rasp/policy/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRaspPolicyDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))

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

    def show_rasp_protect_statistics_async(self, request):
        r"""防护数据统计

        防护数据统计：统计已添加防护服务器的数量以及近七天微服务RASP攻击数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRaspProtectStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowRaspProtectStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowRaspProtectStatisticsResponse`
        """
        http_info = self._show_rasp_protect_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_rasp_protect_statistics_async_invoker(self, request):
        http_info = self._show_rasp_protect_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rasp_protect_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/rasp/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRaspProtectStatisticsResponse"
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

    def show_rasp_server_detail_async(self, request):
        r"""查询防护服务器java应用详情

        查询防护服务器java应用详情：查询防护服务器的java应用状态列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRaspServerDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowRaspServerDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowRaspServerDetailResponse`
        """
        http_info = self._show_rasp_server_detail_http_info(request)
        return self._call_api(**http_info)

    def show_rasp_server_detail_async_invoker(self, request):
        http_info = self._show_rasp_server_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rasp_server_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/rasp/servers/{host_id}/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRaspServerDetailResponse"
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'app_protect_status' in local_var_params:
            query_params.append(('app_protect_status', local_var_params['app_protect_status']))

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

    def show_resource_quotas_async(self, request):
        r"""查询配额信息

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
        r"""查询指定安全配置项的检查结果

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

    def show_single_backup_policy_info_async(self, request):
        r"""查询单个备份策略信息

        查询单个备份策略信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSingleBackupPolicyInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowSingleBackupPolicyInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowSingleBackupPolicyInfoResponse`
        """
        http_info = self._show_single_backup_policy_info_http_info(request)
        return self._call_api(**http_info)

    def show_single_backup_policy_info_async_invoker(self, request):
        http_info = self._show_single_backup_policy_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_single_backup_policy_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/backup/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSingleBackupPolicyInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def show_vul_backup_statistics_async(self, request):
        r"""查询漏洞处理对应主机的备份相关统计信息

        查询漏洞处理对应主机的备份相关统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVulBackupStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowVulBackupStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowVulBackupStatisticsResponse`
        """
        http_info = self._show_vul_backup_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_vul_backup_statistics_async_invoker(self, request):
        http_info = self._show_vul_backup_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vul_backup_statistics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vulnerability/backup-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVulBackupStatisticsResponse"
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

    def show_vul_report_data_async(self, request):
        r"""漏洞管理-主机视图-主机列表-导出报告

        在主机试图中导出漏洞报告详细报告pdf格式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVulReportData
        :type request: :class:`huaweicloudsdkhss.v5.ShowVulReportDataRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowVulReportDataResponse`
        """
        http_info = self._show_vul_report_data_http_info(request)
        return self._call_api(**http_info)

    def show_vul_report_data_async_invoker(self, request):
        http_info = self._show_vul_report_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vul_report_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vulnerability/report/data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVulReportDataResponse"
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

    def start_auto_kill_virus_status_async(self, request):
        r"""开启或关闭程序自动隔离查杀

        开启或关闭程序自动隔离查杀
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartAutoKillVirusStatus
        :type request: :class:`huaweicloudsdkhss.v5.StartAutoKillVirusStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.StartAutoKillVirusStatusResponse`
        """
        http_info = self._start_auto_kill_virus_status_http_info(request)
        return self._call_api(**http_info)

    def start_auto_kill_virus_status_async_invoker(self, request):
        http_info = self._start_auto_kill_virus_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_auto_kill_virus_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/setting/virus-kill",
            "request_type": request.__class__.__name__,
            "response_type": "StartAutoKillVirusStatusResponse"
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

    def start_protection_async(self, request):
        r"""开启勒索病毒防护

        开启勒索病毒防护，请保证该region有cbr云备份服务，勒索服务与云备份服务有关联关系
        
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
        r"""关闭勒索病毒防护

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

    def switch_cluster_protection_mode_async(self, request):
        r"""操作集群防护模式

        操作集群防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchClusterProtectionMode
        :type request: :class:`huaweicloudsdkhss.v5.SwitchClusterProtectionModeRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchClusterProtectionModeResponse`
        """
        http_info = self._switch_cluster_protection_mode_http_info(request)
        return self._call_api(**http_info)

    def switch_cluster_protection_mode_async_invoker(self, request):
        http_info = self._switch_cluster_protection_mode_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_cluster_protection_mode_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/cluster-protect/switch-mod",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchClusterProtectionModeResponse"
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

    def switch_container_protect_status_async(self, request):
        r"""切换防护状态

        切换防护状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchContainerProtectStatus
        :type request: :class:`huaweicloudsdkhss.v5.SwitchContainerProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchContainerProtectStatusResponse`
        """
        http_info = self._switch_container_protect_status_http_info(request)
        return self._call_api(**http_info)

    def switch_container_protect_status_async_invoker(self, request):
        http_info = self._switch_container_protect_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_container_protect_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/switch-version",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchContainerProtectStatusResponse"
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

    def switch_decoy_port_host_policy_async(self, request):
        r"""切换主机动态端口蜜罐策略

        切换主机动态端口蜜罐策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchDecoyPortHostPolicy
        :type request: :class:`huaweicloudsdkhss.v5.SwitchDecoyPortHostPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchDecoyPortHostPolicyResponse`
        """
        http_info = self._switch_decoy_port_host_policy_http_info(request)
        return self._call_api(**http_info)

    def switch_decoy_port_host_policy_async_invoker(self, request):
        http_info = self._switch_decoy_port_host_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_decoy_port_host_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/honeypot-port/host-policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchDecoyPortHostPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def switch_hosts_protect_status_async(self, request):
        r"""切换防护状态

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

    def switch_rasp_async(self, request):
        r"""开启/关闭应用防护，更新防护端口

        开启/关闭应用防护，选择开启的防护策略，选择需要防护的服务器，下发防护策略，可传入端口号更新防护端口，关闭防护则清空策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchRasp
        :type request: :class:`huaweicloudsdkhss.v5.SwitchRaspRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchRaspResponse`
        """
        http_info = self._switch_rasp_http_info(request)
        return self._call_api(**http_info)

    def switch_rasp_async_invoker(self, request):
        http_info = self._switch_rasp_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_rasp_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/rasp/status",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchRaspResponse"
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

    def sync_cluster_list_async(self, request):
        r"""同步容器集群最新数据

        同步容器集群最新数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncClusterList
        :type request: :class:`huaweicloudsdkhss.v5.SyncClusterListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SyncClusterListResponse`
        """
        http_info = self._sync_cluster_list_http_info(request)
        return self._call_api(**http_info)

    def sync_cluster_list_async_invoker(self, request):
        http_info = self._sync_cluster_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_cluster_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/cluster/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncClusterListResponse"
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

    def sync_cluster_protection_event_async(self, request):
        r"""同步集群防护事件

        同步集群防护事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncClusterProtectionEvent
        :type request: :class:`huaweicloudsdkhss.v5.SyncClusterProtectionEventRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SyncClusterProtectionEventResponse`
        """
        http_info = self._sync_cluster_protection_event_http_info(request)
        return self._call_api(**http_info)

    def sync_cluster_protection_event_async_invoker(self, request):
        http_info = self._sync_cluster_protection_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_cluster_protection_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/clusters/protection-event-sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncClusterProtectionEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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

    def sync_container_network_node_async(self, request):
        r"""同步集群下网络节点最新数据

        同步集群下容器网络策略最新数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncContainerNetworkNode
        :type request: :class:`huaweicloudsdkhss.v5.SyncContainerNetworkNodeRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SyncContainerNetworkNodeResponse`
        """
        http_info = self._sync_container_network_node_http_info(request)
        return self._call_api(**http_info)

    def sync_container_network_node_async_invoker(self, request):
        http_info = self._sync_container_network_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_container_network_node_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/node-sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncContainerNetworkNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def sync_container_network_policy_list_async(self, request):
        r"""同步集群下容器网络策略最新数据

        同步集群下容器网络策略最新数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncContainerNetworkPolicyList
        :type request: :class:`huaweicloudsdkhss.v5.SyncContainerNetworkPolicyListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SyncContainerNetworkPolicyListResponse`
        """
        http_info = self._sync_container_network_policy_list_http_info(request)
        return self._call_api(**http_info)

    def sync_container_network_policy_list_async_invoker(self, request):
        http_info = self._sync_container_network_policy_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_container_network_policy_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/policy-sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncContainerNetworkPolicyListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def sync_security_group_policies_async(self, request):
        r"""同步集群下安全组策略最新数据

        同步集群下安全组策略最新数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncSecurityGroupPolicies
        :type request: :class:`huaweicloudsdkhss.v5.SyncSecurityGroupPoliciesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SyncSecurityGroupPoliciesResponse`
        """
        http_info = self._sync_security_group_policies_http_info(request)
        return self._call_api(**http_info)

    def sync_security_group_policies_async_invoker(self, request):
        http_info = self._sync_security_group_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_security_group_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/security-group-policy-sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncSecurityGroupPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def update_backup_policy_info_async(self, request):
        r"""修改存储库绑定的备份策略

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

    def update_container_network_policy_async(self, request):
        r"""容器集群网络更新配置策略

        容器集群网络更新配置策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateContainerNetworkPolicy
        :type request: :class:`huaweicloudsdkhss.v5.UpdateContainerNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateContainerNetworkPolicyResponse`
        """
        http_info = self._update_container_network_policy_http_info(request)
        return self._call_api(**http_info)

    def update_container_network_policy_async_invoker(self, request):
        http_info = self._update_container_network_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_container_network_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateContainerNetworkPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def update_policy_async(self, request):
        r"""修改防护策略

        修改防护策略：修改防护策略内容，包含策略名称、相关规则开启状态、防护动作以及检测规则配置，同时给使用该策略的服务器下发新的策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicy
        :type request: :class:`huaweicloudsdkhss.v5.UpdatePolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdatePolicyResponse`
        """
        http_info = self._update_policy_http_info(request)
        return self._call_api(**http_info)

    def update_policy_async_invoker(self, request):
        http_info = self._update_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/rasp/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))

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

    def update_protection_policy_async(self, request):
        r"""修改勒索防护策略

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

    def update_security_group_policy_async(self, request):
        r"""更新安全组策略

        更新安全组策略(云原生网络模型)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSecurityGroupPolicy
        :type request: :class:`huaweicloudsdkhss.v5.UpdateSecurityGroupPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateSecurityGroupPolicyResponse`
        """
        http_info = self._update_security_group_policy_http_info(request)
        return self._call_api(**http_info)

    def update_security_group_policy_async_invoker(self, request):
        http_info = self._update_security_group_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_security_group_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/container-network/{cluster_id}/{namespace}/security-group-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecurityGroupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def update_system_user_white_list_async(self, request):
        r"""修改系统用户白名单

        修改系统用户白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSystemUserWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.UpdateSystemUserWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateSystemUserWhiteListResponse`
        """
        http_info = self._update_system_user_white_list_http_info(request)
        return self._call_api(**http_info)

    def update_system_user_white_list_async_invoker(self, request):
        http_info = self._update_system_user_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_system_user_white_list_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/event/white-list/userlist",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSystemUserWhiteListResponse"
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

    def add_app_whitelist_policy_host_async(self, request):
        r"""白名单策略添加主机

        白名单策略添加主机
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddAppWhitelistPolicyHost
        :type request: :class:`huaweicloudsdkhss.v5.AddAppWhitelistPolicyHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddAppWhitelistPolicyHostResponse`
        """
        http_info = self._add_app_whitelist_policy_host_http_info(request)
        return self._call_api(**http_info)

    def add_app_whitelist_policy_host_async_invoker(self, request):
        http_info = self._add_app_whitelist_policy_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_app_whitelist_policy_host_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/app/{policy_id}/host",
            "request_type": request.__class__.__name__,
            "response_type": "AddAppWhitelistPolicyHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def add_app_whitelist_policy_process_async(self, request):
        r"""新增进程白名单策略进程

        新增进程白名单策略进程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddAppWhitelistPolicyProcess
        :type request: :class:`huaweicloudsdkhss.v5.AddAppWhitelistPolicyProcessRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddAppWhitelistPolicyProcessResponse`
        """
        http_info = self._add_app_whitelist_policy_process_http_info(request)
        return self._call_api(**http_info)

    def add_app_whitelist_policy_process_async_invoker(self, request):
        http_info = self._add_app_whitelist_policy_process_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_app_whitelist_policy_process_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/app/{policy_id}/process",
            "request_type": request.__class__.__name__,
            "response_type": "AddAppWhitelistPolicyProcessResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))

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

    def change_app_whitelist_policy_async(self, request):
        r"""修改白名单策略

        修改白名单策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAppWhitelistPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ChangeAppWhitelistPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeAppWhitelistPolicyResponse`
        """
        http_info = self._change_app_whitelist_policy_http_info(request)
        return self._call_api(**http_info)

    def change_app_whitelist_policy_async_invoker(self, request):
        http_info = self._change_app_whitelist_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_app_whitelist_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/app/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAppWhitelistPolicyResponse"
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

    def change_app_whitelist_policy_process_status_async(self, request):
        r"""标记进程白名单策略识别进程

        标记进程白名单策略识别进程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAppWhitelistPolicyProcessStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangeAppWhitelistPolicyProcessStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeAppWhitelistPolicyProcessStatusResponse`
        """
        http_info = self._change_app_whitelist_policy_process_status_http_info(request)
        return self._call_api(**http_info)

    def change_app_whitelist_policy_process_status_async_invoker(self, request):
        http_info = self._change_app_whitelist_policy_process_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_app_whitelist_policy_process_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/app/{policy_id}/process",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAppWhitelistPolicyProcessStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def create_app_whitelist_policy_async(self, request):
        r"""创建白名单策略

        创建白名单策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppWhitelistPolicy
        :type request: :class:`huaweicloudsdkhss.v5.CreateAppWhitelistPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateAppWhitelistPolicyResponse`
        """
        http_info = self._create_app_whitelist_policy_http_info(request)
        return self._call_api(**http_info)

    def create_app_whitelist_policy_async_invoker(self, request):
        http_info = self._create_app_whitelist_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_whitelist_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/app/policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppWhitelistPolicyResponse"
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

    def delete_app_whitelist_policy_async(self, request):
        r"""删除白名单策略

        删除白名单策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppWhitelistPolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeleteAppWhitelistPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteAppWhitelistPolicyResponse`
        """
        http_info = self._delete_app_whitelist_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_app_whitelist_policy_async_invoker(self, request):
        http_info = self._delete_app_whitelist_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_whitelist_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/app/policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppWhitelistPolicyResponse"
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

    def delete_app_whitelist_policy_host_async(self, request):
        r"""白名单策略删除主机

        白名单策略删除主机
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppWhitelistPolicyHost
        :type request: :class:`huaweicloudsdkhss.v5.DeleteAppWhitelistPolicyHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteAppWhitelistPolicyHostResponse`
        """
        http_info = self._delete_app_whitelist_policy_host_http_info(request)
        return self._call_api(**http_info)

    def delete_app_whitelist_policy_host_async_invoker(self, request):
        http_info = self._delete_app_whitelist_policy_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_whitelist_policy_host_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/app/{policy_id}/host",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppWhitelistPolicyHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def list_app_whitelist_event_async(self, request):
        r"""查询进程白名单可疑进程

        查询进程白名单可疑进程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppWhitelistEvent
        :type request: :class:`huaweicloudsdkhss.v5.ListAppWhitelistEventRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppWhitelistEventResponse`
        """
        http_info = self._list_app_whitelist_event_http_info(request)
        return self._call_api(**http_info)

    def list_app_whitelist_event_async_invoker(self, request):
        http_info = self._list_app_whitelist_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_whitelist_event_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/app/event",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppWhitelistEventResponse"
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
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_app_whitelist_host_status_async(self, request):
        r"""查询进程白名单可选服务器列表

        查询进程白名单可选服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppWhitelistHostStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListAppWhitelistHostStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppWhitelistHostStatusResponse`
        """
        http_info = self._list_app_whitelist_host_status_http_info(request)
        return self._call_api(**http_info)

    def list_app_whitelist_host_status_async_invoker(self, request):
        http_info = self._list_app_whitelist_host_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_whitelist_host_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/app/host-management/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppWhitelistHostStatusResponse"
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
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def list_app_whitelist_policy_async(self, request):
        r"""查询进程白名单策略列表

        查询进程白名单策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppWhitelistPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ListAppWhitelistPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppWhitelistPolicyResponse`
        """
        http_info = self._list_app_whitelist_policy_http_info(request)
        return self._call_api(**http_info)

    def list_app_whitelist_policy_async_invoker(self, request):
        http_info = self._list_app_whitelist_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_whitelist_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/app/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppWhitelistPolicyResponse"
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
        if 'policy_type' in local_var_params:
            query_params.append(('policy_type', local_var_params['policy_type']))
        if 'learning_status' in local_var_params:
            query_params.append(('learning_status', local_var_params['learning_status']))
        if 'intercept' in local_var_params:
            query_params.append(('intercept', local_var_params['intercept']))

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

    def list_app_whitelist_policy_host_async(self, request):
        r"""查询进程白名单策略关联主机列表

        查询进程白名单策略关联主机列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppWhitelistPolicyHost
        :type request: :class:`huaweicloudsdkhss.v5.ListAppWhitelistPolicyHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppWhitelistPolicyHostResponse`
        """
        http_info = self._list_app_whitelist_policy_host_http_info(request)
        return self._call_api(**http_info)

    def list_app_whitelist_policy_host_async_invoker(self, request):
        http_info = self._list_app_whitelist_policy_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_whitelist_policy_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/app/host",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppWhitelistPolicyHostResponse"
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
        if 'learning_status' in local_var_params:
            query_params.append(('learning_status', local_var_params['learning_status']))
        if 'apply_status' in local_var_params:
            query_params.append(('apply_status', local_var_params['apply_status']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))

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

    def list_app_whitelist_policy_process_async(self, request):
        r"""查询进程白名单策略识别进程

        查询进程白名单策略识别进程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppWhitelistPolicyProcess
        :type request: :class:`huaweicloudsdkhss.v5.ListAppWhitelistPolicyProcessRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppWhitelistPolicyProcessResponse`
        """
        http_info = self._list_app_whitelist_policy_process_http_info(request)
        return self._call_api(**http_info)

    def list_app_whitelist_policy_process_async_invoker(self, request):
        http_info = self._list_app_whitelist_policy_process_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_whitelist_policy_process_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/app/{policy_id}/process",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppWhitelistPolicyProcessResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'process_status' in local_var_params:
            query_params.append(('process_status', local_var_params['process_status']))
        if 'process_type' in local_var_params:
            query_params.append(('process_type', local_var_params['process_type']))
        if 'process_name' in local_var_params:
            query_params.append(('process_name', local_var_params['process_name']))
        if 'process_hash' in local_var_params:
            query_params.append(('process_hash', local_var_params['process_hash']))
        if 'process_path' in local_var_params:
            query_params.append(('process_path', local_var_params['process_path']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'file_signer' in local_var_params:
            query_params.append(('file_signer', local_var_params['file_signer']))

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

    def list_app_whitelist_policy_process_extend_async(self, request):
        r"""查询进程白名单策略进程扩展列表

        查询进程白名单策略进程扩展列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppWhitelistPolicyProcessExtend
        :type request: :class:`huaweicloudsdkhss.v5.ListAppWhitelistPolicyProcessExtendRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppWhitelistPolicyProcessExtendResponse`
        """
        http_info = self._list_app_whitelist_policy_process_extend_http_info(request)
        return self._call_api(**http_info)

    def list_app_whitelist_policy_process_extend_async_invoker(self, request):
        http_info = self._list_app_whitelist_policy_process_extend_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_whitelist_policy_process_extend_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/app/{policy_id}/process-extend",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppWhitelistPolicyProcessExtendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def show_app_whitelist_agent_statics_async(self, request):
        r"""统计agent版本不匹配主机数量

        统计agent版本不匹配主机数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppWhitelistAgentStatics
        :type request: :class:`huaweicloudsdkhss.v5.ShowAppWhitelistAgentStaticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAppWhitelistAgentStaticsResponse`
        """
        http_info = self._show_app_whitelist_agent_statics_http_info(request)
        return self._call_api(**http_info)

    def show_app_whitelist_agent_statics_async_invoker(self, request):
        http_info = self._show_app_whitelist_agent_statics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_whitelist_agent_statics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/app/agent/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppWhitelistAgentStaticsResponse"
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

    def show_app_whitelist_policy_async(self, request):
        r"""查询进程白名单策略详情

        查询进程白名单策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppWhitelistPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ShowAppWhitelistPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAppWhitelistPolicyResponse`
        """
        http_info = self._show_app_whitelist_policy_http_info(request)
        return self._call_api(**http_info)

    def show_app_whitelist_policy_async_invoker(self, request):
        http_info = self._show_app_whitelist_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_whitelist_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/app/{policy_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppWhitelistPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def switch_app_whitelist_policy_host_async(self, request):
        r"""应用白名单策略

        应用白名单策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchAppWhitelistPolicyHost
        :type request: :class:`huaweicloudsdkhss.v5.SwitchAppWhitelistPolicyHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchAppWhitelistPolicyHostResponse`
        """
        http_info = self._switch_app_whitelist_policy_host_http_info(request)
        return self._call_api(**http_info)

    def switch_app_whitelist_policy_host_async_invoker(self, request):
        http_info = self._switch_app_whitelist_policy_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_app_whitelist_policy_host_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/app/host",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAppWhitelistPolicyHostResponse"
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

    def switch_app_whitelist_policy_learn_status_async(self, request):
        r"""操作白名单策略学习状态

        操作白名单策略学习状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchAppWhitelistPolicyLearnStatus
        :type request: :class:`huaweicloudsdkhss.v5.SwitchAppWhitelistPolicyLearnStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchAppWhitelistPolicyLearnStatusResponse`
        """
        http_info = self._switch_app_whitelist_policy_learn_status_http_info(request)
        return self._call_api(**http_info)

    def switch_app_whitelist_policy_learn_status_async_invoker(self, request):
        http_info = self._switch_app_whitelist_policy_learn_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_app_whitelist_policy_learn_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/app/{policy_id}/learn",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAppWhitelistPolicyLearnStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def list_handle_affect_baseline_async(self, request):
        r"""查询基线检查执行操作时影响的范围

        查询基线检查执行操作时影响的范围
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHandleAffectBaseline
        :type request: :class:`huaweicloudsdkhss.v5.ListHandleAffectBaselineRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHandleAffectBaselineResponse`
        """
        http_info = self._list_handle_affect_baseline_http_info(request)
        return self._call_api(**http_info)

    def list_handle_affect_baseline_async_invoker(self, request):
        http_info = self._list_handle_affect_baseline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_handle_affect_baseline_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/baseline/check-rule/handle-affect-baseline",
            "request_type": request.__class__.__name__,
            "response_type": "ListHandleAffectBaselineResponse"
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

    def copy_baseline_policy_group_async(self, request):
        r"""复制配置检测策略信息

        复制配置检测策略信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyBaselinePolicyGroup
        :type request: :class:`huaweicloudsdkhss.v5.CopyBaselinePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CopyBaselinePolicyGroupResponse`
        """
        http_info = self._copy_baseline_policy_group_http_info(request)
        return self._call_api(**http_info)

    def copy_baseline_policy_group_async_invoker(self, request):
        http_info = self._copy_baseline_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_baseline_policy_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/baseline/security-checks/policy-group",
            "request_type": request.__class__.__name__,
            "response_type": "CopyBaselinePolicyGroupResponse"
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

    def show_baseline_directory_async(self, request):
        r"""查询基线检测策略的基线目录信息

        查询基线检测策略的基线目录信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBaselineDirectory
        :type request: :class:`huaweicloudsdkhss.v5.ShowBaselineDirectoryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowBaselineDirectoryResponse`
        """
        http_info = self._show_baseline_directory_http_info(request)
        return self._call_api(**http_info)

    def show_baseline_directory_async_invoker(self, request):
        http_info = self._show_baseline_directory_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_baseline_directory_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/baseline/security-checks/directory",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBaselineDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'support_os' in local_var_params:
            query_params.append(('support_os', local_var_params['support_os']))
        if 'select_type' in local_var_params:
            query_params.append(('select_type', local_var_params['select_type']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def change_antivirus_pay_per_scan_status_async(self, request):
        r"""修改“病毒查杀按次计费”开关状态

        修改“病毒查杀按次计费”开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAntivirusPayPerScanStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangeAntivirusPayPerScanStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeAntivirusPayPerScanStatusResponse`
        """
        http_info = self._change_antivirus_pay_per_scan_status_http_info(request)
        return self._call_api(**http_info)

    def change_antivirus_pay_per_scan_status_async_invoker(self, request):
        http_info = self._change_antivirus_pay_per_scan_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_antivirus_pay_per_scan_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/antivirus/pay-per-scan",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAntivirusPayPerScanStatusResponse"
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

    def change_antivirus_policy_async(self, request):
        r"""编辑自定义查杀策略

        编辑自定义查杀策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAntivirusPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ChangeAntivirusPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeAntivirusPolicyResponse`
        """
        http_info = self._change_antivirus_policy_http_info(request)
        return self._call_api(**http_info)

    def change_antivirus_policy_async_invoker(self, request):
        http_info = self._change_antivirus_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_antivirus_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/antivirus/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAntivirusPolicyResponse"
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

    def create_anti_virus_paid_task_async(self, request):
        r"""创建付费病毒扫描任务

        创建付费病毒扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAntiVirusPaidTask
        :type request: :class:`huaweicloudsdkhss.v5.CreateAntiVirusPaidTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateAntiVirusPaidTaskResponse`
        """
        http_info = self._create_anti_virus_paid_task_http_info(request)
        return self._call_api(**http_info)

    def create_anti_virus_paid_task_async_invoker(self, request):
        http_info = self._create_anti_virus_paid_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_anti_virus_paid_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/antivirus/pay-per-scan/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAntiVirusPaidTaskResponse"
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

    def create_anti_virus_policy_async(self, request):
        r"""创建自定义查杀策略

        创建自定义查杀策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAntiVirusPolicy
        :type request: :class:`huaweicloudsdkhss.v5.CreateAntiVirusPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateAntiVirusPolicyResponse`
        """
        http_info = self._create_anti_virus_policy_http_info(request)
        return self._call_api(**http_info)

    def create_anti_virus_policy_async_invoker(self, request):
        http_info = self._create_anti_virus_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_anti_virus_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/antivirus/policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAntiVirusPolicyResponse"
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

    def create_anti_virus_task_async(self, request):
        r"""创建病毒扫描任务

        创建病毒扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAntiVirusTask
        :type request: :class:`huaweicloudsdkhss.v5.CreateAntiVirusTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateAntiVirusTaskResponse`
        """
        http_info = self._create_anti_virus_task_http_info(request)
        return self._call_api(**http_info)

    def create_anti_virus_task_async_invoker(self, request):
        http_info = self._create_anti_virus_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_anti_virus_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/antivirus/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAntiVirusTaskResponse"
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

    def delete_antivirus_policy_async(self, request):
        r"""删除自定义查杀策略

        删除自定义查杀策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAntivirusPolicy
        :type request: :class:`huaweicloudsdkhss.v5.DeleteAntivirusPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteAntivirusPolicyResponse`
        """
        http_info = self._delete_antivirus_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_antivirus_policy_async_invoker(self, request):
        http_info = self._delete_antivirus_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_antivirus_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/antivirus/policy/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAntivirusPolicyResponse"
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

    def export_anti_virus_result_async(self, request):
        r"""导出病毒扫描结果列表

        导出病毒扫描结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportAntiVirusResult
        :type request: :class:`huaweicloudsdkhss.v5.ExportAntiVirusResultRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ExportAntiVirusResultResponse`
        """
        http_info = self._export_anti_virus_result_http_info(request)
        return self._call_api(**http_info)

    def export_anti_virus_result_async_invoker(self, request):
        http_info = self._export_anti_virus_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_anti_virus_result_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/antivirus/result/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportAntiVirusResultResponse"
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
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity_list' in local_var_params:
            query_params.append(('severity_list', local_var_params['severity_list']))
            collection_formats['severity_list'] = 'csv'
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'malware_name' in local_var_params:
            query_params.append(('malware_name', local_var_params['malware_name']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'export_size' in local_var_params:
            query_params.append(('export_size', local_var_params['export_size']))
        if 'file_hash' in local_var_params:
            query_params.append(('file_hash', local_var_params['file_hash']))
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'manual_isolate' in local_var_params:
            query_params.append(('manual_isolate', local_var_params['manual_isolate']))

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

    def handle_anti_virus_result_async(self, request):
        r"""处置病毒扫描结果

        处置病毒扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for HandleAntiVirusResult
        :type request: :class:`huaweicloudsdkhss.v5.HandleAntiVirusResultRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.HandleAntiVirusResultResponse`
        """
        http_info = self._handle_anti_virus_result_http_info(request)
        return self._call_api(**http_info)

    def handle_anti_virus_result_async_invoker(self, request):
        http_info = self._handle_anti_virus_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _handle_anti_virus_result_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/antivirus/result/operate",
            "request_type": request.__class__.__name__,
            "response_type": "HandleAntiVirusResultResponse"
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

    def list_anti_virus_host_async(self, request):
        r"""查询病毒查杀可选服务器列表

        查询病毒查杀可选服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAntiVirusHost
        :type request: :class:`huaweicloudsdkhss.v5.ListAntiVirusHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAntiVirusHostResponse`
        """
        http_info = self._list_anti_virus_host_http_info(request)
        return self._call_api(**http_info)

    def list_anti_virus_host_async_invoker(self, request):
        http_info = self._list_anti_virus_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_anti_virus_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/host-management/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAntiVirusHostResponse"
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
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'scan_type' in local_var_params:
            query_params.append(('scan_type', local_var_params['scan_type']))
        if 'start_type' in local_var_params:
            query_params.append(('start_type', local_var_params['start_type']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'next_start_time' in local_var_params:
            query_params.append(('next_start_time', local_var_params['next_start_time']))

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

    def list_anti_virus_paid_hosts_async(self, request):
        r"""查询付费病毒查杀服务器列表

        查询付费病毒查杀服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAntiVirusPaidHosts
        :type request: :class:`huaweicloudsdkhss.v5.ListAntiVirusPaidHostsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAntiVirusPaidHostsResponse`
        """
        http_info = self._list_anti_virus_paid_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_anti_virus_paid_hosts_async_invoker(self, request):
        http_info = self._list_anti_virus_paid_hosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_anti_virus_paid_hosts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/pay-per-scan/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAntiVirusPaidHostsResponse"
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
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'scan_type' in local_var_params:
            query_params.append(('scan_type', local_var_params['scan_type']))
        if 'start_type' in local_var_params:
            query_params.append(('start_type', local_var_params['start_type']))

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

    def list_anti_virus_policy_async(self, request):
        r"""查询自定义查杀策略列表

        查询自定义查杀策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAntiVirusPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ListAntiVirusPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAntiVirusPolicyResponse`
        """
        http_info = self._list_anti_virus_policy_http_info(request)
        return self._call_api(**http_info)

    def list_anti_virus_policy_async_invoker(self, request):
        http_info = self._list_anti_virus_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_anti_virus_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListAntiVirusPolicyResponse"
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

    def list_anti_virus_result_async(self, request):
        r"""查询病毒扫描结果列表

        查询病毒扫描结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAntiVirusResult
        :type request: :class:`huaweicloudsdkhss.v5.ListAntiVirusResultRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAntiVirusResultResponse`
        """
        http_info = self._list_anti_virus_result_http_info(request)
        return self._call_api(**http_info)

    def list_anti_virus_result_async_invoker(self, request):
        http_info = self._list_anti_virus_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_anti_virus_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/result",
            "request_type": request.__class__.__name__,
            "response_type": "ListAntiVirusResultResponse"
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
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity_list' in local_var_params:
            query_params.append(('severity_list', local_var_params['severity_list']))
            collection_formats['severity_list'] = 'csv'
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'malware_name' in local_var_params:
            query_params.append(('malware_name', local_var_params['malware_name']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'file_hash' in local_var_params:
            query_params.append(('file_hash', local_var_params['file_hash']))
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'manual_isolate' in local_var_params:
            query_params.append(('manual_isolate', local_var_params['manual_isolate']))

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

    def list_anti_virus_task_async(self, request):
        r"""查看病毒扫描任务列表

        查看病毒扫描任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAntiVirusTask
        :type request: :class:`huaweicloudsdkhss.v5.ListAntiVirusTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAntiVirusTaskResponse`
        """
        http_info = self._list_anti_virus_task_http_info(request)
        return self._call_api(**http_info)

    def list_anti_virus_task_async_invoker(self, request):
        http_info = self._list_anti_virus_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_anti_virus_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/task",
            "request_type": request.__class__.__name__,
            "response_type": "ListAntiVirusTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'task_status' in local_var_params:
            query_params.append(('task_status', local_var_params['task_status']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'whether_paid_task' in local_var_params:
            query_params.append(('whether_paid_task', local_var_params['whether_paid_task']))
        if 'host_task_status' in local_var_params:
            query_params.append(('host_task_status', local_var_params['host_task_status']))
            collection_formats['host_task_status'] = 'csv'

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

    def show_antivirus_free_quota_async(self, request):
        r"""查询病毒查杀免费扫描次数

        查询病毒查杀免费扫描次数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAntivirusFreeQuota
        :type request: :class:`huaweicloudsdkhss.v5.ShowAntivirusFreeQuotaRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAntivirusFreeQuotaResponse`
        """
        http_info = self._show_antivirus_free_quota_http_info(request)
        return self._call_api(**http_info)

    def show_antivirus_free_quota_async_invoker(self, request):
        http_info = self._show_antivirus_free_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_antivirus_free_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/pay-per-scan/free-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAntivirusFreeQuotaResponse"
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

    def show_antivirus_pay_per_scan_status_async(self, request):
        r"""查询“病毒查杀按次计费”开关状态

        查询“病毒查杀按次计费”开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAntivirusPayPerScanStatus
        :type request: :class:`huaweicloudsdkhss.v5.ShowAntivirusPayPerScanStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAntivirusPayPerScanStatusResponse`
        """
        http_info = self._show_antivirus_pay_per_scan_status_http_info(request)
        return self._call_api(**http_info)

    def show_antivirus_pay_per_scan_status_async_invoker(self, request):
        http_info = self._show_antivirus_pay_per_scan_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_antivirus_pay_per_scan_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/pay-per-scan",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAntivirusPayPerScanStatusResponse"
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

    def show_antivirus_statistic_async(self, request):
        r"""查询病毒查杀统计信息

        查询病毒查杀统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAntivirusStatistic
        :type request: :class:`huaweicloudsdkhss.v5.ShowAntivirusStatisticRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAntivirusStatisticResponse`
        """
        http_info = self._show_antivirus_statistic_http_info(request)
        return self._call_api(**http_info)

    def show_antivirus_statistic_async_invoker(self, request):
        http_info = self._show_antivirus_statistic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_antivirus_statistic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/antivirus/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAntivirusStatisticResponse"
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

    def switch_antivirus_task_async(self, request):
        r"""取消扫描任务

        取消扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchAntivirusTask
        :type request: :class:`huaweicloudsdkhss.v5.SwitchAntivirusTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchAntivirusTaskResponse`
        """
        http_info = self._switch_antivirus_task_http_info(request)
        return self._call_api(**http_info)

    def switch_antivirus_task_async_invoker(self, request):
        http_info = self._switch_antivirus_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_antivirus_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/antivirus/task",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAntivirusTaskResponse"
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

    def export_risks_async(self, request):
        r"""导出集群环境安全相关信息

        导出集群环境安全相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportRisks
        :type request: :class:`huaweicloudsdkhss.v5.ExportRisksRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ExportRisksResponse`
        """
        http_info = self._export_risks_http_info(request)
        return self._call_api(**http_info)

    def export_risks_async_invoker(self, request):
        http_info = self._export_risks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_risks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/cluster/risk/export-task",
            "request_type": request.__class__.__name__,
            "response_type": "ExportRisksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'risk_type' in local_var_params:
            query_params.append(('risk_type', local_var_params['risk_type']))
        if 'export_size' in local_var_params:
            query_params.append(('export_size', local_var_params['export_size']))

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

    def list_cluster_risk_affect_resources_async(self, request):
        r"""查询集群风险影响的集群资源列表

        查询集群风险影响的集群资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterRiskAffectResources
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterRiskAffectResourcesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterRiskAffectResourcesResponse`
        """
        http_info = self._list_cluster_risk_affect_resources_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_risk_affect_resources_async_invoker(self, request):
        http_info = self._list_cluster_risk_affect_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_risk_affect_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/cluster/risk/{risk_id}/affected-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterRiskAffectResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'risk_id' in local_var_params:
            path_params['risk_id'] = local_var_params['risk_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

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

    def list_cluster_risks_async(self, request):
        r"""查询集群风险列表

        查询集群风险列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterRisks
        :type request: :class:`huaweicloudsdkhss.v5.ListClusterRisksRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListClusterRisksResponse`
        """
        http_info = self._list_cluster_risks_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_risks_async_invoker(self, request):
        http_info = self._list_cluster_risks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_risks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/cluster/risks",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterRisksResponse"
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
        if 'risk_type' in local_var_params:
            query_params.append(('risk_type', local_var_params['risk_type']))
        if 'risk_status' in local_var_params:
            query_params.append(('risk_status', local_var_params['risk_status']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'risk_name' in local_var_params:
            query_params.append(('risk_name', local_var_params['risk_name']))
        if 'risk_level' in local_var_params:
            query_params.append(('risk_level', local_var_params['risk_level']))
        if 'risk_category' in local_var_params:
            query_params.append(('risk_category', local_var_params['risk_category']))

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

    def show_cluster_scan_statistics_async(self, request):
        r"""查询集群扫描统计数据

        查询集群扫描统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterScanStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowClusterScanStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowClusterScanStatisticsResponse`
        """
        http_info = self._show_cluster_scan_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_scan_statistics_async_invoker(self, request):
        http_info = self._show_cluster_scan_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_scan_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/cluster/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterScanStatisticsResponse"
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

    def list_project_configs_async(self, request):
        r"""查询项目配置

        查询项目配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectConfigs
        :type request: :class:`huaweicloudsdkhss.v5.ListProjectConfigsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProjectConfigsResponse`
        """
        http_info = self._list_project_configs_http_info(request)
        return self._call_api(**http_info)

    def list_project_configs_async_invoker(self, request):
        http_info = self._list_project_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_configs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/config",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectConfigsResponse"
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

    def modify_project_configs_async(self, request):
        r"""修改项目配置

        修改项目配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyProjectConfigs
        :type request: :class:`huaweicloudsdkhss.v5.ModifyProjectConfigsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ModifyProjectConfigsResponse`
        """
        http_info = self._modify_project_configs_http_info(request)
        return self._call_api(**http_info)

    def modify_project_configs_async_invoker(self, request):
        http_info = self._modify_project_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_project_configs_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/config",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyProjectConfigsResponse"
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

    def save_browsing_history_async(self, request):
        r"""保存用户访问记录

        保存用户访问记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SaveBrowsingHistory
        :type request: :class:`huaweicloudsdkhss.v5.SaveBrowsingHistoryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SaveBrowsingHistoryResponse`
        """
        http_info = self._save_browsing_history_http_info(request)
        return self._call_api(**http_info)

    def save_browsing_history_async_invoker(self, request):
        http_info = self._save_browsing_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _save_browsing_history_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/browsing-history",
            "request_type": request.__class__.__name__,
            "response_type": "SaveBrowsingHistoryResponse"
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

    def add_registry_async(self, request):
        r"""新增镜像仓库

        新增镜像仓库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddRegistry
        :type request: :class:`huaweicloudsdkhss.v5.AddRegistryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddRegistryResponse`
        """
        http_info = self._add_registry_http_info(request)
        return self._call_api(**http_info)

    def add_registry_async_invoker(self, request):
        http_info = self._add_registry_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_registry_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/image/registries",
            "request_type": request.__class__.__name__,
            "response_type": "AddRegistryResponse"
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

    def batch_delete_agent_daemonset_async(self, request):
        r"""批量卸载集群daemonset

        批量卸载集群daemonset
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAgentDaemonset
        :type request: :class:`huaweicloudsdkhss.v5.BatchDeleteAgentDaemonsetRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchDeleteAgentDaemonsetResponse`
        """
        http_info = self._batch_delete_agent_daemonset_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_agent_daemonset_async_invoker(self, request):
        http_info = self._batch_delete_agent_daemonset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_agent_daemonset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/daemonsets/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAgentDaemonsetResponse"
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

    def batch_delete_registry_async(self, request):
        r"""批量删除镜像仓接入信息

        批量删除镜像仓接入信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteRegistry
        :type request: :class:`huaweicloudsdkhss.v5.BatchDeleteRegistryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchDeleteRegistryResponse`
        """
        http_info = self._batch_delete_registry_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_registry_async_invoker(self, request):
        http_info = self._batch_delete_registry_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_registry_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/image/registries/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteRegistryResponse"
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

    def batch_upgrade_agent_daemonset_async(self, request):
        r"""批量升级集群daemonset

        批量升级集群daemonset
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpgradeAgentDaemonset
        :type request: :class:`huaweicloudsdkhss.v5.BatchUpgradeAgentDaemonsetRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchUpgradeAgentDaemonsetResponse`
        """
        http_info = self._batch_upgrade_agent_daemonset_http_info(request)
        return self._call_api(**http_info)

    def batch_upgrade_agent_daemonset_async_invoker(self, request):
        http_info = self._batch_upgrade_agent_daemonset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_upgrade_agent_daemonset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/daemonsets/batch-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpgradeAgentDaemonsetResponse"
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

    def create_agent_daemonset_async(self, request):
        r"""创建集群daemonset

        创建集群daemonset
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgentDaemonset
        :type request: :class:`huaweicloudsdkhss.v5.CreateAgentDaemonsetRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateAgentDaemonsetResponse`
        """
        http_info = self._create_agent_daemonset_http_info(request)
        return self._call_api(**http_info)

    def create_agent_daemonset_async_invoker(self, request):
        http_info = self._create_agent_daemonset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agent_daemonset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/{cluster_id}/daemonsets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgentDaemonsetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def create_multi_cloud_clusters_async(self, request):
        r"""创建多云集群

        创建多云集群
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMultiCloudClusters
        :type request: :class:`huaweicloudsdkhss.v5.CreateMultiCloudClustersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateMultiCloudClustersResponse`
        """
        http_info = self._create_multi_cloud_clusters_http_info(request)
        return self._call_api(**http_info)

    def create_multi_cloud_clusters_async_invoker(self, request):
        http_info = self._create_multi_cloud_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_multi_cloud_clusters_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMultiCloudClustersResponse"
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

    def delete_agent_daemonset_async(self, request):
        r"""删除集群daemonset

        删除集群daemonset
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAgentDaemonset
        :type request: :class:`huaweicloudsdkhss.v5.DeleteAgentDaemonsetRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteAgentDaemonsetResponse`
        """
        http_info = self._delete_agent_daemonset_http_info(request)
        return self._call_api(**http_info)

    def delete_agent_daemonset_async_invoker(self, request):
        http_info = self._delete_agent_daemonset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_agent_daemonset_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/{cluster_id}/daemonsets",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgentDaemonsetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'invoked_service' in local_var_params:
            query_params.append(('invoked_service', local_var_params['invoked_service']))

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

    def delete_cicd_configurations_async(self, request):
        r"""删除CI/CD配置

        删除CI/CD配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCicdConfigurations
        :type request: :class:`huaweicloudsdkhss.v5.DeleteCicdConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteCicdConfigurationsResponse`
        """
        http_info = self._delete_cicd_configurations_http_info(request)
        return self._call_api(**http_info)

    def delete_cicd_configurations_async_invoker(self, request):
        http_info = self._delete_cicd_configurations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cicd_configurations_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/image/cicd/configurations/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCicdConfigurationsResponse"
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

    def delete_registry_async(self, request):
        r"""删除镜像仓接入信息

        删除镜像仓接入信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRegistry
        :type request: :class:`huaweicloudsdkhss.v5.DeleteRegistryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteRegistryResponse`
        """
        http_info = self._delete_registry_http_info(request)
        return self._call_api(**http_info)

    def delete_registry_async_invoker(self, request):
        http_info = self._delete_registry_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_registry_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/image/registries/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRegistryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def export_image_security_report_task_async(self, request):
        r"""创建镜像安全报告信息导出任务（支持全量/批量导出）

        创建镜像安全报告信息导出任务（支持全量/批量导出）,支持导出恶意文件、软件信息、文件信息、敏感信息、软件合规、镜像构建指令风险。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportImageSecurityReportTask
        :type request: :class:`huaweicloudsdkhss.v5.ExportImageSecurityReportTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ExportImageSecurityReportTaskResponse`
        """
        http_info = self._export_image_security_report_task_http_info(request)
        return self._call_api(**http_info)

    def export_image_security_report_task_async_invoker(self, request):
        http_info = self._export_image_security_report_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_image_security_report_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/image/security-report/export-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ExportImageSecurityReportTaskResponse"
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

    def list_associate_registries_async(self, request):
        r"""获取镜像同步任务关联的镜像仓的信息

        获取镜像同步任务关联的镜像仓的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAssociateRegistries
        :type request: :class:`huaweicloudsdkhss.v5.ListAssociateRegistriesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAssociateRegistriesResponse`
        """
        http_info = self._list_associate_registries_http_info(request)
        return self._call_api(**http_info)

    def list_associate_registries_async_invoker(self, request):
        http_info = self._list_associate_registries_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_associate_registries_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/image-sync/tasks/{task_id}/registries",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssociateRegistriesResponse"
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
        if 'registry_name' in local_var_params:
            query_params.append(('registry_name', local_var_params['registry_name']))
        if 'registry_type' in local_var_params:
            query_params.append(('registry_type', local_var_params['registry_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))

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

    def list_cicd_configurations_async(self, request):
        r"""查询cicd配置列表

        查询cicd配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCicdConfigurations
        :type request: :class:`huaweicloudsdkhss.v5.ListCicdConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListCicdConfigurationsResponse`
        """
        http_info = self._list_cicd_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_cicd_configurations_async_invoker(self, request):
        http_info = self._list_cicd_configurations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cicd_configurations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/cicd/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListCicdConfigurationsResponse"
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
        if 'cicd_name' in local_var_params:
            query_params.append(('cicd_name', local_var_params['cicd_name']))
        if 'cicd_id' in local_var_params:
            query_params.append(('cicd_id', local_var_params['cicd_id']))

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

    def list_multi_cloud_clusters_async(self, request):
        r"""查询多云集群

        查询多云集群
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMultiCloudClusters
        :type request: :class:`huaweicloudsdkhss.v5.ListMultiCloudClustersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListMultiCloudClustersResponse`
        """
        http_info = self._list_multi_cloud_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_multi_cloud_clusters_async_invoker(self, request):
        http_info = self._list_multi_cloud_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_multi_cloud_clusters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListMultiCloudClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_registry_async(self, request):
        r"""获取镜像仓列表

        获取镜像仓列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRegistry
        :type request: :class:`huaweicloudsdkhss.v5.ListRegistryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRegistryResponse`
        """
        http_info = self._list_registry_http_info(request)
        return self._call_api(**http_info)

    def list_registry_async_invoker(self, request):
        http_info = self._list_registry_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_registry_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/registries",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegistryResponse"
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
        if 'registry_name' in local_var_params:
            query_params.append(('registry_name', local_var_params['registry_name']))
        if 'registry_id' in local_var_params:
            query_params.append(('registry_id', local_var_params['registry_id']))
        if 'registry_type' in local_var_params:
            query_params.append(('registry_type', local_var_params['registry_type']))
        if 'registry_addr' in local_var_params:
            query_params.append(('registry_addr', local_var_params['registry_addr']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_registry_statistics_async(self, request):
        r"""查询镜像仓统计数据

        查询镜像仓统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRegistryStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListRegistryStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRegistryStatisticsResponse`
        """
        http_info = self._list_registry_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_registry_statistics_async_invoker(self, request):
        http_info = self._list_registry_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_registry_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/registries/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegistryStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'registry_type' in local_var_params:
            query_params.append(('registry_type', local_var_params['registry_type']))

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

    def modify_cicd_configuration_async(self, request):
        r"""修改CI/CD配置

        修改CI/CD配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyCicdConfiguration
        :type request: :class:`huaweicloudsdkhss.v5.ModifyCicdConfigurationRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ModifyCicdConfigurationResponse`
        """
        http_info = self._modify_cicd_configuration_http_info(request)
        return self._call_api(**http_info)

    def modify_cicd_configuration_async_invoker(self, request):
        http_info = self._modify_cicd_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_cicd_configuration_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/image/cicd/configurations/{cicd_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyCicdConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cicd_id' in local_var_params:
            path_params['cicd_id'] = local_var_params['cicd_id']

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

    def parse_multi_cloud_cluster_config_async(self, request):
        r"""解析多云集群的配置文件

        解析多云集群的配置文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ParseMultiCloudClusterConfig
        :type request: :class:`huaweicloudsdkhss.v5.ParseMultiCloudClusterConfigRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ParseMultiCloudClusterConfigResponse`
        """
        http_info = self._parse_multi_cloud_cluster_config_http_info(request)
        return self._call_api(**http_info)

    def parse_multi_cloud_cluster_config_async_invoker(self, request):
        http_info = self._parse_multi_cloud_cluster_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _parse_multi_cloud_cluster_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/config-analyze",
            "request_type": request.__class__.__name__,
            "response_type": "ParseMultiCloudClusterConfigResponse"
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

    def remove_multi_cloud_clusters_async(self, request):
        r"""删除多云集群

        删除多云集群
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveMultiCloudClusters
        :type request: :class:`huaweicloudsdkhss.v5.RemoveMultiCloudClustersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.RemoveMultiCloudClustersResponse`
        """
        http_info = self._remove_multi_cloud_clusters_http_info(request)
        return self._call_api(**http_info)

    def remove_multi_cloud_clusters_async_invoker(self, request):
        http_info = self._remove_multi_cloud_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_multi_cloud_clusters_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveMultiCloudClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def show_agent_daemonset_deploy_template_async(self, request):
        r"""获取部署模板

        获取部署模板，在安装Daemonset的时候提供选择
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgentDaemonsetDeployTemplate
        :type request: :class:`huaweicloudsdkhss.v5.ShowAgentDaemonsetDeployTemplateRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAgentDaemonsetDeployTemplateResponse`
        """
        http_info = self._show_agent_daemonset_deploy_template_http_info(request)
        return self._call_api(**http_info)

    def show_agent_daemonset_deploy_template_async_invoker(self, request):
        http_info = self._show_agent_daemonset_deploy_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agent_daemonset_deploy_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes/template",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgentDaemonsetDeployTemplateResponse"
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

    def show_agent_daemonset_detail_info_async(self, request):
        r"""获取集群daemonset信息

        获取集群daemonset信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgentDaemonsetDetailInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowAgentDaemonsetDetailInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAgentDaemonsetDetailInfoResponse`
        """
        http_info = self._show_agent_daemonset_detail_info_http_info(request)
        return self._call_api(**http_info)

    def show_agent_daemonset_detail_info_async_invoker(self, request):
        http_info = self._show_agent_daemonset_detail_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agent_daemonset_detail_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/{cluster_id}/daemonsets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgentDaemonsetDetailInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def show_cicd_configuration_async(self, request):
        r"""查询CI/CD配置信息

        查询CI/CD配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCicdConfiguration
        :type request: :class:`huaweicloudsdkhss.v5.ShowCicdConfigurationRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowCicdConfigurationResponse`
        """
        http_info = self._show_cicd_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_cicd_configuration_async_invoker(self, request):
        http_info = self._show_cicd_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cicd_configuration_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/cicd/configurations/{cicd_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCicdConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cicd_id' in local_var_params:
            path_params['cicd_id'] = local_var_params['cicd_id']

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

    def show_image_upload_command_async(self, request):
        r"""获取扫描组件镜像上传指令

        获取镜像上传指令，上传的镜像是“镜像仓接入功能”和“镜像仓扫描功能”需要的组件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageUploadCommand
        :type request: :class:`huaweicloudsdkhss.v5.ShowImageUploadCommandRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowImageUploadCommandResponse`
        """
        http_info = self._show_image_upload_command_http_info(request)
        return self._call_api(**http_info)

    def show_image_upload_command_async_invoker(self, request):
        http_info = self._show_image_upload_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_upload_command_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/registries/image-upload-command",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageUploadCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'registry_addr' in local_var_params:
            query_params.append(('registry_addr', local_var_params['registry_addr']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))
        if 'password' in local_var_params:
            query_params.append(('password', local_var_params['password']))

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

    def show_multi_cloud_cluster_auth_async(self, request):
        r"""获取多云集群的账号权限

        获取多云集群的账号权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMultiCloudClusterAuth
        :type request: :class:`huaweicloudsdkhss.v5.ShowMultiCloudClusterAuthRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowMultiCloudClusterAuthResponse`
        """
        http_info = self._show_multi_cloud_cluster_auth_http_info(request)
        return self._call_api(**http_info)

    def show_multi_cloud_cluster_auth_async_invoker(self, request):
        http_info = self._show_multi_cloud_cluster_auth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_multi_cloud_cluster_auth_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/clusters/{cluster_id}/permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMultiCloudClusterAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def show_multi_cloud_cluster_image_command_async(self, request):
        r"""获取多云集群的上传镜像指令

        获取多云集群的上传镜像指令
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMultiCloudClusterImageCommand
        :type request: :class:`huaweicloudsdkhss.v5.ShowMultiCloudClusterImageCommandRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowMultiCloudClusterImageCommandResponse`
        """
        http_info = self._show_multi_cloud_cluster_image_command_http_info(request)
        return self._call_api(**http_info)

    def show_multi_cloud_cluster_image_command_async_invoker(self, request):
        http_info = self._show_multi_cloud_cluster_image_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_multi_cloud_cluster_image_command_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/image-upload-command",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMultiCloudClusterImageCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'image_repo' in local_var_params:
            query_params.append(('image_repo', local_var_params['image_repo']))
        if 'organization' in local_var_params:
            query_params.append(('organization', local_var_params['organization']))
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))
        if 'password' in local_var_params:
            query_params.append(('password', local_var_params['password']))
        if 'plug_type' in local_var_params:
            query_params.append(('plug_type', local_var_params['plug_type']))

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

    def show_multi_cloud_cluster_proxy_script_async(self, request):
        r"""获取多云集群的代理安装脚本

        获取多云集群的代理安装脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMultiCloudClusterProxyScript
        :type request: :class:`huaweicloudsdkhss.v5.ShowMultiCloudClusterProxyScriptRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowMultiCloudClusterProxyScriptResponse`
        """
        http_info = self._show_multi_cloud_cluster_proxy_script_http_info(request)
        return self._call_api(**http_info)

    def show_multi_cloud_cluster_proxy_script_async_invoker(self, request):
        http_info = self._show_multi_cloud_cluster_proxy_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_multi_cloud_cluster_proxy_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/clusters/{cluster_id}/agent/install-script",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMultiCloudClusterProxyScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def sync_multi_cloud_cluster_status_async(self, request):
        r"""同步多云集群的接入状态

        同步多云集群的接入状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncMultiCloudClusterStatus
        :type request: :class:`huaweicloudsdkhss.v5.SyncMultiCloudClusterStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SyncMultiCloudClusterStatusResponse`
        """
        http_info = self._sync_multi_cloud_cluster_status_http_info(request)
        return self._call_api(**http_info)

    def sync_multi_cloud_cluster_status_async_invoker(self, request):
        http_info = self._sync_multi_cloud_cluster_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_multi_cloud_cluster_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/clusters/status-synchronize",
            "request_type": request.__class__.__name__,
            "response_type": "SyncMultiCloudClusterStatusResponse"
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

    def update_agent_daemonset_async(self, request):
        r"""更新集群daemonset

        更新集群daemonset
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAgentDaemonset
        :type request: :class:`huaweicloudsdkhss.v5.UpdateAgentDaemonsetRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateAgentDaemonsetResponse`
        """
        http_info = self._update_agent_daemonset_http_info(request)
        return self._call_api(**http_info)

    def update_agent_daemonset_async_invoker(self, request):
        http_info = self._update_agent_daemonset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_agent_daemonset_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/container/kubernetes/clusters/{cluster_id}/daemonsets",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAgentDaemonsetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def update_multi_cloud_clusters_async(self, request):
        r"""更新多云集群

        更新多云集群
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMultiCloudClusters
        :type request: :class:`huaweicloudsdkhss.v5.UpdateMultiCloudClustersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateMultiCloudClustersResponse`
        """
        http_info = self._update_multi_cloud_clusters_http_info(request)
        return self._call_api(**http_info)

    def update_multi_cloud_clusters_async_invoker(self, request):
        http_info = self._update_multi_cloud_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_multi_cloud_clusters_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/container/kubernetes/multi-cloud/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMultiCloudClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def update_registry_async(self, request):
        r"""编辑镜像仓接入信息

        编辑镜像仓接入信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRegistry
        :type request: :class:`huaweicloudsdkhss.v5.UpdateRegistryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateRegistryResponse`
        """
        http_info = self._update_registry_http_info(request)
        return self._call_api(**http_info)

    def update_registry_async_invoker(self, request):
        http_info = self._update_registry_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_registry_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/image/registries/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRegistryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_file_events_async(self, request):
        r"""变更文件列表

        变更文件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFileEvents
        :type request: :class:`huaweicloudsdkhss.v5.ListFileEventsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListFileEventsResponse`
        """
        http_info = self._list_file_events_http_info(request)
        return self._call_api(**http_info)

    def list_file_events_async_invoker(self, request):
        http_info = self._list_file_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_file_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/files/change-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListFileEventsResponse"
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
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'change_type' in local_var_params:
            query_params.append(('change_type', local_var_params['change_type']))
        if 'change_category' in local_var_params:
            query_params.append(('change_category', local_var_params['change_category']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_file_host_event_details_async(self, request):
        r"""某个服务器变更文件信息

        某个服务器变更文件信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFileHostEventDetails
        :type request: :class:`huaweicloudsdkhss.v5.ListFileHostEventDetailsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListFileHostEventDetailsResponse`
        """
        http_info = self._list_file_host_event_details_http_info(request)
        return self._call_api(**http_info)

    def list_file_host_event_details_async_invoker(self, request):
        http_info = self._list_file_host_event_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_file_host_event_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/{host_id}/files/change-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListFileHostEventDetailsResponse"
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
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'change_type' in local_var_params:
            query_params.append(('change_type', local_var_params['change_type']))
        if 'change_category' in local_var_params:
            query_params.append(('change_category', local_var_params['change_category']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_file_hosts_async(self, request):
        r"""云服务器变更列表

        云服务器变更列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFileHosts
        :type request: :class:`huaweicloudsdkhss.v5.ListFileHostsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListFileHostsResponse`
        """
        http_info = self._list_file_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_file_hosts_async_invoker(self, request):
        http_info = self._list_file_hosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_file_hosts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/files/change-host",
            "request_type": request.__class__.__name__,
            "response_type": "ListFileHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def show_file_statistic_async(self, request):
        r"""获取服务器文件统计信息

        获取服务器文件统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFileStatistic
        :type request: :class:`huaweicloudsdkhss.v5.ShowFileStatisticRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowFileStatisticResponse`
        """
        http_info = self._show_file_statistic_http_info(request)
        return self._call_api(**http_info)

    def show_file_statistic_async_invoker(self, request):
        http_info = self._show_file_statistic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_file_statistic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/files/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFileStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
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

    def list_iac_file_risk_paths_async(self, request):
        r"""获取iac文件风险路径列表

        获取iac文件风险路径列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIacFileRiskPaths
        :type request: :class:`huaweicloudsdkhss.v5.ListIacFileRiskPathsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListIacFileRiskPathsResponse`
        """
        http_info = self._list_iac_file_risk_paths_http_info(request)
        return self._call_api(**http_info)

    def list_iac_file_risk_paths_async_invoker(self, request):
        http_info = self._list_iac_file_risk_paths_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_iac_file_risk_paths_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/iac/file/risk/paths",
            "request_type": request.__class__.__name__,
            "response_type": "ListIacFileRiskPathsResponse"
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
        if 'file_id' in local_var_params:
            query_params.append(('file_id', local_var_params['file_id']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

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

    def list_iac_file_risks_async(self, request):
        r"""获取iac文件风险列表

        获取iac文件风险列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIacFileRisks
        :type request: :class:`huaweicloudsdkhss.v5.ListIacFileRisksRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListIacFileRisksResponse`
        """
        http_info = self._list_iac_file_risks_http_info(request)
        return self._call_api(**http_info)

    def list_iac_file_risks_async_invoker(self, request):
        http_info = self._list_iac_file_risks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_iac_file_risks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/iac/file/risks",
            "request_type": request.__class__.__name__,
            "response_type": "ListIacFileRisksResponse"
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
        if 'file_id' in local_var_params:
            query_params.append(('file_id', local_var_params['file_id']))
        if 'risk_name' in local_var_params:
            query_params.append(('risk_name', local_var_params['risk_name']))
        if 'risk_level' in local_var_params:
            query_params.append(('risk_level', local_var_params['risk_level']))
        if 'risk_category' in local_var_params:
            query_params.append(('risk_category', local_var_params['risk_category']))

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

    def list_iac_files_async(self, request):
        r"""获取iac文件列表

        获取iac文件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIacFiles
        :type request: :class:`huaweicloudsdkhss.v5.ListIacFilesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListIacFilesResponse`
        """
        http_info = self._list_iac_files_http_info(request)
        return self._call_api(**http_info)

    def list_iac_files_async_invoker(self, request):
        http_info = self._list_iac_files_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_iac_files_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/container/iac/files",
            "request_type": request.__class__.__name__,
            "response_type": "ListIacFilesResponse"
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
        if 'scan_type' in local_var_params:
            query_params.append(('scan_type', local_var_params['scan_type']))
        if 'file_id' in local_var_params:
            query_params.append(('file_id', local_var_params['file_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'file_type' in local_var_params:
            query_params.append(('file_type', local_var_params['file_type']))
        if 'risky' in local_var_params:
            query_params.append(('risky', local_var_params['risky']))
        if 'cicd_id' in local_var_params:
            query_params.append(('cicd_id', local_var_params['cicd_id']))
        if 'cicd_name' in local_var_params:
            query_params.append(('cicd_name', local_var_params['cicd_name']))

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

    def handle_image_vulnerability_async(self, request):
        r"""处置镜像漏洞

        处置镜像漏洞
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for HandleImageVulnerability
        :type request: :class:`huaweicloudsdkhss.v5.HandleImageVulnerabilityRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.HandleImageVulnerabilityResponse`
        """
        http_info = self._handle_image_vulnerability_http_info(request)
        return self._call_api(**http_info)

    def handle_image_vulnerability_async_invoker(self, request):
        http_info = self._handle_image_vulnerability_http_info(request)
        return AsyncInvoker(self, http_info)

    def _handle_image_vulnerability_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/image/vulnerability/handle",
            "request_type": request.__class__.__name__,
            "response_type": "HandleImageVulnerabilityResponse"
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

    def list_image_white_lists_async(self, request):
        r"""查询镜像白名单列表

        查询镜像白名单列表，目前仅支持漏洞白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageWhiteLists
        :type request: :class:`huaweicloudsdkhss.v5.ListImageWhiteListsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListImageWhiteListsResponse`
        """
        http_info = self._list_image_white_lists_http_info(request)
        return self._call_api(**http_info)

    def list_image_white_lists_async_invoker(self, request):
        http_info = self._list_image_white_lists_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_white_lists_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/whitelists",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageWhiteListsResponse"
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
        if 'global_image_type' in local_var_params:
            query_params.append(('global_image_type', local_var_params['global_image_type']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))
        if 'vul_type' in local_var_params:
            query_params.append(('vul_type', local_var_params['vul_type']))

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

    def list_vul_affect_images_async(self, request):
        r"""查看受漏洞影响的镜像列表

        查看受漏洞影响的镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulAffectImages
        :type request: :class:`huaweicloudsdkhss.v5.ListVulAffectImagesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulAffectImagesResponse`
        """
        http_info = self._list_vul_affect_images_http_info(request)
        return self._call_api(**http_info)

    def list_vul_affect_images_async_invoker(self, request):
        http_info = self._list_vul_affect_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_affect_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulAffectImagesResponse"
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
        if 'is_handled' in local_var_params:
            query_params.append(('is_handled', local_var_params['is_handled']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'repair_necessity' in local_var_params:
            query_params.append(('repair_necessity', local_var_params['repair_necessity']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'registry_name' in local_var_params:
            query_params.append(('registry_name', local_var_params['registry_name']))
        if 'registry_type' in local_var_params:
            query_params.append(('registry_type', local_var_params['registry_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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

    def show_image_white_list_detail_async(self, request):
        r"""查询镜像白名单详情

        查询镜像白名单详情，需要分页查询白名单关联的镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageWhiteListDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowImageWhiteListDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowImageWhiteListDetailResponse`
        """
        http_info = self._show_image_white_list_detail_http_info(request)
        return self._call_api(**http_info)

    def show_image_white_list_detail_async_invoker(self, request):
        http_info = self._show_image_white_list_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_white_list_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/whitelists/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageWhiteListDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'global_image_type' in local_var_params:
            query_params.append(('global_image_type', local_var_params['global_image_type']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_image_scan_task_async(self, request):
        r"""获取扫描任务列表

        获取扫描任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageScanTask
        :type request: :class:`huaweicloudsdkhss.v5.ListImageScanTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListImageScanTaskResponse`
        """
        http_info = self._list_image_scan_task_http_info(request)
        return self._call_api(**http_info)

    def list_image_scan_task_async_invoker(self, request):
        http_info = self._list_image_scan_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_scan_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/image/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageScanTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'global_image_type' in local_var_params:
            query_params.append(('global_image_type', local_var_params['global_image_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'create_time' in local_var_params:
            query_params.append(('create_time', local_var_params['create_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'task_status' in local_var_params:
            query_params.append(('task_status', local_var_params['task_status']))
        if 'scan_scope' in local_var_params:
            query_params.append(('scan_scope', local_var_params['scan_scope']))

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

    def add_policy_group_async(self, request):
        r"""复制策略组

        复制策略组，选择已有的旗舰版或容器版策略组，复制生成新的策略组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddPolicyGroup
        :type request: :class:`huaweicloudsdkhss.v5.AddPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddPolicyGroupResponse`
        """
        http_info = self._add_policy_group_http_info(request)
        return self._call_api(**http_info)

    def add_policy_group_async_invoker(self, request):
        http_info = self._add_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_policy_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/policy/group",
            "request_type": request.__class__.__name__,
            "response_type": "AddPolicyGroupResponse"
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

    def associate_policy_group_async(self, request):
        r"""部署策略组

        为已经开启旗舰版或容器版防护的服务器部署策略组
        
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

    def change_policy_group_async(self, request):
        r"""修改策略组相关内容

        修改策略组相关内容，如防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangePolicyGroup
        :type request: :class:`huaweicloudsdkhss.v5.ChangePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangePolicyGroupResponse`
        """
        http_info = self._change_policy_group_http_info(request)
        return self._call_api(**http_info)

    def change_policy_group_async_invoker(self, request):
        http_info = self._change_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_policy_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/policy/group",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePolicyGroupResponse"
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

    def delete_policy_group_async(self, request):
        r"""删除策略组

        删除策略组，支持删除非默认并且未关联服务器的策略组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicyGroup
        :type request: :class:`huaweicloudsdkhss.v5.DeletePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeletePolicyGroupResponse`
        """
        http_info = self._delete_policy_group_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_group_async_invoker(self, request):
        http_info = self._delete_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_policy_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/policy/group",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyGroupResponse"
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

    def list_policy_group_async(self, request):
        r"""查询策略组列表

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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'container_mode' in local_var_params:
            query_params.append(('container_mode', local_var_params['container_mode']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def list_locked_status_async(self, request):
        r"""查询资源的锁定状态

        按需计费的防护配额转包年/包月过程中，会将防护配额锁定，已锁定的防护配额不支持转包年/包月，通过该接口可查询主机安全防护配额的锁定状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLockedStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListLockedStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListLockedStatusResponse`
        """
        http_info = self._list_locked_status_http_info(request)
        return self._call_api(**http_info)

    def list_locked_status_async_invoker(self, request):
        http_info = self._list_locked_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_locked_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/resources/{resource_id}/locked-status",
            "request_type": request.__class__.__name__,
            "response_type": "ListLockedStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def show_security_check_cluster_report_async(self, request):
        r"""查询集群的安全体检报告信息

        查询集群的安全体检报告信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityCheckClusterReport
        :type request: :class:`huaweicloudsdkhss.v5.ShowSecurityCheckClusterReportRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowSecurityCheckClusterReportResponse`
        """
        http_info = self._show_security_check_cluster_report_http_info(request)
        return self._call_api(**http_info)

    def show_security_check_cluster_report_async_invoker(self, request):
        http_info = self._show_security_check_cluster_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_security_check_cluster_report_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/security-check/containers/cluster-reports/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecurityCheckClusterReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_task_async(self, request):
        r"""创建任务

        创建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkhss.v5.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.CreateTaskResponse`
        """
        http_info = self._create_task_http_info(request)
        return self._call_api(**http_info)

    def create_task_async_invoker(self, request):
        http_info = self._create_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/common/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTaskResponse"
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

    def list_task_resources_async(self, request):
        r"""查询当前任务关联的资源列表

        查询当前任务关联的资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTaskResources
        :type request: :class:`huaweicloudsdkhss.v5.ListTaskResourcesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListTaskResourcesResponse`
        """
        http_info = self._list_task_resources_http_info(request)
        return self._call_api(**http_info)

    def list_task_resources_async_invoker(self, request):
        http_info = self._list_task_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_task_resources_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/common/tasks/{task_id}/resources/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTaskResourcesResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_tasks_async(self, request):
        r"""查询任务列表

        查询任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkhss.v5.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListTasksResponse`
        """
        http_info = self._list_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_async_invoker(self, request):
        http_info = self._list_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tasks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/common/tasks/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksResponse"
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

    def show_task_statistics_async(self, request):
        r"""查询任务统计数据

        查询任务统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowTaskStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowTaskStatisticsResponse`
        """
        http_info = self._show_task_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_task_statistics_async_invoker(self, request):
        http_info = self._show_task_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/common/task-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))

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

    def change_vul_scan_policy_async(self, request):
        r"""修改漏洞扫描策略

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

    def create_vulnerability_scan_task_async(self, request):
        r"""创建漏洞扫描任务

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

    def export_handled_vulnerabilities_async(self, request):
        r"""创建历史处理的漏洞导出任务

        创建历史处理的漏洞导出任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportHandledVulnerabilities
        :type request: :class:`huaweicloudsdkhss.v5.ExportHandledVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ExportHandledVulnerabilitiesResponse`
        """
        http_info = self._export_handled_vulnerabilities_http_info(request)
        return self._call_api(**http_info)

    def export_handled_vulnerabilities_async_invoker(self, request):
        http_info = self._export_handled_vulnerabilities_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_handled_vulnerabilities_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vulnerability/history/export-task",
            "request_type": request.__class__.__name__,
            "response_type": "ExportHandledVulnerabilitiesResponse"
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

    def export_vul_handle_history_async(self, request):
        r"""创建漏洞处置历史记录的导出任务

        创建漏洞处置历史记录的导出任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportVulHandleHistory
        :type request: :class:`huaweicloudsdkhss.v5.ExportVulHandleHistoryRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ExportVulHandleHistoryResponse`
        """
        http_info = self._export_vul_handle_history_http_info(request)
        return self._call_api(**http_info)

    def export_vul_handle_history_async_invoker(self, request):
        http_info = self._export_vul_handle_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_vul_handle_history_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vulnerability/handle-history/export-task",
            "request_type": request.__class__.__name__,
            "response_type": "ExportVulHandleHistoryResponse"
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

    def export_vuls_async(self, request):
        r"""导出漏洞及漏洞影响的主机的相关信息

        导出漏洞及漏洞影响的主机的相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportVuls
        :type request: :class:`huaweicloudsdkhss.v5.ExportVulsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ExportVulsResponse`
        """
        http_info = self._export_vuls_http_info(request)
        return self._call_api(**http_info)

    def export_vuls_async_invoker(self, request):
        http_info = self._export_vuls_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_vuls_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vul/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportVulsResponse"
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
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'export_size' in local_var_params:
            query_params.append(('export_size', local_var_params['export_size']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
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

    def list_host_vuls_async(self, request):
        r"""查询单台服务器漏洞信息

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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))
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

    def list_vul_container_apps_async(self, request):
        r"""查询单个漏洞影响的容器app信息

        查询单个漏洞影响的容器app信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulContainerApps
        :type request: :class:`huaweicloudsdkhss.v5.ListVulContainerAppsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulContainerAppsResponse`
        """
        http_info = self._list_vul_container_apps_http_info(request)
        return self._call_api(**http_info)

    def list_vul_container_apps_async_invoker(self, request):
        http_info = self._list_vul_container_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_container_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/container/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulContainerAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'container_id' in local_var_params:
            query_params.append(('container_id', local_var_params['container_id']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
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

    def list_vul_containers_async(self, request):
        r"""查询单个漏洞影响的容器信息

        查询单个漏洞影响的容器信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVulContainers
        :type request: :class:`huaweicloudsdkhss.v5.ListVulContainersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulContainersResponse`
        """
        http_info = self._list_vul_containers_http_info(request)
        return self._call_api(**http_info)

    def list_vul_containers_async_invoker(self, request):
        http_info = self._list_vul_containers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vul_containers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/containers",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulContainersResponse"
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
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity_level' in local_var_params:
            query_params.append(('severity_level', local_var_params['severity_level']))
        if 'min_scan_time' in local_var_params:
            query_params.append(('min_scan_time', local_var_params['min_scan_time']))
        if 'max_scan_time' in local_var_params:
            query_params.append(('max_scan_time', local_var_params['max_scan_time']))
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

    def list_vul_hosts_async(self, request):
        r"""查询单个漏洞影响的云服务器信息

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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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
        r"""查询漏洞扫描任务列表

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
        r"""查询漏洞扫描任务对应的主机列表

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
        r"""查询漏洞列表

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

    def record_user_view_vul_task_async(self, request):
        r"""记录用户查看漏洞任务管理页面的最后时间

        记录用户查看漏洞任务管理页面的最后时间
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RecordUserViewVulTask
        :type request: :class:`huaweicloudsdkhss.v5.RecordUserViewVulTaskRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.RecordUserViewVulTaskResponse`
        """
        http_info = self._record_user_view_vul_task_http_info(request)
        return self._call_api(**http_info)

    def record_user_view_vul_task_async_invoker(self, request):
        http_info = self._record_user_view_vul_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _record_user_view_vul_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vulnerability/task/user/trace",
            "request_type": request.__class__.__name__,
            "response_type": "RecordUserViewVulTaskResponse"
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

    def show_vul_scan_policy_async(self, request):
        r"""查询漏洞扫描策略

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
        r"""查询漏洞管理统计数据

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

    def show_vul_task_statistics_async(self, request):
        r"""获取漏洞任务的未读数量

        获取漏洞任务的未读数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVulTaskStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowVulTaskStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowVulTaskStatisticsResponse`
        """
        http_info = self._show_vul_task_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_vul_task_statistics_async_invoker(self, request):
        http_info = self._show_vul_task_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vul_task_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vulnerability/task/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVulTaskStatisticsResponse"
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

    def batch_start_web_tamper_protection_async(self, request):
        r"""批量开启网页防篡改防护

        批量开启网页防篡改防护
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartWebTamperProtection
        :type request: :class:`huaweicloudsdkhss.v5.BatchStartWebTamperProtectionRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchStartWebTamperProtectionResponse`
        """
        http_info = self._batch_start_web_tamper_protection_http_info(request)
        return self._call_api(**http_info)

    def batch_start_web_tamper_protection_async_invoker(self, request):
        http_info = self._batch_start_web_tamper_protection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_web_tamper_protection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/webtamper/protection/batch-open",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartWebTamperProtectionResponse"
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

    def delete_backup_host_info_async(self, request):
        r"""删除远端备份服务器

        删除远端备份服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackupHostInfo
        :type request: :class:`huaweicloudsdkhss.v5.DeleteBackupHostInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteBackupHostInfoResponse`
        """
        http_info = self._delete_backup_host_info_http_info(request)
        return self._call_api(**http_info)

    def delete_backup_host_info_async_invoker(self, request):
        http_info = self._delete_backup_host_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_backup_host_info_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/wtp/backup-hosts",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackupHostInfoResponse"
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

    def export_web_tamper_host_async(self, request):
        r"""导出网页防篡改防护目录列表

        导出网页防篡改防护目录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportWebTamperHost
        :type request: :class:`huaweicloudsdkhss.v5.ExportWebTamperHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ExportWebTamperHostResponse`
        """
        http_info = self._export_web_tamper_host_http_info(request)
        return self._call_api(**http_info)

    def export_web_tamper_host_async_invoker(self, request):
        http_info = self._export_web_tamper_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_web_tamper_host_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/webtamper/host/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportWebTamperHostResponse"
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

    def list_backup_hosts_info_async(self, request):
        r"""查询远端备份服务器列表

        查询远端备份服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackupHostsInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListBackupHostsInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListBackupHostsInfoResponse`
        """
        http_info = self._list_backup_hosts_info_http_info(request)
        return self._call_api(**http_info)

    def list_backup_hosts_info_async_invoker(self, request):
        http_info = self._list_backup_hosts_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backup_hosts_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/wtp/backup-hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupHostsInfoResponse"
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
        if 'is_run' in local_var_params:
            query_params.append(('is_run', local_var_params['is_run']))

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

    def list_host_protect_history_info_async(self, request):
        r"""查询主机静态网页防篡改防护动态

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
        r"""查询主机动态网页防篡改防护动态

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

    def list_web_tamper_host_async(self, request):
        r"""查询可开启网页防篡改的服务器列表

        查询可开启网页防篡改的服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWebTamperHost
        :type request: :class:`huaweicloudsdkhss.v5.ListWebTamperHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWebTamperHostResponse`
        """
        http_info = self._list_web_tamper_host_http_info(request)
        return self._call_api(**http_info)

    def list_web_tamper_host_async_invoker(self, request):
        http_info = self._list_web_tamper_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_web_tamper_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/webtamper/host-management/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListWebTamperHostResponse"
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
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'web_app_name' in local_var_params:
            query_params.append(('web_app_name', local_var_params['web_app_name']))

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
        r"""查询防护列表

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
        if 'wtp_status' in local_var_params:
            query_params.append(('wtp_status', local_var_params['wtp_status']))
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

    def set_protect_dir_switch_info_async(self, request):
        r"""暂停或恢复网页防篡改的防护目录

        暂停或恢复网页防篡改的防护目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetProtectDirSwitchInfo
        :type request: :class:`huaweicloudsdkhss.v5.SetProtectDirSwitchInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SetProtectDirSwitchInfoResponse`
        """
        http_info = self._set_protect_dir_switch_info_http_info(request)
        return self._call_api(**http_info)

    def set_protect_dir_switch_info_async_invoker(self, request):
        http_info = self._set_protect_dir_switch_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_protect_dir_switch_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/wtp/{host_id}/protect-directories/status",
            "request_type": request.__class__.__name__,
            "response_type": "SetProtectDirSwitchInfoResponse"
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

    def set_rasp_switch_async(self, request):
        r"""开启/关闭动态网页防篡改防护

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

    def set_remote_backup_info_async(self, request):
        r"""开启或关闭远端备份

        为已开启网页防篡改的服务器，开启或关闭远端备份功能，仅限Linux服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetRemoteBackupInfo
        :type request: :class:`huaweicloudsdkhss.v5.SetRemoteBackupInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SetRemoteBackupInfoResponse`
        """
        http_info = self._set_remote_backup_info_http_info(request)
        return self._call_api(**http_info)

    def set_remote_backup_info_async_invoker(self, request):
        http_info = self._set_remote_backup_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_remote_backup_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/wtp/{host_id}/set-remote-backup",
            "request_type": request.__class__.__name__,
            "response_type": "SetRemoteBackupInfoResponse"
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

    def set_wtp_protection_status_info_async(self, request):
        r"""开启关闭网页防篡改防护

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

    def show_remote_backup_host_info_async(self, request):
        r"""查询远端备份服务器信息

        查询远端备份服务器信息：查询远端备份服务器的相关信息，包含服务器名称、地址、端口号、备份路径、运行状态信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRemoteBackupHostInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowRemoteBackupHostInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowRemoteBackupHostInfoResponse`
        """
        http_info = self._show_remote_backup_host_info_http_info(request)
        return self._call_api(**http_info)

    def show_remote_backup_host_info_async_invoker(self, request):
        http_info = self._show_remote_backup_host_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_remote_backup_host_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/wtp/{host_id}/backup-host",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRemoteBackupHostInfoResponse"
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

    def show_web_tamper_host_policy_async(self, request):
        r"""查看网页防篡改策略信息

        查看网页防篡改策略信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWebTamperHostPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ShowWebTamperHostPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowWebTamperHostPolicyResponse`
        """
        http_info = self._show_web_tamper_host_policy_http_info(request)
        return self._call_api(**http_info)

    def show_web_tamper_host_policy_async_invoker(self, request):
        http_info = self._show_web_tamper_host_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_web_tamper_host_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/webtamper/{host_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWebTamperHostPolicyResponse"
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

    def show_web_tamper_rasp_path_async(self, request):
        r"""查询动态网页防篡改的Tomcat bin目录

        查询动态网页防篡改的Tomcat bin目录：查询动态网页防篡改功能配置的Tomcat bin目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWebTamperRaspPath
        :type request: :class:`huaweicloudsdkhss.v5.ShowWebTamperRaspPathRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowWebTamperRaspPathResponse`
        """
        http_info = self._show_web_tamper_rasp_path_http_info(request)
        return self._call_api(**http_info)

    def show_web_tamper_rasp_path_async_invoker(self, request):
        http_info = self._show_web_tamper_rasp_path_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_web_tamper_rasp_path_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/wtp/{host_id}/rasp-path",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWebTamperRaspPathResponse"
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
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))

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

    def show_wtp_protect_statistics_async(self, request):
        r"""防护数据统计

        防护数据统计：统计防护服务器数、防护目录数、近七天的已防御篡改攻击数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWtpProtectStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ShowWtpProtectStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowWtpProtectStatisticsResponse`
        """
        http_info = self._show_wtp_protect_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_wtp_protect_statistics_async_invoker(self, request):
        http_info = self._show_wtp_protect_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_wtp_protect_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/wtp/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWtpProtectStatisticsResponse"
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

    def update_backup_host_info_async(self, request):
        r"""添加或修改远端备份服务器

        添加或修改远端备份服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBackupHostInfo
        :type request: :class:`huaweicloudsdkhss.v5.UpdateBackupHostInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateBackupHostInfoResponse`
        """
        http_info = self._update_backup_host_info_http_info(request)
        return self._call_api(**http_info)

    def update_backup_host_info_async_invoker(self, request):
        http_info = self._update_backup_host_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_backup_host_info_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/wtp/backup-hosts",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBackupHostInfoResponse"
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

    def update_web_tamper_host_policy_async(self, request):
        r"""编辑网页防篡改策略信息

        编辑网页防篡改策略信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWebTamperHostPolicy
        :type request: :class:`huaweicloudsdkhss.v5.UpdateWebTamperHostPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateWebTamperHostPolicyResponse`
        """
        http_info = self._update_web_tamper_host_policy_http_info(request)
        return self._call_api(**http_info)

    def update_web_tamper_host_policy_async_invoker(self, request):
        http_info = self._update_web_tamper_host_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_web_tamper_host_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/webtamper/{host_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWebTamperHostPolicyResponse"
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

    def update_web_tamper_rasp_path_async(self, request):
        r"""修改动态网页防篡改的Tomcat bin目录

        修改动态网页防篡改的Tomcat bin目录：修改动态网页防篡改的Tomcat bin目录，重新下发动态网页防篡改策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWebTamperRaspPath
        :type request: :class:`huaweicloudsdkhss.v5.UpdateWebTamperRaspPathRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateWebTamperRaspPathResponse`
        """
        http_info = self._update_web_tamper_rasp_path_http_info(request)
        return self._call_api(**http_info)

    def update_web_tamper_rasp_path_async_invoker(self, request):
        http_info = self._update_web_tamper_rasp_path_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_web_tamper_rasp_path_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/wtp/{host_id}/rasp-path",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWebTamperRaspPathResponse"
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
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))

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
