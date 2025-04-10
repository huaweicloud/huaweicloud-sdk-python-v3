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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcloudtable'")


class CloudTableAsyncClient(Client):
    def __init__(self):
        super(CloudTableAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudtable.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CloudTableAsyncClient":
                raise TypeError("client type error, support client type is CloudTableAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_cluster_async(self, request):
        r"""创建CloudTable集群

        创建一个CloudTable集群。
        使用接口前，您需要先获取如下资源信息。
        - 通过VPC创建或查询VPC、子网
        - 通过安全组创建或查询可用的security_group_id
        
        本接口是一个同步接口，当创建CloudTable集群成功后会返回集群id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkcloudtable.v2.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.CreateClusterResponse`
        """
        http_info = self._create_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_async_invoker(self, request):
        http_info = self._create_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_cluster_async(self, request):
        r"""删除CloudTable指定集群

        集群ID为集群唯一标识，根据集群ID删除指定集群。
        如下状态的集群不允许删除：
        - 创建中
        - 扩容中
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkcloudtable.v2.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.DeleteClusterResponse`
        """
        http_info = self._delete_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_async_invoker(self, request):
        http_info = self._delete_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cluster_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}",
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

    def enable_component_async(self, request):
        r"""开启opentsdb组件

        开启opentsdb组件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableComponent
        :type request: :class:`huaweicloudsdkcloudtable.v2.EnableComponentRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.EnableComponentResponse`
        """
        http_info = self._enable_component_http_info(request)
        return self._call_api(**http_info)

    def enable_component_async_invoker(self, request):
        http_info = self._enable_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_component_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/components/{component_name}",
            "request_type": request.__class__.__name__,
            "response_type": "EnableComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'component_name' in local_var_params:
            path_params['component_name'] = local_var_params['component_name']

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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def expand_cluster_component_async(self, request):
        r"""扩容组件

        扩容指定类型的集群节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandClusterComponent
        :type request: :class:`huaweicloudsdkcloudtable.v2.ExpandClusterComponentRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.ExpandClusterComponentResponse`
        """
        http_info = self._expand_cluster_component_http_info(request)
        return self._call_api(**http_info)

    def expand_cluster_component_async_invoker(self, request):
        http_info = self._expand_cluster_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _expand_cluster_component_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandClusterComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_clusters_async(self, request):
        r"""查询CloudTable集群列表

        查看用户创建的集群列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusters
        :type request: :class:`huaweicloudsdkcloudtable.v2.ListClustersRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.ListClustersResponse`
        """
        http_info = self._list_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_clusters_async_invoker(self, request):
        http_info = self._list_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_clusters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListClustersResponse"
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

    def reboot_cloud_table_cluster_async(self, request):
        r"""重启集群的api入口

        重启集群的api入口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RebootCloudTableCluster
        :type request: :class:`huaweicloudsdkcloudtable.v2.RebootCloudTableClusterRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.RebootCloudTableClusterResponse`
        """
        http_info = self._reboot_cloud_table_cluster_http_info(request)
        return self._call_api(**http_info)

    def reboot_cloud_table_cluster_async_invoker(self, request):
        http_info = self._reboot_cloud_table_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reboot_cloud_table_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RebootCloudTableClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cluster_detail_async(self, request):
        r"""查询CloudTable集群详情

        通过集群ID唯一标识一个集群，根据集群ID查询特定CloudTable集群的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterDetail
        :type request: :class:`huaweicloudsdkcloudtable.v2.ShowClusterDetailRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.ShowClusterDetailResponse`
        """
        http_info = self._show_cluster_detail_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_detail_async_invoker(self, request):
        http_info = self._show_cluster_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

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

    def show_cluster_setting_async(self, request):
        r"""查询集群配置

        查询集群配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterSetting
        :type request: :class:`huaweicloudsdkcloudtable.v2.ShowClusterSettingRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.ShowClusterSettingResponse`
        """
        http_info = self._show_cluster_setting_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_setting_async_invoker(self, request):
        http_info = self._show_cluster_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

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

    def update_cluster_setting_async(self, request):
        r"""修改集群配置

        修改集群配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateClusterSetting
        :type request: :class:`huaweicloudsdkcloudtable.v2.UpdateClusterSettingRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.UpdateClusterSettingResponse`
        """
        http_info = self._update_cluster_setting_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_setting_async_invoker(self, request):
        http_info = self._update_cluster_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cluster_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/setting",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_cloud_table_cluster_async(self, request):
        r"""创建CloudTable集群

        创建一个CloudTable集群。
        使用接口前，您需要先获取如下资源信息。
        - 通过VPC创建或查询VPC、子网
        - 通过安全组创建或查询可用的security_group_id
        
        本接口是一个同步接口，当创建CloudTable集群成功后会返回集群id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCloudTableCluster
        :type request: :class:`huaweicloudsdkcloudtable.v2.CreateCloudTableClusterRequest`
        :rtype: :class:`huaweicloudsdkcloudtable.v2.CreateCloudTableClusterResponse`
        """
        http_info = self._create_cloud_table_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_cloud_table_cluster_async_invoker(self, request):
        http_info = self._create_cloud_table_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cloud_table_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCloudTableClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json'])

        auth_settings = []

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
