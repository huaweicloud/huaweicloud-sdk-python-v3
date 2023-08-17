# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CloudRTCClient(Client):
    def __init__(self):
        super(CloudRTCClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudrtc.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CloudRTCClient":
            raise TypeError("client type error, support client type is CloudRTCClient")

        return ClientBuilder(clazz)

    def create_app(self, request):
        """创建应用

        调用此接口创建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.CreateAppResponse`
        """
        return self._create_app_with_http_info(request)

    def _create_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_individual_stream_job(self, request):
        """启动单流任务

        调用此接口接口启动单流任务。
        
        API触发单流录制流名规则：{jobtype}\\_{jobid}\\_{roomid}\\_{userid}
        
        jobtype取值为&#39;s&#39;代表单流录制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIndividualStreamJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.CreateIndividualStreamJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.CreateIndividualStreamJobResponse`
        """
        return self._create_individual_stream_job_with_http_info(request)

    def _create_individual_stream_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/individual-stream-jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIndividualStreamJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_mix_job(self, request):
        """启动合流任务

        调用此接口创建合流转码任务。
        
        支持纯音频录制和音视频录制：
        
        - 纯音频录制
        
          encode_template填audio_only，音频合流会动态选择最大三方的声音。
        
          layout_template、layout_panes以及其他视频相关参数都不填，填就忽略。
        
        - 音视频录制（包括共享桌面）
        
          encode_template非audio_only，layout_template、layout_panes必须非空。
        
          音频合流会动态选择最大三方的声音。
        
          API触发合流录制流名规则：{jobtype}\\_{jobid}\\_{roomid}，其中jobtype取值为&#39;m&#39;代表合流录制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMixJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.CreateMixJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.CreateMixJobResponse`
        """
        return self._create_mix_job_with_http_info(request)

    def _create_mix_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/mix-stream-jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMixJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_rule(self, request):
        """创建或更新录制规则

        调用此接口创建或更新录制规则。
        
        - 若当前app在请求的location中无录制规则，则会创建新的录制规则
        - 若当前app在请求的location中已有录制规则，则会更新原来的录制规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordRule
        :type request: :class:`huaweicloudsdkcloudrtc.v2.CreateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.CreateRecordRuleResponse`
        """
        return self._create_record_rule_with_http_info(request)

    def _create_record_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/record-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRecordRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app(self, request):
        """删除应用

        调用此接口删除单个应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.DeleteAppResponse`
        """
        return self._delete_app_with_http_info(request)

    def _delete_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_record_rule(self, request):
        """删除录制规则

        调用此接口删除录制规则，对于正在使用的录制规则，不允许删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordRule
        :type request: :class:`huaweicloudsdkcloudrtc.v2.DeleteRecordRuleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.DeleteRecordRuleResponse`
        """
        return self._delete_record_rule_with_http_info(request)

    def _delete_record_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/record-rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRecordRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps(self, request):
        """查询应用列表

        调用此接口查询应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ListAppsResponse`
        """
        return self._list_apps_with_http_info(request)

    def _list_apps_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_rules(self, request):
        """查询录制规则列表

        调用此接口查询录制规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordRules
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ListRecordRulesRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ListRecordRulesResponse`
        """
        return self._list_record_rules_with_http_info(request)

    def _list_record_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/record-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRecordRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_room(self, request):
        """解散房间

        调用此接口解散房间，将该房间中所有用户踢出房间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveRoom
        :type request: :class:`huaweicloudsdkcloudrtc.v2.RemoveRoomRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RemoveRoomResponse`
        """
        return self._remove_room_with_http_info(request)

    def _remove_room_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/rooms/{room_id}/dismiss',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveRoomResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_users(self, request):
        """踢除在线用户

        调用此接口强制用户离开房间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveUsers
        :type request: :class:`huaweicloudsdkcloudrtc.v2.RemoveUsersRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RemoveUsersResponse`
        """
        return self._remove_users_with_http_info(request)

    def _remove_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/rooms/{room_id}/batch-remove-users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_app(self, request):
        """查询单个应用

        调用此接口查询单个应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowAppResponse`
        """
        return self._show_app_with_http_info(request)

    def _show_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_auto_record(self, request):
        """查询自动录制配置

        调用此接口查询自动录制配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoRecord
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowAutoRecordRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowAutoRecordResponse`
        """
        return self._show_auto_record_with_http_info(request)

    def _show_auto_record_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/auto-record-mode',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAutoRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_individual_stream_job(self, request):
        """查询单流任务状态

        调用此接口查询单流任务状态。
        
        租户的OBS桶内的情况，暂不支持查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIndividualStreamJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowIndividualStreamJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowIndividualStreamJobResponse`
        """
        return self._show_individual_stream_job_with_http_info(request)

    def _show_individual_stream_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/individual-stream-jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIndividualStreamJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_mix_job(self, request):
        """查询合流任务

        调用此接口查询合流转码任务状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMixJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowMixJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowMixJobResponse`
        """
        return self._show_mix_job_with_http_info(request)

    def _show_mix_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/mix-stream-jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMixJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_callback(self, request):
        """查询增值（录制）事件回调配置

        调用此接口查询增值（录制）事件回调配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordCallback
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowRecordCallbackRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowRecordCallbackResponse`
        """
        return self._show_record_callback_with_http_info(request)

    def _show_record_callback_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/record-callback',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRecordCallbackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_rule(self, request):
        """查询录制规则

        调用此接口查询指定录制规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordRule
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowRecordRuleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowRecordRuleResponse`
        """
        return self._show_record_rule_with_http_info(request)

    def _show_record_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/record-rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRecordRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_url_auth(self, request):
        """查询访问控制参数

        查询应用鉴权配置参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUrlAuth
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowUrlAuthRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowUrlAuthResponse`
        """
        return self._show_url_auth_with_http_info(request)

    def _show_url_auth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/authentication',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUrlAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_app(self, request):
        """启用应用

        调用此接口启用单个应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.StartAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.StartAppResponse`
        """
        return self._start_app_with_http_info(request)

    def _start_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_app(self, request):
        """停用应用

        调用此接口停用单个应用。
        
        应用停用后，新房间无法新增和加入，已加入的房间可以继续使用。合流、录制功能等也不可用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.StopAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.StopAppResponse`
        """
        return self._stop_app_with_http_info(request)

    def _stop_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_individual_stream_job(self, request):
        """停止单流任务

        调用此接口停止单流任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopIndividualStreamJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.StopIndividualStreamJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.StopIndividualStreamJobResponse`
        """
        return self._stop_individual_stream_job_with_http_info(request)

    def _stop_individual_stream_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/individual-stream-jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopIndividualStreamJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_mix_job(self, request):
        """停止合流任务

        调用此接口停止已下发的合流转码任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopMixJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.StopMixJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.StopMixJobResponse`
        """
        return self._stop_mix_job_with_http_info(request)

    def _stop_mix_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/mix-stream-jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopMixJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_auto_record(self, request):
        """更新自动录制配置

        更新自动录制配置，租户可以开启自动单流录制或者停用自动单流录制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutoRecord
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateAutoRecordRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateAutoRecordResponse`
        """
        return self._update_auto_record_with_http_info(request)

    def _update_auto_record_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/auto-record-mode',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAutoRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_individual_stream_job(self, request):
        """更新单流任务

        调用此接口修改单流任务。
        
        仅部分场景支持修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIndividualStreamJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateIndividualStreamJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateIndividualStreamJobResponse`
        """
        return self._update_individual_stream_job_with_http_info(request)

    def _update_individual_stream_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/individual-stream-jobs/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIndividualStreamJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_mix_job(self, request):
        """修改合流任务

        调用此接口更新合流任务布局。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMixJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateMixJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateMixJobResponse`
        """
        return self._update_mix_job_with_http_info(request)

    def _update_mix_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/mix-stream-jobs/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMixJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_record_callback(self, request):
        """配置RTC增值（录制）事件回调

        调用此接口配置增值（录制）事件上报回调。
        
        当任务发生订阅了的事件时，通过该接口配置的回调地址通知。
        
        回调格式参考/customer-record-notify-url定义。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordCallback
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateRecordCallbackRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateRecordCallbackResponse`
        """
        return self._update_record_callback_with_http_info(request)

    def _update_record_callback_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/record-callback',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRecordCallbackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_record_rule(self, request):
        """更新录制规则

        调用此接口更新录制规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordRule
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateRecordRuleResponse`
        """
        return self._update_record_rule_with_http_info(request)

    def _update_record_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/record-rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRecordRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_url_auth(self, request):
        """开关访问控制

        调用此接口开启或关闭URL鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUrlAuth
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateUrlAuthRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateUrlAuthResponse`
        """
        return self._update_url_auth_with_http_info(request)

    def _update_url_auth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/apps/{app_id}/authentication',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUrlAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_obs_bucket_objects(self, request):
        """查询OBS桶下对象列表

        查询OBS桶下对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBucketObjects
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ListObsBucketObjectsRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ListObsBucketObjectsResponse`
        """
        return self._list_obs_bucket_objects_with_http_info(request)

    def _list_obs_bucket_objects_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'location' in local_var_params:
            query_params.append(('location', local_var_params['location']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/rtc-ops/buckets/objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListObsBucketObjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_obs_buckets(self, request):
        """查询OBS桶列表

        查询OBS桶列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBuckets
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ListObsBucketsRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ListObsBucketsResponse`
        """
        return self._list_obs_buckets_with_http_info(request)

    def _list_obs_buckets_with_http_info(self, request):
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

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/rtc-ops/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListObsBucketsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_obs_bucket_authority(self, request):
        """OBS桶授权及取消授权

        OBS桶授权及取消授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateObsBucketAuthority
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateObsBucketAuthorityRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateObsBucketAuthorityResponse`
        """
        return self._update_obs_bucket_authority_with_http_info(request)

    def _update_obs_bucket_authority_with_http_info(self, request):
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

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/rtc-ops/buckets/authentication',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateObsBucketAuthorityResponse',
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
