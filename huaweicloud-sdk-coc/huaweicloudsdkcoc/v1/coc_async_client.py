# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcoc'")


class CocAsyncClient(Client):
    def __init__(self):
        super(CocAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcoc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials,BasicCredentials")
        else:
            if clazz.__name__ != "CocAsyncClient":
                raise TypeError("client type error, support client type is CocAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials,BasicCredentials")

        

        return client_builder

    def show_account_async(self, request):
        r"""查询客户账号

        show account ，使用场景：托管功能 sre 账号使用，查询自己管理的客户账号
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccount
        :type request: :class:`huaweicloudsdkcoc.v1.ShowAccountRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowAccountResponse`
        """
        http_info = self._show_account_http_info(request)
        return self._call_api(**http_info)

    def show_account_async_invoker(self, request):
        http_info = self._show_account_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_account_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/host/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'delegator' in local_var_params:
            query_params.append(('delegator', local_var_params['delegator']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_alarm_handle_histories_async(self, request):
        r"""查询告警工单历史

        查询告警工单历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmHandleHistories
        :type request: :class:`huaweicloudsdkcoc.v1.ListAlarmHandleHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListAlarmHandleHistoriesResponse`
        """
        http_info = self._list_alarm_handle_histories_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_handle_histories_async_invoker(self, request):
        http_info = self._list_alarm_handle_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_handle_histories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/alarm-mgmt/alarm/{alarm_id}/handle-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmHandleHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def show_alarm_async(self, request):
        r"""查询Alarm

        Get alarm info by id
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlarm
        :type request: :class:`huaweicloudsdkcoc.v1.ShowAlarmRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowAlarmResponse`
        """
        http_info = self._show_alarm_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_async_invoker(self, request):
        http_info = self._show_alarm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alarm_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/alarm-mgmt/alarm/{alarm_id}",
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

    def create_report_custom_event_async(self, request):
        r"""支持用户自主接入告警数据

        支持租户将自开发的监控系统按照标准化集成至COC，集成后告警会按照标准格式上报至COC告警中心
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReportCustomEvent
        :type request: :class:`huaweicloudsdkcoc.v1.CreateReportCustomEventRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateReportCustomEventResponse`
        """
        http_info = self._create_report_custom_event_http_info(request)
        return self._call_api(**http_info)

    def create_report_custom_event_async_invoker(self, request):
        http_info = self._create_report_custom_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_report_custom_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/event/huawei/custom/{integration_key}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReportCustomEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'integration_key' in local_var_params:
            path_params['integration_key'] = local_var_params['integration_key']

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
            ['application/json; charset=utf-8'])

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

    def create_document_async(self, request):
        r"""创建自定义作业

        创建自定义作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDocument
        :type request: :class:`huaweicloudsdkcoc.v1.CreateDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateDocumentResponse`
        """
        http_info = self._create_document_http_info(request)
        return self._call_api(**http_info)

    def create_document_async_invoker(self, request):
        http_info = self._create_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_document_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/documents",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDocumentResponse"
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

        response_headers = ["X-request-id", ]

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

    def delete_document_async(self, request):
        r"""删除自定义作业

        删除自定义作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDocument
        :type request: :class:`huaweicloudsdkcoc.v1.DeleteDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DeleteDocumentResponse`
        """
        http_info = self._delete_document_http_info(request)
        return self._call_api(**http_info)

    def delete_document_async_invoker(self, request):
        http_info = self._delete_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_document_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/documents/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def execute_document_async(self, request):
        r"""执行自定义作业

        执行自定义作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteDocument
        :type request: :class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecuteDocumentResponse`
        """
        http_info = self._execute_document_http_info(request)
        return self._call_api(**http_info)

    def execute_document_async_invoker(self, request):
        http_info = self._execute_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_document_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/documents/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def get_document_async(self, request):
        r"""查询自定义作业详情

        查询自定义作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetDocument
        :type request: :class:`huaweicloudsdkcoc.v1.GetDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetDocumentResponse`
        """
        http_info = self._get_document_http_info(request)
        return self._call_api(**http_info)

    def get_document_async_invoker(self, request):
        http_info = self._get_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_document_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/documents/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'document_type' in local_var_params:
            query_params.append(('document_type', local_var_params['document_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def get_document_atomic_info_async(self, request):
        r"""获取原子能力详细

        获取原子能力详细
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetDocumentAtomicInfo
        :type request: :class:`huaweicloudsdkcoc.v1.GetDocumentAtomicInfoRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetDocumentAtomicInfoResponse`
        """
        http_info = self._get_document_atomic_info_http_info(request)
        return self._call_api(**http_info)

    def get_document_atomic_info_async_invoker(self, request):
        http_info = self._get_document_atomic_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_document_atomic_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/atomics/{atomic_unique_key}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDocumentAtomicInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'atomic_unique_key' in local_var_params:
            path_params['atomic_unique_key'] = local_var_params['atomic_unique_key']

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

    def list_document_atomics_async(self, request):
        r"""获取原子能力列表

        获取原子能力列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDocumentAtomics
        :type request: :class:`huaweicloudsdkcoc.v1.ListDocumentAtomicsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListDocumentAtomicsResponse`
        """
        http_info = self._list_document_atomics_http_info(request)
        return self._call_api(**http_info)

    def list_document_atomics_async_invoker(self, request):
        http_info = self._list_document_atomics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_document_atomics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/atomics",
            "request_type": request.__class__.__name__,
            "response_type": "ListDocumentAtomicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_documents_async(self, request):
        r"""查询自定义作业列表

        查询自定义作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDocuments
        :type request: :class:`huaweicloudsdkcoc.v1.ListDocumentsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListDocumentsResponse`
        """
        http_info = self._list_documents_http_info(request)
        return self._call_api(**http_info)

    def list_documents_async_invoker(self, request):
        http_info = self._list_documents_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_documents_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/documents",
            "request_type": request.__class__.__name__,
            "response_type": "ListDocumentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'document_type' in local_var_params:
            query_params.append(('document_type', local_var_params['document_type']))

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

    def update_document_async(self, request):
        r"""修改自定义作业

        修改自定义作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDocument
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateDocumentResponse`
        """
        http_info = self._update_document_http_info(request)
        return self._call_api(**http_info)

    def update_document_async_invoker(self, request):
        http_info = self._update_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_document_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/documents/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_report_prometheus_event_async(self, request):
        r"""Prometheus事件接入

        Prometheus事件接入
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReportPrometheusEvent
        :type request: :class:`huaweicloudsdkcoc.v1.CreateReportPrometheusEventRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateReportPrometheusEventResponse`
        """
        http_info = self._create_report_prometheus_event_http_info(request)
        return self._call_api(**http_info)

    def create_report_prometheus_event_async_invoker(self, request):
        http_info = self._create_report_prometheus_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_report_prometheus_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/event/prometheus/{integration_key}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReportPrometheusEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'integration_key' in local_var_params:
            path_params['integration_key'] = local_var_params['integration_key']

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
            ['application/json; charset=utf-8'])

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

    def get_execution_async(self, request):
        r"""查询作业工单详情

        查询作业工单详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetExecution
        :type request: :class:`huaweicloudsdkcoc.v1.GetExecutionRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetExecutionResponse`
        """
        http_info = self._get_execution_http_info(request)
        return self._call_api(**http_info)

    def get_execution_async_invoker(self, request):
        http_info = self._get_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_execution_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/executions/{execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_execution_instances_async(self, request):
        r"""查询工单步骤批次实例

        查询工单步骤批次实例，如脚本分批操作里的ECS实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExecutionInstances
        :type request: :class:`huaweicloudsdkcoc.v1.ListExecutionInstancesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListExecutionInstancesResponse`
        """
        http_info = self._list_execution_instances_http_info(request)
        return self._call_api(**http_info)

    def list_execution_instances_async_invoker(self, request):
        http_info = self._list_execution_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_execution_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/executions/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecutionInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'execution_step_id' in local_var_params:
            query_params.append(('execution_step_id', local_var_params['execution_step_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_execution_steps_async(self, request):
        r"""查询工单步骤详情

        查询工单步骤详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExecutionSteps
        :type request: :class:`huaweicloudsdkcoc.v1.ListExecutionStepsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListExecutionStepsResponse`
        """
        http_info = self._list_execution_steps_http_info(request)
        return self._call_api(**http_info)

    def list_execution_steps_async_invoker(self, request):
        http_info = self._list_execution_steps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_execution_steps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/executions/{execution_id}/steps",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecutionStepsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'execution_step_id_list' in local_var_params:
            query_params.append(('execution_step_id_list', local_var_params['execution_step_id_list']))
            collection_formats['execution_step_id_list'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_executions_async(self, request):
        r"""查询作业工单列表

        查询作业工单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExecutions
        :type request: :class:`huaweicloudsdkcoc.v1.ListExecutionsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListExecutionsResponse`
        """
        http_info = self._list_executions_http_info(request)
        return self._call_api(**http_info)

    def list_executions_async_invoker(self, request):
        http_info = self._list_executions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_executions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecutionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'document_name' in local_var_params:
            query_params.append(('document_name', local_var_params['document_name']))
        if 'document_id' in local_var_params:
            query_params.append(('document_id', local_var_params['document_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'exclude_child_executions' in local_var_params:
            query_params.append(('exclude_child_executions', local_var_params['exclude_child_executions']))

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

    def operate_execution_async(self, request):
        r"""操作工单

        操作工单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for OperateExecution
        :type request: :class:`huaweicloudsdkcoc.v1.OperateExecutionRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.OperateExecutionResponse`
        """
        http_info = self._operate_execution_http_info(request)
        return self._call_api(**http_info)

    def operate_execution_async_invoker(self, request):
        http_info = self._operate_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _operate_execution_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/executions",
            "request_type": request.__class__.__name__,
            "response_type": "OperateExecutionResponse"
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

    def create_coc_incident_async(self, request):
        r"""CreateExternalIncident 创建事件单

        CreateExternalIncident 创建事件单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCocIncident
        :type request: :class:`huaweicloudsdkcoc.v1.CreateCocIncidentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateCocIncidentResponse`
        """
        http_info = self._create_coc_incident_http_info(request)
        return self._call_api(**http_info)

    def create_coc_incident_async_invoker(self, request):
        http_info = self._create_coc_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_coc_incident_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/incident/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCocIncidentResponse"
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
            ['application/json;charset=UTF-8'])

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

    def handle_coc_incident_async(self, request):
        r"""HandleCocIncident处理事件单

        HandleCocIncident 处理事件单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for HandleCocIncident
        :type request: :class:`huaweicloudsdkcoc.v1.HandleCocIncidentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.HandleCocIncidentResponse`
        """
        http_info = self._handle_coc_incident_http_info(request)
        return self._call_api(**http_info)

    def handle_coc_incident_async_invoker(self, request):
        http_info = self._handle_coc_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _handle_coc_incident_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/incident/handle",
            "request_type": request.__class__.__name__,
            "response_type": "HandleCocIncidentResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_coc_ticket_operation_histories_async(self, request):
        r"""GetCocTicketOperationHistories 获取事件单历史

        ListCocTicketOperationHistories  获取事件单历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCocTicketOperationHistories
        :type request: :class:`huaweicloudsdkcoc.v1.ListCocTicketOperationHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListCocTicketOperationHistoriesResponse`
        """
        http_info = self._list_coc_ticket_operation_histories_http_info(request)
        return self._call_api(**http_info)

    def list_coc_ticket_operation_histories_async_invoker(self, request):
        http_info = self._list_coc_ticket_operation_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_coc_ticket_operation_histories_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/{ticket_type}/list-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListCocTicketOperationHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']

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
            ['application/json;charset=UTF-8'])

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

    def show_coc_incident_detail_async(self, request):
        r"""GetCocIncidentDetail 获取事件单详细

        ShowCocIncidentDetail  获取事件单详细
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCocIncidentDetail
        :type request: :class:`huaweicloudsdkcoc.v1.ShowCocIncidentDetailRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowCocIncidentDetailResponse`
        """
        http_info = self._show_coc_incident_detail_http_info(request)
        return self._call_api(**http_info)

    def show_coc_incident_detail_async_invoker(self, request):
        http_info = self._show_coc_incident_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_coc_incident_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/external/incident/{incident_num}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCocIncidentDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'incident_num' in local_var_params:
            path_params['incident_num'] = local_var_params['incident_num']

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

    def create_coc_issues_async(self, request):
        r"""CreateExternalIssues 创建问题单

        CreateExternalIssues 创建问题单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCocIssues
        :type request: :class:`huaweicloudsdkcoc.v1.CreateCocIssuesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateCocIssuesResponse`
        """
        http_info = self._create_coc_issues_http_info(request)
        return self._call_api(**http_info)

    def create_coc_issues_async_invoker(self, request):
        http_info = self._create_coc_issues_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_coc_issues_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/issues/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCocIssuesResponse"
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
            ['application/json;charset=UTF-8'])

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

    def show_coc_issues_detail_async(self, request):
        r"""GetCocIssuesDetail 获取事件单详细

        ShowCocIssuesDetail  获取事件单详细
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCocIssuesDetail
        :type request: :class:`huaweicloudsdkcoc.v1.ShowCocIssuesDetailRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowCocIssuesDetailResponse`
        """
        http_info = self._show_coc_issues_detail_http_info(request)
        return self._call_api(**http_info)

    def show_coc_issues_detail_async_invoker(self, request):
        http_info = self._show_coc_issues_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_coc_issues_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/external/issues/{ticket_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCocIssuesDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_id' in local_var_params:
            path_params['ticket_id'] = local_var_params['ticket_id']

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

    def list_authorizable_tickets_external_async(self, request):
        r"""查询COC可授权单列表

        查询COC可授权单列表（变更单号、事件单号、warroom和告警）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorizableTicketsExternal
        :type request: :class:`huaweicloudsdkcoc.v1.ListAuthorizableTicketsExternalRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListAuthorizableTicketsExternalResponse`
        """
        http_info = self._list_authorizable_tickets_external_http_info(request)
        return self._call_api(**http_info)

    def list_authorizable_tickets_external_async_invoker(self, request):
        http_info = self._list_authorizable_tickets_external_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_authorizable_tickets_external_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/list/authorizable-tickets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizableTicketsExternalResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_personnel_async(self, request):
        r"""查询人员列表

        获取人员列表（公网调用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPersonnel
        :type request: :class:`huaweicloudsdkcoc.v1.ListPersonnelRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListPersonnelResponse`
        """
        http_info = self._list_personnel_http_info(request)
        return self._call_api(**http_info)

    def list_personnel_async_invoker(self, request):
        http_info = self._list_personnel_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_personnel_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/personnel",
            "request_type": request.__class__.__name__,
            "response_type": "ListPersonnelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'has_mobile' in local_var_params:
            query_params.append(('has_mobile', local_var_params['has_mobile']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def sync_add_personnel_async(self, request):
        r"""同步人员

        同步人员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncAddPersonnel
        :type request: :class:`huaweicloudsdkcoc.v1.SyncAddPersonnelRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.SyncAddPersonnelResponse`
        """
        http_info = self._sync_add_personnel_http_info(request)
        return self._call_api(**http_info)

    def sync_add_personnel_async_invoker(self, request):
        http_info = self._sync_add_personnel_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_add_personnel_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sync/{domain_id}/personnels",
            "request_type": request.__class__.__name__,
            "response_type": "SyncAddPersonnelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def list_script_resource_tags_async(self, request):
        r"""查询资源标签列表

        查询资源标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScriptResourceTags
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptResourceTagsResponse`
        """
        http_info = self._list_script_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_script_resource_tags_async_invoker(self, request):
        http_info = self._list_script_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_script_resource_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/script/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def update_resource_tags_async(self, request):
        r"""更新资源标签

        更新资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResourceTags
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateResourceTagsResponse`
        """
        http_info = self._update_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def update_resource_tags_async_invoker(self, request):
        http_info = self._update_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_resource_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/script/{resource_type}/{resource_id}/tags/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            ['application/json;charset=UTF-8'])

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

    def create_scheduled_task_async(self, request):
        r"""新建定时运维

        Create Scheduled Task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.CreateScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateScheduledTaskResponse`
        """
        http_info = self._create_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def create_scheduled_task_async_invoker(self, request):
        http_info = self._create_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scheduled_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/schedule/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScheduledTaskResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_scheduled_task_async(self, request):
        r"""删除ScheduledTask

        Delete scheduled task by id
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.DeleteScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DeleteScheduledTaskResponse`
        """
        http_info = self._delete_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def delete_scheduled_task_async_invoker(self, request):
        http_info = self._delete_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scheduled_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/schedule/task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def disable_scheduled_task_async(self, request):
        r"""禁用ScheduledTask

        Disable scheduled task by id
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.DisableScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DisableScheduledTaskResponse`
        """
        http_info = self._disable_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def disable_scheduled_task_async_invoker(self, request):
        http_info = self._disable_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_scheduled_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/schedule/task/{task_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def enable_scheduled_task_async(self, request):
        r"""启用ScheduledTask

        Enable scheduled task by id
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.EnableScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.EnableScheduledTaskResponse`
        """
        http_info = self._enable_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def enable_scheduled_task_async_invoker(self, request):
        http_info = self._enable_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_scheduled_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/schedule/task/{task_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            ['application/json;charset=UTF-8'])

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

    def list_scheduled_task_async(self, request):
        r"""查询ScheduledTask列表

        Get ScheduledTask infos
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.ListScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScheduledTaskResponse`
        """
        http_info = self._list_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_task_async_invoker(self, request):
        http_info = self._list_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scheduled_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/schedule/task",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'scheduled_type' in local_var_params:
            query_params.append(('scheduled_type', local_var_params['scheduled_type']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'associated_task_type' in local_var_params:
            query_params.append(('associated_task_type', local_var_params['associated_task_type']))
        if 'risk_level' in local_var_params:
            query_params.append(('risk_level', local_var_params['risk_level']))
        if 'created_by' in local_var_params:
            query_params.append(('created_by', local_var_params['created_by']))
        if 'reviewer' in local_var_params:
            query_params.append(('reviewer', local_var_params['reviewer']))
        if 'reviewer_user_name' in local_var_params:
            query_params.append(('reviewer_user_name', local_var_params['reviewer_user_name']))
        if 'approve_status' in local_var_params:
            query_params.append(('approve_status', local_var_params['approve_status']))
        if 'last_execution_status' in local_var_params:
            query_params.append(('last_execution_status', local_var_params['last_execution_status']))
        if 'last_execution_start_time' in local_var_params:
            query_params.append(('last_execution_start_time', local_var_params['last_execution_start_time']))
        if 'last_execution_end_time' in local_var_params:
            query_params.append(('last_execution_end_time', local_var_params['last_execution_end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_scheduled_task_history_async(self, request):
        r"""查询定时运维历史记录

        get scheduled task history list
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScheduledTaskHistory
        :type request: :class:`huaweicloudsdkcoc.v1.ListScheduledTaskHistoryRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScheduledTaskHistoryResponse`
        """
        http_info = self._list_scheduled_task_history_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_task_history_async_invoker(self, request):
        http_info = self._list_scheduled_task_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scheduled_task_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/schedule/task/history",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledTaskHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'started_start_time' in local_var_params:
            query_params.append(('started_start_time', local_var_params['started_start_time']))
        if 'started_end_time' in local_var_params:
            query_params.append(('started_end_time', local_var_params['started_end_time']))
        if 'finished_start_time' in local_var_params:
            query_params.append(('finished_start_time', local_var_params['finished_start_time']))
        if 'finished_end_time' in local_var_params:
            query_params.append(('finished_end_time', local_var_params['finished_end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def show_scheduled_task_async(self, request):
        r"""查询ScheduledTask

        Get ScheduledTask info by id
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.ShowScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowScheduledTaskResponse`
        """
        http_info = self._show_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def show_scheduled_task_async_invoker(self, request):
        http_info = self._show_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_scheduled_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/schedule/task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def update_scheduled_task_async(self, request):
        r"""修改ScheduledTask

        Update ScheduledTask
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateScheduledTaskResponse`
        """
        http_info = self._update_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def update_scheduled_task_async_invoker(self, request):
        http_info = self._update_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_scheduled_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/schedule/task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            ['application/json;charset=UTF-8'])

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

    def get_script_job_batch_async(self, request):
        r"""展示批次详情

        查询：批次详情，分页获取批次中的实例列表。
        过滤条件：分页参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetScriptJobBatch
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptJobBatchRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptJobBatchResponse`
        """
        http_info = self._get_script_job_batch_http_info(request)
        return self._call_api(**http_info)

    def get_script_job_batch_async_invoker(self, request):
        http_info = self._get_script_job_batch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_script_job_batch_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders/{execute_uuid}/batches/{batch_index}",
            "request_type": request.__class__.__name__,
            "response_type": "GetScriptJobBatchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_index' in local_var_params:
            path_params['batch_index'] = local_var_params['batch_index']
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def get_script_job_info_async(self, request):
        r"""展示脚本工单基本信息

        查询执行：基本信息
        执行类型、执行名称、创建人、创建时间、结束时间、执行状态、标签（脚本id，脚本名，执行脚本参数，执行用户，超时时长、成功率阈值）
        
        不同的任务类型消费标签中的不同key
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetScriptJobInfo
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptJobInfoRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptJobInfoResponse`
        """
        http_info = self._get_script_job_info_http_info(request)
        return self._call_api(**http_info)

    def get_script_job_info_async_invoker(self, request):
        http_info = self._get_script_job_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_script_job_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders/{execute_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "GetScriptJobInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def get_script_job_statistics_async(self, request):
        r"""展示实例状态统计信息

        查询：实例状态统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetScriptJobStatistics
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptJobStatisticsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptJobStatisticsResponse`
        """
        http_info = self._get_script_job_statistics_http_info(request)
        return self._call_api(**http_info)

    def get_script_job_statistics_async_invoker(self, request):
        http_info = self._get_script_job_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_script_job_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders/{execute_uuid}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "GetScriptJobStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_script_job_batches_async(self, request):
        r"""展示批次列表

        查询：批次列表
        返回：批次index、批次标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScriptJobBatches
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptJobBatchesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptJobBatchesResponse`
        """
        http_info = self._list_script_job_batches_http_info(request)
        return self._call_api(**http_info)

    def list_script_job_batches_async_invoker(self, request):
        http_info = self._list_script_job_batches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_script_job_batches_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders/{execute_uuid}/batches",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptJobBatchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_script_jobs_async(self, request):
        r"""展示工单列表

        查询作业工单列表，分页查询
        过滤：创建时间开始，创建时间结束、创建人
        返回：id、脚本名称、区域、创建人、创建时间、结束时间、总耗时、状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScriptJobs
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptJobsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptJobsResponse`
        """
        http_info = self._list_script_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_script_jobs_async_invoker(self, request):
        http_info = self._list_script_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_script_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def operate_script_job_async(self, request):
        r"""操作脚本工单

        操作类型：取消实例、跳过批次、取消整个工单、暂停整个工单、继续整个工单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for OperateScriptJob
        :type request: :class:`huaweicloudsdkcoc.v1.OperateScriptJobRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.OperateScriptJobResponse`
        """
        http_info = self._operate_script_job_http_info(request)
        return self._call_api(**http_info)

    def operate_script_job_async_invoker(self, request):
        http_info = self._operate_script_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _operate_script_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/job/script/orders/{execute_uuid}/operation",
            "request_type": request.__class__.__name__,
            "response_type": "OperateScriptJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def accept_script_async(self, request):
        r"""审批待审批的脚本

        功能：审批脚本。
        约束条件：只有创建脚本填写了审批人，脚本为待审批状态才能审批。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptScript
        :type request: :class:`huaweicloudsdkcoc.v1.AcceptScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.AcceptScriptResponse`
        """
        http_info = self._accept_script_http_info(request)
        return self._call_api(**http_info)

    def accept_script_async_invoker(self, request):
        http_info = self._accept_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _accept_script_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/scripts/{script_uuid}/action",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def check_script_risk_async(self, request):
        r"""评估脚本风险等级

        根据作业内容，对作业评估风险，返回相关分析的结果和信息，结果仅供参考。
        高危命令指影响系统或服务的正常运行，或造成系统特殊文件被恶意删除或修改命令。 高危命令检测通过校验规则正则匹配脚本内容中是否包含高危命令。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckScriptRisk
        :type request: :class:`huaweicloudsdkcoc.v1.CheckScriptRiskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CheckScriptRiskResponse`
        """
        http_info = self._check_script_risk_http_info(request)
        return self._call_api(**http_info)

    def check_script_risk_async_invoker(self, request):
        http_info = self._check_script_risk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_script_risk_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/analyze-job",
            "request_type": request.__class__.__name__,
            "response_type": "CheckScriptRiskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_script_async(self, request):
        r"""创建脚本

        创建作业脚本：自定义脚本
        - 脚本有标签属性，表示是高危脚本。创建时候不需要对脚本进行是否是高危的二次校验。
        - 进行租户隔离；北向接口创建的脚本，审批人字段不填写，默认不需要审批
        - 约束条件：
        - 脚本名称：同一租户下，脚本名称不能重复，最大字符64个字符，支持中文+字母+数字+下划线。
        - 脚本内容最大100kb。
        - 脚本参数个数最多20个。
        - 脚本描述：最大256个字符。
        - 单个参数的参数名称 64个字符，只支持字母+数字+下划线。
        - 单个参数的值最大1024个字符，正则表达式如下：^((?!\\.{2,})[a-zA-Z0-9_\\-/\\.\\*\\x20\\?:\&quot;,&#x3D;+@\\\\\\[\\{\\]\\}])*$。
        - 审批人最多支持5人。
        - 脚本输出的日志总量只支持1MB。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScript
        :type request: :class:`huaweicloudsdkcoc.v1.CreateScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateScriptResponse`
        """
        http_info = self._create_script_http_info(request)
        return self._call_api(**http_info)

    def create_script_async_invoker(self, request):
        http_info = self._create_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_script_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def delete_script_async(self, request):
        r"""删除自定义脚本

        删除作业脚本：自定义脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScript
        :type request: :class:`huaweicloudsdkcoc.v1.DeleteScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DeleteScriptResponse`
        """
        http_info = self._delete_script_http_info(request)
        return self._call_api(**http_info)

    def delete_script_async_invoker(self, request):
        http_info = self._delete_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_script_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/job/scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def execute_script_async(self, request):
        r"""执行自定义脚本

        执行脚本
        
        脚本入参、超时时间、执行用户、资源受限
        脚本入参支持20个。
        单次下发的机器支持200个。
        单次批次内机器数量最大10个。
        最大批次数量为20批。
        脚本输出的日志总量只支持1MB。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteScript
        :type request: :class:`huaweicloudsdkcoc.v1.ExecuteScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecuteScriptResponse`
        """
        http_info = self._execute_script_http_info(request)
        return self._call_api(**http_info)

    def execute_script_async_invoker(self, request):
        http_info = self._execute_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_script_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def get_script_async(self, request):
        r"""获取自定义脚本详情

        获取脚本详情
        约束条件：
        只能查询自定义脚本详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetScript
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptResponse`
        """
        http_info = self._get_script_http_info(request)
        return self._call_api(**http_info)

    def get_script_async_invoker(self, request):
        http_info = self._get_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "GetScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_instances_batch_async(self, request):
        r"""获取自动分批结果

        根据分批策略获取分批结果，只支持自动分批：
        规则如下：
        1.单个批次的所有实例必须属于同一个区域；
             * 2.单个批次的所有实例必须属于同一个可用区；
             * 3.单个批次的所有实例必须属于同一个应用；
             * 4.单个批次内同一分组下的实例不超过50%（除分组下仅以一个实例的情况外）；
             * 5.前三批每批节点数量不超过10。
             * 6.每批次实例数量不超过10。
        
           总机器数量为200。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesBatch
        :type request: :class:`huaweicloudsdkcoc.v1.ListInstancesBatchRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListInstancesBatchResponse`
        """
        http_info = self._list_instances_batch_http_info(request)
        return self._call_api(**http_info)

    def list_instances_batch_async_invoker(self, request):
        http_info = self._list_instances_batch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_batch_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/batches",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesBatchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def list_scripts_async(self, request):
        r"""查询脚本列表

        作业脚本列表：自定义脚本
        
        limit最大为100
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScripts
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptsResponse`
        """
        http_info = self._list_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_scripts_async_invoker(self, request):
        http_info = self._list_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scripts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'risk_level' in local_var_params:
            query_params.append(('risk_level', local_var_params['risk_level']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def update_script_async(self, request):
        r"""修改脚本

        修改作业脚本：自定义脚本
        约束条件：
        脚本名称：同一租户下，脚本名称不能重复，最大字符64个字符，支持中文+字母+数字+下划线。
        脚本内容最大4096个字符。
        脚本参数个数最多20个。
        脚本描述：最大256个字符。
        单个参数的参数名称 64个字符，只支持字母+数字+下划线。
        单个参数的值最大1024个字符，正则表达式如下：^((?!.{2,})[a-zA-Z0-9_-/.*\\x20?:\&quot;,&#x3D;+@\\[{]}])*$。
        修改的脚本如果有审批人，在修改之后，需要再次选择审批人，查询审批
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateScript
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateScriptResponse`
        """
        http_info = self._update_script_http_info(request)
        return self._call_api(**http_info)

    def update_script_async_invoker(self, request):
        http_info = self._update_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_script_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/job/scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def execute_public_script_async(self, request):
        r"""执行公共脚本

        执行公共脚本
        脚本入参、超时时间、执行用户、资源受限
        脚本入参支持20个。
        单次下发的机器支持200个。
        单次批次内机器数量最大10个。
        最大批次数量为20批。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecutePublicScript
        :type request: :class:`huaweicloudsdkcoc.v1.ExecutePublicScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecutePublicScriptResponse`
        """
        http_info = self._execute_public_script_http_info(request)
        return self._call_api(**http_info)

    def execute_public_script_async_invoker(self, request):
        http_info = self._execute_public_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_public_script_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/public-scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "ExecutePublicScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def get_public_script_async(self, request):
        r"""展示公共脚本详情

        展示公共脚本详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetPublicScript
        :type request: :class:`huaweicloudsdkcoc.v1.GetPublicScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetPublicScriptResponse`
        """
        http_info = self._get_public_script_http_info(request)
        return self._call_api(**http_info)

    def get_public_script_async_invoker(self, request):
        http_info = self._get_public_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_public_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/public-scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "GetPublicScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_public_scripts_async(self, request):
        r"""获取公共脚本列表

        获取公共脚本列表，分页逻辑：采用limit+marker方式，提高分页效率。用自增id作为marker参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicScripts
        :type request: :class:`huaweicloudsdkcoc.v1.ListPublicScriptsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListPublicScriptsResponse`
        """
        http_info = self._list_public_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_public_scripts_async_invoker(self, request):
        http_info = self._list_public_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_public_scripts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/public-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'risk_level' in local_var_params:
            query_params.append(('risk_level', local_var_params['risk_level']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def show_sla_customized_template_async(self, request):
        r"""查询Sla模板详情

        Get Sla Template info by id
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSlaCustomizedTemplate
        :type request: :class:`huaweicloudsdkcoc.v1.ShowSlaCustomizedTemplateRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowSlaCustomizedTemplateResponse`
        """
        http_info = self._show_sla_customized_template_http_info(request)
        return self._call_api(**http_info)

    def show_sla_customized_template_async_invoker(self, request):
        http_info = self._show_sla_customized_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sla_customized_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sla-mgmt/customized-template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlaCustomizedTemplateResponse"
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

    def show_sla_order_async(self, request):
        r"""查询SLA工单信息

        SLA 工单信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSlaOrder
        :type request: :class:`huaweicloudsdkcoc.v1.ShowSlaOrderRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowSlaOrderResponse`
        """
        http_info = self._show_sla_order_http_info(request)
        return self._call_api(**http_info)

    def show_sla_order_async_invoker(self, request):
        http_info = self._show_sla_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sla_order_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sla-mgmt/orders/{order_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlaOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'order_id' in local_var_params:
            path_params['order_id'] = local_var_params['order_id']

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

    def list_interrupt_records_async(self, request):
        r"""查询中断记录

        查询中断记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInterruptRecords
        :type request: :class:`huaweicloudsdkcoc.v1.ListInterruptRecordsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListInterruptRecordsResponse`
        """
        http_info = self._list_interrupt_records_http_info(request)
        return self._call_api(**http_info)

    def list_interrupt_records_async_invoker(self, request):
        http_info = self._list_interrupt_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_interrupt_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/slo-mgmt/slos/{slo_id}/interrupt-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListInterruptRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'slo_id' in local_var_params:
            path_params['slo_id'] = local_var_params['slo_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'source_id' in local_var_params:
            query_params.append(('source_id', local_var_params['source_id']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_slo_detail_async(self, request):
        r"""查询SLO详情

        查询SLO详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSloDetail
        :type request: :class:`huaweicloudsdkcoc.v1.ShowSloDetailRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowSloDetailResponse`
        """
        http_info = self._show_slo_detail_http_info(request)
        return self._call_api(**http_info)

    def show_slo_detail_async_invoker(self, request):
        http_info = self._show_slo_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_slo_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/slo-mgmt/slos/{slo_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSloDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'slo_id' in local_var_params:
            path_params['slo_id'] = local_var_params['slo_id']

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

    def create_war_room_async(self, request):
        r"""创建租户区WarRoom

        创建租户区WarRoom
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWarRoom
        :type request: :class:`huaweicloudsdkcoc.v1.CreateWarRoomRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateWarRoomResponse`
        """
        http_info = self._create_war_room_http_info(request)
        return self._call_api(**http_info)

    def create_war_room_async_invoker(self, request):
        http_info = self._create_war_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_war_room_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/warrooms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWarRoomResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_war_rooms_async(self, request):
        r"""查询租户区WarRoom信息列表

        查询租户区WarRoom信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWarRooms
        :type request: :class:`huaweicloudsdkcoc.v1.ListWarRoomsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListWarRoomsResponse`
        """
        http_info = self._list_war_rooms_http_info(request)
        return self._call_api(**http_info)

    def list_war_rooms_async_invoker(self, request):
        http_info = self._list_war_rooms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_war_rooms_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/warrooms/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListWarRoomsResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_applications_async(self, request):
        r"""查询应用

        查询应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdkcoc.v1.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListApplicationsResponse`
        """
        http_info = self._list_applications_http_info(request)
        return self._call_api(**http_info)

    def list_applications_async_invoker(self, request):
        http_info = self._list_applications_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_applications_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id_list' in local_var_params:
            query_params.append(('id_list', local_var_params['id_list']))
            collection_formats['id_list'] = 'csv'
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def list_application_model_async(self, request):
        r"""查询下一级的子应用、组件、分组

        查询下一级的子应用、组件、分组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplicationModel
        :type request: :class:`huaweicloudsdkcoc.v1.ListApplicationModelRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListApplicationModelResponse`
        """
        http_info = self._list_application_model_http_info(request)
        return self._call_api(**http_info)

    def list_application_model_async_invoker(self, request):
        http_info = self._list_application_model_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_application_model_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/application-model/next",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'application_id' in local_var_params:
            query_params.append(('application_id', local_var_params['application_id']))
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))

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

    def batch_create_application_view_async(self, request):
        r"""批量创建应用视图

        批量创建应用视图
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateApplicationView
        :type request: :class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewResponse`
        """
        http_info = self._batch_create_application_view_http_info(request)
        return self._call_api(**http_info)

    def batch_create_application_view_async_invoker(self, request):
        http_info = self._batch_create_application_view_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_application_view_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/application-view/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateApplicationViewResponse"
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
            ['application/json;charset=UTF-8'])

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

    def show_patch_baseline_async(self, request):
        r"""查询Baseline

        Get baseline info by id
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPatchBaseline
        :type request: :class:`huaweicloudsdkcoc.v1.ShowPatchBaselineRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowPatchBaselineResponse`
        """
        http_info = self._show_patch_baseline_http_info(request)
        return self._call_api(**http_info)

    def show_patch_baseline_async_invoker(self, request):
        http_info = self._show_patch_baseline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_patch_baseline_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/patch/baseline/{baseline_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPatchBaselineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'baseline_id' in local_var_params:
            path_params['baseline_id'] = local_var_params['baseline_id']

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

    def list_cce_compliant_async(self, request):
        r"""获取合规性报告cce信息

        分页获取合规性报告cce信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCceCompliant
        :type request: :class:`huaweicloudsdkcoc.v1.ListCceCompliantRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListCceCompliantResponse`
        """
        http_info = self._list_cce_compliant_http_info(request)
        return self._call_api(**http_info)

    def list_cce_compliant_async_invoker(self, request):
        http_info = self._list_cce_compliant_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cce_compliant_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/patch/cce/compliant",
            "request_type": request.__class__.__name__,
            "response_type": "ListCceCompliantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_instance_compliant_async(self, request):
        r"""获取节点合规性报告

        分页获取节点合规性报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceCompliant
        :type request: :class:`huaweicloudsdkcoc.v1.ListInstanceCompliantRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListInstanceCompliantResponse`
        """
        http_info = self._list_instance_compliant_http_info(request)
        return self._call_api(**http_info)

    def list_instance_compliant_async_invoker(self, request):
        http_info = self._list_instance_compliant_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_compliant_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/patch/instance/compliant",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceCompliantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'eip' in local_var_params:
            query_params.append(('eip', local_var_params['eip']))
        if 'operating_system' in local_var_params:
            query_params.append(('operating_system', local_var_params['operating_system']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))
        if 'compliant_status' in local_var_params:
            query_params.append(('compliant_status', local_var_params['compliant_status']))
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'report_scene' in local_var_params:
            query_params.append(('report_scene', local_var_params['report_scene']))
        if 'cce_info_id' in local_var_params:
            query_params.append(('cce_info_id', local_var_params['cce_info_id']))

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

    def show_instance_patch_items_async(self, request):
        r"""分页获取节点补丁详情

        分页获取节点补丁详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstancePatchItems
        :type request: :class:`huaweicloudsdkcoc.v1.ShowInstancePatchItemsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowInstancePatchItemsResponse`
        """
        http_info = self._show_instance_patch_items_http_info(request)
        return self._call_api(**http_info)

    def show_instance_patch_items_async_invoker(self, request):
        http_info = self._show_instance_patch_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_patch_items_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/patch/instance/compliant/{instance_compliant_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstancePatchItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_compliant_id' in local_var_params:
            path_params['instance_compliant_id'] = local_var_params['instance_compliant_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'title' in local_var_params:
            query_params.append(('title', local_var_params['title']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'patch_status' in local_var_params:
            query_params.append(('patch_status', local_var_params['patch_status']))
        if 'classification' in local_var_params:
            query_params.append(('classification', local_var_params['classification']))
        if 'severity_level' in local_var_params:
            query_params.append(('severity_level', local_var_params['severity_level']))
        if 'compliance_level' in local_var_params:
            query_params.append(('compliance_level', local_var_params['compliance_level']))

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

    def list_multi_cloud_resources_async(self, request):
        r"""查询用户在云厂商中的资源

        查询用户在云厂商中的资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMultiCloudResources
        :type request: :class:`huaweicloudsdkcoc.v1.ListMultiCloudResourcesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListMultiCloudResourcesResponse`
        """
        http_info = self._list_multi_cloud_resources_http_info(request)
        return self._call_api(**http_info)

    def list_multi_cloud_resources_async_invoker(self, request):
        http_info = self._list_multi_cloud_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_multi_cloud_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/multicloud-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListMultiCloudResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vendor' in local_var_params:
            query_params.append(('vendor', local_var_params['vendor']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'resource_id_list' in local_var_params:
            query_params.append(('resource_id_list', local_var_params['resource_id_list']))
            collection_formats['resource_id_list'] = 'csv'
        if 'name_list' in local_var_params:
            query_params.append(('name_list', local_var_params['name_list']))
            collection_formats['name_list'] = 'csv'
        if 'region_id_list' in local_var_params:
            query_params.append(('region_id_list', local_var_params['region_id_list']))
            collection_formats['region_id_list'] = 'csv'

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

    def count_multi_resources_async(self, request):
        r"""查询用户各种资源总数

        查询用户各种资源总数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountMultiResources
        :type request: :class:`huaweicloudsdkcoc.v1.CountMultiResourcesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CountMultiResourcesResponse`
        """
        http_info = self._count_multi_resources_http_info(request)
        return self._call_api(**http_info)

    def count_multi_resources_async_invoker(self, request):
        http_info = self._count_multi_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_multi_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources/multi-count",
            "request_type": request.__class__.__name__,
            "response_type": "CountMultiResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vendor' in local_var_params:
            query_params.append(('vendor', local_var_params['vendor']))
        if 'view_id' in local_var_params:
            query_params.append(('view_id', local_var_params['view_id']))
        if 'is_resource' in local_var_params:
            query_params.append(('is_resource', local_var_params['is_resource']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))

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

    def list_resource_async(self, request):
        r"""查询用户所有资源

        查询用户所有资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResource
        :type request: :class:`huaweicloudsdkcoc.v1.ListResourceRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListResourceResponse`
        """
        http_info = self._list_resource_http_info(request)
        return self._call_api(**http_info)

    def list_resource_async_invoker(self, request):
        http_info = self._list_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'resource_id_list' in local_var_params:
            query_params.append(('resource_id_list', local_var_params['resource_id_list']))
            collection_formats['resource_id_list'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'az_id' in local_var_params:
            query_params.append(('az_id', local_var_params['az_id']))
        if 'ip_type' in local_var_params:
            query_params.append(('ip_type', local_var_params['ip_type']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'agent_state' in local_var_params:
            query_params.append(('agent_state', local_var_params['agent_state']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'tag_key' in local_var_params:
            query_params.append(('tag_key', local_var_params['tag_key']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))
        if 'application_id' in local_var_params:
            query_params.append(('application_id', local_var_params['application_id']))
        if 'cce_cluster_id' in local_var_params:
            query_params.append(('cce_cluster_id', local_var_params['cce_cluster_id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
        if 'is_delegated' in local_var_params:
            query_params.append(('is_delegated', local_var_params['is_delegated']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def sync_resource_async(self, request):
        r"""从RMS同步用户所有资源

        从RMS同步用户所有资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncResource
        :type request: :class:`huaweicloudsdkcoc.v1.SyncResourceRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.SyncResourceResponse`
        """
        http_info = self._sync_resource_http_info(request)
        return self._call_api(**http_info)

    def sync_resource_async_invoker(self, request):
        http_info = self._sync_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resources/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncResourceResponse"
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
            ['application/json;charset=UTF-8'])

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
            kwargs["async_request"] = True
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
