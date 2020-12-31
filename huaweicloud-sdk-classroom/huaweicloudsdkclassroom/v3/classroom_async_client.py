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

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ClassroomClient":
            raise TypeError("client type error, support client type is ClassroomClient")

        return ClientBuilder(clazz)

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
        :return: ListClassroomMembersResponse
        """

        all_params = ['classroom_id', 'offset', 'limit', 'filter']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/classrooms/{classroom_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClassroomMembersResponse',
            response_headers=response_headers,
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
        :return: ListClassroomsResponse
        """

        all_params = ['offset', 'limit', 'query_type']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/classrooms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClassroomsResponse',
            response_headers=response_headers,
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
        :return: ShowClassroomDetailResponse
        """

        all_params = ['classroom_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/classrooms/{classroom_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowClassroomDetailResponse',
            response_headers=response_headers,
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
        :return: ListClassroomMemberJobsResponse
        """

        all_params = ['classroom_id', 'member_id', 'offset', 'limit']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/classrooms/{classroom_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClassroomMemberJobsResponse',
            response_headers=response_headers,
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
        :return: ListJobsResponse
        """

        all_params = ['source_from', 'source_id', 'offset', 'limit']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListJobsResponse',
            response_headers=response_headers,
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
        :return: ListMemberJobRecordsResponse
        """

        all_params = ['job_id', 'exercise_id', 'member_id', 'offset', 'limit']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/jobs/{job_id}/exercises/{exercise_id}/records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMemberJobRecordsResponse',
            response_headers=response_headers,
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
        :return: ShowJobDetailResponse
        """

        all_params = ['job_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobDetailResponse',
            response_headers=response_headers,
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
        :return: ShowJobExercisesResponse
        """

        all_params = ['job_id', 'source_from', 'source_id', 'offset', 'limit']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/jobs/{job_id}/exercises',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobExercisesResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)
