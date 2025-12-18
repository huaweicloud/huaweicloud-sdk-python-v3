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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkddm'")


class DdmClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkddm.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DdmClient":
                raise TypeError("client type error, support client type is DdmClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def change_database_version(self, request):
        r"""变更内核版本

        变更内核版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeDatabaseVersion
        :type request: :class:`huaweicloudsdkddm.v1.ChangeDatabaseVersionRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ChangeDatabaseVersionResponse`
        """
        http_info = self._change_database_version_http_info(request)
        return self._call_api(**http_info)

    def change_database_version_invoker(self, request):
        http_info = self._change_database_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_database_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database-version/change-version",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeDatabaseVersionResponse"
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

    def create_ddm_configurations(self, request):
        r"""创建参数组

        创建参数组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDdmConfigurations
        :type request: :class:`huaweicloudsdkddm.v1.CreateDdmConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateDdmConfigurationsResponse`
        """
        http_info = self._create_ddm_configurations_http_info(request)
        return self._call_api(**http_info)

    def create_ddm_configurations_invoker(self, request):
        http_info = self._create_ddm_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ddm_configurations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDdmConfigurationsResponse"
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

    def delete_configuration(self, request):
        r"""删除参数组

        删除参数组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfiguration
        :type request: :class:`huaweicloudsdkddm.v1.DeleteConfigurationRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteConfigurationResponse`
        """
        http_info = self._delete_configuration_http_info(request)
        return self._call_api(**http_info)

    def delete_configuration_invoker(self, request):
        http_info = self._delete_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_configuration_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/configurations/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def list_database_available_versions(self, request):
        r"""查询可变更内核版本

        查询可变更内核版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseAvailableVersions
        :type request: :class:`huaweicloudsdkddm.v1.ListDatabaseAvailableVersionsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListDatabaseAvailableVersionsResponse`
        """
        http_info = self._list_database_available_versions_http_info(request)
        return self._call_api(**http_info)

    def list_database_available_versions_invoker(self, request):
        http_info = self._list_database_available_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_database_available_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database-version/available-versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseAvailableVersionsResponse"
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

    def list_ddm_configurations(self, request):
        r"""获取参数模板列表

        获取参数模板列表，包括所有DDM的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDdmConfigurations
        :type request: :class:`huaweicloudsdkddm.v1.ListDdmConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListDdmConfigurationsResponse`
        """
        http_info = self._list_ddm_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_ddm_configurations_invoker(self, request):
        http_info = self._list_ddm_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ddm_configurations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListDdmConfigurationsResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def modify_configuration(self, request):
        r"""修改实例参数

        修改实例参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyConfiguration
        :type request: :class:`huaweicloudsdkddm.v1.ModifyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ModifyConfigurationResponse`
        """
        http_info = self._modify_configuration_http_info(request)
        return self._call_api(**http_info)

    def modify_configuration_invoker(self, request):
        http_info = self._modify_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyConfigurationResponse"
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

    def roll_back_database_version(self, request):
        r"""回滚内核版本

        回滚内核版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollBackDatabaseVersion
        :type request: :class:`huaweicloudsdkddm.v1.RollBackDatabaseVersionRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RollBackDatabaseVersionResponse`
        """
        http_info = self._roll_back_database_version_http_info(request)
        return self._call_api(**http_info)

    def roll_back_database_version_invoker(self, request):
        http_info = self._roll_back_database_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _roll_back_database_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database-version/rollback-version",
            "request_type": request.__class__.__name__,
            "response_type": "RollBackDatabaseVersionResponse"
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

    def show_configuration(self, request):
        r"""获取指定参数模板的参数

        获取指定参数模板的参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfiguration
        :type request: :class:`huaweicloudsdkddm.v1.ShowConfigurationRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowConfigurationResponse`
        """
        http_info = self._show_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_invoker(self, request):
        http_info = self._show_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def show_risk_info(self, request):
        r"""内核版本风险提醒

        内核版本风险提醒
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRiskInfo
        :type request: :class:`huaweicloudsdkddm.v1.ShowRiskInfoRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowRiskInfoResponse`
        """
        http_info = self._show_risk_info_http_info(request)
        return self._call_api(**http_info)

    def show_risk_info_invoker(self, request):
        http_info = self._show_risk_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_risk_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/show-risk-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRiskInfoResponse"
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

    def list_api_version(self, request):
        r"""查询API版本列表

        查询API版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersion
        :type request: :class:`huaweicloudsdkddm.v1.ListApiVersionRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListApiVersionResponse`
        """
        http_info = self._list_api_version_http_info(request)
        return self._call_api(**http_info)

    def list_api_version_invoker(self, request):
        http_info = self._list_api_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionResponse"
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

    def batch_delete_nodes(self, request):
        r"""批量删除实例的节点

        批量删除实例的节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteNodes
        :type request: :class:`huaweicloudsdkddm.v1.BatchDeleteNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.BatchDeleteNodesResponse`
        """
        http_info = self._batch_delete_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_nodes_invoker(self, request):
        http_info = self._batch_delete_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_nodes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteNodesResponse"
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

    def bind_eip(self, request):
        r"""绑定弹性公网IP

        绑定弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BindEip
        :type request: :class:`huaweicloudsdkddm.v1.BindEipRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.BindEipResponse`
        """
        http_info = self._bind_eip_http_info(request)
        return self._call_api(**http_info)

    def bind_eip_invoker(self, request):
        http_info = self._bind_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _bind_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/eip",
            "request_type": request.__class__.__name__,
            "response_type": "BindEipResponse"
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

    def cancel_migration(self, request):
        r"""取消分片变更

        取消分片变更
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelMigration
        :type request: :class:`huaweicloudsdkddm.v1.CancelMigrationRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CancelMigrationResponse`
        """
        http_info = self._cancel_migration_http_info(request)
        return self._call_api(**http_info)

    def cancel_migration_invoker(self, request):
        http_info = self._cancel_migration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_migration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/jobs/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelMigrationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']
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

    def change_strategy(self, request):
        r"""修改切换路由策略

        修改切换路由策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeStrategy
        :type request: :class:`huaweicloudsdkddm.v1.ChangeStrategyRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ChangeStrategyResponse`
        """
        http_info = self._change_strategy_http_info(request)
        return self._call_api(**http_info)

    def change_strategy_invoker(self, request):
        http_info = self._change_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_strategy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/jobs/{job_id}/route-switch-strategy",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']
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

    def check_migrate_logic_db(self, request):
        r"""分片变更预校验

        分片变更预校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckMigrateLogicDb
        :type request: :class:`huaweicloudsdkddm.v1.CheckMigrateLogicDbRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CheckMigrateLogicDbResponse`
        """
        http_info = self._check_migrate_logic_db_http_info(request)
        return self._call_api(**http_info)

    def check_migrate_logic_db_invoker(self, request):
        http_info = self._check_migrate_logic_db_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_migrate_logic_db_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/precheck",
            "request_type": request.__class__.__name__,
            "response_type": "CheckMigrateLogicDbResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']

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

    def check_preliminary_results(self, request):
        r"""查询分片变更预校验异步结果

        查询分片变更预校验异步结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckPreliminaryResults
        :type request: :class:`huaweicloudsdkddm.v1.CheckPreliminaryResultsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CheckPreliminaryResultsResponse`
        """
        http_info = self._check_preliminary_results_http_info(request)
        return self._call_api(**http_info)

    def check_preliminary_results_invoker(self, request):
        http_info = self._check_preliminary_results_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_preliminary_results_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/precheck/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckPreliminaryResultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']
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

    def clean_migration(self, request):
        r"""清理分片变更

        清理分片变更
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CleanMigration
        :type request: :class:`huaweicloudsdkddm.v1.CleanMigrationRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CleanMigrationResponse`
        """
        http_info = self._clean_migration_http_info(request)
        return self._call_api(**http_info)

    def clean_migration_invoker(self, request):
        http_info = self._clean_migration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _clean_migration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/jobs/{job_id}/clean",
            "request_type": request.__class__.__name__,
            "response_type": "CleanMigrationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']
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

    def create_database(self, request):
        r"""创建DDM逻辑库

        创建DDM逻辑库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabase
        :type request: :class:`huaweicloudsdkddm.v1.CreateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateDatabaseResponse`
        """
        http_info = self._create_database_http_info(request)
        return self._call_api(**http_info)

    def create_database_invoker(self, request):
        http_info = self._create_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseResponse"
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

    def create_ddm_database(self, request):
        r"""创建DDM逻辑库

        创建DDM逻辑库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDdmDatabase
        :type request: :class:`huaweicloudsdkddm.v1.CreateDdmDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateDdmDatabaseResponse`
        """
        http_info = self._create_ddm_database_http_info(request)
        return self._call_api(**http_info)

    def create_ddm_database_invoker(self, request):
        http_info = self._create_ddm_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ddm_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDdmDatabaseResponse"
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

    def create_ddm_instance(self, request):
        r"""购买创建DDM实例

        购买创建DDM实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDdmInstance
        :type request: :class:`huaweicloudsdkddm.v1.CreateDdmInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateDdmInstanceResponse`
        """
        http_info = self._create_ddm_instance_http_info(request)
        return self._call_api(**http_info)

    def create_ddm_instance_invoker(self, request):
        http_info = self._create_ddm_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ddm_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDdmInstanceResponse"
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

    def create_group(self, request):
        r"""创建组

        创建组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGroup
        :type request: :class:`huaweicloudsdkddm.v1.CreateGroupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateGroupResponse`
        """
        http_info = self._create_group_http_info(request)
        return self._call_api(**http_info)

    def create_group_invoker(self, request):
        http_info = self._create_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupResponse"
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

    def create_instance(self, request):
        r"""购买DDM实例

        创建一个DDM实例。
        
        DDM运行于虚拟私有云。申请DDM实例前，需保证有可用的虚拟私有云，并且已配置好子网与安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkddm.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
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

    def create_users(self, request):
        r"""创建DDM帐号

        DDM帐号用于连接和管理逻辑库。一个DDM实例最多能创建100个DDM帐号，一个DDM帐号可以关联多个逻辑库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUsers
        :type request: :class:`huaweicloudsdkddm.v1.CreateUsersRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateUsersResponse`
        """
        http_info = self._create_users_http_info(request)
        return self._call_api(**http_info)

    def create_users_invoker(self, request):
        http_info = self._create_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_users_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUsersResponse"
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

    def delete_backup(self, request):
        r"""删除备份

        删除备份
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBackup
        :type request: :class:`huaweicloudsdkddm.v1.DeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteBackupResponse`
        """
        http_info = self._delete_backup_http_info(request)
        return self._call_api(**http_info)

    def delete_backup_invoker(self, request):
        http_info = self._delete_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_backup_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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

    def delete_database(self, request):
        r"""删除DDM逻辑库

        删除指定的逻辑库，释放该逻辑库的所有资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabase
        :type request: :class:`huaweicloudsdkddm.v1.DeleteDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteDatabaseResponse`
        """
        http_info = self._delete_database_http_info(request)
        return self._call_api(**http_info)

    def delete_database_invoker(self, request):
        http_info = self._delete_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/databases/{ddm_dbname}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ddm_dbname' in local_var_params:
            path_params['ddm_dbname'] = local_var_params['ddm_dbname']

        query_params = []
        if 'delete_rds_data' in local_var_params:
            query_params.append(('delete_rds_data', local_var_params['delete_rds_data']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_ddm_database(self, request):
        r"""删除逻辑库

        删除指定的逻辑库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDdmDatabase
        :type request: :class:`huaweicloudsdkddm.v1.DeleteDdmDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteDdmDatabaseResponse`
        """
        http_info = self._delete_ddm_database_http_info(request)
        return self._call_api(**http_info)

    def delete_ddm_database_invoker(self, request):
        http_info = self._delete_ddm_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ddm_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDdmDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'delete_dn_data' in local_var_params:
            query_params.append(('delete_dn_data', local_var_params['delete_dn_data']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_ddm_instance(self, request):
        r"""删除DDM实例

        删除指定的DDM实例，释放该实例的所有资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDdmInstance
        :type request: :class:`huaweicloudsdkddm.v1.DeleteDdmInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteDdmInstanceResponse`
        """
        http_info = self._delete_ddm_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_ddm_instance_invoker(self, request):
        http_info = self._delete_ddm_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ddm_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDdmInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'delete_dn_data' in local_var_params:
            query_params.append(('delete_dn_data', local_var_params['delete_dn_data']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_group(self, request):
        r"""删除实例组

        删除实例组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGroup
        :type request: :class:`huaweicloudsdkddm.v1.DeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteGroupResponse`
        """
        http_info = self._delete_group_http_info(request)
        return self._call_api(**http_info)

    def delete_group_invoker(self, request):
        http_info = self._delete_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_instance(self, request):
        r"""删除DDM实例

        删除指定的DDM实例，释放该实例的所有资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkddm.v1.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'delete_rds_data' in local_var_params:
            query_params.append(('delete_rds_data', local_var_params['delete_rds_data']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_nodes(self, request):
        r"""删除实例的节点

        删除实例的节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNodes
        :type request: :class:`huaweicloudsdkddm.v1.DeleteNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteNodesResponse`
        """
        http_info = self._delete_nodes_http_info(request)
        return self._call_api(**http_info)

    def delete_nodes_invoker(self, request):
        http_info = self._delete_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_nodes_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNodesResponse"
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

    def delete_user(self, request):
        r"""删除DDM帐号

        删除指定的DDM实例帐号，如果帐号关联了逻辑库，则对应的关联关系也会删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkddm.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteUserResponse`
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
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users/{username}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']

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

    def download_schema_metadata(self, request):
        r"""导出逻辑库元数据

        导出所有逻辑库物理分片在数据节点上的分布关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadSchemaMetadata
        :type request: :class:`huaweicloudsdkddm.v1.DownloadSchemaMetadataRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DownloadSchemaMetadataResponse`
        """
        http_info = self._download_schema_metadata_http_info(request)
        return self._call_api(**http_info)

    def download_schema_metadata_invoker(self, request):
        http_info = self._download_schema_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_schema_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/schema-metadata",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadSchemaMetadataResponse"
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

    def execute_kill_logical_processes(self, request):
        r"""kill逻辑会话

        kill逻辑会话
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteKillLogicalProcesses
        :type request: :class:`huaweicloudsdkddm.v1.ExecuteKillLogicalProcessesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ExecuteKillLogicalProcessesResponse`
        """
        http_info = self._execute_kill_logical_processes_http_info(request)
        return self._call_api(**http_info)

    def execute_kill_logical_processes_invoker(self, request):
        http_info = self._execute_kill_logical_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_kill_logical_processes_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/logical-processes",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteKillLogicalProcessesResponse"
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

    def execute_kill_physical_processes(self, request):
        r"""kill物理会话

        kill物理会话
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteKillPhysicalProcesses
        :type request: :class:`huaweicloudsdkddm.v1.ExecuteKillPhysicalProcessesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ExecuteKillPhysicalProcessesResponse`
        """
        http_info = self._execute_kill_physical_processes_http_info(request)
        return self._call_api(**http_info)

    def execute_kill_physical_processes_invoker(self, request):
        http_info = self._execute_kill_physical_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_kill_physical_processes_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/physical-processes",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteKillPhysicalProcessesResponse"
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

    def expand_ddm_instance_nodes(self, request):
        r"""DDM实例节点扩容

        对指定的DDM实例的节点个数进行扩容，支持按需实例与包周期实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandDdmInstanceNodes
        :type request: :class:`huaweicloudsdkddm.v1.ExpandDdmInstanceNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ExpandDdmInstanceNodesResponse`
        """
        http_info = self._expand_ddm_instance_nodes_http_info(request)
        return self._call_api(**http_info)

    def expand_ddm_instance_nodes_invoker(self, request):
        http_info = self._expand_ddm_instance_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_ddm_instance_nodes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandDdmInstanceNodesResponse"
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

    def expand_instance_nodes(self, request):
        r"""DDM实例节点扩容

        对指定的DDM实例的节点个数进行扩容，支持按需实例与包周期实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandInstanceNodes
        :type request: :class:`huaweicloudsdkddm.v1.ExpandInstanceNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ExpandInstanceNodesResponse`
        """
        http_info = self._expand_instance_nodes_http_info(request)
        return self._call_api(**http_info)

    def expand_instance_nodes_invoker(self, request):
        http_info = self._expand_instance_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_instance_nodes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/action/enlarge",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandInstanceNodesResponse"
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

    def list_available_rds(self, request):
        r"""查询创建逻辑库可选取的数据节点实例列表

        查询创建逻辑库可选取的数据节点实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableRds
        :type request: :class:`huaweicloudsdkddm.v1.ListAvailableRdsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListAvailableRdsResponse`
        """
        http_info = self._list_available_rds_http_info(request)
        return self._call_api(**http_info)

    def list_available_rds_invoker(self, request):
        http_info = self._list_available_rds_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_rds_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/available-data-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableRdsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_available_rds_for_migrate(self, request):
        r"""查询分片变更可选取的数据节点实例列表

        查询分片变更可选取的数据节点实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableRdsForMigrate
        :type request: :class:`huaweicloudsdkddm.v1.ListAvailableRdsForMigrateRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListAvailableRdsForMigrateResponse`
        """
        http_info = self._list_available_rds_for_migrate_http_info(request)
        return self._call_api(**http_info)

    def list_available_rds_for_migrate_invoker(self, request):
        http_info = self._list_available_rds_for_migrate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_rds_for_migrate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/available-data-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableRdsForMigrateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']

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

    def list_available_rds_list(self, request):
        r"""查询创建逻辑库可选取的数据库实例列表

        查询创建逻辑库可选取的数据库实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableRdsList
        :type request: :class:`huaweicloudsdkddm.v1.ListAvailableRdsListRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListAvailableRdsListResponse`
        """
        http_info = self._list_available_rds_list_http_info(request)
        return self._call_api(**http_info)

    def list_available_rds_list_invoker(self, request):
        http_info = self._list_available_rds_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_rds_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/rds",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableRdsListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_backups(self, request):
        r"""获取备份列表

        获取备份列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackups
        :type request: :class:`huaweicloudsdkddm.v1.ListBackupsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListBackupsResponse`
        """
        http_info = self._list_backups_http_info(request)
        return self._call_api(**http_info)

    def list_backups_invoker(self, request):
        http_info = self._list_backups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_backups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
        if 'backup_name' in local_var_params:
            query_params.append(('backup_name', local_var_params['backup_name']))
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

    def list_databases(self, request):
        r"""查询DDM逻辑库列表

        查询DDM逻辑库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkddm.v1.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListDatabasesResponse`
        """
        http_info = self._list_databases_http_info(request)
        return self._call_api(**http_info)

    def list_databases_invoker(self, request):
        http_info = self._list_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_ddm_engines(self, request):
        r"""查询DDM引擎信息

        查询DDM引擎信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDdmEngines
        :type request: :class:`huaweicloudsdkddm.v1.ListDdmEnginesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListDdmEnginesResponse`
        """
        http_info = self._list_ddm_engines_http_info(request)
        return self._call_api(**http_info)

    def list_ddm_engines_invoker(self, request):
        http_info = self._list_ddm_engines_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ddm_engines_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/engines",
            "request_type": request.__class__.__name__,
            "response_type": "ListDdmEnginesResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ddm_flavors(self, request):
        r"""查询DDM可用区规格信息

        查询DDM可用区规格信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDdmFlavors
        :type request: :class:`huaweicloudsdkddm.v1.ListDdmFlavorsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListDdmFlavorsResponse`
        """
        http_info = self._list_ddm_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_ddm_flavors_invoker(self, request):
        http_info = self._list_ddm_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ddm_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListDdmFlavorsResponse"
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
        if 'engine_id' in local_var_params:
            query_params.append(('engine_id', local_var_params['engine_id']))
        if 'engine_version' in local_var_params:
            query_params.append(('engine_version', local_var_params['engine_version']))
        if 'available_zones' in local_var_params:
            query_params.append(('available_zones', local_var_params['available_zones']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_engines(self, request):
        r"""查询DDM引擎信息

        查询DDM引擎信息详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEngines
        :type request: :class:`huaweicloudsdkddm.v1.ListEnginesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListEnginesResponse`
        """
        http_info = self._list_engines_http_info(request)
        return self._call_api(**http_info)

    def list_engines_invoker(self, request):
        http_info = self._list_engines_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_engines_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/engines",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnginesResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""查询DDM可用区规格信息

        查询DDM可用区规格信息详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkddm.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListFlavorsResponse`
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
            "resource_path": "/v2/{project_id}/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_id' in local_var_params:
            query_params.append(('engine_id', local_var_params['engine_id']))
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

    def list_group(self, request):
        r"""获取实例组信息列表

        获取实例组信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroup
        :type request: :class:`huaweicloudsdkddm.v1.ListGroupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListGroupResponse`
        """
        http_info = self._list_group_http_info(request)
        return self._call_api(**http_info)

    def list_group_invoker(self, request):
        http_info = self._list_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_instances(self, request):
        r"""查询DDM实例列表

        查询DDM实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkddm.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_nodes(self, request):
        r"""查询DDM实例节点列表

        查询DDM实例节点列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNodes
        :type request: :class:`huaweicloudsdkddm.v1.ListNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListNodesResponse`
        """
        http_info = self._list_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_nodes_invoker(self, request):
        http_info = self._list_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_nodes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_read_write_ratio(self, request):
        r"""读写比例监控

        查询指定时间段内在DDM实例的读写次数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReadWriteRatio
        :type request: :class:`huaweicloudsdkddm.v1.ListReadWriteRatioRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListReadWriteRatioResponse`
        """
        http_info = self._list_read_write_ratio_http_info(request)
        return self._call_api(**http_info)

    def list_read_write_ratio_invoker(self, request):
        http_info = self._list_read_write_ratio_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_read_write_ratio_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/read-write-ratio",
            "request_type": request.__class__.__name__,
            "response_type": "ListReadWriteRatioResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('perPage', local_var_params['per_page']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_slow_log(self, request):
        r"""慢日志监控

        查询指定时间段内在DDM实例上执行过的慢sql相关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLog
        :type request: :class:`huaweicloudsdkddm.v1.ListSlowLogRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListSlowLogResponse`
        """
        http_info = self._list_slow_log_http_info(request)
        return self._call_api(**http_info)

    def list_slow_log_invoker(self, request):
        http_info = self._list_slow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/slowlog",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('perPage', local_var_params['per_page']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_slow_logs(self, request):
        r"""慢日志监控

        查询指定时间段内在DDM实例上执行过的慢sql相关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLogs
        :type request: :class:`huaweicloudsdkddm.v1.ListSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListSlowLogsResponse`
        """
        http_info = self._list_slow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_slow_logs_invoker(self, request):
        http_info = self._list_slow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tasks(self, request):
        r"""查询任务列表

        查询任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkddm.v1.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListTasksResponse`
        """
        http_info = self._list_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_invoker(self, request):
        http_info = self._list_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksResponse"
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

    def list_users(self, request):
        r"""查询DDM帐号列表

        查询DDM帐号列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkddm.v1.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListUsersResponse`
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
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def migrate_logic_db(self, request):
        r"""分片变更

        分片变更
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateLogicDb
        :type request: :class:`huaweicloudsdkddm.v1.MigrateLogicDbRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.MigrateLogicDbResponse`
        """
        http_info = self._migrate_logic_db_http_info(request)
        return self._call_api(**http_info)

    def migrate_logic_db_invoker(self, request):
        http_info = self._migrate_logic_db_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_logic_db_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateLogicDbResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']

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

    def migrate_results(self, request):
        r"""查询分片变更任务详情

        查询分片变更任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateResults
        :type request: :class:`huaweicloudsdkddm.v1.MigrateResultsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.MigrateResultsResponse`
        """
        http_info = self._migrate_results_http_info(request)
        return self._call_api(**http_info)

    def migrate_results_invoker(self, request):
        http_info = self._migrate_results_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_results_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateResultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']
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

    def modify_eip(self, request):
        r"""修改实例的ELB IP

        修改实例的ELB IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyEip
        :type request: :class:`huaweicloudsdkddm.v1.ModifyEipRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ModifyEipResponse`
        """
        http_info = self._modify_eip_http_info(request)
        return self._call_api(**http_info)

    def modify_eip_invoker(self, request):
        http_info = self._modify_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_eip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/elb/ip",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyEipResponse"
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

    def rebuild_config(self, request):
        r"""DDM表数据重载

        DDM实例跨region容灾场景下，针对目标DDM实例实现表数据reload，使数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebuildConfig
        :type request: :class:`huaweicloudsdkddm.v1.RebuildConfigRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RebuildConfigResponse`
        """
        http_info = self._rebuild_config_http_info(request)
        return self._call_api(**http_info)

    def rebuild_config_invoker(self, request):
        http_info = self._rebuild_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rebuild_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/reload-config",
            "request_type": request.__class__.__name__,
            "response_type": "RebuildConfigResponse"
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

    def reset_administrator(self, request):
        r"""DDM管理员账号密码管理

        首次调用时新建DDM管理员帐号并设置密码。后续调用时仅更新管理员密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetAdministrator
        :type request: :class:`huaweicloudsdkddm.v1.ResetAdministratorRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ResetAdministratorResponse`
        """
        http_info = self._reset_administrator_http_info(request)
        return self._call_api(**http_info)

    def reset_administrator_invoker(self, request):
        http_info = self._reset_administrator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_administrator_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/admin-user",
            "request_type": request.__class__.__name__,
            "response_type": "ResetAdministratorResponse"
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

    def reset_user_password(self, request):
        r"""重置DDM账号密码

        重置现有DDM帐号的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetUserPassword
        :type request: :class:`huaweicloudsdkddm.v1.ResetUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ResetUserPasswordResponse`
        """
        http_info = self._reset_user_password_http_info(request)
        return self._call_api(**http_info)

    def reset_user_password_invoker(self, request):
        http_info = self._reset_user_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_user_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users/{username}/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetUserPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']

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

    def resize_flavor(self, request):
        r"""变更DDM实例规格

        变更DDM实例规格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeFlavor
        :type request: :class:`huaweicloudsdkddm.v1.ResizeFlavorRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ResizeFlavorResponse`
        """
        http_info = self._resize_flavor_http_info(request)
        return self._call_api(**http_info)

    def resize_flavor_invoker(self, request):
        http_info = self._resize_flavor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_flavor_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/flavor",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeFlavorResponse"
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

    def restart_ddm_instance(self, request):
        r"""重启DDM实例

        重启DDM实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartDdmInstance
        :type request: :class:`huaweicloudsdkddm.v1.RestartDdmInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RestartDdmInstanceResponse`
        """
        http_info = self._restart_ddm_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_ddm_instance_invoker(self, request):
        http_info = self._restart_ddm_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_ddm_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartDdmInstanceResponse"
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

    def restart_instance(self, request):
        r"""重启DDM实例

        重启指定的DDM实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartInstance
        :type request: :class:`huaweicloudsdkddm.v1.RestartInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RestartInstanceResponse`
        """
        http_info = self._restart_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_instance_invoker(self, request):
        http_info = self._restart_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "RestartInstanceResponse"
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

    def restart_node(self, request):
        r"""重启DDM节点

        重启DDM节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartNode
        :type request: :class:`huaweicloudsdkddm.v1.RestartNodeRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RestartNodeResponse`
        """
        http_info = self._restart_node_http_info(request)
        return self._call_api(**http_info)

    def restart_node_invoker(self, request):
        http_info = self._restart_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def restore2_exist(self, request):
        r"""恢复到新实例

        恢复到新实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Restore2Exist
        :type request: :class:`huaweicloudsdkddm.v1.Restore2ExistRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.Restore2ExistResponse`
        """
        http_info = self._restore2_exist_http_info(request)
        return self._call_api(**http_info)

    def restore2_exist_invoker(self, request):
        http_info = self._restore2_exist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore2_exist_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/recovery",
            "request_type": request.__class__.__name__,
            "response_type": "Restore2ExistResponse"
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

    def restore_metadata(self, request):
        r"""元数据恢复

        元数据恢复
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreMetadata
        :type request: :class:`huaweicloudsdkddm.v1.RestoreMetadataRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RestoreMetadataResponse`
        """
        http_info = self._restore_metadata_http_info(request)
        return self._call_api(**http_info)

    def restore_metadata_invoker(self, request):
        http_info = self._restore_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_metadata_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/metadata-recovery",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreMetadataResponse"
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

    def retry_migration(self, request):
        r"""重试分片变更

        重试分片变更
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryMigration
        :type request: :class:`huaweicloudsdkddm.v1.RetryMigrationRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RetryMigrationResponse`
        """
        http_info = self._retry_migration_http_info(request)
        return self._call_api(**http_info)

    def retry_migration_invoker(self, request):
        http_info = self._retry_migration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_migration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/jobs/{job_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryMigrationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']
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

    def rollback_migration(self, request):
        r"""回滚分片变更

        回滚分片变更
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollbackMigration
        :type request: :class:`huaweicloudsdkddm.v1.RollbackMigrationRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RollbackMigrationResponse`
        """
        http_info = self._rollback_migration_http_info(request)
        return self._call_api(**http_info)

    def rollback_migration_invoker(self, request):
        http_info = self._rollback_migration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rollback_migration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/jobs/{job_id}/rollback",
            "request_type": request.__class__.__name__,
            "response_type": "RollbackMigrationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']
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

    def show_avalible_ddms(self, request):
        r"""查询可用于恢复的实例列表

        查询可用于恢复的实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAvalibleDdms
        :type request: :class:`huaweicloudsdkddm.v1.ShowAvalibleDdmsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowAvalibleDdmsResponse`
        """
        http_info = self._show_avalible_ddms_http_info(request)
        return self._call_api(**http_info)

    def show_avalible_ddms_invoker(self, request):
        http_info = self._show_avalible_ddms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_avalible_ddms_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/restorable-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAvalibleDdmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_avalible_rds(self, request):
        r"""查询可用于时间点恢复的数据节点列表

        查询可用于时间点恢复的数据节点列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAvalibleRds
        :type request: :class:`huaweicloudsdkddm.v1.ShowAvalibleRdsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowAvalibleRdsResponse`
        """
        http_info = self._show_avalible_rds_http_info(request)
        return self._call_api(**http_info)

    def show_avalible_rds_invoker(self, request):
        http_info = self._show_avalible_rds_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_avalible_rds_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/restorable-data-node",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAvalibleRdsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'target_instance_id' in local_var_params:
            query_params.append(('target_instance_id', local_var_params['target_instance_id']))
        if 'source_dn_instance_id' in local_var_params:
            query_params.append(('source_dn_instance_id', local_var_params['source_dn_instance_id']))
        if 'restore_time' in local_var_params:
            query_params.append(('restore_time', local_var_params['restore_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_avalible_time(self, request):
        r"""查询可恢复时间段

        查询可恢复时间段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAvalibleTime
        :type request: :class:`huaweicloudsdkddm.v1.ShowAvalibleTimeRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowAvalibleTimeResponse`
        """
        http_info = self._show_avalible_time_http_info(request)
        return self._call_api(**http_info)

    def show_avalible_time_invoker(self, request):
        http_info = self._show_avalible_time_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_avalible_time_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/restorable-time-interval",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAvalibleTimeResponse"
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

    def show_backup(self, request):
        r"""查询备份详情

        查询备份详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackup
        :type request: :class:`huaweicloudsdkddm.v1.ShowBackupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowBackupResponse`
        """
        http_info = self._show_backup_http_info(request)
        return self._call_api(**http_info)

    def show_backup_invoker(self, request):
        http_info = self._show_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_backup_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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

    def show_database(self, request):
        r"""查询DDM逻辑库详细信息

        查询指定逻辑库的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatabase
        :type request: :class:`huaweicloudsdkddm.v1.ShowDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowDatabaseResponse`
        """
        http_info = self._show_database_http_info(request)
        return self._call_api(**http_info)

    def show_database_invoker(self, request):
        http_info = self._show_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_database_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/databases/{ddm_dbname}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ddm_dbname' in local_var_params:
            path_params['ddm_dbname'] = local_var_params['ddm_dbname']

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

    def show_ddm_job_result(self, request):
        r"""获取指定ID的任务信息

        获取指定ID的任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDdmJobResult
        :type request: :class:`huaweicloudsdkddm.v1.ShowDdmJobResultRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowDdmJobResultResponse`
        """
        http_info = self._show_ddm_job_result_http_info(request)
        return self._call_api(**http_info)

    def show_ddm_job_result_invoker(self, request):
        http_info = self._show_ddm_job_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ddm_job_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDdmJobResultResponse"
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

    def show_ddm_node_detail(self, request):
        r"""查询DDM实例节点详情

        查询DDM实例节点详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDdmNodeDetail
        :type request: :class:`huaweicloudsdkddm.v1.ShowDdmNodeDetailRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowDdmNodeDetailResponse`
        """
        http_info = self._show_ddm_node_detail_http_info(request)
        return self._call_api(**http_info)

    def show_ddm_node_detail_invoker(self, request):
        http_info = self._show_ddm_node_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ddm_node_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDdmNodeDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def show_instance(self, request):
        r"""查询DDM实例详情

        查询指定DDM实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkddm.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
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

    def show_instance_database(self, request):
        r"""查询逻辑库详情

        查询逻辑库详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceDatabase
        :type request: :class:`huaweicloudsdkddm.v1.ShowInstanceDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowInstanceDatabaseResponse`
        """
        http_info = self._show_instance_database_http_info(request)
        return self._call_api(**http_info)

    def show_instance_database_invoker(self, request):
        http_info = self._show_instance_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_database_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def show_instance_param(self, request):
        r"""查询DDM指定实例的参数详情

        查询DDM指定实例的参数详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceParam
        :type request: :class:`huaweicloudsdkddm.v1.ShowInstanceParamRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowInstanceParamResponse`
        """
        http_info = self._show_instance_param_http_info(request)
        return self._call_api(**http_info)

    def show_instance_param_invoker(self, request):
        http_info = self._show_instance_param_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_param_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceParamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_logical_processes(self, request):
        r"""查询逻辑会话列表

        查询逻辑会话列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogicalProcesses
        :type request: :class:`huaweicloudsdkddm.v1.ShowLogicalProcessesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowLogicalProcessesResponse`
        """
        http_info = self._show_logical_processes_http_info(request)
        return self._call_api(**http_info)

    def show_logical_processes_invoker(self, request):
        http_info = self._show_logical_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logical_processes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/logical-processes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogicalProcessesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def show_node(self, request):
        r"""查询DDM实例节点详情

        查询DDM实例节点详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNode
        :type request: :class:`huaweicloudsdkddm.v1.ShowNodeRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowNodeResponse`
        """
        http_info = self._show_node_http_info(request)
        return self._call_api(**http_info)

    def show_node_invoker(self, request):
        http_info = self._show_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_node_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def show_physical_processes(self, request):
        r"""查询物理会话列表

        查询物理会话列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPhysicalProcesses
        :type request: :class:`huaweicloudsdkddm.v1.ShowPhysicalProcessesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowPhysicalProcessesResponse`
        """
        http_info = self._show_physical_processes_http_info(request)
        return self._call_api(**http_info)

    def show_physical_processes_invoker(self, request):
        http_info = self._show_physical_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_physical_processes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/physical-processes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPhysicalProcessesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def show_processes_audit_log(self, request):
        r"""查询kill会话审计日志

        查询kill会话审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProcessesAuditLog
        :type request: :class:`huaweicloudsdkddm.v1.ShowProcessesAuditLogRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowProcessesAuditLogResponse`
        """
        http_info = self._show_processes_audit_log_http_info(request)
        return self._call_api(**http_info)

    def show_processes_audit_log_invoker(self, request):
        http_info = self._show_processes_audit_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_processes_audit_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/processes-audit-log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProcessesAuditLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_public_ip(self, request):
        r"""获取DDM实例绑定的弹性公网IP信息

        获取DDM实例绑定的弹性公网IP信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPublicIp
        :type request: :class:`huaweicloudsdkddm.v1.ShowPublicIpRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowPublicIpResponse`
        """
        http_info = self._show_public_ip_http_info(request)
        return self._call_api(**http_info)

    def show_public_ip_invoker(self, request):
        http_info = self._show_public_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_public_ip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/public-ips",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_related_dns(self, request):
        r"""查询实例在恢复时间点关联的数据节点

        查询实例在恢复时间点关联的数据节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRelatedDns
        :type request: :class:`huaweicloudsdkddm.v1.ShowRelatedDnsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowRelatedDnsResponse`
        """
        http_info = self._show_related_dns_http_info(request)
        return self._call_api(**http_info)

    def show_related_dns_invoker(self, request):
        http_info = self._show_related_dns_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_related_dns_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/related-dn",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRelatedDnsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'restore_time' in local_var_params:
            query_params.append(('restore_time', local_var_params['restore_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def shrink_instance_nodes(self, request):
        r"""DDM实例节点缩容

        对指定的DDM实例的节点个数进行缩容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShrinkInstanceNodes
        :type request: :class:`huaweicloudsdkddm.v1.ShrinkInstanceNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShrinkInstanceNodesResponse`
        """
        http_info = self._shrink_instance_nodes_http_info(request)
        return self._call_api(**http_info)

    def shrink_instance_nodes_invoker(self, request):
        http_info = self._shrink_instance_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _shrink_instance_nodes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/action/reduce",
            "request_type": request.__class__.__name__,
            "response_type": "ShrinkInstanceNodesResponse"
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

    def switch_route(self, request):
        r"""切换路由

        切换路由
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchRoute
        :type request: :class:`huaweicloudsdkddm.v1.SwitchRouteRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.SwitchRouteResponse`
        """
        http_info = self._switch_route_http_info(request)
        return self._call_api(**http_info)

    def switch_route_invoker(self, request):
        http_info = self._switch_route_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_route_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/{db_name}/migration/jobs/{job_id}/route-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchRouteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']
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

    def switch_ssl(self, request):
        r"""为实例设置SSL数据加密

        为实例设置SSL数据加密。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSsl
        :type request: :class:`huaweicloudsdkddm.v1.SwitchSslRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.SwitchSslResponse`
        """
        http_info = self._switch_ssl_http_info(request)
        return self._call_api(**http_info)

    def switch_ssl_invoker(self, request):
        http_info = self._switch_ssl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_ssl_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/switch-ssl",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchSslResponse"
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

    def sync_dn_information(self, request):
        r"""同步数据节点

        同步数据节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SyncDnInformation
        :type request: :class:`huaweicloudsdkddm.v1.SyncDnInformationRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.SyncDnInformationResponse`
        """
        http_info = self._sync_dn_information_http_info(request)
        return self._call_api(**http_info)

    def sync_dn_information_invoker(self, request):
        http_info = self._sync_dn_information_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _sync_dn_information_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/data-nodes/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncDnInformationResponse"
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

    def unbind_eip(self, request):
        r"""解绑弹性公网IP

        解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnbindEip
        :type request: :class:`huaweicloudsdkddm.v1.UnbindEipRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UnbindEipResponse`
        """
        http_info = self._unbind_eip_http_info(request)
        return self._call_api(**http_info)

    def unbind_eip_invoker(self, request):
        http_info = self._unbind_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unbind_eip_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/eip",
            "request_type": request.__class__.__name__,
            "response_type": "UnbindEipResponse"
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

    def update_database_info(self, request):
        r"""同步DN信息

        同步当前DDM实例已关联的所有DN实例配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabaseInfo
        :type request: :class:`huaweicloudsdkddm.v1.UpdateDatabaseInfoRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateDatabaseInfoResponse`
        """
        http_info = self._update_database_info_http_info(request)
        return self._call_api(**http_info)

    def update_database_info_invoker(self, request):
        http_info = self._update_database_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_database_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/rds/sync",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabaseInfoResponse"
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

    def update_instance_name(self, request):
        r"""修改DDM实例名称

        修改DDM实例名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceName
        :type request: :class:`huaweicloudsdkddm.v1.UpdateInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateInstanceNameResponse`
        """
        http_info = self._update_instance_name_http_info(request)
        return self._call_api(**http_info)

    def update_instance_name_invoker(self, request):
        http_info = self._update_instance_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/modify-name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceNameResponse"
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

    def update_instance_param(self, request):
        r"""修改DDM实例参数

        修改DDM实例参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceParam
        :type request: :class:`huaweicloudsdkddm.v1.UpdateInstanceParamRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateInstanceParamResponse`
        """
        http_info = self._update_instance_param_http_info(request)
        return self._call_api(**http_info)

    def update_instance_param_invoker(self, request):
        http_info = self._update_instance_param_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_param_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceParamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_instance_port(self, request):
        r"""修改实例端口

        修改实例端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstancePort
        :type request: :class:`huaweicloudsdkddm.v1.UpdateInstancePortRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateInstancePortResponse`
        """
        http_info = self._update_instance_port_http_info(request)
        return self._call_api(**http_info)

    def update_instance_port_invoker(self, request):
        http_info = self._update_instance_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_port_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/port",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstancePortResponse"
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

    def update_instance_security_group(self, request):
        r"""修改DDM实例安全组

        修改DDM实例安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceSecurityGroup
        :type request: :class:`huaweicloudsdkddm.v1.UpdateInstanceSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateInstanceSecurityGroupResponse`
        """
        http_info = self._update_instance_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_instance_security_group_invoker(self, request):
        http_info = self._update_instance_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/modify-security-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceSecurityGroupResponse"
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

    def update_read_and_write_strategy(self, request):
        r"""修改DDM已关联的数据库实例的读策略

        修改DDM已关联的数据库实例的读策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateReadAndWriteStrategy
        :type request: :class:`huaweicloudsdkddm.v1.UpdateReadAndWriteStrategyRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateReadAndWriteStrategyResponse`
        """
        http_info = self._update_read_and_write_strategy_http_info(request)
        return self._call_api(**http_info)

    def update_read_and_write_strategy_invoker(self, request):
        http_info = self._update_read_and_write_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_read_and_write_strategy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/action/read-write-strategy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReadAndWriteStrategyResponse"
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

    def update_user(self, request):
        r"""修改DDM帐号

        修改现有DDM帐号的权限或者与逻辑库的管理关系。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkddm.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users/{username}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']

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

    def upload_schema_metadata(self, request):
        r"""导入逻辑库元数据

        导入所有逻辑库物理分片分布关系，以此创建相同物理分片分布关系的逻辑库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadSchemaMetadata
        :type request: :class:`huaweicloudsdkddm.v1.UploadSchemaMetadataRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UploadSchemaMetadataResponse`
        """
        http_info = self._upload_schema_metadata_http_info(request)
        return self._call_api(**http_info)

    def upload_schema_metadata_invoker(self, request):
        http_info = self._upload_schema_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_schema_metadata_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/schema-metadata",
            "request_type": request.__class__.__name__,
            "response_type": "UploadSchemaMetadataResponse"
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

    def validate_weak_password(self, request):
        r"""弱密码校验

        弱密码校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateWeakPassword
        :type request: :class:`huaweicloudsdkddm.v1.ValidateWeakPasswordRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ValidateWeakPasswordResponse`
        """
        http_info = self._validate_weak_password_http_info(request)
        return self._call_api(**http_info)

    def validate_weak_password_invoker(self, request):
        http_info = self._validate_weak_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_weak_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/weak-password-verification",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateWeakPasswordResponse"
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

    def check_data_node_connection_v0_v3(self, request):
        r"""rds连通性检查V3

        rds连通性检查V3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDataNodeConnectionV0V3
        :type request: :class:`huaweicloudsdkddm.v1.CheckDataNodeConnectionV0V3Request`
        :rtype: :class:`huaweicloudsdkddm.v1.CheckDataNodeConnectionV0V3Response`
        """
        http_info = self._check_data_node_connection_v0_v3_http_info(request)
        return self._call_api(**http_info)

    def check_data_node_connection_v0_v3_invoker(self, request):
        http_info = self._check_data_node_connection_v0_v3_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_data_node_connection_v0_v3_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/ddm/instance/rds/connection",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDataNodeConnectionV0V3Response"
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

    def compare_parameter_groups(self, request):
        r"""比较参数组V3

        比较参数组V3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareParameterGroups
        :type request: :class:`huaweicloudsdkddm.v1.CompareParameterGroupsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CompareParameterGroupsResponse`
        """
        http_info = self._compare_parameter_groups_http_info(request)
        return self._call_api(**http_info)

    def compare_parameter_groups_invoker(self, request):
        http_info = self._compare_parameter_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _compare_parameter_groups_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/diff",
            "request_type": request.__class__.__name__,
            "response_type": "CompareParameterGroupsResponse"
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

    def copy_parameter_group(self, request):
        r"""复制参数组V3

        复制参数组V3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyParameterGroup
        :type request: :class:`huaweicloudsdkddm.v1.CopyParameterGroupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CopyParameterGroupResponse`
        """
        http_info = self._copy_parameter_group_http_info(request)
        return self._call_api(**http_info)

    def copy_parameter_group_invoker(self, request):
        http_info = self._copy_parameter_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_parameter_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyParameterGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def list_instances_applied_parameter_group_v0_v3(self, request):
        r"""查询可应用的实例列表V3

        查询可应用的实例列表V3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesAppliedParameterGroupV0V3
        :type request: :class:`huaweicloudsdkddm.v1.ListInstancesAppliedParameterGroupV0V3Request`
        :rtype: :class:`huaweicloudsdkddm.v1.ListInstancesAppliedParameterGroupV0V3Response`
        """
        http_info = self._list_instances_applied_parameter_group_v0_v3_http_info(request)
        return self._call_api(**http_info)

    def list_instances_applied_parameter_group_v0_v3_invoker(self, request):
        http_info = self._list_instances_applied_parameter_group_v0_v3_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_applied_parameter_group_v0_v3_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/query-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesAppliedParameterGroupV0V3Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def list_parameter_group_apply_history_v0_v3(self, request):
        r"""参数组应用记录V3

        参数组应用记录V3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListParameterGroupApplyHistoryV0V3
        :type request: :class:`huaweicloudsdkddm.v1.ListParameterGroupApplyHistoryV0V3Request`
        :rtype: :class:`huaweicloudsdkddm.v1.ListParameterGroupApplyHistoryV0V3Response`
        """
        http_info = self._list_parameter_group_apply_history_v0_v3_http_info(request)
        return self._call_api(**http_info)

    def list_parameter_group_apply_history_v0_v3_invoker(self, request):
        http_info = self._list_parameter_group_apply_history_v0_v3_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_parameter_group_apply_history_v0_v3_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/apply-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListParameterGroupApplyHistoryV0V3Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def reset_parameter_group(self, request):
        r"""更新参数组V3

        更新参数组V3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetParameterGroup
        :type request: :class:`huaweicloudsdkddm.v1.ResetParameterGroupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ResetParameterGroupResponse`
        """
        http_info = self._reset_parameter_group_http_info(request)
        return self._call_api(**http_info)

    def reset_parameter_group_invoker(self, request):
        http_info = self._reset_parameter_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_parameter_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetParameterGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def show_ddm_detail(self, request):
        r"""查询实例详情V3

        查询实例详情V3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDdmDetail
        :type request: :class:`huaweicloudsdkddm.v1.ShowDdmDetailRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowDdmDetailResponse`
        """
        http_info = self._show_ddm_detail_http_info(request)
        return self._call_api(**http_info)

    def show_ddm_detail_invoker(self, request):
        http_info = self._show_ddm_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ddm_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDdmDetailResponse"
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
