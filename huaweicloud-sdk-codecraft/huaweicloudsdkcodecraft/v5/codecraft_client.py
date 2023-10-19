# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CodeCraftClient(Client):
    def __init__(self):
        super(CodeCraftClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodecraft.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeCraftClient":
                raise TypeError("client type error, support client type is CodeCraftClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_competition_score(self, request):
        """登记第三方提交的作品信息（得分回调）

        针对在第三方提交作品的场景：第三方服务对作品完成判分后，调用该接口将作品信息及作品得分返回给大赛平台
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCompetitionScore
        :type request: :class:`huaweicloudsdkcodecraft.v5.CreateCompetitionScoreRequest`
        :rtype: :class:`huaweicloudsdkcodecraft.v5.CreateCompetitionScoreResponse`
        """
        return self._create_competition_score_with_http_info(request)

    def _create_competition_score_with_http_info(self, request):
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
            resource_path='/v5/competitions/score-infos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCompetitionScoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_competition_works(self, request):
        """获取指定时间内选手提交的作品

        第三方服务获取某个大赛某个阶段中一段时间内提交的作品信息。其中以请求参数read_time作为结束时间，定义向前一天或一小时内的时间作为查询范围
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCompetitionWorks
        :type request: :class:`huaweicloudsdkcodecraft.v5.ListCompetitionWorksRequest`
        :rtype: :class:`huaweicloudsdkcodecraft.v5.ListCompetitionWorksResponse`
        """
        return self._list_competition_works_with_http_info(request)

    def _list_competition_works_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/competitions/works',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCompetitionWorksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_competition_info(self, request):
        """验证用户报名信息和团队信息

        第三方服务验证用户是否在大赛平台报名、是否组建团队、是否可以提交作品。如果已经报名但是未组建团队，则创建一个虚拟团队，设置为允许提交作品。如果已经组建团队则根据大赛报名截止时间判断是否可以提交作品。返回团队ID、是否可以提交作品
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterCompetitionInfo
        :type request: :class:`huaweicloudsdkcodecraft.v5.RegisterCompetitionInfoRequest`
        :rtype: :class:`huaweicloudsdkcodecraft.v5.RegisterCompetitionInfoResponse`
        """
        return self._register_competition_info_with_http_info(request)

    def _register_competition_info_with_http_info(self, request):
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
            resource_path='/v5/competitions/registrations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterCompetitionInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_competition_score(self, request):
        """修改平台提交的作品分数（得分回调）

        针对在大赛平台提交作品的场景：第三方服务对作品完成判分后，根据作品ID调用该接口将作品分数、作品状态等信息返回给大赛平台
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCompetitionScore
        :type request: :class:`huaweicloudsdkcodecraft.v5.UpdateCompetitionScoreRequest`
        :rtype: :class:`huaweicloudsdkcodecraft.v5.UpdateCompetitionScoreResponse`
        """
        return self._update_competition_score_with_http_info(request)

    def _update_competition_score_with_http_info(self, request):
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
            resource_path='/v5/competitions/scores',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCompetitionScoreResponse',
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
