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
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

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

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def change_application_async(self, request):
        """修改应用信息

        此API通过应用ID修改应用信息。

        :param ChangeApplicationRequest request
        :return: ChangeApplicationResponse
        """
        return self.change_application_with_http_info(request)

    def change_application_with_http_info(self, request):
        """修改应用信息

        此API通过应用ID修改应用信息。

        :param ChangeApplicationRequest request
        :return: ChangeApplicationResponse
        """

        all_params = ['application_id', 'application_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_application_configuration_async(self, request):
        """修改应用配置信息

        通过此API修改应用配置信息。

        :param ChangeApplicationConfigurationRequest request
        :return: ChangeApplicationConfigurationResponse
        """
        return self.change_application_configuration_with_http_info(request)

    def change_application_configuration_with_http_info(self, request):
        """修改应用配置信息

        通过此API修改应用配置信息。

        :param ChangeApplicationConfigurationRequest request
        :return: ChangeApplicationConfigurationResponse
        """

        all_params = ['application_id', 'application_config_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeApplicationConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_component_async(self, request):
        """根据组件ID修改组件信息

        此API通过组件ID修改组件信息。

        :param ChangeComponentRequest request
        :return: ChangeComponentResponse
        """
        return self.change_component_with_http_info(request)

    def change_component_with_http_info(self, request):
        """根据组件ID修改组件信息

        此API通过组件ID修改组件信息。

        :param ChangeComponentRequest request
        :return: ChangeComponentResponse
        """

        all_params = ['application_id', 'component_id', 'component_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeComponentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_environment_async(self, request):
        """修改环境信息

        此API通过环境ID修改环境信息。

        :param ChangeEnvironmentRequest request
        :return: ChangeEnvironmentResponse
        """
        return self.change_environment_with_http_info(request)

    def change_environment_with_http_info(self, request):
        """修改环境信息

        此API通过环境ID修改环境信息。

        :param ChangeEnvironmentRequest request
        :return: ChangeEnvironmentResponse
        """

        all_params = ['environment_id', 'environment_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_instance_async(self, request):
        """修改应用组件实例

        通过此API修改应用组件实例。

        :param ChangeInstanceRequest request
        :return: ChangeInstanceResponse
        """
        return self.change_instance_with_http_info(request)

    def change_instance_with_http_info(self, request):
        """修改应用组件实例

        通过此API修改应用组件实例。

        :param ChangeInstanceRequest request
        :return: ChangeInstanceResponse
        """

        all_params = ['application_id', 'component_id', 'instance_id', 'instance_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_resource_in_environment_async(self, request):
        """修改环境资源

        此API用来修改环境资源。

        :param ChangeResourceInEnvironmentRequest request
        :return: ChangeResourceInEnvironmentResponse
        """
        return self.change_resource_in_environment_with_http_info(request)

    def change_resource_in_environment_with_http_info(self, request):
        """修改环境资源

        此API用来修改环境资源。

        :param ChangeResourceInEnvironmentRequest request
        :return: ChangeResourceInEnvironmentResponse
        """

        all_params = ['environment_id', 'environment_resource_modify']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeResourceInEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_application_async(self, request):
        """创建应用

        应用是一个功能相对完备的业务系统，由一个或多个特性相关的组件组成。  此API用来创建应用。 

        :param CreateApplicationRequest request
        :return: CreateApplicationResponse
        """
        return self.create_application_with_http_info(request)

    def create_application_with_http_info(self, request):
        """创建应用

        应用是一个功能相对完备的业务系统，由一个或多个特性相关的组件组成。  此API用来创建应用。 

        :param CreateApplicationRequest request
        :return: CreateApplicationResponse
        """

        all_params = ['application_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_component_async(self, request):
        """应用中创建组件

        应用组件是组成应用的某个业务特性实现，以代码或者软件包为载体，可独立部署运行。  此API用来在应用中创建组件。 

        :param CreateComponentRequest request
        :return: CreateComponentResponse
        """
        return self.create_component_with_http_info(request)

    def create_component_with_http_info(self, request):
        """应用中创建组件

        应用组件是组成应用的某个业务特性实现，以代码或者软件包为载体，可独立部署运行。  此API用来在应用中创建组件。 

        :param CreateComponentRequest request
        :return: CreateComponentResponse
        """

        all_params = ['application_id', 'component_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateComponentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_environment_async(self, request):
        """创建环境

        环境是用于应用部署和运行的计算、存储、网络等基础设施的集合。Servicestage把相同VPC下的CCE集群加上多个ELB、RDS、DCS实例组合为一个环境，如：开发环境，测试环境，预生产环境，生产环境。环境内网络互通，可以按环境维度来管理资源、部署服务，减少具体基础设施运维管理的复杂性。  此API用来创建环境。 

        :param CreateEnvironmentRequest request
        :return: CreateEnvironmentResponse
        """
        return self.create_environment_with_http_info(request)

    def create_environment_with_http_info(self, request):
        """创建环境

        环境是用于应用部署和运行的计算、存储、网络等基础设施的集合。Servicestage把相同VPC下的CCE集群加上多个ELB、RDS、DCS实例组合为一个环境，如：开发环境，测试环境，预生产环境，生产环境。环境内网络互通，可以按环境维度来管理资源、部署服务，减少具体基础设施运维管理的复杂性。  此API用来创建环境。 

        :param CreateEnvironmentRequest request
        :return: CreateEnvironmentResponse
        """

        all_params = ['environment_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_instance_async(self, request):
        """创建组件实例

        此API用来创建应用组件实例。

        :param CreateInstanceRequest request
        :return: CreateInstanceResponse
        """
        return self.create_instance_with_http_info(request)

    def create_instance_with_http_info(self, request):
        """创建组件实例

        此API用来创建应用组件实例。

        :param CreateInstanceRequest request
        :return: CreateInstanceResponse
        """

        all_params = ['application_id', 'component_id', 'instance_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_application_async(self, request):
        """根据应用ID删除应用

        此API通过应用ID删除应用。

        :param DeleteApplicationRequest request
        :return: DeleteApplicationResponse
        """
        return self.delete_application_with_http_info(request)

    def delete_application_with_http_info(self, request):
        """根据应用ID删除应用

        此API通过应用ID删除应用。

        :param DeleteApplicationRequest request
        :return: DeleteApplicationResponse
        """

        all_params = ['application_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_application_configuration_async(self, request):
        """删除应用配置

        通过此API删除应用配置信息。

        :param DeleteApplicationConfigurationRequest request
        :return: DeleteApplicationConfigurationResponse
        """
        return self.delete_application_configuration_with_http_info(request)

    def delete_application_configuration_with_http_info(self, request):
        """删除应用配置

        通过此API删除应用配置信息。

        :param DeleteApplicationConfigurationRequest request
        :return: DeleteApplicationConfigurationResponse
        """

        all_params = ['application_id', 'environment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/configuration',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteApplicationConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_component_async(self, request):
        """根据应用组件ID删除应用组件

        此API通过应用组件ID删除应用组件。

        :param DeleteComponentRequest request
        :return: DeleteComponentResponse
        """
        return self.delete_component_with_http_info(request)

    def delete_component_with_http_info(self, request):
        """根据应用组件ID删除应用组件

        此API通过应用组件ID删除应用组件。

        :param DeleteComponentRequest request
        :return: DeleteComponentResponse
        """

        all_params = ['application_id', 'component_id', 'force']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteComponentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_environment_async(self, request):
        """根据环境ID删除环境

        此API通过环境ID删除环境。

        :param DeleteEnvironmentRequest request
        :return: DeleteEnvironmentResponse
        """
        return self.delete_environment_with_http_info(request)

    def delete_environment_with_http_info(self, request):
        """根据环境ID删除环境

        此API通过环境ID删除环境。

        :param DeleteEnvironmentRequest request
        :return: DeleteEnvironmentResponse
        """

        all_params = ['environment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/environments/{environment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_instance_async(self, request):
        """删除应用组件实例

        通过此API删除应用组件实例。

        :param DeleteInstanceRequest request
        :return: DeleteInstanceResponse
        """
        return self.delete_instance_with_http_info(request)

    def delete_instance_with_http_info(self, request):
        """删除应用组件实例

        通过此API删除应用组件实例。

        :param DeleteInstanceRequest request
        :return: DeleteInstanceResponse
        """

        all_params = ['application_id', 'component_id', 'instance_id', 'force']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_applications_async(self, request):
        """获取所有应用

        通过此API可以获取所有已经创建的应用。

        :param ListApplicationsRequest request
        :return: ListApplicationsResponse
        """
        return self.list_applications_with_http_info(request)

    def list_applications_with_http_info(self, request):
        """获取所有应用

        通过此API可以获取所有已经创建的应用。

        :param ListApplicationsRequest request
        :return: ListApplicationsResponse
        """

        all_params = ['limit', 'offset', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApplicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_components_async(self, request):
        """获取应用所有组件

        通过此API获取应用下所有应用组件。

        :param ListComponentsRequest request
        :return: ListComponentsResponse
        """
        return self.list_components_with_http_info(request)

    def list_components_with_http_info(self, request):
        """获取应用所有组件

        通过此API获取应用下所有应用组件。

        :param ListComponentsRequest request
        :return: ListComponentsResponse
        """

        all_params = ['application_id', 'limit', 'offset', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListComponentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_environments_async(self, request):
        """获取所有环境

        此API用来获取所有已经创建环境。

        :param ListEnvironmentsRequest request
        :return: ListEnvironmentsResponse
        """
        return self.list_environments_with_http_info(request)

    def list_environments_with_http_info(self, request):
        """获取所有环境

        此API用来获取所有已经创建环境。

        :param ListEnvironmentsRequest request
        :return: ListEnvironmentsResponse
        """

        all_params = ['limit', 'offset', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/environments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnvironmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instance_snapshots_async(self, request):
        """获取组件实例快照

        通过此API获取应用组件实例快照信息。

        :param ListInstanceSnapshotsRequest request
        :return: ListInstanceSnapshotsResponse
        """
        return self.list_instance_snapshots_with_http_info(request)

    def list_instance_snapshots_with_http_info(self, request):
        """获取组件实例快照

        通过此API获取应用组件实例快照信息。

        :param ListInstanceSnapshotsRequest request
        :return: ListInstanceSnapshotsResponse
        """

        all_params = ['application_id', 'component_id', 'instance_id', 'limit', 'offset', 'snapshot_order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}/snapshots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstanceSnapshotsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instances_async(self, request):
        """获取应用组件实例

        通过此API获取组件下的所有组件实例。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """
        return self.list_instances_with_http_info(request)

    def list_instances_with_http_info(self, request):
        """获取应用组件实例

        通过此API获取组件下的所有组件实例。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """

        all_params = ['application_id', 'component_id', 'limit', 'offset', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_application_configuration_async(self, request):
        """获取应用配置

        通过此API获取应用配置信息。

        :param ShowApplicationConfigurationRequest request
        :return: ShowApplicationConfigurationResponse
        """
        return self.show_application_configuration_with_http_info(request)

    def show_application_configuration_with_http_info(self, request):
        """获取应用配置

        通过此API获取应用配置信息。

        :param ShowApplicationConfigurationRequest request
        :return: ShowApplicationConfigurationResponse
        """

        all_params = ['application_id', 'environment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/configuration',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApplicationConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_application_detail_async(self, request):
        """根据应用ID获取应用详细信息

        此API通过应用ID获取应用详细信息。

        :param ShowApplicationDetailRequest request
        :return: ShowApplicationDetailResponse
        """
        return self.show_application_detail_with_http_info(request)

    def show_application_detail_with_http_info(self, request):
        """根据应用ID获取应用详细信息

        此API通过应用ID获取应用详细信息。

        :param ShowApplicationDetailRequest request
        :return: ShowApplicationDetailResponse
        """

        all_params = ['application_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApplicationDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_component_detail_async(self, request):
        """根据组件ID获取应用组件信息

        通过组件ID获取应用组件信息。

        :param ShowComponentDetailRequest request
        :return: ShowComponentDetailResponse
        """
        return self.show_component_detail_with_http_info(request)

    def show_component_detail_with_http_info(self, request):
        """根据组件ID获取应用组件信息

        通过组件ID获取应用组件信息。

        :param ShowComponentDetailRequest request
        :return: ShowComponentDetailResponse
        """

        all_params = ['application_id', 'component_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowComponentDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_environment_detail_async(self, request):
        """根据环境ID获取环境详细信息

        此API通过环境ID获取环境详细信息。

        :param ShowEnvironmentDetailRequest request
        :return: ShowEnvironmentDetailResponse
        """
        return self.show_environment_detail_with_http_info(request)

    def show_environment_detail_with_http_info(self, request):
        """根据环境ID获取环境详细信息

        此API通过环境ID获取环境详细信息。

        :param ShowEnvironmentDetailRequest request
        :return: ShowEnvironmentDetailResponse
        """

        all_params = ['environment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/environments/{environment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEnvironmentDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance_detail_async(self, request):
        """根据实例ID获取实例详细信息

        此API通过实例ID获取实例详细信息。

        :param ShowInstanceDetailRequest request
        :return: ShowInstanceDetailResponse
        """
        return self.show_instance_detail_with_http_info(request)

    def show_instance_detail_with_http_info(self, request):
        """根据实例ID获取实例详细信息

        此API通过实例ID获取实例详细信息。

        :param ShowInstanceDetailRequest request
        :return: ShowInstanceDetailResponse
        """

        all_params = ['application_id', 'component_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/applications/{application_id}/components/{component_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_job_detail_async(self, request):
        """获取部署任务详细信息

        通过此API获取部署任务详细信息。

        :param ShowJobDetailRequest request
        :return: ShowJobDetailResponse
        """
        return self.show_job_detail_with_http_info(request)

    def show_job_detail_with_http_info(self, request):
        """获取部署任务详细信息

        通过此API获取部署任务详细信息。

        :param ShowJobDetailRequest request
        :return: ShowJobDetailResponse
        """

        all_params = ['job_id', 'instance_id', 'limit', 'offset', 'desc']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_instance_action_async(self, request):
        """对组件实例的操作

        通过此API获取对组件实例的操作。

        :param UpdateInstanceActionRequest request
        :return: UpdateInstanceActionResponse
        """
        return self.update_instance_action_with_http_info(request)

    def update_instance_action_with_http_info(self, request):
        """对组件实例的操作

        通过此API获取对组件实例的操作。

        :param UpdateInstanceActionRequest request
        :return: UpdateInstanceActionResponse
        """

        all_params = ['application_id', 'component_id', 'instance_id', 'instance_action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateInstanceActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_file_async(self, request):
        """创建仓库文件

        在指定仓库项目下创建文件。

        :param CreateFileRequest request
        :return: CreateFileResponse
        """
        return self.create_file_with_http_info(request)

    def create_file_with_http_info(self, request):
        """创建仓库文件

        在指定仓库项目下创建文件。

        :param CreateFileRequest request
        :return: CreateFileResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'path', 'ref', 'file_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_hook_async(self, request):
        """创建项目hook

        创建指定项目的hook。

        :param CreateHookRequest request
        :return: CreateHookResponse
        """
        return self.create_hook_with_http_info(request)

    def create_hook_with_http_info(self, request):
        """创建项目hook

        创建指定项目的hook。

        :param CreateHookRequest request
        :return: CreateHookResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'hook_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateHookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_o_auth_async(self, request):
        """创建OAuth授权

        创建指定Git仓库类型的OAuth授权。

        :param CreateOAuthRequest request
        :return: CreateOAuthResponse
        """
        return self.create_o_auth_with_http_info(request)

    def create_o_auth_with_http_info(self, request):
        """创建OAuth授权

        创建指定Git仓库类型的OAuth授权。

        :param CreateOAuthRequest request
        :return: CreateOAuthResponse
        """

        all_params = ['repo_type', 'tag', 'o_auth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateOAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_password_auth_async(self, request):
        """创建口令授权

        创建指定Git仓库类型的口令授权。

        :param CreatePasswordAuthRequest request
        :return: CreatePasswordAuthResponse
        """
        return self.create_password_auth_with_http_info(request)

    def create_password_auth_with_http_info(self, request):
        """创建口令授权

        创建指定Git仓库类型的口令授权。

        :param CreatePasswordAuthRequest request
        :return: CreatePasswordAuthResponse
        """

        all_params = ['repo_type', 'access_password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreatePasswordAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_personal_auth_async(self, request):
        """创建私人令牌授权

        创建指定Git仓库类型的私人令牌授权。

        :param CreatePersonalAuthRequest request
        :return: CreatePersonalAuthResponse
        """
        return self.create_personal_auth_with_http_info(request)

    def create_personal_auth_with_http_info(self, request):
        """创建私人令牌授权

        创建指定Git仓库类型的私人令牌授权。

        :param CreatePersonalAuthRequest request
        :return: CreatePersonalAuthResponse
        """

        all_params = ['repo_type', 'access_token']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreatePersonalAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_project_async(self, request):
        """创建软件仓库项目

        创建指定组织下的软件仓库项目。

        :param CreateProjectRequest request
        :return: CreateProjectResponse
        """
        return self.create_project_with_http_info(request)

    def create_project_with_http_info(self, request):
        """创建软件仓库项目

        创建指定组织下的软件仓库项目。

        :param CreateProjectRequest request
        :return: CreateProjectResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_tag_async(self, request):
        """创建项目tag标签

        创建指定项目的tag标签。

        :param CreateTagRequest request
        :return: CreateTagResponse
        """
        return self.create_tag_with_http_info(request)

    def create_tag_with_http_info(self, request):
        """创建项目tag标签

        创建指定项目的tag标签。

        :param CreateTagRequest request
        :return: CreateTagResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'ref', 'tag_create']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_authorize_async(self, request):
        """删除仓库授权

        通过名称删除仓库授权。

        :param DeleteAuthorizeRequest request
        :return: DeleteAuthorizeResponse
        """
        return self.delete_authorize_with_http_info(request)

    def delete_authorize_with_http_info(self, request):
        """删除仓库授权

        通过名称删除仓库授权。

        :param DeleteAuthorizeRequest request
        :return: DeleteAuthorizeResponse
        """

        all_params = ['name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/auths/{name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAuthorizeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_file_async(self, request):
        """删除仓库文件

        删除指定项目仓库下的文件。

        :param DeleteFileRequest request
        :return: DeleteFileResponse
        """
        return self.delete_file_with_http_info(request)

    def delete_file_with_http_info(self, request):
        """删除仓库文件

        删除指定项目仓库下的文件。

        :param DeleteFileRequest request
        :return: DeleteFileResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'path', 'ref', 'message', 'sha']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/files/{namespace}/{project}/{path}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_hook_async(self, request):
        """删除项目hook

        删除指定项目的hook。

        :param DeleteHookRequest request
        :return: DeleteHookResponse
        """
        return self.delete_hook_with_http_info(request)

    def delete_hook_with_http_info(self, request):
        """删除项目hook

        删除指定项目的hook。

        :param DeleteHookRequest request
        :return: DeleteHookResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'hook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/hooks/{hook_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteHookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_tag_async(self, request):
        """删除项目tag标签

        删除指定项目的tag标签。

        :param DeleteTagRequest request
        :return: DeleteTagResponse
        """
        return self.delete_tag_with_http_info(request)

    def delete_tag_with_http_info(self, request):
        """删除项目tag标签

        删除指定项目的tag标签。

        :param DeleteTagRequest request
        :return: DeleteTagResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'tag_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/tags/{tag_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_authorizations_async(self, request):
        """获取仓库授权列表

        获取所有Git仓库授权信息。

        :param ListAuthorizationsRequest request
        :return: ListAuthorizationsResponse
        """
        return self.list_authorizations_with_http_info(request)

    def list_authorizations_with_http_info(self, request):
        """获取仓库授权列表

        获取所有Git仓库授权信息。

        :param ListAuthorizationsRequest request
        :return: ListAuthorizationsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/auths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAuthorizationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_branches_async(self, request):
        """获取项目分支

        获取指定项目的所有分支列表。

        :param ListBranchesRequest request
        :return: ListBranchesResponse
        """
        return self.list_branches_with_http_info(request)

    def list_branches_with_http_info(self, request):
        """获取项目分支

        获取指定项目的所有分支列表。

        :param ListBranchesRequest request
        :return: ListBranchesResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/branches',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBranchesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_commits_async(self, request):
        """获取项目commit提交记录

        获取指定项目的最近10次commit提交记录。

        :param ListCommitsRequest request
        :return: ListCommitsResponse
        """
        return self.list_commits_with_http_info(request)

    def list_commits_with_http_info(self, request):
        """获取项目commit提交记录

        获取指定项目的最近10次commit提交记录。

        :param ListCommitsRequest request
        :return: ListCommitsResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/commits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCommitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_hooks_async(self, request):
        """获取项目hooks

        获取指定项目的所有hooks

        :param ListHooksRequest request
        :return: ListHooksResponse
        """
        return self.list_hooks_with_http_info(request)

    def list_hooks_with_http_info(self, request):
        """获取项目hooks

        获取指定项目的所有hooks

        :param ListHooksRequest request
        :return: ListHooksResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/hooks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_namespaces_async(self, request):
        """获取仓库的namespaces

        获取仓库的namespaces。

        :param ListNamespacesRequest request
        :return: ListNamespacesResponse
        """
        return self.list_namespaces_with_http_info(request)

    def list_namespaces_with_http_info(self, request):
        """获取仓库的namespaces

        获取仓库的namespaces。

        :param ListNamespacesRequest request
        :return: ListNamespacesResponse
        """

        all_params = ['x_repo_auth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/namespaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNamespacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_projects_async(self, request):
        """获取组织下所有项目

        获取指定组织下的所有项目。

        :param ListProjectsRequest request
        :return: ListProjectsResponse
        """
        return self.list_projects_with_http_info(request)

    def list_projects_with_http_info(self, request):
        """获取组织下所有项目

        获取指定组织下的所有项目。

        :param ListProjectsRequest request
        :return: ListProjectsResponse
        """

        all_params = ['x_repo_auth', 'namespace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tags_async(self, request):
        """获取项目的所有tag标签

        获取指定项目的所有tag标签。

        :param ListTagsRequest request
        :return: ListTagsResponse
        """
        return self.list_tags_with_http_info(request)

    def list_tags_with_http_info(self, request):
        """获取项目的所有tag标签

        获取指定项目的所有tag标签。

        :param ListTagsRequest request
        :return: ListTagsResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/{namespace}/{project}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_trees_async(self, request):
        """获取仓库文件列表

        获取指定项目仓库的文件列表。

        :param ListTreesRequest request
        :return: ListTreesResponse
        """
        return self.list_trees_with_http_info(request)

    def list_trees_with_http_info(self, request):
        """获取仓库文件列表

        获取指定项目仓库的文件列表。

        :param ListTreesRequest request
        :return: ListTreesResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/files/{namespace}/{project}/trees',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTreesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_content_async(self, request):
        """获取仓库文件内容

        获取指定项目仓库下文件的内容。

        :param ShowContentRequest request
        :return: ShowContentResponse
        """
        return self.show_content_with_http_info(request)

    def show_content_with_http_info(self, request):
        """获取仓库文件内容

        获取指定项目仓库下文件的内容。

        :param ShowContentRequest request
        :return: ShowContentResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'path', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/files/{namespace}/{project}/{path}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowContentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_project_detail_async(self, request):
        """通过clone url 获取仓库信息

        通过指定的clone url 获取仓库信息。

        :param ShowProjectDetailRequest request
        :return: ShowProjectDetailResponse
        """
        return self.show_project_detail_with_http_info(request)

    def show_project_detail_with_http_info(self, request):
        """通过clone url 获取仓库信息

        通过指定的clone url 获取仓库信息。

        :param ShowProjectDetailRequest request
        :return: ShowProjectDetailResponse
        """

        all_params = ['x_repo_auth', 'clone_url']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/repos/project-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_redirect_url_async(self, request):
        """获取授权重定向URL

        获取指定Git仓库类型的授权重定向URL。

        :param ShowRedirectUrlRequest request
        :return: ShowRedirectUrlResponse
        """
        return self.show_redirect_url_with_http_info(request)

    def show_redirect_url_with_http_info(self, request):
        """获取授权重定向URL

        获取指定Git仓库类型的授权重定向URL。

        :param ShowRedirectUrlRequest request
        :return: ShowRedirectUrlResponse
        """

        all_params = ['repo_type', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/git/auths/{repo_type}/redirect',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRedirectUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_file_async(self, request):
        """更新仓库文件内容

        更新指定项目仓库下的文件内容。

        :param UpdateFileRequest request
        :return: UpdateFileResponse
        """
        return self.update_file_with_http_info(request)

    def update_file_with_http_info(self, request):
        """更新仓库文件内容

        更新指定项目仓库下的文件内容。

        :param UpdateFileRequest request
        :return: UpdateFileResponse
        """

        all_params = ['x_repo_auth', 'namespace', 'project', 'path', 'ref', 'file_update']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_flavors_async(self, request):
        """获取所有支持的应用资源规格

        通过此API获取所用支持的应用资源规格。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        """获取所有支持的应用资源规格

        通过此API获取所用支持的应用资源规格。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/metadata/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_runtimes_async(self, request):
        """获取所有支持的应用组件运行时类型

        此API用来获取所有支持应用组件运行时类型。

        :param ListRuntimesRequest request
        :return: ListRuntimesResponse
        """
        return self.list_runtimes_with_http_info(request)

    def list_runtimes_with_http_info(self, request):
        """获取所有支持的应用组件运行时类型

        此API用来获取所有支持应用组件运行时类型。

        :param ListRuntimesRequest request
        :return: ListRuntimesResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/metadata/runtimes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRuntimesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_templates_async(self, request):
        """获取所有支持的应用组件模板

        此API用来获取所有内置应用组件模板。

        :param ListTemplatesRequest request
        :return: ListTemplatesResponse
        """
        return self.list_templates_with_http_info(request)

    def list_templates_with_http_info(self, request):
        """获取所有支持的应用组件模板

        此API用来获取所有内置应用组件模板。

        :param ListTemplatesRequest request
        :return: ListTemplatesResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cas/metadata/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
