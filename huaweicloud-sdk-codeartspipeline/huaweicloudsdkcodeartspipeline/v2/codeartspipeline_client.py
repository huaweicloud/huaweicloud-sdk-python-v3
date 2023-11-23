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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodeartspipeline'")


class CodeArtsPipelineClient(Client):
    def __init__(self):
        super(CodeArtsPipelineClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartspipeline.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeArtsPipelineClient":
                raise TypeError("client type error, support client type is CodeArtsPipelineClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_move_pipeline_to_group(self, request):
        """批量把流水线移动到分组下

        批量把流水线移动到分组下
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchMovePipelineToGroup
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.BatchMovePipelineToGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.BatchMovePipelineToGroupResponse`
        """
        http_info = self._batch_move_pipeline_to_group_http_info(request)
        return self._call_api(**http_info)

    def batch_move_pipeline_to_group_invoker(self, request):
        http_info = self._batch_move_pipeline_to_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_move_pipeline_to_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipeline-group/pipeline/move",
            "request_type": request.__class__.__name__,
            "response_type": "BatchMovePipelineToGroupResponse"
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

    def batch_show_pipelines_status(self, request):
        """批量获取流水线状态

        批量获取流水线状态和阶段信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowPipelinesStatus
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.BatchShowPipelinesStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.BatchShowPipelinesStatusResponse`
        """
        http_info = self._batch_show_pipelines_status_http_info(request)
        return self._call_api(**http_info)

    def batch_show_pipelines_status_invoker(self, request):
        http_info = self._batch_show_pipelines_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_pipelines_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/pipelines/status",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowPipelinesStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pipeline_ids' in local_var_params:
            query_params.append(('pipeline_ids', local_var_params['pipeline_ids']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_basic_plugin(self, request):
        """创建基础插件

        创建基础插件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBasicPlugin
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreateBasicPluginRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreateBasicPluginResponse`
        """
        http_info = self._create_basic_plugin_http_info(request)
        return self._call_api(**http_info)

    def create_basic_plugin_invoker(self, request):
        http_info = self._create_basic_plugin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_basic_plugin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/extension/info/add",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBasicPluginResponse"
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

    def create_open_source_strategy(self, request):
        """创建租户级开源治理策略

        创建租户级开源治理策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOpenSourceStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreateOpenSourceStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreateOpenSourceStrategyResponse`
        """
        http_info = self._create_open_source_strategy_http_info(request)
        return self._call_api(**http_info)

    def create_open_source_strategy_invoker(self, request):
        http_info = self._create_open_source_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_open_source_strategy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{domain_id}/tenant/open-source/rule-sets/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOpenSourceStrategyResponse"
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

    def create_pipeline_by_template(self, request):
        """基于模板快速创建流水线及流水线内任务

        基于模板快速创建流水线及流水线内任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipelineByTemplate
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineByTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineByTemplateResponse`
        """
        http_info = self._create_pipeline_by_template_http_info(request)
        return self._call_api(**http_info)

    def create_pipeline_by_template_invoker(self, request):
        http_info = self._create_pipeline_by_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pipeline_by_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/templates/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePipelineByTemplateResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_pipeline_group(self, request):
        """新建流水线分组

        新建流水线分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipelineGroup
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineGroupResponse`
        """
        http_info = self._create_pipeline_group_http_info(request)
        return self._call_api(**http_info)

    def create_pipeline_group_invoker(self, request):
        http_info = self._create_pipeline_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pipeline_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipeline-group/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePipelineGroupResponse"
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

    def create_plugin_draft(self, request):
        """创建插件草稿版本

        创建插件草稿版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePluginDraft
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePluginDraftRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePluginDraftResponse`
        """
        http_info = self._create_plugin_draft_http_info(request)
        return self._call_api(**http_info)

    def create_plugin_draft_invoker(self, request):
        http_info = self._create_plugin_draft_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_plugin_draft_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/create-draft",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePluginDraftResponse"
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

    def create_plugin_version(self, request):
        """创建插件版本

        创建插件版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePluginVersion
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePluginVersionRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePluginVersionResponse`
        """
        http_info = self._create_plugin_version_http_info(request)
        return self._call_api(**http_info)

    def create_plugin_version_invoker(self, request):
        http_info = self._create_plugin_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_plugin_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePluginVersionResponse"
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

    def create_publisher(self, request):
        """创建发布商

        创建发布商
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePublisher
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePublisherRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePublisherResponse`
        """
        http_info = self._create_publisher_http_info(request)
        return self._call_api(**http_info)

    def create_publisher_invoker(self, request):
        http_info = self._create_publisher_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_publisher_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/publisher/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePublisherResponse"
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

    def create_rule(self, request):
        """创建规则

        创建规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRule
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreateRuleRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreateRuleResponse`
        """
        http_info = self._create_rule_http_info(request)
        return self._call_api(**http_info)

    def create_rule_invoker(self, request):
        http_info = self._create_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{domain_id}/rules/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRuleResponse"
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

    def create_strategy(self, request):
        """创建规则集

        创建规则集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreateStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreateStrategyResponse`
        """
        http_info = self._create_strategy_http_info(request)
        return self._call_api(**http_info)

    def create_strategy_invoker(self, request):
        http_info = self._create_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_strategy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{domain_id}/tenant/rule-sets/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStrategyResponse"
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

    def delete_basic_plugin(self, request):
        """删除基础插件

        删除基础插件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBasicPlugin
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeleteBasicPluginRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeleteBasicPluginResponse`
        """
        http_info = self._delete_basic_plugin_http_info(request)
        return self._call_api(**http_info)

    def delete_basic_plugin_invoker(self, request):
        http_info = self._delete_basic_plugin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_basic_plugin_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/extension/info/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBasicPluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))

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

    def delete_open_source_strategy(self, request):
        """删除租户级开源治理策略

        删除租户级开源治理策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOpenSourceStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeleteOpenSourceStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeleteOpenSourceStrategyResponse`
        """
        http_info = self._delete_open_source_strategy_http_info(request)
        return self._call_api(**http_info)

    def delete_open_source_strategy_invoker(self, request):
        http_info = self._delete_open_source_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_open_source_strategy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{domain_id}/tenant/open-source/rule-sets/{rule_set_id}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpenSourceStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']

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

    def delete_pipeline_group(self, request):
        """删除流水线分组

        删除流水线分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePipelineGroup
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePipelineGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePipelineGroupResponse`
        """
        http_info = self._delete_pipeline_group_http_info(request)
        return self._call_api(**http_info)

    def delete_pipeline_group_invoker(self, request):
        http_info = self._delete_pipeline_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_pipeline_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/api/pipeline-group/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePipelineGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def delete_plugin_draft(self, request):
        """删除插件草稿

        删除插件草稿
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePluginDraft
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePluginDraftRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePluginDraftResponse`
        """
        http_info = self._delete_plugin_draft_http_info(request)
        return self._call_api(**http_info)

    def delete_plugin_draft_invoker(self, request):
        http_info = self._delete_plugin_draft_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_plugin_draft_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/agent-plugin/delete-draft",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePluginDraftResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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

    def delete_publisher(self, request):
        """删除发布商

        删除发布商
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePublisher
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePublisherRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePublisherResponse`
        """
        http_info = self._delete_publisher_http_info(request)
        return self._call_api(**http_info)

    def delete_publisher_invoker(self, request):
        http_info = self._delete_publisher_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_publisher_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/publisher/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePublisherResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'publisher_unique_id' in local_var_params:
            query_params.append(('publisher_unique_id', local_var_params['publisher_unique_id']))

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

    def delete_rule(self, request):
        """删除规则

        删除规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeleteRuleResponse`
        """
        http_info = self._delete_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_rule_invoker(self, request):
        http_info = self._delete_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{domain_id}/rules/{rule_id}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def delete_strategy(self, request):
        """删除规则集

        删除规则集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeleteStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeleteStrategyResponse`
        """
        http_info = self._delete_strategy_http_info(request)
        return self._call_api(**http_info)

    def delete_strategy_invoker(self, request):
        http_info = self._delete_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_strategy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{domain_id}/tenant/rule-sets/{rule_set_id}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']
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

    def list_available_publisher(self, request):
        """查询可用发布商

        查询可用发布商
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailablePublisher
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListAvailablePublisherRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListAvailablePublisherResponse`
        """
        http_info = self._list_available_publisher_http_info(request)
        return self._call_api(**http_info)

    def list_available_publisher_invoker(self, request):
        http_info = self._list_available_publisher_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_publisher_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/publisher/optional-publisher",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailablePublisherResponse"
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

    def list_base_plugins(self, request):
        """查询基础插件列表

        查询基础插件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBasePlugins
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListBasePluginsRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListBasePluginsResponse`
        """
        http_info = self._list_base_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_base_plugins_invoker(self, request):
        http_info = self._list_base_plugins_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_base_plugins_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/relation/plugin/single",
            "request_type": request.__class__.__name__,
            "response_type": "ListBasePluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'attribution' in local_var_params:
            query_params.append(('attribution', local_var_params['attribution']))
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

    def list_base_plugins_new_post(self, request):
        """分页查询可选插件列表

        分页查询可选插件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBasePluginsNewPost
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListBasePluginsNewPostRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListBasePluginsNewPostResponse`
        """
        http_info = self._list_base_plugins_new_post_http_info(request)
        return self._call_api(**http_info)

    def list_base_plugins_new_post_invoker(self, request):
        http_info = self._list_base_plugins_new_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_base_plugins_new_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/relation/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ListBasePluginsNewPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_open_source_strategy(self, request):
        """查询租户级开源治理策略列表

        查询租户级开源治理策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOpenSourceStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListOpenSourceStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListOpenSourceStrategyResponse`
        """
        http_info = self._list_open_source_strategy_http_info(request)
        return self._call_api(**http_info)

    def list_open_source_strategy_invoker(self, request):
        http_info = self._list_open_source_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_open_source_strategy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/tenant/open-source/rule-sets/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpenSourceStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'creator_name' in local_var_params:
            query_params.append(('creator_name', local_var_params['creator_name']))
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

    def list_p_lugin_version(self, request):
        """查询插件所有版本信息

        查询插件所有版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPLuginVersion
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPLuginVersionRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPLuginVersionResponse`
        """
        http_info = self._list_p_lugin_version_http_info(request)
        return self._call_api(**http_info)

    def list_p_lugin_version_invoker(self, request):
        http_info = self._list_p_lugin_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_p_lugin_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/agent-plugin/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListPLuginVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
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

    def list_pipeline_simple_info(self, request):
        """获取流水线列表接口

        获取流水线列表接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelineSimpleInfo
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineSimpleInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineSimpleInfoResponse`
        """
        http_info = self._list_pipeline_simple_info_http_info(request)
        return self._call_api(**http_info)

    def list_pipeline_simple_info_invoker(self, request):
        http_info = self._list_pipeline_simple_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pipeline_simple_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/pipelines/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipelineSimpleInfoResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pipleine_build_result(self, request):
        """获取项目下流水线执行状况

        获取项目下流水线执行状况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipleineBuildResult
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipleineBuildResultRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipleineBuildResultResponse`
        """
        http_info = self._list_pipleine_build_result_http_info(request)
        return self._call_api(**http_info)

    def list_pipleine_build_result_invoker(self, request):
        http_info = self._list_pipleine_build_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pipleine_build_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/pipelines/build-result",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipleineBuildResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_plugin_version_number(self, request):
        """查询插件版本号

        查询插件版本号
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPluginVersionNumber
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPluginVersionNumberRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPluginVersionNumberResponse`
        """
        http_info = self._list_plugin_version_number_http_info(request)
        return self._call_api(**http_info)

    def list_plugin_version_number_invoker(self, request):
        http_info = self._list_plugin_version_number_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_plugin_version_number_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/agent-plugin/all-version",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginVersionNumberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
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

    def list_plugins(self, request):
        """查询插件列表

        查询插件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlugins
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPluginsRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPluginsResponse`
        """
        http_info = self._list_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_plugins_invoker(self, request):
        http_info = self._list_plugins_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_plugins_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/query-all",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_project_open_source_strategy(self, request):
        """查询项目级开源治理策略列表

        查询项目级开源治理策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectOpenSourceStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListProjectOpenSourceStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListProjectOpenSourceStrategyResponse`
        """
        http_info = self._list_project_open_source_strategy_http_info(request)
        return self._call_api(**http_info)

    def list_project_open_source_strategy_invoker(self, request):
        http_info = self._list_project_open_source_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_open_source_strategy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/open-source/rule-sets/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectOpenSourceStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'creator_name' in local_var_params:
            query_params.append(('creator_name', local_var_params['creator_name']))
        if 'include_tenant_rule_set' in local_var_params:
            query_params.append(('include_tenant_rule_set', local_var_params['include_tenant_rule_set']))
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

    def list_project_strategy(self, request):
        """获取规则模板实例列表

        获取规则集列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListProjectStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListProjectStrategyResponse`
        """
        http_info = self._list_project_strategy_http_info(request)
        return self._call_api(**http_info)

    def list_project_strategy_invoker(self, request):
        http_info = self._list_project_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_strategy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/rule-sets/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'include_tenant_rule_set' in local_var_params:
            query_params.append(('include_tenant_rule_set', local_var_params['include_tenant_rule_set']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'is_valid' in local_var_params:
            query_params.append(('is_valid', local_var_params['is_valid']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_publisher(self, request):
        """查询发布商列表

        查询发布商列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublisher
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPublisherRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPublisherResponse`
        """
        http_info = self._list_publisher_http_info(request)
        return self._call_api(**http_info)

    def list_publisher_invoker(self, request):
        http_info = self._list_publisher_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_publisher_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/publisher/query-all",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublisherResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_rule(self, request):
        """分页获取规则列表

        分页获取规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRule
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListRuleRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListRuleResponse`
        """
        http_info = self._list_rule_http_info(request)
        return self._call_api(**http_info)

    def list_rule_invoker(self, request):
        http_info = self._list_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/rules/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'cloud_project_id' in local_var_params:
            query_params.append(('cloud_project_id', local_var_params['cloud_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_stage_plugins(self, request):
        """查询可选插件列表

        查询可选插件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStagePlugins
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListStagePluginsRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListStagePluginsResponse`
        """
        http_info = self._list_stage_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_stage_plugins_invoker(self, request):
        http_info = self._list_stage_plugins_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stage_plugins_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/relation/stage-plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ListStagePluginsResponse"
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

    def list_strategy(self, request):
        """获取规则集列表

        获取规则集列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListStrategyResponse`
        """
        http_info = self._list_strategy_http_info(request)
        return self._call_api(**http_info)

    def list_strategy_invoker(self, request):
        http_info = self._list_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_strategy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/tenant/rule-sets/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'include_tenant_rule_set' in local_var_params:
            query_params.append(('include_tenant_rule_set', local_var_params['include_tenant_rule_set']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'is_valid' in local_var_params:
            query_params.append(('is_valid', local_var_params['is_valid']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'cloud_project_id' in local_var_params:
            query_params.append(('cloud_project_id', local_var_params['cloud_project_id']))

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

    def list_templates(self, request):
        """查询模板列表

        查询模板列表，支持分页查询,支持模板名字模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_type' in local_var_params:
            query_params.append(('template_type', local_var_params['template_type']))
        if 'is_build_in' in local_var_params:
            query_params.append(('is_build_in', local_var_params['is_build_in']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def publish_plugin(self, request):
        """发布插件

        发布插件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishPlugin
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.PublishPluginRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PublishPluginResponse`
        """
        http_info = self._publish_plugin_http_info(request)
        return self._call_api(**http_info)

    def publish_plugin_invoker(self, request):
        http_info = self._publish_plugin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_plugin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/publish-plugin",
            "request_type": request.__class__.__name__,
            "response_type": "PublishPluginResponse"
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

    def publish_plugin_bind(self, request):
        """插件绑定发布商

        插件绑定发布商
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishPluginBind
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.PublishPluginBindRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PublishPluginBindResponse`
        """
        http_info = self._publish_plugin_bind_http_info(request)
        return self._call_api(**http_info)

    def publish_plugin_bind_invoker(self, request):
        http_info = self._publish_plugin_bind_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_plugin_bind_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/publish-plugin-bind",
            "request_type": request.__class__.__name__,
            "response_type": "PublishPluginBindResponse"
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

    def publish_plugin_draft(self, request):
        """发布插件草稿

        发布插件草稿
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishPluginDraft
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.PublishPluginDraftRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PublishPluginDraftResponse`
        """
        http_info = self._publish_plugin_draft_http_info(request)
        return self._call_api(**http_info)

    def publish_plugin_draft_invoker(self, request):
        http_info = self._publish_plugin_draft_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_plugin_draft_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/publish-draft",
            "request_type": request.__class__.__name__,
            "response_type": "PublishPluginDraftResponse"
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

    def remove_pipeline(self, request):
        """删除流水线

        根据id删除流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemovePipeline
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.RemovePipelineRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RemovePipelineResponse`
        """
        http_info = self._remove_pipeline_http_info(request)
        return self._call_api(**http_info)

    def remove_pipeline_invoker(self, request):
        http_info = self._remove_pipeline_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_pipeline_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/pipelines/{pipeline_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemovePipelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_basic_plugin(self, request):
        """查询基础插件详情

        查询基础插件详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBasicPlugin
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowBasicPluginRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowBasicPluginResponse`
        """
        http_info = self._show_basic_plugin_http_info(request)
        return self._call_api(**http_info)

    def show_basic_plugin_invoker(self, request):
        http_info = self._show_basic_plugin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_basic_plugin_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/extension/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBasicPluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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

    def show_instance_status(self, request):
        """检查流水线创建状态

        检查流水线创建状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceStatus
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowInstanceStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowInstanceStatusResponse`
        """
        http_info = self._show_instance_status_http_info(request)
        return self._call_api(**http_info)

    def show_instance_status_invoker(self, request):
        http_info = self._show_instance_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/templates/{task_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceStatusResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_open_source_strategy(self, request):
        """查询租户级开源治理策略详情

        查询租户级开源治理策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOpenSourceStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowOpenSourceStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowOpenSourceStrategyResponse`
        """
        http_info = self._show_open_source_strategy_http_info(request)
        return self._call_api(**http_info)

    def show_open_source_strategy_invoker(self, request):
        http_info = self._show_open_source_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_open_source_strategy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/tenant/open-source/rule-sets/{rule_set_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpenSourceStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']

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

    def show_pipeline_group_tree(self, request):
        """查询流水线分组树

        查询流水线分组树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipelineGroupTree
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineGroupTreeRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineGroupTreeResponse`
        """
        http_info = self._show_pipeline_group_tree_http_info(request)
        return self._call_api(**http_info)

    def show_pipeline_group_tree_invoker(self, request):
        http_info = self._show_pipeline_group_tree_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipeline_group_tree_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/api/pipeline-group/tree",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipelineGroupTreeResponse"
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

    def show_pipleine_status(self, request):
        """获取流水线状态

        获取流水线状态,阶段及任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipleineStatus
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipleineStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipleineStatusResponse`
        """
        http_info = self._show_pipleine_status_http_info(request)
        return self._call_api(**http_info)

    def show_pipleine_status_invoker(self, request):
        http_info = self._show_pipleine_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipleine_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/pipelines/{pipeline_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipleineStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'build_id' in local_var_params:
            query_params.append(('build_id', local_var_params['build_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_plugin_inputs(self, request):
        """查询插件输入配置

        查询插件输入配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPluginInputs
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPluginInputsRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPluginInputsResponse`
        """
        http_info = self._show_plugin_inputs_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_inputs_invoker(self, request):
        http_info = self._show_plugin_inputs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_plugin_inputs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/plugin-input",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginInputsResponse"
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

    def show_plugin_metrics(self, request):
        """查询插件指标配置

        查询插件指标配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPluginMetrics
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPluginMetricsRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPluginMetricsResponse`
        """
        http_info = self._show_plugin_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_metrics_invoker(self, request):
        http_info = self._show_plugin_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_plugin_metrics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/plugin-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginMetricsResponse"
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

    def show_plugin_outputs(self, request):
        """查询插件输出配置

        查询插件输出配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPluginOutputs
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPluginOutputsRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPluginOutputsResponse`
        """
        http_info = self._show_plugin_outputs_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_outputs_invoker(self, request):
        http_info = self._show_plugin_outputs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_plugin_outputs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/plugin-output",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginOutputsResponse"
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

    def show_plugin_version(self, request):
        """查询插件版本详情

        查询插件版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPluginVersion
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPluginVersionRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPluginVersionResponse`
        """
        http_info = self._show_plugin_version_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_version_invoker(self, request):
        http_info = self._show_plugin_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_plugin_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/agent-plugin/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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

    def show_project_open_source_strategy(self, request):
        """查询项目级开源治理策略详情

        查询项目级开源治理策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectOpenSourceStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowProjectOpenSourceStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowProjectOpenSourceStrategyResponse`
        """
        http_info = self._show_project_open_source_strategy_http_info(request)
        return self._call_api(**http_info)

    def show_project_open_source_strategy_invoker(self, request):
        http_info = self._show_project_open_source_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_open_source_strategy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/open-source/rule-sets/{rule_set_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectOpenSourceStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']

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

    def show_project_strategy(self, request):
        """show_project_strategy

        查询项目级策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowProjectStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowProjectStrategyResponse`
        """
        http_info = self._show_project_strategy_http_info(request)
        return self._call_api(**http_info)

    def show_project_strategy_invoker(self, request):
        http_info = self._show_project_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_strategy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/rule-sets/{rule_set_id}/gray/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']
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

    def show_publisher(self, request):
        """查询发布商详情

        查询发布商详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPublisher
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPublisherRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPublisherResponse`
        """
        http_info = self._show_publisher_http_info(request)
        return self._call_api(**http_info)

    def show_publisher_invoker(self, request):
        http_info = self._show_publisher_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_publisher_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/publisher/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublisherResponse"
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

    def show_rule(self, request):
        """获取单条规则详情

        获取单条规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRule
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowRuleRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowRuleResponse`
        """
        http_info = self._show_rule_http_info(request)
        return self._call_api(**http_info)

    def show_rule_invoker(self, request):
        http_info = self._show_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/rules/{rule_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
        if 'cloud_project_id' in local_var_params:
            query_params.append(('cloud_project_id', local_var_params['cloud_project_id']))

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

    def show_strategy(self, request):
        """获取规则集详情

        获取规则集详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowStrategyResponse`
        """
        http_info = self._show_strategy_http_info(request)
        return self._call_api(**http_info)

    def show_strategy_invoker(self, request):
        http_info = self._show_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_strategy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/tenant/rule-sets/{rule_set_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'cloud_project_id' in local_var_params:
            query_params.append(('cloud_project_id', local_var_params['cloud_project_id']))

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

    def show_template_detail(self, request):
        """查询模板详情

        查询模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateDetail
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowTemplateDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowTemplateDetailResponse`
        """
        http_info = self._show_template_detail_http_info(request)
        return self._call_api(**http_info)

    def show_template_detail_invoker(self, request):
        http_info = self._show_template_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_template_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []
        if 'template_type' in local_var_params:
            query_params.append(('template_type', local_var_params['template_type']))
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_new_pipeline(self, request):
        """启动流水线

        启动流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartNewPipeline
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.StartNewPipelineRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.StartNewPipelineResponse`
        """
        http_info = self._start_new_pipeline_http_info(request)
        return self._call_api(**http_info)

    def start_new_pipeline_invoker(self, request):
        http_info = self._start_new_pipeline_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_new_pipeline_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/pipelines/{pipeline_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartNewPipelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_pipeline_new(self, request):
        """停止流水线

        停止流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopPipelineNew
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.StopPipelineNewRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.StopPipelineNewResponse`
        """
        http_info = self._stop_pipeline_new_http_info(request)
        return self._call_api(**http_info)

    def stop_pipeline_new_invoker(self, request):
        http_info = self._stop_pipeline_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_pipeline_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/pipelines/{pipeline_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopPipelineNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'build_id' in local_var_params:
            query_params.append(('build_id', local_var_params['build_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def switch_open_source_strategy(self, request):
        """修改租户级开源治理策略启用状态

        修改租户级开源治理策略启用状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchOpenSourceStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.SwitchOpenSourceStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.SwitchOpenSourceStrategyResponse`
        """
        http_info = self._switch_open_source_strategy_http_info(request)
        return self._call_api(**http_info)

    def switch_open_source_strategy_invoker(self, request):
        http_info = self._switch_open_source_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_open_source_strategy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{domain_id}/tenant/open-source/rule-sets/{rule_set_id}/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchOpenSourceStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']

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

    def switch_strategy(self, request):
        """开关规则集

        修改规则集状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.SwitchStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.SwitchStrategyResponse`
        """
        http_info = self._switch_strategy_http_info(request)
        return self._call_api(**http_info)

    def switch_strategy_invoker(self, request):
        http_info = self._switch_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_strategy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{domain_id}/tenant/rule-sets/{rule_set_id}/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def update_basic_plugin(self, request):
        """更新基础插件

        更新基础插件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBasicPlugin
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UpdateBasicPluginRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UpdateBasicPluginResponse`
        """
        http_info = self._update_basic_plugin_http_info(request)
        return self._call_api(**http_info)

    def update_basic_plugin_invoker(self, request):
        http_info = self._update_basic_plugin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_basic_plugin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/extension/info/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBasicPluginResponse"
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

    def update_open_source_strategy(self, request):
        """修改租户级开源治理策略

        修改租户级开源治理策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOpenSourceStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UpdateOpenSourceStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UpdateOpenSourceStrategyResponse`
        """
        http_info = self._update_open_source_strategy_http_info(request)
        return self._call_api(**http_info)

    def update_open_source_strategy_invoker(self, request):
        http_info = self._update_open_source_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_open_source_strategy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{domain_id}/tenant/open-source/rule-sets/{rule_set_id}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpenSourceStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']

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

    def update_pipeline_group(self, request):
        """更新流水线分组

        更新流水线分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePipelineGroup
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UpdatePipelineGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UpdatePipelineGroupResponse`
        """
        http_info = self._update_pipeline_group_http_info(request)
        return self._call_api(**http_info)

    def update_pipeline_group_invoker(self, request):
        http_info = self._update_pipeline_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_pipeline_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipeline-group/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePipelineGroupResponse"
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

    def update_plugin_base_info(self, request):
        """更新插件基本信息

        更新插件基本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePluginBaseInfo
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UpdatePluginBaseInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UpdatePluginBaseInfoResponse`
        """
        http_info = self._update_plugin_base_info_http_info(request)
        return self._call_api(**http_info)

    def update_plugin_base_info_invoker(self, request):
        http_info = self._update_plugin_base_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_plugin_base_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/update-info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePluginBaseInfoResponse"
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

    def update_plugin_draft(self, request):
        """更新插件草稿

        更新插件草稿
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePluginDraft
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UpdatePluginDraftRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UpdatePluginDraftResponse`
        """
        http_info = self._update_plugin_draft_http_info(request)
        return self._call_api(**http_info)

    def update_plugin_draft_invoker(self, request):
        http_info = self._update_plugin_draft_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_plugin_draft_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/agent-plugin/edit-draft",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePluginDraftResponse"
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

    def update_rule(self, request):
        """更新规则

        更新规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRule
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UpdateRuleRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UpdateRuleResponse`
        """
        http_info = self._update_rule_http_info(request)
        return self._call_api(**http_info)

    def update_rule_invoker(self, request):
        http_info = self._update_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{domain_id}/rules/{rule_id}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def update_strategy(self, request):
        """修改规则集

        修改规则集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStrategy
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UpdateStrategyRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UpdateStrategyResponse`
        """
        http_info = self._update_strategy_http_info(request)
        return self._call_api(**http_info)

    def update_strategy_invoker(self, request):
        http_info = self._update_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_strategy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{domain_id}/tenant/rule-sets/{rule_set_id}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_set_id' in local_var_params:
            path_params['rule_set_id'] = local_var_params['rule_set_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def upload_basic_plugin(self, request):
        """上传基础插件

        上传基础插件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadBasicPlugin
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UploadBasicPluginRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UploadBasicPluginResponse`
        """
        http_info = self._upload_basic_plugin_http_info(request)
        return self._call_api(**http_info)

    def upload_basic_plugin_invoker(self, request):
        http_info = self._upload_basic_plugin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_basic_plugin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/extension/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadBasicPluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'business_type' in local_var_params:
            query_params.append(('business_type', local_var_params['business_type']))

        header_params = {}

        form_params = {}
        if 'upload_file' in local_var_params:
            form_params['upload_file'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upload_plugin_icon(self, request):
        """更新插件图标

        更新插件图标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadPluginIcon
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPluginIconRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPluginIconResponse`
        """
        http_info = self._upload_plugin_icon_http_info(request)
        return self._call_api(**http_info)

    def upload_plugin_icon_invoker(self, request):
        http_info = self._upload_plugin_icon_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_plugin_icon_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/common/upload-plugin-icon",
            "request_type": request.__class__.__name__,
            "response_type": "UploadPluginIconResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))

        header_params = {}

        form_params = {}
        if 'upload_file' in local_var_params:
            form_params['upload_file'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upload_publisher_icon(self, request):
        """更新发布商图标

        更新发布商图标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadPublisherIcon
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPublisherIconRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPublisherIconResponse`
        """
        http_info = self._upload_publisher_icon_http_info(request)
        return self._call_api(**http_info)

    def upload_publisher_icon_invoker(self, request):
        http_info = self._upload_publisher_icon_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_publisher_icon_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/common/upload-publisher-icon",
            "request_type": request.__class__.__name__,
            "response_type": "UploadPublisherIconResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'publisher_en_name' in local_var_params:
            query_params.append(('publisher_en_name', local_var_params['publisher_en_name']))

        header_params = {}

        form_params = {}
        if 'upload_file' in local_var_params:
            form_params['upload_file'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def accept_manual_review(self, request):
        """通过人工审核

        通过人工审核
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AcceptManualReview
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.AcceptManualReviewRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.AcceptManualReviewResponse`
        """
        http_info = self._accept_manual_review_http_info(request)
        return self._call_api(**http_info)

    def accept_manual_review_invoker(self, request):
        http_info = self._accept_manual_review_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _accept_manual_review_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/{pipeline_run_id}/jobs/{job_run_id}/steps/{step_run_id}/pass",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptManualReviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_run_id' in local_var_params:
            path_params['job_run_id'] = local_var_params['job_run_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']
        if 'pipeline_run_id' in local_var_params:
            path_params['pipeline_run_id'] = local_var_params['pipeline_run_id']
        if 'step_run_id' in local_var_params:
            path_params['step_run_id'] = local_var_params['step_run_id']

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

    def batch_show_pipelines_latest_status(self, request):
        """批量获取流水线状态

        批量获取流水线状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowPipelinesLatestStatus
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.BatchShowPipelinesLatestStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.BatchShowPipelinesLatestStatusResponse`
        """
        http_info = self._batch_show_pipelines_latest_status_http_info(request)
        return self._call_api(**http_info)

    def batch_show_pipelines_latest_status_invoker(self, request):
        http_info = self._batch_show_pipelines_latest_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_pipelines_latest_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipelines/status",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowPipelinesLatestStatusResponse"
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

    def create_pipeline_by_template_id(self, request):
        """基于模板创建流水线

        基于模板创建流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipelineByTemplateId
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineByTemplateIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineByTemplateIdResponse`
        """
        http_info = self._create_pipeline_by_template_id_http_info(request)
        return self._call_api(**http_info)

    def create_pipeline_by_template_id_invoker(self, request):
        http_info = self._create_pipeline_by_template_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pipeline_by_template_id_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipeline-templates/{template_id}/create-pipeline",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePipelineByTemplateIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))

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

    def create_pipeline_new(self, request):
        """创建流水线

        创建流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipelineNew
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineNewRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineNewResponse`
        """
        http_info = self._create_pipeline_new_http_info(request)
        return self._call_api(**http_info)

    def create_pipeline_new_invoker(self, request):
        http_info = self._create_pipeline_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pipeline_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipelines",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePipelineNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))

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

    def create_pipeline_template(self, request):
        """创建流水线模板

        创建流水线模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipelineTemplate
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineTemplateResponse`
        """
        http_info = self._create_pipeline_template_http_info(request)
        return self._call_api(**http_info)

    def create_pipeline_template_invoker(self, request):
        http_info = self._create_pipeline_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pipeline_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{tenant_id}/api/pipeline-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePipelineTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

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

    def delete_pipeline(self, request):
        """删除流水线

        删除流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePipeline
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePipelineRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePipelineResponse`
        """
        http_info = self._delete_pipeline_http_info(request)
        return self._call_api(**http_info)

    def delete_pipeline_invoker(self, request):
        http_info = self._delete_pipeline_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_pipeline_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/api/pipelines/{pipeline_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePipelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

    def delete_pipeline_template(self, request):
        """删除流水线模板

        删除流水线模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePipelineTemplate
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePipelineTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePipelineTemplateResponse`
        """
        http_info = self._delete_pipeline_template_http_info(request)
        return self._call_api(**http_info)

    def delete_pipeline_template_invoker(self, request):
        http_info = self._delete_pipeline_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_pipeline_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{tenant_id}/api/pipeline-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePipelineTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
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

    def list_pipeline_runs(self, request):
        """获取流水线执行记录

        获取流水线执行记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelineRuns
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineRunsRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineRunsResponse`
        """
        http_info = self._list_pipeline_runs_http_info(request)
        return self._call_api(**http_info)

    def list_pipeline_runs_invoker(self, request):
        http_info = self._list_pipeline_runs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pipeline_runs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipelineRunsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

    def list_pipeline_templates(self, request):
        """查询模板列表

        查询流水线模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelineTemplates
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineTemplatesResponse`
        """
        http_info = self._list_pipeline_templates_http_info(request)
        return self._call_api(**http_info)

    def list_pipeline_templates_invoker(self, request):
        http_info = self._list_pipeline_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pipeline_templates_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{tenant_id}/api/pipeline-templates/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipelineTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

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

    def list_pipelines(self, request):
        """获取流水线列表/获取项目下流水线执行状况

        获取流水线列表/获取项目下流水线执行状况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelines
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesResponse`
        """
        http_info = self._list_pipelines_http_info(request)
        return self._call_api(**http_info)

    def list_pipelines_invoker(self, request):
        http_info = self._list_pipelines_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pipelines_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipelines/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipelinesResponse"
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

    def reject_manual_review(self, request):
        """驳回人工审核

        驳回人工审核
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RejectManualReview
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.RejectManualReviewRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RejectManualReviewResponse`
        """
        http_info = self._reject_manual_review_http_info(request)
        return self._call_api(**http_info)

    def reject_manual_review_invoker(self, request):
        http_info = self._reject_manual_review_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reject_manual_review_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/{pipeline_run_id}/jobs/{job_run_id}/steps/{step_run_id}/refuse",
            "request_type": request.__class__.__name__,
            "response_type": "RejectManualReviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_run_id' in local_var_params:
            path_params['job_run_id'] = local_var_params['job_run_id']
        if 'step_run_id' in local_var_params:
            path_params['step_run_id'] = local_var_params['step_run_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']
        if 'pipeline_run_id' in local_var_params:
            path_params['pipeline_run_id'] = local_var_params['pipeline_run_id']

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

    def retry_pipeline_run(self, request):
        """重试运行流水线

        重试运行流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryPipelineRun
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.RetryPipelineRunRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RetryPipelineRunResponse`
        """
        http_info = self._retry_pipeline_run_http_info(request)
        return self._call_api(**http_info)

    def retry_pipeline_run_invoker(self, request):
        http_info = self._retry_pipeline_run_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_pipeline_run_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/{pipeline_run_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryPipelineRunResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']
        if 'pipeline_run_id' in local_var_params:
            path_params['pipeline_run_id'] = local_var_params['pipeline_run_id']

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

    def run_pipeline(self, request):
        """启动流水线

        启动流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunPipeline
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineResponse`
        """
        http_info = self._run_pipeline_http_info(request)
        return self._call_api(**http_info)

    def run_pipeline_invoker(self, request):
        http_info = self._run_pipeline_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_pipeline_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipelines/{pipeline_id}/run",
            "request_type": request.__class__.__name__,
            "response_type": "RunPipelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

    def show_pipeline_run_detail(self, request):
        """获取流水线状态/获取流水线执行详情

        获取流水线状态/获取流水线执行详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipelineRunDetail
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineRunDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineRunDetailResponse`
        """
        http_info = self._show_pipeline_run_detail_http_info(request)
        return self._call_api(**http_info)

    def show_pipeline_run_detail_invoker(self, request):
        http_info = self._show_pipeline_run_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipeline_run_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipelineRunDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'pipeline_run_id' in local_var_params:
            query_params.append(('pipeline_run_id', local_var_params['pipeline_run_id']))

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

    def show_pipeline_template_detail(self, request):
        """查询模板详情

        查询模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipelineTemplateDetail
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineTemplateDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineTemplateDetailResponse`
        """
        http_info = self._show_pipeline_template_detail_http_info(request)
        return self._call_api(**http_info)

    def show_pipeline_template_detail_invoker(self, request):
        http_info = self._show_pipeline_template_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipeline_template_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{tenant_id}/api/pipeline-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipelineTemplateDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
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

    def stop_pipeline_run(self, request):
        """停止流水线

        停止流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopPipelineRun
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.StopPipelineRunRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.StopPipelineRunResponse`
        """
        http_info = self._stop_pipeline_run_http_info(request)
        return self._call_api(**http_info)

    def stop_pipeline_run_invoker(self, request):
        http_info = self._stop_pipeline_run_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_pipeline_run_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/{pipeline_run_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopPipelineRunResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']
        if 'pipeline_run_id' in local_var_params:
            path_params['pipeline_run_id'] = local_var_params['pipeline_run_id']

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

    def update_pipeline_template(self, request):
        """更新流水线模板

        更新流水线模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePipelineTemplate
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.UpdatePipelineTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UpdatePipelineTemplateResponse`
        """
        http_info = self._update_pipeline_template_http_info(request)
        return self._call_api(**http_info)

    def update_pipeline_template_invoker(self, request):
        http_info = self._update_pipeline_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_pipeline_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{tenant_id}/api/pipeline-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePipelineTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
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
