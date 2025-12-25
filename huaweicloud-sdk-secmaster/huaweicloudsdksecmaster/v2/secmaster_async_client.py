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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksecmaster'")


class SecMasterAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdksecmaster.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SecMasterAsyncClient":
                raise TypeError("client type error, support client type is SecMasterAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_adhoc_query_async(self, request):
        r"""创建adhoc查询

        创建adhoc查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAdhocQuery
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAdhocQueryRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAdhocQueryResponse`
        """
        http_info = self._create_adhoc_query_http_info(request)
        return self._call_api(**http_info)

    def create_adhoc_query_async_invoker(self, request):
        http_info = self._create_adhoc_query_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_adhoc_query_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/ad-hoc-queries",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAdhocQueryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_alert_rule_async(self, request):
        r"""创建告警规则

        创建告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleResponse`
        """
        http_info = self._create_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def create_alert_rule_async_invoker(self, request):
        http_info = self._create_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_alert_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_analysis_script_async(self, request):
        r"""创建分析脚本

        创建分析脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAnalysisScript
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAnalysisScriptRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAnalysisScriptResponse`
        """
        http_info = self._create_analysis_script_http_info(request)
        return self._call_api(**http_info)

    def create_analysis_script_async_invoker(self, request):
        http_info = self._create_analysis_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_analysis_script_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/analysis-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAnalysisScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_code_segment_async(self, request):
        r"""创建代码片段

        创建代码片段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCodeSegment
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateCodeSegmentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateCodeSegmentResponse`
        """
        http_info = self._create_code_segment_http_info(request)
        return self._call_api(**http_info)

    def create_code_segment_async_invoker(self, request):
        http_info = self._create_code_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_code_segment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/code-segments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCodeSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_customized_checkitem_async(self, request):
        r"""新增自定义检查项

        新增自定义检查项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomizedCheckitem
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateCustomizedCheckitemRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateCustomizedCheckitemResponse`
        """
        http_info = self._create_customized_checkitem_http_info(request)
        return self._call_api(**http_info)

    def create_customized_checkitem_async_invoker(self, request):
        http_info = self._create_customized_checkitem_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_customized_checkitem_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/checkitems",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomizedCheckitemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
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

    def create_customized_compliance_package_async(self, request):
        r"""新增自定义遵从包

        新增自定义遵从包
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomizedCompliancePackage
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateCustomizedCompliancePackageRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateCustomizedCompliancePackageResponse`
        """
        http_info = self._create_customized_compliance_package_http_info(request)
        return self._call_api(**http_info)

    def create_customized_compliance_package_async_invoker(self, request):
        http_info = self._create_customized_compliance_package_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_customized_compliance_package_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/compliance-packages",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomizedCompliancePackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
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

    def create_data_transformation_async(self, request):
        r"""创建数据加工

        创建数据加工
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDataTransformation
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateDataTransformationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateDataTransformationResponse`
        """
        http_info = self._create_data_transformation_http_info(request)
        return self._call_api(**http_info)

    def create_data_transformation_async_invoker(self, request):
        http_info = self._create_data_transformation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_data_transformation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/data-transformations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataTransformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_layout_field_async(self, request):
        r"""创建布局字段

        创建布局字段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLayoutField
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateLayoutFieldRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateLayoutFieldResponse`
        """
        http_info = self._create_layout_field_http_info(request)
        return self._call_api(**http_info)

    def create_layout_field_async_invoker(self, request):
        http_info = self._create_layout_field_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_layout_field_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/soc/layouts/fields",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLayoutFieldResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_pipe_async(self, request):
        r"""创建管道

        创建管道
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePipe
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePipeResponse`
        """
        http_info = self._create_pipe_http_info(request)
        return self._call_api(**http_info)

    def create_pipe_async_invoker(self, request):
        http_info = self._create_pipe_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pipe_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/pipes",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePipeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_retrieve_script_async(self, request):
        r"""创建检索脚本

        创建检索脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRetrieveScript
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateRetrieveScriptRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateRetrieveScriptResponse`
        """
        http_info = self._create_retrieve_script_http_info(request)
        return self._call_api(**http_info)

    def create_retrieve_script_async_invoker(self, request):
        http_info = self._create_retrieve_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_retrieve_script_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/retrieve-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRetrieveScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_table_async(self, request):
        r"""创建表

        创建表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTable
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateTableRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateTableResponse`
        """
        http_info = self._create_table_http_info(request)
        return self._call_api(**http_info)

    def create_table_async_invoker(self, request):
        http_info = self._create_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_table_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def create_table_analysis_async(self, request):
        r"""创建安全分析查询

        创建安全分析查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTableAnalysis
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateTableAnalysisRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateTableAnalysisResponse`
        """
        http_info = self._create_table_analysis_http_info(request)
        return self._call_api(**http_info)

    def create_table_analysis_async_invoker(self, request):
        http_info = self._create_table_analysis_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_table_analysis_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}/analysis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTableAnalysisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def delete_adhoc_query_async(self, request):
        r"""关闭查询操作

        关闭查询操作
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAdhocQuery
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteAdhocQueryRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteAdhocQueryResponse`
        """
        http_info = self._delete_adhoc_query_http_info(request)
        return self._call_api(**http_info)

    def delete_adhoc_query_async_invoker(self, request):
        http_info = self._delete_adhoc_query_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_adhoc_query_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/ad-hoc-queries/{query_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAdhocQueryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

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

    def delete_alert_rule_async(self, request):
        r"""删除告警规则

        删除告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteAlertRuleResponse`
        """
        http_info = self._delete_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_alert_rule_async_invoker(self, request):
        http_info = self._delete_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_alert_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{alert_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_rule_id' in local_var_params:
            path_params['alert_rule_id'] = local_var_params['alert_rule_id']

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

    def delete_analysis_script_async(self, request):
        r"""删除分析脚本

        删除分析脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAnalysisScript
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteAnalysisScriptRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteAnalysisScriptResponse`
        """
        http_info = self._delete_analysis_script_http_info(request)
        return self._call_api(**http_info)

    def delete_analysis_script_async_invoker(self, request):
        http_info = self._delete_analysis_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_analysis_script_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/analysis-scripts/{analysis_script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAnalysisScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'analysis_script_id' in local_var_params:
            path_params['analysis_script_id'] = local_var_params['analysis_script_id']

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

    def delete_code_segment_async(self, request):
        r"""删除代码片段

        删除代码片段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCodeSegment
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteCodeSegmentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteCodeSegmentResponse`
        """
        http_info = self._delete_code_segment_http_info(request)
        return self._call_api(**http_info)

    def delete_code_segment_async_invoker(self, request):
        http_info = self._delete_code_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_code_segment_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/code-segments/{code_segment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCodeSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'code_segment_id' in local_var_params:
            path_params['code_segment_id'] = local_var_params['code_segment_id']

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

    def delete_customized_checkitems_async(self, request):
        r"""删除自定义检查项

        删除自定义检查项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomizedCheckitems
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteCustomizedCheckitemsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteCustomizedCheckitemsResponse`
        """
        http_info = self._delete_customized_checkitems_http_info(request)
        return self._call_api(**http_info)

    def delete_customized_checkitems_async_invoker(self, request):
        http_info = self._delete_customized_checkitems_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_customized_checkitems_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/checkitems",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomizedCheckitemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
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

    def delete_customized_compliance_packages_async(self, request):
        r"""删除自定义遵从包

        删除自定义遵从包
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomizedCompliancePackages
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteCustomizedCompliancePackagesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteCustomizedCompliancePackagesResponse`
        """
        http_info = self._delete_customized_compliance_packages_http_info(request)
        return self._call_api(**http_info)

    def delete_customized_compliance_packages_async_invoker(self, request):
        http_info = self._delete_customized_compliance_packages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_customized_compliance_packages_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/compliance-packages",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomizedCompliancePackagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
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

    def delete_data_transformation_async(self, request):
        r"""删除数据加工

        删除数据加工
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDataTransformation
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteDataTransformationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteDataTransformationResponse`
        """
        http_info = self._delete_data_transformation_http_info(request)
        return self._call_api(**http_info)

    def delete_data_transformation_async_invoker(self, request):
        http_info = self._delete_data_transformation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_data_transformation_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/data-transformations/{data_transformation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataTransformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'data_transformation_id' in local_var_params:
            path_params['data_transformation_id'] = local_var_params['data_transformation_id']

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

    def delete_layout_field_async(self, request):
        r"""批量删除布局字段

        删除布局字段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLayoutField
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteLayoutFieldRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteLayoutFieldResponse`
        """
        http_info = self._delete_layout_field_http_info(request)
        return self._call_api(**http_info)

    def delete_layout_field_async_invoker(self, request):
        http_info = self._delete_layout_field_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_layout_field_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/soc/layouts/fields",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLayoutFieldResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def delete_pipe_async(self, request):
        r"""删除管道

        删除管道
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePipe
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePipeResponse`
        """
        http_info = self._delete_pipe_http_info(request)
        return self._call_api(**http_info)

    def delete_pipe_async_invoker(self, request):
        http_info = self._delete_pipe_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_pipe_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePipeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def delete_retrieve_script_async(self, request):
        r"""删除检索脚本

        删除检索脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRetrieveScript
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteRetrieveScriptRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteRetrieveScriptResponse`
        """
        http_info = self._delete_retrieve_script_http_info(request)
        return self._call_api(**http_info)

    def delete_retrieve_script_async_invoker(self, request):
        http_info = self._delete_retrieve_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_retrieve_script_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/retrieve-scripts/{retrieve_script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRetrieveScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'retrieve_script_id' in local_var_params:
            path_params['retrieve_script_id'] = local_var_params['retrieve_script_id']

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

    def delete_table_async(self, request):
        r"""删除表

        删除表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTable
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteTableRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteTableResponse`
        """
        http_info = self._delete_table_http_info(request)
        return self._call_api(**http_info)

    def delete_table_async_invoker(self, request):
        http_info = self._delete_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_table_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def disable_alert_rule_async(self, request):
        r"""停用告警规则

        停用告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.DisableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DisableAlertRuleResponse`
        """
        http_info = self._disable_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def disable_alert_rule_async_invoker(self, request):
        http_info = self._disable_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_alert_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{alert_rule_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_rule_id' in local_var_params:
            path_params['alert_rule_id'] = local_var_params['alert_rule_id']

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

    def disable_data_consumption_async(self, request):
        r"""关闭实时消费

        关闭实时消费
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableDataConsumption
        :type request: :class:`huaweicloudsdksecmaster.v2.DisableDataConsumptionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DisableDataConsumptionResponse`
        """
        http_info = self._disable_data_consumption_http_info(request)
        return self._call_api(**http_info)

    def disable_data_consumption_async_invoker(self, request):
        http_info = self._disable_data_consumption_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_data_consumption_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}/consumption",
            "request_type": request.__class__.__name__,
            "response_type": "DisableDataConsumptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def disable_data_transformation_async(self, request):
        r"""停用数据加工

        停用数据加工
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableDataTransformation
        :type request: :class:`huaweicloudsdksecmaster.v2.DisableDataTransformationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DisableDataTransformationResponse`
        """
        http_info = self._disable_data_transformation_http_info(request)
        return self._call_api(**http_info)

    def disable_data_transformation_async_invoker(self, request):
        http_info = self._disable_data_transformation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_data_transformation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/data-transformations/{data_transformation_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableDataTransformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'data_transformation_id' in local_var_params:
            path_params['data_transformation_id'] = local_var_params['data_transformation_id']

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

    def enable_alert_rule_async(self, request):
        r"""启用告警规则

        启用告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.EnableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.EnableAlertRuleResponse`
        """
        http_info = self._enable_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def enable_alert_rule_async_invoker(self, request):
        http_info = self._enable_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_alert_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{alert_rule_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_rule_id' in local_var_params:
            path_params['alert_rule_id'] = local_var_params['alert_rule_id']

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

    def enable_data_consumption_async(self, request):
        r"""开启实时消费

        开启实时消费
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDataConsumption
        :type request: :class:`huaweicloudsdksecmaster.v2.EnableDataConsumptionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.EnableDataConsumptionResponse`
        """
        http_info = self._enable_data_consumption_http_info(request)
        return self._call_api(**http_info)

    def enable_data_consumption_async_invoker(self, request):
        http_info = self._enable_data_consumption_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_data_consumption_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}/consumption",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDataConsumptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def enable_data_transformation_async(self, request):
        r"""启用数据加工

        启用数据加工
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDataTransformation
        :type request: :class:`huaweicloudsdksecmaster.v2.EnableDataTransformationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.EnableDataTransformationResponse`
        """
        http_info = self._enable_data_transformation_http_info(request)
        return self._call_api(**http_info)

    def enable_data_transformation_async_invoker(self, request):
        http_info = self._enable_data_transformation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_data_transformation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/data-transformations/{data_transformation_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDataTransformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'data_transformation_id' in local_var_params:
            path_params['data_transformation_id'] = local_var_params['data_transformation_id']

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

    def list_alert_rule_metrics_async(self, request):
        r"""告警规则总览

        告警规则总览
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRuleMetrics
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleMetricsResponse`
        """
        http_info = self._list_alert_rule_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rule_metrics_async_invoker(self, request):
        http_info = self._list_alert_rule_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alert_rule_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRuleMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def list_alert_rule_template_metrics_async(self, request):
        r"""列出告警规则模板总览

        列出告警规则模板总览
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRuleTemplateMetrics
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplateMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplateMetricsResponse`
        """
        http_info = self._list_alert_rule_template_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rule_template_metrics_async_invoker(self, request):
        http_info = self._list_alert_rule_template_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alert_rule_template_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRuleTemplateMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def list_alert_rule_templates_async(self, request):
        r"""列出告警规则模板

        列出告警规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRuleTemplates
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplatesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplatesResponse`
        """
        http_info = self._list_alert_rule_templates_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rule_templates_async_invoker(self, request):
        http_info = self._list_alert_rule_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alert_rule_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRuleTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'template_name' in local_var_params:
            query_params.append(('template_name', local_var_params['template_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
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

    def list_alert_rules_async(self, request):
        r"""列出告警规则

        列出告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRules
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRulesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRulesResponse`
        """
        http_info = self._list_alert_rules_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rules_async_invoker(self, request):
        http_info = self._list_alert_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alert_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'output_table_id' in local_var_params:
            query_params.append(('output_table_id', local_var_params['output_table_id']))
        if 'alert_rule_name' in local_var_params:
            query_params.append(('alert_rule_name', local_var_params['alert_rule_name']))
        if 'alert_rule_id' in local_var_params:
            query_params.append(('alert_rule_id', local_var_params['alert_rule_id']))

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

    def list_analysis_scripts_async(self, request):
        r"""列出分析脚本

        列出分析脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAnalysisScripts
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAnalysisScriptsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAnalysisScriptsResponse`
        """
        http_info = self._list_analysis_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_analysis_scripts_async_invoker(self, request):
        http_info = self._list_analysis_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_analysis_scripts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/analysis-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAnalysisScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
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

    def list_code_segments_async(self, request):
        r"""列出代码片段

        列出代码片段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCodeSegments
        :type request: :class:`huaweicloudsdksecmaster.v2.ListCodeSegmentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListCodeSegmentsResponse`
        """
        http_info = self._list_code_segments_http_info(request)
        return self._call_api(**http_info)

    def list_code_segments_async_invoker(self, request):
        http_info = self._list_code_segments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_code_segments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/code-segments",
            "request_type": request.__class__.__name__,
            "response_type": "ListCodeSegmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'code_segment_id' in local_var_params:
            query_params.append(('code_segment_id', local_var_params['code_segment_id']))
        if 'code_segment_name' in local_var_params:
            query_params.append(('code_segment_name', local_var_params['code_segment_name']))
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

    def list_data_transformation_metrics_async(self, request):
        r"""数据加工总览

        数据加工总览
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDataTransformationMetrics
        :type request: :class:`huaweicloudsdksecmaster.v2.ListDataTransformationMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListDataTransformationMetricsResponse`
        """
        http_info = self._list_data_transformation_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_data_transformation_metrics_async_invoker(self, request):
        http_info = self._list_data_transformation_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_data_transformation_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/data-transformations/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataTransformationMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def list_data_transformations_async(self, request):
        r"""列出数据加工

        列出数据加工
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDataTransformations
        :type request: :class:`huaweicloudsdksecmaster.v2.ListDataTransformationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListDataTransformationsResponse`
        """
        http_info = self._list_data_transformations_http_info(request)
        return self._call_api(**http_info)

    def list_data_transformations_async_invoker(self, request):
        http_info = self._list_data_transformations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_data_transformations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/data-transformations",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataTransformationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'output_table_id' in local_var_params:
            query_params.append(('output_table_id', local_var_params['output_table_id']))
        if 'data_transformation_name' in local_var_params:
            query_params.append(('data_transformation_name', local_var_params['data_transformation_name']))
        if 'data_transformation_id' in local_var_params:
            query_params.append(('data_transformation_id', local_var_params['data_transformation_id']))
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

    def list_directories_async(self, request):
        r"""列出目录分组

        列出目录分组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDirectories
        :type request: :class:`huaweicloudsdksecmaster.v2.ListDirectoriesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListDirectoriesResponse`
        """
        http_info = self._list_directories_http_info(request)
        return self._call_api(**http_info)

    def list_directories_async_invoker(self, request):
        http_info = self._list_directories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_directories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/directories",
            "request_type": request.__class__.__name__,
            "response_type": "ListDirectoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def list_layout_field_all_async(self, request):
        r"""全部布局字段

        查询布局字段列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLayoutFieldAll
        :type request: :class:`huaweicloudsdksecmaster.v2.ListLayoutFieldAllRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListLayoutFieldAllResponse`
        """
        http_info = self._list_layout_field_all_http_info(request)
        return self._call_api(**http_info)

    def list_layout_field_all_async_invoker(self, request):
        http_info = self._list_layout_field_all_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_layout_field_all_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/soc/layouts/fields",
            "request_type": request.__class__.__name__,
            "response_type": "ListLayoutFieldAllResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'is_built_in' in local_var_params:
            query_params.append(('is_built_in', local_var_params['is_built_in']))
        if 'business_code' in local_var_params:
            query_params.append(('business_code', local_var_params['business_code']))
        if 'layout_id' in local_var_params:
            query_params.append(('layout_id', local_var_params['layout_id']))

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

    def list_pipes_async(self, request):
        r"""获取管道列表

        获取管道列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPipes
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPipesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPipesResponse`
        """
        http_info = self._list_pipes_http_info(request)
        return self._call_api(**http_info)

    def list_pipes_async_invoker(self, request):
        http_info = self._list_pipes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pipes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/pipes",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'pipe_name_in_query' in local_var_params:
            query_params.append(('pipe_name_in_query', local_var_params['pipe_name_in_query']))
        if 'pipe_id_in_query' in local_var_params:
            query_params.append(('pipe_id_in_query', local_var_params['pipe_id_in_query']))

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

    def list_retrieve_scripts_async(self, request):
        r"""列出检索脚本

        列出检索脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRetrieveScripts
        :type request: :class:`huaweicloudsdksecmaster.v2.ListRetrieveScriptsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListRetrieveScriptsResponse`
        """
        http_info = self._list_retrieve_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_retrieve_scripts_async_invoker(self, request):
        http_info = self._list_retrieve_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_retrieve_scripts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/retrieve-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListRetrieveScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'table_id' in local_var_params:
            query_params.append(('table_id', local_var_params['table_id']))
        if 'script_name' in local_var_params:
            query_params.append(('script_name', local_var_params['script_name']))
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

    def list_table_histograms_async(self, request):
        r"""检索表直方图

        检索表直方图
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTableHistograms
        :type request: :class:`huaweicloudsdksecmaster.v2.ListTableHistogramsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListTableHistogramsResponse`
        """
        http_info = self._list_table_histograms_http_info(request)
        return self._call_api(**http_info)

    def list_table_histograms_async_invoker(self, request):
        http_info = self._list_table_histograms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_table_histograms_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}/histograms",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableHistogramsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def list_table_logs_async(self, request):
        r"""检索表日志

        检索表日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTableLogs
        :type request: :class:`huaweicloudsdksecmaster.v2.ListTableLogsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListTableLogsResponse`
        """
        http_info = self._list_table_logs_http_info(request)
        return self._call_api(**http_info)

    def list_table_logs_async_invoker(self, request):
        http_info = self._list_table_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_table_logs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def list_tables_async(self, request):
        r"""获取表列表

        获取表列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTables
        :type request: :class:`huaweicloudsdksecmaster.v2.ListTablesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListTablesResponse`
        """
        http_info = self._list_tables_http_info(request)
        return self._call_api(**http_info)

    def list_tables_async_invoker(self, request):
        http_info = self._list_tables_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tables_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'table_id' in local_var_params:
            query_params.append(('table_id', local_var_params['table_id']))
        if 'table_alias' in local_var_params:
            query_params.append(('table_alias', local_var_params['table_alias']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'exists' in local_var_params:
            query_params.append(('exists', local_var_params['exists']))

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

    def search_baseline_async(self, request):
        r"""搜索基线检查结果列表

        搜索基线检查结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchBaseline
        :type request: :class:`huaweicloudsdksecmaster.v2.SearchBaselineRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.SearchBaselineResponse`
        """
        http_info = self._search_baseline_http_info(request)
        return self._call_api(**http_info)

    def search_baseline_async_invoker(self, request):
        http_info = self._search_baseline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_baseline_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchBaselineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
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

    def search_checkitems_async(self, request):
        r"""查询检查项列表

        查询检查项列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchCheckitems
        :type request: :class:`huaweicloudsdksecmaster.v2.SearchCheckitemsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.SearchCheckitemsResponse`
        """
        http_info = self._search_checkitems_http_info(request)
        return self._call_api(**http_info)

    def search_checkitems_async_invoker(self, request):
        http_info = self._search_checkitems_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_checkitems_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/checkitems/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCheckitemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
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

    def search_compliance_packages_async(self, request):
        r"""查询遵从包列表

        查询遵从包列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchCompliancePackages
        :type request: :class:`huaweicloudsdksecmaster.v2.SearchCompliancePackagesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.SearchCompliancePackagesResponse`
        """
        http_info = self._search_compliance_packages_http_info(request)
        return self._call_api(**http_info)

    def search_compliance_packages_async_invoker(self, request):
        http_info = self._search_compliance_packages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_compliance_packages_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/compliance-packages/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCompliancePackagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
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

    def show_adhoc_result_async(self, request):
        r"""获取adhoc查询结果

        获取adhoc查询结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAdhocResult
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAdhocResultRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAdhocResultResponse`
        """
        http_info = self._show_adhoc_result_http_info(request)
        return self._call_api(**http_info)

    def show_adhoc_result_async_invoker(self, request):
        http_info = self._show_adhoc_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_adhoc_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/ad-hoc-queries/{query_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAdhocResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

        query_params = []
        if 'batch' in local_var_params:
            query_params.append(('batch', local_var_params['batch']))

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

    def show_alert_rule_async(self, request):
        r"""查看告警规则

        查看告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleResponse`
        """
        http_info = self._show_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def show_alert_rule_async_invoker(self, request):
        http_info = self._show_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alert_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{alert_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_rule_id' in local_var_params:
            path_params['alert_rule_id'] = local_var_params['alert_rule_id']

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

    def show_alert_rule_template_async(self, request):
        r"""查看告警规则模板

        查看告警规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlertRuleTemplate
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleTemplateResponse`
        """
        http_info = self._show_alert_rule_template_http_info(request)
        return self._call_api(**http_info)

    def show_alert_rule_template_async_invoker(self, request):
        http_info = self._show_alert_rule_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alert_rule_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertRuleTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
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

    def show_analysis_script_async(self, request):
        r"""查看分析脚本

        查看分析脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAnalysisScript
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAnalysisScriptRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAnalysisScriptResponse`
        """
        http_info = self._show_analysis_script_http_info(request)
        return self._call_api(**http_info)

    def show_analysis_script_async_invoker(self, request):
        http_info = self._show_analysis_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_analysis_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/analysis-scripts/{analysis_script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAnalysisScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'analysis_script_id' in local_var_params:
            path_params['analysis_script_id'] = local_var_params['analysis_script_id']

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

    def show_checkitem_detail_async(self, request):
        r"""查询检查项详情

        查询检查项详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCheckitemDetail
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowCheckitemDetailRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowCheckitemDetailResponse`
        """
        http_info = self._show_checkitem_detail_http_info(request)
        return self._call_api(**http_info)

    def show_checkitem_detail_async_invoker(self, request):
        http_info = self._show_checkitem_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_checkitem_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/checkitems/{checkitem_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCheckitemDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'checkitem_id' in local_var_params:
            path_params['checkitem_id'] = local_var_params['checkitem_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_code_segment_async(self, request):
        r"""查看代码片段

        查看代码片段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCodeSegment
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowCodeSegmentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowCodeSegmentResponse`
        """
        http_info = self._show_code_segment_http_info(request)
        return self._call_api(**http_info)

    def show_code_segment_async_invoker(self, request):
        http_info = self._show_code_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_code_segment_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/code-segments/{code_segment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCodeSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'code_segment_id' in local_var_params:
            path_params['code_segment_id'] = local_var_params['code_segment_id']

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

    def show_compliance_package_detail_async(self, request):
        r"""查询遵从包详情

        查询遵从包详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCompliancePackageDetail
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowCompliancePackageDetailRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowCompliancePackageDetailResponse`
        """
        http_info = self._show_compliance_package_detail_http_info(request)
        return self._call_api(**http_info)

    def show_compliance_package_detail_async_invoker(self, request):
        http_info = self._show_compliance_package_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_compliance_package_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/compliance-packages/{compliance_packages_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCompliancePackageDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'compliance_packages_id' in local_var_params:
            path_params['compliance_packages_id'] = local_var_params['compliance_packages_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_data_consumption_async(self, request):
        r"""获取实时消费配置

        获取实时消费配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDataConsumption
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowDataConsumptionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowDataConsumptionResponse`
        """
        http_info = self._show_data_consumption_http_info(request)
        return self._call_api(**http_info)

    def show_data_consumption_async_invoker(self, request):
        http_info = self._show_data_consumption_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_data_consumption_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}/consumption",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataConsumptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def show_data_transformation_async(self, request):
        r"""查看数据加工

        查看数据加工
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDataTransformation
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowDataTransformationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowDataTransformationResponse`
        """
        http_info = self._show_data_transformation_http_info(request)
        return self._call_api(**http_info)

    def show_data_transformation_async_invoker(self, request):
        http_info = self._show_data_transformation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_data_transformation_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/data-transformations/{data_transformation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataTransformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'data_transformation_id' in local_var_params:
            path_params['data_transformation_id'] = local_var_params['data_transformation_id']

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

    def show_layout_field_info_async(self, request):
        r"""展示字段详情

        查询布局字段详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLayoutFieldInfo
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowLayoutFieldInfoRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowLayoutFieldInfoResponse`
        """
        http_info = self._show_layout_field_info_http_info(request)
        return self._call_api(**http_info)

    def show_layout_field_info_async_invoker(self, request):
        http_info = self._show_layout_field_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_layout_field_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/soc/layouts/fields/{field_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLayoutFieldInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'field_id' in local_var_params:
            path_params['field_id'] = local_var_params['field_id']

        query_params = []
        if 'layout_id' in local_var_params:
            query_params.append(('layout_id', local_var_params['layout_id']))

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

    def show_monitor_stats_async(self, request):
        r"""获取监控统计信息

        获取监控统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMonitorStats
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowMonitorStatsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowMonitorStatsResponse`
        """
        http_info = self._show_monitor_stats_http_info(request)
        return self._call_api(**http_info)

    def show_monitor_stats_async_invoker(self, request):
        http_info = self._show_monitor_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_monitor_stats_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMonitorStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def show_pipe_async(self, request):
        r"""获取管道详情

        获取管道详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPipe
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPipeResponse`
        """
        http_info = self._show_pipe_http_info(request)
        return self._call_api(**http_info)

    def show_pipe_async_invoker(self, request):
        http_info = self._show_pipe_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pipe_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def show_retrieve_script_async(self, request):
        r"""查看检索脚本

        查看检索脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRetrieveScript
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowRetrieveScriptRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowRetrieveScriptResponse`
        """
        http_info = self._show_retrieve_script_http_info(request)
        return self._call_api(**http_info)

    def show_retrieve_script_async_invoker(self, request):
        http_info = self._show_retrieve_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_retrieve_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/retrieve-scripts/{retrieve_script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRetrieveScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'retrieve_script_id' in local_var_params:
            path_params['retrieve_script_id'] = local_var_params['retrieve_script_id']

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

    def show_subscription_resources_async(self, request):
        r"""获取订阅资源信息

        获取订阅资源信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubscriptionResources
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowSubscriptionResourcesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowSubscriptionResourcesResponse`
        """
        http_info = self._show_subscription_resources_http_info(request)
        return self._call_api(**http_info)

    def show_subscription_resources_async_invoker(self, request):
        http_info = self._show_subscription_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_subscription_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/subscription/resource",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubscriptionResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'sku' in local_var_params:
            query_params.append(('sku', local_var_params['sku']))

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

    def show_table_async(self, request):
        r"""获取表详情

        获取表详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTable
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowTableRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowTableResponse`
        """
        http_info = self._show_table_http_info(request)
        return self._call_api(**http_info)

    def show_table_async_invoker(self, request):
        http_info = self._show_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_table_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def show_version_async(self, request):
        r"""获取当前可用版本

        获取当前可用版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowVersionResponse`
        """
        http_info = self._show_version_http_info(request)
        return self._call_api(**http_info)

    def show_version_async_invoker(self, request):
        http_info = self._show_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/siem/upgradation/version",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def update_alert_rule_async(self, request):
        r"""更新告警规则

        更新告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleResponse`
        """
        http_info = self._update_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def update_alert_rule_async_invoker(self, request):
        http_info = self._update_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_alert_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{alert_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_rule_id' in local_var_params:
            path_params['alert_rule_id'] = local_var_params['alert_rule_id']

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

    def update_analysis_script_async(self, request):
        r"""更新分析脚本

        更新分析脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAnalysisScript
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateAnalysisScriptRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateAnalysisScriptResponse`
        """
        http_info = self._update_analysis_script_http_info(request)
        return self._call_api(**http_info)

    def update_analysis_script_async_invoker(self, request):
        http_info = self._update_analysis_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_analysis_script_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/analysis-scripts/{analysis_script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAnalysisScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'analysis_script_id' in local_var_params:
            path_params['analysis_script_id'] = local_var_params['analysis_script_id']

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

    def update_checkitem_async(self, request):
        r"""更新检查项

        更新检查项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCheckitem
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateCheckitemRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateCheckitemResponse`
        """
        http_info = self._update_checkitem_http_info(request)
        return self._call_api(**http_info)

    def update_checkitem_async_invoker(self, request):
        http_info = self._update_checkitem_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_checkitem_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/checkitems/{checkitem_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCheckitemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'checkitem_id' in local_var_params:
            path_params['checkitem_id'] = local_var_params['checkitem_id']

        query_params = []

        header_params = {}
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

    def update_code_segment_async(self, request):
        r"""更新代码片段

        更新代码片段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCodeSegment
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateCodeSegmentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateCodeSegmentResponse`
        """
        http_info = self._update_code_segment_http_info(request)
        return self._call_api(**http_info)

    def update_code_segment_async_invoker(self, request):
        http_info = self._update_code_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_code_segment_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/code-segments/{code_segment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCodeSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'code_segment_id' in local_var_params:
            path_params['code_segment_id'] = local_var_params['code_segment_id']

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

    def update_compliance_package_async(self, request):
        r"""更新遵从包

        更新遵从包
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCompliancePackage
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateCompliancePackageRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateCompliancePackageResponse`
        """
        http_info = self._update_compliance_package_http_info(request)
        return self._call_api(**http_info)

    def update_compliance_package_async_invoker(self, request):
        http_info = self._update_compliance_package_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_compliance_package_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/sa/baseline/compliance-packages/{compliance_packages_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCompliancePackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'compliance_packages_id' in local_var_params:
            path_params['compliance_packages_id'] = local_var_params['compliance_packages_id']

        query_params = []

        header_params = {}
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

    def update_data_transformation_async(self, request):
        r"""更新数据加工

        更新数据加工
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDataTransformation
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateDataTransformationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateDataTransformationResponse`
        """
        http_info = self._update_data_transformation_http_info(request)
        return self._call_api(**http_info)

    def update_data_transformation_async_invoker(self, request):
        http_info = self._update_data_transformation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_data_transformation_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/data-transformations/{data_transformation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataTransformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'data_transformation_id' in local_var_params:
            path_params['data_transformation_id'] = local_var_params['data_transformation_id']

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

    def update_layout_field_async(self, request):
        r"""更新字段

        更新布局字段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLayoutField
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateLayoutFieldRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateLayoutFieldResponse`
        """
        http_info = self._update_layout_field_http_info(request)
        return self._call_api(**http_info)

    def update_layout_field_async_invoker(self, request):
        http_info = self._update_layout_field_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_layout_field_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/soc/layouts/fields/{field_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLayoutFieldResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'field_id' in local_var_params:
            path_params['field_id'] = local_var_params['field_id']

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

    def update_pipe_async(self, request):
        r"""更新管道

        更新管道
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePipe
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePipeResponse`
        """
        http_info = self._update_pipe_http_info(request)
        return self._call_api(**http_info)

    def update_pipe_async_invoker(self, request):
        http_info = self._update_pipe_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_pipe_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePipeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def update_pipe_schema_async(self, request):
        r"""更新管道结构

        更新管道结构
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePipeSchema
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePipeSchemaRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePipeSchemaResponse`
        """
        http_info = self._update_pipe_schema_http_info(request)
        return self._call_api(**http_info)

    def update_pipe_schema_async_invoker(self, request):
        http_info = self._update_pipe_schema_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_pipe_schema_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}/schema",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePipeSchemaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def update_retrieve_script_async(self, request):
        r"""更新检索脚本

        更新检索脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRetrieveScript
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateRetrieveScriptRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateRetrieveScriptResponse`
        """
        http_info = self._update_retrieve_script_http_info(request)
        return self._call_api(**http_info)

    def update_retrieve_script_async_invoker(self, request):
        http_info = self._update_retrieve_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_retrieve_script_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/retrieve-scripts/{retrieve_script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRetrieveScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'retrieve_script_id' in local_var_params:
            path_params['retrieve_script_id'] = local_var_params['retrieve_script_id']

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

    def update_table_async(self, request):
        r"""更改表详情

        更改表详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTable
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateTableRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateTableResponse`
        """
        http_info = self._update_table_http_info(request)
        return self._call_api(**http_info)

    def update_table_async_invoker(self, request):
        http_info = self._update_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_table_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def update_table_schema_async(self, request):
        r"""更改表结构

        更改表结构
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTableSchema
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateTableSchemaRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateTableSchemaResponse`
        """
        http_info = self._update_table_schema_http_info(request)
        return self._call_api(**http_info)

    def update_table_schema_async_invoker(self, request):
        http_info = self._update_table_schema_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_table_schema_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/tables/{table_id}/schema",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTableSchemaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def create_sql_validation_async(self, request):
        r"""创建SQL校验

        创建SQL校验
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSqlValidation
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateSqlValidationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateSqlValidationResponse`
        """
        http_info = self._create_sql_validation_http_info(request)
        return self._call_api(**http_info)

    def create_sql_validation_async_invoker(self, request):
        http_info = self._create_sql_validation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sql_validation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workspaces/{workspace_id}/siem/sql/validation",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSqlValidationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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
