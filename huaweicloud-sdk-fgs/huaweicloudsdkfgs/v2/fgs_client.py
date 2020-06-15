# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


class FgsClient(Client):
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
        super(FgsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkfgs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def async_invoke_function(self, request):
        """异步执行函数。

        异步执行函数。

        :param AsyncInvokeFunctionRequest request
        :return: AsyncInvokeFunctionResponse
        """
        return self.async_invoke_function_with_http_info(request)

    def async_invoke_function_with_http_info(self, request):
        """异步执行函数。

        异步执行函数。

        :param AsyncInvokeFunctionRequest request
        :return: tuple(AsyncInvokeFunctionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'async_invoke_function_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/invocations-async', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AsyncInvokeFunctionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_function(self, request):
        """创建函数。

        创建指定的函数。

        :param CreateFunctionRequest request
        :return: CreateFunctionResponse
        """
        return self.create_function_with_http_info(request)

    def create_function_with_http_info(self, request):
        """创建函数。

        创建指定的函数。

        :param CreateFunctionRequest request
        :return: tuple(CreateFunctionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_function_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateFunctionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_function_version(self, request):
        """发布函数版本。

        发布函数版本。

        :param CreateFunctionVersionRequest request
        :return: CreateFunctionVersionResponse
        """
        return self.create_function_version_with_http_info(request)

    def create_function_version_with_http_info(self, request):
        """发布函数版本。

        发布函数版本。

        :param CreateFunctionVersionRequest request
        :return: tuple(CreateFunctionVersionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'create_function_version_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/versions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateFunctionVersionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_version_alias(self, request):
        """创建函数版本别名。

        创建函数灰度版本别名。

        :param CreateVersionAliasRequest request
        :return: CreateVersionAliasResponse
        """
        return self.create_version_alias_with_http_info(request)

    def create_version_alias_with_http_info(self, request):
        """创建函数版本别名。

        创建函数灰度版本别名。

        :param CreateVersionAliasRequest request
        :return: tuple(CreateVersionAliasResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'create_version_alias_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/aliases', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVersionAliasResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_function(self, request):
        """删除函数/版本。

        删除指定的函数或者特定的版本（不允许删除latest版本）。  如果URN中包含函数版本或者别名，则删除特定的函数版本或者别名指向的版本以及该版本关联的trigger。 如果URN中不包含版本或者别名，则删除整个函数，包含所有版本以及别名，触发器。

        :param DeleteFunctionRequest request
        :return: None
        """
        return self.delete_function_with_http_info(request)

    def delete_function_with_http_info(self, request):
        """删除函数/版本。

        删除指定的函数或者特定的版本（不允许删除latest版本）。  如果URN中包含函数版本或者别名，则删除特定的函数版本或者别名指向的版本以及该版本关联的trigger。 如果URN中不包含版本或者别名，则删除整个函数，包含所有版本以及别名，触发器。

        :param DeleteFunctionRequest request
        :return: None
        """

        all_params = ['function_urn']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_version_alias(self, request):
        """删除函数版本别名。

        删除函数版本别名。

        :param DeleteVersionAliasRequest request
        :return: None
        """
        return self.delete_version_alias_with_http_info(request)

    def delete_version_alias_with_http_info(self, request):
        """删除函数版本别名。

        删除函数版本别名。

        :param DeleteVersionAliasRequest request
        :return: None
        """

        all_params = ['function_urn', 'name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/aliases/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def invoke_function(self, request):
        """同步执行函数。

        同步调用指的是客户端请求需要明确等到响应结果，也就是说这样的请求必须得调用到用户的函数，并且等到调用完成才返回。

        :param InvokeFunctionRequest request
        :return: InvokeFunctionResponse
        """
        return self.invoke_function_with_http_info(request)

    def invoke_function_with_http_info(self, request):
        """同步执行函数。

        同步调用指的是客户端请求需要明确等到响应结果，也就是说这样的请求必须得调用到用户的函数，并且等到调用完成才返回。

        :param InvokeFunctionRequest request
        :return: tuple(InvokeFunctionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'invoke_function_request_body', 'x_cff_log_type', 'x_cff_request_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}
        if 'x_cff_log_type' in local_var_params:
            header_params['X-Cff-Log-Type'] = local_var_params['x_cff_log_type']
        if 'x_cff_request_version' in local_var_params:
            header_params['X-CFF-Request-Version'] = local_var_params['x_cff_request_version']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json', 'text/plain'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/invocations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='InvokeFunctionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_function_versions(self, request):
        """获取指定函数的版本列表。

        获取指定函数的版本列表。

        :param ListFunctionVersionsRequest request
        :return: ListFunctionVersionsResponse
        """
        return self.list_function_versions_with_http_info(request)

    def list_function_versions_with_http_info(self, request):
        """获取指定函数的版本列表。

        获取指定函数的版本列表。

        :param ListFunctionVersionsRequest request
        :return: tuple(ListFunctionVersionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'marker', 'maxitems']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'maxitems' in local_var_params:
            query_params.append(('maxitems', local_var_params['maxitems']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/versions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFunctionVersionsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_functions(self, request):
        """获取函数列表

        获取函数列表

        :param ListFunctionsRequest request
        :return: ListFunctionsResponse
        """
        return self.list_functions_with_http_info(request)

    def list_functions_with_http_info(self, request):
        """获取函数列表

        获取函数列表

        :param ListFunctionsRequest request
        :return: tuple(ListFunctionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['marker', 'maxitems']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'maxitems' in local_var_params:
            query_params.append(('maxitems', local_var_params['maxitems']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFunctionsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_version_aliases(self, request):
        """获取指定函数所有版本别名列表。

        获取函数版本别名列表。

        :param ListVersionAliasesRequest request
        :return: list[ListVersionAliasResult]
        """
        return self.list_version_aliases_with_http_info(request)

    def list_version_aliases_with_http_info(self, request):
        """获取指定函数所有版本别名列表。

        获取函数版本别名列表。

        :param ListVersionAliasesRequest request
        :return: tuple(list[ListVersionAliasResult], status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/aliases', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='list[ListVersionAliasResult]',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_function_code(self, request):
        """获取指定函数代码。

        获取指定函数的代码。

        :param ShowFunctionCodeRequest request
        :return: ShowFunctionCodeResponse
        """
        return self.show_function_code_with_http_info(request)

    def show_function_code_with_http_info(self, request):
        """获取指定函数代码。

        获取指定函数的代码。

        :param ShowFunctionCodeRequest request
        :return: tuple(ShowFunctionCodeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/code', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFunctionCodeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_function_config(self, request):
        """获取函数的metadata。

        获取指定函数的metadata。

        :param ShowFunctionConfigRequest request
        :return: ShowFunctionConfigResponse
        """
        return self.show_function_config_with_http_info(request)

    def show_function_config_with_http_info(self, request):
        """获取函数的metadata。

        获取指定函数的metadata。

        :param ShowFunctionConfigRequest request
        :return: tuple(ShowFunctionConfigResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFunctionConfigResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_version_alias(self, request):
        """获取函数版本的指定别名信息。

        获取函数指定的版本别名信息。

        :param ShowVersionAliasRequest request
        :return: ShowVersionAliasResponse
        """
        return self.show_version_alias_with_http_info(request)

    def show_version_alias_with_http_info(self, request):
        """获取函数版本的指定别名信息。

        获取函数指定的版本别名信息。

        :param ShowVersionAliasRequest request
        :return: tuple(ShowVersionAliasResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/aliases/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVersionAliasResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_function_code(self, request):
        """修改函数代码。

        修改指定的函数的代码。

        :param UpdateFunctionCodeRequest request
        :return: UpdateFunctionCodeResponse
        """
        return self.update_function_code_with_http_info(request)

    def update_function_code_with_http_info(self, request):
        """修改函数代码。

        修改指定的函数的代码。

        :param UpdateFunctionCodeRequest request
        :return: tuple(UpdateFunctionCodeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'update_function_code_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/code', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateFunctionCodeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_function_config(self, request):
        """修改函数的metadata信息。

        修改指定的函数的metadata信息。

        :param UpdateFunctionConfigRequest request
        :return: UpdateFunctionConfigResponse
        """
        return self.update_function_config_with_http_info(request)

    def update_function_config_with_http_info(self, request):
        """修改函数的metadata信息。

        修改指定的函数的metadata信息。

        :param UpdateFunctionConfigRequest request
        :return: tuple(UpdateFunctionConfigResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'update_function_config_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/config', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateFunctionConfigResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_version_alias(self, request):
        """修改函数版本别名信息。

        修改函数版本别名信息。

        :param UpdateVersionAliasRequest request
        :return: UpdateVersionAliasResponse
        """
        return self.update_version_alias_with_http_info(request)

    def update_version_alias_with_http_info(self, request):
        """修改函数版本别名信息。

        修改函数版本别名信息。

        :param UpdateVersionAliasRequest request
        :return: tuple(UpdateVersionAliasResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'name', 'update_version_alias_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/functions/{function_urn}/aliases/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVersionAliasResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_function_triggers(self, request):
        """删除指定函数的所有触发器。

        删除指定函数所有触发器设置。  在提供函数版本且非latest的情况下，删除对应函数版本的触发器。 在提供函数别名的情况下，删除对应函数别名的触发器。 在不提供函数版本（也不提供别名）或版本为latest的情况下，删除该函数所有的触发器（包括所有版本和别名）。

        :param BatchDeleteFunctionTriggersRequest request
        :return: None
        """
        return self.batch_delete_function_triggers_with_http_info(request)

    def batch_delete_function_triggers_with_http_info(self, request):
        """删除指定函数的所有触发器。

        删除指定函数所有触发器设置。  在提供函数版本且非latest的情况下，删除对应函数版本的触发器。 在提供函数别名的情况下，删除对应函数别名的触发器。 在不提供函数版本（也不提供别名）或版本为latest的情况下，删除该函数所有的触发器（包括所有版本和别名）。

        :param BatchDeleteFunctionTriggersRequest request
        :return: None
        """

        all_params = ['function_urn']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/triggers/{function_urn}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_function_trigger(self, request):
        """创建触发器。

        创建触发器。  - 可以创建的触发器类型包括TIMER、APIG、CTS、DDS、DMS、DIS、LTS、OBS、SMN、KAFKA。 - DDS和KAFKA触发器创建时默认为DISABLE状态，其他触发器默认为ACTIVE状态。 - TIMER、DDS、DMS、KAFKA、LTS触发器支持禁用，其他触发器不支持。

        :param CreateFunctionTriggerRequest request
        :return: CreateFunctionTriggerResponse
        """
        return self.create_function_trigger_with_http_info(request)

    def create_function_trigger_with_http_info(self, request):
        """创建触发器。

        创建触发器。  - 可以创建的触发器类型包括TIMER、APIG、CTS、DDS、DMS、DIS、LTS、OBS、SMN、KAFKA。 - DDS和KAFKA触发器创建时默认为DISABLE状态，其他触发器默认为ACTIVE状态。 - TIMER、DDS、DMS、KAFKA、LTS触发器支持禁用，其他触发器不支持。

        :param CreateFunctionTriggerRequest request
        :return: tuple(CreateFunctionTriggerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'create_function_trigger_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/triggers/{function_urn}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateFunctionTriggerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_function_trigger(self, request):
        """删除触发器。

        删除触发器。

        :param DeleteFunctionTriggerRequest request
        :return: None
        """
        return self.delete_function_trigger_with_http_info(request)

    def delete_function_trigger_with_http_info(self, request):
        """删除触发器。

        删除触发器。

        :param DeleteFunctionTriggerRequest request
        :return: None
        """

        all_params = ['function_urn', 'trigger_type_code', 'trigger_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'trigger_type_code' in local_var_params:
            path_params['trigger_type_code'] = local_var_params['trigger_type_code']
        if 'trigger_id' in local_var_params:
            path_params['triggerId'] = local_var_params['trigger_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/triggers/{function_urn}/{trigger_type_code}/{triggerId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_function_triggers(self, request):
        """获取指定函数的所有触发器。

        获取指定函数的所有触发器设置。

        :param ListFunctionTriggersRequest request
        :return: list[ListFunctionTriggerResult]
        """
        return self.list_function_triggers_with_http_info(request)

    def list_function_triggers_with_http_info(self, request):
        """获取指定函数的所有触发器。

        获取指定函数的所有触发器设置。

        :param ListFunctionTriggersRequest request
        :return: tuple(list[ListFunctionTriggerResult], status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/triggers/{function_urn}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='list[ListFunctionTriggerResult]',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_function_trigger(self, request):
        """获取指定触发器的信息。

        获取特定触发器的信息。

        :param ShowFunctionTriggerRequest request
        :return: ShowFunctionTriggerResponse
        """
        return self.show_function_trigger_with_http_info(request)

    def show_function_trigger_with_http_info(self, request):
        """获取指定触发器的信息。

        获取特定触发器的信息。

        :param ShowFunctionTriggerRequest request
        :return: tuple(ShowFunctionTriggerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['function_urn', 'trigger_type_code', 'trigger_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'trigger_type_code' in local_var_params:
            path_params['trigger_type_code'] = local_var_params['trigger_type_code']
        if 'trigger_id' in local_var_params:
            path_params['triggerId'] = local_var_params['trigger_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/fgs/triggers/{function_urn}/{trigger_type_code}/{triggerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFunctionTriggerResponse',
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
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats, request_type)
