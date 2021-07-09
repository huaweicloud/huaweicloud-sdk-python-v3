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


class LtsClient(Client):
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
        super(LtsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklts.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "LtsClient":
            raise TypeError("client type error, support client type is LtsClient")

        return ClientBuilder(clazz)

    def create_log_dump_obs(self, request):
        """日志转储

        该接口用于将指定的一个或多个日志流的日志转储到OBS服务。

        :param CreateLogDumpObsRequest request
        :return: CreateLogDumpObsResponse
        """
        return self.create_log_dump_obs_with_http_info(request)

    def create_log_dump_obs_with_http_info(self, request):
        """日志转储

        该接口用于将指定的一个或多个日志流的日志转储到OBS服务。

        :param CreateLogDumpObsRequest request
        :return: CreateLogDumpObsResponse
        """

        all_params = ['create_log_dump_obs_request_body']
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
            resource_path='/v2/{project_id}/log-dump/obs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLogDumpObsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_log_group(self, request):
        """创建日志组

        该接口用于创建一个日志组

        :param CreateLogGroupRequest request
        :return: CreateLogGroupResponse
        """
        return self.create_log_group_with_http_info(request)

    def create_log_group_with_http_info(self, request):
        """创建日志组

        该接口用于创建一个日志组

        :param CreateLogGroupRequest request
        :return: CreateLogGroupResponse
        """

        all_params = ['create_log_group_request_body']
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
            resource_path='/v2/{project_id}/groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLogGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_log_stream(self, request):
        """创建日志流

        该接口用于创建某个指定日志组下的日志流

        :param CreateLogStreamRequest request
        :return: CreateLogStreamResponse
        """
        return self.create_log_stream_with_http_info(request)

    def create_log_stream_with_http_info(self, request):
        """创建日志流

        该接口用于创建某个指定日志组下的日志流

        :param CreateLogStreamRequest request
        :return: CreateLogStreamResponse
        """

        all_params = ['log_group_id', 'create_log_stream_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLogStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_log_group(self, request):
        """删除日志组

        该接口用于删除指定日志组。当日志组中的日志流配置了日志转储，需要取消日志转储后才可删除。

        :param DeleteLogGroupRequest request
        :return: DeleteLogGroupResponse
        """
        return self.delete_log_group_with_http_info(request)

    def delete_log_group_with_http_info(self, request):
        """删除日志组

        该接口用于删除指定日志组。当日志组中的日志流配置了日志转储，需要取消日志转储后才可删除。

        :param DeleteLogGroupRequest request
        :return: DeleteLogGroupResponse
        """

        all_params = ['log_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteLogGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_log_stream(self, request):
        """删除日志流

        该接口用于删除指定日志组下的指定日志流。当该日志流配置了日志转储，需要取消日志转储后才可删除。

        :param DeleteLogStreamRequest request
        :return: DeleteLogStreamResponse
        """
        return self.delete_log_stream_with_http_info(request)

    def delete_log_stream_with_http_info(self, request):
        """删除日志流

        该接口用于删除指定日志组下的指定日志流。当该日志流配置了日志转储，需要取消日志转储后才可删除。

        :param DeleteLogStreamRequest request
        :return: DeleteLogStreamResponse
        """

        all_params = ['log_group_id', 'log_stream_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteLogStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disable_log_collection(self, request):
        """关闭超额采集开关

        该接口用于将超额采集日志功能关闭。

        :param DisableLogCollectionRequest request
        :return: DisableLogCollectionResponse
        """
        return self.disable_log_collection_with_http_info(request)

    def disable_log_collection_with_http_info(self, request):
        """关闭超额采集开关

        该接口用于将超额采集日志功能关闭。

        :param DisableLogCollectionRequest request
        :return: DisableLogCollectionResponse
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
            resource_path='/v2/{project_id}/collection/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisableLogCollectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_log_collection(self, request):
        """打开超额采集开关

        该接口用于将超额采集日志功能打开。

        :param EnableLogCollectionRequest request
        :return: EnableLogCollectionResponse
        """
        return self.enable_log_collection_with_http_info(request)

    def enable_log_collection_with_http_info(self, request):
        """打开超额采集开关

        该接口用于将超额采集日志功能打开。

        :param EnableLogCollectionRequest request
        :return: EnableLogCollectionResponse
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
            resource_path='/v2/{project_id}/collection/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EnableLogCollectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_log_groups(self, request):
        """查询账号下所有日志组

        该接口用于查询账号下所有日志组。

        :param ListLogGroupsRequest request
        :return: ListLogGroupsResponse
        """
        return self.list_log_groups_with_http_info(request)

    def list_log_groups_with_http_info(self, request):
        """查询账号下所有日志组

        该接口用于查询账号下所有日志组。

        :param ListLogGroupsRequest request
        :return: ListLogGroupsResponse
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
            resource_path='/v2/{project_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLogGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_log_stream(self, request):
        """查询指定日志组下的所有日志流

        该接口用于查询指定日志组下的所有日志流信息。

        :param ListLogStreamRequest request
        :return: ListLogStreamResponse
        """
        return self.list_log_stream_with_http_info(request)

    def list_log_stream_with_http_info(self, request):
        """查询指定日志组下的所有日志流

        该接口用于查询指定日志组下的所有日志流信息。

        :param ListLogStreamRequest request
        :return: ListLogStreamResponse
        """

        all_params = ['log_group_id', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLogStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_logs(self, request):
        """查询日志

        该接口用于查询指定日志流下的日志内容。

        :param ListLogsRequest request
        :return: ListLogsResponse
        """
        return self.list_logs_with_http_info(request)

    def list_logs_with_http_info(self, request):
        """查询日志

        该接口用于查询指定日志流下的日志内容。

        :param ListLogsRequest request
        :return: ListLogsResponse
        """

        all_params = ['log_group_id', 'log_stream_id', 'list_logs_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/content/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_query_structured_logs(self, request):
        """查询结构化日志

        该接口用于查询指定日志流下的结构化日志内容。

        :param ListQueryStructuredLogsRequest request
        :return: ListQueryStructuredLogsResponse
        """
        return self.list_query_structured_logs_with_http_info(request)

    def list_query_structured_logs_with_http_info(self, request):
        """查询结构化日志

        该接口用于查询指定日志流下的结构化日志内容。

        :param ListQueryStructuredLogsRequest request
        :return: ListQueryStructuredLogsResponse
        """

        all_params = ['log_group_id', 'log_stream_id', 'list_query_structured_logs_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/struct-content/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQueryStructuredLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_structured_logs_with_time_range(self, request):
        """查询结构化日志（新版）

        该接口用于查询指定日志流下的结构化日志内容（新版）。

        :param ListStructuredLogsWithTimeRangeRequest request
        :return: ListStructuredLogsWithTimeRangeResponse
        """
        return self.list_structured_logs_with_time_range_with_http_info(request)

    def list_structured_logs_with_time_range_with_http_info(self, request):
        """查询结构化日志（新版）

        该接口用于查询指定日志流下的结构化日志内容（新版）。

        :param ListStructuredLogsWithTimeRangeRequest request
        :return: ListStructuredLogsWithTimeRangeResponse
        """

        all_params = ['log_stream_id', 'list_structured_logs_with_time_range_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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
            resource_path='/v2/{project_id}/streams/{log_stream_id}/struct-content/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStructuredLogsWithTimeRangeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_log_group(self, request):
        """修改日志组

        该接口用于修改指定日志组下的日志存储时长。

        :param UpdateLogGroupRequest request
        :return: UpdateLogGroupResponse
        """
        return self.update_log_group_with_http_info(request)

    def update_log_group_with_http_info(self, request):
        """修改日志组

        该接口用于修改指定日志组下的日志存储时长。

        :param UpdateLogGroupRequest request
        :return: UpdateLogGroupResponse
        """

        all_params = ['log_group_id', 'update_log_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateLogGroupResponse',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
