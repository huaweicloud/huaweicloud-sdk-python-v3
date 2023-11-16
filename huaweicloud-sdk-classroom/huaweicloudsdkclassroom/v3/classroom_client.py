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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkclassroom'")


class ClassroomClient(Client):
    def __init__(self):
        super(ClassroomClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkclassroom.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ClassroomClient":
                raise TypeError("client type error, support client type is ClassroomClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def apply_judgement(self, request):
        """下发判题任务

        下发判题任务，根据回调地址、代码来源、源代码文本、语言类型、超时时长、输出类型，触发后台代码编译运行和判题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyJudgement
        :type request: :class:`huaweicloudsdkclassroom.v3.ApplyJudgementRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ApplyJudgementResponse`
        """
        http_info = self._apply_judgement_http_info(request)
        return self._call_api(**http_info)

    def apply_judgement_invoker(self, request):
        http_info = self._apply_judgement_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_judgement_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/enablement/judgements",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyJudgementResponse"
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

    def show_judgement_detail(self, request):
        """获取判题结果详情

        根据判题任务ID获取判题结果详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJudgementDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowJudgementDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowJudgementDetailResponse`
        """
        http_info = self._show_judgement_detail_http_info(request)
        return self._call_api(**http_info)

    def show_judgement_detail_invoker(self, request):
        http_info = self._show_judgement_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_judgement_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/enablement/judgements/{judgement_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJudgementDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'judgement_id' in local_var_params:
            path_params['judgement_id'] = local_var_params['judgement_id']

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

    def show_judgement_file(self, request):
        """下载判题结果文件

        根据文件id或图片id下载输出结果文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJudgementFile
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowJudgementFileRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowJudgementFileResponse`
        """
        http_info = self._show_judgement_file_http_info(request)
        return self._call_api(**http_info)

    def show_judgement_file_invoker(self, request):
        http_info = self._show_judgement_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_judgement_file_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/enablement/judgement/files/{file_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJudgementFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

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

    def execute_exercise(self, request):
        """习题判题

        习题判题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteExercise
        :type request: :class:`huaweicloudsdkclassroom.v3.ExecuteExerciseRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ExecuteExerciseResponse`
        """
        http_info = self._execute_exercise_http_info(request)
        return self._call_api(**http_info)

    def execute_exercise_invoker(self, request):
        http_info = self._execute_exercise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_exercise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/assemble/exercise/{exercise_id}/judge",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteExerciseResponse"
            }

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

    def list_exercises(self, request):
        """查询习题库下习题列表

        查询习题库下习题列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExercises
        :type request: :class:`huaweicloudsdkclassroom.v3.ListExercisesRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListExercisesResponse`
        """
        http_info = self._list_exercises_http_info(request)
        return self._call_api(**http_info)

    def list_exercises_invoker(self, request):
        http_info = self._list_exercises_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_exercises_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/assemble/package/{package_id}/exercise/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListExercisesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

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

    def list_packages(self, request):
        """查询当前租户的习题库列表

        查询当前租户的习题库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPackages
        :type request: :class:`huaweicloudsdkclassroom.v3.ListPackagesRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListPackagesResponse`
        """
        http_info = self._list_packages_http_info(request)
        return self._call_api(**http_info)

    def list_packages_invoker(self, request):
        http_info = self._list_packages_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_packages_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/assemble/package/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListPackagesResponse"
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

    def show_exercise_detail(self, request):
        """查询单个习题详情

        查询单个习题详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExerciseDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowExerciseDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowExerciseDetailResponse`
        """
        http_info = self._show_exercise_detail_http_info(request)
        return self._call_api(**http_info)

    def show_exercise_detail_invoker(self, request):
        http_info = self._show_exercise_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_exercise_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/assemble/exercise/{exercise_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExerciseDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'exercise_id' in local_var_params:
            path_params['exercise_id'] = local_var_params['exercise_id']

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

    def show_package_detail(self, request):
        """查询单个习题库详情

        查询单个习题库详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPackageDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowPackageDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowPackageDetailResponse`
        """
        http_info = self._show_package_detail_http_info(request)
        return self._call_api(**http_info)

    def show_package_detail_invoker(self, request):
        http_info = self._show_package_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_package_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/assemble/package/{package_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPackageDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

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

    def list_all_difficults(self, request):
        """获取习题所有难度

        获取习题所有难度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllDifficults
        :type request: :class:`huaweicloudsdkclassroom.v3.ListAllDifficultsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListAllDifficultsResponse`
        """
        http_info = self._list_all_difficults_http_info(request)
        return self._call_api(**http_info)

    def list_all_difficults_invoker(self, request):
        http_info = self._list_all_difficults_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_difficults_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/baseresource/extend-resource/difficult/all",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllDifficultsResponse"
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

    def list_my_knowledge_points(self, request):
        """获取自身习题知识点

        获取自身习题知识点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMyKnowledgePoints
        :type request: :class:`huaweicloudsdkclassroom.v3.ListMyKnowledgePointsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListMyKnowledgePointsResponse`
        """
        http_info = self._list_my_knowledge_points_http_info(request)
        return self._call_api(**http_info)

    def list_my_knowledge_points_invoker(self, request):
        http_info = self._list_my_knowledge_points_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_my_knowledge_points_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/baseresource/extend-resource/knowledge-point/mine",
            "request_type": request.__class__.__name__,
            "response_type": "ListMyKnowledgePointsResponse"
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

    def list_classroom_members(self, request):
        """根据课堂ID获取指定课堂的课堂成员列表

        根据课堂ID获取指定课堂的课堂成员列表，支持分页，搜索字段默认同时匹配姓名，学号，用户名，班级。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClassroomMembers
        :type request: :class:`huaweicloudsdkclassroom.v3.ListClassroomMembersRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListClassroomMembersResponse`
        """
        http_info = self._list_classroom_members_http_info(request)
        return self._call_api(**http_info)

    def list_classroom_members_invoker(self, request):
        http_info = self._list_classroom_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_classroom_members_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/classrooms/{classroom_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListClassroomMembersResponse"
            }

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

    def list_classrooms(self, request):
        """获取当前用户的课堂列表

        获取当前用户的课堂列表，课堂课表分为我创建的课堂，我加入的课堂以及所有课堂，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClassrooms
        :type request: :class:`huaweicloudsdkclassroom.v3.ListClassroomsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListClassroomsResponse`
        """
        http_info = self._list_classrooms_http_info(request)
        return self._call_api(**http_info)

    def list_classrooms_invoker(self, request):
        http_info = self._list_classrooms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_classrooms_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/classrooms",
            "request_type": request.__class__.__name__,
            "response_type": "ListClassroomsResponse"
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
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))

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

    def show_classroom_detail(self, request):
        """根据课堂ID获取指定课堂的详细信息

        根据课堂ID获取指定课堂的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClassroomDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowClassroomDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowClassroomDetailResponse`
        """
        http_info = self._show_classroom_detail_http_info(request)
        return self._call_api(**http_info)

    def show_classroom_detail_invoker(self, request):
        http_info = self._show_classroom_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_classroom_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/classrooms/{classroom_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClassroomDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'classroom_id' in local_var_params:
            path_params['classroom_id'] = local_var_params['classroom_id']

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

    def list_classroom_member_jobs(self, request):
        """查询课堂下指定成员的作业信息

        查询课堂下指定成员的作业信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClassroomMemberJobs
        :type request: :class:`huaweicloudsdkclassroom.v3.ListClassroomMemberJobsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListClassroomMemberJobsResponse`
        """
        http_info = self._list_classroom_member_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_classroom_member_jobs_invoker(self, request):
        http_info = self._list_classroom_member_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_classroom_member_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/classrooms/{classroom_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListClassroomMemberJobsResponse"
            }

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

    def list_jobs(self, request):
        """查询指定课堂下的作业列表信息

        查询指定课堂下的作业列表信息，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkclassroom.v3.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
            }

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

    def list_member_job_records(self, request):
        """查询学生函数习题提交记录信息

        查询学生指定作业的习题提交记录信息(针对函数习题)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMemberJobRecords
        :type request: :class:`huaweicloudsdkclassroom.v3.ListMemberJobRecordsRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ListMemberJobRecordsResponse`
        """
        http_info = self._list_member_job_records_http_info(request)
        return self._call_api(**http_info)

    def list_member_job_records_invoker(self, request):
        http_info = self._list_member_job_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_member_job_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/exercises/{exercise_id}/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListMemberJobRecordsResponse"
            }

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

    def show_job_detail(self, request):
        """根据作业ID，查询指定作业的信息

        根据作业ID，查询指定作业的信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowJobDetailResponse`
        """
        http_info = self._show_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_job_detail_invoker(self, request):
        http_info = self._show_job_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def show_job_exercises(self, request):
        """查询指定作业下的习题信息

        查询指定作业下的习题信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobExercises
        :type request: :class:`huaweicloudsdkclassroom.v3.ShowJobExercisesRequest`
        :rtype: :class:`huaweicloudsdkclassroom.v3.ShowJobExercisesResponse`
        """
        http_info = self._show_job_exercises_http_info(request)
        return self._call_api(**http_info)

    def show_job_exercises_invoker(self, request):
        http_info = self._show_job_exercises_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_exercises_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/exercises",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobExercisesResponse"
            }

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
