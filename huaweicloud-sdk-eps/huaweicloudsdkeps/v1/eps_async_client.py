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


class EpsAsyncClient(Client):
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
        super(EpsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeps.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "EpsClient":
            raise TypeError("client type error, support client type is EpsClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_enterprise_project_async(self, request):
        """创建企业项目

        创建企业项目。

        :param CreateEnterpriseProjectRequest request
        :return: CreateEnterpriseProjectResponse
        """
        return self.create_enterprise_project_with_http_info(request)

    def create_enterprise_project_with_http_info(self, request):
        """创建企业项目

        创建企业项目。

        :param CreateEnterpriseProjectRequest request
        :return: CreateEnterpriseProjectResponse
        """

        all_params = ['create_ep']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disable_enterprise_project_async(self, request):
        """停用企业项目

        停用企业项目。

        :param DisableEnterpriseProjectRequest request
        :return: DisableEnterpriseProjectResponse
        """
        return self.disable_enterprise_project_with_http_info(request)

    def disable_enterprise_project_with_http_info(self, request):
        """停用企业项目

        停用企业项目。

        :param DisableEnterpriseProjectRequest request
        :return: DisableEnterpriseProjectResponse
        """

        all_params = ['enterprise_project_id', 'action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects/{enterprise_project_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisableEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_enterprise_project_async(self, request):
        """启用企业项目

        启用企业项目。

        :param EnableEnterpriseProjectRequest request
        :return: EnableEnterpriseProjectResponse
        """
        return self.enable_enterprise_project_with_http_info(request)

    def enable_enterprise_project_with_http_info(self, request):
        """启用企业项目

        启用企业项目。

        :param EnableEnterpriseProjectRequest request
        :return: EnableEnterpriseProjectResponse
        """

        all_params = ['enterprise_project_id', 'action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects/{enterprise_project_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EnableEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_api_versions_async(self, request):
        """查询API版本列表

        查询企业项目的API版本列表。

        :param ListApiVersionsRequest request
        :return: ListApiVersionsResponse
        """
        return self.list_api_versions_with_http_info(request)

    def list_api_versions_with_http_info(self, request):
        """查询API版本列表

        查询企业项目的API版本列表。

        :param ListApiVersionsRequest request
        :return: ListApiVersionsResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_enterprise_project_async(self, request):
        """查询企业项目列表

        查询当前用户已授权的企业项目列表，用户可以使用企业项目绑定资源。

        :param ListEnterpriseProjectRequest request
        :return: ListEnterpriseProjectResponse
        """
        return self.list_enterprise_project_with_http_info(request)

    def list_enterprise_project_with_http_info(self, request):
        """查询企业项目列表

        查询当前用户已授权的企业项目列表，用户可以使用企业项目绑定资源。

        :param ListEnterpriseProjectRequest request
        :return: ListEnterpriseProjectResponse
        """

        all_params = ['offset', 'id', 'limit', 'name', 'sort_dir', 'sort_key', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v1.0/enterprise-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def migrate_resource_async(self, request):
        """迁移资源

        迁移资源到目标企业项目。

        :param MigrateResourceRequest request
        :return: MigrateResourceResponse
        """
        return self.migrate_resource_with_http_info(request)

    def migrate_resource_with_http_info(self, request):
        """迁移资源

        迁移资源到目标企业项目。

        :param MigrateResourceRequest request
        :return: MigrateResourceResponse
        """

        all_params = ['enterprise_project_id', 'req_migrate_resource']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects/{enterprise_project_id}/resources-migrate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='MigrateResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def modify_enterprise_project_async(self, request):
        """修改企业项目

        修改企业项目。当前仅支持修改名称和描述。

        :param ModifyEnterpriseProjectRequest request
        :return: ModifyEnterpriseProjectResponse
        """
        return self.modify_enterprise_project_with_http_info(request)

    def modify_enterprise_project_with_http_info(self, request):
        """修改企业项目

        修改企业项目。当前仅支持修改名称和描述。

        :param ModifyEnterpriseProjectRequest request
        :return: ModifyEnterpriseProjectResponse
        """

        all_params = ['enterprise_project_id', 'modify_ep']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects/{enterprise_project_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ModifyEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_api_version_async(self, request):
        """查询API版本号详情

        查询指定的企业项目API版本号详情

        :param ShowApiVersionRequest request
        :return: ShowApiVersionResponse
        """
        return self.show_api_version_with_http_info(request)

    def show_api_version_with_http_info(self, request):
        """查询API版本号详情

        查询指定的企业项目API版本号详情

        :param ShowApiVersionRequest request
        :return: ShowApiVersionResponse
        """

        all_params = ['api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

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
            resource_path='/{api_version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApiVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_enterprise_project_async(self, request):
        """查询企业项目详情

        查询企业项目详情。

        :param ShowEnterpriseProjectRequest request
        :return: ShowEnterpriseProjectResponse
        """
        return self.show_enterprise_project_with_http_info(request)

    def show_enterprise_project_with_http_info(self, request):
        """查询企业项目详情

        查询企业项目详情。

        :param ShowEnterpriseProjectRequest request
        :return: ShowEnterpriseProjectResponse
        """

        all_params = ['enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            resource_path='/v1.0/enterprise-projects/{enterprise_project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_enterprise_project_quota_async(self, request):
        """查询企业项目配额

        查询企业项目的配额信息。

        :param ShowEnterpriseProjectQuotaRequest request
        :return: ShowEnterpriseProjectQuotaResponse
        """
        return self.show_enterprise_project_quota_with_http_info(request)

    def show_enterprise_project_quota_with_http_info(self, request):
        """查询企业项目配额

        查询企业项目的配额信息。

        :param ShowEnterpriseProjectQuotaRequest request
        :return: ShowEnterpriseProjectQuotaResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEnterpriseProjectQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_resource_bind_enterprise_project_async(self, request):
        """查询企业项目绑定的资源列表

        查询企业项目下绑定的资源详情。

        :param ShowResourceBindEnterpriseProjectRequest request
        :return: ShowResourceBindEnterpriseProjectResponse
        """
        return self.show_resource_bind_enterprise_project_with_http_info(request)

    def show_resource_bind_enterprise_project_with_http_info(self, request):
        """查询企业项目绑定的资源列表

        查询企业项目下绑定的资源详情。

        :param ShowResourceBindEnterpriseProjectRequest request
        :return: ShowResourceBindEnterpriseProjectResponse
        """

        all_params = ['enterprise_project_id', 'req_ep_resouce']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects/{enterprise_project_id}/resources/filter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResourceBindEnterpriseProjectResponse',
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
