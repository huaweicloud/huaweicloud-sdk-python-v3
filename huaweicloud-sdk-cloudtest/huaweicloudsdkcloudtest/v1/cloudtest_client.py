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


class CloudtestClient(Client):
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
        super(CloudtestClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudtest.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def create_plan(self, request):
        """项目下创建计划

        项目下创建计划

        :param CreatePlanRequest request
        :return: CreatePlanResponse
        """
        return self.create_plan_with_http_info(request)

    def create_plan_with_http_info(self, request):
        """项目下创建计划

        项目下创建计划

        :param CreatePlanRequest request
        :return: CreatePlanResponse
        """

        all_params = ['project_id', 'create_plan_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/projects/{project_id}/plans',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_test_case_in_plan(self, request):
        """计划中批量添加测试用例

        计划中批量添加测试用例

        :param CreateTestCaseInPlanRequest request
        :return: CreateTestCaseInPlanResponse
        """
        return self.create_test_case_in_plan_with_http_info(request)

    def create_test_case_in_plan_with_http_info(self, request):
        """计划中批量添加测试用例

        计划中批量添加测试用例

        :param CreateTestCaseInPlanRequest request
        :return: CreateTestCaseInPlanResponse
        """

        all_params = ['project_id', 'plan_id', 'create_test_case_in_plan_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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
            resource_path='/v1/projects/{project_id}/plans/{plan_id}/testcases/batch-add',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTestCaseInPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_service(self, request):
        """新测试类型服务注册到云测

        新测试类型服务注册到云测

        :param CreateServiceRequest request
        :return: CreateServiceResponse
        """
        return self.create_service_with_http_info(request)

    def create_service_with_http_info(self, request):
        """新测试类型服务注册到云测

        新测试类型服务注册到云测

        :param CreateServiceRequest request
        :return: CreateServiceResponse
        """

        all_params = ['create_service_request_body']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/services',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_service(self, request):
        """删除已注册服务

        删除已注册服务

        :param DeleteServiceRequest request
        :return: DeleteServiceResponse
        """
        return self.delete_service_with_http_info(request)

    def delete_service_with_http_info(self, request):
        """删除已注册服务

        删除已注册服务

        :param DeleteServiceRequest request
        :return: DeleteServiceResponse
        """

        all_params = ['service_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/services/{service_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_register_service(self, request):
        """用户获取自己当前已经注册的服务

        用户获取自己当前已经注册的服务

        :param ShowRegisterServiceRequest request
        :return: ShowRegisterServiceResponse
        """
        return self.show_register_service_with_http_info(request)

    def show_register_service_with_http_info(self, request):
        """用户获取自己当前已经注册的服务

        用户获取自己当前已经注册的服务

        :param ShowRegisterServiceRequest request
        :return: ShowRegisterServiceResponse
        """

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRegisterServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_service(self, request):
        """更新已注册服务

        更新已注册服务

        :param UpdateServiceRequest request
        :return: UpdateServiceResponse
        """
        return self.update_service_with_http_info(request)

    def update_service_with_http_info(self, request):
        """更新已注册服务

        更新已注册服务

        :param UpdateServiceRequest request
        :return: UpdateServiceResponse
        """

        all_params = ['service_id', 'update_service_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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
            resource_path='/v1/services/{service_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_test_case(self, request):
        """批量删除测试用例

        批量删除测试用例

        :param BatchDeleteTestCaseRequest request
        :return: BatchDeleteTestCaseResponse
        """
        return self.batch_delete_test_case_with_http_info(request)

    def batch_delete_test_case_with_http_info(self, request):
        """批量删除测试用例

        批量删除测试用例

        :param BatchDeleteTestCaseRequest request
        :return: BatchDeleteTestCaseResponse
        """

        all_params = ['project_id', 'batch_delete_test_case_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/projects/{project_id}/testcases/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteTestCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_test_case(self, request):
        """创建测试用例

        创建测试用例

        :param CreateTestCaseRequest request
        :return: CreateTestCaseResponse
        """
        return self.create_test_case_with_http_info(request)

    def create_test_case_with_http_info(self, request):
        """创建测试用例

        创建测试用例

        :param CreateTestCaseRequest request
        :return: CreateTestCaseResponse
        """

        all_params = ['project_id', 'create_test_case_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/projects/{project_id}/testcases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTestCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def run_test_case(self, request):
        """批量执行测试用例

        批量执行测试用例

        :param RunTestCaseRequest request
        :return: RunTestCaseResponse
        """
        return self.run_test_case_with_http_info(request)

    def run_test_case_with_http_info(self, request):
        """批量执行测试用例

        批量执行测试用例

        :param RunTestCaseRequest request
        :return: RunTestCaseResponse
        """

        all_params = ['project_id', 'run_test_case_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/projects/{project_id}/testcases/execution',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunTestCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_test_case_detail(self, request):
        """获取测试用例详情

        获取测试用例详情

        :param ShowTestCaseDetailRequest request
        :return: ShowTestCaseDetailResponse
        """
        return self.show_test_case_detail_with_http_info(request)

    def show_test_case_detail_with_http_info(self, request):
        """获取测试用例详情

        获取测试用例详情

        :param ShowTestCaseDetailRequest request
        :return: ShowTestCaseDetailResponse
        """

        all_params = ['project_id', 'testcase_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'testcase_id' in local_var_params:
            path_params['testcase_id'] = local_var_params['testcase_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/projects/{project_id}/testcases/{testcase_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTestCaseDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_test_case_detail_v2(self, request):
        """通过用例编号或用例ID获取测试用例详情

        通过用例编号或用例ID获取测试用例详情

        :param ShowTestCaseDetailV2Request request
        :return: ShowTestCaseDetailV2Response
        """
        return self.show_test_case_detail_v2_with_http_info(request)

    def show_test_case_detail_v2_with_http_info(self, request):
        """通过用例编号或用例ID获取测试用例详情

        通过用例编号或用例ID获取测试用例详情

        :param ShowTestCaseDetailV2Request request
        :return: ShowTestCaseDetailV2Response
        """

        all_params = ['project_id', 'testcase_number', 'testcase_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'testcase_number' in local_var_params:
            query_params.append(('testcase_number', local_var_params['testcase_number']))
        if 'testcase_id' in local_var_params:
            query_params.append(('testcase_id', local_var_params['testcase_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/projects/{project_id}/testcase',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTestCaseDetailV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_test_case(self, request):
        """更新测试用例接口

        更新测试用例接口

        :param UpdateTestCaseRequest request
        :return: UpdateTestCaseResponse
        """
        return self.update_test_case_with_http_info(request)

    def update_test_case_with_http_info(self, request):
        """更新测试用例接口

        更新测试用例接口

        :param UpdateTestCaseRequest request
        :return: UpdateTestCaseResponse
        """

        all_params = ['project_id', 'testcase_id', 'update_test_case_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'testcase_id' in local_var_params:
            path_params['testcase_id'] = local_var_params['testcase_id']

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
            resource_path='/v1/projects/{project_id}/testcases/{testcase_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTestCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_test_case_result(self, request):
        """批量更新测试用例结果

        批量更新测试用例结果

        :param UpdateTestCaseResultRequest request
        :return: UpdateTestCaseResultResponse
        """
        return self.update_test_case_result_with_http_info(request)

    def update_test_case_result_with_http_info(self, request):
        """批量更新测试用例结果

        批量更新测试用例结果

        :param UpdateTestCaseResultRequest request
        :return: UpdateTestCaseResultResponse
        """

        all_params = ['project_id', 'update_test_case_result_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/projects/{project_id}/testcases/result',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTestCaseResultResponse',
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
