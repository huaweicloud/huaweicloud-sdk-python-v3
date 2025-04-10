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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdataartsfabricep'")


class DataArtsFabricEpAsyncClient(Client):
    def __init__(self):
        super(DataArtsFabricEpAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdataartsfabricep.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DataArtsFabricEpAsyncClient":
                raise TypeError("client type error, support client type is DataArtsFabricEpAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def delete_service_instance_async(self, request):
        r"""删除Service实例

        删除Service实例，释放该实例的资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServiceInstance
        :type request: :class:`huaweicloudsdkdataartsfabricep.v1.DeleteServiceInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.DeleteServiceInstanceResponse`
        """
        http_info = self._delete_service_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_service_instance_async_invoker(self, request):
        http_info = self._delete_service_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_service_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/workspaces/{workspace_id}/services/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServiceInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
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

    def deploy_service_instance_async(self, request):
        r"""部署服务

        部署一个Service实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeployServiceInstance
        :type request: :class:`huaweicloudsdkdataartsfabricep.v1.DeployServiceInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.DeployServiceInstanceResponse`
        """
        http_info = self._deploy_service_instance_http_info(request)
        return self._call_api(**http_info)

    def deploy_service_instance_async_invoker(self, request):
        http_info = self._deploy_service_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _deploy_service_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workspaces/{workspace_id}/services/instances",
            "request_type": request.__class__.__name__,
            "response_type": "DeployServiceInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_services_instances_async(self, request):
        r"""列举已部署的Service实例

        列举已部署的Service实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServicesInstances
        :type request: :class:`huaweicloudsdkdataartsfabricep.v1.ListServicesInstancesRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.ListServicesInstancesResponse`
        """
        http_info = self._list_services_instances_http_info(request)
        return self._call_api(**http_info)

    def list_services_instances_async_invoker(self, request):
        http_info = self._list_services_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_services_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workspaces/{workspace_id}/services/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListServicesInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'source_id' in local_var_params:
            query_params.append(('source_id', local_var_params['source_id']))
        if 'version_id' in local_var_params:
            query_params.append(('version_id', local_var_params['version_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_service_instance_detail_async(self, request):
        r"""查看部署的Service实例详情

        查看部署后的Service实例的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServiceInstanceDetail
        :type request: :class:`huaweicloudsdkdataartsfabricep.v1.ShowServiceInstanceDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.ShowServiceInstanceDetailResponse`
        """
        http_info = self._show_service_instance_detail_http_info(request)
        return self._call_api(**http_info)

    def show_service_instance_detail_async_invoker(self, request):
        http_info = self._show_service_instance_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_service_instance_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workspaces/{workspace_id}/services/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServiceInstanceDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
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

    def update_service_instance_async(self, request):
        r"""更新Service实例

        更新已部署的Service实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServiceInstance
        :type request: :class:`huaweicloudsdkdataartsfabricep.v1.UpdateServiceInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.UpdateServiceInstanceResponse`
        """
        http_info = self._update_service_instance_http_info(request)
        return self._call_api(**http_info)

    def update_service_instance_async_invoker(self, request):
        http_info = self._update_service_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_service_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/workspaces/{workspace_id}/services/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServiceInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
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
