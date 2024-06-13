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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcloudtest'")


class CloudtestClient(Client):
    def __init__(self):
        super(CloudtestClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudtest.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CloudtestClient":
                raise TypeError("client type error, support client type is CloudtestClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_add_relations_by_one_case(self, request):
        """添加需求/缺陷和多个用例关联关系

        添加需求/缺陷和多个用例关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddRelationsByOneCase
        :type request: :class:`huaweicloudsdkcloudtest.v1.BatchAddRelationsByOneCaseRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.BatchAddRelationsByOneCaseResponse`
        """
        http_info = self._batch_add_relations_by_one_case_http_info(request)
        return self._call_api(**http_info)

    def batch_add_relations_by_one_case_invoker(self, request):
        http_info = self._batch_add_relations_by_one_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_relations_by_one_case_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/testrelation/v4/workitems/{workitem_id}/relations",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddRelationsByOneCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workitem_id' in local_var_params:
            path_params['workitem_id'] = local_var_params['workitem_id']

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

    def batch_delete_test_case(self, request):
        """批量删除自定义测试服务类型用例

        批量删除自定义测试服务类型用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTestCase
        :type request: :class:`huaweicloudsdkcloudtest.v1.BatchDeleteTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.BatchDeleteTestCaseResponse`
        """
        http_info = self._batch_delete_test_case_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_test_case_invoker(self, request):
        http_info = self._batch_delete_test_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_test_case_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{project_id}/testcases/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTestCaseResponse"
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

    def batch_delete_test_report(self, request):
        """根据测试报告uri列表，删除测试报告

        根据测试报告uri列表，删除测试报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTestReport
        :type request: :class:`huaweicloudsdkcloudtest.v1.BatchDeleteTestReportRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.BatchDeleteTestReportResponse`
        """
        http_info = self._batch_delete_test_report_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_test_report_invoker(self, request):
        http_info = self._batch_delete_test_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_test_report_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/testreport/v4/{project_id}/test-reports/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTestReportResponse"
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

    def check_permission(self, request):
        """检查项目权限

        检查项目权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckPermission
        :type request: :class:`huaweicloudsdkcloudtest.v1.CheckPermissionRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CheckPermissionResponse`
        """
        http_info = self._check_permission_http_info(request)
        return self._call_api(**http_info)

    def check_permission_invoker(self, request):
        http_info = self._check_permission_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_permission_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/permission/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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

    def create_plan(self, request):
        """项目下创建计划

        项目下创建计划
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlan
        :type request: :class:`huaweicloudsdkcloudtest.v1.CreatePlanRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreatePlanResponse`
        """
        http_info = self._create_plan_http_info(request)
        return self._call_api(**http_info)

    def create_plan_invoker(self, request):
        http_info = self._create_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_plan_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{project_id}/plans",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlanResponse"
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

    def create_relations_by_one_case(self, request):
        """添加一个用例和多个需求/缺陷关联关系

        添加一个用例和多个需求/缺陷关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRelationsByOneCase
        :type request: :class:`huaweicloudsdkcloudtest.v1.CreateRelationsByOneCaseRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateRelationsByOneCaseResponse`
        """
        http_info = self._create_relations_by_one_case_http_info(request)
        return self._call_api(**http_info)

    def create_relations_by_one_case_invoker(self, request):
        http_info = self._create_relations_by_one_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_relations_by_one_case_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/testrelation/v4/testcases/{case_id}/relations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRelationsByOneCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

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

    def create_resource_uri(self, request):
        """生成资源URI

        生成资源URI
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResourceUri
        :type request: :class:`huaweicloudsdkcloudtest.v1.CreateResourceUriRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateResourceUriResponse`
        """
        http_info = self._create_resource_uri_http_info(request)
        return self._call_api(**http_info)

    def create_resource_uri_invoker(self, request):
        http_info = self._create_resource_uri_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_resource_uri_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/GT3KServer/v4/{project_id}/resource-uri",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceUriResponse"
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

    def create_service(self, request):
        """新测试类型服务注册

        通过接口CreateService注册成为自定义服务。 注册完成后界面将会出现此自定义测试类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateService
        :type request: :class:`huaweicloudsdkcloudtest.v1.CreateServiceRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateServiceResponse`
        """
        http_info = self._create_service_http_info(request)
        return self._call_api(**http_info)

    def create_service_invoker(self, request):
        http_info = self._create_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_service_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/services",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServiceResponse"
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

    def create_test_case(self, request):
        """创建自定义测试服务类型用例

        创建自定义测试服务类型用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTestCase
        :type request: :class:`huaweicloudsdkcloudtest.v1.CreateTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateTestCaseResponse`
        """
        http_info = self._create_test_case_http_info(request)
        return self._call_api(**http_info)

    def create_test_case_invoker(self, request):
        http_info = self._create_test_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_test_case_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{project_id}/testcases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTestCaseResponse"
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

    def create_test_case_in_plan(self, request):
        """计划中批量添加测试用例

        计划中批量添加测试用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTestCaseInPlan
        :type request: :class:`huaweicloudsdkcloudtest.v1.CreateTestCaseInPlanRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateTestCaseInPlanResponse`
        """
        http_info = self._create_test_case_in_plan_http_info(request)
        return self._call_api(**http_info)

    def create_test_case_in_plan_invoker(self, request):
        http_info = self._create_test_case_in_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_test_case_in_plan_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{project_id}/plans/{plan_id}/testcases/batch-add",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTestCaseInPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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

    def delete_relations_by_one_case(self, request):
        """删除一个用例和多个需求/缺陷关联关系

        删除一个用例和多个需求/缺陷关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRelationsByOneCase
        :type request: :class:`huaweicloudsdkcloudtest.v1.DeleteRelationsByOneCaseRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.DeleteRelationsByOneCaseResponse`
        """
        http_info = self._delete_relations_by_one_case_http_info(request)
        return self._call_api(**http_info)

    def delete_relations_by_one_case_invoker(self, request):
        http_info = self._delete_relations_by_one_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_relations_by_one_case_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/testrelation/v4/testcases/{case_id}/relations",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRelationsByOneCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

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

    def delete_service(self, request):
        """删除已注册服务

        删除已注册服务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteService
        :type request: :class:`huaweicloudsdkcloudtest.v1.DeleteServiceRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.DeleteServiceResponse`
        """
        http_info = self._delete_service_http_info(request)
        return self._call_api(**http_info)

    def delete_service_invoker(self, request):
        http_info = self._delete_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_service_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def list_all_branches(self, request):
        """获取分支列表

        获取分支列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllBranches
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListAllBranchesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListAllBranchesResponse`
        """
        http_info = self._list_all_branches_http_info(request)
        return self._call_api(**http_info)

    def list_all_branches_invoker(self, request):
        http_info = self._list_all_branches_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_branches_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/branches",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllBranchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_uuid' in local_var_params:
            query_params.append(('project_uuid', local_var_params['project_uuid']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))

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

    def list_all_iterators(self, request):
        """查询项目下所有迭代计划

        查询项目下所有迭代计划
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllIterators
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListAllIteratorsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListAllIteratorsResponse`
        """
        http_info = self._list_all_iterators_http_info(request)
        return self._call_api(**http_info)

    def list_all_iterators_invoker(self, request):
        http_info = self._list_all_iterators_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_iterators_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/projects/{project_id}/iterator-infos",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllIteratorsResponse"
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

    def list_attachments(self, request):
        """查询附件列表

        查询附件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttachments
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListAttachmentsResponse`
        """
        http_info = self._list_attachments_http_info(request)
        return self._call_api(**http_info)

    def list_attachments_invoker(self, request):
        http_info = self._list_attachments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_attachments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/{project_id}/resources/{resource_uri}/attachments",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttachmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_uri' in local_var_params:
            path_params['resource_uri'] = local_var_params['resource_uri']

        query_params = []
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

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

    def list_branches(self, request):
        """获取分支列表

        获取分支列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBranches
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListBranchesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListBranchesResponse`
        """
        http_info = self._list_branches_http_info(request)
        return self._call_api(**http_info)

    def list_branches_invoker(self, request):
        http_info = self._list_branches_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_branches_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/branches",
            "request_type": request.__class__.__name__,
            "response_type": "ListBranchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
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

    def list_issue_tree(self, request):
        """查询需求树

        查询需求树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueTree
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListIssueTreeRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListIssueTreeResponse`
        """
        http_info = self._list_issue_tree_http_info(request)
        return self._call_api(**http_info)

    def list_issue_tree_invoker(self, request):
        http_info = self._list_issue_tree_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issue_tree_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/GT3KServer/v4/{project_id}/versions/{version_id}/issue-tree",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssueTreeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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

    def list_project_field_configs(self, request):
        """查询项目字段配置

        查询项目字段配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectFieldConfigs
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListProjectFieldConfigsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListProjectFieldConfigsResponse`
        """
        http_info = self._list_project_field_configs_http_info(request)
        return self._call_api(**http_info)

    def list_project_field_configs_invoker(self, request):
        http_info = self._list_project_field_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_field_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/projects/{project_id}/field-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectFieldConfigsResponse"
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

    def list_project_test_case_fields(self, request):
        """获取项目测试用例自定义字段列表

        获取项目测试用例自定义字段列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTestCaseFields
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListProjectTestCaseFieldsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListProjectTestCaseFieldsResponse`
        """
        http_info = self._list_project_test_case_fields_http_info(request)
        return self._call_api(**http_info)

    def list_project_test_case_fields_invoker(self, request):
        http_info = self._list_project_test_case_fields_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_test_case_fields_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/{project_id}/testcase/field/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTestCaseFieldsResponse"
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

    def list_reports(self, request):
        """页面报表展示

        页面报表展示
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReports
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListReportsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListReportsResponse`
        """
        http_info = self._list_reports_http_info(request)
        return self._call_api(**http_info)

    def list_reports_invoker(self, request):
        http_info = self._list_reports_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_reports_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/testreport/v4/{project_id}/versions/{version_id}/custom-reports",
            "request_type": request.__class__.__name__,
            "response_type": "ListReportsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_resource_pools(self, request):
        """获取资源池列表

        获取资源池列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourcePools
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListResourcePoolsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListResourcePoolsResponse`
        """
        http_info = self._list_resource_pools_http_info(request)
        return self._call_api(**http_info)

    def list_resource_pools_invoker(self, request):
        http_info = self._list_resource_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/testexecutor/v4/{project_id}/resource-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcePoolsResponse"
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

    def list_task_test_cases(self, request):
        """查询用例关联的测试任务列表

        查询用例关联的测试任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskTestCases
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListTaskTestCasesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListTaskTestCasesResponse`
        """
        http_info = self._list_task_test_cases_http_info(request)
        return self._call_api(**http_info)

    def list_task_test_cases_invoker(self, request):
        http_info = self._list_task_test_cases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_task_test_cases_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/GT3KServer/v4/{project_id}/testcases/tasks/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTaskTestCasesResponse"
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

    def list_test_case_histories(self, request):
        """查询用例修改历史记录

        查询用例修改历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTestCaseHistories
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListTestCaseHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListTestCaseHistoriesResponse`
        """
        http_info = self._list_test_case_histories_http_info(request)
        return self._call_api(**http_info)

    def list_test_case_histories_invoker(self, request):
        http_info = self._list_test_case_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_test_case_histories_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/testcases/{testcase_id}/histories/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTestCaseHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'testcase_id' in local_var_params:
            path_params['testcase_id'] = local_var_params['testcase_id']

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

    def list_test_cases(self, request):
        """查询用例列表

        查询用例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTestCases
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListTestCasesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListTestCasesResponse`
        """
        http_info = self._list_test_cases_http_info(request)
        return self._call_api(**http_info)

    def list_test_cases_invoker(self, request):
        http_info = self._list_test_cases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_test_cases_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/testcases/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTestCasesResponse"
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

    def list_test_reports_by_condition(self, request):
        """根据查询条件获取测试报告列表

        根据查询条件获取测试报告列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTestReportsByCondition
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListTestReportsByConditionRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListTestReportsByConditionResponse`
        """
        http_info = self._list_test_reports_by_condition_http_info(request)
        return self._call_api(**http_info)

    def list_test_reports_by_condition_invoker(self, request):
        http_info = self._list_test_reports_by_condition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_test_reports_by_condition_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/testreport/v4/{project_id}/test-reports",
            "request_type": request.__class__.__name__,
            "response_type": "ListTestReportsByConditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'own' in local_var_params:
            query_params.append(('own', local_var_params['own']))

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

    def list_test_types(self, request):
        """获取测试类型列表

        获取测试类型列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTestTypes
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListTestTypesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListTestTypesResponse`
        """
        http_info = self._list_test_types_http_info(request)
        return self._call_api(**http_info)

    def list_test_types_invoker(self, request):
        http_info = self._list_test_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_test_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/{project_id}/test-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListTestTypesResponse"
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

    def list_testcases_by_project_issues_relation(self, request):
        """查询项目下关联了需求的用例列表

        查询项目下关联了需求的用例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTestcasesByProjectIssuesRelation
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListTestcasesByProjectIssuesRelationRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListTestcasesByProjectIssuesRelationResponse`
        """
        http_info = self._list_testcases_by_project_issues_relation_http_info(request)
        return self._call_api(**http_info)

    def list_testcases_by_project_issues_relation_invoker(self, request):
        http_info = self._list_testcases_by_project_issues_relation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_testcases_by_project_issues_relation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/issues/testcases/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTestcasesByProjectIssuesRelationResponse"
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

    def list_usage_infos(self, request):
        """获取租户订单已用资源信息

        获取租户订单已用资源信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsageInfos
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListUsageInfosRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListUsageInfosResponse`
        """
        http_info = self._list_usage_infos_http_info(request)
        return self._call_api(**http_info)

    def list_usage_infos_invoker(self, request):
        http_info = self._list_usage_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_usage_infos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/domain/usage",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsageInfosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_uuid' in local_var_params:
            query_params.append(('project_uuid', local_var_params['project_uuid']))

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

    def list_user_package_usage(self, request):
        """ListUserPackageUsage

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserPackageUsage
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListUserPackageUsageRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListUserPackageUsageResponse`
        """
        http_info = self._list_user_package_usage_http_info(request)
        return self._call_api(**http_info)

    def list_user_package_usage_invoker(self, request):
        http_info = self._list_user_package_usage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_package_usage_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_id}/package-usage",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserPackageUsageResponse"
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

    def list_user_popup_info(self, request):
        """ListUserPopupInfo

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserPopupInfo
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListUserPopupInfoRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListUserPopupInfoResponse`
        """
        http_info = self._list_user_popup_info_http_info(request)
        return self._call_api(**http_info)

    def list_user_popup_info_invoker(self, request):
        http_info = self._list_user_popup_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_popup_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_id}/package-charge/popup",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserPopupInfoResponse"
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

    def run_test_case(self, request):
        """批量执行测试用例

        批量执行测试用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTestCase
        :type request: :class:`huaweicloudsdkcloudtest.v1.RunTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.RunTestCaseResponse`
        """
        http_info = self._run_test_case_http_info(request)
        return self._call_api(**http_info)

    def run_test_case_invoker(self, request):
        http_info = self._run_test_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_test_case_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{project_id}/testcases/execution",
            "request_type": request.__class__.__name__,
            "response_type": "RunTestCaseResponse"
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

    def show_all_feature_children(self, request):
        """获取特性树V5

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllFeatureChildren
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowAllFeatureChildrenRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowAllFeatureChildrenResponse`
        """
        http_info = self._show_all_feature_children_http_info(request)
        return self._call_api(**http_info)

    def show_all_feature_children_invoker(self, request):
        http_info = self._show_all_feature_children_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_all_feature_children_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/GT3KServer/v5/features/{feature_id}/children",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllFeatureChildrenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'feature_id' in local_var_params:
            path_params['feature_id'] = local_var_params['feature_id']

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

    def show_api_testcase_histories(self, request):
        """获取用例历史执行数据

        获取用例历史执行数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiTestcaseHistories
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowApiTestcaseHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowApiTestcaseHistoriesResponse`
        """
        http_info = self._show_api_testcase_histories_http_info(request)
        return self._call_api(**http_info)

    def show_api_testcase_histories_invoker(self, request):
        http_info = self._show_api_testcase_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_api_testcase_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/api-testcases/{testcase_id}/execute-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiTestcaseHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'testcase_id' in local_var_params:
            path_params['testcase_id'] = local_var_params['testcase_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'plan_id' in local_var_params:
            query_params.append(('plan_id', local_var_params['plan_id']))

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

    def show_background_info(self, request):
        """获取测试报告的模板设置

        获取测试报告的模板设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackgroundInfo
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowBackgroundInfoRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowBackgroundInfoResponse`
        """
        http_info = self._show_background_info_http_info(request)
        return self._call_api(**http_info)

    def show_background_info_invoker(self, request):
        http_info = self._show_background_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_background_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/{project_id}/background",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackgroundInfoResponse"
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

    def show_disclaimer_record(self, request):
        """查询用户免责声明

        查询用户免责声明
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDisclaimerRecord
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowDisclaimerRecordRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowDisclaimerRecordResponse`
        """
        http_info = self._show_disclaimer_record_http_info(request)
        return self._call_api(**http_info)

    def show_disclaimer_record_invoker(self, request):
        http_info = self._show_disclaimer_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_disclaimer_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/disclaimer",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDisclaimerRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def show_domain_info(self, request):
        """根据domainId获取加密的testbirdkey

        根据domainId获取加密的testbirdkey
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainInfo
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowDomainInfoRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowDomainInfoResponse`
        """
        http_info = self._show_domain_info_http_info(request)
        return self._call_api(**http_info)

    def show_domain_info_invoker(self, request):
        http_info = self._show_domain_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/user-info/domain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainInfoResponse"
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

    def show_feature_children(self, request):
        """获取目录\\特性树

        获取目录\\特性树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFeatureChildren
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowFeatureChildrenRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowFeatureChildrenResponse`
        """
        http_info = self._show_feature_children_http_info(request)
        return self._call_api(**http_info)

    def show_feature_children_invoker(self, request):
        http_info = self._show_feature_children_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_feature_children_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/GT3KServer/v4/features/{feature_id}/children",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFeatureChildrenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'feature_id' in local_var_params:
            path_params['feature_id'] = local_var_params['feature_id']

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

    def show_free_declaration(self, request):
        """查询限时免费用户免责声明记录

        查询限时免费用户免责声明记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFreeDeclaration
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowFreeDeclarationRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowFreeDeclarationResponse`
        """
        http_info = self._show_free_declaration_http_info(request)
        return self._call_api(**http_info)

    def show_free_declaration_invoker(self, request):
        http_info = self._show_free_declaration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_free_declaration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/free-declaration",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFreeDeclarationResponse"
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

    def show_issues_by_plan_id(self, request):
        """查询某个测试计划下的需求树

        查询某个测试计划下的需求列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIssuesByPlanId
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowIssuesByPlanIdRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowIssuesByPlanIdResponse`
        """
        http_info = self._show_issues_by_plan_id_http_info(request)
        return self._call_api(**http_info)

    def show_issues_by_plan_id_invoker(self, request):
        http_info = self._show_issues_by_plan_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_issues_by_plan_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_id}/plans/{plan_id}/issues",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIssuesByPlanIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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

    def show_iterator_by_defect(self, request):
        """查询缺陷相关联测试计划

        查询缺陷相关联测试计划
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIteratorByDefect
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowIteratorByDefectRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowIteratorByDefectResponse`
        """
        http_info = self._show_iterator_by_defect_http_info(request)
        return self._call_api(**http_info)

    def show_iterator_by_defect_invoker(self, request):
        http_info = self._show_iterator_by_defect_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_iterator_by_defect_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/{project_id}/defects/{defect_id}/iterators",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIteratorByDefectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'defect_id' in local_var_params:
            path_params['defect_id'] = local_var_params['defect_id']

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

    def show_mindmap_by_page(self, request):
        """根据条件分页获取脑图对象V3

        根据条件分页获取脑图对象V3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMindmapByPage
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowMindmapByPageRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowMindmapByPageResponse`
        """
        http_info = self._show_mindmap_by_page_http_info(request)
        return self._call_api(**http_info)

    def show_mindmap_by_page_invoker(self, request):
        http_info = self._show_mindmap_by_page_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mindmap_by_page_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/mindmaps/page",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMindmapByPageResponse"
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

    def show_mindmap_creator_name(self, request):
        """获取脑图创建人V2

        获取脑图创建人V2
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMindmapCreatorName
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowMindmapCreatorNameRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowMindmapCreatorNameResponse`
        """
        http_info = self._show_mindmap_creator_name_http_info(request)
        return self._call_api(**http_info)

    def show_mindmap_creator_name_invoker(self, request):
        http_info = self._show_mindmap_creator_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mindmap_creator_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/mindmap-creator-name",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMindmapCreatorNameResponse"
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

    def show_plan_journals(self, request):
        """查询某测试计划下的操作历史

        查询某测试计划下的操作历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlanJournals
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowPlanJournalsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowPlanJournalsResponse`
        """
        http_info = self._show_plan_journals_http_info(request)
        return self._call_api(**http_info)

    def show_plan_journals_invoker(self, request):
        http_info = self._show_plan_journals_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_plan_journals_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_id}/plans/{plan_id}/journals",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlanJournalsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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

    def show_plan_list(self, request):
        """项目下查询测试计划列表v2

        项目下查询测试计划列表v2
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlanList
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowPlanListRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowPlanListResponse`
        """
        http_info = self._show_plan_list_http_info(request)
        return self._call_api(**http_info)

    def show_plan_list_invoker(self, request):
        http_info = self._show_plan_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_plan_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/{project_id}/plans",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlanListResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'current_stage' in local_var_params:
            query_params.append(('current_stage', local_var_params['current_stage']))
        if 'branch_uri' in local_var_params:
            query_params.append(('branch_uri', local_var_params['branch_uri']))
        if 'query_all_version' in local_var_params:
            query_params.append(('query_all_version', local_var_params['query_all_version']))
        if 'fix_version_ids' in local_var_params:
            query_params.append(('fix_version_ids', local_var_params['fix_version_ids']))

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

    def show_plans(self, request):
        """项目下查询测试计划列表

        项目下查询测试计划列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlans
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowPlansRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowPlansResponse`
        """
        http_info = self._show_plans_http_info(request)
        return self._call_api(**http_info)

    def show_plans_invoker(self, request):
        http_info = self._show_plans_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_plans_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_id}/plans",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlansResponse"
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
        if 'current_stage' in local_var_params:
            query_params.append(('current_stage', local_var_params['current_stage']))
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

    def show_progress(self, request):
        """获取异步进度

        获取异步进度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProgress
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowProgressRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowProgressResponse`
        """
        http_info = self._show_progress_http_info(request)
        return self._call_api(**http_info)

    def show_progress_invoker(self, request):
        http_info = self._show_progress_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_progress_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/progress/{operation_uri}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProgressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'operation_uri' in local_var_params:
            path_params['operation_uri'] = local_var_params['operation_uri']

        query_params = []
        if 'project_uuid' in local_var_params:
            query_params.append(('project_uuid', local_var_params['project_uuid']))

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

    def show_project_data_dashboard(self, request):
        """查询质量报告看板统计信息

        查询质量报告看板统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectDataDashboard
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowProjectDataDashboardRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowProjectDataDashboardResponse`
        """
        http_info = self._show_project_data_dashboard_http_info(request)
        return self._call_api(**http_info)

    def show_project_data_dashboard_invoker(self, request):
        http_info = self._show_project_data_dashboard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_data_dashboard_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data-dashboard/overview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectDataDashboardResponse"
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

    def show_register_service(self, request):
        """用户获取自己当前已经注册的服务

        用户获取自己当前已经注册的服务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRegisterService
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowRegisterServiceRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowRegisterServiceResponse`
        """
        http_info = self._show_register_service_http_info(request)
        return self._call_api(**http_info)

    def show_register_service_invoker(self, request):
        http_info = self._show_register_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_register_service_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/services",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRegisterServiceResponse"
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

    def show_report(self, request):
        """实时计算单个自定义报表

        实时计算单个自定义报表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReport
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowReportRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowReportResponse`
        """
        http_info = self._show_report_http_info(request)
        return self._call_api(**http_info)

    def show_report_invoker(self, request):
        http_info = self._show_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_report_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/versions/{plan_id}/custom-reports/generate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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

    def show_requirements_overview(self, request):
        """质量报告需求测试情况统计

        质量报告需求测试情况统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRequirementsOverview
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowRequirementsOverviewRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowRequirementsOverviewResponse`
        """
        http_info = self._show_requirements_overview_http_info(request)
        return self._call_api(**http_info)

    def show_requirements_overview_invoker(self, request):
        http_info = self._show_requirements_overview_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_requirements_overview_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/testreport/v4/{project_id}/versions/{version_id}/requirements/overview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRequirementsOverviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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

    def show_system_configs(self, request):
        """根据入参动态查询系统配置中的信息

        根据入参动态查询系统配置中的信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSystemConfigs
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowSystemConfigsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowSystemConfigsResponse`
        """
        http_info = self._show_system_configs_http_info(request)
        return self._call_api(**http_info)

    def show_system_configs_invoker(self, request):
        http_info = self._show_system_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_system_configs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system-config/find-all",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSystemConfigsResponse"
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

    def show_test_case(self, request):
        """查询用例详情

        查询用例详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTestCase
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowTestCaseResponse`
        """
        http_info = self._show_test_case_http_info(request)
        return self._call_api(**http_info)

    def show_test_case_invoker(self, request):
        http_info = self._show_test_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_test_case_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/testcases/{testcase_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTestCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'testcase_id' in local_var_params:
            path_params['testcase_id'] = local_var_params['testcase_id']

        query_params = []
        if 'version_uri' in local_var_params:
            query_params.append(('version_uri', local_var_params['version_uri']))
        if 'project_uuid' in local_var_params:
            query_params.append(('project_uuid', local_var_params['project_uuid']))
        if 'task_uri' in local_var_params:
            query_params.append(('task_uri', local_var_params['task_uri']))
        if 'refresh' in local_var_params:
            query_params.append(('refresh', local_var_params['refresh']))
        if 'is_recycle' in local_var_params:
            query_params.append(('is_recycle', local_var_params['is_recycle']))

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

    def show_test_case_and_defect_info(self, request):
        """查询用户用例关联缺陷的统计信息

        查询用户用例关联缺陷的统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTestCaseAndDefectInfo
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowTestCaseAndDefectInfoRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowTestCaseAndDefectInfoResponse`
        """
        http_info = self._show_test_case_and_defect_info_http_info(request)
        return self._call_api(**http_info)

    def show_test_case_and_defect_info_invoker(self, request):
        http_info = self._show_test_case_and_defect_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_test_case_and_defect_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/testcases/defect-info/list-by-creation-time",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTestCaseAndDefectInfoResponse"
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

    def show_test_case_detail(self, request):
        """获取测试用例详情

        获取测试用例详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTestCaseDetail
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowTestCaseDetailRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowTestCaseDetailResponse`
        """
        http_info = self._show_test_case_detail_http_info(request)
        return self._call_api(**http_info)

    def show_test_case_detail_invoker(self, request):
        http_info = self._show_test_case_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_test_case_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_id}/testcases/{testcase_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTestCaseDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'testcase_id' in local_var_params:
            path_params['testcase_id'] = local_var_params['testcase_id']

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

    def show_test_case_detail_v2(self, request):
        """通过用例编号获取测试用例详情

        通过用例编号获取测试用例详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTestCaseDetailV2
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowTestCaseDetailV2Request`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowTestCaseDetailV2Response`
        """
        http_info = self._show_test_case_detail_v2_http_info(request)
        return self._call_api(**http_info)

    def show_test_case_detail_v2_invoker(self, request):
        http_info = self._show_test_case_detail_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_test_case_detail_v2_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_id}/testcase",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTestCaseDetailV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'testcase_number' in local_var_params:
            query_params.append(('testcase_number', local_var_params['testcase_number']))

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

    def show_user_access_info(self, request):
        """获取租户订单信息

        获取租户订单信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserAccessInfo
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowUserAccessInfoRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowUserAccessInfoResponse`
        """
        http_info = self._show_user_access_info_http_info(request)
        return self._call_api(**http_info)

    def show_user_access_info_invoker(self, request):
        http_info = self._show_user_access_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_access_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/GT3KServer/v4/domain/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserAccessInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_uuid' in local_var_params:
            query_params.append(('project_uuid', local_var_params['project_uuid']))

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

    def show_user_execute_test_case_info(self, request):
        """查询时段内用例的执行情况

        查询时段内用例的执行情况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserExecuteTestCaseInfo
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowUserExecuteTestCaseInfoRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowUserExecuteTestCaseInfoResponse`
        """
        http_info = self._show_user_execute_test_case_info_http_info(request)
        return self._call_api(**http_info)

    def show_user_execute_test_case_info_invoker(self, request):
        http_info = self._show_user_execute_test_case_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_execute_test_case_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/testcases/execute-info/statistic-by-user",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserExecuteTestCaseInfoResponse"
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

    def update_service(self, request):
        """更新已注册服务

        更新已注册服务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateService
        :type request: :class:`huaweicloudsdkcloudtest.v1.UpdateServiceRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.UpdateServiceResponse`
        """
        http_info = self._update_service_http_info(request)
        return self._call_api(**http_info)

    def update_service_invoker(self, request):
        http_info = self._update_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_service_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def update_test_case(self, request):
        """更新自定义测试服务类型用例

        更新自定义测试服务类型用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTestCase
        :type request: :class:`huaweicloudsdkcloudtest.v1.UpdateTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.UpdateTestCaseResponse`
        """
        http_info = self._update_test_case_http_info(request)
        return self._call_api(**http_info)

    def update_test_case_invoker(self, request):
        http_info = self._update_test_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_test_case_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/projects/{project_id}/testcases/{testcase_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTestCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'testcase_id' in local_var_params:
            path_params['testcase_id'] = local_var_params['testcase_id']

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

    def update_test_case_result(self, request):
        """批量更新测试用例结果

        批量更新测试用例结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTestCaseResult
        :type request: :class:`huaweicloudsdkcloudtest.v1.UpdateTestCaseResultRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.UpdateTestCaseResultResponse`
        """
        http_info = self._update_test_case_result_http_info(request)
        return self._call_api(**http_info)

    def update_test_case_result_invoker(self, request):
        http_info = self._update_test_case_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_test_case_result_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{project_id}/testcases/result",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTestCaseResultResponse"
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

    def list_alert_groups_by_condition(self, request):
        """查询告警组列表

        查询告警组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertGroupsByCondition
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListAlertGroupsByConditionRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListAlertGroupsByConditionResponse`
        """
        http_info = self._list_alert_groups_by_condition_http_info(request)
        return self._call_api(**http_info)

    def list_alert_groups_by_condition_invoker(self, request):
        http_info = self._list_alert_groups_by_condition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alert_groups_by_condition_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{service_id}/alert/group/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertGroupsByConditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def list_alert_templates(self, request):
        """查询告警模板

        查询告警模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertTemplates
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListAlertTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListAlertTemplatesResponse`
        """
        http_info = self._list_alert_templates_http_info(request)
        return self._call_api(**http_info)

    def list_alert_templates_invoker(self, request):
        http_info = self._list_alert_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alert_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{service_id}/alert-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'page_num' in local_var_params:
            query_params.append(('pageNum', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))

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

    def list_all_config_item_by_type(self, request):
        """查询任务告警信息

        查询任务告警信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllConfigItemByType
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListAllConfigItemByTypeRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListAllConfigItemByTypeResponse`
        """
        http_info = self._list_all_config_item_by_type_http_info(request)
        return self._call_api(**http_info)

    def list_all_config_item_by_type_invoker(self, request):
        http_info = self._list_all_config_item_by_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_config_item_by_type_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{service_id}/service/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllConfigItemByTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def save_task_setting(self, request):
        """保存任务配置

        保存任务配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveTaskSetting
        :type request: :class:`huaweicloudsdkcloudtest.v1.SaveTaskSettingRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.SaveTaskSettingResponse`
        """
        http_info = self._save_task_setting_http_info(request)
        return self._call_api(**http_info)

    def save_task_setting_invoker(self, request):
        http_info = self._save_task_setting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_task_setting_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{service_id}/task/settings",
            "request_type": request.__class__.__name__,
            "response_type": "SaveTaskSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def show_all_config_value_by_type_and_key(self, request):
        """查询任务配置

        查询任务配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllConfigValueByTypeAndKey
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowAllConfigValueByTypeAndKeyRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowAllConfigValueByTypeAndKeyResponse`
        """
        http_info = self._show_all_config_value_by_type_and_key_http_info(request)
        return self._call_api(**http_info)

    def show_all_config_value_by_type_and_key_invoker(self, request):
        http_info = self._show_all_config_value_by_type_and_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_all_config_value_by_type_and_key_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{service_id}/service/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllConfigValueByTypeAndKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
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

    def show_if_task_name_repeat(self, request):
        """查询告警模板名称是否重复

        查询告警模板名称是否重复
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIfTaskNameRepeat
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowIfTaskNameRepeatRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowIfTaskNameRepeatResponse`
        """
        http_info = self._show_if_task_name_repeat_http_info(request)
        return self._call_api(**http_info)

    def show_if_task_name_repeat_invoker(self, request):
        http_info = self._show_if_task_name_repeat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_if_task_name_repeat_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{service_id}/alert-templates/name",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIfTaskNameRepeatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
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

    def show_if_user_name_repeat(self, request):
        """查询告警组用户名是否重复

        查询告警组用户名是否重复
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIfUserNameRepeat
        :type request: :class:`huaweicloudsdkcloudtest.v1.ShowIfUserNameRepeatRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ShowIfUserNameRepeatResponse`
        """
        http_info = self._show_if_user_name_repeat_http_info(request)
        return self._call_api(**http_info)

    def show_if_user_name_repeat_invoker(self, request):
        http_info = self._show_if_user_name_repeat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_if_user_name_repeat_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{service_id}/alert/user/name",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIfUserNameRepeatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('userId', local_var_params['user_id']))
        if 'user_name' in local_var_params:
            query_params.append(('userName', local_var_params['user_name']))

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

    def create_api_test_suite_by_repo_file(self, request):
        """通过导入仓库中的文件生成接口测试套

        通过导入仓库中的文件生成接口测试套
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApiTestSuiteByRepoFile
        :type request: :class:`huaweicloudsdkcloudtest.v1.CreateApiTestSuiteByRepoFileRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateApiTestSuiteByRepoFileResponse`
        """
        http_info = self._create_api_test_suite_by_repo_file_http_info(request)
        return self._call_api(**http_info)

    def create_api_test_suite_by_repo_file_invoker(self, request):
        http_info = self._create_api_test_suite_by_repo_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_api_test_suite_by_repo_file_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/projects/{project_id}/repository/testsuites",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApiTestSuiteByRepoFileResponse"
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

    def list_environments(self, request):
        """获取环境参数分组列表

        获取环境参数分组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnvironments
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListEnvironmentsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListEnvironmentsResponse`
        """
        http_info = self._list_environments_http_info(request)
        return self._call_api(**http_info)

    def list_environments_invoker(self, request):
        http_info = self._list_environments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_environments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_id}/environments",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvironmentsResponse"
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

    def list_basic_aw(self, request):
        """根据id获取单个basicAW信息

        根据id获取单个basicAW信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBasicAw
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListBasicAwRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListBasicAwResponse`
        """
        http_info = self._list_basic_aw_http_info(request)
        return self._call_api(**http_info)

    def list_basic_aw_invoker(self, request):
        http_info = self._list_basic_aw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_basic_aw_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/basic-aw/{aw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListBasicAwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'aw_id' in local_var_params:
            path_params['aw_id'] = local_var_params['aw_id']

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

    def list_public_lib_and_aws(self, request):
        """获取工程关联的公共aw信息和公共aw所属公共aw库信息

        获取工程关联的公共aw信息和公共aw所属公共aw库信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublicLibAndAws
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListPublicLibAndAwsRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListPublicLibAndAwsResponse`
        """
        http_info = self._list_public_lib_and_aws_http_info(request)
        return self._call_api(**http_info)

    def list_public_lib_and_aws_invoker(self, request):
        http_info = self._list_public_lib_and_aws_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_public_lib_and_aws_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/project/{project_id}/public_aw_lib_and_aws",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicLibAndAwsResponse"
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

    def list_user_dns_mapping(self, request):
        """查询用户DNS映射

        查询用户DNS映射
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserDnsMapping
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListUserDnsMappingRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListUserDnsMappingResponse`
        """
        http_info = self._list_user_dns_mapping_http_info(request)
        return self._call_api(**http_info)

    def list_user_dns_mapping_invoker(self, request):
        http_info = self._list_user_dns_mapping_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_dns_mapping_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dns-mapping",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserDnsMappingResponse"
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

    def list_variables(self, request):
        """查询全局变量参数列表V4

        查询全局变量参数列表V4
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVariables
        :type request: :class:`huaweicloudsdkcloudtest.v1.ListVariablesRequest`
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ListVariablesResponse`
        """
        http_info = self._list_variables_http_info(request)
        return self._call_api(**http_info)

    def list_variables_invoker(self, request):
        http_info = self._list_variables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_variables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{project_id}/variables",
            "request_type": request.__class__.__name__,
            "response_type": "ListVariablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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
