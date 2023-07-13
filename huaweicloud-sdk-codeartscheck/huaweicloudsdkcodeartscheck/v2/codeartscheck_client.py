# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CodeArtsCheckClient(Client):
    def __init__(self):
        super(CodeArtsCheckClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartscheck.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CodeArtsCheckClient":
            raise TypeError("client type error, support client type is CodeArtsCheckClient")

        return ClientBuilder(clazz)

    def check_parameters(self, request):
        """查询任务规则集的检查参数

        查询任务规则集的检查参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckParameters
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.CheckParametersRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.CheckParametersResponse`
        """
        return self._check_parameters_with_http_info(request)

    def _check_parameters_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']

        query_params = []
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/ruleset/{ruleset_id}/check-parameters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckParametersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_record(self, request):
        """历史扫描结果查询

        提供每次扫描的问题数量统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckRecord
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.CheckRecordRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.CheckRecordResponse`
        """
        return self._check_record_with_http_info(request)

    def _check_record_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/checkrecord',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_ruleset_parameters(self, request):
        """查询任务规则集的检查参数

        查询任务规则集的检查参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckRulesetParameters
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.CheckRulesetParametersRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.CheckRulesetParametersResponse`
        """
        return self._check_ruleset_parameters_with_http_info(request)

    def _check_ruleset_parameters_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']

        query_params = []
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/{project_id}/tasks/{task_id}/ruleset/{ruleset_id}/check-parameters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckRulesetParametersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_ruleset(self, request):
        """创建自定义规则集

        可根据需求灵活的组合规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRuleset
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.CreateRulesetRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.CreateRulesetResponse`
        """
        return self._create_ruleset_with_http_info(request)

    def _create_ruleset_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/ruleset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRulesetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_task(self, request):
        """新建检查任务

        新建检查任务但是不执行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.CreateTaskResponse`
        """
        return self._create_task_with_http_info(request)

    def _create_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ruleset(self, request):
        """删除自定义规则集

        删除自定义规则集，正在使用中的或默认规则集不能删除
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRuleset
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.DeleteRulesetRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.DeleteRulesetResponse`
        """
        return self._delete_ruleset_with_http_info(request)

    def _delete_ruleset_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/ruleset/{ruleset_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRulesetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_task(self, request):
        """删除检查任务

        删除检查任务，执行中的任务删除无法再查看
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.DeleteTaskResponse`
        """
        return self._delete_task_with_http_info(request)

    def _delete_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rules(self, request):
        """获取规则列表接口

        根据语言、问题级别等条件查询规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRules
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ListRulesRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ListRulesResponse`
        """
        return self._list_rules_with_http_info(request)

    def _list_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rule_languages' in local_var_params:
            query_params.append(('rule_languages', local_var_params['rule_languages']))
        if 'rule_severity' in local_var_params:
            query_params.append(('rule_severity', local_var_params['rule_severity']))
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rulesets(self, request):
        """查询规则集列表

        根据项目ID、语言等条件查询规则集列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRulesets
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ListRulesetsRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ListRulesetsResponse`
        """
        return self._list_rulesets_with_http_info(request)

    def _list_rulesets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/rulesets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRulesetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_task_parameter(self, request):
        """任务配置检查参数

        任务配置检查参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskParameter
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ListTaskParameterRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ListTaskParameterResponse`
        """
        return self._list_task_parameter_with_http_info(request)

    def _list_task_parameter_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/config-parameters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTaskParameterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_task_ruleset(self, request):
        """查询任务的已选规则集列表

        查询任务的已选规则集列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskRuleset
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ListTaskRulesetRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ListTaskRulesetResponse`
        """
        return self._list_task_ruleset_with_http_info(request)

    def _list_task_ruleset_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/rulesets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTaskRulesetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_template_rules(self, request):
        """查看规则集的规则列表

        根据项目ID、规则集ID等条件查询规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateRules
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ListTemplateRulesRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ListTemplateRulesResponse`
        """
        return self._list_template_rules_with_http_info(request)

    def _list_template_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']

        query_params = []
        if 'types' in local_var_params:
            query_params.append(('types', local_var_params['types']))
        if 'languages' in local_var_params:
            query_params.append(('languages', local_var_params['languages']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/ruleset/{ruleset_id}/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTemplateRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_task(self, request):
        """执行检查任务

        执行检查任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTask
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.RunTaskRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.RunTaskResponse`
        """
        return self._run_task_with_http_info(request)

    def _run_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/run',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_defaul_template(self, request):
        """设置每个项目对应语言的默认规则集配置

        设置每个项目对应语言的默认规则集配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetDefaulTemplate
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.SetDefaulTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.SetDefaulTemplateResponse`
        """
        return self._set_defaul_template_with_http_info(request)

    def _set_defaul_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']
        if 'language' in local_var_params:
            path_params['language'] = local_var_params['language']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/ruleset/{ruleset_id}/{language}/default',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetDefaulTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_progress_detail(self, request):
        """查询任务执行状态

        根据任务ID查询任务执行状态。任务状态：0表示检查中，1表示检查失败，2表示检查成功，3表示任务中止。只有正在检查中才有进度的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProgressDetail
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowProgressDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowProgressDetailResponse`
        """
        return self._show_progress_detail_with_http_info(request)

    def _show_progress_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProgressDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_cmetrics(self, request):
        """查询cmertrics缺陷概要

        根据检查任务ID查询cmertrics缺陷概要。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskCmetrics
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskCmetricsRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskCmetricsResponse`
        """
        return self._show_task_cmetrics_with_http_info(request)

    def _show_task_cmetrics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/metrics-summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskCmetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_defects(self, request):
        """查询缺陷详情

        根据检查任务ID分页查询缺陷结果详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskDefects
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskDefectsRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskDefectsResponse`
        """
        return self._show_task_defects_with_http_info(request)

    def _show_task_defects_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status_ids' in local_var_params:
            query_params.append(('status_ids', local_var_params['status_ids']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/defects-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskDefectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_defects_statistic(self, request):
        """查询缺陷详情的统计

        根据检查任务ID查询缺陷详情的统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskDefectsStatistic
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskDefectsStatisticRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskDefectsStatisticResponse`
        """
        return self._show_task_defects_statistic_with_http_info(request)

    def _show_task_defects_statistic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/defects-statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskDefectsStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_detail(self, request):
        """查询缺陷概要

        根据检查任务ID查询缺陷结果的概要。包括问题概述、问题状态、圈复杂度、代码重复率等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskDetail
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskDetailResponse`
        """
        return self._show_task_detail_with_http_info(request)

    def _show_task_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/defects-summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_list_by_project_id(self, request):
        """查询任务列表

        根据DEVCLOUD_PROJECT_UUID查询该项目下的任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskListByProjectId
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskListByProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskListByProjectIdResponse`
        """
        return self._show_task_list_by_project_id_with_http_info(request)

    def _show_task_list_by_project_id_with_http_info(self, request):
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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskListByProjectIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_path_tree(self, request):
        """获取任务的目录树

        获取任务的目录树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskPathTree
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskPathTreeRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskPathTreeResponse`
        """
        return self._show_task_path_tree_with_http_info(request)

    def _show_task_path_tree_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'current_path' in local_var_params:
            query_params.append(('current_path', local_var_params['current_path']))
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
            resource_path='/v2/{project_id}/tasks/{task_id}/listpathtree',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskPathTreeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_settings(self, request):
        """查询任务的高级选项

        查询任务的高级选项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskSettings
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTaskSettingsResponse`
        """
        return self._show_task_settings_with_http_info(request)

    def _show_task_settings_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/settings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskSettingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tasklog(self, request):
        """查询任务检查失败日志

        查询任务检查失败日志，不传execute_id则查询最近一次的检查日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTasklog
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTasklogRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTasklogResponse`
        """
        return self._show_tasklog_with_http_info(request)

    def _show_tasklog_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'execute_id' in local_var_params:
            query_params.append(('execute_id', local_var_params['execute_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/log-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTasklogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tasks_rulesets(self, request):
        """查询任务的已选规则集列表

        查询任务的已选规则集列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTasksRulesets
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.ShowTasksRulesetsRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ShowTasksRulesetsResponse`
        """
        return self._show_tasks_rulesets_with_http_info(request)

    def _show_tasks_rulesets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/{project_id}/tasks/{task_id}/rulesets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTasksRulesetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_task_by_id(self, request):
        """终止检查任务

        根据任务ID终止检查任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopTaskById
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.StopTaskByIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.StopTaskByIdResponse`
        """
        return self._stop_task_by_id_with_http_info(request)

    def _stop_task_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopTaskByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_defect_status(self, request):
        """修改缺陷状态

        修改检查出的缺陷的状态为已解决、已忽略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDefectStatus
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.UpdateDefectStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.UpdateDefectStatusResponse`
        """
        return self._update_defect_status_with_http_info(request)

    def _update_defect_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/defect-status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDefectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ignore_path(self, request):
        """任务配置屏蔽目录

        任务配置屏蔽目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIgnorePath
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.UpdateIgnorePathRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.UpdateIgnorePathResponse`
        """
        return self._update_ignore_path_with_http_info(request)

    def _update_ignore_path_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/config-ignorepath',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIgnorePathResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_task_ruleset(self, request):
        """修改任务规则集

        修改任务规则集。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskRuleset
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.UpdateTaskRulesetRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.UpdateTaskRulesetResponse`
        """
        return self._update_task_ruleset_with_http_info(request)

    def _update_task_ruleset_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/ruleset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTaskRulesetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_task_settings(self, request):
        """任务配置高级选项

        任务配置高级选项，如自定义镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskSettings
        :type request: :class:`huaweicloudsdkcodeartscheck.v2.UpdateTaskSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.UpdateTaskSettingsResponse`
        """
        return self._update_task_settings_with_http_info(request)

    def _update_task_settings_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/settings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTaskSettingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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
