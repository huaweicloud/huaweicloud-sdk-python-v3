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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcss'")


class CssClient(Client):
    def __init__(self):
        super(CssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcss.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CssClient":
                raise TypeError("client type error, support client type is CssClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_cluster(self, request):
        r"""创建集群V2

        该接口用于创建拥有多种不同节点类型（ess，ess-cold，ess-client，ess-master）组合的集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkcss.v2.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterResponse`
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
            "resource_path": "/v2.0/{project_id}/clusters",
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

    def restart_cluster(self, request):
        r"""重启集群V2

        该接口可以用于重启当前集群拥有的全部节点类型，或部分节点类型组合的节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartCluster
        :type request: :class:`huaweicloudsdkcss.v2.RestartClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v2.RestartClusterResponse`
        """
        http_info = self._restart_cluster_http_info(request)
        return self._call_api(**http_info)

    def restart_cluster_invoker(self, request):
        http_info = self._restart_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/clusters/{cluster_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartClusterResponse"
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

    def rolling_restart(self, request):
        r"""滚动重启

        该接口会一个一个重启节点，在索引数量比较多的情况下耗时较长
        
        &gt;仅当集群的节点数量（含Master节点、Client节点和冷数据节点）大于3时，才支持滚动重启
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollingRestart
        :type request: :class:`huaweicloudsdkcss.v2.RollingRestartRequest`
        :rtype: :class:`huaweicloudsdkcss.v2.RollingRestartResponse`
        """
        http_info = self._rolling_restart_http_info(request)
        return self._call_api(**http_info)

    def rolling_restart_invoker(self, request):
        http_info = self._rolling_restart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rolling_restart_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/clusters/{cluster_id}/rolling-restart",
            "request_type": request.__class__.__name__,
            "response_type": "RollingRestartResponse"
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

    def start_auto_create_snapshots(self, request):
        r"""开启自动创建快照功能

        该接口用于打开自动备份功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartAutoCreateSnapshots
        :type request: :class:`huaweicloudsdkcss.v2.StartAutoCreateSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkcss.v2.StartAutoCreateSnapshotsResponse`
        """
        http_info = self._start_auto_create_snapshots_http_info(request)
        return self._call_api(**http_info)

    def start_auto_create_snapshots_invoker(self, request):
        http_info = self._start_auto_create_snapshots_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_auto_create_snapshots_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/clusters/{cluster_id}/snapshots/policy/open",
            "request_type": request.__class__.__name__,
            "response_type": "StartAutoCreateSnapshotsResponse"
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

    def stop_auto_create_snapshots(self, request):
        r"""关闭自动创建快照功能

        该接口用于关闭自动备份功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopAutoCreateSnapshots
        :type request: :class:`huaweicloudsdkcss.v2.StopAutoCreateSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkcss.v2.StopAutoCreateSnapshotsResponse`
        """
        http_info = self._stop_auto_create_snapshots_http_info(request)
        return self._call_api(**http_info)

    def stop_auto_create_snapshots_invoker(self, request):
        http_info = self._stop_auto_create_snapshots_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_auto_create_snapshots_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/clusters/{cluster_id}/snapshots/policy/close",
            "request_type": request.__class__.__name__,
            "response_type": "StopAutoCreateSnapshotsResponse"
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
