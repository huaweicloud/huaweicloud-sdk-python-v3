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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcampusgo'")


class CampusGoClient(Client):
    def __init__(self):
        super(CampusGoClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcampusgo.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CampusGoClient":
                raise TypeError("client type error, support client type is CampusGoClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_tasks(self, request):
        """创建服务作业

        该接口用于创建服务作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTasks
        :type request: :class:`huaweicloudsdkcampusgo.v2.CreateTasksRequest`
        :rtype: :class:`huaweicloudsdkcampusgo.v2.CreateTasksResponse`
        """
        http_info = self._create_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_tasks_invoker(self, request):
        http_info = self._create_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_name}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

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

    def delete_task(self, request):
        """删除服务作业

        该接口用于删除服务作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkcampusgo.v2.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkcampusgo.v2.DeleteTaskResponse`
        """
        http_info = self._delete_task_http_info(request)
        return self._call_api(**http_info)

    def delete_task_invoker(self, request):
        http_info = self._delete_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/{service_name}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']
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

    def list_tasks_details(self, request):
        """获取服务作业列表

        该接口用于获取服务作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTasksDetails
        :type request: :class:`huaweicloudsdkcampusgo.v2.ListTasksDetailsRequest`
        :rtype: :class:`huaweicloudsdkcampusgo.v2.ListTasksDetailsResponse`
        """
        http_info = self._list_tasks_details_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_details_invoker(self, request):
        http_info = self._list_tasks_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tasks_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_name}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

        query_params = []
        if 'service_version' in local_var_params:
            query_params.append(('service_version', local_var_params['service_version']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'id_like' in local_var_params:
            query_params.append(('id_like', local_var_params['id_like']))
        if 'created_since' in local_var_params:
            query_params.append(('created_since', local_var_params['created_since']))
        if 'created_until' in local_var_params:
            query_params.append(('created_until', local_var_params['created_until']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
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

    def show_task(self, request):
        """查询服务作业

        该接口用于查询服务作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkcampusgo.v2.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkcampusgo.v2.ShowTaskResponse`
        """
        http_info = self._show_task_http_info(request)
        return self._call_api(**http_info)

    def show_task_invoker(self, request):
        http_info = self._show_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_name}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']
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
