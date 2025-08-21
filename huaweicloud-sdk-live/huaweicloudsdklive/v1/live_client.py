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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdklive'")


class LiveClient(Client):
    def __init__(self):
        super(LiveClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklive.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "LiveClient":
                raise TypeError("client type error, support client type is LiveClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_show_ip_belongs(self, request):
        r"""查询IP归属信息

        查询IP归属信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowIpBelongs
        :type request: :class:`huaweicloudsdklive.v1.BatchShowIpBelongsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.BatchShowIpBelongsResponse`
        """
        http_info = self._batch_show_ip_belongs_http_info(request)
        return self._call_api(**http_info)

    def batch_show_ip_belongs_invoker(self, request):
        http_info = self._batch_show_ip_belongs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_ip_belongs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cdn/ip-info",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowIpBelongsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
            collection_formats['ip'] = 'multi'

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

    def create_domain(self, request):
        r"""创建直播域名

        可单独创建直播播放域名或推流域名，每个租户最多可配置64条域名记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDomain
        :type request: :class:`huaweicloudsdklive.v1.CreateDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateDomainResponse`
        """
        http_info = self._create_domain_http_info(request)
        return self._call_api(**http_info)

    def create_domain_invoker(self, request):
        http_info = self._create_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_domain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_domain_mapping(self, request):
        r"""域名映射

        将用户已创建的播放域名和推流域名建立域名映射关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDomainMapping
        :type request: :class:`huaweicloudsdklive.v1.CreateDomainMappingRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateDomainMappingResponse`
        """
        http_info = self._create_domain_mapping_http_info(request)
        return self._call_api(**http_info)

    def create_domain_mapping_invoker(self, request):
        http_info = self._create_domain_mapping_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_domain_mapping_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domains_mapping",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainMappingResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_flow_output(self, request):
        r"""创建转推输出

        创建转推输出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlowOutput
        :type request: :class:`huaweicloudsdklive.v1.CreateFlowOutputRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateFlowOutputResponse`
        """
        http_info = self._create_flow_output_http_info(request)
        return self._call_api(**http_info)

    def create_flow_output_invoker(self, request):
        http_info = self._create_flow_output_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flow_output_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/flows/outputs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlowOutputResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_flows(self, request):
        r"""创建流

        创建流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlows
        :type request: :class:`huaweicloudsdklive.v1.CreateFlowsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateFlowsResponse`
        """
        http_info = self._create_flows_http_info(request)
        return self._call_api(**http_info)

    def create_flows_invoker(self, request):
        http_info = self._create_flows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flows_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/flows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlowsResponse"
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
            ['application/json;charset=utf-8'])

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

    def create_record_callback_config(self, request):
        r"""创建录制回调配置

        创建录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordCallbackConfigResponse`
        """
        http_info = self._create_record_callback_config_http_info(request)
        return self._call_api(**http_info)

    def create_record_callback_config_invoker(self, request):
        http_info = self._create_record_callback_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_record_callback_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/record/callbacks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordCallbackConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_record_index(self, request):
        r"""创建录制视频索引文件

        Create Record Index
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordIndex
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordIndexRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordIndexResponse`
        """
        http_info = self._create_record_index_http_info(request)
        return self._call_api(**http_info)

    def create_record_index_invoker(self, request):
        http_info = self._create_record_index_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_record_index_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/record/indexes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordIndexResponse"
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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def create_record_rule(self, request):
        r"""创建录制规则

        创建录制规则接口，录制规则对新推送的流生效，对已经推送中的流不生效
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordRule
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordRuleResponse`
        """
        http_info = self._create_record_rule_http_info(request)
        return self._call_api(**http_info)

    def create_record_rule_invoker(self, request):
        http_info = self._create_record_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_record_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/record/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordRuleResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_schedule_record_tasks(self, request):
        r"""创建计划录制任务

        通过使用指定录制模板ID对应的配置创建一个在指定时间启动、结束的录制任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScheduleRecordTasks
        :type request: :class:`huaweicloudsdklive.v1.CreateScheduleRecordTasksRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateScheduleRecordTasksResponse`
        """
        http_info = self._create_schedule_record_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_schedule_record_tasks_invoker(self, request):
        http_info = self._create_schedule_record_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_schedule_record_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/schedule/record/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScheduleRecordTasksResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_snapshot_config(self, request):
        r"""创建直播截图配置

        创建直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.CreateSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateSnapshotConfigResponse`
        """
        http_info = self._create_snapshot_config_http_info(request)
        return self._call_api(**http_info)

    def create_snapshot_config_invoker(self, request):
        http_info = self._create_snapshot_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_snapshot_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stream/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSnapshotConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_stream_forbidden(self, request):
        r"""禁止直播推流

        禁止直播推流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.CreateStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateStreamForbiddenResponse`
        """
        http_info = self._create_stream_forbidden_http_info(request)
        return self._call_api(**http_info)

    def create_stream_forbidden_invoker(self, request):
        http_info = self._create_stream_forbidden_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_stream_forbidden_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stream/blocks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStreamForbiddenResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_stream_forbidden_once(self, request):
        r"""禁推闪断

        直播推流闪断接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStreamForbiddenOnce
        :type request: :class:`huaweicloudsdklive.v1.CreateStreamForbiddenOnceRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateStreamForbiddenOnceResponse`
        """
        http_info = self._create_stream_forbidden_once_http_info(request)
        return self._call_api(**http_info)

    def create_stream_forbidden_once_invoker(self, request):
        http_info = self._create_stream_forbidden_once_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_stream_forbidden_once_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stream/block-once",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStreamForbiddenOnceResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_transcodings_template(self, request):
        r"""创建直播转码模板

        创建直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.CreateTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateTranscodingsTemplateResponse`
        """
        http_info = self._create_transcodings_template_http_info(request)
        return self._call_api(**http_info)

    def create_transcodings_template_invoker(self, request):
        http_info = self._create_transcodings_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_transcodings_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTranscodingsTemplateResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_url_authchain(self, request):
        r"""生成URL鉴权串

        生成URL鉴权串
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUrlAuthchain
        :type request: :class:`huaweicloudsdklive.v1.CreateUrlAuthchainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateUrlAuthchainResponse`
        """
        http_info = self._create_url_authchain_http_info(request)
        return self._call_api(**http_info)

    def create_url_authchain_invoker(self, request):
        http_info = self._create_url_authchain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_url_authchain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/auth/chain",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUrlAuthchainResponse"
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
            ['application/json; charset=UTF-8'])

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

    def delete_domain(self, request):
        r"""删除直播域名

        删除域名。只有在域名停用（off）状态时才能删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomain
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainResponse`
        """
        http_info = self._delete_domain_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_invoker(self, request):
        http_info = self._delete_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_domain_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def delete_domain_key_chain(self, request):
        r"""删除指定域名的Key防盗链配置

        删除指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainKeyChainResponse`
        """
        http_info = self._delete_domain_key_chain_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_key_chain_invoker(self, request):
        http_info = self._delete_domain_key_chain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_domain_key_chain_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/guard/key-chain",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainKeyChainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def delete_domain_mapping(self, request):
        r"""删除直播域名映射关系

        将播放域名和推流域名的域名映射关系删除
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainMapping
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainMappingRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainMappingResponse`
        """
        http_info = self._delete_domain_mapping_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_mapping_invoker(self, request):
        http_info = self._delete_domain_mapping_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_domain_mapping_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/domains_mapping",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainMappingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pull_domain' in local_var_params:
            query_params.append(('pull_domain', local_var_params['pull_domain']))
        if 'push_domain' in local_var_params:
            query_params.append(('push_domain', local_var_params['push_domain']))

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

    def delete_flow(self, request):
        r"""删除流

        删除流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlow
        :type request: :class:`huaweicloudsdklive.v1.DeleteFlowRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteFlowResponse`
        """
        http_info = self._delete_flow_http_info(request)
        return self._call_api(**http_info)

    def delete_flow_invoker(self, request):
        http_info = self._delete_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_flow_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/flows",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFlowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))

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

    def delete_flow_output(self, request):
        r"""删除转推输出

        删除转推输出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlowOutput
        :type request: :class:`huaweicloudsdklive.v1.DeleteFlowOutputRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteFlowOutputResponse`
        """
        http_info = self._delete_flow_output_http_info(request)
        return self._call_api(**http_info)

    def delete_flow_output_invoker(self, request):
        http_info = self._delete_flow_output_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_flow_output_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/flows/outputs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFlowOutputResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))
        if 'output_name' in local_var_params:
            query_params.append(('output_name', local_var_params['output_name']))

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

    def delete_publish_template(self, request):
        r"""删除直播推流通知配置

        删除直播推流通知配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePublishTemplate
        :type request: :class:`huaweicloudsdklive.v1.DeletePublishTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeletePublishTemplateResponse`
        """
        http_info = self._delete_publish_template_http_info(request)
        return self._call_api(**http_info)

    def delete_publish_template_invoker(self, request):
        http_info = self._delete_publish_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_publish_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/notifications/publish",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePublishTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def delete_record_callback_config(self, request):
        r"""删除录制回调配置

        删除录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.DeleteRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteRecordCallbackConfigResponse`
        """
        http_info = self._delete_record_callback_config_http_info(request)
        return self._call_api(**http_info)

    def delete_record_callback_config_invoker(self, request):
        http_info = self._delete_record_callback_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_record_callback_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/record/callbacks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordCallbackConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_record_rule(self, request):
        r"""删除录制规则

        删除录制规则接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordRule
        :type request: :class:`huaweicloudsdklive.v1.DeleteRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteRecordRuleResponse`
        """
        http_info = self._delete_record_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_record_rule_invoker(self, request):
        http_info = self._delete_record_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_record_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/record/rules/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_referer_chain(self, request):
        r"""删除Referer防盗链黑白名单

        删除Referer防盗链黑白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRefererChain
        :type request: :class:`huaweicloudsdklive.v1.DeleteRefererChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteRefererChainResponse`
        """
        http_info = self._delete_referer_chain_http_info(request)
        return self._call_api(**http_info)

    def delete_referer_chain_invoker(self, request):
        http_info = self._delete_referer_chain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_referer_chain_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/guard/referer-chain",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRefererChainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def delete_schedule_record_tasks(self, request):
        r"""停止计划录制任务

        停止计划录制任务，当前的录制任务会中止并生产录制文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScheduleRecordTasks
        :type request: :class:`huaweicloudsdklive.v1.DeleteScheduleRecordTasksRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteScheduleRecordTasksResponse`
        """
        http_info = self._delete_schedule_record_tasks_http_info(request)
        return self._call_api(**http_info)

    def delete_schedule_record_tasks_invoker(self, request):
        http_info = self._delete_schedule_record_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_schedule_record_tasks_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/schedule/record/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScheduleRecordTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def delete_snapshot_config(self, request):
        r"""删除直播截图配置

        删除直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.DeleteSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteSnapshotConfigResponse`
        """
        http_info = self._delete_snapshot_config_http_info(request)
        return self._call_api(**http_info)

    def delete_snapshot_config_invoker(self, request):
        http_info = self._delete_snapshot_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_snapshot_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/stream/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSnapshotConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

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

    def delete_stream_forbidden(self, request):
        r"""禁推恢复

        恢复直播推流接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.DeleteStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteStreamForbiddenResponse`
        """
        http_info = self._delete_stream_forbidden_http_info(request)
        return self._call_api(**http_info)

    def delete_stream_forbidden_invoker(self, request):
        http_info = self._delete_stream_forbidden_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_stream_forbidden_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/stream/blocks",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStreamForbiddenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))

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

    def delete_transcodings_template(self, request):
        r"""删除直播转码模板

        删除直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.DeleteTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteTranscodingsTemplateResponse`
        """
        http_info = self._delete_transcodings_template_http_info(request)
        return self._call_api(**http_info)

    def delete_transcodings_template_invoker(self, request):
        http_info = self._delete_transcodings_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_transcodings_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTranscodingsTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

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

    def list_delay_config(self, request):
        r"""查询播放域名延时配置

        查询播放域名延时配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDelayConfig
        :type request: :class:`huaweicloudsdklive.v1.ListDelayConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListDelayConfigResponse`
        """
        http_info = self._list_delay_config_http_info(request)
        return self._call_api(**http_info)

    def list_delay_config_invoker(self, request):
        http_info = self._list_delay_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_delay_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain/delay",
            "request_type": request.__class__.__name__,
            "response_type": "ListDelayConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domain' in local_var_params:
            query_params.append(('play_domain', local_var_params['play_domain']))

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

    def list_flows(self, request):
        r"""获取流列表

        获取流列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlows
        :type request: :class:`huaweicloudsdklive.v1.ListFlowsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListFlowsResponse`
        """
        http_info = self._list_flows_http_info(request)
        return self._call_api(**http_info)

    def list_flows_invoker(self, request):
        http_info = self._list_flows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flows_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/flows",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlowsResponse"
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

    def list_geo_blocking_config(self, request):
        r"""获取地域限制配置列表

        查询播放域名的地域限制列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGeoBlockingConfig
        :type request: :class:`huaweicloudsdklive.v1.ListGeoBlockingConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListGeoBlockingConfigResponse`
        """
        http_info = self._list_geo_blocking_config_http_info(request)
        return self._call_api(**http_info)

    def list_geo_blocking_config_invoker(self, request):
        http_info = self._list_geo_blocking_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_geo_blocking_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain/geo-blocking",
            "request_type": request.__class__.__name__,
            "response_type": "ListGeoBlockingConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domain' in local_var_params:
            query_params.append(('play_domain', local_var_params['play_domain']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_hls_config(self, request):
        r"""查询域名HLS配置

        查询域名HLS配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHlsConfig
        :type request: :class:`huaweicloudsdklive.v1.ListHlsConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListHlsConfigResponse`
        """
        http_info = self._list_hls_config_http_info(request)
        return self._call_api(**http_info)

    def list_hls_config_invoker(self, request):
        http_info = self._list_hls_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_hls_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain/hls",
            "request_type": request.__class__.__name__,
            "response_type": "ListHlsConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'push_domain' in local_var_params:
            query_params.append(('push_domain', local_var_params['push_domain']))

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

    def list_ip_auth_list(self, request):
        r"""查询IP黑/白名单

        查询推流/播放域名的IP黑/白名单。
        - 黑名单模式：禁止指定的IP或网段
        - 白名单模式：仅允许指定的IP或网段
        - 默认：全放通。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpAuthList
        :type request: :class:`huaweicloudsdklive.v1.ListIpAuthListRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListIpAuthListResponse`
        """
        http_info = self._list_ip_auth_list_http_info(request)
        return self._call_api(**http_info)

    def list_ip_auth_list_invoker(self, request):
        http_info = self._list_ip_auth_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ip_auth_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/guard/ip",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpAuthListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_live_sample_logs(self, request):
        r"""获取直播播放日志

        获取直播播放日志，基于域名以5分钟粒度进行打包，日志内容以 \&quot;|\&quot; 进行分隔。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLiveSampleLogs
        :type request: :class:`huaweicloudsdklive.v1.ListLiveSampleLogsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListLiveSampleLogsResponse`
        """
        http_info = self._list_live_sample_logs_http_info(request)
        return self._call_api(**http_info)

    def list_live_sample_logs_invoker(self, request):
        http_info = self._list_live_sample_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_live_sample_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveSampleLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domain' in local_var_params:
            query_params.append(('play_domain', local_var_params['play_domain']))
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

    def list_live_streams_online(self, request):
        r"""查询直播中的流信息

        查询直播中的流信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLiveStreamsOnline
        :type request: :class:`huaweicloudsdklive.v1.ListLiveStreamsOnlineRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListLiveStreamsOnlineResponse`
        """
        http_info = self._list_live_streams_online_http_info(request)
        return self._call_api(**http_info)

    def list_live_streams_online_invoker(self, request):
        http_info = self._list_live_streams_online_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_live_streams_online_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/realtime/streams",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveStreamsOnlineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))

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

    def list_publish_template(self, request):
        r"""查询直播推流通知配置

        查询直播推流通知配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublishTemplate
        :type request: :class:`huaweicloudsdklive.v1.ListPublishTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListPublishTemplateResponse`
        """
        http_info = self._list_publish_template_http_info(request)
        return self._call_api(**http_info)

    def list_publish_template_invoker(self, request):
        http_info = self._list_publish_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_publish_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notifications/publish",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublishTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def list_record_callback_configs(self, request):
        r"""查询录制回调配置列表

        查询录制回调配置列表接口。通过指定条件，查询满足条件的配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordCallbackConfigs
        :type request: :class:`huaweicloudsdklive.v1.ListRecordCallbackConfigsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordCallbackConfigsResponse`
        """
        http_info = self._list_record_callback_configs_http_info(request)
        return self._call_api(**http_info)

    def list_record_callback_configs_invoker(self, request):
        http_info = self._list_record_callback_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_record_callback_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/callbacks",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordCallbackConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
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

    def list_record_contents(self, request):
        r"""录制完成内容的查询

        录制完成的内容查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordContents
        :type request: :class:`huaweicloudsdklive.v1.ListRecordContentsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordContentsResponse`
        """
        http_info = self._list_record_contents_http_info(request)
        return self._call_api(**http_info)

    def list_record_contents_invoker(self, request):
        http_info = self._list_record_contents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_record_contents_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/contents",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordContentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'record_type' in local_var_params:
            query_params.append(('record_type', local_var_params['record_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_record_rules(self, request):
        r"""查询录制规则列表

        查询录制规则列表接口，通过指定条件，查询满足条件的录制规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordRules
        :type request: :class:`huaweicloudsdklive.v1.ListRecordRulesRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordRulesResponse`
        """
        http_info = self._list_record_rules_http_info(request)
        return self._call_api(**http_info)

    def list_record_rules_invoker(self, request):
        http_info = self._list_record_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_record_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'record_type' in local_var_params:
            query_params.append(('record_type', local_var_params['record_type']))
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

    def list_schedule_record_tasks(self, request):
        r"""查询计划录制任务

        查询指定时间范围内启动和结束的计划录制任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScheduleRecordTasks
        :type request: :class:`huaweicloudsdklive.v1.ListScheduleRecordTasksRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListScheduleRecordTasksResponse`
        """
        http_info = self._list_schedule_record_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_schedule_record_tasks_invoker(self, request):
        http_info = self._list_schedule_record_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_schedule_record_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/schedule/record/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduleRecordTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_snapshot_configs(self, request):
        r"""查询直播截图配置

        查询直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshotConfigs
        :type request: :class:`huaweicloudsdklive.v1.ListSnapshotConfigsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListSnapshotConfigsResponse`
        """
        http_info = self._list_snapshot_configs_http_info(request)
        return self._call_api(**http_info)

    def list_snapshot_configs_invoker(self, request):
        http_info = self._list_snapshot_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_snapshot_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stream/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
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

    def list_stream_forbidden(self, request):
        r"""查询禁止直播推流列表

        查询禁播黑名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.ListStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListStreamForbiddenResponse`
        """
        http_info = self._list_stream_forbidden_http_info(request)
        return self._call_api(**http_info)

    def list_stream_forbidden_invoker(self, request):
        http_info = self._list_stream_forbidden_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stream_forbidden_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stream/blocks",
            "request_type": request.__class__.__name__,
            "response_type": "ListStreamForbiddenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

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

    def modify_flow_output(self, request):
        r"""更新转推输出

        更新转推输出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyFlowOutput
        :type request: :class:`huaweicloudsdklive.v1.ModifyFlowOutputRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyFlowOutputResponse`
        """
        http_info = self._modify_flow_output_http_info(request)
        return self._call_api(**http_info)

    def modify_flow_output_invoker(self, request):
        http_info = self._modify_flow_output_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_flow_output_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/flows/outputs",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyFlowOutputResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))
        if 'output_name' in local_var_params:
            query_params.append(('output_name', local_var_params['output_name']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def modify_flow_sources(self, request):
        r"""修改流来源

        修改流来源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyFlowSources
        :type request: :class:`huaweicloudsdklive.v1.ModifyFlowSourcesRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyFlowSourcesResponse`
        """
        http_info = self._modify_flow_sources_http_info(request)
        return self._call_api(**http_info)

    def modify_flow_sources_invoker(self, request):
        http_info = self._modify_flow_sources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_flow_sources_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/flows/sources",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyFlowSourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))
        if 'source_name' in local_var_params:
            query_params.append(('source_name', local_var_params['source_name']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def modify_flow_start(self, request):
        r"""启动流任务

        启动流任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyFlowStart
        :type request: :class:`huaweicloudsdklive.v1.ModifyFlowStartRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyFlowStartResponse`
        """
        http_info = self._modify_flow_start_http_info(request)
        return self._call_api(**http_info)

    def modify_flow_start_invoker(self, request):
        http_info = self._modify_flow_start_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_flow_start_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/flows/start",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyFlowStartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))

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

    def modify_flow_stop(self, request):
        r"""停止流任务

        停止流任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyFlowStop
        :type request: :class:`huaweicloudsdklive.v1.ModifyFlowStopRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyFlowStopResponse`
        """
        http_info = self._modify_flow_stop_http_info(request)
        return self._call_api(**http_info)

    def modify_flow_stop_invoker(self, request):
        http_info = self._modify_flow_stop_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_flow_stop_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/flows/stop",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyFlowStopResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))

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

    def run_record(self, request):
        r"""提交录制控制命令

        对单条流的实时录制控制接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunRecord
        :type request: :class:`huaweicloudsdklive.v1.RunRecordRequest`
        :rtype: :class:`huaweicloudsdklive.v1.RunRecordResponse`
        """
        http_info = self._run_record_http_info(request)
        return self._call_api(**http_info)

    def run_record_invoker(self, request):
        http_info = self._run_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_record_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/record/control",
            "request_type": request.__class__.__name__,
            "response_type": "RunRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def set_referer_chain(self, request):
        r"""设置Referer防盗链黑白名单

        设置Referer黑白名单，直播服务会根据配置的referer黑白名单，对访问者的身份进行识别和过滤，符合规则的可以顺利访问到该内容。如果不符合规则，该访问请求将会被禁止。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRefererChain
        :type request: :class:`huaweicloudsdklive.v1.SetRefererChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.SetRefererChainResponse`
        """
        http_info = self._set_referer_chain_http_info(request)
        return self._call_api(**http_info)

    def set_referer_chain_invoker(self, request):
        http_info = self._set_referer_chain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_referer_chain_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/guard/referer-chain",
            "request_type": request.__class__.__name__,
            "response_type": "SetRefererChainResponse"
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
            ['application/json; charset=UTF-8'])

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

    def show_domain(self, request):
        r"""查询直播域名

        查询直播域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomain
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainResponse`
        """
        http_info = self._show_domain_http_info(request)
        return self._call_api(**http_info)

    def show_domain_invoker(self, request):
        http_info = self._show_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def show_domain_key_chain(self, request):
        r"""查询指定域名的Key防盗链配置

        查询指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainKeyChainResponse`
        """
        http_info = self._show_domain_key_chain_http_info(request)
        return self._call_api(**http_info)

    def show_domain_key_chain_invoker(self, request):
        http_info = self._show_domain_key_chain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_key_chain_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/guard/key-chain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainKeyChainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def show_flow_detail(self, request):
        r"""获取流详情

        获取流详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlowDetail
        :type request: :class:`huaweicloudsdklive.v1.ShowFlowDetailRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowFlowDetailResponse`
        """
        http_info = self._show_flow_detail_http_info(request)
        return self._call_api(**http_info)

    def show_flow_detail_invoker(self, request):
        http_info = self._show_flow_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flow_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/flows/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlowDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))

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

    def show_output_info(self, request):
        r"""查询转推输出

        查询转推输出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOutputInfo
        :type request: :class:`huaweicloudsdklive.v1.ShowOutputInfoRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowOutputInfoResponse`
        """
        http_info = self._show_output_info_http_info(request)
        return self._call_api(**http_info)

    def show_output_info_invoker(self, request):
        http_info = self._show_output_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_output_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/flows/outputs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOutputInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data_display' in local_var_params:
            query_params.append(('data_display', local_var_params['data_display']))
        if 'flow_id' in local_var_params:
            query_params.append(('flow_id', local_var_params['flow_id']))
        if 'output_name' in local_var_params:
            query_params.append(('output_name', local_var_params['output_name']))

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

    def show_pull_sources_config(self, request):
        r"""查询直播拉流回源配置

        查询直播拉流回源配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPullSourcesConfig
        :type request: :class:`huaweicloudsdklive.v1.ShowPullSourcesConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowPullSourcesConfigResponse`
        """
        http_info = self._show_pull_sources_config_http_info(request)
        return self._call_api(**http_info)

    def show_pull_sources_config_invoker(self, request):
        http_info = self._show_pull_sources_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pull_sources_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain/pull-sources",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPullSourcesConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domain' in local_var_params:
            query_params.append(('play_domain', local_var_params['play_domain']))

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

    def show_record_callback_config(self, request):
        r"""查询录制回调配置

        查询录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.ShowRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowRecordCallbackConfigResponse`
        """
        http_info = self._show_record_callback_config_http_info(request)
        return self._call_api(**http_info)

    def show_record_callback_config_invoker(self, request):
        http_info = self._show_record_callback_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_record_callback_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/callbacks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordCallbackConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_record_rule(self, request):
        r"""查询录制规则配置

        查询录制规则接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordRule
        :type request: :class:`huaweicloudsdklive.v1.ShowRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowRecordRuleResponse`
        """
        http_info = self._show_record_rule_http_info(request)
        return self._call_api(**http_info)

    def show_record_rule_invoker(self, request):
        http_info = self._show_record_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_record_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/rules/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_referer_chain(self, request):
        r"""查询Referer防盗链黑白名单

        查询Referer防盗链黑白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRefererChain
        :type request: :class:`huaweicloudsdklive.v1.ShowRefererChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowRefererChainResponse`
        """
        http_info = self._show_referer_chain_http_info(request)
        return self._call_api(**http_info)

    def show_referer_chain_invoker(self, request):
        http_info = self._show_referer_chain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_referer_chain_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/guard/referer-chain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRefererChainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def show_transcodings_template(self, request):
        r"""查询直播转码模板

        查询直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.ShowTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowTranscodingsTemplateResponse`
        """
        http_info = self._show_transcodings_template_http_info(request)
        return self._call_api(**http_info)

    def show_transcodings_template_invoker(self, request):
        http_info = self._show_transcodings_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_transcodings_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTranscodingsTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

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

    def update_delay_config(self, request):
        r"""修改播放域名延时配置

        修改播放域名延时配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDelayConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateDelayConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDelayConfigResponse`
        """
        http_info = self._update_delay_config_http_info(request)
        return self._call_api(**http_info)

    def update_delay_config_invoker(self, request):
        http_info = self._update_delay_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_delay_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain/delay",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDelayConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_domain(self, request):
        r"""修改直播域名

        修改直播播放、RTMP推流加速域名相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomain
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainResponse`
        """
        http_info = self._update_domain_http_info(request)
        return self._call_api(**http_info)

    def update_domain_invoker(self, request):
        http_info = self._update_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_domain_ip6_switch(self, request):
        r"""配置域名IPV6开关

        配置IPV6开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainIp6Switch
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainIp6SwitchRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainIp6SwitchResponse`
        """
        http_info = self._update_domain_ip6_switch_http_info(request)
        return self._call_api(**http_info)

    def update_domain_ip6_switch_invoker(self, request):
        http_info = self._update_domain_ip6_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_ip6_switch_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain/ipv6-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainIp6SwitchResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_domain_key_chain(self, request):
        r"""更新指定域名的Key防盗链配置

        更新指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainKeyChainResponse`
        """
        http_info = self._update_domain_key_chain_http_info(request)
        return self._call_api(**http_info)

    def update_domain_key_chain_invoker(self, request):
        http_info = self._update_domain_key_chain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_key_chain_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/guard/key-chain",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainKeyChainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def update_geo_blocking_config(self, request):
        r"""修改地域限制配置

        修改播放域名的地域限制，选中地域允许接入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGeoBlockingConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateGeoBlockingConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateGeoBlockingConfigResponse`
        """
        http_info = self._update_geo_blocking_config_http_info(request)
        return self._call_api(**http_info)

    def update_geo_blocking_config_invoker(self, request):
        http_info = self._update_geo_blocking_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_geo_blocking_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain/geo-blocking",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGeoBlockingConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domain' in local_var_params:
            query_params.append(('play_domain', local_var_params['play_domain']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def update_hls_config(self, request):
        r"""修改域名HLS配置

        修改域名HLS配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHlsConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateHlsConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateHlsConfigResponse`
        """
        http_info = self._update_hls_config_http_info(request)
        return self._call_api(**http_info)

    def update_hls_config_invoker(self, request):
        http_info = self._update_hls_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_hls_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain/hls",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHlsConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_ip_auth_list(self, request):
        r"""修改IP黑/白名单

        修改推流/播放域名的IP黑/白名单，当前仅支持ipv4。
        - 黑名单模式：禁止指定的IP或网段
        - 白名单模式：仅允许指定的IP或网段
        - 默认：全放通。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIpAuthList
        :type request: :class:`huaweicloudsdklive.v1.UpdateIpAuthListRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateIpAuthListResponse`
        """
        http_info = self._update_ip_auth_list_http_info(request)
        return self._call_api(**http_info)

    def update_ip_auth_list_invoker(self, request):
        http_info = self._update_ip_auth_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ip_auth_list_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/guard/ip",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIpAuthListResponse"
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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def update_publish_template(self, request):
        r"""新增、覆盖直播推流通知配置

        新增、覆盖直播推流通知配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePublishTemplate
        :type request: :class:`huaweicloudsdklive.v1.UpdatePublishTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdatePublishTemplateResponse`
        """
        http_info = self._update_publish_template_http_info(request)
        return self._call_api(**http_info)

    def update_publish_template_invoker(self, request):
        http_info = self._update_publish_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_publish_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/notifications/publish",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublishTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def update_pull_sources_config(self, request):
        r"""修改直播拉流回源配置

        修改直播拉流回源配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePullSourcesConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdatePullSourcesConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdatePullSourcesConfigResponse`
        """
        http_info = self._update_pull_sources_config_http_info(request)
        return self._call_api(**http_info)

    def update_pull_sources_config_invoker(self, request):
        http_info = self._update_pull_sources_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_pull_sources_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain/pull-sources",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePullSourcesConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_record_callback_config(self, request):
        r"""修改录制回调配置

        修改录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateRecordCallbackConfigResponse`
        """
        http_info = self._update_record_callback_config_http_info(request)
        return self._call_api(**http_info)

    def update_record_callback_config_invoker(self, request):
        http_info = self._update_record_callback_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_record_callback_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/record/callbacks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordCallbackConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json; charset=UTF-8'])

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

    def update_record_rule(self, request):
        r"""修改录制规则

        修改录制规则接口，如果规则修改后，修改后的规则对正在录制的流无效，对新的流有效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordRule
        :type request: :class:`huaweicloudsdklive.v1.UpdateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateRecordRuleResponse`
        """
        http_info = self._update_record_rule_http_info(request)
        return self._call_api(**http_info)

    def update_record_rule_invoker(self, request):
        http_info = self._update_record_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_record_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/record/rules/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json; charset=UTF-8'])

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

    def update_snapshot_config(self, request):
        r"""修改直播截图配置

        修改直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateSnapshotConfigResponse`
        """
        http_info = self._update_snapshot_config_http_info(request)
        return self._call_api(**http_info)

    def update_snapshot_config_invoker(self, request):
        http_info = self._update_snapshot_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_snapshot_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/stream/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSnapshotConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_stream_forbidden(self, request):
        r"""修改禁推属性

        修改禁推属性
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.UpdateStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateStreamForbiddenResponse`
        """
        http_info = self._update_stream_forbidden_http_info(request)
        return self._call_api(**http_info)

    def update_stream_forbidden_invoker(self, request):
        http_info = self._update_stream_forbidden_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_stream_forbidden_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/stream/blocks",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStreamForbiddenResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_transcodings_template(self, request):
        r"""配置直播转码模板

        修改直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.UpdateTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateTranscodingsTemplateResponse`
        """
        http_info = self._update_transcodings_template_http_info(request)
        return self._call_api(**http_info)

    def update_transcodings_template_invoker(self, request):
        http_info = self._update_transcodings_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_transcodings_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTranscodingsTemplateResponse"
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
            ['application/json; charset=UTF-8'])

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

    def list_ces_dims_info(self, request):
        r"""维度配置信息查询

        新增维度配置信息查询API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCesDimsInfo
        :type request: :class:`huaweicloudsdklive.v1.ListCesDimsInfoRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListCesDimsInfoResponse`
        """
        http_info = self._list_ces_dims_info_http_info(request)
        return self._call_api(**http_info)

    def list_ces_dims_info_invoker(self, request):
        http_info = self._list_ces_dims_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ces_dims_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ott/dims-info",
            "request_type": request.__class__.__name__,
            "response_type": "ListCesDimsInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

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

    def list_ces_instance(self, request):
        r"""实例查询

        新增实例查询API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCesInstance
        :type request: :class:`huaweicloudsdklive.v1.ListCesInstanceRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListCesInstanceResponse`
        """
        http_info = self._list_ces_instance_http_info(request)
        return self._call_api(**http_info)

    def list_ces_instance_invoker(self, request):
        http_info = self._list_ces_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ces_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ott/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListCesInstanceResponse"
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
            ['application/json; charset=UTF-8'])

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

    def delete_domain_https_cert(self, request):
        r"""删除指定域名的https证书配置

        删除指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainHttpsCertResponse`
        """
        http_info = self._delete_domain_https_cert_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_https_cert_invoker(self, request):
        http_info = self._delete_domain_https_cert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_domain_https_cert_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/guard/https-cert",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainHttpsCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def show_domain_https_cert(self, request):
        r"""查询指定域名的https证书配置

        查询指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainHttpsCertResponse`
        """
        http_info = self._show_domain_https_cert_http_info(request)
        return self._call_api(**http_info)

    def show_domain_https_cert_invoker(self, request):
        http_info = self._show_domain_https_cert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_https_cert_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/guard/https-cert",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainHttpsCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def update_domain_https_cert(self, request):
        r"""修改指定域名的https证书配置

        修改指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainHttpsCertResponse`
        """
        http_info = self._update_domain_https_cert_http_info(request)
        return self._call_api(**http_info)

    def update_domain_https_cert_invoker(self, request):
        http_info = self._update_domain_https_cert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_https_cert_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/guard/https-cert",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainHttpsCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def create_harvest_task(self, request):
        r"""创建Live2VOD任务

        创建Live2VOD任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHarvestTask
        :type request: :class:`huaweicloudsdklive.v1.CreateHarvestTaskRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateHarvestTaskResponse`
        """
        http_info = self._create_harvest_task_http_info(request)
        return self._call_api(**http_info)

    def create_harvest_task_invoker(self, request):
        http_info = self._create_harvest_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_harvest_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ott/harvest/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHarvestTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def delete_harvest_task(self, request):
        r"""删除Live2VOD任务

        删除Live2VOD任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHarvestTask
        :type request: :class:`huaweicloudsdklive.v1.DeleteHarvestTaskRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteHarvestTaskResponse`
        """
        http_info = self._delete_harvest_task_http_info(request)
        return self._call_api(**http_info)

    def delete_harvest_task_invoker(self, request):
        http_info = self._delete_harvest_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_harvest_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/ott/harvest/task",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHarvestTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

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

    def list_harvest_task(self, request):
        r"""查询Live2VOD任务

        查询Live2VOD任务，支持批量查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHarvestTask
        :type request: :class:`huaweicloudsdklive.v1.ListHarvestTaskRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListHarvestTaskResponse`
        """
        http_info = self._list_harvest_task_http_info(request)
        return self._call_api(**http_info)

    def list_harvest_task_invoker(self, request):
        http_info = self._list_harvest_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_harvest_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ott/harvest/task",
            "request_type": request.__class__.__name__,
            "response_type": "ListHarvestTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

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

    def modify_harvest_task(self, request):
        r"""修改Live2VOD任务

        修改Live2VOD任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyHarvestTask
        :type request: :class:`huaweicloudsdklive.v1.ModifyHarvestTaskRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyHarvestTaskResponse`
        """
        http_info = self._modify_harvest_task_http_info(request)
        return self._call_api(**http_info)

    def modify_harvest_task_invoker(self, request):
        http_info = self._modify_harvest_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_harvest_task_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ott/harvest/task",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyHarvestTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def update_harvest_job_status(self, request):
        r"""修改Live2VOD任务状态

        修改Live2VOD任务状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHarvestJobStatus
        :type request: :class:`huaweicloudsdklive.v1.UpdateHarvestJobStatusRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateHarvestJobStatusResponse`
        """
        http_info = self._update_harvest_job_status_http_info(request)
        return self._call_api(**http_info)

    def update_harvest_job_status_invoker(self, request):
        http_info = self._update_harvest_job_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_harvest_job_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ott/harvest/task/status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHarvestJobStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def update_obs_bucket_authority_public(self, request):
        r"""OBS桶授权及取消授权

        OBS桶授权及取消授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateObsBucketAuthorityPublic
        :type request: :class:`huaweicloudsdklive.v1.UpdateObsBucketAuthorityPublicRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateObsBucketAuthorityPublicResponse`
        """
        http_info = self._update_obs_bucket_authority_public_http_info(request)
        return self._call_api(**http_info)

    def update_obs_bucket_authority_public_invoker(self, request):
        http_info = self._update_obs_bucket_authority_public_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_obs_bucket_authority_public_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/obs/authority",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateObsBucketAuthorityPublicResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_ott_channel_info(self, request):
        r"""新建OTT频道

        创建频道接口，支持创建OTT频道。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOttChannelInfo
        :type request: :class:`huaweicloudsdklive.v1.CreateOttChannelInfoRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateOttChannelInfoResponse`
        """
        http_info = self._create_ott_channel_info_http_info(request)
        return self._call_api(**http_info)

    def create_ott_channel_info_invoker(self, request):
        http_info = self._create_ott_channel_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ott_channel_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ott/channels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOttChannelInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def delete_ott_channel_info(self, request):
        r"""删除频道信息

        删除频道信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOttChannelInfo
        :type request: :class:`huaweicloudsdklive.v1.DeleteOttChannelInfoRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteOttChannelInfoResponse`
        """
        http_info = self._delete_ott_channel_info_http_info(request)
        return self._call_api(**http_info)

    def delete_ott_channel_info_invoker(self, request):
        http_info = self._delete_ott_channel_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ott_channel_info_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/ott/channels",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOttChannelInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

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

    def list_ott_channel_info(self, request):
        r"""查询频道信息

        查询频道信息，支持批量查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOttChannelInfo
        :type request: :class:`huaweicloudsdklive.v1.ListOttChannelInfoRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListOttChannelInfoResponse`
        """
        http_info = self._list_ott_channel_info_http_info(request)
        return self._call_api(**http_info)

    def list_ott_channel_info_invoker(self, request):
        http_info = self._list_ott_channel_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ott_channel_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ott/channels",
            "request_type": request.__class__.__name__,
            "response_type": "ListOttChannelInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

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

    def modify_ott_channel_info_encoder_settings(self, request):
        r"""修改频道转码模板信息

        修改频道转码模板信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyOttChannelInfoEncoderSettings
        :type request: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoEncoderSettingsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoEncoderSettingsResponse`
        """
        http_info = self._modify_ott_channel_info_encoder_settings_http_info(request)
        return self._call_api(**http_info)

    def modify_ott_channel_info_encoder_settings_invoker(self, request):
        http_info = self._modify_ott_channel_info_encoder_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_ott_channel_info_encoder_settings_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ott/channels/encorder-settings",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyOttChannelInfoEncoderSettingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def modify_ott_channel_info_end_points(self, request):
        r"""修改频道打包信息

        修改频道打包信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyOttChannelInfoEndPoints
        :type request: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoEndPointsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoEndPointsResponse`
        """
        http_info = self._modify_ott_channel_info_end_points_http_info(request)
        return self._call_api(**http_info)

    def modify_ott_channel_info_end_points_invoker(self, request):
        http_info = self._modify_ott_channel_info_end_points_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_ott_channel_info_end_points_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ott/channels/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyOttChannelInfoEndPointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def modify_ott_channel_info_general(self, request):
        r"""修改频道通用信息

        修改频道通用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyOttChannelInfoGeneral
        :type request: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoGeneralRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoGeneralResponse`
        """
        http_info = self._modify_ott_channel_info_general_http_info(request)
        return self._call_api(**http_info)

    def modify_ott_channel_info_general_invoker(self, request):
        http_info = self._modify_ott_channel_info_general_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_ott_channel_info_general_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ott/channels/general",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyOttChannelInfoGeneralResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def modify_ott_channel_info_input(self, request):
        r"""修改频道入流信息

        修改频道入流信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyOttChannelInfoInput
        :type request: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoInputRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoInputResponse`
        """
        http_info = self._modify_ott_channel_info_input_http_info(request)
        return self._call_api(**http_info)

    def modify_ott_channel_info_input_invoker(self, request):
        http_info = self._modify_ott_channel_info_input_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_ott_channel_info_input_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ott/channels/input",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyOttChannelInfoInputResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def modify_ott_channel_info_record_settings(self, request):
        r"""修改频道录制信息

        修改频道录制信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyOttChannelInfoRecordSettings
        :type request: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoRecordSettingsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoRecordSettingsResponse`
        """
        http_info = self._modify_ott_channel_info_record_settings_http_info(request)
        return self._call_api(**http_info)

    def modify_ott_channel_info_record_settings_invoker(self, request):
        http_info = self._modify_ott_channel_info_record_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_ott_channel_info_record_settings_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ott/channels/record-settings",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyOttChannelInfoRecordSettingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def modify_ott_channel_info_stats(self, request):
        r"""修改频道状态

        修改频道状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyOttChannelInfoStats
        :type request: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoStatsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ModifyOttChannelInfoStatsResponse`
        """
        http_info = self._modify_ott_channel_info_stats_http_info(request)
        return self._call_api(**http_info)

    def modify_ott_channel_info_stats_invoker(self, request):
        http_info = self._modify_ott_channel_info_stats_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_ott_channel_info_stats_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ott/channels/state",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyOttChannelInfoStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def show_channel_statistic(self, request):
        r"""查询频道统计信息

        查询频道的统计信息（入流scte35信号）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowChannelStatistic
        :type request: :class:`huaweicloudsdklive.v1.ShowChannelStatisticRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowChannelStatisticResponse`
        """
        http_info = self._show_channel_statistic_http_info(request)
        return self._call_api(**http_info)

    def show_channel_statistic_invoker(self, request):
        http_info = self._show_channel_statistic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_channel_statistic_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ott/channels/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ShowChannelStatisticResponse"
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
        if 'access_control_allow_internal' in local_var_params:
            header_params['Access-Control-Allow-Internal'] = local_var_params['access_control_allow_internal']
        if 'access_control_allow_external' in local_var_params:
            header_params['Access-Control-Allow-External'] = local_var_params['access_control_allow_external']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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
