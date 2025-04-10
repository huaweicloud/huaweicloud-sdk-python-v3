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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkservicestage'")


class ServiceStageAsyncClient(Client):
    def __init__(self):
        super(ServiceStageAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkservicestage.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ServiceStageAsyncClient":
                raise TypeError("client type error, support client type is ServiceStageAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def change_application_async(self, request):
        r"""修改应用信息

        此API通过应用ID修改应用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeApplication
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeApplicationResponse`
        """
        http_info = self._change_application_http_info(request)
        return self._call_api(**http_info)

    def change_application_async_invoker(self, request):
        http_info = self._change_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_application_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeApplicationResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_application_configuration_async(self, request):
        r"""修改应用配置信息

        通过此API修改应用配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeApplicationConfigurationResponse`
        """
        http_info = self._change_application_configuration_http_info(request)
        return self._call_api(**http_info)

    def change_application_configuration_async_invoker(self, request):
        http_info = self._change_application_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_application_configuration_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeApplicationConfigurationResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_component_async(self, request):
        r"""根据组件ID修改组件信息

        此API通过组件ID修改组件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeComponent
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeComponentResponse`
        """
        http_info = self._change_component_http_info(request)
        return self._call_api(**http_info)

    def change_component_async_invoker(self, request):
        http_info = self._change_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_component_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_environment_async(self, request):
        r"""修改环境信息

        此API通过环境ID修改环境信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeEnvironmentResponse`
        """
        http_info = self._change_environment_http_info(request)
        return self._call_api(**http_info)

    def change_environment_async_invoker(self, request):
        http_info = self._change_environment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_environment_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cas/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeEnvironmentResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_instance_async(self, request):
        r"""修改应用组件实例

        通过此API修改应用组件实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeInstance
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeInstanceRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeInstanceResponse`
        """
        http_info = self._change_instance_http_info(request)
        return self._call_api(**http_info)

    def change_instance_async_invoker(self, request):
        http_info = self._change_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_resource_in_environment_async(self, request):
        r"""修改环境资源

        此API用来修改环境资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeResourceInEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeResourceInEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeResourceInEnvironmentResponse`
        """
        http_info = self._change_resource_in_environment_http_info(request)
        return self._call_api(**http_info)

    def change_resource_in_environment_async_invoker(self, request):
        http_info = self._change_resource_in_environment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_resource_in_environment_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/cas/environments/{environment_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeResourceInEnvironmentResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_application_async(self, request):
        r"""创建应用

        应用是一个功能相对完备的业务系统，由一个或多个特性相关的组件组成。
        
        此API用来创建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApplication
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateApplicationResponse`
        """
        http_info = self._create_application_http_info(request)
        return self._call_api(**http_info)

    def create_application_async_invoker(self, request):
        http_info = self._create_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_application_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cas/applications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationResponse"
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

    def create_cam_instance_async(self, request):
        r"""创建、更新实例

        创建、更新实例


        :param request: Request instance for CreateCamInstance
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateCamInstanceRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateCamInstanceResponse`
        """
        http_info = self._create_cam_instance_http_info(request)
        return self._call_api(**http_info)

    def create_cam_instance_async_invoker(self, request):
        http_info = self._create_cam_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cam_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCamInstanceResponse"
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

    def create_component_async(self, request):
        r"""应用中创建组件

        应用组件是组成应用的某个业务特性实现，以代码或者软件包为载体，可独立部署运行。
        
        此API用来在应用中创建组件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateComponent
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateComponentResponse`
        """
        http_info = self._create_component_http_info(request)
        return self._call_api(**http_info)

    def create_component_async_invoker(self, request):
        http_info = self._create_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_component_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComponentResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_environment_async(self, request):
        r"""创建环境

        环境是用于应用部署和运行的计算、存储、网络等基础设施的集合。Servicestage把相同VPC下的CCE集群加上多个ELB、RDS、DCS实例组合为一个环境，如：开发环境，测试环境，预生产环境，生产环境。环境内网络互通，可以按环境维度来管理资源、部署服务，减少具体基础设施运维管理的复杂性。
        
        此API用来创建环境。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateEnvironmentResponse`
        """
        http_info = self._create_environment_http_info(request)
        return self._call_api(**http_info)

    def create_environment_async_invoker(self, request):
        http_info = self._create_environment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_environment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cas/environments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnvironmentResponse"
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

    def create_instance_async(self, request):
        r"""创建组件实例

        此API用来创建应用组件实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_async_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_template_async(self, request):
        r"""创建模板

        创建模板


        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateTemplateResponse`
        """
        http_info = self._create_template_http_info(request)
        return self._call_api(**http_info)

    def create_template_async_invoker(self, request):
        http_info = self._create_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateResponse"
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

    def delete_application_async(self, request):
        r"""根据应用ID删除应用

        此API通过应用ID删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteApplicationResponse`
        """
        http_info = self._delete_application_http_info(request)
        return self._call_api(**http_info)

    def delete_application_async_invoker(self, request):
        http_info = self._delete_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_application_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_application_configuration_async(self, request):
        r"""删除应用配置

        通过此API删除应用配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteApplicationConfigurationResponse`
        """
        http_info = self._delete_application_configuration_http_info(request)
        return self._call_api(**http_info)

    def delete_application_configuration_async_invoker(self, request):
        http_info = self._delete_application_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_application_configuration_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'environment_id' in local_var_params:
            query_params.append(('environment_id', local_var_params['environment_id']))

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

    def delete_component_async(self, request):
        r"""根据应用组件ID删除应用组件

        此API通过应用组件ID删除应用组件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteComponent
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteComponentResponse`
        """
        http_info = self._delete_component_http_info(request)
        return self._call_api(**http_info)

    def delete_component_async_invoker(self, request):
        http_info = self._delete_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_component_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

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

    def delete_environment_async(self, request):
        r"""根据环境ID删除环境

        此API通过环境ID删除环境。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteEnvironmentResponse`
        """
        http_info = self._delete_environment_http_info(request)
        return self._call_api(**http_info)

    def delete_environment_async_invoker(self, request):
        http_info = self._delete_environment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_environment_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cas/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnvironmentResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_instance_async(self, request):
        r"""删除应用组件实例

        通过此API删除应用组件实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_async_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

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

    def delete_instance_by_id_async(self, request):
        r"""删除实例

        删除实例


        :param request: Request instance for DeleteInstanceById
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteInstanceByIdRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteInstanceByIdResponse`
        """
        http_info = self._delete_instance_by_id_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_by_id_async_invoker(self, request):
        http_info = self._delete_instance_by_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_by_id_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceByIdResponse"
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

    def delete_template_async(self, request):
        r"""删除模板

        删除模板


        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_async_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def deploy_instance_async(self, request):
        r"""部署实例

        部署实例


        :param request: Request instance for DeployInstance
        :type request: :class:`huaweicloudsdkservicestage.v2.DeployInstanceRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeployInstanceResponse`
        """
        http_info = self._deploy_instance_http_info(request)
        return self._call_api(**http_info)

    def deploy_instance_async_invoker(self, request):
        http_info = self._deploy_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _deploy_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instance/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "DeployInstanceResponse"
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

    def list_applications_async(self, request):
        r"""获取所有应用

        通过此API可以获取所有已经创建的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdkservicestage.v2.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListApplicationsResponse`
        """
        http_info = self._list_applications_http_info(request)
        return self._call_api(**http_info)

    def list_applications_async_invoker(self, request):
        http_info = self._list_applications_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_applications_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationsResponse"
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_component_overviews_async(self, request):
        r"""获取应用所有组件部署信息

        通过此API获取应用下所有应用组件部署信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponentOverviews
        :type request: :class:`huaweicloudsdkservicestage.v2.ListComponentOverviewsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListComponentOverviewsResponse`
        """
        http_info = self._list_component_overviews_http_info(request)
        return self._call_api(**http_info)

    def list_component_overviews_async_invoker(self, request):
        http_info = self._list_component_overviews_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_component_overviews_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/overviews",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentOverviewsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_components_async(self, request):
        r"""获取应用所有组件

        通过此API获取应用下所有应用组件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponents
        :type request: :class:`huaweicloudsdkservicestage.v2.ListComponentsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListComponentsResponse`
        """
        http_info = self._list_components_http_info(request)
        return self._call_api(**http_info)

    def list_components_async_invoker(self, request):
        http_info = self._list_components_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_components_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_environments_async(self, request):
        r"""获取所有环境

        此API用来获取所有已经创建环境。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvironments
        :type request: :class:`huaweicloudsdkservicestage.v2.ListEnvironmentsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListEnvironmentsResponse`
        """
        http_info = self._list_environments_http_info(request)
        return self._call_api(**http_info)

    def list_environments_async_invoker(self, request):
        http_info = self._list_environments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_environments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/environments",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvironmentsResponse"
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_instance_snapshots_async(self, request):
        r"""获取组件实例快照

        通过此API获取应用组件实例快照信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceSnapshots
        :type request: :class:`huaweicloudsdkservicestage.v2.ListInstanceSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListInstanceSnapshotsResponse`
        """
        http_info = self._list_instance_snapshots_http_info(request)
        return self._call_api(**http_info)

    def list_instance_snapshots_async_invoker(self, request):
        http_info = self._list_instance_snapshots_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_snapshots_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}/snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceSnapshotsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'snapshot_order_by' in local_var_params:
            query_params.append(('snapshot_order_by', local_var_params['snapshot_order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_instances_async(self, request):
        r"""获取应用组件实例

        通过此API获取组件下的所有组件实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkservicestage.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_async_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def show_application_configuration_async(self, request):
        r"""获取应用配置

        通过此API获取应用配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowApplicationConfigurationResponse`
        """
        http_info = self._show_application_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_application_configuration_async_invoker(self, request):
        http_info = self._show_application_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_application_configuration_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'environment_id' in local_var_params:
            query_params.append(('environment_id', local_var_params['environment_id']))

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

    def show_application_detail_async(self, request):
        r"""根据应用ID获取应用详细信息

        此API通过应用ID获取应用详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApplicationDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowApplicationDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowApplicationDetailResponse`
        """
        http_info = self._show_application_detail_http_info(request)
        return self._call_api(**http_info)

    def show_application_detail_async_invoker(self, request):
        http_info = self._show_application_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_application_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationDetailResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_component_detail_async(self, request):
        r"""根据组件ID获取应用组件信息

        通过组件ID获取应用组件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowComponentDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowComponentDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowComponentDetailResponse`
        """
        http_info = self._show_component_detail_http_info(request)
        return self._call_api(**http_info)

    def show_component_detail_async_invoker(self, request):
        http_info = self._show_component_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_component_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_environment_detail_async(self, request):
        r"""根据环境ID获取环境详细信息

        此API通过环境ID获取环境详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEnvironmentDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowEnvironmentDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowEnvironmentDetailResponse`
        """
        http_info = self._show_environment_detail_http_info(request)
        return self._call_api(**http_info)

    def show_environment_detail_async_invoker(self, request):
        http_info = self._show_environment_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_environment_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvironmentDetailResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_detail_async(self, request):
        r"""根据实例ID获取实例详细信息

        此API通过实例ID获取实例详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowInstanceDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowInstanceDetailResponse`
        """
        http_info = self._show_instance_detail_http_info(request)
        return self._call_api(**http_info)

    def show_instance_detail_async_invoker(self, request):
        http_info = self._show_instance_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
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

    def show_job_detail_async(self, request):
        r"""获取部署任务详细信息

        通过此API获取部署任务详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowJobDetailResponse`
        """
        http_info = self._show_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_job_detail_async_invoker(self, request):
        http_info = self._show_job_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'desc' in local_var_params:
            query_params.append(('desc', local_var_params['desc']))

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

    def update_instance_action_async(self, request):
        r"""对组件实例的操作

        通过此API获取对组件实例的操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceAction
        :type request: :class:`huaweicloudsdkservicestage.v2.UpdateInstanceActionRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.UpdateInstanceActionResponse`
        """
        http_info = self._update_instance_action_http_info(request)
        return self._call_api(**http_info)

    def update_instance_action_async_invoker(self, request):
        http_info = self._update_instance_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_template_async(self, request):
        r"""更新模板

        更新模板


        :param request: Request instance for UpdateTemplate
        :type request: :class:`huaweicloudsdkservicestage.v2.UpdateTemplateRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.UpdateTemplateResponse`
        """
        http_info = self._update_template_http_info(request)
        return self._call_api(**http_info)

    def update_template_async_invoker(self, request):
        http_info = self._update_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_template_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def create_file_async(self, request):
        r"""创建仓库文件

        在指定仓库项目下创建文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFile
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateFileRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateFileResponse`
        """
        http_info = self._create_file_http_info(request)
        return self._call_api(**http_info)

    def create_file_async_invoker(self, request):
        http_info = self._create_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/git/files/{namespace}/{project}/{path}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def create_hook_async(self, request):
        r"""创建项目hook

        创建指定项目的hook。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHook
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateHookRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateHookResponse`
        """
        http_info = self._create_hook_http_info(request)
        return self._call_api(**http_info)

    def create_hook_async_invoker(self, request):
        http_info = self._create_hook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_hook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/{project}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def create_o_auth_async(self, request):
        r"""创建OAuth授权

        创建指定Git仓库类型的OAuth授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOAuth
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateOAuthRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateOAuthResponse`
        """
        http_info = self._create_o_auth_http_info(request)
        return self._call_api(**http_info)

    def create_o_auth_async_invoker(self, request):
        http_info = self._create_o_auth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_o_auth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/git/auths/{repo_type}/oauth",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repo_type' in local_var_params:
            path_params['repo_type'] = local_var_params['repo_type']

        query_params = []
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

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

    def create_password_auth_async(self, request):
        r"""创建口令授权

        创建指定Git仓库类型的口令授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePasswordAuth
        :type request: :class:`huaweicloudsdkservicestage.v2.CreatePasswordAuthRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreatePasswordAuthResponse`
        """
        http_info = self._create_password_auth_http_info(request)
        return self._call_api(**http_info)

    def create_password_auth_async_invoker(self, request):
        http_info = self._create_password_auth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_password_auth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/git/auths/{repo_type}/password",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePasswordAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repo_type' in local_var_params:
            path_params['repo_type'] = local_var_params['repo_type']

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

    def create_personal_auth_async(self, request):
        r"""创建私人令牌授权

        创建指定Git仓库类型的私人令牌授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePersonalAuth
        :type request: :class:`huaweicloudsdkservicestage.v2.CreatePersonalAuthRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreatePersonalAuthResponse`
        """
        http_info = self._create_personal_auth_http_info(request)
        return self._call_api(**http_info)

    def create_personal_auth_async_invoker(self, request):
        http_info = self._create_personal_auth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_personal_auth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/git/auths/{repo_type}/personal",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePersonalAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repo_type' in local_var_params:
            path_params['repo_type'] = local_var_params['repo_type']

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

    def create_project_async(self, request):
        r"""创建软件仓库项目

        创建指定组织下的软件仓库项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProject
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateProjectRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateProjectResponse`
        """
        http_info = self._create_project_http_info(request)
        return self._call_api(**http_info)

    def create_project_async_invoker(self, request):
        http_info = self._create_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_project_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/projects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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
        r"""创建项目tag标签

        创建指定项目的tag标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_async_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/{project}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def delete_authorize_async(self, request):
        r"""删除仓库授权

        通过名称删除仓库授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAuthorize
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteAuthorizeRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteAuthorizeResponse`
        """
        http_info = self._delete_authorize_http_info(request)
        return self._call_api(**http_info)

    def delete_authorize_async_invoker(self, request):
        http_info = self._delete_authorize_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_authorize_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/git/auths/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuthorizeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

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

    def delete_file_async(self, request):
        r"""删除仓库文件

        删除指定项目仓库下的文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFile
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteFileRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteFileResponse`
        """
        http_info = self._delete_file_http_info(request)
        return self._call_api(**http_info)

    def delete_file_async_invoker(self, request):
        http_info = self._delete_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_file_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/git/files/{namespace}/{project}/{path}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))
        if 'message' in local_var_params:
            query_params.append(('message', local_var_params['message']))
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def delete_hook_async(self, request):
        r"""删除项目hook

        删除指定项目的hook。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHook
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteHookRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteHookResponse`
        """
        http_info = self._delete_hook_http_info(request)
        return self._call_api(**http_info)

    def delete_hook_async_invoker(self, request):
        http_info = self._delete_hook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_hook_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/{project}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def delete_tag_async(self, request):
        r"""删除项目tag标签

        删除指定项目的tag标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_async_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/{project}/tags/{tag_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']
        if 'tag_name' in local_var_params:
            path_params['tag_name'] = local_var_params['tag_name']

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def list_authorizations_async(self, request):
        r"""获取仓库授权列表

        获取所有Git仓库授权信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorizations
        :type request: :class:`huaweicloudsdkservicestage.v2.ListAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListAuthorizationsResponse`
        """
        http_info = self._list_authorizations_http_info(request)
        return self._call_api(**http_info)

    def list_authorizations_async_invoker(self, request):
        http_info = self._list_authorizations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_authorizations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/auths",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizationsResponse"
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

    def list_branches_async(self, request):
        r"""获取项目分支

        获取指定项目的所有分支列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBranches
        :type request: :class:`huaweicloudsdkservicestage.v2.ListBranchesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListBranchesResponse`
        """
        http_info = self._list_branches_http_info(request)
        return self._call_api(**http_info)

    def list_branches_async_invoker(self, request):
        http_info = self._list_branches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_branches_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/{project}/branches",
            "request_type": request.__class__.__name__,
            "response_type": "ListBranchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def list_commits_async(self, request):
        r"""获取项目commit提交记录

        获取指定项目的最近10次commit提交记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCommits
        :type request: :class:`huaweicloudsdkservicestage.v2.ListCommitsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListCommitsResponse`
        """
        http_info = self._list_commits_http_info(request)
        return self._call_api(**http_info)

    def list_commits_async_invoker(self, request):
        http_info = self._list_commits_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_commits_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/{project}/commits",
            "request_type": request.__class__.__name__,
            "response_type": "ListCommitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def list_hooks_async(self, request):
        r"""获取项目hooks

        获取指定项目的所有hooks
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHooks
        :type request: :class:`huaweicloudsdkservicestage.v2.ListHooksRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListHooksResponse`
        """
        http_info = self._list_hooks_http_info(request)
        return self._call_api(**http_info)

    def list_hooks_async_invoker(self, request):
        http_info = self._list_hooks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hooks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/{project}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListHooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def list_namespaces_async(self, request):
        r"""获取仓库的namespaces

        获取仓库的namespaces。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNamespaces
        :type request: :class:`huaweicloudsdkservicestage.v2.ListNamespacesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListNamespacesResponse`
        """
        http_info = self._list_namespaces_http_info(request)
        return self._call_api(**http_info)

    def list_namespaces_async_invoker(self, request):
        http_info = self._list_namespaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_namespaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/repos/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListNamespacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def list_projects_async(self, request):
        r"""获取组织下所有项目

        获取指定组织下的所有项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjects
        :type request: :class:`huaweicloudsdkservicestage.v2.ListProjectsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListProjectsResponse`
        """
        http_info = self._list_projects_http_info(request)
        return self._call_api(**http_info)

    def list_projects_async_invoker(self, request):
        http_info = self._list_projects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_projects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def list_tags_async(self, request):
        r"""获取项目的所有tag标签

        获取指定项目的所有tag标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkservicestage.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/repos/{namespace}/{project}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def list_trees_async(self, request):
        r"""获取仓库文件列表

        获取指定项目仓库的文件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrees
        :type request: :class:`huaweicloudsdkservicestage.v2.ListTreesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListTreesResponse`
        """
        http_info = self._list_trees_http_info(request)
        return self._call_api(**http_info)

    def list_trees_async_invoker(self, request):
        http_info = self._list_trees_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_trees_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/files/{namespace}/{project}/trees",
            "request_type": request.__class__.__name__,
            "response_type": "ListTreesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def show_content_async(self, request):
        r"""获取仓库文件内容

        获取指定项目仓库下文件的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowContent
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowContentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowContentResponse`
        """
        http_info = self._show_content_http_info(request)
        return self._call_api(**http_info)

    def show_content_async_invoker(self, request):
        http_info = self._show_content_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_content_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/files/{namespace}/{project}/{path}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowContentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def show_project_detail_async(self, request):
        r"""通过clone url 获取仓库信息

        通过指定的clone url 获取仓库信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowProjectDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowProjectDetailResponse`
        """
        http_info = self._show_project_detail_http_info(request)
        return self._call_api(**http_info)

    def show_project_detail_async_invoker(self, request):
        http_info = self._show_project_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/repos/project-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'clone_url' in local_var_params:
            query_params.append(('clone_url', local_var_params['clone_url']))

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def show_redirect_url_async(self, request):
        r"""获取授权重定向URL

        获取指定Git仓库类型的授权重定向URL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRedirectUrl
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowRedirectUrlRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowRedirectUrlResponse`
        """
        http_info = self._show_redirect_url_http_info(request)
        return self._call_api(**http_info)

    def show_redirect_url_async_invoker(self, request):
        http_info = self._show_redirect_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_redirect_url_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/git/auths/{repo_type}/redirect",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRedirectUrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repo_type' in local_var_params:
            path_params['repo_type'] = local_var_params['repo_type']

        query_params = []
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

    def update_file_async(self, request):
        r"""更新仓库文件内容

        更新指定项目仓库下的文件内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFile
        :type request: :class:`huaweicloudsdkservicestage.v2.UpdateFileRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.UpdateFileResponse`
        """
        http_info = self._update_file_http_info(request)
        return self._call_api(**http_info)

    def update_file_async_invoker(self, request):
        http_info = self._update_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_file_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/git/files/{namespace}/{project}/{path}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

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

    def list_flavors_async(self, request):
        r"""获取所有支持的应用资源规格

        通过此API获取所用支持的应用资源规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkservicestage.v2.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_async_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/metadata/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
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

    def list_runtimes_async(self, request):
        r"""获取所有支持的应用组件运行时类型

        此API用来获取所有支持应用组件运行时类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRuntimes
        :type request: :class:`huaweicloudsdkservicestage.v2.ListRuntimesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListRuntimesResponse`
        """
        http_info = self._list_runtimes_http_info(request)
        return self._call_api(**http_info)

    def list_runtimes_async_invoker(self, request):
        http_info = self._list_runtimes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_runtimes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/metadata/runtimes",
            "request_type": request.__class__.__name__,
            "response_type": "ListRuntimesResponse"
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

    def list_templates_async(self, request):
        r"""获取所有支持的应用组件模板

        此API用来获取所有内置应用组件模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkservicestage.v2.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_async_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cas/metadata/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
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
