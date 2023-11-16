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
