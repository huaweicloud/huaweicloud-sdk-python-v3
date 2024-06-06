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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkiamaccessanalyzer'")


class IAMAccessAnalyzerAsyncClient(Client):
    def __init__(self):
        super(IAMAccessAnalyzerAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiamaccessanalyzer.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "IAMAccessAnalyzerAsyncClient":
                raise TypeError("client type error, support client type is IAMAccessAnalyzerAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_analyzer_async(self, request):
        """创建分析器

        为您的账号或者组织创建分析器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAnalyzer
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.CreateAnalyzerRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.CreateAnalyzerResponse`
        """
        http_info = self._create_analyzer_http_info(request)
        return self._call_api(**http_info)

    def create_analyzer_async_invoker(self, request):
        http_info = self._create_analyzer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_analyzer_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/analyzers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAnalyzerResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_analyzer_async(self, request):
        """删除指定的分析器

        删除指定的分析器。分析器生成的所有检查结果都将被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAnalyzer
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.DeleteAnalyzerRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.DeleteAnalyzerResponse`
        """
        http_info = self._delete_analyzer_http_info(request)
        return self._call_api(**http_info)

    def delete_analyzer_async_invoker(self, request):
        http_info = self._delete_analyzer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_analyzer_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/analyzers/{analyzer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAnalyzerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_analyzers_async(self, request):
        """检索分析器的列表

        检索分析器的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAnalyzers
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListAnalyzersRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListAnalyzersResponse`
        """
        http_info = self._list_analyzers_http_info(request)
        return self._call_api(**http_info)

    def list_analyzers_async_invoker(self, request):
        http_info = self._list_analyzers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_analyzers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/analyzers",
            "request_type": request.__class__.__name__,
            "response_type": "ListAnalyzersResponse"
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
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_analyzer_async(self, request):
        """显示指定的分析器

        检索有关指定分析器的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAnalyzer
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ShowAnalyzerRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ShowAnalyzerResponse`
        """
        http_info = self._show_analyzer_http_info(request)
        return self._call_api(**http_info)

    def show_analyzer_async_invoker(self, request):
        http_info = self._show_analyzer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_analyzer_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/analyzers/{analyzer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAnalyzerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_resource_scan_async(self, request):
        """立即开始扫描应用于指定资源的策略

        立即开始扫描应用于指定资源的策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartResourceScan
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.StartResourceScanRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.StartResourceScanResponse`
        """
        http_info = self._start_resource_scan_http_info(request)
        return self._call_api(**http_info)

    def start_resource_scan_async_invoker(self, request):
        http_info = self._start_resource_scan_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_resource_scan_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/analyzers/{analyzer_id}/scan",
            "request_type": request.__class__.__name__,
            "response_type": "StartResourceScanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def apply_archive_rule_async(self, request):
        """应用存档规则

        以追溯方式将存档规则应用于符合存档规则条件的现有结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyArchiveRule
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ApplyArchiveRuleRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ApplyArchiveRuleResponse`
        """
        http_info = self._apply_archive_rule_http_info(request)
        return self._call_api(**http_info)

    def apply_archive_rule_async_invoker(self, request):
        http_info = self._apply_archive_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_archive_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/analyzers/{analyzer_id}/archive-rules/{archive_rule_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyArchiveRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']
        if 'archive_rule_id' in local_var_params:
            path_params['archive_rule_id'] = local_var_params['archive_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_archive_rule_async(self, request):
        """为指定的分析器创建存档规则

        为指定的分析器创建存档规则。存档规则会自动存档符合您在创建规则时所定义条件的新结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateArchiveRule
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.CreateArchiveRuleRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.CreateArchiveRuleResponse`
        """
        http_info = self._create_archive_rule_http_info(request)
        return self._call_api(**http_info)

    def create_archive_rule_async_invoker(self, request):
        http_info = self._create_archive_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_archive_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/analyzers/{analyzer_id}/archive-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateArchiveRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_archive_rule_async(self, request):
        """删除指定的存档规则

        删除指定的存档规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteArchiveRule
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.DeleteArchiveRuleRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.DeleteArchiveRuleResponse`
        """
        http_info = self._delete_archive_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_archive_rule_async_invoker(self, request):
        http_info = self._delete_archive_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_archive_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/analyzers/{analyzer_id}/archive-rules/{archive_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteArchiveRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']
        if 'archive_rule_id' in local_var_params:
            path_params['archive_rule_id'] = local_var_params['archive_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_archive_rules_async(self, request):
        """检索为指定分析器创建的存档规则的列表

        检索为指定分析器创建的存档规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListArchiveRules
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListArchiveRulesRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListArchiveRulesResponse`
        """
        http_info = self._list_archive_rules_http_info(request)
        return self._call_api(**http_info)

    def list_archive_rules_async_invoker(self, request):
        http_info = self._list_archive_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_archive_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/analyzers/{analyzer_id}/archive-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListArchiveRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_archive_rule_async(self, request):
        """检索有关存档规则的信息

        检索有关存档规则的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowArchiveRule
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ShowArchiveRuleRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ShowArchiveRuleResponse`
        """
        http_info = self._show_archive_rule_http_info(request)
        return self._call_api(**http_info)

    def show_archive_rule_async_invoker(self, request):
        http_info = self._show_archive_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_archive_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/analyzers/{analyzer_id}/archive-rules/{archive_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowArchiveRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']
        if 'archive_rule_id' in local_var_params:
            path_params['archive_rule_id'] = local_var_params['archive_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_archive_rule_async(self, request):
        """更新指定存档规则的条件和值

        更新指定存档规则的条件和值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateArchiveRule
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.UpdateArchiveRuleRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UpdateArchiveRuleResponse`
        """
        http_info = self._update_archive_rule_http_info(request)
        return self._call_api(**http_info)

    def update_archive_rule_async_invoker(self, request):
        http_info = self._update_archive_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_archive_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/analyzers/{analyzer_id}/archive-rules/{archive_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateArchiveRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']
        if 'archive_rule_id' in local_var_params:
            path_params['archive_rule_id'] = local_var_params['archive_rule_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_findings_async(self, request):
        """检索指定分析器生成的访问分析结果列表

        检索指定分析器生成的访问分析结果列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFindings
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListFindingsRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListFindingsResponse`
        """
        http_info = self._list_findings_http_info(request)
        return self._call_api(**http_info)

    def list_findings_async_invoker(self, request):
        http_info = self._list_findings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_findings_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/analyzers/{analyzer_id}/findings",
            "request_type": request.__class__.__name__,
            "response_type": "ListFindingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_finding_async(self, request):
        """检索有关指定结果的信息

        检索有关指定结果的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFinding
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ShowFindingRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ShowFindingResponse`
        """
        http_info = self._show_finding_http_info(request)
        return self._call_api(**http_info)

    def show_finding_async_invoker(self, request):
        http_info = self._show_finding_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_finding_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/analyzers/{analyzer_id}/findings/{finding_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFindingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']
        if 'finding_id' in local_var_params:
            path_params['finding_id'] = local_var_params['finding_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_findings_async(self, request):
        """更新指定结果的状态

        更新指定访问分析结果的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFindings
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.UpdateFindingsRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UpdateFindingsResponse`
        """
        http_info = self._update_findings_http_info(request)
        return self._call_api(**http_info)

    def update_findings_async_invoker(self, request):
        http_info = self._update_findings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_findings_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/analyzers/{analyzer_id}/findings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFindingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_access_preview_async(self, request):
        """创建访问预览

        创建访问预览。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAccessPreview
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.CreateAccessPreviewRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.CreateAccessPreviewResponse`
        """
        http_info = self._create_access_preview_http_info(request)
        return self._call_api(**http_info)

    def create_access_preview_async_invoker(self, request):
        http_info = self._create_access_preview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_access_preview_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/analyzers/{analyzer_id}/access-previews",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccessPreviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_access_preview_findings_async(self, request):
        """获取相关预览生成的分析结果

        获取相关预览生成的分析结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessPreviewFindings
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListAccessPreviewFindingsRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListAccessPreviewFindingsResponse`
        """
        http_info = self._list_access_preview_findings_http_info(request)
        return self._call_api(**http_info)

    def list_access_preview_findings_async_invoker(self, request):
        http_info = self._list_access_preview_findings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_access_preview_findings_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/analyzers/{analyzer_id}/access-previews/{access_preview_id}/findings",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessPreviewFindingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']
        if 'access_preview_id' in local_var_params:
            path_params['access_preview_id'] = local_var_params['access_preview_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_access_previews_async(self, request):
        """获取所有访问预览

        获取所有访问预览。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessPreviews
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListAccessPreviewsRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ListAccessPreviewsResponse`
        """
        http_info = self._list_access_previews_http_info(request)
        return self._call_api(**http_info)

    def list_access_previews_async_invoker(self, request):
        http_info = self._list_access_previews_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_access_previews_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/analyzers/{analyzer_id}/access-previews",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessPreviewsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_access_preview_async(self, request):
        """获取相关访问预览的信息

        获取相关访问预览的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccessPreview
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ShowAccessPreviewRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ShowAccessPreviewResponse`
        """
        http_info = self._show_access_preview_http_info(request)
        return self._call_api(**http_info)

    def show_access_preview_async_invoker(self, request):
        http_info = self._show_access_preview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_access_preview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/analyzers/{analyzer_id}/access-previews/{access_preview_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessPreviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'analyzer_id' in local_var_params:
            path_params['analyzer_id'] = local_var_params['analyzer_id']
        if 'access_preview_id' in local_var_params:
            path_params['access_preview_id'] = local_var_params['access_preview_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def tag_resource_async(self, request):
        """向指定资源添加标签

        向指定资源添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for TagResource
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.TagResourceRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.TagResourceResponse`
        """
        http_info = self._tag_resource_http_info(request)
        return self._call_api(**http_info)

    def tag_resource_async_invoker(self, request):
        http_info = self._tag_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _tag_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "TagResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def untag_resource_async(self, request):
        """从指定资源中删除标签

        从指定资源中删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UntagResource
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.UntagResourceRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UntagResourceResponse`
        """
        http_info = self._untag_resource_http_info(request)
        return self._call_api(**http_info)

    def untag_resource_async_invoker(self, request):
        http_info = self._untag_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _untag_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "UntagResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def validate_policy_async(self, request):
        """校验策略

        校验策略并返回结果列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidatePolicy
        :type request: :class:`huaweicloudsdkiamaccessanalyzer.v1.ValidatePolicyRequest`
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ValidatePolicyResponse`
        """
        http_info = self._validate_policy_http_info(request)
        return self._call_api(**http_info)

    def validate_policy_async_invoker(self, request):
        http_info = self._validate_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/validate",
            "request_type": request.__class__.__name__,
            "response_type": "ValidatePolicyResponse"
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
