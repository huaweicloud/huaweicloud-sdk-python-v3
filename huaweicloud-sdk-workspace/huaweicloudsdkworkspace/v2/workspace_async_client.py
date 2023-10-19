# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


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
        return self._batch_delete_access_policies_with_http_info(request)

    def _batch_delete_access_policies_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/access-policy',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteAccessPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_access_policy_async(self, request):
        """创建接入策略

        该接口用于创建接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAccessPolicy
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateAccessPolicyResponse`
        """
        return self._create_access_policy_with_http_info(request)

    def _create_access_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/access-policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAccessPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_access_policies_async(self, request):
        """查询接入策略

        该接口用于查询接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessPolicies
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAccessPoliciesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAccessPoliciesResponse`
        """
        return self._list_access_policies_with_http_info(request)

    def _list_access_policies_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/access-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccessPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_access_policy_objects_async(self, request):
        """查询指定接入策略的应用对象

        该接口用于查询指定接入策略的应用对象。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessPolicyObjects
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAccessPolicyObjectsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAccessPolicyObjectsResponse`
        """
        return self._list_access_policy_objects_with_http_info(request)

    def _list_access_policy_objects_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/access-policy/{access_policy_id}/objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccessPolicyObjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_access_policy_objects_async(self, request):
        """更新指定接入策略的应用对象

        该接口用于更新指定接入策略的应用对象。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAccessPolicyObjects
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyObjectsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyObjectsResponse`
        """
        return self._update_access_policy_objects_with_http_info(request)

    def _update_access_policy_objects_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_policy_id' in local_var_params:
            path_params['access_policy_id'] = local_var_params['access_policy_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/access-policy/{access_policy_id}/objects',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAccessPolicyObjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_assist_auth_config_async(self, request):
        """查询辅助认证配置

        查询辅助认证的配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAssistAuthConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowAssistAuthConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowAssistAuthConfigResponse`
        """
        return self._show_assist_auth_config_with_http_info(request)

    def _show_assist_auth_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/assist-auth-config/method-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAssistAuthConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_assist_auth_method_config_async(self, request):
        """更新辅助认证策略配置

        更新辅助认证策略配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAssistAuthMethodConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAssistAuthMethodConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAssistAuthMethodConfigResponse`
        """
        return self._update_assist_auth_method_config_with_http_info(request)

    def _update_assist_auth_method_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/assist-auth-config/method-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAssistAuthMethodConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_availability_zones_async(self, request):
        """查询可用分区列表

        该接口用于查询云桌面支持的可用分区列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAvailabilityZonesResponse`
        """
        return self._list_availability_zones_with_http_info(request)

    def _list_availability_zones_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/availability-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_user_login_info_new_async(self, request):
        """导出连接记录

        该接口用于导出连接记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportUserLoginInfoNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ExportUserLoginInfoNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExportUserLoginInfoNewResponse`
        """
        return self._export_user_login_info_new_with_http_info(request)

    def _export_user_login_info_new_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/connections/desktops/export',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportUserLoginInfoNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_history_online_info_new_async(self, request):
        """查询登录人数

        该接口用于查询登录人数，注意查询参数不可全空。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHistoryOnlineInfoNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ListHistoryOnlineInfoNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListHistoryOnlineInfoNewResponse`
        """
        return self._list_history_online_info_new_with_http_info(request)

    def _list_history_online_info_new_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/connections/online-users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHistoryOnlineInfoNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_login_records_new_async(self, request):
        """查询登录信息

        该接口用于查询登录信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoginRecordsNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ListLoginRecordsNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListLoginRecordsNewResponse`
        """
        return self._list_login_records_new_with_http_info(request)

    def _list_login_records_new_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/connections/desktops',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLoginRecordsNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_desktops_async(self, request):
        """批量删除桌面

        批量删除桌面，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsResponse`
        """
        return self._batch_delete_desktops_with_http_info(request)

    def _batch_delete_desktops_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_logoff_desktops_async(self, request):
        """批量注销桌面

        批量注销桌面。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchLogoffDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchLogoffDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchLogoffDesktopsResponse`
        """
        return self._batch_logoff_desktops_with_http_info(request)

    def _batch_logoff_desktops_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/logoff',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchLogoffDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_run_desktops_async(self, request):
        """操作桌面

        批量操作桌面，用于批量开机、关机和重启。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRunDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchRunDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchRunDesktopsResponse`
        """
        return self._batch_run_desktops_with_http_info(request)

    def _batch_run_desktops_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRunDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_desktop_async(self, request):
        """创建桌面

        创建桌面，并将此桌面分配给用户，当桌面创建成功后用户可以登录使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopResponse`
        """
        return self._create_desktop_with_http_info(request)

    def _create_desktop_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDesktopResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_desktop_async(self, request):
        """删除单个桌面

        删除单个桌面，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopResponse`
        """
        return self._delete_desktop_with_http_info(request)

    def _delete_desktop_with_http_info(self, request):
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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/{desktop_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDesktopResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_desktops_async(self, request):
        """查询桌面列表

        该接口用于查询桌面虚拟机列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsResponse`
        """
        return self._list_desktops_with_http_info(request)

    def _list_desktops_with_http_info(self, request):
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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_desktops_detail_async(self, request):
        """查询桌面详情列表

        查询桌面详情信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDesktopsDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsDetailResponse`
        """
        return self._list_desktops_detail_with_http_info(request)

    def _list_desktops_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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
        if 'desktop_id' in local_var_params:
            query_params.append(('desktop_id', local_var_params['desktop_id']))
        if 'desktop_type' in local_var_params:
            query_params.append(('desktop_type', local_var_params['desktop_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDesktopsDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_desktop_async(self, request):
        """变更规格

        变更云桌面规格，只支持变更CPU和内存，不支持变更磁盘，不支持同规格互相变更。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopResponse`
        """
        return self._resize_desktop_with_http_info(request)

    def _resize_desktop_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeDesktopResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_desktop_detail_async(self, request):
        """查询单个桌面详情

        指定桌面Id查询详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDesktopDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopDetailResponse`
        """
        return self._show_desktop_detail_with_http_info(request)

    def _show_desktop_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/{desktop_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDesktopDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_unused_desktops_async(self, request):
        """查询在指定时间段未使用的桌面

        查询在指定时间段未使用的桌面。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUnusedDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUnusedDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUnusedDesktopsResponse`
        """
        return self._list_unused_desktops_with_http_info(request)

    def _list_unused_desktops_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/statistics/unused',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUnusedDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_used_desktop_info_async(self, request):
        """查询使用桌面的时长

        查询使用桌面的时长。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsedDesktopInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsedDesktopInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsedDesktopInfoResponse`
        """
        return self._list_used_desktop_info_with_http_info(request)

    def _list_used_desktop_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/statistics/used',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUsedDesktopInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_user_groups_async(self, request):
        """批量删除用户组

        该接口用于批量删除用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteUserGroups
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteUserGroupsResponse`
        """
        return self._batch_delete_user_groups_with_http_info(request)

    def _batch_delete_user_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteUserGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_user_group_async(self, request):
        """创建用户组

        该接口用于创建用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateUserGroupResponse`
        """
        return self._create_user_group_with_http_info(request)

    def _create_user_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateUserGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_user_group_async(self, request):
        """删除用户组

        删除用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteUserGroupResponse`
        """
        return self._delete_user_group_with_http_info(request)

    def _delete_user_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteUserGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_groups_async(self, request):
        """查询用户组列表

        查询用户组列表，支持分页。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserGroups
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserGroupsResponse`
        """
        return self._list_user_groups_with_http_info(request)

    def _list_user_groups_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUserGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_users_of_group_async(self, request):
        """查询用户组中的用户

        该接口用于查询用户组中的用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsersOfGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsersOfGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsersOfGroupResponse`
        """
        return self._list_users_of_group_with_http_info(request)

    def _list_users_of_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups/{group_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUsersOfGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_actions_on_group_async(self, request):
        """操作用户组

        操作用户组，如添加用户、删除用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunActionsOnGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.RunActionsOnGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.RunActionsOnGroupResponse`
        """
        return self._run_actions_on_group_with_http_info(request)

    def _run_actions_on_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups/{group_id}/actions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunActionsOnGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_group_async(self, request):
        """修改用户组信息

        该接口用于修改用户组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateUserGroupResponse`
        """
        return self._update_user_group_with_http_info(request)

    def _update_user_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_images_async(self, request):
        """查询产品镜像列表

        该接口用于查询云桌面支持的产品镜像列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImages
        :type request: :class:`huaweicloudsdkworkspace.v2.ListImagesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListImagesResponse`
        """
        return self._list_images_with_http_info(request)

    def _list_images_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ita_sub_jobs_async(self, request):
        """子任务查询

        该接口用于查询异步任务执行情况，比如查询创建桌面的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListItaSubJobs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListItaSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListItaSubJobsResponse`
        """
        return self._list_ita_sub_jobs_with_http_info(request)

    def _list_ita_sub_jobs_with_http_info(self, request):
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/workspace-sub-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListItaSubJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def apply_desktops_internet_async(self, request):
        """开通桌面上网功能

        开通桌面上网功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyDesktopsInternet
        :type request: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternetRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternetResponse`
        """
        return self._apply_desktops_internet_with_http_info(request)

    def _apply_desktops_internet_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/eips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyDesktopsInternetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_desktops_eip_async(self, request):
        """桌面绑定EIP

        桌面绑定EIP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateDesktopsEip
        :type request: :class:`huaweicloudsdkworkspace.v2.AssociateDesktopsEipRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssociateDesktopsEipResponse`
        """
        return self._associate_desktops_eip_with_http_info(request)

    def _associate_desktops_eip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/eips/binding',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateDesktopsEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_disassociate_desktops_eip_async(self, request):
        """批量桌面解绑EIP

        批量桌面解绑EIP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociateDesktopsEip
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDisassociateDesktopsEipRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDisassociateDesktopsEipResponse`
        """
        return self._batch_disassociate_desktops_eip_with_http_info(request)

    def _batch_disassociate_desktops_eip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/eips/unbinding',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDisassociateDesktopsEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_desktops_eips_async(self, request):
        """查询已绑定桌面和未绑定的Eip

        查询已绑定桌面和未绑定的Eip。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDesktopsEips
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsEipsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsEipsResponse`
        """
        return self._list_desktops_eips_with_http_info(request)

    def _list_desktops_eips_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/eips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDesktopsEipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_products_async(self, request):
        """查询产品套餐列表

        该接口用于查询云桌面支持的产品套餐列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkworkspace.v2.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListProductsResponse`
        """
        return self._list_products_with_http_info(request)

    def _list_products_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/products',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProductsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas_async(self, request):
        """查询租户配额

        Console Framework和WKSDesktopManager调用该接口查询租户配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowQuotasResponse`
        """
        return self._show_quotas_with_http_info(request)

    def _show_quotas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_terminals_binding_desktops_async(self, request):
        """增加终端与桌面绑定配置

        增加终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsResponse`
        """
        return self._create_terminals_binding_desktops_with_http_info(request)

    def _create_terminals_binding_desktops_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/terminals/binding-desktops',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTerminalsBindingDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_terminals_binding_desktops_async(self, request):
        """删除终端与桌面绑定配置

        删除终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsResponse`
        """
        return self._delete_terminals_binding_desktops_with_http_info(request)

    def _delete_terminals_binding_desktops_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/terminals/binding-desktops/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTerminalsBindingDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_terminals_binding_desktops_async(self, request):
        """查询终端与桌面绑定配置列表

        查询终端与桌面绑定配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsResponse`
        """
        return self._list_terminals_binding_desktops_with_http_info(request)

    def _list_terminals_binding_desktops_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/terminals/binding-desktops',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTerminalsBindingDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_terminals_binding_desktops_config_async(self, request):
        """查询终端与桌面绑定的开关配置信息

        查询终端与桌面绑定的开关配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTerminalsBindingDesktopsConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsConfigResponse`
        """
        return self._list_terminals_binding_desktops_config_with_http_info(request)

    def _list_terminals_binding_desktops_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/terminals/binding-desktops/config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTerminalsBindingDesktopsConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_terminals_binding_desktops_async(self, request):
        """修改终端与桌面绑定配置

        修改终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsResponse`
        """
        return self._update_terminals_binding_desktops_with_http_info(request)

    def _update_terminals_binding_desktops_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/terminals/binding-desktops',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTerminalsBindingDesktopsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_terminals_binding_desktops_config_async(self, request):
        """设置终端与桌面绑定的开关配置

        设置终端与桌面绑定的开关配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTerminalsBindingDesktopsConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsConfigResponse`
        """
        return self._update_terminals_binding_desktops_config_with_http_info(request)

    def _update_terminals_binding_desktops_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/terminals/binding-desktops/config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTerminalsBindingDesktopsConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_users_async(self, request):
        """批量创建用户

        该接口用于批量创建用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateUsers
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchCreateUsersRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchCreateUsersResponse`
        """
        return self._batch_create_users_with_http_info(request)

    def _batch_create_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_otp_devices_async(self, request):
        """解绑OTP设备

        该接口用于解绑用户的OTP设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteOtpDevices
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteOtpDevicesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteOtpDevicesResponse`
        """
        return self._batch_delete_otp_devices_with_http_info(request)

    def _batch_delete_otp_devices_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/{user_id}/otp-devices',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteOtpDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_user_status_async(self, request):
        """操作用户

        该接口用于操作用户，包含三种操作：锁定、解锁和重置密码（重置密码建议使用/v2/{project_id}/users/{user_id}/random-password接口，在没有通知方式的情况下必须使用/v2/{project_id}/users/{user_id}/random-password接口）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeUserStatus
        :type request: :class:`huaweicloudsdkworkspace.v2.ChangeUserStatusRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ChangeUserStatusResponse`
        """
        return self._change_user_status_with_http_info(request)

    def _change_user_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/{user_id}/actions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeUserStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_desktop_user_async(self, request):
        """创建用户

        该接口用于创建桌面用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDesktopUser
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopUserRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopUserResponse`
        """
        return self._create_desktop_user_with_http_info(request)

    def _create_desktop_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDesktopUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_user_async(self, request):
        """删除指定用户

        删除指定的桌面用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteUserResponse`
        """
        return self._delete_user_with_http_info(request)

    def _delete_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_otp_devices_by_user_id_async(self, request):
        """查询OTP设备

        该接口用于查询相应用户下面的OTP设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOtpDevicesByUserId
        :type request: :class:`huaweicloudsdkworkspace.v2.ListOtpDevicesByUserIdRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListOtpDevicesByUserIdResponse`
        """
        return self._list_otp_devices_by_user_id_with_http_info(request)

    def _list_otp_devices_by_user_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/{user_id}/otp-devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOtpDevicesByUserIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_detail_async(self, request):
        """查询用户详情信息

        该接口用于查询指定的桌面用户详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserDetailResponse`
        """
        return self._list_user_detail_with_http_info(request)

    def _list_user_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/{user_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUserDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_users_async(self, request):
        """查询用户列表

        该接口用于查询桌面用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsersResponse`
        """
        return self._list_users_with_http_info(request)

    def _list_users_with_http_info(self, request):
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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_random_password_async(self, request):
        """给用户重置随机密码

        该接口用于给用户重置一个密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetRandomPassword
        :type request: :class:`huaweicloudsdkworkspace.v2.ResetRandomPasswordRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResetRandomPasswordResponse`
        """
        return self._reset_random_password_with_http_info(request)

    def _reset_random_password_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/{user_id}/random-password',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetRandomPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_info_async(self, request):
        """修改用户信息

        该接口用于修改桌面用户信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateUserInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateUserInfoResponse`
        """
        return self._update_user_info_with_http_info(request)

    def _update_user_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_volumes_async(self, request):
        """增加桌面磁盘

        增加桌面磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.AddVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddVolumesResponse`
        """
        return self._add_volumes_with_http_info(request)

    def _add_volumes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/volumes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddVolumesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_desktop_volumes_async(self, request):
        """删除桌面数据盘

        删除桌面数据盘，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDesktopVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopVolumesResponse`
        """
        return self._delete_desktop_volumes_with_http_info(request)

    def _delete_desktop_volumes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/desktops/{desktop_id}/volumes/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDesktopVolumesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def expand_volumes_async(self, request):
        """扩容桌面磁盘

        扩容桌面磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.ExpandVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExpandVolumesResponse`
        """
        return self._expand_volumes_with_http_info(request)

    def _expand_volumes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/volumes/expand',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandVolumesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def apply_workspace_async(self, request):
        """开通云办公服务

        该接口用于开通云办公服务。
        
        作为异步接口，调用成功说明云办公服务后台收到了开通请求，但服务是否开通成功需要通过任务查询接口(GET /v2/{project_id}/workspace-sub-jobs)查询该任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.ApplyWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyWorkspaceResponse`
        """
        return self._apply_workspace_with_http_info(request)

    def _apply_workspace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/workspaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyWorkspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_workspace_async(self, request):
        """注销云办公服务

        该接口用于注销云办公服务。注销前请确保当前用户下的云桌面已经删除，注销后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.CancelWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CancelWorkspaceResponse`
        """
        return self._cancel_workspace_with_http_info(request)

    def _cancel_workspace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/workspaces',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelWorkspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workspaces_async(self, request):
        """查询云办公服务详情

        该接口用于查询云办公服务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkspaces
        :type request: :class:`huaweicloudsdkworkspace.v2.ListWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListWorkspacesResponse`
        """
        return self._list_workspaces_with_http_info(request)

    def _list_workspaces_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/workspaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkspacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_workspace_lock_async(self, request):
        """查询云办公服务是否被锁定

        查询云办公服务是否被锁定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkspaceLock
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowWorkspaceLockRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowWorkspaceLockResponse`
        """
        return self._show_workspace_lock_with_http_info(request)

    def _show_workspace_lock_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/workspaces/lock-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkspaceLockResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def unlock_workspace_async(self, request):
        """解除云办公服务锁定状态

        该接口目前支持解除云办公服务锁定状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnlockWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.UnlockWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UnlockWorkspaceResponse`
        """
        return self._unlock_workspace_with_http_info(request)

    def _unlock_workspace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/workspaces/lock-status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UnlockWorkspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_workspace_async(self, request):
        """修改云办公服务属性

        该接口目前支持修改云办公服务属性。单次请求仅支持修改一种属性类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateWorkspaceResponse`
        """
        return self._update_workspace_with_http_info(request)

    def _update_workspace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/workspaces',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWorkspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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
