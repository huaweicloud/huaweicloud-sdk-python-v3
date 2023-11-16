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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaom'")


class AomClient(Client):
    def __init__(self):
        super(AomClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaom.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AomClient":
                raise TypeError("client type error, support client type is AomClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_app(self, request):
        """新增应用

        新增应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkaom.v3.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.CreateAppResponse`
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
            "resource_path": "/v1/applications",
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_component(self, request):
        """新增组件

        新增组件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateComponent
        :type request: :class:`huaweicloudsdkaom.v3.CreateComponentRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.CreateComponentResponse`
        """
        http_info = self._create_component_http_info(request)
        return self._call_api(**http_info)

    def create_component_invoker(self, request):
        http_info = self._create_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_component_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/components",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComponentResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_env(self, request):
        """创建环境

        创建环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnv
        :type request: :class:`huaweicloudsdkaom.v3.CreateEnvRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.CreateEnvResponse`
        """
        http_info = self._create_env_http_info(request)
        return self._call_api(**http_info)

    def create_env_invoker(self, request):
        http_info = self._create_env_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_env_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/environments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnvResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_sub_app(self, request):
        """新增子应用

        新增子应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubApp
        :type request: :class:`huaweicloudsdkaom.v3.CreateSubAppRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.CreateSubAppResponse`
        """
        http_info = self._create_sub_app_http_info(request)
        return self._call_api(**http_info)

    def create_sub_app_invoker(self, request):
        http_info = self._create_sub_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sub_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sub-applications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubAppResponse"
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

        auth_settings = ['apig-auth-iam']

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
        """删除应用

        删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkaom.v3.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.DeleteAppResponse`
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
            "resource_path": "/v1/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_component(self, request):
        """删除组件

        删除组件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteComponent
        :type request: :class:`huaweicloudsdkaom.v3.DeleteComponentRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.DeleteComponentResponse`
        """
        http_info = self._delete_component_http_info(request)
        return self._call_api(**http_info)

    def delete_component_invoker(self, request):
        http_info = self._delete_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_component_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_env(self, request):
        """删除环境

        删除环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnv
        :type request: :class:`huaweicloudsdkaom.v3.DeleteEnvRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.DeleteEnvResponse`
        """
        http_info = self._delete_env_http_info(request)
        return self._call_api(**http_info)

    def delete_env_invoker(self, request):
        http_info = self._delete_env_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_env_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_sub_app(self, request):
        """删除子应用

        删除子应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubApp
        :type request: :class:`huaweicloudsdkaom.v3.DeleteSubAppRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.DeleteSubAppResponse`
        """
        http_info = self._delete_sub_app_http_info(request)
        return self._call_api(**http_info)

    def delete_sub_app_invoker(self, request):
        http_info = self._delete_sub_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sub_app_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/sub-applications/{sub_app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sub_app_id' in local_var_params:
            path_params['sub_app_id'] = local_var_params['sub_app_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_under_node(self, request):
        """查询绑定在节点上的资源列表

        查询绑定在节点上的资源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceUnderNode
        :type request: :class:`huaweicloudsdkaom.v3.ListResourceUnderNodeRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.ListResourceUnderNodeResponse`
        """
        http_info = self._list_resource_under_node_http_info(request)
        return self._call_api(**http_info)

    def list_resource_under_node_invoker(self, request):
        http_info = self._list_resource_under_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_under_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource/{rf_resource_type}/type/{type}/ci-relationships",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceUnderNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rf_resource_type' in local_var_params:
            path_params['rf_resource_type'] = local_var_params['rf_resource_type']
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

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

        auth_settings = ['apig-auth-iam']

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
        """查询应用详情

        查询应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkaom.v3.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.ShowAppResponse`
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
            "resource_path": "/v1/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_by_name(self, request):
        """根据应用名称查询应用详情

        查询应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppByName
        :type request: :class:`huaweicloudsdkaom.v3.ShowAppByNameRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.ShowAppByNameResponse`
        """
        http_info = self._show_app_by_name_http_info(request)
        return self._call_api(**http_info)

    def show_app_by_name_invoker(self, request):
        http_info = self._show_app_by_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_by_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppByNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'display_name' in local_var_params:
            query_params.append(('display_name', local_var_params['display_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_component(self, request):
        """查询组件详情

        查询组件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponent
        :type request: :class:`huaweicloudsdkaom.v3.ShowComponentRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.ShowComponentResponse`
        """
        http_info = self._show_component_http_info(request)
        return self._call_api(**http_info)

    def show_component_invoker(self, request):
        http_info = self._show_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_component_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_component_by_name(self, request):
        """根据组件名称查询组件详情

        查询组件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponentByName
        :type request: :class:`huaweicloudsdkaom.v3.ShowComponentByNameRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.ShowComponentByNameResponse`
        """
        http_info = self._show_component_by_name_http_info(request)
        return self._call_api(**http_info)

    def show_component_by_name_invoker(self, request):
        http_info = self._show_component_by_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_component_by_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/components/application/{application_id}/name/{component_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentByNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_name' in local_var_params:
            path_params['component_name'] = local_var_params['component_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_env(self, request):
        """查询环境详情

        查询环境详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnv
        :type request: :class:`huaweicloudsdkaom.v3.ShowEnvRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.ShowEnvResponse`
        """
        http_info = self._show_env_http_info(request)
        return self._call_api(**http_info)

    def show_env_invoker(self, request):
        http_info = self._show_env_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_env_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_env_by_name(self, request):
        """根据环境名称查询环境详情

        查询环境详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnvByName
        :type request: :class:`huaweicloudsdkaom.v3.ShowEnvByNameRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.ShowEnvByNameResponse`
        """
        http_info = self._show_env_by_name_http_info(request)
        return self._call_api(**http_info)

    def show_env_by_name_invoker(self, request):
        http_info = self._show_env_by_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_env_by_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/environments/name/{environment_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvByNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_name' in local_var_params:
            path_params['environment_name'] = local_var_params['environment_name']

        query_params = []
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_app(self, request):
        """修改应用

        修改应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkaom.v3.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.UpdateAppResponse`
        """
        http_info = self._update_app_http_info(request)
        return self._call_api(**http_info)

    def update_app_invoker(self, request):
        http_info = self._update_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_app_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_component(self, request):
        """修改组件

        修改组件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateComponent
        :type request: :class:`huaweicloudsdkaom.v3.UpdateComponentRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.UpdateComponentResponse`
        """
        http_info = self._update_component_http_info(request)
        return self._call_api(**http_info)

    def update_component_invoker(self, request):
        http_info = self._update_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_component_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_env(self, request):
        """修改环境

        修改环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEnv
        :type request: :class:`huaweicloudsdkaom.v3.UpdateEnvRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.UpdateEnvResponse`
        """
        http_info = self._update_env_http_info(request)
        return self._call_api(**http_info)

    def update_env_invoker(self, request):
        http_info = self._update_env_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_env_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEnvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_sub_app(self, request):
        """修改子应用

        修改子应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubApp
        :type request: :class:`huaweicloudsdkaom.v3.UpdateSubAppRequest`
        :rtype: :class:`huaweicloudsdkaom.v3.UpdateSubAppResponse`
        """
        http_info = self._update_sub_app_http_info(request)
        return self._call_api(**http_info)

    def update_sub_app_invoker(self, request):
        http_info = self._update_sub_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sub_app_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/sub-applications/{sub_app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sub_app_id' in local_var_params:
            path_params['sub_app_id'] = local_var_params['sub_app_id']

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

        auth_settings = ['apig-auth-iam']

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
