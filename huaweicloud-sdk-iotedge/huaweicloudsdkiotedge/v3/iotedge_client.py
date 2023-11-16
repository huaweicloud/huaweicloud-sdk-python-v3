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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkiotedge'")


class IoTEdgeClient(Client):
    def __init__(self):
        super(IoTEdgeClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiotedge.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IoTEdgeClient":
                raise TypeError("client type error, support client type is IoTEdgeClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_app(self, request):
        """创建应用模板

        应用服务器可调用此接口为创建批量处理任务，对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结、批量解冻、批量下发同步命令、批量下发异步命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkiotedge.v3.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
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

    def delete_app(self, request):
        """删除应用模板

        应用服务器可调用此接口删除应用模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkiotedge.v3.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.DeleteAppResponse`
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
            "resource_path": "/v3/{project_id}/apps/{app_id}",
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        """查询应用模板列表

        应用服务器可调用此接口查询应用模板列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkiotedge.v3.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ListAppsResponse`
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
            "resource_path": "/v3/{project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'provider_type' in local_var_params:
            query_params.append(('provider_type', local_var_params['provider_type']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
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

    def show_app(self, request):
        """查询应用模板详情

        应用服务器可调用此接口查询物联网平台中指定批量任务的信息，包括任务内容、任务状态、任务完成情况统计以及子任务列表等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkiotedge.v3.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ShowAppResponse`
        """
        http_info = self._show_app_http_info(request)
        return self._call_api(**http_info)

    def show_app_invoker(self, request):
        http_info = self._show_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppResponse"
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
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_app_instance(self, request):
        """创建应用实例

        应用服务器可调用此接口为创建应用实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAppInstance
        :type request: :class:`huaweicloudsdkiotedge.v3.CreateAppInstanceRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.CreateAppInstanceResponse`
        """
        http_info = self._create_app_instance_http_info(request)
        return self._call_api(**http_info)

    def create_app_instance_invoker(self, request):
        http_info = self._create_app_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/clusters/{cluster_id}/app-instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_instance(self, request):
        """删除应用实例

        应用服务器可调用此接口为删除应用实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAppInstance
        :type request: :class:`huaweicloudsdkiotedge.v3.DeleteAppInstanceRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.DeleteAppInstanceResponse`
        """
        http_info = self._delete_app_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_app_instance_invoker(self, request):
        http_info = self._delete_app_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_app_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/clusters/{cluster_id}/app-instances/{app_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'app_instance_id' in local_var_params:
            path_params['app_instance_id'] = local_var_params['app_instance_id']

        query_params = []
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

    def list_app_instance_history(self, request):
        """查询应用实例的历史版本列表

        应用服务器可调用此接口查询应用实例的历史版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppInstanceHistory
        :type request: :class:`huaweicloudsdkiotedge.v3.ListAppInstanceHistoryRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ListAppInstanceHistoryResponse`
        """
        http_info = self._list_app_instance_history_http_info(request)
        return self._call_api(**http_info)

    def list_app_instance_history_invoker(self, request):
        http_info = self._list_app_instance_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_instance_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clusters/{cluster_id}/app-instances/{app_instance_id}/history",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppInstanceHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'app_instance_id' in local_var_params:
            path_params['app_instance_id'] = local_var_params['app_instance_id']

        query_params = []
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

    def list_app_instances(self, request):
        """查询应用实例列表

        应用服务器可调用此接口查询应用实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppInstances
        :type request: :class:`huaweicloudsdkiotedge.v3.ListAppInstancesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ListAppInstancesResponse`
        """
        http_info = self._list_app_instances_http_info(request)
        return self._call_api(**http_info)

    def list_app_instances_invoker(self, request):
        http_info = self._list_app_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clusters/{cluster_id}/app-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def update_app_instance(self, request):
        """更新应用实例

        应用服务器可调用此接口为更新应用实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAppInstance
        :type request: :class:`huaweicloudsdkiotedge.v3.UpdateAppInstanceRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.UpdateAppInstanceResponse`
        """
        http_info = self._update_app_instance_http_info(request)
        return self._call_api(**http_info)

    def update_app_instance_invoker(self, request):
        http_info = self._update_app_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_app_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/clusters/{cluster_id}/app-instances/{app_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'app_instance_id' in local_var_params:
            path_params['app_instance_id'] = local_var_params['app_instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_app_version(self, request):
        """创建应用版本

        应用服务器可调用此接口为创建应用版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAppVersion
        :type request: :class:`huaweicloudsdkiotedge.v3.CreateAppVersionRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.CreateAppVersionResponse`
        """
        http_info = self._create_app_version_http_info(request)
        return self._call_api(**http_info)

    def create_app_version_invoker(self, request):
        http_info = self._create_app_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/apps/{app_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

        header_params = {}

        form_params = {}
        if 'chart' in local_var_params:
            form_params['chart'] = local_var_params['chart']
        if 'images' in local_var_params:
            form_params['images'] = local_var_params['images']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_version(self, request):
        """删除应用版本

        应用服务器可调用此接口删除应用版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAppVersion
        :type request: :class:`huaweicloudsdkiotedge.v3.DeleteAppVersionRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.DeleteAppVersionResponse`
        """
        http_info = self._delete_app_version_http_info(request)
        return self._call_api(**http_info)

    def delete_app_version_invoker(self, request):
        http_info = self._delete_app_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_app_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/apps/{app_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def download_app_version(self, request):
        """下载应用版本Chart包

        应用服务器可调用此接口下载应用版本Chart包。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAppVersion
        :type request: :class:`huaweicloudsdkiotedge.v3.DownloadAppVersionRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.DownloadAppVersionResponse`
        """
        http_info = self._download_app_version_http_info(request)
        return self._call_api(**http_info)

    def download_app_version_invoker(self, request):
        http_info = self._download_app_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_app_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/apps/{app_id}/versions/{version}/archive",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAppVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def list_app_image(self, request):
        """查询应用版本包含的镜像列表

        应用服务器可调用此接口查询应用版本包含的镜像列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppImage
        :type request: :class:`huaweicloudsdkiotedge.v3.ListAppImageRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ListAppImageResponse`
        """
        http_info = self._list_app_image_http_info(request)
        return self._call_api(**http_info)

    def list_app_image_invoker(self, request):
        http_info = self._list_app_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_image_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/apps/{app_id}/versions/{version}/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def list_app_versions(self, request):
        """查询应用版本列表

        应用服务器可调用此接口查询应用版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppVersions
        :type request: :class:`huaweicloudsdkiotedge.v3.ListAppVersionsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ListAppVersionsResponse`
        """
        http_info = self._list_app_versions_http_info(request)
        return self._call_api(**http_info)

    def list_app_versions_invoker(self, request):
        http_info = self._list_app_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/apps/{app_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
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

    def show_app_version(self, request):
        """查询应用版本详情

        应用服务器可调用此接口查询应用版本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppVersion
        :type request: :class:`huaweicloudsdkiotedge.v3.ShowAppVersionRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ShowAppVersionResponse`
        """
        http_info = self._show_app_version_http_info(request)
        return self._call_api(**http_info)

    def show_app_version_invoker(self, request):
        http_info = self._show_app_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/apps/{app_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def create_cluster(self, request):
        """创建边缘集群

        应用服务器可调用此接口为创建边缘集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkiotedge.v3.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.CreateClusterResponse`
        """
        http_info = self._create_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_invoker(self, request):
        http_info = self._create_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterResponse"
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

    def create_cluster_install_cmd(self, request):
        """生成边缘集群安装命令

        应用服务器可调用此接口生成边缘集群安装命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterInstallCmd
        :type request: :class:`huaweicloudsdkiotedge.v3.CreateClusterInstallCmdRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.CreateClusterInstallCmdResponse`
        """
        http_info = self._create_cluster_install_cmd_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_install_cmd_invoker(self, request):
        http_info = self._create_cluster_install_cmd_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_install_cmd_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/clusters/{cluster_id}/install-cmd",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterInstallCmdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'arch' in local_var_params:
            query_params.append(('arch', local_var_params['arch']))
        if 'os' in local_var_params:
            query_params.append(('os', local_var_params['os']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_cluster(self, request):
        """删除边缘集群

        应用服务器可调用此接口删除边缘集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkiotedge.v3.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.DeleteClusterResponse`
        """
        http_info = self._delete_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_invoker(self, request):
        http_info = self._delete_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cluster_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_clusters(self, request):
        """查询边缘集群列表

        应用服务器可调用此接口查询边缘集群列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusters
        :type request: :class:`huaweicloudsdkiotedge.v3.ListClustersRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ListClustersResponse`
        """
        http_info = self._list_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_clusters_invoker(self, request):
        http_info = self._list_clusters_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_clusters_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
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

    def show_cluster(self, request):
        """查询边缘集群详情

        应用服务器可调用此接口查询边缘集群详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCluster
        :type request: :class:`huaweicloudsdkiotedge.v3.ShowClusterRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v3.ShowClusterResponse`
        """
        http_info = self._show_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_invoker(self, request):
        http_info = self._show_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
