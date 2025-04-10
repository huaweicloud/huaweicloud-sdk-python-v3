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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcloudrtc'")


class CloudRTCClient(Client):
    def __init__(self):
        super(CloudRTCClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudrtc.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CloudRTCClient":
                raise TypeError("client type error, support client type is CloudRTCClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_app(self, request):
        r"""创建应用

        调用此接口创建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_individual_stream_job(self, request):
        r"""启动单流任务

        调用此接口接口启动单流任务。
        
        API触发单流录制流名规则：{jobtype}\\_{jobid}\\_{roomid}\\_{userid}
        
        jobtype取值为&#39;s&#39;代表单流录制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIndividualStreamJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.CreateIndividualStreamJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.CreateIndividualStreamJobResponse`
        """
        http_info = self._create_individual_stream_job_http_info(request)
        return self._call_api(**http_info)

    def create_individual_stream_job_invoker(self, request):
        http_info = self._create_individual_stream_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_individual_stream_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/apps/{app_id}/individual-stream-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIndividualStreamJobResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_mix_job(self, request):
        r"""启动合流任务

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
        http_info = self._create_mix_job_http_info(request)
        return self._call_api(**http_info)

    def create_mix_job_invoker(self, request):
        http_info = self._create_mix_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_mix_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/apps/{app_id}/mix-stream-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMixJobResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_record_rule(self, request):
        r"""创建或更新录制规则

        调用此接口创建或更新录制规则。
        
        - 若当前app在请求的location中无录制规则，则会创建新的录制规则
        - 若当前app在请求的location中已有录制规则，则会更新原来的录制规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordRule
        :type request: :class:`huaweicloudsdkcloudrtc.v2.CreateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.CreateRecordRuleResponse`
        """
        http_info = self._create_record_rule_http_info(request)
        return self._call_api(**http_info)

    def create_record_rule_invoker(self, request):
        http_info = self._create_record_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_record_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/apps/{app_id}/record-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def delete_app(self, request):
        r"""删除应用

        调用此接口删除单个应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.DeleteAppResponse`
        """
        http_info = self._delete_app_http_info(request)
        return self._call_api(**http_info)

    def delete_app_invoker(self, request):
        http_info = self._delete_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_app_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def delete_record_rule(self, request):
        r"""删除录制规则

        调用此接口删除录制规则，对于正在使用的录制规则，不允许删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordRule
        :type request: :class:`huaweicloudsdkcloudrtc.v2.DeleteRecordRuleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.DeleteRecordRuleResponse`
        """
        http_info = self._delete_record_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_record_rule_invoker(self, request):
        http_info = self._delete_record_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_record_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/apps/{app_id}/record-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordRuleResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def list_apps(self, request):
        r"""查询应用列表

        调用此接口查询应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ListAppsResponse`
        """
        http_info = self._list_apps_http_info(request)
        return self._call_api(**http_info)

    def list_apps_invoker(self, request):
        http_info = self._list_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apps_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def list_record_rules(self, request):
        r"""查询录制规则列表

        调用此接口查询录制规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordRules
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ListRecordRulesRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ListRecordRulesResponse`
        """
        http_info = self._list_record_rules_http_info(request)
        return self._call_api(**http_info)

    def list_record_rules_invoker(self, request):
        http_info = self._list_record_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_record_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/apps/{app_id}/record-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordRulesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def remove_room(self, request):
        r"""解散房间

        调用此接口解散房间，将该房间中所有用户踢出房间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveRoom
        :type request: :class:`huaweicloudsdkcloudrtc.v2.RemoveRoomRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RemoveRoomResponse`
        """
        http_info = self._remove_room_http_info(request)
        return self._call_api(**http_info)

    def remove_room_invoker(self, request):
        http_info = self._remove_room_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_room_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/apps/{app_id}/rooms/{room_id}/dismiss",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveRoomResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def remove_users(self, request):
        r"""踢除在线用户

        调用此接口强制用户离开房间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveUsers
        :type request: :class:`huaweicloudsdkcloudrtc.v2.RemoveUsersRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RemoveUsersResponse`
        """
        http_info = self._remove_users_http_info(request)
        return self._call_api(**http_info)

    def remove_users_invoker(self, request):
        http_info = self._remove_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_users_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/apps/{app_id}/rooms/{room_id}/batch-remove-users",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveUsersResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def show_app(self, request):
        r"""查询单个应用

        调用此接口查询单个应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowAppResponse`
        """
        http_info = self._show_app_http_info(request)
        return self._call_api(**http_info)

    def show_app_invoker(self, request):
        http_info = self._show_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def show_auto_record(self, request):
        r"""查询自动录制配置

        调用此接口查询自动录制配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoRecord
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowAutoRecordRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowAutoRecordResponse`
        """
        http_info = self._show_auto_record_http_info(request)
        return self._call_api(**http_info)

    def show_auto_record_invoker(self, request):
        http_info = self._show_auto_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auto_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/apps/{app_id}/auto-record-mode",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoRecordResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def show_individual_stream_job(self, request):
        r"""查询单流任务状态

        调用此接口查询单流任务状态。
        
        租户的OBS桶内的情况，暂不支持查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIndividualStreamJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowIndividualStreamJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowIndividualStreamJobResponse`
        """
        http_info = self._show_individual_stream_job_http_info(request)
        return self._call_api(**http_info)

    def show_individual_stream_job_invoker(self, request):
        http_info = self._show_individual_stream_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_individual_stream_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/apps/{app_id}/individual-stream-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIndividualStreamJobResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def show_mix_job(self, request):
        r"""查询合流任务

        调用此接口查询合流转码任务状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMixJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowMixJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowMixJobResponse`
        """
        http_info = self._show_mix_job_http_info(request)
        return self._call_api(**http_info)

    def show_mix_job_invoker(self, request):
        http_info = self._show_mix_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mix_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/apps/{app_id}/mix-stream-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMixJobResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def show_record_callback(self, request):
        r"""查询增值（录制）事件回调配置

        调用此接口查询增值（录制）事件回调配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordCallback
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowRecordCallbackRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowRecordCallbackResponse`
        """
        http_info = self._show_record_callback_http_info(request)
        return self._call_api(**http_info)

    def show_record_callback_invoker(self, request):
        http_info = self._show_record_callback_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_record_callback_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/apps/{app_id}/record-callback",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordCallbackResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def show_record_rule(self, request):
        r"""查询录制规则

        调用此接口查询指定录制规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordRule
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ShowRecordRuleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ShowRecordRuleResponse`
        """
        http_info = self._show_record_rule_http_info(request)
        return self._call_api(**http_info)

    def show_record_rule_invoker(self, request):
        http_info = self._show_record_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_record_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/apps/{app_id}/record-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordRuleResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def start_app(self, request):
        r"""启用应用

        调用此接口启用单个应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.StartAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.StartAppResponse`
        """
        http_info = self._start_app_http_info(request)
        return self._call_api(**http_info)

    def start_app_invoker(self, request):
        http_info = self._start_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/apps/{app_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "StartAppResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def stop_app(self, request):
        r"""停用应用

        调用此接口停用单个应用。
        
        应用停用后，新房间无法新增和加入，已加入的房间可以继续使用。合流、录制功能等也不可用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopApp
        :type request: :class:`huaweicloudsdkcloudrtc.v2.StopAppRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.StopAppResponse`
        """
        http_info = self._stop_app_http_info(request)
        return self._call_api(**http_info)

    def stop_app_invoker(self, request):
        http_info = self._stop_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/apps/{app_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "StopAppResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def stop_individual_stream_job(self, request):
        r"""停止单流任务

        调用此接口停止单流任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopIndividualStreamJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.StopIndividualStreamJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.StopIndividualStreamJobResponse`
        """
        http_info = self._stop_individual_stream_job_http_info(request)
        return self._call_api(**http_info)

    def stop_individual_stream_job_invoker(self, request):
        http_info = self._stop_individual_stream_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_individual_stream_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/apps/{app_id}/individual-stream-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "StopIndividualStreamJobResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def stop_mix_job(self, request):
        r"""停止合流任务

        调用此接口停止已下发的合流转码任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopMixJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.StopMixJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.StopMixJobResponse`
        """
        http_info = self._stop_mix_job_http_info(request)
        return self._call_api(**http_info)

    def stop_mix_job_invoker(self, request):
        http_info = self._stop_mix_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_mix_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/apps/{app_id}/mix-stream-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "StopMixJobResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def update_auto_record(self, request):
        r"""更新自动录制配置

        更新自动录制配置，租户可以开启自动单流录制或者停用自动单流录制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutoRecord
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateAutoRecordRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateAutoRecordResponse`
        """
        http_info = self._update_auto_record_http_info(request)
        return self._call_api(**http_info)

    def update_auto_record_invoker(self, request):
        http_info = self._update_auto_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_auto_record_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/apps/{app_id}/auto-record-mode",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutoRecordResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def update_individual_stream_job(self, request):
        r"""更新单流任务

        调用此接口修改单流任务。
        
        仅部分场景支持修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIndividualStreamJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateIndividualStreamJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateIndividualStreamJobResponse`
        """
        http_info = self._update_individual_stream_job_http_info(request)
        return self._call_api(**http_info)

    def update_individual_stream_job_invoker(self, request):
        http_info = self._update_individual_stream_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_individual_stream_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/apps/{app_id}/individual-stream-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIndividualStreamJobResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def update_mix_job(self, request):
        r"""修改合流任务

        调用此接口更新合流任务布局。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMixJob
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateMixJobRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateMixJobResponse`
        """
        http_info = self._update_mix_job_http_info(request)
        return self._call_api(**http_info)

    def update_mix_job_invoker(self, request):
        http_info = self._update_mix_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_mix_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/apps/{app_id}/mix-stream-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMixJobResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def update_record_callback(self, request):
        r"""配置RTC增值（录制）事件回调

        调用此接口配置增值（录制）事件上报回调。
        
        当任务发生订阅了的事件时，通过该接口配置的回调地址通知。
        
        回调格式参考/customer-record-notify-url定义。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordCallback
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateRecordCallbackRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateRecordCallbackResponse`
        """
        http_info = self._update_record_callback_http_info(request)
        return self._call_api(**http_info)

    def update_record_callback_invoker(self, request):
        http_info = self._update_record_callback_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_record_callback_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/apps/{app_id}/record-callback",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordCallbackResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def update_record_rule(self, request):
        r"""更新录制规则

        调用此接口更新录制规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordRule
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateRecordRuleResponse`
        """
        http_info = self._update_record_rule_http_info(request)
        return self._call_api(**http_info)

    def update_record_rule_invoker(self, request):
        http_info = self._update_record_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_record_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/apps/{app_id}/record-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def list_obs_bucket_objects(self, request):
        r"""查询OBS桶下对象列表

        查询OBS桶下对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBucketObjects
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ListObsBucketObjectsRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ListObsBucketObjectsResponse`
        """
        http_info = self._list_obs_bucket_objects_http_info(request)
        return self._call_api(**http_info)

    def list_obs_bucket_objects_invoker(self, request):
        http_info = self._list_obs_bucket_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_obs_bucket_objects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rtc-ops/buckets/objects",
            "request_type": request.__class__.__name__,
            "response_type": "ListObsBucketObjectsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-Id", ]

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

    def list_obs_buckets(self, request):
        r"""查询OBS桶列表

        查询OBS桶列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBuckets
        :type request: :class:`huaweicloudsdkcloudrtc.v2.ListObsBucketsRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.ListObsBucketsResponse`
        """
        http_info = self._list_obs_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_obs_buckets_invoker(self, request):
        http_info = self._list_obs_buckets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_obs_buckets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rtc-ops/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListObsBucketsResponse"
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

        response_headers = ["X-request-Id", ]

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

    def update_obs_bucket_authority(self, request):
        r"""OBS桶授权及取消授权

        OBS桶授权及取消授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateObsBucketAuthority
        :type request: :class:`huaweicloudsdkcloudrtc.v2.UpdateObsBucketAuthorityRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateObsBucketAuthorityResponse`
        """
        http_info = self._update_obs_bucket_authority_http_info(request)
        return self._call_api(**http_info)

    def update_obs_bucket_authority_invoker(self, request):
        http_info = self._update_obs_bucket_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_obs_bucket_authority_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/rtc-ops/buckets/authentication",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateObsBucketAuthorityResponse"
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

        response_headers = ["X-request-Id", ]

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
