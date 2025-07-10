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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkworkspace'")


class WorkspaceClient(Client):
    def __init__(self):
        super(WorkspaceClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkworkspace.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "WorkspaceClient":
                raise TypeError("client type error, support client type is WorkspaceClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_access_address_backup_config(self, request):
        r"""获取云办公服务接入地址备份配置

        该接口用于获取云办公服务接入地址备份配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessAddressBackupConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAccessAddressBackupConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAccessAddressBackupConfigResponse`
        """
        http_info = self._list_access_address_backup_config_http_info(request)
        return self._call_api(**http_info)

    def list_access_address_backup_config_invoker(self, request):
        http_info = self._list_access_address_backup_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_access_address_backup_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/access-config/address-backup",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessAddressBackupConfigResponse"
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

    def update_access_address_backup_config(self, request):
        r"""修改云办公服务接入地址备份配置

        该接口用于修改云办公服务接入地址备份配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccessAddressBackupConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAccessAddressBackupConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAccessAddressBackupConfigResponse`
        """
        http_info = self._update_access_address_backup_config_http_info(request)
        return self._call_api(**http_info)

    def update_access_address_backup_config_invoker(self, request):
        http_info = self._update_access_address_backup_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_access_address_backup_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/access-config/address-backup",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccessAddressBackupConfigResponse"
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

    def batch_delete_access_policies(self, request):
        r"""删除接入策略

        该接口用于删除指定接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAccessPolicies
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteAccessPoliciesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteAccessPoliciesResponse`
        """
        http_info = self._batch_delete_access_policies_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_access_policies_invoker(self, request):
        http_info = self._batch_delete_access_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_access_policies_http_info(cls, request):
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

    def create_access_policy(self, request):
        r"""创建接入策略

        该接口用于创建接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccessPolicy
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateAccessPolicyResponse`
        """
        http_info = self._create_access_policy_http_info(request)
        return self._call_api(**http_info)

    def create_access_policy_invoker(self, request):
        http_info = self._create_access_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_access_policy_http_info(cls, request):
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

    def list_access_policies(self, request):
        r"""查询接入策略

        该接口用于查询接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessPolicies
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAccessPoliciesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAccessPoliciesResponse`
        """
        http_info = self._list_access_policies_http_info(request)
        return self._call_api(**http_info)

    def list_access_policies_invoker(self, request):
        http_info = self._list_access_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_access_policies_http_info(cls, request):
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
        if 'access_control_type' in local_var_params:
            query_params.append(('access_control_type', local_var_params['access_control_type']))
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

    def list_access_policy_objects(self, request):
        r"""查询指定接入策略的应用对象

        该接口用于查询指定接入策略的应用对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessPolicyObjects
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAccessPolicyObjectsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAccessPolicyObjectsResponse`
        """
        http_info = self._list_access_policy_objects_http_info(request)
        return self._call_api(**http_info)

    def list_access_policy_objects_invoker(self, request):
        http_info = self._list_access_policy_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_access_policy_objects_http_info(cls, request):
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

    def update_access_policy(self, request):
        r"""更新指定接入策略

        该接口用于更新指定接入策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccessPolicy
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyResponse`
        """
        http_info = self._update_access_policy_http_info(request)
        return self._call_api(**http_info)

    def update_access_policy_invoker(self, request):
        http_info = self._update_access_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_access_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/access-policy/{access_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccessPolicyResponse"
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

    def update_access_policy_objects(self, request):
        r"""更新指定接入策略的应用对象

        该接口用于更新指定接入策略的应用对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccessPolicyObjects
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyObjectsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyObjectsResponse`
        """
        http_info = self._update_access_policy_objects_http_info(request)
        return self._call_api(**http_info)

    def update_access_policy_objects_invoker(self, request):
        http_info = self._update_access_policy_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_access_policy_objects_http_info(cls, request):
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

    def create_agencies(self, request):
        r"""开通委托功能

        开通委托功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAgencies
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateAgenciesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateAgenciesResponse`
        """
        http_info = self._create_agencies_http_info(request)
        return self._call_api(**http_info)

    def create_agencies_invoker(self, request):
        http_info = self._create_agencies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_agencies_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgenciesResponse"
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

    def list_agencies(self, request):
        r"""查询委托功能

        查询委托功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgencies
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAgenciesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAgenciesResponse`
        """
        http_info = self._list_agencies_http_info(request)
        return self._call_api(**http_info)

    def list_agencies_invoker(self, request):
        http_info = self._list_agencies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_agencies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgenciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_alarm_statistics(self, request):
        r"""查询告警统计

        返回各级别告警数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmStatistics
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAlarmStatisticsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAlarmStatisticsResponse`
        """
        http_info = self._list_alarm_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_statistics_invoker(self, request):
        http_info = self._list_alarm_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmStatisticsResponse"
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

    def list_alarms(self, request):
        r"""查询告警列表

        从ces查询告警列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarms
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAlarmsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAlarmsResponse`
        """
        http_info = self._list_alarms_http_info(request)
        return self._call_api(**http_info)

    def list_alarms_invoker(self, request):
        http_info = self._list_alarms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarms_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
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

    def batch_delete_apps(self, request):
        r"""批量删除应用

        批量删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteApps
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteAppsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteAppsResponse`
        """
        http_info = self._batch_delete_apps_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_apps_invoker(self, request):
        http_info = self._batch_delete_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_apps_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/apps/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAppsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_jobs(self, request):
        r"""批量删除job

        批量删除job。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteJobs
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteJobsResponse`
        """
        http_info = self._batch_delete_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_jobs_invoker(self, request):
        http_info = self._batch_delete_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/jobs/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteJobsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_disable_apps(self, request):
        r"""批量设置不可见

        批量设置不可见。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDisableApps
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDisableAppsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDisableAppsResponse`
        """
        http_info = self._batch_disable_apps_http_info(request)
        return self._call_api(**http_info)

    def batch_disable_apps_invoker(self, request):
        http_info = self._batch_disable_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_disable_apps_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/apps/actions/batch-disable",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisableAppsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_enable_apps(self, request):
        r"""批量设置可见

        批量设置可见。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchEnableApps
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchEnableAppsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchEnableAppsResponse`
        """
        http_info = self._batch_enable_apps_http_info(request)
        return self._call_api(**http_info)

    def batch_enable_apps_invoker(self, request):
        http_info = self._batch_enable_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_enable_apps_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/apps/actions/batch-enable",
            "request_type": request.__class__.__name__,
            "response_type": "BatchEnableAppsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_install_apps(self, request):
        r"""批量自动安装安装应用

        批量自动安装安装应用 (应用需支持静默安装或者解压安装)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchInstallApps
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchInstallAppsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchInstallAppsResponse`
        """
        http_info = self._batch_install_apps_http_info(request)
        return self._call_api(**http_info)

    def batch_install_apps_invoker(self, request):
        http_info = self._batch_install_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_install_apps_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/apps/actions/batch-auto-install",
            "request_type": request.__class__.__name__,
            "response_type": "BatchInstallAppsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_update_app_authorizations(self, request):
        r"""批量设置应用授权

        批量设置应用授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateAppAuthorizations
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchUpdateAppAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchUpdateAppAuthorizationsResponse`
        """
        http_info = self._batch_update_app_authorizations_http_info(request)
        return self._call_api(**http_info)

    def batch_update_app_authorizations_invoker(self, request):
        http_info = self._batch_update_app_authorizations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_app_authorizations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/apps/actions/batch-assign-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateAppAuthorizationsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_and_authorize_bucket(self, request):
        r"""添加并授权默认桶

        添加并授权默认桶,桶不存在时会自动创建OBS桶。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAndAuthorizeBucket
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateAndAuthorizeBucketRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateAndAuthorizeBucketResponse`
        """
        http_info = self._create_and_authorize_bucket_http_info(request)
        return self._call_api(**http_info)

    def create_and_authorize_bucket_invoker(self, request):
        http_info = self._create_and_authorize_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_and_authorize_bucket_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAndAuthorizeBucketResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_bucket_credential(self, request):
        r"""生成访问凭证信息

        生成桶凭证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBucketCredential
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateBucketCredentialRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateBucketCredentialResponse`
        """
        http_info = self._create_bucket_credential_http_info(request)
        return self._call_api(**http_info)

    def create_bucket_credential_invoker(self, request):
        http_info = self._create_bucket_credential_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_bucket_credential_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/buckets/actions/create-credential",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBucketCredentialResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app(self, request):
        r"""删除应用

        删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteAppResponse`
        """
        http_info = self._delete_app_http_info(request)
        return self._call_api(**http_info)

    def delete_app_invoker(self, request):
        http_info = self._delete_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_app_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/app-center/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'reserve_obs_file' in local_var_params:
            query_params.append(('reserve_obs_file', local_var_params['reserve_obs_file']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def install_app(self, request):
        r"""自动安装应用

        自动安装应用(应用需支持静默安装或者解压安装)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InstallApp
        :type request: :class:`huaweicloudsdkworkspace.v2.InstallAppRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.InstallAppResponse`
        """
        http_info = self._install_app_http_info(request)
        return self._call_api(**http_info)

    def install_app_invoker(self, request):
        http_info = self._install_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _install_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/apps/{app_id}/actions/auto-install",
            "request_type": request.__class__.__name__,
            "response_type": "InstallAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_authorizations(self, request):
        r"""查询应用授权信息

        查询应用授权信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppAuthorizations
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAppAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAppAuthorizationsResponse`
        """
        http_info = self._list_app_authorizations_http_info(request)
        return self._call_api(**http_info)

    def list_app_authorizations_invoker(self, request):
        http_info = self._list_app_authorizations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_authorizations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-center/apps/{app_id}/authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppAuthorizationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'target_type' in local_var_params:
            query_params.append(('target_type', local_var_params['target_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_catalogs(self, request):
        r"""查询应用分类信息

        查询应用分类信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppCatalogs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAppCatalogsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAppCatalogsResponse`
        """
        http_info = self._list_app_catalogs_http_info(request)
        return self._call_api(**http_info)

    def list_app_catalogs_invoker(self, request):
        http_info = self._list_app_catalogs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_catalogs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-center/app-catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppCatalogsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apps(self, request):
        r"""按照名称分页查询应用

        按照名称分页查询应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAppsResponse`
        """
        http_info = self._list_apps_http_info(request)
        return self._call_api(**http_info)

    def list_apps_invoker(self, request):
        http_info = self._list_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apps_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-center/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_jobs(self, request):
        r"""查询应用安装job信息

        查询应用安装job信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-center/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
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
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'target' in local_var_params:
            query_params.append(('target', local_var_params['target']))
        if 'job_status' in local_var_params:
            query_params.append(('job_status', local_var_params['job_status']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def retry_jobs(self, request):
        r"""重试失败job

        重试指定失败job(仅支持失败job重试，其他类型job重试会响应错误)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryJobs
        :type request: :class:`huaweicloudsdkworkspace.v2.RetryJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.RetryJobsResponse`
        """
        http_info = self._retry_jobs_http_info(request)
        return self._call_api(**http_info)

    def retry_jobs_invoker(self, request):
        http_info = self._retry_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/jobs/actions/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryJobsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_app_authorizations(self, request):
        r"""设置应用授权

        设置应用授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAppAuthorizations
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAppAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAppAuthorizationsResponse`
        """
        http_info = self._update_app_authorizations_http_info(request)
        return self._call_api(**http_info)

    def update_app_authorizations_invoker(self, request):
        http_info = self._update_app_authorizations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_app_authorizations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/apps/{app_id}/actions/assign-authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppAuthorizationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_uploaded_app(self, request):
        r"""修改应用

        修改应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUploadedApp
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateUploadedAppRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateUploadedAppResponse`
        """
        http_info = self._update_uploaded_app_http_info(request)
        return self._call_api(**http_info)

    def update_uploaded_app_invoker(self, request):
        http_info = self._update_uploaded_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_uploaded_app_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-center/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUploadedAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upload_app(self, request):
        r"""添加应用

        添加应用应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadApp
        :type request: :class:`huaweicloudsdkworkspace.v2.UploadAppRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UploadAppResponse`
        """
        http_info = self._upload_app_http_info(request)
        return self._call_api(**http_info)

    def upload_app_invoker(self, request):
        http_info = self._upload_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/apps",
            "request_type": request.__class__.__name__,
            "response_type": "UploadAppResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_restricted_rule(self, request):
        r"""增加管控规则

        增加管控规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRestrictedRule
        :type request: :class:`huaweicloudsdkworkspace.v2.AddRestrictedRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddRestrictedRuleResponse`
        """
        http_info = self._add_restricted_rule_http_info(request)
        return self._call_api(**http_info)

    def add_restricted_rule_invoker(self, request):
        http_info = self._add_restricted_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_restricted_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/app-restricted-rules",
            "request_type": request.__class__.__name__,
            "response_type": "AddRestrictedRuleResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_app_rules(self, request):
        r"""批量删除规则

        批量删除规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAppRules
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteAppRulesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteAppRulesResponse`
        """
        http_info = self._batch_delete_app_rules_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_app_rules_invoker(self, request):
        http_info = self._batch_delete_app_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_app_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/app-rules/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAppRulesResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_app_rule(self, request):
        r"""创建应用规则

        创建应用规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAppRule
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateAppRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateAppRuleResponse`
        """
        http_info = self._create_app_rule_http_info(request)
        return self._call_api(**http_info)

    def create_app_rule_invoker(self, request):
        http_info = self._create_app_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/app-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppRuleResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_rule(self, request):
        r"""删除应用规则

        删除应用规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAppRule
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteAppRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteAppRuleResponse`
        """
        http_info = self._delete_app_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_app_rule_invoker(self, request):
        http_info = self._delete_app_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_app_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/app-center/app-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_restricted_rule(self, request):
        r"""批量删除管控规则

        批量删除管控规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRestrictedRule
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteRestrictedRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteRestrictedRuleResponse`
        """
        http_info = self._delete_restricted_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_restricted_rule_invoker(self, request):
        http_info = self._delete_restricted_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_restricted_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/app-restricted-rules/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRestrictedRuleResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_rule_restriction(self, request):
        r"""禁用规则管控

        禁用规则管控。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableRuleRestriction
        :type request: :class:`huaweicloudsdkworkspace.v2.DisableRuleRestrictionRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DisableRuleRestrictionResponse`
        """
        http_info = self._disable_rule_restriction_http_info(request)
        return self._call_api(**http_info)

    def disable_rule_restriction_invoker(self, request):
        http_info = self._disable_rule_restriction_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_rule_restriction_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/app-rules/actions/disable-rule-restriction",
            "request_type": request.__class__.__name__,
            "response_type": "DisableRuleRestrictionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_rule_restriction(self, request):
        r"""启用规则管控

        启用规则管控。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableRuleRestriction
        :type request: :class:`huaweicloudsdkworkspace.v2.EnableRuleRestrictionRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.EnableRuleRestrictionResponse`
        """
        http_info = self._enable_rule_restriction_http_info(request)
        return self._call_api(**http_info)

    def enable_rule_restriction_invoker(self, request):
        http_info = self._enable_rule_restriction_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_rule_restriction_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/app-rules/actions/enable-rule-restriction",
            "request_type": request.__class__.__name__,
            "response_type": "EnableRuleRestrictionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_rule(self, request):
        r"""查询应用规则

        查询应用规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppRule
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAppRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAppRuleResponse`
        """
        http_info = self._list_app_rule_http_info(request)
        return self._call_api(**http_info)

    def list_app_rule_invoker(self, request):
        http_info = self._list_app_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-center/app-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppRuleResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_restricted_rule(self, request):
        r"""查询管控规则列表

        查询管控规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestrictedRule
        :type request: :class:`huaweicloudsdkworkspace.v2.ListRestrictedRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListRestrictedRuleResponse`
        """
        http_info = self._list_restricted_rule_http_info(request)
        return self._call_api(**http_info)

    def list_restricted_rule_invoker(self, request):
        http_info = self._list_restricted_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_restricted_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-center/app-restricted-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRestrictedRuleResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_rule_restriction(self, request):
        r"""设置管控规则

        设置管控规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRuleRestriction
        :type request: :class:`huaweicloudsdkworkspace.v2.SetRuleRestrictionRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.SetRuleRestrictionResponse`
        """
        http_info = self._set_rule_restriction_http_info(request)
        return self._call_api(**http_info)

    def set_rule_restriction_invoker(self, request):
        http_info = self._set_rule_restriction_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_rule_restriction_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-center/app-rules/actions/set-rule-restriction",
            "request_type": request.__class__.__name__,
            "response_type": "SetRuleRestrictionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_rule_restriction(self, request):
        r"""查询管控规则

        查询管控规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRuleRestriction
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowRuleRestrictionRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowRuleRestrictionResponse`
        """
        http_info = self._show_rule_restriction_http_info(request)
        return self._call_api(**http_info)

    def show_rule_restriction_invoker(self, request):
        http_info = self._show_rule_restriction_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_rule_restriction_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-center/app-rules/actions/get-rule-restriction",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRuleRestrictionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_app_rule(self, request):
        r"""修改应用规则

        修改应用规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAppRule
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAppRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAppRuleResponse`
        """
        http_info = self._update_app_rule_http_info(request)
        return self._call_api(**http_info)

    def update_app_rule_invoker(self, request):
        http_info = self._update_app_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_app_rule_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-center/app-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_assist_auth_config(self, request):
        r"""查询辅助认证配置

        查询辅助认证的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssistAuthConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowAssistAuthConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowAssistAuthConfigResponse`
        """
        http_info = self._show_assist_auth_config_http_info(request)
        return self._call_api(**http_info)

    def show_assist_auth_config_invoker(self, request):
        http_info = self._show_assist_auth_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_assist_auth_config_http_info(cls, request):
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

    def show_auth_config(self, request):
        r"""查询认证登录方式

        查询认证登录方式配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuthConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowAuthConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowAuthConfigResponse`
        """
        http_info = self._show_auth_config_http_info(request)
        return self._call_api(**http_info)

    def show_auth_config_invoker(self, request):
        http_info = self._show_auth_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auth_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/auth-config/method-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuthConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'auth_type' in local_var_params:
            query_params.append(('auth_type', local_var_params['auth_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_assist_auth_method_config(self, request):
        r"""更新辅助认证策略配置

        更新辅助认证策略配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAssistAuthMethodConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAssistAuthMethodConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAssistAuthMethodConfigResponse`
        """
        http_info = self._update_assist_auth_method_config_http_info(request)
        return self._call_api(**http_info)

    def update_assist_auth_method_config_invoker(self, request):
        http_info = self._update_assist_auth_method_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_assist_auth_method_config_http_info(cls, request):
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

    def update_auth_method_config(self, request):
        r"""更新认证策略配置

        更新认证策略配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuthMethodConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAuthMethodConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAuthMethodConfigResponse`
        """
        http_info = self._update_auth_method_config_http_info(request)
        return self._call_api(**http_info)

    def update_auth_method_config_invoker(self, request):
        http_info = self._update_auth_method_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_auth_method_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/auth-config/method-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuthMethodConfigResponse"
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

    def list_availability_zones(self, request):
        r"""查询可用分区列表

        该接口用于查询云桌面支持的可用分区列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAvailabilityZonesResponse`
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

    def list_azs(self, request):
        r"""查询可用分区列表概要

        该接口用于查询云桌面支持的可用分区列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAzs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAzsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAzsResponse`
        """
        http_info = self._list_azs_http_info(request)
        return self._call_api(**http_info)

    def list_azs_invoker(self, request):
        http_info = self._list_azs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_azs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/availability-zones/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ListAzsResponse"
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

    def show_az_details(self, request):
        r"""查询可用分区详情

        该接口用于查询云桌面支持的可用分区列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAzDetails
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowAzDetailsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowAzDetailsResponse`
        """
        http_info = self._show_az_details_http_info(request)
        return self._call_api(**http_info)

    def show_az_details_invoker(self, request):
        http_info = self._show_az_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_az_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/availability-zones/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAzDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_user_login_info_new(self, request):
        r"""导出连接记录

        该接口用于导出连接记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportUserLoginInfoNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ExportUserLoginInfoNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExportUserLoginInfoNewResponse`
        """
        http_info = self._export_user_login_info_new_http_info(request)
        return self._call_api(**http_info)

    def export_user_login_info_new_invoker(self, request):
        http_info = self._export_user_login_info_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_user_login_info_new_http_info(cls, request):
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

    def list_history_online_info_new(self, request):
        r"""查询登录人数

        该接口用于查询登录人数，注意查询参数不可全空。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistoryOnlineInfoNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ListHistoryOnlineInfoNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListHistoryOnlineInfoNewResponse`
        """
        http_info = self._list_history_online_info_new_http_info(request)
        return self._call_api(**http_info)

    def list_history_online_info_new_invoker(self, request):
        http_info = self._list_history_online_info_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_online_info_new_http_info(cls, request):
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

    def list_instances_status(self, request):
        r"""查询桌面登录状态

        该接口用于查询桌面登录状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesStatus
        :type request: :class:`huaweicloudsdkworkspace.v2.ListInstancesStatusRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListInstancesStatusResponse`
        """
        http_info = self._list_instances_status_http_info(request)
        return self._call_api(**http_info)

    def list_instances_status_invoker(self, request):
        http_info = self._list_instances_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/connections/status",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesStatusResponse"
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

    def list_login_records_new(self, request):
        r"""查询登录信息

        该接口用于查询登录信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLoginRecordsNew
        :type request: :class:`huaweicloudsdkworkspace.v2.ListLoginRecordsNewRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListLoginRecordsNewResponse`
        """
        http_info = self._list_login_records_new_http_info(request)
        return self._call_api(**http_info)

    def list_login_records_new_invoker(self, request):
        http_info = self._list_login_records_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_login_records_new_http_info(cls, request):
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'min_network_rtt' in local_var_params:
            query_params.append(('min_network_rtt', local_var_params['min_network_rtt']))
        if 'max_network_rtt' in local_var_params:
            query_params.append(('max_network_rtt', local_var_params['max_network_rtt']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def attach_instances(self, request):
        r"""分配用户

        将桌面分配给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachInstances
        :type request: :class:`huaweicloudsdkworkspace.v2.AttachInstancesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AttachInstancesResponse`
        """
        http_info = self._attach_instances_http_info(request)
        return self._call_api(**http_info)

    def attach_instances_invoker(self, request):
        http_info = self._attach_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/attach",
            "request_type": request.__class__.__name__,
            "response_type": "AttachInstancesResponse"
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

    def batch_associate_instances(self, request):
        r"""预批量分配用户

        预批量将桌面分配给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAssociateInstances
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchAssociateInstancesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchAssociateInstancesResponse`
        """
        http_info = self._batch_associate_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_instances_invoker(self, request):
        http_info = self._batch_associate_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_associate_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/pre-batch-attach",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAssociateInstancesResponse"
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

    def batch_attach_instances(self, request):
        r"""批量分配用户

        批量分配桌面给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAttachInstances
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchAttachInstancesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchAttachInstancesResponse`
        """
        http_info = self._batch_attach_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_attach_instances_invoker(self, request):
        http_info = self._batch_attach_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_attach_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/batch-attach",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAttachInstancesResponse"
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

    def batch_change_desktop_network(self, request):
        r"""批量切换桌面网络

        批量切换桌面vpc、子网、ip、安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchChangeDesktopNetwork
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchChangeDesktopNetworkRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchChangeDesktopNetworkResponse`
        """
        http_info = self._batch_change_desktop_network_http_info(request)
        return self._call_api(**http_info)

    def batch_change_desktop_network_invoker(self, request):
        http_info = self._batch_change_desktop_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_change_desktop_network_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/networks/batch-change",
            "request_type": request.__class__.__name__,
            "response_type": "BatchChangeDesktopNetworkResponse"
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

    def batch_delete_desktops(self, request):
        r"""批量删除桌面

        批量删除桌面，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsResponse`
        """
        http_info = self._batch_delete_desktops_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_desktops_invoker(self, request):
        http_info = self._batch_delete_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_desktops_http_info(cls, request):
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

    def batch_detach_instances(self, request):
        r"""批量解绑用户

        批量将桌面和用户解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDetachInstances
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDetachInstancesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDetachInstancesResponse`
        """
        http_info = self._batch_detach_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_detach_instances_invoker(self, request):
        http_info = self._batch_detach_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_detach_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/batch-detach",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDetachInstancesResponse"
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

    def batch_install_agent(self, request):
        r"""安装agent

        批量为桌面安装agent。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchInstallAgent
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchInstallAgentRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchInstallAgentResponse`
        """
        http_info = self._batch_install_agent_http_info(request)
        return self._call_api(**http_info)

    def batch_install_agent_invoker(self, request):
        http_info = self._batch_install_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_install_agent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/agents",
            "request_type": request.__class__.__name__,
            "response_type": "BatchInstallAgentResponse"
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

    def batch_logoff_desktops(self, request):
        r"""批量注销桌面

        批量注销桌面。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchLogoffDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchLogoffDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchLogoffDesktopsResponse`
        """
        http_info = self._batch_logoff_desktops_http_info(request)
        return self._call_api(**http_info)

    def batch_logoff_desktops_invoker(self, request):
        http_info = self._batch_logoff_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_logoff_desktops_http_info(cls, request):
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

    def batch_rebuild_desktops_system_disk(self, request):
        r"""重建桌面

        批量重建桌面系统盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRebuildDesktopsSystemDisk
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchRebuildDesktopsSystemDiskRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchRebuildDesktopsSystemDiskResponse`
        """
        http_info = self._batch_rebuild_desktops_system_disk_http_info(request)
        return self._call_api(**http_info)

    def batch_rebuild_desktops_system_disk_invoker(self, request):
        http_info = self._batch_rebuild_desktops_system_disk_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_rebuild_desktops_system_disk_http_info(cls, request):
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

    def batch_run_desktops(self, request):
        r"""操作桌面

        批量操作桌面，用于批量开机、关机、休眠和重启。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRunDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchRunDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchRunDesktopsResponse`
        """
        http_info = self._batch_run_desktops_http_info(request)
        return self._call_api(**http_info)

    def batch_run_desktops_invoker(self, request):
        http_info = self._batch_run_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_run_desktops_http_info(cls, request):
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

    def cancel_remote_assistance(self, request):
        r"""取消远程协助

        取消远程协助。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelRemoteAssistance
        :type request: :class:`huaweicloudsdkworkspace.v2.CancelRemoteAssistanceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CancelRemoteAssistanceResponse`
        """
        http_info = self._cancel_remote_assistance_http_info(request)
        return self._call_api(**http_info)

    def cancel_remote_assistance_invoker(self, request):
        http_info = self._cancel_remote_assistance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_remote_assistance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/remote-assistance",
            "request_type": request.__class__.__name__,
            "response_type": "CancelRemoteAssistanceResponse"
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

    def change_desktop_network(self, request):
        r"""切换桌面网络

        切换桌面vpc、子网、ip、安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeDesktopNetwork
        :type request: :class:`huaweicloudsdkworkspace.v2.ChangeDesktopNetworkRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ChangeDesktopNetworkResponse`
        """
        http_info = self._change_desktop_network_http_info(request)
        return self._call_api(**http_info)

    def change_desktop_network_invoker(self, request):
        http_info = self._change_desktop_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_desktop_network_http_info(cls, request):
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

    def change_desktop_to_image(self, request):
        r"""桌面转镜像

        桌面转镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeDesktopToImage
        :type request: :class:`huaweicloudsdkworkspace.v2.ChangeDesktopToImageRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ChangeDesktopToImageResponse`
        """
        http_info = self._change_desktop_to_image_http_info(request)
        return self._call_api(**http_info)

    def change_desktop_to_image_invoker(self, request):
        http_info = self._change_desktop_to_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_desktop_to_image_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/desktop-to-image",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeDesktopToImageResponse"
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

    def change_user_privilege_group(self, request):
        r"""批量修改用户权限组

        批量修改用户权限组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeUserPrivilegeGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.ChangeUserPrivilegeGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ChangeUserPrivilegeGroupResponse`
        """
        http_info = self._change_user_privilege_group_http_info(request)
        return self._call_api(**http_info)

    def change_user_privilege_group_invoker(self, request):
        http_info = self._change_user_privilege_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_user_privilege_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/change-user-privilege-group",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeUserPrivilegeGroupResponse"
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

    def create_desktop(self, request):
        r"""创建桌面

        创建桌面，并将此桌面分配给用户，当桌面创建成功后用户可以登录使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopResponse`
        """
        http_info = self._create_desktop_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_invoker(self, request):
        http_info = self._create_desktop_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_desktop_http_info(cls, request):
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

    def create_remote_assistance(self, request):
        r"""创建远程协助

        创建远程协助。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRemoteAssistance
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateRemoteAssistanceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateRemoteAssistanceResponse`
        """
        http_info = self._create_remote_assistance_http_info(request)
        return self._call_api(**http_info)

    def create_remote_assistance_invoker(self, request):
        http_info = self._create_remote_assistance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_remote_assistance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/remote-assistance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRemoteAssistanceResponse"
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

    def delete_desktop(self, request):
        r"""删除单个桌面

        删除单个桌面，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopResponse`
        """
        http_info = self._delete_desktop_http_info(request)
        return self._call_api(**http_info)

    def delete_desktop_invoker(self, request):
        http_info = self._delete_desktop_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_desktop_http_info(cls, request):
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

    def detach_instances(self, request):
        r"""解绑用户

        将桌面和用户解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachInstances
        :type request: :class:`huaweicloudsdkworkspace.v2.DetachInstancesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DetachInstancesResponse`
        """
        http_info = self._detach_instances_http_info(request)
        return self._call_api(**http_info)

    def detach_instances_invoker(self, request):
        http_info = self._detach_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/detach",
            "request_type": request.__class__.__name__,
            "response_type": "DetachInstancesResponse"
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

    def list_agents_install_condition(self, request):
        r"""查询桌面安装agent详情

        展示桌面安装agent详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgentsInstallCondition
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAgentsInstallConditionRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAgentsInstallConditionResponse`
        """
        http_info = self._list_agents_install_condition_http_info(request)
        return self._call_api(**http_info)

    def list_agents_install_condition_invoker(self, request):
        http_info = self._list_agents_install_condition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_agents_install_condition_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentsInstallConditionResponse"
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
        if 'is_installed' in local_var_params:
            query_params.append(('is_installed', local_var_params['is_installed']))
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

    def list_desktop_actions(self, request):
        r"""查询桌面开关机信息

        获取桌面开关机信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopActions
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopActionsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopActionsResponse`
        """
        http_info = self._list_desktop_actions_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_actions_invoker(self, request):
        http_info = self._list_desktop_actions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktop_actions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopActionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

        query_params = []
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

    def list_desktops(self, request):
        r"""查询桌面列表

        该接口用于查询桌面虚拟机列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsResponse`
        """
        http_info = self._list_desktops_http_info(request)
        return self._call_api(**http_info)

    def list_desktops_invoker(self, request):
        http_info = self._list_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktops_http_info(cls, request):
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
            collection_formats['user_name'] = 'csv'
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
        if 'is_share_desktop' in local_var_params:
            query_params.append(('is_share_desktop', local_var_params['is_share_desktop']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'desktop_id' in local_var_params:
            query_params.append(('desktop_id', local_var_params['desktop_id']))
            collection_formats['desktop_id'] = 'csv'
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_desktops_connect_status(self, request):
        r"""查询桌面连接状态列表

        查询桌面连接状态列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopsConnectStatus
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsConnectStatusRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsConnectStatusResponse`
        """
        http_info = self._list_desktops_connect_status_http_info(request)
        return self._call_api(**http_info)

    def list_desktops_connect_status_invoker(self, request):
        http_info = self._list_desktops_connect_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktops_connect_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/connect-desktops",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopsConnectStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_names' in local_var_params:
            query_params.append(('user_names', local_var_params['user_names']))
            collection_formats['user_names'] = 'csv'
        if 'connect_status' in local_var_params:
            query_params.append(('connect_status', local_var_params['connect_status']))
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

    def list_desktops_detail(self, request):
        r"""查询桌面详情列表

        查询桌面详情信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopsDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsDetailResponse`
        """
        http_info = self._list_desktops_detail_http_info(request)
        return self._call_api(**http_info)

    def list_desktops_detail_invoker(self, request):
        http_info = self._list_desktops_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktops_detail_http_info(cls, request):
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
        if 'is_share_desktop' in local_var_params:
            query_params.append(('is_share_desktop', local_var_params['is_share_desktop']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))
        if 'is_support_internet' in local_var_params:
            query_params.append(('is_support_internet', local_var_params['is_support_internet']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def register_domain(self, request):
        r"""重新加入AD域

        该接口用于Windows桌面重新加入AD域，一般用于解决桌面脱域的情况使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterDomain
        :type request: :class:`huaweicloudsdkworkspace.v2.RegisterDomainRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.RegisterDomainResponse`
        """
        http_info = self._register_domain_http_info(request)
        return self._call_api(**http_info)

    def register_domain_invoker(self, request):
        http_info = self._register_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_domain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/rejoin-domain",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterDomainResponse"
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

    def resize_desktop(self, request):
        r"""变更规格

        变更云桌面规格，只支持变更CPU和内存，不支持变更磁盘，不支持同规格互相变更。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopResponse`
        """
        http_info = self._resize_desktop_http_info(request)
        return self._call_api(**http_info)

    def resize_desktop_invoker(self, request):
        http_info = self._resize_desktop_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_desktop_http_info(cls, request):
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

    def send_notifications(self, request):
        r"""发送消息通知

        用于管理员向桌面发送消息通知。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendNotifications
        :type request: :class:`huaweicloudsdkworkspace.v2.SendNotificationsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.SendNotificationsResponse`
        """
        http_info = self._send_notifications_http_info(request)
        return self._call_api(**http_info)

    def send_notifications_invoker(self, request):
        http_info = self._send_notifications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_notifications_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "SendNotificationsResponse"
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

    def set_maintenance_mode(self, request):
        r"""批量设置桌面维护模式

        批量设置桌面管理员维护模式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetMaintenanceMode
        :type request: :class:`huaweicloudsdkworkspace.v2.SetMaintenanceModeRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.SetMaintenanceModeResponse`
        """
        http_info = self._set_maintenance_mode_http_info(request)
        return self._call_api(**http_info)

    def set_maintenance_mode_invoker(self, request):
        http_info = self._set_maintenance_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_maintenance_mode_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/desktops/maintenance-mode",
            "request_type": request.__class__.__name__,
            "response_type": "SetMaintenanceModeResponse"
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

    def show_desktop_detail(self, request):
        r"""查询单个桌面详情

        指定桌面Id查询详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDesktopDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopDetailResponse`
        """
        http_info = self._show_desktop_detail_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_detail_invoker(self, request):
        http_info = self._show_desktop_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_desktop_detail_http_info(cls, request):
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

    def show_desktop_monitor_data(self, request):
        r"""查询桌面监控信息

        该接口可获取某一计算机在一段时间段(范围：1小时到30天)的数据信息（例如CPU占用率、内存占用率、用户的在线时间段等），最长数据保存时间不能超过180天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDesktopMonitorData
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopMonitorDataRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopMonitorDataResponse`
        """
        http_info = self._show_desktop_monitor_data_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_monitor_data_invoker(self, request):
        http_info = self._show_desktop_monitor_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_desktop_monitor_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktop-monitor/{desktop_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDesktopMonitorDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_desktop_network(self, request):
        r"""查询桌面网络

        查询桌面vpc、子网、privateIp、EIP、安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDesktopNetwork
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopNetworkRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopNetworkResponse`
        """
        http_info = self._show_desktop_network_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_network_invoker(self, request):
        http_info = self._show_desktop_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_desktop_network_http_info(cls, request):
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

    def show_desktop_networks(self, request):
        r"""批量查询桌面网络

        查询桌面vpc、子网、privateIp、EIP、安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDesktopNetworks
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopNetworksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopNetworksResponse`
        """
        http_info = self._show_desktop_networks_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_networks_invoker(self, request):
        http_info = self._show_desktop_networks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_desktop_networks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/networks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDesktopNetworksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'desktop_ids' in local_var_params:
            query_params.append(('desktop_ids', local_var_params['desktop_ids']))
            collection_formats['desktop_ids'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_desktop_remote_assistance_info(self, request):
        r"""根据桌面id查询远程协助信息

        根据桌面id查询远程协助信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDesktopRemoteAssistanceInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopRemoteAssistanceInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopRemoteAssistanceInfoResponse`
        """
        http_info = self._show_desktop_remote_assistance_info_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_remote_assistance_info_invoker(self, request):
        http_info = self._show_desktop_remote_assistance_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_desktop_remote_assistance_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/remote-assistance",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDesktopRemoteAssistanceInfoResponse"
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

    def show_remote_console_address(self, request):
        r"""远程登录控制台

        用于直接获取远程登录控制台地址。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRemoteConsoleAddress
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowRemoteConsoleAddressRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowRemoteConsoleAddressResponse`
        """
        http_info = self._show_remote_console_address_http_info(request)
        return self._call_api(**http_info)

    def show_remote_console_address_invoker(self, request):
        http_info = self._show_remote_console_address_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_remote_console_address_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/remote-consoles",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRemoteConsoleAddressResponse"
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

    def show_sysprep_info(self, request):
        r"""查询sysprep版本信息

        查询sysprep版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSysprepInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowSysprepInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowSysprepInfoResponse`
        """
        http_info = self._show_sysprep_info_http_info(request)
        return self._call_api(**http_info)

    def show_sysprep_info_invoker(self, request):
        http_info = self._show_sysprep_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sysprep_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/sysprep",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSysprepInfoResponse"
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

    def update_desktop(self, request):
        r"""修改桌面属性

        修改桌面属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDesktop
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopResponse`
        """
        http_info = self._update_desktop_http_info(request)
        return self._call_api(**http_info)

    def update_desktop_invoker(self, request):
        http_info = self._update_desktop_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_desktop_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDesktopResponse"
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

    def update_desktop_sids(self, request):
        r"""更新桌面SID

        该接口用于桌面sid和WindowsAD中的SID不同时，更新桌面SID使其与AD中的SID保持一致，一般用于解决桌面脱域的情况使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDesktopSids
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopSidsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopSidsResponse`
        """
        http_info = self._update_desktop_sids_http_info(request)
        return self._call_api(**http_info)

    def update_desktop_sids_invoker(self, request):
        http_info = self._update_desktop_sids_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_desktop_sids_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/desktops/sids",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDesktopSidsResponse"
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

    def update_desktop_username(self, request):
        r"""AD场景支持桌面更换关联用户名

        AD场景支持桌面更换关联用户名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDesktopUsername
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopUsernameRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopUsernameResponse`
        """
        http_info = self._update_desktop_username_http_info(request)
        return self._call_api(**http_info)

    def update_desktop_username_invoker(self, request):
        http_info = self._update_desktop_username_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_desktop_username_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/desktops/change-username",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDesktopUsernameResponse"
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

    def batch_delete_desktop_name_policy(self, request):
        r"""批量删除桌面名称策略

        批量删除桌面名称策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteDesktopNamePolicy
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopNamePolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopNamePolicyResponse`
        """
        http_info = self._batch_delete_desktop_name_policy_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_desktop_name_policy_invoker(self, request):
        http_info = self._batch_delete_desktop_name_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_desktop_name_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-name-policies/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDesktopNamePolicyResponse"
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

    def create_desktop_name_policy(self, request):
        r"""创建桌面名称策略

        创建桌面名称策略，用于自动生成桌面名称，最多允许50个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDesktopNamePolicy
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopNamePolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopNamePolicyResponse`
        """
        http_info = self._create_desktop_name_policy_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_name_policy_invoker(self, request):
        http_info = self._create_desktop_name_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_desktop_name_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-name-policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDesktopNamePolicyResponse"
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

    def list_desktop_name_policy(self, request):
        r"""获取桌面名称策略

        获取桌面名称策略，用于自动生成桌面名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopNamePolicy
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopNamePolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopNamePolicyResponse`
        """
        http_info = self._list_desktop_name_policy_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_name_policy_invoker(self, request):
        http_info = self._list_desktop_name_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktop_name_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktop-name-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopNamePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_contain_user' in local_var_params:
            query_params.append(('is_contain_user', local_var_params['is_contain_user']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
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

    def update_desktop_name_policy(self, request):
        r"""更新桌面名称策略

        更新桌面名称策略，用于自动生成桌面名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDesktopNamePolicy
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopNamePolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopNamePolicyResponse`
        """
        http_info = self._update_desktop_name_policy_http_info(request)
        return self._call_api(**http_info)

    def update_desktop_name_policy_invoker(self, request):
        http_info = self._update_desktop_name_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_desktop_name_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/desktop-name-policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDesktopNamePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def add_desktop_pool_volumes(self, request):
        r"""桌面池批量添加磁盘

        桌面池批量添加磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDesktopPoolVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.AddDesktopPoolVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddDesktopPoolVolumesResponse`
        """
        http_info = self._add_desktop_pool_volumes_http_info(request)
        return self._call_api(**http_info)

    def add_desktop_pool_volumes_invoker(self, request):
        http_info = self._add_desktop_pool_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_desktop_pool_volumes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/volumes/batch-add",
            "request_type": request.__class__.__name__,
            "response_type": "AddDesktopPoolVolumesResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_desktop_pool(self, request):
        r"""创建桌面池

        创建桌面池，可将此桌面池分配给用户、用户组，用户登录时会绑定其中一个桌面。
        注:需通过开通委托功能接口先对云服务进行授权才可以使用该功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDesktopPool
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolResponse`
        """
        http_info = self._create_desktop_pool_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_pool_invoker(self, request):
        http_info = self._create_desktop_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_desktop_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDesktopPoolResponse"
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

    def create_desktop_pool_authorized_objects(self, request):
        r"""桌面池授权用户、用户组

        该接口用于桌面池授权用户、用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDesktopPoolAuthorizedObjects
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolAuthorizedObjectsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolAuthorizedObjectsResponse`
        """
        http_info = self._create_desktop_pool_authorized_objects_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_pool_authorized_objects_invoker(self, request):
        http_info = self._create_desktop_pool_authorized_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_desktop_pool_authorized_objects_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDesktopPoolAuthorizedObjectsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_desktop_pool(self, request):
        r"""删除桌面池

        当桌面池内无桌面时可删除桌面池，桌面池删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDesktopPool
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopPoolRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopPoolResponse`
        """
        http_info = self._delete_desktop_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_desktop_pool_invoker(self, request):
        http_info = self._delete_desktop_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_desktop_pool_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDesktopPoolResponse"
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

    def delete_desktop_pool_volumes(self, request):
        r"""桌面池批量删除磁盘

        桌面池批量删除磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDesktopPoolVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopPoolVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopPoolVolumesResponse`
        """
        http_info = self._delete_desktop_pool_volumes_http_info(request)
        return self._call_api(**http_info)

    def delete_desktop_pool_volumes_invoker(self, request):
        http_info = self._delete_desktop_pool_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_desktop_pool_volumes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/volumes/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDesktopPoolVolumesResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def execute_desktop_pool_action(self, request):
        r"""操作桌面池

        操作桌面池，用于桌面池里面的桌面批量开机、关机、重启和休眠。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteDesktopPoolAction
        :type request: :class:`huaweicloudsdkworkspace.v2.ExecuteDesktopPoolActionRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExecuteDesktopPoolActionResponse`
        """
        http_info = self._execute_desktop_pool_action_http_info(request)
        return self._call_api(**http_info)

    def execute_desktop_pool_action_invoker(self, request):
        http_info = self._execute_desktop_pool_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_desktop_pool_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteDesktopPoolActionResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def execute_desktop_pool_script(self, request):
        r"""桌面池批量执行脚本

        桌面池批量执行脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteDesktopPoolScript
        :type request: :class:`huaweicloudsdkworkspace.v2.ExecuteDesktopPoolScriptRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExecuteDesktopPoolScriptResponse`
        """
        http_info = self._execute_desktop_pool_script_http_info(request)
        return self._call_api(**http_info)

    def execute_desktop_pool_script_invoker(self, request):
        http_info = self._execute_desktop_pool_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_desktop_pool_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/script-executions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteDesktopPoolScriptResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def expand_desktop_pool(self, request):
        r"""扩容桌面池

        扩容桌面池。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandDesktopPool
        :type request: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolResponse`
        """
        http_info = self._expand_desktop_pool_http_info(request)
        return self._call_api(**http_info)

    def expand_desktop_pool_invoker(self, request):
        http_info = self._expand_desktop_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_desktop_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/expand",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandDesktopPoolResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def expand_desktop_pool_volumes(self, request):
        r"""桌面池批量扩容磁盘

        桌面池批量扩容磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandDesktopPoolVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolVolumesResponse`
        """
        http_info = self._expand_desktop_pool_volumes_http_info(request)
        return self._call_api(**http_info)

    def expand_desktop_pool_volumes_invoker(self, request):
        http_info = self._expand_desktop_pool_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_desktop_pool_volumes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/volumes/batch-expand",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandDesktopPoolVolumesResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_desktop_pool_authorized_objects(self, request):
        r"""查询桌面池授权的用户、用户组

        该接口用于查询指定桌面池授权的用户、用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopPoolAuthorizedObjects
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopPoolAuthorizedObjectsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopPoolAuthorizedObjectsResponse`
        """
        http_info = self._list_desktop_pool_authorized_objects_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_pool_authorized_objects_invoker(self, request):
        http_info = self._list_desktop_pool_authorized_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktop_pool_authorized_objects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopPoolAuthorizedObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

        query_params = []
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

    def list_desktop_pools(self, request):
        r"""查询桌面池列表

        该接口用于查询桌面池列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopPools
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopPoolsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopPoolsResponse`
        """
        http_info = self._list_desktop_pools_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_pools_invoker(self, request):
        http_info = self._list_desktop_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktop_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktop-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopPoolsResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_pool_desktops_detail(self, request):
        r"""查询桌面池下的桌面信息

        该接口用于查询桌面池下的桌面信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPoolDesktopsDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ListPoolDesktopsDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListPoolDesktopsDetailResponse`
        """
        http_info = self._list_pool_desktops_detail_http_info(request)
        return self._call_api(**http_info)

    def list_pool_desktops_detail_invoker(self, request):
        http_info = self._list_pool_desktops_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pool_desktops_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/desktops",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoolDesktopsDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

        query_params = []
        if 'inconsistent_type' in local_var_params:
            query_params.append(('inconsistent_type', local_var_params['inconsistent_type']))
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

    def rebuild_desktop_pool(self, request):
        r"""桌面池重建系统盘

        桌面池重建系统盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebuildDesktopPool
        :type request: :class:`huaweicloudsdkworkspace.v2.RebuildDesktopPoolRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.RebuildDesktopPoolResponse`
        """
        http_info = self._rebuild_desktop_pool_http_info(request)
        return self._call_api(**http_info)

    def rebuild_desktop_pool_invoker(self, request):
        http_info = self._rebuild_desktop_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rebuild_desktop_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/rebuild",
            "request_type": request.__class__.__name__,
            "response_type": "RebuildDesktopPoolResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def resize_desktop_pool(self, request):
        r"""桌面池变更规格

        桌面池变更规格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeDesktopPool
        :type request: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopPoolRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopPoolResponse`
        """
        http_info = self._resize_desktop_pool_http_info(request)
        return self._call_api(**http_info)

    def resize_desktop_pool_invoker(self, request):
        http_info = self._resize_desktop_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_desktop_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeDesktopPoolResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def send_desktop_pool_notifications(self, request):
        r"""发送消息通知

        用于管理员向桌面发送消息通知。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendDesktopPoolNotifications
        :type request: :class:`huaweicloudsdkworkspace.v2.SendDesktopPoolNotificationsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.SendDesktopPoolNotificationsResponse`
        """
        http_info = self._send_desktop_pool_notifications_http_info(request)
        return self._call_api(**http_info)

    def send_desktop_pool_notifications_invoker(self, request):
        http_info = self._send_desktop_pool_notifications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_desktop_pool_notifications_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "SendDesktopPoolNotificationsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_desktop_pool_detail(self, request):
        r"""查询桌面池详情

        指定桌面池Id查询详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDesktopPoolDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopPoolDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopPoolDetailResponse`
        """
        http_info = self._show_desktop_pool_detail_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_pool_detail_invoker(self, request):
        http_info = self._show_desktop_pool_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_desktop_pool_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDesktopPoolDetailResponse"
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

    def show_desktop_pools_script_exec_tasks(self, request):
        r"""查询桌面池的脚本执行任务列表

        桌面池的脚本执行任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDesktopPoolsScriptExecTasks
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowDesktopPoolsScriptExecTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowDesktopPoolsScriptExecTasksResponse`
        """
        http_info = self._show_desktop_pools_script_exec_tasks_http_info(request)
        return self._call_api(**http_info)

    def show_desktop_pools_script_exec_tasks_invoker(self, request):
        http_info = self._show_desktop_pools_script_exec_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_desktop_pools_script_exec_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktop-pools/script-execution-tasks/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDesktopPoolsScriptExecTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'desktop_pool_id' in local_var_params:
            query_params.append(('desktop_pool_id', local_var_params['desktop_pool_id']))
        if 'script_id' in local_var_params:
            query_params.append(('script_id', local_var_params['script_id']))
        if 'script_name' in local_var_params:
            query_params.append(('script_name', local_var_params['script_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'execute_time_start' in local_var_params:
            query_params.append(('execute_time_start', local_var_params['execute_time_start']))
        if 'execute_time_end' in local_var_params:
            query_params.append(('execute_time_end', local_var_params['execute_time_end']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_desktop_pool(self, request):
        r"""修改桌面池属性

        修改桌面池属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDesktopPool
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopPoolRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateDesktopPoolResponse`
        """
        http_info = self._update_desktop_pool_http_info(request)
        return self._call_api(**http_info)

    def update_desktop_pool_invoker(self, request):
        http_info = self._update_desktop_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_desktop_pool_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/desktop-pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDesktopPoolResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_add_desktops_tags(self, request):
        r"""批量添加多个桌面标签

        同时对多个桌面批量添加标签，如果创建的标签已经存在（key相同）则覆，最大支持100个桌面，每个桌面最大20个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddDesktopsTags
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchAddDesktopsTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchAddDesktopsTagsResponse`
        """
        http_info = self._batch_add_desktops_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_add_desktops_tags_invoker(self, request):
        http_info = self._batch_add_desktops_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_desktops_tags_http_info(cls, request):
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

    def batch_change_tags(self, request):
        r"""批量添加删除标签

        为指定桌面批量添加或删除标签。创建时，如果创建的标签已经存在（key相同），则覆盖。删除时，如果删除的标签不存在，默认处理成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchChangeTags
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchChangeTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchChangeTagsResponse`
        """
        http_info = self._batch_change_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_change_tags_invoker(self, request):
        http_info = self._batch_change_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_change_tags_http_info(cls, request):
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

    def batch_delete_desktops_tags(self, request):
        r"""批量删除多个桌面标签

        同时对多个桌面批量添加标签，删除时，如果删除的标签不存在默认处理成功，最大支持100个桌面，每个桌面最大20个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteDesktopsTags
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopsTagsResponse`
        """
        http_info = self._batch_delete_desktops_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_desktops_tags_invoker(self, request):
        http_info = self._batch_delete_desktops_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_desktops_tags_http_info(cls, request):
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

    def create_tag(self, request):
        r"""创建桌面标签

        该接口用于为桌面创建标签，一个桌面上最多有10个标签。创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tag_http_info(cls, request):
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

    def delete_tag(self, request):
        r"""删除桌面标签

        该接口用于删除桌面标签。删除时，如果删除的标签不存在，默认处理成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tag_http_info(cls, request):
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

    def list_desktop_by_tags(self, request):
        r"""使用标签过滤桌面

        使用标签过滤桌面。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopByTags
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopByTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopByTagsResponse`
        """
        http_info = self._list_desktop_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_by_tags_invoker(self, request):
        http_info = self._list_desktop_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktop_by_tags_http_info(cls, request):
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

    def list_project_tags(self, request):
        r"""查询项目标签

        查询租户的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkworkspace.v2.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_tags_http_info(cls, request):
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_tag_by_desktop_id(self, request):
        r"""查询桌面标签

        查询指定桌面的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTagByDesktopId
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowTagByDesktopIdRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowTagByDesktopIdResponse`
        """
        http_info = self._show_tag_by_desktop_id_http_info(request)
        return self._call_api(**http_info)

    def show_tag_by_desktop_id_invoker(self, request):
        http_info = self._show_tag_by_desktop_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tag_by_desktop_id_http_info(cls, request):
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

    def batch_delete_user_groups(self, request):
        r"""批量删除用户组

        该接口用于批量删除用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteUserGroups
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteUserGroupsResponse`
        """
        http_info = self._batch_delete_user_groups_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_user_groups_invoker(self, request):
        http_info = self._batch_delete_user_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_user_groups_http_info(cls, request):
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

    def create_user_group(self, request):
        r"""创建用户组

        该接口用于创建用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateUserGroupResponse`
        """
        http_info = self._create_user_group_http_info(request)
        return self._call_api(**http_info)

    def create_user_group_invoker(self, request):
        http_info = self._create_user_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_user_group_http_info(cls, request):
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

    def delete_user_group(self, request):
        r"""删除用户组

        删除用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteUserGroupResponse`
        """
        http_info = self._delete_user_group_http_info(request)
        return self._call_api(**http_info)

    def delete_user_group_invoker(self, request):
        http_info = self._delete_user_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_user_group_http_info(cls, request):
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

    def list_user_groups(self, request):
        r"""查询用户组列表

        查询用户组列表，支持分页。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserGroups
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserGroupsResponse`
        """
        http_info = self._list_user_groups_http_info(request)
        return self._call_api(**http_info)

    def list_user_groups_invoker(self, request):
        http_info = self._list_user_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_groups_http_info(cls, request):
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

    def list_users_of_group(self, request):
        r"""查询用户组中的用户

        该接口用于查询用户组中的用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsersOfGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsersOfGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsersOfGroupResponse`
        """
        http_info = self._list_users_of_group_http_info(request)
        return self._call_api(**http_info)

    def list_users_of_group_invoker(self, request):
        http_info = self._list_users_of_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_users_of_group_http_info(cls, request):
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

    def run_actions_on_group(self, request):
        r"""操作用户组

        操作用户组，如添加用户、删除用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunActionsOnGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.RunActionsOnGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.RunActionsOnGroupResponse`
        """
        http_info = self._run_actions_on_group_http_info(request)
        return self._call_api(**http_info)

    def run_actions_on_group_invoker(self, request):
        http_info = self._run_actions_on_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_actions_on_group_http_info(cls, request):
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

    def update_user_group(self, request):
        r"""修改用户组信息

        该接口用于修改用户组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateUserGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateUserGroupResponse`
        """
        http_info = self._update_user_group_http_info(request)
        return self._call_api(**http_info)

    def update_user_group_invoker(self, request):
        http_info = self._update_user_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_group_http_info(cls, request):
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

    def list_images(self, request):
        r"""查询产品镜像列表

        该接口用于查询云桌面支持的产品镜像列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImages
        :type request: :class:`huaweicloudsdkworkspace.v2.ListImagesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListImagesResponse`
        """
        http_info = self._list_images_http_info(request)
        return self._call_api(**http_info)

    def list_images_invoker(self, request):
        http_info = self._list_images_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_images_http_info(cls, request):
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
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_market_images(self, request):
        r"""获取云市场镜像列表

        获取云市场镜像列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMarketImages
        :type request: :class:`huaweicloudsdkworkspace.v2.ListMarketImagesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListMarketImagesResponse`
        """
        http_info = self._list_market_images_http_info(request)
        return self._call_api(**http_info)

    def list_market_images_invoker(self, request):
        http_info = self._list_market_images_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_market_images_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/market-images",
            "request_type": request.__class__.__name__,
            "response_type": "ListMarketImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'image_ids' in local_var_params:
            query_params.append(('image_ids', local_var_params['image_ids']))
            collection_formats['image_ids'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def estimate_add_resources(self, request):
        r"""包周期桌面增配变更批量询价

        包周期桌面增配变更批量询价。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateAddResources
        :type request: :class:`huaweicloudsdkworkspace.v2.EstimateAddResourcesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateAddResourcesResponse`
        """
        http_info = self._estimate_add_resources_http_info(request)
        return self._call_api(**http_info)

    def estimate_add_resources_invoker(self, request):
        http_info = self._estimate_add_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _estimate_add_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/periodic/inquiry/add-resources",
            "request_type": request.__class__.__name__,
            "response_type": "EstimateAddResourcesResponse"
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

    def estimate_change_images(self, request):
        r"""批量包周期桌面切换镜像询价

        批量包周期桌面切换镜像(由不收费镜像变更至收费镜像)询价。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateChangeImages
        :type request: :class:`huaweicloudsdkworkspace.v2.EstimateChangeImagesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateChangeImagesResponse`
        """
        http_info = self._estimate_change_images_http_info(request)
        return self._call_api(**http_info)

    def estimate_change_images_invoker(self, request):
        http_info = self._estimate_change_images_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _estimate_change_images_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/periodic/inquiry/change-image",
            "request_type": request.__class__.__name__,
            "response_type": "EstimateChangeImagesResponse"
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

    def estimate_desktop_pool_add_volume(self, request):
        r"""包周期桌面池添加单个磁盘批量询价

        包周期桌面池添加单个磁盘批量询价。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateDesktopPoolAddVolume
        :type request: :class:`huaweicloudsdkworkspace.v2.EstimateDesktopPoolAddVolumeRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateDesktopPoolAddVolumeResponse`
        """
        http_info = self._estimate_desktop_pool_add_volume_http_info(request)
        return self._call_api(**http_info)

    def estimate_desktop_pool_add_volume_invoker(self, request):
        http_info = self._estimate_desktop_pool_add_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _estimate_desktop_pool_add_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pool/periodic/inquiry/add-volume",
            "request_type": request.__class__.__name__,
            "response_type": "EstimateDesktopPoolAddVolumeResponse"
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

    def estimate_desktop_pool_change_image(self, request):
        r"""包周期桌面池切换镜像批量询价

        包周期桌面池切换镜像(由不收费镜像变更至收费镜像)批量询价。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateDesktopPoolChangeImage
        :type request: :class:`huaweicloudsdkworkspace.v2.EstimateDesktopPoolChangeImageRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateDesktopPoolChangeImageResponse`
        """
        http_info = self._estimate_desktop_pool_change_image_http_info(request)
        return self._call_api(**http_info)

    def estimate_desktop_pool_change_image_invoker(self, request):
        http_info = self._estimate_desktop_pool_change_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _estimate_desktop_pool_change_image_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pool/periodic/inquiry/change-image",
            "request_type": request.__class__.__name__,
            "response_type": "EstimateDesktopPoolChangeImageResponse"
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

    def estimate_desktop_pool_extend_volume(self, request):
        r"""包周期桌面池扩容磁盘批量询价

        包周期桌面池扩容磁盘批量询价。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateDesktopPoolExtendVolume
        :type request: :class:`huaweicloudsdkworkspace.v2.EstimateDesktopPoolExtendVolumeRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateDesktopPoolExtendVolumeResponse`
        """
        http_info = self._estimate_desktop_pool_extend_volume_http_info(request)
        return self._call_api(**http_info)

    def estimate_desktop_pool_extend_volume_invoker(self, request):
        http_info = self._estimate_desktop_pool_extend_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _estimate_desktop_pool_extend_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pool/periodic/inquiry/extend-volume",
            "request_type": request.__class__.__name__,
            "response_type": "EstimateDesktopPoolExtendVolumeResponse"
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

    def estimate_desktop_pool_resize(self, request):
        r"""包周期桌面池变更规格批量询价

        包周期桌面池变更规格批量询价。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateDesktopPoolResize
        :type request: :class:`huaweicloudsdkworkspace.v2.EstimateDesktopPoolResizeRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateDesktopPoolResizeResponse`
        """
        http_info = self._estimate_desktop_pool_resize_http_info(request)
        return self._call_api(**http_info)

    def estimate_desktop_pool_resize_invoker(self, request):
        http_info = self._estimate_desktop_pool_resize_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _estimate_desktop_pool_resize_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pool/periodic/inquiry/resize",
            "request_type": request.__class__.__name__,
            "response_type": "EstimateDesktopPoolResizeResponse"
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

    def run_actions_on_workspace_job(self, request):
        r"""重试任务

        该接口用来对失败的任务进行重试，当前仅支持开户和销户的任务重试。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunActionsOnWorkspaceJob
        :type request: :class:`huaweicloudsdkworkspace.v2.RunActionsOnWorkspaceJobRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.RunActionsOnWorkspaceJobResponse`
        """
        http_info = self._run_actions_on_workspace_job_http_info(request)
        return self._call_api(**http_info)

    def run_actions_on_workspace_job_invoker(self, request):
        http_info = self._run_actions_on_workspace_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_actions_on_workspace_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspace-jobs/{job_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "RunActionsOnWorkspaceJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def batch_delete_sub_jobs(self, request):
        r"""删除子任务

        该接口用于删除子任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteSubJobs
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteSubJobsResponse`
        """
        http_info = self._batch_delete_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_sub_jobs_invoker(self, request):
        http_info = self._batch_delete_sub_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_sub_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspace-sub-jobs/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteSubJobsResponse"
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

    def list_ita_sub_jobs(self, request):
        r"""子任务查询

        该接口用于查询异步任务执行情况，比如查询创建桌面的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListItaSubJobs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListItaSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListItaSubJobsResponse`
        """
        http_info = self._list_ita_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_ita_sub_jobs_invoker(self, request):
        http_info = self._list_ita_sub_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ita_sub_jobs_http_info(cls, request):
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

    def show_job(self, request):
        r"""查询任务详情

        该接口用于查询异步任务的执行情况，比如查询创建桌面任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspace-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def list_nat_mapping_configs(self, request):
        r"""查询租户的NAT映射配置项

        查询租户的NAT映射配置项。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNatMappingConfigs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListNatMappingConfigsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListNatMappingConfigsResponse`
        """
        http_info = self._list_nat_mapping_configs_http_info(request)
        return self._call_api(**http_info)

    def list_nat_mapping_configs_invoker(self, request):
        http_info = self._list_nat_mapping_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_nat_mapping_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/nat-mapping-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListNatMappingConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_nat_mapping_configs(self, request):
        r"""修改租户的NAT映射配置项

        修改租户的NAT映射配置项。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNatMappingConfigs
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateNatMappingConfigsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateNatMappingConfigsResponse`
        """
        http_info = self._update_nat_mapping_configs_http_info(request)
        return self._call_api(**http_info)

    def update_nat_mapping_configs_invoker(self, request):
        http_info = self._update_nat_mapping_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_nat_mapping_configs_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/nat-mapping-configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNatMappingConfigsResponse"
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

    def apply_desktops_internet(self, request):
        r"""开通桌面上网功能

        开通桌面上网功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyDesktopsInternet
        :type request: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternetRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternetResponse`
        """
        http_info = self._apply_desktops_internet_http_info(request)
        return self._call_api(**http_info)

    def apply_desktops_internet_invoker(self, request):
        http_info = self._apply_desktops_internet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_desktops_internet_http_info(cls, request):
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

    def apply_internet(self, request):
        r"""开通上网功能

        开通上网功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyInternet
        :type request: :class:`huaweicloudsdkworkspace.v2.ApplyInternetRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyInternetResponse`
        """
        http_info = self._apply_internet_http_info(request)
        return self._call_api(**http_info)

    def apply_internet_invoker(self, request):
        http_info = self._apply_internet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_internet_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/internet",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyInternetResponse"
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

    def apply_subnet_bandwidth(self, request):
        r"""创建云办公带宽

        创建按需云办公带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplySubnetBandwidth
        :type request: :class:`huaweicloudsdkworkspace.v2.ApplySubnetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplySubnetBandwidthResponse`
        """
        http_info = self._apply_subnet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def apply_subnet_bandwidth_invoker(self, request):
        http_info = self._apply_subnet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_subnet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ApplySubnetBandwidthResponse"
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

    def associate_desktops_eip(self, request):
        r"""桌面绑定EIP

        桌面绑定EIP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateDesktopsEip
        :type request: :class:`huaweicloudsdkworkspace.v2.AssociateDesktopsEipRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssociateDesktopsEipResponse`
        """
        http_info = self._associate_desktops_eip_http_info(request)
        return self._call_api(**http_info)

    def associate_desktops_eip_invoker(self, request):
        http_info = self._associate_desktops_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_desktops_eip_http_info(cls, request):
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

    def batch_disassociate_desktops_eip(self, request):
        r"""批量桌面解绑EIP

        批量桌面解绑EIP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDisassociateDesktopsEip
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDisassociateDesktopsEipRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDisassociateDesktopsEipResponse`
        """
        http_info = self._batch_disassociate_desktops_eip_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_desktops_eip_invoker(self, request):
        http_info = self._batch_disassociate_desktops_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_disassociate_desktops_eip_http_info(cls, request):
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

    def delete_subnet_bandwidth(self, request):
        r"""删除云办公带宽

        删除云办公带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubnetBandwidth
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteSubnetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteSubnetBandwidthResponse`
        """
        http_info = self._delete_subnet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def delete_subnet_bandwidth_invoker(self, request):
        http_info = self._delete_subnet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_subnet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/bandwidths/{bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubnetBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def list_desktops_eips(self, request):
        r"""查询已绑定桌面和未绑定的EIP

        查询已绑定桌面和未绑定的EIP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopsEips
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsEipsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsEipsResponse`
        """
        http_info = self._list_desktops_eips_http_info(request)
        return self._call_api(**http_info)

    def list_desktops_eips_invoker(self, request):
        http_info = self._list_desktops_eips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktops_eips_http_info(cls, request):
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

    def list_internet(self, request):
        r"""查询上网功能

        查询上网功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInternet
        :type request: :class:`huaweicloudsdkworkspace.v2.ListInternetRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListInternetResponse`
        """
        http_info = self._list_internet_http_info(request)
        return self._call_api(**http_info)

    def list_internet_invoker(self, request):
        http_info = self._list_internet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_internet_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/internet",
            "request_type": request.__class__.__name__,
            "response_type": "ListInternetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'nat_name' in local_var_params:
            query_params.append(('nat_name', local_var_params['nat_name']))
        if 'eip' in local_var_params:
            query_params.append(('eip', local_var_params['eip']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_nat_gateways(self, request):
        r"""查询NAT网关列表

        查询NAT网关列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNatGateways
        :type request: :class:`huaweicloudsdkworkspace.v2.ListNatGatewaysRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListNatGatewaysResponse`
        """
        http_info = self._list_nat_gateways_http_info(request)
        return self._call_api(**http_info)

    def list_nat_gateways_invoker(self, request):
        http_info = self._list_nat_gateways_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_nat_gateways_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/nat-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListNatGatewaysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'spec' in local_var_params:
            query_params.append(('spec', local_var_params['spec']))
            collection_formats['spec'] = 'csv'
        if 'router_id' in local_var_params:
            query_params.append(('router_id', local_var_params['router_id']))
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

    def list_ports(self, request):
        r"""查询端口列表

        查询端口列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPorts
        :type request: :class:`huaweicloudsdkworkspace.v2.ListPortsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListPortsResponse`
        """
        http_info = self._list_ports_http_info(request)
        return self._call_api(**http_info)

    def list_ports_invoker(self, request):
        http_info = self._list_ports_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ports_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/ports",
            "request_type": request.__class__.__name__,
            "response_type": "ListPortsResponse"
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
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))
        if 'is_used' in local_var_params:
            query_params.append(('is_used', local_var_params['is_used']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_subnet_bandwidths(self, request):
        r"""查询云办公带宽列表

        查询云办公带宽列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubnetBandwidths
        :type request: :class:`huaweicloudsdkworkspace.v2.ListSubnetBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListSubnetBandwidthsResponse`
        """
        http_info = self._list_subnet_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def list_subnet_bandwidths_invoker(self, request):
        http_info = self._list_subnet_bandwidths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_subnet_bandwidths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubnetBandwidthsResponse"
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
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))
        if 'bandwidth_id' in local_var_params:
            query_params.append(('bandwidth_id', local_var_params['bandwidth_id']))
        if 'bandwidth_name' in local_var_params:
            query_params.append(('bandwidth_name', local_var_params['bandwidth_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_subnet_bandwidth_control_list(self, request):
        r"""查询云办公带宽的控制配置

        查询云办公带宽的控制配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSubnetBandwidthControlList
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowSubnetBandwidthControlListRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowSubnetBandwidthControlListResponse`
        """
        http_info = self._show_subnet_bandwidth_control_list_http_info(request)
        return self._call_api(**http_info)

    def show_subnet_bandwidth_control_list_invoker(self, request):
        http_info = self._show_subnet_bandwidth_control_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_subnet_bandwidth_control_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/bandwidths/{bandwidth_id}/control-list",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubnetBandwidthControlListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

        query_params = []
        if 'desktop_id' in local_var_params:
            query_params.append(('desktop_id', local_var_params['desktop_id']))
        if 'desktop_name' in local_var_params:
            query_params.append(('desktop_name', local_var_params['desktop_name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'control_mode' in local_var_params:
            query_params.append(('control_mode', local_var_params['control_mode']))
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

    def show_using_subnets(self, request):
        r"""查询正在被使用的子网id列表

        根据子网id列表查询正在被桌面使用的子网id，并且返回subnetId列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUsingSubnets
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowUsingSubnetsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowUsingSubnetsResponse`
        """
        http_info = self._show_using_subnets_http_info(request)
        return self._call_api(**http_info)

    def show_using_subnets_invoker(self, request):
        http_info = self._show_using_subnets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_using_subnets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/subnets/using-subnets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUsingSubnetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subnet_ids' in local_var_params:
            query_params.append(('subnet_ids', local_var_params['subnet_ids']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_subnet_bandwidth(self, request):
        r"""修改云办公带宽

        修改云办公带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubnetBandwidth
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetBandwidthResponse`
        """
        http_info = self._update_subnet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_subnet_bandwidth_invoker(self, request):
        http_info = self._update_subnet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_subnet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/bandwidths/{bandwidth_id}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubnetBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def update_subnet_bandwidth_control_list(self, request):
        r"""修改云办公带宽的控制配置

        修改云办公带宽的控制配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubnetBandwidthControlList
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetBandwidthControlListRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetBandwidthControlListResponse`
        """
        http_info = self._update_subnet_bandwidth_control_list_http_info(request)
        return self._call_api(**http_info)

    def update_subnet_bandwidth_control_list_invoker(self, request):
        http_info = self._update_subnet_bandwidth_control_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_subnet_bandwidth_control_list_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/bandwidths/{bandwidth_id}/control-list",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubnetBandwidthControlListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def create_change_order(self, request):
        r"""创建变更订单

        变更规格、扩容磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateChangeOrder
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateChangeOrderRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateChangeOrderResponse`
        """
        http_info = self._create_change_order_http_info(request)
        return self._call_api(**http_info)

    def create_change_order_invoker(self, request):
        http_info = self._create_change_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_change_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/periodic/{desktop_id}/change/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateChangeOrderResponse"
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

    def create_desktop_batch_order(self, request):
        r"""包周期桌面批量变更下单

        包周期桌面批量变更下单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDesktopBatchOrder
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopBatchOrderRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopBatchOrderResponse`
        """
        http_info = self._create_desktop_batch_order_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_batch_order_invoker(self, request):
        http_info = self._create_desktop_batch_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_desktop_batch_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/periodic/change/batch-order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDesktopBatchOrderResponse"
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

    def create_desktop_order(self, request):
        r"""创建桌面订单

        创建桌面订单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDesktopOrder
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopOrderRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopOrderResponse`
        """
        http_info = self._create_desktop_order_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_order_invoker(self, request):
        http_info = self._create_desktop_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_desktop_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/orders/subscribe",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDesktopOrderResponse"
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

    def create_desktop_pool_change_order(self, request):
        r"""包周期桌面池批量变更下单

        包周期桌面池批量变更下单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDesktopPoolChangeOrder
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolChangeOrderRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolChangeOrderResponse`
        """
        http_info = self._create_desktop_pool_change_order_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_pool_change_order_invoker(self, request):
        http_info = self._create_desktop_pool_change_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_desktop_pool_change_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop-pool/periodic/change/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDesktopPoolChangeOrderResponse"
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

    def create_order(self, request):
        r"""包周期下单

        包周期资源（桌面、磁盘）下订单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrder
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateOrderRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateOrderResponse`
        """
        http_info = self._create_order_http_info(request)
        return self._call_api(**http_info)

    def create_order_invoker(self, request):
        http_info = self._create_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/periodic/subscribe/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrderResponse"
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

    def create_subnet_bandwidth_change_order(self, request):
        r"""包周期云办公带宽变更下单

        包周期云办公带宽变更下单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubnetBandwidthChangeOrder
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateSubnetBandwidthChangeOrderRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateSubnetBandwidthChangeOrderResponse`
        """
        http_info = self._create_subnet_bandwidth_change_order_http_info(request)
        return self._call_api(**http_info)

    def create_subnet_bandwidth_change_order_invoker(self, request):
        http_info = self._create_subnet_bandwidth_change_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_subnet_bandwidth_change_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/bandwidths/{bandwidth_id}/periodic/change/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubnetBandwidthChangeOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def add_ou(self, request):
        r"""新增OU信息

        该接口用于创建OU。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddOu
        :type request: :class:`huaweicloudsdkworkspace.v2.AddOuRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddOuResponse`
        """
        http_info = self._add_ou_http_info(request)
        return self._call_api(**http_info)

    def add_ou_invoker(self, request):
        http_info = self._add_ou_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_ou_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ous",
            "request_type": request.__class__.__name__,
            "response_type": "AddOuResponse"
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

    def delete_ou(self, request):
        r"""删除OU信息

        该接口用于删除OU信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOu
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteOuRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteOuResponse`
        """
        http_info = self._delete_ou_http_info(request)
        return self._call_api(**http_info)

    def delete_ou_invoker(self, request):
        http_info = self._delete_ou_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ou_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/ous/{ou_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOuResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ou_id' in local_var_params:
            path_params['ou_id'] = local_var_params['ou_id']

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

    def list_ad_ou_users(self, request):
        r"""查询OU下用户信息

        查询OU下用户信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAdOuUsers
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAdOuUsersRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAdOuUsersResponse`
        """
        http_info = self._list_ad_ou_users_http_info(request)
        return self._call_api(**http_info)

    def list_ad_ou_users_invoker(self, request):
        http_info = self._list_ad_ou_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ad_ou_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/ou-users",
            "request_type": request.__class__.__name__,
            "response_type": "ListAdOuUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ou_dn' in local_var_params:
            query_params.append(('ou_dn', local_var_params['ou_dn']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'has_existed' in local_var_params:
            query_params.append(('has_existed', local_var_params['has_existed']))
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

    def list_ad_ous(self, request):
        r"""查询AD里的OU列表

        查询AD里的OU列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAdOus
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAdOusRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAdOusResponse`
        """
        http_info = self._list_ad_ous_http_info(request)
        return self._call_api(**http_info)

    def list_ad_ous_invoker(self, request):
        http_info = self._list_ad_ous_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ad_ous_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/ad-ous",
            "request_type": request.__class__.__name__,
            "response_type": "ListAdOusResponse"
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

    def list_ou_details(self, request):
        r"""查询OU列表

        查询OU列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOuDetails
        :type request: :class:`huaweicloudsdkworkspace.v2.ListOuDetailsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListOuDetailsResponse`
        """
        http_info = self._list_ou_details_http_info(request)
        return self._call_api(**http_info)

    def list_ou_details_invoker(self, request):
        http_info = self._list_ou_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ou_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/ous",
            "request_type": request.__class__.__name__,
            "response_type": "ListOuDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ou_name' in local_var_params:
            query_params.append(('ou_name', local_var_params['ou_name']))
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

    def update_ou_info(self, request):
        r"""更新OU信息

        更新OU信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOuInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateOuInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateOuInfoResponse`
        """
        http_info = self._update_ou_info_http_info(request)
        return self._call_api(**http_info)

    def update_ou_info_invoker(self, request):
        http_info = self._update_ou_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ou_info_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/ous/{ou_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOuInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ou_id' in local_var_params:
            path_params['ou_id'] = local_var_params['ou_id']

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

    def batch_update_target_of_policy_group(self, request):
        r"""修改策略组应用对象

        批量增加、删除应用对象到指定策略组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateTargetOfPolicyGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchUpdateTargetOfPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchUpdateTargetOfPolicyGroupResponse`
        """
        http_info = self._batch_update_target_of_policy_group_http_info(request)
        return self._call_api(**http_info)

    def batch_update_target_of_policy_group_invoker(self, request):
        http_info = self._batch_update_target_of_policy_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_target_of_policy_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/policy-groups/{policy_group_id}/targets",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateTargetOfPolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

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

    def create_policy_group(self, request):
        r"""新增策略组

        新增策略组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePolicyGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.CreatePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreatePolicyGroupResponse`
        """
        http_info = self._create_policy_group_http_info(request)
        return self._call_api(**http_info)

    def create_policy_group_invoker(self, request):
        http_info = self._create_policy_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_policy_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/policy-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyGroupResponse"
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

    def delete_policy_group(self, request):
        r"""删除策略组

        删除指定策略组，包含策略组对应的策略信息以及应用对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicyGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.DeletePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeletePolicyGroupResponse`
        """
        http_info = self._delete_policy_group_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_group_invoker(self, request):
        http_info = self._delete_policy_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/policy-groups/{policy_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

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

    def list_original_policy_info(self, request):
        r"""查询初始策略项

        查询初始策略项。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOriginalPolicyInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.ListOriginalPolicyInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListOriginalPolicyInfoResponse`
        """
        http_info = self._list_original_policy_info_http_info(request)
        return self._call_api(**http_info)

    def list_original_policy_info_invoker(self, request):
        http_info = self._list_original_policy_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_original_policy_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/policy-groups/original-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListOriginalPolicyInfoResponse"
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

    def list_policies_of_policy_group(self, request):
        r"""查询策略组中的策略项

        查询指定策略组内的策略项。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPoliciesOfPolicyGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.ListPoliciesOfPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListPoliciesOfPolicyGroupResponse`
        """
        http_info = self._list_policies_of_policy_group_http_info(request)
        return self._call_api(**http_info)

    def list_policies_of_policy_group_invoker(self, request):
        http_info = self._list_policies_of_policy_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policies_of_policy_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/policy-groups/{policy_group_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoliciesOfPolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

        query_params = []
        if 'policy_type' in local_var_params:
            query_params.append(('policy_type', local_var_params['policy_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_detail_info_by_id(self, request):
        r"""查询策略组

        根据策略组ID查询策略组详细信息，包含策略信息以及应用对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyDetailInfoById
        :type request: :class:`huaweicloudsdkworkspace.v2.ListPolicyDetailInfoByIdRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListPolicyDetailInfoByIdResponse`
        """
        http_info = self._list_policy_detail_info_by_id_http_info(request)
        return self._call_api(**http_info)

    def list_policy_detail_info_by_id_invoker(self, request):
        http_info = self._list_policy_detail_info_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_detail_info_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/policy-groups/{policy_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyDetailInfoByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

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

    def list_policy_group(self, request):
        r"""查询策略组列表

        查询策略组概要信息列表，不包含策略信息以及应用对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.ListPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListPolicyGroupResponse`
        """
        http_info = self._list_policy_group_http_info(request)
        return self._call_api(**http_info)

    def list_policy_group_invoker(self, request):
        http_info = self._list_policy_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/policy-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyGroupResponse"
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
        if 'policy_group_id' in local_var_params:
            query_params.append(('policy_group_id', local_var_params['policy_group_id']))
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'priority' in local_var_params:
            query_params.append(('priority', local_var_params['priority']))
        if 'update_time' in local_var_params:
            query_params.append(('update_time', local_var_params['update_time']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'is_group_name_accurate' in local_var_params:
            query_params.append(('is_group_name_accurate', local_var_params['is_group_name_accurate']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_group_info(self, request):
        r"""查询策略组详情列表

        包含策略信息以及应用对象的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyGroupInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.ListPolicyGroupInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListPolicyGroupInfoResponse`
        """
        http_info = self._list_policy_group_info_http_info(request)
        return self._call_api(**http_info)

    def list_policy_group_info_invoker(self, request):
        http_info = self._list_policy_group_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_group_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/policy-groups/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyGroupInfoResponse"
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
        if 'policy_group_id' in local_var_params:
            query_params.append(('policy_group_id', local_var_params['policy_group_id']))
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'priority' in local_var_params:
            query_params.append(('priority', local_var_params['priority']))
        if 'update_time' in local_var_params:
            query_params.append(('update_time', local_var_params['update_time']))
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

    def list_target_of_policy_group(self, request):
        r"""查询策略组应用对象

        查询指定策略组所应用的对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTargetOfPolicyGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTargetOfPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTargetOfPolicyGroupResponse`
        """
        http_info = self._list_target_of_policy_group_http_info(request)
        return self._call_api(**http_info)

    def list_target_of_policy_group_invoker(self, request):
        http_info = self._list_target_of_policy_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_target_of_policy_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/policy-groups/{policy_group_id}/targets",
            "request_type": request.__class__.__name__,
            "response_type": "ListTargetOfPolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

        query_params = []
        if 'target_type' in local_var_params:
            query_params.append(('target_type', local_var_params['target_type']))
        if 'target_name' in local_var_params:
            query_params.append(('target_name', local_var_params['target_name']))
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

    def update_policies_of_policy_group(self, request):
        r"""修改策略组中的策略项

        修改一个策略组的部分或者所有策略项。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePoliciesOfPolicyGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdatePoliciesOfPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdatePoliciesOfPolicyGroupResponse`
        """
        http_info = self._update_policies_of_policy_group_http_info(request)
        return self._call_api(**http_info)

    def update_policies_of_policy_group_invoker(self, request):
        http_info = self._update_policies_of_policy_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policies_of_policy_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/policy-groups/{policy_group_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePoliciesOfPolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

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

    def update_policy_group(self, request):
        r"""修改策略组

        修改指定策略组的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicyGroup
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdatePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdatePolicyGroupResponse`
        """
        http_info = self._update_policy_group_http_info(request)
        return self._call_api(**http_info)

    def update_policy_group_invoker(self, request):
        http_info = self._update_policy_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policy_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/policy-groups/{policy_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

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

    def list_hour_packages_type(self, request):
        r"""查询可订购小时包类型

        该接口用于查询可订购小时包类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHourPackagesType
        :type request: :class:`huaweicloudsdkworkspace.v2.ListHourPackagesTypeRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListHourPackagesTypeResponse`
        """
        http_info = self._list_hour_packages_type_http_info(request)
        return self._call_api(**http_info)

    def list_hour_packages_type_invoker(self, request):
        http_info = self._list_hour_packages_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_hour_packages_type_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/products/hour-packages",
            "request_type": request.__class__.__name__,
            "response_type": "ListHourPackagesTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'desktop_resource_spec_code' in local_var_params:
            query_params.append(('desktop_resource_spec_code', local_var_params['desktop_resource_spec_code']))
        if 'resource_spec_code' in local_var_params:
            query_params.append(('resource_spec_code', local_var_params['resource_spec_code']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_products(self, request):
        r"""查询产品套餐列表

        该接口用于查询云桌面支持的产品套餐列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkworkspace.v2.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListProductsResponse`
        """
        http_info = self._list_products_http_info(request)
        return self._call_api(**http_info)

    def list_products_invoker(self, request):
        http_info = self._list_products_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_products_http_info(cls, request):
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

    def list_sharer_products(self, request):
        r"""查询协同套餐列表

        该接口用于查询协同套餐列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSharerProducts
        :type request: :class:`huaweicloudsdkworkspace.v2.ListSharerProductsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListSharerProductsResponse`
        """
        http_info = self._list_sharer_products_http_info(request)
        return self._call_api(**http_info)

    def list_sharer_products_invoker(self, request):
        http_info = self._list_sharer_products_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sharer_products_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/products/sharer",
            "request_type": request.__class__.__name__,
            "response_type": "ListSharerProductsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'share_space_size' in local_var_params:
            query_params.append(('share_space_size', local_var_params['share_space_size']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'is_gpu' in local_var_params:
            query_params.append(('is_gpu', local_var_params['is_gpu']))
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

    def list_tenant_profiles(self, request):
        r"""查询租户功能状态

        查询租户功能状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTenantProfiles
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTenantProfilesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTenantProfilesResponse`
        """
        http_info = self._list_tenant_profiles_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_profiles_invoker(self, request):
        http_info = self._list_tenant_profiles_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tenant_profiles_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-center/profiles",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantProfilesResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_tenant_profile(self, request):
        r"""启禁用租户功能

        启禁用租户功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTenantProfile
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateTenantProfileRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTenantProfileResponse`
        """
        http_info = self._update_tenant_profile_http_info(request)
        return self._call_api(**http_info)

    def update_tenant_profile_invoker(self, request):
        http_info = self._update_tenant_profile_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_tenant_profile_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-center/profiles",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTenantProfileResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_quota_details(self, request):
        r"""查询租户单个站点配额详情

        查询租户单个站点配额详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotaDetails
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowQuotaDetailsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowQuotaDetailsResponse`
        """
        http_info = self._show_quota_details_http_info(request)
        return self._call_api(**http_info)

    def show_quota_details_invoker(self, request):
        http_info = self._show_quota_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quota_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quotas/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))
        if 'az_code' in local_var_params:
            query_params.append(('az_code', local_var_params['az_code']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_quotas(self, request):
        r"""查询租户配额

        Console Framework和WKSDesktopManager调用该接口查询租户配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quotas_http_info(cls, request):
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

    def batch_delete_scheduled_tasks(self, request):
        r"""批量删除定时任务

        批量删除定时任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteScheduledTasks
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteScheduledTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteScheduledTasksResponse`
        """
        http_info = self._batch_delete_scheduled_tasks_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_scheduled_tasks_invoker(self, request):
        http_info = self._batch_delete_scheduled_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_scheduled_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/scheduled-tasks/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteScheduledTasksResponse"
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

    def create_scheduled_tasks(self, request):
        r"""创建定时任务

        创建定时任务。
        注:需通过开通委托功能接口先对云服务进行授权才可以使用该功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScheduledTasks
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateScheduledTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateScheduledTasksResponse`
        """
        http_info = self._create_scheduled_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_scheduled_tasks_invoker(self, request):
        http_info = self._create_scheduled_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_scheduled_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/scheduled-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScheduledTasksResponse"
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

    def delete_scheduled_tasks(self, request):
        r"""删除定时任务

        删除定时任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScheduledTasks
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteScheduledTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteScheduledTasksResponse`
        """
        http_info = self._delete_scheduled_tasks_http_info(request)
        return self._call_api(**http_info)

    def delete_scheduled_tasks_invoker(self, request):
        http_info = self._delete_scheduled_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_scheduled_tasks_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/scheduled-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScheduledTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def list_future_executions(self, request):
        r"""未来执行的具体时间列表

        未来执行的具体时间列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFutureExecutions
        :type request: :class:`huaweicloudsdkworkspace.v2.ListFutureExecutionsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListFutureExecutionsResponse`
        """
        http_info = self._list_future_executions_http_info(request)
        return self._call_api(**http_info)

    def list_future_executions_invoker(self, request):
        http_info = self._list_future_executions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_future_executions_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/scheduled-tasks/future-executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListFutureExecutionsResponse"
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

    def list_scheduled_tasks(self, request):
        r"""查询定时任务列表

        查询定时任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScheduledTasks
        :type request: :class:`huaweicloudsdkworkspace.v2.ListScheduledTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListScheduledTasksResponse`
        """
        http_info = self._list_scheduled_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_tasks_invoker(self, request):
        http_info = self._list_scheduled_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scheduled_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/scheduled-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledTasksResponse"
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
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'scheduled_type' in local_var_params:
            query_params.append(('scheduled_type', local_var_params['scheduled_type']))
        if 'life_cycle_type' in local_var_params:
            query_params.append(('life_cycle_type', local_var_params['life_cycle_type']))
        if 'last_status' in local_var_params:
            query_params.append(('last_status', local_var_params['last_status']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_scheduled_tasks_records(self, request):
        r"""查询定时任务执行记录

        查询定时任务执行记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScheduledTasksRecords
        :type request: :class:`huaweicloudsdkworkspace.v2.ListScheduledTasksRecordsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListScheduledTasksRecordsResponse`
        """
        http_info = self._list_scheduled_tasks_records_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_tasks_records_invoker(self, request):
        http_info = self._list_scheduled_tasks_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scheduled_tasks_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/scheduled-tasks/{task_id}/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledTasksRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
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

    def list_scheduled_tasks_records_details(self, request):
        r"""查询定时任务执行记录详情

        查询定时任务执行记录详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScheduledTasksRecordsDetails
        :type request: :class:`huaweicloudsdkworkspace.v2.ListScheduledTasksRecordsDetailsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListScheduledTasksRecordsDetailsResponse`
        """
        http_info = self._list_scheduled_tasks_records_details_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_tasks_records_details_invoker(self, request):
        http_info = self._list_scheduled_tasks_records_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scheduled_tasks_records_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/scheduled-tasks/{task_id}/records/{record_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledTasksRecordsDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []
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

    def list_time_zones(self, request):
        r"""获取时区配置

        获取时区配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTimeZones
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTimeZonesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTimeZonesResponse`
        """
        http_info = self._list_time_zones_http_info(request)
        return self._call_api(**http_info)

    def list_time_zones_invoker(self, request):
        http_info = self._list_time_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_time_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/common/timezones",
            "request_type": request.__class__.__name__,
            "response_type": "ListTimeZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'time_zone_name' in local_var_params:
            query_params.append(('time_zone_name', local_var_params['time_zone_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_scheduled_tasks(self, request):
        r"""查询定时任务详情

        查询定时任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScheduledTasks
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowScheduledTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowScheduledTasksResponse`
        """
        http_info = self._show_scheduled_tasks_http_info(request)
        return self._call_api(**http_info)

    def show_scheduled_tasks_invoker(self, request):
        http_info = self._show_scheduled_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_scheduled_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/scheduled-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScheduledTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def update_scheduled_tasks(self, request):
        r"""修改定时任务

        修改定时任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateScheduledTasks
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateScheduledTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateScheduledTasksResponse`
        """
        http_info = self._update_scheduled_tasks_http_info(request)
        return self._call_api(**http_info)

    def update_scheduled_tasks_invoker(self, request):
        http_info = self._update_scheduled_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_scheduled_tasks_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/scheduled-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScheduledTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def batch_delete_screen_records(self, request):
        r"""批量删除录屏记录

        批量删除录屏记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteScreenRecords
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteScreenRecordsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteScreenRecordsResponse`
        """
        http_info = self._batch_delete_screen_records_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_screen_records_invoker(self, request):
        http_info = self._batch_delete_screen_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_screen_records_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/screen-records/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteScreenRecordsResponse"
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
            ['application/json;charset=utf-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_desktop_operations(self, request):
        r"""查询桌面关键事件列表

        查询桌面关键事件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopOperations
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopOperationsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopOperationsResponse`
        """
        http_info = self._list_desktop_operations_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_operations_invoker(self, request):
        http_info = self._list_desktop_operations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktop_operations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/screen-records/{record_id}/os-operations",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopOperationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'event_id' in local_var_params:
            query_params.append(('event_id', local_var_params['event_id']))
        if 'event_level' in local_var_params:
            query_params.append(('event_level', local_var_params['event_level']))
        if 'event_data' in local_var_params:
            query_params.append(('event_data', local_var_params['event_data']))
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

    def list_download_address(self, request):
        r"""查询下载地址列表

        查询下载地址列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDownloadAddress
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDownloadAddressRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDownloadAddressResponse`
        """
        http_info = self._list_download_address_http_info(request)
        return self._call_api(**http_info)

    def list_download_address_invoker(self, request):
        http_info = self._list_download_address_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_download_address_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/screen-records/download-address",
            "request_type": request.__class__.__name__,
            "response_type": "ListDownloadAddressResponse"
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
            ['application/json;charset=utf-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_screen_records(self, request):
        r"""查询录屏记录列表

        查询录屏记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScreenRecords
        :type request: :class:`huaweicloudsdkworkspace.v2.ListScreenRecordsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListScreenRecordsResponse`
        """
        http_info = self._list_screen_records_http_info(request)
        return self._call_api(**http_info)

    def list_screen_records_invoker(self, request):
        http_info = self._list_screen_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_screen_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/screen-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListScreenRecordsResponse"
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
        if 'desktop_id' in local_var_params:
            query_params.append(('desktop_id', local_var_params['desktop_id']))
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_screen_record(self, request):
        r"""查询录屏详情

        查询录屏详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScreenRecord
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowScreenRecordRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowScreenRecordResponse`
        """
        http_info = self._show_screen_record_http_info(request)
        return self._call_api(**http_info)

    def show_screen_record_invoker(self, request):
        http_info = self._show_screen_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_screen_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/screen-records/{record_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScreenRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

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

    def create_script(self, request):
        r"""新增脚本

        新增脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScript
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateScriptRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateScriptResponse`
        """
        http_info = self._create_script_http_info(request)
        return self._call_api(**http_info)

    def create_script_invoker(self, request):
        http_info = self._create_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScriptResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_script(self, request):
        r"""删除脚本

        删除脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScript
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteScriptRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteScriptResponse`
        """
        http_info = self._delete_script_http_info(request)
        return self._call_api(**http_info)

    def delete_script_invoker(self, request):
        http_info = self._delete_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_script_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def execute_script_or_command(self, request):
        r"""批量执行脚本或命令

        批量执行脚本或命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteScriptOrCommand
        :type request: :class:`huaweicloudsdkworkspace.v2.ExecuteScriptOrCommandRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExecuteScriptOrCommandResponse`
        """
        http_info = self._execute_script_or_command_http_info(request)
        return self._call_api(**http_info)

    def execute_script_or_command_invoker(self, request):
        http_info = self._execute_script_or_command_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_script_or_command_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/script-executions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteScriptOrCommandResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_script_records(self, request):
        r"""查询脚本执行记录列表

        查询脚本执行记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScriptRecords
        :type request: :class:`huaweicloudsdkworkspace.v2.ListScriptRecordsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListScriptRecordsResponse`
        """
        http_info = self._list_script_records_http_info(request)
        return self._call_api(**http_info)

    def list_script_records_invoker(self, request):
        http_info = self._list_script_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_script_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/script-execution-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptRecordsResponse"
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
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
            collection_formats['resource_id'] = 'csv'
        if 'resource_group_id' in local_var_params:
            query_params.append(('resource_group_id', local_var_params['resource_group_id']))
            collection_formats['resource_group_id'] = 'csv'
        if 'script_id' in local_var_params:
            query_params.append(('script_id', local_var_params['script_id']))
            collection_formats['script_id'] = 'csv'
        if 'script_name' in local_var_params:
            query_params.append(('script_name', local_var_params['script_name']))
            collection_formats['script_name'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'is_first_order' in local_var_params:
            query_params.append(('is_first_order', local_var_params['is_first_order']))
        if 'script_task_id' in local_var_params:
            query_params.append(('script_task_id', local_var_params['script_task_id']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'show_history' in local_var_params:
            query_params.append(('show_history', local_var_params['show_history']))
        if 'execute_time_start' in local_var_params:
            query_params.append(('execute_time_start', local_var_params['execute_time_start']))
        if 'execute_time_end' in local_var_params:
            query_params.append(('execute_time_end', local_var_params['execute_time_end']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_script_tasks(self, request):
        r"""查询脚本任务列表

        查询脚本任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScriptTasks
        :type request: :class:`huaweicloudsdkworkspace.v2.ListScriptTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListScriptTasksResponse`
        """
        http_info = self._list_script_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_script_tasks_invoker(self, request):
        http_info = self._list_script_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_script_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/script-execution-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptTasksResponse"
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
        if 'resource_group_id' in local_var_params:
            query_params.append(('resource_group_id', local_var_params['resource_group_id']))
            collection_formats['resource_group_id'] = 'csv'
        if 'script_id' in local_var_params:
            query_params.append(('script_id', local_var_params['script_id']))
        if 'script_name' in local_var_params:
            query_params.append(('script_name', local_var_params['script_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'resource_group_type' in local_var_params:
            query_params.append(('resource_group_type', local_var_params['resource_group_type']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'csv'
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'execute_time_start' in local_var_params:
            query_params.append(('execute_time_start', local_var_params['execute_time_start']))
        if 'execute_time_end' in local_var_params:
            query_params.append(('execute_time_end', local_var_params['execute_time_end']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_scripts(self, request):
        r"""查询脚本列表

        查询脚本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScripts
        :type request: :class:`huaweicloudsdkworkspace.v2.ListScriptsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListScriptsResponse`
        """
        http_info = self._list_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_scripts_invoker(self, request):
        http_info = self._list_scripts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scripts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def retry_script_execution(self, request):
        r"""重试脚本或执行脚本失败的任务

        重试脚本或执行脚本失败的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryScriptExecution
        :type request: :class:`huaweicloudsdkworkspace.v2.RetryScriptExecutionRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.RetryScriptExecutionResponse`
        """
        http_info = self._retry_script_execution_http_info(request)
        return self._call_api(**http_info)

    def retry_script_execution_invoker(self, request):
        http_info = self._retry_script_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_script_execution_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/script-executions/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryScriptExecutionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_script_detail(self, request):
        r"""查询脚本详情

        查询脚本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScriptDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowScriptDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowScriptDetailResponse`
        """
        http_info = self._show_script_detail_http_info(request)
        return self._call_api(**http_info)

    def show_script_detail_invoker(self, request):
        http_info = self._show_script_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_script_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScriptDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []
        if 'script_task_id' in local_var_params:
            query_params.append(('script_task_id', local_var_params['script_task_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_script_record_detail(self, request):
        r"""查询脚本执行记录详情

        查询脚本执行记录详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScriptRecordDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowScriptRecordDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowScriptRecordDetailResponse`
        """
        http_info = self._show_script_record_detail_http_info(request)
        return self._call_api(**http_info)

    def show_script_record_detail_invoker(self, request):
        http_info = self._show_script_record_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_script_record_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/script-execution-records/{record_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScriptRecordDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_script_execution(self, request):
        r"""停止脚本或者命令执行任务

        停止脚本或者命令执行任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopScriptExecution
        :type request: :class:`huaweicloudsdkworkspace.v2.StopScriptExecutionRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.StopScriptExecutionResponse`
        """
        http_info = self._stop_script_execution_http_info(request)
        return self._call_api(**http_info)

    def stop_script_execution_invoker(self, request):
        http_info = self._stop_script_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_script_execution_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/script-executions/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopScriptExecutionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_script(self, request):
        r"""更新脚本

        更新脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateScript
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateScriptRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateScriptResponse`
        """
        http_info = self._update_script_http_info(request)
        return self._call_api(**http_info)

    def update_script_invoker(self, request):
        http_info = self._update_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_script_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_desktop_sub_resources(self, request):
        r"""桌面购买附属资源

        存量桌面购买附属资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDesktopSubResources
        :type request: :class:`huaweicloudsdkworkspace.v2.AddDesktopSubResourcesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddDesktopSubResourcesResponse`
        """
        http_info = self._add_desktop_sub_resources_http_info(request)
        return self._call_api(**http_info)

    def add_desktop_sub_resources_invoker(self, request):
        http_info = self._add_desktop_sub_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_desktop_sub_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop/sub-resources",
            "request_type": request.__class__.__name__,
            "response_type": "AddDesktopSubResourcesResponse"
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

    def delete_desktop_sub_resources(self, request):
        r"""桌面删除附属资源

        桌面删除附属资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDesktopSubResources
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopSubResourcesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopSubResourcesResponse`
        """
        http_info = self._delete_desktop_sub_resources_http_info(request)
        return self._call_api(**http_info)

    def delete_desktop_sub_resources_invoker(self, request):
        http_info = self._delete_desktop_sub_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_desktop_sub_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktop/delete-sub-resources",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDesktopSubResourcesResponse"
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

    def show_share_space_config(self, request):
        r"""查询协同桌面默认用户配置

        查询协同桌面默认用户配置（当前功能公测中,需要使用请联系管理员申请使用）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowShareSpaceConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowShareSpaceConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowShareSpaceConfigResponse`
        """
        http_info = self._show_share_space_config_http_info(request)
        return self._call_api(**http_info)

    def show_share_space_config_invoker(self, request):
        http_info = self._show_share_space_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_share_space_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/share-space/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ShowShareSpaceConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def update_share_space_config(self, request):
        r"""设置协同桌面默认用户配置

        设置协同桌面默认用户配置（当前功能公测中，需要使用请联系管理员申请使用）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateShareSpaceConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateShareSpaceConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateShareSpaceConfigResponse`
        """
        http_info = self._update_share_space_config_http_info(request)
        return self._call_api(**http_info)

    def update_share_space_config_invoker(self, request):
        http_info = self._update_share_space_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_share_space_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/share-space/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateShareSpaceConfigResponse"
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

    def add_site(self, request):
        r"""新增站点

        用于查询站点信息的接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddSite
        :type request: :class:`huaweicloudsdkworkspace.v2.AddSiteRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddSiteResponse`
        """
        http_info = self._add_site_http_info(request)
        return self._call_api(**http_info)

    def add_site_invoker(self, request):
        http_info = self._add_site_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_site_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sites",
            "request_type": request.__class__.__name__,
            "response_type": "AddSiteResponse"
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

    def delete_site(self, request):
        r"""删除站点

        用于删除站点的接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSite
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteSiteRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteSiteResponse`
        """
        http_info = self._delete_site_http_info(request)
        return self._call_api(**http_info)

    def delete_site_invoker(self, request):
        http_info = self._delete_site_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_site_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/sites/{site_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSiteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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

    def list_site_configs(self, request):
        r"""查询站点信息

        用于查询站点信息的接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSiteConfigs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListSiteConfigsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListSiteConfigsResponse`
        """
        http_info = self._list_site_configs_http_info(request)
        return self._call_api(**http_info)

    def list_site_configs_invoker(self, request):
        http_info = self._list_site_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_site_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sites",
            "request_type": request.__class__.__name__,
            "response_type": "ListSiteConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))
        if 'site_type' in local_var_params:
            query_params.append(('site_type', local_var_params['site_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_wks_edge_sites(self, request):
        r"""查询边缘小站列表

        查询边缘小站列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWksEdgeSites
        :type request: :class:`huaweicloudsdkworkspace.v2.ListWksEdgeSitesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListWksEdgeSitesResponse`
        """
        http_info = self._list_wks_edge_sites_http_info(request)
        return self._call_api(**http_info)

    def list_wks_edge_sites_invoker(self, request):
        http_info = self._list_wks_edge_sites_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_wks_edge_sites_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/wks-edge-sites",
            "request_type": request.__class__.__name__,
            "response_type": "ListWksEdgeSitesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))
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

    def update_access_mode(self, request):
        r"""修改站点接入方式

        用于修改站点接入方式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccessMode
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateAccessModeRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAccessModeResponse`
        """
        http_info = self._update_access_mode_http_info(request)
        return self._call_api(**http_info)

    def update_access_mode_invoker(self, request):
        http_info = self._update_access_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_access_mode_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/sites/{site_id}/access-mode",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccessModeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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

    def update_subnet_ids(self, request):
        r"""修改站点业务子网

        用于修改站点业务子网。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubnetIds
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetIdsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetIdsResponse`
        """
        http_info = self._update_subnet_ids_http_info(request)
        return self._call_api(**http_info)

    def update_subnet_ids_invoker(self, request):
        http_info = self._update_subnet_ids_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_subnet_ids_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/sites/{site_id}/subnet-ids",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubnetIdsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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

    def batch_create_desktop_snapshot(self, request):
        r"""批量创建快照

        批量创建快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateDesktopSnapshot
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchCreateDesktopSnapshotRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchCreateDesktopSnapshotResponse`
        """
        http_info = self._batch_create_desktop_snapshot_http_info(request)
        return self._call_api(**http_info)

    def batch_create_desktop_snapshot_invoker(self, request):
        http_info = self._batch_create_desktop_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_desktop_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/snapshots/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateDesktopSnapshotResponse"
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

    def batch_delete_desktop_snapshot(self, request):
        r"""批量删除快照

        批量删除快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteDesktopSnapshot
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopSnapshotRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteDesktopSnapshotResponse`
        """
        http_info = self._batch_delete_desktop_snapshot_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_desktop_snapshot_invoker(self, request):
        http_info = self._batch_delete_desktop_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_desktop_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/snapshots/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDesktopSnapshotResponse"
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

    def batch_restore_desktop_snapshot(self, request):
        r"""批量恢复快照

        批量恢快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRestoreDesktopSnapshot
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchRestoreDesktopSnapshotRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchRestoreDesktopSnapshotResponse`
        """
        http_info = self._batch_restore_desktop_snapshot_http_info(request)
        return self._call_api(**http_info)

    def batch_restore_desktop_snapshot_invoker(self, request):
        http_info = self._batch_restore_desktop_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_restore_desktop_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/snapshots/batch-restore",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRestoreDesktopSnapshotResponse"
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

    def list_desktop_snapshot(self, request):
        r"""查询快照列表

        查询快照列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopSnapshot
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopSnapshotRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopSnapshotResponse`
        """
        http_info = self._list_desktop_snapshot_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_snapshot_invoker(self, request):
        http_info = self._list_desktop_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktop_snapshot_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'desktop_id' in local_var_params:
            query_params.append(('desktop_id', local_var_params['desktop_id']))
        if 'desktop_name' in local_var_params:
            query_params.append(('desktop_name', local_var_params['desktop_name']))
        if 'snapshot_name' in local_var_params:
            query_params.append(('snapshot_name', local_var_params['snapshot_name']))
        if 'disk_type' in local_var_params:
            query_params.append(('disk_type', local_var_params['disk_type']))
        if 'create_type' in local_var_params:
            query_params.append(('create_type', local_var_params['create_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
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

    def add_metric_notify_rule(self, request):
        r"""新增通知规则

        新增对应指标的通知规则;对应指标满足相应的规则条件时发送通知
        同一指标的规则不允许重复;
        统计指标名称，目前仅支持固定值：desktop_idle_duration
          * &#x60;desktop_idle_duration&#x60; -  桌面空闲时长, 仅允许设置 &#39;&gt;&#x3D;&#39; 阈值
        注：需先为云服务添加委托授权，否则无法正常发送通知到SMN
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddMetricNotifyRule
        :type request: :class:`huaweicloudsdkworkspace.v2.AddMetricNotifyRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddMetricNotifyRuleResponse`
        """
        http_info = self._add_metric_notify_rule_http_info(request)
        return self._call_api(**http_info)

    def add_metric_notify_rule_invoker(self, request):
        http_info = self._add_metric_notify_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_metric_notify_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/statistics/notify-rules",
            "request_type": request.__class__.__name__,
            "response_type": "AddMetricNotifyRuleResponse"
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

    def delete_metric_notify_rule(self, request):
        r"""删除通知规则

        删除对应指标的通知规则;对应指标满足相应的规则条件时发送通知
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMetricNotifyRule
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteMetricNotifyRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteMetricNotifyRuleResponse`
        """
        http_info = self._delete_metric_notify_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_metric_notify_rule_invoker(self, request):
        http_info = self._delete_metric_notify_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_metric_notify_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/statistics/notify-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMetricNotifyRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def list_app_user_access_data(self, request):
        r"""查询云应用接入统计数据

        查询云应用接入统计数据，一次最多查询30天，支持最近30天的数据查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppUserAccessData
        :type request: :class:`huaweicloudsdkworkspace.v2.ListAppUserAccessDataRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListAppUserAccessDataResponse`
        """
        http_info = self._list_app_user_access_data_http_info(request)
        return self._call_api(**http_info)

    def list_app_user_access_data_invoker(self, request):
        http_info = self._list_app_user_access_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_user_access_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/metrics/app-user-access",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppUserAccessDataResponse"
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
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
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

    def list_desktop_usage_metric(self, request):
        r"""查询桌面使用情况统计数据

        查询桌面使用统计信息;
        云服务每天凌晨02:00进行聚合运算前一天00:00:00~23:59:59的使用时长,并将周期范围内的数据聚合到周期边界上
        跨天的记录会按照统计周期进行计算
        假设一天内桌面登录多次，09:00~12:00,13:00~21:00,22:00~01:00(次日):
        则当天的累计使用时长数据会被汇聚到23:59:59这个点;总使用时长为 3hours(09:00~12:00)+8hours(13:00~21:00)+2hours(22:00~00:00)
        仅能查询最近180天已进行汇聚计算的数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopUsageMetric
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopUsageMetricRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopUsageMetricResponse`
        """
        http_info = self._list_desktop_usage_metric_http_info(request)
        return self._call_api(**http_info)

    def list_desktop_usage_metric_invoker(self, request):
        http_info = self._list_desktop_usage_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktop_usage_metric_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/metrics/desktops",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopUsageMetricResponse"
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
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'min_idle_days' in local_var_params:
            query_params.append(('min_idle_days', local_var_params['min_idle_days']))
        if 'max_idle_days' in local_var_params:
            query_params.append(('max_idle_days', local_var_params['max_idle_days']))
        if 'usage_min_hours' in local_var_params:
            query_params.append(('usage_min_hours', local_var_params['usage_min_hours']))
        if 'usage_max_hours' in local_var_params:
            query_params.append(('usage_max_hours', local_var_params['usage_max_hours']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
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

    def list_desktops_statistics(self, request):
        r"""桌面统计

        统计租户下的普通桌面、桌面池状态，默认仅统计总数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDesktopsStatistics
        :type request: :class:`huaweicloudsdkworkspace.v2.ListDesktopsStatisticsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListDesktopsStatisticsResponse`
        """
        http_info = self._list_desktops_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_desktops_statistics_invoker(self, request):
        http_info = self._list_desktops_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_desktops_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListDesktopsStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'desktop_type' in local_var_params:
            query_params.append(('desktop_type', local_var_params['desktop_type']))
            collection_formats['desktop_type'] = 'csv'
        if 'statistics_type' in local_var_params:
            query_params.append(('statistics_type', local_var_params['statistics_type']))
            collection_formats['statistics_type'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_login_state(self, request):
        r"""登录状态统计

        查询租户桌面登录状态统计。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLoginState
        :type request: :class:`huaweicloudsdkworkspace.v2.ListLoginStateRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListLoginStateResponse`
        """
        http_info = self._list_login_state_http_info(request)
        return self._call_api(**http_info)

    def list_login_state_invoker(self, request):
        http_info = self._list_login_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_login_state_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/statistics/login-state",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoginStateResponse"
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

    def list_metric_notify_record(self, request):
        r"""查询对应指标维度是否存在满足通知规则的记录

        查询对应指标维度是否存在满足通知规则的记录;
        查询结果仅表示满足相应指标维度下对应通知规则可产生的通知记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetricNotifyRecord
        :type request: :class:`huaweicloudsdkworkspace.v2.ListMetricNotifyRecordRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListMetricNotifyRecordResponse`
        """
        http_info = self._list_metric_notify_record_http_info(request)
        return self._call_api(**http_info)

    def list_metric_notify_record_invoker(self, request):
        http_info = self._list_metric_notify_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metric_notify_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/notification-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricNotifyRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
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

    def list_metric_notify_rule(self, request):
        r"""查询通知规则

        查询对应指标的通知规则;。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetricNotifyRule
        :type request: :class:`huaweicloudsdkworkspace.v2.ListMetricNotifyRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListMetricNotifyRuleResponse`
        """
        http_info = self._list_metric_notify_rule_http_info(request)
        return self._call_api(**http_info)

    def list_metric_notify_rule_invoker(self, request):
        http_info = self._list_metric_notify_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metric_notify_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/notify-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricNotifyRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
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

    def list_metrics(self, request):
        r"""查询指标

        查询指标。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetrics
        :type request: :class:`huaweicloudsdkworkspace.v2.ListMetricsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListMetricsResponse`
        """
        http_info = self._list_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_metrics_invoker(self, request):
        http_info = self._list_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricsResponse"
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
        if 'dim' in local_var_params:
            query_params.append(('dim', local_var_params['dim']))
        if 'metric_names' in local_var_params:
            query_params.append(('metric_names', local_var_params['metric_names']))
            collection_formats['metric_names'] = 'csv'
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_metrics_trend(self, request):
        r"""查询指标趋势

        查询指标趋势。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetricsTrend
        :type request: :class:`huaweicloudsdkworkspace.v2.ListMetricsTrendRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListMetricsTrendResponse`
        """
        http_info = self._list_metrics_trend_http_info(request)
        return self._call_api(**http_info)

    def list_metrics_trend_invoker(self, request):
        http_info = self._list_metrics_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metrics_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/metrics/trend",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricsTrendResponse"
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
        if 'dim' in local_var_params:
            query_params.append(('dim', local_var_params['dim']))
        if 'metric_names' in local_var_params:
            query_params.append(('metric_names', local_var_params['metric_names']))
            collection_formats['metric_names'] = 'csv'
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_run_state(self, request):
        r"""运行状态统计

        租户桌面运行状态统计。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRunState
        :type request: :class:`huaweicloudsdkworkspace.v2.ListRunStateRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListRunStateResponse`
        """
        http_info = self._list_run_state_http_info(request)
        return self._call_api(**http_info)

    def list_run_state_invoker(self, request):
        http_info = self._list_run_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_run_state_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/desktops/statistics/run-state",
            "request_type": request.__class__.__name__,
            "response_type": "ListRunStateResponse"
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

    def list_unused_desktops(self, request):
        r"""查询在指定时间段未使用的桌面

        查询在指定时间段未使用的桌面。已废弃，不推荐使用。统计数据推荐使用[查询桌面使用情况统计数据接口](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api&#x3D;ListDesktopUsageMetric)和[查询用户使用统计数据接口](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api&#x3D;ListUserUsageMetric)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUnusedDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUnusedDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUnusedDesktopsResponse`
        """
        http_info = self._list_unused_desktops_http_info(request)
        return self._call_api(**http_info)

    def list_unused_desktops_invoker(self, request):
        http_info = self._list_unused_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_unused_desktops_http_info(cls, request):
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

    def list_used_desktop_info(self, request):
        r"""查询使用桌面的时长

        查询使用桌面的时长。已废弃，不推荐使用。统计数据推荐使用[查询桌面使用情况统计数据接口](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api&#x3D;ListDesktopUsageMetric)和[查询用户使用统计数据接口](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api&#x3D;ListUserUsageMetric)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsedDesktopInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsedDesktopInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsedDesktopInfoResponse`
        """
        http_info = self._list_used_desktop_info_http_info(request)
        return self._call_api(**http_info)

    def list_used_desktop_info_invoker(self, request):
        http_info = self._list_used_desktop_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_used_desktop_info_http_info(cls, request):
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

    def list_user_usage_metric(self, request):
        r"""查询用户使用统计数据

        查询用户使用统计信息;
        最多查询30天内的数据;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserUsageMetric
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserUsageMetricRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserUsageMetricResponse`
        """
        http_info = self._list_user_usage_metric_http_info(request)
        return self._call_api(**http_info)

    def list_user_usage_metric_invoker(self, request):
        http_info = self._list_user_usage_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_usage_metric_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/metrics/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserUsageMetricResponse"
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
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))
        if 'usage_min_hours' in local_var_params:
            query_params.append(('usage_min_hours', local_var_params['usage_min_hours']))
        if 'usage_max_hours' in local_var_params:
            query_params.append(('usage_max_hours', local_var_params['usage_max_hours']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
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

    def show_growth_rate(self, request):
        r"""查询指标环比值

        查询指标环比值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGrowthRate
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowGrowthRateRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowGrowthRateResponse`
        """
        http_info = self._show_growth_rate_http_info(request)
        return self._call_api(**http_info)

    def show_growth_rate_invoker(self, request):
        http_info = self._show_growth_rate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_growth_rate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/growth-rate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGrowthRateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'grow_period' in local_var_params:
            query_params.append(('grow_period', local_var_params['grow_period']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'dim' in local_var_params:
            query_params.append(('dim', local_var_params['dim']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_user_access_stages(self, request):
        r"""查询接入云桌面或云应用各阶段时长数据

        查询接入云桌面或云应用各阶段时长数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserAccessStages
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowUserAccessStagesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowUserAccessStagesResponse`
        """
        http_info = self._show_user_access_stages_http_info(request)
        return self._call_api(**http_info)

    def show_user_access_stages_invoker(self, request):
        http_info = self._show_user_access_stages_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_access_stages_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/metrics/access-stages",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserAccessStagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'transaction_id' in local_var_params:
            query_params.append(('transaction_id', local_var_params['transaction_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_metric_notify_rule(self, request):
        r"""更新通知规则

        更新对应指标的通知规则;对应指标满足相应的规则条件时发送通知。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMetricNotifyRule
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateMetricNotifyRuleRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateMetricNotifyRuleResponse`
        """
        http_info = self._update_metric_notify_rule_http_info(request)
        return self._call_api(**http_info)

    def update_metric_notify_rule_invoker(self, request):
        http_info = self._update_metric_notify_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_metric_notify_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/statistics/notify-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMetricNotifyRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_available_ip(self, request):
        r"""根据子网id查询该子网下可用的ip

        根据子网id查询该子网下可用的ip。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAvailableIp
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowAvailableIpRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowAvailableIpResponse`
        """
        http_info = self._show_available_ip_http_info(request)
        return self._call_api(**http_info)

    def show_available_ip_invoker(self, request):
        http_info = self._show_available_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_available_ip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/subnets/{subnet_id}/available-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAvailableIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def list_tenant_configs(self, request):
        r"""查询租户个性配置列表

        查询租户个性配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTenantConfigs
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTenantConfigsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTenantConfigsResponse`
        """
        http_info = self._list_tenant_configs_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_configs_invoker(self, request):
        http_info = self._list_tenant_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tenant_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/tenant-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def update_tenant_config(self, request):
        r"""修改租户个性配置

        租户个性配置修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTenantConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateTenantConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTenantConfigResponse`
        """
        http_info = self._update_tenant_config_http_info(request)
        return self._call_api(**http_info)

    def update_tenant_config_invoker(self, request):
        http_info = self._update_tenant_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_tenant_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/tenant-configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTenantConfigResponse"
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

    def create_terminals_binding_desktops(self, request):
        r"""增加终端与桌面绑定配置

        增加终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsResponse`
        """
        http_info = self._create_terminals_binding_desktops_http_info(request)
        return self._call_api(**http_info)

    def create_terminals_binding_desktops_invoker(self, request):
        http_info = self._create_terminals_binding_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_terminals_binding_desktops_http_info(cls, request):
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

    def delete_terminals_binding_desktops(self, request):
        r"""删除终端与桌面绑定配置

        删除终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsResponse`
        """
        http_info = self._delete_terminals_binding_desktops_http_info(request)
        return self._call_api(**http_info)

    def delete_terminals_binding_desktops_invoker(self, request):
        http_info = self._delete_terminals_binding_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_terminals_binding_desktops_http_info(cls, request):
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

    def list_terminals_binding_desktops(self, request):
        r"""查询终端与桌面绑定配置列表

        查询终端与桌面绑定配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsResponse`
        """
        http_info = self._list_terminals_binding_desktops_http_info(request)
        return self._call_api(**http_info)

    def list_terminals_binding_desktops_invoker(self, request):
        http_info = self._list_terminals_binding_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_terminals_binding_desktops_http_info(cls, request):
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

    def list_terminals_binding_desktops_config(self, request):
        r"""查询终端与桌面绑定的开关配置信息

        查询终端与桌面绑定的开关配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTerminalsBindingDesktopsConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListTerminalsBindingDesktopsConfigResponse`
        """
        http_info = self._list_terminals_binding_desktops_config_http_info(request)
        return self._call_api(**http_info)

    def list_terminals_binding_desktops_config_invoker(self, request):
        http_info = self._list_terminals_binding_desktops_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_terminals_binding_desktops_config_http_info(cls, request):
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

    def update_terminals_binding_desktops(self, request):
        r"""修改终端与桌面绑定配置

        修改终端与桌面绑定配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTerminalsBindingDesktops
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsResponse`
        """
        http_info = self._update_terminals_binding_desktops_http_info(request)
        return self._call_api(**http_info)

    def update_terminals_binding_desktops_invoker(self, request):
        http_info = self._update_terminals_binding_desktops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_terminals_binding_desktops_http_info(cls, request):
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

    def update_terminals_binding_desktops_config(self, request):
        r"""设置终端与桌面绑定的开关配置

        设置终端与桌面绑定的开关配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTerminalsBindingDesktopsConfig
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTerminalsBindingDesktopsConfigResponse`
        """
        http_info = self._update_terminals_binding_desktops_config_http_info(request)
        return self._call_api(**http_info)

    def update_terminals_binding_desktops_config_invoker(self, request):
        http_info = self._update_terminals_binding_desktops_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_terminals_binding_desktops_config_http_info(cls, request):
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

    def batch_create_users(self, request):
        r"""批量创建用户

        该接口用于批量创建用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateUsers
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchCreateUsersRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchCreateUsersResponse`
        """
        http_info = self._batch_create_users_http_info(request)
        return self._call_api(**http_info)

    def batch_create_users_invoker(self, request):
        http_info = self._batch_create_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_users_http_info(cls, request):
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

    def batch_delete_otp_devices(self, request):
        r"""解绑OTP设备

        该接口用于解绑用户的OTP设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteOtpDevices
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteOtpDevicesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteOtpDevicesResponse`
        """
        http_info = self._batch_delete_otp_devices_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_otp_devices_invoker(self, request):
        http_info = self._batch_delete_otp_devices_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_otp_devices_http_info(cls, request):
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

    def batch_delete_user(self, request):
        r"""批量删除用户

        该接口用于批量删除桌面用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteUser
        :type request: :class:`huaweicloudsdkworkspace.v2.BatchDeleteUserRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchDeleteUserResponse`
        """
        http_info = self._batch_delete_user_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_user_invoker(self, request):
        http_info = self._batch_delete_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/users/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteUserResponse"
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

    def change_user_status(self, request):
        r"""操作用户

        该接口用于操作用户，包含三种操作：锁定、解锁和重置密码（重置密码建议使用/v2/{project_id}/users/{user_id}/random-password接口，在没有通知方式的情况下必须使用/v2/{project_id}/users/{user_id}/random-password接口）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeUserStatus
        :type request: :class:`huaweicloudsdkworkspace.v2.ChangeUserStatusRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ChangeUserStatusResponse`
        """
        http_info = self._change_user_status_http_info(request)
        return self._call_api(**http_info)

    def change_user_status_invoker(self, request):
        http_info = self._change_user_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_user_status_http_info(cls, request):
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

    def create_desktop_user(self, request):
        r"""创建用户

        该接口用于创建桌面用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDesktopUser
        :type request: :class:`huaweicloudsdkworkspace.v2.CreateDesktopUserRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopUserResponse`
        """
        http_info = self._create_desktop_user_http_info(request)
        return self._call_api(**http_info)

    def create_desktop_user_invoker(self, request):
        http_info = self._create_desktop_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_desktop_user_http_info(cls, request):
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

    def delete_user(self, request):
        r"""删除指定用户

        删除指定的桌面用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_user_http_info(cls, request):
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

    def list_otp_devices_by_user_id(self, request):
        r"""查询OTP设备

        该接口用于查询相应用户下面的OTP设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOtpDevicesByUserId
        :type request: :class:`huaweicloudsdkworkspace.v2.ListOtpDevicesByUserIdRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListOtpDevicesByUserIdResponse`
        """
        http_info = self._list_otp_devices_by_user_id_http_info(request)
        return self._call_api(**http_info)

    def list_otp_devices_by_user_id_invoker(self, request):
        http_info = self._list_otp_devices_by_user_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_otp_devices_by_user_id_http_info(cls, request):
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

    def list_user_detail(self, request):
        r"""查询用户详情信息

        该接口用于查询指定的桌面用户详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserDetail
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserDetailResponse`
        """
        http_info = self._list_user_detail_http_info(request)
        return self._call_api(**http_info)

    def list_user_detail_invoker(self, request):
        http_info = self._list_user_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_detail_http_info(cls, request):
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

    def list_users(self, request):
        r"""查询用户列表

        该接口用于查询桌面用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_users_http_info(cls, request):
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
        if 'share_space_subscription' in local_var_params:
            query_params.append(('share_space_subscription', local_var_params['share_space_subscription']))
        if 'share_space_desktops' in local_var_params:
            query_params.append(('share_space_desktops', local_var_params['share_space_desktops']))
        if 'is_query_total_desktops' in local_var_params:
            query_params.append(('is_query_total_desktops', local_var_params['is_query_total_desktops']))
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

    def reset_random_password(self, request):
        r"""给用户重置随机密码

        该接口用于给用户重置一个密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetRandomPassword
        :type request: :class:`huaweicloudsdkworkspace.v2.ResetRandomPasswordRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResetRandomPasswordResponse`
        """
        http_info = self._reset_random_password_http_info(request)
        return self._call_api(**http_info)

    def reset_random_password_invoker(self, request):
        http_info = self._reset_random_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_random_password_http_info(cls, request):
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

    def send_email(self, request):
        r"""重新发送邮件

        该接口用于重新发送邮件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendEmail
        :type request: :class:`huaweicloudsdkworkspace.v2.SendEmailRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.SendEmailResponse`
        """
        http_info = self._send_email_http_info(request)
        return self._call_api(**http_info)

    def send_email_invoker(self, request):
        http_info = self._send_email_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_email_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/users/{user_id}/resend-email",
            "request_type": request.__class__.__name__,
            "response_type": "SendEmailResponse"
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

    def update_user_info(self, request):
        r"""修改用户信息

        该接口用于修改桌面用户信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateUserInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateUserInfoResponse`
        """
        http_info = self._update_user_info_http_info(request)
        return self._call_api(**http_info)

    def update_user_info_invoker(self, request):
        http_info = self._update_user_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_info_http_info(cls, request):
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

    def list_user_events(self, request):
        r"""查询用户事件

        查询用户事件，一次最多查询30天，支持最近30天的数据查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserEvents
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserEventsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserEventsResponse`
        """
        http_info = self._list_user_events_http_info(request)
        return self._call_api(**http_info)

    def list_user_events_invoker(self, request):
        http_info = self._list_user_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_events_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/user-events",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserEventsResponse"
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
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
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

    def list_user_events_lts_configurations(self, request):
        r"""查询用户事件LTS配置

        查询用户事件LTS配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserEventsLtsConfigurations
        :type request: :class:`huaweicloudsdkworkspace.v2.ListUserEventsLtsConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListUserEventsLtsConfigurationsResponse`
        """
        http_info = self._list_user_events_lts_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_user_events_lts_configurations_invoker(self, request):
        http_info = self._list_user_events_lts_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_events_lts_configurations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/user-events/lts-configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserEventsLtsConfigurationsResponse"
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

    def set_user_events_lts_configurations(self, request):
        r"""配置用户事件LTS

        配置用户事件LTS。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetUserEventsLtsConfigurations
        :type request: :class:`huaweicloudsdkworkspace.v2.SetUserEventsLtsConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.SetUserEventsLtsConfigurationsResponse`
        """
        http_info = self._set_user_events_lts_configurations_http_info(request)
        return self._call_api(**http_info)

    def set_user_events_lts_configurations_invoker(self, request):
        http_info = self._set_user_events_lts_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_user_events_lts_configurations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/user-events/lts-configurations",
            "request_type": request.__class__.__name__,
            "response_type": "SetUserEventsLtsConfigurationsResponse"
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

    def add_desktop_volumes(self, request):
        r"""增加桌面磁盘

        给单个桌面增加磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDesktopVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.AddDesktopVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddDesktopVolumesResponse`
        """
        http_info = self._add_desktop_volumes_http_info(request)
        return self._call_api(**http_info)

    def add_desktop_volumes_invoker(self, request):
        http_info = self._add_desktop_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_desktop_volumes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/volumes",
            "request_type": request.__class__.__name__,
            "response_type": "AddDesktopVolumesResponse"
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

    def add_volumes(self, request):
        r"""批量增加桌面磁盘

        批量增加桌面磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.AddVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddVolumesResponse`
        """
        http_info = self._add_volumes_http_info(request)
        return self._call_api(**http_info)

    def add_volumes_invoker(self, request):
        http_info = self._add_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_volumes_http_info(cls, request):
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

    def delete_desktop_volumes(self, request):
        r"""删除桌面数据盘

        删除桌面数据盘，删除后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDesktopVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteDesktopVolumesResponse`
        """
        http_info = self._delete_desktop_volumes_http_info(request)
        return self._call_api(**http_info)

    def delete_desktop_volumes_invoker(self, request):
        http_info = self._delete_desktop_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_desktop_volumes_http_info(cls, request):
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

    def expand_desktop_volume(self, request):
        r"""扩容磁盘

        扩容磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandDesktopVolume
        :type request: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopVolumeRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopVolumeResponse`
        """
        http_info = self._expand_desktop_volume_http_info(request)
        return self._call_api(**http_info)

    def expand_desktop_volume_invoker(self, request):
        http_info = self._expand_desktop_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_desktop_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/desktops/{desktop_id}/volumes/{volume_id}/expand",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandDesktopVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'desktop_id' in local_var_params:
            path_params['desktop_id'] = local_var_params['desktop_id']
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def expand_volumes(self, request):
        r"""扩容桌面磁盘

        扩容桌面磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandVolumes
        :type request: :class:`huaweicloudsdkworkspace.v2.ExpandVolumesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExpandVolumesResponse`
        """
        http_info = self._expand_volumes_http_info(request)
        return self._call_api(**http_info)

    def expand_volumes_invoker(self, request):
        http_info = self._expand_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_volumes_http_info(cls, request):
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

    def list_volume_product_info(self, request):
        r"""查询磁盘产品信息

        查询磁盘产品信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVolumeProductInfo
        :type request: :class:`huaweicloudsdkworkspace.v2.ListVolumeProductInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListVolumeProductInfoResponse`
        """
        http_info = self._list_volume_product_info_http_info(request)
        return self._call_api(**http_info)

    def list_volume_product_info_invoker(self, request):
        http_info = self._list_volume_product_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_volume_product_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/volume/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListVolumeProductInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'volume_type' in local_var_params:
            query_params.append(('volume_type', local_var_params['volume_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def apply_workspace(self, request):
        r"""开通云办公服务

        该接口用于开通云办公服务。
        
        作为异步接口，调用成功说明云办公服务后台收到了开通请求，但服务是否开通成功需要通过任务查询接口(GET /v2/{project_id}/workspace-sub-jobs)查询该任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.ApplyWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyWorkspaceResponse`
        """
        http_info = self._apply_workspace_http_info(request)
        return self._call_api(**http_info)

    def apply_workspace_invoker(self, request):
        http_info = self._apply_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_workspace_http_info(cls, request):
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

    def cancel_workspace(self, request):
        r"""注销云办公服务

        该接口用于注销云办公服务。注销前请确保当前用户下的云桌面已经删除，注销后无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.CancelWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.CancelWorkspaceResponse`
        """
        http_info = self._cancel_workspace_http_info(request)
        return self._call_api(**http_info)

    def cancel_workspace_invoker(self, request):
        http_info = self._cancel_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_workspace_http_info(cls, request):
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

    def list_workspaces(self, request):
        r"""查询云办公服务详情

        该接口用于查询云办公服务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkspaces
        :type request: :class:`huaweicloudsdkworkspace.v2.ListWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListWorkspacesResponse`
        """
        http_info = self._list_workspaces_http_info(request)
        return self._call_api(**http_info)

    def list_workspaces_invoker(self, request):
        http_info = self._list_workspaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workspaces_http_info(cls, request):
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

    def show_workspace_lock(self, request):
        r"""查询云办公服务是否被锁定

        查询云办公服务是否被锁定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkspaceLock
        :type request: :class:`huaweicloudsdkworkspace.v2.ShowWorkspaceLockRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.ShowWorkspaceLockResponse`
        """
        http_info = self._show_workspace_lock_http_info(request)
        return self._call_api(**http_info)

    def show_workspace_lock_invoker(self, request):
        http_info = self._show_workspace_lock_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_workspace_lock_http_info(cls, request):
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

    def unlock_workspace(self, request):
        r"""解除云办公服务锁定状态

        该接口目前支持解除云办公服务锁定状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnlockWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.UnlockWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UnlockWorkspaceResponse`
        """
        http_info = self._unlock_workspace_http_info(request)
        return self._call_api(**http_info)

    def unlock_workspace_invoker(self, request):
        http_info = self._unlock_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unlock_workspace_http_info(cls, request):
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

    def update_enterprise_id(self, request):
        r"""修改企业ID

        修改租户的企业ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEnterpriseId
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateEnterpriseIdRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateEnterpriseIdResponse`
        """
        http_info = self._update_enterprise_id_http_info(request)
        return self._call_api(**http_info)

    def update_enterprise_id_invoker(self, request):
        http_info = self._update_enterprise_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_enterprise_id_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/enterprise-id",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEnterpriseIdResponse"
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

    def update_workspace(self, request):
        r"""修改云办公服务属性

        该接口目前支持修改云办公服务属性。单次请求仅支持修改一种属性类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkspace
        :type request: :class:`huaweicloudsdkworkspace.v2.UpdateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateWorkspaceResponse`
        """
        http_info = self._update_workspace_http_info(request)
        return self._call_api(**http_info)

    def update_workspace_invoker(self, request):
        http_info = self._update_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_workspace_http_info(cls, request):
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
