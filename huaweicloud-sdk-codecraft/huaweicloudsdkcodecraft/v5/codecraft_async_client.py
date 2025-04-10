# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodecraft'")


class CodeCraftAsyncClient(Client):
    def __init__(self):
        super(CodeCraftAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodecraft.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeCraftAsyncClient":
                raise TypeError("client type error, support client type is CodeCraftAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_competition_score_async(self, request):
        r"""登记第三方提交的作品信息（得分回调）

        针对在第三方提交作品的场景：第三方服务对作品完成判分后，调用该接口将作品信息及作品得分返回给大赛平台
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCompetitionScore
        :type request: :class:`huaweicloudsdkcodecraft.v5.CreateCompetitionScoreRequest`
        :rtype: :class:`huaweicloudsdkcodecraft.v5.CreateCompetitionScoreResponse`
        """
        http_info = self._create_competition_score_http_info(request)
        return self._call_api(**http_info)

    def create_competition_score_async_invoker(self, request):
        http_info = self._create_competition_score_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_competition_score_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/competitions/score-infos",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCompetitionScoreResponse"
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

    def list_competition_works_async(self, request):
        r"""获取指定时间内选手提交的作品

        第三方服务获取某个大赛某个阶段中一段时间内提交的作品信息。其中以请求参数read_time作为结束时间，定义向前一天或一小时内的时间作为查询范围
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCompetitionWorks
        :type request: :class:`huaweicloudsdkcodecraft.v5.ListCompetitionWorksRequest`
        :rtype: :class:`huaweicloudsdkcodecraft.v5.ListCompetitionWorksResponse`
        """
        http_info = self._list_competition_works_http_info(request)
        return self._call_api(**http_info)

    def list_competition_works_async_invoker(self, request):
        http_info = self._list_competition_works_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_competition_works_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/competitions/works",
            "request_type": request.__class__.__name__,
            "response_type": "ListCompetitionWorksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'competition_id' in local_var_params:
            query_params.append(('competition_id', local_var_params['competition_id']))
        if 'stage_id' in local_var_params:
            query_params.append(('stage_id', local_var_params['stage_id']))
        if 'read_time' in local_var_params:
            query_params.append(('read_time', local_var_params['read_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def register_competition_info_async(self, request):
        r"""验证用户报名信息和团队信息

        第三方服务验证用户是否在大赛平台报名、是否组建团队、是否可以提交作品。如果已经报名但是未组建团队，则创建一个虚拟团队，设置为允许提交作品。如果已经组建团队则根据大赛报名截止时间判断是否可以提交作品。返回团队ID、是否可以提交作品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterCompetitionInfo
        :type request: :class:`huaweicloudsdkcodecraft.v5.RegisterCompetitionInfoRequest`
        :rtype: :class:`huaweicloudsdkcodecraft.v5.RegisterCompetitionInfoResponse`
        """
        http_info = self._register_competition_info_http_info(request)
        return self._call_api(**http_info)

    def register_competition_info_async_invoker(self, request):
        http_info = self._register_competition_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_competition_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/competitions/registrations",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterCompetitionInfoResponse"
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

    def update_competition_score_async(self, request):
        r"""修改平台提交的作品分数（得分回调）

        针对在大赛平台提交作品的场景：第三方服务对作品完成判分后，根据作品ID调用该接口将作品分数、作品状态等信息返回给大赛平台
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCompetitionScore
        :type request: :class:`huaweicloudsdkcodecraft.v5.UpdateCompetitionScoreRequest`
        :rtype: :class:`huaweicloudsdkcodecraft.v5.UpdateCompetitionScoreResponse`
        """
        http_info = self._update_competition_score_http_info(request)
        return self._call_api(**http_info)

    def update_competition_score_async_invoker(self, request):
        http_info = self._update_competition_score_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_competition_score_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/competitions/scores",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCompetitionScoreResponse"
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

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	        async_request=True)
