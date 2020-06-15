# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


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
        self.model_package = importlib.import_module("huaweicloudsdkces.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def batch_list_metric_data_async(self, request):
        """批量查询监控数据

        批量查询指定时间范围内指定指标的指定粒度的监控数据，目前最多支持10指标的批量查询。

        :param BatchListMetricDataRequest request
        :return: BatchListMetricDataResponse
        """
        return self.batch_list_metric_data_with_http_info(request)

    def batch_list_metric_data_with_http_info(self, request):
        """批量查询监控数据

        批量查询指定时间范围内指定指标的指定粒度的监控数据，目前最多支持10指标的批量查询。

        :param BatchListMetricDataRequest request
        :return: tuple(BatchListMetricDataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['batch_list_metric_data_request_body']
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
            ['*/*'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/batch-query-metric-data', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListMetricDataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alarm_async(self, request):
        """创建告警规则

        创建一条告警规则。

        :param CreateAlarmRequest request
        :return: CreateAlarmResponse
        """
        return self.create_alarm_with_http_info(request)

    def create_alarm_with_http_info(self, request):
        """创建告警规则

        创建一条告警规则。

        :param CreateAlarmRequest request
        :return: tuple(CreateAlarmResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_alarm_request_body']
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
            ['*/*'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/alarms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAlarmResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_events_async(self, request):
        """上报事件

        上报自定义事件。

        :param CreateEventsRequest request
        :return: list[CreateEventsResponseBody]
        """
        return self.create_events_with_http_info(request)

    def create_events_with_http_info(self, request):
        """上报事件

        上报自定义事件。

        :param CreateEventsRequest request
        :return: tuple(list[CreateEventsResponseBody], status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['event_items']
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
            ['*/*'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/events', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='list[CreateEventsResponseBody]',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_metric_data_async(self, request):
        """添加监控数据

        添加一条或多条指标监控数据。

        :param CreateMetricDataRequest request
        :return: None
        """
        return self.create_metric_data_with_http_info(request)

    def create_metric_data_with_http_info(self, request):
        """添加监控数据

        添加一条或多条指标监控数据。

        :param CreateMetricDataRequest request
        :return: None
        """

        all_params = ['metric_data_item']
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


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/metric-data', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alarm_async(self, request):
        """删除告警规则

        删除一条告警规则。

        :param DeleteAlarmRequest request
        :return: None
        """
        return self.delete_alarm_with_http_info(request)

    def delete_alarm_with_http_info(self, request):
        """删除告警规则

        删除一条告警规则。

        :param DeleteAlarmRequest request
        :return: None
        """

        all_params = ['alarm_id']
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
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/alarms/{alarm_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarms_async(self, request):
        """查询告警规则列表

        查询告警规则列表，可以指定分页条件限制结果数量，可以指定排序规则。

        :param ListAlarmsRequest request
        :return: ListAlarmsResponse
        """
        return self.list_alarms_with_http_info(request)

    def list_alarms_with_http_info(self, request):
        """查询告警规则列表

        查询告警规则列表，可以指定分页条件限制结果数量，可以指定排序规则。

        :param ListAlarmsRequest request
        :return: tuple(ListAlarmsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'order', 'start']
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*'])

        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/alarms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAlarmsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_metrics_async(self, request):
        """查询指标列表

        查询系统当前可监控指标列表，可以指定指标命名空间、指标名称、维度、排序方式，起始记录和最大记录条数过滤查询结果。

        :param ListMetricsRequest request
        :return: ListMetricsResponse
        """
        return self.list_metrics_with_http_info(request)

    def list_metrics_with_http_info(self, request):
        """查询指标列表

        查询系统当前可监控指标列表，可以指定指标命名空间、指标名称、维度、排序方式，起始记录和最大记录条数过滤查询结果。

        :param ListMetricsRequest request
        :return: tuple(ListMetricsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['dim_0', 'dim_1', 'dim_2', 'limit', 'metric_name', 'namespace', 'order', 'start']
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
        if 'dim_0' in local_var_params:
            query_params.append(('dim.0', local_var_params['dim_0']))
        if 'dim_1' in local_var_params:
            query_params.append(('dim.1', local_var_params['dim_1']))
        if 'dim_2' in local_var_params:
            query_params.append(('dim.2', local_var_params['dim_2']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*'])

        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMetricsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alarm_async(self, request):
        """查询单条告警规则信息

        根据告警ID查询告警规则信息。

        :param ShowAlarmRequest request
        :return: ShowAlarmResponse
        """
        return self.show_alarm_with_http_info(request)

    def show_alarm_with_http_info(self, request):
        """查询单条告警规则信息

        根据告警ID查询告警规则信息。

        :param ShowAlarmRequest request
        :return: tuple(ShowAlarmResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['alarm_id']
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
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*'])

        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/alarms/{alarm_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAlarmResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_event_data_async(self, request):
        """查询主机配置数据

        查询指定时间范围指定事件类型的主机配置数据，可以通过参数指定需要查询的数据维度。注意：该接口提供给HANA场景下SAP Monitor查询主机配置数据，其他场景下查不到主机配置数据。

        :param ShowEventDataRequest request
        :return: ShowEventDataResponse
        """
        return self.show_event_data_with_http_info(request)

    def show_event_data_with_http_info(self, request):
        """查询主机配置数据

        查询指定时间范围指定事件类型的主机配置数据，可以通过参数指定需要查询的数据维度。注意：该接口提供给HANA场景下SAP Monitor查询主机配置数据，其他场景下查不到主机配置数据。

        :param ShowEventDataRequest request
        :return: tuple(ShowEventDataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['dim_0', '_from', 'namespace', 'to', 'type', 'dim_1', 'dim_2']
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
        if 'dim_0' in local_var_params:
            query_params.append(('dim.0', local_var_params['dim_0']))
        if 'dim_1' in local_var_params:
            query_params.append(('dim.1', local_var_params['dim_1']))
        if 'dim_2' in local_var_params:
            query_params.append(('dim.2', local_var_params['dim_2']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*'])

        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/event-data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEventDataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_metric_data_async(self, request):
        """查询监控数据

        查询指定时间范围指定指标的指定粒度的监控数据，可以通过参数指定需要查询的数据维度。

        :param ShowMetricDataRequest request
        :return: ShowMetricDataResponse
        """
        return self.show_metric_data_with_http_info(request)

    def show_metric_data_with_http_info(self, request):
        """查询监控数据

        查询指定时间范围指定指标的指定粒度的监控数据，可以通过参数指定需要查询的数据维度。

        :param ShowMetricDataRequest request
        :return: tuple(ShowMetricDataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['dim_0', 'filter', '_from', 'metric_name', 'namespace', 'period', 'to', 'dim_1', 'dim_2']
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
        if 'dim_0' in local_var_params:
            query_params.append(('dim.0', local_var_params['dim_0']))
        if 'dim_1' in local_var_params:
            query_params.append(('dim.1', local_var_params['dim_1']))
        if 'dim_2' in local_var_params:
            query_params.append(('dim.2', local_var_params['dim_2']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*'])

        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/metric-data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMetricDataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas_async(self, request):
        """查询配额

        查询用户可以创建的资源配额总数及当前使用量，当前仅有告警规则一种资源类型。

        :param ShowQuotasRequest request
        :return: ShowQuotasResponse
        """
        return self.show_quotas_with_http_info(request)

    def show_quotas_with_http_info(self, request):
        """查询配额

        查询用户可以创建的资源配额总数及当前使用量，当前仅有告警规则一种资源类型。

        :param ShowQuotasRequest request
        :return: tuple(ShowQuotasResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
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

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*'])

        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/quotas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotasResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_action_async(self, request):
        """启停告警规则

        启动或停止一条告警规则。

        :param UpdateAlarmActionRequest request
        :return: None
        """
        return self.update_alarm_action_with_http_info(request)

    def update_alarm_action_with_http_info(self, request):
        """启停告警规则

        启动或停止一条告警规则。

        :param UpdateAlarmActionRequest request
        :return: None
        """

        all_params = ['alarm_id', 'modify_alarm_action_req']
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
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/V1.0/{project_id}/alarms/{alarm_id}/action', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
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
                                    response_type, collection_formats, request_type, True)
