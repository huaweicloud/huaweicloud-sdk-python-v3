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


class CesClient(Client):
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
        super(CesClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkces.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def batch_list_metric_data(self, request):
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
        :return: BatchListMetricDataResponse
        """

        all_params = ['batch_list_metric_data_request_body']
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
            resource_path='/V1.0/{project_id}/batch-query-metric-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListMetricDataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_alarm(self, request):
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
        :return: CreateAlarmResponse
        """

        all_params = ['create_alarm_request_body']
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
            resource_path='/V1.0/{project_id}/alarms',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAlarmResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_events(self, request):
        """上报事件

        上报自定义事件。

        :param CreateEventsRequest request
        :return: CreateEventsResponse
        """
        return self.create_events_with_http_info(request)

    def create_events_with_http_info(self, request):
        """上报事件

        上报自定义事件。

        :param CreateEventsRequest request
        :return: CreateEventsResponse
        """

        all_params = ['event_items']
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
            resource_path='/V1.0/{project_id}/events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEventsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_metric_data(self, request):
        """添加监控数据

        添加一条或多条指标监控数据。

        :param CreateMetricDataRequest request
        :return: CreateMetricDataResponse
        """
        return self.create_metric_data_with_http_info(request)

    def create_metric_data_with_http_info(self, request):
        """添加监控数据

        添加一条或多条指标监控数据。

        :param CreateMetricDataRequest request
        :return: CreateMetricDataResponse
        """

        all_params = ['metric_data_item']
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
            resource_path='/V1.0/{project_id}/metric-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMetricDataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_alarm(self, request):
        """删除告警规则

        删除一条告警规则。

        :param DeleteAlarmRequest request
        :return: DeleteAlarmResponse
        """
        return self.delete_alarm_with_http_info(request)

    def delete_alarm_with_http_info(self, request):
        """删除告警规则

        删除一条告警规则。

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


        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/alarms/{alarm_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAlarmResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_alarms(self, request):
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
        :return: ListAlarmsResponse
        """

        all_params = ['limit', 'order', 'start']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/alarms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAlarmsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_metrics(self, request):
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
        :return: ListMetricsResponse
        """

        all_params = ['dim_0', 'dim_1', 'dim_2', 'limit', 'metric_name', 'namespace', 'order', 'start']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/metrics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMetricsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_alarm(self, request):
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
        :return: ShowAlarmResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/alarms/{alarm_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAlarmResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_event_data(self, request):
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
        :return: ShowEventDataResponse
        """

        all_params = ['dim_0', '_from', 'namespace', 'to', 'type', 'dim_1', 'dim_2']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/event-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEventDataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_metric_data(self, request):
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
        :return: ShowMetricDataResponse
        """

        all_params = ['dim_0', 'filter', '_from', 'metric_name', 'namespace', 'period', 'to', 'dim_1', 'dim_2']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/metric-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMetricDataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_quotas(self, request):
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
        :return: ShowQuotasResponse
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
            resource_path='/V1.0/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotasResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_alarm_action(self, request):
        """启停告警规则

        启动或停止一条告警规则。

        :param UpdateAlarmActionRequest request
        :return: UpdateAlarmActionResponse
        """
        return self.update_alarm_action_with_http_info(request)

    def update_alarm_action_with_http_info(self, request):
        """启停告警规则

        启动或停止一条告警规则。

        :param UpdateAlarmActionRequest request
        :return: UpdateAlarmActionResponse
        """

        all_params = ['alarm_id', 'modify_alarm_action_req']
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/alarms/{alarm_id}/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAlarmActionResponse',
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
