# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkces'")


class CesClient(Client):
    def __init__(self):
        super(CesClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkces.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CesClient":
                raise TypeError("client type error, support client type is CesClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_list_metric_data(self, request):
        r"""批量查询监控数据

        批量查询指定时间范围内指定指标的指定粒度的监控数据，目前最多支持500指标的批量查询。 对于不同的period取值和查询的指标数量，默认的最大查询区间(to-from)不同。 规则为\&quot;指标数量*(to-from)/监控周期&lt;&#x3D;3000\&quot;，若超出阈值，会自动调整from以满足规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchListMetricData
        :type request: :class:`huaweicloudsdkces.v1.BatchListMetricDataRequest`
        :rtype: :class:`huaweicloudsdkces.v1.BatchListMetricDataResponse`
        """
        http_info = self._batch_list_metric_data_http_info(request)
        return self._call_api(**http_info)

    def batch_list_metric_data_invoker(self, request):
        http_info = self._batch_list_metric_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_list_metric_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/V1.0/{project_id}/batch-query-metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_alarm(self, request):
        r"""创建告警规则

        创建一条告警规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlarm
        :type request: :class:`huaweicloudsdkces.v1.CreateAlarmRequest`
        :rtype: :class:`huaweicloudsdkces.v1.CreateAlarmResponse`
        """
        http_info = self._create_alarm_http_info(request)
        return self._call_api(**http_info)

    def create_alarm_invoker(self, request):
        http_info = self._create_alarm_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_alarm_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/V1.0/{project_id}/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlarmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_alarm_template(self, request):
        r"""创建自定义告警模板

        创建自定义告警模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v1.CreateAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v1.CreateAlarmTemplateResponse`
        """
        http_info = self._create_alarm_template_http_info(request)
        return self._call_api(**http_info)

    def create_alarm_template_invoker(self, request):
        http_info = self._create_alarm_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_alarm_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/V1.0/{project_id}/alarm-template",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlarmTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_events(self, request):
        r"""上报事件

        上报自定义事件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEvents
        :type request: :class:`huaweicloudsdkces.v1.CreateEventsRequest`
        :rtype: :class:`huaweicloudsdkces.v1.CreateEventsResponse`
        """
        http_info = self._create_events_http_info(request)
        return self._call_api(**http_info)

    def create_events_invoker(self, request):
        http_info = self._create_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_events_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/V1.0/{project_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_metric_data(self, request):
        r"""添加监控数据

        添加一条或多条指标监控数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMetricData
        :type request: :class:`huaweicloudsdkces.v1.CreateMetricDataRequest`
        :rtype: :class:`huaweicloudsdkces.v1.CreateMetricDataResponse`
        """
        http_info = self._create_metric_data_http_info(request)
        return self._call_api(**http_info)

    def create_metric_data_invoker(self, request):
        http_info = self._create_metric_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_metric_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/V1.0/{project_id}/metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_resource_group(self, request):
        r"""创建资源分组

        创建资源分组，资源分组支持将各类资源按照业务集中进行分组管理，可以从分组角度查看监控与告警信息，以提升运维效率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResourceGroup
        :type request: :class:`huaweicloudsdkces.v1.CreateResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v1.CreateResourceGroupResponse`
        """
        http_info = self._create_resource_group_http_info(request)
        return self._call_api(**http_info)

    def create_resource_group_invoker(self, request):
        http_info = self._create_resource_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_resource_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/V1.0/{project_id}/resource-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_alarm(self, request):
        r"""删除告警规则

        删除一条告警规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlarm
        :type request: :class:`huaweicloudsdkces.v1.DeleteAlarmRequest`
        :rtype: :class:`huaweicloudsdkces.v1.DeleteAlarmResponse`
        """
        http_info = self._delete_alarm_http_info(request)
        return self._call_api(**http_info)

    def delete_alarm_invoker(self, request):
        http_info = self._delete_alarm_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_alarm_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/V1.0/{project_id}/alarms/{alarm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlarmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_alarm_template(self, request):
        r"""删除自定义告警模板

        根据ID删除自定义告警模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v1.DeleteAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v1.DeleteAlarmTemplateResponse`
        """
        http_info = self._delete_alarm_template_http_info(request)
        return self._call_api(**http_info)

    def delete_alarm_template_invoker(self, request):
        http_info = self._delete_alarm_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_alarm_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/V1.0/{project_id}/alarm-template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlarmTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_resource_group(self, request):
        r"""删除资源分组

        删除一条资源分组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResourceGroup
        :type request: :class:`huaweicloudsdkces.v1.DeleteResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v1.DeleteResourceGroupResponse`
        """
        http_info = self._delete_resource_group_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_group_invoker(self, request):
        http_info = self._delete_resource_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_resource_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/V1.0/{project_id}/resource-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_alarm_histories(self, request):
        r"""查询告警历史

        查询告警历史列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmHistories
        :type request: :class:`huaweicloudsdkces.v1.ListAlarmHistoriesRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ListAlarmHistoriesResponse`
        """
        http_info = self._list_alarm_histories_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_histories_invoker(self, request):
        http_info = self._list_alarm_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/alarm-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'alarm_id' in local_var_params:
            query_params.append(('alarm_id', local_var_params['alarm_id']))
        if 'alarm_name' in local_var_params:
            query_params.append(('alarm_name', local_var_params['alarm_name']))
        if 'alarm_status' in local_var_params:
            query_params.append(('alarm_status', local_var_params['alarm_status']))
        if 'alarm_level' in local_var_params:
            query_params.append(('alarm_level', local_var_params['alarm_level']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_alarm_templates(self, request):
        r"""查询自定义告警模板列表

        查询自定义告警模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmTemplates
        :type request: :class:`huaweicloudsdkces.v1.ListAlarmTemplatesRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ListAlarmTemplatesResponse`
        """
        http_info = self._list_alarm_templates_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_templates_invoker(self, request):
        http_info = self._list_alarm_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/alarm-template",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alarm_template_id' in local_var_params:
            query_params.append(('alarmTemplateId', local_var_params['alarm_template_id']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'dname' in local_var_params:
            query_params.append(('dname', local_var_params['dname']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_alarms(self, request):
        r"""查询告警规则列表

        查询告警规则列表，可以指定分页条件限制结果数量，可以指定排序规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarms
        :type request: :class:`huaweicloudsdkces.v1.ListAlarmsRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ListAlarmsResponse`
        """
        http_info = self._list_alarms_http_info(request)
        return self._call_api(**http_info)

    def list_alarms_invoker(self, request):
        http_info = self._list_alarms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarms_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_event_detail(self, request):
        r"""查询某一事件监控详情

        根据事件监控名称，查询该事件发生的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEventDetail
        :type request: :class:`huaweicloudsdkces.v1.ListEventDetailRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ListEventDetailResponse`
        """
        http_info = self._list_event_detail_http_info(request)
        return self._call_api(**http_info)

    def list_event_detail_invoker(self, request):
        http_info = self._list_event_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_event_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/event/{event_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_name' in local_var_params:
            path_params['event_name'] = local_var_params['event_name']

        query_params = []
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'sub_event_type' in local_var_params:
            query_params.append(('sub_event_type', local_var_params['sub_event_type']))
        if 'event_source' in local_var_params:
            query_params.append(('event_source', local_var_params['event_source']))
        if 'event_level' in local_var_params:
            query_params.append(('event_level', local_var_params['event_level']))
        if 'event_user' in local_var_params:
            query_params.append(('event_user', local_var_params['event_user']))
        if 'event_state' in local_var_params:
            query_params.append(('event_state', local_var_params['event_state']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_events(self, request):
        r"""查询事件监控列表

        查询事件监控列表，包括系统事件和自定义事件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkces.v1.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ListEventsResponse`
        """
        http_info = self._list_events_http_info(request)
        return self._call_api(**http_info)

    def list_events_invoker(self, request):
        http_info = self._list_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_events_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'sub_event_type' in local_var_params:
            query_params.append(('sub_event_type', local_var_params['sub_event_type']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_metrics(self, request):
        r"""查询指标列表

        查询系统当前可监控指标列表，可以指定指标命名空间、指标名称、维度、排序方式，起始记录和最大记录条数过滤查询结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetrics
        :type request: :class:`huaweicloudsdkces.v1.ListMetricsRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ListMetricsResponse`
        """
        http_info = self._list_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_metrics_invoker(self, request):
        http_info = self._list_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_group(self, request):
        r"""查询所有资源分组

        查询所创建的所有资源分组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceGroup
        :type request: :class:`huaweicloudsdkces.v1.ListResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ListResourceGroupResponse`
        """
        http_info = self._list_resource_group_http_info(request)
        return self._call_api(**http_info)

    def list_resource_group_invoker(self, request):
        http_info = self._list_resource_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/resource-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_alarm(self, request):
        r"""查询单条告警规则信息

        根据告警ID查询告警规则信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlarm
        :type request: :class:`huaweicloudsdkces.v1.ShowAlarmRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ShowAlarmResponse`
        """
        http_info = self._show_alarm_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_invoker(self, request):
        http_info = self._show_alarm_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alarm_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/alarms/{alarm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_event_data(self, request):
        r"""查询主机配置数据

        查询指定时间范围指定事件类型的主机配置数据，可以通过参数指定需要查询的数据维度。注意：该接口提供给HANA场景下SAP Monitor查询主机配置数据，其他场景下查不到主机配置数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEventData
        :type request: :class:`huaweicloudsdkces.v1.ShowEventDataRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ShowEventDataResponse`
        """
        http_info = self._show_event_data_http_info(request)
        return self._call_api(**http_info)

    def show_event_data_invoker(self, request):
        http_info = self._show_event_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_event_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/event-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEventDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'dim_0' in local_var_params:
            query_params.append(('dim.0', local_var_params['dim_0']))
        if 'dim_1' in local_var_params:
            query_params.append(('dim.1', local_var_params['dim_1']))
        if 'dim_2' in local_var_params:
            query_params.append(('dim.2', local_var_params['dim_2']))
        if 'dim_3' in local_var_params:
            query_params.append(('dim.3', local_var_params['dim_3']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_metric_data(self, request):
        r"""查询监控数据

        查询指定时间范围指定指标的指定粒度的监控数据，可以通过参数指定需要查询的数据维度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricData
        :type request: :class:`huaweicloudsdkces.v1.ShowMetricDataRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ShowMetricDataResponse`
        """
        http_info = self._show_metric_data_http_info(request)
        return self._call_api(**http_info)

    def show_metric_data_invoker(self, request):
        http_info = self._show_metric_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_metric_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'dim_0' in local_var_params:
            query_params.append(('dim.0', local_var_params['dim_0']))
        if 'dim_1' in local_var_params:
            query_params.append(('dim.1', local_var_params['dim_1']))
        if 'dim_2' in local_var_params:
            query_params.append(('dim.2', local_var_params['dim_2']))
        if 'dim_3' in local_var_params:
            query_params.append(('dim.3', local_var_params['dim_3']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_quotas(self, request):
        r"""查询配额

        查询用户可以创建的资源配额总数及当前使用量，当前仅有告警规则一种资源类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkces.v1.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_resource_group(self, request):
        r"""查询资源分组下的资源

        根据资源分组ID查询资源分组下的资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceGroup
        :type request: :class:`huaweicloudsdkces.v1.ShowResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v1.ShowResourceGroupResponse`
        """
        http_info = self._show_resource_group_http_info(request)
        return self._call_api(**http_info)

    def show_resource_group_invoker(self, request):
        http_info = self._show_resource_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/V1.0/{project_id}/resource-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'dname' in local_var_params:
            query_params.append(('dname', local_var_params['dname']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_alarm(self, request):
        r"""修改告警规则

        修改告警规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarm
        :type request: :class:`huaweicloudsdkces.v1.UpdateAlarmRequest`
        :rtype: :class:`huaweicloudsdkces.v1.UpdateAlarmResponse`
        """
        http_info = self._update_alarm_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_invoker(self, request):
        http_info = self._update_alarm_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/V1.0/{project_id}/alarms/{alarm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_alarm_action(self, request):
        r"""启停告警规则

        启动或停止一条告警规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmAction
        :type request: :class:`huaweicloudsdkces.v1.UpdateAlarmActionRequest`
        :rtype: :class:`huaweicloudsdkces.v1.UpdateAlarmActionResponse`
        """
        http_info = self._update_alarm_action_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_action_invoker(self, request):
        http_info = self._update_alarm_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_action_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/V1.0/{project_id}/alarms/{alarm_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_alarm_template(self, request):
        r"""更新自定义告警模板

        更新自定义告警模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v1.UpdateAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v1.UpdateAlarmTemplateResponse`
        """
        http_info = self._update_alarm_template_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_template_invoker(self, request):
        http_info = self._update_alarm_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/V1.0/{project_id}/alarm-template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_resource_group(self, request):
        r"""更新资源分组

        更新资源分组，资源分组支持将各类资源按照业务集中进行分组管理，可以从分组角度查看监控与告警信息，以提升运维效率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResourceGroup
        :type request: :class:`huaweicloudsdkces.v1.UpdateResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v1.UpdateResourceGroupResponse`
        """
        http_info = self._update_resource_group_http_info(request)
        return self._call_api(**http_info)

    def update_resource_group_invoker(self, request):
        http_info = self._update_resource_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_resource_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/V1.0/{project_id}/resource-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
