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


class CbsAsyncClient(Client):
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
        super(CbsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcbs.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CbsClient":
            raise TypeError("client type error, support client type is CbsClient")

        return ClientBuilder(clazz)

    def collect_hot_questions_async(self, request):
        """热点问题统计

        获取完全匹配的热点标准问题列表。
        默认按照完全匹配标准问题被问及的频次降序排序。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectHotQuestions
        :type request: :class:`huaweicloudsdkcbs.v1.CollectHotQuestionsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CollectHotQuestionsResponse`
        """
        return self.collect_hot_questions_with_http_info(request)

    def collect_hot_questions_with_http_info(self, request):
        all_params = ['qabot_id', 'start_time', 'end_time', 'top', 'domain', 'domain_id', 'exclude']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'exclude' in local_var_params:
            query_params.append(('exclude', local_var_params['exclude']))

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/qa-pairs/hots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectHotQuestionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_key_words_async(self, request):
        """关键词统计

        用户问关键词统计。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectKeyWords
        :type request: :class:`huaweicloudsdkcbs.v1.CollectKeyWordsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CollectKeyWordsResponse`
        """
        return self.collect_key_words_with_http_info(request)

    def collect_key_words_with_http_info(self, request):
        all_params = ['qabot_id', 'start_time', 'end_time', 'top']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/keywords',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectKeyWordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_reply_rates_async(self, request):
        """问答统计

        指定领域获取指定时间范围内的问题答复率，支持按周期统计。
        如果领域未指定则表示获取所有领域的问题答复率。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectReplyRates
        :type request: :class:`huaweicloudsdkcbs.v1.CollectReplyRatesRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CollectReplyRatesResponse`
        """
        return self.collect_reply_rates_with_http_info(request)

    def collect_reply_rates_with_http_info(self, request):
        all_params = ['qabot_id', 'start_time', 'end_time', 'interval', 'time_zone', 'domain']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'time_zone' in local_var_params:
            query_params.append(('time_zone', local_var_params['time_zone']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/reply-rates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectReplyRatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_session_stats_async(self, request):
        """访问统计

        获取用户会话统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectSessionStats
        :type request: :class:`huaweicloudsdkcbs.v1.CollectSessionStatsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CollectSessionStatsResponse`
        """
        return self.collect_session_stats_with_http_info(request)

    def collect_session_stats_with_http_info(self, request):
        all_params = ['qabot_id', 'start_time', 'end_time', 'interval', 'time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'time_zone' in local_var_params:
            query_params.append(('time_zone', local_var_params['time_zone']))

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/session-stats',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectSessionStatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_session_async(self, request):
        """开启会话

        问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口创建会话。该接口仅支持老用户，新用户请优先使用问答机器人API接口进行调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSession
        :type request: :class:`huaweicloudsdkcbs.v1.CreateSessionRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CreateSessionResponse`
        """
        return self.create_session_with_http_info(request)

    def create_session_with_http_info(self, request):
        all_params = ['qabot_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/sessions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_session_async(self, request):
        """关闭会话

        问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口关闭会话。该接口即将下线，请优先使用问答机器人API接口进行调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSession
        :type request: :class:`huaweicloudsdkcbs.v1.DeleteSessionRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.DeleteSessionResponse`
        """
        return self.delete_session_with_http_info(request)

    def delete_session_with_http_info(self, request):
        all_params = ['qabot_id', 'session_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/sessions/{session_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_qa_chat_async(self, request):
        """问答机器人会话

        用户调用该接口和机器人进行聊天。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteQaChat
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteQaChatRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteQaChatResponse`
        """
        return self.execute_qa_chat_with_http_info(request)

    def execute_qa_chat_with_http_info(self, request):
        all_params = ['qabot_id', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/chat',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteQaChatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_session_async(self, request):
        """处理会话

        问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口与机器人进行会话。该接口即将下线，请优先使用问答机器人API接口进行调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteSession
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteSessionRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteSessionResponse`
        """
        return self.execute_session_with_http_info(request)

    def execute_session_with_http_info(self, request):
        all_params = ['qabot_id', 'session_id', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/sessions/{session_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_suggestions_async(self, request):
        """获取问题提示

        获取用户输入问题的提示问题列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSuggestions
        :type request: :class:`huaweicloudsdkcbs.v1.ListSuggestionsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ListSuggestionsResponse`
        """
        return self.list_suggestions_with_http_info(request)

    def list_suggestions_with_http_info(self, request):
        all_params = ['qabot_id', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/suggestions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSuggestionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_labor_async(self, request):
        """标记为转人工

        智能问答返回的结果后，用户是否转人工。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for TagLabor
        :type request: :class:`huaweicloudsdkcbs.v1.TagLaborRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.TagLaborResponse`
        """
        return self.tag_labor_with_http_info(request)

    def tag_labor_with_http_info(self, request):
        all_params = ['qabot_id', 'request_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/{request_id}/labor',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagLaborResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_satisfaction_async(self, request):
        """问答满意评价

        用户提出问题后，对智能问答返回的结果是否满意。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for TagSatisfaction
        :type request: :class:`huaweicloudsdkcbs.v1.TagSatisfactionRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.TagSatisfactionResponse`
        """
        return self.tag_satisfaction_with_http_info(request)

    def tag_satisfaction_with_http_info(self, request):
        all_params = ['qabot_id', 'request_id', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']

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
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/{request_id}/satisfaction',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagSatisfactionResponse',
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
