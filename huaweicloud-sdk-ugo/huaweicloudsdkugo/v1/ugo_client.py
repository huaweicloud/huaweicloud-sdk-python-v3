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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkugo'")


class UgoClient(Client):
    def __init__(self):
        super(UgoClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkugo.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "UgoClient":
                raise TypeError("client type error, support client type is UgoClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def check_permission(self, request):
        """目标库权限检查。

        目标库权限检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckPermission
        :type request: :class:`huaweicloudsdkugo.v1.CheckPermissionRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CheckPermissionResponse`
        """
        http_info = self._check_permission_http_info(request)
        return self._call_api(**http_info)

    def check_permission_invoker(self, request):
        http_info = self._check_permission_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_permission_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/permission-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def commit_syntax_conversion(self, request):
        """提交语法转换

        提交语法转换。只有migration_project_status为\&quot;READY\&quot;时才能调用该接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CommitSyntaxConversion
        :type request: :class:`huaweicloudsdkugo.v1.CommitSyntaxConversionRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CommitSyntaxConversionResponse`
        """
        http_info = self._commit_syntax_conversion_http_info(request)
        return self._call_api(**http_info)

    def commit_syntax_conversion_invoker(self, request):
        http_info = self._commit_syntax_conversion_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _commit_syntax_conversion_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/syntax-conversion",
            "request_type": request.__class__.__name__,
            "response_type": "CommitSyntaxConversionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def commit_verification(self, request):
        """提交验证。

        提交验证。语法转换完成后，才能调用该接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CommitVerification
        :type request: :class:`huaweicloudsdkugo.v1.CommitVerificationRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CommitVerificationResponse`
        """
        http_info = self._commit_verification_http_info(request)
        return self._call_api(**http_info)

    def commit_verification_invoker(self, request):
        http_info = self._commit_verification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _commit_verification_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/verification",
            "request_type": request.__class__.__name__,
            "response_type": "CommitVerificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def confirm_target_db_type(self, request):
        """评估项目确认目标数据库类型。

        评估项目确认目标数据库类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmTargetDbType
        :type request: :class:`huaweicloudsdkugo.v1.ConfirmTargetDbTypeRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ConfirmTargetDbTypeResponse`
        """
        http_info = self._confirm_target_db_type_http_info(request)
        return self._call_api(**http_info)

    def confirm_target_db_type_invoker(self, request):
        http_info = self._confirm_target_db_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _confirm_target_db_type_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/evaluation-projects/target-confirmation",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmTargetDbTypeResponse"
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

    def create_evaluation_project(self, request):
        """创建评估项目。

        创建评估项目。评估项目分2个阶段：采集、评估。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEvaluationProject
        :type request: :class:`huaweicloudsdkugo.v1.CreateEvaluationProjectRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CreateEvaluationProjectResponse`
        """
        http_info = self._create_evaluation_project_http_info(request)
        return self._call_api(**http_info)

    def create_evaluation_project_invoker(self, request):
        http_info = self._create_evaluation_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_evaluation_project_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/evaluation-projects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEvaluationProjectResponse"
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

    def create_migration_project(self, request):
        """创建迁移项目。

        创建迁移项目。创建迁移项目需要关联状态为“COMPLETED”的评估项目。迁移项目依次经历以下几个阶段：目标库权限检查、语法转换、验证、下载迁移失败的报告、删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMigrationProject
        :type request: :class:`huaweicloudsdkugo.v1.CreateMigrationProjectRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.CreateMigrationProjectResponse`
        """
        http_info = self._create_migration_project_http_info(request)
        return self._call_api(**http_info)

    def create_migration_project_invoker(self, request):
        http_info = self._create_migration_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_migration_project_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/migration-projects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMigrationProjectResponse"
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

    def delete_evaluation_project(self, request):
        """删除评估项目。

        删除评估项目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEvaluationProject
        :type request: :class:`huaweicloudsdkugo.v1.DeleteEvaluationProjectRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.DeleteEvaluationProjectResponse`
        """
        http_info = self._delete_evaluation_project_http_info(request)
        return self._call_api(**http_info)

    def delete_evaluation_project_invoker(self, request):
        http_info = self._delete_evaluation_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_evaluation_project_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/evaluation-projects/{evaluation_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEvaluationProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluation_project_id' in local_var_params:
            path_params['evaluation_project_id'] = local_var_params['evaluation_project_id']

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

    def delete_migration_project(self, request):
        """删除迁移项目

        删除迁移项目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMigrationProject
        :type request: :class:`huaweicloudsdkugo.v1.DeleteMigrationProjectRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.DeleteMigrationProjectResponse`
        """
        http_info = self._delete_migration_project_http_info(request)
        return self._call_api(**http_info)

    def delete_migration_project_invoker(self, request):
        http_info = self._delete_migration_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_migration_project_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMigrationProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def download_failure_report(self, request):
        """下载迁移错误报告。

        下载迁移错误报告。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadFailureReport
        :type request: :class:`huaweicloudsdkugo.v1.DownloadFailureReportRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.DownloadFailureReportResponse`
        """
        http_info = self._download_failure_report_http_info(request)
        return self._call_api(**http_info)

    def download_failure_report_invoker(self, request):
        http_info = self._download_failure_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_failure_report_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/download-failure-report",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadFailureReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def list_evaluation_projects(self, request):
        """查询评估项目列表。

        查询评估项目列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEvaluationProjects
        :type request: :class:`huaweicloudsdkugo.v1.ListEvaluationProjectsRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListEvaluationProjectsResponse`
        """
        http_info = self._list_evaluation_projects_http_info(request)
        return self._call_api(**http_info)

    def list_evaluation_projects_invoker(self, request):
        http_info = self._list_evaluation_projects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_evaluation_projects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/evaluation-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListEvaluationProjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_migration_projects(self, request):
        """查询迁移项目列表。

        查询迁移项目列表。创建迁移项目之后，调用该接口，根据项目名称，获取项目ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMigrationProjects
        :type request: :class:`huaweicloudsdkugo.v1.ListMigrationProjectsRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListMigrationProjectsResponse`
        """
        http_info = self._list_migration_projects_http_info(request)
        return self._call_api(**http_info)

    def list_migration_projects_invoker(self, request):
        http_info = self._list_migration_projects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_migration_projects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/migration-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListMigrationProjectsResponse"
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

    def list_permission_check_result(self, request):
        """查询权限检查结果。

        查询权限检查结果。permission_check_status 为 \&quot;SUCCESS\&quot; 或者 \&quot;FAILED\&quot; 时，才能调用该接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPermissionCheckResult
        :type request: :class:`huaweicloudsdkugo.v1.ListPermissionCheckResultRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListPermissionCheckResultResponse`
        """
        http_info = self._list_permission_check_result_http_info(request)
        return self._call_api(**http_info)

    def list_permission_check_result_invoker(self, request):
        http_info = self._list_permission_check_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_permission_check_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/permission-result",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermissionCheckResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_quotas(self, request):
        """查询配额。

        查询单租户的配额，包括评估项目配额、迁移项目配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkugo.v1.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
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

    def list_syntax_conversion_progress(self, request):
        """查询语法转换的进度。

        查询语法转换的进度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSyntaxConversionProgress
        :type request: :class:`huaweicloudsdkugo.v1.ListSyntaxConversionProgressRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListSyntaxConversionProgressResponse`
        """
        http_info = self._list_syntax_conversion_progress_http_info(request)
        return self._call_api(**http_info)

    def list_syntax_conversion_progress_invoker(self, request):
        http_info = self._list_syntax_conversion_progress_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_syntax_conversion_progress_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/syntax-conversion-progress",
            "request_type": request.__class__.__name__,
            "response_type": "ListSyntaxConversionProgressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def list_verification_progress(self, request):
        """查询验证进度。

        查询验证进度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVerificationProgress
        :type request: :class:`huaweicloudsdkugo.v1.ListVerificationProgressRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListVerificationProgressResponse`
        """
        http_info = self._list_verification_progress_http_info(request)
        return self._call_api(**http_info)

    def list_verification_progress_invoker(self, request):
        http_info = self._list_verification_progress_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_verification_progress_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/verification-progress",
            "request_type": request.__class__.__name__,
            "response_type": "ListVerificationProgressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def show_evaluation_project_detail(self, request):
        """查询评估项目详情。

        查询评估项目详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEvaluationProjectDetail
        :type request: :class:`huaweicloudsdkugo.v1.ShowEvaluationProjectDetailRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowEvaluationProjectDetailResponse`
        """
        http_info = self._show_evaluation_project_detail_http_info(request)
        return self._call_api(**http_info)

    def show_evaluation_project_detail_invoker(self, request):
        http_info = self._show_evaluation_project_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_evaluation_project_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/evaluation-projects/{evaluation_project_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEvaluationProjectDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluation_project_id' in local_var_params:
            path_params['evaluation_project_id'] = local_var_params['evaluation_project_id']

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

    def show_evaluation_project_status(self, request):
        """查询评估项目状态。

        查询评估项目状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEvaluationProjectStatus
        :type request: :class:`huaweicloudsdkugo.v1.ShowEvaluationProjectStatusRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowEvaluationProjectStatusResponse`
        """
        http_info = self._show_evaluation_project_status_http_info(request)
        return self._call_api(**http_info)

    def show_evaluation_project_status_invoker(self, request):
        http_info = self._show_evaluation_project_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_evaluation_project_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/evaluation-projects/{evaluation_project_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEvaluationProjectStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluation_project_id' in local_var_params:
            path_params['evaluation_project_id'] = local_var_params['evaluation_project_id']

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

    def show_migration_project_detail(self, request):
        """查询迁移项目详情。

        查询迁移项目详情。只有migration_project_status为\&quot;READY\&quot;时才能调用该接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMigrationProjectDetail
        :type request: :class:`huaweicloudsdkugo.v1.ShowMigrationProjectDetailRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowMigrationProjectDetailResponse`
        """
        http_info = self._show_migration_project_detail_http_info(request)
        return self._call_api(**http_info)

    def show_migration_project_detail_invoker(self, request):
        http_info = self._show_migration_project_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_migration_project_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMigrationProjectDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def show_migration_project_status(self, request):
        """查询迁移项目状态。

        查询迁移项目状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMigrationProjectStatus
        :type request: :class:`huaweicloudsdkugo.v1.ShowMigrationProjectStatusRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowMigrationProjectStatusResponse`
        """
        http_info = self._show_migration_project_status_http_info(request)
        return self._call_api(**http_info)

    def show_migration_project_status_invoker(self, request):
        http_info = self._show_migration_project_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_migration_project_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/migration-projects/{migration_project_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMigrationProjectStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'migration_project_id' in local_var_params:
            path_params['migration_project_id'] = local_var_params['migration_project_id']

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

    def list_api_versions(self, request):
        """查询API版本信息列表。

        查询API版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkugo.v1.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsResponse"
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

    def show_api_version_info(self, request):
        """查询指定版本号的API版本信息。

        查询指定版本号的API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiVersionInfo
        :type request: :class:`huaweicloudsdkugo.v1.ShowApiVersionInfoRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.ShowApiVersionInfoResponse`
        """
        http_info = self._show_api_version_info_http_info(request)
        return self._call_api(**http_info)

    def show_api_version_info_invoker(self, request):
        http_info = self._show_api_version_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_api_version_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{api_version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiVersionInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

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

    def run_sql_conversion(self, request):
        """SQL语句转换。

        SQL语句转换。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSqlConversion
        :type request: :class:`huaweicloudsdkugo.v1.RunSqlConversionRequest`
        :rtype: :class:`huaweicloudsdkugo.v1.RunSqlConversionResponse`
        """
        http_info = self._run_sql_conversion_http_info(request)
        return self._call_api(**http_info)

    def run_sql_conversion_invoker(self, request):
        http_info = self._run_sql_conversion_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_sql_conversion_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sql-conversion",
            "request_type": request.__class__.__name__,
            "response_type": "RunSqlConversionResponse"
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
