# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class ServiceStageAsyncClient(Client):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(ServiceStageAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkservicestage.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ServiceStageClient":
            raise TypeError("client type error, support client type is ServiceStageClient")

        return ClientBuilder(clazz)

    def change_application_async(self, request):
        """修改应用信息

        此API通过应用ID修改应用信息。


        :param request: Request instance for ChangeApplication
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeApplicationResponse`
        """
        return self.change_application_with_http_info(request)

    def change_application_with_http_info(self, request):
        all_params = ['application_id', 'application_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_application_configuration_async(self, request):
        """修改应用配置信息

        通过此API修改应用配置信息。


        :param request: Request instance for ChangeApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeApplicationConfigurationResponse`
        """
        return self.change_application_configuration_with_http_info(request)

    def change_application_configuration_with_http_info(self, request):
        all_params = ['application_id', 'application_config_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}/configuration',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeApplicationConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_component_async(self, request):
        """根据组件ID修改组件信息

        此API通过组件ID修改组件信息。


        :param request: Request instance for ChangeComponent
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeComponentResponse`
        """
        return self.change_component_with_http_info(request)

    def change_component_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'component_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeComponentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_environment_async(self, request):
        """修改环境信息

        此API通过环境ID修改环境信息。


        :param request: Request instance for ChangeEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeEnvironmentResponse`
        """
        return self.change_environment_with_http_info(request)

    def change_environment_with_http_info(self, request):
        all_params = ['environment_id', 'environment_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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
            resource_path='/v2/{project_id}/cas/environments/{environment_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_instance_async(self, request):
        """修改应用组件实例

        通过此API修改应用组件实例。


        :param request: Request instance for ChangeInstance
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeInstanceRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeInstanceResponse`
        """
        return self.change_instance_with_http_info(request)

    def change_instance_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'instance_id', 'instance_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_resource_in_environment_async(self, request):
        """修改环境资源

        此API用来修改环境资源。


        :param request: Request instance for ChangeResourceInEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v2.ChangeResourceInEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ChangeResourceInEnvironmentResponse`
        """
        return self.change_resource_in_environment_with_http_info(request)

    def change_resource_in_environment_with_http_info(self, request):
        all_params = ['environment_id', 'environment_resource_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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
            resource_path='/v2/{project_id}/cas/environments/{environment_id}/resources',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeResourceInEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_application_async(self, request):
        """创建应用

        应用是一个功能相对完备的业务系统，由一个或多个特性相关的组件组成。
        
        此API用来创建应用。


        :param request: Request instance for CreateApplication
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateApplicationResponse`
        """
        return self.create_application_with_http_info(request)

    def create_application_with_http_info(self, request):
        all_params = ['application_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/applications',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_component_async(self, request):
        """应用中创建组件

        应用组件是组成应用的某个业务特性实现，以代码或者软件包为载体，可独立部署运行。
        
        此API用来在应用中创建组件。


        :param request: Request instance for CreateComponent
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateComponentResponse`
        """
        return self.create_component_with_http_info(request)

    def create_component_with_http_info(self, request):
        all_params = ['application_id', 'component_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateComponentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_environment_async(self, request):
        """创建环境

        环境是用于应用部署和运行的计算、存储、网络等基础设施的集合。Servicestage把相同VPC下的CCE集群加上多个ELB、RDS、DCS实例组合为一个环境，如：开发环境，测试环境，预生产环境，生产环境。环境内网络互通，可以按环境维度来管理资源、部署服务，减少具体基础设施运维管理的复杂性。
        
        此API用来创建环境。


        :param request: Request instance for CreateEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateEnvironmentResponse`
        """
        return self.create_environment_with_http_info(request)

    def create_environment_with_http_info(self, request):
        all_params = ['environment_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/environments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_async(self, request):
        """创建组件实例

        此API用来创建应用组件实例。


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateInstanceResponse`
        """
        return self.create_instance_with_http_info(request)

    def create_instance_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'instance_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_application_async(self, request):
        """根据应用ID删除应用

        此API通过应用ID删除应用。


        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteApplicationResponse`
        """
        return self.delete_application_with_http_info(request)

    def delete_application_with_http_info(self, request):
        all_params = ['application_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_application_configuration_async(self, request):
        """删除应用配置

        通过此API删除应用配置信息。


        :param request: Request instance for DeleteApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteApplicationConfigurationResponse`
        """
        return self.delete_application_configuration_with_http_info(request)

    def delete_application_configuration_with_http_info(self, request):
        all_params = ['application_id', 'environment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/configuration',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApplicationConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_component_async(self, request):
        """根据应用组件ID删除应用组件

        此API通过应用组件ID删除应用组件。


        :param request: Request instance for DeleteComponent
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteComponentResponse`
        """
        return self.delete_component_with_http_info(request)

    def delete_component_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'force']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteComponentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_environment_async(self, request):
        """根据环境ID删除环境

        此API通过环境ID删除环境。


        :param request: Request instance for DeleteEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteEnvironmentResponse`
        """
        return self.delete_environment_with_http_info(request)

    def delete_environment_with_http_info(self, request):
        all_params = ['environment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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
            resource_path='/v2/{project_id}/cas/environments/{environment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instance_async(self, request):
        """删除应用组件实例

        通过此API删除应用组件实例。


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteInstanceResponse`
        """
        return self.delete_instance_with_http_info(request)

    def delete_instance_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'instance_id', 'force']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_applications_async(self, request):
        """获取所有应用

        通过此API可以获取所有已经创建的应用。


        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdkservicestage.v2.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListApplicationsResponse`
        """
        return self.list_applications_with_http_info(request)

    def list_applications_with_http_info(self, request):
        all_params = ['limit', 'offset', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApplicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_components_async(self, request):
        """获取应用所有组件

        通过此API获取应用下所有应用组件。


        :param request: Request instance for ListComponents
        :type request: :class:`huaweicloudsdkservicestage.v2.ListComponentsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListComponentsResponse`
        """
        return self.list_components_with_http_info(request)

    def list_components_with_http_info(self, request):
        all_params = ['application_id', 'limit', 'offset', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListComponentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_environments_async(self, request):
        """获取所有环境

        此API用来获取所有已经创建环境。


        :param request: Request instance for ListEnvironments
        :type request: :class:`huaweicloudsdkservicestage.v2.ListEnvironmentsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListEnvironmentsResponse`
        """
        return self.list_environments_with_http_info(request)

    def list_environments_with_http_info(self, request):
        all_params = ['limit', 'offset', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/environments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnvironmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_snapshots_async(self, request):
        """获取组件实例快照

        通过此API获取应用组件实例快照信息。


        :param request: Request instance for ListInstanceSnapshots
        :type request: :class:`huaweicloudsdkservicestage.v2.ListInstanceSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListInstanceSnapshotsResponse`
        """
        return self.list_instance_snapshots_with_http_info(request)

    def list_instance_snapshots_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'instance_id', 'limit', 'offset', 'snapshot_order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}/snapshots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceSnapshotsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_async(self, request):
        """获取应用组件实例

        通过此API获取组件下的所有组件实例。


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkservicestage.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListInstancesResponse`
        """
        return self.list_instances_with_http_info(request)

    def list_instances_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'limit', 'offset', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_application_configuration_async(self, request):
        """获取应用配置

        通过此API获取应用配置信息。


        :param request: Request instance for ShowApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowApplicationConfigurationResponse`
        """
        return self.show_application_configuration_with_http_info(request)

    def show_application_configuration_with_http_info(self, request):
        all_params = ['application_id', 'environment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/configuration',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApplicationConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_application_detail_async(self, request):
        """根据应用ID获取应用详细信息

        此API通过应用ID获取应用详细信息。


        :param request: Request instance for ShowApplicationDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowApplicationDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowApplicationDetailResponse`
        """
        return self.show_application_detail_with_http_info(request)

    def show_application_detail_with_http_info(self, request):
        all_params = ['application_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApplicationDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_component_detail_async(self, request):
        """根据组件ID获取应用组件信息

        通过组件ID获取应用组件信息。


        :param request: Request instance for ShowComponentDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowComponentDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowComponentDetailResponse`
        """
        return self.show_component_detail_with_http_info(request)

    def show_component_detail_with_http_info(self, request):
        all_params = ['application_id', 'component_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowComponentDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_environment_detail_async(self, request):
        """根据环境ID获取环境详细信息

        此API通过环境ID获取环境详细信息。


        :param request: Request instance for ShowEnvironmentDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowEnvironmentDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowEnvironmentDetailResponse`
        """
        return self.show_environment_detail_with_http_info(request)

    def show_environment_detail_with_http_info(self, request):
        all_params = ['environment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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
            resource_path='/v2/{project_id}/cas/environments/{environment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEnvironmentDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_detail_async(self, request):
        """根据实例ID获取实例详细信息

        此API通过实例ID获取实例详细信息。


        :param request: Request instance for ShowInstanceDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowInstanceDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowInstanceDetailResponse`
        """
        return self.show_instance_detail_with_http_info(request)

    def show_instance_detail_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_detail_async(self, request):
        """获取部署任务详细信息

        通过此API获取部署任务详细信息。


        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowJobDetailResponse`
        """
        return self.show_job_detail_with_http_info(request)

    def show_job_detail_with_http_info(self, request):
        all_params = ['job_id', 'instance_id', 'limit', 'offset', 'desc']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_action_async(self, request):
        """对组件实例的操作

        通过此API获取对组件实例的操作。


        :param request: Request instance for UpdateInstanceAction
        :type request: :class:`huaweicloudsdkservicestage.v2.UpdateInstanceActionRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.UpdateInstanceActionResponse`
        """
        return self.update_instance_action_with_http_info(request)

    def update_instance_action_with_http_info(self, request):
        all_params = ['application_id', 'component_id', 'instance_id', 'instance_action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_file_async(self, request):
        """创建仓库文件

        在指定仓库项目下创建文件。


        :param request: Request instance for CreateFile
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateFileRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateFileResponse`
        """
        return self.create_file_with_http_info(request)

    def create_file_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'path', 'ref', 'file_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/git/files/{namespace}/{project}/{path}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_hook_async(self, request):
        """创建项目hook

        创建指定项目的hook。


        :param request: Request instance for CreateHook
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateHookRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateHookResponse`
        """
        return self.create_hook_with_http_info(request)

    def create_hook_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'hook_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/hooks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateHookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_o_auth_async(self, request):
        """创建OAuth授权

        创建指定Git仓库类型的OAuth授权。


        :param request: Request instance for CreateOAuth
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateOAuthRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateOAuthResponse`
        """
        return self.create_o_auth_with_http_info(request)

    def create_o_auth_with_http_info(self, request):
        all_params = ['repo_type', 'tag', 'o_auth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/git/auths/{repo_type}/oauth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_password_auth_async(self, request):
        """创建口令授权

        创建指定Git仓库类型的口令授权。


        :param request: Request instance for CreatePasswordAuth
        :type request: :class:`huaweicloudsdkservicestage.v2.CreatePasswordAuthRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreatePasswordAuthResponse`
        """
        return self.create_password_auth_with_http_info(request)

    def create_password_auth_with_http_info(self, request):
        all_params = ['repo_type', 'access_password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repo_type' in local_var_params:
            path_params['repo_type'] = local_var_params['repo_type']

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
            resource_path='/v1/{project_id}/git/auths/{repo_type}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePasswordAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_personal_auth_async(self, request):
        """创建私人令牌授权

        创建指定Git仓库类型的私人令牌授权。


        :param request: Request instance for CreatePersonalAuth
        :type request: :class:`huaweicloudsdkservicestage.v2.CreatePersonalAuthRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreatePersonalAuthResponse`
        """
        return self.create_personal_auth_with_http_info(request)

    def create_personal_auth_with_http_info(self, request):
        all_params = ['repo_type', 'access_token']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repo_type' in local_var_params:
            path_params['repo_type'] = local_var_params['repo_type']

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
            resource_path='/v1/{project_id}/git/auths/{repo_type}/personal',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePersonalAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project_async(self, request):
        """创建软件仓库项目

        创建指定组织下的软件仓库项目。


        :param request: Request instance for CreateProject
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateProjectRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateProjectResponse`
        """
        return self.create_project_with_http_info(request)

    def create_project_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/git/repos/{namespace}/projects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tag_async(self, request):
        """创建项目tag标签

        创建指定项目的tag标签。


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkservicestage.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.CreateTagResponse`
        """
        return self.create_tag_with_http_info(request)

    def create_tag_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'ref', 'tag_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_authorize_async(self, request):
        """删除仓库授权

        通过名称删除仓库授权。


        :param request: Request instance for DeleteAuthorize
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteAuthorizeRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteAuthorizeResponse`
        """
        return self.delete_authorize_with_http_info(request)

    def delete_authorize_with_http_info(self, request):
        all_params = ['name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

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
            resource_path='/v1/{project_id}/git/auths/{name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAuthorizeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_file_async(self, request):
        """删除仓库文件

        删除指定项目仓库下的文件。


        :param request: Request instance for DeleteFile
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteFileRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteFileResponse`
        """
        return self.delete_file_with_http_info(request)

    def delete_file_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'path', 'ref', 'message', 'sha']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/files/{namespace}/{project}/{path}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_hook_async(self, request):
        """删除项目hook

        删除指定项目的hook。


        :param request: Request instance for DeleteHook
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteHookRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteHookResponse`
        """
        return self.delete_hook_with_http_info(request)

    def delete_hook_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'hook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/hooks/{hook_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteHookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tag_async(self, request):
        """删除项目tag标签

        删除指定项目的tag标签。


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkservicestage.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.DeleteTagResponse`
        """
        return self.delete_tag_with_http_info(request)

    def delete_tag_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'tag_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/tags/{tag_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_authorizations_async(self, request):
        """获取仓库授权列表

        获取所有Git仓库授权信息。


        :param request: Request instance for ListAuthorizations
        :type request: :class:`huaweicloudsdkservicestage.v2.ListAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListAuthorizationsResponse`
        """
        return self.list_authorizations_with_http_info(request)

    def list_authorizations_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/git/auths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuthorizationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_branches_async(self, request):
        """获取项目分支

        获取指定项目的所有分支列表。


        :param request: Request instance for ListBranches
        :type request: :class:`huaweicloudsdkservicestage.v2.ListBranchesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListBranchesResponse`
        """
        return self.list_branches_with_http_info(request)

    def list_branches_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/branches',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBranchesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_commits_async(self, request):
        """获取项目commit提交记录

        获取指定项目的最近10次commit提交记录。


        :param request: Request instance for ListCommits
        :type request: :class:`huaweicloudsdkservicestage.v2.ListCommitsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListCommitsResponse`
        """
        return self.list_commits_with_http_info(request)

    def list_commits_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/commits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCommitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_hooks_async(self, request):
        """获取项目hooks

        获取指定项目的所有hooks


        :param request: Request instance for ListHooks
        :type request: :class:`huaweicloudsdkservicestage.v2.ListHooksRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListHooksResponse`
        """
        return self.list_hooks_with_http_info(request)

    def list_hooks_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/hooks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_namespaces_async(self, request):
        """获取仓库的namespaces

        获取仓库的namespaces。


        :param request: Request instance for ListNamespaces
        :type request: :class:`huaweicloudsdkservicestage.v2.ListNamespacesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListNamespacesResponse`
        """
        return self.list_namespaces_with_http_info(request)

    def list_namespaces_with_http_info(self, request):
        all_params = ['x_repo_auth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_repo_auth' in local_var_params:
            header_params['X-Repo-Auth'] = local_var_params['x_repo_auth']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/namespaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNamespacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_projects_async(self, request):
        """获取组织下所有项目

        获取指定组织下的所有项目。


        :param request: Request instance for ListProjects
        :type request: :class:`huaweicloudsdkservicestage.v2.ListProjectsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListProjectsResponse`
        """
        return self.list_projects_with_http_info(request)

    def list_projects_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_async(self, request):
        """获取项目的所有tag标签

        获取指定项目的所有tag标签。


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkservicestage.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListTagsResponse`
        """
        return self.list_tags_with_http_info(request)

    def list_tags_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_trees_async(self, request):
        """获取仓库文件列表

        获取指定项目仓库的文件列表。


        :param request: Request instance for ListTrees
        :type request: :class:`huaweicloudsdkservicestage.v2.ListTreesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListTreesResponse`
        """
        return self.list_trees_with_http_info(request)

    def list_trees_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/files/{namespace}/{project}/trees',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTreesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_content_async(self, request):
        """获取仓库文件内容

        获取指定项目仓库下文件的内容。


        :param request: Request instance for ShowContent
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowContentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowContentResponse`
        """
        return self.show_content_with_http_info(request)

    def show_content_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'path', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/files/{namespace}/{project}/{path}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowContentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_detail_async(self, request):
        """通过clone url 获取仓库信息

        通过指定的clone url 获取仓库信息。


        :param request: Request instance for ShowProjectDetail
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowProjectDetailRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowProjectDetailResponse`
        """
        return self.show_project_detail_with_http_info(request)

    def show_project_detail_with_http_info(self, request):
        all_params = ['x_repo_auth', 'clone_url']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/project-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_redirect_url_async(self, request):
        """获取授权重定向URL

        获取指定Git仓库类型的授权重定向URL。


        :param request: Request instance for ShowRedirectUrl
        :type request: :class:`huaweicloudsdkservicestage.v2.ShowRedirectUrlRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ShowRedirectUrlResponse`
        """
        return self.show_redirect_url_with_http_info(request)

    def show_redirect_url_with_http_info(self, request):
        all_params = ['repo_type', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/auths/{repo_type}/redirect',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRedirectUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_file_async(self, request):
        """更新仓库文件内容

        更新指定项目仓库下的文件内容。


        :param request: Request instance for UpdateFile
        :type request: :class:`huaweicloudsdkservicestage.v2.UpdateFileRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.UpdateFileResponse`
        """
        return self.update_file_with_http_info(request)

    def update_file_with_http_info(self, request):
        all_params = ['x_repo_auth', 'namespace', 'project', 'path', 'ref', 'file_update']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/git/files/{namespace}/{project}/{path}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors_async(self, request):
        """获取所有支持的应用资源规格

        通过此API获取所用支持的应用资源规格。


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkservicestage.v2.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListFlavorsResponse`
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/metadata/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_runtimes_async(self, request):
        """获取所有支持的应用组件运行时类型

        此API用来获取所有支持应用组件运行时类型。


        :param request: Request instance for ListRuntimes
        :type request: :class:`huaweicloudsdkservicestage.v2.ListRuntimesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListRuntimesResponse`
        """
        return self.list_runtimes_with_http_info(request)

    def list_runtimes_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/metadata/runtimes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRuntimesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_templates_async(self, request):
        """获取所有支持的应用组件模板

        此API用来获取所有内置应用组件模板。


        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkservicestage.v2.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v2.ListTemplatesResponse`
        """
        return self.list_templates_with_http_info(request)

    def list_templates_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/cas/metadata/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTemplatesResponse',
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
