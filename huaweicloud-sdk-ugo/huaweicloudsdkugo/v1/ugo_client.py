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


class UgoClient(Client):
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
        super(UgoClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkugo.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "UgoClient":
            raise TypeError("client type error, support client type is UgoClient")

        return ClientBuilder(clazz)

    def check_permission(self, request):
        """目标库权限检查。

        目标库权限检查。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckPermission
        :type request: :class:`huaweicloudsdkugo.v1.CheckPermissionRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CheckPermissionResponse`
        """
        return self.check_permission_with_http_info(request)

    def check_permission_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/permission-check',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckPermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def commit_syntax_conversion(self, request):
        """提交语法转换

        提交语法转换。只有migration_project_status为\&quot;READY\&quot;时才能调用该接口。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CommitSyntaxConversion
        :type request: :class:`huaweicloudsdkugo.v1.CommitSyntaxConversionRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CommitSyntaxConversionResponse`
        """
        return self.commit_syntax_conversion_with_http_info(request)

    def commit_syntax_conversion_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/syntax-conversion',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CommitSyntaxConversionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def commit_verification(self, request):
        """提交验证。

        提交验证。语法转换完成后，才能调用该接口。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CommitVerification
        :type request: :class:`huaweicloudsdkugo.v1.CommitVerificationRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CommitVerificationResponse`
        """
        return self.commit_verification_with_http_info(request)

    def commit_verification_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/verification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CommitVerificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def confirm_target_db_type(self, request):
        """评估项目确认目标数据库类型。

        评估项目确认目标数据库类型。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ConfirmTargetDbType
        :type request: :class:`huaweicloudsdkugo.v1.ConfirmTargetDbTypeRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ConfirmTargetDbTypeResponse`
        """
        return self.confirm_target_db_type_with_http_info(request)

    def confirm_target_db_type_with_http_info(self, request):
        all_params = ['confirm_target_db_req']
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
            resource_path='/v1/{project_id}/evaluation-projects/target-confirmation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConfirmTargetDbTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_evaluation_project(self, request):
        """创建评估项目。

        创建评估项目。评估项目分2个阶段：采集、评估。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateEvaluationProject
        :type request: :class:`huaweicloudsdkugo.v1.CreateEvaluationProjectRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CreateEvaluationProjectResponse`
        """
        return self.create_evaluation_project_with_http_info(request)

    def create_evaluation_project_with_http_info(self, request):
        all_params = ['create_evaluation_req']
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
            resource_path='/v1/{project_id}/evaluation-projects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEvaluationProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_migration_project(self, request):
        """创建迁移项目。

        创建迁移项目。创建迁移项目需要关联状态为“COMPLETED”的评估项目。迁移项目依次经历以下几个阶段：目标库权限检查、语法转换、验证、下载迁移失败的报告、删除。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateMigrationProject
        :type request: :class:`huaweicloudsdkugo.v1.CreateMigrationProjectRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CreateMigrationProjectResponse`
        """
        return self.create_migration_project_with_http_info(request)

    def create_migration_project_with_http_info(self, request):
        all_params = ['create_migration_project']
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
            resource_path='/v1/{project_id}/migration-projects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMigrationProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_evaluation_project(self, request):
        """删除评估项目。

        删除评估项目。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteEvaluationProject
        :type request: :class:`huaweicloudsdkugo.v1.DeleteEvaluationProjectRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.DeleteEvaluationProjectResponse`
        """
        return self.delete_evaluation_project_with_http_info(request)

    def delete_evaluation_project_with_http_info(self, request):
        all_params = ['evaluation_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'evaluation_project_id' in local_var_params:
            path_params['evaluation_project_id'] = local_var_params['evaluation_project_id']

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
            resource_path='/v1/{project_id}/evaluation-projects/{evaluation_project_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEvaluationProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_migration_project(self, request):
        """删除迁移项目

        删除迁移项目。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteMigrationProject
        :type request: :class:`huaweicloudsdkugo.v1.DeleteMigrationProjectRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.DeleteMigrationProjectResponse`
        """
        return self.delete_migration_project_with_http_info(request)

    def delete_migration_project_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMigrationProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_failure_report(self, request):
        """下载迁移错误报告。

        下载迁移错误报告。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DownloadFailureReport
        :type request: :class:`huaweicloudsdkugo.v1.DownloadFailureReportRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.DownloadFailureReportResponse`
        """
        return self.download_failure_report_with_http_info(request)

    def download_failure_report_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/download-failure-report',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadFailureReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_evaluation_projects(self, request):
        """查询评估项目列表。

        查询评估项目列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEvaluationProjects
        :type request: :class:`huaweicloudsdkugo.v1.ListEvaluationProjectsRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListEvaluationProjectsResponse`
        """
        return self.list_evaluation_projects_with_http_info(request)

    def list_evaluation_projects_with_http_info(self, request):
        all_params = ['evaluation_project_name', 'evaluation_project_status', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'evaluation_project_name' in local_var_params:
            query_params.append(('evaluation_project_name', local_var_params['evaluation_project_name']))
        if 'evaluation_project_status' in local_var_params:
            query_params.append(('evaluation_project_status', local_var_params['evaluation_project_status']))
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
            resource_path='/v1/{project_id}/evaluation-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEvaluationProjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_migration_projects(self, request):
        """查询迁移项目列表。

        查询迁移项目列表。创建迁移项目之后，调用该接口，根据项目名称，获取项目ID。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMigrationProjects
        :type request: :class:`huaweicloudsdkugo.v1.ListMigrationProjectsRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListMigrationProjectsResponse`
        """
        return self.list_migration_projects_with_http_info(request)

    def list_migration_projects_with_http_info(self, request):
        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

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
            resource_path='/v1/{project_id}/migration-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMigrationProjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_permission_check_result(self, request):
        """查询权限检查结果。

        查询权限检查结果。permission_check_status 为 \&quot;SUCCESS\&quot; 或者 \&quot;FAILED\&quot; 时，才能调用该接口。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPermissionCheckResult
        :type request: :class:`huaweicloudsdkugo.v1.ListPermissionCheckResultRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListPermissionCheckResultResponse`
        """
        return self.list_permission_check_result_with_http_info(request)

    def list_permission_check_result_with_http_info(self, request):
        all_params = ['migration_project_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/permission-result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPermissionCheckResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas(self, request):
        """查询配额。

        查询单租户的配额，包括评估项目配额、迁移项目配额。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkugo.v1.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListQuotasResponse`
        """
        return self.list_quotas_with_http_info(request)

    def list_quotas_with_http_info(self, request):
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_syntax_conversion_progress(self, request):
        """查询语法转换的进度。

        查询语法转换的进度。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSyntaxConversionProgress
        :type request: :class:`huaweicloudsdkugo.v1.ListSyntaxConversionProgressRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListSyntaxConversionProgressResponse`
        """
        return self.list_syntax_conversion_progress_with_http_info(request)

    def list_syntax_conversion_progress_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/syntax-conversion-progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSyntaxConversionProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_verification_progress(self, request):
        """查询验证进度。

        查询验证进度。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListVerificationProgress
        :type request: :class:`huaweicloudsdkugo.v1.ListVerificationProgressRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListVerificationProgressResponse`
        """
        return self.list_verification_progress_with_http_info(request)

    def list_verification_progress_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/verification-progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVerificationProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_evaluation_project_detail(self, request):
        """查询评估项目详情。

        查询评估项目详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowEvaluationProjectDetail
        :type request: :class:`huaweicloudsdkugo.v1.ShowEvaluationProjectDetailRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowEvaluationProjectDetailResponse`
        """
        return self.show_evaluation_project_detail_with_http_info(request)

    def show_evaluation_project_detail_with_http_info(self, request):
        all_params = ['evaluation_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'evaluation_project_id' in local_var_params:
            path_params['evaluation_project_id'] = local_var_params['evaluation_project_id']

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
            resource_path='/v1/{project_id}/evaluation-projects/{evaluation_project_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEvaluationProjectDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_evaluation_project_status(self, request):
        """查询评估项目状态。

        查询评估项目状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowEvaluationProjectStatus
        :type request: :class:`huaweicloudsdkugo.v1.ShowEvaluationProjectStatusRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowEvaluationProjectStatusResponse`
        """
        return self.show_evaluation_project_status_with_http_info(request)

    def show_evaluation_project_status_with_http_info(self, request):
        all_params = ['evaluation_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'evaluation_project_id' in local_var_params:
            path_params['evaluation_project_id'] = local_var_params['evaluation_project_id']

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
            resource_path='/v1/{project_id}/evaluation-projects/{evaluation_project_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEvaluationProjectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_migration_project_detail(self, request):
        """查询迁移项目详情。

        查询迁移项目详情。只有migration_project_status为\&quot;READY\&quot;时才能调用该接口。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMigrationProjectDetail
        :type request: :class:`huaweicloudsdkugo.v1.ShowMigrationProjectDetailRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowMigrationProjectDetailResponse`
        """
        return self.show_migration_project_detail_with_http_info(request)

    def show_migration_project_detail_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMigrationProjectDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_migration_project_status(self, request):
        """查询迁移项目状态。

        查询迁移项目状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMigrationProjectStatus
        :type request: :class:`huaweicloudsdkugo.v1.ShowMigrationProjectStatusRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowMigrationProjectStatusResponse`
        """
        return self.show_migration_project_status_with_http_info(request)

    def show_migration_project_status_with_http_info(self, request):
        all_params = ['migration_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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
            resource_path='/v1/{project_id}/migration-projects/{migration_project_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMigrationProjectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_versions(self, request):
        """查询API版本信息列表。

        查询API版本信息列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkugo.v1.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListApiVersionsResponse`
        """
        return self.list_api_versions_with_http_info(request)

    def list_api_versions_with_http_info(self, request):
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api_version_info(self, request):
        """查询指定版本号的API版本信息。

        查询指定版本号的API版本信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowApiVersionInfo
        :type request: :class:`huaweicloudsdkugo.v1.ShowApiVersionInfoRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowApiVersionInfoResponse`
        """
        return self.show_api_version_info_with_http_info(request)

    def show_api_version_info_with_http_info(self, request):
        all_params = ['api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

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
            resource_path='/{api_version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApiVersionInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_sql_conversion(self, request):
        """SQL语句转换。

        SQL语句转换。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunSqlConversion
        :type request: :class:`huaweicloudsdkugo.v1.RunSqlConversionRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.RunSqlConversionResponse`
        """
        return self.run_sql_conversion_with_http_info(request)

    def run_sql_conversion_with_http_info(self, request):
        all_params = ['sql_convert_req']
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
            resource_path='/v1/{project_id}/sql-conversion',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunSqlConversionResponse',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
