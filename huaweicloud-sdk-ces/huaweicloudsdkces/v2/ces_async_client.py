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


class CesAsyncClient(Client):
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
        super(CesAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkces.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CesClient":
            raise TypeError("client type error, support client type is CesClient")

        return ClientBuilder(clazz)

    def add_alarm_resources_async(self, request):
        """增加告警资源(资源分组类型的告警规则不支持)

        增加告警资源(资源分组类型的告警规则不支持)

        :param AddAlarmResourcesRequest request
        :return: AddAlarmResourcesResponse
        """
        return self.add_alarm_resources_with_http_info(request)

    def add_alarm_resources_with_http_info(self, request):
        """增加告警资源(资源分组类型的告警规则不支持)

        增加告警资源(资源分组类型的告警规则不支持)

        :param AddAlarmResourcesRequest request
        :return: AddAlarmResourcesResponse
        """

        all_params = ['alarm_id', 'add_alarm_resources_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/resources/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddAlarmResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_resource_groups_resources_batch_async(self, request):
        """自定义资源分组批量增加关联资源

        给自定义资源分组,即非自动企业项目和标签关联,批量增加关联资源

        :param AddResourceGroupsResourcesBatchRequest request
        :return: AddResourceGroupsResourcesBatchResponse
        """
        return self.add_resource_groups_resources_batch_with_http_info(request)

    def add_resource_groups_resources_batch_with_http_info(self, request):
        """自定义资源分组批量增加关联资源

        给自定义资源分组,即非自动企业项目和标签关联,批量增加关联资源

        :param AddResourceGroupsResourcesBatchRequest request
        :return: AddResourceGroupsResourcesBatchResponse
        """

        all_params = ['group_id', 'resource_group_resources_add_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/resource-groups/{group_id}/resources/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddResourceGroupsResourcesBatchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_alarm_async(self, request):
        """创建告警

        创建告警，接口对应后端API路径open-alarms

        :param CreateAlarmRequest request
        :return: CreateAlarmResponse
        """
        return self.create_alarm_with_http_info(request)

    def create_alarm_with_http_info(self, request):
        """创建告警

        创建告警，接口对应后端API路径open-alarms

        :param CreateAlarmRequest request
        :return: CreateAlarmResponse
        """

        all_params = ['create_alarm_v2_request_body']
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
            resource_path='/v2/{project_id}/alarms',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAlarmResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_alarm_async(self, request):
        """删除告警规则

        删除告警规则V2接口，APIG上注册为V2，后端实际上使用的是V1

        :param DeleteAlarmRequest request
        :return: DeleteAlarmResponse
        """
        return self.delete_alarm_with_http_info(request)

    def delete_alarm_with_http_info(self, request):
        """删除告警规则

        删除告警规则V2接口，APIG上注册为V2，后端实际上使用的是V1

        :param DeleteAlarmRequest request
        :return: DeleteAlarmResponse
        """

        all_params = ['alarm_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAlarmResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_alarm_resources_async(self, request):
        """删除告警资源（资源分组类型的告警规则不支持）

        删除告警资源（资源分组类型的告警规则不支持）

        :param DeleteAlarmResourcesRequest request
        :return: DeleteAlarmResourcesResponse
        """
        return self.delete_alarm_resources_with_http_info(request)

    def delete_alarm_resources_with_http_info(self, request):
        """删除告警资源（资源分组类型的告警规则不支持）

        删除告警资源（资源分组类型的告警规则不支持）

        :param DeleteAlarmResourcesRequest request
        :return: DeleteAlarmResourcesResponse
        """

        all_params = ['alarm_id', 'delete_alarm_resources_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/resources/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAlarmResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_resource_groups_resources_batch_async(self, request):
        """自定义资源分组批量删除关联资源

        给自定义资源分组,即非自动企业项目和标签关联,批量删除关联资源

        :param DeleteResourceGroupsResourcesBatchRequest request
        :return: DeleteResourceGroupsResourcesBatchResponse
        """
        return self.delete_resource_groups_resources_batch_with_http_info(request)

    def delete_resource_groups_resources_batch_with_http_info(self, request):
        """自定义资源分组批量删除关联资源

        给自定义资源分组,即非自动企业项目和标签关联,批量删除关联资源

        :param DeleteResourceGroupsResourcesBatchRequest request
        :return: DeleteResourceGroupsResourcesBatchResponse
        """

        all_params = ['group_id', 'resource_group_resources_delete_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/resource-groups/{group_id}/resources/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResourceGroupsResourcesBatchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_alarm_histories_async(self, request):
        """查询告警历史

        查询告警历史列表

        :param ListAlarmHistoriesRequest request
        :return: ListAlarmHistoriesResponse
        """
        return self.list_alarm_histories_with_http_info(request)

    def list_alarm_histories_with_http_info(self, request):
        """查询告警历史

        查询告警历史列表

        :param ListAlarmHistoriesRequest request
        :return: ListAlarmHistoriesResponse
        """

        all_params = ['alarm_id', 'name', 'status', 'level', 'namespace', 'resource_id', '_from', 'to', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alarm_id' in local_var_params:
            query_params.append(('alarm_id', local_var_params['alarm_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/alarm-histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAlarmHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_alarm_resources_async(self, request):
        """根据告警ID查询告警资源列表

        根据告警ID查询告警资源列表

        :param ListAlarmResourcesRequest request
        :return: ListAlarmResourcesResponse
        """
        return self.list_alarm_resources_with_http_info(request)

    def list_alarm_resources_with_http_info(self, request):
        """根据告警ID查询告警资源列表

        根据告警ID查询告警资源列表

        :param ListAlarmResourcesRequest request
        :return: ListAlarmResourcesResponse
        """

        all_params = ['alarm_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAlarmResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_alarms_async(self, request):
        """查询告警列表

        查询告警列表,实际上内部对应的是v3的版本号

        :param ListAlarmsRequest request
        :return: ListAlarmsResponse
        """
        return self.list_alarms_with_http_info(request)

    def list_alarms_with_http_info(self, request):
        """查询告警列表

        查询告警列表,实际上内部对应的是v3的版本号

        :param ListAlarmsRequest request
        :return: ListAlarmsResponse
        """

        all_params = ['alarm_id', 'name', 'namespace', 'resource_id', 'enterprise_project_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alarm_id' in local_var_params:
            query_params.append(('alarm_id', local_var_params['alarm_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/alarms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAlarmsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_alarm_action_async(self, request):
        """修改告警规则基本信息

        修改告警规则基本信息

        :param UpdateAlarmActionRequest request
        :return: UpdateAlarmActionResponse
        """
        return self.update_alarm_action_with_http_info(request)

    def update_alarm_action_with_http_info(self, request):
        """修改告警规则基本信息

        修改告警规则基本信息

        :param UpdateAlarmActionRequest request
        :return: UpdateAlarmActionResponse
        """

        all_params = ['alarm_id', 'update_alarm_action_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/base-info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAlarmActionResponse',
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
