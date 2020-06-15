# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


class ClassroomAsyncClient(Client):
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
        super(ClassroomAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkclassroom.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def list_classroom_members_async(self, request):
        """根据课堂ID获取指定课堂的课堂成员列表

        根据课堂ID获取指定课堂的课堂成员列表，支持分页，搜索字段默认同时匹配姓名，学号，用户名，班级。

        :param ListClassroomMembersRequest request
        :return: ListClassroomMembersResponse
        """
        return self.list_classroom_members_with_http_info(request)

    def list_classroom_members_with_http_info(self, request):
        """根据课堂ID获取指定课堂的课堂成员列表

        根据课堂ID获取指定课堂的课堂成员列表，支持分页，搜索字段默认同时匹配姓名，学号，用户名，班级。

        :param ListClassroomMembersRequest request
        :return: tuple(ListClassroomMembersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['classroom_id', 'offset', 'limit', 'filter']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'classroom_id' in local_var_params:
            path_params['classroom_id'] = local_var_params['classroom_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/classrooms/{classroom_id}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClassroomMembersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_classrooms_async(self, request):
        """获取当前用户的课堂列表

        获取当前用户的课堂列表，课堂课表分为我创建的课堂，我加入的课堂以及所有课堂，支持分页查询。

        :param ListClassroomsRequest request
        :return: ListClassroomsResponse
        """
        return self.list_classrooms_with_http_info(request)

    def list_classrooms_with_http_info(self, request):
        """获取当前用户的课堂列表

        获取当前用户的课堂列表，课堂课表分为我创建的课堂，我加入的课堂以及所有课堂，支持分页查询。

        :param ListClassroomsRequest request
        :return: tuple(ListClassroomsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['offset', 'limit', 'query_type']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/classrooms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClassroomsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_classroom_detail_async(self, request):
        """根据课堂ID获取指定课堂的详细信息

        根据课堂ID获取指定课堂的详细信息

        :param ShowClassroomDetailRequest request
        :return: ShowClassroomDetailResponse
        """
        return self.show_classroom_detail_with_http_info(request)

    def show_classroom_detail_with_http_info(self, request):
        """根据课堂ID获取指定课堂的详细信息

        根据课堂ID获取指定课堂的详细信息

        :param ShowClassroomDetailRequest request
        :return: tuple(ShowClassroomDetailResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['classroom_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'classroom_id' in local_var_params:
            path_params['classroom_id'] = local_var_params['classroom_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/classrooms/{classroom_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowClassroomDetailResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_classroom_member_jobs_async(self, request):
        """查询课堂下指定成员的作业信息

        查询课堂下指定成员的作业信息

        :param ListClassroomMemberJobsRequest request
        :return: ListClassroomMemberJobsResponse
        """
        return self.list_classroom_member_jobs_with_http_info(request)

    def list_classroom_member_jobs_with_http_info(self, request):
        """查询课堂下指定成员的作业信息

        查询课堂下指定成员的作业信息

        :param ListClassroomMemberJobsRequest request
        :return: tuple(ListClassroomMemberJobsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['classroom_id', 'member_id', 'offset', 'limit']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'classroom_id' in local_var_params:
            path_params['classroom_id'] = local_var_params['classroom_id']

        query_params = []
        if 'member_id' in local_var_params:
            query_params.append(('member_id', local_var_params['member_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/classrooms/{classroom_id}/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClassroomMemberJobsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_jobs_async(self, request):
        """查询指定课堂下的作业列表信息

        查询指定课堂下的作业列表信息，支持分页查询。

        :param ListJobsRequest request
        :return: ListJobsResponse
        """
        return self.list_jobs_with_http_info(request)

    def list_jobs_with_http_info(self, request):
        """查询指定课堂下的作业列表信息

        查询指定课堂下的作业列表信息，支持分页查询。

        :param ListJobsRequest request
        :return: tuple(ListJobsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['source_from', 'source_id', 'offset', 'limit']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source_from' in local_var_params:
            query_params.append(('source_from', local_var_params['source_from']))
        if 'source_id' in local_var_params:
            query_params.append(('source_id', local_var_params['source_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListJobsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_member_job_records_async(self, request):
        """查询学生函数习题提交记录信息

        查询学生指定作业的习题提交记录信息(针对函数习题)

        :param ListMemberJobRecordsRequest request
        :return: ListMemberJobRecordsResponse
        """
        return self.list_member_job_records_with_http_info(request)

    def list_member_job_records_with_http_info(self, request):
        """查询学生函数习题提交记录信息

        查询学生指定作业的习题提交记录信息(针对函数习题)

        :param ListMemberJobRecordsRequest request
        :return: tuple(ListMemberJobRecordsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['job_id', 'exercise_id', 'member_id', 'offset', 'limit']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'exercise_id' in local_var_params:
            path_params['exercise_id'] = local_var_params['exercise_id']

        query_params = []
        if 'member_id' in local_var_params:
            query_params.append(('member_id', local_var_params['member_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/jobs/{job_id}/exercises/{exercise_id}/records', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMemberJobRecordsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_detail_async(self, request):
        """根据作业ID，查询指定作业的信息

        根据作业ID，查询指定作业的信息

        :param ShowJobDetailRequest request
        :return: ShowJobDetailResponse
        """
        return self.show_job_detail_with_http_info(request)

    def show_job_detail_with_http_info(self, request):
        """根据作业ID，查询指定作业的信息

        根据作业ID，查询指定作业的信息

        :param ShowJobDetailRequest request
        :return: tuple(ShowJobDetailResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['job_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/jobs/{job_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobDetailResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_exercises_async(self, request):
        """查询指定作业下的习题信息

        查询指定作业下的习题信息

        :param ShowJobExercisesRequest request
        :return: ShowJobExercisesResponse
        """
        return self.show_job_exercises_with_http_info(request)

    def show_job_exercises_with_http_info(self, request):
        """查询指定作业下的习题信息

        查询指定作业下的习题信息

        :param ShowJobExercisesRequest request
        :return: tuple(ShowJobExercisesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['job_id', 'source_from', 'source_id', 'offset', 'limit']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'source_from' in local_var_params:
            query_params.append(('source_from', local_var_params['source_from']))
        if 'source_id' in local_var_params:
            query_params.append(('source_id', local_var_params['source_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/jobs/{job_id}/exercises', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobExercisesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats, request_type, True)
