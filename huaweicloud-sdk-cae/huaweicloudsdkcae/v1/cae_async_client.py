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


class CaeAsyncClient(Client):
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
        super(CaeAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcae.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CaeClient":
            raise TypeError("client type error, support client type is CaeClient")

        return ClientBuilder(clazz)

    def create_agency_async(self, request):
        """创建委托

        本接口用于创建cae_trust委托
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgency
        :type request: :class:`huaweicloudsdkcae.v1.CreateAgencyRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateAgencyResponse`
        """
        return self.create_agency_with_http_info(request)

    def create_agency_with_http_info(self, request):
        all_params = ['body']
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
            resource_path='/v1/{project_id}/cae/agencies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_agency_async(self, request):
        """获取委托

        本接口用于获取cae_trust委托，如果委托不存在则创建委托
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgency
        :type request: :class:`huaweicloudsdkcae.v1.ShowAgencyRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowAgencyResponse`
        """
        return self.show_agency_with_http_info(request)

    def show_agency_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/cae/agencies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_application_async(self, request):
        """创建应用

        本接口用于创建一个应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApplication
        :type request: :class:`huaweicloudsdkcae.v1.CreateApplicationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateApplicationResponse`
        """
        return self.create_application_with_http_info(request)

    def create_application_with_http_info(self, request):
        all_params = ['x_environment_id', 'body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v1/{project_id}/cae/applications',
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

    def delete_application_async(self, request):
        """删除应用

        本接口用于删除指定应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkcae.v1.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteApplicationResponse`
        """
        return self.delete_application_with_http_info(request)

    def delete_application_with_http_info(self, request):
        all_params = ['application_id', 'x_environment_id', 'x_enterprise_project_id']
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
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}',
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

    def list_applications_async(self, request):
        """获取应用列表

        本接口用于获取当前环境下的应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdkcae.v1.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListApplicationsResponse`
        """
        return self.list_applications_with_http_info(request)

    def list_applications_with_http_info(self, request):
        all_params = ['x_environment_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications',
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

    def show_application_async(self, request):
        """获取应用

        本接口用于获取指定应用详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApplication
        :type request: :class:`huaweicloudsdkcae.v1.ShowApplicationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowApplicationResponse`
        """
        return self.show_application_with_http_info(request)

    def show_application_with_http_info(self, request):
        all_params = ['application_id', 'x_environment_id', 'x_enterprise_project_id']
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
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_component_async(self, request):
        """创建组件

        本接口用于创建一个组件，组件是CAE的最小部署单位，支持将用户的源码，部署包，镜像等资源部署到组件上
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateComponent
        :type request: :class:`huaweicloudsdkcae.v1.CreateComponentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentResponse`
        """
        return self.create_component_with_http_info(request)

    def create_component_with_http_info(self, request):
        all_params = ['x_environment_id', 'application_id', 'body', 'x_enterprise_project_id']
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
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components',
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

    def delete_component_async(self, request):
        """删除组件

        本接口用于删除指定的组件，组件是CAE的最小部署单位，支持将用户的源码，部署包，镜像等资源部署到组件上
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteComponent
        :type request: :class:`huaweicloudsdkcae.v1.DeleteComponentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteComponentResponse`
        """
        return self.delete_component_with_http_info(request)

    def delete_component_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}',
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

    def execute_action_async(self, request):
        """操作组件

        本接口用于对组件执行指定操作，如部署、升级、重启、停止、启动、伸缩、重试、配置、回滚
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteAction
        :type request: :class:`huaweicloudsdkcae.v1.ExecuteActionRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ExecuteActionResponse`
        """
        return self.execute_action_with_http_info(request)

    def execute_action_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_component_snapshots_async(self, request):
        """获取组件快照列表

        本接口用于获取组件快照版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponentSnapshots
        :type request: :class:`huaweicloudsdkcae.v1.ListComponentSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListComponentSnapshotsResponse`
        """
        return self.list_component_snapshots_with_http_info(request)

    def list_component_snapshots_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/snapshots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListComponentSnapshotsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_components_async(self, request):
        """获取组件列表

        本接口用于获取组件列表，组件是CAE的最小部署单位，支持将用户的源码，部署包，镜像等资源部署到组件上
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponents
        :type request: :class:`huaweicloudsdkcae.v1.ListComponentsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListComponentsResponse`
        """
        return self.list_components_with_http_info(request)

    def list_components_with_http_info(self, request):
        all_params = ['x_environment_id', 'application_id', 'x_enterprise_project_id', 'limit', 'offset']
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

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components',
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

    def list_events_async(self, request):
        """获取事件列表

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkcae.v1.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListEventsResponse`
        """
        return self.list_events_with_http_info(request)

    def list_events_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_async(self, request):
        """获取组件实例列表

        本接口用于获取组件实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkcae.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListInstancesResponse`
        """
        return self.list_instances_with_http_info(request)

    def list_instances_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/instances',
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

    def show_component_async(self, request):
        """获取组件

        本接口用于获取指定的组件，组件是CAE的最小部署单位，支持将用户的源码，部署包，镜像等资源部署到组件上
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowComponent
        :type request: :class:`huaweicloudsdkcae.v1.ShowComponentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowComponentResponse`
        """
        return self.show_component_with_http_info(request)

    def show_component_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowComponentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_component_async(self, request):
        """更新组件

        本接口用于更新指定的组件，组件是CAE的最小部署单位，支持将用户的源码，部署包，镜像等资源部署到组件上
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateComponent
        :type request: :class:`huaweicloudsdkcae.v1.UpdateComponentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateComponentResponse`
        """
        return self.update_component_with_http_info(request)

    def update_component_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateComponentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_component_configuration_async(self, request):
        """创建组件配置

        本接口用于创建组件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateComponentConfiguration
        :type request: :class:`huaweicloudsdkcae.v1.CreateComponentConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentConfigurationResponse`
        """
        return self.create_component_configuration_with_http_info(request)

    def create_component_configuration_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/configurations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateComponentConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_component_configuration_async(self, request):
        """删除组件配置

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteComponentConfiguration
        :type request: :class:`huaweicloudsdkcae.v1.DeleteComponentConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteComponentConfigurationResponse`
        """
        return self.delete_component_configuration_with_http_info(request)

    def delete_component_configuration_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/configurations',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteComponentConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configurations_async(self, request):
        """获取组件配置列表

        本接口用于获取组件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkcae.v1.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListConfigurationsResponse`
        """
        return self.list_configurations_with_http_info(request)

    def list_configurations_with_http_info(self, request):
        all_params = ['component_id', 'x_environment_id', 'application_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/configurations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_environment_async(self, request):
        """创建环境

        本接口用于创建一个环境，环境是CAE定义的一个资源维度，所有的用户组件都放在环境下
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnvironment
        :type request: :class:`huaweicloudsdkcae.v1.CreateEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateEnvironmentResponse`
        """
        return self.create_environment_with_http_info(request)

    def create_environment_with_http_info(self, request):
        all_params = ['body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v1/{project_id}/cae/environments',
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

    def delete_environment_async(self, request):
        """删除环境

        本接口用于删除环境，暂未开放。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnvironment
        :type request: :class:`huaweicloudsdkcae.v1.DeleteEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteEnvironmentResponse`
        """
        return self.delete_environment_with_http_info(request)

    def delete_environment_with_http_info(self, request):
        all_params = ['environment_id', 'x_enterprise_project_id']
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/environments/{environment_id}',
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

    def list_environments_async(self, request):
        """获取环境列表

        本接口用于获取当前租户环境信息，环境是CAE定义的一个资源维度，所有的用户组件都放在环境下
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvironments
        :type request: :class:`huaweicloudsdkcae.v1.ListEnvironmentsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListEnvironmentsResponse`
        """
        return self.list_environments_with_http_info(request)

    def list_environments_with_http_info(self, request):
        all_params = ['x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/environments',
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

    def retry_job_async(self, request):
        """重试任务

        本接口用于重试任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryJob
        :type request: :class:`huaweicloudsdkcae.v1.RetryJobRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.RetryJobResponse`
        """
        return self.retry_job_with_http_info(request)

    def retry_job_with_http_info(self, request):
        all_params = ['job_id']
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
            resource_path='/v1/{project_id}/cae/jobs/{job_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RetryJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_async(self, request):
        """获取任务详情

        本接口用于获取任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkcae.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowJobResponse`
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        all_params = ['job_id', 'x_enterprise_project_id']
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

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_volume_async(self, request):
        """创建卷

        本接口用于创建卷
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVolume
        :type request: :class:`huaweicloudsdkcae.v1.CreateVolumeRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateVolumeResponse`
        """
        return self.create_volume_with_http_info(request)

    def create_volume_with_http_info(self, request):
        all_params = ['x_environment_id', 'body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v1/{project_id}/cae/volumes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_volume_async(self, request):
        """删除卷

        本接口用于创建卷
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVolume
        :type request: :class:`huaweicloudsdkcae.v1.DeleteVolumeRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteVolumeResponse`
        """
        return self.delete_volume_with_http_info(request)

    def delete_volume_with_http_info(self, request):
        all_params = ['id', 'x_environment_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/volumes/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_volumes_async(self, request):
        """获取卷列表

        本接口用于获取卷列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVolumes
        :type request: :class:`huaweicloudsdkcae.v1.ListVolumesRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListVolumesResponse`
        """
        return self.list_volumes_with_http_info(request)

    def list_volumes_with_http_info(self, request):
        all_params = ['x_environment_id', 'resource_type', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

        header_params = {}
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cae/volumes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVolumesResponse',
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
