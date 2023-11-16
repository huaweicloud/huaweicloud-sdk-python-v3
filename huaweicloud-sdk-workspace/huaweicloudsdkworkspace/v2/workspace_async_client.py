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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkworkspace'")


class WorkspaceAsyncClient(Client):
    def __init__(self):
        super(WorkspaceAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkworkspace.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "WorkspaceAsyncClient":
                raise TypeError("client type error, support client type is WorkspaceAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_delete_access_policies_async(self, request):
        """删除接入策略

        该接口用于删除指定接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAccessPolicies
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteAccessPoliciesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteAccessPoliciesResponse`
        """
        http_info = self._batch_delete_access_policies_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_access_policies_async_invoker(self, request):
        http_info = self._batch_delete_access_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_access_policies_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/access-policy",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAccessPoliciesResponse"
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

    def create_access_policy_async(self, request):
        """创建接入策略

        该接口用于创建接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAccessPolicy
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateAccessPolicyResponse`
        """
        http_info = self._create_access_policy_http_info(request)
        return self._call_api(**http_info)

    def create_access_policy_async_invoker(self, request):
        http_info = self._create_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_access_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/access-policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccessPolicyResponse"
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

    def list_access_policies_async(self, request):
        """查询接入策略

        该接口用于查询接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessPolicies
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAccessPoliciesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAccessPoliciesResponse`
        """
        http_info = self._list_access_policies_http_info(request)
        return self._call_api(**http_info)

    def list_access_policies_async_invoker(self, request):
        http_info = self._list_access_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_access_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/access-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessPoliciesResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_access_policy_objects_async(self, request):
        """查询指定接入策略的应用对象

        该接口用于查询指定接入策略的应用对象。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessPolicyObjects
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAccessPolicyObjectsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAccessPolicyObjectsResponse`
        """
        http_info = self._list_access_policy_objects_http_info(request)
        return self._call_api(**http_info)

    def list_access_policy_objects_async_invoker(self, request):
        http_info = self._list_access_policy_objects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_access_policy_objects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/access-policy/{access_policy_id}/objects",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessPolicyObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_policy_id' in local_var_params:
            path_params['access_policy_id'] = local_var_params['access_policy_id']

        query_params = []
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

    def update_access_policy_objects_async(self, request):
        """更新指定接入策略的应用对象

        该接口用于更新指定接入策略的应用对象。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAccessPolicyObjects
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyObjectsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyObjectsResponse`
        """
        http_info = self._update_access_policy_objects_http_info(request)
        return self._call_api(**http_info)

    def update_access_policy_objects_async_invoker(self, request):
        http_info = self._update_access_policy_objects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_access_policy_objects_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/access-policy/{access_policy_id}/objects",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccessPolicyObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_policy_id' in local_var_params:
            path_params['access_policy_id'] = local_var_params['access_policy_id']

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

    def show_assist_auth_config_async(self, request):
        """查询辅助认证配置

        查询辅助认证的配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAssistAuthConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowAssistAuthConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowAssistAuthConfigResponse`
        """
        http_info = self._show_assist_auth_config_http_info(request)
        return self._call_api(**http_info)

    def show_assist_auth_config_async_invoker(self, request):
        http_info = self._show_assist_auth_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_assist_auth_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/assist-auth-config/method-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssistAuthConfigResponse"
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

    def update_assist_auth_method_config_async(self, request):
        """更新辅助认证策略配置

        更新辅助认证策略配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAssistAuthMethodConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAssistAuthMethodConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAssistAuthMethodConfigResponse`
        """
        http_info = self._update_assist_auth_method_config_http_info(request)
        return self._call_api(**http_info)

    def update_assist_auth_method_config_async_invoker(self, request):
        http_info = self._update_assist_auth_method_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_assist_auth_method_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/assist-auth-config/method-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssistAuthMethodConfigResponse"
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

    def list_availability_zones_async(self, request):
        """查询可用分区列表

        该接口用于查询云桌面支持的可用分区列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAvailabilityZonesResponse`
        """
        http_info = self._list_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zones_async_invoker(self, request):
        http_info = self._list_availability_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_availability_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/availability-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZonesResponse"
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

    def export_user_login_info_new_async(self, request):
        """导出连接记录

        该接口用于导出连接记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportUserLoginInfoNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ExportUserLoginInfoNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExportUserLoginInfoNewResponse`
        """
        http_info = self._export_user_login_info_new_http_info(request)
        return self._call_api(**http_info)

    def export_user_login_info_new_async_invoker(self, request):
        http_info = self._export_user_login_info_new_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_user_login_info_new_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/connections/desktops/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportUserLoginInfoNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'computer_name' in local_var_params:
            query_params.append(('computer_name', local_var_params['computer_name']))
        if 'terminal_type' in local_var_params:
            query_params.append(('terminal_type', local_var_params['terminal_type']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_history_online_info_new_async(self, request):
        """查询登录人数

        该接口用于查询登录人数，注意查询参数不可全空。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHistoryOnlineInfoNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ListHistoryOnlineInfoNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListHistoryOnlineInfoNewResponse`
        """
        http_info = self._list_history_online_info_new_http_info(request)
        return self._call_api(**http_info)

    def list_history_online_info_new_async_invoker(self, request):
        http_info = self._list_history_online_info_new_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_history_online_info_new_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/connections/online-users",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryOnlineInfoNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_login_records_new_async(self, request):
        """查询登录信息

        该接口用于查询登录信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoginRecordsNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ListLoginRecordsNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListLoginRecordsNewResponse`
        """
        http_info = self._list_login_records_new_http_info(request)
        return self._call_api(**http_info)

    def list_login_records_new_async_invoker(self, request):
        http_info = self._list_login_records_new_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_login_records_new_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/connections/desktops",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoginRecordsNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'computer_name' in local_var_params:
            query_params.append(('computer_name', local_var_params['computer_name']))
        if 'terminal_type' in local_var_params:
            query_params.append(('terminal_type', local_var_params['terminal_type']))
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

    def batch_delete_desktops_async(self, request):
        """批量删除桌面

        批量删除桌面，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsResponse`
        """
        http_info = self._batch_delete_desktops_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_desktops_async_invoker(self, request):
        http_info = self._batch_delete_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_desktops_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDesktopsResponse"
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

    def batch_logoff_desktops_async(self, request):
        """批量注销桌面

        批量注销桌面。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchLogoffDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchLogoffDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchLogoffDesktopsResponse`
        """
        http_info = self._batch_logoff_desktops_http_info(request)
        return self._call_api(**http_info)

    def batch_logoff_desktops_async_invoker(self, request):
        http_info = self._batch_logoff_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_logoff_desktops_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/logoff",
            "request_type": request.__class__.__name__,
            "response_type": "BatchLogoffDesktopsResponse"
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

    def batch_rebuild_desktops_system_disk_async(self, request):
        """重建桌面

        批量重建桌面系统盘。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebuildDesktopsSystemDisk
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchRebuildDesktopsSystemDiskRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchRebuildDesktopsSystemDiskResponse`
        """
        http_info = self._batch_rebuild_desktops_system_disk_http_info(request)
        return self._call_api(**http_info)

    def batch_rebuild_desktops_system_disk_async_invoker(self, request):
        http_info = self._batch_rebuild_desktops_system_disk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_rebuild_desktops_system_disk_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/rebuild",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRebuildDesktopsSystemDiskResponse"
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

    def batch_run_desktops_async(self, request):
        """操作桌面

        批量操作桌面，用于批量开机、关机和重启。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRunDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchRunDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchRunDesktopsResponse`
        """
        http_info = self._batch_run_desktops_http_info(request)
        return self._call_api(**http_info)

    def batch_run_desktops_async_invoker(self, request):
        http_info = self._batch_run_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_run_desktops_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRunDesktopsResponse"
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

    def change_desktop_network_async(self, request):
        """切换桌面网络

        切换桌面vpc、子网、ip、安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeDesktopNetwork
        :type request: :class:`huaweicloudsdkworkspace.v2.ChangeDesktopNetworkRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ChangeDesktopNetworkResponse`
        """
        http_info = self._change_desktop_network_http_info(request)
        return self._call_api(**http_info)

    def change_desktop_network_async_invoker(self, request):
        http_info = self._change_desktop_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_desktop_network_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/networks",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeDesktopNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

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

    def create_desktop_async(self, request):
        """创建桌面

        创建桌面，并将此桌面分配给用户，当桌面创建成功后用户可以登录使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopResponse`
        """
        http_info = self._create_desktop_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_async_invoker(self, request):
        http_info = self._create_desktop_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_desktop_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDesktopResponse"
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

    def delete_desktop_async(self, request):
        """删除单个桌面

        删除单个桌面，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopResponse`
        """
        http_info = self._delete_desktop_http_info(request)
        return self._call_api(**http_info)

    def delete_desktop_async_invoker(self, request):
        http_info = self._delete_desktop_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_desktop_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDesktopResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

        query_params = []
        if 'delete_users' in local_var_params:
            query_params.append(('delete_users', local_var_params['delete_users']))
        if 'email_notification' in local_var_params:
            query_params.append(('email_notification', local_var_params['email_notification']))
        if 'is_force_delete' in local_var_params:
            query_params.append(('is_force_delete', local_var_params['is_force_delete']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_desktops_async(self, request):
        """查询桌面列表

        该接口用于查询桌面虚拟机列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsResponse`
        """
        http_info = self._list_desktops_http_info(request)
        return self._call_api(**http_info)

    def list_desktops_async_invoker(self, request):
        http_info = self._list_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_desktops_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'computer_name' in local_var_params:
            query_params.append(('computer_name', local_var_params['computer_name']))
        if 'desktop_ip' in local_var_params:
            query_params.append(('desktop_ip', local_var_params['desktop_ip']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'desktop_type' in local_var_params:
            query_params.append(('desktop_type', local_var_params['desktop_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_desktops_detail_async(self, request):
        """查询桌面详情列表

        查询桌面详情信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDesktopsDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsDetailResponse`
        """
        http_info = self._list_desktops_detail_http_info(request)
        return self._call_api(**http_info)

    def list_desktops_detail_async_invoker(self, request):
        http_info = self._list_desktops_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_desktops_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopsDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'user_names' in local_var_params:
            query_params.append(('user_names', local_var_params['user_names']))
            collection_formats['user_names'] = 'csv'
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
        if 'computer_name' in local_var_params:
            query_params.append(('computer_name', local_var_params['computer_name']))
        if 'desktop_ip' in local_var_params:
            query_params.append(('desktop_ip', local_var_params['desktop_ip']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'desktop_id' in local_var_params:
            query_params.append(('desktop_id', local_var_params['desktop_id']))
            collection_formats['desktop_id'] = 'csv'
        if 'desktop_type' in local_var_params:
            query_params.append(('desktop_type', local_var_params['desktop_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
        if 'user_attached' in local_var_params:
            query_params.append(('user_attached', local_var_params['user_attached']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'in_maintenance_mode' in local_var_params:
            query_params.append(('in_maintenance_mode', local_var_params['in_maintenance_mode']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def resize_desktop_async(self, request):
        """变更规格

        变更云桌面规格，只支持变更CPU和内存，不支持变更磁盘，不支持同规格互相变更。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopResponse`
        """
        http_info = self._resize_desktop_http_info(request)
        return self._call_api(**http_info)

    def resize_desktop_async_invoker(self, request):
        http_info = self._resize_desktop_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_desktop_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeDesktopResponse"
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

    def show_desktop_detail_async(self, request):
        """查询单个桌面详情

        指定桌面Id查询详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDesktopDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopDetailResponse`
        """
        http_info = self._show_desktop_detail_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_detail_async_invoker(self, request):
        http_info = self._show_desktop_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_desktop_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDesktopDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

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

    def show_desktop_network_async(self, request):
        """查询桌面网络

        查询桌面vpc、子网、privateIp、EIP、安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDesktopNetwork
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopNetworkRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopNetworkResponse`
        """
        http_info = self._show_desktop_network_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_network_async_invoker(self, request):
        http_info = self._show_desktop_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_desktop_network_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/networks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDesktopNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

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

    def list_unused_desktops_async(self, request):
        """查询在指定时间段未使用的桌面

        查询在指定时间段未使用的桌面。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUnusedDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUnusedDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUnusedDesktopsResponse`
        """
        http_info = self._list_unused_desktops_http_info(request)
        return self._call_api(**http_info)

    def list_unused_desktops_async_invoker(self, request):
        http_info = self._list_unused_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_unused_desktops_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/statistics/unused",
            "request_type": request.__class__.__name__,
            "response_type": "ListUnusedDesktopsResponse"
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

    def list_used_desktop_info_async(self, request):
        """查询使用桌面的时长

        查询使用桌面的时长。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsedDesktopInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsedDesktopInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsedDesktopInfoResponse`
        """
        http_info = self._list_used_desktop_info_http_info(request)
        return self._call_api(**http_info)

    def list_used_desktop_info_async_invoker(self, request):
        http_info = self._list_used_desktop_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_used_desktop_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/statistics/used",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsedDesktopInfoResponse"
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

    def batch_add_desktops_tags_async(self, request):
        """批量添加多个桌面标签

        同时对多个桌面批量添加标签，如果创建的标签已经存在（key相同）则覆，最大支持100个桌面，每个桌面最大20个标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddDesktopsTags
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchAddDesktopsTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchAddDesktopsTagsResponse`
        """
        http_info = self._batch_add_desktops_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_add_desktops_tags_async_invoker(self, request):
        http_info = self._batch_add_desktops_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_desktops_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/batch-tags",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddDesktopsTagsResponse"
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

    def batch_change_tags_async(self, request):
        """批量添加删除标签

        为指定桌面批量添加或删除标签。创建时，如果创建的标签已经存在（key相同），则覆盖。删除时，如果删除的标签不存在，默认处理成功
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchChangeTags
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchChangeTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchChangeTagsResponse`
        """
        http_info = self._batch_change_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_change_tags_async_invoker(self, request):
        http_info = self._batch_change_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_change_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchChangeTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

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

    def batch_delete_desktops_tags_async(self, request):
        """批量删除多个桌面标签

        同时对多个桌面批量添加标签，删除时，如果删除的标签不存在默认处理成功，最大支持100个桌面，每个桌面最大20个标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteDesktopsTags
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsTagsResponse`
        """
        http_info = self._batch_delete_desktops_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_desktops_tags_async_invoker(self, request):
        http_info = self._batch_delete_desktops_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_desktops_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/desktops/batch-tags",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDesktopsTagsResponse"
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

    def create_tag_async(self, request):
        """创建桌面标签

        该接口用于为桌面创建标签，一个桌面上最多有10个标签。创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_async_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

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

    def delete_tag_async(self, request):
        """删除桌面标签

        该接口用于删除桌面标签。删除时，如果删除的标签不存在，默认处理成功。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_async_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']
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

    def list_desktop_by_tags_async(self, request):
        """使用标签过滤桌面

        使用标签过滤桌面
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDesktopByTags
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopByTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopByTagsResponse`
        """
        http_info = self._list_desktop_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_by_tags_async_invoker(self, request):
        http_info = self._list_desktop_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_desktop_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopByTagsResponse"
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

    def list_project_tags_async(self, request):
        """查询项目标签

        查询租户的所有标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkworkspace.v2.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_async_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagsResponse"
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

    def show_tag_by_desktop_id_async(self, request):
        """查询桌面标签

        查询指定桌面的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTagByDesktopId
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowTagByDesktopIdRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowTagByDesktopIdResponse`
        """
        http_info = self._show_tag_by_desktop_id_http_info(request)
        return self._call_api(**http_info)

    def show_tag_by_desktop_id_async_invoker(self, request):
        http_info = self._show_tag_by_desktop_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tag_by_desktop_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTagByDesktopIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

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

    def batch_delete_user_groups_async(self, request):
        """批量删除用户组

        该接口用于批量删除用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteUserGroups
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteUserGroupsResponse`
        """
        http_info = self._batch_delete_user_groups_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_user_groups_async_invoker(self, request):
        http_info = self._batch_delete_user_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_user_groups_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteUserGroupsResponse"
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

    def create_user_group_async(self, request):
        """创建用户组

        该接口用于创建用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateUserGroupResponse`
        """
        http_info = self._create_user_group_http_info(request)
        return self._call_api(**http_info)

    def create_user_group_async_invoker(self, request):
        http_info = self._create_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_user_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserGroupResponse"
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

    def delete_user_group_async(self, request):
        """删除用户组

        删除用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteUserGroupResponse`
        """
        http_info = self._delete_user_group_http_info(request)
        return self._call_api(**http_info)

    def delete_user_group_async_invoker(self, request):
        http_info = self._delete_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_user_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_user_groups_async(self, request):
        """查询用户组列表

        查询用户组列表，支持分页。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserGroups
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserGroupsResponse`
        """
        http_info = self._list_user_groups_http_info(request)
        return self._call_api(**http_info)

    def list_user_groups_async_invoker(self, request):
        http_info = self._list_user_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserGroupsResponse"
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

    def list_users_of_group_async(self, request):
        """查询用户组中的用户

        该接口用于查询用户组中的用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsersOfGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsersOfGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsersOfGroupResponse`
        """
        http_info = self._list_users_of_group_http_info(request)
        return self._call_api(**http_info)

    def list_users_of_group_async_invoker(self, request):
        http_info = self._list_users_of_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_users_of_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/groups/{group_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersOfGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'active_type' in local_var_params:
            query_params.append(('active_type', local_var_params['active_type']))
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

    def run_actions_on_group_async(self, request):
        """操作用户组

        操作用户组，如添加用户、删除用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunActionsOnGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.RunActionsOnGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.RunActionsOnGroupResponse`
        """
        http_info = self._run_actions_on_group_http_info(request)
        return self._call_api(**http_info)

    def run_actions_on_group_async_invoker(self, request):
        http_info = self._run_actions_on_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_actions_on_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups/{group_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "RunActionsOnGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def update_user_group_async(self, request):
        """修改用户组信息

        该接口用于修改用户组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateUserGroupResponse`
        """
        http_info = self._update_user_group_http_info(request)
        return self._call_api(**http_info)

    def update_user_group_async_invoker(self, request):
        http_info = self._update_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_images_async(self, request):
        """查询产品镜像列表

        该接口用于查询云桌面支持的产品镜像列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImages
        :type request: :class:`huaweicloudsdkworkspace.v2.ListImagesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListImagesResponse`
        """
        http_info = self._list_images_http_info(request)
        return self._call_api(**http_info)

    def list_images_async_invoker(self, request):
        http_info = self._list_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'platform' in local_var_params:
            query_params.append(('platform', local_var_params['platform']))
        if 'architecture' in local_var_params:
            query_params.append(('architecture', local_var_params['architecture']))
        if 'package_type' in local_var_params:
            query_params.append(('package_type', local_var_params['package_type']))
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

    def list_ita_sub_jobs_async(self, request):
        """子任务查询

        该接口用于查询异步任务执行情况，比如查询创建桌面的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListItaSubJobs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListItaSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListItaSubJobsResponse`
        """
        http_info = self._list_ita_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_ita_sub_jobs_async_invoker(self, request):
        http_info = self._list_ita_sub_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ita_sub_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspace-sub-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListItaSubJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'desktop_pool_id' in local_var_params:
            query_params.append(('desktop_pool_id', local_var_params['desktop_pool_id']))
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

    def apply_desktops_internet_async(self, request):
        """开通桌面上网功能

        开通桌面上网功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyDesktopsInternet
        :type request: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternetRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternetResponse`
        """
        http_info = self._apply_desktops_internet_http_info(request)
        return self._call_api(**http_info)

    def apply_desktops_internet_async_invoker(self, request):
        http_info = self._apply_desktops_internet_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_desktops_internet_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/eips",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyDesktopsInternetResponse"
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

    def associate_desktops_eip_async(self, request):
        """桌面绑定EIP

        桌面绑定EIP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateDesktopsEip
        :type request: :class:`huaweicloudsdkworkspace.v2.AssociateDesktopsEipRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssociateDesktopsEipResponse`
        """
        http_info = self._associate_desktops_eip_http_info(request)
        return self._call_api(**http_info)

    def associate_desktops_eip_async_invoker(self, request):
        http_info = self._associate_desktops_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_desktops_eip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/eips/binding",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateDesktopsEipResponse"
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

    def batch_disassociate_desktops_eip_async(self, request):
        """批量桌面解绑EIP

        批量桌面解绑EIP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociateDesktopsEip
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDisassociateDesktopsEipRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDisassociateDesktopsEipResponse`
        """
        http_info = self._batch_disassociate_desktops_eip_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_desktops_eip_async_invoker(self, request):
        http_info = self._batch_disassociate_desktops_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disassociate_desktops_eip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/eips/unbinding",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisassociateDesktopsEipResponse"
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

    def list_desktops_eips_async(self, request):
        """查询已绑定桌面和未绑定的Eip

        查询已绑定桌面和未绑定的Eip。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDesktopsEips
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsEipsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsEipsResponse`
        """
        http_info = self._list_desktops_eips_http_info(request)
        return self._call_api(**http_info)

    def list_desktops_eips_async_invoker(self, request):
        http_info = self._list_desktops_eips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_desktops_eips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/eips",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopsEipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'desktop_id' in local_var_params:
            query_params.append(('desktop_id', local_var_params['desktop_id']))
        if 'desktop_name' in local_var_params:
            query_params.append(('desktop_name', local_var_params['desktop_name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_products_async(self, request):
        """查询产品套餐列表

        该接口用于查询云桌面支持的产品套餐列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkworkspace.v2.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListProductsResponse`
        """
        http_info = self._list_products_http_info(request)
        return self._call_api(**http_info)

    def list_products_async_invoker(self, request):
        http_info = self._list_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'architecture' in local_var_params:
            query_params.append(('architecture', local_var_params['architecture']))
        if 'package_type' in local_var_params:
            query_params.append(('package_type', local_var_params['package_type']))
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

    def show_quotas_async(self, request):
        """查询租户配额

        Console Framework和WKSDesktopManager调用该接口查询租户配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_async_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasResponse"
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

    def create_terminals_binding_desktops_async(self, request):
        """增加终端与桌面绑定配置

        增加终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsResponse`
        """
        http_info = self._create_terminals_binding_desktops_http_info(request)
        return self._call_api(**http_info)

    def create_terminals_binding_desktops_async_invoker(self, request):
        http_info = self._create_terminals_binding_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_terminals_binding_desktops_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/terminals/binding-desktops",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTerminalsBindingDesktopsResponse"
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

    def delete_terminals_binding_desktops_async(self, request):
        """删除终端与桌面绑定配置

        删除终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsResponse`
        """
        http_info = self._delete_terminals_binding_desktops_http_info(request)
        return self._call_api(**http_info)

    def delete_terminals_binding_desktops_async_invoker(self, request):
        http_info = self._delete_terminals_binding_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_terminals_binding_desktops_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/terminals/binding-desktops/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTerminalsBindingDesktopsResponse"
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

    def list_terminals_binding_desktops_async(self, request):
        """查询终端与桌面绑定配置列表

        查询终端与桌面绑定配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsResponse`
        """
        http_info = self._list_terminals_binding_desktops_http_info(request)
        return self._call_api(**http_info)

    def list_terminals_binding_desktops_async_invoker(self, request):
        http_info = self._list_terminals_binding_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_terminals_binding_desktops_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/terminals/binding-desktops",
            "request_type": request.__class__.__name__,
            "response_type": "ListTerminalsBindingDesktopsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'computer_name' in local_var_params:
            query_params.append(('computer_name', local_var_params['computer_name']))
        if 'mac' in local_var_params:
            query_params.append(('mac', local_var_params['mac']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'count_only' in local_var_params:
            query_params.append(('count_only', local_var_params['count_only']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_terminals_binding_desktops_config_async(self, request):
        """查询终端与桌面绑定的开关配置信息

        查询终端与桌面绑定的开关配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTerminalsBindingDesktopsConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsConfigResponse`
        """
        http_info = self._list_terminals_binding_desktops_config_http_info(request)
        return self._call_api(**http_info)

    def list_terminals_binding_desktops_config_async_invoker(self, request):
        http_info = self._list_terminals_binding_desktops_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_terminals_binding_desktops_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/terminals/binding-desktops/config",
            "request_type": request.__class__.__name__,
            "response_type": "ListTerminalsBindingDesktopsConfigResponse"
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

    def update_terminals_binding_desktops_async(self, request):
        """修改终端与桌面绑定配置

        修改终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsResponse`
        """
        http_info = self._update_terminals_binding_desktops_http_info(request)
        return self._call_api(**http_info)

    def update_terminals_binding_desktops_async_invoker(self, request):
        http_info = self._update_terminals_binding_desktops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_terminals_binding_desktops_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/terminals/binding-desktops",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTerminalsBindingDesktopsResponse"
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

    def update_terminals_binding_desktops_config_async(self, request):
        """设置终端与桌面绑定的开关配置

        设置终端与桌面绑定的开关配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTerminalsBindingDesktopsConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsConfigResponse`
        """
        http_info = self._update_terminals_binding_desktops_config_http_info(request)
        return self._call_api(**http_info)

    def update_terminals_binding_desktops_config_async_invoker(self, request):
        http_info = self._update_terminals_binding_desktops_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_terminals_binding_desktops_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/terminals/binding-desktops/config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTerminalsBindingDesktopsConfigResponse"
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

    def batch_create_users_async(self, request):
        """批量创建用户

        该接口用于批量创建用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateUsers
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchCreateUsersRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchCreateUsersResponse`
        """
        http_info = self._batch_create_users_http_info(request)
        return self._call_api(**http_info)

    def batch_create_users_async_invoker(self, request):
        http_info = self._batch_create_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_users_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/users/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateUsersResponse"
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

    def batch_delete_otp_devices_async(self, request):
        """解绑OTP设备

        该接口用于解绑用户的OTP设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteOtpDevices
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteOtpDevicesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteOtpDevicesResponse`
        """
        http_info = self._batch_delete_otp_devices_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_otp_devices_async_invoker(self, request):
        http_info = self._batch_delete_otp_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_otp_devices_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/users/{user_id}/otp-devices",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteOtpDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def change_user_status_async(self, request):
        """操作用户

        该接口用于操作用户，包含三种操作：锁定、解锁和重置密码（重置密码建议使用/v2/{project_id}/users/{user_id}/random-password接口，在没有通知方式的情况下必须使用/v2/{project_id}/users/{user_id}/random-password接口）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeUserStatus
        :type request: :class:`huaweicloudsdkworkspace.v2.ChangeUserStatusRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ChangeUserStatusResponse`
        """
        http_info = self._change_user_status_http_info(request)
        return self._call_api(**http_info)

    def change_user_status_async_invoker(self, request):
        http_info = self._change_user_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_user_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/users/{user_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeUserStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def create_desktop_user_async(self, request):
        """创建用户

        该接口用于创建桌面用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDesktopUser
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopUserRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopUserResponse`
        """
        http_info = self._create_desktop_user_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_user_async_invoker(self, request):
        http_info = self._create_desktop_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_desktop_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDesktopUserResponse"
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

    def delete_user_async(self, request):
        """删除指定用户

        删除指定的桌面用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_async_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_user_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def list_otp_devices_by_user_id_async(self, request):
        """查询OTP设备

        该接口用于查询相应用户下面的OTP设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOtpDevicesByUserId
        :type request: :class:`huaweicloudsdkworkspace.v2.ListOtpDevicesByUserIdRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListOtpDevicesByUserIdResponse`
        """
        http_info = self._list_otp_devices_by_user_id_http_info(request)
        return self._call_api(**http_info)

    def list_otp_devices_by_user_id_async_invoker(self, request):
        http_info = self._list_otp_devices_by_user_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_otp_devices_by_user_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/users/{user_id}/otp-devices",
            "request_type": request.__class__.__name__,
            "response_type": "ListOtpDevicesByUserIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def list_user_detail_async(self, request):
        """查询用户详情信息

        该接口用于查询指定的桌面用户详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserDetailResponse`
        """
        http_info = self._list_user_detail_http_info(request)
        return self._call_api(**http_info)

    def list_user_detail_async_invoker(self, request):
        http_info = self._list_user_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def list_users_async(self, request):
        """查询用户列表

        该接口用于查询桌面用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_async_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'active_type' in local_var_params:
            query_params.append(('active_type', local_var_params['active_type']))
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

    def reset_random_password_async(self, request):
        """给用户重置随机密码

        该接口用于给用户重置一个密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetRandomPassword
        :type request: :class:`huaweicloudsdkworkspace.v2.ResetRandomPasswordRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResetRandomPasswordResponse`
        """
        http_info = self._reset_random_password_http_info(request)
        return self._call_api(**http_info)

    def reset_random_password_async_invoker(self, request):
        http_info = self._reset_random_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_random_password_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/users/{user_id}/random-password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetRandomPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []
        if 'notification_type' in local_var_params:
            query_params.append(('notification_type', local_var_params['notification_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_user_info_async(self, request):
        """修改用户信息

        该接口用于修改桌面用户信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateUserInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateUserInfoResponse`
        """
        http_info = self._update_user_info_http_info(request)
        return self._call_api(**http_info)

    def update_user_info_async_invoker(self, request):
        http_info = self._update_user_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_info_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def add_volumes_async(self, request):
        """增加桌面磁盘

        增加桌面磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.AddVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddVolumesResponse`
        """
        http_info = self._add_volumes_http_info(request)
        return self._call_api(**http_info)

    def add_volumes_async_invoker(self, request):
        http_info = self._add_volumes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_volumes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/volumes",
            "request_type": request.__class__.__name__,
            "response_type": "AddVolumesResponse"
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

    def delete_desktop_volumes_async(self, request):
        """删除桌面数据盘

        删除桌面数据盘，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDesktopVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopVolumesResponse`
        """
        http_info = self._delete_desktop_volumes_http_info(request)
        return self._call_api(**http_info)

    def delete_desktop_volumes_async_invoker(self, request):
        http_info = self._delete_desktop_volumes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_desktop_volumes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/volumes/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDesktopVolumesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

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

    def expand_volumes_async(self, request):
        """扩容桌面磁盘

        扩容桌面磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.ExpandVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExpandVolumesResponse`
        """
        http_info = self._expand_volumes_http_info(request)
        return self._call_api(**http_info)

    def expand_volumes_async_invoker(self, request):
        http_info = self._expand_volumes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _expand_volumes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/volumes/expand",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandVolumesResponse"
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

    def apply_workspace_async(self, request):
        """开通云办公服务

        该接口用于开通云办公服务。
        
        作为异步接口，调用成功说明云办公服务后台收到了开通请求，但服务是否开通成功需要通过任务查询接口(GET /v2/{project_id}/workspace-sub-jobs)查询该任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.ApplyWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyWorkspaceResponse`
        """
        http_info = self._apply_workspace_http_info(request)
        return self._call_api(**http_info)

    def apply_workspace_async_invoker(self, request):
        http_info = self._apply_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_workspace_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyWorkspaceResponse"
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

    def cancel_workspace_async(self, request):
        """注销云办公服务

        该接口用于注销云办公服务。注销前请确保当前用户下的云桌面已经删除，注销后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.CancelWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CancelWorkspaceResponse`
        """
        http_info = self._cancel_workspace_http_info(request)
        return self._call_api(**http_info)

    def cancel_workspace_async_invoker(self, request):
        http_info = self._cancel_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_workspace_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "CancelWorkspaceResponse"
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

    def list_workspaces_async(self, request):
        """查询云办公服务详情

        该接口用于查询云办公服务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkspaces
        :type request: :class:`huaweicloudsdkworkspace.v2.ListWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListWorkspacesResponse`
        """
        http_info = self._list_workspaces_http_info(request)
        return self._call_api(**http_info)

    def list_workspaces_async_invoker(self, request):
        http_info = self._list_workspaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workspaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkspacesResponse"
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

    def show_workspace_lock_async(self, request):
        """查询云办公服务是否被锁定

        查询云办公服务是否被锁定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkspaceLock
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowWorkspaceLockRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowWorkspaceLockResponse`
        """
        http_info = self._show_workspace_lock_http_info(request)
        return self._call_api(**http_info)

    def show_workspace_lock_async_invoker(self, request):
        http_info = self._show_workspace_lock_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workspace_lock_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/lock-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkspaceLockResponse"
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

    def unlock_workspace_async(self, request):
        """解除云办公服务锁定状态

        该接口目前支持解除云办公服务锁定状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnlockWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.UnlockWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UnlockWorkspaceResponse`
        """
        http_info = self._unlock_workspace_http_info(request)
        return self._call_api(**http_info)

    def unlock_workspace_async_invoker(self, request):
        http_info = self._unlock_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unlock_workspace_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/lock-status",
            "request_type": request.__class__.__name__,
            "response_type": "UnlockWorkspaceResponse"
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

    def update_workspace_async(self, request):
        """修改云办公服务属性

        该接口目前支持修改云办公服务属性。单次请求仅支持修改一种属性类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateWorkspaceResponse`
        """
        http_info = self._update_workspace_http_info(request)
        return self._call_api(**http_info)

    def update_workspace_async_invoker(self, request):
        http_info = self._update_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workspace_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkspaceResponse"
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
