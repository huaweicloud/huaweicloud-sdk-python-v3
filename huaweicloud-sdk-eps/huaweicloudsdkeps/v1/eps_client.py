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


class EpsClient(Client):
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
        super(EpsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeps.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz, "GlobalCredentials")

    def create_ep(self, request):
        """创建企业项目

        创建企业项目。

        :param CreateEpRequest request
        :return: CreateEpResponse
        """
        return self.create_ep_with_http_info(request)

    def create_ep_with_http_info(self, request):
        """创建企业项目

        创建企业项目。

        :param CreateEpRequest request
        :return: CreateEpResponse
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
            response_type='CreateEpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disable_ep(self, request):
        """停用企业项目

        停用企业项目。

        :param DisableEpRequest request
        :return: DisableEpResponse
        """
        return self.disable_ep_with_http_info(request)

    def disable_ep_with_http_info(self, request):
        """停用企业项目

        停用企业项目。

        :param DisableEpRequest request
        :return: DisableEpResponse
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
            response_type='DisableEpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_ep(self, request):
        """启用企业项目

        启用企业项目。

        :param EnableEpRequest request
        :return: EnableEpResponse
        """
        return self.enable_ep_with_http_info(request)

    def enable_ep_with_http_info(self, request):
        """启用企业项目

        启用企业项目。

        :param EnableEpRequest request
        :return: EnableEpResponse
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
            response_type='EnableEpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_api_versions(self, request):
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
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ep(self, request):
        """查询企业项目列表

        查询当前用户已授权的企业项目列表，用户可以使用企业项目绑定资源。

        :param ListEpRequest request
        :return: ListEpResponse
        """
        return self.list_ep_with_http_info(request)

    def list_ep_with_http_info(self, request):
        """查询企业项目列表

        查询当前用户已授权的企业项目列表，用户可以使用企业项目绑定资源。

        :param ListEpRequest request
        :return: ListEpResponse
        """

        all_params = ['offset', 'id', 'name', 'status', 'limit', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def migrate_resource(self, request):
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
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def modify_ep(self, request):
        """修改企业项目

        修改企业项目。当前仅支持修改名称和描述。

        :param ModifyEpRequest request
        :return: ModifyEpResponse
        """
        return self.modify_ep_with_http_info(request)

    def modify_ep_with_http_info(self, request):
        """修改企业项目

        修改企业项目。当前仅支持修改名称和描述。

        :param ModifyEpRequest request
        :return: ModifyEpResponse
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
            response_type='ModifyEpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_api_version(self, request):
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
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ep(self, request):
        """查询企业项目详情

        查询企业项目详情。

        :param ShowEpRequest request
        :return: ShowEpResponse
        """
        return self.show_ep_with_http_info(request)

    def show_ep_with_http_info(self, request):
        """查询企业项目详情

        查询企业项目详情。

        :param ShowEpRequest request
        :return: ShowEpResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects/{enterprise_project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ep_quota(self, request):
        """查询企业项目配额

        查询企业项目的配额信息。

        :param ShowEpQuotaRequest request
        :return: ShowEpQuotaResponse
        """
        return self.show_ep_quota_with_http_info(request)

    def show_ep_quota_with_http_info(self, request):
        """查询企业项目配额

        查询企业项目的配额信息。

        :param ShowEpQuotaRequest request
        :return: ShowEpQuotaResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/enterprise-projects/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEpQuotaResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_resource_bind_ep(self, request):
        """查询企业项目绑定的资源列表

        查询企业项目下绑定的资源详情。

        :param ShowResourceBindEpRequest request
        :return: ShowResourceBindEpResponse
        """
        return self.show_resource_bind_ep_with_http_info(request)

    def show_resource_bind_ep_with_http_info(self, request):
        """查询企业项目绑定的资源列表

        查询企业项目下绑定的资源详情。

        :param ShowResourceBindEpRequest request
        :return: ShowResourceBindEpResponse
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
            response_type='ShowResourceBindEpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
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
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
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
            collection_formats=collection_formats,
            request_type=request_type)
