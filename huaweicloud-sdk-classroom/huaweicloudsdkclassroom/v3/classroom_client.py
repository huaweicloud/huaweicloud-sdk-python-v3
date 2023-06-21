# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class ClassroomClient(Client):
    def __init__(self):
        super(ClassroomClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkclassroom.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ClassroomClient":
            raise TypeError("client type error, support client type is ClassroomClient")

        return ClientBuilder(clazz)

    def apply_judgement(self, request):
        """下发判题任务

        下发判题任务，根据回调地址、代码来源、源代码文本、语言类型、超时时长、输出类型，触发后台代码编译运行和判题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyJudgement
        :type request: :class:`huaweicloudsdkclassroom.v3.ApplyJudgementRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ApplyJudgementResponse`
        """
        return self._apply_judgement_with_http_info(request)

    def _apply_judgement_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/enablement/judgements',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyJudgementResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_judgement_detail(self, request):
        """获取判题结果详情

        根据判题任务ID获取判题结果详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJudgementDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowJudgementDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowJudgementDetailResponse`
        """
        return self._show_judgement_detail_with_http_info(request)

    def _show_judgement_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'judgement_id' in local_var_params:
            path_params['judgement_id'] = local_var_params['judgement_id']

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
            resource_path='/v1/enablement/judgements/{judgement_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJudgementDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_judgement_file(self, request):
        """下载判题结果文件

        根据文件id或图片id下载输出结果文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJudgementFile
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowJudgementFileRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowJudgementFileResponse`
        """
        return self._show_judgement_file_with_http_info(request)

    def _show_judgement_file_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

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
            resource_path='/v1/enablement/judgement/files/{file_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJudgementFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_exercise(self, request):
        """习题判题

        习题判题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteExercise
        :type request: :class:`huaweicloudsdkclassroom.v3.ExecuteExerciseRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ExecuteExerciseResponse`
        """
        return self._execute_exercise_with_http_info(request)

    def _execute_exercise_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'exercise_id' in local_var_params:
            path_params['exercise_id'] = local_var_params['exercise_id']

        query_params = []

        header_params = {}
        if 'user_token' in local_var_params:
            header_params['user-token'] = local_var_params['user_token']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/assemble/exercise/{exercise_id}/judge',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteExerciseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_exercises(self, request):
        """查询习题库下习题列表

        查询习题库下习题列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExercises
        :type request: :class:`huaweicloudsdkclassroom.v3.ListExercisesRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListExercisesResponse`
        """
        return self._list_exercises_with_http_info(request)

    def _list_exercises_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/assemble/package/{package_id}/exercise/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListExercisesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_packages(self, request):
        """查询当前租户的习题库列表

        查询当前租户的习题库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPackages
        :type request: :class:`huaweicloudsdkclassroom.v3.ListPackagesRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListPackagesResponse`
        """
        return self._list_packages_with_http_info(request)

    def _list_packages_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/assemble/package/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPackagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_exercise_detail(self, request):
        """查询单个习题详情

        查询单个习题详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExerciseDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowExerciseDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowExerciseDetailResponse`
        """
        return self._show_exercise_detail_with_http_info(request)

    def _show_exercise_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'exercise_id' in local_var_params:
            path_params['exercise_id'] = local_var_params['exercise_id']

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
            resource_path='/v1/assemble/exercise/{exercise_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowExerciseDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_package_detail(self, request):
        """查询单个习题库详情

        查询单个习题库详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPackageDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowPackageDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowPackageDetailResponse`
        """
        return self._show_package_detail_with_http_info(request)

    def _show_package_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

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
            resource_path='/v1/assemble/package/{package_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPackageDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_difficults(self, request):
        """获取习题所有难度

        获取习题所有难度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllDifficults
        :type request: :class:`huaweicloudsdkclassroom.v3.ListAllDifficultsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListAllDifficultsResponse`
        """
        return self._list_all_difficults_with_http_info(request)

    def _list_all_difficults_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/baseresource/extend-resource/difficult/all',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllDifficultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_my_knowledge_points(self, request):
        """获取自身习题知识点

        获取自身习题知识点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMyKnowledgePoints
        :type request: :class:`huaweicloudsdkclassroom.v3.ListMyKnowledgePointsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListMyKnowledgePointsResponse`
        """
        return self._list_my_knowledge_points_with_http_info(request)

    def _list_my_knowledge_points_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/baseresource/extend-resource/knowledge-point/mine',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMyKnowledgePointsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_classroom_members(self, request):
        """根据课堂ID获取指定课堂的课堂成员列表

        根据课堂ID获取指定课堂的课堂成员列表，支持分页，搜索字段默认同时匹配姓名，学号，用户名，班级。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClassroomMembers
        :type request: :class:`huaweicloudsdkclassroom.v3.ListClassroomMembersRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListClassroomMembersResponse`
        """
        return self._list_classroom_members_with_http_info(request)

    def _list_classroom_members_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListClassroomMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_classrooms(self, request):
        """获取当前用户的课堂列表

        获取当前用户的课堂列表，课堂课表分为我创建的课堂，我加入的课堂以及所有课堂，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClassrooms
        :type request: :class:`huaweicloudsdkclassroom.v3.ListClassroomsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListClassroomsResponse`
        """
        return self._list_classrooms_with_http_info(request)

    def _list_classrooms_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListClassroomsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_classroom_detail(self, request):
        """根据课堂ID获取指定课堂的详细信息

        根据课堂ID获取指定课堂的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClassroomDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowClassroomDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowClassroomDetailResponse`
        """
        return self._show_classroom_detail_with_http_info(request)

    def _show_classroom_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowClassroomDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_classroom_member_jobs(self, request):
        """查询课堂下指定成员的作业信息

        查询课堂下指定成员的作业信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClassroomMemberJobs
        :type request: :class:`huaweicloudsdkclassroom.v3.ListClassroomMemberJobsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListClassroomMemberJobsResponse`
        """
        return self._list_classroom_member_jobs_with_http_info(request)

    def _list_classroom_member_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListClassroomMemberJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_jobs(self, request):
        """查询指定课堂下的作业列表信息

        查询指定课堂下的作业列表信息，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkclassroom.v3.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListJobsResponse`
        """
        return self._list_jobs_with_http_info(request)

    def _list_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_member_job_records(self, request):
        """查询学生函数习题提交记录信息

        查询学生指定作业的习题提交记录信息(针对函数习题)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMemberJobRecords
        :type request: :class:`huaweicloudsdkclassroom.v3.ListMemberJobRecordsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListMemberJobRecordsResponse`
        """
        return self._list_member_job_records_with_http_info(request)

    def _list_member_job_records_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListMemberJobRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_detail(self, request):
        """根据作业ID，查询指定作业的信息

        根据作业ID，查询指定作业的信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowJobDetailResponse`
        """
        return self._show_job_detail_with_http_info(request)

    def _show_job_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowJobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_exercises(self, request):
        """查询指定作业下的习题信息

        查询指定作业下的习题信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobExercises
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowJobExercisesRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowJobExercisesResponse`
        """
        return self._show_job_exercises_with_http_info(request)

    def _show_job_exercises_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowJobExercisesResponse',
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
